---
title: "外键约束"
book: "系统原理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006078419.html"
tags:
  - oceanbase
  - standalone
  - ref-oceanbase-database-concepts
---

# 外键约束

#### 说明

OceanBase 数据库支持非唯一索引上创建外键约束。

#### 说明

OceanBase 数据库外键和引用键的类型可以是：

- UNSIGNED FLOAT 和 FLOAT。
- FLOAT 和 UNSIGNED FLOAT
- UNSIGNED DOUBLE 和 DOUBLE。
- DOUBLE 和 UNSIGNED DOUBLE。

#### 注意

OceanBase 数据库 MySQL 模式外键级联操作会激活触发器。
