---
title: DBA_RGROUP
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4218.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_RGROUP` displays all refresh groups.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `REFGROUP` | `NUMBER` |  | Internal identifier of the refresh group |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the object in the refresh group |
| `NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object in the refresh group |
| `IMPLICIT_DESTROY` | `VARCHAR2(1)` |  | Indicates whether the refresh group is destroyed when its last item is removed (`Y`) or not (`N`) |
| `PUSH_DEFERRED_RPC` | `VARCHAR2(1)` |  | Indicates whether changes are pushed from the snapshot to the master before refresh (`Y`) or not (`N`) |
| `REFRESH_AFTER_ERRORS` | `VARCHAR2(1)` |  | Indicates whether to proceed with refresh despite errors when pushing deferred RPCs (`Y`) or not (`N`) |
| `ROLLBACK_SEG` | `VARCHAR2(30)` |  | Name of the rollback segment to use while refreshing |
| `JOB` | `NUMBER` | `NOT NULL` | Identifier of the job used to refresh the group automatically |
| `PURGE_OPTION` | `NUMBER(38)` |  | Method for purging the transaction queue after each push. `1` indicates quick purge option; `2` indicates precise purge option |
| `PARALLELISM` | `NUMBER(38)` |  | Level of parallelism for transaction propagation |
| `HEAP_SIZE` | `NUMBER(38)` |  | Size of the heap |