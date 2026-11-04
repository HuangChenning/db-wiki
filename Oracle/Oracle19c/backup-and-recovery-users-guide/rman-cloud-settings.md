---
title: Persistent Settings for RMAN Cloud Backups
book: Backup and Recovery User Guide
doc_id: E96241-26
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/rman-cloud-settings.html
tags:
  - oracle
  - 19c
  - backup-and-recovery-users-guide
---

After you install the Oracle Database Cloud Backup Module, use the RMAN `CONFIGURE` command to create a persistent RMAN configuration for cloud backup and restore operations.

## About Configuring SBT Channel

RMAN requires the system backup to tape (SBT) channel to perform cloud backup and recovery operations.

Use the [`CONFIGURE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/bradv&id=RCMRF-GUID-B5094E73-C26C-4FED-AE39-8C2E9540050A) command to create an automatic SBT channel that corresponds with a cloud backup destination.

**Using Native SBT Libraries for SBT Channel Configuration**

While configuring the RMAN SBT channel, use the `SBT_LIBRARY` parameter to specify the media library that enables RMAN to communicate with the cloud backup module.

Starting in Oracle Database 19c Release Update version 27 (19.27), Oracle provides native SBT libraries for RMAN backup and recovery operations with cloud storage. The native SBT library files are available in the Oracle home directory as part of the Oracle Database installation. When you configure an SBT channel, use the `SBT_LIBRARY` parameter to specify the absolute path to the native SBT library file located in the Oracle home directory. Oracle recommends that you use the native SBT libraries instead of downloading the library while installing the cloud backup module.

Starting in Oracle Database 19c Release Update version 28 (19.28), each native SBT library has a predefined alias name. For example, `oracle.oci` is the SBT library alias used for Oracle Cloud backups. `oracle.azure` is the SBT library alias used for backups to Microsoft Azure Blob Storage.

When you define the `SBT_LIBRARY` parameter, you can either specify the native SBT library alias (recommended) or provide the absolute path to the library file located in the Oracle home directory. See [Oracle Database Cloud Backup Modules and RMAN SBT Libraries](rman-backup-cloud.md) for the SBT library alias name that corresponds to each cloud backup module.

**Note:** For Oracle Database 19c Release Update version 26 (19.26) and earlier versions, download the operating system-specific cloud backup modules from [My Oracle Support Patch Number 37855779](https://support.oracle.com/epmos/faces/ui/patch/PatchDetail.jspx?patchId=37855779). Run the backup module installer to set up the authentication required for RMAN to access the cloud storage. You must use the SBT library included with the patch instead of downloading the library while running the installer.

**Specifying the Backup Module Configuration File Required for SBT Channel Operations**

The backup module installer creates the configuration file that contains the parameters required to authenticate RMAN operations with the chosen cloud service.

The configuration file name format is `<backup module prefix><ORACLE_SID>.ora`, where `ORACLE_SID` is the system identifier of the Oracle Database being backed up to a cloud storage. For example, `osbwsHRDB.ora` is a configuration file name where `osbws` is the prefix for Oracle Database Cloud Backup for Amazon S3, and `HRDB` is the unique identifier of the target database.

This example shows the contents of a sample configuration file `osbwsHRDB.ora` created by the Oracle Database Cloud Backup for Amazon S3 installer.

```md
OSB_WS_HOST=www-proxy.example.com,
OSB_WS_PROXY=www-proxy.example.com:80,
OSB_WS_WALLET='location=file:/myfiles/osbws_wallet',
CREDENTIAL_ALIAS=example-a_aws,
OSB_WS_BUCKET=HRDBBackups
```

The default location of the configuration file is `$ORACLE_HOME/dbs` on UNIX and Linux systems, and `%ORACLE_HOME%\database` on Windows systems.

When you configure the SBT channel, use the `ENV` parameter (on UNIX and Linux) or the `SBT_PARMS` parameter (on Windows) to specify the location of the backup module configuration file.

```md
RMAN> CONFIGURE CHANNEL DEVICE TYPE 'SBT'
PARMS 'SBT_LIBRARY=<SBT library alias>,
ENV=(<backup module prefix>_PFILE=<absolute path of configuration file>)';
```

In this example, the `SBT_PARMS` parameter specifies the location of the configuration file `osbwsHRDB.ora`.

```md
RMAN> CONFIGURE CHANNEL DEVICE TYPE 'SBT'
PARMS 'SBT_LIBRARY=oracle.osbws,
ENV=(OSB_WS_PFILE=/myfiles/osbswsHRDB.ora)';
```

**Note:**

To avoid backing up the configuration file, Oracle recommends that you copy and paste the contents of the configuration file instead of providing the location of the file, as shown in this example.

```md
RMAN> CONFIGURE CHANNEL DEVICE TYPE 'SBT'
PARMS 'SBT_LIBRARY=oracle.osbws,
SBT_PARMS=(OSB_WS_HOST=www-proxy.example.com,
OSB_WS_PROXY=www-proxy.example.com:80,
OSB_WS_WALLET='location=file:/myfiles/osbws_wallet',
CREDENTIAL_ALIAS=example-a_aws,
OSB_WS_BUCKET=DBbackups)';
```

**Persistent RMAN Configuration for Cloud Backup and Restores**

Use the [CONFIGURE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/bradv&id=RCMRF-GUID-B5094E73-C26C-4FED-AE39-8C2E9540050A) command to change the RMAN default device type to `SBT`. This ensures that the RMAN environment is configured to create all backups to cloud by default. The backup destination is determined by the SBT channel that is currently in use.

This command configures an automatic SBT channel using the SBT library alias. The `ENV` environment variable defines the backup module specific parameter (such as `OPC_PFILE` for OCI and `AZ_PFILE` for Azure) to indicate the location of the configuration file.

```md
RMAN> CONFIGURE CHANNEL DEVICE TYPE 'SBT'
PARMS 'SBT_LIBRARY=<SBT library alias>,
ENV=(<backup module prefix>_PFILE=absolute path of configuration file)';
```

This command configures an SBT channel using the absolute path of the SBT library file located in the Oracle home directory. The `ENV` parameter defines the configuration file.

```md
RMAN> CONFIGURE CHANNEL DEVICE TYPE 'SBT'
PARMS 'SBT_LIBRARY=<SBT library file pathname>,
ENV=(<backup module prefix>_PFILE=absolute path of configuration file)';
```

**Note:**

You can skip the `ENV` parameter or the `SBT_PARMS` parameter if the configuration file is created in the default directory chosen by the backup module installer.

```md
RMAN> CONFIGURE CHANNEL DEVICE TYPE 'SBT'
PARMS 'SBT_LIBRARY=<SBT library file alias/pathname>';
```

This command modifies the RMAN default device type to ‘SBT’.

```md
RMAN> CONFIGURE DEFAULT DEVICE TYPE TO sbt;
```

You can configure multiple SBT channels. The default cloud backup destination is determined by the RMAN SBT device configuration that is currently in use. For example, if the SBT device type is configured to use the `oracle.oci` library, then RMAN creates backups to Oracle Cloud Infrastructure Object Storage. To back up to a different location, such as Microsoft Azure Blob Storage, you can configure a separate SBT channel that corresponds to the `oracle.azure` SBT library.

**Note:**

An automatic SBT channel creates a persistent default SBT device setting that applies to all backup and recovery operations. Alternatively, you can use the `ALLOCATE CHANNEL` command to manually allocate a one-time SBT channel before each backup or restore operation. This command shows a manually allocated SBT channel (on UNIX and Linux systems) for creating a backup to Oracle Cloud.

```md
RMAN> RUN
{
ALLOCATE CHANNEL c1 DEVICE TYPE sbt
PARMS 'SBT_LIBRARY=oracle.oci,
ENV=(OPC_PFILE=/myfiles/opc<ORACLE_SID>.ora)';
BACKUP DATABASE;
}
```

See [Configuring Channels](configuring-rman-client-basic.md) for detailed information about RMAN channels.

**Configuring an Automatic SBT Channel for Oracle Cloud (OCI)**

```md
RMAN> CONFIGURE CHANNEL DEVICE TYPE 'SBT'
PARMS 'SBT_LIBRARY=oracle.oci,
ENV=(OPC_PFILE=/myfiles/opc<ORACLE_SID>.ora)';
```

You can optionally specify the native SBT library path instead of the library alias, as shown below.

```md
RMAN> CONFIGURE CHANNEL DEVICE TYPE 'SBT'
PARMS 'SBT_LIBRARY=$ORACLE_HOME/lib/libopc.so,
ENV=(OPC_PFILE=/myfiles/opc<ORACLE_SID>.ora)';
```

```md
RMAN> CONFIGURE CHANNEL DEVICE TYPE 'SBT'
PARMS 'SBT_LIBRARY=oracle.oci,
SBT_PARMS=(OPC_PFILE=C:\myfiles\opc<ORACLE_SID>.ora)';
```

You can optionally specify the native SBT library path instead of the library alias, as shown below.

```md
RMAN> CONFIGURE CHANNEL DEVICE TYPE 'SBT'
PARMS 'SBT_LIBRARY=%ORACLE_HOME%\bin\oraopc.dll,
SBT_PARMS=(OPC_PFILE=C:\myfiles\opc<ORACLE_SID>.ora)';
```

**Configuring an Automatic SBT Channel for Microsoft Azure Blob Storage**

```md
RMAN> CONFIGURE CHANNEL DEVICE TYPE 'SBT'
PARMS 'SBT_LIBRARY=oracle.azure,
ENV=(AZ_PFILE=/myfiles/az<ORACLE_SID>.ora)';
```

You can optionally specify the native SBT library path instead of the library alias, as shown below.

```md
RMAN> CONFIGURE CHANNEL DEVICE TYPE 'SBT'
PARMS 'SBT_LIBRARY=$ORACLE_HOME/lib/libaz.so,
ENV=(AZ_PFILE=/myfiles/az<ORACLE_SID>.ora)';
```

```md
RMAN> CONFIGURE CHANNEL DEVICE TYPE 'SBT'
PARMS 'SBT_LIBRARY=oracle.azure,
SBT_PARMS=(AZ_PFILE=C:\myfiles\az<ORACLE_SID>.ora)';
```

You can optionally specify the native SBT library path instead of the library alias, as shown below.

```md
RMAN> CONFIGURE CHANNEL DEVICE TYPE 'SBT'
PARMS 'SBT_LIBRARY=%ORACLE_HOME%\bin\oraaz.dll,
SBT_PARMS=(AZ_PFILE=C:\myfiles\az<ORACLE_SID>.ora)';
```

**Configuring an Automatic SBT channel for Amazon S3 Cloud (AWS)**

```md
RMAN> CONFIGURE CHANNEL DEVICE TYPE 'SBT'
PARMS 'SBT_LIBRARY=oracle.osbws,
ENV=(OSB_WS_PFILE=/myfiles/osbsws<ORACLE_SID>.ora)';
```

You can optionally specify the native SBT library path instead of the library alias, as shown below.

```md
RMAN> CONFIGURE CHANNEL DEVICE TYPE 'SBT'
PARMS 'SBT_LIBRARY=$ORACLE_HOME/lib/libosbws.so,
ENV=(OSB_WS_PFILE=/myfiles/osbsws<ORACLE_SID>.ora)';
```

```md
RMAN> CONFIGURE CHANNEL DEVICE TYPE 'SBT'
PARMS 'SBT_LIBRARY=oracle.osbws,
SBT_PARMS=(OSB_WS_PFILE=C:\myfiles\osbsws<ORACLE_SID>.ora)';
```

You can optionally specify the native SBT library path instead of the library alias, as shown below.

```md
RMAN> CONFIGURE CHANNEL DEVICE TYPE 'SBT'
PARMS 'SBT_LIBRARY=%ORACLE_HOME%\bin\oraosbws.dll,
SBT_PARMS=(OSB_WS_PFILE=C:\myfiles\osbsws<ORACLE_SID>.ora)';
```

**Related Topics**

- [Oracle Database Cloud Backup Modules and RMAN SBT Libraries](rman-backup-cloud.md)
- [Configuring the Default Device for Backups: Disk or SBT](configuring-rman-client-basic.md)
- [RMAN Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/bradv&id=RCMRF-GUID-B5094E73-C26C-4FED-AE39-8C2E9540050A)

## About Securing Cloud Backups

To ensure backup security and data protection, Oracle recommends that you make RMAN backup encryption a standard part of your backup processes.

RMAN backup encryption provides enhanced security for your database backups, particularly if you are storing critical backup data on a cloud storage location. Encrypting RMAN backups can also assist you in meeting key audit and regulatory compliance requirements for the data of your organization.

You can use the `CONFIGURE` command to create persistent encryption settings for your RMAN backups.

**Note:** Backups must be encrypted before they can be sent to Oracle Cloud using Oracle Database Backup Cloud Service. If a backup is not encrypted, then RMAN signals `ORA-19511` with a descriptive error message as shown below.

```md
RMAN-03009: failure of backup command on ORA_SBT_TAPE_1 channel at 08/15/2014 14:00:43
ORA-27030: skgfwrt: sbtwrite2 returned error
ORA-19511: non RMAN, but media manager or vendor specific failure, error text:
   KBHS-01602: backup piece 14p0jso8_1_1 is not encrypted
```

See [Configuring Backup Encryption](configuring-rman-client-advanced.md) for information about encryption methodologies and choosing an encryption algorithm.

## Configuring Compression for Cloud Backups

You can optionally use compression when backing up Oracle Databases to cloud. Compression conserves bandwidth by reducing the size of your backups before they are sent to the cloud. You can specify compression when you perform a backup.

Recovery Manager (RMAN) supports binary compression using one of the following compression levels: `HIGH`, `MEDIUM`, `BASIC`, and `LOW`. The recommended level for cloud backups is `MEDIUM`.

For example, the following RMAN commands configure compression using the `MEDIUM` algorithm:

```md
RMAN> CONFIGURE COMPRESSION ALGORITHM 'MEDIUM';
RMAN> CONFIGURE DEVICE TYPE sbt BACKUP TYPE TO COMPRESSED BACKUPSET;
```

Backups must be in the form of backup sets, not image copies. For information about configuring compression for backups, see [Configuring Compression Options](configuring-rman-client-advanced.md).

## Configuring Autobackups

Oracle recommends that you configure RMAN to automatically back up the database control file and server parameter file.

With a control file autobackup, RMAN can recover the database even if the current control file, recovery catalog, and server parameter file are inaccessible.

The autobackup feature is disabled by default. Use the `CONFIGURE` command to enable autobackup.

```md
RMAN> CONFIGURE CONTROLFILE AUTOBACKUP ON;
```

See [Configuring Control File and Server Parameter File Autobackups](configuring-rman-client-basic.md) for information about autobackups.

## Best Practices to Optimize Cloud Backup Rates

Because cloud backups are sent over the public internet, backup performance is affected by network bandwidth limitations. Use RMAN parallelism and compression to speed up cloud backups and restores.

To optimize performance:

- Use multiple RMAN channels for higher parallelism, which results in full utilization of the network. You can configure as many RMAN channels as you want. For example, the following configuration uses eight channels in parallel to back up to the cloud:
	```md
	RMAN> CONFIGURE DEVICE TYPE sbt PARALLELISM 8;
	```
	Try increasing the parallelism until you find the optimal transfer rate.
- Use an RMAN compression level of MEDIUM.
- Use multisection backups. With these, multiple RMAN channels are used in parallel to back up large data files in separate sections.
	You create multisection backups by specifying the `SECTION SIZE` parameter with the `BACKUP` command. For example, the following command specifies a backup section size of 1 GB:
	```md
	RMAN> BACKUP DEVICE TYPE sbt DATABASE SECTION SIZE 1g;
	```
- Use a backup strategy of weekly full and daily incremental backups. This results in faster backups and could save a significant amount of network bandwidth. Use the RMAN fast incremental backup feature (based on block change tracking) to optimize the performance of your daily incremental backups.
- Also note it is recommended practice to include the RMAN format string `%d` and `%U` to ensure uniqueness of each backup piece.
- Use a recovery catalog to store long-term backups. For information about recovery catalogs, see [Managing a Recovery Catalog](managing-recovery-catalog.md).

**Note:** You can test network throughput by using the throughput measurement tool. See [Testing Network Throughput](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/bradv&id=MMOCS-GUID-5B8E1D7D-76EF-467C-9A82-592798D195F3) in *Managing and Monitoring Oracle Cloud*.

## Best Practices for Cloud Restores

Recovery best practices ensure that, in the event of a failure, the cloud backups required to recover your Oracle Database are available and usable.

Use the following recovery best practices:

- Verify that the cloud backups are restorable.
	Before creating new cloud backups, run the `RESTORE DATABASE PREVIEW VALIDATE HEADER` command to ensure that the old backups are available and restorable.
- Validate backups to check for physical and logical corruptions.
	Use the RMAN `RESTORE DATABASE VALIDATE` command to check the data files for physical corruptions. Run the `RESTORE DATABASE VALIDATE` `CHECK LOGICAL` command to check for logical corruptions.
- Crosscheck your backups periodically.
	If you use non-RMAN techniques for your cloud backups, then ensure to run the RMAN `CROSSCHECK BACKUP` command to crosscheck the backups before restoring.

**Related Topics**