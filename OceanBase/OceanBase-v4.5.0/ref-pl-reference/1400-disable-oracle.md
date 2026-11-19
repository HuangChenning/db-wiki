---
title: DISABLE
book: "PL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004479966.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
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
