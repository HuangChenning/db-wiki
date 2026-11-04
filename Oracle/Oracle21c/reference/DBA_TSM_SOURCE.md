---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_TSM_SOURCE.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.67 DBA\_TSM\_SOURCE

`DBA_TSM_SOURCE` lists transparent session migration (TSM) source session statistics.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SOURCE_DATABASE_NAME` | `VARCHAR2(4000)` |  | Database name of source session |
| `SOURCE_INSTANCE_NAME` | `VARCHAR2(4000)` |  | Instance name of source session |
| `SOURCE_INSTANCE_ID` | `VARCHAR2(4000)` |  | Instance ID of source session |
| `SOURCE_INSTANCE_START_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Instance start time of source session |
| `SEQUENCE#` | `NUMBER` |  | Migration sequence number |
| `SOURCE_SID` | `NUMBER` |  | Session ID of source session |
| `SOURCE_SERIAL#` | `NUMBER` |  | Source serial number of source session |
| `SOURCE_STATE` | `VARCHAR2(24)` |  | Migration state of source session |
| `CONNECT_STRING` | `VARCHAR2(4000)` |  | Connect string specified for migration |
| `SOURCE_START_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Start time for migration on source session |
| `COST` | `NUMBER` |  | Estimate of migration cost |
| `FAILURE_REASON` | `VARCHAR2(34)` |  | Reason for migration failure, if any |
| `SOURCE_END_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | End time for migration on source session |
| `ROUNDTRIPS` | `NUMBER` |  | Number of client/server round trips during migration |
| `SOURCE_USER_NAME` | `VARCHAR2(128)` | `NOT NULL` | User associated with the source session |
| `SOURCE_SCHEMA_NAME` | `VARCHAR2(128)` | `NOT NULL` | Schema associated with the source session |
| `DESTINATION_DATABASE_NAME` | `VARCHAR2(4000)` |  | Database name of the destination session |