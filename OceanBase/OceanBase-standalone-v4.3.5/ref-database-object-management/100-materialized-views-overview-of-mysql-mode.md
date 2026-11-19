---
title: "物化视图概述"
book: "数据库对象管理"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003578272.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 物化视图概述

#### 说明

对于 OceanBase 数据库 V4.3.5 版本：

- 从 V4.3.5 BP2 版本开始支持普通视图作为物化视图的基表来创建全量刷新物化视图。
- 从 V4.3.5 BP5 版本开始支持普通视图声明为维度表（`AS OF PROCTIME()`）时，可以作为增量刷新物化视图的基表。

#### 说明

对于 V4.3.5 版本，从 V4.3.5 BP4 版本开始支持物化视图日志自动管理功能，详细信息，参见 [物化视图日志自动管理](250-automatic-management-materialized-views-log-of-mysql-mode.md)。
