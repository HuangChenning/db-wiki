---
title: "V$FILESPACE_USAGE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1140.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$FILESPACE_USAGE` summarizes space allocation information of each datafile and tempfile.

| Column | Datatype | Description |
| --- | --- | --- |
| `TABLESPACE_ID` | `NUMBER` | ID of the tablespace to which the file belongs |
| `RFNO` | `NUMBER` | Relative file number of the file |
| `ALLOCATED_SPACE` | `NUMBER` | Total allocated space in the file |
| `FILE_SIZE` | `NUMBER` | Current file size |
| `FILE_MAXSIZE` | `NUMBER` | Maximum file size |
| `CHANGESCN_BASE` | `NUMBER` | SCN base of the last change to the file |
| `CHANGESCN_WRAP` | `NUMBER` | SCN wrap of the last change to the file |
| `FLAG` | `NUMBER` | Flags for file attributes |