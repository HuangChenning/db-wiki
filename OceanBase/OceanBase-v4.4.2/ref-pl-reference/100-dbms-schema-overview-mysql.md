---
title: "DBMS_SCHEMA 概述"
book: "PL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005936903.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# DBMS_SCHEMA 概述

`DBMS_SCHEMA` 用于提供 Schema 多版本历史数据（Schema History）回收和 Root Service 自检（Root Inspection）的手动触发能力。

<main id="notice" type='explain'>
<h4>说明</h4>
<p>对于 V4.4.2 版本，该系统包从 OceanBase 数据库 V4.4.2 BP1 版本开始引入。</p>
</main>

## DBMS_SCHEMA 子程序概览

下表列出了 OceanBase 数据库当前版本所支持的 `DBMS_SCHEMA` 子程序以及简要描述。

|                **子程序**             |                 **描述**                       |
|-----------------------------------------|------------------------------------------------|
|[RECYCLE_SCHEMA_HISTORY](200.recycle-schema-history-mysql.md)|用于手动执行一轮 Schema 多版本历史数据的回收。|
|[RUN_INSPECTION](300.run-inspection-mysql.md)|用于手动执行一次 Root Service 自检。|
