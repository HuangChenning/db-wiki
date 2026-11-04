---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-2-create-database-replication-administrator-user.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 2: Create the Database Replication Administrator User

The source and target Oracle databases need a GoldenGate Administrator user with appropriate privileges assigned.

For single tenant (non-CDB architecture) databases, see [Establishing Oracle GoldenGate Credentials](https://docs.oracle.com/en/middleware/goldengate/core/21.3/oracle-db/establishing-oracle-goldengate-credentials.html#GUID-F9EBB989-E22F-4355-BE60-40F957B8515E)

For a multitenant source database, GoldenGate Extract must be configured to connect to a user in the root container database, using a `c##` account. For a multitenant target database, a separate GoldenGate administrator user is needed for each PDB that a Replicat applies data to.

For more details about creating a GoldenGate Administrator in an Oracle Multitenant Database, see [Configuring Oracle GoldenGate in a Multitenant Container Database](https://docs.oracle.com/en/middleware/goldengate/core/21.3/oracle-db/configuring-oracle-goldengate-multitenant-container-database-1.html#GUID-0B0CEB35-51C6-4319-BEE1-FA208FF4DE05)