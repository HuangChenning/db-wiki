---
title: "URL 外部表"
book: OceanBase AP
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006123843.html"
tags:
  - oceanbase
  - standalone
  - obap
---

# URL 外部表

#### 注意

- CSV 查询结果默认为 `VARCHAR` 类型（可通过后续 `CAST` 转换）。
- Parquet / ORC 自动推断 Schema（含嵌套结构）。
- 单次读取受集群资源、外部存储与网络条件限制；文档未定义固定文件数或大小上限。
- ODPS 不支持 `FILES()`，须使用 `SOURCE()`（当前以 MySQL 模式 `LOAD DATA` 语法为主）。
- URL 外表（`FILES()` / Location URL）在 MySQL 与 Oracle 模式均支持；具体语法见各模式 SQL 参考。

#### 说明

- `outfiles/` 指定外表文件存放的路径，支持子目录递归扫描。

&nbsp;

- `FORMAT` 用于指定外部文件格式为 CSV 及相关解析选项。

&nbsp;

- `PATTERN` 指定正则模式串，用于过滤 `LOCATION` 目录下的文件；若不指定，则读取所有文件。

&nbsp;

- **重要**：使用 URL 外表读取 CSV 文件时，所有列的数据类型默认为 VARCHAR（可通过后续 CAST 转换为其他类型）。

#### 说明

敏感凭证（如 AccessKey）由 OceanBase 加密存储于系统表；可通过预配置 Location 对象复用，避免在 SQL 中重复明文填写（Location 语法以 SQL 参考为准）。
