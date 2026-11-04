---
title: "MySQL :: MySQL 26.7 Reference Manual :: 10.2 Optimizing SQL Statements"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/statement-optimization.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

## 10.2 Optimizing SQL Statements

The core logic of a database application is performed through SQL statements, whether issued directly through an interpreter or submitted behind the scenes through an API. The tuning guidelines in this section help to speed up all kinds of MySQL applications. The guidelines cover SQL operations that read and write data, the behind-the-scenes overhead for SQL operations in general, and operations used in specific scenarios such as database monitoring.