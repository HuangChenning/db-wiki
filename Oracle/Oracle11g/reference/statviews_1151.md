---
title: ALL_MVIEW_LOGS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1151.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_MVIEW_LOGS` describes all materialized view logs accessible to the current user.

Related Views

- `DBA_MVIEW_LOGS` describes all materialized view logs in the database.
- `USER_MVIEW_LOGS` describes all materialized view logs owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `LOG_OWNER` | `VARCHAR2(30)` |  | Owner of the materialized view log |
| `MASTER` | `VARCHAR2(30)` |  | Name of the master table or master materialized view whose changes are logged |
| `LOG_TABLE` | `VARCHAR2(30)` |  | Name of the table where the changes to the master table or master materialized view are logged |
| `LOG_TRIGGER` | `VARCHAR2(30)` |  | Obsolete with Oracle8i and later. Set to NULL. Formerly, this parameter was an after-row trigger on the master which inserted rows into the log. |
| `ROWIDS` | `VARCHAR2(3)` |  | Indicates whether rowid information is recorded (`YES`) or not (`NO`) |
| `PRIMARY_KEY` | `VARCHAR2(3)` |  | Indicates whether primary key information is recorded (`YES`) or not (`NO`) |
| `OBJECT_ID` | `VARCHAR2(3)` |  | Indicates whether object identifier information in an object table is recorded (`YES`) or not (`NO`) |
| `FILTER_COLUMNS` | `VARCHAR2(3)` |  | Indicates whether filter column information is recorded (`YES`) or not (`NO`) |
| `SEQUENCE` | `VARCHAR2(3)` |  | Indicates whether the sequence value, which provides additional ordering information, is recorded (`YES`) or not (`NO`) |
| `INCLUDE_NEW_VALUES` | `VARCHAR2(3)` |  | Indicates whether both old and new values are recorded (`YES`) or old values are recorded but new values are not recorded (`NO`) |
| `PURGE_ASYNCHRONOUS` | `VARCHAR2(3)` |  | Indicates whether the materialized view log is purged asynchronously (`YES`) or not (`NO`) |
| `PURGE_DEFERRED` | `VARCHAR2(3)` |  | Indicates whether the materialized view log is purged in a deferred manner (`YES`) or not (`NO`) |
| `PURGE_START` | `DATE` |  | For deferred purge, the purge start date |
| `PURGE_INTERVAL` | `VARCHAR2(200)` |  | For deferred purge, the purge interval |
| `LAST_PURGE_DATE` | `DATE` |  | Date of the last purge |
| `LAST_PURGE_STATUS` | `NUMBER` |  | Status of the last purge (error code or `0` for success) |
| `NUM_ROWS_PURGED` | `NUMBER` |  | Number of rows purged in the last purge |
| `COMMIT_SCN_BASED` | `VARCHAR2(3)` |  | Indicates whether the materialized view log is commit SCN-based (`YES`) or not (`NO`) |

See Also:

- ["DBA\_MVIEW\_LOGS"](statviews_4147.md)
- ["USER\_MVIEW\_LOGS"](statviews_5366.md)