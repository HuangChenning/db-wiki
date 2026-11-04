---
title: "V$ASM_VOLUME_STAT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1037.htm
tags:
  - oracle
  - 11g
  - reference
---

In an Oracle Automatic Storage Management (Oracle ASM) instance, `V$ASM_VOLUME_STAT` displays information about statistics for each Oracle ADVM volume.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_NUMBER` | `NUMBER` | Cluster-wide number assigned to the disk group (composite primary key) |
| `VOLUME_NAME` | `VARCHAR2(30)` | Name of the volume |
| `COMPOUND_INDEX` | `NUMBER` | A 32-bit number consisting of a disk group number in the high-order 8 bits and a volume number in the low-order 24 bits (for efficient access to the view) |
| `VOLUME_NUMBER` | `NUMBER` | Number of the Volume within the disk group (composite primary key) |
| `READS` | `NUMBER` | Total number of read requests for this volume |
| `WRITES` | `NUMBER` | Total number of write requests for this volume |
| `READ_ERRS` | `NUMBER` | Total number of failed read I/O operations for this volume |
| `WRITE_ERRS` | `NUMBER` | Total number of failed write I/O operations for this volume |
| `READ_TIME` | `NUMBER` | Total I/O time (in seconds) for read requests for this volume |
| `WRITE_TIME` | `NUMBER` | Total I/O time (in seconds) for write requests for this volume |
| `BYTES_READ` | `NUMBER` | Total number of bytes read for this volume |
| `BYTES_WRITTEN` | `NUMBER` | Total number of bytes written for this volume |