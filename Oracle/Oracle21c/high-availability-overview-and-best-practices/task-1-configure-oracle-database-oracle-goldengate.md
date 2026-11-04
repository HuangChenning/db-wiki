---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-1-configure-oracle-database-oracle-goldengate.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 1: Configure the Oracle Database for Oracle GoldenGate

The source and target Oracle GoldenGate databases should be configured using the following recommendations.

- Enable Oracle GoldenGate replication by setting the database initialization parameter `ENABLE_GOLDENGATE_REPLICATION=TRUE`.
- Run the Oracle GoldenGate source database in `ARCHIVELOG` mode.
- Enable `FORCE LOGGING` mode in the Oracle GoldenGate source database.
- Enable minimal supplemental logging in the source database. Additionally, add schema or table level logging for all replicated objects.
- If the Replicat process will be used, configure the streams pool in the System Global Area (SGA) on the source database using the `STREAMS_POOL_SIZE` initialization parameter.
	Note that the streams pool is only needed on the target database if integrated Replicat will be used.
	Use the following equation to determine the value for `STREAMS_POOL_SIZE`:
	`STREAMS_POOL_SIZE` = (#Extracts and #Integrated Replicats \* 1GB) \* 1.25
	For example, in a database with 2 Extracts and 2 integrated Replicats:
	`STREAMS_POOL_SIZE` = 4GB \* 1.25 = 5GB
	When adding Extract or Replicat processes, it is important to recalculate and configure the new streams pool size requirement.

For more information about preparing the database for Oracle GoldenGate, see [Preparing the Database for Oracle GoldenGate](https://docs.oracle.com/en/middleware/goldengate/core/21.3/oracle-db/preparing-database-oracle-goldengate.html#GUID-E06838BD-0933-4027-8A6C-D4A17BDF4E41).