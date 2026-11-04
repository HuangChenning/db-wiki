---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-10-configure-oracle-goldengate-processes-oggma-cloud-rac-adg.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 10 - Configure Oracle GoldenGate Processes

In addition to the advice provided in [Cloud: Oracle GoldenGate Microservices Architecture on Oracle Exadata Database Service Configuration Best Practices](ogg-microservices-cloud1.md), follow the recommendations provided below for Extract, Distribution Paths, and Replicats.

Perform the following steps to complete this task:

- Step 10.1 - Modify the Extract Configuration on the Primary System
- Step 10.2 - Modify the Distribution Path Configuration on the Primary and Standby Systems

Step 10.1 - Modify the Extract Configuration on the Primary System

For Extract processes using Data Guard configurations that are using redo transport Maximum Performance or Maximum Availability modes, the following parameter must be added to the Extract process parameter file on the primary system to avoid losing transactions and resulting in logical data inconsistencies:

```
TRANLOGOPTIONS HANDLEDLFAILOVER
```

This parameter prevents Extract from extracting transaction data from redo that has not yet been applied to the Data Guard standby database. This is crucial to preventing Oracle GoldenGate from replicating data to a target database that does not exist in the source standby database.

If this parameter is not specified, after a data loss failover of the source database it is possible to have data in the target database that is not present in the source database, leading to logical data inconsistencies.

By default, after 60 seconds, a warning message will be written to the Extract report file when the Extract is stalled due to not being able to query the standby database applied SCN information. For example:

`WARNING OGG-02721 Extract has been waiting for the standby                     database for 60 seconds.`

The amount of time before the warning message is written to Extract report file can be adjusted using the Extract parameter `TRANLOGOPTIONS                     HANDLEDLFAILOVER STANDBY_WARNING`.

If the Extract is still not able to query the standby database applied SCN information after 30 minutes (default), the Extract process will abend, logging the following message in the Extract report file:

`ERROR OGG-02722 Extract abended waiting for 1,800 seconds for                     the standby database to be accessible or caught up with the primary                     database.`

If the standby database becomes available before the default 30 timeout expires, Extract continues mining data from the source database and reports the following message to the report file:

`INFO OGG-02723 Extract resumed from stalled state and started                     processing LCRs.`

The timeout value of 30 minutes can be adjusted using the Extract parameter `TRANLOGOPTIONS HANDLEDLFAILOVER STANDBY_ABEND                     <value>`, where value is the number of seconds the standby is unavailable before abending.

If the standby database will be unavailable for a prolonged duration, such as during a planned maintenance outage, and you wish Extract to continue extracting data from the primary database, remove the `TRANLOGOPTIONS                     HANDLEDLFAILOVER` parameter from the Extract parameter file and restart Extract. Remember to set the parameter after the standby becomes available.

Note:

If extracting from a primary database continues while the standby is unavailable, a data loss failover could result after the standby becomes available, and not all the primary redo was applied before a failover. The Oracle GoldenGate target database will contain data that does not exist in the source database.

If the Extract process has been assigned an auto restart profile, as documented in [Cloud: Oracle GoldenGate Microservices Architecture on Oracle Exadata Database Service Configuration Best Practices](ogg-microservices-cloud1.md), after a Data Guard role transition, the Extract process will automatically restart. Extract will continue to mine redo data from the new primary database, ignoring the current state of the new standby database, until a default 5-minute timeout period expires. After this time, if the standby is not available Extract will abend with the following errors:

`INFO OGG-25053 Timeout waiting for 300 seconds for standby                     database reinstatement. Now enforcing HANDLEDLFAILOVER.`

`ERROR OGG-06219 Unable to extract data from the Logmining server                     OGG$CAP_XXXXX.`

`ERROR OGG-02078 Extract encountered a fatal error in a                     processing thread and is abending.`

Extract will continue to automatically restart, based on the Oracle GoldenGate Microservices auto restart profile, and failing due to reaching the `HANDLEDLFAILOVER` timeout, until the number retries is reached or the new standby database becomes available.

During the timeout period following a database role transition, the `HANDLEDLFAILOVER` parameter is automatically suspended, so data will be replicated to the Oracle GoldenGate replica database without consideration of the source standby database not being kept up to date. The timeout period for the standby database to start up before Extract abends can be adjusted using the Extract parameter `TRANLOGOPTIONS DLFAILOVER_TIMEOUT`.

It is recommended that you leave `DLFAILOVER_TIMEOUT` at the default of 5 minutes, to allow the old primary to convert to a standby. If the new standby database will be unavailable for an extended period of time or completely gone, then in order for Extract to start and remain running, you must remove the `HANDLEDLFAILOVER` parameter from the Extract parameter file. After removing the parameter, Extract no longer waits until redo has been applied to the standby database before extracting the data.

During the time it takes for the standby database to come back online and apply all the redo from the primary database, there will be data divergence between it and the Oracle GoldenGate replica database. This will be resolved once the standby database is up to date. At which point, add the `HANDLEDLFAILOVER` parameter back into the integrated Extract process parameter file, and then stop and restart the Extract.

When Oracle Data Guard Fast-Start Failover is disabled, such that the broker can automatically fail over to a standby database in the event of loss of the primary database, you must specify an additional integrated Extract parameter shown below.

`TRANLOGOPTIONS FAILOVERTARGETDESTID n`

This parameter identifies which standby database the Oracle GoldenGate Extract process must remain behind, with regards to not extracting redo data that has not yet been applied to the standby database.

If Oracle Data Guard Fast-Start Failover is disabled, and you don’t specify the additional integrated Extract parameter `FAILOVERTARGETDESTID`, the extract will abend with the following errors:

`ERROR OGG-06219 Unable to extract data from the Logmining server                     OGG$CAP_XXXXX.`

`ERROR OGG-02078 Extract encountered a fatal error in a processing                     thread and is abending.`

To determine the correct value for `FAILOVERTARGETDESTID`, use the `LOG_ARCHIVE_DEST_N` parameter from the Oracle GoldenGate source database which is used for sending redo to the source standby database. For example, if `LOG_ARCHIVE_DEST_2` points to the standby database, then use a value of 2.

As the `oracle` user on the primary system, execute the following command:

```
[opc@exapri-node1 ~]$ sudo su - oracle
[oracle@exapri-node1 ~]$ source <db_name>.env
[oracle@exapri-node1 ~]$ sqlplus / as sysdba
 
SQL> show parameters log_archive_dest
NAME                  TYPE        VALUE
--------------------- ----------- ---------------------------------------------------
log_archive_dest_1    string      location=USE_DB_RECOVERY_FILE_DEST,
                                  valid_for=(ALL_LOGFILES, ALL_ROLES)

log_archive_dest_2    string      service="<db_name>", SYNC AFFIRM delay=0
                                  optional compression=disable max_failure=0 reopen=300
                                  db_unique_name="<db_name>" net_timeout=30,
                                  valid_for=(online_logfile,all_roles)
```

In this example, the Extract parameter would be set to the following:

`TRANLOGOPTIONS FAILOVERTARGETDESTID 2`

To add the parameters to the Extract parameter file:

1. Log in into the Oracle GoldenGate Administration Server in the Source Oracle GoldenGate.
2. Click in Overview under Administration Service.
3. Click the Action button next to the Extract that you want to modify.
4. Select Details.
5. Select the Parameters tab, and then select the pencil icon to edit the current parameter file.
6. Add the `TRANLOGOPTIONS` parameters and select Apply to save the changes.

For the new parameters to take effect, the Extract process needs to be stopped and restarted, which can be done using the Administration Server.

See [Oracle GoldenGate Parameters and Functions Reference Guide](https://docs.oracle.com/en/database/goldengate/core/26/reference/tranlogoptions.html) for further information about the Extract `TRANLOGOPTIONS` parameters.

Step 10.2 - Modify the Distribution Path Configuration on the Primary and Standby Systems

When the target database of an Oracle GoldenGate environment, where the Receiver Server runs, is protected with Oracle Data Guard, there is an important consideration that must be given to any Distribution Path that are sending trail files to the Receiver Server. When the Receiver Server moves to a different system after an Oracle Data Guard role transition, any Distribution Path must be altered to reflect the new target system address.

You can automatically change the Distribution Paths using a database role transition trigger in the target database on the Receiver Server system.

If the primary and standby system VIPs use different root CA certificates, the standby certificate will need to be added to the source deployment Service Manager, as detailed in the "Step 11.3 - Distribution Path Configuration” of [Task 11 - Configure Oracle GoldenGate Processes](task-11-configure-oracle-goldengate-processes.md)

Follow the instructions below to create a database role transition trigger to modify the Distribution Path target address when the receiver server moves between the primary and standby system, during target database Data Guard role transitions.

Perform the following sub-steps to complete this step:

- Step 10.2.1 - Create a Shell Script to Modify the Distribution Paths
- Step 10.2.2 - Create a DBMS\_SCHEDULER job
- Step 10.2.3 - Create the Deployment Config File
- Step 10.2.4 - Create the Database Role Transition Trigger

Step 10.2.1 - Create a Shell Script to Modify the Distribution Paths

[Example Distribution Path Target Change Script](example-distribution-path-target-change-script-oggma-cloud-rac-adg.md) contains an example shell script that can be used to modify a distribution path target address. Refer to the example script comments for setting appropriate variable values.

Note:

The script should be placed in the same local directory on all Oracle RAC nodes of the TARGETprimary and standby database systems. Set the script file permissions to 6751.

As the `oracle` OS user on the `TARGET` primary and standby systems, follow the steps to create and distribute the script `change_path_target.sh`:

```
[opc@exadb-node1 ~]$ sudo su – oracle
[oracle@exadb-node1 ~]$ /usr/local/bin/dcli -l oracle -g ~/dbs_group mkdir
 -p /u02/app/oracle/goldengate/scripts
[oracle@exadb-node1 ~]$ vi /u02/app/oracle/goldengate/scripts/change_path_target.sh
# Paste the script from Example Distribution Path Target Change Script
[oracle@exadb-node1 ~]$ /usr/local/bin/dcli -l oracle -g ~/dbs_group
 -f /u02/app/oracle/goldengate/scripts/change_path_target.sh
 -d /u02/app/oracle/goldengate/scripts
```

Step 10.2.2 - Create a DBMS\_SCHEDULER job

Creating a `DBMS_SCHEDULER` job is required to run an operating system shell script from within PL/SQL.

1. As the `oracle` OS user on the `TARGET` primary system, create the scheduler job as a `SYSDBA` user in the root container database (CDB):
	```
	[opc@exapri-node1 ~]$ sudo su - oracle
	[oracle@exapri-node1 ~]$ source <db_name>.env
	[oracle@exapri-node1 ~]$ sqlplus / as sysdba
	SQL> exec dbms_scheduler.create_job(job_name=>'gg_change_path_target',
	 job_type=>'EXECUTABLE', number_of_arguments => 6,
	 job_action=>'/u02/app/oracle/goldengate/scripts/change_path_target.sh',
	 enabled=>FALSE);
	```
	To run an external job, you must set the `run_user` and `run_group` parameters in the `$ORACLE_HOME/rdbms/admin/externaljob.ora` file to the Oracle database operating system user and group.
2. As the `root` OS user on the `TARGET` primary and standby systems, create file `externaljob.ora`:
	```
	[opc@exadb-node1 ~]$ sudo su –
	[root@exadb-node1 ~]# export DB_NAME=<database_name>
	[root@exadb-node1 ~]# dbaascli database getDetails
	 --dbname $DB_NAME |grep homePath |uniq
	      "homePath" : "/u02/app/oracle/product/19.0.0.0/dbhome_1",
	[root@exadb-node1 ~]# vi
	 /u02/app/oracle/product/19.0.0.0/dbhome_1/rdbms/admin/externaljob.ora
	# Before
	run_user = nobody
	run_group = nobody
	# After
	run_user = oracle
	run_group = oinstall
	```
3. Repeat this step on all nodes on the primary and standby systems.
	Note:
	The `extrernaljob.ora` must be configured on all Oracle RAC nodes of the primary and standby database systems.

Step 10.2.3 - Create the Deployment Config File

The example shell script uses REST API calls to access the Oracle GoldenGate distribution path. In order to make the REST API calls secure, it is recommended that you include the user name and password in a configuration file, which is read by `curl`.

As the `oracle` OS user on the `TARGET` primary and standby systems, create the configuration file containing the deployment credentials:

```
[opc@exadb-node1 ~]$ sudo su – oracle
[oracle@exadb-node1 ~]$
cat > /u02/app/oracle/goldengate/scripts/<INSTANCE_NAME>.cfg << EOF
                user = "oggadmin:<password>"
EOF
[oracle@exadb-node1 ~]$ chmod 600 /u02/app/oracle/goldengate/scripts/<INSTANCE_NAME>.cfg
[oracle@exadb-node1 ~]$ /usr/local/bin/dcli -l oracle -g ~/dbs_group
 -f /u02/app/oracle/goldengate/scripts/<INSTANCE_NAME>.cfg
 -d /u02/app/oracle/goldengate/scripts
```

Step 10.2.4 - Create the Database Role Transition Trigger

Create a role transition trigger on the Oracle GoldenGate source database that will be fire when a standby database becomes a primary database, changing the distribution path target address.

As the `oracle` OS user on the `TARGET` primary system, execute the following SQL sentence to create the role transition trigger:

```
[opc@exapri-node1 ~]$ sudo su - oracle
[oracle@exapri-node1 ~]$ source <db_name>.env
[oracle@exapri-node1 ~]$ sqlplus / as sysdba
CREATE OR REPLACE TRIGGER gg_change_path
AFTER db_role_change ON DATABASE
declare
  role varchar2(30);
  hostname varchar2(64);
begin
  select database_role into role from v$database;
  select host_name into hostname from v$instance;
  DBMS_SCHEDULER.SET_JOB_ARGUMENT_VALUE('gg_change_path_target',1,'<PRIMARY Source VIP');
  DBMS_SCHEDULER.SET_JOB_ARGUMENT_VALUE('gg_change_path_target',2,'<STANDBY Source VIP');
  DBMS_SCHEDULER.SET_JOB_ARGUMENT_VALUE('gg_change_path_target',4,'<Distribution path name');
  DBMS_SCHEDULER.SET_JOB_ARGUMENT_VALUE('gg_change_path_target',5,'<Instance name>'
  DBMS_SCHEDULER.SET_JOB_ARGUMENT_VALUE('gg_change_path_target',6,'<Config file containing the deployment credentials>');
  if role = 'PRIMARY' and hostname like '<primary target cluster name>%'
  then
    DBMS_SCHEDULER.SET_JOB_ARGUMENT_VALUE('gg_change_path_target',3,'<PRIMARY Target VIP>:443');
  elsif role = 'PRIMARY'
  then
    DBMS_SCHEDULER.SET_JOB_ARGUMENT_VALUE('gg_change_path_target',3,'<STANDBY Target VIP>:443');
  end if;
  DBMS_SCHEDULER.RUN_JOB(job_name=>'gg_change_path_target');
end;
/
```

Step 10.3 - Replicat Configuration on the Primary System

As documented in “Step 11.4 - Replicat Configuration” of [Task 11 - Configure Oracle GoldenGate Processes](task-11-configure-oracle-goldengate-processes.md), a checkpoint table in the target database is required for all Oracle GoldenGate Replicat processes. There are no other configuration requirements for Replicat when configured with Oracle Data Guard.