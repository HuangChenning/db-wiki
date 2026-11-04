---
title: DB_BLOCK_CHECKING
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams048.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DB_BLOCK_CHECKING = { FALSE \| OFF \| LOW \| MEDIUM \| TRUE \| FULL }` |
| Default value | `FALSE` |
| Modifiable | `ALTER SYSTEM` |
| Basic | No |

`DB_BLOCK_CHECKING` specifies whether or not Oracle performs block checking for database blocks.

Values:

- `OFF` or `FALSE`
	No block checking is performed for blocks in user tablespaces. However, semantic block checking for `SYSTEM` tablespace blocks is always turned on.
- `LOW`
	Basic block header checks are performed after block contents change in memory (for example, after `UPDATE` or `INSERT` statements, on-disk reads, or inter-instance block transfers in Oracle RAC).
- `MEDIUM`
	All `LOW` checks and full semantic checks are performed for all objects except indexes (whose contents can be reconstructed by a drop+rebuild on encountering a corruption).
- `FULL` or `TRUE`
	All `LOW` and `MEDIUM` checks and full semantic checks are performed for all objects.

Oracle checks a block by going through the data in the block, making sure it is logically self-consistent. Block checking can often prevent memory and data corruption. Block checking typically causes 1% to 10% overhead, depending on workload and the parameter value. Specific DML overhead may be higher. The more updates or inserts in a workload, the more expensive it is to turn on block checking. You should set `DB_BLOCK_CHECKING` to `FULL` if the performance overhead is acceptable.

For backward compatibility, the use of `FALSE` (implying `OFF`) and `TRUE` (implying `FULL`) is preserved.