---
title: "自动分区推荐配置"
book: "数据库对象管理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006078122.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 自动分区推荐配置

本文将介绍 OceanBase 数据库自动分区功能的推荐配置参数及版本要求，包括 OceanBase 数据库及KV 客户端的配置建议。

## OceanBase 数据库配置

### 版本建议

推荐使用 OceanBase 数据库 V4.4.0 及之后版本。

### 分裂相关参数

| 参数名 | 建议值 | 建议值说明 |
|----|----|----|
| [enable_auto_split](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005285820) | True | 启用自动分区分裂功能。 |
| [auto_split_tablet_size](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005285732) | 16GB | 设置触发自动分区的阈值，避免表级分区数太多超过允许的上限。 |

### 负载均衡参数

在自动分区后，建议调整以下参数以加速 OceanBase 集群的负载均衡（分区均衡）：

| 参数名 | 建议值 | 建议值说明 |
|----|----|----|
| [partition_balance_schedule_interval](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005285755) | 600s | 缩短分区均衡调度间隔，提升新分区的资源利用率，即让分区均衡更快调度。 |

## KV 客户端配置

### KV 版本建议

- 如果使用 OBKV，推荐使用 V1.4.0 及之后版本。
- 如果使用 OBHBase V1.x，推荐使用 V1.1.0 及之后版本。
- 如果使用 OBHBase V2.x，推荐使用 V2.1.0 及之后版本。

### KV 参数建议

建议调整以下参数，避免因自动分裂带来的性能抖动或报错。

| 参数名 | 建议值 | 建议值说明 |
|----|----|----|
| table.entry.refresh.interval.wait | True | 避免多线程同时刷新，同时等待正在刷新的线程完成，避免读到旧路由，客户端默认打开。 |
| server.enable.rerouting | False | 客户端实现原因，与单分片刷新特性互斥，客户端默认关闭。 |
| runtime.retry.times | 100 | 遇到可重试错误的重试次数。 |
| runtime.max.wait | 3000ms | 重试超时时间，与重试次数满足其中一个就会报错。 |
| runtime.retry.interval | 1ms | 重试等待间隔。 |
