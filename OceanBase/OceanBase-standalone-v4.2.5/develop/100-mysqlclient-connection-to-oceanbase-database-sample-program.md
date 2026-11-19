---
title: mysqlclient
book: "应用开发"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002702168.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# mysqlclient

#### 说明

您也可以直接运行 `pip install mysqlclient` 命令安装 mysqlclient 库。

#### 说明

您也可以直接运行 `sudo pip install mysqlclient` 命令安装 mysqlclient 库。

#### 注意

连接租户的用户需要拥有该数据库的 `CREATE`、`INSERT` 和 `SELECT` 权限。更多有关用户权限的信息，请参见 [MySQL 模式下的权限分类](../manage/100-permission-classification-of-mysql.md)。

#### 注意

字段年龄的数据类型是整型。

#### 说明

本文获取的代码中只列出了 mysqlclient 库的版本要求，可以通过 `pip install -r requirements.txt` 命令安装，执行以上命令后，会自动安装所需的库。

#### 注意

具体的属性（参数）配置取决于项目需求和数据库的特点，建议您根据实际情况进行调整和配置。

#### 说明

这种写法可以避免在导入该模块时自动执行 `main` 函数，从而保证程序的可重用性和可扩展性。
