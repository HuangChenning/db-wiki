---
title: ALL_QUEUE_TABLES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2018.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_QUEUE_TABLES` describes the queues in the queue tables accessible to the current user.

Related Views

- `DBA_QUEUE_TABLES` describes the queues in all queue tables in the database.
- `USER_QUEUE_TABLES` describes the queues in the queue tables created in the current user's schema. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the queue table |
| `QUEUE_TABLE` | `VARCHAR2(30)` |  | Name of the queue table |
| `TYPE` | `VARCHAR2(7)` |  | Type of user data: - `RAW` - Raw type - `OBJECT` - User-defined object type - `VARIANT` - Variant type (for internal use only) |
| `OBJECT_TYPE` | `VARCHAR2(61)` |  | Object type of the payload when `TYPE` is `OBJECT` |
| `SORT_ORDER` | `VARCHAR2(22)` |  | User-specified sort order |
| `RECIPIENTS` | `VARCHAR2(8)` |  | `SINGLE` or `MULTIPLE` recipients |
| `MESSAGE_GROUPING` | `VARCHAR2(13)` |  | `NONE` or `TRANSACTIONAL` |
| `COMPATIBLE` | `VARCHAR2(6)` |  | Lowest release level which the queue table is compatible with (for example, `8.0.3`) |
| `PRIMARY_INSTANCE` | `NUMBER` |  | Indicates the instance number of the instance which is the primary owner of the queue table. A value of `0` indicates that there is no primary owner. |
| `SECONDARY_INSTANCE` | `NUMBER` |  | Indicates the instance number of the instance which is the secondary owner of the queue table. This instance becomes the owner of the queue table if the primary owner is not alive. A value of `0` indicates that there is no secondary owner. |
| `OWNER_INSTANCE` | `NUMBER` |  | Instance number of the instance which currently owns the queue table |
| `USER_COMMENT` | `VARCHAR2(50)` |  | Comment supplied by the user |
| `SECURE` | `VARCHAR2(3)` |  | Indicates whether the queue table is secure (`YES`) or not (`NO`) |

See Also:

- ["DBA\_QUEUE\_TABLES"](statviews_4193.md)
- ["USER\_QUEUE\_TABLES"](statviews_5405.md)
- [Oracle Streams Advanced Queuing User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e11013/toc.htm) for more information about these views and Advanced Queuing