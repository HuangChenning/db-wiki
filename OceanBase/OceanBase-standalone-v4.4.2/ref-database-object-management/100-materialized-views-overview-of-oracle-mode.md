---
title: "物化视图概述"
book: "数据库对象管理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006078103.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 物化视图概述

#### 说明

OceanBase 数据库支持普通视图声明为维度表（`AS OF PROCTIME()`）时，可以作为增量刷新物化视图的基表。

#### 说明

OceanBase 数据库支持外表作为物化视图的基表来创建全量刷新物化视图。
