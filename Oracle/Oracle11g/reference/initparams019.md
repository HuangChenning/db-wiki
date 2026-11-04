---
title: BACKGROUND_CORE_DUMP
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams019.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `BACKGROUND_CORE_DUMP = { partial \| full }` |
| Default value | `partial` |
| Modifiable | No |
| Basic | No |

`BACKGROUND_CORE_DUMP` specifies whether Oracle includes the SGA in the core file for Oracle background processes.

Values:

- `partial`
	Oracle does not include the SGA in the core dump.
- `full`
	Oracle includes the SGA in the core dump.

See Also:

["SHADOW\_CORE\_DUMP"](initparams237.md)