---
title: VALIDATE_PASSWORD_STRENGTH
book: "SQL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005287557.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# VALIDATE_PASSWORD_STRENGTH

## 声明

```sql
VALIDATE_PASSWORD_STRENGTH(str)
```

## 说明

对指定的密码字符串，返回一个整数以指示密码的强度。返回值范围从 0（弱）到 100（强）。密码评估涉及的系统变量，可通过 `SHOW VARIABLES LIKE 'validate_password%';` 进行查看。

## 示例

```sql
obclient [test]> SELECT VALIDATE_PASSWORD_STRENGTH('ob$_@123');
+----------------------------------------------+
| VALIDATE_PASSWORD_STRENGTH('ob$_@123') |
+----------------------------------------------+
|                                          100 |
+----------------------------------------------+
1 row in set
```
