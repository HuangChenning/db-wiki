---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-AQ_NONDUR_REGISTRATIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.27 V$AQ\_NONDUR\_REGISTRATIONS

| Column | Datatype | Description |
| --- | --- | --- |
| `REG_ID` | `NUMBER` | Registration ID |
| `SUBSCRIPTION` | `VARCHAR2(128)` | Subscription name |
| `LOCATION` | `VARCHAR2(256)` | Location name |
| `USER#` | `NUMBER` | User ID |
| `USER_CONTEXT` | `RAW(32)` | Context the user provided |
| `CONTEXT_SIZE` | `NUMBER` | Size of the context |
| `NAMESPACE` | `NUMBER` | Subscription namespace |
| `VERSION` | `NUMBER` | Database version number |
| `STATE` | `NUMBER` | State of the registration:  - `ENABLED`: The registration is enabled for notification - `STOPPING`: The registration is in a transient state before it becomes `DISABLED` - `DISABLED`: The registration is disabled for notification - `DEAD`: The registration does not exist any more, and it is marked for deferred cleanup. |
| `QOS` | `NUMBER` | Quality of service |
| `REG_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Time of registration |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

[Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADQUE0100) for more information about Oracle Database Advanced Queueing