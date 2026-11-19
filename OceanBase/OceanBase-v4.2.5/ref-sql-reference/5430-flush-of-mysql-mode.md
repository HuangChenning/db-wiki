---
title: FLUSH
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001503320.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# FLUSH

## 描述

该语句用于清理或刷新特定的内部缓存、日志和表。

## 语法

```sql
FLUSH [NO_WRITE_TO_BINLOG | LOCAL] {
    flush_option [, flush_option] ...
}

flush_option: {
    BINARY LOGS
  | DES_KEY_FILE
  | ENGINE LOGS
  | ERROR LOGS
  | GENERAL LOGS
  | HOSTS
  | LOGS
  | PRIVILEGES
  | OPTIMIZER_COSTS
  | QUERY CACHE
  | RELAY LOGS [FOR CHANNEL channel]
  | SLOW LOGS
  | STATUS
  | USER_RESOURCES
}
```

<main id="notice" type='notice'>
  <h4>注意</h4>
  <p>当前版本仅支持该关键字语法，功能并不会实际生效。</p>
</main>
