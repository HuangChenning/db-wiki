---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-3-create-standby-database-service.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 3: Create the Standby Database Service

On the standby cluster, a database service is required for the standby database so that the Oracle Grid Infrastructure Agent automatically starts the Oracle GoldenGate deployment when the database is opened with the primary role.

When a source database is in a multitenant environment, a separate service is required for the root container database (CDB) and the pluggable database (PDB) that contains the schema being replicated. For a multitenant environment target database, a single service is required for the PDB.

Create the service using the following command, as the `oracle` user, the same way the service was created on the primary cluster.

```
$ srvctl add service -db dbName -service service_name
 -preferred instance_1 -available instance_2, instance_3 etc.
 -pdb pdbName -role PRIMARY
```

It is recommended that you use the same service name as was specified on the primary cluster. The service must be created as a singleton service, using the `–preferred` option, because the application Virtual IP address (VIP), DBFS, and Oracle GoldenGate run on the cluster node where the service is running.

If the database is not in a multitenant environment, or the database is a target database for Oracle GoldenGate, omit the `-pdb` parameter.