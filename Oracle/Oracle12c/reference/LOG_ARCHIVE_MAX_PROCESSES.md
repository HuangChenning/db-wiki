---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/LOG_ARCHIVE_MAX_PROCESSES.html
tags:
  - oracle
  - 12c
  - reference
---

`LOG_ARCHIVE_MAX_PROCESSES` specifies the maximum number of ARCn processes that can be created.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `4` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | `1` to `30` |
| Basic | No |

See Also:

- " [Background Processes](background-processes.md) " for more information about ARCn processes
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADMIN11337) for more information about `LOG_ARCHIVE_MAX_PROCESSES`