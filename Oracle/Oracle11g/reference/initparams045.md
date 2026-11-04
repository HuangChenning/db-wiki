---
title: CURSOR_SPACE_FOR_TIME
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams045.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | No |
| Range of values | `true \| false` |
| Basic | No |

Note:

The `CURSOR_SPACE_FOR_TIME` parameter is deprecated. It is retained for backward compatibility only.

`CURSOR_SPACE_FOR_TIME` lets you use more space for cursors in order to save time. It affects both the shared SQL area and the client's private SQL area.

Most users will not need to set this parameter because of the significantly enhanced concurrency modifications introduced in Oracle Database 10g Release 2 (10.2.0.2) and later.

Values:

- `true`
	Shared SQL areas are kept pinned in the shared pool. As a result, shared SQL areas are not aged out of the pool as long as an open cursor references them. Because each active cursor's SQL area is present in memory, execution is faster. However, the shared SQL areas never leave memory while they are in use. Therefore, you should set this parameter to `true` only when the shared pool is large enough to hold all open cursors simultaneously.
	In addition, a setting of `true` retains the private SQL area allocated for each cursor between executions instead of discarding it after cursor execution, saving cursor allocation and initialization time.
- `false`
	Shared SQL areas can be deallocated from the library cache to make room for new SQL statements.

Note:

If this parameter is set to `true`, then the `SERIAL_REUSE` parameter is disabled.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm) and [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm)
- ["SERIAL\_REUSE"](initparams230.md)