---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LOG.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.46 V$LOG

`V$LOG` displays log file information from the control file.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP#` | `NUMBER` | Log group number |
| `THREAD#` | `NUMBER` | Log thread number |
| `SEQUENCE#` | `NUMBER` | Log sequence number |
| `BYTES` | `NUMBER` | Size of the log (in bytes) |
| `BLOCKSIZE` | `NUMBER` | Block size of the logfile (512 or 4096) |
| `MEMBERS` | `NUMBER` | Number of members in the log group |
| `ARCHIVED` | `VARCHAR2(3)` | Archive status (`YES`) or (`NO`) |
| `STATUS` | `VARCHAR2(16)` | Log status:  - `UNUSED` - Online redo log has never been written to. This is the state of a redo log that was just added, or just after a `RESETLOGS`, when it is not the current redo log. - `CURRENT` - Current redo log. This implies that the redo log is active. The redo log could be open or closed. - `ACTIVE` - Log is active but is not the current log. It is needed for crash recovery. It may be in use for block recovery. It may or may not be archived. - `CLEARING` - Log is being re-created as an empty log after an `ALTER DATABASE CLEAR LOGFILE` statement. After the log is cleared, the status changes to `UNUSED`. - `CLEARING_CURRENT` - Current log is being cleared of a closed thread. The log can stay in this status if there is some failure in the switch such as an I/O error writing the new log header. - `INACTIVE` - Log is no longer needed for instance recovery. It may be in use for media recovery. It may or may not be archived. |
| `FIRST_CHANGE#` | `NUMBER` | Lowest system change number (SCN) in the log |
| `FIRST_TIME` | `DATE` | Time of the first SCN in the log |
| `NEXT_CHANGE#` | `NUMBER` | Highest change number (SCN) in the log  When `STATUS=CURRENT`, `NEXT_CHANGE#` is set to the highest possible SCN, 9295429630892703743. |
| `NEXT_TIME` | `DATE` | Time of the highest SCN in the log. When `STATUS=CURRENT`, `NEXT_TIME` is set to `NULL`. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |