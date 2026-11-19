---
title: OB_VERSION
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702831.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# OB_VERSION

## 声明

```sql
OB_VERSION()
```

## 说明

返回当前 OceanBase 数据库的版本信息，字符集为 utf8mb4。

## 示例

```sql
obclient> SELECT OB_VERSION() FROM DUAL;
+--------------+
| OB_VERSION() |
+--------------+
| 4.0.0.0      |
+--------------+
1 row in set
```
