---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_PARAMETER.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.17 DBA\_HIST\_PARAMETER

`DBA_HIST_PARAMETER` displays historical information about the initialization parameters that were in effect for the instance.

This view contains snapshots of `V$SYSTEM_PARAMETER`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `PARAMETER_HASH` | `NUMBER` | `NOT NULL` | Parameter hash |
| `PARAMETER_NAME` | `VARCHAR2(64)` | `NOT NULL` | Name of the parameter |
| `VALUE` | `VARCHAR2(512)` |  | Parameter value for the session (if modified within the session); otherwise, the instance-wide parameter value |
| `ISDEFAULT` | `VARCHAR2(9)` |  | Indicates whether the parameter is set to the default value (`TRUE`) or the parameter value was specified in the parameter file (`FALSE`) |
| `ISMODIFIED` | `VARCHAR2(10)` |  | Indicates whether the parameter has been modified after instance startup:  - `MODIFIED` - Parameter has been modified with `ALTER SESSION` - `SYSTEM_MOD` - Parameter has been modified with `ALTER SYSTEM` (which causes all the currently logged in sessions' values to be modified) - `FALSE` - Parameter has not been modified after instance startup |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$SYSTEM\_PARAMETER](V-SYSTEM_PARAMETER.md) "