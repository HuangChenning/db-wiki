---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_REFRESH.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.24 ALL\_REFRESH

`ALL_REFRESH` describes all the refresh groups accessible to the current user.

Related Views

- `DBA_REFRESH` describes all refresh groups in the database.
- `USER_REFRESH` describes all refresh groups owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ROWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the refresh group |
| `RNAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the refresh group |
| `REFGROUP` | `NUMBER` |  | Internal identifier of the refresh group |
| `IMPLICIT_DESTROY ` | `VARCHAR2(1)` |  | Indicates whether the refresh group is destroyed when its last item is subtracted (`Y`) or not (`N`) |
| `PUSH_DEFERRED_RPC` | `VARCHAR2(1)` |  | Indicates whether changes are pushed from the snapshot to the master before refresh (`Y`) or not (`N`) |
| `REFRESH_AFTER _ERRORS` | `VARCHAR2(1)` |  | Indicates whether to proceed with refresh despite errors when pushing deferred RPCs (`Y`) or not (`N`) |
| `ROLLBACK_SEG` | `VARCHAR2(128)` |  | Name of the rollback segment to use while refreshing |
| `JOB` | `NUMBER` |  | Identifier of the job used to refresh the group automatically |
| `NEXT_DATE ` | `DATE` |  | Date that this job will next be refreshed automatically, if not broken |
| `INTERVAL` | `VARCHAR2(200)` |  | A date function used to compute the next `NEXT_DATE` |
| `BROKEN` | `VARCHAR2(1)` |  | Indicates whether the job is broken and will never be run (`Y`) or not (`N`) |
| `PURGE_OPTION` | `NUMBER(38)` |  | Method for purging the transaction queue after each push (`1` indicates quick purge option; `2` indicates precise purge option) |
| `PARALLELISM` | `NUMBER(38)` |  | Level of parallelism for transaction propagation |
| `HEAP_SIZE` | `NUMBER(38)` |  | Size of the heap |
| `JOB_NAME` | `VARCHAR2(128)` |  | The name of the job used to automatically refresh the group |

See Also:

- " [DBA\_REFRESH](DBA_REFRESH.md) "
- " [USER\_REFRESH](USER_REFRESH.md) "