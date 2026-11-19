---
title: "创建租户"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577615.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 创建租户

#### 说明

基于 OceanBase 数据库 3.x 版本的大量实践经验，OceanBase 数据库 V4.0 的资源管理功能有很大改进：

- 支持 Unit 级别管理 CPU、内存、日志盘空间、IOPS 等资源项，不支持 Unit 级别管理数据盘空间和 Session 个数等资源项。为了兼容 3.x 版本的运维工具和测试用例，`CREATE RESOURCE UNIT` 语句依然可以指定 `MAX_DISK_SIZE` 和 `MAX_SESSION_NUM`，但是不会生效，也不会报错。
- 支持 CPU 超卖，通过超卖配置项 `resource_hard_limit` 控制。`GV$OB_SERVERS` 视图中的 `CPU_CAPACITY` 和 `CPU_CAPACITY_MAX` 字段分别表示节点 CPU 总容量和节点 CPU 总容量的超卖值，且 `CPU_CAPACITY_MAX = CPU_CAPACITY * resource_hard_limit`。
- 不再支持内存超卖，引入内存超卖可能会导致租户工作不稳定。
- 支持租户间日志盘空间隔离，系统为每个租户预留日志盘空间，避免 V3.x 版本某个租户大量写入导致日志盘写爆从而影响其他租户的问题。
- 支持租户间 IOPS 隔离，引入三个 IOPS 规格参数：`MIN_IOPS`、`MAX_IOPS`、`IOPS_WEIGHT`，IOPS 规格参数默认不需要指定，系统根据 CPU 规格自动计算。如果一个节点上所有 Unit 的 `MIN_IOPS` 之和超过了磁盘 IOPS 上限，则会根据 `IOPS_WEIGHT` 权重来分配 IOPS 资源。
- Meta 租户没有独立的 Unit，系统创建租户时默认为 Meta 租户预留资源，各项资源从用户租户资源中扣除。Meta 各项资源采用默认配置，不支持用户指定。
- 创建资源规格时 CPU 规格 和内存规格是必选项，其他参数可以自动计算，其中日志盘空间按照内存规格自动计算，IOPS 规格按照 CPU 规格自动计算。

#### 注意

在指定 `PRIMARY_ZONE` 时，其值可以设置为 RANDOM（必须大写），表示指定租户所在的所有 Zone 作为 `PRIMARY_ZONE` 的第一优先级。
