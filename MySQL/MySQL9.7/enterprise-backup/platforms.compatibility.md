---
title: "C.2 Cross-Platform Compatibility"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/platforms.compatibility.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

MySQL Enterprise Backup is by nature cross-platform compatible when running on the Linux and Windows operating systems: backups on a Linux machine can, in principle, be restored on a Windows machine, and vice versa. However, because [Identifier Case Sensitivity](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/identifier-case-sensitivity.html) is dependent on the case sensitivity of the underlying operating system (which varies across platforms), data transfer problems might occur due to letter case issues with the database or table names. Therefore, to ensure cross-platform compatibility, the following two conditions must be fulfilled:

- Both the backed-up and the restored servers have [`lower_case_table_names`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/server-system-variables.html#sysvar_lower_case_table_names) =1 (which means both servers were initialized with that setting, as [`lower_case_table_names`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/server-system-variables.html#sysvar_lower_case_table_names) cannot be changed after server initialization), so that all table and database names are stored in lowercase on disk and name comparisons are not case-sensitive.
- All applications that connect to the backed-up and the restored servers are always consistent on their use of letter cases when referring to the database and table names.

Warning

Meeting these conditions does not guarantee cross-platform compatibility. Users should perform tests on their systems to make sure cross-platform restores work as desired.