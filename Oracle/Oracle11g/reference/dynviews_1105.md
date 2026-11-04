---
title: "V$DATAGUARD_STATUS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1105.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$DATAGUARD_STATUS` displays messages recently written to the alert log or server process trace files that concern physical standby databases or redo transport services for all standby database types.

| Column | Datatype | Description |
| --- | --- | --- |
| `FACILITY` | `VARCHAR2(24)` | Facility that encountered the event: |
| `SEVERITY` | `VARCHAR2(13)` | Severity of the event: - `Informational` - Informational message - `Warning` - Warning message - `Error` - Indicates the process has failed - `Fatal` - `Control` - An expected change in state such as the start or completion of an archival, log recovery, or switchover operation |
| `DEST_ID` | `NUMBER` | Destination ID number to which the event pertains. If the event does not pertain to a particular destination, then the value is `0`. |
| `MESSAGE_NUM` | `NUMBER` | A chronologically increasing number giving each event a unique number |
| `ERROR_CODE` | `NUMBER` | Error ID pertaining to the event |
| `CALLOUT` | `VARCHAR2(3)` | Reserved for future use |
| `TIMESTAMP` | `DATE` | Message date |
| `MESSAGE` | `VARCHAR2(256)` | A text message describing the event |