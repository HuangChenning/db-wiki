---
title: STARTUP
book: "SQL*Plus User's Guide and Reference"
doc_id: E16604-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve045.htm
tags:
  - oracle
  - 11g
  - sqlplus-users-guide-and-reference
---

---

Syntax

STARTUP options | upgrade\_options

where options has the following syntax:

\[FORCE\] \[RESTRICT\] \[PFILE=filename\] \[QUIET\] \[ MOUNT \[dbname\] | \[ OPEN \[open\_options\] \[dbname\] \] | NOMOUNT \]

where open\_options has the following syntax:

READ {ONLY | WRITE \[RECOVER\]} | RECOVER

and where upgrade\_options has the following syntax:

\[PFILE=filename\] {UPGRADE | DOWNGRADE} \[QUIET\]

Starts an Oracle Database instance with several options, including mounting and opening a database.

Terms

FORCE

Shuts down the current Oracle Database instance (if it is running) with SHUTDOWN mode ABORT, before restarting it. If the current instance is running and FORCE is not specified, an error results. FORCE is useful while debugging and under abnormal circumstances. It should not normally be used.

RESTRICT

Only enables Oracle Database users with the RESTRICTED SESSION system privilege to connect to the database. Later, you can use the ALTER SYSTEM command to disable the restricted session feature.

PFILE=filename

Specifies the client parameter file to be used while starting the instance. If PFILE is not specified, the server attempts to access a default server parameter file (spfile). If the default spfile isn't found, the server then attempts to access a default pfile. The default files are platform specific. For example, the default file is $ORACLE\_HOME/dbs/init$ORACLE\_SID.ora on UNIX, and ORACLE\_HOME\\database\\initORCL.ora on Windows.

QUIET

Suppresses the display of System Global Area information for the starting instance.

MOUNT dbname

Mounts a database but does not open it.

dbname is the name of the database to mount or open. If no database name is specified, the database name is taken from the initialization parameter DB\_NAME.

OPEN

Mounts and opens the specified database.

NOMOUNT

Causes the database not to be mounted upon instance startup.

Cannot be used with MOUNT, or OPEN.

RECOVER

Specifies that media recovery should be performed, if necessary, before starting the instance. STARTUP RECOVER has the same effect as issuing the RECOVER DATABASE command and starting an instance. Only complete recovery is possible with the RECOVER option.

Recovery proceeds, if necessary, as if AUTORECOVERY is set to ON, regardless of whether or not AUTORECOVERY is enabled. If a redo log file is not found in the expected location, recovery continues as if AUTORECOVERY is disabled, by prompting you with the suggested location and name of the subsequent log files that need to be applied.

UPGRADE

Starts the database in OPEN UPGRADE mode and sets system initialization parameters to specific values required to enable database upgrade scripts to be run. UPGRADE should only be used when a database is first started with a new version of the Oracle Database Server.

See the [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm) for details about preparing for, testing and implementing a database version upgrade.

When run, upgrade scripts transform an installed version or release of an Oracle database into a later version, for example, to upgrade an Oracle9i database to Oracle Database 10g. Once the upgrade completes, the database should be shut down and restarted normally.

DOWNGRADE

Starts the database in OPEN DOWNGRADE mode and sets system initialization parameters to specific values required to enable database downgrade scripts to be run.

See the [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm) for details about preparing for, testing and implementing a database version downgrade.

When run, downgrade scripts transform an installed version or release of Oracle Database into a previous version, for example, to downgrade an Oracle10g database to an Oracle9i database. Once the downgrade completes, the database should be shut down and restarted normally.

Usage

You must be connected to a database as SYSOPER, or SYSDBA. You cannot be connected to a shared server via a dispatcher.

STARTUP with no arguments is equivalent to STARTUP OPEN.

STARTUP OPEN RECOVER mounts and opens the database even when recovery fails.

Examples

To start an instance using the standard parameter file, mount the default database, and open the database, enter

```
STARTUP
```

or enter

```
STARTUP OPEN database
```

To start an instance using the standard parameter file, mount the default database, and open the database, enter

```
STARTUP FORCE RESTRICT MOUNT
```

To start an instance using the parameter file TESTPARM without mounting the database, enter

```
STARTUP PFILE=testparm NOMOUNT
```

To shutdown a particular database, immediately restart and open it, allow access only to users with the RESTRICTED SESSION privilege, and use the parameter file MYINIT.ORA. enter

```
STARTUP FORCE RESTRICT PFILE=myinit.ora OPEN database
```

To startup an instance and mount but not open a database, enter

```
CONNECT / as SYSDBA
```

```
Connected to an idle instance.
```

```
STARTUP MOUNT
```

```
ORACLE instance started. 
 
Total System Global Area                              7629732 bytes
Fixed Size                                              60324 bytes
Variable Size                                         6627328 bytes
Database Buffers                                       409600 bytes
Redo Buffers                                           532480 bytes
```