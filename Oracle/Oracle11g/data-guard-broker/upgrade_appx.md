---
title: Data Guard Broker Upgrading and Downgrading
book: Data Guard Broker
doc_id: E40771-07
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40771/upgrade_appx.htm
tags:
  - oracle
  - 11g
  - data-guard-broker
---

## B Data Guard Broker Upgrading and Downgrading

This appendix guides you through the process of upgrading or downgrading the Oracle databases and Oracle Enterprise Manager in a broker configuration. It contains the following topics:

See Also:

[Chapter 2, "Oracle Data Guard Installation"](install.md)

## B.1 Upgrading from Release 9.2.0 to Release 11.2

If you are currently running an Oracle Data Guard release 9.2.0 configuration, you must upgrade to Oracle Database release 11.2, and re-create the broker configuration, as follows:

1. Delete (remove) the release 9.2.0 broker configuration using Data Guard Manager or DGMGRL release 9.2.0. For example, the DGMGRL `REMOVE CONFIGURATION` command can be used.
2. If using DGMGRL, clear the `LOG_ARCHIVE_DEST_` `n` initialization parameter settings by using the `ALTER SYSTEM SET LOG_ARCHIVE_DEST_` n `=" "` SQL\*Plus command.
3. Upgrade the database software to Oracle release 11.2. See the Oracle Database installation documentation that is appropriate for your operating system.
4. Oracle Enterprise Manager and Data Guard Manager release 9.2.0 cannot manage a broker configuration running Oracle Data Guard release 11.2.
	See Also:
	My Oracle Support note 787461.1 at `http://support.oracle.com` for information about which versions of Enterprise Manager Grid Control are required to manage the full set of Data Guard features in various Oracle Database releases
5. If you are using DGMGRL release 9.2.0, you must upgrade to Data Guard command-line interface release 11.2:
	- DGMGRL release 9.2.0 is not compatible with Oracle Data Guard release 11.2.
		Note:
		Existing Oracle9i command-line scripts are supported in Oracle Database 11.2 for non-Oracle RAC databases. See [Appendix A](deprecated_appx.md) for information about deprecated commands.
		- DGMGRL release 11.2 is not compatible with Oracle Data Guard release 9.2.0.
		Note:
		Oracle Database 11.2 command-line scripts are not supported in Oracle9i.
6. Invoke Enterprise Manager or the DGMGRL command-line interface, and re-create the broker configuration.

## B.2 Upgrading from Release 10.n and 11.1 to Release 11.2

If you are currently running an Oracle Data Guard release 10.n or 11.1 configuration, you can upgrade the database software to Oracle release 11.2 using the Oracle Database installation documentation that is appropriate for your operating system.

Note:

Prior to Release 11.2, the configuration file was restricted to reside only on disks having the same sector size (physical block size) as that upon which the file was initially created. This was not a problem because there was typically a single sector size in use within a given broker configuration. In anticipation of having mixed sector sizes somewhere within a given broker configuration, the 11.2 broker configuration file is now completely insensitive to the underlying sector size, so long as the sector size is 4KB or less.

Conversion of the configuration file to be insensitive to the underlying sector size occurs during the upgrade processing in Step 5 below.

Step 1 Disable fast-start failover if it is enabled.

Issue the following DGMGRL command to disable fast-start failover:

```
DGMGRL> DISABLE FAST_START FAILOVER;
```

Step 2 Shut down the 10.n or 11.1 Data Guard broker, whichever version you are running.

Disable the broker's management of the configuration and then stop the broker. For example:

1. Issue the following DGMGRL command to disable the broker's active management of the databases in the Data Guard configuration:
	```
	DGMGRL> DISABLE CONFIGURATION;
	```
2. Issue the following SQL\*Plus statement to stop the broker:
	```
	SQL> ALTER SYSTEM SET DG_BROKER_START=FALSE;
	```

Step 3 Make a copy of the current broker configuration files.

Make a copy of the current broker configuration files, as indicated by the following initialization parameters: `DG_BROKER_CONFIG_FILE1` and `DG_BROKER_CONFIG_FILE2`.

Step 4 Upgrade the Oracle Database software to release 11.2.

For step-by-step upgrade instructions, see the Oracle Database installation documentation that is appropriate for your operating system.

The DGMGRL command-line interface must also be upgraded to release 11.2 in order to manage and monitor a broker configuration running Oracle Data Guard release 11.2. DGMGRL release 11.2 cannot be used to manage Data Guard releases 10.n or 11.1.

Note:

Existing release 10.n or 11.1 DGMGRL command-line scripts are supported by the DGMGRL command-line interface available in release 11.2.

Release 11.n DGMGRL command-line scripts are not guaranteed to be supported by Oracle Database release 10.n.

Step 5 Start the broker.

After the upgrade, start the release 11.2 Data Guard Broker. For example:

1. Issue the following SQL\*Plus statements to start the broker:
	```
	SQL> ALTER SYSTEM SET DG_BROKER_START=TRUE;
	```
2. Issue the following DGMGRL command to enable the broker's active management of the databases in the Data Guard configuration:
	```
	DGMGRL> ENABLE CONFIGURATION
	```

The first time the release 11.2 broker starts, it will detect the existence of the release 10.n and 11.1 broker configuration files and automatically upgrade them to include any new properties that were introduced in release 11.2 (for example, the fast-start failover properties). This automatic conversion is transparent, permanent, and occurs only once.

Note:

As of this automatic upgrade that occurs in Step 5, the configuration file may henceforth reside on a disk having any supported disk sector size (physical block size) up to and including 4KB sectors.

Note:

The observer that was started prior to the upgrade will automatically be stopped and unable to observe the configuration once the upgrade is complete. You must use an 11.2 version of the Oracle Observer software to observe Oracle databases running version 11.2 or higher.

See Also:

[Appendix A, "Changed and Deprecated Features"](deprecated_appx.md)

## B.3 Upgrading from Release 11.2.0.1 to 11.2.0.2 and other Patch Releases

In a Data Guard broker configuration, the process for upgrading from one patch release to the next (for example, from 11.2.0.1 to 11.2.0.2 or from 11.2.0.2 to 11.2.0.3) is the same process as described in "Upgrading from Release 10.n and 11.1 to Release 11.2". The broker must be disabled before the upgrade and re-enabled after the upgrade is complete.

## B.4 Downgrading from Release 11.2

If you have upgraded to release 11.2 and want to downgrade to your prior release, you must downgrade the database release and re-create the broker configuration as follows:

1. Delete (remove) the release 11.2 broker configuration using Enterprise Manager or DGMGRL release 11.2. For example, the DGMGRL `REMOVE CONFIGURATION` command can be used.
2. Downgrade the Oracle Database software to the prior Oracle release. See the Oracle Database documentation that is appropriate for your operating system.
3. You can downgrade the Data Guard broker to release 10.n or 11.1 as follows:
	- If you are confident that you made no changes to your broker configuration after upgrading to release 11.2, you can copy the broker configuration files that you created during the upgrade procedure (described in Section B.2). Then, invoke Enterprise Manager or the DGMGRL command-line interface and reenable the broker configuration as it existed at the time you made that copy.
		- Alternatively, you can invoke Enterprise Manager or the DGMGRL command-line interface to re-create the broker configuration.
4. You can downgrade the Data Guard broker to Oracle release 9.2.0, as follows:
	- If you were using Enterprise Manager, you can continue to use the Oracle Enterprise Manager release 10.2 to manage your 9.2.0 broker configuration. You can also downgrade to the Data Guard Manager by re-installing Oracle Enterprise Manager release 9.2.0.
		- Invoke Enterprise Manager, the Data Guard Manager, or the DGMGRL command-line interface and re-create the broker configuration.