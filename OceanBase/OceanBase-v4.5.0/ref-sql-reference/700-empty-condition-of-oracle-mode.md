---
title: "空条件"
book: "SQL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004479752.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# 空条件

空条件（Null Condition）可以检测 NULL 值，是用于检测 NULL 的唯一条件。

## 空条件语法

空条件语法如下：

```sql
expr IS [ NOT ] NULL
```

有关空值的详细信息，请参见 [空值](../300.basic-elements-of-oracle-mode/500.null-of-oracle-mode/100.empty-value-overview-of-oracle-mode.md)。

## 示例

```sql
SELECT last_name FROM emp WHERE comm_pct IS NULL ORDER BY last_name;
```
