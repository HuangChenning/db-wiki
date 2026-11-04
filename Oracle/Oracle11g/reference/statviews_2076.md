---
title: ALL_STORED_SETTINGS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2076.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_STORED_SETTINGS` provides information about the persistent parameter settings for stored PL/SQL units for which the current user has execute privileges.

Related Views

- `DBA_STORED_SETTINGS` lists information about the persistent parameter settings for stored PL/SQL units for which the current user has execute privileges. It also returns parameter information for all objects in the database and is accessible only to users with the `SELECT_CATALOG_ROLE` privilege.
- `USER_STORED_SETTINGS` lists information about the persistent parameter settings for stored PL/SQL units, but only shows information about PL/SQL units owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Name of the database user owning the stored PL/SQL unit |
| `OBJECT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the PL/SQL unit |
| `OBJECT_ID` | `NUMBER` | `NOT NULL` | Object number of the PL/SQL unit |
| `OBJECT_TYPE` | `VARCHAR2(12)` |  | The type of PL/SQL unit: `PROCEDURE`, `FUNCTION`, `PACKAGE`, `PACKAGE` `BODY`, `TRIGGER`, `TYPE`, or `TYPE` `BODY` |
| `PARAM_NAME` | `VARCHAR2(30)` |  | The name of the parameter stored persistently with the PL/SQL unit |
| `PARAM_VALUE` | `VARCHAR2(4000)` |  | The `TO_CHAR()` representation of the value of the persistently stored parameter. The width of this column is operating system dependent; however, it is never less than `255`. |

Note:

This view is deprecated in favor of the `ALL_PLSQL_OBJECT_SETTINGS` view. Oracle recommends that you use `ALL_PLSQL_OBJECT_SETTINGS` instead. `ALL_STORED_SETTINGS` is retained for backward compatibility only.