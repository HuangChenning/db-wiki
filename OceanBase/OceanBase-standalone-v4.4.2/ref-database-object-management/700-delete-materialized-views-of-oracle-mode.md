---
title: "删除物化视图"
book: "数据库对象管理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006078102.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 删除物化视图

#### 注意

Oracle 模式中视图 `sys.DBA_MVIEWS` 中字段 `OWNER` 匹配 Schema 名时，Schema 名需使用大写字母。

#### 注意

物化视图的基表上如果创建了物化视图日志，需要先删除基表上的物化视图日志，才能删除基表，否则报错。
