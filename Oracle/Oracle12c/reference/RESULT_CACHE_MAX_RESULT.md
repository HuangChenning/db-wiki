---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/RESULT_CACHE_MAX_RESULT.html
tags:
  - oracle
  - 12c
  - reference
---

`RESULT_CACHE_MAX_RESULT` specifies the percentage of `RESULT_CACHE_MAX_SIZE` that any single result can use.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `5` percent |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | `0` to `100` |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |