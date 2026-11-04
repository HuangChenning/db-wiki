---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/HS_FDS_CLASS.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.197 HS\_FDS\_CLASS

`HS_FDS_CLASS` contains information about legal non-Oracle (FDS) classes.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `FDS_CLASS_NAME ` | `VARCHAR2(30) ` | `NOT NULL` | Name of the FDS class (for example, ODBC, DB2) |
| `FDS_CLASS _COMMENTS ` | `VARCHAR2(255)` |  | Text description of the non-Oracle class |
| `FDS_CLASS_ID ` | `NUMBER` | ` NOT NULL` | Sequence: a counter that is incremented for every row inserted (used internally) |