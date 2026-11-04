---
title: "13.7.1 Account Management Statements"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/account-management-statements.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 13.7.1 Account Management Statements

MySQL account information is stored in the tables of the `mysql` system database. This database and the access control system are discussed extensively in [Chapter 5, *MySQL Server Administration*](server-administration.md), which you should consult for additional details.

Important

Some MySQL releases introduce changes to the grant tables to add new privileges or features. To make sure that you can take advantage of any new capabilities, update your grant tables to the current structure whenever you upgrade MySQL. See [Section 2.10, “Upgrading MySQL”](upgrading.md).

When the [`read_only`](server-system-variables.md) system variable is enabled, account-management statements require the [`SUPER`](privileges-provided.md) privilege, in addition to any other required privileges. This is because they modify tables in the `mysql` system database.