---
title: "创建表"
book: "应用开发"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701986.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# 创建表

#### 说明

您可以使用 `SHOW TABLES;` 语句查看数据库中表的信息。

#### 注意

因为未添加列信息，所以下方这条 SQL 暂时还不能被运行。

#### 说明

如果系统变量 `SQL_MODE` 的值为 `NO_AUTO_VALUE_ON_ZERO`，则表示不要在插入值为零的列中生成 `AUTO_INCREMENT`。

#### 注意

对于 Hash/Key 分区，如果是通过指定分区数的方式（例如，`SUBPARTITIONS 5`）进行二次分区，则在创建模板化二级分区表时，不需要指定 `SUBPARTITION TEMPLATE` 关键字。
