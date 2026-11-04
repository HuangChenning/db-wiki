---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/CLIENT_RESULT_CACHE_SIZE.html
tags:
  - oracle
  - 12c
  - reference
---

`CLIENT_RESULT_CACHE_SIZE` specifies the maximum size of the client per-process result set cache (in bytes).

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `CLIENT_RESULT_CACHE_SIZE = ` `integer` ` [K \| M \| G]` |
| Default value | `0` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | `0` to operating system-dependent |
| Basic | No |

All OCI client processes inherit this maximum size. Setting a nonzero value enables the client query cache feature. This can be overridden by the client configuration parameter `OCI_RESULT_CACHE_MAX_SIZE`.

See Also:

[Oracle Call Interface Programmer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=LNOCI10103) for more information about the client query cache feature