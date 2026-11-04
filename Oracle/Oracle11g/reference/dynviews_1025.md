---
title: "V$ASM_DISK_IOSTAT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1025.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ASM_DISK_IOSTAT` displays information about disk I/O statistics for each ASM client. If this view is queried from the database instance, only the rows for that instance are shown.

| Column | Datatype | Description |
| --- | --- | --- |
| `INSTNAME` | `VARCHAR2(64)` | Identifier for the DB/ADVM instance client |
| `DBNAME` | `VARCHAR2(8)` | Unique database name (`DB_UNIQUE_NAME`) |
| `GROUP_NUMBER` | `NUMBER` | Number of the disk group containing the disk |
| `DISK_NUMBER` | `NUMBER` | Number assigned to the disk within its disk group |
| `FAILGROUP` | `VARCHAR2(30)` | Name of the failure group to which the disk belongs |
| `READS` | `NUMBER` | Total number of I/O read requests for the disk |
| `WRITES` | `NUMBER` | Total number of I/O write requests for the disk |
| `READ_ERRS` | `NUMBER` | Total number of failed I/O read requests for the disk |
| `WRITE_ERRS` | `NUMBER` | Total number of failed I/O write requests for the disk |
| `READ_TIME` | `NUMBER` | Total I/O time (in seconds) for read requests for the disk if the `TIMED_STATISTICS` initialization parameter is set to `TRUE` (`0` if set to `FALSE`). |
| `WRITE_TIME` | `NUMBER` | Total I/O time (in seconds) for write requests for the disk if the `TIMED_STATISTICS` initialization parameter is set to `TRUE` (`0` if set to `FALSE`) |
| `BYTES_READ` | `NUMBER` | Total number of bytes read from the disk |
| `BYTES_WRITTEN` | `NUMBER` | Total number of bytes written from the disk |
| `HOT_READS` | `NUMBER` | Number of reads from the hot region on disk |
| `HOT_WRITES` | `NUMBER` | Number of writes to the hot region on disk |
| `HOT_BYTES_READ` | `NUMBER` | Number of bytes read from the hot region on disk |
| `HOT_BYTES_WRITTEN` | `NUMBER` | Number of bytes written to the hot region on disk |
| `COLD_READS` | `NUMBER` | Number of reads from the cold region on disk |
| `COLD_WRITES` | `NUMBER` | Number of writes to the cold region on disk |
| `COLD_BYTES_READ` | `NUMBER` | Number of bytes read from the cold region on disk |
| `COLD_BYTES_WRITTEN` | `NUMBER` | Number of bytes written to the cold region on disk |