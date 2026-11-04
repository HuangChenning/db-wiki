---
title: DBA_TEMP_FREE_SPACE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5062.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_TEMP_FREE_SPACE` displays temporary space usage information at tablespace level.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the tablespace |
| `TABLESPACE_SIZE` | `NUMBER` |  | Total size of the tablespace, in bytes |
| `ALLOCATED_SPACE` | `NUMBER` |  | Total allocated space, in bytes, including space that is currently allocated and used and space that is currently allocated and available for reuse |
| `FREE_SPACE` | `NUMBER` |  | Total free space available, in bytes, including space that is currently allocated and available for reuse and space that is currently unallocated |