---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_RSRC_IO_CALIBRATE.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_RSRC_IO_CALIBRATE` displays I/O calibration results for the latest calibration run.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `START_TIME` | `TIMESTAMP(6)` |  | Start time of the most recent I/O calibration |
| `END_TIME` | `TIMESTAMP(6)` |  | End time of the most recent I/O calibration |
| `MAX_IOPS` | `NUMBER` |  | Maximum number of data block read requests that can be sustained per second |
| `MAX_MBPS` | `NUMBER` |  | Maximum megabytes per second of maximum-sized read requests that can be sustained |
| `MAX_PMBPS` | `NUMBER` |  | Maximum megabytes per second of large I/O requests that can be sustained by a single process |
| `LATENCY` | `NUMBER` |  | Latency for data block read requests |
| `NUM_PHYSICAL_DISKS` | `NUMBER` |  | Number of physical disks in the storage subsystem (as specified by the user) |