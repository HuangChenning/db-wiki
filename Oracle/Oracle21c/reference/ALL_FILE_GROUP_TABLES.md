---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_FILE_GROUP_TABLES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.193 ALL\_FILE\_GROUP\_TABLES

`ALL_FILE_GROUP_TABLES` shows information about the tables accessible to the current user that can be imported using the file set.

Related Views

- `DBA_FILE_GROUP_TABLES` shows information about all the tables in the database that can be imported using the file set.
- `USER_FILE_GROUP_TABLES` shows information about tables owned by the current user that can be imported using the file set. This view does not display the `FILE_GROUP_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `FILE_GROUP_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the file group |
| `FILE_GROUP_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the file group |
| `VERSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Version of the file group that contains the table |
| `VERSION` | `NUMBER` | `NOT NULL` | Internal version number |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Schema to which the table belongs |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Name of the tablespace to which the table belongs |
| `SCN` | `NUMBER` |  | SCN at which the table was exported (available only for Streams-prepared tables) |

See Also:

- " [DBA\_FILE\_GROUP\_TABLES](DBA_FILE_GROUP_TABLES.md) "
- " [USER\_FILE\_GROUP\_TABLES](USER_FILE_GROUP_TABLES.md) "