---
title: Broker
book: Data Guard Broker
doc_id: F31839-04
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/dgbkr/examples-using-data-guard-broker-dgpdb-DGMGRL-utility.html
tags:
  - oracle
  - 21c
  - data-guard-broker
---

Use these scenarios understand how to create, manage, and monitor an Oracle Data Guard broker configuration that provides data protection and disaster recovery for one ore more pluggable databases (PDBs).

Read the information about prerequisites for getting started using the Oracle Data Guard command-line interface (DGMGRL), so that you can prepare your instances. Then read the scenarios to understand how you can use DGMGRL to create, manage, and monitor a broker configuration.

### Prerequisites for Using DG PDB

Ensure that the prerequisites for using a DG PDB environment are met.

- The source database and target database must exist.
- You must use a server parameter file. If the source database or target database uses an initialization parameter files (PFILE), convert this file into a server parameter file (SPFILE)
- If an instance was not started with a server parameter file, then you must shut down the instance and restart it using the server parameter file.
- The `DG_BROKER_START` initialization parameter must be set to `TRUE` for the source database and target database in the DG PDB configuration.

The following assumptions are made in the DG PDB scenarios:

- TCP/IP is used to connect to source database with the target database.
- The DG PDB configuration consists of the following:
	- The name of the source configuration is `MyConfig1`. The database unique name (`DB_UNIQUE_NAME`) of the source database is `boston`. The source PDB is named `sales`.
		- The name of the target configuration is `MyConfig2`. The database unique name (`DB_UNIQUE_NAME`) of the target database is `newyork`. The target PDB is named ` dgpdb_sales`.
		- The protection mode is maximum performance.
		- The transport mode is `ASYNC` mode.

### Scenario 1: Create the Source and Target Configuration

1. Create the source configuration `MyConfig1`. It must contains the source database `boston` and the PDBs `sales`, `acct`, and `finance`. The source PDB that must be protected using a DG PDB configuration is `sales`.
2. Create the target configuration `MyConfig2`. It must contain the target database `newyork`, which is used to provide data protection to the source PDB `sales` in `MyConfig1`. The source PDB is instantiated as `dgpdb_sales` in target database `newyork`.

See [Scenario 1: Creating a Configuration](examples-using-data-guard-broker-DGMGRL-utility.md) for information about creating a configuration.

### Scenario 2: Establish a Connection Between the Configurations

Establish a connection between the source configuration and the target configuration.

Run the following command, when connected to the primary database `boston` in the configuration `MyConfig1`, to establish a connection with the configuration `MyConfig2`.

```
ADD CONFIGURATION MyConfig2 CONNECT IDENTIFIER IS newyork_ci;
```

### Scenario 3: Setting Up Data Guard for the Source PDB

Identify the source PDB to be protected at the target database.

- Use the `ADD PLUGGABLE DATABASE` command to create a DGPDB for the source PDB in the target container database.
	```
	DGMGRL> ADD PLUGGABLE DATABASE 'dgpdb_sales' AT 'newyork'
	SOURCE IS 'sales' AT 'boston' 
	PDBFileNameConvert IS 'dbs/boston-sales, dbs/newyork-sales-dg';
	```

A standby PDB for source PDB `sales` is created as `dgpdb_sales` in the target database `newyork`.

See [ADD PLUGGABLE DATABASE](oracle-data-guard-broker-commands.md) for information about prerequisites and usage information for the `ADD                     PLUGGABLE DATABASE` command.

### Scenario 4: Enable the DG PDB Configuration and Start Redo Transport

Prerequisites

After you add the source PDB, and before you start recovery on the target PDB, ensure that the database files that correspond to the source PDB are copied to the target database. Use RMAN or operating system copy commands to instantiate source PDB files.

The data files that were copied can be from a point in time that is before, during, or after the creation of the target PDB provided they are from the same branch of redo that was active at the source CDB when the target PDB was created.

Note:

When copying the datafiles associated with the source PDB, the naming must follow what's specified in the `PDBFileNameConvert` clause of the `ADD PLUGGABLE DATABASE`... command.

To enable a DG PDB configuration:

- Use the `ALL` keyword with the `ENABLE                             CONFIGURATION` command.
	```
	DGMGRL> ENABLE CONFIGURATION ALL;
	Enabled “MyConfig1” with primary database “boston”.
	Enabled “MyConfig2” with primary database “newyork”.
	```
- If this is the first DGPDB being added, connect to the target database, set context to the DGPDB, and add the standby redo logs.

### Scenario 5: Switchover Source PDB to Target PDB

Use the `SWITCHOVER TO` command switch the role of the surce database and the target database in a DG PDB environment.

Prerequisites

- The state of the primary database is `TRANSPORT-ON` and that of the target PDB is `APPLY-ON`.
- The source database and target database are in good health, without any errors or warnings.
- Standby redo log files are configured on the source database.

To perform a switchover for a source PDB:

1. Check the status of the source database and the source PDB.
	The following commands displays the state, health, and properties of the source database and source PDB.
	```
	DGMGRL> SHOW DATABASE boston;
	 
	Database - boston
	  Role: PRIMARY
	  Intended State: TRANSPORT-ON
	  PDB Data Guard Role: SOURCE
	  Data Guard Source PDB(s): 1
	  Instance(s):
	    bos1
	Database Status:
	SUCCESS
	DGMGRL> SHOW PLUGGABLE DATABASE 'sales' AT boston;
	Pluggable database - SALES at boston
	  Data Guard Role: Primary
	  Con_ID: 6
	  Active Target: con_id 7 at newyork
	Pluggable Database Status:
	SUCCESS
	```
2. Check the status of the target database and target PDB.
	The following commands displays the state, health, and properties of the target database and target PDB.
	```
	DGMGRL> SHOW DATABASE newyork;
	 Database - newyork
	  Role: PRIMARY
	  Intended State: TRANSPORT-OFF
	  PDB Data Guard Role: TARGET
	  Data Guard Target PDB(s): 1
	  Instance(s):
	    ny1
	    
	Database Status:
	SUCCESS
	DGMGRL> show pluggable database dgpdb_sales at newyork ;
	Pluggable database - DGPDB_SALES at newyork
	  Data Guard Role: DataGuard Standby
	  Con_ID: 7
	  Source: con_id 6 at boston
	  Transport Lag: 0 seconds (computed 29 seconds ago)
	  Intended State: APPLY-ON
	  Apply State: Running
	  Apply Instance: ny1
	  Average Apply Rate: 23 KByte/s
	  Real Time Query: OFF
	Pluggable Database Status:
	SUCCESS
	```
3. Issue the `SWITCHOVER TO` command to switch to the target database.
	The following command switches the source PDB `sales` to its designated target PDB `dgpdb_sales`:
	```
	DGMGRL> SWITCHOVER TO PLUGGABLE DATABASE dgpdb_sales AT newyork;
	Verifying conditions for Switchover...
	  Source pluggable database is 'SALES' at database 'newyork'
	Performing switchover NOW, please wait...
	  Closing pluggable database 'SALES'...
	  Switching 'SALES' to standby role...
	  Waiting for 'DGPDB_SALES' to recover all redo data...
	  Stopping recovery at 'DGPDB_SALES'...
	  Converting 'DGPDB_SALES' to primary role...
	  Opening new primary 'DGPDB_SALES'...
	  Waiting for redo data from new primary 'DGPDB_SALES'...
	  Starting recovery at new standby 'SALES'...
	Switchover succeeded, new primary is "DGPDB_SALES"
	DGMGRL>
	```
4. Verify that the switchover was successful.
	The following command displays the DG PDB configuration with source and target databases switched. The individual PDBs show the new roles
	```
	DGMGRL> SHOW CONFIGURATION;
	Configuration – MyConfig2
	  Protection Mode: MaxPerformance
	  Members:
	  newyork  - Primary database
	     boston – Primary database at MyConfig1 configuration
	Data Guard Pluggable Database: ENABLED (Source role)
	Configuration Status:
	ENABLED
	```

### Scenario 6: Failover to Target PDB

You invoke a failover operation in an emergency situation, typically when the source PDB is unavailable or inaccessible. It reverses the roles of the source PDB and its designated target PDB.

In DG PDB environments, if the source PDB is unavailable or inaccessible but the container database and other PDBs are okay, the failover operation is very similar to a switchover operation in the sense that the original source PDB within the container database is converted and marked as a physical standby, however, recovery will not be started.

To perform a failover:

1. Run the failover command to make the target PDB the new source PDB.
	```
	DGMGRL> FAILOVER TO PLUGGABLE DATABASE 'dgpdb_sales' AT 'newyork';
	Verifying conditions for Failover...
	  Source pluggable database is 'SALES' at database 'newyork'
	Performing failover NOW, please wait...
	  Closing pluggable database 'SALES'...
	  Switching 'SALES' to standby role...
	  Waiting for 'DGPDB_SALES' to recover all redo data...
	  Stopping recovery at 'DGPDB_SALES'...
	  Converting 'DGPDB_SALES' to primary role...
	  Opening new primary 'DGPDB_SALES'...
	  Waiting for redo data from new primary 'DGPDB_SALES'...
	Failover succeeded, new primary is "DGPDB_SALES"
	DGMGRL>
	```
	Note that after the failover completes, recovery is not started on the former (failed) source PDB. It can be used as a target PDB only after it is reinstated.
	Note: After the failover completes, recovery is not started on the former (failed) source PDB; not even if the container database is restarted or an `ENABLE DATABASE` is issued at the database level.
2. Verify that the failover operation completed successfully.
	```
	DGMGRL> SHOW PLUGGABLE DATABASE 'dgpdb_sales' AT newyork;
	Pluggable database 'dgpdb_sales' at database 'newyork'
	  Data Guard Role: Primary
	  Con_ID: 7
	  Active Target: None Available
	Pluggable Database Status:
	ORA-16912: Target pluggable database may have been removed or a role change may have occurred.
	```
3. Verify that the former (failed) source PDB is not operational as an active standby.
	```
	DGMGRL> SHOW PLUGGABLE DATABASE sales AT boston;
	Pluggable database 'sales' at database 'boston'
	  Data Guard Role: DataGuard Standby
	  Con_ID: 7
	  Source: (unknown)
	Pluggable Database Status:
	ORA-16911: Redo data from new source database has not been registered.
	```
4. Make the former source PDB operational as a target PDB.
	After you address the issues that necessitated the failover, you can operationalize the former source PDB so that it functions as a target PDB for the new source PDB.
	For example, run the following command to reinstate the former source PDB `sales`:
	```
	EDIT PLUGGABLE DATABASE sales AT boston SET STATE=APPLY-ON;
	```

### Scenario 7: Monitoring a DG PDB Configuration

Use DGMGRL to monitor the status of the members in a DG PDB configuration.

Viewing Configuration Information Using DGMGRL

Use the `SHOW CONFIGURATION` command to display the current status of the DG PDB configuration. This command displays the configuration status and roles played by the primary databases in both broker configurations.

```
DGMGRL> SHOW CONFIGURATION;
Configuration – MyConfig2
  Protection Mode: MaxPerformance
  Members:
  newyork  - Primary database
    boston – Primary database at MyConfig1 configuration
Data Guard Pluggable Database: ENABLED (Target role)
Configuration Status:
ENABLED
```

Viewing Database and PDB Information Using DGMGRL

Use the `SHOW PLUGGABLE                 DATABASE` command to view the status and details of the source database or target database in a DG PDB configuration.
```
DGMGRL> SHOW DATABASE boston;
 
Database - boston

  Role: PRIMARY
  Intended State: TRANSPORT-ON
  DGPluggable State: SOURCE
  Instance(s):
    bos1
  Data Guard Source PDB(s): 1

Database Status:
SUCCESS
```

Use the `SHOW PLUGGABLE DATABASE` command to view the status of a source PDB or target PDB. Other information includes the role played by the PDB, state, transport lag, and apply lag.

```
DGMGRL> SHOW PLUGGABLE DATABASE dgpdb_sales AT newyork;
 Pluggable database - DGPDB_SALES at newyork

  Data Guard Role: DataGuard Standby
  Con_ID: 7
  Source: con_id 6 at boston
  Transport Lag: 0 seconds (computed 29 seconds ago)
  Intended State: APPLY-ON
  Apply State: Running
  Apply Instance: ny1
  Average Apply Rate: 23 KByte/s
  Real Time Query: OFF

Pluggable Database Status:
SUCCESS
```