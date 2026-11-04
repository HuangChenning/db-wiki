---
title: Format of RMAN Commands
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmcomma003.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

The RMAN language is free-form. Keywords must be separated by at least one white space character (such as a space, tab, or line break). An RMAN command starts with a keyword corresponding to a command described in [Chapter 2, "RMAN Commands: @ (at sign) to QUIT"](rcmsynta.md), followed by arguments and ending with a semicolon, as shown in the syntax diagrams. The following example shows an RMAN backup command:

```
BACKUP DATABASE;
```

A command can span multiple lines. For example, you can rewrite each keyword in the preceding command on a separate line as follows:

```
BACKUP
  DATABASE
;
```

The maximum length for an RMAN command in a single line is 4000 characters. When a command exceeds this length, you can either split the command into multiple commands or use multiple lines for the command (use the Enter key to make the command span multiple lines). For example, if a `BACKUP` command that backs up multiple data files exceeds 4000 characters, then you can either split this command into two separate `BACKUP` commands or make the single `BACKUP` command span multiple lines.

You can insert a comment by using a pound (`#`) character at any point in a line. After the `#` character, the remainder of the line is ignored. For example:

```
# run this command once each day
BACKUP INCREMENTAL LEVEL 1 
  FOR RECOVER OF COPY      # using incrementally updated backups
  WITH TAG "DAILY_BACKUP"  # daily backup routine
  DATABASE;
```