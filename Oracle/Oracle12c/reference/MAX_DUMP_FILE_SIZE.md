---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/MAX_DUMP_FILE_SIZE.html
tags:
  - oracle
  - 12c
  - reference
---

`MAX_DUMP_FILE_SIZE` specifies the maximum size of trace files (excluding the alert log).

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `MAX_DUMP_FILE_SIZE = { ` `integer` ` [K \| M \| G] \| UNLIMITED }` |
| Default value | `UNLIMITED` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | 0 to unlimited, or `UNLIMITED` |
| Basic | No |

You can change this limit if you are concerned that trace files may use too much space.

- A numeric value for `MAX_DUMP_FILE_SIZE` specifies the maximum size in operating system blocks.
- A numeric value followed by a `K` or `M` or `G` suffix specifies the file size in kilobytes, megabytes, or gigabytes.
- The special value string `UNLIMITED` means that there is no upper limit on trace file size. Thus, dump files can be as large as the operating system permits.

When the trace file is limited in size, it may be automatically split into multiple files, called segments, if needed. This process is call trace file segmentation. The segments will have the same file name as the active trace file, but with an extra segment number appended.

The trace file can be split into a maximum of 5 segments, and the size of each segment will typically be 1/5th of the trace file limit.

When the combined size of all the trace file segments exceeds the specified limit, the oldest segment is deleted, and a new, empty segment is created. Thus, the trace file always contains the most recent trace information. The first segment is never deleted, because it may contain relevant information about the initial state of the process.

Note that trace file segmentation will not occur when this parameter is set to a value less than 25 MB.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADMIN11244) and [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=TGSQL809) for more information on setting this parameter