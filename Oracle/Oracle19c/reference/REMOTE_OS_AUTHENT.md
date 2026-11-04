---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/REMOTE_OS_AUTHENT.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.307 REMOTE\_OS\_AUTHENT

`REMOTE_OS_AUTHENT` specifies whether remote clients will be authenticated with the value of the `OS_AUTHENT_PREFIX` parameter.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |

Note:

The `REMOTE_OS_AUTHENT` parameter is deprecated. It is retained for backward compatibility only.

See Also:

" [OS\_AUTHENT\_PREFIX](OS_AUTHENT_PREFIX.md) "