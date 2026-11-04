---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_MVIEW_LOGS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.287 ALL\_MVIEW\_LOGS

`ALL_MVIEW_LOGS` describes all materialized view logs accessible to the current user.

Related Views

- `DBA_MVIEW_LOGS` describes all materialized view logs in the database.
- `USER_MVIEW_LOGS` describes all materialized view logs owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `LOG_OWNER` | `VARCHAR2(128)` |  | Owner of the materialized view log |
| `MASTER` | `VARCHAR2(128)` |  | Name of the master table or master materialized view whose changes are logged |
| `LOG_TABLE` | `VARCHAR2(128)` |  | Name of the table where the changes to the master table or master materialized view are logged |
| `LOG_TRIGGER` | `VARCHAR2(128)` |  | Obsolete with Oracle8i and later. Set to NULL. Formerly, this parameter was an after-row trigger on the master which inserted rows into the log. |
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
| `STAGING_LOG` | `VARCHAR2(3)` |  | Indicates whether the materialized view log is a staging log for synchronous refresh (`YES`) or not (`NO`) |
| `AUTO` <sup>Foot 1</sup> | `VARCHAR2(6)` |  | Indicates whether the materialized view log is an automatic materialized view log. Possible values:  - `YES` - It is an automatic materialized view log - `NO` - It is a user-created materialized view log - `HYBRID` - It is a hybrid materialized view log. It was initially a user-created materialized view log and was subsequently altered automatically to include one or more additional columns to support an automatic materialized view. |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 21c.

See Also:

- " [DBA\_MVIEW\_LOGS](DBA_MVIEW_LOGS.md) "
- " [USER\_MVIEW\_LOGS](USER_MVIEW_LOGS.md) "