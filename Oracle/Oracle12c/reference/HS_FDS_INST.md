---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/HS_FDS_INST.html
tags:
  - oracle
  - 12c
  - reference
---

`HS_FDS_INST` contains information about non-Oracle (FDS) instances.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `FDS_INST_NAME` | `VARCHAR2(30) ` | `NOT NULL` | Name of the FDS instance |
| `FDS_INST_COMMENTS ` | `VARCHAR2(255)` |  | Text description of the non-Oracle instance |
| `FDS_CLASS_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the FDS class |
| `FDS_INST_ID` | `NUMBER ` | `NOT NULL` | Sequence: a counter that is incremented for every row inserted (used internally) |
| `FDS_CLASS_ID` | `NUMBER ` | `NOT NULL` | Sequence: a counter that is incremented for every row inserted (used internally) |