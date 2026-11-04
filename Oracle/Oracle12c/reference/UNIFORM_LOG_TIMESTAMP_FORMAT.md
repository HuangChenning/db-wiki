---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/UNIFORM_LOG_TIMESTAMP_FORMAT.html
tags:
  - oracle
  - 12c
  - reference
---

`UNIFORM_LOG_TIMESTAMP_FORMAT` specifies that a uniform timestamp format be used in Oracle Database trace (.trc) files and log files (such as the alert log).

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `true` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | Multiple instances should use the same value. |

When the value of `UNIFORM_LOG_TIMESTAMP_FORMAT` is `TRUE`, the format used for timestamps in trace files is standardized on universal time with millisecond precision. For example:

```
2012-09-26 00:16:47.154
```

When the value of `UNIFORM_LOG_TIMESTAMP_FORMAT` is `FALSE`, trace files include a mix of timestamps using different precisions, with some timestamps showing local time and other timestamps showing universal time.

Note:

This initialization parameter is available starting with Oracle Database 12c Release 2 (12.2.0.1).