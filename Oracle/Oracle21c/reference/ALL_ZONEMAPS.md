---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_ZONEMAPS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.172 ALL\_ZONEMAPS

`ALL_ZONEMAPS` describes all the zone maps accessible to the user.

Related Views

- `DBA_ZONEMAPS` describes all the zone maps in the database.
- `USER_ZONEMAPS` describes all the zone maps owned by the user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the zone map |
| `ZONEMAP_NAME` | `VARCHAR2(128)` |  | Name of the zone map |
| `FACT_OWNER` | `VARCHAR2(128)` |  | Owner of the fact table of the zone map |
| `FACT_TABLE` | `VARCHAR2(128)` |  | Name of the fact table on which the zone map is defined |
| `SCALE` | `NUMBER` |  | Scale factor of the zone map |
| `HIERARCHICAL` | `VARCHAR2(12)` |  | Indicates whether the zone map is hierarchical (`YES`) or not (`NO`) |
| `WITH_CLUSTERING` | `VARCHAR2(15)` |  | Indicates whether the zone map is created with the `CLUSTERING` clause (`YES`) or not (`NO`) |
| `AUTOMATIC` <sup>Foot 1</sup> | `VARCHAR2(9)` |  | Indicates whether the zone map is automatic (`YES`) or not (`NO`) |
| `QUERY` | `LONG` |  | Zone map defining query |
| `QUERY_LEN` | `NUMBER(38)` |  | Length of defining query in bytes |
| `PRUNING` | `VARCHAR2(8)` |  | Indicates whether the zone map is enabled for pruning (`ENABLED`) or not (`DISABLED`) |
| `REFRESH_MODE` | `VARCHAR2(17)` |  | Refresh mode for the zone map:  - `COMMIT` - `DEMAND` - `DATAMOVEMENT` - `LOAD` - `LOAD` `DATAMOVEMENT` |
| `REFRESH_METHOD` | `VARCHAR2(14)` |  | Refresh method for the zone map  - `COMPLETE` - `FORCE` - `FAST` |
| `LAST_REFRESH_METHOD` | `VARCHAR2(19)` |  | The last refresh method used for the zone map:  - `NA` - `COMPLETE` - `FAST` - `ERROR-UNKNOWN` |
| `LAST_REFRESH_TIME` | `TIMESTAMP(9)` |  | Time of the last refresh |
| `INVALID` | `VARCHAR2(7)` |  | Indicates whether the zone map is invalid due to some DDL (`YES`) or not (`NO`) |
| `STALE` | `VARCHAR2(7)` |  | Indicates whether the zone map is stale because of DML operations and cannot be used for pruning (`YES`) or not (`NO`), or whether this cannot be determined (`UNKNOWN`) |
| `PARTLY_STALE` <sup>Foot 1</sup> | `VARCHAR2(12)` |  | Indicates whether the zone map is partly stale (`YES`) or not (`NO`), or whether this cannot be determined (`UNKNOWN`). A partly stale zone map contains both fresh and stale zones. |
| `INCOMPLETE` <sup>Foot 1</sup> | `VARCHAR2(12)` |  | Indicates whether the zone map has missing zones (`YES`) or not (`NO`), or whether this cannot be determined (`UNKNOWN`). Missing zones result when data is added to the base table and a subsequent refresh of the zone map is not performed. |
| `UNUSABLE` | `VARCHAR2(8)` |  | Indicates whether the zone map has been marked unusable by the owner (`YES`) or not (`NO`) |
| `COMPILE_STATE` | `VARCHAR2(19)` |  | Current compile state of the zone map:  - `VALID` - `AUTHORIZATION_ERROR` - `COMPILATION_ERROR` - `NEEDS_COMPILE` - `ERROR_UNKNOWN`  Similar to `ALL_MVIEWS`.`COMPILE_STATE`. |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 21c.

Note:

This view is intended for use with Oracle Exadata release 12.1.2.1.1 or later.

See Also:

- " [DBA\_ZONEMAPS](DBA_ZONEMAPS.md) "
- " [USER\_ZONEMAPS](USER_ZONEMAPS.md) "
- [Oracle Database Data Warehousing Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DWHSG-GUID-BEA5ACA1-6718-4948-AB38-1F2C0335FDE4) for more information about zone maps