---
title: "11.1.6 Boolean Literals"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/boolean-literals.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

Skip to Main Content

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 11.1.6 Boolean Literals

The constants `TRUE` and `FALSE` evaluate to `1` and `0`, respectively. The constant names can be written in any lettercase.

```
mysql> SELECT TRUE, true, FALSE, false;
        -> 1, 1, 0, 0
```

[MySQL Documentation Library](https://docs.oracle.com/cd/E17952_01/index.html "Go to MySQL Doc Library")