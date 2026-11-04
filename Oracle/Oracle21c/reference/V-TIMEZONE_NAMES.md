---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-TIMEZONE_NAMES.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.119 V$TIMEZONE\_NAMES

| Column | Datatype | Description |
| --- | --- | --- |
| `TZNAME` | `VARCHAR2(64)` | Time zone region (for example, `US/Pacific`) |
| `TZABBREV` | `VARCHAR2(64)` | Corresponding daylight abbreviation (for example, `PDT`) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |