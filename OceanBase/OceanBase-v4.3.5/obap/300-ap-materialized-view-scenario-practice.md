---
title: "物化视图经典场景实践"
book: OceanBase AP
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005787634.html"
tags:
  - oceanbase
  - distributed
  - obap
---

# 物化视图经典场景实践

#### 说明

语法、限制条件等详细信息，参见：[创建物化视图](../ref-database-object-management/300-create-materialized-views-of-mysql-mode.md)、[刷新物化视图](../ref-database-object-management/400-refresh-materialized-views-of-mysql-mode.md)、[物化视图查询改写](../ref-database-object-management/500-materialized-views-rewrite-of-mysql-mode.md)、[物化视图日志](../ref-database-object-management/200-materialized-views-log-of-mysql-mode.md)、[物化视图日志自动管理](../ref-database-object-management/250-automatic-management-materialized-views-log-of-mysql-mode.md)。

#### 注意

实时数仓并不等于“所有查询都实时刷新”。若业务可接受分钟级延迟，优先采用 FAST + 调度；仅在确有低延迟要求且可接受读时开销时，再引入 `ENABLE ON QUERY COMPUTATION`。
