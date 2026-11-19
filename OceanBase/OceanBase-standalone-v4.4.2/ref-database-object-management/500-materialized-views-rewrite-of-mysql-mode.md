---
title: "物化视图查询改写"
book: "数据库对象管理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006078126.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 物化视图查询改写

#### 说明

`MV_REWRITE` 和 `NO_MV_REWRITE` Hint 的优先级高于系统变量 `query_rewrite_enabled`，因此不需要设置 `query_rewrite_enabled`。但是需要设置 `query_rewrite_integrity` 为 `stale_tolerated` 才可以使用非实时物化视图进行改写。

#### 说明

以下示例中查询语句创建的物化视图是全量刷新物化视图。增量刷新物化视图的查询语句如果满足对应条件，同样支持相同场景的查询改写。
