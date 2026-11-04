---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_GLOBAL_CONTEXT.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_GLOBAL_CONTEXT` displays the definition (name, schema, and package) of all global contexts created in the database.

This view is a subset of `DBA_CONTEXT`, which describes all contexts, including global contexts.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAMESPACE` | `VARCHAR2(128)` | `NOT NULL` | Name of the context namespace |
| `SCHEMA` | `VARCHAR2(128)` | `NOT NULL` | Schema of the package that administers the globally accessible context |
| `PACKAGE` | `VARCHAR2(128)` | `NOT NULL` | Package that administers the globally accessible context |

See Also:

- " [DBA\_CONTEXT](DBA_CONTEXT.md) "
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=DBSEG70005) for more information about using global application contexts
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ARPLS68061) for more information about the `DBMS_SESSION.SET_CONTEXT` procedure