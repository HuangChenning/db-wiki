---
title: "数据湖概述"
book: OceanBase AP
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000006319714.html"
tags:
  - oceanbase
  - distributed
  - obap
---

# 数据湖概述

#### 说明

数据湖相关能力以 **MySQL 模式**为主；Catalog 能力当前仅 MySQL 模式支持。具体语法与版本边界以 `700.reference` 下 SQL 参考文档为准；接入步骤详见本目录各子文档。

#### 注意

当前 [CREATE EXTERNAL CATALOG](../ref-sql-reference/2150-create-external-catalog-of-mysql-mode.md) SQL 参考文档主要说明 `TYPE = 'ODPS'` 的用法。创建 ODPS Catalog 需 OceanBase 数据库 V4.3.5 BP2 及以上版本。详细说明参见 [ODPS Catalog](100-odps-catalog.md)。

#### 说明

Azure Blob（`azblob://`）当前见于备份/归档等场景；外表 `LOCATION` 是否支持请以 [CREATE EXTERNAL TABLE](../ref-sql-reference/2200-create-external-table-of-mysql-mode.md) 为准。
