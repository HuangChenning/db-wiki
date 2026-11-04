---
title: "15.7.1 Account Management Statements"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/account-management-statements.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 15.7.1 Account Management Statements

MySQL account information is stored in the tables of the `mysql` system schema. This database and the access control system are discussed extensively in [Chapter 7, *MySQL Server Administration*](server-administration.md), which you should consult for additional details.

Important

Some MySQL releases introduce changes to the grant tables to add new privileges or features. To make sure that you can take advantage of any new capabilities, update your grant tables to the current structure whenever you upgrade MySQL. See [Chapter 3, *Upgrading MySQL*](upgrading.md).

When the [`read_only`](server-system-variables.md) system variable is enabled, account-management statements require the [`CONNECTION_ADMIN`](privileges-provided.md) privilege (or the deprecated [`SUPER`](privileges-provided.md) privilege), in addition to any other required privileges. This is because they modify tables in the `mysql` system schema.

Account management statements are atomic and crash safe. For more information, see [Section 15.1.1, “Atomic Data Definition Statement Support”](atomic-ddl.md).