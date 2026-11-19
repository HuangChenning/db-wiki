---
title: UUID
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702743.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
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
