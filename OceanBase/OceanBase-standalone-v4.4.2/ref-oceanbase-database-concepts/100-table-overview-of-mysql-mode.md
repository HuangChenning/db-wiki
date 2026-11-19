---
title: "表概述"
book: "系统原理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006078168.html"
tags:
  - oceanbase
  - standalone
  - ref-oceanbase-database-concepts
---

# 表概述

#### 注意

- 自 OceanBase 数据库 V4.1.0 BP4 版本起，MySQL 模式下已禁用临时表功能。

- 对于 V4.4.x 版本，自 V4.4.2 版本起，MySQL 模式下支持临时表功能。

  ## 列

  ​在数据库中，列（Column）用于记录一张表上某个属性的字段的值，用户给每个属性起的名称即为列名。除了列名以外，列上还有数据类型以及数据类型的最大长度（精度）等信息。

  除了普通列以外，OceanBase 数据库 MySQL 模式下还包括虚拟列（Virtual Column/Generated Column）和自增列（Auto_increment Column）。

  虚拟列不像普通列一样具有真实的物理存储空间，而是在查询时通过用户在虚拟列上定义的一个表达式或函数来计算得到结果的。

  自增列满足以下三个条件：

  - 多分区全局唯一

  - 语句内连续递增

  - 生成的自增列值大于用户显式插入的值

  ## 行

  在数据库中，行（Row）表示表中单条记录中所有列的数据集合。简单来说，数据库可以认为是由列和行组成的。表中的每一行代表一组相关数据，并且表中的每一行具有相同的结构。

  例如，一张与公司信息相关的数据表，每一行代表一个公司，对应的列可能代表诸如公司名称、公司街道地址、增值税号等内容。
