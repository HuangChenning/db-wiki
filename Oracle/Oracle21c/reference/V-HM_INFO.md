---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-HM_INFO.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.280 V$HM\_INFO

`V$HM_INFO` displays information about Health Monitor runs, findings, and recommendations.

The information for a run/finding/recommendation is organized as a name, value pair.

If the type of information is `RUN`, then the data represents the input parameters for that run. If the type of information is `FINDING` or `RECOMMENDATION`, then the data represents the information about that particular finding/recommendation.

| Column | Datatype | Description |
| --- | --- | --- |
| `ID` | `NUMBER` | Unique identifier of the information |
| `TYPE` | `VARCHAR2(14)` | Type of the information:  - `RUN` - `RUN-RESUME` - `FINDING` - `RECOMMENDATION` |
| `NAME` | `VARCHAR2(32)` | Information parameter name |
| `VALUE` | `VARCHAR2(513)` | Information parameter value |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |