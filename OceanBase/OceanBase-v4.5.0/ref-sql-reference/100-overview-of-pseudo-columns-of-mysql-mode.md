---
title: "伪列概述"
book: "SQL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004479656.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# 伪列概述

伪列（Pseudocolumn）的行为与表中的列相同，但并未存储具体数值。因此，伪列只具备读属性，您不可以对伪列进行插入、更新、删除的等行为。本章节主要介绍 OceanBase 数据库当前版本所支持的伪列及使用说明。

OceanBase 数据库 MySQL 模式当前版本支持如下伪列类型：

* [PARTITIONID 伪列](200.partititionid-pseudo-column-of-mysql-mode.md)
* [序列伪列](300.sequence-pseudo-column-of-mysql-mode.md)
