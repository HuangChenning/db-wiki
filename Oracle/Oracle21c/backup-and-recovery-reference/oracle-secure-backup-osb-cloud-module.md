---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/oracle-secure-backup-osb-cloud-module.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

The Oracle Secure Backup (OSB) Cloud Module enables you to take advantage of internet-based data storage services offered by Amazon Simple Storage Service (S3) for RMAN backup and recovery tasks.

This appendix contains the following topics:

### F.1 About Backup on the Cloud Using Oracle Secure Backup Cloud Module

The Oracle Secure Backup Cloud Module is part of the Oracle Secure Backup product family and provides the flexibility to back up your database to the Amazon S3 Cloud and to tape. With this cloud offering, local disk backups are sent directly to Amazon S3 for offsite storage and are fully integrated with Recovery Manager (RMAN) features and functionality.

The Oracle Secure Backup Cloud Module efficiently handles the backing up of Oracle databases to S3 storage. You can backup Oracle databases starting with Oracle Database 9 `i` Release 2 or higher. In addition, Oracle Secure Backup Cloud Module backups work with tools like Oracle Enterprise Manager and your customized RMAN scripts. The Oracle Secure Backup Cloud Module does not back up operating system files.

The Oracle Secure Backup Cloud Module uses the RMAN SBT (System Backup to Tape) interface to extend the Amazon S3 functionality for Oracle backup operations. The Oracle Secure Backup Cloud Module offers an easy-to-manage, cost efficient, and scalable alternative to maintaining in-house data storage and managing a local, fully configured backup infrastructure.

The Oracle Secure Backup Cloud Module has several advantages over traditional tape-based offsite backups:

- Continuous Accessibility
	Oracle Secure Backup Cloud Module backups stored on Amazon S3 storage are always accessible. The cloud storage services availability and access model helps an organization to streamline recovery operations. For example, there is no need to ship or load tapes before a restore can be performed. You can still use familiar and standard tools like Enterprise Manager and your organization's current scripts continue to execute backup and restore tasks. With the ability to continually and easily access backups, the time spent restoring backups may be substantially reduced.
- Improved Reliability
	Because S3 storage is disk based, it is inherently more reliable than tape media. Internet storage service providers keep multiple, redundant copies of your data for availability and scalability purposes and the benefit of this practice to your organization and your data is increased reliability.

#### F.1.1 Configuration Parameters for the Oracle Secure Backup Cloud Module

Use configuration parameters to specify the settings that are used when performing backups with the Oracle Secure Backup Cloud Module.

Configuration parameters can be set in one of the following locations:

- Configuration file for the Oracle Secure Backup Cloud Module
	The name of the configuration file is specified in the `OSB_WS_PFILE` parameter
- `ENV` variable when configuring SBT channels

The following table describes the configuration parameters that can be set when using the Oracle Secure Backup Cloud Module.

| Parameter Name | Mandatory? | Description |
| --- | --- | --- |
| `OSB_WS_PFILE` | No | Indicates the configuration file for the SBT library. The default location for the configuration file is:  Linux: `?/dbs/osbws` `ORACLE_SID``.ora`  Windows: `?\database\osbws` `ORACLE_SID``.ora`  Here, `?` represents the `ORACLE_HOME` and `ORACLE_SID` represents the SID of the target database. |
| `OSB_WS_HOST` | Yes | Specifies the name of the host to which the backups are sent. |
| `OSB_WS_PROXY` | No | Specifies the proxy server and port when the target database is behind a firewall. It is specified in the \<host>:\<port> format. |
| `OSB_WS_BUCKET` | No | Specifies the bucket in which the SBT library stores backups. If this parameter is not specified, then the SBT library first attempts to find an existing bucket whose location matches the specified location from buckets whose names are prefixed with `oracle-data-` `account name` `-`. If no such bucket exists, then the SBT library creates a unique bucket with the above prefix. |
| `OSB_WS_LOCATION` | No | Specifies the Amazon S3 location where the backups must be stored. This value must match the location of the specified `OSB_WS_HOST` and the location of the `OSB_WS_BUCKET` (if specified). If this parameter is not specified, then the default Amazon S3 region is used.  Refer to the Amazon S3 documentation for a list of valid pairs of endpoints and locations. |
| `OSB_WS_CHUNK_SIZE` | No | Specifies the object size, in bytes, that will used when storing backups to Amazon S3. The default size is 100MB. |
| `OSB_WS_LICENSE_ID` | No | Specifies the unique license ID generated during installation for each AWS account.  The current installer does not perform registration and therefore, this parameter is available only for compatibility reasons. |
| `OSB_WS_LICENSE_MAX_SESSIONS` | No | Specifies the number of connection sessions that can run. The SBT library does not allow you to create more than the specified number of sessions at any given time. |
| `OSB_WS_WALLET` | Yes | Defines the wallet location, alias, and proxy authentication alias through which the SBT library reads credentials.  The format of this parameter is:  `LOCATION=<filename> CREDENTIAL_ALIAS=<alias> PROXY_AUTH_ALIAS=<alias>`  `LOCATION` defines the location of wallet, `CREDENTIAL_ALIAS` defines the alias in the wallet from which AWS credentials are retrieved, and `PROXY_AUTH_ALIAS` defines the alias in the wallet from which the proxy authentication credentials are retrieved. `PROXY_AUTH_ALIAS` is optional, the others are mandatory. |
| `OSB_WS_VIRTUAL_HOST` | No | Specifies the format of the host. The default value is TRUE.  When set to TRUE, the format is http\[s\]://\<bucket>.\<host>. When set to FALSE, the format is http\[s\]://\<host>/\<bucket>. Use FALSE when the storage provider is not Amazon S3, but is compatible with S3. |
| `OSB_WS_IAM_ROLE` | Yes, when using the metadata service. | Specifies the name of the IAM role that can be used to back up to Amazon S3. The Amazon EC2 instance must be configured with the specified IAM role. |
| `OSB_WS_IAM_ROLE_META_URI` | No | Specifies the name of the metadata URI where temporary credentials for the IAM role are stored. |
| `OSB_WS_PRIVATE_CLOUD` | No | This parameter is the same as `OSB_WS_VIRTUAL_HOST`. It is obsolete and is available only for compatibility reasons. |

### F.2 Using Oracle Secure Backup Cloud Module on Amazon S3

To use Oracle Secure Backup Cloud Module on Amazon S3, you must set up an Amazon Web Services (AWS) account. You also need the S3 Backup installer and a compatible version of Java software.

Here are the steps to set up, install, verify and run the Oracle Secure Backup Cloud Module:

| Steps | Description |
| --- | --- |
| 1 | Hardware and Software Prerequisites for Oracle Secure Backup Cloud Module |
| 2 | Signing Up For Amazon S3 - AWS Account |
| 3 | Getting Your AWS Identifiers |
| 4 | Installing the OSB Cloud Module Library |
| 5 | Running the S3 Backup Installer  - Verifying Java Version - Verifying `$ORACLE_HOME` |
| 6 | Storing Configuration Information in the RMAN Repository (Optional) |
| 7 | Using the OSB Web Services Library and First Backup |

#### F.2.1 Hardware and Software Prerequisites for Oracle Secure Backup Cloud Module

Certain hardware and software requirements must be met to use the Oracle Secure Backup Cloud module.

The following table lists the prerequisites for the Oracle Secure Backup Cloud Module:

| Hardware/Software | Version |
| --- | --- |
| Java | Java 1.7 or later on the computer where you plan to run the S3 Backup Installer |
| Supported Platforms | - Linux x86-64 - Microsoft Windows (64-bit) - Oracle Solaris on SPARC (64–bit) - Oracle Solaris X64 - ZLinux-64 - AIX (PPC64) - HP-UX IA64 	Note: HP-UX PA-RISC 64–bit is not supported. |
| Oracle Database | You can backup databases starting with Oracle Database 9 `i` Release 2 or later. Operating system files cannot be backed up with RMAN or the RMAN SBT interface. |
| S3 Backup Installer File | `osbws_install.jar`  The installer downloads the library that is appropriate for the platform it is running on. It also creates the library configuration file and the Oracle Wallet where the AWS credentials are stored.  If you are using Oracle provided Amazon Machine Images (AMIs) to run the Oracle Database on Amazon's Elastic Compute Cloud (EC2), then the installer can be found in the `/home/oracle/scripts ` directory. Otherwise, you can download the file from the Cloud Computing Center link found on the Oracle Technical Network (OTN) website at  [`http://www.oracle.com/technetwork/products/secure-backup/secure-backup-s3-484709.html`](http://www.oracle.com/technetwork/products/secure-backup/secure-backup-s3-484709.html)  Oracle recommends that users include any of the command-line options in a file and secure the file with appropriate operating system permissions. The S3 Backup Installer can then read the file, invoke the options, and prohibit unauthorized users from reading the file. |
| Oracle Wallet Directory | The Oracle Wallet Directory stores your AWS identifiers and must exist before you can run the S3 Backup installer. If you have not set up a wallet directory then you must create one.  Here are the suggested platform-specific locations for the wallet directory:  - Linux: `$ORACLE_HOME/dbs/osbws_wallet` - Windows: `$ORACLE_HOME\database\osbws_wallet` |
| System Time | The authentication method used by S3 relies on the client's system time being similar to S3's time. In this case, the client is the computer where you run the OSB Web Services library. S3 time is Coordinated Universal Time (UTC), so you must ensure that the system time on your client is within a few minutes of UTC. |

#### F.2.3 Signing Up For Amazon S3 - AWS Account

Before you can use the Oracle Secure Backup Cloud Backup Module and access Amazon S3, you must create an AWS account.

You can open one at: [`http://aws.amazon.com`](http://aws.amazon.com/). Click My Account and then select Security Credentials.

The account requires that you provide a means of payment for Amazon to charge for your AWS S3 usage.

#### F.2.4 Getting Your AWS Credentials

AWS credentials are required to back up to Amazon S3.

You can use one of the following techniques to authenticate and access Amazon S3:

- AWS Identifiers
	You obtain these credentials by going to the AWS website at [`http://aws.amazon.com`](http://aws.amazon.com/), selecting My Account, and then AWS Management Console.
	You need the following mandatory AWS identifiers that are assigned when you create your AWS account: Access Key ID and Secret Access Key.
	Note: It is a good idea to secure these credentials since they authorize charges for all Amazon Web Services and enable access to RMAN backups stored on Amazon S3.
- AWS IAM role
	Enables Amazon Elastic Cloud Compute (EC2) instance users to leverage the metadata service. When the EC2 instance is configured with an IAM role, applications running on EC2 can use temporary credentials associated with the IAM role to create backups to Amazon S3. EC2 stores the temporary credentials in a predetermined location in JSON format. The installer retrieves the temporary credentials and stores them in the Oracle wallet.
	The IAM role must have the privileges required to access Amazon S3.
	Provide the following parameters to use IAM roles: AWS IAM Role Name (mandatory) and Metadata URI for the specified IAM Role (optional).

See Also:

For more information about IAM roles for Amazon EC2, refer to: [`http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html`](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html)

#### F.2.5 Installing the OSB Cloud Module Library

The Oracle Secure Backup Cloud Module library needs to be installed before you can back up databases to Amazon S3 Cloud.

If this is the first time you run the S3 Backup installer, Oracle recommends that you run it initially without any parameters to get a listing and explanation of the mandatory and optional parameters. Analyzing and reviewing this information before executing the S3 Backup installer helps to ensure a successful installation.

To run the S3 Backup installer without parameters, type:

```
% java -jar osbws_install.jar
```

The following table provides an explanation for the various parameters used during installation.

Table F-1 Parameters Used when Installing the OSB Cloud Module Library

| Parameter Name | Description | Mandatory? |
| --- | --- | --- |
| `AWSID` | Access Key ID for the Amazon Web Services account that is used to store RMAN backups. | Yes, if you use AWS identifiers to authenticate with Amazon S3. |
| `AWSKey` | Secret access key for the Amazon Web Services account specified in `-AWSID`.  Note: To authenticate with Amazon S3, you must provide one of the following:  - `AWSID` along with `AWSKey` - `IAMRole` | Yes, if you use AWS identifiers to authenticate with Amazon S3. |
| `IAMRole` | AWS IAM (Identity and Access Management) role name that contains the temporary credentials that RMAN will use for backup and recovery operations. This role must be assigned the appropriate privilege to access your S3 account.  Note: To authenticate with Amazon S3, you must provide one of the following:  - `IAMRole` - `AWSID` along with `AWSKey` | Yes, if you use IAM roles to authenticate with Amazon S3. |
| `IAMRoleMetaURI` | Metadata URI where temporary credentials for the specified IAM role are stored. For Amazon EC2 users, specifying the metadata URI is optional. If this parameter is omitted, the temporary credentials are retrieved from the instance metadata. | No |
| `awsEndpoint` | Host name to which backups must be sent. If this parameter is omitted, backups will be stored on the default host. | No |
| `awsPort` | Non-default HTTP/HTTPS connection port number. The default port number for HTTP is 80 and HTTPS is 443. | No |
| `location` | Amazon S3 location where the RMAN backups must be stored. If specified, the value must match the location of the value of `awsEndPoint`. For third-party S3-compatible services, if a location is not required, set location to “us”.  Refer to the Amazon S3 documentation for a list of valid locations.. | No |
| `walletDir` | Location that stores the Oracle wallet that contains S3 credentials and proxy information.  The Oracle wallet directory must exist before running the S3 Backup installer.  Consult Hardware and Software Prerequisites for Oracle Secure Backup Cloud Module for more information. | Yes |
| `configFile` | Name, with the complete path, of the configuration file that will be created by the installer. The parameters that are used while running RMAN jobs are obtained from this configuration file.  If this parameter is omitted, the installer creates the configuration file and places it in a default system-dependent location.  Default Linux location: `$ORACLE_HOME/dbs/osbsws<ORACLE_SID>.ora`  Default Windows location: $ `ORACLE_HOME\database\osbsws<ORACLE_SID>.ora` | No |
| `libDir` | Directory into which the OSB Cloud Module library is downloaded. If this parameter is omitted, the installer does not download the library.  Suggested Linux location: $ `ORACLE_HOME/lib/`  Suggested Windows location: $ `$ORACLE_HOME\bin\` | No |
| `libPlatform` | Platform on which the library must be installed.  The install tool determines the platform automatically by examining the system where it is running. This parameter allows specifying it explicitly.  Supported values for the parameter are: linux64, windows64, solaris\_sparc64, solaris\_x64, hpux\_ia64  Note: The install tool determines the platform automatically by examining the system where it is running. This parameter allows specifying it explicitly. | No |
| `proxyHost` | Name of the HTTP proxy server, if required. If the proxy server is specified, then the `-proxyID` and `-proxyPass` parameters are required. | No |
| `proxyPort` | Port number of the HTTP proxy server. | No |
| `proxyID` | User name for the HTTP proxy server. | No |
| `proxyPass` | Password for the HTTP proxy server user | No |
| `trustedCerts` | List of SSL certificate to be imported into the Oracle wallet. | No |
| `argFile` | Name of the file from which arguments must be read during installation. To read arguments from the standard input, specify “-”. | No |
| `useHttps` | Sets up an HTTPS connection. If omitted, and HTTP connection is used. | No |
| `useSigV2` | Sets up an authentication scheme. If this parameter is specified, Signature Version 2 authentication is set up; else Signature Version 4 is set up. The recommended scheme is Signature Version 4. | No |

Check and collect the relevant information for any optional parameters that you want to include. For example, you may need to know the proxy server name, port and credentials of your installation.

At this point, you are ready to execute the installer.

#### F.2.6 Running the S3 Backup Installer

Oracle recommends running the Java installer in a secure mode, so avoid running it directly from the command line.

A preferred method is to include the command-line options in a file and secure access to the file with the appropriate operating system permissions:

```
% java -jar osbws_install.jar -ARGFILE filename
```

Another method is to embed the run command, parameters and values in a file that can be executed as either a shell script or a Windows batch file.

Follow these steps:

- Create a file
- Set file permissions to grant owner of the file exclusive access
	Note:
	Setting the file permissions to restrict access is critical since the file contains AWS credentials.
- Edit the file to contain a single line with the installer's run command and the mandatory parameters. You can compose a one-line invocation by populating the parameters with the information you obtained in the previous section.
- Execute the file as a shell script or Windows batch file

Note: To make the following example easier to read, `$ORACLE_HOME` is set to `/orclhome`. In your installation, the value of `$ORACLE_HOME` is something like `/usr/oracle/product/11.2.0 ` (Linux).

Example F-1 Running the S3 Backup Installer Using AWS Credentials

The following shows a sample run of the S3 Backup installer under Linux.

The first thing to do is to verify that the correct version of Java is present on the computer and that `$ORACLE_HOME` is defined.

Enter the following commands and review the output:

```
% java -version
java version "1.7.0"
Java(TM) SE Runtime Environment (build 1.7.0-b147)
Java HotSpot(TM) 64-Bit Server VM (build 21.0-b17, mixed mode)
```
```
% echo $ORACLE_HOME
/orclhome
```

Create a file that contains the installer's invocation line and ensure that the file permissions restrict access except to the file owner.

```
% touch osbws.sh
% chmod 700 osbws.sh
```

Edit the file and add a line to invoke the installer. This example uses AWS identifiers to authenticate.

```
java -jar osbws_install.jar -AWSID access key ID -AWSKey secret key -walletDir $ORACLE_HOME/dbs/osbws_wallet -libDir $ORACLE_HOME/lib/ -proxyHost www-proxy.example.com
```

Execute the file.

```
% ./osbws.sh
```

Here is the start of the S3 Backup installer output:

```
AWS credentials are valid.
Oracle Secure Backup Web Service wallet created in directory /orclhome/dbs/osbws_wallet.
Oracle Secure Backup Web Service initialization file /orclhome/dbs/osbwst1.ora created.
Downloading OSB Web Services Software Library.
Downloaded 13165919 bytes in 204 seconds. Transfer rate was 64538 bytes/second.
Download complete.
Extracted file /orclhome/lib/libosbws.so
```

When the installer completes, you should have these three files on your system:

1. The OSB Web Services Library
2. The Configuration file
3. The OSB Web Services Wallet

Note: The installer requires the AWS credentials to create the wallet and perform other installation operations. Only your AWS credentials are retained when the installer has finished and they are stored in the Oracle Wallet. The AWS credentials are used solely to authenticate the library's interactions with S3 and are not used or sent anywhere else.

Example F-2 Running the S3 Installer Using an IAM Role

This example shows a sample run of the S3 Backup installer on Linux using an IAM role names `s3access`.

`java -jar osbws_install.jar —IAMRole s3access walletDir $ORACLE_HOME/dbs/osbws_wallet -libDir $ORACLE_HOME/lib/ -proxyHost www-proxy.example.com`

Here is the start of the S3 installer output.

```
AWS credentials are valid.
Oracle Secure Backup Web Service wallet created in directory /orclhome/dbs/osbws_wallet.
Oracle Secure Backup Web Service initialization file /orclhome/dbs/osbwst1.ora created.
Downloading OSB Web Services Software Library.
Downloaded 13165919 bytes in 204 seconds. Transfer rate was 64538 bytes/second.
Download complete.
Extracted file /orclhome/lib/libosbws.so
```

#### F.2.7 Storing Configuration Information in the RMAN Repository (Optional)

To avoid having to provide the configuration information each time a backup is invoked, it is a good idea to store the Oracle Secure Backup Cloud Module configuration information in the RMAN repository.

This example is for a pre-11g Release 2 database:

```
RMAN> configure channel device type sbt parms  
"SBT_LIBRARY=/orclhome/lib/libosbwsll.so
ENV=(OSB_WS_PFILE=/orclhome/dbs/osbwst1.ora)';
```
```
using target database control file instead of recovery catalog
new RMAN configuration parameters:

"SBT_LIBRARY=/orclhome/lib/libosbwsll.so 
ENV=(OSB_WS_PFILE=/orclhome/dbs/osbwst1.ora)';
new RMAN configuration parameters are successfully stored
```

When this example completes, the system is configured for OSB Cloud Module backups and you can use your usual RMAN backup and restore commands.

Note: For 11g Release 2 databases and later, you must use the `SBT_PARMS` parameter to specify environment variables.

#### F.2.8 Using the OSB Web Services Library and First Backup

After installing and configuring the Oracle Secure Backup Cloud Module, you are ready to connect to your target database and configure an RMAN channel.

You must specify both the library and the configuration file in the command.

The following example configures an RMAN channel for an Oracle Database:

```
RMAN> run {
            allocate channel dev1 type
            sbt parms='SBT_LIBRARY=/orclhome/lib/libosbws11.so,
            SBT_PARMS=(OSB_WS_PFILE=/orclhome/dbs/osbwst1.ora)';
          }
```

At this point, you can issue your usual RMAN backup and restore commands.

Note: On Windows, Oracle recommends that you use the `SBT_PARMS` parameter to specify the environment variables, instead of the `ENV` parameter. For example, `PARMS 'SBT_PARMS=(OB_DEVICE_1=tape1)' 'SBT_LIBRARY=lib_name'`.

See Also:

Database Backup in the Cloud technical brief and the Backup Database Demonstration on the OTN: Cloud Computing Center website

### F.3 Securing OSB Cloud Module Backups

To ensure that your data is properly secured, Oracle recommends that you make RMAN backup encryption a standard part of your backup processes.

This recommendation is even more important to implement when you are storing critical backup data off-premises. Encrypting RMAN backups on Amazon S3 can also assist you in meeting key audit and regulatory compliance requirements for your organization's data.

See Also:

" [Encryption of Backup Sets](BACKUP.md) " for a discussion of RMAN encryption options.

### F.4 Helpful Links: Oracle Secure Backup Cloud Module

For more information on Oracle Secure Backup Cloud Module, see the Frequently Asked Questions (FAQ) in My Oracle Support Note 740226.1 at [`https://support.oracle.com/rs?type=doc&id=740226.1`](https://support.oracle.com/rs?type=doc&id=740226.1)

### F.5 Troubleshooting the OSB Cloud Module

This section lists potential issues that may affect the installation or the operation of the Oracle Secure Backup Cloud Module.

| Symptoms | Error Messages | Resolution |
| --- | --- | --- |
| The S3 Backup installation cannot create the license file on Amazon S3. | `Time-out waiting for license file to be created.` | The first time you run the S3 Backup installer for a set of AWS identifiers, the installer creates a license file on Amazon S3. If there are problems preventing its creation the time-out error message is displayed in the installation output.  Contact Oracle support to resolve the issue. |