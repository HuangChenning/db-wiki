---
title: "空值条件"
book: "SQL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000006306459.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# 空值条件

空值条件（Null Condition）用于检测 NULL 值。

## 语法

```sql
expr IS [ NOT ] NULL
```

## 使用说明

* `IS NULL` 用于检测表达式是否为 NULL，如果为 NULL 则返回 TRUE，否则返回 FALSE。
* `IS NOT NULL` 用于检测表达式是否不为 NULL，如果不为 NULL 则返回 TRUE，否则返回 FALSE。

## 示例

```sql
obclient> CREATE TABLE emp (
  empno INT,
  last_name VARCHAR(20),
  comm_pct DECIMAL(5, 2)
);
obclient> INSERT INTO emp VALUES
  (1, 'Smith', NULL),
  (2, 'Jones', 0.10);

obclient> SELECT last_name FROM emp WHERE comm_pct IS NULL ORDER BY last_name;
```
