---
title: DBA_ADDM_INSTANCES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3005.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_ADDM_INSTANCES` displays instance-level information for ADDM tasks that finished executing. For each instance that was supposed to be analyzed (whether it was or not) there is one row describing information about it.

Related View

`USER_ADDM_INSTANCES` displays instance-level information for ADDM tasks that finished executing in all instances owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TASK_ID` | `NUMBER` | `NOT NULL` | The ID of the main ADDM task |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | The number of the instance |
| `INSTANCE_NAME` | `VARCHAR2(16)` |  | The name of the instance |
| `HOST_NAME` | `VARCHAR2(64)` |  | The name of the machine on which the instance was running |
| `STATUS` | `VARCHAR2(10)` |  | How information from this instance was used by the ADDM task.  A value of ANALYZED means that the instance participated fully in the analysis. For the following remaining values, the instance was not used during task execution, for the stated reason:  BOUNCED - the instance was shut down or started during the analysis period  NO\_SNAPS - there were either begin or end snapshots missing for the instance  NO\_STATS - there were key statistics missing for the instance  NOT\_FOUND - no mention of this instance could be found in AWR during the analysis period |
| `DATABASE_TIME` | `NUMBER` |  | The database time, in microseconds, accumulated by this instance during the analysis period |
| `ACTIVE_SESSIONS` | `NUMBER` |  | The average number of active sessions for the instance during the analysis period |
| `PERC_ACTIVE_SESS` | `NUMBER` |  | The percentage of active sessions for this instance, out of the total active sessions for the task |
| `METER_LEVEL` | `VARCHAR2(6)` |  | Reserved for future use |
| `LOCAL_TASK_ID` | `NUMBER` |  | The ID of a local ADDM task that contained an analysis of the instance for the same analysis period as that of the main task. If the main task is a local ADDM, then this value is the same as the `TASK_ID` value. |