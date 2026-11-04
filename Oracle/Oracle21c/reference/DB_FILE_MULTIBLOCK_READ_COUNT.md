---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DB_FILE_MULTIBLOCK_READ_COUNT.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.81 DB\_FILE\_MULTIBLOCK\_READ\_COUNT

`DB_FILE_MULTIBLOCK_READ_COUNT` specifies the maximum number of blocks read in one I/O operation during a sequential scan.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | The default value corresponds to the maximum I/O size that can be efficiently performed and is platform-dependent |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | Operating system-dependent |
| Basic | No |

`DB_FILE_MULTIBLOCK_READ_COUNT` is one of the parameters you can use to minimize I/O during table scans. The total number of I/Os needed to perform a full table scan depends on such factors as the size of the table, the multiblock read count, and whether parallel execution is being utilized for the operation.

The default value of this parameter is a value that corresponds to the maximum I/O size that can be performed efficiently. This value is platform-dependent and is 1MB for most platforms.

Because the parameter is expressed in blocks, it will be set to a value that is equal to the maximum I/O size that can be performed efficiently divided by the standard block size. Note that if the number of sessions is extremely large the multiblock read count value is decreased to avoid the buffer cache getting flooded with too many table scan buffers.

Even though the default value may be a large value, the optimizer will not favor large I/Os if you do not set this parameter. It will favor large I/Os only if you explicitly set this parameter to a large value.

Online transaction processing (OLTP) and batch environments typically have values in the range of 4 to 16 for this parameter. DSS and data warehouse environments tend to benefit most from maximizing the value of this parameter. The optimizer is more likely to choose a full table scan over an index if the value of this parameter is high.

The maximum value is the operating system's maximum I/O size expressed as Oracle blocks ((max I/O size)/ `DB_BLOCK_SIZE`). If you set this parameter to a value greater than the maximum, then Oracle uses the maximum.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA-GUID-E8F12EF9-B4A8-441F-9814-763BB793FAF9) for information about how setting this parameter incorrectly can cause excessive I/O waits for some execution plans