---
title: "删除分区"
book: "数据库对象管理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150358.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 删除分区

#### 说明

- 删除一级分区时，可以删除一个或多个分区，但不能删除全部分区。

- 删除分区会同时删除分区中的数据。如果您只需要删除数据，可以使用 `TRUNCATE` 语句。
