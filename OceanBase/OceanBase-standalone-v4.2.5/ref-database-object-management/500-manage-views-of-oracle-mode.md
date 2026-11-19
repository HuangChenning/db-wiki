---
title: "管理视图"
book: "数据库对象管理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150379.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 管理视图

#### 说明

Oracle 模式下的 `WITH CHECK OPTION` 语法不支持指定为 `LOCAL` 或 `CASCADED`，默认为 `CASCADED`。

#### 注意

当过滤条件中使用 `WITH CHECK OPTION` 子句时，视图定义中暂不支持使用 `JOIN` 操作。
