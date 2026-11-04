---
title: DBA_COMPARISON
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3113.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_COMPARISON` displays information about all comparison objects in the database.

Related View

`USER_COMPARISON` displays information about the comparison objects owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the comparison |
| `COMPARISON_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the comparison |
| `COMPARISON_MODE` | `VARCHAR2(5)` |  | Mode of the comparison: - `TABLE` |
| `SCHEMA_NAME` | `VARCHAR2(30)` |  | Schema name of the local object |
| `OBJECT_NAME` | `VARCHAR2(30)` |  | Name of the local object |
| `OBJECT_TYPE` | `VARCHAR2(17)` |  | Type of the local object: - `TABLE` - `VIEW` - `SYNONYM` - `MATERIALIZED VIEW` |
| `REMOTE_SCHEMA_NAME` | `VARCHAR2(30)` |  | Schema name of the remote object |
| `REMOTE_OBJECT_NAME` | `VARCHAR2(30)` |  | Name of the remote object |
| `REMOTE_OBJECT_TYPE` | `VARCHAR2(17)` |  | Type of the remote object: - `TABLE` - `VIEW` - `SYNONYM` - `MATERIALIZED VIEW` |
| `DBLINK_NAME` | `VARCHAR2(128)` |  | Database link name to the remote database |
| `SCAN_MODE` | `VARCHAR2(9)` |  | Scan mode of the comparison: FULL - `FULL` - `RANDOM` - `CYCLIC` - `CUSTOM` |
| `SCAN_PERCENT` | `NUMBER` |  | Scan percent of the comparison; applicable to random and cyclic modes |
| `CYCLIC_INDEX_VALUE` | `VARCHAR2(4000)` |  | Last index column value used in a cyclic scan |
| `NULL_VALUE` | `VARCHAR2(4000)` |  | Value to use for NULL columns |
| `LOCAL_CONVERGE_TAG` | `RAW(2000)` |  | Local Streams tag used while performing converge DMLs |
| `REMOTE_CONVERGE_TAG` | `RAW(2000)` |  | Remote Streams tag used while performing converge DMLs |
| `MAX_NUM_BUCKETS` | `NUMBER` |  | Suggested maximum number of buckets in a scan |
| `MIN_ROWS_IN_BUCKET` | `NUMBER` |  | Suggested minimum number of rows in a bucket |
| `LAST_UPDATE_TIME` | `TIMESTAMP(6)` |  | Time that this row was last updated |