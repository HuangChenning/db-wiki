---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/TRACE_ENABLED.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.367 TRACE\_ENABLED

`TRACE_ENABLED` controls tracing of the execution history, or code path, of Oracle. Oracle Support Services uses this information for debugging.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `true` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | The default value is `TRUE`. Oracle recommends that multiple instances have the same value. |

When `TRACE_ENABLED` is set to `true`, Oracle records information in specific files when errors occur.

Oracle records this information for all instances, even if only one instance terminates. This allows Oracle to retain diagnostics for an entire cluster.

Although the overhead incurred from this processing is not excessive, you can improve performance by setting `TRACE_ENABLED` to `false`. You might do this, for example, to meet high-end benchmark requirements. However, if you leave this parameter set to `false`, you may lose valuable diagnostic information. Therefore, always set `TRACE_ENABLED` to `true` to trace system problems and to reduce diagnostic efforts when unexplained instance failures occur.