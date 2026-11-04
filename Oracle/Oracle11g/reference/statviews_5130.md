---
title: HS_ALL_INITS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5130.htm
tags:
  - oracle
  - 11g
  - reference
---

`HS_ALL_INITS` contains initialization parameter information about non-Oracle (FDS) data stores.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `INIT_VALUE_NAME` | `VARCHAR2(64)` |  | Name of the initialization parameter |
| `INIT_VALUE` | `VARCHAR2(255)` |  | Value of the initialization parameter |
| `INIT_VALUE_TYPE` | `VARCHAR2(1)` |  | Environment variable (`T` or `F`). `T` means this is an environment variable; `F` means do not set as an environment variable |
| `FDS_CLASS_NAME` | `VARCHAR2(30)` |  | Name of the FDS Class |
| `FDS_INST_NAME` | `VARCHAR2(30)` |  | Name of the FDS instance |