---
title: "执行计划"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002702030.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 执行计划

#### 注意

- 查询 `GV$OB_PLAN_CACHE_PLAN_EXPLAIN` 视图时 , 需要指定 `TENANT_ID`、`SVR_IP`、`SVR_PORT`、`PLAN_ID` 的等值条件，否则查询结果为空。
- 查询 `V$OB_PLAN_CACHE_PLAN_EXPLAIN` 视图时, 需要指定 `TENANT_ID`、`PLAN_ID` 的等值条件，否则查询结果为空。
