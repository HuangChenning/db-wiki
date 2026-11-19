---
title: ALTER RESOURCE TENANT
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700694.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# ALTER RESOURCE TENANT

ALTER RESOURCE TENANT
=======================================

描述
-----------------------

该语句用来修改租户资源池的配置。

语法
-----------------------

```sql
ALTER RESOURCE TENANT tenant_name UNIT_NUM [=] unit_num; 
```

参数解释
-------------------------

|  **参数**   |   **描述**   |
|-----------|------------|
| tenant_name | 修改配置的租户名称。 |
| UNIT_NUM [=] unit_num |修改租户下所有资源池的 Unit 个数。取值要小于等于对应 Zone 中的 OBServer 节点个数。 |

示例
-----------------------

修改租户 `tenant1` 下所有资源池的 Unit 个数为 3。

```sql
obclient> ALTER RESOURCE TENANT tenant1 UNIT_NUM = 3;
Query OK, 0 rows affected 
```
