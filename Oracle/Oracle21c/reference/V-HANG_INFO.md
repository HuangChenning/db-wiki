---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-HANG_INFO.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.273 V$HANG\_INFO

`V$HANG_INFO` displays information about hangs found on the cluster.

A hang can be an open wait chain or closed wait chain (cycle or deadlock). A wait chain is a series of sessions that are blocking one another. Each row represents a hang and describes how severe the hang is. This view also includes the victim or final blocker of the hang.

| Column | Datatype | Description |
| --- | --- | --- |
| `HANG_ID` | `NUMBER` | A number identifying the hang |
| `HANG_CHAIN_SESSIONS` | `NUMBER` | Indicates how many sessions are in the main wait chain of the hang |
| `TOTAL_HUNG_SESSIONS` | `NUMBER` | Indicates how many total sessions are affected by the hang, including the main wait chain and any wait chains branching off of the main wait chain |
| `HANG_TYPE` | `VARCHAR2(18)` | Is set to `Hang` if this is an open wait chain or `Deadlock` if this is a cycle or closed wait chain |
| `HANG_STATUS` <sup>Foot 1</sup> | `VARCHAR2(20)` | Status of the hang. Possible values:  - `Invalid` - The hang is about to be removed because its hung status has become in doubt - `Pending` `Resolution` - The hang or deadlock has been marked for resolution and will be resolved shortly - `Reconfiguration` - A reconfiguration occurred and the hang or deadlock must be re-detected and verified before any action can be taken toward resolution - `Requires` `Verification` - The hang is about to be verified to confirm if its sessions are still hung - `Resolved` - The hang or deadlock was resolved by terminating the final blocker (or root) or, if necessary, by terminating the instance - `Self-Resolved` - The hang was detected but resolved on its own without Hang Manager intervention - `Unresolvable` - The hang was determined to be a special case that is not resolvable - `Valid` - The hang or deadlock was detected but not yet verified - `Verified` `Hung` - The hang has been verified and a decision will be made soon on whether the hang will be resolved or ignored - `Victim` `Selected` - A victim has been selected. If the hang is marked for resolution, the victim will be terminated. |
| `HANG_CREATE_TIME` | `VARCHAR2(20)` | Date and time that the hang was detected |
| `HANG_RESOLVE_TIME` | `VARCHAR2(20)` | Time that the hang may be automatically resolved |
| `IGNORED_HANG` | `VARCHAR2(1)` | `Y` - Hang was ignored and will not be automatically resolved at this time  `N` - The hang has not yet been verified |
| `RESOLUTION_ATTEMPTED` | `VARCHAR2(1)` | `Y` - An attempt was made to resolve the hang  `N` - No attempt was made to resolve the hang |
| `GLOBAL_HANG` | `VARCHAR2(1)` | `Y` - The hang spans multiple nodes in the cluster  `N` - All of the sessions in the hang reside on a single instance |
| `ESCALATED_HANG` | `VARCHAR2(1)` | `Y` - An attempt was made to resolve the hang but was unsuccessful, and the hang is becoming more severe. Another resolution attempt will be made.  `N` - The first resolution attempt was successful and it was not necessary to escalate the hang to a higher resolution level. |
| `RESOLUTION_STATUS` | `VARCHAR2(45)` | Contains the reason why the hang was resolved or ignored |
| `VICTIM_INSTANCE` | `NUMBER` | Instance number of the instance on which the victim or final blocker session resides |
| `VICTIM_SESSION_ID` | `NUMBER` | Victim or final blocker's Oracle session ID |
| `VICTIM_SERIAL#` | `NUMBER` | Victim or final blocker's Oracle session serial number |
| `VICTIM_OSPID` | `VARCHAR2(24)` | Victim or final blocker's operating system process ID |
| `FATAL_BACKGROUND` | `VARCHAR2(1)` | `Y` - Victim or final blocker is a critical background process  `N` - Victim or final blocker is not a critical background process |
| `PNAME` | `VARCHAR2(5)` | Name of the victim or final blocker process |
| `VICTIM_PDB_ID` | `NUMBER` | Victim or final blocker's container ID or PDB ID |
| `WAIT_EVENT_TEXT` | `VARCHAR2(64)` | Resource or event for which the victim or final blocker is waiting; set to `not in a wait` if the session is not waiting on a resource |
| `VICTIM_QOS_PC_RANK` | `VARCHAR2(12)` | Oracle Database Quality of Service (QoS) Management Performance Class rank of the victim or final blocker of the hang. |
| `VICTIM_QOS_PC_ITT` | `NUMBER` | Oracle Database QoS Management Performance Class In-Trouble Threshold of the victim or final blocker of the hang |
| `VICTIM_QOS_PC_RTT` | `NUMBER` | Oracle Database QoS Management Performance Class Root Termination allowed Threshold of the victim or final blocker of the hang |
| `VICTIM_QOS_PC_KEY` | `NUMBER` | Oracle Database QoS Management Performance Class Key of the victim or final blocker of the hang |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 21c.