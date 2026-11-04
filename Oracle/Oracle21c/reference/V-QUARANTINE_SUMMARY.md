---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-QUARANTINE_SUMMARY.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.153 V$QUARANTINE\_SUMMARY

`V$QUARANTINE_SUMMARY` provides a summary of quarantine for each pluggable database (PDB).

| Column | Datatype | Description |
| --- | --- | --- |
| `OBJECT_COUNT` | `NUMBER` | Number of objects in quarantine |
| `OBJECT_LIMIT` | `NUMBER` | Limit on the number of objects that can be in quarantine before a termination will occur |
| `MEMORY_TOTAL` | `NUMBER` | Number of bytes in quarantine |
| `MEMORY_LIMIT` | `NUMBER` | Limit on the amount of memory that can be in quarantine before a termination will occur |
| `RECENT_COUNT` | `NUMBER` | Number of objects recently placed in quarantine (within the last hour) |
| `RECENT_LIMIT` | `NUMBER` | Limit on the number of recently quarantined objects before a termination will occur |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$QUARANTINE](V-QUARANTINE.md) " for additional details on objects recently placed into quarantine