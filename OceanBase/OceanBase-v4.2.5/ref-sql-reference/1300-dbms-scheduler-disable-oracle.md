---
title: DISABLE
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001503786.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# DISABLE

`DISABLE` 用于禁用定时分区均衡功能。

## 语法

```sql
DBMS_SCHEDULER.DISABLE('SCHEDULED_TRIGGER_PARTITION_BALANCE');
```

## 示例

```shell
obclient> CALL DBMS_SCHEDULER.DISABLE('SCHEDULED_TRIGGER_PARTITION_BALANCE');
Query OK, 0 rows affected (0.010 sec)
```
