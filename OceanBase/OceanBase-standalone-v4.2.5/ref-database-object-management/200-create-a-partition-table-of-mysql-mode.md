---
title: "创建分区表"
book: "数据库对象管理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150296.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 创建分区表

#### 注意

- 当使用 List 分区时，需要遵循以下规则：

- 分区表达式的结果必须是整型。

- 分区表达式只能引用一列，不能有多列（即列向量）。

#### 说明

对于 Hash/Key 分区，创建时如果没有指定分区的名字，分区的命名由系统根据命名规则完成。对于一级分区表，则每个分区分别命名为 p0、p1、...、pn。

#### 说明

- 模板化二级分区表的每个一级分区下的二级分区都按照模板中的二级分区定义，即每个一级分区下的二级分区定义均相同。
- 对于模板化二级分区表来说，定义二级分区后，每个二级分区的命名规则为 `($part_name)s($subpart_name)`。例如：对于下⾯的 `tbl_rr` 表，一级分区 `p0` 下的 3 个二级分区的分区名分别为 `p0smp1`、`p0smp2`、`p0smp3`。
