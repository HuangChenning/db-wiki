---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PX_INSTANCE_GROUP.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.143 V$PX\_INSTANCE\_GROUP

`V$PX_INSTANCE_GROUP` provides information about the instance groups being used for parallel operations by the current session.

| Column | Datatype | Description |
| --- | --- | --- |
| `QC_INSTANCE_GROUP` | `VARCHAR2(64)` | The instance group being used by this session for parallel operations. This value repeats for every row returned. |
| `WHY` | `VARCHAR2(23)` | Where the current instance group name comes from, as follows:  SERVICE - the instance group being used is from the session's service name  PARALLEL\_INSTANCE\_GROUP - the instance group being used is being used because the PARALLEL\_INSTANCE\_GROUP initialization parameter has been set.  The value repeats for every row returned. |
| `INSTANCE_NUMBER` | `NUMBER` | Instance number of the instance providing this instance group. There will be one row for each instance in the instance group that the Query Coordinator is using. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [PARALLEL\_INSTANCE\_GROUP](PARALLEL_INSTANCE_GROUP.md) "