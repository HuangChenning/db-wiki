---
title: "添加分区"
book: "数据库对象管理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150357.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 添加分区

#### 说明

- 对于 Range 分区，只能在最大的分区之后添加一个分区，不可以在中间某个或者开始的地方添加分区。如果当前的分区中有 `MAXVALUE` 的分区，则不能继续添加分区。

- 向 List 分区中添加一级分区时，要求添加的分区与之前的分区不冲突。如果一个 List 分区有默认分区即 `Default Partition`，则不能添加任何分区。

- 在 Range/List 分区中添加一级分区不会影响全局索引和局部索引的使用。

- 对于模板化二级分区表，添加一级分区时只需要指定一级分区的定义即可，二级分区的定义会⾃动按照模板填充。

#### 说明

对于非模板化二级分区表，添加一级分区时，需要同时指定一级分区的定义和该一级分区下的二级分区定义。
