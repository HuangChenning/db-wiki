---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-TEMPORARY_LOBS.html
tags:
  - oracle
  - 19c
  - reference
---

## 9.111 V$TEMPORARY\_LOBS

`V$TEMPORARY_LOBS` displays information about temporary and abstract LOBs.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session ID |
| `CACHE_LOBS` | `NUMBER` | Number of cache temp LOBs |
| `NOCACHE_LOBS` | `NUMBER` | Number of nocache temp LOBs |
| `ABSTRACT_LOBS` | `NUMBER` | Number of abstract LOBs |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |