---
title: ENABLE
book: "PL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004479960.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# ENABLE

`ENABLE` 用于启用定时分区均衡功能。

## 语法

```sql
DBMS_SCHEDULER.ENABLE('SCHEDULED_TRIGGER_PARTITION_BALANCE');
```

## 注意事项

开启定时分区均衡任务 `SCHEDULED_TRIGGER_PARTITION_BALANCE` 时，要求租户级配置项 `partition_balance_schedule_interval = 0`，否则报错 `OB_OP_NOT_ALLOW`。配置项触发与定时任务触发不可同时开启。

## 示例

```shell
obclient> CALL DBMS_SCHEDULER.ENABLE('SCHEDULED_TRIGGER_PARTITION_BALANCE');
Query OK, 0 rows affected
```

## 相关阅读

* [partition_balance_schedule_interval](../../../../800.configuration-items-and-system-variables/100.system-configuration-items/400.tenant-level-configuration-items/6400.partition_balance_schedule_interval.md)
