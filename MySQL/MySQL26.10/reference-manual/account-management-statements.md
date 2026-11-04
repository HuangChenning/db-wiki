---
title: "MySQL :: MySQL 26.10 Reference Manual :: 15.7.1 Account Management Statements"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/account-management-statements.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 15.7.1 Account Management Statements

MySQL account information is stored in the tables of the `mysql` system schema. This database and the access control system are discussed extensively in [Chapter 7, *MySQL Server Administration*](server-administration.md), which you should consult for additional details.

Important

Some MySQL releases introduce changes to the grant tables to add new privileges or features. To make sure that you can take advantage of any new capabilities, update your grant tables to the current structure whenever you upgrade MySQL. See [Chapter 3, *Upgrading MySQL*](upgrading.md).

When the [`read_only`](server-system-variables.md) system variable is enabled, account-management statements require the [`CONNECTION_ADMIN`](privileges-provided.md) privilege (or the deprecated [`SUPER`](privileges-provided.md) privilege), in addition to any other required privileges. This is because they modify tables in the `mysql` system schema.

Account management statements are atomic and crash safe. For more information, see [Section 15.1.1, “Atomic Data Definition Statement Support”](atomic-ddl.md).