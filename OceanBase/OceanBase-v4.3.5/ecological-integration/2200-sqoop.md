---
title: Sqoop
book: "生态集成"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005724642.html"
tags:
  - oceanbase
  - distributed
  - ecological-integration
---

# Sqoop

#### 注意

连接租户的用户需要拥有该数据库的 `CREATE`、`INSERT`、`DROP` 和 `SELECT` 权限。更多有关用户权限的信息，请参见 [MySQL 模式下的权限分类](../manage/100-permission-classification-of-mysql.md)。

#### 注意

Oracle 模式下必须使用 `--query` 参数，不支持使用 `--table` 参数，否则会报语法错误。

#### 注意

Oracle 模式下导出功能不可用，使用 `--table` 参数会报语法错误 `ORA-00900`，原因是 Oracle 不支持表名使用 `AS` 语法。
