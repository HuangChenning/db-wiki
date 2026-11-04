---
title: ALL_SCHEDULER_GLOBAL_ATTRIBUTE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2038.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SCHEDULER_GLOBAL_ATTRIBUTE` displays the values of all scheduler attributes (for example, `DEFAULT_TIMEZONE` and `CURRENT_OPEN_WINDOW`).

Related View

`DBA_SCHEDULER_GLOBAL_ATTRIBUTE` displays the values of all scheduler attributes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ATTRIBUTE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the Scheduler attribute |
| `VALUE` | `VARCHAR2(128)` |  | Value of the Scheduler attribute |

See Also:

["DBA\_SCHEDULER\_GLOBAL\_ATTRIBUTE"](statviews_4242.md)