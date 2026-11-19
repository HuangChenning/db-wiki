---
title: SpringDataJPA
book: "应用开发"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077969.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# SpringDataJPA

#### 说明

本文档运行代码使用的工具是 IntelliJ IDEA 2021.3.2 (Community Edition) 版本，您也可以根据个人喜好选择适合自己的工具运行示例代码。

#### 说明

本文中给出的操作步骤是基于 Windows 环境生成。如果您使用的是其他操作系统环境或编译器，那么操作步骤可能会略有不同。

#### 说明

在 `application.yml` 文件中需要这里的 URL 信息。

#### 说明

当使用 IntelliJ IDEA 导入项目时，IntelliJ IDEA 会自动检测项目中的 pom.xml 文件，并根据文件中描述的依赖关系自动下载所需的依赖库，并将它们添加到项目中。

#### 注意

使用 MySQL Connector/J 8.x 时，确保账号密码不包含井号(#)。否则，可能会遇到连接错误。

#### 说明

如果您只是想验证示例，那么请使用默认代码，无需修改。您也可以按照以下讲解，根据自己的需求修改 `pom.xml` 文件。
