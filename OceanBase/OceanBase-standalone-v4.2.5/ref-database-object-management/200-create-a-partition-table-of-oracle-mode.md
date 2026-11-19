---
title: "创建分区表"
book: "数据库对象管理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150354.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 创建分区表

#### 说明

- List 分区的分区键不能是表达式。
- 如果最后一个 List 分区指定了 `DEFAULT`，则不能新增分区。

#### 说明

对于 Hash 分区，创建时如果没有指定分区的名字，分区的命名由系统根据命名规则完成。对于一级分区表，则每个分区分别命名为 p0、p1、...、pn。

#### 说明

- 模板化二级分区表的每个一级分区下的二级分区都按照模板中的二级分区定义，即每个一级分区下的二级分区的定义均相同。
- 对于模板化二级分区表来说，二级分区的命名规则为 `($part_name)s($subpart_name)`。

#### 说明

非模板化二级分区表的每个一级分区下的二级分区均可以自由定义，即每个一级分区下的二级分区的定义可以相同也可以不同。
