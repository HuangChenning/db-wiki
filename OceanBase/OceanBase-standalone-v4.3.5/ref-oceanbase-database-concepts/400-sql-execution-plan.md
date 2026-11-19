---
title: "SQL 执行计划"
book: "系统原理"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003578041.html"
tags:
  - oceanbase
  - standalone
  - ref-oceanbase-database-concepts
---

# SQL 执行计划

#### 说明

在表操作中，`NAME` 字段会显示该操作涉及的表的名称（别名），如果是使用索引访问，还会在名称后的括号中展示该索引的名称，例如 `t1(t1_c2)` 表示使用了索引 `t1_c2`。如果扫描的顺序是逆序，还会在后面使用 `RESERVE` 关键字标识，例如 `t1(t1_c2,RESERVE)`。
