---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_WR_SETTINGS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.87 DBA\_HIST\_WR\_SETTINGS

`DBA_HIST_WR_SETTINGS` displays the settings and metadata for the Workload Repository.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `LOCAL_AWRDBID` | `NUMBER` | `NOT NULL` | Database ID of the local database |
| `VIEW_LOCATION` | `VARCHAR2(8)` |  | Data source of the DBA\_HIST dictionary views. Possible values include:  - `AWR_PDB`: Views display AWR data stored in the PDB. - `AWR_ROOT`: Views display AWR data stored in the root. |
| `CON_ID` | `NUMBER` |  | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire multitenant container database (CDB). This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |