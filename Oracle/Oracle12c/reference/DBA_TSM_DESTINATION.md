---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_TSM_DESTINATION.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_TSM_DESTINATION` lists transparent session migration (TSM) destination session statistics.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SOURCE_DATABASE_NAME` | `VARCHAR2(4000)` |  | Database name of source session |
| `DESTINATION_DATABASE_NAME` | `VARCHAR2(4000)` |  | Database name of destination session |
| `DESTINATION_INSTANCE_NAME` | `VARCHAR2(4000)` |  | Instance name of destination session |
| `DESTINATION_INSTANCE_ID` | `VARCHAR2(4000)` |  | Instance ID of destination session |
| `DESTINATION_INST_START_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Instance start time of destination session |
| `SEQUENCE#` | `NUMBER` |  | Migration sequence number |
| `DESTINATION_SID` | `NUMBER` |  | Session ID of destination session |
| `DESTINATION_SERIAL#` | `NUMBER` |  | Session serial number of destination session |
| `DESTINATION_START_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Start time for migration on destination session |
| `DESTINATION_END_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | End time for migration on destination session |
| `DESTINATION_USER_NAME` | `VARCHAR2(128)` | `NOT NULL` | User associated with the destination session |
| `DESTINATION_SCHEMA_NAME` | `VARCHAR2(128)` | `NOT NULL` | Schema associated with the destination session |
| `DESTINATION_STATE` | `VARCHAR2(24)` |  | Migration state of destination session |