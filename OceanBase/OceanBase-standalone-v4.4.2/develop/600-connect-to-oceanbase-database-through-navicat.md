---
title: "通过 Navicat 连接数据库"
book: "应用开发"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077439.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# 通过 Navicat 连接数据库

#### 注意

连接租户的用户需要拥有该数据库的 `CREATE`、`INSERT`、`DROP` 和 `SELECT` 权限。更多有关用户权限的信息，请参见 [MySQL 模式下的权限分类](../manage/100-permission-classification-of-mysql.md)。

#### 说明

不同 Navicat 版本的操作界面可能不同，本文档以 Navicat 16.3.7 版本为例提供数据库的连接指导，其他版本的操作请参考 Navicat 对应版本的产品文档。

#### 说明

您可通过 IP 直连方式连接数据库。直连时 Port 填写配置的 \`mysql_port\` 进行连接，默认端口为 2881。
