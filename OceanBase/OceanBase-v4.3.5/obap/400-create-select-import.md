---
title: "使用 CREATE TABLE AS SELECT 语句旁路导入数据"
book: OceanBase AP
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000006273219.html"
tags:
  - oceanbase
  - distributed
  - obap
---

# 使用 CREATE TABLE AS SELECT 语句旁路导入数据

#### 注意

当 `load_mode` 取值为 `inc_replace` 时，`CREATE TABLE AS SELECT` 语句中不允许有 `REPLACE` 或 `IGNORE` 关键字。
