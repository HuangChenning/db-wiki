---
title: Apache Flink
book: "生态集成"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005146839.html"
tags:
  - oceanbase
  - distributed
  - ecological-integration
---

# Apache Flink

#### 说明

通过 `CREATE TABLE` 定义源与目标，再用一条 `INSERT INTO ... SELECT` 语句，即可实现实时、带转换的数据同步。

#### 注意

- 不同 Connector 不可互换，需根据场景精准选择。
- OceanBase 数据库 MySQL 租户兼容性较好，可以复用 Flink MySQL Connector；Oracle 租户则必须使用 Flink OceanBase Connector。

#### 注意

仅支持 OceanBase 数据库 MySQL 模式租户，Oracle 模式租户暂不支持。

#### 注意

全表扫描是单并行度，但 Lookup 场景通常是点查，不受此限制。

#### 说明

选型建议如下：

- 需要多列族：强烈推荐 OBKV HBase。
  - HBase：一个表搞定多个列族，简单方便。
  - HBase2：需要为每个列族创建单独的表，再分别写入，比较麻烦。
- 需要动态列、部分列更新、时间戳控制等高级特性：必须选择 OBKV HBase2。
- 简单场景（固定列，单列族）：两者都可以，HBase2 表定义更简洁，推荐优先使用。
- 新项目推荐：单列族场景推荐 OBKV HBase2，多列族场景推荐 OBKV HBase。

#### 说明

选型建议如下：

- CDC 场景（全量+增量同步）：优先选择 OceanBase CDC（仅 MySQL 租户）
- Lookup Join 场景（维度表关联）：选择 JDBC Connector。
- 批量全表读取：优先 OceanBase CDC（MySQL 租户），Oracle 租户只能用 JDBC Connector（性能较慢）
