---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-FILEMETRIC.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.228 V$FILEMETRIC

`V$FILEMETRIC` displays values of file metrics for the most recent 10-minute interval. A history of the last one hour will be kept in the system.

| Column | Datatype | Description |
| --- | --- | --- |
| `BEGIN_TIME` | `DATE` | Begin time of the interval |
| `END_TIME` | `DATE` | End time of the interval |
| `INTSIZE_CSEC` | `NUMBER` | Interval size (in hundredths of a second) |
| `FILE_ID` | `NUMBER` | File number |
| `CREATION_TIME` | `NUMBER` | Timestamp of the file creation |
| `AVERAGE_READ_TIME` | `NUMBER` | Average file read time (in hundredths of a second) |
| `AVERAGE_WRITE_TIME` | `NUMBER` | Average file write time (in hundredths of a second) |
| `PHYSICAL_READS` | `NUMBER` | Number of physical reads |
| `PHYSICAL_WRITES` | `NUMBER` | Number of physical writes |
| `PHYSICAL_BLOCK_READS` | `NUMBER` | Number of physical block reads |
| `PHYSICAL_BLOCK_WRITES` | `NUMBER` | Number of physical block writes |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |