---
title: DBA_HIST_SESSMETRIC_HISTORY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4038.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_SESSMETRIC_HISTORY` displays the history of several important session metrics.

Note:

This view is populated only if a session metric exceeds a server metric threshold that was configured using the `DBMS_SERVER_ALERT` package.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `BEGIN_TIME` | `DATE` | `NOT NULL` | Begin time of the interval |
| `END_TIME` | `DATE` | `NOT NULL` | End time of the interval |
| `SESSID` | `NUMBER` | `NOT NULL` | Session ID |
| `SERIAL#` | `NUMBER` | `NOT NULL` | Session serial number |
| `INTSIZE` | `NUMBER` | `NOT NULL` | Interval size (in hundredths of a second) |
| `GROUP_ID` | `NUMBER` | `NOT NULL` | Group ID |
| `METRIC_ID` | `NUMBER` | `NOT NULL` | Metric ID |
| `METRIC_NAME` | `VARCHAR2(64)` | `NOT NULL` | Metric name |
| `VALUE` | `NUMBER` | `NOT NULL` | Metric Value |
| `METRIC_UNIT` | `VARCHAR2(64)` | `NOT NULL` | Unit of measurement |

See Also:

The `DBMS_SERVER_ALERT` package in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_server_alert.htm#ARPLS016)