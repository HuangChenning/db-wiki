---
title: OLAP_PAGE_POOL_SIZE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams162.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `OLAP_PAGE_POOL_SIZE =` `integer` `[K \| M \| G]` |
| Default value | `0` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM ... DEFERRED` |
| Range of values | `0` to 2 GB |

`OLAP_PAGE_POOL_SIZE` specifies (in bytes) the size of the OLAP page pool.

See Also:

[Oracle OLAP User's Guide](https://docs.oracle.com/cd/E11882_01/olap.112/e17123/toc.htm) for more information about the OLAP page pool