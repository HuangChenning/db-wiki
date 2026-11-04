---
title: ALL_TAB_STAT_PREFS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2113.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_TAB_STAT_PREFS` displays information about statistics preferences for the tables accessible to the current user.

Related Views

- `DBA_TAB_STAT_PREFS` displays information about statistics preferences for all tables in the database.
- `USER_TAB_STAT_PREFS` displays information about statistics preferences for the tables owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the table |
| `PREFERENCE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the preference |
| `PREFERENCE_VALUE` | `VARCHAR2(1000)` |  | Value of the preference |