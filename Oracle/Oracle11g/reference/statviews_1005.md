---
title: ALL_APPLY_CHANGE_HANDLERS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1005.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_APPLY_CHANGE_HANDLERS` displays information about the change handlers on the tables accessible to the current user.

Related View

`DBA_APPLY_CHANGE_HANDLERS` displays information about the change handlers on all tables in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CHANGE_TABLE_OWNER` | `VARCHAR2(30)` |  | Owner of the change table |
| `CHANGE_TABLE_NAME` | `VARCHAR2(30)` |  | Name of the change table |
| `SOURCE_TABLE_OWNER` | `VARCHAR2(30)` |  | Owner of the source table |
| `SOURCE_TABLE_NAME` | `VARCHAR2(30)` |  | Name of the source table |
| `HANDLER_NAME` | `VARCHAR2(30)` |  | Name of the statement-based change handler |
| `CAPTURE_VALUES` | `VARCHAR2(3)` |  | Indicates whether to capture the old (`OLD`), new (`NEW`), or both (`*`) values |
| `APPLY_NAME` | `VARCHAR2(30)` |  | Name of the apply process |
| `OPERATION_NAME` | `VARCHAR2(10)` |  | Name of the DML operation to which the DML handler is set: |
| `CREATION_TIME` | `TIMESTAMP(6)` |  | Change handler creation time |
| `MODIFICATION_TIME` | `TIMESTAMP(6)` |  | Change handler modification time |

See Also:

["DBA\_APPLY\_CHANGE\_HANDLERS"](statviews_3048.md)