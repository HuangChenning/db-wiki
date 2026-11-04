---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_HIST_SQL_BIND_METADATA.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_HIST_SQL_BIND_METADATA` displays historical information on metadata for bind variables used by SQL cursors.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `SQL_ID` | `VARCHAR2(13)` | `NOT NULL` | SQL identifier of the parent cursor in the library cache |
| `NAME` | `VARCHAR2(128)` |  | Name of the bind variable |
| `POSITION` | `NUMBER` | `NOT NULL` | Position of the bind variable in the SQL statement |
| `DUP_POSITION` | `NUMBER` |  | If the binding is performed by name and the bind variable is duplicated, then this column gives the position of the primary bind variable |
| `DATATYPE` | `NUMBER` |  | Internal identifier for the bind data type. Beginning in Oracle Database 12c, a number representing a PL/SQL data type can appear in this column. |
| `DATATYPE_STRING` | `VARCHAR2(15)` |  | Textual representation of the bind data type. Beginning in Oracle Database 12c, a text representation of a PL/SQL-only data type can appear in this column. If the actual data type is a PL/SQL sub type, the name of the data type, not the sub type will be displayed. |
| `CHARACTER_SID` | `NUMBER` |  | National character set identifier |
| `PRECISION` | `NUMBER` |  | Precision (for numeric binds) |
| `SCALE` | `NUMBER` |  | Scale (for numeric binds) |
| `MAX_LENGTH` | `NUMBER` |  | Maximum bind length |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |