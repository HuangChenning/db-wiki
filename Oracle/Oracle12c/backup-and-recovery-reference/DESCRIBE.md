---
title: Database Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: E85640-04
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/rcmrf/DESCRIBE.html
tags:
  - oracle
  - 12c
  - backup-and-recovery-reference
---

Purpose

Use the `DESCRIBE` command to list the column definitions of a table or view.

This command provides the functionality of the SQL\*Plus `DESCRIBE` command within RMAN.

Prerequisites

To access a table or view in another schema, you must have `READ` or `SELECT` privileges on the object or connect in `AS SYSDBA` mode. The `SYSBACKUP` privilege does not grant access to user tables or views.

Usage Notes

Descriptions provide this information for each column in the table or view:

- Name
- Whether null values are permitted (`NULL` or `NOT NULL`)
- Data type and, where applicable, the precision or scale

Syntax

describecmd::=

![describecmd](img/describecmd.gif)

> DESCRIBE \[CATALOG\] \[ schema.\] table \[@ dblink\]


Semantics

| Syntax Element | Description |
| --- | --- |
| `CATALOG` | Identifies the object as residing in the database containing the recovery catalog, |
| `schema` | Schema location of the table or view, required only when it is not in your login schema. |
| `table` | Name of a table or view. |
| `dblink` | Database link name for the database where the object exists, required only when it is not in the login database. |

Examples

This example describes the `V$CONTROLFILE` table:

```
RMAN> desc v$controlfile
 Name                                      Null?    Type
 ----------------------------------------- -------- ----------------------------
 STATUS                                             VARCHAR2(7)
 NAME                                               VARCHAR2(513)
 IS_RECOVERY_DEST_FILE                              VARCHAR2(3)
 BLOCK_SIZE                                         NUMBER
 FILE_SIZE_BLKS                                     NUMBER
 CON_ID                                             NUMBER
```