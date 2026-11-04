---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_STORED_SETTINGS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.88 ALL\_STORED\_SETTINGS

`ALL_STORED_SETTINGS` provides information about the persistent parameter settings for stored PL/SQL units for which the current user has execute privileges.

Related Views

- `DBA_STORED_SETTINGS` lists information about the persistent parameter settings for stored PL/SQL units for which the current user has execute privileges. It also returns parameter information for all objects in the database and is accessible only to users with the `SELECT_CATALOG_ROLE` privilege.
- `USER_STORED_SETTINGS` lists information about the persistent parameter settings for stored PL/SQL units, but only shows information about PL/SQL units owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Name of the database user owning the stored PL/SQL unit |
| `OBJECT_NAME ` | `VARCHAR2(128)` | `NOT NULL` | Name of the PL/SQL unit |
| `OBJECT_ID ` | `NUMBER` | `NOT NULL` | Object number of the PL/SQL unit |
| `OBJECT_TYPE` | `VARCHAR2(12)` |  | The type of PL/SQL unit: `PROCEDURE`, `FUNCTION`, `PACKAGE`, `PACKAGE` `BODY`, `TRIGGER`, `TYPE`, or `TYPE` `BODY` |
| `PARAM_NAME` | `VARCHAR2(128)` | `NOT NULL` | The name of the parameter stored persistently with the PL/SQL unit |
| `PARAM_VALUE` | `VARCHAR2(4000)` |  | The `TO_CHAR()` representation of the value of the persistently stored parameter. The width of this column is operating system dependent; however, it is never less than `255`. |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root) |

Note:

This view is deprecated in favor of the `ALL_PLSQL_OBJECT_SETTINGS` view. Oracle recommends that you use `ALL_PLSQL_OBJECT_SETTINGS` instead. `ALL_STORED_SETTINGS` is retained for backward compatibility only.

See Also:

" [ALL\_PLSQL\_OBJECT\_SETTINGS](ALL_PLSQL_OBJECT_SETTINGS.md) "