---
title: DBA_FLASHBACK_ARCHIVE_TABLES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3190.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_FLASHBACK_ARCHIVE_TABLES` displays information about all tables in the database that are enabled for Flashback Archive.

Related View

`USER_FLASHBACK_ARCHIVE_TABLES` displays information about the tables owned by the current user that are enabled for Flashback Archive.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the table enabled for Flashback Archive |
| `OWNER_NAME` | `VARCHAR2(30)` | `NOT NULL` | Owner name of the table enabled for Flashback Archive |
| `FLASHBACK_ARCHIVE_NAME` | `VARCHAR2(255)` | `NOT NULL` | Name of the flashback archive |
| `ARCHIVE_TABLE_NAME` | `VARCHAR2(53)` |  | Name of the archive table containing the historical data for the user table |
| `STATUS` | `VARCHAR2(13)` |  | Status of whether flashback archive is enabled or being disabled on the table |

See Also:

["USER\_FLASHBACK\_ARCHIVE\_TABLES"](statviews_5311.md)