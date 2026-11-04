---
title: SHADOW_CORE_DUMP
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams237.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `SHADOW_CORE_DUMP = { partial \| full \| none }` |
| Default value | `partial` |
| Modifiable | No |

`SHADOW_CORE_DUMP` specifies whether Oracle includes the SGA in the core file for foreground (client) processes.

Values:

- `partial`
	Oracle does not include the SGA in the core dump.
- `full`
	Oracle includes the SGA in the core dump.
- `none`
	No core files will be generated for foreground processes.

See Also:

["BACKGROUND\_CORE\_DUMP"](initparams019.md)