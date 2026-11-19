---
title: ITERATE
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502954.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# ITERATE

| Description   |                 |
|---------------|-----------------|
| keywords      |                 |
| dir-name      |                 |
| dir-name-en   |                 |
| tenant-type   | MySQL Mode      |
|machine-translation|en,ja-marker|
|slug|iterate-mysql-compatible-mode|

# ITERATE 


`ITERATE` 语句用于再次启动循环语句。

`ITERATE` 语句的语法如下：

```sql
ITERATE label
```

`ITERATE` 只能出现在 `LOOP`、`REPEAT` 和 `WHILE` 语句中。
