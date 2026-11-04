---
title: Administering Database Instances and Cluster Databases
book: Real Application Clusters Administration and Deployment Guide
doc_id: E41960-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/rac.112/e41960/admin.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-administration-and-deployment-guide
---

## 3 Administering Database Instances and Cluster Databases

This chapter describes how to administer Oracle Real Application Clusters (Oracle RAC) databases and database instances.

The topics in this chapter include:

See Also:

The Oracle Enterprise Manager online help for more information about Oracle Enterprise Manager

## Tools for Administering Oracle RAC

The following sections introduce Oracle RAC administration using the three tools that you commonly use to manage Oracle RAC databases and instances: Oracle Enterprise Manager, SQL\*Plus, and the SRVCTL utility. In many cases, you use these tools the same way to manage Oracle RAC environments as you would use them manage noncluster Oracle databases:

- Overview of Oracle RAC Database Administration
- Administering Oracle RAC with Oracle Enterprise Manager
- Administering Oracle RAC with SQL\*Plus
- Administering Oracle RAC with SRVCTL

### Overview of Oracle RAC Database Administration

Prior to Oracle RAC 11g release 2 (11.2), DBAs had to hard-code parameters, such as database instance number and redo threads, to allocate specific Oracle RAC database instances to nodes within the cluster. If a node in the cluster does not start, then the database instance does not start. In Oracle RAC 11g release 2 (11.2.0.2), this method of managing your Oracle RAC database continues to be available. An Oracle RAC database managed in this manner is referred to as an [administrator-managed database](rac_glossary.md). Administrator-managed databases include pre-11g release 2 (11.2) Oracle databases and upgraded Oracle databases. You can manage these databases using the same commands or methods (such as DBCA or Oracle Enterprise Manager) you used with previous releases of Oracle Database. All commands and utilities maintain backward compatibility.

With Oracle RAC 11g release 2 (11.2), you define a database as a resource in Oracle Clusterware. The resource is automatically created when you create your database with DBCA or the resource can be manually created by adding your database with SRVCTL. This resource contains the Oracle home, the SPFILE, one or more server pools, and one or more Oracle ASM disk groups required for the database. The database resource also has a weak start dependency on the VIP, which means that the resource tries to start the VIP for the node when the database instance starts. If the VIP does not start successfully, then the instance still starts but the service does not. The database service resource depends on a running VIP.

When you review the database resource for an administrator-managed database, you see a server pool defined with the same name as the Oracle database. This server pool is part of a special Oracle-defined server pool called Generic. Oracle RAC manages the Generic server pool to support administrator-managed databases. When you add or remove an administrator-managed database using either SRVCTL or DBCA, Oracle RAC creates or removes the server pools that are members of Generic. You cannot use SRVCTL or CRSCTL commands to modify the Generic server pool.

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/crschp.htm#CWADD91277) for more information about defining resources, server pools, and resource dependencies

In Oracle RAC 11g release 2 (11.2), Oracle introduces [policy-managed database](rac_glossary.md) s to move away from any hard coding of parameters, and to help to replace nodes in a cluster or expand the cluster as requirements change. If you use policy-managed databases, then you must install the Oracle home software on every node in your cluster. Policy-managed databases must use Oracle Database 11g release 2 (11.2) and cannot coexist on the same servers as administrator-managed databases.

Note:

You cannot run more than one instance of the same database on the same node.

A policy-managed database is defined by [cardinality](rac_glossary.md), which is the number of database instances you want running during normal operations. A policy-managed database runs in one or more database server pools that are created in the cluster by a user assigned the CRS Administrator role, and it can run on different servers at different times. A database instance starts on all servers that are in the server pools defined for the database. If you are using Oracle Automatic Storage Management (Oracle ASM) with Oracle Managed Files for your database storage, then, when an instance starts and there is no redo thread available, Oracle RAC automatically enables one and creates the required redo log files and undo tablespace. Clients can connect to a policy-managed database using the same SCAN-based connect string no matter which servers they happen to be running on at the time.

See Also:

"Converting an Administrator-Managed Database to a Policy-Managed Database"

Using the Same Cluster for Administrator-Managed and Policy-Managed Databases

If you want to create an administrator-managed database on a cluster that already hosts policy-managed databases, then you must carefully select the nodes for the administrator-managed database. This is because the nodes that you select for an administrator-managed database that are in policy-managed server pools will be moved into the Generic server pool as part of this process.

If you select nodes that already run other policy-managed database instances, then DBCA prompts you with a message that lists the instances and services that will be shut down when DBCA creates the administrator-managed database. If you select the Yes button on the dialog box when DBCA asks "Do you want to continue?," then your policy-managed database instances and services will be shut down as a result of the administrator-managed database creation process.

Note:

This is also true if you use the `srvctl add instance` command, which returns a similar error message indicating that the databases would be shut down. If you also use the force option (`-f`) with the `srvctl add instance` command, then this is the same as choosing Yes on the DBCA dialog. Doing this shuts down any policy-managed databases that are running on the node before moving the node into the Generic server pool.

### Administering Oracle RAC with Oracle Enterprise Manager

Oracle Enterprise Manager provides a central point of control for the Oracle RAC environment, allowing you to perform administrative tasks simultaneously on multiple cluster databases. It has both the Database Control and Grid Control graphical user interfaces (GUIs) for managing noncluster and Oracle RAC environments. Because there is one Oracle Enterprise Manager Agent on each node of an Oracle RAC database, for Database Control you can use any URL for that database to administer it with Oracle Enterprise Manager.

In Oracle Enterprise Manager, Oracle RAC-specific administrative tasks generally focus on two levels: tasks that affect an entire [cluster database](rac_glossary.md) and tasks that affect specific instances. For example, you can use Oracle Enterprise Manager to start, stop, and monitor databases, cluster database instances, and their listeners, and to schedule jobs or set up alert thresholds for metrics. Or you can perform instance-specific commands such as setting parameters or creating resource plans. You can also use Oracle Enterprise Manager to manage schemas, security, and cluster database storage features.

See Also:

- [Oracle Database 2 Day + Real Application Clusters Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/toc.htm) for a task-oriented guide that explains how to use Oracle Enterprise Manager to perform routine Oracle RAC database administrative tasks
- "Advanced Oracle Enterprise Manager Administration" for advanced administration tasks not covered in [Oracle Database 2 Day + Real Application Clusters Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/toc.htm)

### Administering Oracle RAC with SQL\*Plus

SQL\*Plus commands operate on the current instance. The current instance can be either the local default instance on which you initiated your SQL\*Plus session, or it can be a remote instance to which you connect with Oracle Net Services.

Because, by default, the SQL\*Plus prompt does not identify the current instance, you should direct your commands to the correct instance. Starting a SQL\*Plus session and connecting to the database without specifying an instance directs all SQL\*Plus commands to the local instance. In this case, the default instance is also the current instance.

To connect to a different instance in SQL\*Plus, issue a new `CONNECT` command and specify a remote instance net service name, as shown in the following example, where `password` is the password:

```
CONNECT user_name
@net_service_name
Enter password: password
```

Connecting as `SYSOPER` or `SYSDBA` enables you to perform privileged operations, such as instance startup and shutdown. Multiple SQL\*Plus sessions can connect to the same instance at the same time. SQL\*Plus automatically disconnects you from the first instance whenever you connect to another one.

Note:

Use the `SYSASM` privilege instead of the `SYSDBA` privilege to connect to and administer an Oracle ASM instance. If you use the `SYSDBA` privilege to connect to an Oracle ASM instance, then Oracle Database writes warnings to the alert log files because commands that run using the `SYSDBA` privilege on an Oracle ASM instance are deprecated.

See the [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asminst.htm#OSTMG02600) for more information.

See Also:

- [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/cd/E11882_01/server.112/e16604/toc.htm)
- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for the proper specification of `net_service_name`
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for information about connecting to the database using `SYSDBA` or `SYSOPER` privileges

#### Changing the SQL\*Plus Prompt

To change the SQL\*Plus prompt so that it includes the name of the current instance:

```
SET SQLPROMPT '_CONNECT_IDENTIFIER> '
```

This command replaces the "SQL" string in front of the greater than symbol (>) with the user variable `_CONNECT_IDENTIFIER` that displays the current instance name for the duration of your current session.

To change the prompt for all sessions automatically, add an entry similar to the following entry in your `glogin.sql` file, found in the SQL\*Plus administrative directory:

```
SET SQLPROMPT '_CONNECT_IDENTIFIER> '
```

You may include any other required text or SQL\*Plus user variable between the single quotes in the command.

#### How SQL\*Plus Commands Affect Instances

Most SQL statements affect the current instance. You can use SQL\*Plus to start and stop instances in the Oracle RAC database. You do not need to run SQL\*Plus commands as `root` on Linux and UNIX systems or as `Administrator` on Windows systems. You need only the proper database account with the privileges that you normally use for a noncluster Oracle database. Some examples of how SQL\*Plus commands affect instances are:

- `ALTER SYSTEM CHECKPOINT LOCAL` affects only the instance to which you are currently connected, rather than the default instance or all instances.
- `ALTER SYSTEM CHECKPOINT` or `ALTER SYSTEM CHECKPOINT GLOBAL` affects all instances in the cluster database.
- `ALTER SYSTEM SWITCH LOGFILE` affects only the current instance.
	- To force a global log switch, use the `ALTER SYSTEM ARCHIVE LOG CURRENT` statement.
		- The `INSTANCE` option of `ALTER SYSTEM ARCHIVE LOG` enables you to archive each online redo log file for a specific instance.

Table 3-1 describes how SQL\*Plus commands affect instances.

Table 3-1 How SQL\*Plus Commands Affect Instances

| SQL\*Plus Command | Associated Instance |
| --- | --- |
| `ARCHIVE LOG` | Always affects the current instance. |
| `CONNECT` | Affects the default instance if no instance is specified in the `CONNECT` command. |
| `HOST` | Affects the node running the SQL\*Plus session, regardless of the location of the current and default instances. |
| `RECOVER` | Does not affect any particular instance, but rather the database. |
| `SHOW INSTANCE` | Displays information about the current instance, which can be different from the default local instance if you have redirected your commands to a remote instance. |
| `SHOW PARAMETER` and `SHOW SGA` | Displays parameter and SGA information from the current instance. |
| `STARTUP` and `SHUTDOWN` | Always affects the current instance. These are privileged SQL\*Plus commands. |

### Administering Oracle RAC with SRVCTL

Note:

if you currently set environment variables other than Oracle home and Oracle SID in your session or profile when accessing the Oracle database, then use the `srvctl setenv` command to set them for SRVCTL.

The Server Control Utility (SRVCTL) is a command-line interface that you can use to manage an Oracle RAC database from a single point. You can use SRVCTL to start and stop the database and instances, and to delete or move instances and services. You can also use SRVCTL to add services and manage configuration information, in addition to other resources in the cluster.

When you use SRVCTL to perform configuration operations on your cluster, SRVCTL stores configuration data in the Oracle Cluster Registry (OCR). SRVCTL performs other operations, such as starting and stopping instances, by configuring and managing Oracle Clusterware resources, which define agents that perform database startup and shutdown operations using Oracle Call Interface APIs.

See Also:

[Appendix A, "Server Control Utility Reference"](srvctladmin.md) for more information about SRVCTL

## Starting and Stopping Instances and Oracle RAC Databases

You can start and stop instances with Oracle Enterprise Manager, SQL\*Plus or SRVCTL as described in the following sections. Both Oracle Enterprise Manager and SRVCTL provide options to start and stop all of the instances in an Oracle RAC database with a single step.

You can only perform certain operations when the database is in a `NOMOUNT` or `MOUNT` state. Performing other operations requires that the database be `OPEN`. In addition, some operations require that only one instance be in the required state, while other operations require that all of the instances be in an identical state.

Note:

Oracle does not support running more than one instance of the same database on the same node.

The procedures in the following sections discuss starting and stopping Oracle RAC database instances:

- Overview of Starting and Stopping Oracle RAC Instances
- Starting and Stopping with Oracle Enterprise Manager
- Starting Up and Shutting Down with SQL\*Plus
- Starting Up and Shutting Down with SRVCTL

### Overview of Starting and Stopping Oracle RAC Instances

Before you can start an Oracle RAC instance, your clusterware and any required operating system-specific processes must be running. For more information about these processes, see your operating system documentation.

The procedure for shutting down Oracle RAC instances is identical to shutting down instances in noncluster Oracle databases, with the exceptions described here.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for more information about shutting down Oracle databases

- In Oracle RAC, shutting down one instance does not interfere with the operation of other running instances.
- To shut down an Oracle RAC database completely, shut down every instance that has the database open or mounted.
- After a `NORMAL` or `IMMEDIATE` shutdown, instance recovery is not required. Recovery is required, however, after you issue the `SHUTDOWN ABORT` command or after an instance terminates abnormally. An instance that is still running performs instance recovery for the instance that shut down. If no other instances are running, the next instance to open the database performs instance recovery for any instances needing it.
- The `SHUTDOWN TRANSACTIONAL` command with the `LOCAL` option is useful to shutdown an instance after all active transactions on the instance have either committed or rolled back. This is in addition to what this command does for `SHUTDOWN IMMEDIATE`. Transactions on other instances do not block this operation. If you omit the `LOCAL` option, then this operation waits until transactions on all other instances that started before the shutdown was issued either commit or rollback.

### Starting and Stopping with Oracle Enterprise Manager

See the [Oracle Database 2 Day + Real Application Clusters Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/adminrac.htm#TDPRC193) for step-by-step instructions on using Oracle Enterprise Manager to start or stop a cluster database instance or a cluster database.

### Starting Up and Shutting Down with SQL\*Plus

Note:

This section assumes you are using an SPFILE.

If you want to start or stop just one instance and you are connected to your local node, you should first ensure that your current environment includes the SID for the local instance. Note that any subsequent commands in your session, whether inside or outside a SQL\*Plus session, are associated with that same SID.

To start or shutdown your local instance, initiate a SQL\*Plus session and connect with the `SYSDBA` or `SYSOPER` privilege and then issue the required command. For example to start and mount an instance on your local node, run the following commands in your SQL\*Plus session:

```
CONNECT / AS SYSDBA 
STARTUP MOUNT
```

Note:

If you use Oracle ASM disk groups, use the `SYSASM` privilege instead of the `SYSDBA` privilege to connect to and administer the Oracle ASM instances. See the [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asminst.htm#OSTMG02600) for more information.

You can start multiple instances from a single SQL\*Plus session on one node using Oracle Net Services. Connect to each instance in turn by using a Net Services connection string, typically an instance-specific alias from your `TNSNAMES.ORA` file.

Note:

To ensure that you connect to the correct instance, you must use an alias in the connect string that is associated with just one instance. If you use an alias to a service or with multiple addresses, you may not be connected to your intended instance.

For example, you can use a SQL\*Plus session on a local node to perform a transactional shutdown for two instances on remote nodes by connecting to each in turn using the instance's individual alias name. Assume the alias name for the first instance is `db1` and that the alias for the second instance is `db2`. Connect to the first instance and shut it down as follows:

```
CONNECT /@db1 AS SYSDBA
SHUTDOWN TRANSACTIONAL
```

Then connect to and shutdown the second instance by entering the following from your SQL\*Plus session:

```
CONNECT /@db2 AS SYSDBA 
SHUTDOWN TRANSACTIONAL
```

It is not possible to start or stop multiple instances, simultaneously, with SQL\*Plus, so you cannot start or stop all of the instances for a cluster database with a single SQL\*Plus command. You may want to create a script that connects to each instance in turn and start it up and shut it down. However, you must maintain this script manually if you add or drop instances.

See Also:

[SQL\*Plus User's Guide and Reference](https://docs.oracle.com/cd/E11882_01/server.112/e16604/toc.htm) for information about other startup and shut down keywords, such as `NOMOUNT`, `MOUNT`, `IMMEDIATE`, and so on

### Starting Up and Shutting Down with SRVCTL

Note:

This section assumes that you are using an SPFILE for your database.

Enter the following SRVCTL syntax from the command line, providing the required database name and instance name, or include multiple instance names to start multiple specific instances:

To start administrator-managed databases, enter a comma-delimited list of instance names:

```
$ srvctl start instance -d db_unique_name
 -i instance_name_list
 [-o start_options
]
```

In Windows you must enclose a comma-delimited list in double quotation marks (`""`).

To start policy-managed databases, enter a single node name:

```
$ srvctl start instance -d db_unique_name
 -n node_name
 [-o start_options
]
```

Note that this command also starts all enabled and non-running services that have `AUTOMATIC` management policy, and for which the database role matches one of the service's roles.

To stop one or more instances, enter the following SRVCTL syntax from the command line:

```
$ srvctl stop instance -d db_unique_name
 [ -i "instance_name_list
" | 
  -n node_name
 ] [ -o stop_options
 ]
```

You can enter either a comma-delimited list of instance names to stop several instances or you can enter a node name to stop one instance. In Windows you must enclose a comma-delimited list in double quotation marks (`""`).

This command also stops the services related to the terminated instances on the nodes where the instances were running. As an example, the following command shuts down the two instances, `orcl3` and `orcl4`, on the `orcl` database using the `immediate` stop option:

```
$ srvctl stop instance -d orcl -i "orcl3,orcl4" -o immediate
```

To start or stop your entire cluster database, that is, all of the instances and its enabled services, enter the following SRVCTL commands:

```
$ srvctl start database -d db_unique_name [-o start_options
]
```
```
$ srvctl stop database -d db_unique_name [-o stop_options
]
```

The following SRVCTL command, for example, mounts all of the non-running instances of an Oracle RAC database:

```
$ srvctl start database -d orcl -o mount
```

See Also:

[Appendix A, "Server Control Utility Reference"](srvctladmin.md) for information about SRVCTL options and information about other administrative tasks that you can perform with SRVCTL

## Verifying That Instances are Running

To verify that instances are running, on any node from a SQL\*Plus prompt enter the following, where `password` is the password:

```
CONNECT SYS/as SYSDBA
Enter password: password
SELECT * FROM V$ACTIVE_INSTANCES;
```

This query returns output similar to the following:

```
INST_NUMBER INST_NAME    
-----------  ----------------- 
1            db1-sun:db1  
2            db2-sun:db2  
3            db3-sun:db3
```

The output columns for this example are shown in Table 3-2.

Table 3-2 Descriptions of V$ACTIVE\_INSTANCES Columns

| Column | Description |
| --- | --- |
| `INST_NUMBER` | Identifies the instance number. |
| `INST_NAME` | Identifies the host name and instance name as `host_name`:`instance_name`. |

## Terminating Sessions On a Specific Cluster Instance

You can use the `ALTER SYSTEM KILL SESSION` statement to terminate a session on a specific instance. When a session is terminated, any active transactions of the session are rolled back, and resources held by the session (such as locks and memory areas) are immediately released and available to other sessions.

Using this statement enables you to maintain strict application service-level agreements in Oracle RAC environments. Often, the goal of a service-level agreement is to execute a transaction in a specified time limit. In an Oracle RAC environment, this may require terminating a transaction on an instance and retrying the transaction on another instance within a specified time frame.

To terminate sessions, follow these steps:

1. Query the value of the `INST_ID` column in the `GV$SESSION` dynamic performance view to identify which session to terminate.
2. Issue the `ALTER SYSTEM KILL SESSION` and specify the session index number (SID) and serial number of a session that you identified with the `GV$SESSION` dynamic performance view.
	```
	KILL SESSION 'integer1, integer2[, @integer3]'
	```
	- For `integer1`, specify the value of the SID column.
		- For `integer2`, specify the value of the SERIAL# column.
		- For the optional `integer3`, specify the ID of the instance where the session to be killed exists. You can find the instance ID by querying the `GV$` tables.
	To use this statement, your instance must have the database open, and your session and the session to be terminated must be on the same instance unless you specify `integer3`.

If the session is performing some activity that must be completed, such as waiting for a reply from a remote database or rolling back a transaction, then Oracle Database waits for this activity to complete, marks the session as terminated, and then returns control to you. If the waiting lasts a minute, then Oracle Database marks the session to be terminated and returns control to you with a message that the session is marked to be terminated. The PMON background process then marks the session as terminated when the activity is complete.

The following examples provide three scenarios in which a user identifies and terminates a specific session. In each example, the SYSDBA first queries the `GV$SESSION` view for the `SCOTT` user's session to identify the session to terminate, and then runs the `ALTER SYSTEM KILL SESSION` statement to terminate the session on the instance.

See Also:

[Oracle Database 2 Day + Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10822/tdppt_realtime.htm#TDPPT367) for examples of these procedures using Oracle Enterprise Manager

Example 1 Identify and terminate the session on an busy instance

In this example, assume that the executing session is `SYSDBA` on the instance `INST_ID=1`. The `ORA-00031` message is returned because some activity must be completed before the session can be terminated.

```
SQL> SELECT SID, SERIAL#, INST_ID FROM GV$SESSION WHERE USERNAME='SCOTT';
 
       SID    SERIAL#    INST_ID
---------- ---------- ----------
        80          4          2
 
SQL> ALTER SYSTEM KILL SESSION '80, 4, @2';
alter system kill session '80, 4, @2'
*
ERROR at line 1:
ORA-00031: session marked for kill
SQL>
```

Example 2 Identify and terminate the session on an idle instance

In this example, assume that the executing session is `SYSDBA` on the instance `INST_ID=1`. The session on instance `INST_ID=2` is terminated immediately when Oracle Database executes the statement within 60 seconds.

```
SQL> SELECT SID, SERIAL#, INST_ID FROM GV$SESSION WHERE USERNAME='SCOTT';
 
       SID    SERIAL#    INST_ID
---------- ---------- ----------
        80          6          2
 
SQL> ALTER SYSTEM KILL SESSION '80, 6, @2';

System altered.

SQL>
```

Example 3 Using the IMMEDIATE parameter

The following example includes the optional `IMMEDIATE` clause to immediately terminate the session without waiting for outstanding activity to complete.

```
SQL> SELECT SID, SERIAL#, INST_ID FROM GV$SESSION WHERE USERNAME='SCOTT';
 
       SID    SERIAL#    INST_ID
---------- ---------- ----------
        80          8          2
 
SQL> ALTER SYSTEM KILL SESSION '80, 8, @2' IMMEDIATE;
 
System altered.
 
SQL>
```

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/manproc.htm#ADMIN11192) for more information about terminating sessions

## Overview of Initialization Parameter Files in Oracle RAC

When you create the database, Oracle Database creates an SPFILE in the file location that you specify. This location can be an Oracle ASM disk group, a [cluster file system](rac_glossary.md), or a shared raw device. If you manually create your database, then Oracle recommends that you create an SPFILE from an initialization parameter file (PFILE).

Note:

Oracle RAC uses a traditional PFILE only if an SPFILE does not exist or if you specify `PFILE` in your `STARTUP` command. Oracle recommends that you use an SPFILE to simplify administration, to maintain parameter setting consistency, and to guarantee parameter setting persistence across database shutdown and startup events. In addition, you can configure RMAN to back up your SPFILE.

All instances in the cluster database use the same SPFILE at startup. Because the SPFILE is a binary file, do not directly edit the SPFILE with an editor. Instead, change SPFILE parameter settings using Oracle Enterprise Manager or `ALTER SYSTEM` SQL statements.

When creating an SPFILE, if you include the `FROM MEMORY` clause (for example, `CREATE PFILE FROM MEMORY` or `CREATE SPFILE FROM MEMORY`), then the `CREATE` statement creates a PFILE or SPFILE using the current system-wide parameter settings. In an Oracle RAC environment, the created file contains the parameter settings from each instance. Because the `FROM MEMORY` clause requires all other instances to send their parameter settings to the instance that is trying to create the parameter file, the total execution time depends on the number of instances, the number of parameter settings on each instance, and the amount of data for these settings.

This section includes the following topics:

- Setting SPFILE Parameter Values for Oracle RAC
- Parameter File Search Order in Oracle RAC
- Backing Up the Server Parameter File

### Setting SPFILE Parameter Values for Oracle RAC

You can change SPFILE settings with Oracle Enterprise Manager or by using the `SET` clause of the `ALTER SYSTEM` statement.

Note:

Modifying the SPFILE using tools other than Oracle Enterprise Manager or SQL\*Plus can corrupt the file and prevent database startup. To repair the file, you might be required to create a PFILE and then regenerate the SPFILE.

The examples in this section appear in ASCII text although the SPFILE is a binary file. Assume that you start an instance with an SPFILE containing the following entries:

```
*.OPEN_CURSORS=500
prod1.OPEN_CURSORS=1000
```

The value before the period (.) in an SPFILE entry identifies the instance to which the particular parameter value belongs. When an asterisk (\*) precedes the period, the value is applied to all instances that do not have a subsequent, individual value listed in the SPFILE.

For the instance with the Oracle system identifier (SID) `prod1`, the `OPEN_CURSORS` parameter is set to `1000` even though it has a database-wide setting of `500`. Parameter file entries that have the asterisk (\*) wildcard character only affect the instances without an instance-specific entry. This gives you control over parameter settings for instance `prod1`. These two types of settings can appear in any order in the parameter file.

If another DBA runs the following statement, then Oracle Database updates the setting on all instances except the instance with SID `prod1`:

```
ALTER SYSTEM SET OPEN_CURSORS=1500 sid='*' SCOPE=MEMORY;
```

Then if you run the following statement on another instance, the instance with sid `prod1` also assumes the new setting of `2000`:

```
ALTER SYSTEM SET OPEN_CURSORS=2000 sid='*' SCOPE=MEMORY;
```

In the following example, the server parameter file contains these entries:

```
prod1.OPEN_CURSORS=1000
*.OPEN_CURSORS=500
```

Run the following statement to make Oracle Database disregard the first entry from the server parameter file:

```
ALTER SYSTEM RESET OPEN_CURSORS SCOPE=SPFILE;
```

Run the following statement to reset a parameter to its default value for instance `prod1` only:

```
ALTER SYSTEM RESET OPEN_CURSORS SCOPE=SPFILE SID='prod1';
```

### Parameter File Search Order in Oracle RAC

Oracle Database searches for your parameter file in a particular order depending on your platform.

On Linux and UNIX platforms, the search order is as follows:

1. `$ORACLE_HOME/dbs/spfile` `sid``.ora`
2. `$ORACLE_HOME/dbs/spfile.ora`
3. `$ORACLE_HOME/dbs/init` `sid``.ora`

On Windows platforms, the search order is as follows:

1. `%ORACLE_HOME%\database\spfile` `sid``.ora`
2. `%ORACLE_HOME%\database\spfile.ora`
3. `%ORACLE_HOME%\database\init` `sid``.ora`

Note:

Oracle recommends that you do not use the default SPFILE names because all instances must use the same file and they all have different SIDs. Instead, store the SPFILE on Oracle ASM. If you store the SPFILE on a cluster file system, then use the following naming convention for the SPFILE: `$ORACLE_HOME/dbs/spfile` `db_unique_name``.ora`. Create a PFILE named `$ORACLE_HOME/dbs/init` `sid``.ora` that contains the name `SPFILE=` `ORACLE_HOME` `/dbs/spfile` `db_unique_name``.ora`.

### Backing Up the Server Parameter File

Oracle recommends that you regularly back up the server parameter file for recovery purposes. Do this using Oracle Enterprise Manager (as described in the [Oracle Database 2 Day + Real Application Clusters Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/configwlm.htm#TDPRC298)) or use the `CREATE PFILE` statement. For example:

```
CREATE PFILE='?/dbs/initdbname.ora'
FROM SPFILE='/dev/vx/rdsk/oracle_dg/dbspfile'
```

You can use Recovery Manager (RMAN) to create backups of the server parameter file. You can also recover an SPFILE by starting an instance using a client-side initialization parameter file. Then re-create the server parameter file using the `CREATE SPFILE` statement. Note that if the parameter file that you use for this operation was for a single instance, then the parameter file does not contain instance-specific values, even those that must be unique in Oracle RAC instances. Therefore, ensure that your parameter file contains the appropriate settings as described earlier in this chapter.

To ensure that your SPFILE (and control files) are automatically backed up by RMAN during typical backup operations, use Oracle Enterprise Manager or the RMAN `CONTROLFILE AUTOBACKUP` statement to enable the RMAN autobackup feature

See Also:

- [Oracle Database 2 Day + Real Application Clusters Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=TDPRC0711) to perform backup jobs using Oracle Enterprise Manager
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_6.htm#SQLRF013) for more information about the `CREATE SPFILE` statement
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF90084) for more information about the `CONTROLFILE AUTOBACKUP` statement

## Initialization Parameter Use in Oracle RAC

By default, most parameters are set to a default value and this value is the same across all instances. However, many initialization parameters can also have different values on different instances as described in Table 3-3. Other parameters must either be unique or identical as described in the following sections

- Parameters That Must Have Identical Settings on All Instances
- Parameters That Have Unique Settings on All Instances
- Parameters That Should Have Identical Settings on All Instances

Table 3-3 summarizes the initialization parameters used specifically for Oracle RAC databases.

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for additional information about these and other initialization parameters

Table 3-3 Initialization Parameters Specific to Oracle RAC

| Parameter | Description |
| --- | --- |
| [`ACTIVE_INSTANCE_COUNT`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams007.htm#REFRN10001) | This initialization parameter is deprecated in Oracle RAC 11g release 2 (11.2). Instead, use a service with one preferred and one available instance. |
| [`ASM_PREFERRED_READ_FAILURE_GROUPS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams013.htm#REFRN10279) | Specifies a set of disks to be the preferred disks from which to read mirror data copies. The values you set for this parameter are instance specific and need not be the same on all instances. |
| [`CLUSTER_DATABASE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams028.htm#REFRN10015) | Enables a database to be started in cluster mode. Set this parameter to `TRUE`. |
| [`CLUSTER_DATABASE_INSTANCES`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams029.htm#REFRN10016) | Oracle RAC uses this parameter to allocate adequate memory resources. It must be set to the same value on all instances.  - For policy-managed databases, Oracle internally sets this parameter to 16 - For administrator-managed databases, Oracle internally sets it to the number of configured Oracle RAC instances  You can set this parameter to a value that is greater than the current number of instances, if you are planning to add instances. For policy-managed databases, you should set this parameter to a higher value only if you intend to run a database with more than 16 instances. In this case, set the parameter to the expected maximum number of instances on which this database will run. |
| [`CLUSTER_INTERCONNECTS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams030.htm#REFRN10017) | Specifies an alternative cluster interconnect for the private network when there are multiple interconnects. The `CLUSTER_INTERCONNECTS` initialization parameter is used only in Linux and UNIX environments where UDP IPC is enabled.  Notes:  - Oracle recommends that all Oracle databases and Oracle Clusterware use the same interconnect network. If an Oracle database runs on a separate network from Oracle Clusterware, then the timeout on error is 900s. - Oracle does not recommend setting the `CLUSTER_INTERCONNECTS` parameter except in certain situations. See "Administering Multiple Cluster Interconnects on Linux and UNIX Platforms" for more details. - This parameter is stored in the Grid Plug and Play profile in a Grid Plug and Play environment. |
| `DB_NAME` | If you set a value for `DB_NAME` in instance-specific parameter files, the setting must be identical for all instances. |
| [`DISPATCHERS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams080.htm#REFRN10049) | Set the `DISPATCHERS` parameter to enable a shared server configuration, that is a server that is configured to enable many user processes to share very few server processes. With shared server configurations, many user processes connect to a dispatcher. The `DISPATCHERS` parameter may contain many attributes.  Oracle recommends that you configure at least the `PROTOCOL` and `LISTENER` attributes. `PROTOCOL` specifies the network protocol for which the dispatcher process generates a listening end point. `LISTENER` specifies an alias name for the Oracle Net Services listeners. Set the alias to a name that is resolved through a naming method such as a `tnsnames.ora` file. The `tnsnames.ora` file contains net service names. Clients, nodes, and the Oracle Performance Manager node need this file. Oracle Enterprise Manager does not require `tnsnames.ora` entries on the client for Database Control or Grid Control.  See Also: [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for complete information about configuring the `DISPATCHERS` parameter and its attributes and for configuring the shared server |
| [`GCS_SERVER_PROCESSES`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams096.htm#REFRN10259) | This static parameter specifies the initial number of server processes for an Oracle RAC instance's Global Cache Service (GCS). The GCS processes manage the routing of interinstance traffic among Oracle RAC instances. The default number of GCS server processes is calculated based on system resources with a minimum setting of 2. For systems with one CPU, there is one GCS server process. For systems with two to eight CPUs, there are two GCS server processes. For systems with more than eight CPUs, the number of GCS server processes equals the number of CPUs divided by 4, dropping any fractions. For example, if you have 10 CPUs, then 10 divided by 4 means that your system has 2 GCS processes. You can set this parameter to different values on different instances. |
| [`INSTANCE_NAME`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams105.htm#REFRN10072) | Specifies the unique name of an instance. Clients can use this name to force their session to be connected to a specific instance in the cluster. The format of the `INSTANCE_NAME` parameter is generally `db_unique_name_instance_number`, such as `orcldb_2`.  Note: In Grid Plug and Play environments, the `INSTANCE_NAME` parameter is not required and defaults to `db_unique_name_instance_number` if not specified. |
| [`RESULT_CACHE_MAX_SIZE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams220.htm#REFRN10272) | In a clustered database, you can either set `RESULT_CACHE_MAX_SIZE=0` on every instance to disable the [result cache](rac_glossary.md), or use a nonzero value on every instance to enable the result cache. To switch between enabled and disabled result cache requires that you restart every instance:  - Enabling the result cache: Set `RESULT_CACHE_MAX_SIZE` to a value greater than `0`, or leave the parameter unset. You can size the cache differently on individual instances. - Disabling the result cache: Set `RESULT_CACHE_MAX_SIZE=0` on all instances to disable the result cache. If you set `RESULT_CACHE_MAX_SIZE=0` upon startup of any one instance, then you must set the parameter to zero on all instance startups because disabling the result cache must done clusterwide. Disabling the result cache on some instances may lead to incorrect results.  If you do not set the `RESULT_CACHE_MAX_SIZE` parameter, the parameter resolves to a default, nonzero value. |
| [`SERVICE_NAMES`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams231.htm#REFRN10194) | When you use services, Oracle recommends that you do not set a value for the `SERVICE_NAMES` parameter but instead you should create cluster managed services through the Cluster Managed Services page in Oracle Enterprise Manager Database Control. This is because Oracle Clusterware controls the setting for this parameter for the services that you create and for the default database service. The service features described in [Chapter 5, "Introduction to Automatic Workload Management"](hafeats.md) are not directly related to the features that Oracle provides when you set `SERVICE_NAMES`. In addition, setting a value for this parameter may override some benefits of using services.  Note: Entries in the `SERVICE_NAMES` parameter may be used by client connections rather than the `INSTANCE_NAME` parameter value. The `SERVICE_NAMES` parameter may include one or more names and different instances may share one or more names with other instances, enabling a client to connect to either a specific instance or to any one of a set of instances, depending on the service name chosen in the connection string. |
| [`SPFILE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams247.htm#REFRN10207) | When you use an SPFILE, all Oracle RAC database instances must use the SPFILE and the file must be on shared storage. |
| [`THREAD`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams257.htm#REFRN10216) | Specifies the number of the redo threads to be used by an instance. You can specify any available redo thread number if that thread number is enabled and is not used. If specified, this parameter must have unique values on all instances. The best practice is to use the `INSTANCE_NAME` parameter to specify redo log groups. |

### Parameters That Must Have Identical Settings on All Instances

Certain initialization parameters that are critical at database creation or that affect certain database operations must have the same value for every instance in an Oracle RAC database. Specify these parameter values in the SPFILE or in the individual PFILEs for each instance. The following list contains the parameters that must be identical on every instance:

  
[`COMPATIBLE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams035.htm#REFRN10019)  
[`CLUSTER_DATABASE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams028.htm#REFRN10015)  
[`CLUSTER_DATABASE_INSTANCES`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams029.htm#REFRN10016)  
[`CONTROL_FILES`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams037.htm#REFRN10021)  
[`DB_BLOCK_SIZE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams050.htm#REFRN10031)  
[`DB_DOMAIN`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams055.htm#REFRN10036)  
[`DB_FILES`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams058.htm#REFRN10039)  
[`DB_NAME`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams064.htm#REFRN10041)  
[`DB_RECOVERY_FILE_DEST`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams065.htm#REFRN10234)  
[`DB_RECOVERY_FILE_DEST_SIZE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams066.htm#REFRN10235)  
[`DB_UNIQUE_NAME`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams070.htm#REFRN10242)  
[`INSTANCE_TYPE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams107.htm#REFRN10244) (RDBMS or ASM)  
[`PARALLEL_EXECUTION_MESSAGE_SIZE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams182.htm#REFRN10156)  
[`REMOTE_LOGIN_PASSWORDFILE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams212.htm#REFRN10184)  
[`UNDO_MANAGEMENT`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams264.htm#REFRN10224)

The following parameters must be identical on every instance only if the parameter value is set to zero:

  
`DML_LOCKS`  
`RESULT_CACHE_MAX_SIZE`

### Parameters That Have Unique Settings on All Instances

When it is necessary to set parameters that have unique settings on a policy-managed database, you can ensure that instances always use the same name on particular nodes by running the `srvctl modify instance -n` `node_name` `-i` `instance_name` command for each server that can be assigned to the database's server pool. Then a unique value of the parameter can be specified for `instance_name` that is used whenever the database runs on `node_name`.

Specify the `ORACLE_SID` environment variable, which consists of the database name and the number of the `INSTANCE_NAME` assigned to the instance.

Use the `CLUSTER_INTERCONNECTS` initialization parameter to specify an alternative interconnect to the one Oracle Clusterware is using for the private network. Each instance of the Oracle RAC database gets a unique value when setting the `CLUSTER_INTERCONNECTS` initialization parameter.

See Also:

"Administering Multiple Cluster Interconnects on Linux and UNIX Platforms" for more information about the `CLUSTER_INTERCONNECTS` initialization parameter

Oracle Database uses the `INSTANCE_NUMBER` parameter to distinguish among instances at startup and the `INSTANCE_NAME` parameter to assign redo log groups to specific instances. The instance name can take the form `db_unique_name_instance_number` and when it has this form of name and number separated by an underscore, the number after the underscore is used as the `INSTANCE_NUMBER`. With Oracle Database 11.2 using Grid Plug and Play, you no longer have to explicitly assign instance numbers for policy-managed databases and the instance name defaults to `db_unique_name_instance_number`, where Oracle Database assigns the instance number.

When you specify `UNDO_TABLESPACE` with automatic undo management enabled, then set this parameter to a unique undo tablespace name for each instance.

If you use the `ROLLBACK_SEGMENTS` parameters, then Oracle recommends setting unique values for it by using the `SID` identifier in the SPFILE. However, you must set a unique value for `INSTANCE_NUMBER` for each instance and you cannot use a default value.

Using the `ASM_PREFERRED_READ_FAILURE_GROUPS` initialization parameter, you can specify a list of preferred read failure group names. The disks in those failure groups become the preferred read disks. Thus, every node can read from its local disks. This results in higher efficiency and performance and reduced network traffic. The setting for this parameter is instance-specific, and the values need not be the same on all instances.

### Parameters That Should Have Identical Settings on All Instances

Oracle recommends that you set the values for the parameters in Table 3-4 to the same value on all instances. Although you can have different settings for these parameters on different instances, setting each parameter to the same value on all instances simplifies administration.

Table 3-4 Parameters That Should Have Identical Settings on All Instances

| Parameter | Description |
| --- | --- |
| [`ARCHIVE_LAG_TARGET`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams009.htm#REFRN10003) | Different values for instances in your Oracle RAC database are likely to increase overhead because of additional automatic synchronization performed by the database processing.  When using Streams with your Oracle RAC database, the value should be greater than zero. |
| [`LICENSE_MAX_USERS`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams117.htm#REFRN10080) | Because this parameter determines a database-wide limit on the number of users defined in the database, it is useful to have the same value on all instances of your database so you can see the current value no matter which instance you are using. Setting different values may cause Oracle Database to generate additional warning messages during instance startup, or cause commands related to database user management to fail on some instances. |
| [`LOG_ARCHIVE_FORMAT`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams128.htm#REFRN10089) | If you do not use the same value for all your instances, then you unnecessarily complicate media recovery. The recovering instance expects the required archive log file names to have the format defined by its own value of `LOG_ARCHIVE_FORMAT`, regardless of which instance created the archive log files.  Databases that support Data Guard, either to send or receive archived redo log files, must use the same value of `LOG_ARCHIVE_FORMAT` for all instances. |
| [`SPFILE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams247.htm#REFRN10207) | If this parameter does not identify the same file to all instances, then each instance may behave differently and unpredictably in fail over, load-balancing, and during normal operations. Additionally, a change you make to the SPFILE with an `ALTER SYSTEM SET` or `ALTER SYSTEM RESET` command is saved only in the SPFILE used by the instance where you run the command. Your change is not reflected in instances using different SPFILEs.  If the SPFILE values are different in instances for which the values were set by the server, then you should restart the instances that are not using the default SPFILE. |
| [`TRACE_ENABLED`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams260.htm#REFRN10219) | If you want diagnostic trace information to be always available for your Oracle RAC database, you must set `TRACE_ENABLED` to `TRUE` on all of your database instances. If you trace on only some of your instances, then diagnostic information might not be available when required should the only accessible instances be those with `TRACE_ENABLED` set to `FALSE`. |
| [`UNDO_RETENTION`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams265.htm#REFRN10225) | By setting different values for `UNDO_RETENTION` in each instance, you are likely to reduce scalability and encounter unpredictable behavior following a failover. Therefore, you should carefully consider whether there are any benefits before you assign different values for this parameter to the instances in your Oracle RAC database. |

## Converting an Administrator-Managed Database to a Policy-Managed Database

You can convert an administrator-managed database to a policy-managed database, as follows:

1. Check the current configuration of all services and the database (if you make a mistake and need to recover, then you can know what the configuration looked like when you began), as follows:
	```
	srvctl config database -d db_unique_name
	srvctl config service -d db_unique_name
	```
2. Caution:
	By default, any named user may create a server pool. To restrict the operating system users that have this privilege, Oracle strongly recommends that you add specific users to the CRS Administrators list.
	See Also:
	[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD91105) for more information about adding users to the CRS Administrators list
	Create a server pool for the policy-managed database (you must have CRS Administrator privileges to do this), as follows:
	```
	srvctl add srvpool -g server_pool -l 0 -u n
	```
	In the preceding command, `n` is the number of servers you want in the server pool.
	Note:
	This step does not necessarily place servers in the newly-created server pool. If there are no servers in the Free pool from which the new server pool can allocate servers, for example, then you may have to use the `srvctl relocate server` command to relocate a server from another server pool.
3. Modify the database to be in the new server pool, as follows:
	```
	srvctl modify database -d db_unique_name -g server_pool
	```
4. Check the status of the database to confirm that it is now policy managed by repeating the commands in step 1.

See Also:

[Appendix A, "Server Control Utility Reference"](srvctladmin.md) for more information about these commands

Configure Oracle Enterprise Manager to recognize the change you made in the previous procedure, as follows:

1. In order for Oracle Enterprise Manager Database Control to recognize the new database instances, you must change the instance name from `db_unique_name#` to `db_unique_name_#` (notice the additional underscore (\_) before the number sign (#) character).
2. Rename the `orapwd` file in the `dbs/database` directory (or create a new `orapwd` file by running the `orapwd` command).
	By default, there is an `orapwd` file with the instance name appended to it, such as `orapwdORCL1`. You must change the name of the file to correspond to the instance name you changed in the previous step. For example, you must change `orapwdORCL1` to `orapwdORCL_1` or create a new `orapwd` file.
3. Run `emca` to reconfigure Oracle Enterprise Manager Database Control, as follows:
	```
	emca -config dbcontrol db -cluster
	```

You cannot directly convert a policy-managed database to an administrator-managed database. Instead, you can remove the policy-managed configuration using the `srvctl remove database` and `srvctl remove service` commands, and then register the same database as an administrator-managed database using the `srvctl add database` and `srvctl add instance` commands. Once you register the database and instance, you must use the `srvctl add service` command to add back the services as you removed them.

See Also:

["SRVCTL Command Reference"](srvctladmin.md) for more information about these commands

Services for administrator-managed databases continue to be defined by the `PREFERRED` and `AVAILABLE` definitions. For policy-managed databases, a service is defined to a database server pool and can either be uniform (running on all instances in the server pool) or singleton (running on only one instance in the server pool). If you change the management policy of the database, then you must recreate the database services to be either uniform/singleton or `PREFERRED` / `AVAILABLE`, depending upon which database management policy you choose.

See Also:

["Service Deployment Options"](hafeats.md) for more information about managing services

## Quiescing Oracle RAC Databases

The procedure for quiescing Oracle RAC databases is identical to quiescing a noncluster database. You use the `ALTER SYSTEM QUIESCE RESTRICTED` statement from one instance. You cannot open the database from any instance while the database is in the process of being quiesced. When all non-DBA sessions become inactive, the `ALTER SYSTEM QUIESCE RESTRICTED` statement finishes, and the database is considered as in a quiesced state. In an Oracle RAC environment, this statement affects all instances, not just the one from which the statement is issued.

To successfully issue the `ALTER SYSTEM QUIESCE RESTRICTED` statement in an Oracle RAC environment, you must have the Database Resource Manager feature activated, and it must have been activated since instance startup for all instances in the cluster database. It is through the facilities of the Database Resource Manager that non-DBA sessions are prevented from becoming active. Also, while this statement is in effect, any attempt to change the current resource plan is queued until after the system is unquiesced.

These conditions apply to Oracle RAC:

- If you issued the `ALTER SYSTEM QUIESCE RESTRICTED` statement but Oracle Database has not finished processing it, you cannot open the database.
- You cannot open the database if it is in a quiesced state.
- The `ALTER SYSTEM QUIESCE RESTRICTED` and `ALTER SYSTEM UNQUIESCE` statements affect all instances in an Oracle RAC environment, not just the instance that issues the command.

Note:

You cannot use the quiesced state to take a cold backup. This is because Oracle Database background processes may still perform updates for Oracle Database internal purposes even while the database is in quiesced state. In addition, the file headers of online data files continue to look like they are being accessed. They do not look the same as if a clean shutdown were done. You can still take online backups while the database is in a quiesced state.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/start.htm#ADMIN10263) for details on the quiesce database feature
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_2014.htm#SQLRF00902) for more information about the `ALTER SYSTEM QUIESCE RESTRICTED` syntax

## Administering Multiple Cluster Interconnects on Linux and UNIX Platforms

In Oracle RAC environments that run on Linux and UNIX platforms where UDP IPC is enabled, you can use the `CLUSTER_INTERCONNECTS` initialization parameter to specify an alternative interconnect to the one Oracle Clusterware is using for the private network.

If you set multiple values for `CLUSTER_INTERCONNECTS`, then Oracle Database uses all of the interconnects that you specify, providing load balancing if all of the listed interconnects remain operational. You must use identical values, including the order in which the interconnects are listed, on all instances of your database when defining multiple interconnects with this parameter.

Oracle does not recommend setting the `CLUSTER_INTERCONNECTS` parameter, which overrides the default interconnect settings at the operating system level. Instead, the best practice is to use operating system bonding techniques (also referred to as NIC (network interface card) bonding). See your platform-specific Oracle RAC installation guide for information about setting up NIC bonding at the operating system level.

This section includes the following topics:

- Recommendations for Setting the CLUSTER\_INTERCONNECTS Parameter
- Usage Examples for the CLUSTER\_INTERCONNECTS Parameter

### Recommendations for Setting the CLUSTER\_INTERCONNECTS Parameter

The `CLUSTER_INTERCONNECTS` initialization parameter requires an IP address. It enables you to specify multiple IP addresses, separated by colons. Oracle RAC network traffic is distributed between the specified IP addresses.

Notes:

- Oracle does not recommend setting the `CLUSTER_INTERCONNECTS` parameter when using a policy-managed database.
	If you must set the `CLUSTER_INTERCONNECTS` parameter for a policy-managed database, then Oracle recommends that you use the `srvctl modify instance -n` `node_name` `-i` `instance_name` command for all servers in the server pool.
- Oracle recommends that all databases and Oracle Clusterware use the same interconnect network.

Typically, you set the `CLUSTER_INTERCONNECTS` parameter only in the following situations:

- Due to operating system limitations, you cannot use NIC bonding to provide increased bandwidth using multiple network interfaces.
- The cluster is running multiple databases and you need the interconnect traffic to be separated.
- You have a single IP address that is made highly available by the operating system, and it does not have a stable interface name (for example, the name can change when you restart).

Do not set the `CLUSTER_INTERCONNECTS` parameter for the following common configurations:

- If you have only one cluster interconnect.
- If the default cluster interconnect meets the bandwidth requirements of your Oracle RAC database, which is typically the case.

Consider the following important points when specifying the `CLUSTER_INTERCONNECTS` initialization parameter:

- The `CLUSTER_INTERCONNECTS` initialization parameter is useful only in Linux and UNIX environments where UDP IPC is enabled.
- Specify a different value for each instance of the Oracle RAC database when setting the `CLUSTER_INTERCONNECTS` initialization parameter in the parameter file.
- The IP addresses you specify for the different instances of the same database on different nodes must belong to network adapters that connect to the same interconnect network.
- If you specify multiple IP addresses for this parameter, then list them in the same order for all instances of the same database. For example, if the parameter for the first instance on `node1` lists the IP addresses of the `alt0:`, `fta0:`, and `ics0:` devices in that order, then the parameter for the second instance on `node2` must list the IP addresses of the equivalent network adapters in the same order. See the examples in "Usage Examples for the CLUSTER\_INTERCONNECTS Parameter" for more information about setting multiple interconnects with this parameter.
- If an operating system error occurs while Oracle Database is writing to the interconnect that you specify with the `CLUSTER_INTERCONNECTS` parameter, then Oracle Database returns an error even if some other interfaces are available. This is because the communication protocols between Oracle Database and the interconnect can vary greatly depending on your platform. See your Oracle Database platform-specific documentation for more information.

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams030.htm#REFRN10017) for more information about the `CLUSTER_INTERCONNECTS` initialization parameter

### Usage Examples for the CLUSTER\_INTERCONNECTS Parameter

This section provides two examples for setting the `CLUSTER_INTERCONNECTS` parameter.

Example 1

Consider setting `CLUSTER_INTERCONNECTS` when a single cluster interconnect cannot meet your bandwidth requirements. You may need to set this parameter in data warehouse environments with high interconnect bandwidth demands from one or more databases as described here.

For example, if you have two databases with high interconnect bandwidth requirements, then you can override the default interconnect provided by your operating system and nominate a different interconnect for each database using the following syntax in each server parameter file where `ip` `n` is an IP address in standard dot-decimal format, for example: `144.25.16.214`:

```
Database One: crm1.CLUSTER_INTERCONNECTS = ip1
Database Two: ext1.CLUSTER_INTERCONNECTS = ip2
```

If you have one database with high bandwidth demands, then you can nominate multiple interconnects using the following syntax:

```
CLUSTER_INTERCONNECTS = ip1:ip2:...:ipn
```

Example 2

Use the `ifconfig` or `netstat` command to display the IP address of a device. This command provides a map between device names and IP addresses. For example, to determine the IP address of a device, run the following command as the `root` user:

```
# /usr/sbin/ifconfig -a 
fta0: flags=c63<UP,BROADCAST,NOTRAILERS,RUNNING,MULTICAST,SIMPLEX> 
      inet 192.34.137.212 netmask fffffc00 broadcast 192.34.139.255 ipmtu 1500

lo0:  flags=100c89<UP,LOOPBACK,NOARP,MULTICAST,SIMPLEX,NOCHECKSUM> 
      inet 172.0.0.1 netmask ff000000 ipmtu 4096 

ics0:  flags=1100063<UP,BROADCAST,NOTRAILERS,RUNNING,NOCHECKSUM,CLUIF> 
      inet 10.0.0.1 netmask ffffff00 broadcast 10.0.0.255 ipmtu 7000 

sl0:  flags=10<POINTOPOINT>

tun0: flags=80<NOARP>
```

In the preceding example, the interface `fta0:` has an IP address of `192.34.137.212` and the interface `ics0:` has an IP address of `10.0.0.1`.

To use the network interface whose IP address is `192.34.137.212` for all GCS, GES, and IPQ IPC traffic, set the `CLUSTER_INTERCONNECTS` parameter as follows:

```
CLUSTER_INTERCONNECTS=192.34.137.212
```

## Customizing How Oracle Clusterware Manages Oracle RAC Databases

By default, Oracle Clusterware controls database restarts in Oracle RAC environments. In some cases, you may need to minimize the level of control that Oracle Clusterware has over your Oracle RAC database, for example, during database upgrades.

Note:

When using third-party clusterware, Oracle recommends that you allow Oracle Clusterware to manage the Oracle RAC instances. If you set the instance to manual and start it with third-party clusterware, do not use the third-party clusterware to monitor and restart database instances, Oracle Clusterware must do that.

To prevent Oracle Clusterware from restarting your Oracle RAC database when you restart your system, or to avoid restarting failed instances more than once, configure a policy to define the degree of control. There are two policies: AUTOMATIC, which is the default, and MANUAL. If the policy is set to AUTOMATIC, the database is automatically restored to its previous running condition (started or stopped) upon restart of the database host computer. If MANUAL, the database is never automatically restarted upon restart of the database host computer. A MANUAL setting does not prevent Oracle Restart from monitoring the database while it is running and restarting it if a failure occurs.

Use SRVCTL commands to display and change the Oracle Clusterware policies, as shown in the following examples:

Example 1 Display the Current Policy

For example, use the following command syntax to display the current policy where `db_unique_name` is the name of the database for which you want to change policies:

```
srvctl config database -d db_unique_name -a
```

See Also:

`"srvctl config database"` for more information about the `srvctl config database` command and its options

Example 2 Change the Current Policy to Another Policy

Use the following SRVCTL command syntax to change the current policy to either AUTOMATIC or MANUAL:

```
srvctl modify database -d db_unique_name -y [AUTOMATIC | MANUAL]
```

See Also:

`"srvctl modify database"` for more information about the `srvctl modify database` command and its options

This command syntax sets the resource attribute of the database resource.

Example 3 Specify a Policy for a New Database

When you add a new database using the SRVCTL command, you can use the `-y` option to specify the management policy as either AUTOMATIC or MANUAL, as shown in the following example where `db_unique_name` is the name of the database:

```
srvctl add database -d db_unique_name -y [AUTOMATIC | MANUAL] -o $ORACLE_HOME -a DATA
```

See Also:

`"srvctl add database"` for more information about the `srvctl add database` command and its options

This command syntax places the new database under the control of Oracle Clusterware. If you do not provide a management policy option, then Oracle Database uses the default value of `automatic`. After you change the policy, the Oracle Clusterware resource records the new value for the affected database.

## Advanced Oracle Enterprise Manager Administration

You can install, configure, and monitor an Oracle RAC database from a single location using either Oracle Enterprise Manager Database Control or Oracle Enterprise Manager Grid Control.

This section provides advanced administration tasks that are not covered in [Oracle Database 2 Day + Real Application Clusters Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/toc.htm) or in ["Overview of Monitoring and Tuning Oracle RAC Databases"](monitor.md).

See Also:

[Oracle Database 2 Day + Real Application Clusters Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/toc.htm) for a task-oriented guide that explains how to use Oracle Enterprise Manager to perform routine Oracle RAC database administrative tasks

This section includes the following topics:

- Using Oracle Enterprise Manager Grid Control to Discover Nodes and Instances
- Other Oracle Enterprise Manager Capabilities
- Administering Jobs and Alerts in Oracle RAC

### Using Oracle Enterprise Manager Grid Control to Discover Nodes and Instances

Discovering Oracle RAC database and instance targets in Oracle Enterprise Manager enables monitoring and administration from the console:

- Database Control does not require discovery because DBCA performs any necessary configuration while creating the database. Database Control also monitors a single database.
- Grid Control enables you to use the Oracle Enterprise Manager console interface to discover Oracle RAC database and instance targets.
	If the Grid Control agents are installed on a cluster that has an Oracle RAC database, Oracle RAC database targets are discovered at install time. You can use the console interface to discover targets if a database is created after agents are installed or if a database is not automatically discovered at agent install time.

To discover nodes and instances, use Oracle Enterprise Manager Grid Control as follows:

1. Log in to Oracle Enterprise Manager and click the Targets tab.
2. Click the Database tab to view all of the available targets. The column labeled Types shows the Oracle RAC databases using the entry Cluster Database.
3. Add the database target by selecting the target name, then clicking Add. The Add Database Target: Specify Host page appears, which enables you to add databases, listeners, and Oracle ASM as monitored targets.
4. Click the flashlight icon to display the available host names, select a host, then click Continue. The Add Database: Specify Source page appears.
5. Either request Oracle Enterprise Manager to discover only noncluster databases and listeners, or to discover all cluster databases, noncluster databases, and listeners on the cluster, then click Continue.
6. If this procedure did not discover your reconfigured cluster database and all of its instances, you can use the Targets Discovered on Cluster page to manually configure your cluster database and noncluster databases.

### Other Oracle Enterprise Manager Capabilities

This section lists Oracle Enterprise Manager capabilities available with Oracle Enterprise Manager 11g release 2 (11.2).

- A new deployment procedure—Oracle Grid Infrastructure/Oracle RAC Provisioning—provisions Oracle RAC 11g release 2 (11.2) and Oracle Grid Infrastructure. This procedure also introduces a feature called Profiles, which enables you to record the inputs and subsequently use them for repeated deployments.
- Dynamic prerequisites for the new procedures enable Oracle Enterprise Manager, when connected to My Oracle Support (formerly OracleMetaLink), to download the latest prerequisites and tools for Oracle RAC provisioning.
- The existing One-Click Extend Cluster Database capability now supports Oracle RAC 11g release 2 (11.2) stack.
- The existing Delete/Scale down Oracle Real Application Clusters capability is certified with Oracle RAC 11g release 2 (11.2) clusters.
- The existing Oracle Database Provisioning procedure now supports provisioning of single instances of Oracle Database 11g release 2 (11.2).
- A new deployment procedure—Oracle Grid Infrastructure Provisioning for Standalone Servers—has been introduced to provision Oracle Grid Infrastructure 11g release 2 (11.2) for noncluster databases.

### Administering Jobs and Alerts in Oracle RAC

The Cluster Database Home page shows all of the instances in the Oracle RAC database and provides an aggregate collection of several Oracle RAC-specific statistics that are collected by the [Automatic Workload Repository (AWR)](rac_glossary.md) for server manageability.

You do not need to navigate to an instance-specific page to see these details. However, on the Cluster Database Home page, if an instance is down that should be operating, or if an instance has a high number of alerts, then you can drill down to the instance-specific page for each alert.

To perform specific administrative tasks as described in the remainder of this section, log in to the target Oracle RAC database, navigate to the Cluster Database Home page, and click the Administration tab.

This section includes the following topics:

- Administering Jobs in Oracle RAC
- Administering Alerts in Oracle RAC with Oracle Enterprise Manager
- Performing Scheduled Maintenance Using Defined Blackouts in Oracle Enterprise Manager

#### Administering Jobs in Oracle RAC

You can administer Oracle Enterprise Manager jobs at both the database and instance levels. For example, you can create a job at the cluster database level to run on any active instance of the target Oracle RAC database. Or you can create a job at the instance level to run on the specific instance for which you created it. In the event of a failure, recurring jobs can run on a surviving instance.

Because you can create jobs at the instance level, cluster level, or cluster database level, jobs can run on any available host in the cluster database. This applies to scheduled jobs as well. Oracle Enterprise Manager also displays job activity in several categories, including, `Active`, `History`, and `Library`.

Use the Jobs tab to submit operating system scripts and SQL scripts and to examine scheduled jobs. For example, to create a backup job for a specific Oracle RAC database:

1. Click Targets and click the database for which you want to create the job.
2. Log in to the target database.
3. When Oracle Enterprise Manager displays the Database Home page, click Maintenance.
4. Complete the Enterprise Manage Job Wizard pages to create the job.

#### Administering Alerts in Oracle RAC with Oracle Enterprise Manager

You can use Oracle Enterprise Manager to configure Oracle RAC environment alerts. You can also configure special Oracle RAC database tests, such as global cache converts, consistent read requests, and so on.

Oracle Enterprise Manager distinguishes between database- and instance-level alerts in Oracle RAC environments. Alert thresholds for instance-level alerts, such as archive log alerts, can be set at the instance target level. This function enables you to receive alerts for the specific instance if performance exceeds your threshold. You can also configure alerts at the database level, such as setting alerts for tablespaces, to avoid receiving duplicate alerts at each instance.

See Also:

Oracle Technology Network for an example of configuring alerts in Oracle RAC and the [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for information about using packages to configure thresholds

#### Performing Scheduled Maintenance Using Defined Blackouts in Oracle Enterprise Manager

You can define blackouts (which are time periods in which database monitoring is suspended so that maintenance operations do not skew monitoring data or generate needless alerts) for all managed targets of an Oracle RAC database to prevent alerts from occurring while performing maintenance. You can define blackouts for an entire cluster database or for specific cluster database instances.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/dbcontrol.htm#ADMIN13425) for more information about defining blackouts