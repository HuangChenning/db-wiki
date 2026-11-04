---
title: DBA_HIST_PARAMETER
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4017.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_PARAMETER` displays historical information about the initialization parameters that were in effect for the instance. This view contains snapshots of `V$SYSTEM_PARAMETER`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` |  | Unique snapshot ID |
| `DBID` | `NUMBER` |  | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` |  | Instance number for the snapshot |
| `PARAMETER_HASH` | `NUMBER` |  | Parameter hash |
| `PARAMETER_NAME` | `VARCHAR2(64)` |  | Name of the parameter |
| `VALUE` | `VARCHAR2(512)` |  | Parameter value for the session (if modified within the session); otherwise, the instance-wide parameter value |
| `ISDEFAULT` | `VARCHAR2(9)` |  | Indicates whether the parameter is set to the default value (`TRUE`) or the parameter value was specified in the parameter file (`FALSE`) |
| `ISMODIFIED` | `VARCHAR2(10)` |  | Indicates whether the parameter has been modified after instance startup: - `MODIFIED` - Parameter has been modified with `ALTER SESSION` - `SYSTEM_MOD` - Parameter has been modified with `ALTER SYSTEM` (which causes all the currently logged in sessions' values to be modified) - `FALSE` - Parameter has not been modified after instance startup |