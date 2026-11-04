---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-ACTIVE_INSTANCES.html
tags:
  - oracle
  - 12c
  - reference
---

`V$ACTIVE_INSTANCES` displays the mapping between instance names and instance numbers for all instances that have the database currently mounted.

| Column | Datatype | Description |
| --- | --- | --- |
| `INST_NUMBER` | `NUMBER` | Instance number |
| `INST_NAME` | `VARCHAR2(60)` | Instance name |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |