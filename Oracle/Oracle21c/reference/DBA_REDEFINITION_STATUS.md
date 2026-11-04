---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_REDEFINITION_STATUS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.273 DBA\_REDEFINITION\_STATUS

`DBA_REDEFINITION_STATUS` is an online redefinition view. It provides information about the online redefinition status.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `REDEFINITION_ID` | `NUMBER(38)` | `NOT NULL` | ID for the redefinition object |
| `BASE_TABLE_OWNER` | `VARCHAR2(128)` |  | Owner of the base table of the redefinition object |
| `BASE_TABLE_NAME` | `VARCHAR2(128)` |  | Name of the base table of the redefinition object |
| `BASE_OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the base object of the redefinition object |
| `BASE_OBJECT_TYPE` | `VARCHAR2(9)` |  | Type of the base object of the redefinition object |
| `INTERIM_OBJECT_OWNER` | `VARCHAR2(128)` |  | Owner of the interim object of the redefinition object |
| `INTERIM_OBJECT_NAME` | `VARCHAR2(128)` |  | Name of the interim object of the redefinition object |
| `OPERATION` | `VARCHAR2(128)` | `NOT NULL` | The current redefinition operation:  - `START_REDEF_TABLE` - `SYNC_INTERIM_TABLE` - `COPY_TABLE_DEPENDENTS` - `FINISH_REDEF_TABLE` |
| `STATUS` | `VARCHAR2(128)` | `NOT NULL` | Status of the previous redefinition operation:  - `FAILURE` - `SUCCESS` |
| `RESTARTABLE` | `VARCHAR2(1)` | `NOT NULL` | Indicates whether the previous operation can be restarted |
| `ERR_TXT` | `VARCHAR2(1000)` |  | The error message raised from the previous operation |
| `ACTION` | `VARCHAR2(400)` |  | The suggested action |
| `REFRESH_DEP_MVIEWS` | `VARCHAR2(1)` |  | Indicates whether the online redefinition will also refresh dependent materialized views when syncing the interim table (`Y`) or not (`N`) |

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN11668) for more information about online redefinition