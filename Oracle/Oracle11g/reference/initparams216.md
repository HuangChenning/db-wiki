---
title: RESOURCE_LIMIT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams216.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | `ALTER SYSTEM` |
| Range of values | `true \| false` |

`RESOURCE_LIMIT` determines whether resource limits are enforced in database profiles.

Values:

- `TRUE`
	Enables the enforcement of resource limits
- `FALSE`
	Disables the enforcement of resource limits

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) and [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for more information on setting resource limits for profiles