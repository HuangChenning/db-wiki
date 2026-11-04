---
title: DBA_TS_QUOTAS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5068.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_TS_QUOTAS` describes tablespace quotas for all users.

Related View

`USER_TS_QUOTAS` describes tablespace quotas for the current user. This view does not display the `USERNAME` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Tablespace name |
| `USERNAME` | `VARCHAR2(30)` | `NOT NULL` | User with resource rights on the tablespace |
| `BYTES` | `NUMBER` |  | Number of bytes charged to the user |
| `MAX_BYTES` | `NUMBER` |  | User's quota in bytes, or `-1` if no limit |
| `BLOCKS` | `NUMBER` | `NOT NULL` | Number of Oracle blocks charged to the user |
| `MAX_BLOCKS` | `NUMBER` |  | User's quota in Oracle blocks, or `-1` if no limit |
| `DROPPED` | `VARCHAR2(3)` |  | Whether the tablespace has been dropped |