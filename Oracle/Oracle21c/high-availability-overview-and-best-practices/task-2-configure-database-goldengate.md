---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-2-configure-database-goldengate.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 2 - Configure the Oracle Database for GoldenGate

The source and target Oracle GoldenGate databases should be configured using the following recommendations.

Perform the following steps to complete this task:

- Step 2.1 - Database Configuration
- Step 2.2 - Create the Database Replication Administrator User
- Step 2.3 - Create the Database Services

Step 2.1 - Database Configuration

The source and target Oracle GoldenGate databases should be configured using the following recommendations.

1. Enable Oracle GoldenGate replication by setting the database initialization parameter.
2. Source Oracle GoldenGate Database:
	- Run the database in `ARCHIVELOG` mode
		- Enable `FORCE LOGGING` mode
		- Enable minimal supplemental logging
		- Additionally, add schema or table level logging for all replicated objects
3. Configure the streams pool in the System Global Area (SGA) on the source database using the `STREAMS_POOL_SIZE` initialization parameter. The streams pool is only needed on the target database if integrated Replicat will be used.

For the steps on preparing the database for Oracle GoldenGate, refer to [Using Oracle GoldenGate Classic Architecture with Oracle Database](https://docs.oracle.com/en/middleware/goldengate/core/21.3/oracle-db/preparing-database-oracle-goldengate.html#GUID-E06838BD-0933-4027-8A6C-D4A17BDF4E41).

1. As the `oracle` OS user on the source and target systems, issue the following SQL instructions to configure the database:
	```
	[opc@exadb-node1 ~]$ sudo su - oracle
	[oracle@exadb-node1 ~]$ source <db_name>.env
	[oracle@exadb-node1 ~]$ sqlplus / as sysdba
	SQL> alter system set ENABLE_GOLDENGATE_REPLICATION=true scope=both sid='*';
	SQL> alter system set STREAMS_POOL_SIZE=<SIZE_IN_GB> scope=both sid='*';
	```
2. As the `oracle` OS user on the source system, issue the following SQL instructions to configure the database:
	```
	[opc@exadb-node1 ~]$ sudo su - oracle
	[oracle@exadb-node1 ~]$ source <db_name>.env
	[oracle@exadb-node1 ~]$ sqlplus / as sysdba
	SQL> ALTER DATABASE FORCE LOGGING;
	SQL> ALTER DATABASE ADD SUPPLEMENTAL LOG DATA;
	SQL> ARCHIVE LOG LIST
	Database log mode              Archive Mode
	Automatic archival             Enabled
	Archive destination            USE_DB_RECOVERY_FILE_DEST
	Oldest online log sequence     110
	Next log sequence to archive   113
	Current log sequence           113
	```

Step 2.2 - Create the Database Replication Administrator User

The source and target Oracle databases need a GoldenGate Administrator user created, with appropriate privileges assigned:

- For multitenant container database (CDB):
	- Source database, GoldenGate Extract must be configured to connect to a user in the root container database, using a `c##`
		- Target database, a separate GoldenGate administrator user is needed for each pluggable database (PDB). For details about creating a GoldenGate Administrator in an Oracle Multitenant Database, see [Configuring Oracle GoldenGate in a Multitenant Container Database](https://docs.oracle.com/en/middleware/goldengate/core/21.3/oracle-db/configuring-oracle-goldengate-multitenant-container-database-1.html#GUID-0B0CEB35-51C6-4319-BEE1-FA208FF4DE05).
- For non-CDB databases, see [Establishing Oracle GoldenGate Credentials](https://docs.oracle.com/en/middleware/goldengate/core/21.3/oracle-db/establishing-oracle-goldengate-credentials.html#GUID-E40B375A-5042-4195-B563-BE7EDC251880).
1. As the `oracle` OS user on the source system, issue the following SQL instructions to create the database user for Oracle GoldenGate and assign the required privileges:
	```
	[opc@exadb-node1 ~]$ sudo su - oracle
	[oracle@exadb-node1 ~]$ source <db_name>.env
	[oracle@exadb-node1 ~]$ sqlplus / as sysdba
	# CDB
	alter session set container=cdb$root;
	create user c##ggadmin identified by "<ggadmin_password>" container=all default
	 tablespace USERS temporary tablespace temp;
	alter user c##ggadmin quota unlimited on users;
	grant set container to c##ggadmin container=all;
	grant alter system to c##ggadmin container=all;
	grant create session to c##ggadmin container=all;
	grant alter any table to c##ggadmin container=all;
	grant resource to c##ggadmin container=all;
	exec dbms_goldengate_auth.grant_admin_privilege('c##ggadmin',container=>'all');
	# Source PDB
	alter session set container=<PDB_name>;
	create user ggadmin identified by "<ggadmin_password>" container=current;
	grant create session to ggadmin container=current;
	grant alter any table to ggadmin container=current;
	grant resource to ggadmin container=current;
	exec dbms_goldengate_auth.grant_admin_privilege('ggadmin');
	```
2. As the `oracle` OS user on the target system, issue the following SQL instructions to create the database user for Oracle GoldenGate and assign the required privileges:
	```
	# Target PDB
	[opc@exadb-node1 ~]$ sudo su - oracle
	[oracle@exadb-node1 ~]$ source <db_name>.env
	[oracle@exadb-node1 ~]$ sqlplus / as sysdba
	alter session set container=<PDB_name>;
	create user ggadmin identified by "<ggadmin_password>" container=current;
	grant alter system to ggadmin container=current;
	grant create session to ggadmin container=current;
	grant alter any table to ggadmin container=current;
	grant resource to ggadmin container=current;
	grant dv_goldengate_admin, dv_goldengate_redo_access to ggadmin container=current;
	exec dbms_goldengate_auth.grant_admin_privilege('ggadmin');
	```

Step 2.3 - Create the Database Services

A database service is required so that the Oracle Grid Infrastructure Agent will automatically start the Oracle GoldenGate deployment when the database is opened. When DBFS is used for the shared file system, the database service is also used to mount DBFS to the correct RAC instance.

When using a source multitenant database, a separate service is required for the root container database (CDB) and the pluggable database (PDB) that contains the schema being replicated. For a target multitenant database, a single service is required for the PDB.

1. As the `oracle` OS user, create and start the CDB database service using the following command:
	```
	[oracle@exadb-node1 ~]$ source <db_name>.env
	[oracle@exadb-node1 ~]$ srvctl add service -db $ORACLE_UNQNAME
	 -service \`echo $ORACLE_UNQNAME\`_ogg -preferred <SID1> -available <SID2>
	 -role PRIMARY
	[oracle@exadb-node1 ~]$ srvctl start service -db $ORACLE_UNQNAME
	 -service \`echo $ORACLE_UNQNAME\`_ogg
	```
	If your database is part of a multitenant environment, remember to create the service at the pluggable database (PDB).
2. As the `oracle` OS user, create and start the PDB database service using the following command:
	```
	[oracle@exadb-node1 ~]$ dbaascli database getDetails
	 --dbname <db_name> |grep pdbName
	      "pdbName" : "<PDB_NAME>",
	[oracle@exadb-node1 ~]$ srvctl add service -db $ORACLE_UNQNAME
	 -service <PDB_NAME>_ogg -preferred <SID1>,<SID2> -pdb <PDB_NAME> -role PRIMARY
	[oracle@exadb-node1 ~]$ srvctl start service -db $ORACLE_UNQNAME
	 -service <PDB_NAME>_ogg
	```
3. As the `oracle` OS user, verify that the services are running:
	```
	[oracle@exadb-node1 ~]$ srvctl status service -d $ORACLE_UNQNAME |grep _ogg
	Service <ORACLE_UNQNAME>_ogg is running on instance(s) <SID1>
	Service <PDB_NAME>_ogg is running on instance(s) <SID1>
	```

See [Server Control Utility Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=RACAD-GUID-3ED4DBCE-A148-462B-8A79-534A3F0D6E7D) in Oracle Real Application Clusters Administration and Deployment Guide for details about creating database services.