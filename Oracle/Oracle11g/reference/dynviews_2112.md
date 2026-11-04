---
title: "V$PX_INSTANCE_GROUP"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2112.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$PX_INSTANCE_GROUP` provides information about the instance groups being used for parallel operations by the current session.

| Column | Datatype | Description |
| --- | --- | --- |
| `QC_INSTANCE_GROUP` | `VARCHAR2(64)` | The instance group being used by this session for parallel operations. This value repeats for every row returned. |
| `WHY` | `VARCHAR2(23)` | Where the current instance group name comes from, as follows:  SERVICE - the instance group being used is from the session's service name  PARALLEL\_INSTANCE\_GROUP - the instance group being used is being used because the PARALLEL\_INSTANCE\_GROUP initialization parameter has been set.  The value repeats for every row returned. |
| `INSTANCE_NUMBER` | `NUMBER` | Instance number of the instance providing this instance group. There will be one row for each instance in the instance group that the Query Coordinator is using. |