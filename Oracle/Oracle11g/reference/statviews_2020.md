---
title: ALL_REFRESH
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2020.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_REFRESH` describes all the refresh groups accessible to the current user.

Related Views

- `DBA_REFRESH` describes all refresh groups in the database.
- `USER_REFRESH` describes all refresh groups owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ROWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the refresh group |
| `RNAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the refresh group |
| `REFGROUP` | `NUMBER` |  | Internal identifier of the refresh group |
| `IMPLICIT_DESTROY` | `VARCHAR2(1)` |  | Indicates whether the refresh group is destroyed when its last item is subtracted (`Y`) or not (`N`) |
| `PUSH_DEFERRED_RPC` | `VARCHAR2(1)` |  | Indicates whether changes are pushed from the snapshot to the master before refresh (`Y`) or not (`N`) |
| `REFRESH_AFTER   _ERRORS` | `VARCHAR2(1)` |  | Indicates whether to proceed with refresh despite errors when pushing deferred RPCs (`Y`) or not (`N`) |
| `ROLLBACK_SEG` | `VARCHAR2(30)` |  | Name of the rollback segment to use while refreshing |
| `JOB` | `NUMBER` |  | Identifier of the job used to refresh the group automatically |
| `NEXT_DATE` | `DATE` |  | Date that this job will next be refreshed automatically, if not broken |
| `INTERVAL` | `VARCHAR2(200)` |  | A date function used to compute the next `NEXT_DATE` |
| `BROKEN` | `VARCHAR2(1)` |  | Indicates whether the job is broken and will never be run (`Y`) or not (`N`) |
| `PURGE_OPTION` | `NUMBER(38)` |  | Method for purging the transaction queue after each push (`1` indicates quick purge option; `2` indicates precise purge option) |
| `PARALLELISM` | `NUMBER(38)` |  | Level of parallelism for transaction propagation |
| `HEAP_SIZE` | `NUMBER(38)` |  | Size of the heap |