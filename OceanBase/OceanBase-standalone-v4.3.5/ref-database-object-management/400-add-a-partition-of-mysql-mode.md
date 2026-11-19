---
title: "添加分区"
book: "数据库对象管理"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577944.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 添加分区

#### 说明

- 对于 Range/Range Columns 分区，只能在最大的分区之后添加一个分区，不可以在中间或者开始的地方添加。如果当前的分区中有 `MAXVALUE` 的分区，则不能继续添加分区。

- List/List Columns 分区添加一级分区时，要求添加的分区不与之前的分区冲突即可。如果一个 List/List Columns 分区有默认分区即 `Default Partition`，则不能添加任何分区。

- 向 Range/Range Columns/List/List Columns 分区中添加一级分区不会影响全局索引和局部索引的使用。

- 对于模板化二级分区表，添加一级分区时只需要指定一级分区的定义即可，对应二级分区的定义会⾃动按照模板填充。

#### 说明

对于非模板化二级分区表，添加一级分区时，需要同时指定一级分区的定义和该一级分区下的二级分区定义。

#### 注意

- 不支持二级分区类型是 Hash 或 Key 类型的场景新增二级分区。
- 对于 OceanBase 数据库 V4.3.5 版本，从 V4.3.5 BP1 版本开始支持新增二级分区。
- 添加的二级分区不能与表内现有的一级或二级分区重名。
- 添加 Range 二级分区时，Range 上界要大于当前一级分区下最大分区的上界；添加多个 Range 二级分区时，上界要递增排列，即上界大的 Range 分区写在后面。
- 添加 List 二级分区时，不能与当前一级分区下现有的二级分区值重复。
- 添加多个二级分区的操作是原子的，要么都成功，要么都失败。
