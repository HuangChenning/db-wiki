---
title: OPTIMIZER_SECURE_VIEW_MERGING
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams172.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `true` |
| Modifiable | `ALTER SYSTEM` |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | Multiple instances can have different values |

`OPTIMIZER_SECURE_VIEW_MERGING` enables the optimizer to use view merging to improve query performance without performing the checks that would otherwise be performed to ensure that view merging does not violate any security intentions of the view creator.

Values:

- `false`
	Oracle does not perform security checks that may prevent view merging and predicate move-around.
- `true`
	Oracle performs checks to ensure that view merging and predicate move-around do not violate any security intentions of the view creator.

To take advantage of query rewrite for a particular query, you must disable the `OPTIMIZER_SECURE_VIEW_MERGING` parameter.