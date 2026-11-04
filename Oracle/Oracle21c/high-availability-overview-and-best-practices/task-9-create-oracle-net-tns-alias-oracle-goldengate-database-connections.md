---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-9-create-oracle-net-tns-alias-oracle-goldengate-database-connections.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 9: Create Oracle Net TNS Alias for Oracle GoldenGate Database Connections

Create a TNS alias on all of the Oracle RAC nodes where Oracle GoldenGate may be started to provide local database connections for the GoldenGate processes when switching between Oracle RAC nodes. Create the TNS alias in the `tnsnames.ora` file in the `TNS_ADMIN` directory specified in the deployment creation.

If the source database is a multitenant database, two TNS alias entries are required: one for the container database (CDB) and one for the pluggable database (PDB) that is being replicated. For a target multitenant database, the TNS alias connects the PDB where replicated data is being applied to. The pluggable database `SERVICE_NAME` should be set to the database service created in an earlier step (refer to [Task 3: Create the Database Services](task-3-create-database-services.md)).

Below are some example source database TNS alias definitions using the IPC protocol, which must be defined locally on all RAC nodes.

```
OGGSOURCE_CDB =
    (DESCRIPTION =
      (ADDRESS = (PROTOCOL=IPC)(KEY=LISTENER))
      (CONNECT_DATA =
        (SERVICE_NAME = oggserv_cdb)
       )
    )

OGGSOURCE_PDB =
    (DESCRIPTION =
      (ADDRESS = (PROTOCOL=IPC)(KEY=LISTENER))
      (CONNECT_DATA =

        (SERVICE_NAME = oggserv_pdb)
       )
    )
```

Note:

When the `tnsnames.ora` or `sqlnet.ora`, located in the `TNS_ADMIN` directory for the GoldenGate deployment, are modified, the deployment needs to be restarted in order to pick up the changes.

With the GoldenGate deployment created, use the Administration Server home page to create the database credentials using the above TNS alias names. See Figure 6 below for an example of the database credential creation using the TNS alias appended to the database user name in the ‘User ID” field.

If the source database is a multitenant database, create database credentials for the CDB and PDB. If the target database is a multitenant database, create a single credential for the PDB.