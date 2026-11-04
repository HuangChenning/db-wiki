---
title: "dmPython_pool 包"
book: "DM8 dmPython 使用手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dmpython_pool-package.html
tags:
  - dameng
  - dm8
  - dmpython
---

## 8.1 简介及安装

### 8.1.1 简介

在高并发服务（如 Web API、任务队列、多线程采集等）中，频繁创建和释放数据库连接会带来显著的开销，并可能导致数据库侧会话数大幅波动、连接风暴、响应抖动等问题。为了解决上述可能的问题，连接池通过复用连接、控制并发连接数、提供等待/超时/背压机制，从而提升吞吐并增强稳定性。

dmPython\_pool 是一个“纯 Python、零额外依赖”的连接池实现，面向 dmPython（Python DB-API 2.0）连接对象：

- 推荐使用上下文管理器：with pool.connection() as conn:...。
- 默认返回“包装连接”（PooledConnection）：conn.close()表示归还连接到池，而不是关闭底层连接。
- 支持 min\_size/max\_size、等待超时 timeout、等待队列上限 max\_waiting、健康检查 check、连接回收策略等。
- 提供可观测性：stats()、dump\_in\_use()，支持连接持有超时告警（leak\_timeout）。

**适用场景：**

- 同步 dmPython 驱动 + 多线程/多进程工作负载（Gunicorn worker、线程池、定时任务等）。
- Web 服务请求高峰期需要平滑控制连接数，避免数据库侧连接耗尽。
- 希望快速定位连接泄漏、长事务占用、池耗尽等问题。

### 8.1.2 安装与依赖

dmPython\_pool 以普通 Python 包形式供用户使用。

dmPython\_pool 包需从源码安装，可以使用以下命令在 Windows 和 Linux 操作系统下安装 dmPython\_pool：

```
// 较高pip版本可以进入到setup.py所在的源码目录，使用以下命令安装:
pip install .
// 如报错可以执行以下命令安装：
python setup.py install
```

**依赖说明：**

1. 需保证系统环境中已正确安装 dmPython，并配置好了 DPI 运行环境（例如 DM\_HOME/LD\_LIBRARY\_PATH 等）。
2. dmPython\_pool 本身不包含任何 C 扩展，安装不依赖编译器。

## 8.2 快速开始

下面通过示例展示最常见的 dmPython\_pool 连接池初始化与使用方式。

> **注意**
> 
> 1）不要对“真实连接”对象使用with conn:语法。  
> 2）在dmPython中，Connection.\_\_exit\_\_的行为是关闭连接并回滚未提交事务（close+rollback）。因此应始终使用with pool.connection()获取连接，或使用包装连接的上下文管理器。

### 8.2.1 使用传参方式建立连接池

```
from dmPython_pool import ConnectionPool
pool = ConnectionPool(
    connect_kwargs={
        "user": "SYSDBA",
        "password": "Dmsys_123",
        "server": "127.0.0.1",
        "port": 5236,
        "autoCommit": True,
    },
    min_size=2,
    max_size=10,
    timeout=5,          # 等待连接的最大时间（秒）
    max_waiting=100,    # 等待队列最大长度，超过直接报错（背压）
    check="ping",       # 连接健康检查（none/dead/ping 或 callable）
)

with pool.connection() as conn:
    cur = conn.cursor()
    cur.execute("select 1")
    print(cur.fetchone())
    cur.close()

pool.close()
pool.wait(timeout=10)
```

### 8.2.2 使用连接串方式建立连接池

```
from dmPython_pool import ConnectionPool
pool = ConnectionPool(
    conninfo="SYSDBA/Dmsys_123@127.0.0.1:5236/sch1",
    min_size=1,
    max_size=5,
)
```

## 8.3 核心类及接口说明

dmPython\_pool 主要提供 ConnectionPool 类及包装连接 PooledConnection。

### 8.3.1 ConnectionPool

相对于 PooledConnection，ConnectionPool 为“真实连接”。

#### 8.3.1.1 参数

下表仅列出 ConnectionPool 的常用参数，实际使用中可能使用到的 dmPython.connect 的连接属性说明请参考\[3.2.2 属性\](#3.2.2 属性)。

表8.1 ConnectionPool的常用参数

| **参数** | **类型/取值** | **默认值** | **说明** |
| --- | --- | --- | --- |
| conninfo | str | None | 连接串（user/pwd@host:port/schema） |
| connect\_args | tuple | () | 通过位置参数方式传参给 dmPython.connect |
| connect\_kwargs | dict | {} | 通过关键字方式传参给 dmPython.connect（推荐使用） |
| creator | callable | dmPython.connect | 自定义连接创建函数，便于测试或兼容其他 DB-API 驱动 |
| min\_size | int | 1 | 连接池最小连接数（可预热） |
| max\_size | int | 10 | 连接池最大连接数（硬上限） |
| timeout | float | 30.0 | 池耗尽时等待连接的最大时间（秒） |
| max\_waiting | int 或 None | None | 等待队列上限；达到上限立即报错 PoolBusyError（背压） |
| max\_idle | float 或 None | 300.0 | 空闲连接最大存活时间（秒），超过将被回收 |
| max\_lifetime | float 或 None | 3600.0 | 连接最大生命周期（秒），超过将被回收 |
| check | callable 或取值"none"/"dead"/"ping" | "ping" | 进行借出时的健康检查；CallableStatement：接收 conn 返回 bool 类型结果 |
| ping\_reconnect | bool | False | check=ping 时是否允许 ping 失败后重连 |
| reset\_on\_return | bool | True | 归还连接时是否重置，默认为 rollback |
| reset | callable 或 None | None | 自定义归还重置逻辑，例如 rollback + set schema |
| configure | callable 或 None | None | 新建连接后一次性配置；例如：设置时区/模式/会话参数 |
| leak\_timeout | float 或 None | None | 连接持有超过该值时输出告警日志，用于排查泄漏/长事务 |
| capture\_stack | bool | False | 记录借出时堆栈（定位泄漏；建议仅调试开启） |
| wrap | bool | True | 是否返回 PooledConnection 包装器；False 则直接返回真实连接 |

#### 8.3.1.2 接口

##### 8.3.1.2.1 ConnectionPool.open

**功能描述**

预创建连接至 min\_size 设置个数；可选，构造时 open=True 会自动执行。

**语法格式**

```
ConnectionPool.open()
```

##### 8.3.1.2.2 ConnectionPool.close

**功能描述**

关闭连接池；立即关闭空闲连接，正在使用的连接在归还时关闭。

**语法格式**

```
ConnectionPool.close()
```

##### 8.3.1.2.3 ConnectionPool.wait

**功能描述**

等待所有 in\_use 的连接归还（用于优雅下线）。

**语法格式**

```
ConnectionPool.wait(timeout=None)
```

##### 8.3.1.2.4 ConnectionPool.onnection

**功能描述**

上下文管理器获取连接，退出时自动归还。推荐使用。

**语法格式**

```
ConnectionPool.onnection(timeout=None)
```

##### 8.3.1.2.5 ConnectionPool.raw\_connection

**功能描述**

获取真实 dmPython 连接，当少数框架需要严格类型时使用。

**语法格式**

```
ConnectionPool.raw_connection(timeout=None)
```

##### 8.3.1.2.6 ConnectionPool.getconn()、ConnectionPool.putconn()

**功能描述**

底层借还接口；一般不建议直接用，除非非常明确接口的生命周期。

**语法格式**

```
ConnectionPool.getconn()
ConnectionPool.putconn()
```

##### 8.3.1.2.7 ConnectionPool.get\_connection()

**功能描述**

兼容 mysql-connector 的命名，返回包装连接。

**语法格式**

```
ConnectionPool.get_connection()
```

##### 8.3.1.2.8 ConnectionPool.stats()

**功能描述**

返回连接池统计信息，包含总数/空闲/占用/等待/累计创建/超时等。

**语法格式**

```
ConnectionPool.stats()
```

##### 8.3.1.2.9 ConnectionPool.dump\_in\_use()

**功能描述**

返回当前占用连接清单（包含持有时长、线程、可选堆栈），用于排查泄漏。

**语法格式**

```
ConnectionPool.dump_in_use()
```

### 8.3.2 PooledConnection

PooledConnection 为包装连接。

默认情况下，连接池返回 PooledConnection，存在如下注意事项：

1. 调用 close()并不会关闭底层数据库连接，而是把连接归还到池中。
2. 在 with 语句结束时会自动归还，且保证幂等（即使用户提前 close()也不会二次归还）。
3. 归还后再次使用该对象会抛出异常，避免“归还后继续使用”的隐蔽问题。

## 8.4 进阶使用

### 8.4.1 设置 configure：连接创建后初始化会话参数

```
from dmPython_pool import ConnectionPool

def configure(conn):
    # 示例：设置当前会话schema（也可以执行 set schema ...）
    cur = conn.cursor()
    cur.execute("set schema USER_SCH")
    cur.close()

pool = ConnectionPool(
    connect_kwargs={"user": "SYSDBA", "password": "Dmsys_123", "server": "127.0.0.1", "port": 5236},
    configure=configure,
    min_size=2,
    max_size=10,
)
```

### 8.4.2 自定义 check：用轻量 SQL 验证连接可用性

```
from dmPython_pool import ConnectionPool

def check(conn) -> bool:
    try:
        cur = conn.cursor()
        cur.execute("select 1")
        cur.fetchone()
        cur.close()
        return True
    except Exception:
        return False

pool = ConnectionPool(
connect_kwargs={"user": "SYSDBA", "password": "Dmsys_123", "server": "127.0.0.1", "port": 5236},
    check=check,
    max_size=20,
)
```

### 8.4.3 泄漏排查：leak\_timeout + dump\_in\_use()

当出现池耗尽（timeout/busy）或响应变慢时，可开启 leak\_timeout，并在日志中输出占用情况：

```
import logging
from dmPython_pool import ConnectionPool
import time

logging.basicConfig(level=logging.INFO)

pool = ConnectionPool(
connect_kwargs={"user": "SYSDBA", "password": "Dmsys_123", "server": "127.0.0.1", "port": 5236},
    max_size=10,
    timeout=2,
    leak_timeout=3,       # 连接持有超过 3 秒，输出告警
    capture_stack=True,   # 需要定位借出位置时开启（有性能开销）
)

# 发生异常时输出当前占用连接信息
try:
    with pool.connection() as conn:
        time.sleep(4)
except Exception:
    logging.warning("pool stats=%s", pool.stats())
    logging.warning("in-use=%s", pool.dump_in_use())
    raise
```

## 8.5 Web 服务集成建议

以下建议适用于 Sanic/FastAPI/Flask 等服务端项目：

1. 池大小（max\_size）应结合数据库端最大会话数与应用实例数设置。建议先从 2×CPU 核数或 8~32 的量级起步，压测后再调整。
2. 尽量缩短“占用连接时间”：把连接获取放到最靠近 SQL 的位置，用完立即归还。不要把连接对象跨层传递、跨 await 传递。
3. 为池耗尽设置明确策略：timeout + max\_waiting。不要设置无限排队，否则会导致服务整体雪崩。
4. 在服务关闭（SIGTERM）时调用 pool.close()并调用 pool.wait()，可实现优雅下线，减少半途事务与异常。
5. 如果所用框架是异步的，但数据库驱动是同步的，建议把数据库操作放到线程池中执行，并确保每个线程用完连接及时归还。

## 8.6 常见问题与排障

**问题 1：**

PoolTimeoutError/PoolBusyError 频繁出现。

**原因：**

并发请求超过池的容量，或连接被长时间占用未归还（存在长事务/慢 SQL/泄漏）。

**建议：**

1）先使用 stats()/dump\_in\_use()查看是否有连接被长期占用；

2）开启 leak\_timeout 定位长期占用位置；

3）评估 max\_size 设置值，并结合数据库最大会话数进行调整；

4）优化慢 SQL 或缩短事务范围。

**问题 2：**

归还后连接不可用/报错。

**原因：**

连接在使用过程中断开或被服务器关闭。

**建议：**

1）启用 check='ping'或自定义 check；

2）设置 max\_lifetime，定期轮换连接；

3）必要时设置 ping\_reconnect=True（需要注意失败重连的语义）。

**问题 3：**

使用 with conn:导致连接被关闭，池里全是坏连接。

**原因：**

dmPython 的 Connection.\_\_exit\_\_会关闭连接并回滚未提交事务。

**建议：**

调整为仅使用 with pool.connection() as conn。若必须使用 with conn:，请使用包装连接（wrap 默认为 True）。

## 8.7 兼容 MySQLConnectionPool 风格的接口

由于在部分场景下（例如使用 mysql-connector）会调用 get\_connection()获取连接，dmPython\_pool 提供 get\_connection()作为别名，以降低改造成本：

```
# 兼容写法：cnxpool.get_connection()
conn = pool.get_connection()
try:
    cur = conn.cursor()
    ...
finally:
    conn.close()   # close=归还池
```