---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-TSDP_SUPPORTED_FEATURE.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.124 V$TSDP\_SUPPORTED\_FEATURE

`V$TSDP_SUPPORTED_FEATURE` displays information about the features supported by Transparent Sensitive Data Protection (TSDP).

| Column | Datatype | Description |
| --- | --- | --- |
| `FEATURE_NAME` | `VARCHAR2(200)` | The name of the supported feature |
| `FUNCTIONALITY` | `VARCHAR2(200)` | The functionality that is supported within the feature. If all of the functionality of the feature is supported, the value is `ALL`, otherwise the value will show the specific functionality that is supported. |
| `COMMENTS$` | `VARCHAR2(4000)` | More information regarding the support for the feature and the specific functionality |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG855) for more information about using Transparent Sensitive Data Protection.