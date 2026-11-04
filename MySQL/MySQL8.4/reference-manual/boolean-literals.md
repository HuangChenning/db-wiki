---
title: "11.1.6 Boolean Literals"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/boolean-literals.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

Skip to Main Content

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 11.1.6 Boolean Literals

The constants `TRUE` and `FALSE` evaluate to `1` and `0`, respectively. The constant names can be written in any lettercase.

```
mysql> SELECT TRUE, true, FALSE, false;
        -> 1, 1, 0, 0
```

[MySQL Documentation Library](https://docs.oracle.com/cd/E17952_01/index.html "Go to MySQL Doc Library")