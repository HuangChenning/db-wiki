---
title: RANDOM_BYTES
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699908.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
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
