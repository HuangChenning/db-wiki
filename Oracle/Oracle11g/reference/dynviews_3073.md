---
title: "V$STANDBY_EVENT_HISTOGRAM"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3073.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$STANDBY_EVENT_HISTOGRAM` displays the histogram of apply lag on the physical standby. Each distinct value of apply lag has its own bucket and the count in the corresponding bucket represents the number of occurrences so far. The physical standby samples the apply lag every second and increments the corresponding bucket in the histogram.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(64)` | Name of the event (currently `APPLY LAG` is the only valid value) |
| `TIME` | `NUMBER` | Time duration that the bucket represents |
| `UNIT` | `VARCHAR2(16)` | Time unit (`seconds`, `minutes`, `hours`, or `days`) |
| `COUNT` | `NUMBER` | Each row is a histogram bucket for apply lag. `COUNT` is the number of occurrences the apply lag falls into the histogram bucket. |
| `LAST_TIME_UPDATED` | `VARCHAR2(20)` | Last time the bucket was updated by an event falling into that time duration |