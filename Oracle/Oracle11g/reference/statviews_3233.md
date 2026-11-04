---
title: DBA_HIST_IOSTAT_FILETYPE_NAME
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3233.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_IOSTAT_FILETYPE_NAME` displays historical I/O statistics for file type names. This view contains snapshots of `V$IOSTAT_FILE`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `FILETYPE_ID` | `NUMBER` | `NOT NULL` | Type of file (for example, log file, data file, and so on) |
| `FILETYPE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the file, in the case of a data file or temp file. For all other files, a corresponding string to be displayed (for example, `ARCHIVELOG`). |