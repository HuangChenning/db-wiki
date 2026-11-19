---
title: "查看租户和资源信息"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077272.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 查看租户和资源信息

本文介绍如何通过视图查看租户以及资源的相关信息。

## 租户的资源

数据库中的资源分为逻辑资源和物理资源两大类。逻辑资源指的是逻辑概念对应的实体，包括数据结构、线程、锁、会话等。物理资源指的是硬件资源，包括 CPU、磁盘、内存等。租户能够创建的逻辑资源量受物理资源的限制，一个逻辑资源可能受一个或者多个物理资源的限制。

### 逻辑资源

OceanBase 数据库中的逻辑资源及相关说明如下表所示。

[TABLE]

### 物理资源

OceanBase 数据库中的物理资源及相关说明如下表所示。

| 资源名称  | 描述                                                         |
|-----------|--------------------------------------------------------------|
| DATA_DISK | 数据盘，用于存储用户业务数据的磁盘，当前所有租户共用数据盘。 |
| CLOG_DISK | 日志盘，用于存储租户 clog 的磁盘。                           |
| CPU       | CPU，租户能够使用的计算资源。                                |
| MEMORY    | 内存，租户能够使用的总内存。                                 |
| MEMSTORE  | 业务数据内存，租户能够使用的业务数据内存。                   |

### 相关视图

OceanBase 数据库提供了租户和资源信息相关的视图，可以在系统租户 oceanbase 数据库中通过这些视图查询相关信息。

- `DBA_OB_UNIT_CONFIGS`：展示所有的资源规格信息，包括资源规格 ID、名称、资源配置等。
- `DBA_OB_RESOURCE_POOLS`：展示所有的资源池信息，包括资源池 ID、名称、绑定租户、Zone 列表等。
- `DBA_OB_TENANTS`：展示所有租户的配置信息，包括租户 ID、名称、类型、资源等。
- `GV$OB_UNITS`：展示节点的 Unit 信息，包括节点 IP、端口、资源规格 ID、租户 ID、资源配置等。
- `GV$OB_SERVERS`：展示节点的资源分配信息，包括节点 IP、端口、归属的 Zone、资源使用情况等。
- `GV$OB_TENANT_RESOURCE_LIMIT`：展示租户在每个 Unit 上的逻辑资源使用量、上限值、生效限制条件、宕机重启后的最大曾用量。
- `GV$OB_TENANT_RESOURCE_LIMIT_DETAIL`：展示租户逻辑资源所受的限制，以及每种限制的上限值。

## 查看所有资源规格信息

通过 `DBA_OB_UNIT_CONFIGS` 视图，可以查看所有资源规格信息。示例如下：

以查询结果第二行数据为例，资源规格（NAME）名称是 `test_unit`，资源规格 ID（UNIT_CONFIG_ID）是 1001，创建时间（CREATE_TIME）是 `2026-04-27 15:28:07.606777`，CPU 规格上限（MAX_CPU）是 3C，内存规格（MEMORY_SIZE）是 5G，日志盘空间（LOG_DISK_SIZE）是 20G。

```
obclient(root@sys)[oceanbase]> SELECT * FROM DBA_OB_UNIT_CONFIGS;
```

查询结果如下：

```
+----------------+-----------------+----------------------------+----------------------------+---------+---------+-------------+---------------+----------------+---------------------+---------------------+-------------+---------------------+----------------------+
| UNIT_CONFIG_ID | NAME            | CREATE_TIME                | MODIFY_TIME                | MAX_CPU | MIN_CPU | MEMORY_SIZE | LOG_DISK_SIZE | DATA_DISK_SIZE | MAX_IOPS            | MIN_IOPS            | IOPS_WEIGHT | MAX_NET_BANDWIDTH   | NET_BANDWIDTH_WEIGHT |
+----------------+-----------------+----------------------------+----------------------------+---------+---------+-------------+---------------+----------------+---------------------+---------------------+-------------+---------------------+----------------------+
|              1 | sys_unit_config | 2026-04-27 15:27:50.325926 | 2026-04-27 15:27:52.317894 |       2 |       2 |  1073741824 |    3221225472 |           NULL | 9223372036854775807 | 9223372036854775807 |           2 | 9223372036854775807 |                    2 |
|           1001 | test_unit       | 2026-04-27 15:28:07.606777 | 2026-04-27 15:28:07.606777 |       3 |       3 |  5368709120 |   21474836480 |           NULL | 9223372036854775807 | 9223372036854775807 |           3 | 9223372036854775807 |                    3 |
|           1002 | S1_unit_config  | 2026-04-27 15:30:52.380350 | 2026-04-27 15:30:52.380350 |       1 |       1 |  5368709120 |    6442450944 |           NULL |               10000 |               10000 |           1 | 9223372036854775807 |                    1 |
+----------------+-----------------+----------------------------+----------------------------+---------+---------+-------------+---------------+----------------+---------------------+---------------------+-------------+---------------------+----------------------+
3 rows in set
```

`DBA_OB_UNIT_CONFIGS` 视图参数详细说明，参见 [DBA_OB_UNIT_CONFIGS](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005284431)。

## 查看所有的资源池信息

通过 `DBA_OB_RESOURCE_POOLS` 视图，可以查看所有资源池信息。示例如下：

以查询结果第二行数据为例，资源池（NAME）名称是 `test_pool`，资源池的 ID（RESOURCE_POOL_ID）是 1001、归属于的租户 ID（TENANT_ID）是 1002、使用的资源规格 ID（UNIT_CONFIG_ID）是 1001，资源池的 Unit 个数（UNIT_COUNT）是 1，使用的 Zone 列表（ZONE_LIST）是 zone1。

```
obclient(root@sys)[oceanbase]> SELECT * FROM oceanbase.DBA_OB_RESOURCE_POOLS;
```

查询结果如下：

```
+------------------+------------+-----------+----------------------------+----------------------------+------------+----------------+-----------+--------------+
| RESOURCE_POOL_ID | NAME       | TENANT_ID | CREATE_TIME                | MODIFY_TIME                | UNIT_COUNT | UNIT_CONFIG_ID | ZONE_LIST | REPLICA_TYPE |
+------------------+------------+-----------+----------------------------+----------------------------+------------+----------------+-----------+--------------+
|                1 | sys_pool   |         1 | 2026-04-27 15:27:50.328370 | 2026-04-27 15:27:50.328370 |          1 |              1 | zone1     | FULL         |
|             1001 | test_pool  |      1002 | 2026-04-27 15:28:07.623621 | 2026-04-27 15:28:07.642679 |          1 |           1001 | zone1     | FULL         |
|             1002 | mq_pool_01 |      1004 | 2026-04-27 15:31:40.027348 | 2026-04-27 15:32:31.466142 |          1 |           1002 | zone1     | FULL         |
+------------------+------------+-----------+----------------------------+----------------------------+------------+----------------+-----------+--------------+
3 rows in set
```

`DBA_OB_RESOURCE_POOLS` 视图参数详细说明，参见 [DBA_OB_RESOURCE_POOLS](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005284630)。

## 查看所有租户信息

通过 `DBA_OB_TENANTS` 视图，可以查看所有的租户信息，示例如下：

以查询结果的第三行数据为例，租户名称（`TENANT_NAME`）是 test，租户 ID（`TENANT_ID`）是 1002，租户类型（TENANT_TYPE）是用户租户，租户创建时间是（CREATE_TIME）是 `2026-04-27 15:28:07.640565`，租户的 PRIMARY_ZONE（`PRIMARY_ZONE`）是 `RANDOM`，租户副本分布（LOCALITY）在 zone1，兼容模式（COMPATIBILITY_MODE）是 MySQL。

```
obclient(root@sys)[oceanbase]> SELECT TENANT_ID, TENANT_NAME, TENANT_TYPE, CREATE_TIME, PRIMARY_ZONE, LOCALITY, COMPATIBILITY_MODE, STATUS FROM oceanbase.DBA_OB_TENANTS;
```

查询结果如下：

```
+-----------+-------------+-------------+----------------------------+--------------+---------------+--------------------+--------+
| TENANT_ID | TENANT_NAME | TENANT_TYPE | CREATE_TIME                | PRIMARY_ZONE | LOCALITY      | COMPATIBILITY_MODE | STATUS |
+-----------+-------------+-------------+----------------------------+--------------+---------------+--------------------+--------+
|         1 | sys         | SYS         | 2026-04-27 15:27:50.340622 | RANDOM       | FULL{1}@zone1 | MYSQL              | NORMAL |
|      1001 | META$1002   | META        | 2026-04-27 15:28:07.637913 | RANDOM       | FULL{1}@zone1 | MYSQL              | NORMAL |
|      1002 | test        | USER        | 2026-04-27 15:28:07.640565 | RANDOM       | FULL{1}@zone1 | MYSQL              | NORMAL |
|      1003 | META$1004   | META        | 2026-04-27 15:32:31.464025 | zone1        | FULL{1}@zone1 | MYSQL              | NORMAL |
|      1004 | mq_t1       | USER        | 2026-04-27 15:32:31.464025 | zone1        | FULL{1}@zone1 | MYSQL              | NORMAL |
+-----------+-------------+-------------+----------------------------+--------------+---------------+--------------------+--------+
5 rows in set
```

`DBA_OB_TENANTS` 视图参数详细说明，参见 [DBA_OB_TENANTS](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005284400)。

## 查看租户资源配置

通过如下语句，在多个视图中查找租户资源配置信息。

以查询结果中 test 租户为例，`pool:conf` 列可以看到该租户的资源池名称和所用的资源规格名称，`unit_info` 列可以看到资源池的 Unit 个数为 1 和相应的 CPU 配置为 3C、内存配置都是 5G。

```
obclient(root@sys)[oceanbase]>SELECT c.TENANT_ID, e.TENANT_NAME, concat(c.NAME, ': ', d.NAME) `pool:conf`,concat(c.UNIT_COUNT, ' unit: ', d.min_cpu, 'C/', ROUND(d.MEMORY_SIZE/1024/1024/1024,0), "G") unit_info
                FROM DBA_OB_RESOURCE_POOLS c, DBA_OB_UNIT_CONFIGS d, DBA_OB_TENANTS e
                WHERE c.UNIT_CONFIG_ID=d.UNIT_CONFIG_ID AND c.TENANT_ID=e.TENANT_ID AND c.TENANT_ID>1000
                ORDER BY c.TENANT_ID;
```

返回结果如下：

```
+-----------+-------------+----------------------------+---------------+
| TENANT_ID | TENANT_NAME | pool:conf                  | unit_info     |
+-----------+-------------+----------------------------+---------------+
|      1002 | test        | test_pool: test_unit       | 1 unit: 3C/5G |
|      1004 | mq_t1       | mq_pool_01: S1_unit_config | 1 unit: 1C/5G |
+-----------+-------------+----------------------------+---------------+
2 rows in set
```

## 查看租户的资源单元部署位置

通过以下语句，查看当前已创建租户资源单元所在设备 IP 信息。

在查询结果中可以看到每个租户对应的 ID 和资源所在节点的 IP。

```
obclient(root@sys)[oceanbase]> SELECT a.TENANT_NAME,a.TENANT_ID,b.SVR_IP FROM DBA_OB_TENANTS a,GV$OB_UNITS b WHERE a.TENANT_ID=b.TENANT_ID;
```

查询结果如下：

```
+-------------+-----------+-----------------+
| TENANT_NAME | TENANT_ID | SVR_IP          |
+-------------+-----------+-----------------+
| sys         |         1 | xxx.xxx.xxx.135 |
| META$1002   |      1001 | xxx.xxx.xxx.135 |
| test        |      1002 | xxx.xxx.xxx.135 |
| META$1004   |      1003 | xxx.xxx.xxx.135 |
| mq_t1       |      1004 | xxx.xxx.xxx.135 |
+-------------+-----------+-----------------+
5 rows in set
```

## 查看节点的 Unit 信息

通过 `GV$OB_UNITS` 视图，可以查看所有节点的 Unit 信息，示例如下：

- 以查询结果第三行为例，节点 IP（SVR_IP）是 `xxx.xxx.xxx.135`，服务器端口号（SVR_PORT）是 28821，unit ID（UNIT_ID）是 1001，租户 ID（TENANT_ID）是 1002，对应的 Zone 名称（ZONE）是 zone1，CPU 规格上限（MAX_CPU）是 3C，内存大小（MEMORY_SIZE）是 5G，日志盘大小（LOG_DISK_SIZE）是 18G，日志盘已使用（LOG_DISK_IN_USE）0.1924G，数据盘使用（DATA_DISK_IN_USE）12.97M，unit 状态（STATUS）正常。
- 结合 SVR_IP 都为 xxx.xxx.xxx.135 的五行一起看，表示该节点有 5 个 unit，分别属于 TENANT_ID 为 1、1001、1002、1003、1004 的租户。

```
obclient(root@sys)[oceanbase]> SELECT * FROM GV$OB_UNITS;
```

查询结果如下：

```
+-----------------+----------+---------+-----------+-------+-----------+---------------+---------+---------+-------------+---------------------+---------------------+-------------+---------------------+----------------------+---------------+-----------------+----------------+------------------+--------+----------------------------+--------------+
| SVR_IP          | SVR_PORT | UNIT_ID | TENANT_ID | ZONE  | ZONE_TYPE | REGION        | MAX_CPU | MIN_CPU | MEMORY_SIZE | MAX_IOPS            | MIN_IOPS            | IOPS_WEIGHT | MAX_NET_BANDWIDTH   | NET_BANDWIDTH_WEIGHT | LOG_DISK_SIZE | LOG_DISK_IN_USE | DATA_DISK_SIZE | DATA_DISK_IN_USE | STATUS | CREATE_TIME                | REPLICA_TYPE |
+-----------------+----------+---------+-----------+-------+-----------+---------------+---------+---------+-------------+---------------------+---------------------+-------------+---------------------+----------------------+---------------+-----------------+----------------+------------------+--------+----------------------------+--------------+
| xxx.xxx.xxx.135 |    28821 |       1 |         1 | zone1 | ReadWrite | deault_region |       2 |       2 |  1073741824 | 9223372036854775807 | 9223372036854775807 |           2 | 9223372036854775807 |                    2 |    3221225472 |       198536805 |           NULL |         20660224 | NORMAL | 2026-04-27 15:27:48.906316 | FULL         |
| xxx.xxx.xxx.135 |    28821 |    1001 |      1001 | zone1 | ReadWrite | deault_region |    NULL |    NULL |  1073741824 |                NULL |                NULL |        NULL |                NULL |                 NULL |    2147483648 |        93942106 |           NULL |         18595840 | NORMAL | 2026-04-27 15:28:07.643767 | FULL         |
| xxx.xxx.xxx.135 |    28821 |    1001 |      1002 | zone1 | ReadWrite | deault_region |       3 |       3 |  4294967296 | 9223372036854775807 | 9223372036854775807 |           3 | 9223372036854775807 |                    3 |   19327352832 |       206601388 |           NULL |         13598720 | NORMAL | 2026-04-27 15:28:07.643767 | FULL         |
| xxx.xxx.xxx.135 |    28821 |    1002 |      1003 | zone1 | ReadWrite | deault_region |    NULL |    NULL |  1073741824 |                NULL |                NULL |        NULL |                NULL |                 NULL |     644245094 |        92082001 |           NULL |         18595840 | NORMAL | 2026-04-27 15:32:31.467439 | FULL         |
| xxx.xxx.xxx.135 |    28821 |    1002 |      1004 | zone1 | ReadWrite | deault_region |       1 |       1 |  4294967296 |               10000 |               10000 |           1 | 9223372036854775807 |                    1 |    5798205850 |       178703715 |           NULL |         13598720 | NORMAL | 2026-04-27 15:32:31.467439 | FULL         |
+-----------------+----------+---------+-----------+-------+-----------+---------------+---------+---------+-------------+---------------------+---------------------+-------------+---------------------+----------------------+---------------+-----------------+----------------+------------------+--------+----------------------------+--------------+
5 rows in set
```

`GV$OB_UNITS` 视图参数详细说明，参见 [GV\$OB_UNITS](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005284981)。

## 查看节点的资源分配信息

通过 `GV$OB_SERVERS` 视图，可以查看 OBServer 的信息，示例如下：

以查询结果的第一行数据为例，节点 IP（SVR_IP）是 `xxx.xxx.xxx.135`，服务器端口号（SVR_PORT）是 28821，对应的 zone 名称（zone）是 zone1，SQL 端口（SQL_PORT）是 28811，observer 进程可用的 CPU 数量（CPU_CAPACITY）是 8C，observer 进程可用的内存（MEM_CAPACITY）是 14G，已分配的内存（MEM_ASSIGNED）是 11G，日志盘总空间（LOG_DISK_CAPACITY）为 48G，已分配日志盘空间（LOG_DISK_ASSIGNED）是 29G，日志盘已使用（LOG_DISK_IN_USE） 1.0625G，数据盘空间（DATA_DISK_CAPACITY） 200G，数据盘已使用（DATA_DISK_IN_USE） 98M。

```
obclient(root@sys)[oceanbase]> SELECT * FROM GV$OB_SERVERS;
```

查询结果如下：

```
+-----------------+----------+-------+----------+--------------+------------------+--------------+------------------+--------------+--------------+-------------------+-------------------+-----------------+--------------------+--------------------+------------------+-------------------------+--------------+---------------------+-------------------------+-----------------------+----------------------------------+-----------------------------+
| SVR_IP          | SVR_PORT | ZONE  | SQL_PORT | CPU_CAPACITY | CPU_CAPACITY_MAX | CPU_ASSIGNED | CPU_ASSIGNED_MAX | MEM_CAPACITY | MEM_ASSIGNED | LOG_DISK_CAPACITY | LOG_DISK_ASSIGNED | LOG_DISK_IN_USE | DATA_DISK_CAPACITY | DATA_DISK_ASSIGNED | DATA_DISK_IN_USE | DATA_DISK_HEALTH_STATUS | MEMORY_LIMIT | DATA_DISK_ALLOCATED | DATA_DISK_ABNORMAL_TIME | SSL_CERT_EXPIRED_TIME | SS_DATA_DISK_OPERATION_SUGGESTED | SS_DATA_DISK_SIZE_SUGGESTED |
+-----------------+----------+-------+----------+--------------+------------------+--------------+------------------+--------------+--------------+-------------------+-------------------+-----------------+--------------------+--------------------+------------------+-------------------------+--------------+---------------------+-------------------------+-----------------------+----------------------------------+-----------------------------+
| xxx.xxx.xxx.135 |    28821 | zone1 |    28811 |            8 |                8 |            6 |                6 |  15032385536 |  11811160064 |       51539607552 |       31138512896 |      1140850688 |       214748364800 |               NULL |        102760448 | NORMAL                  |  21474836480 |          2147483648 | NULL                    | NULL                  | NULL                             |                        NULL |
+-----------------+----------+-------+----------+--------------+------------------+--------------+------------------+--------------+--------------+-------------------+-------------------+-----------------+--------------------+--------------------+------------------+-------------------------+--------------+---------------------+-------------------------+-----------------------+----------------------------------+-----------------------------+
1 row in set
```

`GV$OB_SERVERS` 视图参数详细说明，参见 [GV\$OB_SERVERS](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005284839)。

## 查看租户各资源组的实时 IO 统计信息

sys 租户通过 `GV$OB_GROUP_IO_STAT` 视图，可以实时查看 OBServer 节点上每个资源组的实时 IOPS 和带宽统计信息，示例如下：

```
obclient(root@sys)[oceanbase]> SELECT * FROM oceanbase.GV$OB_GROUP_IO_STAT WHERE TENANT_ID=1002 LIMIT 5;
```

查询结果如下：

```
+-----------+-----------------+----------+----------+----------------+-------+---------------------+---------------------+-----------+-----------+---------------------+---------------------------+--------------------+----------------------------+
| TENANT_ID | SVR_IP          | SVR_PORT | GROUP_ID | GROUP_NAME     | MODE  | MIN_IOPS            | MAX_IOPS            | NORM_IOPS | REAL_IOPS | MAX_NET_BANDWIDTH   | MAX_NET_BANDWIDTH_DISPLAY | REAL_NET_BANDWIDTH | REAL_NET_BANDWIDTH_DISPLAY |
+-----------+-----------------+----------+----------+----------------+-------+---------------------+---------------------+-----------+-----------+---------------------+---------------------------+--------------------+----------------------------+
|      1002 | xxx.xxx.xxx.135 |    28821 |        0 | OTHER_GROUP    | READ  | 9223372036854775807 | 9223372036854775807 |         0 |         0 | 9223372036854775807 | unlimited                 |                  0 | 0B/s                       |
|      1002 | xxx.xxx.xxx.135 |    28821 |        0 | OTHER_GROUP    | WRITE | 9223372036854775807 | 9223372036854775807 |         0 |         0 | 9223372036854775807 | unlimited                 |                  0 | 0B/s                       |
|      1002 | xxx.xxx.xxx.135 |    28821 |        1 | SLOG_IO        | READ  |                   0 | 9223372036854775807 |         0 |         0 | 9223372036854775807 | unlimited                 |                  0 | 0B/s                       |
|      1002 | xxx.xxx.xxx.135 |    28821 |        1 | SLOG_IO        | WRITE |                   0 | 9223372036854775807 |         1 |         5 | 9223372036854775807 | unlimited                 |                  0 | 0B/s                       |
|      1002 | xxx.xxx.xxx.135 |    28821 |        2 | CALIBRATION_IO | READ  |                   0 | 9223372036854775807 |         0 |         0 | 9223372036854775807 | unlimited                 |                  0 | 0B/s                       |
+-----------+-----------------+----------+----------+----------------+-------+---------------------+---------------------+-----------+-----------+---------------------+---------------------------+--------------------+----------------------------+
5 rows in set
```

查询结果中，`OTHER_GROUP` 为系统内置的资源组，`SLOG_IO` 和 `CALIBRATION_IO` 为自定义资源组。在配置资源管理计划内容时，如果未绑定资源组，则默认使用系统内置的资源组 `OTHER_GROUP`。

从第三行结果可知，租户 `1002` 在 `xxx.xxx.xxx.135` 节点上，资源组 `interactive_group` 中读操作的最小 IOPS 为 0， 最大 IOPS 为 `9223372036854775807`，当前实际的 IOPS 为 0，配置的最大网络带宽为 unlimited（无限），当前网络带宽为 0B/s。

## 查看租户 Function 级后台任务的实时 IO 统计信息

sys 租户通过 `GV$OB_FUNCTION_IO_STAT` 视图，可以实时查看所有 OBServer 节点上 Function 级别的 IO 统计信息，示例如下：

```
obclient(root@sys)[oceanbase]> SELECT * FROM oceanbase.GV$OB_FUNCTION_IO_STAT WHERE TENANT_ID=1002 LIMIT 5;
```

查询结果如下：

```
+-----------------+----------+-----------+------------------+--------------+------+-----------+-----------+-------------+-------------+----------+
| SVR_IP          | SVR_PORT | TENANT_ID | FUNCTION_NAME    | MODE         | SIZE | REAL_IOPS | REAL_MBPS | SCHEDULE_US | IO_DELAY_US | TOTAL_US |
+-----------------+----------+-----------+------------------+--------------+------+-----------+-----------+-------------+-------------+----------+
| xxx.xxx.xxx.135 |     2882 |      1002 | DEFAULT_FUNCTION | LOCAL READ   |    0 |         0 |         0 |           0 |           0 |        0 |
| xxx.xxx.xxx.135 |     2882 |      1002 | DEFAULT_FUNCTION | LOCAL WRITE  | 4096 |         2 |         0 |          20 |         142 |      178 |
| xxx.xxx.xxx.135 |     2882 |      1002 | DEFAULT_FUNCTION | REMOTE READ  |    0 |         0 |         0 |          20 |         142 |      178 |
| xxx.xxx.xxx.135 |     2882 |      1002 | DEFAULT_FUNCTION | REMOTE WRITE |    0 |         0 |         0 |          20 |         142 |      178 |
| xxx.xxx.xxx.135 |     2882 |      1002 | COMPACTION_HIGH  | LOCAL READ   |    0 |         0 |         0 |          20 |         142 |      178 |
+-----------------+----------+-----------+------------------+--------------+------+-----------+-----------+-------------+-------------+----------+
5 rows in set
```

查询结果中，`COMPACTION_HIGH` 为定义的 Mini Merge 和 DDL KV Merge 等任务，`DEFAULT_FUNCTION` 为除了已定义的后台任务以外的其他所有后台任务。

从第五行结果可知，租户 `1002` 在 `xxx.xxx.xxx.135` 节点上，Mini Merge 和 DDL KV Merge 等任务（`COMPACTION_HIGH`）本地读的平均 IO（`SIZE`）大小为 0，实际 IOPS（`REAL_IOPS`） 为 0， 实际所使用的带宽（`REAL_MBPS`）为 0 MB/S，IO 调度的平均消耗时间（`SCHEDULE_US`）为 20 us，磁盘 IO 的平均执行时间（`IO_DELAY_US`）为 142 us，IO 的总体平均执行时间（`TOTAL_US`）为 178 us。

## 查看租户的逻辑资源使用情况及限制

sys 租户通过 `GV$OB_TENANT_RESOURCE_LIMIT` 视图，可以查看租户在每个 Unit 上逻辑资源的使用情况，示例如下：

```
obclient(root@sys)[oceanbase]> SELECT * FROM oceanbase.GV$OB_TENANT_RESOURCE_LIMIT WHERE TENANT_ID=1004;
```

查询结果如下：

```
+-----------------+----------+-----------+-------+---------------+---------------------+-----------------+----------------+-------------+----------------------+
| SVR_IP          | SVR_PORT | TENANT_ID | ZONE  | RESOURCE_NAME | CURRENT_UTILIZATION | MAX_UTILIZATION | RESERVED_VALUE | LIMIT_VALUE | EFFECTIVE_LIMIT_TYPE |
+-----------------+----------+-----------+-------+---------------+---------------------+-----------------+----------------+-------------+----------------------+
| xxx.xxx.xxx.135 |    28821 |      1004 | zone1 | ls            |                   2 |               2 |              0 |           8 | memory               |
| xxx.xxx.xxx.135 |    28821 |      1004 | zone1 | tablet        |                 832 |             832 |              0 |       80000 | configuration        |
+-----------------+----------+-----------+-------+---------------+---------------------+-----------------+----------------+-------------+----------------------+
2 rows in set
```

从第一行结果可知，租户 1004 在 `xxx.xxx.xxx.135` 节点上，当前有 2 个日志流（`CURRENT_UTILIZATION`），曾经同时存在过最多 2 个日志流（`MAX_UTILIZATION`），最大可以创建 8 个日志流（`LIMIT_VALUE`），并且这 8 个日志流的上限值由租户内存（`memory`）计算得来。

从第二行结果可知，租户 1004 在 `xxx.xxx.xxx.135` 节点上，当前有 832 个 TABLET（`CURRENT_UTILIZATION`），曾经同时存在过最多 832 个 TABLET（`MAX_UTILIZATION`），最大可以创建 80000 个 TABLET（`LIMIT_VALUE`），并且这 80000 个 TABLET 的上限值是根据租户内存（`configuration`）计算得来。

由于租户在每个节点上能创建的逻辑资源会受到各种物理资源或配置项值的限制，可以通过视图 `GV$OB_TENANT_RESOURCE_LIMIT_DETAIL` 进一步查看租户逻辑资源具体所受的限制及各种限制的上限值。

```
obclient(root@sys)[oceanbase]> SELECT * FROM oceanbase.GV$OB_TENANT_RESOURCE_LIMIT_DETAIL WHERE TENANT_ID=1004;
```

查询结果如下：

```
+-----------------+----------+-----------+---------------+---------------+---------------------+
| SVR_IP          | SVR_PORT | TENANT_ID | RESOURCE_NAME | LIMIT_TYPE    | LIMIT_VALUE         |
+-----------------+----------+-----------+---------------+---------------+---------------------+
| xxx.xxx.xxx.135 |    28821 |      1004 | ls            | configuration |                  90 |
| xxx.xxx.xxx.135 |    28821 |      1004 | ls            | memstore      | 9223372036854775807 |
| xxx.xxx.xxx.135 |    28821 |      1004 | ls            | memory        |                   8 |
| xxx.xxx.xxx.135 |    28821 |      1004 | ls            | data_disk     | 9223372036854775807 |
| xxx.xxx.xxx.135 |    28821 |      1004 | ls            | clog_disk     |                  10 |
| xxx.xxx.xxx.135 |    28821 |      1004 | ls            | cpu           | 9223372036854775807 |
| xxx.xxx.xxx.135 |    28821 |      1004 | tablet        | configuration |               80000 |
| xxx.xxx.xxx.135 |    28821 |      1004 | tablet        | memstore      | 9223372036854775807 |
| xxx.xxx.xxx.135 |    28821 |      1004 | tablet        | memory        |               81920 |
| xxx.xxx.xxx.135 |    28821 |      1004 | tablet        | data_disk     | 9223372036854775807 |
| xxx.xxx.xxx.135 |    28821 |      1004 | tablet        | clog_disk     | 9223372036854775807 |
| xxx.xxx.xxx.135 |    28821 |      1004 | tablet        | cpu           | 9223372036854775807 |
+-----------------+----------+-----------+---------------+---------------+---------------------+
12 rows in set
```

从查询结果可知，租户 1004 在 `xxx.xxx.xxx.135` 节点上，限制创建的日志流个数的因素如下（`9223372036854775807` 表示无限制）：

- 配置项（`configuration`）限制创建的个数为 90。

- 租户内存（`memory`）限制创建的个数为 8。

- 日志盘（`clog_disk`）限制创建的个数为 10。
