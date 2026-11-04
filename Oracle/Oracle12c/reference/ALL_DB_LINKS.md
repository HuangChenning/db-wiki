---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_DB_LINKS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_DB_LINKS` describes the database links accessible to the current user.

Related Views

- `DBA_DB_LINKS` describes all database links in the database.
- `USER_DB_LINKS` describes the database links owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the database link |
| `DB_LINK` | `VARCHAR2(128)` | `NOT NULL` | Name of the database link |
| `USERNAME` | `VARCHAR2(128)` |  | Name of the user when logging in |
| `HOST` | `VARCHAR2(2000)` |  | Oracle Net connect string |
| `CREATED` | `DATE` | `NOT NULL` | Creation time of the database link |
| `HIDDEN` | `VARCHAR2(3)` |  | For internal use only  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |