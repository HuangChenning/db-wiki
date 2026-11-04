---
title: "dmAsync 包"
book: "DM8 dmPython 使用手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dmasync-package.html
tags:
  - dameng
  - dm8
  - dmpython
---

## 7.1 简介及安装

dmAsync 是基于 python 的异步 DM 数据库驱动库，dmAsync 使用 asyncio 库实现 python 中的异步数据库操作，依赖于 dmPython 以及 async\_timeout 库。

dmAsync 可以运行在任何安装了 python 的平台上，可以使用在线安装，也可以直接用源码安装。

可以使用以下命令很方便地在 Windows 和 Linux 操作系统下编译并安装 dmAsync：

```
// 较高pip版本可以进入到setup.py所在的源码目录，使用以下命令安装:
pip install .
// 如报错可以执行以下命令安装：
python setup.py install
```

如果希望在线安装，可以直接使用以下命令：

```
pip install dmAsync
// 如需指定安装x.x.x版本请使用：
pip install dmAsync==x.x.x
```

## 7.2 使用

### 7.2.1 接口与常量

dmAsync 的接口以及常量与 dmPython 保持一致，具体请参照\[章节 3.1.1\](#3.1.1 接口)与\[章节 3.1.2\](#3.1.2 常量)。

### 7.2.2 Connection

dmAsync 的 Connection 与 dmPython 的类似，如果需要访问属性，可以直接通过 Connection 类中的\_conn 对象进行访问属性，名称与 dmPython 中的名称保持一致。

例如访问连接中的 server\_version：

```
import asyncio
import dmAsync

async def test_example():
  conn = await dmAsync.connect(host='localhost', port=5236, user='SYSDBA', password='Hust4400_DBA')
  print(conn._conn.server_version)
  conn.close()
asyncio.run(test_example())
```

接口的使用方法与基本方法类似，可以直接通过 Connection 的方法调用执行，在执行方法前添加 await 关键字即可。

例如创建游标：

```
import asyncio
import dmAsync

async def test_example():
  conn = await dmAsync.connect(host='localhost', port=5236, user='SYSDBA', password='Hust4400_DBA')
  cursor = await conn.cursor()
  await cursor.execute("create or replace function func1(c1 int, c2 int) return varchar as  t1 int;begin   t1=c1;   "
  "print t1;    return 'success';end;")
  result = await cursor.callfunc('FUNC1', 10, 10)
  print(result)
conn.close()
  
asyncio.run(test_example())
```

### 7.2.3 Cusor

dmAsync 的 Cursor 与 dmPython 的类似，如果需要访问属性，可以直接通过 Connection 类中的\_impl 对象进行访问属性，名称与 dmPython 中的名称保持一致。

例如访问连接中的 bindarraysize：

```
import asyncio
import dmAsync
 
async def test_example():
  conn = await dmAsync.connect(host='localhost', port=5236, user='SYSDBA', password='Hust4400_DBA')
  async with conn.cursor() as cur:
  print(cur._impl.bindarraysize)
conn.close()

asyncio.run(test_example())
```

接口的使用方法与基本方法类似，可以直接通过 Cursor 的方法调用执行，在执行方法前添加 await 关键字即可。

例如执行语句创建 procedure，之后调用 callproc 方法调用 procedure 并输出返回值：

```
import asyncio
import dmAsync

async def test_example():
  conn = await dmAsync.connect(host='localhost', port=5236, user='SYSDBA', password='Hust4400_DBA')
  async with conn.cursor() as cur:
  await cur.execute('drop procedure if exists myinc;')
  await cur.execute('create procedure myinc(p1 int) as begin select p1+1;end;')
  await cur.callproc('MYINC', [1])
  (ret, ) = await cur.fetchone()
  assert 2, ret
  print(ret)
conn.close()

asyncio.run(test_example())
```