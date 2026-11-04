---
title: DBMS_XDB_ADMIN
book: PL/SQL Packages and Types Reference
doc_id: E96430-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_XDB_ADMIN.html
tags:
  - oracle
  - 19c
  - pl-sql-packages-and-types-reference
---

The `DBMS_XDB_ADMIN` package provides an interface to manage the Oracle XML DB repository.

This chapter contains the following topics:

- DBMS\_XDB\_ADMIN Security Model
- Summary of DBMS\_XDB\_ADMIN Subprograms

**See Also:** [*Oracle XML DB Developer’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADXDB6017) for information about Oracle XML DB Repository

### DBMS\_XDB\_ADMIN Security Model

Owned by `XDB`, the `DBMS_XDB_ADMIN` package must be created by `SYS` or `XDB`. The `EXECUTE` privilege is granted to `SYS` or `XDB` or `DBA`. Subprograms in this package are executed using the privileges of the current user.

### Summary of DBMS\_XDB\_ADMIN Subprograms

This table lists the package subprograms in alphabetical order.

Table 1 DBMS\_XDB\_ADM Package Subprograms

| Subprogram | Description |
| --- | --- |
| CREATENONCEKEY Procedure | Generates a nonce value for use in digest authentication |
| INSTALLDEFAULTWALLET Procedure | Installs the default XDB wallet in the default XDB wallet directory |
| MOVEXDB\_TABLESPACE Procedure | Moves the XDB (user) to the specified tablespace |
| REBUILDHIERARCHICALINDEX Procedure | Rebuilds the hierarchical index after import or export operations |

### CREATENONCEKEY Procedure

This procedure generates a nonce value for use in digest authentication.

**Syntax**

```md
DBMS_XDB_ADMIN.CREATENONCEKEY;
```

### INSTALLDEFAULTWALLET Procedure

This procedure installs the default XDB wallet in the default XDB wallet directory.

The directory name where the XDB wallet is stored is prefixed either by `ORACLE_BASE` when it is defined, or `ORACLE_HOME`. It is then followed by `/admin/` *db\_name* `/xdb_wallet` where *db\_name* is the unique database name.

**Syntax**

```md
DBMS_XDB_ADMIN.INSTALLDEFAULTWALLET;
```

**Usage Notes**

Only `SYS` can install or replace the default wallet.

### MOVEXDB\_TABLESPACE Procedure

This procedure moves the XDB (user) to the specified tablespace.

**Syntax**

```md
DBMS_XDB_ADMIN.MOVEXDB_TABLESPACE(
   new_tablespace   IN  VARCHAR2);
```

**Parameters**

Table 2 MOVEXDB\_TABLESPACE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `new_tablespace` | Name of the tablespace to where the XDB is moved |

**Usage Notes**

- This operation waits for all concurrent XDB sessions to exit.
- If `MOVEXDB_TABLESPACE` fails, the user should restart the database before issuing any further command.Failure to do so will result into unexpected behavior from the database.
- The XDB repository by default resides in the `SYSAUX` tablespace. Using this procedure it can be moved to another tablespace. As a best practice we recommend to create a dedicated tablespace for the XDB repository only and not share it with other objects (such as tables). The tablespace containing the XDB repository should never be set to `READ` `ONLY` because this might affect various XML operations being executed.

### REBUILDHIERARCHICALINDEX Procedure

This procedure rebuilds the hierarchical index after import or export operations. This is necessary because data cannot be exported from index tables.

**Syntax**

```md
DBMS_XDB_ADMIN.REBUILDHIERARCHICALINDEX;
```