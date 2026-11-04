---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/HS_CLASS_INIT.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.199 HS\_CLASS\_INIT

`HS_CLASS_INIT` displays information about the non-Oracle (FDS) class-specific initialization parameters.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `INIT_VALUE_NAME` | `VARCHAR2(64) ` | `NOT NULL` | Name of the initialization parameter |
| `INIT_VALUE` | `VARCHAR2(255) ` | `NOT NULL` | Value of the initialization parameter |
| `INIT_VALUE_TYPE` | `VARCHAR2(1) ` | `NOT NULL` | Environment variable (`T` or `F`). `T` means this is an environment variable;` F` means do not set as an environment variable |
| `FDS_CLASS_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the FDS Class |
| `FDS_CLASS_INIT_ID` | `NUMBER ` | `NOT NULL` | Sequence: a counter that is incremented for every row inserted (used internally) |
| `FDS_CLASS_ID` | `NUMBER ` | `NOT NULL` | Sequence: a counter that is incremented for every row inserted (used internally) |