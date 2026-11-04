---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_TABLESPACE_USAGE_METRICS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.49 DBA\_TABLESPACE\_USAGE\_METRICS

`DBA_TABLESPACE_USAGE_METRICS` describes tablespace usage metrics for all types of tablespaces, including permanent, temporary, and undo tablespaces.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Tablespace name |
| `USED_SPACE` | `NUMBER` |  | Total space consumed by all objects created in the tablespace, expressed as number of data blocks  For undo tablespaces, the value of this column includes space consumed by both expired and unexpired undo segments. |
| `TABLESPACE_SIZE` | `NUMBER` |  | The maximum size of the tablespace, expressed as number of data blocks  - If the tablespace contains any datafiles with autoextend enabled, then this column displays the maximum size to which the tablespace can grow. Underlying storage free space, such as Oracle ASM or file system storage, is taken into account when computing this value. If the value of the `MAX_PDB_STORAGE` property of the `CDB_PROPERTIES` view is non-zero, then that value is also taken into account. 	For example: 	- If a tablespace has a current size of 5 GB, the combined maximum size of its datafiles is 32 GB, and its underlying storage has 20 GB of free space, then this column will have a value of approximately 25 GB. 		- If a tablespace has a current size of 10 GB, the combined maximum size of its datafiles is 20 GB, and its underlying storage has 25 GB of free space, then this column will have a value of approximately 20 GB. 		- If a tablespace has a current size of 15 GB, the combined maximum size of its datafiles is 32 GB, its underlying storage has 90 GB of free space, the current PDB size is 40 GB, and `MAX_PDB_STORAGE` is 50 GB, then this column will have a value of approximately 25 GB. - If the tablespace contains only datafiles with autoextend disabled, then this column displays the combined size of all datafiles in the tablespace. |
| `USED_PERCENT` | `NUMBER` |  | Percentage of used space, as a function of the maximum possible tablespace size |