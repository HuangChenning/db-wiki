---
title: CREATE SCRIPT
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta014.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

Purpose

Use the `CREATE SCRIPT` command to create a stored script in the recovery catalog. A stored script is a sequence of RMAN commands that is given a name and stored in the recovery catalog for later execution.

See Also:

- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmcatdb.htm#BRADV182) to learn how to use stored scripts
- `REPLACE SCRIPT` to learn how to update a stored script

Prerequisites

Execute `CREATE SCRIPT` only at the RMAN prompt. RMAN must be connected to a target database and a recovery catalog. The recovery catalog database must be open.

If `GLOBAL` is specified, then a global script with this name must not exist in the recovery catalog. If `GLOBAL` is not specified, then a local script must not exist with the same name for the same target database. In you do not meet these prerequisites, then RMAN returns error `RMAN-20401`.

Usage Notes

A stored script may be local or global. A local script is created for the current target database only, whereas a global script is available for use with any database registered in the recovery catalog.

It is permissible to create a global script with the same name as a local script, or a local script with the same name as a global script.

Substitution Variables in Stored Scripts

RMAN supports the use of substitution variables in a stored script. `&1` indicates where to place the first value, `&2` indicate where to place the second value, and so on. Special characters must be quoted.

The substitution variable syntax is `&` `integer` followed by an optional period, for example, `&1.3`. The optional period is part of the variable and replaced with the value, thus enabling the substitution text to be immediately followed by another integer. For example, if you pass the value `mybackup` to a command file that contains the substitution variable `&1.3`, then the result of the substitution is `mybackup3`. To create the result `mybackup.3`, you use the syntax `&1..3`.

When you create a stored script with substitution variables, you must provide example values at create time. You can provide these values with the `USING` clause when starting RMAN (see `RMAN`) or enter them when prompted (see Example 2-62).

Semantics

| Syntax Element | Description |
| --- | --- |
| `GLOBAL` | Identifies the script as global.  Note: A virtual private catalog has read-only access to global scripts. Creating or updating global scripts must be done while connected to the base recovery catalog. |
| `SCRIPT` `script_name` | Specifies the name of the script. Quotes must be used around the script name when the name contains either spaces or reserved words. |
| `   COMMENT` `'` `comment` `'` | Associates an explanatory comment with the stored script in the recovery catalog. The comment is used in the output of `LIST` `SCRIPT NAMES`. |
| `backupCommands`  `maintenanceCommands`  `miscellaneousCommands`  `restoreCommands` | Specifies commands to include in the stored script. The commands allowable within the brackets of the `CREATE SCRIPT` `'` `script_name` `'` `{``...``}` command are the same commands supported within a `RUN` command. Any command that is valid within a `RUN` command is permitted in the stored script. The following commands are not valid within stored scripts: `RUN`, `@ (at sign)`, and `@@ (double at sign)`. |
| `FROM FILE '` `filename` `'` | Reads the sequence of commands to define the script from the specified file.  The file should look like the body of a valid stored script. The first line of the file must be a left brace (`{`) and the last line must contain a right brace (`}`). The RMAN commands in the file must be valid in a stored script. |

Examples

Example 2-60 Creating a Local Stored Script

Assume that you want to create a local stored script for backing up database `prod`. You start RMAN, connect to `prod` as `TARGET`, and connect to a recovery catalog. You create a stored script called `backup_whole` and then use `EXECUTE SCRIPT` to run it as follows:

```
CREATE SCRIPT backup_whole 
COMMENT "backup whole database and archived redo log files"
{
    BACKUP 
      INCREMENTAL LEVEL 0 TAG backup_whole
      FORMAT "/disk2/backup/%U"
      DATABASE PLUS ARCHIVELOG;
}
RUN { EXECUTE SCRIPT backup_whole; }
```

Example 2-61 Creating a Global Stored Script

This example connects RMAN to target database `prod` and recovery catalog database `catdb` as catalog user `rco`. The example creates a global script called `global_backup_db` that backs up the database and archived redo log files:

```
RMAN> CONNECT TARGET SYS@prod

target database Password: password
connected to target database: PROD (DBID=39525561)

RMAN> CONNECT CATALOG rco@catdb

recovery catalog database Password: password
connected to recovery catalog database

RMAN> CREATE GLOBAL SCRIPT global_backup_db { BACKUP DATABASE PLUS ARCHIVELOG; }
RMAN> EXIT;
```

You can now connect RMAN to a different target database such as `prod2` and run the global stored script:

```
RMAN> CONNECT TARGET SYS@prod2

target database Password: password
connected to target database: PROD2 (DBID=36508508)

RMAN> CONNECT CATALOG rco@catdb

recovery catalog database Password: password
connected to recovery catalog database

RMAN> RUN { EXECUTE SCRIPT global_backup_db; }
```

Example 2-62 Creating a Stored Script That Uses Substitution Variables

The following example connects RMAN to a target database and recovery catalog and uses `CREATE SCRIPT` to create a backup script that includes three substitution variables. RMAN prompts you to enter initial values for the variables (user input is shown in bold).

```
RMAN> CONNECT TARGET /
RMAN> CONNECT CATALOG rman@catdb

recovery catalog database Password: password
connected to recovery catalog database

RMAN> CREATE SCRIPT backup_df 
2> { BACKUP DATAFILE &1 TAG &2.1 FORMAT '/disk1/&3_%U'; }
 Enter value for 1: 1
 
Enter value for 2: df1_backup
 
Enter value for 3: df1

starting full resync of recovery catalog
full resync complete
created script backup_df
```

When you run `EXECUTE SCRIPT`, you can pass different values to the script. The following example passes the values `3`, `test_backup`, and `test` to the substitution variables in the stored script:

```
RMAN> RUN { EXECUTE SCRIPT backup_df USING 3 test_backup df3; }
```

After the values are substituted, the script executes as follows:

```
BACKUP DATAFILE 3 TAG test_backup1 FORMAT '/disk1/df3_%U';
```