---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_WARNING_SETTINGS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.142 ALL\_WARNING\_SETTINGS

`ALL_WARNING_SETTINGS` displays information about the warning parameter settings for the objects accessible to the current user.

Related Views

- `DBA_WARNING_SETTINGS` displays information about the warning parameter settings for all objects in the database.
- `USER_WARNING_SETTINGS` displays information about the warning parameter settings for the objects owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the object |
| `OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the object |
| `OBJECT_ID` | `NUMBER` | `NOT NULL` | Object number of the object |
| `OBJECT_TYPE` | `VARCHAR2(12)` |  | Type of the object:  - `PROCEDURE` - `FUNCTION` - `PACKAGE` - `PACKAGE BODY` - `TRIGGER` - `TYPE` - `TYPE BODY` |
| `WARNING` | `VARCHAR2(40)` |  | Warning number or category:  - `INFORMATIONAL` - `PERFORMANCE` - `SEVERE` - `ALL` |
| `SETTING` | `VARCHAR2(7)` |  | Value of the warning setting:  - `DISABLE` - `ENABLE` - `ERROR` |

See Also:

- " [DBA\_WARNING\_SETTINGS](DBA_WARNING_SETTINGS.md) "
- " [USER\_WARNING\_SETTINGS](USER_WARNING_SETTINGS.md) "