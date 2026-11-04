---
title: DBMS_FLASHBACK_ARCHIVE
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_flashb_archive.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 70 DBMS\_FLASHBACK\_ARCHIVE

The `DBMS_FLASHBACK_ARCHIVE` package contains two simple procedures for disassociation and reassociation of a Flashback Data Archive (FDA) enabled table from/with its underlying FDA respectively.

See Also:

Oracle Database Advanced Application Developer's Guide

This chapter contains the following topics:

- Using DBMS\_FLASHBACK\_ARCHIVE
- Summary of DBMS\_FLASHBACK\_ARCHIVE Subprograms

---

## Using DBMS\_FLASHBACK\_ARCHIVE

---

### Overview

The Flashback Data Archive feature, which is available through the Total Recall option, provides strict protection on the internal history tables that it creates and maintains for users.

The read-only semantics provided prohibits users, including a DBA, from doing updates, deletes, and inserts on the Flashback Data Archive internal history tables. The feature also prohibits users from issuing any DDL statements on these tables. This strict security enforcement by Flashback Data Archive meets the requirements of regulatory-compliance type of applications. The feature supports a lot of common DDL statements, including some DDL statements that alter table definition or incur data movement, on user tables that are enabled for Flashback Data Archive. However, there are some DDL statements that are not supported on tables enabled for the feature. Since most applications schemas evolve as they release new versions of their software, the ability to perform DDL operations on the base table is a key customer requirement.

In order to support user applications' schema evolution during application upgrade and other table maintenance tasks beyond DDL statements supported by Flashback Data Archive, the `DBMS_FLASHBACK_ARCHIVE` package provides a set of simple-to-use PL/SQL procedures:

- To disassociate a Flashback Data Archive enabled base table from the underlying FDA.
- To reassociate a temporarily disassociated base table with its underlying FDA.

After a user has disassociated the base table from its FDA, it's possible to issue any DDL statements on the base table or the history tables in the FDA. Having finished with the schema changes, the user can then reassociate the base table with its FDA so that Flashback Data Archive protection is in operation and automatic tracking and archiving is resumed.

---

### Security Model

Users with `the FLASHBACK` `ARCHIVE` `ADMINISTER` system privilege can execute the disassociation and reassociation PL/SQL procedures. Once a table is disassociated, normal users can perform DDL and DML statements as long as they have the necessary privileges on the tables.

---

### Examples

Normally, users cannot perform any modification to the history table:

```
SQL> DELETE FROM scott.SYS_FBA_HIST_61527;

ERROR at line 1: 
ORA-55622: DML, ALTER and CREATE UNIQUE INDEX operations are not allowed on table "SCOTT"."SYS_FBA_HIST_61527"
```

Users also cannot issue DDL statements on history tables:

```
SQL> ALTER TABLE scott.SYS_FBA_HIST_61527 DROP COLUMN comm;

ERROR at line 1: 
ORA-55622: DML, ALTER and CREATE UNIQUE INDEX operations are not allowed on table "SCOTT"."SYS_FBA_HIST_61527"
```

Use the DISASSOCIATE\_FBA Procedure to disassociate the `scott`.`emp_test` table:

```
SQL> EXEC DBMS_FLASHBACK_ARCHIVE.DISASSOCIATE_FBA('scott','emp_test');

PL/SQL procedure successfully completed.
```

Now a user can perform table structural modifications (through DDL statements) to the user base table:

```
SQL> ALTER TABLE scott.emp_test RENAME COLUMN sal TO salary;

Table altered.
```

Users can also modify the contents in the history table that they couldn't modify previously.

```
SQL> DELETE FROM scott.SYS_FBA_HIST_61527 WHERE empno=3968;

2 rows deleted.
```

If a user tries to reassociate the history table with the base table, this will fail as the user has not performed corresponding structural modifications (through DDL statements) to the history table:

```
SQL> EXEC DBMS_FLASHBACK_ARCHIVE.REASSOCIATE_FBA('scott','emp_test');
BEGIN DBMS_FLASHBACK_ARCHIVE.REASSOCIATE_FBA('scott','emp_test');
END;

ERROR at line 1:
ORA-55636: Flashback Data Archive enabled table "SCOTT"."EMP_TEST" has different definition from its history table
ORA-06512: at "SYS.DBMS_FLASHBACK_ARCHIVE", line 17
ORA-06512: at line 1
```

Disassociate the table and fix the table definition problem:

```
SQL> EXEC DBMS_FLASHBACK_ARCHIVE.DISASSOCIATE_FBA('scott','emp_test');

PL/SQL procedure successfully completed.
```

Perform the same rename column DDL on the history table to make its definition conform to its base table `scott`.`emp_test`:

```
SQL> ALTER TABLE scott.SYS_FBA_HIST_61527 RENAME COLUMN sal TO salary;

Table altered.
```

Finally, reassociate the base table with its history table successfully:

```
SQL> EXEC DBMS_FLASHBACK_ARCHIVE.REASSOCIATE_FBA('scott','emp_test')

PL/SQL procedure successfully completed.
```

The above example is used as an illustration. `RENAME COLUMN` is available as a supported DDL and you do not need to invoke disassociate/reassociate as a matter of course. You need to disasociate/reassociate only if the operation is not supported by flashback archive and produces a `55610` error message.

```
SQL> create table emp_test as select empno, sal from emp;
```

Table created.

```
SQL> alter table emp_test flashback archive;
```

Table altered.

Create a temporary history table with the same form as the base table but with the additional metadata columns.

```
SQL>  EXEC DBMS_FLASHBACK_ARCHIVE.CREATE_TEMP_HISTORY_TABLE('scott','emp_test');
```

PL/SQL procedure successfully completed.

```
SQL> describe scott.temp_history
 Name                                      Null?    Type
 ----------------------------------------- -------- ----------------------------
 RID                                                VARCHAR2(4000)
 STARTSCN                                           NUMBER
 ENDSCN                                             NUMBER
 XID                                                RAW(8)
 OPERATION                                          VARCHAR2(1)
 EMPNO                                              NUMBER(4)
 SAL                                                NUMBER(7,2)
```

Do the following once per database. This will extend mappings to the past so that import of old history can be done. Goes back to 01-JAN-88.

```
SQL> EXEC DBMS_FLASHBACK_ARCHIVE.extend_mappings();
```

PL/SQL procedure successfully completed.

```
SQL> insert into scott.temp_history values (NULL, timestamp_to_scn(to_date('01-JAN-06')), timestamp_to_scn(to_date('31-DEC-06')), NULL, 'U', 1, 1000);
```

1 row created.

```
SQL> commit;
```

Commit complete.

```
SQL> EXEC DBMS_FLASHBACK_ARCHIVE.IMPORT_HISTORY('scott','emp_test');
```

PL/SQL procedure successfully completed.

Now flashback queries of the imported data are possible.

```
SQL> select * from scott.emp_test as of timestamp to_date('06-JUN-06') where empno=1;
 
     EMPNO        SAL                                                          
---------- ----------                                                          
         1       1000
```

---

## Summary of DBMS\_FLASHBACK\_ARCHIVE Subprograms

Table 70-1 DBMS\_FLASHBACK\_ARCHIVE Package Subprograms

| Subprogram | Description |
| --- | --- |
| DISASSOCIATE\_FBA Procedure | Disassociates the given table from the flashback data archive |
| REASSOCIATE\_FBA Procedure | Reassociates the given table with the flashback data archive |

---

### DISASSOCIATE\_FBA Procedure

This procedure disassociates the given table from the flashback data archive.

Syntax

```
DBMS_FLASHBACK_ARCHIVE.DISASSOCIATE_FBA (
   owner_name      VARCHAR2, 
   table_name      VARCHAR2);
```

Parameters

Table 70-2 DISASSOCIATE\_FBA Procedure Parameters

| Parameter | Description |
| --- | --- |
| `owner_name` | Schema of the Flashback Data Archive enabled base table |
| `table_name` | Name of the Flashback Data Archive enabled base table |

Exceptions

Table 70-3 DISASSOCIATE\_FBA Procedure Exceptions

| Parameter | Description |
| --- | --- |
| `ORA-55602` | User table is not enabled for Flashback Data Archive |
| `ORA-55634` | Cannot acquire the lock on the table for disassociation |

---

### REASSOCIATE\_FBA Procedure

This procedure reassociates the given table with the flashback data archive.

Syntax

```
DBMS_FLASHBACK_ARCHIVE.REASSOCIATE_FBA (
   owner_name      VARCHAR2, 
   table_name      VARCHAR2);
```

Parameters

Table 70-4 REASSOCIATE\_FBA Procedure Parameters

| Parameter | Description |
| --- | --- |
| `owner_name` | Schema of the Flashback Data Archive enabled base table |
| `table_name` | Name of the Flashback Data Archive enabled base table |

Exceptions

Table 70-5 REASSOCIATE\_FBA Procedure Exceptions

| Parameter | Description |
| --- | --- |
| `ORA-55602` | User table is not enabled for Flashback Data Archive |
| `ORA-55636` | table definition validation failed |

Usage Notes

- The procedure will signal an error if the base table and the history table do not have identical data definitions. For example when columns are added or table is split, the resulting base table and history table need to have the same schema.
- The FDA internal history table schema has some row versions metadata columns. The procedure will signal an error if any of the metadata columns is dropped by users.