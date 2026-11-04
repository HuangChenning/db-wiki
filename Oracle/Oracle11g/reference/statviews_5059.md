---
title: DBA_TABLESPACE_USAGE_METRICS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5059.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_TABLESPACE_USAGE_METRICS` describes tablespace usage metrics for all types of tablespaces, including permanent, temporary, and undo tablespaces.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Tablespace name |
| `USED_SPACE` | `NUMBER` |  | Total space consumed by the tablespace, in database blocks |
| `TABLESPACE_SIZE` | `NUMBER` |  | Maximum size of the tablespace, in database blocks |
| `USED_PERCENT` | `NUMBER` |  | Percentage of used space, as a function of the maximum possible tablespace size |