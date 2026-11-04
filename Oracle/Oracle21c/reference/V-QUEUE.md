---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-QUEUE.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.154 V$QUEUE

`V$QUEUE` contains information on the shared server message queues.

| Column | Datatype | Description |
| --- | --- | --- |
| `PADDR` | `RAW(4 \| 8)` | Address of the process that owns the queue |
| `TYPE` | `VARCHAR2(10)` | Type of queue:  - `COMMON` - Processed by servers - `DISPATCHER` |
| `QUEUED` | `NUMBER` | Number of items in the queue |
| `WAIT` | `NUMBER` | Total time that all items in this queue have waited (in hundredths of a second). Divide by `TOTALQ` for average wait per item. |
| `TOTALQ` | `NUMBER` | Total number of items that have ever been in the queue |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |