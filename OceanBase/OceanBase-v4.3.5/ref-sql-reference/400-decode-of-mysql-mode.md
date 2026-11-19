---
title: DECODE
book: "SQL 参考"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002017653.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# DECODE

## 声明

```sql
DECODE(crypt_str,pass_str)
```

## 说明

`DECODE()` 使用 `pass_str` 作为密码对加密的字符串 `crypt_str` 进行解密并返回解密后的字符串。

## 示例

```sql
obclient> SELECT DECODE(ENCODE('secret','cry'), 'cry');
+---------------------------------------+
| DECODE(ENCODE('secret','cry'), 'cry') |
+---------------------------------------+
| secret                                |
+---------------------------------------+
1 row in set
```
