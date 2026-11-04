---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_CONTEXT.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.141 ALL\_CONTEXT

`ALL_CONTEXT` describes all context namespaces in the current session for which attributes and values have been specified using the `DBMS_SESSION.SET_CONTEXT` procedure. This view does not display the `TYPE` and `ORIGIN_CON_ID` columns.

Related View

`DBA_CONTEXT` describes all context namespaces defined in the database, regardless whether any attributes have been specified for them using the `DBMS_SESSION.SET_CONTEXT` procedure.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAMESPACE` | `VARCHAR2(128)` | `NOT NULL` | Name of the context namespace |
| `SCHEMA` | `VARCHAR2(128)` | `NOT NULL` | Schema name of the designated package that can set attributes using this namespace |
| `PACKAGE` | `VARCHAR2(128)` | `NOT NULL` | Package name of the designated package that can set attributes using this namespace |

See Also:

- " [DBA\_CONTEXT](DBA_CONTEXT.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS68061) for more information about the `DBMS_SESSION.SET_CONTEXT` procedure