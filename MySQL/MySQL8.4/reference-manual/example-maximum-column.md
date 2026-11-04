---
title: "5.6.1 The Maximum Value for a Column"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/example-maximum-column.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

Skip to Main Content

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 5.6.1 The Maximum Value for a Column

“What is the highest item number?”

```
SELECT MAX(article) AS article FROM shop;

+---------+
| article |
+---------+
|       4 |
+---------+
```

[MySQL Documentation Library](https://docs.oracle.com/cd/E17952_01/index.html "Go to MySQL Doc Library")