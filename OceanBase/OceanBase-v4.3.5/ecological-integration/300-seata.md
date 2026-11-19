---
title: Seata
book: "生态集成"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000006053913.html"
tags:
  - oceanbase
  - distributed
  - ecological-integration
---

# Seata

#### 注意

连接租户的用户需要拥有该数据库的 `CREATE`、`INSERT`、`DROP` 和 `SELECT` 权限。更多有关用户权限的信息，请参见 [MySQL 模式下的权限分类](../manage/100-permission-classification-of-mysql.md)。

#### 注意

请将 `$host`、`$port`、`$database_name`、`$user_name`、`$password` 替换为您的实际 OceanBase 数据库连接信息。

#### 注意

请将 `$test_host` 和 `$test_port` 替换为您的实际测试服务地址和端口。
