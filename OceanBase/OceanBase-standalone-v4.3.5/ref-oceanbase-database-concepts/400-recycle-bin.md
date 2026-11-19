---
title: "回收站"
book: "系统原理"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577987.html"
tags:
  - oceanbase
  - standalone
  - ref-oceanbase-database-concepts
---

# 回收站

#### 注意

- 直接删除索引，该索引不会进入回收站。删除表时，表上的索引会随主表一起进入回收站。
- 不能对回收站对象做任何查询和 DML 操作，DDL 操作中也仅支持 Purge 和 Flashback 操作。
- 租户回收站的管理主要由 `sys` 租户来完成。
