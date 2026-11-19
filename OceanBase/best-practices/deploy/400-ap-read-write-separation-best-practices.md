---
title: "OceanBase AP 场景下读写分离配置指南"
book: "安装部署"
version: master
source: "https://www.oceanbase.com/docs/common-best-practices-1000000003048509.html"
tags:
  - oceanbase
  - best-practices
  - deploy
---

# OceanBase AP 场景下读写分离配置指南

## 应用背景与目标

在 HTAP 场景中，既有 OLTP 类的在线联机交易场景，又有 OLAP 类的在线分析场景，两种类型的业务场景同时跑在一套数据库集群上，OLAP（联机分析处理）请求可能因高资源占用影响核心 OLTP（联机事务处理）的性能，因此我们一般会采用读写分离的方式，将一部分的读请求，路由到 Follower 副本上，从而降低复杂分析计算对资源的侵占，影响在线业务的响应延迟。

OceanBase 通过 **列存副本** 和 **ODP 路由策略** 实现以下目标：

- **OLTP 请求**：通过 Leader 副本保高性能及数据正确性。
- **AP 请求**：新建 **列存副本** 利用列存加速分析并隔离资源。

**版本要求**：列存副本需要 OceanBase V4.3.3 版本及以上 和 OCP V4.3.3 及以上。

## 配置方法

### 方法一：列存副本配置（AP 加速核心）

**解决的问题**：

- AP 请求需要高性能分析，但 OLTP Leader 副本资源有限。
- 行存副本无法同时满足 OLTP 低延迟与 AP 高吞吐需求。

OceanBase V4.3.3 版本及以上支持为 AP 请求创建 **列存副本**。

#### OceanBase 集群中部署列存副本并配置 ODP

| 场景特点             | 推荐方式           | 适用阶段   | 参考部署方式      |
|----------------------|--------------------|------------|-------------------|
| 新建分析型业务       | 创建含列存副本租户 | 系统初始化 | 下文中 **方式一** |
| 存量业务扩展分析能力 | 添加列存副本       | 业务扩展期 | 下文中 **方式二** |

**方式一：创建包含列存副本的新租户**

1.  配置资源单元与资源池，SQL 语句示例如下：

    ``` sql
    CREATE RESOURCE UNIT unit1, MAX_CPU=5, MIN_CPU=5, MEMORY_SIZE= '32G', MAX_IOPS=10000, MIN_IOPS=5000, LOG_DISK_SIZE=5301023539200;
    CREATE RESOURCE POOL pool1 UNIT='unit1', UNIT_NUM = 1, ZONE_LIST = ('zone1','zone2','zone3');
    ```

2.  创建租户指定 Locality，SQL 语句示例如下：

    ``` sql
    CREATE TENANT tenant_c LOCALITY = 'F@zone1,F@zone2,C@zone3', primary_zone='zone1;zone2,zone3', RESOURCE_POOL_LIST=('pool1') SET ob_tcp_invited_nodes = '%';
    ```

3.  部署并配置 ODP。

具体部署列存副本详细步骤可以参考官网文档 [使用列存副本](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002012841)。

**方式二：为已有租户增加列存副本**

1.  在集群中[添加新的 Zone](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002013108)，并向新的 Zone 内[增加节点](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002013119)。

2.  新增资源单元与资源池，SQL 语句示例如下：

    ``` sql
    CREATE RESOURCE UNIT unit2, MAX_CPU=5, MIN_CPU=5, MEMORY_SIZE= '32G', MAX_IOPS=10000, MIN_IOPS=5000, LOG_DISK_SIZE=5301023539200;
    CREATE RESOURCE POOL pool2 UNIT = 'unit2', UNIT_NUM = 1, ZONE_LIST = ('zone4');
    ALTER TENANT tenant_c RESOURCE_POOL_LIST = ('pool1','pool2');
    ```

3.  修改租户指定 Locality，SQL 语句示例如下：

    ``` sql
    ALTER TENANT tenant_c LOCALITY = 'F@zone1,F@zone2,F@zone3,C@zone4';
    ```

4.  部署并配置 ODP。

具体部署列存副本详细步骤可以参考官网文档 [使用列存副本](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002012841)。

#### 通过 OCP 设置列存只读副本

您也可以通过 OCP 白屏操作设置列存只读副本，这种方式更为便捷简单。

1.  添加只读列存副本：

    - **情况 1**：给现有集群添加 Zone：

      即在 OCP 集群管理中，进到对应的集群中，点击新增 Zone，填入新加的 Zone 信息，选择对应的机器，以及设置配置。

    - **情况 2**：给需要创建列存副本的租户添加副本。

      即完成 Zone 的添加之后，您需要进入到集群对应的租户里，然后给租户添加副本，添加对应的只读列存型副本即可。

2.  添加单独的 ODP：如果需要单独的 ODP，那么再创建一个 ODP 单独给 AP 请求使用。

3.  配置读写分离：列存副本添加完成之后，就可以设置读写分离策略，您可以参考 [ODP 路由最佳实践](../route/7800-odp_routing_best_practices.md)。

您也可以参见部署专用 ODP 及弱读请求详细步骤：[使用列存副本](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002012841)。

### 方法二：开启弱一致性读（AP 请求基础前提）

**解决的问题**：AP 请求需访问 Follower 副本，但默认路由策略为强一致性。

AP 请求需通过弱一致性读访问 Follower /列存副本，配置方法如下：

``` sql
-- 全局会话设置（推荐）  
SET GLOBAL OB_READ_CONSISTENCY='WEAK';  

-- 或通过 ODP 级配置：  
ALTER PROXYCONFIG SET OBPROXY_READ_CONSISTENCY=1;  -- 1 表示弱读  
```

### 方法三：大查询资源隔离配置

**解决的问题**：AP 大查询可能占用过多 CPU 资源，导致 OLTP 请求延迟。

OceanBase 数据库通过参数限制大查询资源占用，避免阻塞 OLTP，减少大查询对小查询的资源占用。通过参数限制 AP 查询资源占用，避免阻塞 OLTP，设置方法如下：

``` sql
ALTER SYSTEM SET LARGE_QUERY_THRESHOLD = '10s';     -- 超过 10 秒为大查询，默认为 5  
ALTER SYSTEM SET LARGE_QUERY_WORKER_PERCENTAGE = 25; -- 大查询仅占用 25% CPU资源，默认为 30
```

OceanBase 数据库通过限制大查询能使用的租户活跃工作线程数来约束大查询最多能够使用的 CPU 资源，以此来保证系统还会有足够的 CPU 资源来执行 OLTP（例如，交易型的小事务）负载。通过这样的方式来保证对响应时间比较敏感的 OLTP 负载能够得到足够多的 CPU 资源尽快地被执行。

另外需要注意的是，虽然 OceanBase 数据库可以做到大查询和 OLTP 资源的分配，large_query_threshold 参数也应设置在一个在合理的范围内，不应该设置成为一个过大的值。否则大查询很容易抢占系统的 CPU 资源进而引发 OLTP 响应过慢甚至队列堆积的问题。

## 典型配置案例

### 案例一：列存副本专用路由

**场景**：适用于电商大促后分析用户行为数据的场景。

**配置步骤**：

1.  **创建列存副本 Zone**（zone5）并绑定到分析请求专用 ODP。

2.  **设置路由策略**：

    ``` sql
    ALTER PROXYCONFIG SET PROXY_ROUTE_POLICY="follower_only";  
    ```

3.  **验证路由**：

    ``` sql
    EXPLAIN SELECT * FROM analysis_table WHERE region = 'east';  
    -- 确认计划中数据来源为 zone5 的列存副本  
    ```

**优势**：

- 列存加速聚合计算（如 `SUM`, `GROUP BY`）。
- 完全隔离 OLAP 与 OLTP 资源。

### 案例二：跨机房 AP 请求就近路由

**场景**：跨地域部署下，AP 请求就近访问列存副本。

**配置步骤**：

1.  **绑定 Zone 地理位置**：

    ``` sql
    ALTER SYSTEM MODIFY ZONE "zone5" SET REGION="SHANGHAI", IDC="idc5";  -- 列存副本所在机房  
    ```

2.  **设置路由偏好**：

    ``` sql
    ALTER PROXYCONFIG SET PROXY_ROUTE_POLICY="follower_first";  
    ```

**优势**：

- 上海机房的 AP 请求优先访问 zone5 的列存副本，避免跨城延迟。

## 附录一：关键配置参数说明

| **参数** | **作用** | **推荐值** |
|----|----|----|
| `OBPROXY_READ_CONSISTENCY` | 控制 ODP 默认读一致性级别（1 = 弱读） | 1 |
| `PROXY_ROUTE_POLICY` | 路由策略（`follower_only` 为 AP 场景推荐） | `follower_only` |
| `LARGE_QUERY_THRESHOLD` | 定义大查询阈值，超时后触发资源限制 | `10s`（根据业务响应调整） |
| `LARGE_QUERY_WORKER_PERCENTAGE` | 大查询占用 CPU 资源上限 | `25`~`30` |

## 附录二：ODP 路由策略与 LDC 基础

### 随机路由策略

OceanBase 的 ODP 代理支持三级路由策略，为了保证弱一致性的读请求能够优先路由到 Follower 副本上，还需要对 ODP 设置 `proxy_route_policy` 参数。

- 当设置为 FOLLOWER_FIRST 时，请求优先发送到 Follower 副本上，如果 Follower 不可用，则发送到 Leader 副本。

  ``` sql
  ALTER PROXYCONFIG SET PROXY_ROUTE_POLICY="follower_first";  
  ```

- 当设置为 FOLLOWER_ONLY 时，请求只会随机发送到 Follower 副本上，如果 Follower 不可用，则报错。

  ``` sql
  ALTER PROXYCONFIG SET PROXY_ROUTE_POLICY="follower_only";  
  ```

### LDC 配置（可选）

典型 AP 场景均是单独创建列存副本，无需考虑配置 LDC 路由。若集群内部配置读写分离，您可以参考本章节，了解按地理位置优化路由：

1.  **设置 Zone 地理位置**：

    ``` sql
    ALTER SYSTEM MODIFY ZONE "zone5" SET REGION="SHANGHAI", IDC="idc5";  
    ```

2.  **绑定 ODP 的 LDC 信息**：

    方法一：ODP 进程启动时通过 `-o` 参数指定设置 LDC 信息：

    ``` bash
    ./obproxy -o proxy_idc_name=idc5  
    ```

    方法二：通过执行 SQL 语句设置 LDC 信息：

    ```
    obclient> alter proxyconfig set proxy_idc_name='idc1';
    ```

## 相关文档

- 如需了解 OceanBase 的路由策略，并尝试部署与配置，您可以查看详细的官网文档：[OceanBase 数据库代理 ODP，OBProxy](https://www.oceanbase.com/docs/common-odp-doc-cn-1000000002839661)

- 如需了解 OceanBase 数据库代理（OceanBase Database Proxy，简称 ODP，又称 OBProxy）常用的路由功能及配置方式，在业务实践中正确配置路由策略及快速排查路由问题，您可以查看 [ODP 路由最佳实践](../route/7800-odp_routing_best_practices.md)
