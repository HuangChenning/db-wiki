---
title: CONTROL_FILE_RECORD_KEEP_TIME
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams036.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `7` (days) |
| Modifiable | `ALTER SYSTEM` |
| Range of values | `0` to `365` (days) |
| Basic | No |

`CONTROL_FILE_RECORD_KEEP_TIME` specifies the minimum number of days before a reusable record in the control file can be reused. In the event a new record needs to be added to a reusable section and the oldest record has not aged enough, the record section expands. If this parameter is set to 0, then reusable sections never expand, and records are reused as needed.

If the number of reusable records in the control file exceeds the circular reuse record limit `UB4MAXVAL`, then reusable records will be overwritten even if `CONTROL_FILE_RECORD_KEEP_TIME` has not elapsed. `UB4MAXVAL` is defined in the `oratypes`.`h` header file, which is found in the `public` directory. Its value may vary according to the operating system you are using.

Note:

This parameter applies only to records in the control file that are circularly reusable (such as archive log records and various backup records). It does not apply to records such as datafile, tablespace, and redo thread records, which are never reused unless the corresponding object is dropped from the tablespace.