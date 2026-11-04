---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-CORRUPT_XID_LIST.html
tags:
  - oracle
  - 12c
  - reference
---

| Column | Datatype | Description |
| --- | --- | --- |
| `CORRUPT_XID` | `VARCHAR2(256)` | Name of corrupt XID |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |