---
title: DBA_HIST_IC_CLIENT_STATS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3226.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_IC_CLIENT_STATS` displays information about the usage of an interconnect device by the instance. The information is divided into several areas of the Oracle Database, each identified by the `NAME` value.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `NAME` | `VARCHAR2(9)` | `NOT NULL` | Identifies the area of the Oracle Database:  All other values are internal to Oracle and are not expected to have high usage. |
| `BYTES_SENT` | `NUMBER` |  | Number of bytes sent by the instance since instance startup for the software area identified by `NAME`. This information is aggregated across all devices used by the instance. |
| `BYTES_RECEIVED` | `NUMBER` |  | Number of bytes received by the instance since instance startup for the software area identified by `NAME`. This information is aggregated across all devices used by the instance. |