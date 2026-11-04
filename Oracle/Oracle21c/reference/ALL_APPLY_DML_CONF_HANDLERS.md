---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_APPLY_DML_CONF_HANDLERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.65 ALL\_APPLY\_DML\_CONF\_HANDLERS

`ALL_APPLY_DML_CONF_HANDLERS` provides details about DML conflict handlers on objects visible to the current user.

Related View

`DBA_APPLY_DML_CONF_HANDLERS` provides details about DML conflict handlers.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `APPLY_NAME` | `VARCHAR2(128)` |  | Name of the apply process |
| `OBJECT_OWNER` | `VARCHAR2(128)` |  | Owner of the target object |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Name of the target object |
| `SOURCE_OBJECT_OWNER` | `VARCHAR2(128)` |  | Source database owner of the object |
| `SOURCE_OBJECT_NAME` | `VARCHAR2(128)` |  | Source database name of the object |
| `COMMAND_TYPE` | `VARCHAR2(6)` |  | Type of the DML operation: `INSERT`, `UPDATE`, or `DELETE` |
| `CONFLICT_TYPE` | `VARCHAR2(11)` |  | Type of conflict:  - `ROW EXISTS` - `ROW MISSING` |
| `METHOD_NAME` | `VARCHAR2(9)` |  | Method used for resolving the error, depending on the conflict type:  - `OVERWRITE` - `RECORD` - `IGNORE` - `MAXIMUM` - `MINIMUM` - `DELTA` |
| `CONFLICT_HANDLER_NAME` | `VARCHAR2(128)` |  | Name of the conflict handler |
| `RESOLUTION_COLUMN` | `VARCHAR2(128)` |  | Name of the column used to resolve the conflict for `MAXIMUM`, `MINIMUM`, and `DELTA` |
| `SET_BY` | `VARCHAR2(10)` |  | Entity that set up the handler:  - `USER` - `GOLDENGATE` |

See Also:

" [DBA\_APPLY\_DML\_CONF\_HANDLERS](DBA_APPLY_DML_CONF_HANDLERS.md) "