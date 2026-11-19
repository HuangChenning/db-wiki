---
title: "数据库开发规范最佳实践"
book: "数据表设计"
version: master
source: "https://www.oceanbase.com/docs/common-best-practices-1000000001598457.html"
tags:
  - oceanbase
  - best-practices
  - database-design
---

# 数据库开发规范最佳实践

#### 说明

MYSQL 数据库表存储模型也是 `IOT`，Oracle 数据库则不是，建议从 Oracle 数据库迁移过来的表将主键改为唯一索引以实现和 Oracle 表存储近似的效果（比如下述分区表，Oracle 堆表不要求主键必须包含分区键）。

#### 说明

`gmt_create`，`gmt_modified` 的类型选择 `DATE` （精确到秒）或 `TIMESTAMP WITH TIME ZONE`（精确到微秒，且带当前时区信息），可以使用 `SYSDATE` 或 `SYSTIMESTAMP` 函数。

#### 注意

`NUMBER(1)` 也可以表达是与否的概念，但占用的空间更大些。

#### 注意

字符数据类型的列可以存储所有字母数字值，但是 `NUMBER` 数据类型的列只能存储数字值。
