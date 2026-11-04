---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_SR_PARTN_OPS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.390 DBA\_SR\_PARTN\_OPS

`DBA_SR_PARTN_OPS` provides information on the partition operations registered on the base tables of the materialized views registered for synchronous refresh.

These rows last only as long as the registrations are active; that is, they disappear after `EXECUTE_REFRESH` or `ABORT_REFRESH` of the base table by the `DBMS_SYNC_REFRESH` package.

Related View

`USER_SR_PARTN_OPS` provides information on the partition operations registered on the base tables of the materialized views registered for synchronous refresh belonging to the current user. Its columns are the same as those in `DBA_SR_PARTN_OPS`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the base table registered for synchronous refresh |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table |
| `PARTITION_OP` | `VARCHAR2(128)` | `NOT NULL` | Type of partition operation:  - `DROP` - `EXCHANGE` - `TRUNCATE` |
| `PARTITION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the partition to be changed |
| `OUTSIDE_TABLE_SCHEMA` | `VARCHAR2(128)` |  | Schema in which the outside table (for `EXCHANGE PARTITION`) was created |
| `OUTSIDE_TABLE_NAME` | `VARCHAR2(128)` |  | Name of the outside table (for `EXCHANGE PARTITION`) |

See Also:

- " [USER\_SR\_PARTN\_OPS](USER_SR_PARTN_OPS.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS73623) for more information about the `DBMS_SYNC_REFRESH` package