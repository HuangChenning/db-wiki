---
title: "10.8.2 COLLATE Clause Precedence"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/charset-collate-precedence.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

Skip to Main Content

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 10.8.2 COLLATE Clause Precedence

The `COLLATE` clause has high precedence (higher than [`||`](logical-operators.md)), so the following two expressions are equivalent:

```
x || y COLLATE z
x || (y COLLATE z)
```

[MySQL Documentation Library](https://docs.oracle.com/cd/E17952_01/index.html "Go to MySQL Doc Library")