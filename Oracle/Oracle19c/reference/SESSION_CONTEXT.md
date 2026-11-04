---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/SESSION_CONTEXT.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.240 SESSION\_CONTEXT

`SESSION_CONTEXT` describes the context attributes and their values set for the current session.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAMESPACE` | `VARCHAR2(128)` |  | Namespace that the active attribute is in |
| `ATTRIBUTE` | `VARCHAR2(128)` |  | Name of the active attribute |
| `VALUE` | `VARCHAR2(4000)` |  | Value of the active attribute |