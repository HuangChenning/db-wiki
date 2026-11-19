---
title: "集合操作"
book: "应用开发"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577772.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# 集合操作

#### 说明

OceanBase 数据库 Oracle 模式仅支持 `MINUS`，不支持 `EXCEPT`，尽管两者的语义相同。

#### 注意

各个集合运算符只能操作 `SELECT` 语句的结果集，且各个结果集的列数和数据类型必须相同。
