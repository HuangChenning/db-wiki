---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_REGISTRY_BACKPORTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.280 DBA\_REGISTRY\_BACKPORTS

`DBA_REGISTRY_BACKPORTS` displays information about backported bug fixes recorded to support database upgrade and downgrade operations. It is not intended to provide a complete list of all bug fixes or all data dictionary changes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `BUGNO` | `NUMBER` | `NOT NULL` | Bug number |
| `VERSION_FULL` | `VARCHAR2(30)` | `NOT NULL` | Component full version |
| `COMP_ID` | `VARCHAR2(30)` | `NOT NULL` | Component identifier |
| `NAMESPACE` | `VARCHAR2(30)` | `NOT NULL` | Component namespace |
| `BACKPORT_TYPE` | `VARCHAR2(30)` | `NOT NULL` | Type of backported bug fix  The value of this column is always `DICTIONARY`, which indicates that the bug fix changed the data dictionary of the database. |
| `BACKPORT_TIME` | `TIMESTAMP(6)` | `NOT NULL` | Date and time at which the backported bug fix was applied |