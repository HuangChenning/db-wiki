---
title: Proxool
book: "应用开发"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006078000.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# Proxool

#### 说明

本文档运行代码使用的工具是 IntelliJ IDEA Community Edition 2021.3.2 版本，您也可以根据个人喜好选择适合自己的工具运行的示例代码。

#### 说明

本文中给出的操作步骤是在 Windows 环境下使用 IntelliJ IDEA Community Edition 2021.3.2 编译和运行该项目的步骤。如果您使用的是其他操作系统环境或编译器，那么操作步骤可能会略有不同。

#### 说明

当使用 IntelliJ IDEA 导入 Maven 项目时，IntelliJ IDEA 会自动检测项目中的 `pom.xml` 文件，并根据文件中描述的依赖关系自动下载所需的依赖库，并将它们添加到项目中。

#### 注意

连接租户的用户需要拥有 `CREATE SESSION` 权限和该 Schema 的 `CREATE TABLE`、`INSERT`、`DELETE`、`UPDATE` 和 `SELECT` 权限。更多有关用户权限的信息，请参见 [Oracle 模式下的权限分类](../manage/000-permission-classification-of-oracle-mode.md)。

#### 说明

Java 1.8 和 Java 8 是同一个版本的不同命名方式。

#### 说明

本部分代码定义项目所依赖组件是 OceanBase Connector/J 的 V2.4.2 版本，如果需要了解其他版本的信息，请参见 [OceanBase JDBC 驱动程序](https://www.oceanbase.com/docs/oceanbase-connector-j-cn)

#### 说明

使用 `.properties` 文件配置 Proxool 连接池时，需要遵循以下规则：

1.  以 `jdbc` 为前缀的自定义名称来标识每个连接池。可以自定义这个名称，用于唯一标识每个连接池。
2.  Proxool 连接池的相关属性应该以 `proxool.` 为前缀，这些属性将被用于配置 Proxool 连接池自身的属性。
3.  没有以 `jdbc` 为前缀的属性将会被忽略，不会被 Proxool 使用。
4.  没有以 `proxool.` 为前缀的属性将被传递给实际的数据库连接，即这些属性将被传递给实际的数据库驱动程序。

更多配置 Proxool 连接池的方法，请参见 [Configuration](https://proxool.sourceforge.net/configure.html)。

#### 注意

具体的属性（参数）配置取决于项目需求和数据库的特点，建议您根据实际情况进行调整和配置。更多 Proxool 连接池参数的信息，请参见 [Properties](https://proxool.sourceforge.net/properties.html)。
