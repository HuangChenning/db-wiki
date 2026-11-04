---
title: "V$SQL_BIND_CAPTURE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3044.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SQL_BIND_CAPTURE` displays information on bind variables used by SQL cursors. Each row in the view contains information for one bind variable defined in a cursor. This includes:

- Reference to the cursor defining the bind variable
	(`hash_value`, `address`) for the parent cursor and (`hash_value`, `child_address`) for the child cursor.
- Bind metadata
	Name, position, datatype, character set ID, precision, scale, and maximum length of the bind variable.
- Bind data
	One of the bind values used for the bind variable during a past execution of its associated SQL statement. Bind values are not always captured for this view. Bind values are displayed by this view only when the type of the bind variable is simple (this excludes LONG, LOB, and ADT datatypes) and when the bind variable is used in the `WHERE` or `HAVING` clauses of the SQL statement.

Bind capture is disabled when the `STATISTICS_LEVEL` initialization parameter is set to `BASIC`. This view can be joined with `V$SQLAREA` on (`HASH_VALUE`, `ADDRESS`) and with `V$SQL` on (`HASH_VALUE`, `CHILD_ADDRESS`).

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDRESS` | `RAW(4 \| 8)` | Address of the parent cursor |
| `HASH_VALUE` | `NUMBER` | Hash value of the parent cursor in the library cache. The hash value is a fixed index for the view and should always be used to speed up access to the view. |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of the parent cursor in the library cache |
| `CHILD_ADDRESS` | `RAW(4 \| 8)` | Address of the child cursor |
| `CHILD_NUMBER` | `NUMBER` | Child cursor number |
| `NAME` | `VARCHAR2(30)` | Name of the bind variable |
| `POSITION` | `NUMBER` | Position of the bind variable in the SQL statement |
| `DUP_POSITION` | `NUMBER` | If the binding is performed by name and the bind variable is duplicated, then this column gives the position of the primary bind variable. |
| `DATATYPE` | `NUMBER` | Internal identifier for the bind datatype |
| `DATATYPE_STRING` | `VARCHAR2(15)` | Textual representation of the bind datatype |
| `CHARACTER_SID` | `NUMBER` | National character set identifier |
| `PRECISION` | `NUMBER` | Precision (for numeric binds) |
| `SCALE` | `NUMBER` | Scale (for numeric binds) |
| `MAX_LENGTH` | `NUMBER` | Maximum bind length |
| `WAS_CAPTURED` | `VARCHAR2(3)` | Indicates whether the bind value was captured (`YES`) or not (`NO`) |
| `LAST_CAPTURED` | `DATE` | Date when the bind value was captured. Bind values are captured when SQL statements are executed. To limit the overhead, binds are captured at most every 15 minutes for a given cursor. |
| `VALUE_STRING` | `VARCHAR2(4000)` | Value of the bind represented as a string |
| `VALUE_ANYDATA` | `ANYDATA` | Value of the bind represented using the `ANYDATA` datatype. This representation is useful to programmatically decode the value of the bind variable. |