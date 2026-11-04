---
title: "10.2.5 Optimizing Data Change Statements"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/data-change-optimization.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 10.2.5 Optimizing Data Change Statements

This section explains how to speed up data change statements: [`INSERT`](insert.md), [`UPDATE`](update.md), and [`DELETE`](delete.md). Traditional OLTP applications and modern web applications typically do many small data change operations, where concurrency is vital. Data analysis and reporting applications typically run data change operations that affect many rows at once, where the main considerations is the I/O to write large amounts of data and keep indexes up-to-date. For inserting and updating large volumes of data (known in the industry as ETL, for “extract-transform-load”), sometimes you use other SQL statements or external commands, that mimic the effects of [`INSERT`](insert.md), [`UPDATE`](update.md), and [`DELETE`](delete.md) statements.