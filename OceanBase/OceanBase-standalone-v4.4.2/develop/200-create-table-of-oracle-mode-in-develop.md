---
title: "创建表"
book: "应用开发"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077475.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# 创建表

#### 说明

对于 V4.4.2 版本，从 V4.4.2 BP2 版本开始支持在创建模板化二级分区表时，为某一级分区定义与定义模板不同的二级分区策略，实现模板化与自定义二级分区的混合使用。

#### 注意

对于 Hash 分区，如果是通过指定分区数的方式（例如，`SUBPARTITIONS 5`）进行二次分区，则在创建模板化二级分区表时，不需要指定 `SUBPARTITION TEMPLATE` 关键字。
