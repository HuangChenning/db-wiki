---
title: CONNECTION_ID
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702760.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# CONNECTION_ID

## 声明

```sql
CONNECTION_ID()
```

## 说明

返回当前会话的 `SESSION_ID`，该 ID 是会话在客户端中的唯一标识。

您可以通过 `SHOW PROCESSLIST` 语句查询当前数据库中会话的数量及会话的 ID。

## 示例

```sql
obclient> select CONNECTION_ID();
+-----------------+
| CONNECTION_ID() |
+-----------------+
|      3221638476 |
+-----------------+
1 row in set 

obclient> SELECT SESSION_ID,TRANS_ID FROM oceanbase.__all_virtual_trans_stat WHERE SESSION_ID=CONNECTION_ID();
+------------+------------------------------------------------------------------------------------------+
| SESSION_ID | TRANS_ID                                                                                 |
+------------+------------------------------------------------------------------------------------------+
| 3221638476 | {hash:6868349667767780996, inc:95279944, addr:"xxx.xxx.xx.xxx:xxxx", t:1626333606027937} |
+------------+------------------------------------------------------------------------------------------+
1 row in set 
```
