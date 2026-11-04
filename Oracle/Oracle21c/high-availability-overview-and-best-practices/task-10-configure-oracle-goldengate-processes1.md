---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-10-configure-oracle-goldengate-processes1.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 10: Configure Oracle GoldenGate Processes

In addition to the guidance provided in [Task 10: Configure Oracle GoldenGate Processes](task-10-configure-oracle-goldengate-processes.md), follow the recommendations provided below for Extract, Distribution Paths, and Replicats.

Extract Configuration on the Primary Cluster

For GoldenGate Extract processes using Data Guard configurations that are using redo transport Maximum Performance or Maximum Availability modes, the following parameter must be added to the Extract process parameter file on the primary cluster to avoid losing transactions and resulting in logical data inconsistencies:

```
TRANLOGOPTIONS HANDLEDLFAILOVER
```

This parameter prevents Extract from extracting transaction data from redo that has not yet been applied to the Data Guard standby database. This is crucial to preventing Oracle GoldenGate from replicating data to a target database that does not exist in the source standby database.

If this parameter is not specified, after a data loss failover of the source database it is possible to have data in the target database that is not present in the source database, leading to logical data inconsistencies.

By default, after 60 seconds, a warning message will be written to the Extract report file when the Extract is stalled due to not being able to query the standby database applied SCN information. For example:

`WARNING OGG-02721 Extract has been waiting for the standby database for 60                     seconds.`

The amount of time before the warning message is written to Extract report file can be adjusted using the Extract parameter `TRANLOGOPTIONS HANDLEDLFAILOVER                     STANDBY_WARNING`.

If the Extract is still not able to query the standby database applied SCN information after 30 minutes (default), the Extract process will abend, logging the following message in the Extract report file:

`ERROR OGG-02722 Extract abended waiting for 1,800 seconds for the standby                     database to be accessible or caught up with the primary database.`

If the standby database becomes available before the 30 default timeout expires, Extract continues mining data from the source database and reports the following message to the report file:

`INFO OGG-02723 Extract resumed from stalled state and started processing                     LCRs.`

The timeout value of 30 minutes can be adjusted using the Extract parameter `TRANLOGOPTIONS HANDLEDLFAILOVER STANDBY_ABEND                     value`, where value is the number of seconds the standby is unavailable before abending.

If the standby database will be unavailable for a prolonged duration, such as during a planned maintenance outage, and you wish Extract to continue extracting data from the primary database, remove the `TRANLOGOPTIONS HANDLEDLFAILOVER` parameter from the Extract parameter file and restart Extract. Remember to set the parameter after the standby becomes available.

Note:

If extracting from a primary database continues while the standby is unavailable, a data loss failover could result after the standby becomes available, and not all the primary redo was applied before a failover. The GoldenGate target database will contain data that does not exist in the source database.

See [TRANLOGOPTIONS](https://docs.oracle.com/en/database/goldengate/core/26/reference/tranlogoptions.html#GUID-B6ADFEC9-10E6-456D-9477-088513E113AF) for more information about the `TRANLOGOPTIONS HANDLEDLFAILOVER` parameters.

If the Extract process has been assigned an auto restart profile, as documented in [Task 11: Configure Autostart of Extract and Replicat Processes](task-11-configure-autostart-extract-and-replicat-processes.md), after a Data Guard role transition, the Extract process will automatically restart. Extract will continue to mine redo data from the new primary database, ignoring the current state of the new standby database, until a default 5 minute timeout period expires. After this time, if the standby is not available Extract will abend with the following errors:

`INFO OGG-25053 Timeout waiting for 300 seconds for standby database                     reinstatement. Now enforcing HANDLEDLFAILOVER.`

`ERROR OGG-06219 Unable to extract data from the Logmining server                     OGG$CAP_EXT1.`

`ERROR OGG-02078 Extract encountered a fatal error in a processing thread and                     is abending.`

Extract will continue to automatically restart, based on the Oracle GoldenGate Microservices auto restart profile, and failing due to reaching the `HANDLEDLFAILOVER` timeout, until the number retries is reached or the new standby database becomes available.

During the timeout period following a database role transition, the `HANDLEDLFAILOVER` parameter is automatically suspended, so data will be replicated to the Oracle GoldenGate replica database without consideration of the source standby database not being kept up to date. The timeout period for the standby database to start up before Extract abends can be adjusted using the Extract parameter `TRANLOGOPTIONS DLFAILOVER_TIMEOUT`.

It is recommended that you leave `DLFAILOVER_TIMEOUT` at the default of 5 minutes, to allow the old primary to convert to a standby. If the new standby database will be unavailable for an extended period of time or completely gone, then in order for Extract to start and remain running, you must remove the `HANDLEDLFAILOVER` parameter from the Extract parameter file. After removing the parameter, Extract no longer waits until redo has been applied to the standby database before extracting the data.

During the time it takes for the standby database to come back online and apply all the redo from the primary

database, there will be data divergence between it and the Oracle GoldenGate replica database. This will be resolved once the standby database is up to date. At which point, add the `HANDLEDLFAILOVER` parameter back into the integrated Extract process parameter file, and then stop and restart the Extract.

When Oracle Data Guard is configured with fast-start failover, such that the broker can automatically fail over to a standby database in the event of loss of the primary database, you must specify an additional integrated Extract parameter shown below.

`TRANLOGOPTIONS FAILOVERTARGETDESTID n`

This parameter identifies which standby database the Oracle GoldenGate Extract process must remain behind, with regards to not extracting redo data that has not yet been applied to the standby database.

To determine the correct value for `FAILOVERTARGETDESTID`, use the `LOG_ARCHIVE_DEST_N` parameter from the GoldenGate source database which is used for sending redo to the source standby database. For example, if `LOG_ARCHIVE_DEST_2` points to the standby database, then use a value of 2.

For example:

```
SQL> show parameters log_archive_dest

NAME                  TYPE     VALUE
--------------------- -------- ---------------------------------------------------
log_archive_dest_1    string   location=USE_DB_RECOVERY_FILE_DEST,
                               valid_for=(ALL_LOGFILES, ALL_ROLES)

log_archive_dest_2    string   service="ggnorths", SYNC AFFIRM delay=0
                               optional compression=disable max_failure=0 reopen=300
                               db_unique_name="GGNORTHS" net_timeout=30,
                               valid_for=(online_logfile,all_roles)
```

In this example, the Extract parameter would be set to the following:

`TRANLOGOPTIONS FAILOVERTARGETDESTID 2`

To add the parameters to the Extract parameter file, use the Oracle GoldenGate Administration Server to select display the Extract details

1. On the Administration Service tab, select the Actions menu for the Extract and choose Details.
2. In the Extract details view select the Parameters tab, and then select the pencil icon to edit the current parameter file,
3. Add the `TRANLOGOPTIONS` parameters and select Apply to save the changes.

For the new parameters to take effect, the Extract process needs to be stopped and restarted, which can be done using the Administration Server.

More information about the Extract `TRANLOGOPTIONS` parameters mentioned above, can be found in [TRANLOGOPTIONS](https://docs.oracle.com/en/database/goldengate/core/26/reference/tranlogoptions.html#GUID-B6ADFEC9-10E6-456D-9477-088513E113AF).

Distribution Path Configuration on the Primary and Standby Cluster

When the target database of an Oracle GoldenGate environment, where the Receiver Server runs, is protected with Oracle Data Guard, there is an important consideration that must be given to any Distribution Paths that are sending trail files to the Receiver Server. When the Receiver Server moves to a different cluster after an Oracle Data Guard role transition, any distribution paths must be altered to reflect the new target cluster address.

You can automatically change the distribution paths using a database role transition trigger in the target database on the Receiver Server cluster.

If the primary and standby cluster VIPs use different root CA certificates, the standby certificate will need to be added to the source deployment Service Manager, as detailed in [On-Premises: Oracle GoldenGate Microservices Architecture with Oracle Real Application Clusters Configuration Best Practices](ogg-microservices-premises1.md).

Follow the instructions below to create a database role transition trigger to modify the distribution path target address when the receiver server moves between the primary and standby cluster, during target database Data Guard role transitions.

1. Create a shell script to modify the distribution paths.
	[Example Distribution Path Target Change Script](prem-example-distribution-path-target-change-script.md) contains an example shell script that can be used to modify a distribution path target address. Refer to the example script comments for setting appropriate variable values.
	The script should be placed in the same local directory on all Oracle RAC nodes of the primary and standby database clusters. Set the script file permissions to 6751.
	For example:
	```
	$ chmod 6751 /u01/oracle/goldengate/scripts/change_path_target.sh
	```
	The example shell script uses REST API calls to access the GoldenGate distribution path. In order to make the REST API calls secure, it is recommended that you include the GoldenGate deployment administrator user name and password in a configuration file (`access.cfg`), as shown here.
	```
	$ cat /u01/oracle/goldengate/scripts/access.cfg
	user = "oggadmin:<password>"
	```
	The `access.cfg` file is also referenced in the database role transition trigger below.
2. Create a `DBMS_SCHEDULER` job.
	Creating a `DBMS_SCHEDULER` job is required to run an operating system shell script from within PL/SQL. Create the scheduler job as a SYSDBA user in the root container database (CDB).
	For example:
	```
	SQL> exec dbms_scheduler.drop_job('gg_change_path_target');
	SQL> exec dbms_scheduler.create_job(job_name=>'gg_change_path_target',
	 job_type=>'EXECUTABLE', number_of_arguments => 6,
	 job_action=>'/u01/oracle/goldengate/scripts/change_path_target.sh',
	 enabled=>FALSE);
	```
	To run an external job, you must set the `run_user` and `run_group` parameters in the `$ORACLE_HOME/rdbms/admin/externaljob.ora` file to the Oracle database operating system user and group.
	For example:
	```
	run_user = oracle
	run_group = oinstall
	```
	The `extrernaljob.ora` must be configured on all Oracle RAC nodes of the primary and standby database clusters.
3. Create the database role transition trigger.
	Create a role transition trigger on the GoldenGate target database that will fire when a standby database becomes a primary database, changing the distribution path target address, using the following example.
	```
	CREATE OR REPLACE TRIGGER gg_change_path
	AFTER db_role_change ON DATABASE
	declare
	  role varchar2(30);
	  hostname varchar2(64);
	begin
	  select database_role into role from v$database;
	  select host_name into hostname from v$instance;
	  DBMS_SCHEDULER.SET_JOB_ARGUMENT_VALUE('gg_change_path_target',1,'source_primary_cluster_VIP');
	DBMS_SCHEDULER.SET_JOB_ARGUMENT_VALUE('gg_change_path_target',2,'source_standby_cluster_VIP');
	  DBMS_SCHEDULER.SET_JOB_ARGUMENT_VALUE('gg_change_path_target',4,'dist_path_name');
	  DBMS_SCHEDULER.SET_JOB_ARGUMENT_VALUE('gg_change_path_target',5,'deployment_name');
	  DBMS_SCHEDULER.SET_JOB_ARGUMENT_VALUE('gg_change_path_target',6, '<dir/access.cfg>');
	  if role = 'PRIMARY' and hostname like 'primary_target_cluster_name%'
	  then
	    DBMS_SCHEDULER.SET_JOB_ARGUMENT_VALUE('gg_change_path_target',3,'primary_target_cluster_VIP:443');
	  elsif role = 'PRIMARY'
	  then
	    DBMS_SCHEDULER.SET_JOB_ARGUMENT_VALUE('gg_change_path_target',3,'standby_target_cluster_VIP:443');
	  end if;
	  DBMS_SCHEDULER.RUN_JOB(job_name=>'gg_change_path_target');
	end;
	/
	```
	After creating the database trigger, switch the log file on the primary database to ensure the code is propagated to the standby database using the following command:
	```
	SQL> alter system switch all logfile;
	```

Replicat Configuration on the Primary Cluster

As documented in [On-Premises: Oracle GoldenGate Microservices Architecture with Oracle Real Application Clusters Configuration Best Practices](ogg-microservices-premises1.md), a checkpoint table in the target database is required for all Oracle GoldenGate Replicat processes. There are no other configuration requirements for Replicat when configured with Oracle Data Guard.