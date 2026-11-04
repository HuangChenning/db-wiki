---
title: Oracle Database Cloud Backup Module for Azure
book: Backup and Recovery User Guide
doc_id: E96241-26
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/azure-sbt-module.html
tags:
  - oracle
  - 19c
  - backup-and-recovery-users-guide
---

Use the Oracle Database Cloud Backup Module for Azure to backup your Oracle Databases to Microsoft Azure Cloud Storage using RMAN.

## About Oracle Database Cloud Backup Module for Azure

You can use RMAN to backup Oracle Database 19c Release Update version 28 (19.28) or higher version to Azure Blob Storage containers.

The RMAN SBT library for Azure enables RMAN to communicate with the Oracle Database Cloud Backup Module to perform backup and recovery tasks with Azure Storage. Backups are directly stored in Azure blob containers.

Before creating backups to Azure, you must create an Azure Storage account and obtain the storage account credentials required for authentication. Next, set up the Oracle Database Cloud Backup Module for Azure on the target Oracle Database server. Finally, you must configure an RMAN SBT channel using the RMAN SBT library for Azure. This creates a persistent RMAN configuration for all backups and restores with Azure storage containers.

**Note:** The Oracle Database Cloud Backup Module for Azure is compatible with Oracle Databases deployed on-premises or on Azure virtual machines. Backups to Azure Blob Storage for Oracle Database Cloud Services are not available.

## Sign-up for a Microsoft Azure Blob Storage Account

To backup your Oracle Database to Microsoft Azure, you need an existing Microsoft Azure Blob Storage account.

Create a Microsoft Azure Storage account. See [Create an Azure storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal#create-a-storage-account).

Ensure to obtain these credentials associated with your Azure Storage account. These values are mandatory to set up the Oracle Database Cloud Backup Module for Azure.

- `storageaccount` - Azure Blob Storage Account Name
- `sharedkey` - Azure Blog Storage Account Key
- `container` - Azure Blob Container Name

## Set Up the Oracle Database Cloud Backup Module for Azure

Before you backup to Azure, you must set up the Oracle Database Cloud Backup Module for Azure on the target Oracle Database server.

The backup module setup tool `az_setup.zip` is available in the Oracle home directory after you install the Oracle Database.

***Table 32-1 File Name and Location of the Oracle Database Cloud Backup Module for Azure Setup Tool***

| Oracle Database Cloud Backup Module for Azure Setup Tool | Location on UNIX and Linux Systems | Location on Windows Systems |
| --- | --- | --- |
| `az_setup.zip` | `$ORACLE_HOME/lib` | `%ORACLE_HOME%\lib` |

### Prerequisites for the Oracle Database Cloud Backup Module for Azure

Verify these minimum requirements before you set up the Oracle Database Cloud Backup Module for Azure.

***Table 32-2 Minimum System Requirements for the Oracle Database Cloud Backup Module for Azure***

| System | Supported Versions |
| --- | --- |
| Oracle Database | - Oracle Database 19c Release Update version 28 (19.28) or higher versions - Oracle Database 23ai Release Update version 8 (23.8) or higher versions |
| Java SE Development Kit (JDK) | Default JDK version supported by the target Oracle Database release. |

### Parameters for Running the Oracle Database Cloud Backup Module for Azure Setup Tool

Review the mandatory parameters and compile their values before you set up the Oracle Database Cloud Backup Module for Azure.

After you install Oracle Database, the backup module setup tool `az_setup.zip` is available in the Oracle home directory (see Table 32-1).

Extract the `az_setup.zip` setup tool to a subdirectory of your choice. To preview the parameters, run this command from the subdirectory that contains the extracted setup files.

```md
$ java -jar az_setup.jar
```

***Example 32-1 Extracting the Oracle Database Cloud Backup Module for Azure Setup Files and Previewing the Parameters (on UNIX and Linux systems)***

In this example, extract the contents of the `az_setup.zip` file to the `azmodule` subdirectory.

```md
$ mkdir -p $ORACLE_HOME/lib/azmodule
$ cd $ORACLE_HOME/lib/azmodule
unzip -q $ORACLE_HOME/lib/az_setup.zip
```

To preview the parameters, run this command from the `azmodule` subdirectory that contains the extracted setup files.

```md
$ java -jar az_setup.jar
```

***Table 32-3 Parameters to Set Up the Oracle Database Cloud Backup Module for Azure***

| Parameter | Description | Required or Optional |
| --- | --- | --- |
| `-storageaccount` | The account name for your Microsoft Azure Blob Storage account used for RMAN backups. | Required |
| `-sharedkey` | The access key for the specified Microsoft Azure `-storageaccount`. | Required |
| `-container` | A custom container associated with the specified Azure `-storageaccount`.  When you backup to Azure, RMAN stores the backups in the specified container. The setup tool will create the specified container, if it does not exist.  Skip the `-container` parameter in these scenarios:  - If you want to store backups in a default container created by the setup tool. - If you want to store backups in an Azure immutable storage container instead of a regular container. In this case, specify the `-immutable-container` parameter. | - Required - If you want to store RMAN backups in an Azure Blob Storage container created by you. - Optional - If you want to store RMAN backups in the default container created by the setup tool or if you want to specify an immutable container to store backups. |
| `-immutable-container` | A WORM compliant (immutable) Azure storage container to store RMAN backups.  See [Microsoft Azure Immutable Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/immutable-storage-overview) for more information. | Optional |
| `-temp-metadata-container` | A container used to store temporary metadata during RMAN backup and recovery operations. | Required if you have specified a `-immutable-container`. |
| `-walletDir` | Directory that contains the Azure storage account credentials required to authenticate RMAN operations.  Create the wallet directory before you run the setup tool. If you skip this parameter, then the setup tool prompts you to enter the wallet directory. | Required |
| `-updateWalletNoValidate` | Updates the wallet without verifying the target host connection.  If you have changed the Microsoft Azure Blob Storage account credentials and want to update the existing wallet, then rerun the installer by specifying the `updateWalletNoValidate` and `walletDir` parameters to directly update the wallet without validating the host.  In this example, you run the installer with the `updateWalletNoValidate` parameter. `oracle/dbs/az_wallet` specifies the location of the wallet which contains the changed credentials. The installer directly updates the wallet without validating the target host connection, as shown in the sample output.  `java -jar az_setup.jar -storageaccount rmanDBbackup -sharedkey 67t7tninefkn -walletDir oracle/dbs/az_wallet -updateWalletNoValidate`  `Oracle Database Cloud Backup Module Setup Tool, build MAIN_2026-06-12`  `Oracle Database Cloud Backup Module wallet updated in directory oracle/dbs/az_wallet` | Optional |
| `-trustedCerts` | List of SSL certificates that needs to be imported into the Oracle wallet. | Required - If you want to manually add a list of SSL certificates to the wallet.  Optional - If you want the setup tool to retrieve the required SSL certificates. |
| `-configFile` | Specifies a custom name and location for the Azure backup module configuration file created by the setup tool. For example, `-configFile=/myfiles/azureconfig.ora`.  Skip the `-configFile` parameter if you want to create the configuration file in the default location chosen by the setup tool.  - Default location on `UNIX` and Linux systems: `$ORACLE_HOME/dbs` - Default location on Windows systems: `%ORACLE_HOME%\database`.  The default name for the configuration file is `az<ORACLE_SID>.ora`, where `<ORACLE_SID>` is the system identifier of the Oracle Database being backed up to Azure Blob Storage. | Optional |
| `-proxyHost` | HTTP proxy server host name | Optional |
| `-proxyPort` | HTTP proxy server port number | Optional |
| `-proxyId` | HTTP proxy server user name, if needed. | Optional |
| `-proxyPass` | HTTP proxy server password, if needed. | Optional |
| `-argFile` | A plain text file which contains the input parameters for the Azure Backup Module setup tool.  Specify `-argFile` and the filename if you want the setup tool to read the input parameters from a specified arguments file.  For example, assume that the `arguments.txt` file contains this parameter definition:  `-storageaccount "myStorageAccount" -sharedkey "myStorageAccountKey" -walletDir home/oracle/az_wallet -proxyHost www-proxy.example.com -proxyPort 80 -import-all-trustcerts`  This example shows that you can set up the backup module using the parameters specified in the `arguments.txt` file:  `java -jar az_setup.jar -argFile arguments.txt` | Optional |
| `-import-all-trustcerts` | Imports all `X509` certificates from Java truststore. This is the default behaviour. | Optional |
| `-import-current-trustcert-only` | Import current `X509` certificate from Java truststore. | Optional |

### Run the Setup for the Backup Module for Azure

Use these steps to set up the Oracle Database Cloud Backup Module for Azure on the target database server.

Before you begin, ensure to verify the prerequisites and compile the mandatory parameter values.

- Prerequisites for the Oracle Database Cloud Backup Module for Azure
- Parameters for Running the Oracle Database Cloud Backup Module for Azure Setup Tool
1. The Oracle Database Cloud Backup Module for Azure setup tool `az_setup.zip` is available in the Oracle home directory (see Table 32-1).
	Extract the `az_setup.zip` file to a subdirectory of your choice. In this example, you extract the setup files to the `azmodule` subdirectory.
	```md
	$ mkdir -p $ORACLE_HOME/lib/azmodule
	$ cd $ORACLE_HOME/lib/azmodule
	unzip -q $ORACLE_HOME/lib/az_setup.zip
	```
2. On the target database server, go to the directory where you have extracted the Azure Backup Module setup files.
	In this example, you go to the `azmodule` subdirectory which contains the `az_setup.jar` file and the README file `az_readme.txt`.
	```md
	$ cd $ORACLE_HOME/lib/azmodule
	```
3. Run the setup tool `az_setup.jar`. Specify the parameters and values as shown in this example.
	```md
	java -jar az_setup.jar
	-storageaccount rmanDBbackup
	-sharedkey aaaaaaaasd754pijuwheaq67t7tninefkn
	-container RMANbackupContainer
	-proxyHost www-proxy.example.com
	-walletDir oracle/dbs/az_wallet
	-proxyPort 80
	```

The Oracle Database Cloud Backup Module for Azure setup tool creates these files:

- Configuration file `az<ORACLE_SID>.ora`, where `<ORACLE_SID>` is the system identifier of the Oracle Database that is being backed up to Azure storage.
	By default, the configuration file is located in the `$ORACLE_HOME/dbs` directory on `UNIX` and Linux systems. On Windows systems, the default location of the configuration file is `%ORACLE_HOME%\database.`
- Oracle wallet file, that securely stores the Microsoft Azure Storage account credentials. RMAN requires the wallet file for authentication during backup and restore operations with Azure blob containers..
1. Review the output.
	This example shows a sample run of the setup tool. The setup tool creates the wallet file `az_wallet` and the configuration file. `azsbt.ora`.
	```md
	Oracle Database Cloud Backup Module Setup Tool, build 23.8.0.25.04
	Oracle Database Cloud Backup Module credentials are valid.
	Backups would be sent to container RMANbackupContainer.
	Oracle Database Cloud Backup Module wallet created in directory /oracle/dbs/az_wallet.
	Oracle Database Cloud Backup Module initialization file /oracle/dbs/azsbt.ora created.
	```

## Configuration Parameters Created by the Oracle Database Cloud Backup Module for Azure

The setup tool creates the configuration file with parameter values required for RMAN operations with the Oracle Database Cloud Backup Module for Azure.

You can optionally modify the parameter values in the configuration file.

***Table 32-4 Configuration Parameters To Specify Settings for the Oracle Database Cloud Backup Module for Azure***

| Parameter Name | Mandatory? | Description |
| --- | --- | --- |
| `AZ_HOST` | Yes | Specifies the name of the host to which the RMAN backups are sent. |
| `AZ_PROXY` | No | Specifies the proxy server and port when the target database is behind a firewall. It is specified in the `<host>:<port>` format. |
| `AZ_CONTAINER` | No | Specifies the Azure Blob Storage container in which RMAN stores the database backups. If this parameter is not specified, then the SBT library first attempts to find an existing bucket in the specified location and named in the format *oracle-data-account name-*. If no such bucket exists, then the SBT library creates a unique bucket with the *oracle-data-account name-* prefix. |
| `AZ_TEMP_CONTAINER` | No | Name of the Azure Blob Storage container that stores the temporary files associated with immutable backups. The backup module requires the temporary container for backup operations.  Create a separate container to store the temporary files. Run the setup tool by specifying the container name in the `-temp-metadata-container` parameter.  Alternatively, you can define the `-temp-metadata-container` value in the `az.ORACLE_SID.ora` configuration file after you run the setup tool. |
| `AZ_CHUNK_SIZE` | No | Specifies the object size, in bytes, that will used when storing backups to Azure Blob Storage. The default chunk size is 100MB. |
| `AZ_WALLET` | Yes | Defines the wallet location, alias, and proxy authentication alias through which the SBT library reads the Azure account credentials. The format of this parameter is: `LOCATION` = `<wallet filename>` `PASSWORD=<wallet password>` `CREDENTIAL_ALIAS=<alias>` ` PROXY_AUTH_ALIAS=<alias>`.  `LOCATION` defines the location of wallet, and `PASSWORD` defines the password used to open the wallet. `CREDENTIAL_ALIAS` defines the alias in the wallet from which Azure Blob Storage account credentials are retrieved, and `PROXY_AUTH_ALIAS` defines the alias in the wallet from which the proxy authentication credentials are retrieved. `PROXY_AUTH_ALIAS` is an optional parameter. |

## Configuring SBT Channel for Azure Storage

Configure an automatic SBT channel so that RMAN can directly send backups to Azure Blob Storage containers.

1. Start RMAN and connect to the target database.
2. Use the `CONFIGURE` command to preconfigure an automatic `sbt` channel. Specify the `oracle.azure` `SBT_LIBRARY` alias of the Oracle-supplied native SBT library for RMAN operations with Microsoft Azure. You can optionally specify the native SBT library path instead of the library alias.
	```md
	RMAN>
	CONFIGURE DEFAULT DEVICE TYPE sbt;
	CONFIGURE CHANNEL DEVICE TYPE 'SBT'
	PARMS 'SBT_LIBRARY=oracle.azure,
	ENV=(AZ_PFILE=myfiles/az<ORACLE_SID>.ora)';
	```
	You can optionally specify the native SBT library path instead of the library alias, as shown below.
	```md
	RMAN>
	CONFIGURE DEFAULT DEVICE TYPE sbt;
	CONFIGURE CHANNEL DEVICE TYPE 'SBT'
	PARMS 'SBT_LIBRARY=$ORACLE_HOME/lib/libaz.so,
	SBT_PARMS=(AZ_PFILE=myfiles/az<ORACLE_SID>.ora)';
	```
	```md
	RMAN> CONFIGURE DEFAULT DEVICE TYPE sbt;
	CONFIGURE CHANNEL DEVICE TYPE 'SBT'
	PARMS 'SBT_LIBRARY=oracle.azure,
	ENV=(AZ_PFILE=C:\myfiles\az<ORACLE_SID>.ora)';
	```
	You can optionally specify the native SBT library path instead of the library alias, as shown below.
	```md
	RMAN> CONFIGURE DEFAULT DEVICE TYPE sbt;
	CONFIGURE CHANNEL DEVICE TYPE 'SBT'
	PARMS 'SBT_LIBRARY=%ORACLE_HOME%\bin\oraaz.dll,
	SBT_PARMS=(AZ_PFILE=C:\myfiles\az<ORACLE_SID>.ora)';
	```
	This example configures an automatic channel to send all RMAN backups to tape by default. The `SBT_LIBRARY` parameter specifies the Azure Backup Module library `oracle.azure` that enables RMAN backups to Azure Blob Storage containers. The `ENV` parameter (UNIX and Linux) or the `SBT_PARMS` parameter (Windows) specifies the Azure Backup Module configuration file `azORACLE_SID.ora` which provides the parameters required for RMAN jobs. *`ORACLE_SID`* is the system identifier of the target Oracle Database being backed up to Microsoft Azure Blob Storage.
	**Note:**
	- On Windows systems, use the `SBT_PARMS` parameter instead of the `ENV` parameter to specify the configuration file.
	- You can skip the `ENV` or `SBT_PARMS` parameter if the configuration file is created in the default directory chosen by the backup module setup tool.
	- An automatic SBT channel creates a persistent default SBT device setting that applies to all backup and recovery operations. Alternatively, you can use the `ALLOCATE CHANNEL` command to manually allocate a one-time SBT channel before each backup or restore operation.
3. Use the `SHOW` command to review the RMAN configuration and to confirm that you have set Azure as the backup destination.
	In this example, you run the `SHOW ALL CHANGED` command to view the RMAN configuration changes for the `sales` database.
	```md
	RMAN> SHOW ALL CHANGED;
	show all changed;
	using target database control file instead of recovery catalog
	RMAN configuration parameters for database with db_unique_name sales are:
	CONFIGURE DEFAULT DEVICE TYPE TO 'SBT_TAPE';
	CONFIGURE DEVICE TYPE 'SBT_TAPE' PARALLELISM 3 BACKUP TYPE TO BACKUPSET;
	CONFIGURE CHANNEL DEVICE TYPE 'SBT_TAPE' PARMS  'SBT_LIBRARY=/oracle/lib/libaz.so, ENV=(AZ_PFILE=/myfiles/azsbt.ora)';
	```

## Backup and Restore with Azure Storage Using RMAN

After you set up the Oracle Database Backup Module for Azure and configure a corresponding SBT channel, use this procedure to directly backup and restore with Azure blob storage.

1. Start RMAN and connect to the target database.
2. Run the `SHOW ALL CHANGED` command to verify that the RMAN environment is configured for backups with Azure Blob Storage.
	```md
	RMAN> SHOW ALL CHANGED;
	```
	This sample configuration indicates that the `SBT_TAPE` channel is configured to use the `oracle.azure` SBT library. The default device type is set to `'SBT_TAPE'` which indicates that Azure Storage is the default backup destination.
	```md
	show all changed;
	using target database control file instead of recovery catalog
	RMAN configuration parameters for database with db_unique_name sales are:
	CONFIGURE DEFAULT DEVICE TYPE TO 'SBT_TAPE';
	CONFIGURE DEVICE TYPE 'SBT_TAPE' PARALLELISM 3 BACKUP TYPE TO BACKUPSET;
	CONFIGURE CHANNEL DEVICE TYPE 'SBT_TAPE' PARMS  'SBT_LIBRARY=oracle.azure';
	```
3. Run the `BACKUP DATABASE` command (see the sample output).
	```md
	BACKUP DATABASE;
	```
	```md
	backup database;
	Starting backup at 06-FEB-25
	allocated channel: ORA_SBT_TAPE_1
	channel ORA_SBT_TAPE_1: SID=61 device type=SBT_TAPE
	channel ORA_SBT_TAPE_1: Oracle Database Azure Backup Service Library VER 23.8.
	allocated channel: ORA_SBT_TAPE_2
	channel ORA_SBT_TAPE_2: SID=204 device type=SBT_TAPE
	channel ORA_SBT_TAPE_2: Oracle Database Azure Backup Service Library VER 23.8
	allocated channel: ORA_SBT_TAPE_3
	channel ORA_SBT_TAPE_3: SID=193 device type=SBT_TAPE
	channel ORA_SBT_TAPE_3: Oracle Database Azure Backup Service Library VER 23.8
	channel ORA_SBT_TAPE_1: starting full datafile backup set
	```
4. Run the `RESTORE` and `RECOVER` commands to recover the target database using backups stored in Azure Storage.
	```md
	RESTORE DATABASE;
	RECOVER DATABASE;
	```