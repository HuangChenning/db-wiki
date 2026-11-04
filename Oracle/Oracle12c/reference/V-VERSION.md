---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-VERSION.html
tags:
  - oracle
  - 12c
  - reference
---

`V$VERSION` displays version numbers of core library components in the Oracle Database. There is one row for each component.

| Column | Datatype | Description |
| --- | --- | --- |
| `BANNER` | `VARCHAR2(80)` | Component name and version number |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |