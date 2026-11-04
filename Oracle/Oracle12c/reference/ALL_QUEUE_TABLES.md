---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_QUEUE_TABLES.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_QUEUE_TABLES` describes the queues in the queue tables accessible to the current user.

Related Views

- `DBA_QUEUE_TABLES` describes the queues in all queue tables in the database.
- `USER_QUEUE_TABLES` describes the queues in the queue tables created in the current user's schema. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the queue table |
| `QUEUE_TABLE` | `VARCHAR2(128)` |  | Name of the queue table |
| `TYPE` | `VARCHAR2(9)` |  | Type of user data:  - `RAW` - Raw type - `OBJECT` - User-defined object type - `VARIANT` - Variant type (for internal use only) |
| `OBJECT_TYPE` | `VARCHAR2(257)` |  | Object type of the payload when `TYPE` is `OBJECT` |
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

- " [DBA\_QUEUE\_TABLES](DBA_QUEUE_TABLES.md) "
- " [USER\_QUEUE\_TABLES](USER_QUEUE_TABLES.md) "
- [Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADQUE0100) for more information Advanced Queuing