---
title: "V$EVENT_NAME"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1130.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$EVENT_NAME` displays information about wait events.

| Column | Datatype | Description |
| --- | --- | --- |
| `EVENT#` | `NUMBER` | Number of the wait event |
| `EVENT_ID` | `NUMBER` | Identifier of the wait event |
| `NAME` | `VARCHAR2(64)` | Name of the wait event |
| `PARAMETER1` | `VARCHAR2(64)` | Description of the first parameter for the wait event |
| `PARAMETER2` | `VARCHAR2(64)` | Description of the second parameter for the wait event |
| `PARAMETER3` | `VARCHAR2(64)` | Description of the third parameter for the wait event |
| `WAIT_CLASS_ID` | `NUMBER` | Identifier of the class of the wait event |
| `WAIT_CLASS#` | `NUMBER` | Number of the class of the wait event |
| `WAIT_CLASS` | `VARCHAR2(64)` | Name of the class of the wait event  See Also: ["Classes of Wait Events"](waitevents001.md) for a description of the different wait event classes |