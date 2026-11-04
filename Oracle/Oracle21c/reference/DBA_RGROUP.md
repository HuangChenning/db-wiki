---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_RGROUP.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.292 DBA\_RGROUP

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `REFGROUP` | `NUMBER` |  | Internal identifier of the refresh group |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the object in the refresh group |
| `NAME ` | `VARCHAR2(128)` | `NOT NULL` | Name of the object in the refresh group |
| `IMPLICIT_DESTROY` | `VARCHAR2(1)` |  | Indicates whether the refresh group is destroyed when its last item is removed (`Y`) or not (`N`) |
| `PUSH_DEFERRED_RPC` | `VARCHAR2(1)` |  | Indicates whether changes are pushed from the snapshot to the master before refresh (`Y`) or not (`N`) |
| `REFRESH_AFTER_ERRORS` | `VARCHAR2(1)` |  | Indicates whether to proceed with refresh despite errors when pushing deferred RPCs (`Y`) or not (`N`) |
| `ROLLBACK_SEG` | `VARCHAR2(128)` |  | Name of the rollback segment to use while refreshing |
| `JOB` | `NUMBER` | `NOT NULL` | Identifier of the job used to refresh the group automatically |
| `PURGE_OPTION` | `NUMBER(38)` |  | Method for purging the transaction queue after each push. `1` indicates quick purge option; `2` indicates precise purge option |
| `PARALLELISM` | `NUMBER(38)` |  | Level of parallelism for transaction propagation |
| `HEAP_SIZE` | `NUMBER(38)` |  | Size of the heap |
| `JOB_NAME` | `VARCHAR2(128)` |  | The name of the job used to automatically refresh the group |