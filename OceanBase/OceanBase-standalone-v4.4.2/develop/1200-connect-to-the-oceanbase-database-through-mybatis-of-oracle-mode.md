---
title: MyBatis
book: "应用开发"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006078011.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# MyBatis

#### 说明

本文档运行代码使用的工具是 IntelliJ IDEA 2021.3.2 (Community Edition) 版本，您也可以根据个人喜好选择适合自己的工具运行示例代码。

#### 说明

本文中给出的操作步骤是基于 Windows 环境生成。如果您使用的是其他操作系统环境或编译器，那么操作步骤可能会略有不同。

#### 说明

在 `jdbc.properties` 文件中需要这里的 URL 信息。

#### 说明

当使用 IntelliJ IDEA 导入项目时，IntelliJ IDEA 会自动检测项目中的 pom.xml 文件，并根据文件中描述的依赖关系自动下载所需的依赖库，并将它们添加到项目中。

#### 说明

如果您只是想验证示例，那么请使用默认代码，无需修改。您也可以按照以下讲解，根据自己的需求修改 `pom.xml` 文件。

#### 说明

代码中各字段的值从 **步骤一：获取 OceanBase 数据库连接串** 中直接获取。

#### 说明

settings 元素中的子元素是可选的，可以根据实际情况进行添加或删除。

#### 说明

在 MyBatis 的其他配置元素中，可以使用 `${}` 占位符来引用环境中配置的数据源、事务管理器和执行器等。

#### 说明

如果使用 XML 配置文件，需要在 mapper 元素中指定 XML 文件的路径和文件名；如果使用 Java 接口，需要在 mapper 元素中指定 Java 类的全限定名。

#### 说明

如果您只是想验证示例，那么请使用默认代码，无需修改。若需要修改，请根据实际情修改。
