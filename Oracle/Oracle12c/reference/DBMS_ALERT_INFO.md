---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBMS_ALERT_INFO.html
tags:
  - oracle
  - 12c
  - reference
---

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the alert |
| `SID` | `VARCHAR2(30)` | `NOT NULL` | Session ID of a session waiting for this alert |
| `CHANGED` | `VARCHAR2(1)` |  | Boolean flag to indicate that an alert has been signaled. `Y`: alert signaled, `N`: no alert. |
| `MESSAGE` | `VARCHAR2(1800)` |  | Optional message passed by signaler |