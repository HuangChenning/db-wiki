---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/STARTUP.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
STARTUP db_options  | cdb_options | upgrade_options
```

where db options has the following syntax:

```
[FORCE] [RESTRICT] [PFILE=filename] [QUIET]  [ MOUNT [dbname] |  [ OPEN
 [open_db_options] [dbname] ] | NOMOUNT ]
```

where open\_db\_options has the following syntax:

```
READ {ONLY | WRITE [RECOVER]} | RECOVER
```

where cdb\_options has the following syntax:

```
root_connection_options | pdb_connection_options
```

where root\_connection\_options has the following syntax:

```
PLUGGABLE DATABASE pdbname  [FORCE] | [UPGRADE] | [RESTRICT] [ OPEN
 {open_pdb_options}]
```

where pdb\_connection\_options has the following syntax:

```
[FORCE] | [UPGRADE] | [RESTRICT] [ OPEN
 {open_pdb_options}]
```

where open\_pdb\_options has the following syntax:

```
READ WRITE
 | READ ONLY
```

and where upgrade\_options has the following syntax:

```
[PFILE=filename] {UPGRADE | DOWNGRADE} [QUIET]
```

Starts an Oracle Database instance with several options, including mounting and opening a database.

Prerequisites for a PDB STARTUP

When the current container is a pluggable database (PDB), the STARTUP command can only be used if:

- The current user has SYSDBA, SYSOPER, SYSBACKUP, or SYSDG system privilege.
- The privilege is either commonly granted or locally granted in the PDB.
- The current user exercises the privilege using AS SYSDBA, AS SYSOPER, SYSBACKUP, or AS SYSDG at connect time.
- The PDB is in MOUNTED mode, excluding the use of the FORCE option.
- The PDB must be in READ ONLY or READ WRITE mode to be in mounted mode.

For more information, see the [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=ADMIN14098)

Note:

Only use db\_options to start a Database.

Only use root\_connection\_options to start a Pluggable Database while connected to the Root.

Only use pdb\_options to start a Pluggable Database to which you are connected.

Only use upgrade\_options to start a Database for upgrade or downgrade.

If neither `READ WRITE` nor `READ ONLY` is specified, a PDB will be opened in `READ ONLY` if a CDB to which it belongs is used as a physical standby database, otherwise the PDB will be opened `READ WRITE`.

For more information about using Consolidated and Pluggable Databases, see [Creating and Configuring an Oracle Database](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=ADMIN-GUID-807DE711-C82C-4BB2-8C31-5EE89CA71349).

Terms

```
FORCE
```

Shuts down the current Oracle Database instance (if it is running) with SHUTDOWN mode ABORT, before restarting it. If the current instance is running and FORCE is not specified, an error results. FORCE is useful while debugging and under abnormal circumstances. It should not normally be used.

```
RESTRICT
```

Only enables Oracle Database users with the RESTRICTED SESSION system privilege to connect to the database. Later, you can use the ALTER SYSTEM command to disable the restricted session feature.

```
PFILE=filename
```

Specifies the client parameter file to be used while starting the instance. If PFILE is not specified, the server attempts to access a default server parameter file (spfile). If the default spfile isn't found, the server then attempts to access a default pfile. The default files are platform specific. For example, the default file is $ORACLE\_HOME/dbs/init$ORACLE\_SID.ora on UNIX, and ORACLE\_HOME\\database\\initORCL.ora on Windows.

```
QUIET
```

Suppresses the display of System Global Area information for the starting instance.

```
MOUNT dbname
```

Mounts a database but does not open it.

dbname is the name of the database to mount or open. If no database name is specified, the database name is taken from the initialization parameter DB\_NAME.

```
OPEN
```

Mounts and opens the specified database.

```
NOMOUNT
```

Causes the database not to be mounted upon instance startup.

Cannot be used with MOUNT, or OPEN.

```
RECOVER
```

Specifies that media recovery should be performed, if necessary, before starting the instance. STARTUP RECOVER has the same effect as issuing the RECOVER DATABASE command and starting an instance. Only complete recovery is possible with the RECOVER option.

Recovery proceeds, if necessary, as if AUTORECOVERY is set to ON, regardless of whether or not AUTORECOVERY is enabled. If a redo log file is not found in the expected location, recovery continues as if AUTORECOVERY is disabled, by prompting you with the suggested location and name of the subsequent log files that need to be applied.

```
UPGRADE
```

Starts the database in OPEN UPGRADE mode and sets system initialization parameters to specific values required to enable database upgrade scripts to be run. UPGRADE should only be used when a database is first started with a new version of the Oracle Database Server.

When run, upgrade scripts transform an installed version or release of an Oracle database into a later version, for example, to upgrade an Oracle9i database to Oracle Database 10g. Once the upgrade completes, the database should be shut down and restarted normally.

```
DOWNGRADE
```

Starts the database in OPEN DOWNGRADE mode and sets system initialization parameters to specific values required to enable database downgrade scripts to be run.

When run, downgrade scripts transform an installed version or release of Oracle Database into a previous version, for example, to downgrade an Oracle10g database to an Oracle9i database. Once the downgrade completes, the database should be shut down and restarted normally.

```
PLUGGABLE DATABASE
```

Use the pluggable database pdbname option to specify the plugggable database on which you want the STARTUP command to act.

Usage

You must be connected to a database as SYSDBA, SYSOPER, SYSBACKUP, or SYSDG. You cannot be connected to a shared server via a dispatcher.

STARTUP with no arguments is equivalent to STARTUP OPEN.

STARTUP OPEN RECOVER mounts and opens the database even when recovery fails.

Examples

To start a CDB instance using the standard parameter file, mount the default database, and open the database, enter

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

To startup a PDB from a PDB container, enter the following sequence

```
CONNECT SYS/<password>@CDB1_PDB1 AS SYSDBA
```
```
Connected.
```
```
SHOW CON_NAME
```
```
CON_NAME
------------------------------
CDB1_PDB1
```
```
SHOW PDBS
```
```
CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         3 CDB1_PDB1                      MOUNTED
```
```
STARTUP
```
```
Pluggable Database opened.
```
```
SHOW PDBS
```
```
CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         3 CDB1_PDB1                      READ WRITE NO
```

To startup a PDB from root, enter the following sequence

```
CONNECT / AS SYSDBA
```
```
Connected.
```
```
SHOW CON_NAME
```
```
CON_NAME
------------------------------
CDB$ROOT
```
```
SHOW PDBS
```
```
CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
          2 PDB$SEED                       READ ONLY  NO
          3 CDB1_PDB1                      MOUNTED
```
```
STARTUP PLUGGABLE DATABASE CDB1_PDB1
```
```
Pluggable Database opened.
```
```
SHOW PDBS
```
```
CON_ID CON_NAME     OPEN MODE  RESTRICTED
---------- ------------- ---------- ----------
          2 PDB$SEED     READ ONLY  NO
          3 CDB1_PDB1    READ WRITE NO
```