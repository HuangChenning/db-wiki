---
title: PyMySQL
book: "应用开发"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077978.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# PyMySQL

#### 说明

您也可以直接打开命令提示符或 PowerShell 终端运行 `pip install pymysql` 命令安装 PyMySQL 库。PyMySQL 是一个纯 Python 实现的库，安装简单，无需编译，适合开发环境和测试环境使用。

#### 注意

连接租户的用户需要拥有该数据库的 `CREATE`、`INSERT`、`DROP` 和 `SELECT` 权限。更多有关用户权限的信息，请参见 [MySQL 模式下的权限分类](../manage/100-permission-classification-of-mysql.md)。

#### 说明

本文获取的代码中只列出了 PyMySQL 库的版本要求，可以通过 `sudo pip install -r requirements.txt` 命令安装，执行以上命令后，会自动安装所需的库。

#### 注意

这里的参数值是根据具体环境和数据库设置而定的，需要根据实际情况进行修改。
