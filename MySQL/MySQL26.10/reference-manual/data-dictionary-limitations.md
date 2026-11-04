---
title: "MySQL :: MySQL 26.10 Reference Manual :: 16.8 Data Dictionary Limitations"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/data-dictionary-limitations.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

## 16.8 Data Dictionary Limitations

This section describes temporary limitations introduced with the MySQL data dictionary.

- Manual creation of database directories under the data directory (for example, with **mkdir**) is unsupported. Manually created database directories are not recognized by the MySQL Server.
- DDL operations take longer due to writing to storage, undo logs, and redo logs instead of `.frm` files.