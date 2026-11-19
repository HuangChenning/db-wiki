---
title: SpringBatch
book: "应用开发"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003578116.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# SpringBatch

#### 说明

本文档运行代码使用的工具是 IntelliJ IDEA 2021.3.2 (Community Edition) 版本，您也可以根据个人喜好选择适合自己的工具运行示例代码。

#### 说明

本文中给出的操作步骤是基于 Windows 环境生成。如果您使用的是其他操作系统环境或编译器，那么操作步骤可能会略有不同。

#### 说明

在 `application.properties` 文件中需要这里的 URL 信息。

#### 说明

当使用 IntelliJ IDEA 导入项目时，IntelliJ IDEA 会自动检测项目中的 pom.xml 文件，并根据文件中描述的依赖关系自动下载所需的依赖库，并将它们添加到项目中。

#### 注意

使用 MySQL Connector/J 8.x 时，确保账号密码不包含井号(#)。否则，可能会遇到连接错误。

#### 说明

如果您只是想验证示例，那么请使用默认代码，无需修改。您也可以按照以下讲解，根据自己的需求修改 `pom.xml` 文件。

#### 说明

在 Spring Batch 中，`spring.batch.job.enabled` 属性的作用是控制批处理作业的执行行为。

- `spring.batch.job.enabled=true` (默认值)：表示在 Spring Boot 应用启动时，自动运行所有定义的批处理作业。这意味着在应用启动时，Spring Batch 会自动发现并执行所有定义的作业。
- `spring.batch.job.enabled=false`：表示禁用自动执行批处理作业。这通常用于开发或测试环境，或者当你希望手动控制作业执行时。设为 `false` 后，作业不会在应用启动时自动执行，您可以通过其他方式（如 REST 接口、命令行等）手动触发作业。

总结来说，设置 `spring.batch.job.enabled=false` 可以帮助您避免在应用启动时自动运行作业，提供更大的灵活性来控制何时执行批处理作业。
