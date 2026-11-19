---
title: location_cache_refresh_sql_timeout
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700943.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# location_cache_refresh_sql_timeout

`location_cache_refresh_sql_timeout`表示通过 SQL 刷新 `location_cache` 的超时时间。

## 描述

|        属性        |    描述     |
|------------------|-----------|
| 参数类型             | 时间类型      |
| 默认值              | 1s        |
| 取值范围             | \[1ms,+∞） |
| 是否重启 OBServer 节点生效 | 否         |

**示例**

```sql
obclient> ALTER SYSTEM SET location_cache_refresh_sql_timeout = '2s';
```
