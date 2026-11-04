---
title: DBMS_TNS
book: PL/SQL Packages and Types Reference
doc_id: E96430-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_TNS.html
tags:
  - oracle
  - 19c
  - pl-sql-packages-and-types-reference
---

The `DBMS_TNS` package provides the `RESOLVE_TNSNAME` function to resolve a TNS name and return the corresponding Oracle Net8 connection string.

This chapter contains the following topics:

### DBMS\_TNS Overview

The `DBMS_TNS` package contains one function, `RESOLVE_TNSNAME`, which returns the resolved connect string from configured sources that have been defined in the `names.directory_path` parameter in the `sqlnet.ora` file.

The `RESOLVE_TNSNAME` function in this package helps you to identify interconnected databases and trace the system change number (SCN) flow across distributed databases.

**See Also:**

- [*Oracle Database Administrator’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADMIN-GUID-D7B3AB7D-8862-4504-AA46-596D222119BD) for more information about finding database link information
- [*Oracle Database Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=REFRN20050) for information about the `ALL_DB_LINKS` data dictionary view

### DBMS\_TNS Security Model

You must be granted the `EXECUTE` privilege on the `DBMS_TNS` package.

### Summary of DBMS\_TNS Subprograms

This table lists the `DBMS_TNS` subprograms and briefly describes them.

Table 1 DBMS\_TNS Parameters

| Subprogram | Description |
| --- | --- |
| RESOLVE\_TNSNAME Function | Returns the resolved connect string from any configured source (tnsnames, LDAP, Easy Connect) as indicated in the `sqlnet.ora` `names.directory_path` parameter) |

### RESOLVE\_TNSNAME Function

This function returns the resolved connect string from any configured source (for example, TNS names, Lightweight Directory Access Protocol (LDAP), or Oracle Easy Connect) as indicated in the `sqlnet.ora` `names.directory_path` parameter.

**Syntax**

```md
DBMS_TNS.RESOLVE_TNSNAME (
   tns_name VARCHAR2)
  RETURN VARCHAR2;
```

**RESOLVE\_TNSNAME Function Parameters**

| Parameter | Description |
| --- | --- |
| `tns_name` | Database address for establishing the connection |

**Usage Notes**

- Database administrators and system management tools can explicitly call the `DBMS_TNS.RESOLVE_TNSNAME function` to resolve a `tns_name`:
- Because the resolved value can change over time, Oracle does not recommend storing or caching this value, because these kinds of values can become invalid over time.
- You can use the `DBMS_TNS.RESOLVE_TNSNAME` function to resolve TNS names that were referred to by other data dictionary views such as `ALL_DB_LINKS` and `USER_DB_LINKS`. In addition, you can use it to find any TNS name entry in the `tnsnames.ora` file.

**Example**

```md
SELECT DB_LINK, DBMS_TNS.RESOLVE_TNSNAME(HOST) FROM DBA_DB_LINKS;

DB_LINK
--------------------------------------------------------------------------------
DBMS_TNS.RESOLVE_TNSNAME(HOST)
--------------------------------------------------------------------------------
US.EXAMPLE.COM
(DESCRIPTION=(ADDRESS=(PROTOCOL=ipc)(KEY=may))(CONNECT_DATA=(SERVICE_NAME=us.example.com)(CID=(PROGRAM=oracle)(HOST=juno)(USER=psmith))
))
```