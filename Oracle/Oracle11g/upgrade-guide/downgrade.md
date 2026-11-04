---
title: Downgrading Oracle Database to an Earlier Release
book: Upgrade Guide
doc_id: E23633-11
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e23633/downgrade.htm
tags:
  - oracle
  - 11g
  - upgrade-guide
---

## 6 Downgrading Oracle Database to an Earlier Release

Oracle Database can only be downgraded to the release from which you upgraded. For example, if you upgrade from Oracle Database 10g Release 1 (10.1.0.5) to Oracle Database 11g Release 2 (11.2), then you cannot subsequently downgrade to Oracle Database 10g Release 2 (10.2); you can only downgrade to Oracle Database 10g Release 1 (10.1.0.5).

This chapter contains the following topics:

See Also:

[Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for your operating system for discussions of downgrading that are operating system-specific

## Supported Releases for Downgrading Oracle Database

You can downgrade both major releases and patchset releases, based on the original release from which the database was upgraded. Major release downgrades are supported back to Oracle Database 11g Release 1 (11.1.0.6), Oracle Database 10g Release 2 (10.2.0.2), and Oracle Database 10g Release 1 (10.1.0.5). Patchset downgrades are supported back to all prior 11.2 patch releases.

Note:

You cannot downgrade a database that was upgraded from Oracle Database Express Edition.

If you have Oracle Database Vault installed with your Oracle Database 11g Release 2 (11.2) database, then you can downgrade to release 11.1.0.6 and release 11.1.0.7 only.

If you have Messaging Gateway or Workspace Manager in your database, then be aware that neither of them are part of Oracle Database patchsets earlier than release 10.2.0.4. Therefore, you must separately apply all relevant patches to the release 10.2.0.3 or release 10.1.0.5 Oracle home before downgrading.

Downgrade is not supported for Oracle Enterprise Manager. However, if you save your Oracle Enterprise Manager Database Control files and data before upgrading your database, then you can restore the old version of Database Control after downgrading the database.

Note:

You must use Oracle Data Pump full database export with the `INCLUDE=DBLINK` parameter to export all database links into a dump file suitable for import into the downgraded database. This dump file can then be used to replace the database links after the downgrade.

## Check for Incompatibilities Between Oracle Database Releases

Check the compatibility level of your release of Oracle Database to see if the database might have incompatibilities that prevent you from downgrading. If the compatibility level of your Oracle Database 11g Release 2 (11.2) database is `11.2.0` or higher, then you cannot downgrade.

See Also:

["Checking the Compatibility Level of Oracle Database"](intro.md)

If you are downgrading to Oracle Database 11g Release 1 (11.1), then the `COMPATIBLE` initialization parameter must be set to `11.0.0` or lower.

If you are downgrading to Oracle Database 10g Release 2 (10.2), then the `COMPATIBLE` initialization parameter must be set to `10.2.0` or lower.

If you are downgrading to Oracle Database 10g Release 1 (10.1), then the `COMPATIBLE` initialization parameter must be set to `10.1.0`.

## Remove Unsupported Parameters from Server Parameter File (SPFILE)

If the database uses an SPFILE, new parameters may have been added during installation or upgrade that are not supported in the earlier release to which you want to downgrade. After the downgrade, the new parameters may prevent the database from starting. Therefore, you must remove the parameters from the SPFILE that are not supported by the earlier release. You can change SPFILE settings by using the `SET` clause of the `ALTER SYSTEM` statement as described in [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/admin.htm#RACAD815).

To find information about new parameters for the current release from which you are downgrading, see the [Oracle Database New Features Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41360/toc.htm) for that release.

## Perform a Full Backup of Oracle Database Before Downgrading

Perform a full backup of your Oracle Database 11g Release 2 (11.2) database before you downgrade. Follow the procedures given in [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm).

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm) for more information

## Downgrading Oracle Database to an Earlier Release

You can downgrade your Oracle Database 11g Release 2 (11.2) database to a major release or a relevant patchset upgrade.

To downgrade the database to an earlier release

1. If you have enabled Oracle Database Vault on your database, then you must:
	- Grant the Database Vault `DV_PATCH_ADMIN` role for the `SYS` account.
		- Disable Database Vault before downgrading the database.
	See Also:
	[Oracle Database Vault Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23090/dvdisabl.htm#DVADM012) for instructions about disabling Oracle Database Vault
2. If you previously had upgraded the database and then used the `DBMS_DST` PL/SQL package to update the database time zone version, then you must apply the patch for the same time zone file version into the earlier release's Oracle home before downgrading.
	As an example scenario, assume that a release 10.2.0.4 database on Linux x64 using DSTv4 had been upgraded to release 11.2.0.2, and `DBMS_DST` was then run to update this database to DSTv14. Then, before downgrading from release 11.2.0.3 to 10.2.0.4, you need to apply on the release 10.2.0.4 side the DSTv14 patch for 10.2.0.4 for Linux x64. This ensures that your `TIMESTAMP` `WITH` `TIME` `ZONE` data is not logically corrupted during retrieval.
	To find which time zone file version your database is using, run:
	```
	SELECT value$ FROM sys.props$ WHERE NAME = 'DST_PRIMARY_TT_VERSION';
	```
	See Also:
	[Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/ch4datetime.htm#NLSPG261) for information on applying time zone files
3. If you had set the `ORA_TZFILE` environment variable to the full path name of the `timezone.dat` file when you upgraded to Oracle Database 11g Release 2 (11.2), then you must unset it if you subsequently downgrade your database.
	Two time zone files are included in the Oracle home directory:
	- The default time zone file at
		```
		$ORACLE_HOME/oracore/zoneinfo/timezonelrg.dat
		```
		- A smaller time zone file at
		```
		$ORACLE_HOME/oracore/zoneinfo/timezone.dat
		```
	If you do not unset the `ORA_TZFILE` variable, then connecting to the database using the smaller time zone file might produce the following errors:
	```
	SP2-1503: Unable to initialize Oracle call interface
	SP2-0152: ORACLE may not be functioning properly
	```
	See Also:
	[Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/ch4datetime.htm#NLSPG004) for more information about date and time data types and time zone support
4. If you have Oracle Application Express on your database, then you must copy the `apxrelod.sql` file from the Oracle Database 11g Release 2 (11.2) `ORACLE_HOME/apex/` directory to a directory outside of the Oracle home, such as the temporary directory on your system.
	Make a note of the new location of this file.
5. If you have created objects based on fixed objects, then drop these objects to avoid possible `ORA-00600` errors. You can re-create these objects after the downgrade.
6. Log in to the system as the owner of the Oracle Database 11g Release 2 (11.2) Oracle home directory.
7. This step is required only if Enterprise Manager Database Control is already configured for the database.
	Stop Database Control, as follows:
	1. Set the `ORACLE_UNQNAME` environment variable to the database unique name.
		2. Run the following command:
		```
		ORACLE_HOME/bin/emctl stop dbconsole
		```
	If the database being downgraded is an Oracle RAC database, then perform this step on all instances.
8. If you are downgrading an Oracle RAC database to 10g Release 1 (10.1), then you must remove extra voting disks before shutting down the Oracle Clusterware stack.
	1. To see the number of voting disks used and to list voting disk paths, run the following command:
		```
		Oracle_Clusterware_Home/bin/crsctl query css votedisk
		```
		2. Remove each additional voting disk you find in the previous step by running the following command, where `path` is the voting disk path listed in the `File` `Name` column displayed in the previous step:
		```
		Oracle_Clusterware_Home/bin/crsctl delete css votedisk path
		```
		For example:
		```
		Oracle_Clusterware_Home/bin/crsctl delete css votedisk /share/cluster2/vote_cluster2.dbf
		```
		Do not delete the last voting disk.
9. At a system prompt, change to the ORACLE\_HOME `/rdbms/admin` directory.
	Note:
	If you are downgrading a cluster database, then shut down the instance completely and change the `CLUSTER_DATABASE` initialization parameter to `FALSE`. After the downgrade, you must set this parameter back to `TRUE`.
10. Using SQL\*Plus, connect to the database instance as a user with `SYSDBA` privileges.
11. Start up the instance in `DOWNGRADE` mode:
	```
	SQL> STARTUP DOWNGRADE
	```
	You might be required to use the `PFILE` option to specify the location of your initialization parameter file.
12. If you have Enterprise Manager configured in your database, then drop the Enterprise Manager user:
	```
	DROP USER sysman CASCADE;
	```
	Note:
	After this step, MGMT\* synonyms may be invalid. Follow the guidelines in "Restoring Oracle Enterprise Manager after Downgrading Oracle Database" to validate the synonyms.
13. Set the system to spool results to a log file so you can track the changes and issues:
	```
	SQL> SPOOL downgrade.log
	```
14. Run `catdwgrd.sql`:
	```
	SQL> @catdwgrd.sql
	```
	The following are notes about running the script:
	- You must use the version of the script included with Oracle Database 11g Release 2 (11.2).
		- You must run the script in the Oracle Database 11g Release 2 (11.2) environment.
		- The script downgrades all Oracle Database components in the database to the major release or Oracle Database 11g patch release from which you originally upgraded.
	If you encounter any problems when you run the script, or any of the scripts in the remaining steps, then correct the causes of the problems and rerun the script. You can rerun any of the scripts described in this chapter as many times as necessary.
	If the downgrade for a component fails, then an `ORA-39709` error is displayed and the SQL\*Plus session terminates without downgrading the Oracle Database data dictionary. All components must be successfully downgraded before the Oracle Database data dictionary is downgraded. You must identify and fix the problem before rerunning the `catdwgrd.sql` script.
15. Turn off the spooling of script results to the log file:
	```
	SQL> SPOOL OFF
	```
	Then, check the spool file and verify that there were no errors generated during the downgrade. You named the spool file in Step [^2] and the suggested name was `downgrade.log`. Correct any problems you find in this file and rerun the downgrade script if necessary.
	Note:
	If you want to save the results of the first time you ran the downgrade script, then before you rerun it be sure to rename `downgrade.log` to something else.
16. Shut down the instance:
	```
	SQL> SHUTDOWN IMMEDIATE
	```
17. Exit SQL\*Plus.
18. If your operating system is Linux or UNIX, then change the following environment variables to point to the directories of the release to which you are downgrading:
	- `ORACLE_HOME`
		- `PATH`
	You should also check that your `oratab` file and any client scripts that set the value of `ORACLE_HOME` point to the downgraded Oracle home.
	See Also:
	[Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for your operating system for information about setting other important environment variables on your operating system
19. If your operating system is Windows, then complete the following steps:
	1. Stop all Oracle services, including the `OracleService` `SID` Oracle service of the Oracle Database 11g Release 2 (11.2) database, where `SID` is the instance name.
		For example, if your SID is ORCL, then enter the following at a command prompt:
		```
		C:\> NET STOP OracleServiceORCL
		```
		See Also:
		[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm)
		2. Delete the Oracle service at a command prompt by issuing the `ORADIM` command. For example, if your SID is ORCL, then enter the following command:
		```
		C:\> ORADIM -DELETE -SID ORCL
		```
		3. Create the Oracle service of the database that you are downgrading at a command prompt using the `ORADIM` command.
		```
		C:\> ORADIM -NEW -SID SID -INTPWD PASSWORD -MAXUSERS USERS
		     -STARTMODE AUTO -PFILE ORACLE_HOME\DATABASE\INITSID.ORA
		```
		This syntax includes the following variables:
		| Variable | Description |
		| --- | --- |
		| `SID` | Same SID name as the SID of the database being downgraded. |
		| `PASSWORD` | Password for the database instance. This is the password for the user connected with `SYSDBA` privileges. The - `INTPWD` option is not required. If you do not specify it, then operating system authentication is used, and no password is required. |
		| `USERS` | Maximum number of users who can be granted `SYSDBA` and `SYSOPER` privileges. |
		| `ORACLE_HOME` | Oracle home directory of the database to which you are downgrading. Ensure that you specify the full path name with the `-PFILE` option, including drive letter of the Oracle home directory. |
		For example, if you are downgrading to Oracle Database 10g Release 2 (10.2), if your SID is `ORCL`, your PASSWORD is `TWxy5791`, the maximum number of USERS is 10, and the ORACLE\_HOME directory is C:\\ORANT, then enter the following command:
		```
		C:\> ORADIM -NEW -SID ORCL -INTPWD TWxy5791 -MAXUSERS 10
		     -STARTMODE AUTO -PFILE C:\ORANT\DATABASE\INITORCL.ORA
		```
		Note:
		You are not required to change any Windows Registry settings when downgrading a database. The `ORADIM` utility makes all necessary changes automatically.
20. Restore the configuration files (for example, parameter files, password files, and so on) of the release to which you are downgrading.
	If this is an Oracle RAC database, execute the following command to return the database to single instance mode:
	```
	set CLUSTER_DATABASE=FALSE
	```
	Note:
	If you are downgrading a cluster database, then perform this step on all nodes in which this cluster database has instances configured. Set the `CLUSTER_DATABASE` initialization parameter to `FALSE`. After the downgrade, you must set this initialization parameter back to `TRUE`.
21. At a system prompt, change to the `ORACLE_HOME` `/rdbms/admin` directory of the previous release.
22. Start SQL\*Plus.
23. Connect to the database instance as a user with `SYSDBA` privileges.
24. Start up the instance:
	```
	SQL> STARTUP UPGRADE
	```
25. Set the system to spool results to a log file to track changes and issues:
	```
	SQL> SPOOL reload.log
	```
26. Run `catrelod.sql`:
	```
	SQL> @catrelod.sql
	```
	The `catrelod.sql` script reloads the appropriate version of all of the database components in the downgraded database.
27. If you are downgrading to Oracle Database 11g Release 1 (11.1.0.6), run the `xsrelod.sql` script:
	```
	SQL> @xsrelod.sql
	```
	Running the `xsrelod.sql` script avoids the following error:
	```
	PLS-00306: wrong number or types of arguments in call
	to 'INVALIDATE_DSD_CACHE' DBMS_XS_DATA_SECURITY_EVENTS
	PL/SQL: Statement ignored
	```
	Note:
	The PLS-00306 error is not an issue for Oracle Database release 11.2.0.7 or later.
28. If you are downgrading to Oracle Database 10g Release 1 (10.1.0.5) and you have XDB in your database, then run the `dbmsxdbt.sql` script:
	```
	@dbmsxdbt.sql
	```
	Running the `dbmsxdbt.sql` script avoids the following errors when reloading `XDB.DBMS_XDBT` package:
	```
	PLS-00201: identifier 'CTXSYS.CTX_OUTPUT' must be declaredPLS-00201: identifier 'CTX_DDL' must be declared
	```
29. If you are downgrading to Oracle Database 11g Release 1 or earlier, and you have Oracle Application Express in your database, then change to the directory to which you had copied the `apxrelod.sql` script (in step [^1]). Manually reload Oracle Application Express by running the `apxrelod.sql` script:
	```
	SQL> @apxrelod.sql
	```
	Running the `apxrelod.sql` script avoids package `APEX_030200.WWV_FLOW_HELP` being `INVALID` due to the following error:
	```
	PLS-00201: identifier 'CTX_DDL' must be declared
	```
30. Turn off the spooling of script results to the log file:
	```
	SQL> SPOOL OFF
	```
	Then, check the spool file and verify that the packages and procedures compiled successfully. You named the spool file in Step [^3]; the suggested name was `reload.log`. Correct any problems you find in this file and rerun the appropriate script if necessary.
31. Shut down and restart the instance for normal operation:
	```
	SQL> SHUTDOWN IMMEDIATE
	SQL> STARTUP
	```
	You might be required to use the `PFILE` option to specify the location of your initialization parameter file.
32. Perform this step if the database is configured for Oracle Label Security and you are downgrading to Oracle Database 10g Release 1 (10.1).
	1. Copy the `olstrig.sql` script from the Oracle Database 11g Release 2 (11.2) Oracle home to the Oracle home of the version to which the database is to be downgraded.
		2. Run `olstrig.sql` to re-create DML triggers on tables with Oracle Label Security policies.
		```
		SQL> @olstrig.sql
		```
	See the [Oracle Label Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e10745/toc.htm) for more information.
33. Run the `utlrp.sql` script:
	```
	SQL> @utlrp.sql
	```
	The `utlrp.sql` script recompiles all existing PL/SQL modules that were previously in an `INVALID` state, such as packages, procedures, types, and so on.
34. Exit SQL\*Plus.
35. If you are downgrading a cluster database, then you must run the following command to downgrade the Oracle Clusterware database configuration:
	```
	$ srvctl downgrade database -d db-unique-name -o old_ORACLE_HOME -t to_relnum
	```
	\[where `db-unique-name` is the database name (not the instance name), `old_ORACLE_HOME` is the location of the old Oracle home in which the downgraded database will be running. In this example, `to_relnum` is the database release number to which the database is being downgraded. (For example: 11.2.0.1.0.)\]
	Caution:
	By default, any named user may create a server pool. To restrict the operating system users that have this privilege, Oracle strongly recommends that you add specific users to the CRS Administrators list.
	See Also: [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD91105) for more information about adding users to the CRS Administrators list
	Note:
	Execute this command from the current Oracle home, not from the Oracle home to which the database is being downgraded.

Your database is now downgraded.

## Post-Downgrade Tasks for Oracle Database

Tasks might be required after downgrading Oracle Database. This section contains the following topics:

- Re-creating the Network Listener When Downgrading to Oracle Database Releases 10.2 or 11.1
- Restoring Oracle Enterprise Manager after Downgrading Oracle Database
	- Single-Instance Oracle Database Without Oracle ASM
		- Oracle RAC Database Without Oracle ASM
		- Single-Instance Oracle ASM Instance
		- Oracle ASM on Oracle RAC Instance
		- Single-Instance Oracle Database With Oracle ASM
		- Oracle RAC Database and Oracle ASM Instance
- Re-enabling Oracle Database Vault after Downgrading Oracle Database
- Restoration of the Configuration for Oracle Clusterware after Downgrading
- Downgrading and Database Links from Earlier Releases

### Re-creating the Network Listener When Downgrading to Oracle Database Releases 10.2 or 11.1

If you are downgrading the new database to Oracle Database 10g or Oracle Database 11g Release 1, then you must recreate the listener after performing the downgrade steps. Run Oracle Net Manager to delete the old listener and create a new listener.

- To start Oracle Net Manager from the Oracle Enterprise Manager console, select Service Management from the Tools menu, and then select Oracle Net Manager.
- On Microsoft Windows, select Programs from the Start menu, and then select Oracle - HOME\_NAME. Next, select Configuration and Migration Tools, and then Net Manager.
	See Also:
	[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm)

### Restoring Oracle Enterprise Manager after Downgrading Oracle Database

This task is required only if you are downgrading in some form and Oracle Enterprise Manager is configured on the host. To restore Oracle Enterprise Manager to its previous state, you must have saved your Oracle Enterprise Manager files and data before upgrading.

See Also:

["Saving Database Control Files and Data with the emdwgrd Utility"](upgrade.md)

If this is an Oracle RAC database using Oracle Clusterware, the database must be registered with the `srvctl` before running the `emca -restore` command. This needs to be executed from the `ORACLE_HOME` /bin of the version to which the database is being downgraded.

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/toc.htm) for information about `srvctl`

Run the `emca` `-restore` command with the appropriate options to restore Oracle Enterprise Manager Database Control or Grid Control to the old Oracle home. The options that you specify depend on whether the database being downgraded is an Oracle RAC database or an Oracle ASM database, as follows:

Note:

Use the Oracle Database 11g Release 2 (11.2) version of `emca` for this procedure. See [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for complete information about `emca`.

Single-Instance Oracle Database Without Oracle ASM

```
111Home/bin/emca -restore db
```

You are prompted to enter the following information:

- Oracle home for the database to be restored
- Database SID
- Listener port number

Oracle RAC Database Without Oracle ASM

```
111Home/bin/emca -restore db -cluster
```

You are prompted to enter the following information:

- Oracle home for the database to be restored
- Database unique name
- Listener port number

Single-Instance Oracle ASM Instance

```
111Home/bin/emca -restore asm
```

You are prompted to enter the following information:

- Oracle home for the database to be restored
- Oracle ASM port
- Oracle ASM SID

Oracle ASM on Oracle RAC Instance

```
111Home/bin/emca -restore asm -cluster
```

You are prompted to enter the following information:

- Oracle home for the database to be restored
- Oracle ASM port

Single-Instance Oracle Database With Oracle ASM

```
111Home/bin/emca -restore db_asm
```

You are prompted to enter the following information:

- Oracle home for the database to be restored
- Database SID
- Listener port number
- Oracle ASM port
- Oracle ASM home
- Oracle ASM SID \[+ASM\]

Oracle RAC Database and Oracle ASM Instance

```
111Home/bin/emca -restore db_asm -cluster
```

You are prompted to enter the following information:

- Oracle home for the database to be restored
- Database unique name
- Listener port number
- Oracle ASM port
- Oracle ASM Oracle home
- Oracle ASM SID \[+ASM\]

The output of `emca` varies according to the options that you specify and the values that you enter at the prompts.

For an inplace patchset upgrade, the original home backup you saved before applying the patchset must be restored. This step must be repeated on all the nodes in Oracle RAC environments. Running the `emca` `-restore` command is not required for an inplace patchset upgrade.

After completing the `emca` `-restore` procedure you are ready to restore the Oracle Enterprise Manager Database files and data with the `emdwgrd` utility. You must run the emdwgrd utility from the Oracle Database 11g Release 2 (11.2) home. But `ORACLE_HOME` and other environment variables must be set to point to the Oracle home from which the upgrade originally took place.

The following procedure is for Linux and UNIX. To run it on Windows, simply substitute `emdwgrd.bat` for `emdwgrd`.

Follow these steps to restore your database control files and data:

1. Set `ORACLE_HOME` to the Oracle home from which the database upgrade originally took place.
	For an inplace patchset upgrade, restore the backup of the original home (with one-off patch of Bug 7131048 if upgrading from 11.1.0.6), and set `ORACLE_HOME` to the current Oracle home.
2. Set `ORACLE_SID` to the SID of the database that was upgraded and then downgraded.
3. Set `PATH`, `LD_LIBRARY_PATH` and `SHLIB_PATH` to point to the Oracle home from which the database upgrade originally took place.
4. Go to the Oracle Database 11g Release 2 (11.2) home:
	```
	cd ORACLE_HOME/bin
	```
5. Execute one of the following:
	1. For a single-instance database, run the following command, where `SID` is the SID of the database that was upgraded and then downgraded and `save_directory` is the path to the storage location you chose when saving your database control files and data:
		```
		emdwgrd -restore -sid SID -path save_sirectory -tempTablespace TEMP
		```
		2. For an Oracle RAC database, remote copy is required across the cluster nodes. Define an environment variable to indicate which remote copy is configured. For example:
		```
		setenv EM_REMCP /usr/bin/scp
		```
		Then, execute the following `restore` command:
		```
		emdwgrd -restore -tempTablespace TEMP -cluster -sid SID10g -path save_directory
		```
		If 10g Oracle home is on a shared device, add `-shared` to the previous command line.
6. Enter the SYS and SYSMAN passwords when prompted by `emdwgrd`.
7. On a single-instance database, the `emdwgrd` utility produces output similar to the following:
	```
	Sat Apr 28 09:27:09 2007 - Verify EM DB Control files ... pass
	Sat Apr 28 09:27:09 2007 - Validating DB Connection to DB102 ... pass
	Sat Apr 28 09:27:19 2007 - Validating TEMP tablespace in DB102 ... pass
	Sat Apr 28 09:27:20 2007 - creating directory ... created
	Sat Apr 28 09:27:20 2007 - Stopping DB Control ... stopped
	Sat Apr 28 09:27:21 2007 - dropping sysman schema ... dropped
	Sat Apr 28 09:27:22 2007 - recreating sysman user ... recreated
	Sat Apr 28 09:27:23 2007 - Restoring DB Control files ... restored
	Sat Apr 28 09:27:23 2007 - Importing sysman schema ... imported
	Sat Apr 28 09:30:42 2007 - recompiling invalid objects ... recompiled
	Sat Apr 28 09:30:54 2007 - Starting DB Control ... started
	Sat Apr 28 09:32:37 2007 - DB Control was restored successfully.
	```
	When `emdwgrd` finishes, Oracle Enterprise Manager Database Control has been downgraded to the old Oracle home.
	On an Oracle RAC database, the `emdwgrd` utility produces output similar to the following:
	```
	$ /scratch/oracle/product/11.1.0/db_1/bin/emdwgrd -srcOracleHome $ORACLE_HOME -sid DB102 -path /scratch/rpattabh/ravi/tmp/dbcdir5 -restore –cluster -tempTablespace TEMP
	 
	Enter sys password for database DB102?
	*****
	 
	Enter sysman password for database DB102?
	*****
	 
	Sat Apr 28 09:27:09 2007 - Verify EM DB Control files ... pass
	Sat Apr 28 09:27:09 2007 - Validating DB Connection to DB102 ... pass
	Sat Apr 28 09:27:19 2007 - Validating TEMP tablespace in DB102 ... pass
	Sat Apr 28 09:27:20 2007 - creating directory ... created
	Sat Apr 28 09:27:20 2007 - Stopping DB Control on all Nodes 
	stbdq04, r101b1, /oradbnas/sangeeta/10.1.0/db, stop, 0
	stbdq05, r101b2, /oradbnas/sangeeta/10.1.0/db, stop, 1
	 
	Please Execute '/tmp/racdwgrd_dbctl.sh' on Node1, Node2. 
	 
	Press yes to continue when the operations are successful. 
	Continue (yes/no) ?
	y
	 
	... stopped
	Sat Apr 28 09:27:21 2007 - dropping sysman schema ... dropped
	Sat Apr 28 09:27:22 2007 - recreating sysman user ... recreated
	Sat Apr 28 09:27:23 2007 - Restoring DB Control files 
	Executing Restore directories to node Node1
	Executing Restore directories to node Node2
	 
	... restored
	Sat Apr 28 09:27:23 2007 - Importing sysman schema ... imported
	Sat Apr 28 09:30:42 2007 - recompiling invalid objects ... recompiled
	Sat Apr 28 09:32:37 2007 - DB Control was restored successfully.
	Sat Apr 28 09:33:54 2007 - Starting DB Control On All nodes 
	 
	Please Execute '/tmp/racdwgrd_dbctl.sh' on Node1, Node2. 
	 
	Press yes to continue when the operations are successful. 
	Continue (yes/no) ?
	y
	 
	... started
	Sat Apr 28 09:38:57 2007 - Dump directory was dropped successfully.
	```

### Re-enabling Oracle Database Vault after Downgrading Oracle Database

If you use Oracle Database Vault, then you were instructed to disable it before downgrading your database. To use Oracle Database Vault after downgrading, you must re-enable it.

To enable Oracle Database Vault after downgrading:

1. Connect to SQL\*Plus as a user who has been granted the `DV_OWNER` role.
2. Issue the following statements:
	```
	ALTER TRIGGER DVSYS.DV_BEFORE_DDL_TRG ENABLE;
	ALTER TRIGGER DVSYS.DV_AFTER_DDL_TRG ENABLE;
	```

See Also:

[Oracle Database Vault Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23090/dvdisabl.htm#DVADM012)

### Restoration of the Configuration for Oracle Clusterware after Downgrading

You can restore the Oracle Clusterware configuration to the state it was in before the Oracle Clusterware 11g release 2 (11.2) upgrade. To do this, you must restore the release from which you were upgrading. Any configuration changes you have performed during or after the 11g release 2 (11.2) upgrade process are removed and cannot be recovered.

See Also:

- [Oracle Grid Infrastructure Installation Guide for Linux](https://docs.oracle.com/cd/E11882_01/install.112/e41961/toc.htm)
- [Oracle Grid Infrastructure Installation Guide for Microsoft Windows (32-Bit), Microsoft Windows (64-Bit) on Intel Itanium, Microsoft Windows x64](https://docs.oracle.com/cd/E11882_01/install.112/e48194/toc.htm)
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/toc.htm)
- [Oracle Database Storage Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm)

### Downgrading and Database Links from Earlier Releases

Before downgrading, you must use Oracle Data Pump full database export with the `INCLUDE=DBLINK` parameter to export all database links into a dump file suitable for import into the downgraded database. This dump file can then be used to replace the database links after the downgrade.

Ensure that you know the password for any newly-created database links (that is, database links that you may have created while running the new release from which you are downgrading. Knowing the database link password is necessary because you will need to reset the database link password after downgrading to the earlier release. This is only required for newly-created dblinks, those that you created after you upgraded to the new release.

Unless the database link password is reset, an internal error will be displayed when anyone attempts to make use of the database link. The internal error that is reported in the Oracle trace file when the Oracle server fails to retrieve the password of the database link is as follows: "ORA-00600: \[kzdlk\_zt2 err\], \[18446744073709551601\]". Alternatively, you may just recreate the dblinks after you complete the downgrade.

Note:

You can work with Oracle Support if you want to create new database links that are immune to the ORA-00600 issue while running the new Oracle Database release 11.2 upgrade.

## Troubleshooting the Downgrade of Oracle Database

Oracle provides troubleshooting information for issues that may occur when downgrading Oracle Database. For the latest information on this release, also refer to [Oracle Database Readme](https://docs.oracle.com/cd/E11882_01/readmes.112/e41331/toc.htm).

Downgrading release 11.2 of Oracle Grid Infrastructure fails

If downgrading release 11.2 of Oracle Grid Infrastructure fails, then refer to the support note "How to Proceed from Failed Upgrade to Grid Infrastructure" on Linux/Unix \[ID 969254.1\]" on `https://support.oracle.com`. Oracle recommends that you read the entire note before taking action.

Error raised from the 11.2.0.1 xsrelod.sql script

When downgrading Oracle Database from release 11.2.0.2 or 11.2.0.3 to release 11.2.0.1, an error may be raised from the `xsrelod.sql` script, which is included with release 11.2.0.1. This problem only occurs after downgrading to release 11.2.0.1 and then attempting to enable XML DB indexes. The error "ORA-01418: specified index does not exist" may be raised and can safely be ignored.

Error raised from the Oracle Multimedia imrelod.sql script

When downgrading Oracle Database to release 11.2.0.2, an error may be raised from the `imrelod.sql` script which is included with release 11.2.0.2. The error "ORA-20000: Oracle ORDIM component in registry is status: DOWNGRADED. Oracle ORDIM must be installed and valid prior to Oracle Multimedia upgrade, downgrade, or patch." can safely be ignored.

Downgrading Oracle Database causes invalid object CTX\_FILTER\_CACHE\_STATISTICS

After downgrading Oracle Database, the following invalid Text object may be seen:

```
CTX_FILTER_CACHE_STATISTICS (synonym)
CTX_FILTER_CACHE_STATISTICS (view)
```

To fix this problem, in the current release of Oracle Database, after running the `catdwgrd.sql` script and before running the `catrelod.sql` script, issue the following two commands:

```
SQL> drop public synonym ctx_filter_cache_statistics;
SQL> drop view ctx_filter_cache_statistics;
```

[^1]: If you have Oracle Application Express on your database, then you must copy the `apxrelod.sql` file from the Oracle Database 11g Release 2 (11.2) `ORACLE_HOME/apex/` directory to a directory outside of the Oracle home, such as the temporary directory on your system.

Make a note of the new location of this file.

[^undefined]: If you have created objects based on fixed objects, then drop these objects to avoid possible `ORA-00600` errors. You can re-create these objects after the downgrade.

[^undefined]: Log in to the system as the owner of the Oracle Database 11g Release 2 (11.2) Oracle home directory.

[^undefined]: This step is required only if Enterprise Manager Database Control is already configured for the database.

Stop Database Control, as follows:

1. Set the `ORACLE_UNQNAME` environment variable to the database unique name.
2. Run the following command:
	```
	ORACLE_HOME/bin/emctl stop dbconsole
	```

If the database being downgraded is an Oracle RAC database, then perform this step on all instances.

[^undefined]: If you are downgrading an Oracle RAC database to 10g Release 1 (10.1), then you must remove extra voting disks before shutting down the Oracle Clusterware stack.

1. To see the number of voting disks used and to list voting disk paths, run the following command:
	```
	Oracle_Clusterware_Home/bin/crsctl query css votedisk
	```
2. Remove each additional voting disk you find in the previous step by running the following command, where `path` is the voting disk path listed in the `File` `Name` column displayed in the previous step:
	```
	Oracle_Clusterware_Home/bin/crsctl delete css votedisk path
	```
	For example:
	```
	Oracle_Clusterware_Home/bin/crsctl delete css votedisk /share/cluster2/vote_cluster2.dbf
	```
	Do not delete the last voting disk.

[^undefined]: At a system prompt, change to the ORACLE\_HOME `/rdbms/admin` directory.

Note:

If you are downgrading a cluster database, then shut down the instance completely and change the `CLUSTER_DATABASE` initialization parameter to `FALSE`. After the downgrade, you must set this parameter back to `TRUE`.

[^undefined]: Using SQL\*Plus, connect to the database instance as a user with `SYSDBA` privileges.

[^undefined]: Start up the instance in `DOWNGRADE` mode:

```
SQL> STARTUP DOWNGRADE
```

You might be required to use the `PFILE` option to specify the location of your initialization parameter file.

[^undefined]: If you have Enterprise Manager configured in your database, then drop the Enterprise Manager user:

```
DROP USER sysman CASCADE;
```

Note:

After this step, MGMT\* synonyms may be invalid. Follow the guidelines in "Restoring Oracle Enterprise Manager after Downgrading Oracle Database" to validate the synonyms.

[^2]: Set the system to spool results to a log file so you can track the changes and issues:

```
SQL> SPOOL downgrade.log
```

[^undefined]: Run `catdwgrd.sql`:

```
SQL> @catdwgrd.sql
```

The following are notes about running the script:

- You must use the version of the script included with Oracle Database 11g Release 2 (11.2).
- You must run the script in the Oracle Database 11g Release 2 (11.2) environment.
- The script downgrades all Oracle Database components in the database to the major release or Oracle Database 11g patch release from which you originally upgraded.

If you encounter any problems when you run the script, or any of the scripts in the remaining steps, then correct the causes of the problems and rerun the script. You can rerun any of the scripts described in this chapter as many times as necessary.

If the downgrade for a component fails, then an `ORA-39709` error is displayed and the SQL\*Plus session terminates without downgrading the Oracle Database data dictionary. All components must be successfully downgraded before the Oracle Database data dictionary is downgraded. You must identify and fix the problem before rerunning the `catdwgrd.sql` script.

[^undefined]: Turn off the spooling of script results to the log file:

```
SQL> SPOOL OFF
```

Then, check the spool file and verify that there were no errors generated during the downgrade. You named the spool file in Step 13 and the suggested name was `downgrade.log`. Correct any problems you find in this file and rerun the downgrade script if necessary.

Note:

If you want to save the results of the first time you ran the downgrade script, then before you rerun it be sure to rename `downgrade.log` to something else.

[^undefined]: Shut down the instance:

```
SQL> SHUTDOWN IMMEDIATE
```

[^undefined]: Exit SQL\*Plus.

[^undefined]: If your operating system is Linux or UNIX, then change the following environment variables to point to the directories of the release to which you are downgrading:

- `ORACLE_HOME`
- `PATH`

You should also check that your `oratab` file and any client scripts that set the value of `ORACLE_HOME` point to the downgraded Oracle home.

See Also:

[Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for your operating system for information about setting other important environment variables on your operating system

[^undefined]: If your operating system is Windows, then complete the following steps:

1. Stop all Oracle services, including the `OracleService` `SID` Oracle service of the Oracle Database 11g Release 2 (11.2) database, where `SID` is the instance name.
	For example, if your SID is ORCL, then enter the following at a command prompt:
	```
	C:\> NET STOP OracleServiceORCL
	```
	See Also:
	[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm)
2. Delete the Oracle service at a command prompt by issuing the `ORADIM` command. For example, if your SID is ORCL, then enter the following command:
	```
	C:\> ORADIM -DELETE -SID ORCL
	```
3. Create the Oracle service of the database that you are downgrading at a command prompt using the `ORADIM` command.
	```
	C:\> ORADIM -NEW -SID SID -INTPWD PASSWORD -MAXUSERS USERS
	     -STARTMODE AUTO -PFILE ORACLE_HOME\DATABASE\INITSID.ORA
	```
	This syntax includes the following variables:
	| Variable | Description |
	| --- | --- |
	| `SID` | Same SID name as the SID of the database being downgraded. |
	| `PASSWORD` | Password for the database instance. This is the password for the user connected with `SYSDBA` privileges. The - `INTPWD` option is not required. If you do not specify it, then operating system authentication is used, and no password is required. |
	| `USERS` | Maximum number of users who can be granted `SYSDBA` and `SYSOPER` privileges. |
	| `ORACLE_HOME` | Oracle home directory of the database to which you are downgrading. Ensure that you specify the full path name with the `-PFILE` option, including drive letter of the Oracle home directory. |
	For example, if you are downgrading to Oracle Database 10g Release 2 (10.2), if your SID is `ORCL`, your PASSWORD is `TWxy5791`, the maximum number of USERS is 10, and the ORACLE\_HOME directory is C:\\ORANT, then enter the following command:
	```
	C:\> ORADIM -NEW -SID ORCL -INTPWD TWxy5791 -MAXUSERS 10
	     -STARTMODE AUTO -PFILE C:\ORANT\DATABASE\INITORCL.ORA
	```
	Note:
	You are not required to change any Windows Registry settings when downgrading a database. The `ORADIM` utility makes all necessary changes automatically.

[^undefined]: Restore the configuration files (for example, parameter files, password files, and so on) of the release to which you are downgrading.

If this is an Oracle RAC database, execute the following command to return the database to single instance mode:

```
set CLUSTER_DATABASE=FALSE
```

Note:

If you are downgrading a cluster database, then perform this step on all nodes in which this cluster database has instances configured. Set the `CLUSTER_DATABASE` initialization parameter to `FALSE`. After the downgrade, you must set this initialization parameter back to `TRUE`.

[^undefined]: At a system prompt, change to the `ORACLE_HOME` `/rdbms/admin` directory of the previous release.

[^3]: Set the system to spool results to a log file to track changes and issues:

```
SQL> SPOOL reload.log
```

[^undefined]: Run `catrelod.sql`:

```
SQL> @catrelod.sql
```

The `catrelod.sql` script reloads the appropriate version of all of the database components in the downgraded database.

[^undefined]: If you are downgrading to Oracle Database 11g Release 1 (11.1.0.6), run the `xsrelod.sql` script:

```
SQL> @xsrelod.sql
```

Running the `xsrelod.sql` script avoids the following error:

```
PLS-00306: wrong number or types of arguments in call
to 'INVALIDATE_DSD_CACHE' DBMS_XS_DATA_SECURITY_EVENTS
PL/SQL: Statement ignored
```

Note:

The PLS-00306 error is not an issue for Oracle Database release 11.2.0.7 or later.

[^undefined]: If you are downgrading to Oracle Database 10g Release 1 (10.1.0.5) and you have XDB in your database, then run the `dbmsxdbt.sql` script:

```
@dbmsxdbt.sql
```

Running the `dbmsxdbt.sql` script avoids the following errors when reloading `XDB.DBMS_XDBT` package:

```
PLS-00201: identifier 'CTXSYS.CTX_OUTPUT' must be declaredPLS-00201: identifier 'CTX_DDL' must be declared
```

[^undefined]: If you are downgrading to Oracle Database 11g Release 1 or earlier, and you have Oracle Application Express in your database, then change to the directory to which you had copied the `apxrelod.sql` script (in step 4). Manually reload Oracle Application Express by running the `apxrelod.sql` script:

```
SQL> @apxrelod.sql
```

Running the `apxrelod.sql` script avoids package `APEX_030200.WWV_FLOW_HELP` being `INVALID` due to the following error:

```
PLS-00201: identifier 'CTX_DDL' must be declared
```

[^undefined]: Turn off the spooling of script results to the log file:

```
SQL> SPOOL OFF
```

Then, check the spool file and verify that the packages and procedures compiled successfully. You named the spool file in Step 25; the suggested name was `reload.log`. Correct any problems you find in this file and rerun the appropriate script if necessary.

[^undefined]: Shut down and restart the instance for normal operation:

```
SQL> SHUTDOWN IMMEDIATE
SQL> STARTUP
```

You might be required to use the `PFILE` option to specify the location of your initialization parameter file.

[^undefined]: Perform this step if the database is configured for Oracle Label Security and you are downgrading to Oracle Database 10g Release 1 (10.1).

1. Copy the `olstrig.sql` script from the Oracle Database 11g Release 2 (11.2) Oracle home to the Oracle home of the version to which the database is to be downgraded.
2. Run `olstrig.sql` to re-create DML triggers on tables with Oracle Label Security policies.
	```
	SQL> @olstrig.sql
	```

See the [Oracle Label Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e10745/toc.htm) for more information.

[^undefined]: Run the `utlrp.sql` script:

```
SQL> @utlrp.sql
```

The `utlrp.sql` script recompiles all existing PL/SQL modules that were previously in an `INVALID` state, such as packages, procedures, types, and so on.

[^undefined]: Exit SQL\*Plus.

[^undefined]: If you are downgrading a cluster database, then you must run the following command to downgrade the Oracle Clusterware database configuration:

```
$ srvctl downgrade database -d db-unique-name -o old_ORACLE_HOME -t to_relnum
```

\[where `db-unique-name` is the database name (not the instance name), `old_ORACLE_HOME` is the location of the old Oracle home in which the downgraded database will be running. In this example, `to_relnum` is the database release number to which the database is being downgraded. (For example: 11.2.0.1.0.)\]

Caution:

By default, any named user may create a server pool. To restrict the operating system users that have this privilege, Oracle strongly recommends that you add specific users to the CRS Administrators list.

See Also: [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD91105) for more information about adding users to the CRS Administrators list

Note:

Execute this command from the current Oracle home, not from the Oracle home to which the database is being downgraded.