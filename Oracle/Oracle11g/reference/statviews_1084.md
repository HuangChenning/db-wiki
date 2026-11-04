---
title: ALL_EDITIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1084.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_EDITIONS` describes the editions accessible to the current user.

Related View

`DBA_EDITIONS` describes all editions in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `EDITION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the edition |
| `PARENT_EDITION_NAME` | `VARCHAR2(30)` |  | Name of the parent edition for this edition |
| `USABLE` | `VARCHAR2(3)` |  | Indicates whether the edition is usable (`YES`) or unusable (`NO`) |

See Also:

- ["DBA\_EDITIONS"](statviews_3165.md)
- [Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/adfns_editions.htm#ADFNS99923) for more information about editions