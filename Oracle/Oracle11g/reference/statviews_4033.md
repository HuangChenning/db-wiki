---
title: DBA_HIST_SEG_STAT_OBJ
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4033.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_SEG_STAT_OBJ` displays all the names of the segments captured in the workload repository. This view is used with the `DBA_HIST_SEG_STAT` view.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `TS#` | `NUMBER` | `NOT NULL` | Tablespace number |
| `OBJ#` | `NUMBER` | `NOT NULL` | Dictionary object number |
| `DATAOBJ#` | `NUMBER` | `NOT NULL` | Data object number |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the object |
| `OBJECT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object |
| `SUBOBJECT_NAME` | `VARCHAR2(30)` |  | Name of the subobject |
| `OBJECT_TYPE` | `VARCHAR2(18)` |  | Type of the object |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Tablespace Name for the object |
| `PARTITION_TYPE` | `VARCHAR2(8)` |  | Partition Type, if relevant |