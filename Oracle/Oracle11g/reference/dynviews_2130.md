---
title: "V$REDO_DEST_RESP_HISTOGRAM"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2130.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$REDO_DEST_RESP_HISTOGRAM` provides statistical information for each redo transport destination.

| Column | Datatype | Description |
| --- | --- | --- |
| `DEST_ID` | `NUMBER` | A non-negative integer value from 1 - 10 for each possible `LGWR` `SYNC` standby destination |
| `TIME` | `VARCHAR2(20)` | A text string that shows the last wall-clock time that a bucket was hit |
| `DURATION` | `NUMBER` | A positive integer value that represents a bucket of seconds, 1, 2, 3, up to 300 seconds, followed by 5 additional buckets that represent 600, 1200, 2400, 4800, and 9600 ( >= 4801) seconds |
| `FREQUENCY` | `NUMBER` | A non-negative integer that shows the number of times a particular bucket was hit by the `SYNC` `LNS` process |