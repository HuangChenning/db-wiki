---
title: ENABLE_RULE
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699743.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# ENABLE_RULE

`ENABLE_RULE` 过程用于开启自定义改写规则，让自定义改写规则生效。

  <main id="notice" >
    <h4>功能适用性</h4>
    <p>该内容仅适用于 OceanBase 数据库企业版。OceanBase 数据库社区版仅提供 MySQL 模式。</p>
  </main>

## 语法

```sql
PROCEDURE ENABLE_RULE (
    rule_name          VARCHAR(256));
```

## 参数说明

| 参数 | 描述 |
| --- | --- |
| rule_name | 规则名称。 |

## 示例

```shell
obclient> CALL DBMS_UDR.ENABLE_RULE('rule1');
Query OK, 0 rows affected 

obclient> SELECT 1 FROM DUAL;
+-------+
| ? + 1 |
+-------+
|     2 |
+-------+
1 row in set
```
