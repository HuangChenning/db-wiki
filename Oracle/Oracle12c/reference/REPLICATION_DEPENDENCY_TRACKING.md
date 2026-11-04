---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/REPLICATION_DEPENDENCY_TRACKING.html
tags:
  - oracle
  - 12c
  - reference
---

`REPLICATION_DEPENDENCY_TRACKING` enables or disables dependency tracking for read/write operations to the database.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `true` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |

Dependency tracking is essential for propagating changes in a replicated environment in parallel.

Values

- `TRUE`
	Enables dependency tracking.
- `FALSE`
	Allows read/write operations to the database to run faster, but does not produce dependency information for Oracle to perform parallel propagation.
	Note:
	Do not specify this value unless you are sure that your application will not perform any read/write operations to the replicated tables.