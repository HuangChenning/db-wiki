---
title: "Truncate 分区"
book: "数据库对象管理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150300.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# Truncate 分区

#### 说明

- Truncate 一级分区时，可以将一个或多个分区中的数据清空。

- 在 Truncate 一级分区时，请尽量保证该分区上不存在活动的事务或查询，否则可能会导致 SQL 语句报错，或者出现一些异常情况。在 `sys` 租户下，通过视图 `oceanbase.GV$OB_TRANSACTION_PARTICIPANTS` 查询当前还未结束的事务上下文状态。

- 对于二级分区表，Truncate 一级分区时，会将一个或多个一级分区及其对应的二级分区中的数据全部清空。

#### 说明

- Truncate 二级分区表中的二级分区时，请尽量保证该分区上不存在活动的事务或查询，否则可能会导致 SQL 语句报错，或者出现一些异常情况。在 `sys` 租户下，通过视图 `oceanbase.GV$OB_TRANSACTION_PARTICIPANTS` 查询当前还未结束的事务上下文状态。

- 当 Truncate 多个二级分区时，这些二级分区必须属于同一个一级分区。
