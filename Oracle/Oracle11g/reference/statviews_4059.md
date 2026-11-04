---
title: DBA_HIST_SYSMETRIC_HISTORY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4059.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_SYSMETRIC_HISTORY` externalizes all available history of the system metric values for the entire set of data kept in the database. This view contains snapshots of `V$SYSMETRIC_HISTORY`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `BEGIN_TIME` | `DATE` | `NOT NULL` | Begin time of the interval |
| `END_TIME` | `DATE` | `NOT NULL` | End time of the interval |
| `INTSIZE` | `NUMBER` | `NOT NULL` | Interval size (in hundredths of a second) |
| `GROUP_ID` | `NUMBER` | `NOT NULL` | Group ID |
| `METRIC_ID` | `NUMBER` | `NOT NULL` | Metric ID |
| `METRIC_NAME` | `VARCHAR2(64)` | `NOT NULL` | Metric name |
| `VALUE` | `NUMBER` | `NOT NULL` | Metric Value |
| `METRIC_UNIT` | `VARCHAR2(64)` | `NOT NULL` | Unit of measurement |