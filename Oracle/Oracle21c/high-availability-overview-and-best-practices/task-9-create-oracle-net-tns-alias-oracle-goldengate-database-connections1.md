---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-9-create-oracle-net-tns-alias-oracle-goldengate-database-connections1.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 9 - Create Oracle Net TNS Alias for Oracle GoldenGate Database Connections

To provide local database connections for the Oracle GoldenGate processes when switching between Oracle RAC nodes, create a TNS alias on all of the Oracle RAC nodes where Oracle GoldenGate may be started.

Create the TNS alias in the `tnsnames.ora` file in the `TNS_ADMIN` directory specified in the deployment creation.

Perform the following steps to complete this task:

- Step 9.1 - Create the TNS Alias Definitions
- Step 9.2 - Create the Database Credentials
Step 9.1 - Create the TNS Alias Definitions

If the source database is a multitenant database, two TNS alias entries are required, one for the container database (CDB) and one for the pluggable database (PDB) that is being replicated.

For a target Multitenant database, the TNS alias connects the PDB to where replicated data is being applied. The pluggable database `SERVICE_NAME` should be set to the database service created in an earlier step (Step 2.3: Create the Database Services).

1. As the `oracle` OS user, find the database domain name:
	```
	[opc@exadb-node1]$ sudo su - oracle
	[oracle@exadb-node1]$ source DB_NAME.env
	[oracle@exadb-node1]$ sqlplus / as sysdba
	SQL> show parameter db_domain
	NAME                                 TYPE        VALUE
	------------------------------------ ----------- ------------------------------
	db_domain                            string      <db_domain_name>
	```
2. As the `oracle` OS user on the first database node, follow the steps to create the TNS alias definitions and distribute them to all database nodes:
	```
	[opc@exadb-node1 ~]$ sudo su - oracle
	[oracle@exadb-node1 ~]$ dcli -l oracle -g ~/dbs_group mkdir -p /u02/app/oracle/goldengate/network/admin
	[oracle@exadb-node1 ~]$ vi /u02/app/oracle/goldengate/network/admin/tnsnames.ora
	OGGSRV_CDB =
	    (DESCRIPTION =
	      (ADDRESS = (PROTOCOL=IPC)(KEY=LISTENER))
	      (CONNECT_DATA =
	        (SERVICE_NAME = <cdb_service_name>.<db_domain_name>)
	       )
	    )
	OGGSRV_<PDB_NAME> =
	    (DESCRIPTION =
	      (ADDRESS = (PROTOCOL=IPC)(KEY=LISTENER))
	      (CONNECT_DATA =
	        (SERVICE_NAME = <pdb_service_name>.<db_domain_name>)
	       )
	    )
	[oracle@exadb-node1 ~]$ /usr/local/bin/dcli -l oracle -g ~/dbs_group -f /u02/app/oracle/goldengate/network/admin/*.ora -d /u02/app/oracle/goldengate/network/admin
	```

Note:

When the `tnsnames.ora` or `sqlnet.ora` located in the TNS\_ADMIN directory for the Oracle GoldenGate deployment are modified; the deployment needs to be restarted to pick up the changes.

Step 9.2 - Create the Database Credentials

With the Oracle GoldenGate deployment created, use the Oracle GoldenGate Administration Service home page to create the database credentials using the above TNS alias names.

As the `oggadmin` user, create the database credentials:

1. Log in into the Administration Service: https://localhost:\<localPort>/<instance\_name>/adminsrvr
2. Click on Configuration under Administration Service.
3. Click the plus button to Add Credentials.
4. Add the required information.
	If the source database is a Multitenant Database, create database credentials for the CDB and PDB. If the target database is a Multitenant Database, create a single credential for the PDB.