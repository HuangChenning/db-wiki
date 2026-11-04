---
title: TRACE_ENABLED
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams260.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `true` |
| Modifiable | `ALTER SYSTEM` |
| Range of values | `true \| false` |
| Oracle RAC | The default value is `TRUE`. Oracle recommends that multiple instances have the same value. |

`TRACE_ENABLED` controls tracing of the execution history, or code path, of Oracle. Oracle Support Services uses this information for debugging.

When `TRACE_ENABLED` is set to `true`, Oracle records information in specific files when errors occur.

Oracle records this information for all instances, even if only one instance terminates. This allows Oracle to retain diagnostics for an entire cluster.

Although the overhead incurred from this processing is not excessive, you can improve performance by setting `TRACE_ENABLED` to `false`. You might do this, for example, to meet high-end benchmark requirements. However, if you leave this parameter set to `false`, you may lose valuable diagnostic information. Therefore, always set `TRACE_ENABLED` to `true` to trace system problems and to reduce diagnostic efforts in the event of unexplained instance failures.