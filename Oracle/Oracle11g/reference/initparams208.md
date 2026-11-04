---
title: RECYCLEBIN
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams208.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `RECYCLEBIN = { on \| off }` |
| Default value | `on` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM ... DEFERRED` |
| Basic | No |

`RECYCLEBIN` is used to control whether the Flashback Drop capability is turned on or off. If the parameter is set to `off`, then dropped tables do not go into the recycle bin. If this parameter is set to `on`, then dropped tables go into the recycle bin and can be recovered.