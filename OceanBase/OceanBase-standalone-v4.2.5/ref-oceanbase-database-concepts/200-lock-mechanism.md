---
title: "锁机制"
book: "系统原理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150225.html"
tags:
  - oceanbase
  - standalone
  - ref-oceanbase-database-concepts
---

# 锁机制

#### 注意

- `SELECT ... FOR UPDATE` 无法做到读写不互斥。

- 在事务提交过程中，为了维护事务的一致性快照，会有短暂的读写互斥，我们称之为 lock for read。

#### 说明

下面这条 SQL 仅用于展示，并暂时无法执行。

#### 说明

下面这条 SQL 仅用于展示，并暂时无法执行。
