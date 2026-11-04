---
title: ALL_WARNING_SETTINGS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2135.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_WARNING_SETTINGS` displays information about the warning parameter settings for the objects accessible to the current user.

Related Views

- `DBA_WARNING_SETTINGS` displays information about the warning parameter settings for all objects in the database.
- `USER_WARNING_SETTINGS` displays information about the warning parameter settings for the objects owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the object |
| `OBJECT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object |
| `OBJECT_ID` | `NUMBER` | `NOT NULL` | Object number of the object |
| `OBJECT_TYPE` | `VARCHAR2(12)` |  | Type of the object: |
| `WARNING` | `VARCHAR2(40)` |  | Warning number or category: |
| `SETTING` | `VARCHAR2(7)` |  | Value of the warning setting: |

See Also:

- ["DBA\_WARNING\_SETTINGS"](statviews_5089.md)
- ["USER\_WARNING\_SETTINGS"](statviews_5511.md)