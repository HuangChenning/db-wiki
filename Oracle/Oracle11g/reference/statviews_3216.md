---
title: DBA_HIST_DATAFILE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3216.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_DATAFILE` displays a history of the datafile information from the control file. This view contains snapshots of `V$DATAFILE`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `FILE#` | `NUMBER` | `NOT NULL` | File identification number |
| `CREATION_CHANGE#` | `NUMBER` | `NOT NULL` | Change number at which the datafile was created |
| `FILENAME` | `VARCHAR2(513)` | `NOT NULL` | Name of the datafile |
| `TS#` | `NUMBER` | `NOT NULL` | Tablespace number |
| `TSNAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the tablespace |
| `BLOCK_SIZE` | `NUMBER` |  | Block size of the datafile |