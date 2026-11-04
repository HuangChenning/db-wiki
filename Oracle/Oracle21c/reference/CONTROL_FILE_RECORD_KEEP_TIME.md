---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/CONTROL_FILE_RECORD_KEEP_TIME.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.54 CONTROL\_FILE\_RECORD\_KEEP\_TIME

`CONTROL_FILE_RECORD_KEEP_TIME` specifies the minimum number of days before a reusable record in the control file can be reused.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `7` (days) |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | `0` to `365` (days) |
| Basic | No |

In the event a new record must be added to a reusable section and the oldest record has not aged enough, the record section expands. If this parameter is set to 0, then reusable sections never expand, and records are reused as needed.

If the number of reusable records in the control file exceeds the circular reuse record limit `UB4MAXVAL`, then reusable records will be overwritten even if `CONTROL_FILE_RECORD_KEEP_TIME` has not elapsed. `UB4MAXVAL` is defined in the `oratypes`.`h` header file, which is found in the `public` directory. Its value may vary according to the operating system you are using.

Note:

This parameter applies only to records in the control file that are circularly reusable (such as archive log records and various backup records). It does not apply to records such as data file, tablespace, and redo thread records, which are never reused unless the corresponding object is dropped from the tablespace.

See Also:

- " [CONTROL\_FILES](CONTROL_FILES.md) "
- [Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=BRADV89687) for more information about this parameter