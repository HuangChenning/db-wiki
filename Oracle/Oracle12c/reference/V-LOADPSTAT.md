---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-LOADPSTAT.html
tags:
  - oracle
  - 12c
  - reference
---

`V$LOADPSTAT` contains statistics about the number of rows loaded into a partition, or subpartition, during a load using the Direct Path API.

| Column | Datatype | Description |
| --- | --- | --- |
| `OWNER` | `VARCHAR2(31)` | Schema name |
| `TABNAME` | `VARCHAR2(31)` | Table name |
| `PARTNAME` | `VARCHAR2(31)` | Partition name |
| `LOADED` | `NUMBER` | Number of rows loaded |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |