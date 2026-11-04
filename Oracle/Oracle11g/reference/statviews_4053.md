---
title: DBA_HIST_SQLTEXT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4053.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_SQLTEXT` displays the text of SQL statements belonging to shared SQL cursors captured in the Workload Repository. This view captures information from `V$SQL` and is used with the `DBA_HIST_SQLSTAT` view.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `SQL_ID` | `VARCHAR2(13)` | `NOT NULL` | SQL identifier of the parent cursor in the library cache |
| `SQL_TEXT` | `CLOB` |  | Full text for the SQL statement exposed as a CLOB column |
| `COMMAND_TYPE` | `NUMBER` |  | Oracle command type definition |