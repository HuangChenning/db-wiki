---
title: "Chapter 19 mysqlbackup commands"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/backup-commands.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

These are commands for the major operations for **mysqlbackup**. Only one of them can be specified for each **mysqlbackup** invocation, and, unlike the command options, the name of a command is not preceded by any dashes.

Each of these commands has its own set of required or allowed command options. For example, the `backup` command typically requires connection information to the database server. The `` `apply-log` `` and other commands that operate on the backup data after it is produced require the options that specify where the backup data is located.

The major groups of commands are: