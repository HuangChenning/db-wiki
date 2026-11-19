---
title: Dataphin
book: "生态集成"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005476952.html"
tags:
  - oceanbase
  - distributed
  - ecological-integration
---

# Dataphin

#### 注意

连接租户的用户需要拥有该数据库的 `CREATE`、`INSERT`、`DROP` 和 `SELECT` 权限。更多有关用户权限的信息，请参见 [MySQL 模式下的权限分类](../manage/100-permission-classification-of-mysql.md)。

#### 注意

离线计算每次执行都是全量数据采集。如果数据在目标表中不存在则插入，存在就不再插入。

#### 注意

Dataphin 实时计算不支持直接选择 OceanBase 作为数据源。OceanBase 连接器在 Flink 中只能作为目的表和维表，不能作为源表。
