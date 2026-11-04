---
title: DBA_GLOBAL_CONTEXT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3197.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_GLOBAL_CONTEXT` displays the definition (name, schema, and package) of all global contexts created in the database. This view is a subset of `DBA_CONTEXT`, which describes all contexts, including global contexts.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAMESPACE` | `VARCHAR2(128)` | `NOT NULL` | Name of the context namespace |
| `SCHEMA` | `VARCHAR2(128)` | `NOT NULL` | Schema of the package that administers the globally accessible context |
| `PACKAGE` | `VARCHAR2(128)` | `NOT NULL` | Package that administers the globally accessible context |

See Also:

- ["DBA\_CONTEXT"](statviews_3121.md)
- [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/app_context.htm#DBSEG70005) for more information about using global application contexts
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_sessio.htm#ARPLS68061) for more information about the `DBMS_SESSION.SET_CONTEXT` procedure