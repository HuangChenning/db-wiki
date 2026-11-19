---
title: "数据湖概述"
book: OceanBase AP
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006338113.html"
tags:
  - oceanbase
  - standalone
  - obap
---

# 数据湖概述

#### 说明

数据湖相关能力以 **MySQL 模式**为主；Catalog 能力当前仅 MySQL 模式支持。具体语法与版本边界以 `700.reference` 下 SQL 参考文档为准；接入步骤详见本目录各子文档。

#### 注意

当前 [CREATE EXTERNAL CATALOG](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005286499) SQL 参考文档主要说明 `TYPE = 'ODPS'` 的用法。创建 ODPS Catalog 需 OceanBase 数据库 V4.3.5 BP2 及以上版本；创建 HMS Catalog 需 V4.4.1 及以上版本。HMS Catalog 的详细说明参见 [通过 Catalog 加载 Hive 表](100-load-hive-via-catalog.md)。

#### 说明

Azure Blob（`azblob://`）当前见于备份/归档等场景；外表 `LOCATION` 是否支持请以 [CREATE EXTERNAL TABLE](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005286424) 为准。
