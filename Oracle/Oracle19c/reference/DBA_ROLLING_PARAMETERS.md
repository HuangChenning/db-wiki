---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_ROLLING_PARAMETERS.html
tags:
  - oracle
  - 19c
  - reference
---

## 5.296 DBA\_ROLLING\_PARAMETERS

`DBA_ROLLING_PARAMETERS` lists the available parameters of the `DBMS_ROLLING` PL/SQL package.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SCOPE` | `VARCHAR2(128)` |  | Database unique name associated with a parameter |
| `TYPE` | `VARCHAR2(7)` |  | Type of parameter |
| `NAME` | `VARCHAR2(32)` |  | Name of the parameter |
| `DESCRIPTION` | `VARCHAR2(256)` |  | Description of the parameter |
| `CURVAL` | `VARCHAR2(256)` |  | Current value of the parameter |
| `LSTVAL` | `VARCHAR2(256)` |  | Prior value of the parameter |
| `DEFVAL` | `VARCHAR2(256)` |  | Default value of the parameter |
| `MINVAL` | `NUMBER` |  | Minimum value of the parameter |
| `MAXVAL` | `NUMBER` |  | Maximum value of the parameter |

See Also:

- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=SBYDB5214) for more information about rolling operations.
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=ARPLS73534) for more information about the `DBMS_ROLLING` package