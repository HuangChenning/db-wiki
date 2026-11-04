---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/HS_FDS_INST.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.201 HS\_FDS\_INST

`HS_FDS_INST` contains information about non-Oracle (FDS) instances.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `FDS_INST_NAME` | `VARCHAR2(30) ` | `NOT NULL` | Name of the FDS instance |
| `FDS_INST_COMMENTS ` | `VARCHAR2(255)` |  | Text description of the non-Oracle instance |
| `FDS_CLASS_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the FDS class |
| `FDS_INST_ID` | `NUMBER ` | `NOT NULL` | Sequence: a counter that is incremented for every row inserted (used internally) |
| `FDS_CLASS_ID` | `NUMBER ` | `NOT NULL` | Sequence: a counter that is incremented for every row inserted (used internally) |