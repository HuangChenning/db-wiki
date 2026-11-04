---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/LOG_BUFFER.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.192 LOG\_BUFFER

`LOG_BUFFER` specifies the amount of memory (in bytes) that Oracle uses when buffering redo entries to a redo log file.

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Default value | 2 MB to 32 MB, depending on the SGA size and CPU count |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | 2 MB to operating system-dependent |
| Basic | No |

Redo log entries contain a record of the changes that have been made to the database block buffers. The LGWR process writes redo log entries from the log buffer to a redo log file.

The log buffer size depends on the number of redo strands in the system. One redo strand is allocated for every 16 CPUs and has a default size of 2 MB. Oracle allocates a minimum of 2 redo strands per instance. When the log buffer size is not specified, any remaining memory in the redo granules is given to the log buffer.

See Also:

- Your operating system-specific Oracle documentation for the default value and range of values
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA555) for information on resizing the redo log buffer using this parameter