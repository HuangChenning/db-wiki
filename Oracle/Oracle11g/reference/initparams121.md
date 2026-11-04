---
title: LOCK_NAME_SPACE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams121.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `LOCK_NAME_SPACE =` `namespace` |
| Default value | There is no default value. |
| Modifiable | No |
| Range of values | Up to 8 alphanumeric characters. No special characters allowed. |
| Basic | No |

Note:

The `LOCK_NAME_SPACE` parameter is deprecated. It is retained for backward compatibility only.

`LOCK_NAME_SPACE` specifies the namespace that the distributed lock manager (DLM) uses to generate lock names. Consider setting this parameter if a standby or clone database has the same database name on the same cluster as the primary database.

If the standby database resides on the same file system as the primary database, then set `LOCK_NAME_SPACE` in the standby parameter file to a distinct value such as the following:

```
LOCK_NAME_SPACE = standby
```