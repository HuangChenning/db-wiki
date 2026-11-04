---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/gghub-cloud-one-region-task-1-configure-source-and-target-databases-oracle-goldengate.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 1: Configure the Source and Target Databases for Oracle GoldenGate

### Step 1.1 - Configure the Databases

For Oracle Autonomous Database (ADB-D), Oracle Database 19c (19.20) or a later release is required to support parallel integrated Replicat and conflict resolution. For Oracle Exadata Database Service (ExaDB) or BaseDB, you can use any supported Oracle Database release available in the Oracle cloud.

The database configuration steps that follow are applicable for each Database Cloud Service that supports Platinum MAA solution.

The source and target Oracle GoldenGate databases should be configured using the following recommendations:

For Oracle Autonomous Database (ADB-D), you only need to add supplemental logging:

```
PDB: ALTER PLUGGABLE DATABASE ADD SUPPLEMENTAL LOG DATA;
```

For Oracle Exadata Database Service (ExaDB) or BaseDB do the following steps:

1. Enable Archivelog Mode.
	```
	SQL> ARCHIVE LOG LIST
	Database log mode              Archive Mode
	Automatic archival             Enabled
	Archive destination            USE_DB_RECOVERY_FILE_DEST
	Oldest online log sequence     110
	Next log sequence to archive   113
	Current log sequence           113
	```
2. Enable Force Logging.
	```
	ALTER DATABASE FORCE LOGGING;
	```
3. Enable GoldenGate replication.
	```
	ALTER SYSTEM SET ENABLE_GOLDENGATE_REPLICATION=TRUE SCOPE=BOTH SID='*'
	```
4. Add supplemental logging.
	```
	ALTER DATABASE ADD SUPPLEMENTAL LOG DATA;
	```
5. Configure `STREAMS_POOL_SIZE` larger to accommodate GoldenGate.
	Use this formula to calculate the appropriate `STREAMS_POOL_SIZE` value:
	`STREAMS_POOL_SIZE = (((#Extracts + #Integrated                             Replicats) * 1GB) * 1.25)`
	For example, in a database with 2 Extracts and 2 integrated Replicats:
	`STREAMS_POOL_SIZE = 4GB * 1.25 = 5GB`
	And the parameter is set:
	```
	ALTER SYSTEM SET STREAMS_POOL_SIZE=5G SCOPE=BOTH SID='*';
	```

For the steps to prepare the database for Oracle GoldenGate, see [Preparing the Database for Oracle GoldenGate](https://docs.oracle.com/en/middleware/goldengate/core/21.3/oracle-db/preparing-database-oracle-goldengate.html#GUID-E06838BD-0933-4027-8A6C-D4A17BDF4E41).

### Step 1.2 - Create a GoldenGate Database Administrator User

For ADB-D

For ADB-D deployments, you only need to issue

```
ALTER USER ggadmin IDENTIFIED BY <password> ACCOUNT UNLOCK;
```

For Oracle Exadata Database Service (ExaDB) or BaseDB

The following steps are only applicable for Oracle Exadata Database Service (ExaDB) or BaseDB.

The source and target databases need a GoldenGate administrator user created, with appropriate privileges assigned as follows:

- For the multitenant container database (CDB):
	- Source database - GoldenGate Extract must be configured to connect to a user in the root container database, using a c##
		- Target database - a separate GoldenGate administrator user is needed for each pluggable database (PDB).
		- For details about creating a GoldenGate administrator in an Oracle Multitenant Database, see [Configuring Oracle GoldenGate in a Multitenant Container Database](https://docs.oracle.com/en/middleware/goldengate/core/21.3/oracle-db/configuring-oracle-goldengate-multitenant-container-database-1.html#GUID-0B0CEB35-51C6-4319-BEE1-FA208FF4DE05).
- For non-CDB databases, see [Establishing Oracle GoldenGate Credentials](https://docs.oracle.com/en/middleware/goldengate/core/21.3/oracle-db/establishing-oracle-goldengate-credentials.html#GUID-E40B375A-5042-4195-B563-BE7EDC251880)
1. As the `oracle` OS user on the source database system, execute the following SQL instructions to create the database user for Oracle GoldenGate and assign the required privileges:
	```
	[opc@exadb1_node1 ~]$ sudo su - oracle
	[oracle@exadb1_node1 ~]$ source dbName.env
	[oracle@exadb1_node1 ~]$ sqlplus / as sysdba
	# Source CDB
	SQL>
	alter session set container=cdb$root;
	create user c##ggadmin identified by "ggadmin_password" container=all default tablespace USERS temporary tablespace temp;
	alter user c##ggadmin quota unlimited on users;
	grant set container to c##ggadmin container=all;
	grant alter system to c##ggadmin container=all;
	grant create session to c##ggadmin container=all;
	grant alter any table to c##ggadmin container=all;
	grant resource to c##ggadmin container=all;
	exec dbms_goldengate_auth.grant_admin_privilege('c##ggadmin',container=>'all');
	# Source PDB
	SQL>
	alter session set container=pdbName;
	create user ggadmin identified by "ggadmin_password" container=current;
	grant create session to ggadmin container=current;
	grant alter any table to ggadmin container=current;
	grant resource to ggadmin container=current;
	exec dbms_goldengate_auth.grant_admin_privilege('ggadmin');
	```
2. As the `oracle` OS user on the target system, execute the following SQL instructions to create the database user for Oracle GoldenGate and assign the required privileges:
	```
	[opc@exadb2_node1 ~]$ sudo su - oracle
	[oracle@exadb2_node1 ~]$ source dbName.env
	[oracle@exadb2_node1 ~]$ sqlplus / as sysdba
	# Target PDB
	SQL>
	alter session set container=pdbName;
	create user ggadmin identified by "ggadmin_password" container=current;
	grant alter system to ggadmin container=current;
	grant create session to ggadmin container=current;
	grant alter any table to ggadmin container=current;
	grant resource to ggadmin container=current;
	grant dv_goldengate_admin, dv_goldengate_redo_access to ggadmin container=current;
	exec dbms_goldengate_auth.grant_admin_privilege('ggadmin');
	```

### Step 1.3 - Create the Database Services

Note:

This step is not required for ADB-D deployments.

If the source and target databases are running the recommended configuration on an Oracle RAC cluster with Oracle Data Guard, a role-based service must be created that allows the Extract or Replicat processes to connect to the correct Data Guard primary database instance.

When using a source multitenant database, a separate service is required for the root container database (CDB) and the pluggable database (PDB) that contains the schema being replicated. For a target multitenant database, a single service is required for the PDB.

1. As the `oracle` OS user on the primary database system, use `dbaascli` to find the CDB and PDB name, as shown here:
	```
	[opc@exadb1_node1 ~]$ sudo su - oracle
	[oracle@exadb1_node1 ~]$ source dbName.env
	[oracle@exadb1_node1 ~]$ dbaascli database getDetails
	 --dbname dbName |egrep 'dbName|pdbName'
	  "dbName" : "dbName",
	      "pdbName" : "pdbName",
	```
2. As the `oracle` OS user on the primary and standby database systems, create and start the CDB database service using the following command:
	```
	[opc@exadb1_node1 ~]$ sudo su - oracle
	[oracle@exadb1_node1 ~]$ source dbName.env
	[oracle@exadb1_node1 ~]$ srvctl add service -db $ORACLE_UNQNAME
	 -service dbName.goldengate.com -preferred ORACLE_SID1
	 -available ORACLE_SID2 -role PRIMARY
	```
3. As the `oracle` OS user on the primary and standby database systems, create and start the PDB database service using the following command:
	```
	[oracle@exadb1_node1 ~]$ srvctl add service -db $ORACLE_UNQNAME
	 -service dbName.pdbName.goldengate.com -preferred ORACLE_SID1
	 -available ORACLE_SID2 -pdb pdbName -role PRIMARY
	```
4. As the `oracle` OS user on the primary and standby database systems, start and verify that the services are running, as shown here:
	```
	[oracle@exadb1_node1 ~]$ srvctl start service -db $ORACLE_UNQNAME -role
	[oracle@exadb1_node1 ~]$ srvctl status service -d $ORACLE_UNQNAME |grep goldengate
	Service dbName.goldengate.com  is running on instance(s) SID1
	Service dbName.pdbName.goldengate.com is running on instance(s) SID1
	```

Note:

Repeat Step 1.3 in the source and target database system.