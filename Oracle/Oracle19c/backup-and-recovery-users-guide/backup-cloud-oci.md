---
title: Oracle Database Backup Cloud Service
book: Backup and Recovery User Guide
doc_id: E96241-26
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/backup-cloud-oci.html
tags:
  - oracle
  - 19c
  - backup-and-recovery-users-guide
---

Oracle Database Backup Cloud Service is a secure, scalable, on-demand storage solution for backing up Oracle Databases to Oracle Cloud. The service complements your existing backup strategy by providing an off-site storage location in the public cloud.

## About Oracle Database Backup Cloud Service

Oracle Database Backup Cloud Service is a secure, scalable, on-demand storage solution for backing up Oracle databases to Oracle Cloud. The service complements your existing backup strategy by providing an off-site storage location in the public cloud.

**Note:** The information provided in this section applies to Oracle Database 19c Release Update version 27 (19.27) and later releases. For Oracle Database 19c Release Update version 26 (19.26) and earlier versions, Oracle recommends that you use the procedures described in the [Using Oracle Database Backup Cloud Service](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/bradv&id=CSDBB-GUID-AF5723AC-3A75-41CB-A760-2B16B9E699C6) guide.

To use Oracle Database Backup Cloud Service you must subscribe to the service, install the Oracle Database Cloud Backup Module, and then configure your environment to send backups to the cloud. You can then use familiar Recovery Manager (RMAN) commands to perform backup, restore, recovery, and maintenance operations. You can also use other tools for your cloud backups.

With Oracle Database Backup Cloud Service, cloud backups are always accessible over the Internet and are immediately available for recovery when needed. Data is replicated across multiple storage nodes, which protects against hardware failure and data corruption.

Oracle Database Backup Cloud Service is used to store Oracle Database backups only. To store other types of data, use Oracle Cloud Infrastructure Object Storage.

For more information, see:

- [How to Begin with Database Cloud Service Subscriptions](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/bradv&id=CSDBI-GUID-7D1DA798-97DB-4305-8853-C84DEBC29F31) in *Using Oracle Database Cloud Service*.
- [Backing Up and Restoring Databases on Database Cloud Service](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/bradv&id=CSDBI3342) in *Using Oracle Database Cloud Service*.

## About Backup and Recovery Using Oracle Database Backup Cloud Service

Oracle Databases can be backed to Oracle Cloud using Oracle Database Backup Cloud Service. You can use RMAN to perform database restore and recovery using the backups stored in Oracle Cloud.

Oracle Database Backup Cloud Service can perform backup and recovery with the following:

- Oracle Cloud Infrastructure
	To create backups to Oracle Cloud Infrastructure, you must have a subscription to an Oracle Cloud Service and install the Oracle Database Cloud Backup Module for OCI. You can access the backup module installer file `oci_installer.zip` from the Oracle home directory.
- Oracle Cloud Infrastructure Object Storage Service with Swift APIs
	To create backups to Oracle Cloud Infrastructure Object Storage Service with Swift APIs, you must have a subscription to an Oracle Cloud Service and install the Oracle Database Cloud Backup Module for OCI Classic. You can access the backup module installer file `opc_installer.zip` from the Oracle home directory.

**Oracle Database Optimizations Supported by Oracle Database Backup Cloud Service**

Oracle Database Backup Cloud Service supports the following Oracle Database optimizations:

- RMAN backup encryption
	Using RMAN encryption, your data is encrypted at the source, securely transmitted to the cloud, and securely stored in the cloud. The keys are kept at your site, not in the cloud.
- All RMAN backup compression algorithms
	Using RMAN backup compression, you can conserve bandwidth and improve performance by reducing the size of backups before the backups are sent to the cloud for storage.

For licensing information about these optimizations, see [Oracle Database Backup Cloud Service](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/bradv&id=DBLIC-GUID-75262092-CD86-4B30-A21B-92ECC1C2E130) in the *Oracle Database Licensing Information User Manual*.

## About the Oracle Database Cloud Backup Module for OCI

The Oracle Database Cloud Backup Module for OCI makes it possible to perform backups and restores with Oracle Cloud Infrastructure. Backups are stored in Oracle Cloud Infrastructure Object Storage.

Oracle Database Cloud Backup Module for OCI is a system backup to tape (SBT) interface that is integrated with Recovery Manager (RMAN). You can use standard RMAN commands to perform backup, restore, recovery, and maintenance operations.

Install the Oracle Database Cloud Backup Module for OCI using the `oci_installer.zip` file located in the Oracle home directory. Install the backup module on the target database server. Multiple database versions and operating systems are supported.

Installing and using the module requires your Oracle Cloud credentials. After the module is installed, the authentication keys are stored securely in the Oracle wallet and are used to authenticate the backup module operations with Oracle Cloud Infrastructure Object Storage.

**Related Topics**

- Installing the Oracle Database Cloud Backup Module for OCI

## About the Oracle Database Cloud Backup Module for OCI Classic

The Oracle Database Cloud Backup Module for OCI Classic makes it possible to perform cloud backups and restores with Oracle Cloud Infrastructure (OCI) Object Storage Service with Swift API (previously called OCI Object Storage Classic).

Oracle Database Cloud Backup Module for OCI Classic is a system backup to tape (SBT) interface that is tightly integrated with Recovery Manager (RMAN), which means you do not need to learn new tools or commands. You can continue to use standard RMAN commands for all backup, restore, recovery, and maintenance operations.

You must install the Oracle Database Cloud Backup Module for OCI Classic using the `opc_installer.zip` file located in the Oracle home directory. Install the backup module on the target database server. Multiple database versions and operating systems are supported.

**Related Topics**

- Installing the Oracle Database Cloud Backup Module for OCI Classic

## Important Information About Oracle Database Backup Cloud Service Subscriptions

When you request a trial of Oracle Database Backup Cloud Service, you actually get a trial of Oracle Storage Cloud Service. Oracle Database Backup Cloud Service uses Oracle Storage Cloud Service to store cloud backups.

To try Oracle Database Backup Cloud Service, visit [Oracle Cloud Infrastructure (OCI)](https://www.oracle.com/cloud/) and click **Try OCI for free**.

For trials and paid subscriptions to Oracle Database Backup Cloud Service, the service is listed as Oracle Storage Cloud Service in Cloud Portal. Email from Oracle references Oracle Storage Cloud Service.

## Request Trial or Paid Subscription to Oracle Database Backup Cloud Service

Learn how to get started with Oracle Database Backup Cloud Service subscriptions.

1. Request a trial or purchase a subscription to Oracle Database Backup Cloud Service using any of these methods:
	- Request a trial subscription to Oracle Database Backup Cloud Service. Visit [Oracle Cloud Infrastructure (OCI)](https://www.oracle.com/cloud/) and click **Try OCI for free**.
		- Purchase a paid subscription to Oracle Database Backup Cloud Service. See [Buy a Nonmetered Subscription to an Oracle Cloud Service](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/bradv&id=CSGSG-GUID-555489F1-B03A-4C45-8810-26D46116CD03) in *Getting Started with Oracle Cloud* or [How Do I Sign Up?](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/bradv&id=CSGSG-GUID-6B820F62-A02B-485F-BE1A-AB84ED9EDE66) in *Getting Started with Oracle Cloud* for information about universal credits.
	Oracle Database Backup Cloud Service trials and paid subscriptions appear as Oracle Storage Cloud Service subscriptions. See Important Information About Oracle Database Backup Cloud Service Subscriptions.
2. Activate and verify the service. See [Activate Your Order](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/bradv&id=CSGSG-GUID-768DDA2A-33DA-4DD0-8C89-08AB7E742571) in *Getting Started with Oracle Cloud*.
3. Verify activation. See [Verify That Your Services are Ready](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/bradv&id=CSGSG-GUID-8295D8CB-690D-4B99-893F-CF9811FF9E72) in *Getting Started with Oracle Cloud*.
4. **Important:** Select a data center for your service. See, *Using Oracle Cloud Infrastructure Object Storage Classic*.
	You do not need to create a storage container as mentioned in the procedure. A default storage container is created for you automatically when you install the backup module used by Oracle Database Backup Cloud Service.
	If you enable georeplication, you will be billed for the capacity utilized in both the source and target data centers.
	The replication policy must be set before you run the backup module installer. Otherwise you’ll get errors such as `Could not authenticate to Oracle Database Cloud Backup Module` or `403 Forbidden`. Set the replication policy and wait at least 10 minutes for synchronization to complete before you retry the installation.
5. Create accounts for your users and assign them appropriate privileges and roles. See [Managing User Accounts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/bradv&id=CSGSG177) and [Managing User Roles](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/bradv&id=CSGSG193) in *Managing and Monitoring Oracle Cloud*.
	**Note:** For Oracle Database Public Cloud Services subscriptions, users must have either the Storage Administrator or Database Backup Administrator role to back up to the cloud.

**Note:** For answers to frequently asked questions (FAQs) about the Oracle Database Backup Cloud Service, see [My Oracle Support Note 1640149.1](https://support.oracle.com/epmos/faces/DocContentDisplay?id=1640149.1).

## Software Prerequisites for Oracle Database Backup Cloud Service

Verify these minimum requirements before installing the Oracle Database Backup Cloud Service.

The following table lists the supported database versions, operating systems, and prerequisites for operations with Oracle Cloud Infrastructure and Oracle Cloud Infrastructure Object Storage Service with Swift APIs. You can also review the Recovery Manager (RMAN) compression and encryption options.

***Table 31-1 Supported Oracle Database Versions, Operating Systems, and RMAN Options for Oracle Database Cloud Backup Module for OCI and OCI Classic***

| System | Supported Versions |
| --- | --- |
| Oracle Database | Enterprise Edition: 11g Release 2 (11.2.0.4) and later  Standard Edition (SE, SE1, SE2): 11g Release 2 (11.2.0.4) and later  \* Unsupported Oracle Database versions are in deprecated mode. See [My Oracle Support Note 1640149.1](https://support.oracle.com/epmos/faces/DocContentDisplay?id=1640149.1) for the latest support matrix. |
| Oracle Database Backup Cloud Service subscription and account.  - Oracle Database Cloud Backup Module for OCI 	An Oracle Cloud account with access to Oracle Cloud Infrastructure Object Storage. 	Oracle Cloud Infrastructure API signing keys, tenant OCID, and user OCID. - Oracle Database Cloud Backup Module for OCI Classic 	An Oracle Database Backup Cloud Service account user name, password, and storage capacity. | - Oracle Database Cloud Backup Module for OCI 	See [Overview of Object Storage](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/objectstorageoverview.htm) in the Oracle Cloud Infrastructure Documentation. 	You may specify a compartment ID. However, if the compartment ID is not specified, the tenant ID is used as the compartment ID. See [Required Keys and OCIDs](https://docs.cloud.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm). - Oracle Database Cloud Backup Module for OCI Classic 	See Request Trial or Paid Subscription to Oracle Database Backup Cloud Service |
| Java SE Development Kit (JDK) | Default JDK version supported by the target Oracle Database release. |
| The required patch if you are using the Standard Edition of Oracle Database | See [My Oracle Support Note 1640149.1](https://support.oracle.com/epmos/faces/DocContentDisplay?id=1640149.1). |
| Values for the parameters required to run the Oracle Database Cloud Backup Module installer. | Review the mandatory parameters and compile their values before you run the installer.  - See Parameters to Run the Oracle Database Cloud Backup Module for OCI. - See Parameters to Run the Oracle Database Cloud Backup Module for OCI Classic Installer |
| RMAN compression | HIGH, MEDIUM, BASIC, LOW |
| RMAN encryption | Enterprise Edition: Password, Transparent Data Encryption (TDE), dual mode.  Standard Edition: Password, TDE, dual mode. Requires a patch.  See [My Oracle Support Note 1640149.1](https://support.oracle.com/epmos/faces/DocContentDisplay?id=1640149.1). |

**Note:**

- If your database server has multiple Oracle homes, then you must install the Oracle Database Cloud Backup Module for OCI into each `ORACLE_HOME`. Alternatively, you can copy the `opcSID.ora` configuration file to the other Oracle home locations assuming that you are using the same cloud credentials for backing up all the databases in the database server.
- Copy and rename the `opcSID.ora` file for each database instance you are backing up to the cloud, where `SID` matches the SID for the database instance.

## Installing the Oracle Database Cloud Backup Module for OCI

Before you back up to Oracle Cloud Infrastructure, you must install the Oracle Database Cloud Backup Module for OCI on the target database server.

The backup module installer file `oci_installer.zip` is available in the Oracle home directory after you install the Oracle Database.

***Table 31-2 Name and Location of the OCI Backup Module Installer File***

| Oracle Database Cloud Backup Module for OCI Installer File | Location on UNIX and Linux Systems | Location on Windows Systems |
| --- | --- | --- |
| `oci_installer.zip` | `$ORACLE_HOME/lib` | `%ORACLE_HOME%\lib` |

**Note:** For Oracle Database 19c Release Update version 26 (19.26) and earlier versions, download the operating system-specific cloud backup modules from [My Oracle Support Patch Number 37855779](https://support.oracle.com/epmos/faces/ui/patch/PatchDetail.jspx?patchId=37855779). Run the backup module installer to set up the authentication required for RMAN to access the cloud storage. You must use the SBT library included with the patch instead of downloading the library while running the installer.

### Parameters to Run the Oracle Database Cloud Backup Module for OCI

Review the mandatory parameters and compile their values before you run the Oracle Database Cloud Backup Module for OCI.

After you install the Oracle Database, the backup module installer file `oci_installer.zip` is available in the Oracle home directory (see Table 31-2).

Extract the `oci_installer.zip` file to a subdirectory of your choice. To preview the installation parameters, run this command from the subdirectory that contains the extracted installer files.

```md
$ java -jar oci_install.jar
```

The mandatory parameters include the host name for the Oracle Cloud Infrastructure account and the private key used to sign Oracle Cloud Infrastructure API requests. For example:

```md
java -jar oci_install.jar
-host https://objectstorage.us-phoenix-1.oraclecloud.com
-pvtKeyFile oci_private_key -pubFingerPrint oci_public_fingerprint
-uOCID user_ocid -tOCID tenancy_ocid
-walletDir /wallet_directory
```

***Example 31-1 Extracting the Oracle Database Cloud Backup Module for OCI and Previewing the Installation Parameters (on UNIX and Linux systems)***

In this example, extract the contents of the `oci_installer.zip` file to the `ocimodule` subdirectory.

```md
$ mkdir -p $ORACLE_HOME/lib/ocimodule
$ cd $ORACLE_HOME/lib/ocimodule
unzip -q $ORACLE_HOME/lib/oci_installer.zip
```

To preview the installation parameters, run this command from the `ocimodule` subdirectory that contains the extracted files.

```md
$ java -jar oci_install.jar
```

***Table 31-3 Parameters Required to Install the Oracle Database Cloud Backup Module for OCI***

| Parameter | Description | Required or Optional |
| --- | --- | --- |
| `-host` | End point of the Oracle Cloud Infrastructure account. For information about finding the Native Oracle Cloud Service Object Storage API endpoints for your account, see the [Object Storage FAQs](https://cloud.oracle.com/STORAGE/OBJECT-STORAGE/FAQ) in the Oracle Cloud Infrastructure documentation. | Required |
| `-pvtKeyFile` | File that contains the private key used to authenticate Oracle Cloud Infrastructure API requests. The key file must be in PEM format. See [Required Keys and OCIDs](https://docs.cloud.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm) in Oracle Cloud Infrastructure Documentation for information about generating API signing keys.  This private key is never transmitted outside of the computer where the installer is run. | Required |
| `-pubFingerPrint` | Finger print of the public key paired with the specified private key. The finger print tells Oracle Cloud Infrastructure which private and public key pair is used to authenticate the API requests | Required |
| `-tOCID` | Tenancy OCID for the Oracle Cloud Infrastructure account. See [Required Keys and OCIDs](https://docs.cloud.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm) in *Oracle Cloud Infrastructure Documentation* for information about obtaining the `tOCID` and `uOCID`. | Required |
| `-uOCID` | User OCID for the Oracle Cloud Infrastructure account. | Required |
| `-bucket` | Name of the bucket in which backups are stored. If this bucket does not exist, then the installer creates it.  When this parameter is omitted, a default bucket is automatically created to store backups.  If you want the Backup module to create backups to an immutable bucket, then skip the `-bucket` parameter. | Optional |
| `-immutable-bucket` | Name of the regulatory-compliant cloud bucket created by you to store immutable backups.  In Oracle Cloud Infrastructure Object Storage, an immutable bucket is a backup storage location governed by time-bound retention rules that protect backups from modification or deletion for a specified duration.  To create immutable backups using the Backup module, you must first create two buckets in Oracle Cloud Infrastructure Object Storage:  - Regulatory Compliance Bucket configured with retention rules and rule lock (if necessary). - Temporary Metadata Bucket with no retention rules or retention settings.  When you run the installer, skip the `-bucket` parameter and specify values for the `-immutable-bucket` and `-temp-metadata-bucket` parameters.  The temporary metadata bucket is used to store metadata and temporary files generated during a backup operation.  For information about Oracle Cloud Infrastructure Object Storage buckets and retention rules, see [Using Retention Rules to Preserve Data](https://docs.oracle.com/iaas/Content/Object/Tasks/usingretentionrules.htm) in Oracle Cloud Infrastructure documentation. | Optional  Specify this parameter if you want the Backup module to create backups to an immutable bucket instead of the default bucket. |
| `-temp-metadata-bucket` | Name of the bucket that contains metadata and temporary files associated with immutable backups. The backup module requires the temporary metadata bucket for backup operations.  Before you run the installer, create an Object Storage bucket with no retention rules or retention settings. Run the installer by specifying the bucket name in the `-temp-metadata-bucket` parameter.  For information about Oracle Cloud Infrastructure Object Storage buckets and retention rules, see [Using Retention Rules to Preserve Data](https://docs.oracle.com/iaas/Content/Object/Tasks/usingretentionrules.htm) in Oracle Cloud Infrastructure documentation. | Required, if you want the Backup module to create immutable backups and if you have specified a value for the `-immutable-bucket` parameter. |
| `-cOCID` | Resource compartment ID for the Oracle Cloud Infrastructure account. The default value is the tenancy OCID if not specified. | Optional |
| `-newRSAKeyPair` | Set up a new pair of public and private RSA keys for authentication. If specified, the installer generates a random RSA private and public key pair of 2048 bits and stores them in the specified Oracle wallet directory. | Optional |
| `-walletDir` | Directory in which Oracle Cloud Infrastructure Object Storage credentials are stored.  Suggested location on Linux and UNIX systems:  `$ORACLE_HOME/dbs/opc_wallet`  Suggested location on Windows systems:  `%ORACLE_HOME%\database\opc_wallet`  If the specified wallet directory does not exist (for example, `opc_wallet`), the installer creates it. | Required |
| `-updateWalletNoValidate` | Updates the wallet without verifying the target host connection.  If you have changed the OCI Object Storage account credentials and want to update the existing wallet, then rerun the installer by specifying the `updateWalletNoValidate` and `walletDir` parameters. The installer directly updates the wallet without validating the target host.  In this example, you run the installer with the `updateWalletNoValidate` parameter. `oracle/dbs/new_oci_wallet` specifies the location of the wallet which contains the changed credentials. The installer directly updates the wallet without validating the target host connection, as shown in the sample output.  `java -jar oci_install.jar`  `-walletDir /oracle/dbs/new_oci_wallet -updateWalletNoValidate`  `Oracle Database Cloud Backup Module Setup Tool, build MAIN_2026-06-12`  `Oracle Database Cloud Backup Module wallet updated in directory /oracle/dbs/new_oci_wallet`  `Skipping library download because option -libDir is not specified.` | Optional |
| `-configFile` | Specifies a custom file name and location for the backup module configuration file. For example: `` -configFile=`/myfiles/OCIconfig.ora` ``.  Skip the `-configFile` parameter if you want to create the configuration file in the default location chosen by the installer.  - Default location on UNIX and Linux systems: `$ORACLE_HOME/dbs` - Default location on Windows systems: `%ORACLE_HOME%\database`  The default name for the configuration file is `opcSID.ora`, where `SID` is the system identifier of the Oracle Database being backed up to Oracle Cloud Infrastructure Object Storage Service. | Optional |
| `-trustedCerts` | Comma-separated list of SSL certificates that must be added to the wallet. If the installer is unable to retrieve the certificates required for the SSL connection from local Java truststore, this SSL certificates specified by this parameter are imported. All SSL certificates must be in the PEM format. | Optional |
| `-import-all-trustcerts` | Import all X509 certificates from the Java truststore. | Optional |
| `-proxyHost` | HTTP proxy server host name | Optional |
| `-proxyPort` | HTTP proxy server port number | Optional |
| `-proxyId` | HTTP proxy server user name, if needed. | Optional |
| `-proxyPass` | HTTP proxy server password, if needed. | Optional |
| `-argFile` | Indicates that parameters should be read from the specified file. For example, a file named `arguments.txt` might contain the following:  `-opcID 'myAccount@myCompany.com' -opcPass 'abc123$' -host https://objectstorage.us-phoenix-1.oraclecloud.com -libDir /home/oracle/OPC/lib -walletDir /home/oracle/OPC/wallet`  For this example, the following command installs the Oracle Database Cloud Backup Module for OCI using the parameters specified in the file:  `java -jar oci_install.jar -argFile arguments.txt ` | Optional |
| `-enableArchiving` | Whether backups must be automatically moved from standard Object Storage buckets to Archive Storage. The default value is FALSE. Set this parameter to TRUE to enable automatic archival of backups.  Backups are automatically moved to Archive Storage if they meet the criteria set by the object lifecycle policy rule that is associated with the bucket containing the backups. The installer creates an appropriate lifecycle policy rule using the values of the `archiveAfterBackup` and `retainAfterRestore` parameters. Do not modify this policy rule.  To enable archiving of backups, the Object Storage service in the region must be granted permission to manage objects. See [Using Object Lifecycle Management](https://docs.cloud.oracle.com/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm) in the Oracle Cloud Infrastructure Documentation. | Optional |
| `-archiveAfterBackup` | Period of time, in days or years, after which backups are moved from standard Object Storage to Archive Storage. The default is 0 days. This means that the backups are moved to Archive Storage any time between 0 and 24 hours from the time they were created. Examples:  ```md -archiveAfterBackup "25 days" -archiveAfterBackup "1 year" ``` | Optional |
| `-retainAfterRestore` | Period of time, in hours, for which backups that were restored from Archive Storage to standard Object Storage are retained in the Object Storage bucket. The default is 48 hours. Example:  ```md -retainAfterRestore "24 hours" ```  While restoring using archived backups, the backups must first be recalled from Archive Storage. Recalled backups are retained in Object Storage for the time specified by `retainAfterRestore`. After the specified time elapses, the backups return to Archive Storage. | Optional |

### Run the Backup Module for OCI Installer

Use these steps to install the Oracle Database Cloud Backup Module for OCI on the target database server.

Before you begin, ensure that you have verified the prerequisites and compiled the parameter values required to run the Oracle Database Cloud Backup Module for OCI.

- Software Prerequisites for Oracle Database Backup Cloud Service
- Parameters to Run the Oracle Database Cloud Backup Module for OCI
1. The OCI Backup Module installer zip file `oci_installer.zip` is available in the Oracle home directory (see Table 31-2).
	Extract the `oci_installer.zip` file to a subdirectory of your choice. In this example, extract the installer files to the `ocimodule` subdirectory.
	```md
	$ mkdir -p $ORACLE_HOME/lib/ocimodule
	$ cd $ORACLE_HOME/lib/ocimodule
	unzip -q $ORACLE_HOME/lib/oci_installer.zip
	```
2. (Optional) To configure automatic movement of backups from standard Object Storage to Archive Storage, authorize the Object Storage service to move backups to Archive Storage.
	See *Service Permissions* in the [Required IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm#permissions) section of the Oracle Cloud Infrastructure documentation
3. Go to the directory where you have extracted the OCI Backup Module installer files. In this example, the `ocimodule` directory contains the `oci_install.jar` file and the README file `oci_readme.txt`.
	```md
	$ cd $ORACLE_HOME/lib/ocimodule
	```
4. Run the OCI Backup Module installer file: `oci_install.jar`. Specify the parameters and values as shown in this example.
	The following is an example run of the OCI Backup Module installer using sample parameter values.
	```md
	java -jar oci_install.jar -host https://objectstorage.us-ashburn-1.oraclecloud.com
	-bucket DBOCIbackups
	-pvtKeyFile /oracle/dbs/oci_wallet/oci_pvt
	-pubFingerPrint 2c:22:f3:v3:e2:2w:21:55:76:98:55:e7:65:bn:tg:98
	-tOCID ocid1.tenancy.oc1..aaaaaaaa754pijuwheaq67t7t7z7aibtusjxwxyv3gfa
	-uOCID ocid1.user.oc1..aaaaaaaap4fvkch3arjfdizhfigpiliifieyl6wn4yceelo6job2du7f4r4q
	-cOCID ocid1.compartment.oc1..aaaaaaaaxslrgbvo5gh7t5iljdmydfolgfygwdpnrq7vtt5cj4ksb3lvwu67
	-walletDir /oracle/dbs/oci_wallet
	```
	This sample output shows how the installer automatically creates a wallet that contains the Oracle Database Backup Cloud Service identifiers and credentials, and also creates the backup module configuration file `opc<ORACLE_SID>.ora`.
	```md
	Oracle Database Cloud Backup Module Setup Tool, build 23.8.0.25.04
	Oracle Database Cloud Backup Module credentials are valid.
	Backups would be sent to bucket DBOCIbackups.
	Oracle Database Cloud Backup Module wallet created in directory /oracle/dbs/oci_wallet.
	Oracle Database Cloud Backup Module initialization file oracle/dbs/opcsbt.ora created.
	Skipping library download because option -libDir is not specified.
	```

***Example 31-2 Enabling Automatic Archival of Backups When Installing the Oracle Database Cloud Backup Module for OCI***

This example installs the Oracle Database Cloud Backup Module for OCI and creates a standard bucket named `backup_archival_60`, with archiving enabled. Backups stored in this bucket are automatically moved from standard Object Storage to Archive Storage 60 days after they are created. During a restore operation, backups recalled from Archive Storage are retained in the Object Storage bucket for 72 hours. An object lifecycle policy is created and associated with the bucket `backup_archival_60`. The information specified in the `-archiveAfterBackup` and `-retainAfterRestore` parameters are stored in this object lifecycle policy.

Before you run the installer, ensure that you authorize the Object Storage service to move backups to Archive Storage, as described in Step 3.

```md
java -jar oci_install.jar -host https://objectstorage.us-ashburn-1.oraclecloud.com
-pvtKeyFile /oracle/dbs/oci_wallet/oci_pvt
-pubFingerPrint 2c:22:f3:v3:e2:2w:21:55:76:98:55:e7:65:bn:tg:98
-tOCID ocid1.tenancy.oc1..aaaaaaaa754pijuwheaq67t7t7z7aibtusjxwxyv3gfa
-uOCID ocid1.user.oc1..aaaaaaaap4fvkch3arjfdizhfigpiliifieyl6wn4yceelo6job2du7f4r4q
-cOCID ocid1.compartment.oc1..aaaaaaaaxslrgbvo5gh7t5iljdmydfolgfygwdpnrq7vtt5cj4ksb3lvwu67
-walletDir /oracle/dbs/oci_wallet
 -enableArchiving true
 -archiveAfterBackup "60 days" -retainAfterRestore "72 hours"
 -bucket backup_archival_60
 -configFile /oracle/dbs/oci_config.ora
```

Review the sample output.

```md
Oracle Database Cloud Backup Module Setup Tool, build MAIN_2025-02-28
Oracle Database Cloud Backup Module credentials are valid.
Backups would be sent to bucket backup_archival_60.
Oracle Database Cloud Backup Module wallet created in directory /oracle/dbs/oci_wallet.
Oracle Database Cloud Backup Module initialization file /oracle/dbs/oci_config.ora created.
Skipping library download because option -libDir is not specified.
```

### Files Created by the Oracle Database Cloud Backup Module for OCI Installer

After you run the installer for the Oracle Database Cloud Backup Module for OCI, ensure that the required files are created on the target database server.

***Table 31-4 Files Created By the Oracle Database Cloud Backup Module for OCI Installer***

| File | Location | Purpose |
| --- | --- | --- |
| `opcSID.ora` | As specified for the `-configFile` parameter when you run the installer for the Oracle Database Cloud Backup Module for OCI.  Default location on `UNIX` and Linux systems:  `$ORACLE_HOME/dbs`  Default location on Windows systems:  `%ORACLE_HOME%\database` | Configuration file that contains the Oracle Cloud Infrastructure Object Storage bucket URL and credential wallet location, where `SID` is the system identifier of the Oracle database being backed up to Oracle Cloud Infrastructure. |
| `cwallet.sso` | As specified for the `-walletDir` parameter when you run the Oracle Database Cloud Backup Module for OCI installer.  - Location on `UNIX` and Linux systems: 	`$ORACLE_HOME/dbs/opc_wallet` - Location on Windows systems: 	`%ORACLE_HOME%\database\opc_wallet` | Oracle wallet file that securely stores Oracle Cloud Infrastructure Object Storage credentials. This file is used during Recovery Manager (RMAN) backup and restore operations and is stored in the Oracle Cloud Infrastructure Object Storage wallet directory (for example, `opc_wallet`). |

## Installing the Oracle Database Cloud Backup Module for OCI Classic

Before you back up to Oracle Cloud Infrastructure Object Storage Service with Swift API, you must install the cloud backup module on the target database server.

The backup module installer file `opc_installer.zip` is available in the Oracle home directory after you install the Oracle Database.

***Table 31-5 File Name and Location of the Backup Module for OCI Classic Installer***

| Oracle Database Cloud Backup Module for OCI Classic Installer File Name | Location on UNIX and Linux Systems | Location on Windows Systems |
| --- | --- | --- |
| `opc_installer.zip` | `$ORACLE_HOME/lib` | `%ORACLE_HOME%\lib` |

**Note:** For Oracle Database 19c Release Update version 26 (19.26) and earlier versions, download the operating system-specific cloud backup modules from [My Oracle Support Patch Number 37855779](https://support.oracle.com/epmos/faces/ui/patch/PatchDetail.jspx?patchId=37855779). Run the backup module installer to set up the authentication required for RMAN to access the cloud storage. You must use the SBT library included with the patch instead of downloading the library while running the installer.

### Parameters to Run the Oracle Database Cloud Backup Module for OCI Classic Installer

Review the mandatory parameters and compile their values before installing the Oracle Database Cloud Backup Module for OCI Classic module. Parameters include host (REST endpoint) and account credentials.

After you install the Oracle Database, the Oracle Database Cloud Backup Module for OCI Classic zip file `opc_installer.zip` is available in the Oracle home directory.

Extract the `opc_installer.zip` file to a subdirectory of your choice. To preview the installation parameters, run this command from the subdirectory that contains the extracted files.

```md
$ java -jar opc_install.jar
```

***Example 31-3 Extracting the Oracle Database Cloud Backup Module for OCI Classic Installer Files and Previewing the Installation Parameters***

In this example, extract the contents of the `opc_installer.zip` file to the `OCIclassic` subdirectory.

```md
$ mkdir -p $ORACLE_HOME/lib/OCIclassic
$ cd $ORACLE_HOME/lib/OCIclassic
unzip -q $ORACLE_HOME/lib/opc_installer.zip
```

To preview the installation parameters, run this command from the `OCIclassic` subdirectory that contains the extracted installer files.

```md
$ java -jar opc_install.jar
```

***Table 31-6 Parameters used by the Oracle Database Cloud Backup Module for OCI Classic Installer***

| Parameter | Description | Required or Optional |
| --- | --- | --- |
| `-host` | REST endpoint for your service as listed on the service details page. For example:  `https://swiftobjectstorage.us-ashburn-1.oraclecloud.com/v1/hr-abc`  For information about finding the URL for your account, see the documentation for Using Oracle Cloud Infrastructure Object Storage Classic. | Required |
| `-opcId` | User name for your Oracle Database Backup Cloud Service account.  Enclose the user name in single quotes, for example `'myAccount@myCompany.com'`. On Windows systems, use double quotes if the user name contains special characters. | Required |
| `-opcPass` | Password for the Oracle Database Backup Cloud Service account specified by `-opcId`.  Enclose the password in single quotes, for example `'opc_password'`. On Windows systems, use double quotes if the password contains special characters. | Required |
| `-walletDir` | Directory in which Oracle Database Backup Cloud Service credentials are stored.  Suggested location on Linux and UNIX systems:  `$ORACLE_HOME/dbs/opc_wallet`  Suggested location on Windows systems:  `%ORACLE_HOME%\database\opc_wallet`  If the specified wallet directory does not exist (for example, `opc_wallet`), the installer creates it. | Required |
| `-updateWalletNoValidate` | Updates the wallet without verifying the target host connection.  If you have changed the Object Storage Service with Swift API account credentials and want to update the existing wallet, then rerun the installer by specifying the `updateWalletNoValidate` and `walletDir` parameters. The installer directly updates the wallet without validating the target host.  In this example, you run the installer with the `updateWalletNoValidate` parameter. `oracle/dbs/new_opc_wallet` specifies the location of the wallet which contains the changed credentials. The installer directly updates the wallet without validating the target host connection, as shown in the sample output.  `java -jar opc_install.jar -opcId "testuser" -opcPass "test" -walletDir oracle/dbs/new_opc_wallet -updateWalletNoValidate`  `Oracle Database Cloud Backup Module Setup Tool, build MAIN_2026-06-12`  `Oracle Database Cloud Backup Module wallet updated in directory oracle/dbs/new_opc_wallet`  `Skipping library download because option -libDir is not specified.` | Optional |
| `-container` | Custom container created by you, separate from Oracle Database Backup Cloud Service, to store backups. If omitted, backups are stored in the default container that's created when the backup module is installed. See Storing Backups in Custom Locations.  Note: Containers that are used by Recovery Manager (RMAN) cannot have server-side encryption enabled. Because RMAN backups are already encrypted at the client side, server-side encryption is not required.  If you want the Backup module to create backups to an immutable container, then skip the `-container` parameter. | Optional |
| `-immutable-container` | Name of the regulatory-compliant cloud container created by you to store immutable backups.  In Oracle Cloud Infrastructure Object Storage, an immutable container is a backup storage location governed by time-bound retention rules that protect backups from modification or deletion for a specified duration.  To create immutable backups using the Backup module, you must first create two containers in Oracle Cloud Infrastructure Object Storage:  - Regulatory Compliance Container configured with retention rules and rule lock (if necessary). - Temporary Metadata Container with no retention rules or retention settings.  When you run the installer, skip the `-container` parameter and specify values for the `-immutable-container` and `-temp-metadata-container` parameters.  The temporary metadata container is used to store metadata and temporary files generated during a backup operation. | Optional  Specify this parameter if you want the Backup module to create backups to an immutable container instead of the default container. The default container is created when you run the installer. |
| `-temp-metadata-container` | Name of the container that stores metadata and temporary files associated with immutable backups. The backup module requires the temporary metadata container for backup operations.  Before you run the installer, create an Object Storage container with no retention rules or retention settings. Run the installer by specifying the container name in the `-temp-metadata-container` parameter. | Required, if you want the Backup module to create immutable backups and if you have specified a value for the `-immutable-container` parameter. |
| `-containerClass` | Storage class of the custom container. The valid values for this parameter are:  - `Standard`: Represents Standard storage container. - `Tiering`: Represents a Standard storage container whose Lifecycle Tiering Policy is set. 	This option creates a container for which automatic archive is enabled. The tiering policy controls the frequency at which objects stored in this container are archived. The Oracle Database Cloud Backup Module for OCI Classic sets default parameters for the tiering policy. The default tiering policy excludes XML files and moves backups to archive storage immediately.  If this parameter is omitted, then the default is either `Standard` or the storage class of the container specified using `-container`, if the container exists. | Optional |
| `-containerLTP` | Name of Lifecycle Tiering Policy (LTP) file. This file is a JSON document that specifies the time after which objects in the storage container will be moved to the archive tier and type of objects which can be excluded from being archived.  To create archival backups, specify the name of the LTP file that defines the archival policy for the storage container by using the `-containerLTP` parameter. You can optionally set `-containerClass` to `Tiering`.  Note: The Lifecycle Tiering Policy file must exclude XML files. If this is not done, an error is displayed both when installing and using the Oracle Database Cloud Backup Module for OCI Classic. The `exclusions` field of the policy must be exactly like the one shown in Example 31-5. | Optional |
| `-configFile` | Specifies a custom name and location for the OCI Classic configuration file. For example, `-configFile=/myfiles/OCIClassicConfig.ora`.  Skip the `configFile` parameter if you want to create the configuration file in the default location chosen by the installer.  - Default location on `UNIX` and Linux systems: `$ORACLE_HOME/dbs` - Default location on Windows systems: `%ORACLE_HOME%\database`  The default name for the configuration file is `opcSID.ora`, where `SID` is the system identifier of the Oracle Database being backed up to Oracle Database Backup Cloud Service. | Optional |
| `-proxyHost` | HTTP proxy server host name | Optional |
| `-proxyPort` | HTTP proxy server port number | Optional |
| `-proxyId` | HTTP proxy server user name, if needed | Optional |
| `-proxyPass` | HTTP proxy server password, if needed | Optional |
| `-argFile` | Indicates that parameters should be read from the specified file. For example, a file named `arguments.txt` might contain the following:  `-opcID 'myAccount@myCompany.com' -opcPass 'abc123$' -host https://swiftobjectstorage.us-ashburn-1.oraclecloud.com/v1/hr-abc -libDir /home/oracle/OPC/lib -walletDir /home/oracle/OPC/wallet`  For this example, the following command installs the Oracle Database Backup Module for OCI Classic using the parameters specified in the file:  `java -jar opc_install.jar -argFile arguments.txt ` | Optional |

### Run the Backup Module for OCI Classic Installer

Use these steps to install the Oracle Database Cloud Backup Module for OCI Classic on the target database server.

Before you begin, ensure that you have verified the prerequisites and compiled the parameter values required to run the Oracle Database Cloud Backup Module for OCI Classic.

- Software Prerequisites for Oracle Database Backup Cloud Service
- Parameters to Run the Oracle Database Cloud Backup Module for OCI Classic Installer
1. The OCI Classic backup module installer file `opc_install.zip` is available in the Oracle home directory (see Table 31-5).
	Extract the contents of the `opc_install.zip` file to a subdirectory of your choice. In this example, extract the installer files to the `OCIclassic` subdirectory.
	```md
	$ mkdir -p $ORACLE_HOME/lib/OCIclassic
	$ cd $ORACLE_HOME/lib/OCIclassic
	unzip -q $ORACLE_HOME/lib/opc_installer.zip
	```
2. Go to the directory where you have extracted the OCI Classic backup module installer files. In this example, the `OCIclassic` directory contains the `opc_installer.jar` installer file and the README file `opc_readme.txt`.
	```md
	$ cd $ORACLE_HOME/lib/OCIclassic
	```
3. Run the OCI Classic backup module installer `opc_install.jar`. Specify the parameters and values.
	```md
	java -jar opc_install.jar -host https://swiftobjectstorage.us-ashburn-1.oraclecloud.com/v1/hr-abc
	-opcId 'myAccount@myCompany.com' -opcPass 'opc_pswd1'
	-walletDir /home/oracle/OPC/wallet
	```
	This sample run output shows how the installer automatically creates a wallet that contains Oracle Database Backup Cloud Service identifiers and credentials, and creates the Oracle Database Cloud Backup Module for OCI Classic configuration file `opc<ORACLE_SID>.ora`.
	```md
	Oracle Database Cloud Backup Module Install Tool, build 23.8.0.25.04
	Oracle Database Cloud Backup Module credentials are valid.
	Oracle Database Cloud Backup Module wallet created in directory /home/oracle/OPC/wallet.
	Oracle Database Cloud Backup Module initialization file /orclhome/dbs/opcsalesDB.ora created.
	```

***Example 31-4 Creating a Tiering Container When Installing the Oracle Database Cloud Backup Module for OCI Classic***

This example installs the Oracle Database Cloud Backup Module for OCI Classic and creates a container named `archive_container` for which automatic archive is enabled. To create a container with automatic archiving, you must specify `Tiering` for the `containerClass`. A default Lifecycle Tiering Policy is associated with this container and the values specified by the tiering policy control when backups stored in this container are moved to archive storage.

```md
% java -jar opc_install.jar -host https://swiftobjectstorage.us-ashburn-1.oraclecloud.com/v1/hr-abc
  -opcId 'myAccount@myCompany.com' -opcPass 'opc_pswd1'
  -walletDir /home/oracle/opc/opc_wallet
  -containerClass Tiering -container archive_container
Oracle Database Cloud Backup Module Install Tool, build 23.8.0.25.04
Oracle Database Cloud Backup Module credentials are valid.
Backups would be sent to container archive_container.
Oracle Database Cloud Backup Module wallet created in directory /home/oracle/opc/opc_wallet.
Oracle Database Cloud Backup Module initialization file /orclhome/dbs/opcSALESDB.ora created.
```

***Example 31-5 JSON Document for Lifecycle Tiering Policy File***

The following example shows a JSON document that contains the information required to define a Lifecycle Tiering Policy for an archive container. The Lifecycle Tiering Policy set using this JSON document excludes all XML files from the backup and moves backups to the Archive tier after 7 days.

```md
{
   "archiveAfter":
   {
     "timeUnit":"DAYS",
     "time":7
   },
   "exclusions":[{"exclusionType":"REGEX","exclusionFilter":"\\.xml"}]
}
```

**Note:** A value greater than 0 for `archiveAfter` is only supported in limited data centers.

### Files Created When the Oracle Database Cloud Backup Module for OCI Classic is Installed

After you run the Oracle Database Cloud Backup Module for OCI Classic, make sure the required files are created on the database server.

***Table 31-7 Files Created By the Oracle Database Cloud Backup Module for OCI Classic Installer***

| File | Location | Purpose |
| --- | --- | --- |
| `opcSID.ora` | As specified for the `-configFile` parameter when you run the Oracle Database Cloud Backup Module for OCI Classic installer.  Default location on Linux and UNIX systems:  `$ORACLE_HOME/dbs`  Default location on Windows systems:  `$ORACLE_HOME\database` | Configuration file that contains the Oracle Database Backup Cloud Service container URL and credential wallet location, where `SID` is the system identifier of the Oracle database being backed up to Oracle Database Backup Cloud Service.  Note: Containers that are used by Recovery Manager (RMAN) cannot have server-side encryption enabled. Because RMAN backups are already encrypted at the client side, server-side encryption is not required. |
| `cwallet.sso` | As specified for the `-walletDir` parameter when you run the Oracle Database Cloud Backup Module for OCI Classic installer.  Example location:  `ORACLE_HOME/dbs/opc_wallet` | Oracle wallet file that securely stores Oracle Database Backup Cloud Service credentials. This file is used during Recovery Manager (RMAN) backup and restore operations and is stored in the Oracle Database Backup Cloud Service wallet directory (for example, `opc_wallet`). |

## Configuring SBT Channel for Oracle Cloud (OCI)

Configure an automatic SBT channel so that RMAN can directly send database backups to Oracle Cloud.

Create a separate SBT channel for backups to Oracle Cloud Infrastructure and Oracle Cloud Infrastructure Classic. Specify `oracle.oci` as the `SBT_LIBRARY` for both channels. The default backup location is determined by the SBT channel that is currently set in the RMAN configuration. For example, if the RMAN environment is currently configured to use an SBT channel where `SBT_LIBRARY` is `oracle.oci` and `SBT_PARMS` is set to the Oracle Database Cloud Backup Module for OCI configuration file, then RMAN will send backups to Oracle Cloud Infrastructure Object Storage by default. To back up to a different location, for example Oracle Cloud Infrastructure Object Storage Service with Swift APIs, configure a separate SBT channel that corresponds to Oracle Database Cloud Backup Module for OCI Classic configuration.

Use these steps to configure an automatic SBT channel for backups to Oracle Cloud.

1. Start RMAN and connect to the target database.
2. Use the `CONFIGURE` command to configure an automatic SBT channel. You must include the `SBT_LIBRARY` parameter to specify the `oracle.oci` SBT library that enables RMAN backup and restore operations with Oracle Cloud. You can also provide the absolute path to the library file located in the Oracle home directory.
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
	This example configures an SBT channel. The `SBT_LIBRARY` parameter specifies the `oracle.oci` SBT library. The `ENV` parameter (on UNIX and Linux) or the `SBT_PARMS` parameter (Windows) specifies the Oracle Database Cloud Backup Module for OCI configuration file `opc<ORACLE_SID>.ora` which provides the parameters required for RMAN jobs. *`<ORACLE_SID>`* is the system identifier of the target Oracle Database being backed up to Oracle Database Cloud Backup Module for OCI.
3. Use the `SHOW ALL CHANGED` command to review the RMAN configuration and to confirm that Oracle Cloud is the configured backup destination.
	**Note:** On Windows systems, if you encounter System or Media Management Loading errors when you try to perform a backup, your Windows environment could be missing C libraries needed by the backup module. Download the [Redistributable Package for Visual Studio 2013](https://www.microsoft.com/en-us/download/details.aspx?id=40784). Choose the 64-bit version and run the downloaded `EXE` file. This should resolve the problem. In a Windows environment, pass `ORACLE_HOME` as a parameter to the channel by using `SBT_PARMS`.

## Additional Options for Using Oracle Database Backup Cloud Service

This section describes the different backup and recovery options you can use with Oracle Database Backup Cloud Service.

### Configuring Encryption for OCI Backups

Backups must be encrypted before they can be sent to Oracle Database Backup Cloud Service.

Use the `CONFIGURE` command to configure the default encryption algorithm for all RMAN backups that you create. Alternatively, use the `SET` command to explicitly specify the encryption when you perform a backup.

For information about encryption methodologies and choosing an encryption algorithm, see [Configuring Backup Encryption](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/bradv&id=BRADV-GUID-21D5FCCE-7AF1-4CF8-BC53-2496ECE3C56E).

If a backup is not encrypted, the RMAN reports this error message when you try to back up to OCI.

```md
RMAN-03009: failure of backup command on ORA_SBT_TAPE_1 channel at 08/15/2014 14:00:43
ORA-27030: skgfwrt: sbtwrite2 returned error
ORA-19511: non RMAN, but media manager or vendor specific failure, error text:
   KBHS-01602: backup piece 14p0jso8_1_1 is not encrypted
```

Recovery Manager (RMAN) encrypted backups are securely created, transmitted, and stored in the cloud. Use one of the following RMAN encryption modes to encrypt backups:

- Password encryption
- Transparent Data Encryption (TDE)
- Dual-mode encryption (combination of password and TDE)

### Configuring Automatic Archival to Oracle Cloud Infrastructure

You can move backups that are rarely accessed, but must be retained for long periods, to Archive Storage. Archive Storage is more cost effective than Object Storage for preserving cold data.

You can either create a new bucket or use an existing bucket to store backups that must be automatically moved to Archive Storage.

To configure automatic archival of backups to Oracle Cloud Infrastructure Archive Storage:

1. Authorize Object Storage service to move backups to Archive Storage. See *Service Permissions* in [Using Object Lifecycle Management](https://docs.cloud.oracle.com/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm#permissions) of the *Oracle Cloud Infrastructure Documentation*.
2. To use an existing bucket, ensure that automatic archival is enabled for the bucket.
	1. Check if automatic archival is enabled by viewing the bucket details. See [Managing Buckets](https://docs.cloud.oracle.com/iaas/Content/Object/Tasks/managingbuckets.htm#usingconsole) in the *Oracle Cloud Infrastructure Documentation*.
		2. If automatic archival is not enabled, run the installer with the `-enableArchiving` parameter to enable archiving for the bucket.
		The command to run the installer is similar to the one in Run the Backup Module for OCI Installer. The `-bucket` parameter must specify the name of the existing bucket. The default values are used if the `-archiveAfterBackup` and `-retainAfterRestore` parameters are not specified.
		An archiving rule is applied to all the existing objects in the bucket. For example, if you apply a lifecycle policy that archives after two weeks to an existing bucket containing objects, all the objects older than two weeks will be archived.
3. To create a new bucket, run the installer with the `-bucket` and `-enableArchiving` parameters.
	See Run the Backup Module for OCI Installer for an example.
4. Configure an RMAN channel that corresponds to the Oracle Database Cloud Backup Module for OCI. See Configuring SBT Channel for Oracle Cloud (OCI).

### Configuring Automatic Archival to Oracle Cloud Infrastructure Object Storage Service with Swift API

Infrequently-used backups can be moved from standard storage to archive storage after a specified number of days. This frees up space on the standard storage for new backups.

To archive backups, you must store them in a standard container that is associated with a Lifecycle Tiering Policy (LTP). The LTP is a container policy that defines the type of tiering that is associated with the standard container. After the number of days specified by the LTP elapses, the backups stored in the standard container are automatically archived. You can explicitly exclude specific objects from being archived automatically.

To configure automatic archive of backups to Oracle Cloud Infrastructure Object Storage Service with Swift APIs:

1. Use one of the following techniques, when installing the Oracle Database Cloud Backup Module for OCI Classic, to specify the container to which backups must be archived:
	- Create a standard container that is associated with an LTP
		Specify the name that must be used for the new standard container by using the `-container` parameter. Set the `-containerClass` parameter to Tiering. To specify a user-defined LTP, use the `-containerLTP` parameter. If you omit this parameter, the default LTP is associated with the new container.
		See Run the Backup Module for OCI Classic Installer
		For example:
		```md
		-container PAYROLL_ARC
		-containerClass Tiering
		```
		The standard container with the specified name is created and a default LTP is assigned to it. All backups, except XML objects, are archived when the number of days specified by the LTP elapses. This automatically adds the `OPC_CONTAINER` and `OPC_CONTAINER_CLASS` parameters to the `opc` *SID*`.ora` file so that these settings are used for backups.
		- Specify only the container class
		Set `-containerClass` to `Tiering`.
		The `OPC_CONTAINER_CLASS` parameter is set to `Tiering` in the `opc` *SID*`.ora` configuration file. The Oracle Database Cloud Backup Module for OCI Classic installer attempts to find an existing standard container that is associated with an LTP. If no such container is found, a new standard container with the default LTP is created. The naming convention used for the new container is `oracle-data-` *account\_name* `-` *index*.
		- Use an existing standard container that is associated with an LTP
		Include the `-container` parameter with the name of an existing standard container that is associated with an LTP.
		For example:
		```md
		-container PAYROLL_ARC
		```
		This automatically adds the `OPC_CONTAINER` parameter to the `opc` *SID*`.ora` configuration file so that the specified container is used to store backups.
2. Configure an RMAN channel that corresponds to the Oracle Database Cloud Backup Module for OCI Classic. See Configuring SBT Channel for Oracle Cloud (OCI).

### Storing Backups in OCI Immutable Buckets

Learn how to configure the Oracle Database Cloud Backup Module to store backups in OCI immutable buckets.

In Oracle Cloud Infrastructure (OCI) Object Storage, an immutable bucket is a storage location governed by time-bound retention rules that protect data from modification or deletion for a specified duration. Use immutable buckets to implement a flexible backup retention strategy for each target database, and to prevent any modification to backups.

The Oracle Database Cloud Backup Module supports storing backups in immutable buckets that you have created in OCI.

To store backups in immutable buckets, you must first create these buckets in OCI Object storage:

- Regulatory Compliance Bucket configured with retention rules and rule lock (if necessary)
	You can also reuse an existing bucket associated with retention rules.
- Temporary Metadata Bucket with no retention rules or retention settings
	During backup operations, the temporary bucket is used to store backup metadata and files temporarily.

**Note:** If you have stored your database backups in an existing regular bucket, then you can configure the same bucket to store immutable backups. In this case, first specify the existing bucket and a temporary bucket in the `opcSID.ora` configuration file (or run the backup module installer again), and then apply retention rules to the bucket in OCI. This ensures that your existing backups are also protected for the duration defined in the retention rule.

**Note:** Your databases may have varied demands for backup retention. As a best practice, Oracle recommends that you maintain a separate immutable bucket and a corresponding unique temporary metadata bucket for each target database. For example, if you create an immutable bucket named `sales_db`, then create a temporary metadata bucket named `sales_db_temp`. If you plan to reuse an existing OCI bucket that is currently used by more than one target database, ensure that you reconfigure the bucket per the best practice recommended by Oracle.

For more information about creating buckets and retention rules, see *OCI Object Storage* documentation.

**To Store Immutable Backups with Oracle Database Cloud Backup Module for OCI**

1. Install the Oracle Database Cloud Backup Module on your database server. See Installing the Oracle Database Cloud Backup Module for OCI.
	When you run the backup module, specify the `-bucket` parameter with the name of an existing bucket or a new immutable bucket that you have created in OCI.
2. After you install the backup module, add the `OPC_CONTAINER` parameter, the `OPC_TEMP_CONTAINER` parameter, and the bucket names in `opcSID.ora`.
	This example specifies the immutable bucket `sales_db` and the temporary metadata bucket `sales_db_temp` in the `opcSID.ora` file:
	```md
	OPC_CONTAINER=sales_db
	OPC_TEMP_CONTAINER=sales_db_temp
	```
3. In the OCI Console, review the retention rule applied on the immutable bucket to ensure that you have specified the exact duration for which you want to prevent any modification to backups. Lock the rule, if necessary.

**Note:** Ensure that the duration you specify in a retention rule is shorter than the RMAN recovery window period. RMAN issues an error while trying to delete an expired backup that exists in the retention period.

If you use the Oracle Database Backup Cloud Service Module for OCI Classic, use a similar procedure to install the backup module, and then add the `OPC_CONTAINER` parameter, the `OPC_TEMP_CONTAINER` parameter, and the container names in `opcSID.ora`.

**Related Topics**

- Installing the Oracle Database Cloud Backup Module for OCI
- Installing the Oracle Database Cloud Backup Module for OCI Classic
- Files Created by the Oracle Database Cloud Backup Module for OCI Installer
- [Oracle Cloud Infrastructure Object Storage](https://docs.oracle.com/en-us/iaas/Content/Object/home.htm)

### Storing Backups in Custom Locations

A default location is created when you install the Oracle Database Cloud Backup Module for OCI or Oracle Database Cloud Backup Module for OCI Classic and backups are stored as objects in this location. You can also store backups in custom locations you’ve created yourself.

With the Oracle Database Cloud Backup Module for OCI, a default bucket is created. With the Oracle Database Cloud Backup Module for OCI Classic, a default storage container is created.

Custom containers and custom buckets can be created using REST calls or third-party tools such as CloudBerry Explorer.

To create containers using the REST API, see the tutorial [Oracle Cloud Infrastructure Object Storage Classic: Creating Containers Using the REST API](https://www.oracle.com/webfolder/technetwork/tutorials/obe/cloud/objectstorage/creating_containers_REST_API/creating_containers_REST_API.html). For related Oracle Cloud Infrastructure Object Storage Classic Service documentation, see [Creating a Container](https://www.oracle.com/webfolder/technetwork/tutorials/obe/cloud/objectstorage/oss_creating_container/creating-container.html).

To create buckets using the REST API or the OCI Console, see [Managing Buckets](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets.htm).

**Note:** If you are using Oracle Cloud Infrastructure Object Storage or Oracle Exadata Database Service on Dedicated Infrastructure and want to automatically store backups in cloud storage, you need to create buckets or containers before you create your database deployment. For information about backing up your deployment to the cloud, see [OCI Object Storage](https://docs.oracle.com/en-us/iaas/Content/Object/home.htm) or [Manage Database Backup and Recovery on Oracle Exadata Database Service on Dedicated Infrastructure](https://docs.oracle.com/en-us/iaas/exadatacloud/exacs/ecs-managing-db-backup-and-recovery.html#GUID-0CA094F9-7160-43FA-AB23-D51986CBBE85).

**Note:** Containers that are used by Recovery Manager (RMAN) cannot have server-side encryption enabled. Because RMAN backups are already encrypted at the client side, server-side encryption is not required.

***Example 31-6 Using Custom Buckets with Oracle Cloud Infrastructure***

You can specify that backups must be stored in custom containers either while installing the Oracle Database Cloud Backup Module for OCI or after the installation.

- While running the Oracle Database Cloud Backup Module for OCI installer, include the `-bucket` parameter and the custom bucket name, as shown in this example.
	```md
	-bucket SALES_DB
	```
	This automatically adds the `OPC_CONTAINER` parameter to the `opcSID.ora` configuration file so the custom bucket is used for backups, where `SID` is the system identifier of the Oracle Database being backed up to Oracle Database Backup Cloud Service.
- To specify a custom container after you have set up the Oracle Database Cloud Backup Module for OCI, add the `OPC_CONTAINER` parameter and the bucket name to `opcSID.ora`, as shown on this example.
	```md
	OPC_CONTAINER=SALES_DB
	```

***Example 31-7 Using Custom Containers with Oracle Cloud Infrastructure Classic***

Specify that backups must be stored in a custom container either while installing the Oracle Database Cloud Backup Module for OCI Classic or after the installation.

- While running the Oracle Database Cloud Backup Module for OCI Classic installer, include the `-container` parameter and the custom container name, as shown in this example.
	```md
	-container PAYROLL_DB
	```
	This automatically adds the `OPC_CONTAINER` parameter to the `opcSID.ora` configuration file so the custom container is used for backups, where `SID` is the system identifier of the Oracle Database being backed up to Oracle Database Backup Cloud Service.
- To specify a custom container after you have installed the Oracle Database Cloud Backup Module for OCI Classic, add the `OPC_CONTAINER` parameter and the container name to `opcSID.ora`, as shown in this example.
	```md
	OPC_CONTAINER=PAYROLL_DB
	```

For information about parameters used by the installer, see Parameters to Run the Oracle Database Cloud Backup Module for OCI Classic Installer.

For information about the `opcSID.ora` configuration file, see Files Created When the Oracle Database Cloud Backup Module for OCI Classic is Installed.

## Backing Up to Oracle Database Backup Cloud Service

After you install the required backup module and configure Recovery Manager (RMAN) settings, you can create backups using familiar RMAN commands.

Information about your cloud backups is maintained in the database control file, and in the recovery catalog if you use one.

Encryption is required to back up to Oracle Database Backup Cloud Service. You can use password encryption, Transparent Data Encryption (TDE), or dual-mode encryption, which is a combination of password and TDE.

**Note:** Use RMAN parallelism, compression, and other best practices to speed up cloud backups and restores. For more information about optimizing performance, see the guidelines listed in [Best Practices to Optimize Cloud Backup Rates](rman-cloud-settings.md).

For information about performing various types of backup and restore operations, see [Backing Up and Archiving Data](part-backing-up-archiving.md).

For information about RMAN commands, see [About RMAN Commands](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/bradv&id=RCMRF-GUID-0385D88E-6D36-41AC-BEA0-DD7F5C97D253) in *Oracle Database Backup and Recovery Reference*.

**Topics**

- [Best Practices to Optimize Cloud Backup Rates](rman-cloud-settings.md)
- Prerequisites for Backups and Restores with Oracle Database Backup Cloud Service
- Backing Up to Oracle Database Backup Cloud Service Using Password Encryption
- Backing Up to Oracle Database Backup Cloud Service Using Transparent Data Encryption (TDE)
- Backing Up to Oracle Database Backup Cloud Service Using Dual-Mode Encryption
- Using the Weekly Full and Daily Incremental Backup Strategy
- Backing Up from the Fast Recovery Area (FRA) to Oracle Database Backup Cloud Service
- Monitoring Your Storage Capacity
- Extracting Backup Metadata from OCI Object Storage

### Prerequisites for Backups and Restores with Oracle Database Backup Cloud Service

Certain prerequisite steps must be completed before you can back up to or restore from Oracle Database Backup Cloud Service.

**Prerequisites**

- Install the backup module that corresponds to the destination in which backups must be stored.
	- To create backups to Oracle Cloud Infrastructure, install the Oracle Database Cloud Backup Module for OCI. Backups created using this module are stored in Oracle Cloud Infrastructure Object Storage. See Installing the Oracle Database Cloud Backup Module for OCI.
		- To create backups to Oracle Cloud Infrastructure Classic, install the Oracle Database Cloud Backup Module for OCI Classic. Backups created using this module are stored in Oracle Cloud Infrastructure Object Storage Classic. See Installing the Oracle Database Cloud Backup Module for OCI Classic.
- Configure an RMAN channel that will be used to create the required backups.
	To configure channels, see Configuring SBT Channel for Oracle Cloud (OCI). To configure other backup settings, see Additional Options for Using Oracle Database Backup Cloud Service.
	To automatically move infrequently-used backups to archive storage, see Configuring Automatic Archival to Oracle Cloud Infrastructure Object Storage Service with Swift API.

### Backing Up to Oracle Database Backup Cloud Service Using Password Encryption

You can use password encryption to back up to Oracle Database Backup Cloud Service. The password must be specified each time you back up and restore.

**Prerequisites**

See Prerequisites for Backups and Restores with Oracle Database Backup Cloud Service for prerequisites.

**Procedure**

1. Specify the password that must be used to encrypt backups. Use the `SET ENCRYPTION` command.
2. Back up the database using the `BACKUP DATABASE` command. Include archived redo log files, if required.

**Note:** If you forget or lose the password, you will not be able to restore the backup.

The following example configures password encryption for the backup and creates a backup of the entire database:

```md
RMAN> SET ENCRYPTION ON IDENTIFIED BY 'my_pswd' ONLY;
RMAN> BACKUP DEVICE TYPE sbt DATABASE;
```

For information about restoring and recovering backups, see Restoring Backups from Oracle Database Backup Cloud Service.

### Backing Up to Oracle Database Backup Cloud Service Using Dual-Mode Encryption

You can use dual-mode encryption to back up to Oracle Database Backup Cloud Service. Dual-mode encryption is a combination of password encryption and Transparent Data Encryption (TDE).

**Prerequisites**

See Prerequisites for Backups and Restores with Oracle Database Backup Cloud Service for prerequisites.

**Procedure**

1. Enable encryption using the `SET ENCRYPTION` command.
	If TDE is configured for the Oracle Database you’re backing up, omit the `ONLY` keyword with the `SET ENCRYPTION` command to indicate the backup is protected with both a password and the configured transparent encryption.
2. Back up the database using the `BACKUP DATABASE` command. Include archived redo log files, if required.

**Note:** If you forget or lose the password, you won’t be able to restore the backup.

For information about restoring and recovering backups, see Restoring Backups from Oracle Database Backup Cloud Service.

The following commands create a backup of the entire database by using dual-mode encryption.

```md
RMAN> SET ENCRYPTION ON IDENTIFIED BY 'my_pswd';
RMAN> BACKUP DEVICE TYPE sbt DATABASE;
```

### Backing Up to Oracle Database Backup Cloud Service Using Transparent Data Encryption (TDE)

You can use Transparent Data Encryption (TDE) to back up to Oracle Database Backup Cloud Service. With TDE you don’t need to provide a password every time you create or restore a backup.

**Prerequisites**

To back up using TDE you need to have a TDE wallet (TDE keystore), which is different from the OPC wallet that stores Oracle Database Backup Cloud Service credentials.

See Prerequisites for Backups and Restores with Oracle Database Backup Cloud Service for prerequisites.

**Procedure**

To create a TDE wallet if you don’t already have one:

1. Add the following line to the `sqlnet.ora` file:
	```md
	ENCRYPTION_WALLET_LOCATION=
	  (SOURCE=(METHOD=FILE)(METHOD_DATA=
	    (DIRECTORY=path_to_TDE_wallet)))
	```
	where *path\_to\_TDE\_wallet* is the location where the TDE wallet is to be created; this must be different from the OPC wallet location.
2. Start SQL\*Plus as sys:
	```md
	sqlplus / as sysdba
	```
3. Create the TDE wallet in the location specified in `sqlnet.ora`:
	```md
	SQLPLUS> alter system set encryption key identified by "TDE-password";
	```
	where `TDE-password` is the password that must be used to open the TDE wallet.
4. Whenever the database is restarted, open the TDE wallet with the following command:
	```md
	SQLPLUS> alter system set encryption wallet open identified by "TDE-password";
	```

For complete information about TDE, see [Using Transparent Data Encryption](https://docs.oracle.com/pls/topic/lookup?ctx=db121&id=ASOAG600) in *Oracle Database Advanced Security Guide*.

To back up an Oracle Database that uses TDE:

1. Connect Recovery Manager (RMAN) to the target database to be backed up and configure encryption for the database:
	```md
	RMAN> SET ENCRYPTION ON;
	```
2. Back up the database:
	```md
	RMAN> BACKUP DATABASE;
	```

For information about restoring and recovering backups, see Restoring Backups from Oracle Database Backup Cloud Service.

### Backing Up from the Fast Recovery Area (FRA) to Oracle Database Backup Cloud Service

You can back up image copies and backup sets from the fast recovery area (FRA) to Oracle Database Backup Cloud Service.

**Prerequisites**

See Prerequisites for Backups and Restores with Oracle Database Backup Cloud Service for prerequisites.

**Procedure**

To back up image copies from FRA to Oracle Database Backup Cloud Service, use these commands:

```md
RMAN> BACKUP RECOVERY AREA;
RMAN> BACKUP DEVICE TYPE sbt COPY OF DATABASE;
RMAN> BACKUP RECOVERY FILES;
RMAN> BACKUP RECOVERY FILE DESTINATION;
```

To back up backup sets from FRA to Oracle Database Backup Cloud Service, use this command:

```md
RMAN> BACKUP DEVICE TYPE sbt BACKUPSET ALL;
```

For information about restoring and recovering backups, see Restoring Backups from Oracle Database Backup Cloud Service.

### Using the Weekly Full and Daily Incremental Backup Strategy

The weekly full and daily incremental backup strategy is set up once. Backups continue to be created forever and they can be used to perform restore or recovery operations when required.

To configure a weekly full and daily incremental backup strategy:

1. Configure an RMAN channel that corresponds to the destination to which you want to save backups. See Configuring SBT Channel for Oracle Cloud (OCI).
2. Configure autobackups for the control file. See [Configuring Autobackups](rman-cloud-settings.md).
3. Configure any additional optimizations such as compression, parallelism, or multisection backups. See [Best Practices to Optimize Cloud Backup Rates](rman-cloud-settings.md).
4. Set up the backup strategy using the following commands:
	```md
	BACKUP INCREMENTAL LEVEL 0 DATABASE PLUS ARCHIVELOG NOT BACKED UP DELETE INPUT;
	BACKUP INCREMENTAL LEVEL 1 DATABASE PLUS ARCHIVELOG NOT BACKED UP DELETE INPUT;
	```

### Monitoring Your Storage Capacity

When you subscribe to Oracle Database Backup Cloud Service you purchase the amount of storage capacity you want for your backups. If you reach your storage capacity limit and try to back up your database, your backup will fail.

You can quickly increase the limit by purchasing more capacity on demand. Once you buy more capacity, you can continue doing backups. You can also free up space by using RMAN to delete obsolete backups.

You can monitor how much storage capacity you’ve used by viewing detailed metrics about your usage. If your backups are stored in Object Storage Classic, use the Infrastructure Classic Console. If your backups are stored in Object Storage, use the Cost Analysis tools. See [Monitor Your billing Data](https://docs.oracle.com/en/cloud/get-started/subscriptions-cloud/mmocs/monitor-your-billing-data.html) in *Oracle Cloud Managing and Monitoring Oracle Cloud* or [Checking Your Balance and Usage](https://docs.cloud.oracle.com/iaas/Content/GSG/Concepts/costs.htm) in the *Oracle Cloud Infrastructure* documentation or.

You can also check the capacity used by your account or under a container by using cURL.

Example commands for Oracle Cloud Infrastructure Classic:

```md
# curl -v -s -X GET
       -H "X-Storage-User: service-identitydomain:userid"
       -H "X-Storage-Pass: password"
       https://identitydomain.storage.oraclecloud.com/auth/v1.0
```

Use the `Auth-Token` entry to get the header information:

```md
# curl -v -X HEAD
       -H "X-Auth-Token: auth-token"
       https://identitydomain.storage.oraclecloud.com/v1/service-identitydomain
```

Example output (pertinent details in bold):

```md
< HTTP/1.1 204 No Content
< X-Account-Container-Count: 2
< X-Account-Object-Count: 567
* Server Oracle-Storage-Cloud-Service is not blacklisted
< Server: Oracle-Storage-Cloud-Service
< X-Account-Meta-Policy-Georeplication: us2
< X-Account-Meta-Policy-Archive: arch-us2
< X-Timestamp: 1446492266.33718
< X-Account-Bytes-Used: 7884540569
< X-Account-Meta-Quota-Bytes: 536870912000
< Accept-Ranges: bytes
< X-Trans-Id: txeb611621958647a681cd6-0056a4404bga
< Date: Sun, 24 Jan 2016 03:08:59 GMT
< Connection: keep-alive
< X-Storage-Class: Standard
< X-Container-Meta-Policy-Georeplication: us2
< X-Last-Modified-Timestamp: 1446492266.33718
< Content-Type: text/plain;charset=UTF-8
```

Example output for a tiering container (pertinent details in bold):

```md
< HTTP/1.1 204 No Content
< X-Container-Object-Count: 0
< X-Container-Write: myIdentity4.Storage.Storage_ReadWriteGroup
< Accept-Ranges: bytes
< X-Timestamp: 1531949125.70314
< X-Container-Read: myIdentity4.Storage.Storage_ReadOnlyGroup,myIdentity3.Storage.Storage_ReadWriteGroup
< X-Container-Bytes-Used: 0
< X-Trans-Id: tx0d71e235b8814b94b197b-005b4fb04ega
< Date: Wed, 18 Jul 2018 21:25:34 GMT
< Connection: keep-alive
< X-Storage-Class: Standard
< Container-Meta-Policy-Georeplication: uscom-central-1
< Container-Policies-Enabled: tiering
< Last-Modified-Timestamp: 1531949125.70314
< Content-Type: text/plain;charset=utf-8
< Server: Oracle-Storage-Cloud-Service
```

### Extracting Backup Metadata from OCI Object Storage

Use this procedure to extract the backup metadata from OCI Object Storage and store the information in an XML file.

If your database backups are stored in OCI Object Storage, then you can use the `odbsrmt.py` tool to manually extract the backup metadata into an XML file.

The `odbsrmt.py` file and the associated readme are both located in the Oracle home directory (`ORACLE_HOME/rdbms/admin`) of the target database.

1. On the database server, install the Oracle Database Cloud Backup Module for OCI Classic module if you are using the Swift endpoints to access Object Storage. If you are using the OCI native endpoints, then install the Oracle Database Cloud Backup Module for OCI module.
2. Run the `odbsrmt.py` tool on the database server by providing the mandatory parameters and their values.
	- If you are using the Swift endpoints to access an Object Storage bucket, then provide these mandatory parameters and values to generate a backup metadata XML file.
		```md
		--mode=rman-listfile
		--ocitype=classic
		--credential=user name for your cloud backup module for OCI Classic account/password
		--host=REST endpoint for the OCI Object Storage Service with Swift APIs
		--container=Name of the storage container that contains the source database backups
		--forcename=Specify a name for the metadata XML file
		--dir=Directory to store the metadata XML file
		--dbid=The DBID of the source database
		--prefix=The common prefix used in the backup piece names
		```
		- If you are using the OCI native APIs to access an Object Storage bucket, then provide these mandatory parameters and values to generate the backup metadata XML file.
		```md
		--mode=rman-listfile
		--ocitype=bmc
		--uocid=User OCID for the Oracle Cloud Infrastructure account
		--tocid=Tenancy OCID for the Oracle Cloud Infrastructure account
		--pubfingerprint=public key fingerprint
		--pvtkeyfile=private key used to authenticate OCI API requests
		--host=REST endpoint for the OCI account
		--container=Name of the bucket that contains the source database backups
		--forcename=Specify a name for the metadata XML file
		--dir=Directory to store the metadata XML file
		--dbid=The DBID of the source database
		--prefix=The common prefix used in the backup piece names
		```
		- The `rman-listfile` mode generates the backup metadata in an XML file that can be read by RMAN to perform a `DUPLCIATE` operation of the source database. You can run the `DUPLICATE` command along with the `BACKUP LOCATION FROM FILE backup_list_file` clause to specify the XML file required for duplication. See *Backup and Recovery Reference* for more information.
		- The `odbsrmt.py` tool searches a bucket or container for backup piece names that start with the specified `prefix`.
	This example shows how the `odbsrmt.py` tool creates a backup metadata file `duplicate.xml` for a database backup stored in the Object Storage container `PRODBACKUPS`
	```md
	$ $ORACLE_HOME/bin/python /home/oracle/OPC/lib/odbsrmt.py
	--mode=rman-listfile
	--host= https://swiftobjectstorage.us-ashburn-1.oraclecloud.com/v1/hr-abc
	--ocitype=classic
	--credential='myAccount@myCompany.com'/'account-password'
	--container=PRODBACKUPS
	--forcename=duplicate.xml
	--dir=/home/oracle/OPC
	--dbid=2500571935
	--prefix=CloudBkp
	odbsrmt.pl: ALL report output will be written to [/home/oracle/OPC/duplicate.xml]
	odbsrmt.pm: gathering information from container PRODBACKUPS...
	odbsrmt.pm: object count = 10 in container PRODBACKUPS
	odbsrmt.pm: scanned all entries in PRODBACKUPS
	odbsrmt.pl: ALL report output has been written to [/home/oracle/OPC/duplicate.xml]
	odbsrmt.pl: Reporting completed
	```
	This example shows how the `odbsrmt.py` tool creates a backup metadata file `duplicate.xml` for a database backup stored in the Object Storage bucket `OCIBACKUPS`
	```md
	python ./ocilib/odbsrmt.py
	--mode=rman-listfile
	--host=https://objectstorage.us-ashburn-1.oraclecloud.com
	--ocitype=bmc
	--uocid=ocid1.user.oc1..aaaaaaaasd754pijuwheaq67t7tninefkn7z7aibtusj7jqac5lpm7wm37va
	--tocid=ocid1.tenancy.oc1..aaaaaaaavjhvwf4c7q2ozzyduh7njrft58i6ts3ryjk7v83w7q4wdr2ka
	--pubfingerprint=e5:10:06:b1:fb:24:ef:db:46:21:16:20:46:jk:th:35
	--pvtkeyfile=./oci_api_key.pem
	--container=OCIBACKUPS
	--dbid=2275063903
	--forcename=duplicate.xml
	--dir=/home/oracle
	```
	This example shows the sample contents of an XML file that contains the backup metadata.
	```md
	<MetaData>
	   <File>
	      <Filename>6GJ28IEKFL_07CEC18D372F4D29E06379624664E053</Filename>
	      <SetStamp>1150345378</SetStamp>
	      <IsSpfile>NO</IsSpfile>
	      <IsControlFile>NO</IsControlFile>
	      <PieceNo>1</PieceNo>
	      <Dbname>SALESDB</Dbname>
	      <Dbid>3483424530</Dbid>
	   </File>
	   <File>
	      <Filename>6GJ28IEKFL_07CEC18D374B4D29E06379624664E053</Filename>
	      <SetStamp>1150345398</SetStamp>
	      <IsSpfile>NO</IsSpfile>
	      <IsControlFile>NO</IsControlFile>
	      <PieceNo>1</PieceNo>
	      <Dbname>SALESDB</Dbname>
	      <Dbid>3483424530</Dbid>
	   </File>
	   <File>
	      <Filename>6GJ28IEKFL_07CEC1A625064D36E0637962466444CD</Filename>
	      <SetStamp>1150345378</SetStamp>
	      <IsSpfile>NO</IsSpfile>
	      <IsControlFile>NO</IsControlFile>
	      <PieceNo>1</PieceNo>
	      <Dbname>SALESDB</Dbname>
	      <Dbid>3483424530</Dbid>
	   </File>
	   <File>
	      <Filename>6GJ28IEKFL_07CEC1A6254D4D36E0637962466444CD</Filename>
	      <SetStamp>1150345451</SetStamp>
	      <IsSpfile>NO</IsSpfile>
	      <IsControlFile>NO</IsControlFile>
	      <PieceNo>1</PieceNo>
	      <Dbname>SALESDB</Dbname>
	      <Dbid>3483424530</Dbid>
	   </File>
	</MetaData>
	```

## Restoring Backups from Oracle Database Backup Cloud Service

You can use standard Recovery Manager (RMAN) commands to perform restore and recovery operations from Oracle Database Backup Cloud Service. You can also use RMAN to specify retention policies, perform crosschecks, and delete backups.

A few possible scenarios are addressed here. For complete information about using RMAN to perform various types of restore and recovery operations, see [Overview of RMAN Data Repair](rman-data-repair-concepts.md).

For information about RMAN commands, see [About RMAN Commands](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/bradv&id=RCMRF-GUID-0385D88E-6D36-41AC-BEA0-DD7F5C97D253) in *Oracle Database Backup and Recovery Reference*.

The concepts and commands in these RMAN guides are applicable to the database backed up to Oracle Database Backup Cloud Service.

**Topics**

- Restore and Recover Using Oracle Cloud Backups
- Recovering Databases from OCI Archive Storage
- Restoring OCI Backups to a New Database Host
- Creating a Data Guard Standby Database in Oracle Cloud

### Restore and Recover Using Oracle Cloud Backups

Oracle Database backups stored in Oracle cloud can be restored and recovered using Recovery Manager (RMAN). All RMAN restore and recovery operations are supported with cloud backups.

Before you restore backups, configure an RMAN channel that corresponds to the location where the backup that must be restored is stored. The backups can be stored in Oracle Cloud Infrastructure Object Storage or Oracle Cloud Infrastructure Object Storage Classic. For information about configuring channels, see Configuring SBT Channel for Oracle Cloud (OCI).

For example, if password encryption was used to encrypt the backup, commands for a typical restore for the entire database would look as follows, specifying the password that was used to encrypt the backup:

```md
RMAN> SET DECRYPTION IDENTIFIED BY 'my_pswd';
RMAN> RESTORE DATABASE;
RMAN> RECOVER DATABASE;
```

If Transparent Data Encryption (TDE) was used to encrypt the backup, use this command to perform restore and recovery:

```md
RMAN> SET ENCRYPTION ON;
RMAN> RESTORE DATABASE;
RMAN> RECOVER DATABASE;
```

### Recovering Databases from OCI Archive Storage

Oracle Database backups stored in archive storage can be restored and recovered using Recovery Manager (RMAN).

Backups can be stored in Oracle Cloud Infrastructure Archive Storage or archive storage in Oracle Cloud Infrastructure Classic. Backups stored in archive storage need to be recalled first before they can be restored. You must plan in advance for restore and recover operations using backups stored in archive storage. Use `RESTORE DATABASE PREVIEW ... RECALL` to initiate a recall operation for the required backups. After you begin the restore operation, if the backups are still not available to read from the archive storage, then the restore operation waits until the required backups are available. This may slow down the restore operation.

To recover a database using backups from archive storage:

1. Start RMAN and connect to the target database.
2. If the database is not mounted, then mount but do not open the database.
	For example, enter the following command:
	```md
	STARTUP MOUNT;
	```
3. Depending on where the backups are stored, configure an RMAN channel that corresponds to Oracle Database Cloud Backup Module for OCI or Oracle Database Cloud Backup Module for OCI Classic. See [Configuring Autobackups](rman-cloud-settings.md).
4. Provide information required to decrypt the backups.
	- If password or dual-mode encryption was used to create the backups, provide the encryption password using the following syntax:
		```md
		RMAN> SET DECRYPTION IDENTIFIED BY encryption_password;
		```
		- If Transparent Data Encryption (TDE) with a password-protected software keystore was used to create the backups, ensure that the keystore that contains the encryption key is open.
		The following command, in SQL\*Plus, opens a password-protected keystore:
		```md
		ADMINISTER KEY MANAGEMENT SET KEYSTORE OPEN IDENTIFIED BY 'password';
		```
5. Preview the backups required for the restore operation using the `PREVIEW` option of the `RESTORE` command.
	The following command previews backups that will be used for the restore operation:
	```md
	RESTORE DATABASE PREVIEW;
	```
	The output displays a detailed list of the backup pieces that will be used in the restore operation and the location of these backup pieces (standard Object Storage or Archive Storage). If any backup pieces are in Archive Storage, the output indicates that these are remote files.
6. Recall the required backups from archive storage using the `RECALL` option in the `RESTORE` command.
	The following command recalls database backups from archive storage:
	```md
	RESTORE DATABASE PREVIEW RECALL;
	```
7. Restore and recover the database using the following commands:
	```md
	RESTORE DATABASE;
	RECOVER DATABASE;
	```

**Related Topics**

- [*Oracle Database Backup and Recovery User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=db121&id=BRADV89771)

### Restoring OCI Backups to a New Database Host

If there is a site failure and if your database servers are down, you can use the backups in the cloud to restore to a new host. The following example shows how to restore backups from Oracle Database Backup Cloud Service to a new host.

**Note:** If you want to restore the database to an Oracle Database Cloud Service database deployment (non-Virtual Image), see [Creating a Database Deployment Using a Cloud Backup](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/bradv&id=CSDBI-GUID-2A704C0A-B27A-4604-A2A6-BFADC899FF9B) in *Using Oracle Database Cloud Service*. Otherwise, use the following steps to restore to a new host. You would also use these steps to restore to Oracle Database Cloud Service - Virtual Image database deployments.

To perform the steps in this example, the new host must have the following:

- Internet connectivity to connect to Oracle Database Backup Cloud Service
- A compatible operating system with the same endian format as the source host
- The same version of Oracle Database software as the source host
	If the new host has a higher version of Oracle software, ensure that there is a supported upgrade path between the Oracle Database version on the source host and the destination host. Then, perform the steps required to upgrade the destination database after the RMAN restore.

You must also know the following:

- DBID of the source database
- Password used to encrypt the backup if password-based encryption was used
- TDE encryption wallet from the source database if TDE encryption was used

To restore from a cloud backup stored using Oracle Cloud Infrastructure or Oracle Cloud Infrastructure Classic to a new host:

1. Install the Oracle Database Cloud Backup Module for OCI or Oracle Database Cloud Backup Module for OCI Classic on the new host using the same subscription credentials and custom container (if any) used for the backup. For information about installing the module, see Run the Backup Module for OCI Installer or Run the Backup Module for OCI Classic Installer.
	For example, with Oracle Cloud Infrastructure Classic, the service name (`-serviceName`), identity domain (`-identityDomain`), user name (`-opcId`), password (`-opcPass`), and container name (`-container`), if you used a custom container, must be the same. With Oracle Cloud Infrastructure, the tenancy OCID (`-tOCID`), user OCID (`-uOCID`), and bucket (`-bucket`), if you used a custom bucket, must be the same.
2. On the new host, connect to Recovery Manager (RMAN), set the decryption password, set the DBID, and restore the SPFILE.
	For example:
	```md
	rman target /
	RMAN> STARTUP NOMOUNT;
	RMAN> SET DECRYPTION IDENTIFIED BY 'my_bkup_pwd';
	RMAN> SET DBID=3389098001;
	RMAN> RUN {
	ALLOCATE CHANNEL t1 DEVICE TYPE sbt PARMS 'SBT_LIBRARY=libopc.so ENV=(OPC_PFILE=/u01/app/oracle/product/12.1.0/dbhome_1/dbs/opcDUP.ora)';
	RESTORE SPFILE TO PFILE '/u01/app/oracle/product/12.1.0/dbhome_1/dbs/initDUP.ora' FROM AUTOBACKUP;
	}
	```
	The same password used to encrypt the backup must be used for restore and recovery operations.
	If the TDE wallet was used to encrypt the backup, the wallet must be copied to the new host and the wallet location must be set in the `sqlnet.ora` file before restoration is started. Also, use `SET ENCRYPTION ON;` instead of `SET DECRYPTION IDENTIFIED BY 'my_bkup_pwd';` as shown in the example above.
	See [My Oracle Support Note 1560327.1](https://support.oracle.com/epmos/faces/DocContentDisplay?id=1560327.1).
3. Edit the PFILE to reflect the new host, changing control file locations, create and recovery file destinations, and audit file destinations. For example, change the `*_dest` parameters so all destinations are correct, change the `control_files` parameter, and so on. If necessary, create the relevant directories on the new host.
4. Shut down the target database instance on the new host, restart the instance to the `NOMOUNT` state, restore the control file, and mount the database.
	For example:
	```md
	RMAN> SHUTDOWN IMMEDIATE;
	RMAN> STARTUP NOMOUNT;
	RMAN> RUN {
	ALLOCATE CHANNEL t1 DEVICE TYPE sbt PARMS 'SBT_LIBRARY=libopc.so ENV=(OPC_PFILE=/u01/app/oracle/product/12.1.0/dbhome_1/dbs/opcDUP.ora)';
	RESTORE CONTROLFILE FROM AUTOBACKUP;
	}
	RMAN> ALTER DATABASE MOUNT;
	```
5. If necessary, use the `SET NEWNAMES` command to define a new location for the restored data file (Oracle Database 10g and later) or database (Oracle Database 11g and later), and then start the restoration and recovery.
	For example:
	```md
	RMAN> RUN {
	SET NEWNAME FOR DATABASE TO '/u02/app/oracle/oradata/DUP/%U';
	ALLOCATE CHANNEL t1 DEVICE TYPE sbt PARMS 'SBT_LIBRARY=libopc.so ENV=(OPC_PFILE=/u01/app/oracle/product/12.1.0/dbhome_1/dbs/opcDUP.ora)';
	ALLOCATE CHANNEL t2 DEVICE TYPE sbt PARMS 'SBT_LIBRARY=libopc.so ENV=(OPC_PFILE=/u01/app/oracle/product/12.1.0/dbhome_1/dbs/opcDUP.ora)';
	ALLOCATE CHANNEL t3 DEVICE TYPE sbt PARMS 'SBT_LIBRARY=libopc.so ENV=(OPC_PFILE=/u01/app/oracle/product/12.1.0/dbhome_1/dbs/opcDUP.ora)';
	RESTORE DATABASE;
	SWITCH DATAFILE ALL;
	SQL "ALTER DATABASE RENAME FILE ''+DATA/ASMDEMO1/ONLINELOG/group_3.263.873380343'' TO ''/u04/app/oracle/redo/redo03.log''";
	SQL "ALTER DATABASE RENAME FILE ''+FRA/ASMDEMO1/ONLINELOG/group_3.260.873380343'' TO ''/u04/app/oracle/redo/redo01.log''";
	SQL "ALTER DATABASE RENAME FILE ''+DATA/ASMDEMO1/ONLINELOG/group_2.262.873380341'' TO ''/u04/app/oracle/redo/redo02.log''";
	SQL "ALTER DATABASE RENAME FILE ''+FRA/ASMDEMO1/ONLINELOG/group_2.259.873380341'' TO ''/u04/app/oracle/redo/redo04.log''";
	SQL "ALTER DATABASE RENAME FILE ''+DATA/ASMDEMO1/ONLINELOG/group_1.261.873380341'' TO ''/u04/app/oracle/redo/redo05.log''";
	SQL "ALTER DATABASE RENAME FILE ''+FRA/ASMDEMO1/ONLINELOG/group_1.258.873380341'' TO ''/u04/app/oracle/redo/redo06.log''";
	}
	```
6. Find the system change number (SCN) to make the database consistent:
	```md
	RMAN> RESTORE DATABASE PREVIEW DEVICE TYPE SBT;
	```
	The output includes the name and location of backup pieces that will be used when restoring the database.
7. Recall any required backup pieces that were archived.
	If the `RESTORE...PREVIEW` command output contains a section named *List of remote backup files*, it means that some required backup pieces were archived. Recall these backup pieces using the following command:
	```md
	RMAN> RESTORE DATABASE PREVIEW RECALL DEVICE TYPE SBT;
	```
8. Restore the database using the following command:
	```md
	RESTORE DATABASE DEVICE TYPE SBT;
	```
9. Recover the database to that point:
	```md
	RMAN> RECOVER DATABASE DEVICE TYPE SBT UNTIL SCN scn;
	```
	where `scn` is the SCN identified in the previous step.
	For Oracle Database 12c Release 2 (12.2) and higher, you can use the `RECOVER DATABASE UNTIL AVAILABLE REDO` command.
10. Open the database with the `RESETLOGS` option after restore and recovery is complete:
	```md
	RMAN> ALTER DATABASE OPEN RESETLOGS;
	```

### Creating a Data Guard Standby Database in Oracle Cloud

To deploy a disaster recovery site for an on-premises production database using Oracle Database Cloud Service or Oracle Database Exadata Cloud Service, you need to create a standby database in the cloud to be used with Oracle Data Guard or Oracle Active Data Guard.

One way to create a standby database is to restore the backup performed from the on-premises production database.

## Troubleshooting Oracle Database Backup Cloud Service

You might encounter some problems when you use Oracle Database Backup Cloud Service.

This section lists common problems and their possible solutions. For detailed information, see:

- Oracle Database Backup Cloud Service FAQ: [My Oracle Support Note 1640149.1](https://support.oracle.com/epmos/faces/DocContentDisplay?id=1640149.1).
- Cloud Backup Performance Analysis: [My Oracle Support Note 2078576.1](https://support.oracle.com/epmos/faces/DocContentDisplay?id=2078576.1).

**Topics**

- Problems with Installing the Backup Module
- Problems with Backing Up and Restoring
- Problems with Connectivity

### Problems with Installing the Backup Module

The following solutions apply if you run into issues when you install the Oracle Database Cloud Backup Module.

For general information about installation, see Installing the Oracle Database Cloud Backup Module for OCI or Installing the Oracle Database Cloud Backup Module for OCI Classic.

**Note:**

Before you review the information in this section, ensure to verify these additional items:

- **Java SE Development Kit:** Default JDK version supported by the target Oracle Database release.
- **Identity domain name or service name:** Ensure that the domain name or service name is spelled correctly
- **Backup module:** Ensure that you have installed the Oracle Database Cloud Backup module on the target database server.
- **Proxy or firewall issues:** Ensure that your proxy is set up correctly, and you can reach general URLs from your system

**I get a Request to set the lifecycle policy failed error**

Specific error:

```md
Exception in thread "main" java.lang.RuntimeException:
SetBucketLCP: 400 Bad Request. at oracle.backup.opc.install.BmcConfig.SetBucketLCP(BmcConfig.java:851)
  at oracle.backup.opc.install.BmcConfig.setBucket(BmcConfig.java:620)
  at oracle.backup.opc.install.BmcConfig.doBmcConfig(BmcConfig.java:236)
  at oracle.backup.opc.install.BmcConfig.main(BmcConfig.java:219)
Failed: 1 ()
```

`SetbucketLCP` is setting the lifecycle policy on the bucket, which means `enableArchive` was set to True. But the Object Storage service in the region was not granted the permission to manage objects, and hence the request to set the lifecycle policy failed.

Authorize the Object Storage service to move backups to Archive Storage. See *Service Permissions* in the [Required IAM Policies](https://docs.cloud.oracle.com/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm#Service) section of the Oracle Cloud Infrastructure documentation.

**I get an HTTP response code error when I run the installer for Oracle Cloud Infrastructure Classic**

Specific error:

```md
Server returned HTTP response code: 504 for URL:
https://identityDomain.storage.oraclecloud.com/v1/storage-identityDomain/?format=xml
```

Use the `-host` parameter when you run the installer, instead of the `-serviceName` and `-identityDomain` parameters. For example:

`https://swiftobjectstorage.us-ashburn-1.oraclecloud.com/v1/hr-abc`

Exclude `/?format=xml` at the end of the URL. For information about these parameters, see Parameters to Run the Oracle Database Cloud Backup Module for OCI Classic Installer.

**I get a ConfigFile was not specified error when I run the installer**

Specific error:

```md
ConfigFile was not specified, and a default location could not be
determined because ORACLE_HOME and ORACLE_SID are not both set.
```

Set `ORACLE_HOME` and `ORACLE_SID` and rerun the installer.

**I get a Specified directory does not exist error when I run the installer**

Specific error:

```md
Specified directory /home/oracle/OPC/lib does not exist.
```

The directory specified for the `-libDir` parameter does not exist. Create the directory and rerun the installer.

**I get a java.io.IOException or java.io.FileNotFound error when I run the installer**

For example:

```md
java.io.IOException: Server returned HTTP response code: 401 for
the URL URL-name
```

The installer can’t connect to Oracle Cloud with the information you provided. Try the following:

- Make sure the user name, password, service name, and identity domain used to run the installer are correct. With Oracle Cloud Infrastructure, make sure that the user OCID, tenancy OCID, fingerprint, and keys are correct.
	Enclose the user name and password in single quotes, for example `'myAccount@myCompany.com'` and `'opc_pswd'`. On Windows systems, use double quotes if the user name or password contains special characters.
	Fix any errors and rerun the installer. If the information you provided is correct, contact Oracle Support to verify your account information.
	**Note:** If you have a pre-paid metered subscription for Oracle Cloud Infrastructure Classic, the default service name is `Storage` (case sensitive). This is the name you’ll use for the `-serviceName` parameter when you install the backup module.
- Check connectivity and see if you can reach the cloud storage endpoint URL from your database server. For example:
	```md
	$ ping storage.us2.oraclecloud.com
	PING storage.us2.oraclecloud.com (160.34.0.51): 56 data bytes
	64 bytes from 160.34.0.51: icmp_seq=0 ttl=239 time=63.738 ms
	64 bytes from 160.34.0.51: icmp_seq=1 ttl=239 time=67.288 ms
	```

**I get a Could not authenticate or 403 Forbidden error when I run the installer for Oracle Cloud Infrastructure Classic**

This could be because you need to select a data center. See Request Trial or Paid Subscription to Oracle Database Backup Cloud Service.

The replication policy must be set before you run the backup module installer. Otherwise you’ll get errors such as `Could not authenticate to Oracle Database Cloud Backup Module` or `403 Forbidden`. Set the replication policy and wait at least 10 minutes for synchronization to complete before you retry the installation.

**I get a Failed to load Media Management Library error**

If you’re on a Windows system and keep getting System or Media Management Loading errors, your Windows environment could be missing C libraries needed by the RMAN backup module. Download the Redistributable Package for Visual Studio 2013 from [`https://www.microsoft.com/en-us/download/details.aspx?id=40784`](https://www.microsoft.com/en-us/download/details.aspx?id=40784). Choose the 64-bit version and run the downloaded EXE file. This should resolve the problem.

If the problem persists, run the following operating system command (all platforms):

`sbttest -f foo.txt -libname full-path-to-libopc|oraopc-library`

The output shows why the module is not being loaded.

**I’m using a Solaris 64-bit operating system and keep getting ORA-27211 - Failed to load Media Management Library**

Installation is most likely failing because the `libc.so.1` file does not exist in your environment. Confirm this by running the following operating system command:

`sbttool -f foo.txt -libname full-path-to-libopc.so`

To resolve the issue, set the operating system variable `LD_LIBRARY_PATH_64` to the 64-bit library path that has the `libc.so.1` file. If that doesn’t resolve the issue and you’re using an Oracle Solaris release earlier than Solaris 10 Update 10 (s10u10), upgrade your system to at least s10u10.

**I get an Exception in thread error when I run the installer**

Specific error:

```md
Exception in thread "main" java.io.FileNotFoundException:
orclhome/dbs/opcdb1210.ora (No such file or directory)
```

The installer can’t create the configuration file under the `ORACLE_HOME/dbs` directory. Make sure the directory is accessible. Also make sure the path for `ORACLE_HOME` is set correctly.

**I get a PKIX path building failed: unable to find valid certification path to requested target error when I run the installer**

Your database server’s Java keystore does not have the SSL certificate of Oracle Cloud. You can work around this problem by using the `-no-check-certificate` option from the command line.

**The wallet directory can’t be created by the installer**

Make sure the path you specified is correct, and the user account (`oracle`, for instance) has read/write/execute (rwx) access to that path. Alternatively, create a wallet directory and use that as the location for the `-walletDir` parameter.

**I have a pre-paid metered subscription and don’t know what service name to use to install the Oracle Database Cloud Backup Module for OCI Classic**

If you have a pre-paid metered subscription, the service name is `Storage` (case sensitive). This is the name you’ll use for the `-serviceName` parameter when you install the backup module.

### Problems with Backing Up and Restoring

The following solutions apply if you run into issues when you perform cloud backup and restore operations.

For general information about cloud backups and restores, see Backing Up to Oracle Database Backup Cloud Service and Restoring Backups from Oracle Database Backup Cloud Service.

**I get an RMAN encryption error when I try to back up**

Specific error:

```md
RMAN-03009: failure of backup command on ORA_SBT_TAPE_1 channel at 08/15/2014 14:00:43
ORA-27030: skgfwrt: sbtwrite2 returned error
ORA-19511: non RMAN, but media manager or vendor specific failure, error text:
   KBHS-01602: backup piece 14p0jso8_1_1 is not encrypted
```

Backups must be encrypted before they can be sent to the cloud. Specify encryption and try backing up again.

**I changed my password for Oracle Cloud and now my backups to Oracle Cloud Infrastructure Classic are failing**

When you change your password for Oracle Cloud, you also need to update your password in the wallet used for backing up to Oracle Cloud Infrastructure Classic. Credentials in the wallet are used to authenticate to the cloud before backup data is sent. If the password isn’t updated in the wallet, the backup fails because of the incorrect password.

To update the password in the wallet, rerun the Oracle Database Cloud Backup Module for OCI Classic installer with the new credentials. See Run the Backup Module for OCI Classic Installer.

If you are using Oracle Database Cloud Service or Oracle Database Exadata Cloud Service and use object storage for backups, you need to update the password used for backing up after you change your password for Oracle Cloud. For Database Cloud Service, see [Updating the Password for Backing Up to the Storage Cloud](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/bradv&id=CSDBI-GUID-92F8D8CC-478E-405E-A60F-F10F8FF3C611) in *Using Oracle Database Cloud Service*. For Exadata Cloud Service, see [Updating the Password for Backing Up to the Storage Cloud](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/bradv&id=CSEXA-GUID-92F8D8CC-478E-405E-A60F-F10F8FF3C611) in *Using Oracle Database Exadata Cloud Service*.

**I get a Request Entity Too Large error when I try to back up**

When you subscribe to Oracle Database Backup Cloud Service, you purchase the amount of storage capacity you want. If you reach your storage capacity limit and try to back up your database, your backup will fail. An error related to this might look as follows:

```md
RMAN-00571: ===========================================================
RMAN-00569: =============== ERROR MESSAGE STACK FOLLOWS ===============
RMAN-00571: ===========================================================
RMAN-03009: failure of backup command on c1 channel at 12/02/2014 16:35:58
ORA-27030: skgfwrt: sbtwrite2 returned error
ORA-19511: Error received from media manager layer, error text:
KBHS-01404: See trace file /u01/app/oracle/admin/proddb/diag/rdbms/proddb/trace/
sbtio_5884_123456.log for details
KBHS-00700: HTTP response error 'Request Entity Too Large'
```

You can quickly increase the limit by purchasing more storage capacity on demand. Once you buy more capacity, you can continue doing backups. You can also use the RMAN `DELETE` operation to free up space. As a best practice you should set up a proper retention period and periodically run RMAN backup management operations such as `CROSSCHECK`, `OBSOLETE`, and `DELETE`.

You can monitor how much storage capacity you’ve used by viewing detailed metrics. You can also check the capacity used by your account or under a container by using cURL. See Monitoring Your Storage Capacity.

**I’m on a Windows system and keep getting System or Media Management Loading errors when I try to back up. How do I resolve this?**

Your Windows environment could be missing C libraries needed by the RMAN backup module. Download the Redistributable Package for Visual Studio 2013 from [`https://www.microsoft.com/en-us/download/details.aspx?id=40784`](https://www.microsoft.com/en-us/download/details.aspx?id=40784). Choose the 64-bit version and run the downloaded EXE file. This should resolve the problem.

**How do I get more information when a backup fails?**

Add the following parameter to the `opcSID.ora` configuration file to enable tracing, and then rerun the RMAN command:

`_OPC_TRACE_LEVEL=100`

This adds trace data to the `sbtio.log` file. To disable tracing, remove the `_OPC_TRACE_LEVEL` parameter or set the value to 0.

For information about the `opcSID.ora` configuration file, see Files Created When the Oracle Database Cloud Backup Module for OCI Classic is Installed.

**I get an error when I use password-based encryption for my backup**

Specific error:

```md
RMAN-03009: failure of backup command on ORA_SBT_TAPE_1 channel at 08/15/2014 11:10:57
ORA-19914: unable to encrypt backup
ORA-28361: master key not yet set
```

You probably did not include the `ONLY` parameter when you specified password encryption. It should be something like this:

```md
RMAN> SET ENCRYPTION ON IDENTIFIED BY 'my_pswd' ONLY;
```

**I used password-based encryption for my backup and forgot the password - how do I restore the backup?**

If you forget or lose the password, you cannot restore the backup. The password used to encrypt a backup must also be used to decrypt it for restore and recovery operations.

**RMAN restores from another location, not the cloud**

Use `SHOW ALL` to confirm that RMAN is configured to use Oracle Database Backup Cloud Service as the backup destination. See [Configuring Autobackups](rman-cloud-settings.md). Also check for proper syntax.

### Problems with Connectivity

The following solution applies if you run into issues when you try to connect to Oracle Database Backup Cloud Service.

**I get connectivity errors from my database server**

This could be caused by any number of things, including network bandwidth issues and incorrect proxy settings. Test to see if you can reach general URLs from your system.