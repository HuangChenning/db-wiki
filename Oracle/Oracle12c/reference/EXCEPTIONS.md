---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/EXCEPTIONS.html
tags:
  - oracle
  - 12c
  - reference
---

`EXCEPTIONS` contains information on violations of integrity constraints. This table is created by the `utlexcpt.sql` script.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ROW_ID` | `ROWID` |  | Row that caused the violation |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the table |
| `CONSTRAINT` | `VARCHAR2(128)` |  | Integrity constraint that was violated |