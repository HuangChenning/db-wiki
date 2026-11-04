---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-REDO_DEST_RESP_HISTOGRAM.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.164 V$REDO\_DEST\_RESP\_HISTOGRAM

`V$REDO_DEST_RESP_HISTOGRAM` provides statistical information for each redo transport destination.

| Column | Datatype | Description |
| --- | --- | --- |
| `DEST_ID` | `NUMBER` | A nonnegative integer value representing a `SYNC` standby destination |
| `TIME` | `VARCHAR2(20)` | A text string that shows the last wall-clock time that a bucket was hit |
| `DURATION` | `NUMBER` | A positive integer value that represents a bucket of seconds, 1, 2, 3, up to 300 seconds, followed by 5 additional buckets that represent 600, 1200, 2400, 4800, and 9600 ( >= 4801) seconds |
| `FREQUENCY` | `NUMBER` | A nonnegative integer that shows the number of times a particular bucket was hit by the destination specified by `DEST_ID` |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |