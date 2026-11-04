---
title: DBA_HIST_SQLBIND
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4050.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_SQLBIND` displays historical information on bind variables used by SQL cursors. This view contains snapshots of `V$SQL_BIND_CAPTURE`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` |  | Unique snapshot ID |
| `DBID` | `NUMBER` |  | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` |  | Instance number for the snapshot |
| `SQL_ID` | `VARCHAR2(13)` |  | SQL identifier of the parent cursor in the library cache |
| `NAME` | `VARCHAR2(30)` |  | Name of the bind variable |
| `POSITION` | `NUMBER` |  | Position of the bind variable in the SQL statement |
| `DUP_POSITION` | `NUMBER` |  | If the binding is performed by name and the bind variable is duplicated, then this column gives the position of the primary bind variable. |
| `DATATYPE` | `NUMBER` |  | Internal identifier for the bind datatype |
| `DATATYPE_STRING` | `VARCHAR2(15)` |  | Textual representation of the bind datatype |
| `CHARACTER_SID` | `NUMBER` |  | National character set identifier |
| `PRECISION` | `NUMBER` |  | Precision (for numeric binds) |
| `SCALE` | `NUMBER` |  | Scale (for numeric binds) |
| `MAX_LENGTH` | `NUMBER` |  | Maximum bind length |
| `WAS_CAPTURED` | `VARCHAR2(3)` |  | Indicates whether the bind value was captured (`YES`) or not (`NO`) |
| `LAST_CAPTURED` | `DATE` |  | Date when the bind value was captured. Bind values are captured when SQL statements are executed. To limit the overhead, binds are captured at most every 15 minutes for a given cursor. |
| `VALUE_STRING` | `VARCHAR2(4000)` |  | Value of the bind represented as a string |
| `VALUE_ANYDATA` | `ANYDATA` |  | Value of the bind represented using the self-descriptive `Sys.AnyData` datatype. This representation is useful to programmatically decode the value of the bind variable. |