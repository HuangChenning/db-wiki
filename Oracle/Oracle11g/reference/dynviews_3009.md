---
title: "V$SERVICE_WAIT_CLASS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3009.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SERVICE_WAIT_CLASS` displays aggregated wait counts and wait times for each wait statistic. An aggregation of these wait classes is used when thresholds are imported.

| Column | Datatype | Description |
| --- | --- | --- |
| `SERVICE_NAME` | `VARCHAR2(64)` | Service name from `V$SERVICES` |
| `SERVICE_NAME_HASH` | `NUMBER` | Service name hash from `V$SERVICES` |
| `WAIT_CLASS_ID` | `NUMBER` | Identifier of the wait class |
| `WAIT_CLASS#` | `NUMBER` | Number of the wait class |
| `WAIT_CLASS` | `VARCHAR2(64)` | Name of the wait class |
| `TOTAL_WAITS` | `NUMBER` | Number of times waits of the class occurred for this client |
| `TIME_WAITED` | `NUMBER` | Amount of time (in hundredths of a second) spent in the class by this session |