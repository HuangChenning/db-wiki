---
title: "4.3.7 Making a Back Up of In-Memory Database Data"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/exec-option.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

### 4.3.7 Making a Back Up of In-Memory Database Data

The [`--exec-when-locked`](backup-special-options.md) option of **mysqlbackup** lets you specify a command (together with the desired command arguments) to run near the end of the backup while the database's non-InnoDB tables are still locked. This command can copy or create additional files in the backup directory. For example, you can use this option to back up `MEMORY` tables with the **mysqldump** command, storing the output in the backup directory. To delay any redirection or variable substitution until the command is executed, enclose the entire option value within single quotes.