---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/BACKGROUND_CORE_DUMP.html
tags:
  - oracle
  - 12c
  - reference
---

`BACKGROUND_CORE_DUMP` specifies whether Oracle includes the SGA in the core file for Oracle background processes.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `BACKGROUND_CORE_DUMP = { partial \| full }` |
| Default value | `partial` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |

Values

- `partial`
	Oracle does not include the SGA in the core dump.
- `full`
	Oracle includes the SGA in the core dump.

See Also:

" [SHADOW\_CORE\_DUMP](SHADOW_CORE_DUMP.md) "