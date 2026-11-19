---
title: Connector/J
book: "应用开发"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077963.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# Connector/J

#### 注意

连接租户的用户需要拥有该数据库的 `CREATE`、`INSERT`、`DROP` 和 `SELECT` 权限。更多有关用户权限的信息，请参见 [MySQL 模式下的权限分类](../manage/100-permission-classification-of-mysql.md)。

#### 注意

若使用 MySQL Connector/J 8.x，账号密码中需避免包含 `#`，否则会导致示例工程运行报错。

#### 注意

如果是 MySQL Connector/J 8.x 版本，`Class.forName("com.mysql.jdbc.Driver")` 中的 `com.mysql.jdbc.Driver` 需要替换成 `com.mysql.cj.jdbc.Driver`。

#### 说明

本部分代码定义项目所依赖组件是 MySQL Connector/J 的 V5.1.40 版本，如果需要了解其他版本的信息，请参见 [MySQL Connector/J](https://downloads.mysql.com/archives/c-j/)。

#### 注意

使用 MySQL Connector/J 8.x 版本时，账号密码中需避免包含 `#` 字符，否则可能导致连接失败。
