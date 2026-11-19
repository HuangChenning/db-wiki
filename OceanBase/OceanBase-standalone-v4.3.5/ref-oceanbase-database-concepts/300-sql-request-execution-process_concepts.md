---
title: "SQL 请求执行流程"
book: "系统原理"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003578042.html"
tags:
  - oceanbase
  - standalone
  - ref-oceanbase-database-concepts
---

# SQL 请求执行流程

#### 说明

此执行流程适用于 DML 和 `SELECT` 语句，其他语句（例如 DCL ）没有优化器等步骤。
