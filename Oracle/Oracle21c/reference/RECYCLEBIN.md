---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/RECYCLEBIN.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.301 RECYCLEBIN

`RECYCLEBIN` is used to control whether the Flashback Drop capability is turned on or off.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `RECYCLEBIN = { on \| off }` |
| Default value | `on` |
| Modifiable | `ALTER SESSION`,` ALTER SYSTEM ... DEFERRED` |
| Modifiable in a PDB | Yes |
| Basic | No |

If the parameter is set to `off`, then dropped tables do not go into the recycle bin. If this parameter is set to `on`, then dropped tables go into the recycle bin and can be recovered.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN01511) for more information about using Flashback Drop and managing the recycle bin