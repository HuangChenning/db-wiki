---
title: "19.6 Other Operations"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/backup-commands-other.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

This group of operations consists of any **mysqlbackup** commands not covered in other sections of this chapter.

```
mysqlbackup --error-code=CODE print-message
```

`print-message`

Prints the associated exit message for a **mysqlbackup** exit code to the `stdout` stream.

Use the [`--error-code`](standard-options.md) option to supply the exit code for which you want to receive the associated exit message:

```
$ mysqlbackup print-message --error-code=4 2> /dev/null

One of the required files not found
```

For a list of **mysqlbackup** exit codes and messages, see [Section 17.1, “Exit codes of MySQL Enterprise Backup”](meb-exitcodes.md).