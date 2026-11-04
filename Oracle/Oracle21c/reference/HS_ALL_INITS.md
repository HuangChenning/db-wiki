---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/HS_ALL_INITS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.194 HS\_ALL\_INITS

`HS_ALL_INITS` contains initialization parameter information about non-Oracle (FDS) data stores.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `INIT_VALUE_NAME` | `VARCHAR2(64)` |  | Name of the initialization parameter |
| `INIT_VALUE ` | `VARCHAR2(255)` |  | Value of the initialization parameter |
| `INIT_VALUE_TYPE` | `VARCHAR2(1)` |  | Environment variable (`T` or `F`). `T` means this is an environment variable; `F` means do not set as an environment variable |
| `FDS_CLASS_NAME` | `VARCHAR2(30) ` |  | Name of the FDS Class |
| `FDS_INST_NAME` | `VARCHAR2(30)` |  | Name of the FDS instance |