---
title: DBMS_ALERT_INFO
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5115.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBMS_ALERT_INFO` describes registered alerts.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the alert |
| `SID` | `VARCHAR2(30)` | `NOT NULL` | Session ID of a session waiting for this alert |
| `CHANGED` | `VARCHAR2(1)` |  | Boolean flag to indicate that an alert has been signaled. `Y`: alert signaled, `N`: no alert. |
| `MESSAGE` | `VARCHAR2(1800)` |  | Optional message passed by signaler |