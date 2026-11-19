---
title: SQLAlchemy
book: "应用开发"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077977.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# SQLAlchemy

#### 注意

连接租户的用户需要拥有该数据库的 `CREATE`、`INSERT`、`UPDATE` 和 `SELECT` 权限。更多有关用户权限的信息，请参见 [MySQL 模式下的权限分类](../manage/100-permission-classification-of-mysql.md)。

#### 说明

SQLAlchemy 是一个功能强大的 ORM 库，它提供了两种使用方式：Core 和 ORM。Core 提供了 SQL 表达式语言，而 ORM 提供了对象关系映射功能。本文示例主要使用 ORM 方式。
