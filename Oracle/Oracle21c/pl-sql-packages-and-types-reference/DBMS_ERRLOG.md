---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_ERRLOG.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 73 DBMS\_ERRLOG

The `DBMS_ERRLOG` package provides a procedure that enables you to create an error logging table so that DML operations can continue after encountering errors rather than abort and roll back. This enables you to save time and system resources.

This chapter contains the following topics:

- Security Model
- Summary of DBMS\_ERRLOG Subprograms

See Also:

[Oracle Database Data Warehousing Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=DWHSG-GUID-5B2CC8B6-8503-4B41-A75E-79A4925FCE4B) for more information regarding how to use `DBMS_ERRLOG` and [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=SQLRF01604) for `error_logging_clause` syntax

### 73.1 DBMS\_ERRLOG Security Model

Security on this package can be controlled by granting `EXECUTE` on this package to selected users or roles. The `EXECUTE` privilege is granted publicly. However, to create an error logging table, you need `SELECT` access on the base table or view, the `CREATE` `TABLE` privilege, as well as tablespace quota for the target tablespace.

### 73.2 Summary of DBMS\_ERRLOG Subprograms

The `DBMS_ERRORLOG` package includes the CREATE\_ERROR\_LOG procedure subprogram.

Table 73-1 DBMS\_ERRLOG Package Subprograms

| Subprogram | Description |
| --- | --- |
| CREATE\_ERROR\_LOG Procedure | Creates the error logging table used in DML error logging |

#### 73.2.1 CREATE\_ERROR\_LOG Procedure

This procedure creates the error logging table needed to use the DML error logging capability.

`LONG`, `CLOB`, `BLOB`, `BFILE`, and `ADT` datatypes are not supported in the columns.

Syntax

```
DBMS_ERRLOG.CREATE_ERROR_LOG (
   dml_table_name            IN VARCHAR2,
   err_log_table_name        IN VARCHAR2 := NULL,
   err_log_table_owner       IN VARCHAR2 := NULL,
   err_log_table_space       IN VARCHAR2 := NULL,
   skip_unsupported          IN BOOLEAN := FALSE);
```

Parameters

Table 73-2 CREATE\_ERROR\_LOG Procedure Parameters

| Parameter | Description |
| --- | --- |
| `dml_table_name` | The name of the DML table to base the error logging table on. The name can be fully qualified (for example, `emp`, `scott.emp`, `"EMP"`, `"SCOTT"."EMP"`). If a name component is enclosed in double quotes, it will not be upper cased. |
| `err_log_table_name` | The name of the error logging table you will create.  The default is the first 25 characters in the name of the DML table prefixed with `'ERR$_'`. Examples are the following:  `dml_table_name`: `'EMP'`, `err_log_table_name`:` 'ERR$_EMP'`  `dml_table_name`: `'"Emp2"'`, `err_log_table_name`: `'ERR$_Emp2'` |
| `err_log_table_owner` | The name of the owner of the error logging table. You can specify the owner in `dml_table_name`. Otherwise, the schema of the current connected user is used. |
| `err_log_table_space` | The tablespace the error logging table will be created in. If not specified, the default tablespace for the user owning the DML error logging table will be used. |
| `skip_unsupported` | When set to `TRUE`, column types that are not supported by error logging will be skipped over and not added to the error logging table.  When set to `FALSE`, an unsupported column type will cause the procedure to terminate.  The default is `FALSE`. |

Examples

First, create an error log table for the `channels` table in the `SH` schema, using the default name generation.

Then, see all columns of the table `channels`:

```
SQL> DESC channels
Name                                   Null?       Type
---------------------------            -------     -----
CHANNEL_ID                             NOT NULL    CHAR(1)
CHANNEL_DESC                           NOT NULL    VARCHAR2(20)
CHANNEL_CLASS                                      VARCHAR2(20)
```

Finally, see all columns of the generated error log table. Note the mandatory control columns that are created by the package:

```
SQL> DESC ERR$_CHANNELS
Name                              Null?    Type
-----------------                 ----     ----
ORA_ERR_NUMBER$                            NUMBER
ORA_ERR_MESG$                              VARCHAR2(2000)
ORA_ERR_ROWID$                             ROWID
ORA_ERR_OPTYP$                             VARCHAR2(2)
ORA_ERR_TAG$                               VARCHAR2(2000)
CHANNEL_ID                                 VARCHAR2(4000)
CHANNEL_DESC                               VARCHAR2(4000)
CHANNEL_CLASS                              VARCHAR2(4000)
```

See [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADMIN10261) for more information regarding control columns.