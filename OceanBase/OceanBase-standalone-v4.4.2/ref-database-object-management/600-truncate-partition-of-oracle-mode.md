---
title: "Truncate 分区"
book: "数据库对象管理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077663.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# Truncate 分区

#### 说明

对于 V4.4.2 版本，从 V4.4.2 BP1 版本开始 `INTERVAL` 分区表支持 `UPDATE GLOBAL INDEXES` 语法。

#### 说明

- Truncate 一级分区时，支持将一个或多个分区中的数据清空。

- Truncate 二级分区表中的一级分区时，会将该分区及其对应的二级分区中的数据全部清空。

#### 说明

Truncate 二级分区时，支持将一个或多个二级分区中的数据全部清空。
