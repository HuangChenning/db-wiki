---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/MAX_DISPATCHERS.html
tags:
  - oracle
  - 12c
  - reference
---

`MAX_DISPATCHERS` specifies the maximum number of dispatcher processes allowed to be running simultaneously.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | There is no default value. |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | If `MAX_DISPATCHERS` is specified, then it should be greater than or equal to the number of dispatchers specified by the `DISPATCHERS` parameter and less than the number of processes specified by the `PROCESSES` parameter. |
| Basic | No |

This parameter can be overridden by the `DISPATCHERS` parameter and is maintained for backward compatibility with older releases.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADMIN11180) for more information about this parameter
- Your operating system-specific Oracle documentation for the default value and range of values