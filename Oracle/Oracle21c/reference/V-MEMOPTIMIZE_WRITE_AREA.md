---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-MEMOPTIMIZE_WRITE_AREA.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.75 V$MEMOPTIMIZE\_WRITE\_AREA

`V$MEMOPTIMIZE_WRITE_AREA` displays information about fast ingest data in the large pool.

| Column | Datatype | Description |
| --- | --- | --- |
| `TOTAL_SIZE` | `NUMBER` | Total amount of memory allocated for fast ingest data in the large pool (in bytes) |
| `USED_SPACE` | `NUMBER` | Total amount of memory currently used by fast ingest data in the large pool (in bytes) |
| `FREE_SPACE` | `NUMBER` | Total amount of memory currently free for storing fast ingest data in the large pool (in bytes) |
| `NUM_WRITES` | `NUMBER` | Number of fast ingest insert operations for which data is still in the large pool and is yet to be written to disk |
| `NUM_WRITERS` | `NUMBER` | Number of clients currently using fast ingest for inserting data into the database |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |