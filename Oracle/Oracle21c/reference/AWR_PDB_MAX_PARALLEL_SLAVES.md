---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/AWR_PDB_MAX_PARALLEL_SLAVES.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.29 AWR\_PDB\_MAX\_PARALLEL\_SLAVES

`AWR_PDB_MAX_PARALLEL_SLAVES` enables a DBA to allocate the correct amount of resources to enable quick and timely Automatic Workload Repository (AWR) flushes for multitenant container databases (CDBs).

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | 10 |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | 1 – 30 |
| Basic | No |
| Oracle RAC | Different instances can use different values. |

Use `AWR_PDB_MAX_PARALLEL_SLAVES` to control the amount of resources dedicated to AWR snapshot flushing in pluggable databases (PDBs). With this parameter, a DBA can modify the maximum number of MMON worker processes (Mnnn background processes) that can concurrently be used to handle AWR flush operations for the entire CDB.

For CDBs with a large number of PDBs enabled to create automatic AWR snapshots, a DBA can increase this parameter to enable timely AWR flushing. For CDBs with a small number of PDBs enabled, the value of this parameter can be decreased to reduce the concurrency and the chance of performance spikes.

Note that this parameter is set in the root of a CDB and determines the maximum degree of parallelism used to create AWR automatic snapshots for PDBs.

See Also:

- " [AWR\_PDB\_AUTOFLUSH\_ENABLED](AWR_PDB_AUTOFLUSH_ENABLED.md) " for information about enabling the automatic creation of AWR PDB snapshots
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA-GUID-9D3A3890-8E68-48C5-84D0-DB0A8D93C53A) for an introduction to AWR
- " [Background Processes](background-processes.md) " for more information about the MMON and Mnnn background processes