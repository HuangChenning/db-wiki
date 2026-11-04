---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ASM_DISK_IOSTAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.57 V$ASM\_DISK\_IOSTAT

`V$ASM_DISK_IOSTAT` displays information about disk I/O statistics for each Oracle Automatic Storage Management (Oracle ASM) client.

If this view is queried from the database instance, only the rows for that instance are shown.

| Column | Datatype | Description |
| --- | --- | --- |
| `INSTNAME` | `VARCHAR2(64)` | Identifier for the DB/ADVM instance client |
| `DBNAME` | `VARCHAR2(8)` | Unique database name (`DB_UNIQUE_NAME`) |
| `CLUSTERNAME` | `VARCHAR2(31)` | Name of the cluster |
| `GROUP_NUMBER` | `NUMBER` | Number of the disk group containing the disk |
| `DISK_NUMBER` | `NUMBER` | Number assigned to the disk within its disk group |
| `FAILGROUP` | `VARCHAR2(30)` | Name of the failure group to which the disk belongs |
| `SITE_NAME` | `VARCHAR2(30)` | This is the name of the site to which the disk belongs |
| `READS` | `NUMBER` | Total number of I/O read requests for the disk |
| `WRITES` | `NUMBER` | Total number of I/O write requests for the disk |
| `READ_ERRS` | `NUMBER` | Total number of failed I/O read requests for the disk |
| `WRITE_ERRS` | `NUMBER` | Total number of failed I/O write requests for the disk |
| `READ_TIMEOUT` | `NUMBER` | Number of read I/Os that are timed out |
| `WRITE_TIMEOUT` | `NUMBER` | Number of write I/Os that are timed out |
| `READ_TIME` | `NUMBER` | Total I/O time (in seconds) for read requests for the disk if the `TIMED_STATISTICS` initialization parameter is set to `TRUE` (`0` if set to `FALSE`). |
| `WRITE_TIME` | `NUMBER` | Total I/O time (in seconds) for write requests for the disk if the `TIMED_STATISTICS` initialization parameter is set to `TRUE` (`0` if set to `FALSE`) |
| `BYTES_READ` | `NUMBER` | Total number of bytes read from the disk |
| `BYTES_WRITTEN` | `NUMBER` | Total number of bytes written from the disk |
| `HOT_READS` <sup>Foot 1</sup> | `NUMBER` | This column is not meaningful and its value is always `0` |
| `HOT_WRITES` <sup>Foot 1</sup> | `NUMBER` | This column is not meaningful and its value is always `0` |
| `HOT_BYTES_READ` <sup>Foot 1</sup> | `NUMBER` | This column is not meaningful and its value is always `0` |
| `HOT_BYTES_WRITTEN` <sup>Foot 1</sup> | `NUMBER` | This column is not meaningful and its value is always `0` |
| `COLD_READS` <sup>Foot 1</sup> | `NUMBER` | Number of reads from the disk |
| `COLD_WRITES` <sup>Foot 1</sup> | `NUMBER` | Number of writes to the disk |
| `COLD_BYTES_READ` <sup>Foot 1</sup> | `NUMBER` | Number of bytes read from the disk |
| `COLD_BYTES_WRITTEN` <sup>Foot 1</sup> | `NUMBER` | Number of bytes written to the disk |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data  For this view, the value is always `0`. |

<sup>Footnote 1</sup> Intelligent Data Placement is desupported starting with Oracle Database 21c. As a result, the `HOT_READS`, `HOT_WRITES`, `HOT_BYTES_READ`, and `HOT_BYTES_WRITTEN` columns are no longer meaningful and always return `0`, and the `COLD_READS`, `COLD_WRITES`, `COLD_BYTES_READ`, and `COLD_BYTES_WRITTEN` columns return statistics for the entire disk.

Note:

In an Oracle Database instance, this view returns 0 rows when queried from a PDB.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG10030) for additional information about using views to display Oracle ASM information