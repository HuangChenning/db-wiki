---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-HEAT_MAP_SEGMENT.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.276 V$HEAT\_MAP\_SEGMENT

| Column | Datatype | Description |
| --- | --- | --- |
| `OBJECT_NAME` | `VARCHAR2(128)` | Name of the object |
| `SUBOBJECT_NAME` | `VARCHAR2(128)` | Name of the subobject |
| `OBJ#` | `NUMBER` | Object number |
| `DATAOBJ#` | `NUMBER` | Data object number |
| `TS#` | `NUMBER` | ID of the tablespace containing the segment whose heat map is tracked |
| `TRACK_TIME` | `DATE` | Timestamp of current activity tracking |
| `SEGMENT_WRITE` | `VARCHAR2(3)` | Indicates whether the segment has write access: (`YES` or `NO`) |
| `SEGMENT_READ` | `VARCHAR2(3)` | Indicates whether the segment has read access: (`YES` or `NO`) |
| `FULL_SCAN` | `VARCHAR2(3)` | Indicates whether the segment has full table scan: (`YES` or `NO`) |
| `LOOKUP_SCAN` | `VARCHAR2(3)` | Indicates whether the segment has lookup scan: (`YES` or `NO`) |
| `N_SEGMENT_WRITE` | `NUMBER` | Number of segment writes |
| `N_FULL_SCAN` | `NUMBER` | Number of table scans |
| `N_LOOKUP_SCAN` | `NUMBER` | Number of lookup scans |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [ALL\_HEAT\_MAP\_SEGMENT](ALL_HEAT_MAP_SEGMENT.md) "