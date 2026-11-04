---
title: "V$ENABLEDPRIVS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1123.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ENABLEDPRIVS` displays which privileges are enabled. These privileges can be found in the table `SYSTEM_PRIVILEGE_MAP`.

| Column | Datatype | Description |
| --- | --- | --- |
| `PRIV_NUMBER` | `NUMBER` | Numeric identifier of enabled privileges |

See Also:

["SYSTEM\_PRIVILEGE\_MAP"](statviews_5186.md)