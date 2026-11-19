---
title: information_schema.CHECK_CONSTRAINTS
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699248.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# information_schema.CHECK_CONSTRAINTS

## 功能

记录了 `CREATE TABLE` 操作时，有关表和列相关的约束信息。

## 字段说明

|        字段名称        |      类型       | 是否可以为 NULL |          描述           |
|--------------------|---------------|------------|-----------------------|
| CONSTRAINT_CATALOG | varchar(64) | NO         | 约束所属的目录名称。该值始终为 `def` |
| CONSTRAINT_SCHEMA  | varchar(128)  | NO         | 约束所属的 `SCHEMA` 名称     |
| CONSTRAINT_NAME    | varchar(64)  | NO         | 约束的名称                 |
| CHECK_CLAUSE       | CHAR(2048) | NO         | 指定约束条件的表达式            |
