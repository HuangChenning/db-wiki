---
title: "删除分区"
book: "数据库对象管理"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577943.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 删除分区

#### 说明

- 删除一级分区时，可以删除一个或多个分区，但不能删除全部分区。

- 删除一级分区时，请尽量保证该分区上不存在活动的事务或查询，否则可能会导致 SQL 语句报错，或者出现一些异常情况。在 `sys` 租户下，通过视图 `oceanbase.GV$OB_TRANSACTION_PARTICIPANTS` 查询当前还未结束的事务上下文状态。

- 删除一级分区时，会同时删除分区中的数据，如果只需要删除数据，则可以使用 `TRUNCATE` 语句。

- 对于二级分区表，删除一级分区时，会同时删除该一级分区的定义和其对应的二级分区及数据。

#### 说明

- 删除二级分区表中的二级分区时，请尽量保证该分区上不存在活动的事务或查询，否则可能会导致 SQL 语句报错，或者出现一些异常情况。在 `sys` 租户下，通过视图 `oceanbase.GV$OB_TRANSACTION_PARTICIPANTS` 查询当前还未结束的事务上下文状态。

- 删除二级分区会同时删除该分区的定义和其中的数据。

- 当删除多个二级分区时，这些二级分区必须属于同一个一级分区。
