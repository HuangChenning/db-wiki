---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_TABLESPACE_USAGE_METRICS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_TABLESPACE_USAGE_METRICS` describes tablespace usage metrics for all types of tablespaces, including permanent, temporary, and undo tablespaces.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Tablespace name |
| `USED_SPACE` | `NUMBER` |  | Total space consumed by the tablespace, in database blocks  For undo tablespaces, the value of this column includes space consumed by both expired and unexpired undo segments. |
| `TABLESPACE_SIZE` | `NUMBER` |  | Tablespace size, in database blocks  - If the tablespace contains any datafiles with autoextend enabled, then this column displays the amount of underlying storage free space for the tablespace. For example, if the current tablespace size is 1 GB, the combined maximum size of all of its datafiles is 32 GB, and its underlying storage (for example, ASM or file system storage) has 20 GB of free space, then this column will have a value of approximately 20 GB. - If the tablespace contains only datafiles with autoextend disabled, then this column displays the allocated space for the entire tablespace, that is, the combined size of all datafiles in the tablespace. Datafile size can be obtained by querying the `BLOCKS` column of the `DBA_DATA_FILES` view. |
| `USED_PERCENT` | `NUMBER` |  | Percentage of used space, as a function of the maximum possible tablespace size |