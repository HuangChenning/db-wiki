---
title: ALL_SOURCE_AE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2065.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SOURCE_AE` describes the text source of the stored objects (across all editions) accessible to the current user.

Related Views

- `DBA_SOURCE_AE` describes the text source of all stored objects (across all editions) in the database.
- `USER_SOURCE_AE` describes the text source of the stored objects (across all editions) owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the object |
| `NAME` | `VARCHAR2(30)` |  | Name of the object |
| `TYPE` | `VARCHAR2(12)` |  | Type of the object: |
| `LINE` | `NUMBER` |  | Line number of this line of source |
| `TEXT` | `VARCHAR2(4000)` |  | Source text |
| `EDITION_NAME` | `VARCHAR2(30)` |  | Name of the Edition |

See Also:

- ["DBA\_SOURCE\_AE"](statviews_4273.md)
- ["USER\_SOURCE\_AE"](statviews_5448.md)