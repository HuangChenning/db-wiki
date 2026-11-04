---
title: WORKAREA_SIZE_POLICY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams271.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `WORKAREA_SIZE_POLICY = { AUTO \| MANUAL }` |
| Default value | `AUTO` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |

`WORKAREA_SIZE_POLICY` specifies the policy for sizing work areas. This parameter controls the mode in which working areas are tuned.

Values:

- `AUTO`
	Work areas used by memory-intensive operators are sized automatically, based on the PGA memory used by the system, the target PGA memory set in `PGA_AGGREGATE_TARGET`, and the requirement of each individual operator.
- `MANUAL`
	The sizing of work areas is manual and based on the values of the \* `_AREA_SIZE` parameter corresponding to the operation (for example, a sort uses `SORT_AREA_SIZE`). Specifying `MANUAL` may result in sub-optimal performance and poor PGA memory utilization.