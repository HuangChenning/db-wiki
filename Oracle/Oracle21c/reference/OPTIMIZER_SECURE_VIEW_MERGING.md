---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/OPTIMIZER_SECURE_VIEW_MERGING.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.255 OPTIMIZER\_SECURE\_VIEW\_MERGING

`OPTIMIZER_SECURE_VIEW_MERGING` enables the optimizer to use view merging to improve query performance without performing the checks that would otherwise be performed to ensure that view merging does not violate any security intentions of the view creator.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `true` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | Multiple instances can have different values |

Values

- `false`
	Oracle Database does not perform security checks that may prevent view merging and predicate move-around.
- `true`
	Oracle Database performs checks to ensure that view merging and predicate move-around do not violate any security intentions of the view creator.

To enable the optimizer to use view merging for any query issued by a user, you must grant the `MERGE ANY VIEW` privilege to the user. Grant the `MERGE VIEW` privilege to a user on specific views to enable the optimizer to use view merging for queries on these views. These privileges are required only under specific conditions, such as when a view is not merged because the security checks fail.

See Also:

[Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGSQL209) for more information about view merging