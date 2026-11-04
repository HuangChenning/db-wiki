---
title: "13.7.4 SET Statements"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/set-statement.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 13.7.4 SET Statements

The `SET` statement has several forms. Descriptions for those forms that are not associated with a specific server capability appear in subsections of this section:

- [``SET           *`var_name`* =           *`value`*``](set-variable.md) enables you to assign values to variables that affect the operation of the server or clients. See [Section 13.7.4.1, “SET Syntax for Variable Assignment”](set-variable.md).
- [`SET CHARACTER SET`](set-character-set.md) and [`SET NAMES`](set-names.md) assign values to character set and collation variables associated with the current connection to the server. See [Section 13.7.4.2, “SET CHARACTER SET Statement”](set-character-set.md), and [Section 13.7.4.3, “SET NAMES Statement”](set-names.md).

Descriptions for the other forms appear elsewhere, grouped with other statements related to the capability they help implement: