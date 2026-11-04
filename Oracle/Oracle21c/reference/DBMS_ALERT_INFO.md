---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBMS_ALERT_INFO.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.175 DBMS\_ALERT\_INFO

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the alert |
| `SID` | `VARCHAR2(30)` | `NOT NULL` | Session ID of a session waiting for this alert |
| `CHANGED` | `VARCHAR2(1)` |  | Boolean flag to indicate that an alert has been signaled. `Y`: alert signaled, `N`: no alert. |
| `MESSAGE` | `VARCHAR2(1800)` |  | Optional message passed by signaler |