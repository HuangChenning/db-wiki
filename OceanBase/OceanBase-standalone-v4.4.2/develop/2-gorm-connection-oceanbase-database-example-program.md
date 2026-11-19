---
title: GORM
book: "应用开发"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077972.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# GORM

#### 说明

本文档编写代码使用的工具是 IntelliJ IDEA 2021.3.2 (Community Edition) 版本，您也可以根据个人喜好选择适合自己的工具查看示例代码。

#### 说明

本文中给出的操作步骤是在 Windows 环境下生成的。如果您使用的是其他操作系统环境或编译器，那么操作步骤可能会略有不同。

#### 说明

本文档使用的 Go 安装包名为 go1.20.6.windows-amd64.msi。

#### 说明

`\usr\local\go\bin`为默认安装目录，若在安装 Go 语言时修改了安装目录，请替换为对应的目录。

#### 注意

`/usr/local/go/src` 需要替换成 Go 实际安装目录操作。

#### 注意

部分版本 `go install` 的默认执行目录可能不是 `/src`，可以通过 `go install` 执行后的报错判断实际目录。例如，报错 `cannot find package "mysql" in: /usr/local/go/src/vendor/mysql`，则应该将 mysql 文件夹放在 `/src/vendor` 目录下再执行安装命令。

#### 说明

在 `test.go` 文件中需要这里的 URL 信息。

#### 说明

`go.sum` 文件根据运行环境的不同所需要的依赖不同，请根据执行提示下载您所需的依赖项。
