---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-2-configure-database-goldengate-ogg-ma-cloud-rac-adg.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 2 - Configure the Oracle Database for GoldenGate

Perform the following steps to complete this task:

- Step 2.1 - Configure the Standby Database for Oracle GoldenGate
- Step 2.2 - Modify the Primary Database Service
- Step 2.3 - Create the Standby Database Service

Step 2.1 - Configure the Standby Database for Oracle GoldenGate

The standby database initialization parameters should match those of the primary database, as specified in [Cloud: Oracle GoldenGate Microservices Architecture on Oracle Exadata Database Service Configuration Best Practices](ogg-microservices-cloud1.md).

This includes the following parameters:

- `ENABLE_GOLDENGATE_REPLICATION=TRUE`
- For Oracle GoldenGate source databases, enable `FORCE LOGGING` mode and enable minimal supplemental logging.
- If an Oracle GoldenGate source database or running integrated Replicat (parallel or non-parallel), configure the `STREAMS_POOL_SIZE`.

Step 2.2 - Modify the Primary Database Service

On the primary database server, validate the existing database services that were created as part of the original Oracle GoldenGate on Oracle Exadata Database Service configuration.

By default, the service role is defined as `PRIMARY`, so that the service is only started when the database becomes the Data Guard primary database role after a role transition.

As the `oracle` OS user on the primary system, validate the service role using the following command:

```
[opc@exapri-node1 ~]$ sudo su - oracle
[oracle@exapri-node1 ~]$ source <db_name>.env
[oracle@exapri-node1 ~]$ srvctl config service -db $ORACLE_UNQNAME |
 egrep 'Service name|role|Pluggable database name'
Service name: <CDB_SERVICE_NAME>
Service role: PRIMARY
Pluggable database name:
Service name: <PDB_SERVICE_NAME>
Service role: PRIMARY
Pluggable database name: <PDB_NAME>
```

If the roles is not `PRIMARY`, modify the service using the following command:

```
[oracle@exapri-node1 ~]$ srvctl modify service -db $ORACLE_UNQNAME
 -service <service_name> -role PRIMARY
```

If your database is part of a multitenant environment, remember to modify both the multitenant container database (CDB) and pluggable database (PDB) services.

Step 2.3 - Create the Standby Database Service

On the standby Oracle Exadata Database Service, a database service is required for the standby database so that the Oracle Grid Infrastructure Agent will automatically start the Oracle GoldenGate deployment when the database is opened with the primary role.

When a source database is in a multitenant environment, a separate service is required for the root container database (CDB) and the pluggable database (PDB) that contains the schema being replicated. For a multitenant environment target database, a single service is required for the PDB.

Create the service in the standby database as it was created on the primary database. It is recommended that you use the same service name as was specified on the primary system. The service must be created as a singleton service, using the -preferred option, because the application Virtual IP address (VIP), DBFS, and Oracle GoldenGate will run on the system node where the service is running.

1. As the `oracle` OS user, get the Fully Qualified Domain Name (FQDN):
	```
	[opc@exadb-node1 ~]$ sudo su - oracle
	[oracle@exadb-node1 ~]$ hostname -f
	exadb-node1.<FQDN>
	```
2. As the oracle OS user on the standby system, create the service using the following command:
	```
	[opc@exastb-node1 ~]$ sudo su - oracle
	[oracle@exastb-node1 ~]$ source <db_name>.env
	[oracle@exastb-node1 ~]$ srvctl add service -db $ORACLE_UNQNAME
	 -service <CDB_SERVICE_NAME>.<FQDN> -preferred <SID1> -available <SID2>
	 -role PRIMARY
	[oracle@exastb-node1 ~]$ srvctl add service -db $ORACLE_UNQNAME
	 -service <PDB_SERVICE_NAME>.<FQDN> -preferred <SID1> -available <SID2>
	 -pdb <PDB name> -role PRIMARY
	```