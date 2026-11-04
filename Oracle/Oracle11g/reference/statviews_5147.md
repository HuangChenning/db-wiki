---
title: NLS_DATABASE_PARAMETERS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5147.htm
tags:
  - oracle
  - 11g
  - reference
---

`NLS_DATABASE_PARAMETERS` lists permanent NLS parameters of the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PARAMETER` | `VARCHAR2(30)` | `NOT NULL` | Parameter name |
| `VALUE` | `VARCHAR2(40)` |  | Parameter value |