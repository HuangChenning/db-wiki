---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/SESSION_CONTEXT.html
tags:
  - oracle
  - 12c
  - reference
---

`SESSION_CONTEXT` describes the context attributes and their values set for the current session.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAMESPACE` | `VARCHAR2(128)` |  | Namespace that the active attribute is in |
| `ATTRIBUTE` | `VARCHAR2(128)` |  | Name of the active attribute |
| `VALUE` | `VARCHAR2(4000)` |  | Value of the active attribute |