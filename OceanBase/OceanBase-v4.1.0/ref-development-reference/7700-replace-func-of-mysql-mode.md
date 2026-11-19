---
title: REPLACE
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000001964944.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# REPLACE

## 声明

```sql
REPLACE(str, from_str, to_str)
```

## 说明

返回字符串 `str` 以及所有被字符 `to_str` 替代的字符串 `from_str`。

该函数是多字节安全的。

## 示例

```sql
obclient> SELECT REPLACE('abc.efg.gpg.nowdew.abc.dabc.e', 'abc.', 'www');
+---------------------------------------------------------+
| REPLACE('abc.efg.gpg.nowdew.abc.dabc.e', 'abc.', 'www') |
+---------------------------------------------------------+
| wwwefg.gpg.nowdew.wwwdwwwe                              |
+---------------------------------------------------------+
1 row in set 
```
