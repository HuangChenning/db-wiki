---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ADVISOR_FINDING_NAMES.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.29 DBA\_ADVISOR\_FINDING\_NAMES

`DBA_ADVISOR_FINDING_NAMES` provides a list of all finding names registered with the Advisor Framework.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ID` | `NUMBER` |  | ID of the finding name |
| `ADVISOR_NAME` | `VARCHAR2(128)` | `NOT NULL` | Advisor name |
| `FINDING_NAME` | `VARCHAR2(4000)` |  | Finding name |