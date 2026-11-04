---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_LIBCACHE.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 103 DBMS\_LIBCACHE

`The DBMS_LIBCACHE` package consists of one subprogram that prepares the library cache on an Oracle instance by extracting SQL and PL/SQL from a remote instance and compiling this SQL locally without execution. The value of compiling the cache of an instance is to prepare the information the application requires to execute in advance of failover or switchover.

This chapter contains the following topics:

### 103.1 DBMS\_LIBCACHE Overview

Compiling a shared cursor consists of open, parse, and bind operations, plus the type-checking and execution plan functions performed at the first execution. All of these steps are executed in advance by the package `DBMS_LIBCACHE` for `SELECT` statements.

The open and parse functions are executed in advance for PL/SQL and DML. For PL/SQL, executing the parse phase has the effect of loading all library cache heaps other than the `MCODE`.

### 103.2 DBMS\_LIBCACHE Security Model

To execute `DBMS_LIBCACHE` you must directly access the same objects as do SQL statements. You can best accomplish this by utilizing the same user id as the original system on the remote system.

When there are multiple schema users, `DBMS_LIBCACHE` should be called for each.

Alternatively, `DBMS_LIBCACHE` may be called with the generic user `PARSER`. However, this user cannot parse the SQL that uses objects with access granted though roles. This is a standard PL/SQL security limitation.

### 103.3 Summary of DBMS\_LIBCACHE Subprograms

The `DBMS_LIBCACHE` package includes the `COMPILE_FROM_REMOTE` procedure subprogram.

Table 103-1 DBMS\_LIBCACHE Package Subprograms

| Subprogram | Description |
| --- | --- |
| COMPILE\_FROM\_REMOTE Procedure | Extracts SQL in batch from the source instance and compiles the SQL at the target instance |

#### 103.3.1 COMPILE\_FROM\_REMOTE Procedure

This procedure extracts SQL in batch from the source instance and compiles the SQL at the target instance.

Syntax

```
DBMS_LIBCACHE.COMPILE_FROM_REMOTE ( 
   p_db_link                 IN     dbms_libcache$def.db_link%type, 
   p_username                IN     VARCHAR2 default null,
   p_threshold_executions    IN     NATURAL  default 3,
   p_threshold_sharable_mem  IN     NATURAL  default 1000,
   p_parallel_degree         IN     NATURAL  default 1);
```

Parameters

Table 103-2 COMPILE\_FROM\_REMOTE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `p_db_link` | Database link to the source name (mandatory). The database link pointing to the instance that will be used for extracting the SQL statements. The user must have the role `SELECT_ON_CATALOG` at the source instance. For improved security, the connection may use a password file or LDAP authentication. The database link is mandatory only for releases with `dbms_libcache$def.ACCESS_METHOD = DB_LINK_METHOD ` |
| `p_instance_name` | (Reserved for future use). The name of the instance that will be used for extracting the SQL statements. The instance name must be unique for all instances excluding the local instance. The name is not case sensitive. |
| `p_username` | Source username (default is all users). The name of the username that will be used for extracting the SQL statements. The username is an optional parameter that is used to ensure the parsing user id is the same as that on the source instance. For an application where users connect as a single `user_id`, for example `APPS`, `APPS` is the parsing `user_id` that is recorded in the shared pool. To select only SQL statements parsed by `APPS`, enter the string 'APPS' in this field. To also select statements executed by batch, repeat the executing the procedure with the schema owner, for example GL. If the username is supplied, it must be valid. The name is not case sensitive. |
| `p_threshold_executions` | The lower bound for the number of executions, below which a SQL statement will not be selected for parsing. This parameter is optional. It allows the application to extract and compile statements with executions, for example, greater than 3. The default value is 1. This means SQL statements that have never executed, including invalid SQL statements, will not be extracted. |
| `p_threshold_sharable_mem` | The lower bound for the size of the shared memory consumed by the cursors on the source instance. Below this value a SQL statement will not be selected for parsing. This parameter is optional. It allows the application to extract and compile statements with shared memory for example, greater than 10000 bytes. |
| `p_parallel_degree` | The number of parallel jobs that execute to complete the parse operation. These tasks are spawned as parallel jobs against a sub-range of the SQL statements selected for parsing. This parameter is reserved for parallel compile jobs which are currently not implemented. |