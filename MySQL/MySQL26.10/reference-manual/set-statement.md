---
title: "MySQL :: MySQL 26.10 Reference Manual :: 15.7.6 SET Statements"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/set-statement.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 15.7.6 SET Statements

The `SET` statement has several forms. Descriptions for those forms that are not associated with a specific server capability appear in subsections of this section:

- [``SET           *`var_name`* =           *`value`*``](set-variable.md) enables you to assign values to variables that affect the operation of the server or clients. See [Section 15.7.6.1, “SET Syntax for Variable Assignment”](set-variable.md).
- [`SET CHARACTER SET`](set-character-set.md) and [`SET NAMES`](set-names.md) assign values to character set and collation variables associated with the current connection to the server. See [Section 15.7.6.2, “SET CHARACTER SET Statement”](set-character-set.md), and [Section 15.7.6.3, “SET NAMES Statement”](set-names.md).

Descriptions for the other forms appear elsewhere, grouped with other statements related to the capability they help implement:

- [`SET DEFAULT ROLE`](set-default-role.md) and [`SET ROLE`](set-role.md) set the default role and current role for user accounts. See [Section 15.7.1.9, “SET DEFAULT ROLE Statement”](set-default-role.md), and [Section 15.7.1.11, “SET ROLE Statement”](set-role.md).
- [`SET PASSWORD`](set-password.md) assigns account passwords. See [Section 15.7.1.10, “SET PASSWORD Statement”](set-password.md).
- `SET RESOURCE GROUP` assigns threads to a resource group. See [Section 15.7.2.4, “SET RESOURCE GROUP Statement”](set-resource-group.md).
- [`SET           TRANSACTION ISOLATION LEVEL`](set-transaction.md) sets the isolation level for transaction processing. See [Section 15.3.7, “SET TRANSACTION Statement”](set-transaction.md).