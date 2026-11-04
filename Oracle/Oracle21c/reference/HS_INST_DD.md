---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/HS_INST_DD.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.203 HS\_INST\_DD

`HS_INST_DD` displays information from the non-Oracle (FDS) instance-specific data dictionary translations.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DD_TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the Oracle data dictionary table |
| `DD_TABLE_DESC` | `VARCHAR2(255)` |  | Description of the Oracle data dictionary table |
| `TRANSLATION_TYPE` | `CHAR(1) ` | `NOT NULL` | `T` = Translation, `M` = Mimic |
| `TRANSLATION_TEXT` | `VARCHAR2(4000)` |  | SQL statement containing the mapping |
| `FDS_CLASS_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the FDS class (for example, ODBC, DB2) |
| `FDS_INST_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the FDS instance |
| `DD_TABLE_ID` | `NUMBER ` | `NOT NULL` | Sequence: a counter that is incremented for every row inserted (used internally) |
| `FDS_CLASS_ID` | `NUMBER ` | `NOT NULL` | Sequence: a counter that is incremented for every row inserted (used internally) |
| `FDS_INST_ID` | `NUMBER ` | `NOT NULL` | Sequence: a counter that is incremented for every row inserted (used internally) |