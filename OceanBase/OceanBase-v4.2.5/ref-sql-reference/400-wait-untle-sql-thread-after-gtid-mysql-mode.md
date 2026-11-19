---
title: WAIT_UNTIL_SQL_THREAD_AFTER_GTIDS()
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001504250.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# WAIT_UNTIL_SQL_THREAD_AFTER_GTIDS()

## 描述

该函数用于等待直到 SQL 线程执行了指定的 GTID 集合中的所有事务。

## 语法

```sql
WAIT_UNTIL_SQL_THREAD_AFTER_GTIDS(gtid_set[, timeout][,channel])
```

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>仅支持该关键字语法，功能不生效。</p>
</main>
