---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/HS_ALL_DD.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.193 HS\_ALL\_DD

`HS_ALL_DD` contains data dictionary information about non-Oracle (FDS) data stores.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DD_TABLE_NAME` | `VARCHAR2(128)` |  | Data dictionary table name |
| `TRANSLATION_TYPE` | `CHAR(1) ` |  | `T` = Translation, `M` = Mimic |
| `TRANSLATION_TEXT` | `VARCHAR2(4000) ` |  | SQL statement containing the mapping |
| `FDS_CLASS_NAME` | `VARCHAR2(30) ` |  | Name of the FDS Class |
| `FDS_INST_NAME` | `VARCHAR2(30)` |  | Name of the FDS instance |
| `DD_TABLE_DESC` | `VARCHAR2(255)` |  | Description of the Oracle data dictionary table |