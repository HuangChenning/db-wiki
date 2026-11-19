---
title: ALTER SYSTEM PARAMETER
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001701410.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# ALTER SYSTEM PARAMETER

## 描述

该语句用来修改本租户的配置项信息。

## 语法

```sql
ALTER SYSTEM SET parameter_name = expression;
```

## 参数解释

|     **参数**     |    **描述**    |
|----------------|--------------|
| parameter_name | 指定要修改的配置项名称。 |
| expression     | 指定修改后的配置项的值。 |

## 示例

修改配置项 `log_disk_utilization_threshold` 的信息。

```sql
obclient> SHOW PARAMETERS LIKE 'log_disk_utilization_threshold';
+-------+----------+----------------+----------+--------------------------------+-----------+-------+--------------------------------------------------------------------------------------------------------------------------------------+------------+--------+---------+-------------------+
| zone  | svr_type | svr_ip         | svr_port | name                           | data_type | value | info                                                                                                                                 | section    | scope  | source  | edit_level        |
+-------+----------+----------------+----------+--------------------------------+-----------+-------+--------------------------------------------------------------------------------------------------------------------------------------+------------+--------+---------+-------------------+
| zone1 | observer | xx.xx.xx.xx    |     2882 | log_disk_utilization_threshold | NULL      | 80    | log disk utilization threshold before reuse log files, should be smaller than log_disk_utilization_limit_threshold. Range: [10, 100) | LOGSERVICE | TENANT | DEFAULT | DYNAMIC_EFFECTIVE |
+-------+----------+----------------+----------+--------------------------------+-----------+-------+--------------------------------------------------------------------------------------------------------------------------------------+------------+--------+---------+-------------------+
1 row in set 

obclient> ALTER SYSTEM SET log_disk_utilization_threshold = 20;
Query OK, 0 rows affected

obclient> SHOW PARAMETERS LIKE 'log_disk_utilization_threshold';
+-------+----------+----------------+----------+--------------------------------+-----------+-------+--------------------------------------------------------------------------------------------------------------------------------------+------------+--------+---------+-------------------+
| zone  | svr_type | svr_ip         | svr_port | name                           | data_type | value | info                                                                                                                                 | section    | scope  | source  | edit_level        |
+-------+----------+----------------+----------+--------------------------------+-----------+-------+--------------------------------------------------------------------------------------------------------------------------------------+------------+--------+---------+-------------------+
| zone1 | observer | xx.xx.xx.xx    |     2882 | log_disk_utilization_threshold | NULL      | 20    | log disk utilization threshold before reuse log files, should be smaller than log_disk_utilization_limit_threshold. Range: [10, 100) | LOGSERVICE | TENANT | DEFAULT | DYNAMIC_EFFECTIVE |
+-------+----------+----------------+----------+--------------------------------+-----------+-------+--------------------------------------------------------------------------------------------------------------------------------------+------------+--------+---------+-------------------+
1 row in set 
```
