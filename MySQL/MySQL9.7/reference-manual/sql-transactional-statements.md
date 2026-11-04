---
title: "15.3 Transactional and Locking Statements"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/sql-transactional-statements.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

MySQL supports local transactions (within a given client session) through statements such as [`SET autocommit`](commit.md), [`START TRANSACTION`](commit.md), [`COMMIT`](commit.md), and [`ROLLBACK`](commit.md). See [Section 15.3.1, “START TRANSACTION, COMMIT, and ROLLBACK Statements”](commit.md). XA transaction support enables MySQL to participate in distributed transactions as well. See [Section 15.3.8, “XA Transactions”](xa.md).