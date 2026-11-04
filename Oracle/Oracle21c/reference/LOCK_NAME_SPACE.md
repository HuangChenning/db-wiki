---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/LOCK_NAME_SPACE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.181 LOCK\_NAME\_SPACE

`LOCK_NAME_SPACE` specifies the namespace that the distributed lock manager (DLM) uses to generate lock names.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `LOCK_NAME_SPACE = ` `namespace` |
| Default value | There is no default value. |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | Up to 8 alphanumeric characters. No special characters allowed. |
| Basic | No |

Note:

The `LOCK_NAME_SPACE` parameter is deprecated. It is retained for backward compatibility only.

Consider setting this parameter if a standby or clone database has the same database name on the same cluster as the primary database.

If the standby database resides on the same file system as the primary database, then set `LOCK_NAME_SPACE` in the standby parameter file to a distinct value such as the following:

```
LOCK_NAME_SPACE = standby
```