---
title: DBCP
book: "应用开发"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002702174.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# DBCP

#### 说明

本文档运行代码使用的工具是 Eclipse IDE for Java Developers 2022-03 版本，您也可以根据个人喜好选择适合自己的工具运行的示例代码。

#### 说明

本文中给出的操作步骤是在 Windows 环境下使用 Eclipse IDE for Java Developers 2022-03 编译和运行该项目的步骤。如果您使用的是其他操作系统环境或编译器，那么操作步骤可能会略有不同。

#### 说明

当使用 Eclipse 导入 Maven 项目时，Eclipse 会自动检测项目中的 `pom.xml` 文件，并根据文件中描述的依赖关系自动下载所需的依赖库，并将它们添加到项目中。

#### 注意

连接租户的用户需要拥有该数据库的 `CREATE`、`INSERT`、`DELETE`、`UPDATE` 和 `SELECT` 权限。更多有关用户权限的信息，请参见 [MySQL 模式下的权限分类](../manage/100-permission-classification-of-mysql.md)。

#### 说明

Java 1.8 和 Java 8 是同一个版本的不同命名方式。

#### 注意

具体的属性（参数）配置取决于项目需求和数据库的特点，建议您根据实际情况进行调整和配置。更多 DBCP 连接池参数的信息，请参见 [BasicDataSource Configuration Parameters](https://commons.apache.org/proper/commons-dbcp/configuration.html)。

#### 注意

`username` 和 `password` 属性将被明确传递，因此不需要在此处包含它们。
