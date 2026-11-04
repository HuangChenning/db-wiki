---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-WAITSTAT.html
tags:
  - oracle
  - 12c
  - reference
---

This table is only updated when timed statistics are enabled.

| Column | Datatype | Description |
| --- | --- | --- |
| `CLASS` | `VARCHAR2(18)` | Class of the block |
| `COUNT` | `NUMBER` | Number of waits by this `OPERATION` for this `CLASS` of block |
| `TIME` | `NUMBER` | Sum of all wait times for all the waits by this `OPERATION` for this `CLASS` of block (in centiseconds) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |