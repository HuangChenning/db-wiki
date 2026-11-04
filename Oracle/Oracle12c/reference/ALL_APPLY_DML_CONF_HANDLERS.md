---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_APPLY_DML_CONF_HANDLERS.html
tags:
  - oracle
  - 12c
  - reference
---

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

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

" [DBA\_APPLY\_DML\_CONF\_HANDLERS](DBA_APPLY_DML_CONF_HANDLERS.md) "