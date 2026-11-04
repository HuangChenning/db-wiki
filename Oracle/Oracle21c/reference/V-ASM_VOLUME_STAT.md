---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ASM_VOLUME_STAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.74 V$ASM\_VOLUME\_STAT

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
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data  For this view, the value is always `0`. |

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG10030) for additional information about using views to display Oracle ASM information