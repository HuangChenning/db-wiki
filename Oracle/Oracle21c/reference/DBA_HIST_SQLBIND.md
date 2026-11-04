---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_SQLBIND.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.63 DBA\_HIST\_SQLBIND

`DBA_HIST_SQLBIND` displays historical information on bind variables used by SQL cursors.

This view contains snapshots of `V$SQL_BIND_CAPTURE`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `SQL_ID` | `VARCHAR2(13)` | `NOT NULL` | SQL identifier of the parent cursor in the library cache |
| `NAME` | `VARCHAR2(128)` |  | Name of the bind variable |
| `POSITION` | `NUMBER` | `NOT NULL` | Position of the bind variable in the SQL statement |
| `DUP_POSITION` | `NUMBER` |  | If the binding is performed by name and the bind variable is duplicated, then this column gives the position of the primary bind variable. |
| `DATATYPE` | `NUMBER` |  | Internal identifier for the bind data type. Beginning in Oracle Database 12c, a number representing a PL/SQL data type can appear in this column. |
| `DATATYPE_STRING` | `VARCHAR2(15)` |  | Textual representation of the bind data type. Beginning in Oracle Database 12c, a text representation of a PL/SQL-only data type can appear in this column. If the actual data type is a PL/SQL sub type, the name of the data type, not the sub type will be displayed. |
| `CHARACTER_SID` | `NUMBER` |  | National character set identifier |
| `PRECISION` | `NUMBER` |  | Precision (for numeric binds) |
| `SCALE` | `NUMBER` |  | Scale (for numeric binds) |
| `MAX_LENGTH` | `NUMBER` |  | Maximum bind length |
| `WAS_CAPTURED` | `VARCHAR2(3)` |  | Indicates whether the bind value was captured (`YES`) or not (`NO`) |
| `LAST_CAPTURED` | `DATE` |  | Date when the bind value was captured. Bind values are captured when SQL statements are executed. To limit the overhead, binds are captured at most every 15 minutes for a given cursor. |
| `VALUE_STRING` | `VARCHAR2(4000)` |  | Value of the bind represented as a string |
| `VALUE_ANYDATA` | `ANYDATA` |  | Value of the bind represented using the self-descriptive `Sys.AnyData` data type. This representation is useful to programmatically decode the value of the bind variable. This column is NULL if a PL/SQL-only data type appears in the `DATATYPE` column. |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$SQL\_BIND\_CAPTURE](V-SQL_BIND_CAPTURE.md) "