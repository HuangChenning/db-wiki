---
title: EXCEPTIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5124.htm
tags:
  - oracle
  - 11g
  - reference
---

`EXCEPTIONS` contains information on violations of integrity constraints. This table is created by the `utlexcpt.sql` script.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ROW_ID` | `ROWID` |  | Row that caused the violation |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Name of the table |
| `CONSTRAINT` | `VARCHAR2(30)` |  | Integrity constraint that was violated |