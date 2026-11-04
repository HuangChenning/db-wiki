---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-1-configure-standby-database-oracle-goldengate.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 1: Configure the Standby Database for Oracle GoldenGate

The standby database initialization parameters should match those of the primary database.

See [Task 1: Configure the Oracle Database for Oracle GoldenGate](task-1-configure-oracle-database-oracle-goldengate.md) for details. This includes the following parameters:

- `ENABLE_GOLDENGATE_REPLICATION=TRUE`
- For Oracle GoldenGate source databases, enable `FORCE LOGGING` mode and enable minimal supplemental logging.
- If a GoldenGate source database, or running integrated Replicat (parallel or non-parallel), configure the `STREAMS_POOL_SIZE`.