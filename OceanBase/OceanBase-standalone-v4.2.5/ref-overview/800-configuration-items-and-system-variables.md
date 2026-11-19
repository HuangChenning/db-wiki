---
title: "配置项和系统变量"
book: "参考指南概览"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150394.html"
tags:
  - oceanbase
  - standalone
  - ref-overview
---

# 配置项和系统变量

#### 说明

- OceanBase 集中式数据库与分布式数据库源自于同一套内核底座，SQL 语法、系统视图、系统变量、配置项等参考信息完全一致。为确保内容的唯一性与时效性，本章节将跳转至分布式数据库文档的对应章节，相关内容同样适用于集中式数据库；如存在差异，将在对应章节中单独说明。

#### 注意

关于 OceanBase 数据库视图的详细介绍以及每一个视图的含义和使用示例，参见 [配置项和变量](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001499714)

#### 说明

配置项一般分为动态生效和重启生效两种方式，大部分配置项为动态生效方式，即不需要重启 OBServer 节点就可以生效。

#### 注意

Oracle 模式下设置 `ALTER SYSTEM SET XXX='True'/'False'` 有部分调整：

1.  在 V4.2.1 BP5 之前版本和 V4.2.3 版本中，True/False 必须加上单引号才能配置。
2.  在 V4.2.1 BP5 及之后版本（V4.2.3 版本除外），True/False 加不加引号都可配置。
