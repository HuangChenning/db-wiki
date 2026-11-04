---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_ADVISOR_FINDING_NAMES.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_ADVISOR_FINDING_NAMES` provides a list of all finding names registered with the Advisor Framework.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ID` | `NUMBER` |  | ID of the finding name |
| `ADVISOR_NAME` | `VARCHAR2(128)` | `NOT NULL` | Advisor name |
| `FINDING_NAME` | `VARCHAR2(4000)` |  | Finding name |