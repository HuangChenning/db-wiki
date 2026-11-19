---
title: REMOVE_RULE
book: "PL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005286812.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# REMOVE_RULE

`REMOVE_RULE` 过程用于删除自定义改写规则。

## 语法

```sql
PROCEDURE REMOVE_RULE (
    rule_name          VARCHAR(256));
```

## 参数说明

| 参数 | 描述 |
| --- | --- |
| rule_name | 规则名称。 |

## 示例

```shell
obclient> CALL DBMS_UDR.REMOVE_RULE('rule1');
Query OK, 0 rows affected

obclient> SELECT DB_NAME, RULE_NAME, PATTERN, REPLACEMENT, NORMALIZED_PATTERN, STATUS, PATTERN_DIGEST
    FROM oceanbase.DBA_OB_USER_DEFINED_RULES;
Empty set
```
