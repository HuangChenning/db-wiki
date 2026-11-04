---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/HS_CLASS_INIT.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.196 HS\_CLASS\_INIT

`HS_CLASS_INIT` displays information about the non-Oracle (FDS) class-specific initialization parameters.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `INIT_VALUE_NAME` | `VARCHAR2(64) ` | `NOT NULL` | Name of the initialization parameter |
| `INIT_VALUE` | `VARCHAR2(255) ` | `NOT NULL` | Value of the initialization parameter |
| `INIT_VALUE_TYPE` | `VARCHAR2(1) ` | `NOT NULL` | Environment variable (`T` or `F`). `T` means this is an environment variable;` F` means do not set as an environment variable |
| `FDS_CLASS_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the FDS Class |
| `FDS_CLASS_INIT_ID` | `NUMBER ` | `NOT NULL` | Sequence: a counter that is incremented for every row inserted (used internally) |
| `FDS_CLASS_ID` | `NUMBER ` | `NOT NULL` | Sequence: a counter that is incremented for every row inserted (used internally) |