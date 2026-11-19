---
title: "定义自增列"
book: "数据库对象管理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077720.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 定义自增列

#### 说明

OceanBase 数据库也支持表级设置 `auto_increment_cache_size`，相关语法信息请参见 [CREATE TABLE](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005286449) 和 [ALTER TABLE](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005286496)。

#### 注意

该场景下，仅作为 Leader 的 OBServer 节点发生重启或宕机时，才会发生自增值跳变的问题，其他作为 Follower 的 OBServer 节点由于不保存缓存，即使发生了宕机也不会影响自增值生成的连续性。

#### 说明

如果 `SQL_MODE` 设置为 `NO_AUTO_VALUE_ON_ZERO`，则表示不要在列中的 `INSERT` 为零时生成 `AUTO_INCREMENT`。

#### 说明

修改为自增列时，可以同时修改该列的数据类型，但需要确保修改后的数据类型是允许自增的数据类型。

#### 说明

如果在建表时未指定自增模式，则表创建成功后，系统会按照配置项的自增模式来指定，该配置项默认为 `ORDER`。

#### 注意

当减小一个表的自增字段的值时，需注意以下情况：\
如果表中已存在数据并且自增列中的最大值不小于新指定的 `AUTO_INCREMENT` 值时，新的 `AUTO_INCREMENT` 值将自动调整为表中自增列现有最大值的下一个取值。例如，自增列当前的最大值为 5，当前 `AUTO_INCREMENT` 的值是 8，而 `AUTO_INCREMENT` 设置为介于 0 到 6 之间的任何值，语句执行成功后，实际的 `AUTO_INCREMENT` 值都会被调整为 6。

#### 说明

通过查询结果可以观察到，`AUTO_INCREMENT` 的值为 6。这是由于表中的自增列已经包含数据，且当前自增列的最大值（5）超过了尝试设置的较小值（3）。因此，尽管减小自增值的命令执行没有报错，但实际的 `AUTO_INCREMENT` 值自动调整为现有最大自增值的下一个数字，即 6。
