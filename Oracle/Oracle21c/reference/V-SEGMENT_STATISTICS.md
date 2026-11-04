---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SEGMENT_STATISTICS.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.3 V$SEGMENT\_STATISTICS

| Column | Datatype | Description |
| --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | Owner of the object |
| `OBJECT_NAME` | `VARCHAR2(128)` | Name of the object |
| `SUBOBJECT_NAME` | `VARCHAR2(128)` | Name of the subobject |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | Name of the table space to which the object belongs |
| `TS#` | `NUMBER` | Tablespace number |
| `OBJ#` | `NUMBER` | Dictionary object number of the object |
| `DATAOBJ#` | `NUMBER` | Data object number of the object |
| `OBJECT_TYPE` | `VARCHAR2(18)` | Type of the object |
| `STATISTIC_NAME` | `VARCHAR2(64)` | Name of the statistic |
| `STATISTIC#` | `NUMBER` | Statistic number |
| `VALUE` | `NUMBER` | Statistic value |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |