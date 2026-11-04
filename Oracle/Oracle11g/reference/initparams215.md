---
title: REPLICATION_DEPENDENCY_TRACKING
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams215.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `true` |
| Modifiable | No |
| Range of values | `true \| false` |

`REPLICATION_DEPENDENCY_TRACKING` enables or disables dependency tracking for read/write operations to the database. Dependency tracking is essential for propagating changes in a replicated environment in parallel.

Values:

- `TRUE`
	Enables dependency tracking.
- `FALSE`
	Allows read/write operations to the database to run faster, but does not produce dependency information for Oracle to perform parallel propagation.
	Note:
	Do not specify this value unless you are sure that your application will not perform any read/write operations to the replicated tables.

See Also:

[Oracle Database Advanced Replication](https://docs.oracle.com/cd/E11882_01/server.112/e10706/toc.htm) for more information on parallel propagation dependency tracking