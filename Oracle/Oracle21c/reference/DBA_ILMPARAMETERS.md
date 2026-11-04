---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ILMPARAMETERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.100 DBA\_ILMPARAMETERS

`DBA_ILMPARAMETERS` can be queried to provide information on the Automatic Data Optimization parameters in the database and their values.

Note:

Automatic Data Optimization is supported in Oracle Database 12c Release 2 multitenant environments.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR2(128)` |  | Name of the Automatic Data Optimization environment parameter. The value is one of the constants defined in the `DBMS_ILM_ADMIN` package. |
| `VALUE` | `NUMBER` |  | Value of the parameter |

See Also:

- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS73513) for more information about the API interface for implementing Automatic Data Optimization strategies
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS74887) for more information about the `DBMS_ILM_ADMIN` package