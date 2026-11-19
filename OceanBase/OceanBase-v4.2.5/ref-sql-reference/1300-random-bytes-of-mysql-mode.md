---
title: RANDOM_BYTES
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001504315.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# RANDOM_BYTES

## 声明

```sql
RANDOM_BYTES(len)
```

## 说明

返回 len 字节长度的随机二进制字符串，长度 len 的合法取值为 [1~1024]。

## 示例

```sql
obclient [test]> select RANDOM_BYTES(2);
+-----------------+
| RANDOM_BYTES(2) |
+-----------------+
| H              |
+-----------------+
1 row in set
```
