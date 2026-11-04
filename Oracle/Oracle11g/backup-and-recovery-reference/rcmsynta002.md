---
title: "@@ (double at sign)"
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta002.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

Purpose

Use the `@@` command to execute a series of RMAN commands stored in an operating system file with the specified file name.

If `@@` is contained in a command file, then `@@` `filename` directs RMAN to look for the specified file name in the same directory as the command file from which it was called. If not used within a command file, the `@@` command is identical to the `@ (at sign)` command.

Prerequisites

The command file must contain complete RMAN commands.

Usage Notes

The command file is local to the RMAN client. The name resolution of the file is dependent on the operating system. For example, `@tmp/cmd1.rman` in UNIX or Windows means that `tmp` is a subdirectory of the current directory and that the file `cmd1.rman` is in this subdirectory.

To illustrate the differences between the `@` and `@@` commands, assume that you invoke RMAN as follows:

```
% rman TARGET /
RMAN> @/tmp/cmd1.rman
```

Assume that the command `@@cmd2.rman` appears inside the `cmd1.rman` script. In this case, the `@@` command directs RMAN to search for the file `cmd2.rman` in the directory `/tmp`.

As with the `@` command, you can specify substitution variables in a command file and then pass values to the command file during execution of `@@` (see Example 2-4).

Syntax

@@::=

  
[Description of the illustration atat.gif](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/img_text/atat.htm)  

Semantics

| Syntax Element | Description |
| --- | --- |
| `filename` | Specifies the name of a command file, for example, `@@cmd2.rman`. |

Example

Example 2-4 Calling a Command File Within Another Command File

The following operating system commands create command files `backup_logs.rman` and `backup_db.rman`:

```
% echo "BACKUP ARCHIVELOG ALL;" > /tmp/bkup_logs.rman
% echo "BACKUP TAG &1 DATABASE;" > /tmp/bkup_db.rman
% echo "@@bkup_logs.rman" >> /tmp/bkup_db.rman
```

The following example starts RMAN from the command line and connects to the target database with operating system authentication. The `@` command executes `bkup_db.rman`, which contains the command `@@bkup_logs.rman`. The `@@` command specifies that RMAN should look for the `bkup_logs.rman` script in the same directory in which `bkup_db.rman` is located. The example uses a substitution variable to specify the tag `WHOLE_DB` for the database backup.

```
% rman TARGET /
RMAN> @/tmp/bkup_db.rman whole_db
```