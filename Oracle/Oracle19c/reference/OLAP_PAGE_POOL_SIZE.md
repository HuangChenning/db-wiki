---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/OLAP_PAGE_POOL_SIZE.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.239 OLAP\_PAGE\_POOL\_SIZE

`OLAP_PAGE_POOL_SIZE` specifies (in bytes) the size of the OLAP page pool.

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `OLAP_PAGE_POOL_SIZE = ` `integer` ` [K \| M \| G]` |
| Default value | `0` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM ... DEFERRED` |
| Modifiable in a PDB | Yes |
| Range of values | 0, 2097152 (2 MB) to 2 <sup>31</sup> - 1 |
| Basic | No |

Caution:

Oracle strongly recommends that you leave this parameter set to its default value of `0`. This instructs the database to autonomously adjust the OLAP page pool size to serve the requirements of the analytic workspaces. Setting this parameter to a value other than `0` can lead to errors in OLAP processing or wasted memory.

See Also:

[Oracle OLAP User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=OLAUG100) for more information about the OLAP option for Oracle Database