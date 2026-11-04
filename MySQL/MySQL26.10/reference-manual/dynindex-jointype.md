---
title: "MySQL :: MySQL 26.10 Reference Manual :: Join Types Index"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/dynindex-jointype.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

[Documentation Home](https://dev.mysql.com/doc/)

---

MySQL 26.10 Reference Manual

Related Documentation

[MySQL 26.10 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/26.10/en/)

Download this Manual

[PDF (US Ltr)](https://downloads.mysql.com/docs/refman-26.10-en.pdf) - 42.3Mb  
[PDF (A4)](https://downloads.mysql.com/docs/refman-26.10-en.a4.pdf) - 42.4Mb  
[Man Pages (TGZ)](https://downloads.mysql.com/docs/refman-26.10-en.man-gpl.tar.gz) - 272.9Kb  
[Man Pages (Zip)](https://downloads.mysql.com/docs/refman-26.10-en.man-gpl.zip) - 379.1Kb  
[Info (Gzip)](https://downloads.mysql.com/docs/mysql-26.10.info.gz) - 4.2Mb  
[Info (Zip)](https://downloads.mysql.com/docs/mysql-26.10.info.zip) - 4.2Mb

version 26.10

[26.7](https://dev.mysql.com/doc/refman/26.7/en/dynindex-jointype.html)  
[9.7 current](https://dev.mysql.com/doc/refman/9.7/en/dynindex-jointype.html)  
[8.4](https://dev.mysql.com/doc/refman/8.4/en/dynindex-jointype.html)  
[8.0](https://dev.mysql.com/doc/refman/8.0/en/dynindex-jointype.html)  

[8.0 Japanese](https://dev.mysql.com/doc/refman/8.0/ja/)

[MySQL 26.10 Reference Manual](https://dev.mysql.com/doc/refman/26.10/en/) / [Indexes](indexes.md) / Join Types Index

## Join Types Index

A | C | E | F | I | R | S | U

### A

\[index top\]

### ALL

[Section 10.2.1.23, “Avoiding Full Table Scans”](table-scan-avoidance.md)

[Section 10.2.1.12, “Block Nested-Loop and Batched Key Access Joins”](bnl-bka-optimization.md)

[Section 10.8.2, “EXPLAIN Output Format”](explain-output.md)

### C

\[index top\]

### const

[Section 10.8.2, “EXPLAIN Output Format”](explain-output.md)

[Section 10.8.3, “Extended EXPLAIN Output Format”](explain-extended.md)

[Section 25.4.3.9.2, “NDB Cluster System Variables”](mysql-cluster-options-variables.md)

[Section 10.9.3, “Optimizer Hints”](optimizer-hints.md)

[Section 10.2.1.16, “ORDER BY Optimization”](order-by-optimization.md)

[Section 10.2.1.2, “Range Optimization”](range-optimization.md)

[Section 15.2.13, “SELECT Statement”](select.md)

### E

\[index top\]

### eq\_ref

[Section 10.2.1.12, “Block Nested-Loop and Batched Key Access Joins”](bnl-bka-optimization.md)

[Section 10.8.2, “EXPLAIN Output Format”](explain-output.md)

[Section 10.2.1.6, “Index Condition Pushdown Optimization”](index-condition-pushdown-optimization.md)

[Section 18.7.1, “MERGE Table Advantages and Disadvantages”](merge-table-advantages.md)

[Section 25.4.3.9.2, “NDB Cluster System Variables”](mysql-cluster-options-variables.md)

[Section 10.2.2.3, “Optimizing Subqueries with the EXISTS Strategy”](subquery-optimization-with-exists.md)

[Section 29.12.4.1, “The events\_waits\_current Table”](performance-schema-events-waits-current-table.md)

### F

\[index top\]

### fulltext

[Section 10.8.2, “EXPLAIN Output Format”](explain-output.md)

### I

\[index top\]

### index

[Section 10.2.1.12, “Block Nested-Loop and Batched Key Access Joins”](bnl-bka-optimization.md)

[Section 10.8.2, “EXPLAIN Output Format”](explain-output.md)

### index\_merge

[Section 10.8.2, “EXPLAIN Output Format”](explain-output.md)

[Section 10.2.1.3, “Index Merge Optimization”](index-merge-optimization.md)

### index\_subquery

[Section 10.8.2, “EXPLAIN Output Format”](explain-output.md)

[Section 10.2.2.3, “Optimizing Subqueries with the EXISTS Strategy”](subquery-optimization-with-exists.md)

### R

\[index top\]

### range

[Section 10.2.1.12, “Block Nested-Loop and Batched Key Access Joins”](bnl-bka-optimization.md)

[Section 10.8.2, “EXPLAIN Output Format”](explain-output.md)

[Section 10.2.1.17, “GROUP BY Optimization”](group-by-optimization.md)

[Section 10.2.1.6, “Index Condition Pushdown Optimization”](index-condition-pushdown-optimization.md)

[Section 10.2.1.3, “Index Merge Optimization”](index-merge-optimization.md)

[Section 10.9.3, “Optimizer Hints”](optimizer-hints.md)

[Section 10.2.1.2, “Range Optimization”](range-optimization.md)

### ref

[Section 10.2.1.12, “Block Nested-Loop and Batched Key Access Joins”](bnl-bka-optimization.md)

[Section 10.8.2, “EXPLAIN Output Format”](explain-output.md)

[Section 10.8.3, “Extended EXPLAIN Output Format”](explain-extended.md)

[Section 10.2.1.6, “Index Condition Pushdown Optimization”](index-condition-pushdown-optimization.md)

[Section 10.3.8, “InnoDB and MyISAM Index Statistics Collection”](index-statistics.md)

[Section 18.7.1, “MERGE Table Advantages and Disadvantages”](merge-table-advantages.md)

[Section 25.4.3.9.2, “NDB Cluster System Variables”](mysql-cluster-options-variables.md)

[Section 10.9.3, “Optimizer Hints”](optimizer-hints.md)

[Section 10.2.2.4, “Optimizing Derived Tables, View References, and Common Table Expressions with Merging or Materialization”](derived-table-optimization.md)

[Section 10.2.2.3, “Optimizing Subqueries with the EXISTS Strategy”](subquery-optimization-with-exists.md)

### ref\_or\_null

[Section 10.8.2, “EXPLAIN Output Format”](explain-output.md)

[Section 10.2.1.6, “Index Condition Pushdown Optimization”](index-condition-pushdown-optimization.md)

[Section 10.2.1.15, “IS NULL Optimization”](is-null-optimization.md)

[Section 10.2.2.3, “Optimizing Subqueries with the EXISTS Strategy”](subquery-optimization-with-exists.md)

### S

\[index top\]

### system

[Section 10.8.2, “EXPLAIN Output Format”](explain-output.md)

[Section 10.8.3, “Extended EXPLAIN Output Format”](explain-extended.md)

[Section 10.2.1.2, “Range Optimization”](range-optimization.md)

[Section 15.2.13, “SELECT Statement”](select.md)

### U

\[index top\]

### unique\_subquery

[Section 10.8.2, “EXPLAIN Output Format”](explain-output.md)

[Section 10.2.2.3, “Optimizing Subqueries with the EXISTS Strategy”](subquery-optimization-with-exists.md)

[PREV](dynindex-is.md) [HOME](index.md) [UP](indexes.md) [NEXT](dynindex-operator.md)

Related Documentation

[MySQL 26.10 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/26.10/en/)

Download this Manual

[PDF (US Ltr)](https://downloads.mysql.com/docs/refman-26.10-en.pdf) - 42.3Mb  
[PDF (A4)](https://downloads.mysql.com/docs/refman-26.10-en.a4.pdf) - 42.4Mb  
[Man Pages (TGZ)](https://downloads.mysql.com/docs/refman-26.10-en.man-gpl.tar.gz) - 272.9Kb  
[Man Pages (Zip)](https://downloads.mysql.com/docs/refman-26.10-en.man-gpl.zip) - 379.1Kb  
[Info (Gzip)](https://downloads.mysql.com/docs/mysql-26.10.info.gz) - 4.2Mb  
[Info (Zip)](https://downloads.mysql.com/docs/mysql-26.10.info.zip) - 4.2Mb