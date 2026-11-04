---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_TS_QUOTAS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_TS_QUOTAS` describes tablespace quotas for all users.

Related View

`USER_TS_QUOTAS` describes tablespace quotas for the current user. This view does not display the `USERNAME` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Tablespace name |
| `USERNAME ` | `VARCHAR2(128)` | `NOT NULL` | User with resource rights on the tablespace |
| `BYTES ` | `NUMBER` |  | Number of bytes charged to the user |
| `MAX_BYTES` | `NUMBER` |  | User's quota in bytes, or `-1` if no limit |
| `BLOCKS` | `NUMBER` |  | Number of Oracle blocks charged to the user |
| `MAX_BLOCKS` | `NUMBER` |  | User's quota in Oracle blocks, or `-1` if no limit |
| `DROPPED` | `VARCHAR2(3)` |  | Whether the tablespace has been dropped |

See Also:

" [USER\_TS\_QUOTAS](USER_TS_QUOTAS.md) "