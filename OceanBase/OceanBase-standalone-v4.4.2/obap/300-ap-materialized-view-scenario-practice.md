---
title: "物化视图经典场景实践"
book: OceanBase AP
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006209118.html"
tags:
  - oceanbase
  - standalone
  - obap
---

# 物化视图经典场景实践

#### 说明

语法、限制条件等详细信息，参见：[创建物化视图](../ref-database-object-management/300-create-materialized-views-of-mysql-mode.md)、[刷新物化视图](../ref-database-object-management/400-refresh-materialized-views-of-mysql-mode.md)、[物化视图查询改写](../ref-database-object-management/500-materialized-views-rewrite-of-mysql-mode.md)。

#### 注意

实时数仓并不等于“所有查询都实时刷新”。若业务可接受分钟级延迟，优先采用 FAST + 调度；仅在确有低延迟要求且可接受读时开销时，再引入 `ENABLE ON QUERY COMPUTATION`。

#### 说明

如果使用 V4.4.2 BP2 之前版本，物化视图定义中聚合函数在 `SELECT` 子句中必须包含依赖列，详细介绍参见 [刷新物化视图（MySQL 模式）](../ref-database-object-management/400-refresh-materialized-views-of-mysql-mode.md) 和 [刷新物化视图（Oracle 模式）](../ref-database-object-management/400-refresh-materialized-views-of-oracle-mode.md)。

#### 说明

如果使用 V4.4.2 BP2 之前版本，物化视图定义中聚合函数在 `SELECT` 子句中必须包含依赖列，详细介绍参见 [刷新物化视图（MySQL 模式）](../ref-database-object-management/400-refresh-materialized-views-of-mysql-mode.md) 和 [刷新物化视图（Oracle 模式）](../ref-database-object-management/400-refresh-materialized-views-of-oracle-mode.md)。

#### 说明

如果使用 V4.4.2 BP2 之前版本，物化视图定义中聚合函数在 `SELECT` 子句中必须包含依赖列，详细介绍参见 [刷新物化视图（MySQL 模式）](../ref-database-object-management/400-refresh-materialized-views-of-mysql-mode.md) 和 [刷新物化视图（Oracle 模式）](../ref-database-object-management/400-refresh-materialized-views-of-oracle-mode.md)。
