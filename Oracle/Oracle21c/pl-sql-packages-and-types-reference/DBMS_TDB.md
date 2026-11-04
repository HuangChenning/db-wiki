---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_TDB.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 181 DBMS\_TDB

The `DBMS_TDB` package reports whether a database can be transported between platforms using the RMAN `CONVERT DATABASE` command.

The package verifies that databases on the current host platform are of the same endian format as the destination platform, and that the state of the current database does not prevent transport of the database.

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=SQLRF009) regarding database transport using `CONVERT DATABASE`

This chapter contains the following topics:

### 181.1 DBMS\_TDB Overview

In many cases, Oracle supports transporting databases between platforms which have the same endian format. However, even when the endian formats are the same, a database must undergo a conversion process to move from one platform to another. There are also preconditions required for the process of transporting a database, such as having the database to be transported open read-only.

The `DBMS_TDB` package serves two purposes:

- Confirming that Oracle supports transporting a database from a given source platform to a given target platform
- Determining whether a database to be transported has been properly prepared for transport, and if not, identifying the condition that prevents database transport

The actual conversion is performed using the Recovery Manager `CONVERT DATABASE` command. For a complete discussion of the requirements for transporting a database, the process of converting a database for transport across platforms, and examples of the use of the `DBMS_TDB` subprograms in the conversion process, see [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=SQLRF009).

### 181.2 DBMS\_TDB Security Model

Use of this package requires the `DBA` privilege.

### 181.3 DBMS\_TDB Constants

The `DBMS_TDB` package defines several enumerated constants that should be used for specifying parameter values. Enumerated constants must be prefixed with the package name, for example, `DBMS_TDB.SKIP_NONE`.

The `DBMS_TDB` package uses the constants shown in Table 181-1.

Table 181-1 DBMS\_TDB Constants

| Name | Type | Value | Description |
| --- | --- | --- | --- |
| `SKIP_NONE` | `NUMBER` | `0` | Check all files when checking whether a database is ready for transport. |
| `SKIP_OFFLINE` | `NUMBER` | `2` | Skip files in offline tablespaces when checking whether a database is ready for transport. |
| `SKIP_READONLY` | `NUMBER` | `3` | Skip files in read-only tablespaces when checking whether a database is ready for transport. |

### 181.4 DBMS\_TDB Views

The `DBMS_TDB` package uses the `V$DB_TRANSPORTABLE_PLATFORM` view.

This view is described in [Oracle Database Reference.](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=REFRN30376)

- [`V$DB_TRANSPORTABLE_PLATFORM`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=REFRN30376), which specifies which combinations of source and target platforms support database transport

### 181.5 DBMS\_TDB Operational Notes

The following notes apply to `DBMS_TDB`.

- The subprograms in this package are useful both in determining whether the desired cross-platform database conversion is possible, and in checking whether the database is ready for conversion. See [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=SQLRF009) for details on the different uses of these subprograms are used in the conversion process.
- The subprograms in this package return simple `TRUE` or `FALSE` results to indicate whether database transport is possible. Use the subprograms with `SERVEROUTPUT` `ON` for informative messages about why transport is not possible.

### 181.6 Summary of DBMS\_TDB Subprograms

This table lists the `DBMS_TDB` subprograms and briefly describes them.

Table 181-2 DBMS\_TDB Package Subprograms

| Subprogram | Description |
| --- | --- |
| CHECK\_DB Function | Checks whether a database can be transported to a target platform |
| CHECK\_EXTERNAL Function | Checks whether a database has external tables, directory or BFILEs |

#### 181.6.1 CHECK\_DB Function

This function checks whether a database can be transported to a target platform. It tests whether transport is supported at all for a given source and destination platform, and whether the database is currently in the correct state for transport.

You can specify whether to skip checking parts of the database that are read-only or offline, if you do not plan to transport them.

The function is overloaded. The different functionality of each form of syntax is presented along with the definition.

Syntax

```
DBMS_TDB.CHECK_DB (
     target_platform_name   IN VARCHAR2, 
     skip_option            IN  NUMBER)
   RETURN BOOLEAN;

DBMS_TDB.CHECK_DB (
     target_platform_name   IN VARCHAR2)
   RETURN BOOLEAN;

DBMS_TDB.CHECK_DB 
   RETURN BOOLEAN;
```

Parameters

Table 181-3 CHECK\_DB Function Parameters

| Parameter | Description |
| --- | --- |
| `target_platform_name` | The name of the destination platform, as it appears in [`V$DB_TRANSPORTABLE_PLATFORM`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=REFRN30376). |
| `skip_option` | Specifies which, if any, parts of the database to skip when checking whether the database can be transported. Supported values are listed in Table 181-1. |

Return Values

If the database cannot be transported to the target platform or is not ready to be transported, returns `FALSE`. If the database is ready for transport, returns `TRUE`.

Usage Notes

- If `SERVEROUTPUT` is `ON`, then the output will contain the reasons why the database cannot be transported and how to fix the problems. For details on possible reasons and fixes, see Table 181-4.
	Table 181-4 Reasons for CHECK\_DB Function to Return FALSE
	| Cause | Action |
	| --- | --- |
	| Unrecognized target platform name. | Check [`V$DB_TRANSPORTABLE_PLATFORM`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=REFRN30376) for recognized platform names. |
	| Target platform has a different endian format. | Conversion is not supported. |
	| Database is not open read-only. | Open database read-only and retry. |
	| There are active or in-doubt transactions in the database. | Open the database read-write. After the active transactions are rolled back, open the database read-only and retry the operation.  This situation can occur if users flash back the database and open it read only. The active transactions will be rolled back when the database is opened read-write. |
	| Deferred transaction rollback needs to be done. | Open the database read-write and bring online the necessary tablespaces. Once the deferred transaction rollback is complete, open the database read-only and retry the operation. |
	| Database compatibility version is below 10.0.0. | Change the `COMPATIBLE` initialization parameter to 10.0.0 or higher, open the database read-only, and retry the operation. |
	| Some tablespaces have not been open read-write with compatibility version is 10.0.0 or higher. | Change the `COMPATIBLE` initialization parameter to 10.0.0 or higher, then open the affected tablespaces read-write. Shut down the database, open it read-only, and retry the operation. |

Examples

This example illustrates the use of `CHECK_DB` with a database that is open read-write:

```
SQL> SET SERVEROUTPUT ON
SQL> DECLARE
       db_ready BOOLEAN;
     BEGIN
       db_ready := DBMS_TDB.CHECK_DB('Microsoft Windows IA (32-bit)');
     END;
     /
  
Database is not open READ ONLY. Please open database READ ONLY and retry.

PL/SQL procedure successfully completed.
```

#### 181.6.2 CHECK\_EXTERNAL Function

This function determines whether a database has external tables, directories, or BFILEs.

Syntax

```
DBMS_TDB.CHECK_EXTERNAL 
   RETURN BOOLEAN;
```

Return Values

If the database has external tables, directories, or BFILEs, return `TRUE`. Otherwise, return `FALSE`.

Usage Notes

- If `SERVEROUTPUT` is `ON`, then the function will output the names of the external tables, directories, and BFILEs in the database.
- The database must be open read-write.

Examples

This example illustrates the use of `CHECK_EXTERNAL` with a database that has several external tables, directories, and BFILEs:

```
SQL> SET SERVEROUTPUT ON
SQL> DECLARE
        external BOOLEAN;
     BEGIN
       external := DBMS_TDB.CHECK_EXTERNAL;
     END;
     /
The following external tables exist in the database:
SH.SALES_TRANSACTIONS_EXT
The following directories exist in the database:
SYS.MEDIA_DIR, SYS.DATA_FILE_DIR, SYS.LOG_FILE_DIR, SYS.DATA_PUMP_DIR
The following BFILEs exist in the database:
PM.PRINT_MEDIA
 
PL/SQL procedure successfully completed.
```