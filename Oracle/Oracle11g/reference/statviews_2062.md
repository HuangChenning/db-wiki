---
title: ALL_SEQUENCES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2062.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SEQUENCES` describes all sequences accessible to the current user.

Related Views

- `DBA_SEQUENCES` describes all sequences in the database.
- `USER_SEQUENCES` describes all sequences owned by the current user. This view does not display the `SEQUENCE_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SEQUENCE_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the sequence |
| `SEQUENCE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Sequence name |
| `MIN_VALUE` | `NUMBER` |  | Minimum value of the sequence |
| `MAX_VALUE` | `NUMBER` |  | Maximum value of the sequence |
| `INCREMENT_BY` | `NUMBER` | `NOT NULL` | Value by which sequence is incremented |
| `CYCLE_FLAG` | `VARCHAR2(1)` |  | Indicates whether the sequence wraps around on reaching the limit (`Y`) or not (`N`) |
| `ORDER_FLAG` | `VARCHAR2(1)` |  | Indicates whether sequence numbers are generated in order (`Y`) or not (`N`) |
| `CACHE_SIZE` | `NUMBER` | `NOT NULL` | Number of sequence numbers to cache |
| `LAST_NUMBER` | `NUMBER` | `NOT NULL` | Last sequence number written to disk. If a sequence uses caching, the number written to disk is the last number placed in the sequence cache. This number is likely to be greater than the last sequence number that was used. |