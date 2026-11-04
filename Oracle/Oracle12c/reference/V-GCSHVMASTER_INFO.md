---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-GCSHVMASTER_INFO.html
tags:
  - oracle
  - 12c
  - reference
---

`V$GCSHVMASTER_INFO` describes the current and previous master instances and the number of re-masterings of Global Cache Service resources except those belonging to files mapped to a particular master.

| Column | Datatype | Description |
| --- | --- | --- |
| `HV_ID` | `NUMBER` | PCM hash value ID |
| `CURRENT_MASTER` | `NUMBER` | Master instance of this PCM hash value ID |
| `PREVIOUS_MASTER` | `NUMBER` | Previous master instance of this PCM hash value ID |
| `REMASTER_CNT` | `NUMBER` | Number of times this has been remastered |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |