---
title: ALL_SCHEDULER_DESTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2035.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SCHEDULER_DESTS` displays information about the destination objects for jobs accessible to the current user.

Related Views

- `DBA_SCHEDULER_DESTS` displays information about all destination objects for jobs in the database.
- `USER_SCHEDULER_DESTS` displays information about the destination objects for jobs owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of this destination object |
| `DESTINATION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of this destination object |
| `DESTINATION_TYPE` | `VARCHAR2(8)` |  | Type of this destination object: |
| `ENABLED` | `VARCHAR2(5)` |  | Indicates whether this destination object is enabled (`TRUE`) or disabled (`FALSE`) |
| `COMMENTS` | `VARCHAR2(240)` |  | Optional comment |

See Also:

- ["DBA\_SCHEDULER\_DESTS"](statviews_4239.md)
- ["USER\_SCHEDULER\_DESTS"](statviews_5427.md)