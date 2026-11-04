---
title: DBA_HIST_SQL_BIND_METADATA
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4046.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_SQL_BIND_METADATA` displays historical information on metadata for bind variables used by SQL cursors.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `SQL_ID` | `VARCHAR2(13)` | `NOT NULL` | SQL identifier of the parent cursor in the library cache |
| `NAME` | `VARCHAR2(30)` |  | Name of the bind variable |
| `POSITION` | `NUMBER` | `NOT NULL` | Position of the bind variable in the SQL statement |
| `DUP_POSITION` | `NUMBER` |  | If the binding is performed by name and the bind variable is duplicated, then this column gives the position of the primary bind variable |
| `DATATYPE` | `NUMBER` |  | Internal identifier for the bind datatype |
| `DATATYPE_STRING` | `VARCHAR2(15)` |  | Textual representation of the bind datatype |
| `CHARACTER_SID` | `NUMBER` |  | National character set identifier |
| `PRECISION` | `NUMBER` |  | Precision (for numeric binds) |
| `SCALE` | `NUMBER` |  | Scale (for numeric binds) |
| `MAX_LENGTH` | `NUMBER` |  | Maximum bind length |