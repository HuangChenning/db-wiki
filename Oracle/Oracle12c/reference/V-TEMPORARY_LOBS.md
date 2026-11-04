---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-TEMPORARY_LOBS.html
tags:
  - oracle
  - 12c
  - reference
---

`V$TEMPORARY_LOBS` displays information about temporary and abstract LOBs.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session ID |
| `CACHE_LOBS` | `NUMBER` | Number of cache temp LOBs |
| `NOCACHE_LOBS` | `NUMBER` | Number of nocache temp LOBs |
| `ABSTRACT_LOBS` | `NUMBER` | Number of abstract LOBs |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |