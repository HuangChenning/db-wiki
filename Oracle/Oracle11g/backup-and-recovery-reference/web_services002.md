---
title: Getting Started
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/web_services002.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

To use OSB Cloud Module on Amazon S3, you must set up both an Oracle Technical Network (OTN) and an Amazon Web Services (AWS) account. You also need the S3 Backup installer and a compatible version of Java software.

Here are the steps to set up, install, verify and run the OSB Cloud Module:

| Steps | Description |
| --- | --- |
| 1 | Hardware and Software Prerequisites |
| 2 | Registering for An Oracle Technology Network (OTN) Account |
| 3 | Signing Up For Amazon S3 - AWS Account |
| 4 | Getting Your AWS Identifiers |
| 5 | Installing the OSB Cloud Module Library |
| 6 | Running the S3 Backup Installer - Verifying Java Version - Verifying `$ORACLE_HOME` |
| 7 | Storing Configuration in RMAN Repository - optional |
| 8 | Using the OSB Web Services Library and First Backup |

## Hardware and Software Prerequisites

The prerequisites for the OSB Cloud Module:

| Hardware/Software | Version |
| --- | --- |
| Java | JDK 1.5 or later on the computer where you plan to run the S3 Backup Installer |
| Supported Platforms | - Linux x86 - Linux x86-64 - Microsoft Windows (32-bit) |
| Oracle Database | You can backup databases starting with Oracle Database 9 `i` Release 2 or later. Operating system files cannot be backed up with RMAN or the RMAN SBT interface. |
| S3 Backup Installer File | `osbws_install.jar`  The installer downloads the library that is appropriate for the platform it is running on. It also creates the library configuration file and the Oracle Wallet where the AWS credentials are stored.  If you are using Oracle provided Amazon Machine Images (AMIs) to run the Oracle Database on Amazon's Elastic Compute Cloud (EC2), then the installer can be found in the `/home/oracle/scripts` directory. Otherwise, you can download the file from the Cloud Computing Center link found on the Oracle Technical Network (OTN) website at  `http://www.oracle.com/technetwork/topics/cloud/downloads/index.html`  Oracle recommends that users include any of the command-line options in a file and secure the file with appropriate operating system permissions. The S3 Backup Installer can then read the file, invoke the options, and prohibit unauthorized users from reading the file. |
| Oracle Wallet Directory | The Oracle Wallet Directory stores your AWS identifiers and must exist before you can run the S3 Backup installer. If you have not set up a wallet directory then you must create one.  Here are the suggested platform-specific locations for the wallet directory:  - Linux: `$ORACLE_HOME/dbs/osbws_wallet` - Windows: `$ORACLE_HOME\database\osbws_wallet` |
| System Time | The authentication method used by S3 relies on the client's system time being similar to S3's time. In this case, the client is the computer where you run the OSB Web Services library. S3 time is Coordinated Universal Time (UTC), so you must ensure that the system time on your client is within a few minutes of UTC. |

## Signing Up For Amazon S3 - AWS Account

Before you can use the OSB Cloud Backup Module and access Amazon S3, you must create an AWS account.

You can open one at: `http://aws.amazon.com`, using the upper right-hand corner link: "Create an AWS Account".

The account requires that you provide a means of payment for Amazon to charge for your AWS S3 usage.

## Getting Your AWS Identifiers

You need the two AWS Identifiers that are assigned when you create your AWS account:

- Access Key ID
- Secret Access Key

You obtain these two credentials by:

- Going to the AWS website at: `http://aws.amazon.com`
- Pointing to "Your Web Services Account" to display a list of options
- Clicking on "AWS Access Identifiers" link and logging in to your AWS account.

Note: It is a good idea to secure these credentials since they authorize charges for all Amazon Web Services and enable access to RMAN backups stored on Amazon S3.

## Installing the OSB Cloud Module Library

If this is the first time you run the S3 Backup installer, Oracle recommends that you run it initially without any parameters to get a listing and explanation of the mandatory and optional parameters. Analyzing and reviewing this information before executing the S3 Backup installer helps to ensure a successful installation.

To run the S3 Backup installer without parameters, type:

```
% java -jar osbws_install.jar
```

The explanation for the various parameters in the out put of the first run follows:

```
-AWSID:       AWS Access Key ID
-AWSKey:      AWS Secret Access Key
```

The credentials for Amazon Web Services. Mandatory.

```
-otnUser:     OTN Username
-otnPass:     OTN Password
```

The credentials for OTN, which the installer uses to identify the customer. Mandatory.

```
-walletDir:   Directory to store wallet
```

The location for the Oracle Wallet used to store S3 credentials and proxy information (if specified, see below). Mandatory.

Note: The Oracle wallet directory must exist before running the S3 Backup installer. Consult Hardware and Software Prerequisites for more information.

```
-configFile:   File name of config file
```

The location where the configuration file will reside. If omitted, the installer creates the configuration file and place it in a default system-dependent location. Optional.

Default Linux location: `$ORACLE_HOME/dbs/osbsws<ORACLE_SID>.ora`

Default Windows location: $ `ORACLE_HOME\database\osbsws<ORACLE_SID>.ora`

```
-libDir:      Directory to store library
```

The location where the library is placed. If this parameter is omitted, the installer does not download the library. Optional.

Suggested Linux location: $ `ORACLE_HOME/lib/`

Suggested Windows location: $ `$ORACLE_HOME\bin\`

```
-libPlatform:   The desired platform for the library
```

The install tool determines the platform automatically by examining the system where it is running. This parameter allows specifying it explicitly. Optional.

In this version the supported values for the parameter are: linux32, linux64, windows32.

```
-proxyHost:   HTTP proxy server
-proxyPort:   HTTP proxy server port
-proxyID:     HTTP proxy server username
-proxyPass:   HTTP proxy server password
```

The name and port of the HTTP proxy server, if required. If the proxy server is specified, the user name and password, if required. Optional.

Steps 1 through 4 help you identify all the mandatory parameters and needed set up information for the installer. Check and collect the relevant information for any optional parameters that you want to include. For example, you may need to know the proxy server name, port and credentials of your installation.

At this point, you are ready to execute the installer.

## Running the S3 Backup Installer

Oracle recommends running the Java installer in a secure mode, so avoid running it directly from the command line. A preferred method is to include the command-line options in a file and secure access to the file with the appropriate operating system permissions:

```
% java -jar osbws_install.jar -ARGFILE filename
```

Another method is to embed the run command, parameters and values in a file that can be executed as either a shell script or a Windows batch file.

Follow these steps:

- Create a file
- Set file permissions to grant owner of the file exclusive access
	Note:
	Setting the file permissions to restrict access is critical since the file contains both AWS and OTN credentials.
- Edit the file to contain a single line with the installer's run command and the mandatory parameters. You can compose a one-line invocation by populating the parameters with the information you obtained in the previous section.
- Execute the file as a shell script or Windows batch file

Note: To make the following example easier to read, `$ORACLE_HOME` is set to `/orclhome`. In your installation, the value of `$ORACLE_HOME` is something like `/usr/oracle/product/11.2.0` (Linux).

Example C-1 Running the S3 Backup Installer

The following shows a sample run of the S3 Backup installer under Linux.

The first thing to do is to verify that the correct version of Java is present on the computer and that `$ORACLE_HOME` is defined.

Enter the following commands and review the output:

```
% java -version
java version "1.5.0_11"
Java(TM) 2 Runtime Environment, Standard Edition (build 1.5.0_11-b03)
Java HotSpot(TM) Client VM (build 1.5.0_11-b03, mixed mode)
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

Edit the file and add a line to invoke the installer.

```
java -jar osbws_install.jar -AWSID access key ID -AWSKey secret key -otnUser jane.smith@example.com  -otnPass password for OTN -walletDir $ORACLE_HOME/dbs/osbws_wallet  -libDir $ORACLE_HOME/lib/ -proxyHost www-proxy.example.com
```

Execute the file.

```
% ./osbws.sh
```

Here is the start of the S3 Backup installer output:

```
OTN userid is valid.
AWS credentials are valid.
Creating new registration for this S3 user.
Created new log bucket.
Registration ID: 0f0a8aac-dad0-6254-7d70-be4ac4f112c4
S3 Logging Bucket: oracle-log-jane-smith-1
Create credential oracle.security.client.connect_string1
OSB web-services wallet created in directory /orclhome/dbs/osbws_wallet.OSB web-services initialization file /orclhome/dbs/osbwst1.ora created.
Downloading OSB Web Services Software Library.
Downloaded 13165919 bytes in 204 seconds. Transfer rate was 64538 bytes/second.
Download complete.
Extracted file /orclhome/lib/libosbws11.so
```

When the installer completes, you should have these three files on your system:

1. The OSB Web Services Library
2. The Configuration file
3. The OSB Web Services Wallet

Note: The installer requires both the OTN and AWS credentials to create the wallet and perform other installation operations. Only your AWS credentials are retained when the installer has finished and they are stored in the Oracle Wallet. The AWS credentials are used solely to authenticate the library's interactions with S3 and are not used or sent anywhere else.

## Storing Configuration in RMAN Repository - optional

To avoid having to provide the configuration information each time a backup is invoked, it is a good idea to store the OSB Cloud Module configuration information in the RMAN repository.

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

## Using the OSB Web Services Library and First Backup

You are now ready to connect to your target database and configure an RMAN channel. You must specify both the library and the configuration file in the command.

This example configures an RMAN channel for an Oracle 11g Release 2 database:

```
RMAN> run {
            allocate channel dev1 type
            sbt parms='SBT_LIBRARY=/orclhome/lib/libosbws11.so,
            SBT_PARMS=(OSB_WS_PFILE=/orclhome/dbs/osbwst1.ora)';
          }
```

At this point, you can issue your usual RMAN backup and restore commands.

Note: For Oracle 11g Release 2 databases and later, you must use the `SBT_PARMS` parameter for specifying environment variables. For pre-Oracle 11g Release 2 databases, you can still use the `ENV` parameter of the `PARMS` option to specify environment variables.

See Also:

Database Backup in the Cloud technical white paper and the Backup Up Database Demonstration on the OTN: Cloud Computing Center website