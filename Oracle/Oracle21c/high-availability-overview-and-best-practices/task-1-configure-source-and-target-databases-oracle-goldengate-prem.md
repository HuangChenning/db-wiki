---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-1-configure-source-and-target-databases-oracle-goldengate-prem.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 1: Configure the Source and Target Databases for Oracle GoldenGate

The source and target Oracle GoldenGate databases should be configured using the following recommendations.

Perform the following steps to complete this task:

- Step 1.1 - Database Configuration
- Step 1.2 - Create the Database Replication Administrator User
- Step 1.3 - Create the Database Services

Step 1.1 - Database Configuration

The source and target Oracle GoldenGate databases should be configured using the following recommendations:

| Configuration | Scope | Example |
| --- | --- | --- |
| Enable Archivelog Mode | Source and Target | ``` SQL> ARCHIVE LOG LIST Database log mode              Archive Mode Automatic archival             Enabled Archive destination            USE_DB_RECOVERY_FILE_DEST Oldest online log sequence     110 Next log sequence to archive   113 Current log sequence           113 ``` |
| Enable `FORCE                                                   LOGGING` | Source and Target | ``` ALTER DATABASE FORCE LOGGING; ``` |
| `ENABLE_GOLDENGATE_REPLICATION` | Source, Target, and Standbys | ``` ALTER SYSTEM  SET ENABLE_GOLDENGATE_REPLICATION=TRUE  SCOPE=BOTH SID='*'; ``` |
| Enable Subset Database Replication Logging | Source  Required on Target for cases when replication reverses | To enable subset database replication logging follow the steps in the Oracle GoldenGate Microservices Architecture documentation: [Enable Subset Database Replication Logging](https://docs.oracle.com/en/database/goldengate/core/26/coredoc/prepare-transaction-logs-settings-and-requirements-ogg-oracle.html#GUID-4BF9C545-1AD7-4364-8B26-1D3A1F6460E4) |
| Set `STREAMS_POOL_SIZE` larger to accommodate GoldenGate only if CDB Root-Level integrated Extract and integrated Replicat is used  Note:  Note: It is recommended that you use per-PDB Extract and parallel Replicat which uses Shared Pool, and there is no need to explicitly set the Streams Pool. Refer to MOS document 2998659.1 for clarification. | Source  Required on Target for cases when replication reverses | The value of `STREAMS_POOL_SIZE` should be set to the following value:  `STREAMS_POOL_SIZE` = (((#Extracts + #Integrated Replicats) \* 1GB) \* 1.25)  For example, in a database with 2 Extracts and 2 integrated Replicats:  `STREAMS_POOL_SIZE` = 4GB \* 1.25 = 5GB  ``` ALTER SYSTEM  SET STREAMS_POOL_SIZE=5G  SCOPE=BOTH SID='*'; ``` |

Step 1.2 - Create the Database Replication Administrator User

A GoldenGate administrator user account is required in both source and target databases, where GoldenGate Extract and Replicat processes connect to.

Configure the Extract process to be a per-PDB Extract. The Extract process can be configured as a per-PDB Extract or a root CDB Extract. It is recommended that you use a per-PDB Extract, which does not require a c## common database user. A per-PDB Extract requires a local GoldenGate administrator user (for example, `ggadmin`) in the PDB it is extracting from. This can be the same GoldenGate administrator account that is used by Replicat, with additional privileges that Extract requires.

Create the GoldenGate administrator database user, and assign the appropriate privileges as detailed in [Prepare Database Users and Privileges for Oracle](https://docs.oracle.com/en/database/goldengate/core/26/coredoc/prepare-database-user-and-privileges-oracle.html#GUID-09A64B84-23C6-4EDD-ABC0-D82ED62068BA).

Step 1.3 - Create the Database Services

If the source and target databases are running the recommended configuration on an Oracle RAC cluster with Oracle Data Guard, a role-based service must be created that allows the Extract or Replicat processes to connect to the correct Data Guard primary database instance.

When using a source multitenant database with a root level Extract, separate services are required for the root container database (CDB) and the pluggable database (PDB) that contains the schema being replicated. For a target multitenant database, a single service is required for the PDB. A root container database service is not required for a per-PDB Extract.

1. As the `oracle` OS user on the primary and standby database systems, create and start the CDB database service using the following command:
	```
	[oracle@exadb1_node1 ~]$ srvctl add service -db <dbName>
	 -service <dbName>_goldengate -preferred <ORACLE_SID1> -available <ORACLE_SID2>
	 -role PRIMARY
	```
2. As the `oracle` OS user on the primary and standby database systems, create and start the PDB database service using the following command:
	```
	[oracle@exadb1_node1 ~]$ srvctl add service -db <dbName>
	 -service <dbName>_<pdbName>_goldengate -preferred <ORACLE_SID1>
	 -available <ORACLE_SID2> -pdb <pdbName> -role PRIMARY
	```
3. As the `oracle` OS user on the primary and standby database systems, start and verify that the services are running, as shown here:
	```
	[oracle@exadb1_node1 ~]$ srvctl start service -db <dbName> -role
	[oracle@exadb1_node1 ~]$ srvctl status service -db <dbName> |grep goldengate
	Service <dbName>_goldengate  is running on instance(s) <SID1>
	Service <dbName>_<pdbName>_goldengate is running on instance(s) <SID1>
	```

Note:

Repeat step 1.3 in the source and target database system.