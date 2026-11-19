---
title: UUID
book: "SQL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005687311.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# UUID

## 声明

```sql
uuid()
```

## 说明

生成一个全局唯一 ID。

## 示例

```sql
obclient> SELECT UUID();
+--------------------------------------+
| UUID()                               |
+--------------------------------------+
| eef95d17-e944-11eb-824a-ca1fa9040697 |
+--------------------------------------+
1 row in set
```
