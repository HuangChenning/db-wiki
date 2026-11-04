---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-STANDBY_EVENT_HISTOGRAM.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.80 V$STANDBY\_EVENT\_HISTOGRAM

Each distinct value of apply lag has its own bucket and the count in the corresponding bucket represents the number of occurrences so far. The physical standby samples the apply lag every second and increments the corresponding bucket in the histogram.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(64)` | Name of the event (currently `APPLY LAG` is the only valid value) |
| `TIME` | `NUMBER` | Time duration that the bucket represents |
| `UNIT` | `VARCHAR2(16)` | Time unit (`seconds`, `minutes`, `hours`, or `days`) |
| `COUNT` | `NUMBER` | Each row is a histogram bucket for apply lag. `COUNT` is the number of occurrences the apply lag falls into the histogram bucket. |
| `LAST_TIME_UPDATED` | `VARCHAR2(20)` | Last time the bucket was updated by an event falling into that time duration |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |