---
title: ALL_CONTEXT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1048.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CONTEXT` describes all context namespaces in the current session for which attributes and values have been specified using the `DBMS_SESSION.SET_CONTEXT` procedure. This view does not display the `TYPE` column.

Related View

`DBA_CONTEXT` describes all context namespaces defined in the database, regardless whether any attributes have been specified for them using the `DBMS_SESSION.SET_CONTEXT` procedure.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAMESPACE` | `VARCHAR2(30)` | `NOT NULL` | Name of the context namespace |
| `SCHEMA` | `VARCHAR2(30)` | `NOT NULL` | Schema name of the designated package that can set attributes using this namespace |
| `PACKAGE` | `VARCHAR2(30)` | `NOT NULL` | Package name of the designated package that can set attributes using this namespace |
| `TYPE` | `VARCHAR2(22)` |  | Type of the context: |