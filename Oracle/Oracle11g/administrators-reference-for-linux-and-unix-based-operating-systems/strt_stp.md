---
title: Stopping and Starting Oracle Software
book: "Administrator's Reference for Linux and UNIX-Based Operating Systems"
doc_id: E10839-25
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e10839/strt_stp.htm
tags:
  - oracle
  - 11g
  - administrators-reference-for-linux-and-unix-based-operating-systems
---

## 2 Stopping and Starting Oracle Software

This chapter describes how to identify Oracle Database processes, and provides basic information about how to stop and restart them. It also describes how to set up automatic startup and shutdown of the Oracle Database. It contains the following sections:

- Oracle Restart
- Stopping and Starting Oracle Processes

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) and [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm) for more information about SRVCTL commands

## 2.1 Oracle Restart

Starting with Oracle Database 11g Release 2 (11.2), the `dbstart` and `dbshut` scripts that were used to automate database startup and shutdown, are deprecated. Configure Oracle Database with the Oracle Restart feature to automatically restart the database, the listener, Oracle Automatic Storage Management (Oracle ASM), and other Oracle components after a hardware or software failure or when the database host computer restarts.

Note:

When using Oracle Restart, you can use Service Control Utility (SRVCTL), a command-line interface, to manage Oracle processes (database instance, listener, ASM instance). With SRVCTL, you can manage the Oracle Restart configuration, see the status of processes managed by Oracle Restart, and start or stop processes such as the Oracle Database. SRVCTL has been enhanced to support single instance databases with Oracle Restart on standalone servers and on clusters with Oracle Clusterware.

See Also:

[Configuring Automatic Restart of an Oracle Database](https://docs.oracle.com/cd/E11882_01/server.112/e25494/restart.htm#ADMIN12708) in Oracle Database Administrator's Guide for more information about configuring automatic restart

## 2.2 Stopping and Starting Oracle Processes

This section describes how to stop and start Oracle processes. It contains the following topics:

### 2.2.1 Stopping and Starting Oracle Database and Automatic Storage Management Instances

This section describes how to stop and start Oracle Database and Automatic Storage Management instances.

#### 2.2.1.1 Stopping an Oracle Database or Automatic Storage Management Instance

Caution:

Do not stop an Automatic Storage Management instance until you have stopped all Oracle Database instances that use that Automatic Storage Management instance to manage their storage.

To stop an Oracle Database or Automatic Storage Management instance:

#### 2.2.1.2 Restarting an Oracle Database or Automatic Storage Management Instance

Caution:

If the database instance uses Automatic Storage Management for storage management, then you must start the Automatic Storage Management instance before you start the database instance.

To restart an Oracle Database or Automatic Storage Management instance:

1. If required, repeat steps [^1] and [^2] to set the `ORACLE_SID` and `ORACLE_HOME` environment variables to identify the SID and Oracle home directory for the instance you want to start.
2. Run the following commands to start the instance:
	```
	$ sqlplus
	SQL> CONNECT SYS as SYSASM
	Enter password: sys_password
	SQL> STARTUP
	```
	After the instance starts, you can exit from SQL\*Plus.

### 2.2.2 Stopping and Starting Oracle Restart

The CRSCTL utility helps to start and stop Oracle Restart. The `srvctl` commands are no longer used to start or stop Oracle Restart.

See Also:

[About Starting and Stopping Oracle Restart](https://docs.oracle.com/cd/E11882_01/server.112/e25494/restart.htm#ADMIN13177) in Oracle Database Administrator's Guide for more information about starting and stopping Oracle Restart

### 2.2.3 Stopping and Starting Oracle Enterprise Manager Database Control

This section describes how to stop and start Oracle Enterprise Manager Database Control.

Stopping Oracle Enterprise Manager Database Control

To stop Oracle Enterprise Manager Database Control:

1. Depending on the default shell, run the `oraenv` or `coraenv` script to set the environment for the database managed by the Database Control that you want to stop:
	- `coraenv` script:
		```
		% source /usr/local/bin/coraenv
		```
		- `oraenv` script:
		```
		$ . /usr/local/bin/oraenv
		```
2. Run the following command to stop the Database Control:
	```
	$ $ORACLE_HOME/bin/emctl stop dbconsole
	```

Starting Oracle Enterprise Manager Database Control

To start Database Control:

1. Set the `ORACLE_SID` and `ORACLE_HOME` environment variables to identify the SID and Oracle home directory for the database control that you want to start:
	- Bourne, Bash, or Korn shell:
		```
		$ ORACLE_HOME=oracle_home
		$ ORACLE_SID=sid
		$ export ORACLE_HOME ORACLE_SID
		```
		- C shell:
		```
		% setenv ORACLE_HOME oracle_home
		% setenv ORACLE_SID sid
		```
2. Run the following command to start the Database Control:
	```
	$ $ORACLE_HOME/bin/emctl start dbconsole
	```

### 2.2.4 Stopping and Starting Oracle Management Agent

If you are using Oracle Enterprise Manager Grid Control to manage multiple Oracle products from a central location, then you must have an Oracle Management Agent installed on each host system. Typically, the Oracle Management Agent is installed in its own Oracle home directory.

This section describes how to stop and start Oracle Management Agent.

Stopping Oracle Management Agent

To stop Oracle Management Agent:

1. Run the following command to determine the Oracle home directory for Oracle Management Agent:
	```
	$ ps -ef | grep emagent
	```
	This command displays information about the Oracle Management Agent processes. The output of this command is similar to the following:
	```
	94248 ?? I 0:00.18 oracle_home/agent/bin/emagent ...
	```
2. If required, set the `ORACLE_HOME` environment variable to specify the appropriate Oracle home directory for the Oracle Management Agent:
	- Bourne, Bash, or Korn shell:
		```
		$ ORACLE_HOME=oracle_home
		$ export ORACLE_HOME
		```
		- C shell:
		```
		% setenv ORACLE_HOME oracle_home
		```
3. Run the following command to stop Oracle Management Agent:
	```
	$ $ORACLE_HOME/agent/bin/emctl stop agent
	```

Starting Oracle Management Agent

To start Oracle Management Agent:

1. If required, set the `ORACLE_HOME` environment variable to specify the appropriate Oracle home directory for Oracle Management Agent:
	- Bourne, Bash, or Korn shell:
		```
		$ ORACLE_HOME=oracle_home
		$ export ORACLE_HOME
		```
		- C shell:
		```
		% setenv ORACLE_HOME oracle_home
		```
2. Run the following command to start Oracle Management Agent:
	```
	$ $ORACLE_HOME/agent/bin/emctl start agent
	```

[^1]: To identify the `SID` and Oracle home directory for the instance that should be shut down, run the following command:

On Solaris:

```
$ cat /var/opt/oracle/oratab
```

On other operating systems:

```
$ cat /etc/oratab
```

The `oratab` file contains lines similar to the following, which identify the SID and corresponding Oracle home directory for each database or Automatic Storage Management instance on the system:

```
sid:oracle_home_directory:[Y|N]
```

Note:

Oracle recommends that you use the plus sign (+) as the first character in the SID of Automatic Storage Management instances.

[^2]: Depending on the default shell, run the `oraenv` or `coraenv` script to set the environment variables for the instance that should be shut down:

- Bourne, Bash, or Korn shell:
	```
	$ . /usr/local/bin/oraenv
	```
- C shell:
	```
	% source /usr/local/bin/coraenv
	```

When prompted, specify the SID for the instance.

[^undefined]: Run the following commands to shut down the instance:

```
$ sqlplus
SQL> CONNECT SYS as SYSASM
Enter password: sys_password
SQL> SHUTDOWN NORMAL
```

After the instance shuts down, you can quit SQL\*Plus.