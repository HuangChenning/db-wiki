---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LCR_CACHE.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.33 V$LCR\_CACHE

`V$LCR_CACHE` displays information about entries in the logical change record (LCR) cache.

| Column | Datatype | Description |
| --- | --- | --- |
| `LCR_TYPE` | `CHAR(12)` | Indicates whether the LCR is `INTERNAL` or `EXTERNAL` |
| `COMPONENT_NAME` | `VARCHAR2(128)` | Component name |
| `COMPONENT_TYPE` | `VARCHAR2(40)` | Component type. Possible values:  - `APPLY` `COORDINATOR` - `APPLY` `READER` - `APPLY` `SERVER` - `CAPTURE` `COORDINATOR` - `CAPTURE` `READER` - `CAPTURE` `SERVER` |
| `NUM_COLUMNS` | `NUMBER` | Number of columns in the LCR |
| `FREE_COUNT` | `NUMBER` | Number of available LCRs |
| `REQUEST_COUNT` | `NUMBER` | Total request count |
| `CACHE_HITS` | `NUMBER` | Cache hit count |
| `ALT_CACHE_HITS` | `NUMBER` | Hit count from an alternate LCR cache entry |
| `PURGED_COUNT` | `NUMBER` | Cache purge count |
| `SID` | `NUMBER` | Session ID of the component process |
| `SERIAL#` | `NUMBER` | Session serial number of the component process |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view is available starting with Oracle Database 21c.