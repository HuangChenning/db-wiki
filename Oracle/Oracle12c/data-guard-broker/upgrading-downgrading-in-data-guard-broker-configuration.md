---
title: Broker
book: Data Guard Broker
doc_id: E85768-01
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/dgbkr/upgrading-downgrading-in-data-guard-broker-configuration.html
tags:
  - oracle
  - 12c
  - data-guard-broker
---

Use these topics to upgrade or downgrade Oracle databases and Oracle Enterprise Manager Cloud Control (Cloud Control) in a broker configuration.

See Also:

[Oracle Data Guard Installation](oracle-data-guard-broker-installation-requirements.md)

### A.1 Upgrading from Oracle Database 9i Release 2 (9.2) to Oracle Database 12c

If you are currently running a broker configuration in Oracle Database 9i Release 2 (9.2), then you must upgrade to Oracle Database 12c Release 1 (12.1) or Oracle Database 12c Release 2 (12.2), and then re-create the broker configuration.

The following steps use Oracle Database 12c Release 2 (12.2), but you could substitute Oracle Database 12c Release 1 (12.1).

1. Delete (remove) the Oracle Database 9i Release 2 (9.2) broker configuration. For example, the DGMGRL `REMOVE CONFIGURATION` command can be used. To perform the deletion you must use Oracle Data Guard Manager or DGMGRL running on Oracle Database 9i Release 2 (9.2).
2. If using DGMGRL, clear the `LOG_ARCHIVE_DEST_` `n` initialization parameter settings by using the `ALTER SYSTEM SET LOG_ARCHIVE_DEST_` n `=" "` SQL\*Plus command.
3. Upgrade the database software to Oracle Database 12c Release 2 (12.2). See the Oracle Database installation documentation that is appropriate for your operating system.
4. Oracle Enterprise Manager and Oracle Data Guard Manager running on Oracle Database 9i Release 2 (9.2) cannot manage a broker configuration running on Oracle Database 12c Release 2 (12.2).
	See Also:
	My Oracle Support note 787461.1 at [`http://support.oracle.com`](http://support.oracle.com/) for information about which versions of Enterprise Manager Cloud Control (formerly called Grid Control) are required to manage the full set of Oracle Data Guard features in various Oracle Database releases
5. If you are using DGMGRL running on Oracle Database 9i Release 2 (9.2), then you must upgrade to DGMGRL running on Oracle Database 12c Release 2 (12.2):
	- DGMGRL running on Oracle Database 9i Release 2 (9.2) is not compatible with Oracle Data Guard running on Oracle Database 12c Release 2 (12.2).
	- DGMGRL running on Oracle Database 12c Release 2 (12.2) is not compatible with Oracle Data Guard running on Oracle Database 9i Release 2 (9.2).
		Note:
		Oracle Database 12c command-line scripts are not supported in Oracle9i.
6. Invoke Enterprise Manager or the DGMGRL command-line interface, and re-create the broker configuration.

### A.2 Upgrading from Oracle Database 10g and Oracle Database 11g to Oracle Database 12c

If you are currently running Oracle Data Guard on Oracle Database 10g or Oracle Database 11g, then you can upgrade the database software to Oracle Database 12c Release 1 (12.1) or Oracle Database 12c Release 2 (12.2) using the Oracle Database installation documentation that is appropriate for your operating system.

Note:

Prior to Oracle Database 11g Release 2 (11.2), the configuration file was restricted to reside only on disks having the same sector size (physical block size) as that upon which the file was initially created. This was not a problem because there was typically a single sector size in use within a given broker configuration. In anticipation of having mixed sector sizes somewhere within a given broker configuration, the broker configuration file is now completely insensitive to the underlying sector size, so long as the sector size is 4KB or less.

Conversion of the configuration file to be insensitive to the underlying sector size occurs during the upgrade processing in Step 5 below.

The following steps use Oracle Database 12c Release 2 (12.2), but you could substitute Oracle Database 12c Release 1 (12.1).

1. Issue the following DGMGRL command to disable fast-start failover:
	```
	DGMGRL> DISABLE FAST_START FAILOVER;
	```
2. Shut down the 10.n or 11.n Oracle Data Guard broker, whichever version you are running.
	1. Issue the following DGMGRL command to disable the broker's active management of the databases in the Oracle Data Guard configuration:
		```
		DGMGRL> DISABLE CONFIGURATION;
		```
		2. Issue the following SQL\*Plus statement to stop the broker:
		```
		SQL> ALTER SYSTEM SET DG_BROKER_START=FALSE;
		```
3. Make a copy of the current broker configuration files, as indicated by the following initialization parameters: `DG_BROKER_CONFIG_FILE1` and `DG_BROKER_CONFIG_FILE2`.
4. Upgrade the Oracle Database software to Oracle Database 12c Release 2 (12.2). For step-by-step upgrade instructions, see the Oracle Database installation documentation that is appropriate for your operating system.
	The DGMGRL command-line interface must also be upgraded in order to manage and monitor a broker configuration running on Oracle Database 12c Release 2 (12.2). DGMGRL running on Oracle Database 12c Release 2 (12.2) cannot be used to manage Oracle Data Guard running on Oracle Database 10g or Oracle Database 11g.
	Note:
	Existing DGMGRL command-line scripts for Oracle Database 10g and Oracle Database 11g are supported by the DGMGRL command-line interface available in Oracle Database 12c Release 2 (12.2).
	DGMGRL command-line scripts for Oracle Database 11g are not guaranteed to be supported by Oracle Database 10g.
5. After the upgrade to Oracle Database 12c Release 2 (12.2), start the broker. For example:
	1. Issue the following SQL\*Plus statements to start the broker:
		```
		SQL> ALTER SYSTEM SET DG_BROKER_START=TRUE;
		```
		2. Issue the following DGMGRL command to enable the broker's active management of the databases in the Oracle Data Guard configuration:
		```
		DGMGRL> ENABLE CONFIGURATION;
		```
	The first time the broker starts on Oracle Database 12c Release 2 (12.2) it detects the existence of the Oracle Database 10g and Oracle Database 11g broker configuration files. It automatically upgrades them to include any new properties that were introduced in Oracle Database 12c Release 2 (12.2). This automatic conversion is transparent, permanent, and occurs only once.
	Note:
	As of this automatic upgrade that occurs in Step 5, the configuration file may henceforth reside on a disk having any supported disk sector size (physical block size) up to and including 4KB sectors.

Note:

The observer that was started prior to the upgrade will automatically be stopped and unable to observe the configuration once the upgrade is complete. You must use an Oracle Database 12c version of the Oracle Observer software to observe Oracle databases running on Oracle Database 12c Release 2 (12.2) or higher.

### A.3 Downgrading from Oracle Database 12c

If you have upgraded to Oracle Database 12c Release 1 (12.1) or Oracle Database 12c Release 2 (12.2) and want to downgrade to your prior release, then you must downgrade the database release and re-create the broker configuration.

Take the following steps (these steps use Oracle Database 12c Release 2 (12.2), but you could substitute Oracle Database 12c Release 1 (12.1)).

1. Delete (remove) the Oracle Database 12c Release 2 (12.2) broker configuration using Enterprise Manager or DGMGRL running on Oracle Database 12c Release 2 (12.2). For example, the DGMGRL `REMOVE CONFIGURATION` command can be used.
2. Downgrade the Oracle Database software to the prior Oracle release. See the Oracle Database documentation that is appropriate for your operating system.
3. You can downgrade the Oracle Data Guard broker to Oracle Database 10g or Oracle Database 11g as follows:
	- If you are confident that you made no changes to your broker configuration after upgrading to Oracle Database 12c Release 2 (12.2), then you can copy the broker configuration files that you created during the upgrade procedure (described in Upgrading from Oracle Database 10g and Oracle Database 11g to Oracle Database 12c). Then, invoke Enterprise Manager or the DGMGRL command-line interface and reenable the broker configuration as it existed at the time you made that copy.
	- Alternatively, you can invoke Enterprise Manager or the DGMGRL command-line interface to re-create the broker configuration.
4. You can downgrade the Oracle Data Guard broker to Oracle Database 9i Release 2 (9.2), as follows:
	- If you were using Oracle Enterprise Manager, you can continue to use it running on Oracle Database 10g Release 2 (10.2) to manage your Oracle Database 9i Release 2 (9.2) broker configuration. You can also downgrade to the Oracle Data Guard Manager by re-installing Oracle Database 9i Release 2 (9.2) Enterprise Manager.
	- Invoke Enterprise Manager, the Oracle Data Guard Manager, or the DGMGRL command-line interface and re-create the broker configuration.