---
title: Backing Up an Oracle Database to Cloud
book: Backup and Recovery User Guide
doc_id: E96241-26
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/rman-backup-cloud.html
tags:
  - oracle
  - 19c
  - backup-and-recovery-users-guide
---

Using an off-site storage location, such as public cloud, can be an important part of your Oracle Database backup strategy. Cloud backups are always accessible over the Internet and are immediately available for recovery purposes when needed.

## About Using RMAN to Backup an On-Premises Oracle Database to Cloud

RMAN can backup directly to Oracle Cloud, Microsoft Azure Blob Storage, and Amazon Web Services. Obtain a subscription to the preferred cloud storage provider and then configure RMAN to directly backup to the cloud storage destination.

The Oracle Database Cloud Backup module is an Oracle-supplied media management software that enables RMAN to directly backup and restore with a cloud service. Starting with Oracle Database 19c Release Update version 27 (19.27), the backup module installer files are available in the Oracle home directory after you install the Oracle Database.

On the target database server, install the Oracle Database Cloud Backup Module that corresponds to your preferred cloud backup destination. For example, to backup your Oracle Database to Azure Blob Storage, you must set up the Oracle Database Cloud Backup Module for Azure on the target database server.

RMAN uses the SBT (tape) channel to create backups on cloud storage. When you configure an SBT channel, you must also specify the SBT library that corresponds with a cloud backup module.

Starting with Oracle Database 19c Release Update version 28 (19.28), each SBT library has a predefined alias name. For example, `oracle.azure` is the SBT library for Azure Blob Storage. You can either specify the native SBT library alias (recommended) or provide the absolute path to the library file located in the Oracle home directory.

**Note:** For Oracle Database 19c Release Update version 26 (19.26) and earlier versions, download the operating system-specific cloud backup modules from [My Oracle Support Patch Number 37855779](https://support.oracle.com/epmos/faces/ui/patch/PatchDetail.jspx?patchId=37855779). Run the backup module installer to set up the authentication required for RMAN to access the cloud storage. You must use the SBT library included with the patch instead of downloading the library while running the installer.

After you install the backup module and configure the SBT channels, you can use the RMAN utility to perform backup and restores with the chosen cloud backup destination.

These are the high-level steps to set up RMAN for cloud backup and restores.

1. Obtain a subscription to the preferred cloud storage service. You must have an active account and credentials associated with the chosen cloud service.
	RMAN supports backups and restores with these popular cloud services:
	- Oracle Cloud Infrastructure (OCI) Object Storage
		- Oracle Cloud Infrastructure (OCI) Object Storage Service with Swift APIs
		- Microsoft Azure Blob Storage
		- Amazon Simple Storage Service (S3)
2. Install the Oracle Database Cloud Backup Module on the target database server.
	The backup module installer files are available in the Oracle home directory as part of the database installation.
3. Configure an RMAN SBT (tape) channel and specify the SBT library for backup and restore operations with the chosen cloud service.
4. Use RMAN to directly backup and restore to cloud.

## Oracle Database Cloud Backup Modules and RMAN SBT Libraries

To create backups to cloud, you must install or setup the Oracle Database Cloud Backup Module, and then configure an RMAN SBT channel using the relevant SBT Library.

***Table 29-1 Oracle Database Cloud Backup Modules and RMAN SBT Library Matrix***

| To Store Backups in | Install/Setup | Using the Installer File/Setup Tool | SBT\_LIBRARY |
| --- | --- | --- | --- |
| Oracle Cloud Infrastructure Object Storage | [Oracle Database Cloud Backup Module for OCI](backup-cloud-oci.md) | `oci_installer.zip` | `oracle.oci` |
| Oracle Cloud Infrastructure Object Storage Service with Swift APIs | [Oracle Database Cloud Backup Module for OCI Classic](backup-cloud-oci.md) | `opc_installer.zip` | `oracle.oci` |
| Microsoft Azure Blob Storage | [Oracle Database Cloud Backup Module for Azure](azure-sbt-module.md) | `az_setup.zip` | `oracle.azure` |
| Amazon Simple Storage Service (S3) (AWS) | [Oracle Database Cloud Backup for Amazon S3](backup-cloud-osb.md) | `osbws_installer.zip` | `oracle.osbws` |

## Typical Workflow to Configure RMAN for Cloud Backups

Refer this workflow to set up RMAN for cloud backup and restores.

***Table 29-2 Task Workflow to Set Up RMAN for Cloud Backups and Restores***

| Step | Description | More Information |
| --- | --- | --- |
| Obtain a cloud service account | Create an account with the chosen cloud service provider: Oracle Cloud (OCI), Microsoft Azure Blob Storage, or Amazon S3 (AWS).  The cloud service account details are required to authenticate RMAN operations with the chosen cloud service. | - [Request Trial or Paid Subscription to Oracle Database Backup Cloud Service](backup-cloud-oci.md) - [Sign-up for a Microsoft Azure Blob Storage Account](azure-sbt-module.md) - [Sign-up for an Amazon S3 - AWS Account](backup-cloud-osb.md) |
| Verify the prerequisites | Review the supported Oracle Database version and the requirements specific to each cloud backup module. | - [Software Prerequisites for Oracle Database Backup Cloud Service](backup-cloud-oci.md) - [Prerequisites for the Oracle Database Cloud Backup Module for Azure](azure-sbt-module.md) - [Prerequisites for Oracle Database Cloud Backup for Amazon S3](backup-cloud-osb.md) |
| Install or setup the required Oracle Database Cloud Backup Module. | Access the Oracle Database Cloud Backup Module installer files from the Oracle home directory of the target database. | - [Installing the Oracle Database Cloud Backup Module for OCI](backup-cloud-oci.md) - [Installing the Oracle Database Cloud Backup Module for OCI Classic](backup-cloud-oci.md) - [Set Up the Oracle Database Cloud Backup Module for Azure](azure-sbt-module.md) - [Installing Oracle Database Cloud Backup for Amazon S3](backup-cloud-osb.md) |
| Configure the RMAN environment to create persistent settings for cloud backup and restores. | Use the RMAN `CONFIGURE` command to create an automatic SBT channel for RMAN cloud backup and restore operations. Configure SBT as the default device type to directly send all backups to the configured cloud destination. | - [Configuring SBT Channel for Oracle Cloud (OCI)](backup-cloud-oci.md) - [Configuring SBT Channel for Azure Storage](azure-sbt-module.md) - [Configuring SBT Channel for Amazon S3](backup-cloud-osb.md) |
| Configure RMAN Encryption | Configure RMAN encryption. Oracle recommends that you encrypt the RMAN database backups before they can be sent to the cloud. | - [About Securing Cloud Backups](rman-cloud-settings.md) |
| Configure RMAN Compression (optional) | Configure compression to reduce the size of RMAN database backups before they are sent to the cloud. | - [Configuring Compression for Cloud Backups](rman-cloud-settings.md) |
| Perform Cloud Backup and Recovery operations using RMAN | Connect RMAN to the target Oracle Database. Use RMAN commands to create a backup to cloud and restore backups from cloud. | - [Backing Up to Oracle Database Backup Cloud Service](backup-cloud-oci.md) - [Backup and Restore with Azure Storage Using RMAN](azure-sbt-module.md) - [Backup and Recover with Amazon S3 Cloud](backup-cloud-osb.md) |

## Management Interfaces for Cloud Backups

You can use any of the following options to manage cloud backup operations.

- RMAN interface
	Use the RMAN command-line interface to run familiar commands and perform backups on demand. You can also create automated backup jobs using the cron utility.
- Oracle Enterprise Manager Cloud Control
	Use Oracle Enterprise Manager Cloud Control to configure the backup module and perform backup and recovery operations.
- Third-party tools
	Use third-party tools such as CloudBerry Lab’s cloud backup solution. See [`https://www.cloudberrylab.com/backup.aspx`](https://www.cloudberrylab.com/backup.aspx).