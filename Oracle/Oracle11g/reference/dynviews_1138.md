---
title: "V$FILEMETRIC"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1138.htm
tags:
  - oracle
  - 11g
  - reference
---

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