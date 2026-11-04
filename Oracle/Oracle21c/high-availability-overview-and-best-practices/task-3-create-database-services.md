---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-3-create-database-services.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 3: Create the Database Services

A database service is required so that the Oracle Grid Infrastructure Agent automatically starts the GoldenGate deployment when the database is opened. When DBFS is used for the shared file system, the database service is also used to mount DBFS to the correct Oracle RAC instance.

When using a source multitenant database, a separate service is required for the root container database (CDB) and the pluggable database (PDB) that contains the schema being replicated. For a target multitenant database, a single service is required for the PDB.

Create the service using the following command, as the `oracle` user.

```
$ srvctl add service -db db_name -service service_name
 -preferred instance_1 -available instance_2, instance_3 etc.
 -pdb PDB_name
```

For example:

```
$ srvctl add service -db ggdb -service oggserv_pdb -preferred ggdb1
    -available ggdb2 –pdb GGPDB01
```

It you are not using Oracle Multitenant Database, omit the `-pdb` parameter.