---
title: "15.3 Transactional and Locking Statements"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/sql-transactional-statements.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

MySQL supports local transactions (within a given client session) through statements such as [`SET autocommit`](commit.md), [`START TRANSACTION`](commit.md), [`COMMIT`](commit.md), and [`ROLLBACK`](commit.md). See [Section 15.3.1, “START TRANSACTION, COMMIT, and ROLLBACK Statements”](commit.md). XA transaction support enables MySQL to participate in distributed transactions as well. See [Section 15.3.8, “XA Transactions”](xa.md).