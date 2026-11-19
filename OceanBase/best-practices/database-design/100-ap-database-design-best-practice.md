---
title: "OceanBase 数据表设计与索引优化最佳实践指南"
book: "数据表设计"
version: master
source: "https://www.oceanbase.com/docs/common-best-practices-1000000002910319.html"
tags:
  - oceanbase
  - best-practices
  - database-design
---

# OceanBase 数据表设计与索引优化最佳实践指南

#### 说明

此示例默认为索引组织表。OceanBase 数据库提供配置项 `default_table_organization` 控制默认创建表的表组织模式。设置配置项的值为 HEAP，表示表组织形式为堆组织表；设置配置项的值为 INDEX，表示表组织形式为索引组织表。详细信息，参考[default_table_organization](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002502221)。

#### 注意

OceanBase 数据库 KEY 分区仅 MySQL 模式支持。
