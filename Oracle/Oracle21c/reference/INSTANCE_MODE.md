---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/INSTANCE_MODE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.163 INSTANCE\_MODE

`INSTANCE_MODE` indicates whether the instance is read-write, read-only, or read-mostly.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `INSTANCE_MODE = { READ-WRITE \| READ-ONLY \| READ-MOSTLY }` |
| Default value | `READ-WRITE` |
| Modifiable | No |
| Basic | No |
| Oracle RAC | See the Oracle RAC restrictions in the initialization parameter description below. |

A `READ-WRITE` instance is a regular Oracle instance.

A `READ-ONLY` instance is an Oracle instance that can only be opened in read-only mode.

A `READ-MOSTLY` instance is an Oracle instance that performs very few database writes.

These restrictions apply when setting the parameter on different Oracle Real Application Clusters (Oracle RAC) instances:

1. There must be at least one running instance with `INSTANCE_MODE` set to `READ-WRITE` at any given time. If the only instance with `INSTANCE_MODE` set to `READ-WRITE` goes down, all other instances will be brought down by Oracle automatically.
2. An instance with `INSTANCE_MODE` set to `READ-ONLY` cannot be the first instance to open a database or any pluggable database (PDB) among all instances in an Oracle RAC cluster.
3. Oracle does not support co-existence of an instance with `INSTANCE_MODE` set to `READ-ONLY` and an instance with `INSTANCE_MODE` set to `READ-MOSTLY` in the same Oracle RAC cluster.