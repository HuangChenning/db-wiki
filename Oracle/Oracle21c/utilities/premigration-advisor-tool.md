---
title: Utilities
book: Oracle AI Database Utilities Guide
doc_id: F30732-30
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sutil/premigration-advisor-tool.html
tags:
  - oracle
  - 21c
  - utilities
---

## 19 Cloud Premigration Advisor Tool

To evaluate the compatibility of the source database before you migrate to an Oracle Cloud database, use the Cloud Premigration Advisor Tool (CPAT).

**Parent topic:** [Other Utilities](other-oracle-utilities.md)

### 19.1 What is the Cloud Premigration Advisor Tool

The Cloud Premigration Advisor Tool (CPAT) is a migration assistant that analyzes database metadata in an Oracle Database, and provides information to assist you to move data to Oracle Autonomous Database in Oracle Cloud.

The purpose of the Cloud Premigration Advisor Tool (CPAT) is to help plan successful migrations to Oracle Databases in the Oracle Cloud or on-premises. It analyzes the compatibility of the source database with your database target and chosen migration method, and suggests a course of action for potential incompatibilities. CPAT provides you with information to consider for different migration tools.

Running the Cloud Premigration Advisor Tool does not require any changes to the source database. It does not require adding users, or granting roles, or loading packages.

How the Cloud Premigration Advisor Tool Works

The Cloud Premigration Advisor Tool performs source database metadata checks, and provides you with information for your migration. It does not perform the actual migration. You use that information as part of your migration plan. CPAT runs using Java 7 or later releases, Java 8 Java Runtime Environment ( JRE) preferred.

Note:

Installing and running CPAT does not modify Oracle Database. CPAT does not create any users, any packages, or require granting any roles or privileges. CPAT treats the database as `READ                     ONLY`.

A **check** is something that can be determined programmatically about a database, database object, user, or component. Checks are intended to determine the suitability of the database and database schema for moving to a particular Oracle Cloud Database deployment option. For example: Oracle Autonomous Database on Shared Exadata Infrastructure (ADB-S), using a particular migration method, such as Oracle Data Pump.

The source database is the database that you want to analyze for suitability to migrate to an Oracle Autonomous Database. The target is either a particular Oracle Autonomous Database, or a generic Oracle Autonomous Database deployment option that you can select when you run CPAT.

You start CPAT by running it either as Java command-line tool, or as a SQL command-line tool, using SQLcl. You then specify a source database and an Oracle Autonomous Database target, or specify `DEFAULT` for other Oracle Cloud Infrastructure (OCI) target databases, such as Exadata Cloud@Customer, Exadata Cloud Service, or an on-premises database. CPAT performs a number of checks on the source database and schema contents. These checks are guided by the target that you select, and your intended migration option.

After CPAT completes the source database checks, it generates a report indicating what was found. Reports contain both summary information and details for each check including the check result: Passing, Review Suggested, Review Required, or Action Required. In addition, CPAT identifies additional metadata in the source database that can be relevant for the migration.

The check results are compiled and presented in a report. The report can be a machine-readable report (`JSON`), a human-readable format (plain text, or HTML, or both). If the you do not specifiy a specific report type on the command line with `--reportformat`, then by default CPAT will generate both Text and HTML reports. These reports can also be used directly by other Oracle migration products and features, such as Oracle Zero Downtime Migration (ZDM) Cloud Service, and the Oracle Cloud Infrastructure (OCI) Database Migration Service. You can specify

Premigration Advisor Tool Properties

You can specify how CPAT runs, and what checks it performs, by specifying properties in the command line to provide information for its analysis checks.

Cloud Premigration Advisor Tool Reports

CPAT recommends any relevant actions, such as using certain migration commands, setting certain database parameters, or performing SQL scripts on either the source or target instance, because the checks can be performed on target deployment options, as well as actual database targets, the reports use the term "Locus" instead of "Target" when something needs to be completed on either the Source or Target database. When the report recommends that you use particular parameters and commands, Oracle strongly recommends that you follow the guidance in the report.

**Related Topics**

- [Cloud Premigration Advisor Tool (CPAT) Analyzes Databases for Suitability of Cloud Migration (Doc ID 2758371.1)](https://support.oracle.com/rs?type=doc&id=2758371.1)

**Parent topic:** Cloud Premigration Advisor Tool

### 19.2 Prerequisites for Using the Cloud Premigration Advisor Tool

Ensure that you have the required Java environment, user permissions and security set up to run the Cloud Premigration Advisor Tool (CPAT).

Java Runtime Environment (JRE) Requirement

You must have Java 7 or later installed on the server or client where you run CPAT. Oracle recommends that you use Java 8 Java Runtime Environment (JRE).

CPAT looks for a JRE using the environment variables `JAVA_HOME` and `ORACLE_HOME`. If your source Oracle Database is later than Oracle 12c Release 1 (12.1.0.2), then a version of the Java JRE that can run CPAT is available in the Oracle home. If you are migrating from an earlier release of Oracle Database, or if you want to specify to use a later Java release Oracle home, then ensure that the environment variable is set to an appropriate Java home for CPAT.

If you use a thick Oracle Call Interface-based JDBC connect string, then CPAT currently expects the following environment variables to be set: `ORACLE_SID`, `ORACLE_HOME`, and `LD_LIBRARY_PATH`.

Note:

Oracle recommends that you set `ORACLE_SID`, `ORACLE_HOME`, and `LD_LIBRARY_PATH` by using the `oraenv` script available within the Oracle Database home.

More details on connect strings and associated environment variables can be found in the Advanced Usage Notes section titled [Connection Strings](https://support.oracle.com/epmos/faces/DocumentDisplay?parent=DOCUMENT&sourceId=2758371.1&id=2758371.1#connection_strings).

User Privileges on the Source Database

When you specify a user to connect to the source database for checks, and provide that user with the CPAT `--username` property, the user name that you specify must be granted the `SELECT ANY DICTIONARY` privilege, and be granted `SELECT` on `SYSTEM.DUM$COLUMNS` and `SYSTEM.DUM$DATABASE`.

Access to the `DUM$` tables is needed only if the source and target character sets indicate that Oracle Database Migration Assistant for Unicode (DMU) is required.

Note:

Installing and running CPAT does not modify the Oracle Database. CPAT creates no users or packages, and CPAT does not grant any roles or privileges. The CPAT access to the database is `READ                     ONLY`. It only checks database metadata; no application or business data is checked.

Security Configuration

- Use the `--outdir` property to set the output location of CPAT logs and uses a secure location on your server or client.
- Set the user file creation mode mask (`umask`) on Linux and Unix systems so that the default values for the `r|w|x` privileges on CPAT scripts are restricted to authorized users.

**Parent topic:** Cloud Premigration Advisor Tool

### 19.3 Downloading and Configuring Cloud Premigration Advisor Tool

Download the most recent update to the Cloud Premigration Advisor Tool (CPAT), extract it to a directory, and set up environment variables.

To run CPAT, download the latest version from My Oracle Support, as described in the procedure.

If you cannot access My Oracle Support, then you can use Oracle SQLcl and the SQLcl command `- MIGRATEADVSOR`. You can download SQLcl from the following URL:

[https://www.oracle.com/database/sqldeveloper/.](https://www.oracle.com/database/sqldeveloper/)

1. Read the My Oracle Support note about CPAT, and download and extract the CPAT patch from the following URL:
	[Cloud Premigration Advisor Tool (CPAT) Analyzes Databases for Suitability of Cloud Migration (Doc ID 2758371.1)](https://support.oracle.com/rs?type=doc&id=2758371.1).
	You require an Oracle account to log in to My Oracle Support.
2. Ensure that you have Java installed, and the `JAVA_HOME` user environment variable and other environment variables are set.
	After you download and unzip CPAT, ensure that you have an appropriate Java Runtime Environment (JRE) installed on the machine where CPAT is run. The minimum JRE version required for CPAT is Java 7.
	CPAT searches for a JRE home using the environment variables `JAVA_HOME` and `ORACLE_HOME`. If the version of Java in ORACLE\_HOME is Java 6 or an earlier release, which should only be the case with an Oracle Database 12g Release 1 or earlier home, then set `JAVA_HOME` to point to a Java 7 (or higher) JRE. To upgrade Java in an ORACLE\_HOME, visit [https://support.oracle.com](https://support.oracle.com/) and search for Document 2366614.1 (patch id 25803774) for Oracle Database 11g databases, or Document 2495017.1 (patch id 27301652) for Oracle Database 12.1 databases.
	To set `JAVA_HOME` on a Microsoft Windows system:
	1. Right click My Computer and select Properties.
		2. On the Advanced tab, select Environment Variables, and then edit `JAVA_HOME` to point to the location of the of the Java Runtime Environment (JRE).
		For example:
		```
		C:\Program Files\Java\jdk1.8\jre
		```
		JRE is part of the Java Development Kit (JDK), but you can download it separately.
	To set `JAVA_HOME` on a Linux or Unix system (Korn or Bash shell):
	```
	export JAVA_HOME=jdk-install-dir
	export PATH=$JAVA_HOME/bin:$PATH
	```
	Note:
	On Linux and Unix, systems, Oracle recommends that you set the `ORACLE_SID`, `ORACLE_HOME,` and `LD_LIBRARY_PATH` variables using the `oraenv` script that comes with Oracle Database.
	If you want to use CPAT without defining ORACLE\_HOME, and you don't need to use the Oracle Call interface JDBC connection string, then ensure that `JAVA_HOME` is set to a Java 7 (or higher) JRE. When possible, Oracle recommends that you use a Java 8 or higher JRE. Among other benefits, the functionality included in `OJDBC8` jars simplifies wallet-based connections such as those used when connecting to Oracle Cloud instances.

**Related Topics**

- [Cloud Premigration Advisor Tool (CPAT) Analyzes Databases for Suitability of Cloud Migration (Doc ID 2758371.1)](https://support.oracle.com/rs?type=doc&id=2758371.1)

**Parent topic:** Cloud Premigration Advisor Tool

### 19.4 Getting Started with the Cloud Premigration Advisor Tool (CPAT)

After you download Oracle SQLcl or CPAT, ensure that your source database has the required Java home, set up environment variables, and decide what kinds of checks you want to perform.

The workflow for using the Cloud Premigration Advisor tool (CPAT) is as follows:

1. Determine the type of Cloud database to which you want to migrate.
2. Run CPAT to generate a CPAT properties file using the `gettargetprops`. This switch gathers the properties of the target database, if one has been created. The target properties are used when analyzing the source database to focus, and limits the checks that are run to those required for the target database.
3. Run CPAT with the options required for your migration scenario. You can run CPAT to test different migration scenarios. If you do run CPAT repeatedly, then to distinguish between the tests, Oracle recommends using the `--outfileprefix` and `--outdir` switches to keep the outputs organized, and to keep reports from being overwritten.

The CPAT patch distribution kit contains `premigration.sh` for running CPAT on Linux and Unix platforms, and `premigration.cmd` for running CPAT on Microsoft Windows platforms. CPAT can be run from any host with network access to the database instance that you want to analyze.

Note:

Running the premigration script on the server doesn't modify Oracle Database. CPAT itself creates no users or packages, and requires granting no roles or privileges. CPAT treats the database as `READ ONLY`. It only checks database metadata; no application or business data is checked.

In this example, `premigration.sh` is used (use `premigration.cmd` on Microsoft Windows systems)

Example 19-1 Generating a CPAT Properties File

This example checks whether your source database is ready to migrate to an Oracle Autonomous Database Shared for Transaction Processing and Mixed Workloads (ATP-S), you generate a properties file for the requirements:

```
premigration.sh --connectstring \
'jdbc:oracle:thin:@db_tp_tunnel?TNS_ADMIN=/path/to/wallets/Wallet1' --username ADMIN \
--gettargetprops --outdir migration
```

The output of that command is as follows:

` Enter password for ADMIN user: Cloud Premigration Advisor Tool                     Version 22.10.0 Cloud Premigration Advisor Tool generated properties file                     location:                     /home/oracle/migration/configprops/atps_premigration_advisor_analysis.properties`

Note:

When CPAT is run with the `--username` switch, the Oracle user name you specify must have the `SELECT ANY DICTIONARY` privilege, and must be granted `SELECT` on `SYSTEM.DUM$COLUMNS` and `SYSTEM.DUM$DATABASE`. Access to the `DUM$` tables is needed only if the source and target character sets indicate that Oracle Database Migration Assistant for Unicode (DMU) is required.

**Parent topic:** Cloud Premigration Advisor Tool

### 19.5 Connection Strings for Cloud Premigration Advisor Tool

The Cloud Premigration Advisor Tool (CPAT) accepts standard Oracle JDBC format connection strings.

Using standard Oracle JDBC format connection strings means that you can use either the thick" or the "thin" Oracle JDBC driver for connections.

Table 19-1 Example JDBC Connection Strings

| Connection Description | Connection String | Notes |
| --- | --- | --- |
| Thin client | `jdbc:oracle:thin:@host:port:sid` | Replace the variables `host`, `port` and `sid` with the host the connection port, and the system identifier for your source. |
| Thin client with PDB Service | jdbc:oracle:thin:@host:port/pdb-service-name | Replace the variables `host`, `port` and `pdb-service-name` with the host the connection port, and the PDB service name for your source. |
| Thin with AWS RDS | `jdbc:oracle:thin:@database-1.xxx.us-east-1.rds.amazonaws.com:port:sid` | Consult the Amazon Web Services Relational Database (AWS RDS) documentation for instructions on finding your database's endpoint and port details. |
| Operating system authentication | `jdbc:oracle:oci:@` | The CPAT command line must also include the property `--sysdba` |
| Operating system authentication with PDB | `jdbc:oracle:oci:@` | The CPAT command line must also include the properties `--sysdba` and `--pdbname                                         pdb-name`, where `pdb-name` is the name of the PDB. |
| Wallet-based with Java 8 JRE | `` jdbc:oracle:thin:@service-name?TNS_ADMIN=`path-to-wallet` `` | The `TNS_ADMIN` connection property specifies the following, represented by `path-to-wallet`:  The location of `tnsnames.ora`.  The location of Oracle Wallet (`ewallet.sso`, `ewallet.p12`) or Java KeyStore (JKS) files (`truststore.jks`, `keystore.jks`).  The location of `ojdbc.properties`. This file contains the connection properties required to use Oracle Wallets or Java KeyStore (JKS).  For more information about using a keystore, see the Oracle Autonomous Database documentation. |

Additional Connection String Information

Using the `--pdbname` property is only required when the connection string is for `CDB$ROOT`.

If you use keystore connection strings such as `jdbc:oracle:thin:@service-name?TNS_ADMIN=path-to-wallet`, then JDBC requires that one of the following is true:

- An `ojdbc.properties` file is located in the Wallet directory, and it contains `oracle.net.wallet_location property ` with a value such as `oracle.net.wallet_location=(SOURCE=(METHOD=FILE)(METHOD_DATA=(DIRECTORY=${TNS_ADMIN})))`
- The `JAVA_TOOL_OPTIONS` environment variable is set with the appropriate values, such as the following:
	`export                                 JAVA_TOOLS_OPTIONS='-Doracle.net.tns_admin=path-to-wallet-dir                                 -Doracle.net.wallet_location=(SOURCE=(METHOD=FILE)(METHOD_DATA=(DIRECTORY=path-to-wallet-dir)))'`

**Related Topics**

- [Oracle Database Insider: Migrating from AWS RDS to Oracle Autonomous Database via Data Pump](https://blogs.oracle.com/database/post/migrating-from-aws-rds-to-oracle-autonomous-database)
- [Using Oracle Autonomous Database on Shared Exadata Infrastructure: Using a JDBC URL Connection String with JDBC Thin Driver and Wallets](https://docs.oracle.com/en/cloud/paas/autonomous-database/adbsa/connect-jdbc-thin-wallet.html#GUID-1640CC02-BF3E-48C2-8FFE-A596614A6A40)

**Parent topic:** Cloud Premigration Advisor Tool

### 19.6 Required Command-Line Strings for Cloud Premigration Advisor Tool

Depending on your use case, some strings are required to run the Cloud Premigration Advisor Tool (CPAT).

When using CPAT to analyze a source database, three properties are required in the command string: one specifying the cloud target (`targetcloud`), one specifying the connection string (`connectstring`), and one for user authentication provided either with the `sysdba` or `username` property.

The first two required command-line properties are:

- `--targetcloud type` (or `-t                         type`), where `type is                     the Oracle Cloud target type`
- `--connectstring jdbc-connect-string`, or `-c jdbc-connect-string`, where `jdbc-connect-string` is the JDBC connection string you use to connect to the migration source Oracle Database.

The other required property provides user credentials, and so it depends on what user credentials you use to start the analysis:

- For operating system authentication by user account, or authorization on the local system by using the `SYS` user, you use `--sysdba`, or `-d`. This starts CPAT by connecting to the source database with `AS SYSDBA`. This authentication option is also required if you connect as a user that has been granted `SYSDBA` but not the other privileges required by CPAT.
- For user account-based authentication, where you are not using a wallet or operating system authentication, use `--username name`, or `-u name`, where `name` is the user account name you use to log in to the source system. CPAT prompts you for the user password. The provided username must be granted both the `SYSDBA` and `ADMIN` privileges.
	If you authenticate CPAT with the `username` property, then the Oracle user name that you specify must have the `SELECT ANY DICTIONARY` privilege, and must be granted `SELECT` on `SYSTEM.DUM$COLUMNS` and `SYSTEM.DUM$DATABASE`. Access to the `DUM$` tables is only required if migration involves Oracle Database Migration Assistant for Unicode (DMU), based on the source and target character set compatibility.

Command-Line Interface and Load Password Modes.

Starting with CPAT 25.6, CPAT supports a Command-Line Interface (CLI) mode.

In CLI mode, you can run source analysis interactively for one or more databases at a time. The "load password" option lets you store encrypted database credentials in a local keystore, which enables you to run automated, unattended analysis. When you combine CLI mode with the `--noconsole` flag, CPAT runs multiple analyses sequentially without users prompts.

Load Password Mode enables users to store encrypted database credentials in a local keystore. This mode enables CPAT to run multiple analyses sequentially without prompts.

Command-line mode:

```
/premigration.sh --parfile <config-file-path>
#No console mode:
/premigration.sh --noconsole --parfile <config-file-path>
#Load password mode:
/premigration.sh --parfile <config-file-path> --loadpassword
```

The following is an example configuration file (for multiple databases):

```
# Database 1
a.targetcloud=ATPD
a.reportformat=json,text,html
a.outfileprefix=DB1
a.username=SYSTEM
a.connectstring=<connectstring>
a.migrationmethod=GOLDENGATE,DATAPUMP
a.full=true
a.pdbname=ORCLPDB1

# Database 2
b.targetcloud=ATPD
b.reportformat=json,text,html
b.outfileprefix=DB2
b.username=SYSTEM
b.connectstring=<connectstring>
b.migrationmethod=GOLDENGATE,DATAPUMP
b.full=true
b.pdbname=ORCLPDB1

# Database 3
c.targetcloud=ATPD
c.reportformat=json,text,html
c.outfileprefix=DB3
c.username=SYSTEM
c.connectstring=<connectstring>
c.migrationmethod=GOLDENGATE,DATAPUMP
c.full=true
c.pdbname=ORCLPDB1
```

In this example, you load passwords into CPAT using the Load Password mode:

```
Managing Credentials with Load Password Mode (example):
Starting CPAT Password Loader - Type help for available options
Creating new CPAT keystore - Password required
Enter password:
Enter password again:
CPAT keystore was successfully created

>> add orcdb2 -user system
Enter your secret/Password:
Re-enter your secret/Password:
Done
Database Name Space: orcdb2      User: system

>> list
Database Name Space: orcdb2      User: system

>> add orcdb2 -user SYSTEM -nocheck
Replacing existing entry system.
Enter your secret/Password:
Re-enter your secret/Password:
Done
Database Name Space: orcdb2      User: system

>> exit
Save the CPAT keystore before exiting [YES|NO]? yes
Convert the CPAT keystore to auto-login [YES|NO]? yes
```

These features enhance automation, security, and flexibility when executing CPAT across multiple environments. For a complete list of supported options and usage patterns, refer to CPAT’s --help output or consult the official documentation.

**Parent topic:** Cloud Premigration Advisor Tool

### 19.7 FULL Mode and SCHEMA Mode

The Cloud Premigration Advisor Tool (CPAT) can run against the entire instance, or against a schema.

FULL Mode

`FULL` mode is the default mode. In this mode, CPAT runs any check relevant to the migration methods and the Cloud target types you choose, and analyzes data in all schemas that are not maintained by Oracle. In `FULL` mode, `SCHEMA`, `INSTANCE`, and `UNIVERSAL` scope checks are run.

Note:

Even in `FULL` mode, CPAT by default excludes checking data in schemas known to be maintained by Oracle. The use of the `--excludeschemas` property does not change CPAT's default `FULL` mode.

SCHEMA Mode

SCHEMA mode is set with the `--schemas` property. When `--schemas` is set, and `--full` is not also specified, then CPAT runs in `SCHEMA` mode. In `SCHEMA` mode, `SCHEMA` and `UNIVERSAL` scope checks are run. `INSTANCE` scope checks are not run.

Controlling CPAT Modes

The CPAT mode is controlled by the use of two options properties:

- The schemas property (`--schemas 'schemaname' ['schemaname''schemaname']`, runs checks against the schemas that you list, in a space-delimited schema name list of one or more schema names, where the names are specified within single straight quotes. In schema mode, `SCHEMA` and `UNIVERSAL` scope checks are run. `INSTANCE` scope checks are not run.
- The Full property (`--full`) runs checks against the entire source database instance.

If you do not specify a value for the `--schemas` property, then the default is `FULL` mode.

If you specify `--schemas` on the command line, then CPAT runs in `SCHEMA` mode unless you also specify `--full` in the command line. If both properties are used, then `SCHEMA`, `INSTANCE`, and `UNIVERSAL` scope checks are run, but only on the list of schemas in the `-schemas` list.

If a schema name is lowercase, mixed case, or uses special characters, then use double quotation marks as well as single quotation marks to designate the schema name. For example:

`premigration.sh --schemas 'PARdUS' '"ComEDIT"' '"faciem.$meam"'                     --targetcloud ATPS --connectstring jdbc-connect-string"`

**Parent topic:** Cloud Premigration Advisor Tool

### 19.8 Interpreting Cloud Premigration Advisor Tool (CPAT) Report Data

Reports generated by CPAT contain summary information, and details for each check that is performed successfully.

Each check includes the following information in the Premigration Advisor report:

- Description: This field describes what the check is looking for, or why the check is being performed.
- Impact: This field describes the consequences of a result other than Passing.
- Action: This check describes what, if anything, you should do before migration to correct issues, if the check result is not Passing.

Each check CPAT runs is given a report status of Passing, Review Suggested, Review Required, or Action Required.

The overall result of the CPAT report will be the most severe result of all checks performed. For example, if 30 checks have the status Passing, one check has a Review Required status, then the overall result will be Review Required.

The current definitions of each of the CPAT check results are as follows:

Table 19-2 Premigration Advisor Tool (CPAT) Check Result Definitions

| Check | Definition |
| --- | --- |
| Passing | Indicates that the migration should succeed, and that there should be no difference in behavior of applications. |
| Review Suggested | Indicates that migration should succeed, and that applications likely will have no functional difference. However, database administrators should evaluate each check with this status to look for potential issues before migration. |
| Review Required | Indicates that migration may succeed (at least in part), but that either you cannot expect everything to work exactly as it did in the source database, or that a database administrator must complete additional work after migration to bring the target instance into alignment with the source database. |
| Action Required | Indicates something that likely would cause the migration to be unsuccessful. Checks with this result typically must be resolved before attempting migration. |
| Failed | The Cloud Premigration Advisor was unable to complete its analysis. Please contact Oracle Support Services. |

Note: A CPAT result of Action Required does not necessarily mean that, for instance, Oracle Data Pump import will terminate prematurely while importing the data. It means that there will likely be errors during import which can indicate not all data has been migrated. It is imperative that an administrator familiar with both the database and the applications supported by the database examine the results of any checks that are not Passing.

Why are Checks sometimes marked as "skipped"

Checks marked in the Premigration Advisor report as `Skipped` should have completed during the CPAT analysis for properties provided in the CPAT command (for example, `--targetcloud` `--migrationmethod`, or other report value), but were not run in this particular Premigration Advisor report.

Either one of these two cases are the cause of a "Skipped" status:

- The check should be run but it is impossible to run at the time the report is generated, either due to the current contents or configuration of the source database. In this case, the check result will be Review Suggested or more severe.
- The check does not need to be completed at the time of the report, due to the current contents or configuration of the source database. The check result in this case will be Passing.

**Parent topic:** Cloud Premigration Advisor Tool

### 19.9 Command-Line Syntax and Properties

Use the Cloud Premigration Advisor Tool (CPAT) properties to specify the checks and other operations you want to perform in CPAT command-line syntax.

- Premigration Advisor Tool Command-Line Syntax  
	You run the Premigration Advisor Tool as a command-line shell script.
- Premigration Advisor Tool Command-Line Properties  
	Review the Premigration Advisor Tool properties to construct a command tree and options for your Oracle Database migration scenario.

**Parent topic:** Cloud Premigration Advisor Tool

#### 19.9.1 Premigration Advisor Tool Command-Line Syntax

You run the Premigration Advisor Tool as a command-line shell script.

Prerequisites

- You must have Java Development Kit (JDK) 7 or later installed in your source environment. Oracle recommends that you use Java 8 Runtime Environment (JRE).
	JDK 8 is installed with every release starting with Oracle Database 12c Release 2 (12.2). For any release earlier than 12.2, you must either run Premigration Advisor Tool (CPAT) using the Java release in the target Oracle Database, or you must install JDK 8 on your source database server.

Java File Path

Obtain the latest CPAT zip file from My Oracle Support. The application and deployment instructions for the application are available from My Oracle Support note 2758371.1. Because CPAT is a Java-based tool, it requires that an appropriate Java Runtime Environment (JRE) is installed on the machine where the tool is run.

For thin clients, CPAT searches for a Java Runtime Environment (JRE) using the environment variables `JAVA_HOME` and `ORACLE_HOME`. The JRE should be in one of these paths.

For thick clients, CPAT uses an Oracle Call Interface (OCI) based JDBC connect string. With this type of connection string, CPAT connects to the database typically by using the environment variables: `ORACLE_SID`, `ORACLE_HOME`, and `LD_LIBRARY_PATH`.

Note:

You only need to set the `ORACLE_SID` if you use operating system authentication for the user running CPAT. If necessary, the CPAT script can set `LD_LIBRARY_PATH` by itself, so in most cases, you only need to set an `ORACLE_HOME` environment variable.

Syntax

The Premigration Advisor Tool command syntax is case-sensitive. You can pass properties either as character strings or as text strings, as noted for each command property.

The syntax takes the following format, where `character` is a single case-sensitive character, `command-string` is a case-sensitive string, and `value` is an input option or value specified by the command property.

Shell command:

`./premigration.sh [-character                         [value] | --command-string                               value`\]\]

Multiple properties can be concatenated in the command syntax, using either the character flag or the full name of a property.

**Parent topic:** Command-Line Syntax and Properties

#### 19.9.2 Premigration Advisor Tool Command-Line Properties

Review the Premigration Advisor Tool properties to construct a command tree and options for your Oracle Database migration scenario.

- analysisprops  
	The Premigration Advisor Tool property `analysisprops` specifies the path and name of a properties file for the source database.
- connectstring  
	The Premigration Advisor Tool property `connectstring` provides the JDBC connect string for the source database.
- excludeschemas  
	The Premigration Advisor Tool property `excludeschemas` specifies a list of schemas that you want to exclude from analysis for migration.
- full  
	The Premigration Advisor Tool (CPAT) property `full` specifies that the full set of checks are run, even when `--schemas` is used.
- gatherdetails  
	The Premigration Advisor Tool property `gatherdetails` enables you to specify different levels of details for the database that you want to migrate.
- gettargetprops  
	The Premigration Advisor Tool property `gettargetprops` reads the connection properties for the migration target database instance for analysis against the source database instance.
- help  
	The Premigration Advisor Tool property `help` prints out the command line help information, and exits.
- logginglevel  
	The Premigration Advisor Tool property `logginglevel` specifies the level of issues recorded in the logging file.
- maxrelevantobjects  
	The Premigration Advisor Tool property `maxrelevantobjects` specifies the maximum number of relevant objects included in all reports.
- maxtextdatarows  
	The Premigration Advisor Tool property `maxtextdatarows` specifies a limit to the number of relevant object rows displayed in text reports (does not apply to JSON reports).
- migrationmethod  
	The Premigration Advisor Tool property `migrationmethod` specifies the type of method or tooling that you intend to use to migrate to Oracle Cloud.
- outdir  
	The Premigration Advisor Tool property `outdir` specifies the directory path where you want premigration analysis log files and report files to be generated.
- outfileprefix  
	The Premigration Advisor Tool property `outfileprefix` specifies a prefix for the Premigration Advisor Tool reports.
- pdbname  
	The Premigration Advisor Tool property `pdbname` specifies the name of a source PDB on a CDB for which you want CPAT to generate a report.
- reportformat  
	The Premigration Advisor Tool (CPAT) property `reportformat` specifies the format of CPAT report output.
- schemas  
	The Premigration Advisor Tool property `schemas` specifies a list of schemas that you want to analyze for migration.
- sqltext  
	The Premigration Advisor Tool property `sqltext` specifies to show the SQL used for CPAT checks in TEXT reports
- sysdba  
	The Premigration Advisor Tool property `sysdba` is used to force `AS SYSDBA` when connecting to the database.
- targetcloud  
	The Premigration Advisor Tool property `targetcloud` specifies the type of Oracle Cloud database to which you want to migrate.
- username  
	The Premigration Advisor Tool property `username` specifies the username to use when connecting to the source database.
- version  
	The Premigration Advisor Tool property `version` prints out the current version of CPAT, and then exits.
- updatecheck  
	The Premigration Advisor Tool property `updatecheck` prints the current version of CPAT, checks to see if there is a more recent version available, and then exits.

**Parent topic:** Command-Line Syntax and Properties

##### 19.9.2.1 analysisprops

The Premigration Advisor Tool property `analysisprops` specifies the path and name of a properties file for the source database.

| Property | Description |
| --- | --- |
| property type | character, string |
| Syntax | `-a\|--analysisprops                     --property-file-name` |

Description

The Premigration Advisor Tool `analysisprops` property specifies the path and name of a properties file that you have generated previously for the source database by using the Premigration Advisor Tool command-line property `--gettargetprops`. You use this properties file with the Premigration Advisor Tool to analyze properties of the database.

Usage Notes

In the command string, you must also specify the options `--connectString ` (`-c`) to the source database, and `--targetcloud` (`-t`) to specify the type of Cloud database to which you want to migrate.

Examples

In this example, you obtain the properties file `premigration_advisor_analysis.properties` from the target instance, and identify that file to use with `analysisprops`:

```
./premigration.sh --connectstring jdbc:oracle:oci:@ --targetcloud ATPD --sysdba \
--analysisprops premigration_advisor_analysis.properties
```

**Parent topic:** Premigration Advisor Tool Command-Line Properties

##### 19.9.2.2 connectstring

The Premigration Advisor Tool property `connectstring` provides the JDBC connect string for the source database.

| Property | Description |
| --- | --- |
| property type | character, string |
| Syntax | ``` -c, --connectstring connect-string [--pdbname pdb-name] ``` |
| Default value | None |

Description

The `connectstring` property specifies the JDBC connect string for the source database. If the connect string is for a CDB, then you must also specify a PDB name using the `--pdbname` switch, using `--pdbname pdb-name`, where `pdb-name` is the name of the PDB containing the source database.

CPAT connections have the following steps:

1. Connect to and obtain properties from the target instance using primigration.sh. This connection requires connnection information for the target instance, but does not require `--targetcloud`. It is this step that creates the `premigration_advisor_analysis` properties file. `connectstring` is required.
2. If necessary, connect to the computer where you will analyze the source instance, and copy the `premigration_advisor_analysis.properties` file to that computer.
3. Generate a CPAT report by running `premigration.sh` with the connection information for the source instance.

If you have a properties file that has Cloud service/lockdown information about the target, then `--targetcloud` is not required. If you do not provide a properties file, or if the properties file doesn't specify the Cloud service, then to obtain the most relevant information, you must use `--targetcloud` or `-t` to specify a target cloud. If you don't specify a target cloud using `--targetcloud` or `-t`, then the default is a Cloud target with no known Cloud service/lockdown profile set on the PDB target.

Note:

The restrictions enforced by a lockdown profile are for the entire PDB, and affect all users on that PDB, including `SYS` and `SYSTEM`.

Examples

In the following example, the PDB name is `sales1`, and `connect-string` indicates where the connection string is placed.

```
premigration.sh -c connect-string --pdbname sales1
```

**Parent topic:** Premigration Advisor Tool Command-Line Properties

##### 19.9.2.3 excludeschemas

The Premigration Advisor Tool property `excludeschemas` specifies a list of schemas that you want to exclude from analysis for migration.

| Property | Description |
| --- | --- |
| property type | string |
| Syntax | `--excludeschemas schemaname ['schemaname'                     'schemaname' ...]`  where `schemaname` is the name of one or more schema names, separated by spaces.  Schema names are assumed to be case sensitive. For example, use `SYSTEM`, not `system`. If a schema name is lowercase, mixed case, or uses special characters, then use double quotation marks as well as single quotation marks to designate the schema name. For example:  ``` --excludeschemas '"MixedCase"' '"Special.Char$"' ``` |

Description

The Premigration Advisor Tool `excludeschemas` property specifies the schemas that you want to exclude from analysis for their readiness to migrate to the Cloud.

Usage Notes

Use to indicate the schemas on which you do not want premigration checks to be performed. If `excludeschemas` is omitted, and `schemas` is not used, then all schemas in the database will be analyzed. The `excludeschemas` property cannot be used in conjunction with `schemas`.

In the command string, you must also specify the options `--connectString ` (`-c`) to the source database, and `--targetcloud` (`-t`) to specify the type of Cloud database to which you want to migrate.

**Parent topic:** Premigration Advisor Tool Command-Line Properties

##### 19.9.2.4 full

The Premigration Advisor Tool (CPAT) property `full` specifies that the full set of checks are run, even when `--schemas` is used.

| Property | Description |
| --- | --- |
| property type | character, string |
| Syntax | `-f\|--full` |

Description

Each CPAT check has a defined scope. If the scope of a check is `INSTANCE`, then that check will not be run unless you override that defined scope by selecting `FULL`. The CPAT `full` property forces the full set of checks to be run on the source database, even when `--schemas` has also been specified in the command string to limit the scope of checks.

Usage Notes

The option you use with CPAT should also be used with Oracle Data Pump. If you intend to use Oracle Data Pump with `FULL` mode, then you should run CPAT with the `full` property. If you intend to use Oracle Data Pump in `SCHEMA` mode, then run CPAT in `schema` mode.

Examples

Suppose you have 100 schemas in your source database instance, but you want to migrate only three schemas, s1, s2 and s3, to Autonomous Transaction Processing Dedicated (ATP-D).

In this case, you do not need to analyze all the schemas, but you do want to run `INSTANCE SCOPED` checks on all three schemas. You can do this by running CPAT with `--schemas s1 s2 s3 --full`

**Parent topic:** Premigration Advisor Tool Command-Line Properties

##### 19.9.2.5 gatherdetails

The Premigration Advisor Tool property `gatherdetails` enables you to specify different levels of details for the database that you want to migrate.

| Property | Description |
| --- | --- |
| property type | string |
| Syntax | `-D\|--gatherdetails --option`  Options:  - `all` Fetches all possible details (except performance metrics used by Oracle Estate Explorer). - `none` Does not fetch any additional details. (Default) - `oee` Fetches additional details required by Oracle Estate Explorer. - `oee_full` Fetches all additional details required by Oracle Estate Explorer, including performance metrics. (Note: Gathering performance metrics can take a considerable amount of time and requires a Diagnostic Pack license.). - `schema_objects` Fetches details about schema objects for the schemas being migrated. |

Description

The Premigration Advisor Tool `gatherdetails` property specifies what level of information you want to have reported by CPAT. This option enhances information collection, and provides a more comprehensive view of your database.

Usage Notes

The report can include details about server memory, System Global Area (SGA), Program Global Area (PGA), server CPUs, Oracle Data Guard, and supplemental logging.. You can also view database High Water Mark statistics, a schema summary (tables, indexes, LOBs, invalid objects, column type distribution, largest tables and objects), installed options, National Language Support (NLS) parameters, initialization parameters, database instances, and other details relevant to review before migration.

To generate a report, use the `--gatherdetails --option` switch and and provide your connection parameters with `targetconnection`.

For more information, run `premigration.sh --help`, or `premigration.com --help` on Microsoft Windows systems.

Examples

```
./premigration.sh --gatherdetails --all --connectstring jdbc:oracle:thin:@atpd_high?TNS_ADMIN=/path/wallet . . .
```

**Parent topic:** Premigration Advisor Tool Command-Line Properties

##### 19.9.2.6 gettargetprops

The Premigration Advisor Tool property `gettargetprops` reads the connection properties for the migration target database instance for analysis against the source database instance.

| Property | Description |
| --- | --- |
| property type | string |
| Syntax | `` -g\|--gettargetprops                     `property` `` |

Description

The Premigration Advisor Tool `gettargetprops` property specifies that CPAT collects the connection parameters for the migration target instance. CPAT collects properties of the migration target instance, so that it can then analyze those properties on the source database instance.

Usage Notes

These properties are typically set by tools that use CPAT in their migration flow, and use these properties to specify to CPAT that certain migration operations have been or will be performed during migration. Generate the properties file with the `--gettargetprops` switch and `targetconnection` parameters

For more information, run `premigration.sh --help`, or `premigration.com --help` on Microsoft Windows systems.

Examples

```
./premigration.sh --gettargetprops --connectstring jdbc:oracle:thin:@atpd_high?TNS_ADMIN=/path/wallet . . .
```

**Parent topic:** Premigration Advisor Tool Command-Line Properties

##### 19.9.2.7 help

The Premigration Advisor Tool property `help` prints out the command line help information, and exits.

| Property | Description |
| --- | --- |
| property type | string |
| Syntax | `-h\|--help` |

Description

The Premigration Advisor Tool `help` property prints out the command-line help instructions, and causes the advisor to exit.

Usage Notes

Use this option to obtain help information about the version of the Premigration Advisor Tool that you are running.

Examples

```
premigration.sh --help
```

**Parent topic:** Premigration Advisor Tool Command-Line Properties

##### 19.9.2.8 logginglevel

The Premigration Advisor Tool property `logginglevel` specifies the level of issues recorded in the logging file.

| Property | Description |
| --- | --- |
| property type | string |
| Syntax | `-l\|--logginglevel                   -[severe\|warning\|info\|config\|fine\|finer\|finest]` |
| Default | If you do not provide this property in the command string, then the default is `fine`. |

Description

The Premigration Advisor Tool `logginglevel` property specifies the severity of issues that you want to have logged in the Premigration Advisor Tool Report

Usage Notes

Use to indicate which type of checks you want to perform on the target database or databases. Log properties:

- `severe`
- `warning`
- `info`
- `config`
- `fine`
- `finer`
- `finest`

**Parent topic:** Premigration Advisor Tool Command-Line Properties

##### 19.9.2.9 maxrelevantobjects

The Premigration Advisor Tool property `maxrelevantobjects` specifies the maximum number of relevant objects included in all reports.

| Property | Description |
| --- | --- |
| property type | string |
| Syntax | `-M\|--maxrelevantobjects                     maximum-relevant-objects` |

Description

The Premigration Advisor Tool `maxrelevantobjects` property specifies the maximum number of relevant objects displayed in premigration advisor reports, specified by a numeric value. For `TEXT` reports, this property overrides the `maxtextdatarows` property.

Note:

If you specify a limit to the number of objects reported, then there can be objects that can affect your migration that are not published in reports.

Usage Notes

The purpose of this property is to place limits on the report that CPAT generates:

- Limit the size of a CPAT report
- Limit the memory CPAT uses
- Exclude inclusion of objects that may contain proprietary or confidential table, column or other information in the report.

Examples

```
premigration.sh  -maxrelevantobjects 5 -outfileprefix limit -targettype adws -analysisprops /usr/example/CPAT/ cloud_premigration_advisor_analysis.properties
```

**Parent topic:** Premigration Advisor Tool Command-Line Properties

##### 19.9.2.10 maxtextdatarows

The Premigration Advisor Tool property `maxtextdatarows` specifies a limit to the number of relevant object rows displayed in text reports (does not apply to JSON reports).

| Property | Description |
| --- | --- |
| property type | string |
| Syntax | `-n\|--maxtextdatarows                     maximum-number-of-data-rows` |
| Default | All rows in data tables (no maximum). |

Description

The Premigration Advisor Tool `maxtextdatarows` property specifies the maximum number of relevant object rows that are included in the `TEXT` reports, and provides a message indicating that rows after the maximum row number is reached are not displayed. If this property is not set, then all relevant objects are included (no maximum). This property does not apply to JSON reports

Usage Notes

Where there is a conflict in property settings, `maxrelevantobjects` overrides the setting for `maxtextdatarows` for Premigration Advisor TEXT report files.

Examples

**Parent topic:** Premigration Advisor Tool Command-Line Properties

##### 19.9.2.11 migrationmethod

The Premigration Advisor Tool property `migrationmethod` specifies the type of method or tooling that you intend to use to migrate to Oracle Cloud.

| Property | Description |
| --- | --- |
| property type | string |
| Syntax | `-m\|--migrationmethod                   -['datapump'\|'goldengate']` |
| Default | If no value is supplied, then the default is `datapump`. |

Description

The Premigration Advisor Tool `migrationmethod` property specifies the type of migration method or tooling that you intend to use to migrate databases to the Cloud. The migration method is used to influence what checks are done on the source database. Anything found in the source database that is incompatible with the migration method will be included in the generated report.

Usage Notes

Use to indicate which type of checks you want to perform on the target database or databases.

| Option | Description |
| --- | --- |
| `datapump` | Specifies that the Preupgrade Advisor Tool performs checks for using Oracle Data Pump to perform migrations to the Oracle Cloud deployment you select. |
| `goldengate` | Specifies that the Preupgrade Advisor Tool performs checks for using Oracle GoldenGate to perform migrations to the Oracle Cloud deployment you select. |

Examples

In the following example, `connect-string` indicates where the connection string is placed. The target Oracle Cloud database is Autonomous Transaction Processing Shared, and the migration method selected is Oracle GoldenGate.

```
premigration.cmd --connectstring some-string --targetcloud atps --username SYSTEM -migrationmethod 'goldengate'
```

**Parent topic:** Premigration Advisor Tool Command-Line Properties

##### 19.9.2.12 outdir

The Premigration Advisor Tool property `outdir` specifies the directory path where you want premigration analysis log files and report files to be generated.

| Property | Description |
| --- | --- |
| property type | string |
| Syntax | `-o\|--outdir directory-path`  where `directory-path` is the path for the log file and report directory. |

Description

The Premigration Advisor Tool `outdir` property specifies where the log files and report files should be created.

Usage Notes

If the path you provide is not an absolute path then the Premigration Advisor Tool specifies the directory relative to the file path location from which CPAT was started. If you do not specify an output file name, then the default file name is `premigration`. CPAT creates the filename, if it does not exist.

Examples

In the following example, `connect-string` indicates where the connection string is placed. The target PDB is `trend1`, the Oracle Cloud database is Autonomous Data Warehouse Dedicated, and the output directory path is `/users/analytic/adwd-migr`.

```
premigration.cmd --connectstring connect-string --targetcloud adwd --username SYSTEM --pdbname trend1 -outdir /users/analytic/adwd-migr
```

**Parent topic:** Premigration Advisor Tool Command-Line Properties

##### 19.9.2.13 outfileprefix

The Premigration Advisor Tool property `outfileprefix` specifies a prefix for the Premigration Advisor Tool reports.

| Property | Description |
| --- | --- |
| property type | string |
| Syntax | `-P\|--outfileprefix prefix-string` |

Description

The Premigration Advisor Tool `outfileprefix` property specifies a prefix that you want to place on the output reports generated for the source database. Without a prefix, the standard name for a Premigration Advisor Tool report or log is `premigration_advisor`.

Usage Notes

Use a prefix to distinguish different report outputs. For example, you can use a prefix to distinguish the reports for a database where you generate one report for a migration using Oracle GoldenGate, and another report for a migration using Oracle Data Pump, or generate separate reports for each of the PDBs in a CDB.

Examples

In the following example, the prefix string is `cdb4`, `connect-string` indicates where the connection string is placed, and the migration target Oracle Cloud database is Autonomous Transaction Processing Shared. The reports for this command are `cdb4_premigration_advisor_report.txt ` and `cdb4_premigration_advisor.log`.

```
./premigration.sh -c connect-string --targetcloud atps -P cdb4
```

**Parent topic:** Premigration Advisor Tool Command-Line Properties

##### 19.9.2.14 pdbname

The Premigration Advisor Tool property `pdbname` specifies the name of a source PDB on a CDB for which you want CPAT to generate a report.

| Property | Description |
| --- | --- |
| property type | string |
| Syntax | `-p\|--pdbname pdbname` |

Description

The name of a PDB to connect to. Applicable only when the source database connect string is for a CDB.

Usage Notes

You only need to use this property when the source database connect string is for a CDB.

Examples

In the following example, connect-string indicates where the connection string is placed for the source CDB. The source PDB is `trend4`, and the target is an Oracle Cloud Autonomous Data Warehouse Dedicated database.

```
premigration.cmd --connectstring connect-string --targetcloud adwd --username SYSTEM --pdbname trend4
```

**Parent topic:** Premigration Advisor Tool Command-Line Properties

##### 19.9.2.15 reportformat

The Premigration Advisor Tool (CPAT) property `reportformat` specifies the format of CPAT report output.

| Property | Description |
| --- | --- |
| property type | string |
| Syntax | `-r\|--reportformat -format                     [format                                              format]`  where `format` is a report format. The CPAT supports a machine-readable report in JSON format, and human-readable formats HTML or TEXT. Multiple formats are space-delimited. If you do not specifiy a specific report type on the command line with --reportformat, then by default CPAT will generate both Text and HTML reports. |

Description

At the time of this release, the Premigration Advisor Tool can generate reports in either JSON or text format. Use the `reportformat` property to specify which report outputs you require.

Usage Notes

Use to indicate which type of report output you want to generate. If this property is not specified, then the default is TEXT.

Note:

Oracle recommends that you specify both text and JSON reports, and that you always save reports and log files. If you encounter an issue during migration, then it is important to include all possible information to assist with the resolution of the issue, including the log file, and both the text and JSON reports.

| Option | Description |
| --- | --- |
| `json` | Specifies that the Preupgrade Advisor Tool produces a report in JSON format. |
| `text` | Specifies that the Preupgrade Advisor Tool produces a report in text file format. |

Examples

In the following example, report outputs in JSON and text formats are specified for a report where the target is an Oracle Cloud Autonomous Data Warehouse Dedicated database. The reports generated are `premigration_advisor_report.json` `premigration_advisor_report.txt`.

```
premigration.cmd --connectstring connect-string --targetcloud adwd --username SYSTEM --sqltext
```

**Parent topic:** Premigration Advisor Tool Command-Line Properties

##### 19.9.2.16 schemas

The Premigration Advisor Tool property `schemas` specifies a list of schemas that you want to analyze for migration.

| Property | Description |
| --- | --- |
| property type | string |
| Syntax | `-s\|--schemas 'schemaname' ['schemaname'                     'schemaname' ...]`  where `schemaname` is the name of one or more schema names, separated by spaces. |

Description

The Premigration Advisor Tool `schemas` property specifies the schemas that you want to check for their readiness to migrate to the Cloud. The migration method is used to influence what checks are done on the source database. Anything found in the source database that is incompatible with the migration method will be included in the generated report.

Usage Notes

Use to restrict the report to a specific list of schemas on which you want to perform checks. In schema mode, `SCHEMA` and `UNIVERSAL` scope checks are run. `INSTANCE` scope checks are not run. If you do not specify `schemas`, and `excludeschemas` is not used, then the default is to run with the `full` property. All schemas in the database will be analyzed, except for the schemas managed by Oracle. This can result in your receiving a report that lists problems in schemas that you do not intend to migrate to the Cloud target.

Note:

The option you use with CPAT should also be used with Oracle Data Pump. If you intend to use Oracle Data Pump with `FULL` mode, then you should run CPAT with the `full` property. If you intend to use Oracle Data Pump in `SCHEMA` mode, then run CPAT in `schema` mode.

The `schemas` property cannot be used in conjunction with `excludeschemas`. Limiting the scope of schemas that you check can be particularly useful if the source instance hosts multiple applications, each of which you may want to migrate to different Oracle Autonomous Database instances.

Note:

If you specify the `--full` property, then it forces the full set of checks to be run on the source database, overriding the restrictions that otherwise are in force when you limit the scope of checks with `--schemas`.

Schema names are assumed to be case sensitive. For example, use `SYSTEM`, not `system`. If a schema name is lowercase, mixed case, or uses special characters, then use double quotation marks as well as single quotation marks to designate the schema name. For example:

```
--schemas '"MixedCase"' '"Special.Char$"'
```

Examples

In the following example, a report is generated for the schemas `ADMIN` and `MixedCase` where the target is an Oracle Cloud Autonomous Data Warehouse Dedicated database, and `connect-string` represents the connection string to the source database.

```
premigration.cmd --connectstring connect-string --targetcloud atps --username ADMIN -s 'SYSTEM' '"MixedCase'"
```

**Parent topic:** Premigration Advisor Tool Command-Line Properties

##### 19.9.2.17 sqltext

The Premigration Advisor Tool property `sqltext` specifies to show the SQL used for CPAT checks in TEXT reports

| Property | Description |
| --- | --- |
| property type | string |
| Syntax | `-S\|--sqltext` |

Description

The Premigration Advisor Tool `sqltext` property overides the default to hide SQL that was run for CPAT checks in TEXT reports. This property does not apply to JSON reports. It does not take any options.

Usage Notes

CPAT performs checks on the database using SQL statements. CPAT reports can be generated in both TEXT and JSON format. By default the SQL that was executed for each check is not included in the TEXT report. To have the SQL shown in the TEXT report, you can use this parameter.

Examples

```
premigration.cmd --connectstring connect-string --targetcloud adwd --username SYSTEM --sqltext
```

**Parent topic:** Premigration Advisor Tool Command-Line Properties

##### 19.9.2.18 sysdba

The Premigration Advisor Tool property `sysdba` is used to force `AS SYSDBA` when connecting to the database.

| Property | Description |
| --- | --- |
| property type | character, string |
| Syntax | `-d,--sysdba` |

Description

The Premigration Advisor Tool `sysdba` property specifies that the Premigration Advisor Tool connects to the source database AS SYSDBA..

Usage Notes

If you are using operating aystem authentication, or the SYS user then you must use `--sysdba`.You also must use `--sysdba` to connect as a user who has been granted `SYSDBA`, but not the other privileges required by CPAT to perform checks.

Examples

```
./premigration.sh --connectstring jdbc:oracle:oci:@ --targetcloud ATPD --sysdba --analysisprops premigration_advisor_analysis.properties
```

**Parent topic:** Premigration Advisor Tool Command-Line Properties

##### 19.9.2.19 targetcloud

The Premigration Advisor Tool property `targetcloud` specifies the type of Oracle Cloud database to which you want to migrate.

| Property | Description |
| --- | --- |
| property type | string |
| Syntax | `-t \| --targetcloud cloudtype` |
| Default | DEFAULT indicates a target with no known lockdown profile. |

Description

This option is used The Premigration Advisor Tool `targetcloud` property specifies the type of Cloud database to which you want to migrate. In a configuration file, you can set this value to a different value for each database that you want to check.

Usage Notes

Use to identify the type of cloud to which you are migrating, which affects the kinds of checks performed on the source database.

| Option | Description |
| --- | --- |
| `'ATPD'` | Oracle Autonomous Database Transaction Processing Dedicated |
| `'ATPS'` | Oracle Autonomous Database Serverless |
| `'ADWD'` | Oracle Autonomous Data Warehouse Dedicated |
| `'ADWS'` | Oracle Autonomous Data Warehouse Serverless. |
| 'DEFAULT' | Use for targets such as Oracle Autonomous Database on Exadata Cloud@Customer or Oracle Autonomous Database Cloud Service, where typically there is no predefined lockdown profile |

Examples

```
./premigration.sh --targetcloud atps --outfileprefix ATPS_RUN_01 --outdir /path/CPAT_output --reportformat TEXT JSON ...
```

**Parent topic:** Premigration Advisor Tool Command-Line Properties

##### 19.9.2.20 username

The Premigration Advisor Tool property `username` specifies the username to use when connecting to the source database.

| Property | Description |
| --- | --- |
| property type | string |
| Syntax | `-u\|--username user-name` |

Description

The `--username` switch provides CPAT with the user to connect to the source database.

Usage Notes

The user name you specify must have the `SELECT ANY DICTIONARY` privilege, and be granted `SELECT` on `SYSTEM.DUM$COLUMNS` and `SYSTEM.DUM$DATABASE`. When connecting to the target database, use the `ADMIN` user, or another user with the `PDB_DBA` role.

Examples

```
premigration --connectstring jdbc:oracle:thin:@example.oracle.com:1521/ORCLPDB1 --username ADMIN -t atps
```

**Parent topic:** Premigration Advisor Tool Command-Line Properties

##### 19.9.2.21 version

The Premigration Advisor Tool property `version` prints out the current version of CPAT, and then exits.

| Property | Description |
| --- | --- |
| property type | string |
| Syntax | `-v\|--version ` |

Description

The Premigration Advisor Tool `version` property enables you to print out the version number of the Premigration Advisor Tool, and the date it was released.

Usage Notes

Use this option to obtain information about the version of the Preupgrade Advisor Tool that you are running.

Examples

```
premigration.sh -v
Premigration Advisor Application Version: 22.10.0 (production)
Build date: 2022/10/18 10:55:43
Build hash: 53950fd
```
```
premigration.com --version
Premigration Advisor Application Version: 22.10.0 (production)
Build date: 2022/10/18 10:55:43
Build hash: 53950fd
```

**Parent topic:** Premigration Advisor Tool Command-Line Properties

##### 19.9.2.22 updatecheck

The Premigration Advisor Tool property `updatecheck` prints the current version of CPAT, checks to see if there is a more recent version available, and then exits.

| Property | Description |
| --- | --- |
| property type | string |
| Syntax | `-U \|                 --updatecheck` |
| Default value | None |

Description

Checks to see if an updated version of Cloud Premigration Advisor Tool (CPAT) is available. If here is a newer version, it prints yes. If there is not a newer version, it prints no. After completing the checc, CPAT exits. Network access is required for a successful check.

The Premigration Advisor Tool `updatecheck` property checks Oracle Support to determine if an updated version of Cloud Premigration Advisor Tool (CPAT) is available.

Usage Notes

To use this property, you must have a network connection. If you do not have a network connection, then you receive the error `CPAT-4001: Error checking for           latest available version of the Cloud Premigration Advisor Tool`. If your network is behind a firewall, then this switch must be used with an appropriate HTTPS proxy defined.

Example

```
export _JAVA_OPTIONS='-Dhttps.proxyHost=www-proxy.us.oracle.com -Dhttps.proxyPort=80'
./premigration.sh --updatecheck
```

If you already have the latest version of CPAT, then you should see the following output:

`Picked up _JAVA_OPTIONS: -Dhttps.proxyHost=www-proxy.us.oracle.com           -Dhttps.proxyPort=80There is no newer version available of the Cloud Premigration Advisor           Tool`

**Parent topic:** Premigration Advisor Tool Command-Line Properties

### 19.10 List of Checks Performed By the Premigration Advisor Tool

Review information about the checks you find in a Premigration Advisor Tool report.

Note:

When you specify the source database and your migration target, the Premigration Advisor Tool performs the checks required for that migration scenario. Only the checks required for that scenario are performed. Your report provides responses to the migration scenario you specify when you start CPAT.

- dp\_has\_low\_streams\_pool\_size  
	The Premigration Advisor Tool check `dp_has_low_streams_pool_size` verifies the `STREAMS_POOL_SIZE` amount is large enough for Data Pump migrations to start and work efficiently.
- gg\_enabled\_replication  
	The Premigration Advisor Tool check `gg_enabled_replication` notifies you that the initialization parameter `ENABLE_GOLDENGATE_REPLICATION` is not set on the source database.
- gg\_force\_logging  
	The Premigration Advisor Tool check `gg_force_logging` indicates that forced logging of all transactions and loads during the migration is not set.
- gg\_has\_low\_streams\_pool\_size  
	The Premigration Advisor Tool check `gg_has_low_streams_pool_size` verifies that the `STREAMS_POOL_SIZE` amount is large enough for Oracle GoldenGate.
- gg\_not\_unique  
	The Premigration Advisor Tool check `gg_not_unique` indicates that forced logging of all transactions and loads during the migration is not set.
- gg\_not\_unique\_bad\_col\_no  
	The Premigration Advisor Tool check `gg_not_unique_bad_col_no` finds tables that have no primary key and no non-nullable unique index.
- gg\_not\_unique\_bad\_col\_yes  
	The Premigration Advisor Tool check `gg_not_unique_bad_col_yes` finds tables that have no primary key, unique index, or key columns, including table columns defined with unbounded data types.
- gg\_objects\_not\_supported  
	The Premigration Advisor Tool check `gg_objects_not_supported` indicates that there are unsupported objects on the source database.
- gg\_supplemental\_log\_data\_min  
	The Premigration Advisor Tool check `gg_supplemental_log_data_min` indicates that minimal supplemental logging is not enabled on the source database.
- gg\_tables\_not\_supported  
	The Premigration Advisor Tool check `gg_tables_not_supported_adb` indicates that some objects in the database cannot be replicated using Oracle GoldenGate.
- gg\_tables\_not\_supported  
	The Premigration Advisor Tool check `gg_tables_not_supported` indicates that some objects in the non-ADB database cannot be replicated using Oracle GoldenGate.
- gg\_user\_objects\_in\_ggadmin\_schemas  
	The Premigration Advisor Tool check `gg_user_objects_in_ggadmin_schemas` indicates the presence of user objects in schemas that have Oracle GoldenGate administrator privileges.
- has\_absent\_default\_tablespace  
	The Premigration Advisor Tool check `has_absent_default_tablespace` indicates that schema Owner default tablespaces are missing.
- has\_absent\_temp\_tablespace  
	The Premigration Advisor Tool check `has_absent_temp_tablespace` indicates that schema Owner temporary tablespaces are missing.
- has\_active\_data\_guard\_dedicated  
	The Premigration Advisor Tool check `has_active_data_guard_dedicated` detects whether Active Data Guard is being used on the source instance.
- has\_active\_data\_guard\_serverless  
	The Premigration Advisor Tool check `has_active_data_guard_serverless` detects whether Active Data Guard is being used on the source instance.
- has\_basic\_file\_lobs  
	The Premigration Advisor Tool check `has_basic_file_lobs` indicates BASICFILE LOBs are present in the schema, which are not supported with Oracle Autonomous Database.
- has\_clustered\_tables  
	The Premigration Advisor Tool check `has_clustered_tables` indicates table clusters are present in the schema, which are not supported with Oracle Autonomous Database.
- has\_columns\_of\_rowid\_type  
	The Premigration Advisor Tool check `has_columns_of_rowid_type` indicates tables with columns with `ROWID` data type that cannot be migrated.
- has\_columns\_with\_local\_timezone  
	The Premigration Advisor Tool check `has_columns_with_local_timezone` indicates tables have local DBTIMEZONE columns that do not match the target instance DBTIMEZONE.
- has\_columns\_with\_media\_data\_types\_adb  
	The Premigration Advisor Tool check `has_columns_with_media_data_types_adb` indicates tables with multimedia data type that cannot be migrated.
- has\_columns\_with\_media\_data\_types\_default  
	The Premigration Advisor Tool check `has_columns_with_media_data_types_default` indicates tables with multimedia columns.
- has\_columns\_with\_spatial\_data\_types  
	The Premigration Advisor Tool check `has_columns_with_spatial_data_types` indicates there are spatial objects that are not fully supported.
- has\_common\_objects  
	The Premigration Advisor Tool check `has_common_objects` indicates there are common objects in the database instance.
- has\_compression\_disabled\_for\_objects  
	The Premigration Advisor Tool check `has_compression_disabled_for_objects` indicates there are tables or partitions lacking a `COMPRESSION` clause.
- has\_csmig\_schema  
	The Premigration Advisor Tool check `has_csmig_schema` indicates the CSSCAN utility is installed and configured on the source database..
- has\_data\_in\_other\_tablespaces\_dedicated  
	The Premigration Advisor Tool check `has_data_in_other_tablespaces_dedicated` identifies data subject to tablespace restrictions when migrating to Oracle Autonomous Databases on Dedicated Infrastructure..
- has\_data\_in\_other\_tablespaces\_serverless  
	The Premigration Advisor Tool check `has_data_in_other_tablespaces_serverless` identifies data subject to tablespace restrictions when migrating to Oracle Autonomous Databases on Shared Infrastructure.
- has\_db\_link\_synonyms  
	The Premigration Advisor Tool check `has_db_link_synonyms` indicates the schema contains synonyms with database links.
- has\_db\_links  
	The Premigration Advisor Tool check `has_db_links` indicates the schema contains synonyms with database links.
- has\_dbms\_credentials  
	The Premigration Advisor Tool check `has_dbms_credentials` indicates the schema contains credentials that were not created with `DBMS_CLOUD.CREATE_CREDENTIAL`.
- has\_dbms\_credentials  
	The Premigration Advisor Tool check `has_dbms_credentials` indicates the schema contains credentials that were not created with `DBMS_CLOUD.CREATE_CREDENTIAL`.
- has\_directories  
	The Premigration Advisor Tool check `has_directories` indicates that there are directories objects in the source database.
- has\_enabled\_scheduler\_jobs  
	The Premigration Advisor Tool check `has_enabled_scheduler_jobs     ` indicates that there are List scheduler jobs that may interfere with Oracle Data Pump export.
- has\_external\_tables\_dedicated  
	The Premigration Advisor Tool check `has_external_tables_dedicated` indicates that Non-Cloud Objects Storage External tables exist in the source database.
- has\_external\_tables\_default  
	The Premigration Advisor Tool check `has_external_tables_default` indicates that external tables cannot be migrated unless the `DIRECTORY` objects the tables rely on have been created.
- has\_external\_tables\_serverless  
	The Premigration Advisor Tool check `has_external_tables_serverless` indicates that there are non-cloud Objects Storage external tables in the source database.
- has\_fmw\_registry\_in\_system  
	The Premigration Advisor Tool check `has_fmw_registry_in_system` indicates that the Fusion Middleware Schema Version Registry must be moved out of the `SYSTEM` schema before migration.
- has\_illegal\_characters\_in\_comments  
	The Premigration Advisor Tool check `has_illegal_characters_in_comments` indicates that there are characters in table comments that are not legal in the databases character set.
- has\_ilm\_ado\_policies  
	The Premigration Advisor Tool check `has_ilm_ado_policies` indicates that Information Lifestyle Management (ILM) Automatic Data Optimization Policies (ADO) will not migrate.
- has\_incompatible\_jobs  
	The Premigration Advisor Tool check `has_incompatible_jobs` indicates that Information Lifestyle Management (ILM) Automatic Data Optimization Policies (ADO) will not migrate.
- has\_index\_organized\_tables  
	The Premigration Advisor Tool check `has_index_organized_tables` indicates that Index Organized tables are present in the source database.
- has\_java\_objects  
	The Premigration Advisor Tool check `has_java_objects` indicates that there are Java objects present in the source database.
- has\_java\_source  
	The Premigration Advisor Tool check `has_java_source` indicates that there are Java sources present in the source database.
- has\_libraries  
	The Premigration Advisor Tool check `has_libraries` indicates that there are applications that require the `CREATE LIBRARY` statement.
- has\_logging\_off\_for\_partitions  
	The Premigration Advisor Tool check `has_logging_off_for_partitions` indicates that there are Partitions using the `NOLOGGING` storage attribute.
- has\_logging\_off\_for\_subpartitions  
	The Premigration Advisor Tool check `has_logging_off_for_subpartitions` indicates that there are Partitions using the `NOLOGGING` storage attribute.
- has\_logging\_off\_for\_tables  
	The Premigration Advisor Tool check `has_logging_off_for_tables` indicates that there are tables using the `NOLOGGING` storage attribute.
- has\_low\_streams\_pool\_size  
	The Premigration Advisor Tool check `has_low_streams_pool_size` indicates that Mining Models with unexpected or incorrect attributes are detected.
- has\_noexport\_object\_grants  
	The Premigration Advisor Tool check `has_noexport_object_grants` indicates that Oracle Data Pump is unable to export all object grants.
- has\_oracle\_streams  
	The Premigration Advisor Tool check `has_oracle_streams` indicates that Oracle Streams is configured in the database.
- has\_parallel\_indexes\_enabled  
	The Premigration Advisor Tool check `has_parallel_indexes_enabled` indicates that `PARALLEL` clause indexes exist.
- has\_profile\_not\_default  
	The Premigration Advisor Tool check `has_profile_not_default` indicates that schemas exist whose `PROFILE` is not available on the target system.
- has\_public\_synonyms  
	The Premigration Advisor Tool check `has_public_synonyms` indicates that Public Synonyms exist in source system schemas.
- has\_refs\_to\_restricted\_packages\_dedicated  
	The Premigration Advisor Tool check `has_refs_to_restricted_packages_dedicated` indicates that there are references to partially or completely unsupported packages.
- has\_refs\_to\_restricted\_packages\_serverless  
	The Premigration Advisor Tool check `has_refs_to_restricted_packages_serverless` indicates that there are references to partially or completely unsupported packages.
- has\_refs\_to\_user\_objects\_in\_sys  
	The Premigration Advisor Tool check `has_refs_to_user_objects_in_sys` indicates that there are user schema objects dependent on `SYS` or `SYSTEM`.
- has\_role\_privileges  
	The Premigration Advisor Tool check `has_role_privileges` indicates that some role privileges used in the source database are not available in the target database
- has\_sqlt\_objects\_adb  
	The Premigration Advisor Tool check `has_sqlt_objects_adb` indicates that `SQLTXPLAIN` objects are detected.
- has\_sqlt\_objects\_default  
	The Premigration Advisor Tool check `has_sqlt_objects_default` indicates that ` SQLTXPLAIN` objects are detected that Oracle Data Pump does not export.
- has\_sys\_privileges  
	The Premigration Advisor Tool check `has_sys_privileges` indicates that some system privileges in the source database are not available in the target database.
- has\_tables\_that\_fail\_with\_dblink  
	The Premigration Advisor Tool check `has_tables_that_fail_with_dblink` indicates that there are tables with `LONG` or `LONG RAW` data types
- has\_tables\_with\_long\_raw\_datatype  
	The Premigration Advisor Tool check `has_tables_with_long_raw_datatype` indicates that there are tables with `LONG` or `LONG RAW` data types
- has\_tables\_with\_xmltype\_column  
	The Premigration Advisor Tool check `has_tables_with_xmltype_column` indicates that there are tables with `XMLTYPE` columns.
- has\_trusted\_server\_entries  
	The Premigration Advisor Tool check `has_trusted_server_entries` indicates that there are `TRUSTED_SERVER` entries that cannot be recreated on Oracle Autonomous Database.
- has\_unstructured\_xml\_indexes Check  
	The Premigration Advisor Tool check `has_unstructured_xml_indexes` indicates that there are Unstructured XML Indexes.
- has\_user\_defined\_objects\_in\_sys  
	The Premigration Advisor Tool check `has_user_defined_objects_in_sys` indicates that there are User-defined objects in the `SYS` schema.
- has\_user\_defined\_objects\_in\_system  
	The Premigration Advisor Tool check `has_user_defined_objects_in_system` indicates that there are User-defined objects in the `SYSTEM` schema.
- has\_user\_defined\_objects\_no\_quota  
	The Premigration Advisor Tool check `has_user_defined_objects_no_quota` indicates that there are are objects in the source database that belong to users without quota.
- has\_user\_defined\_pvfs  
	The Premigration Advisor Tool check `has_user_defined_pvfs` indicates that there are User-defined Password Verification Functions.
- has\_users\_with\_10g\_password\_version  
	The Premigration Advisor Tool check `has_users_with_10g_password_version` indicates that there are user accounts using `10G` password version.
- has\_xmlschema\_objects  
	The Premigration Advisor Tool check `has_xmlschema_objects` indicates that there are XML Schema Objects in the source database.
- has\_xmltype\_tables  
	The Premigration Advisor Tool check `has_xmltype_tables` indicates that there are `XMLType` tables in the source database.
- modified\_db\_parameters\_dedicated  
	The Premigration Advisor Tool check `modified_db_parameters_dedicated` indicates that restricted initialization parameters are modified.
- modified\_db\_parameters\_serverless  
	The Premigration Advisor Tool check `modified_db_parameters_serverless` indicates that restricted initialization parameters are modified.
- nls\_character\_set\_conversion  
	The Premigration Advisor Tool check `nls_character_set_conversion` indicates that there are character codes on the source database that are invalid in Oracle Autonomous Database.
- nls\_national\_character\_set  
	The Premigration Advisor Tool check `nls_national_character_set` indicates that the `NCHAR` and `NVARCHAR2` lengths are different on the source and target databases.
- nls\_nchar\_ora\_910  
	The Premigration Advisor Tool check `nls_nchar_ora_910` indicates that the `NCHAR` and `NVARCHAR2` lengths are greater than the maximum length on the target databases.
- options\_in\_use\_not\_available\_dedicated  
	The Premigration Advisor Tool check `options_in_use_not_available_dedicated` indicates that unavailable database options are present on the source database.
- options\_in\_use\_not\_available\_serverless  
	The Premigration Advisor Tool check `options_in_use_not_available_serverless` indicates that unavailable database options are present on the source database.
- standard\_traditional\_audit\_adb  
	The Premigration Advisor Tool check `standard_traditional_audit_adb` indicates that Traditional Audit configurations are detected in the database.
- standard\_traditional\_audit\_default  
	The Premigration Advisor Tool check `standard_traditional_audit_default` indicates that Traditional Audit configurations are detected in the database.
- timezone\_table\_compatibility\_higher\_dedicated  
	The Premigration Advisor Tool check `timezone_table_compatibility_higher_dedicated` indicates that the timezone setting is a more recent version on the source than on the target database.
- timezone\_table\_compatibility\_higher\_default  
	The Premigration Advisor Tool check `timezone_table_compatibility_higher_default` indicates that the timezone setting is a more recent version on the source than on the target database.
- timezone\_table\_compatibility\_higher\_serverless  
	The Premigration Advisor Tool check `timezone_table_compatibility_higher_serverless` indicates that the timezone setting is a more recent version on the source than on the target database.
- unified\_and\_standard\_traditional\_audit\_adb  
	The Premigration Advisor Tool check `unified_and_standard_traditional_audit_adb` indicates that Traditional Audit configurations are detected in the database.
- unified\_and\_standard\_traditional\_audit\_default  
	The Premigration Advisor Tool check `unified_and_standard_traditional_audit_default` indicates that Traditional Audit configurations are detected in the database.
- xdb\_resource\_view\_has\_entries Check  
	The Premigration Advisor Tool check `xdb_resource_view_has_entries       Check` indicates that there is an XDB Repository that is not supported in Oracle Autonomous Database. Entries in `RESOURCE_VIEW` will not migrate.

**Parent topic:** Cloud Premigration Advisor Tool

#### 19.10.1 dp\_has\_low\_streams\_pool\_size

The Premigration Advisor Tool check `dp_has_low_streams_pool_size` verifies the `STREAMS_POOL_SIZE` amount is large enough for Data Pump migrations to start and work efficiently.

Result Criticality

Runtime

Has Fixup

Yes

Scope

`UNIVERSAL`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared
- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Description

The Premigration Advisor Tool check `dp_has_low_streams_pool_size` verifies the `STREAMS_POOL_SIZE` has been preallocated to an amount is large enough for Oracle Data Pump migrations to start and work efficiently.

Effect

The database initialization parameter `STREAMS_POOL_SIZE` value helps determine the size of the Streams pool. You should allocate sufficient memory to `STREAMS_POOL_SIZE` for the export. Failure to do this can reduce Oracle Data Pump export performance, or cause the export to fail. Oracle recommends that you define a minimum value for ` STREAMS_POOL_SIZE` in the source database before export.

Action

Run SQL to set `STREAMS_POOL_SIZE` to allocate memory for the export. For example:

```
ALTER SYSTEM SET streams_pool_size=256M SCOPE=BOTH
```

After allocating memory, restart your instance if necessary.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.2 gg\_enabled\_replication

The Premigration Advisor Tool check `gg_enabled_replication` notifies you that the initialization parameter `ENABLE_GOLDENGATE_REPLICATION` is not set on the source database.

Result Criticality

Action required

Has Fixup

Yes

Scope

`UNIVERSAL`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared
- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Description

The Premigration Advisor Tool `gg_enabled_replication` check indicates that you have selected Oracle GoldenGate as your migration method, but the initialization parameter `ENABLE_GOLDENGATE_REPLICATION` is not set to `TRUE`.

Effect

For Oracle GoldenGate to perform data migration, the source database initialization parameter `ENABLE_GOLDENGATE_REPLICATION` must be set to `TRUE`. If it is not set, then the migration fails.

Action

Set `ENABLE_GOLDENGATE_REPLICATION` to `TRUE` in the database initialization file.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.3 gg\_force\_logging

The Premigration Advisor Tool check `gg_force_logging` indicates that forced logging of all transactions and loads during the migration is not set.

Result Criticality

Review required

Has Fixup

Yes

Target Cloud

This is a default check. It applies to the following:

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared
- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Scope

`UNIVERSAL`

Description

Forced logging mode is not set on the source database. When force logging mode is set, this forces the logging of all transactions and loads, overriding any user or storage settings that indicate these transactions and loads should not be logged.

Note:

When the source instance is Oracle Autonomous Database, the gg\_force\_logging check is skipped..

Effect

If forced logging is not set, then source data in the Oracle GoldenGate Extract configuration may be missed during the migration.

Action

To enable forced logging at tablespace and database level, log in as `SYSDBA`, and turn on forced logging. For example:

```
SQL> alter database force logging;
Database altered.
```

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.4 gg\_has\_low\_streams\_pool\_size

The Premigration Advisor Tool check `gg_has_low_streams_pool_size` verifies that the `STREAMS_POOL_SIZE` amount is large enough for Oracle GoldenGate.

Result Criticality

Runtime

Has Fixup

Yes

Scope

`UNIVERSAL`

Target Cloud

This is a default check. It applies to the following:

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared
- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Description

The Premigration Advisor Tool check `gg_has_low_streams_pool_size` verifies the `STREAMS_POOL_SIZE` has been preallocated to an amount is large enough for Oracle GoldenGate migrations to start and work efficiently.

Oracle GoldenGate Extract interacts with an underlying logmining server in the source database, and Replicat interacts with an inbound server in the target database.

The shared memory that is used by the servers comes from the Streams pool portion of the System Global Area (SGA) in the database.Therefore, you must set the database initialization parameter `STREAMS_POOL_SIZE` high enough to keep enough memory available for the number of Extract and Replicat processes that you expect to run in integrated mode. Note that Streams pool is also used by other components of the database (including Oracle Streams, Advanced Queuing, and Oracle Data Pump export/import), so take other components into account when sizing the Streams pool for Oracle GoldenGate.

By default, one Extract requests the logmining server to run with of 1GB. As a best practice, keep 25 percent of the Streams pool available. Therefor, for a single process the minimum STREAMS\_POOL\_SIZE would be 1.25 GB. For more information see Oracle Support Document ID 2078459.1 and the Oracle GoldenGate documentation.

Effect

Allocate sufficient memory to `STREAMS_POOL_SIZE` for Oracle GoldenGate processes. Failure to do this can reduce Oracle GoldenGate performance, or cause the Extract or Replicat to fail. Oracle recommends that you define a minimum value for `STREAMS_POOL_SIZE` in the source database before running Oracle GoldenGate

Action

Run SQL to set `STREAMS_POOL_SIZE` to allocate memory for Extract and Replicat, depending on the number of Oracle GoldenGate processes that will run. For example:

```
ALTER SYSTEM SET streams_pool_size=1250M SCOPE=BOTH;
```

After allocating memory, restart your instance if necessary.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.5 gg\_not\_unique

The Premigration Advisor Tool check `gg_not_unique` indicates that forced logging of all transactions and loads during the migration is not set.

Criticality

Action required

Target Cloud

This is a default check. It applies to the following:

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared
- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Scope

`SCHEMA`

Description

This check applies to schemas for Oracle GoldenGate migrations on Oracle Database 19c. It identifies tables that have no primary key and no non-nullable unique index.

Effect

If there are tables without any uniqueness, then significant changes on these tables may cause GoldenGate to increasingly fall behind and not recover.

Action

To address this issue, do one of the following:

- Add a primary key to the listed tables.
- Quiesce the database as much as possible during migration.
- Migrate changes to the tables using other means, such as Oracle Data Pump.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.6 gg\_not\_unique\_bad\_col\_no

The Premigration Advisor Tool check `gg_not_unique_bad_col_no` finds tables that have no primary key and no non-nullable unique index.

Result Criticality

Review required

Has Fixup

No

Scope

`SCHEMA`

Target Cloud

This is a default check. It applies to the following:

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared
- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Migration Method

`GOLDENGATE`

Description

The Premigration Advisor Tool check `gg_not_unique_bad_col_no` finds tables that have no primary key and no non-nullable unique index.

High amounts of mutations on the tables identified in this check can cause GoldenGate replication to fall behind and never catch up. A full table scan is needed to replicate every `INSERT`, `UPDATE`, or `DELETE` operation.

Effect

If Oracle GoldenGate has to perform significant changes on these tables, then it can fall behind progressively as the replication continues, and not recover.

Action

To address this issue, do one of the following:

- Add a primary key to the listed tables
- Quiesce the database as much as possible during migration
- Migrate changes to the tables using another method, such as Oracle Data Pump

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.7 gg\_not\_unique\_bad\_col\_yes

The Premigration Advisor Tool check `gg_not_unique_bad_col_yes` finds tables that have no primary key, unique index, or key columns, including table columns defined with unbounded data types.

Result Criticality

Action required

Has Fixup

No

Scope

`SCHEMA`

Target Cloud

This is a default check. It applies to the following:

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared
- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Description

The Premigration Advisor Tool check `gg_not_unique_bad_col_yes` finds tables that have no Primary Key, Unique Index or Key Columns. A **Problematic Column** indicates that the table has a column not useful in the predicate (`where` clause). The table column is defined using an unbounded data type, such as `LONG` or `BLOB`.

Effect

If there are tables without any uniqueness, and with unbounded data\_types, then the table records cannot be uniquely identified and cannot be used for logical replication. These tables are not supported in the Oracle GoldenGate Guide for Oracle Databases, and cannot be migrated using Oracle GoldenGate

Action

To address this issue, if possible add a primary or unique key to the tables. If you cannot add a primary or uniquen key, then you must use some other method of migrating the tables, such as Oracle Data Pump.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.8 gg\_objects\_not\_supported

The Premigration Advisor Tool check `gg_objects_not_supported` indicates that there are unsupported objects on the source database.

Result Criticality

Action required

Has Fixup

No

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared
- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Scope

`SCHEMA`

Description

This check applies to schemas for Oracle GoldenGate migrations. Objects exist on the source database that are not supported for migration with Oracle GoldenGate.

Effect

Typically, the objects listed under this check are not replicated successfully in the migration without additional configuration.

Action

Consult the Oracle GoldenGate documentation to see how objects with the listed `SUPPORT_MODE` values can be replicated successfully.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.9 gg\_supplemental\_log\_data\_min

The Premigration Advisor Tool check `gg_supplemental_log_data_min` indicates that minimal supplemental logging is not enabled on the source database.

Result Criticality

Action required

Has Fixup

Yes

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared
- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Scope

`UNIVERSAL`

Description

This check applies to schemas for Oracle GoldenGate migrations. Minimal supplemental logging, a database-level option, is required for an Oracle source database when using Oracle GoldenGate. This configuration adds row chaining information, if any exists, to the redo log for update operations.

Effect

If minimal supplemental log data is not enabled, then Oracle GoldenGate cannot function.

Action

Log in as `SYSDBA`, and enable minimal supplemental logging on the source database. For example:

```
SQL> ALTER DATABASE ADD SUPPLEMENTAL LOG DATA;
```

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.10 gg\_tables\_not\_supported

The Premigration Advisor Tool check `gg_tables_not_supported_adb` indicates that some objects in the database cannot be replicated using Oracle GoldenGate.

Result Criticality

Action required

Has Fixup

No

Target Cloud

This is a default check. It applies to the following:

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Scope

`SCHEMA`

Description

This check applies to schemas for Oracle GoldenGate migrations. When objects in the source database cannot be replicated by Oracle GoldenGate, the report provides a list of those objects with this check message.

Effect

The listed objects will not be migrated with Oracle GoldenGate.

Action

At the time of the switchover, you must move the listed relevant objects to the target database using another migration method, such as Oracle Data Pump.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.11 gg\_tables\_not\_supported

The Premigration Advisor Tool check `gg_tables_not_supported` indicates that some objects in the non-ADB database cannot be replicated using Oracle GoldenGate.

Result Criticality

Action required

Has Fixup

No

Target Cloud

- Default (an Oracle Database instance that is not Oracle Autonomous Database, or ADB)

Scope

`SCHEMA`

Description

This check applies to schemas for Oracle GoldenGate migrations. When objects in the source database cannot be replicated by Oracle GoldenGate, the report provides a list of those objects with this check message.

Effect

The listed objects will not be migrated with Oracle GoldenGate.

Action

At the time of the switchover, you must move the listed relevant objects to the target database using another migration method, such as Oracle Data Pump.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.12 gg\_user\_objects\_in\_ggadmin\_schemas

The Premigration Advisor Tool check `gg_user_objects_in_ggadmin_schemas` indicates the presence of user objects in schemas that have Oracle GoldenGate administrator privileges.

Result Criticality

Action required

Has Fixup

No

Target Cloud

This is a default check. It applies to the following:

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared
- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Scope

`SCHEMA`

Description

This check applies to schemas for Oracle GoldenGate migrations. When user objects in schemas have Oracle GoldenGate administrator privileges, those schemas are listed in CPAT report. Oracle GoldenGate cannot migrate them.

Effect

The listed objects will not be migrated with Oracle GoldenGate.

Action

Exclude these schemas from the Oracle GoldenGate data migration. You must move the listed relevant objects to the target database using another migration method, such as Oracle Data Pump.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.13 has\_absent\_default\_tablespace

The Premigration Advisor Tool check `has_absent_default_tablespace` indicates that schema Owner default tablespaces are missing.

Result Criticality

Review required.

Has Fixup

No

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ATPD Autonomous Transaction Processing Dedicated
- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Scope

`SCHEMA`

Description

This check applies to schemas for Oracle Data Pump and Oracle GoldenGate migrations. When CPAT detects that one or more schema Owner's default tablespace are missing, the schemas are listed in the report.

Effect

Schemas without a valid `DEFAULT TABLESPACE` cannot be created on the target instance due to ORA-00959 errors..

Action

If the schemas are no longer being used, then drop those schemas. However, if the schemas are being used, then either create a valid default tablespace for the schema, or define default tablespace by running a query on `DBA_TABLESPACE` to list all valid tablespace names, and select one as a valid default tablespace.

#### 19.10.14 has\_absent\_temp\_tablespace

The Premigration Advisor Tool check `has_absent_temp_tablespace` indicates that schema Owner temporary tablespaces are missing.

Result Criticality

Review required.

Has Fixup

No

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ATPD Autonomous Transaction Processing Dedicated
- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Scope

`SCHEMA`

Description

This check applies to schemas for Oracle Data Pump and Oracle GoldenGate migrations. When CPAT detects that one or more schema Owner's temporary tablespace are missing, the schemas are listed in the report.

Effect

For Oracle Autonomous Database Dedicated Infrastructure for Transaction Processing (ATPD) and Oracle Autonomous Database Dedicated Infrastructure for Data Warehouse (ADWD), unless the needed temporary tablespaces have been created before migration on the target the source database schemas without a valid `TEMPORARY TABLESPACE` cannot be created on the target instance due to ORA-00959 errors.

Action

Create the needed temporary tablespaces on the Oracle Autonomous Database Dedicated infrastructure before you start the migration, or use tablespace remapping parameters to map other tablespaces into the `TEMP` tablespace when you start migration tools. Oracle Zero Downtime Migration and Database Migration Service can perform tablespace precreation and mapping automatically as part of the migration.

#### 19.10.15 has\_active\_data\_guard\_dedicated

The Premigration Advisor Tool check `has_active_data_guard_dedicated` detects whether Active Data Guard is being used on the source instance.

Result Criticality

Review suggested.

Has Fixup

No

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ATPD Autonomous Transaction Processing Dedicated

Scope

`INSTANCE`

Description

This check detects whether Active Data Guard is being used on the source instance.

Effect

If applications or schemas that are being migrated depend on certain capabilities of Active Data Guard, then those applications may no longer work after migration.

Action

Consider using Autonomous Data Guard on your target Oracle Autonomous Database instance. For more information, and to evaluate the capabilities of Autonomous Data Guard, see "Protect Critical Databases from Failures and Disasters Using Autonomous Data Guard" in Oracle Cloud Oracle Autonomous Database on Dedicated Exadata Infrastructure.

#### 19.10.16 has\_active\_data\_guard\_serverless

The Premigration Advisor Tool check `has_active_data_guard_serverless` detects whether Active Data Guard is being used on the source instance.

Result Criticality

Review suggested.

Has Fixup

No

Target Cloud

- ADWS Autonomous Data Warehouse Shared
- ATPS Autonomous Transaction Processing Shared

Scope

`INSTANCE`

Description

This check detects whether Active Data Guard is being used on the source instance.

Effect

If applications or schemas that are being migrated depend on certain capabilities of Active Data Guard, then those applications may no longer work after migration.

Action

Consider using Autonomous Data Guard on your target Oracle Autonomous Database instance. For more information, and to evaluate the capabilities of Autonomous Data Guard, see "Using Standby Databases with Autonomous Database for Disaster Recovery " in Oracle Cloud Using Oracle Autonomous Database on Shared Exadata Infrastructure.

#### 19.10.17 has\_basic\_file\_lobs

The Premigration Advisor Tool check `has_basic_file_lobs` indicates BASICFILE LOBs are present in the schema, which are not supported with Oracle Autonomous Database.

Result Criticality

Review required.

Has Fixup

No

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Scope

`SCHEMA`

Description

This check applies to schemas for Oracle Data Pump and Oracle GoldenGate migrations. When CPAT detects that one or more schema Owner's temporary tablespace contain BASICFILE LOBs, the schemas are listed in the report..

Effect

During migration, all `BASICFILE` LOBs are converted automatically to `SECUREFILE` LOBs at the time of the import.

Action

No action is required.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.18 has\_clustered\_tables

The Premigration Advisor Tool check `has_clustered_tables` indicates table clusters are present in the schema, which are not supported with Oracle Autonomous Database.

Result Criticality

Review suggested.

Has Fixup

No

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Scope

`SCHEMA`

Description

This check applies to schemas for Oracle Data Pump and Oracle GoldenGate migrations. When CPAT detects that one or more schema s contain table clusters, the schemas are listed in the report..

Effect

When tables are created with a `CLUSTER` clause on the Oracle Autonomous Database, the table is created as a regular table.

Action

No action is required. Consider doing some performance testing to ensure that there are no adverse effects.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.19 has\_columns\_of\_rowid\_type

The Premigration Advisor Tool check `has_columns_of_rowid_type` indicates tables with columns with `ROWID` data type that cannot be migrated.

Result Criticality

Action required.

Has Fixup

Yes

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ATPD Autonomous Transaction Processing Dedicated

Scope

`SCHEMA`

Description

This check applies to schemas for Oracle Data Pump and Oracle GoldenGate migrations. The `ROWID` data type is not enabled by default in Oracle Autonomous Database on Dedicated Exadata Infrastructure deployments.

Effect

By default, columns with `ROWID` data type cannot be migrated to ATPD or ADWD.

Action

You can choose to enable the `ROWID` data type by setting the initialization parameter `ALLOW_ROWID_COLUMN_TYPE` to `true` on the target ADBD instance. However, if you do enable it, then be aware that `ROWID` columns are incompatible with rolling upgrade operations, and other internal operations that physically move a row. At a minimum, during upgrades, Oracle recommends that you suspend database activities involving `ROWID`. Applications using `ROWID` columns should introduce correctness validation to check for logical errors in the application if a row relocates.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.20 has\_columns\_with\_local\_timezone

The Premigration Advisor Tool check `has_columns_with_local_timezone` indicates tables have local DBTIMEZONE columns that do not match the target instance DBTIMEZONE.

Result Criticality

Review required.

Has Fixup

Y

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Scope

`SCHEMA`

Description

This check applies to schemas for Oracle Data Pump and Oracle GoldenGate migrations. It identifies tables being migrated that have columns using `TIMESTAMP           WITH LOCAL TIMEZONE` data types when the source instance `DBTIMEZONE` does not match the target instance `DBTIMEZONE`.

Effect

Migrated data will appear to be corrupted, as it will be interpreted with an incorrect time zone. This issue can cause unexpected data and other application issues.

Action

Set the `DBTIMEZONE` on the target instance to match the source instance. For example: `ALTER DATABASE SET TIME_ZONE =         'America/New_York';`

CPAT generates a fixup script for this action, called `alter_time_zone.sql`. After applying this fixup on the target instance, you must restart the instance.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.21 has\_columns\_with\_media\_data\_types\_adb

The Premigration Advisor Tool check `has_columns_with_media_data_types_adb` indicates tables with multimedia data type that cannot be migrated.

Result Criticality

Action required.

Has Fixup

No

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Scope

`SCHEMA`

Description

This check applies to schemas for Oracle Data Pump and Oracle GoldenGate migrations. Multimedia object types such as those from `ORDSYS` cannot be used in Oracle Autonomous Database.

Effect

Migration of tables with multimedia columns will fail.

Action

Columns with media data types are not allowed in Oracle Autonomous Database. As an alternative, Oracle recommends that you consider using SecureFiles LOBs for media type storage.

Follow the instructions in the Oracle Multimedia README.txt file in `Oracle_home/ord/im/admin/README.txt`, or Oracle Support Document ID 2555923.1 to determine if Oracle Multimedia methods and packages are being used. If Oracle Multimedia is being used, then refer to Oracle Support Document ID 2347372.1 for suggestions on replacing Oracle Multimedia. Refer to Oracle Support Document ID 2375644.1 "How To Migrate Data From Oracle Multimedia Data Types to BLOB columns" for information on how to move data stored in Oracle Multimedia object types to SecureFiles LOBs.

**Related Topics**

- [Desupport of Oracle Multimedia Component in Oracle 19c (Doc ID 2555923.1)](https://support.oracle.com/rs?type=doc&id=2555923.1)
- [Oracle Multimedia Statement of Direction (Doc ID 2347372.1)](https://support.oracle.com/rs?type=doc&id=2347372.1)
- [How To Migrate Data From Oracle Multimedia Data Types to BLOB columns (Doc ID 2375644.1)](https://support.oracle.com/rs?type=doc&id=2375644.1)

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.22 has\_columns\_with\_media\_data\_types\_default

The Premigration Advisor Tool check `has_columns_with_media_data_types_default` indicates tables with multimedia columns.

Result Criticality

Action required.

Has Fixup

No

Scope

`SCHEMA`

Target Cloud

- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Description

This check applies to schemas for Oracle Data Pump and Oracle GoldenGate migrations. Multimedia object types such as those from `ORDSYS` are desupported in Oracle Database 19c and later releases.

Effect

Migration of tables with multimedia columns can fail.

Action

Oracle Multimedia was desupported in Oracle Database 19c. Oracle recommends that you consider using SecureFiles LOBs for media type storage.

Follow the instructions in the Oracle Multimedia README.txt file in `Oracle_home/ord/im/admin/README.txt`, or Oracle Support Document ID 2555923.1 to determine if Oracle Multimedia methods and packages are being used. If Oracle Multimedia is being used, then refer to Oracle Support Document ID 2347372.1 for suggestions on replacing Oracle Multimedia. Refer to Oracle Support Document ID 2375644.1 "How To Migrate Data From Oracle Multimedia Data Types to BLOB columns" for information on how to move data stored in Oracle Multimedia object types to SecureFiles LOBs.

**Related Topics**

- [Desupport of Oracle Multimedia Component in Oracle 19c (Doc ID 2555923.1)](https://support.oracle.com/rs?type=doc&id=2555923.1)
- [Oracle Multimedia Statement of Direction (Doc ID 2347372.1)](https://support.oracle.com/rs?type=doc&id=2347372.1)
- [How To Migrate Data From Oracle Multimedia Data Types to BLOB columns (Doc ID 2375644.1)](https://support.oracle.com/rs?type=doc&id=2375644.1)

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.23 has\_columns\_with\_spatial\_data\_types

The Premigration Advisor Tool check `has_columns_with_spatial_data_types` indicates there are spatial objects that are not fully supported.

Result Criticality

Review required.

Has Fixup

Yes

Target Cloud

- ADWS Autonomous Data Warehouse Shared
- ATPS Autonomous Transaction Processing Shared

Scope

`SCHEMA`

Description

This check applies to schemas for Oracle Data Pump and Oracle GoldenGate migrations. It indicates the presence of spatial data type objects.

Effect

Because some of the functionality of spatial objects are dependent on the Oracle Java (`JAVAVM`) feature, there can be objects not fully supported with Oracle Autonomous Databases on Shared Infrastructure until `JAVAVM` is enabled.

Action

Enable the JAVAVM feature on the target system by running this SQL, and then restart your instance:

```
BEGIN
   DBMS_CLOUD_ADMIN.ENABLE_FEATURE(
       feature_name => 'JAVAVM' );
END;
/
```

For more information on enabling the JAVAVM feature see "Using Oracle Java on Autonomous Database" in Oracle Cloud Using Oracle Autonomous Database Serverless For more information on using Spatial on ADB, see "Use Oracle Spatial with Autonomous Database" in Oracle Cloud Using Oracle Autonomous Database Serverless.

#### 19.10.24 has\_common\_objects

The Premigration Advisor Tool check `has_common_objects` indicates there are common objects in the database instance.

Result Criticality

Action required.

Has Fixup

Yes

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared
- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Scope

`INSTANCE`

Description

This is a default check. This check applies to source instances for Oracle Data Pump and Oracle GoldenGate migrations. It indicates the presence of common objects.

Effect

Oracle Data Pump does not migrate common objects to Oracle Autonomous Database in Oracle Cloud, and these objects are not supported on Oracle Autonomous Database (ADB). Anything dependent on the common objects will fail to be migrated properly.

Action

Those common objects needed by applications must be recreated on the target system before you start the migration. When targeting ADB, the common objects that you require must be recreated as local objects. This can be done using `DBMS_METADATA.GET_DDL`, as shown in Oracle Support Document ID 2739952.1

**Related Topics**

- [How to Extract DDL for User including Privileges and Roles Using dbms\_metadata.get\_ddl (Doc ID 2739952.1)](https://support.oracle.com/rs?type=doc&id=2739952.1)

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.25 has\_compression\_disabled\_for\_objects

The Premigration Advisor Tool check `has_compression_disabled_for_objects` indicates there are tables or partitions lacking a `COMPRESSION` clause.

Result Criticality

Review suggested.

Has Fixup

No

Target Cloud

- ADWS Autonomous Data Warehouse Shared
- ATPS Autonomous Transaction Processing Shared

Scope

`SCHEMA`

Description

This check applies to source schema for Oracle Data Pump and Oracle GoldenGate migrations. It indicates the presence of tables or partitions that do not have a `COMPRESSION` clause. Tables and Partitions must be compressed to `QUERY HIGH` in Oracle Autonomous Data Warehouse (ADW).

Effect

When migrating to ADW, if a table or partition SQL data definition language (DDL) statement does not contain a `COMPRESSION` clause, then it is created during the migration with a default compression of `QUERY HIGH`.

Action

No action required. To modify this behavior, either add a compression clause of your choice (or even `NOCOMPRESS`) before starting the export, or alter the compression clause after the import..

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.26 has\_csmig\_schema

The Premigration Advisor Tool check `has_csmig_schema` indicates the CSSCAN utility is installed and configured on the source database..

Result Criticality

Review suggested.

Has Fixup

Yes

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared
- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Scope

`UNIVERSAL`

Description

This is a default check. The CSSCAN utility is no longer supported, and has been replaced by the Database Migration Assistant for Unicode (DMU) Tool..

Effect

Migration tools can ignore any objects, users, or roles related with CSSCAN utility.

Action

Remove the CSMIG user and any objects created by the CSSCAN utility: For example:

```
BEGIN FOR REC IN (SELECT SYNONYM_NAME FROM DBA_SYNONYMS WHERE TABLE_OWNER = 'CSMIG') LOOP
      EXECUTE IMMEDIATE 'DROP PUBLIC SYNONYM ' || REC.SYNONYM_NAME; END LOOP; END; / DROP VIEW
      SYS.CSMV$KTFBUE; DROP USER CSMIG CASCADE;
```

Use The Database Migration Assistant for Unicode (DMU) Tool to scan for character set migration issues. For more information on DMU see Oracle Support Document ID 1272374.1

**Related Topics**

- [The Database Migration Assistant for Unicode (DMU) Tool (Doc ID 1272374.1)](https://support.oracle.com/rs?type=doc&id=1272374.1)

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.27 has\_data\_in\_other\_tablespaces\_dedicated

The Premigration Advisor Tool check `has_data_in_other_tablespaces_dedicated` identifies data subject to tablespace restrictions when migrating to Oracle Autonomous Databases on Dedicated Infrastructure..

Result Criticality

Action required.

Has Fixup

No

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ATPD Autonomous Transaction Processing Dedicated

Scope

`SCHEMA`

Description

This check applies to source schema for Oracle Data Pump and Oracle GoldenGate migrations. It indicates the presence of data that is subject to tablespace restrictions when migrating to Autonomous Databases on Dedicated Infrastructure.

Effect

For ATPD and ADWD (Dedicated Infrastructure), errors are reported for tablespaces that have not been precreated on the target. If tablespace mapping is not employed, then errors can occur during migration.

Action

If you are migrating the database using either Zero Downtime Migration (ZDM) or Database Migration Service (DMS) then they precreate and map tablespaces automatically, so the issue does not occur.

If you are migrating using Oracle Data Pump manually, then specify `IGNORE=TABLESPACE` and `REMAP_TABLESPACE='%:DATA'` in your Data Pump `impdp` parameter file, so that other tablespaces into the `DATA` tablespace when starting migration tooling.

In all cases, you should assess your application for any dependencies on specific tablespace names.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.28 has\_data\_in\_other\_tablespaces\_serverless

The Premigration Advisor Tool check `has_data_in_other_tablespaces_serverless` identifies data subject to tablespace restrictions when migrating to Oracle Autonomous Databases on Shared Infrastructure.

Result Criticality

Action required.

Has Fixup

No

Target Cloud

- ADWS Autonomous Data Warehouse Shared
- ATPS Autonomous Transaction Processing Shared

Scope

`SCHEMA`

Description

This check applies to source schema for Oracle Data Pump and Oracle GoldenGate migrations. It indicates the presence of tables that have other tablespaces mapped into their table.

Effect

User-defined tablespaces are not allowed in ATPS and ADWS (Serverless Infrastructure). Each database in this cloud environment has a single 'DATA' tablespace. If tablespace mapping is not employed, and the user performing migration does not have privileges on the `DATA` tablespace, then errors can occur during migration.

Action

If you are migrating the database using either Zero Downtime Migration (ZDM) or Database Migration Service (DMS) then they precreate and map tablespaces automatically, so the issue does not occur.

If you are migrating using Oracle Data Pump manually, then specify `IGNORE=TABLESPACE` and `REMAP_TABLESPACE='%:DATA'` in your Data Pump `impdp` parameter file, so that other tablespaces into the `DATA` tablespace when starting migration tooling.

In all cases, you should assess your application for any dependencies on specific tablespace names.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.29 has\_db\_link\_synonyms

The Premigration Advisor Tool check `has_db_link_synonyms` indicates the schema contains synonyms with database links.

Result Criticality

Review suggested.

Has Fixup

Yes

Target Cloud

- ADWS Autonomous Data Warehouse Shared
- ATPS Autonomous Transaction Processing Shared

Scope

`SCHEMA`

Description

This check applies to source schema for Oracle Data Pump and Oracle GoldenGate migrations. Database links cannot be migrated.

Effect

After migration, applications relying on the synonym will fail until the database links are recreated.

Action

After migration is complete, create database links in the target Oracle Autonomous Database in using `DBMS_CLOUD_ADMIN.CREATE_DATABASE_LINK`, and then recreate the synonyms.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.30 has\_db\_links

The Premigration Advisor Tool check `has_db_links` indicates the schema contains synonyms with database links.

Result Criticality

Review required

Has Fixup

No

Target Cloud

- ADWS Autonomous Data Warehouse Shared
- ATPS Autonomous Transaction Processing Shared

Scope

`SCHEMA`

Description

This check applies to source schema for Oracle Data Pump and Oracle GoldenGate migrations. Database links cannot be migrated.

Effect

After migration, applications relying on database links will fail until the database links are recreated.

Action

Precreate Database Links manually in ADB using `DBMS_CLOUD_ADMIN.CREATE_DATABASE_LINK` in the respective database schemas before migrating. The proper sequence of statements is as follows:

1. Create the schemas that own the links.
2. Create the links using `DBMS_CLOUD_ADMIN.CREATE_DATABASE_LINK`.
3. Import the schemas that you are migrating.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.31 has\_dbms\_credentials

The Premigration Advisor Tool check `has_dbms_credentials` indicates the schema contains credentials that were not created with `DBMS_CLOUD.CREATE_CREDENTIAL`.

Result Criticality

Review required

Has Fixup

No

Target Cloud

- ADWS Autonomous Data Warehouse Shared
- ATPS Autonomous Transaction Processing Shared

Scope

`SCHEMA`

Description

This check applies to source schema for Oracle Data Pump and Oracle GoldenGate migrations. Credentials originally created with `DBMS_CREDENTIAL` or `DBMS_SCHEDULER` packages cannot be automatically migrated to Oracle Autonomous Database.

Effect

After migration, users with credentials originally created with `DBMS_CREDENTIAL` or `DBMS_SCHEDULER` packages receive ORA-27486: insufficient privileges errors. These credentials cannot be migrated automatically to ADBS.

Action

After migration is complete, verify that the listed credentials are still required on the target Oracle Autonomous Database instance. If these credentials are required, then recreate the credentials using `DBMS_CLOUD.CREATE_CREDENTIAL`. For more information, see My Oracle Support Document ID 2746284.1.

**Related Topics**

- [Autonomous Database (Shared) - dbms\_credential.create\_credential failed with ORA-27486 (Doc ID 2746284.1)](https://support.oracle.com/rs?type=doc&id=2746284.1)

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.32 has\_dbms\_credentials

The Premigration Advisor Tool check `has_dbms_credentials` indicates the schema contains credentials that were not created with `DBMS_CLOUD.CREATE_CREDENTIAL`.

Result Criticality

Review required

Has Fixup

No

Target Cloud

- ADWS Autonomous Data Warehouse Shared
- ATPS Autonomous Transaction Processing Shared

Scope

`SCHEMA`

Description

This check applies to source schema for Oracle Data Pump and Oracle GoldenGate migrations. Credentials originally created with `DBMS_CREDENTIAL` or `DBMS_SCHEDULER` packages cannot be automatically migrated to Oracle Autonomous Database.

Effect

After migration, users with credentials originally created with `DBMS_CREDENTIAL` or `DBMS_SCHEDULER` packages receive ORA-27486: insufficient privileges errors. The schema Owner's default tablespace must be `'DATA'`.

Action

The schema owner's `DEFAULT TABLESPACE` will be modified in ADB to be `'DATA'`. If a user has quota on multiple tablespaces, then after migration is complete, ensure that the proper quota is set.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.33 has\_directories

The Premigration Advisor Tool check `has_directories` indicates that there are directories objects in the source database.

Result Criticality

Review required

Has Fixup

No

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Scope

`INSTANCE`

Description

This check indicates that there are directories objects in the source database.

Effect

After migration, applications that rely on the directories will not work until the directories on the source database are recreated on the target database.

Action

After migration is complete, recreate the directories on the Oracle Autonomous Database instance.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.34 has\_enabled\_scheduler\_jobs

The Premigration Advisor Tool check `has_enabled_scheduler_jobs     ` indicates that there are List scheduler jobs that may interfere with Oracle Data Pump export.

Result Criticality

Review suggested

Has Fixup

No

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared
- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Scope

`INSTANCE`

Description

This is a default check. This check indicates that there are List scheduler jobs that may interfere with Oracle Data Pump export.

Effect

If a scheduler job runs at the same time as a `FULL` export is under way, then Oracle Data Pump Export can fail with an ORA-39127 error.

Action

Disable any non-critical scheduler jobs, or plan the export at a time when you are certain that no scheduler jobs are running. Either stop scheduler jobs before the migration, or plan the export for a time when you are certain that no scheduler jobs are running.

You can run the following SQL statement to ensure no Scheduler Jobs are running during migration:

```
ALTER SYSTEM SET JOB_QUEUE_PROCESSES=0;
```

No restart is required after you run the statement.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.35 has\_external\_tables\_dedicated

The Premigration Advisor Tool check `has_external_tables_dedicated` indicates that Non-Cloud Objects Storage External tables exist in the source database.

Result Criticality

Review required

Has Fixup

No

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ATPD Autonomous Transaction Processing Dedicated

Scope

`SCHEMA`

Description

This check indicates that Non-Cloud Objects Storage external tables exist in the source database. These tables are not allowed in Oracle Autonomous Databases.

Effect

Applications relying on user-created external tables will not function as expected.

Action

Consider using the `DBMS_CLOUD` package to create external tables that use Cloud Object Storage.

#### 19.10.36 has\_external\_tables\_default

The Premigration Advisor Tool check `has_external_tables_default` indicates that external tables cannot be migrated unless the `DIRECTORY` objects the tables rely on have been created.

Result Criticality

Action required

Has Fixup

No

Target Cloud

This is a default check. It applies to the following:

- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Scope

`SCHEMA`

Description

This check indicates that external tables cannot be migrated unless the `DIRECTORY` objects that the tables rely on have been created already in the target database.

Effect

The schema mode migration of external tables will fail when those tables rely on `DIRECTORY` objects that don't already exist.

Action

Before migration, create the necessary `DIRECTORY` objects on the target database, or migrate to the target database using Full mode.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.37 has\_external\_tables\_serverless

The Premigration Advisor Tool check `has_external_tables_serverless` indicates that there are non-cloud Objects Storage external tables in the source database.

Result Criticality

Review required

Has Fixup

No

Target Cloud

- ADWS Autonomous Data Warehouse Shared
- ATPS Autonomous Transaction Processing Shared

Scope

`SCHEMA`

Description

Non-Cloud Objects Storage External tables were found. These objects are not allowed in Oracle Autonomous Database.

Effect

Applications relying on user-created external tables will not function as expected. External tables in Oracle Autonomous Database (ADB) must be recreated using Object Storage Service or File Storage Service.

Attempting to create a non-Cloud Object Storage external tables as part of the migration results in those tables being created as non-external tables.

Action

Drop the empty imported table. Use the `DBMS_CLOUD` package to create External Tables using Cloud Object Storage Service or use File Storage Service. for more info see

#### 19.10.38 has\_fmw\_registry\_in\_system

The Premigration Advisor Tool check `has_fmw_registry_in_system` indicates that the Fusion Middleware Schema Version Registry must be moved out of the `SYSTEM` schema before migration.

Result Criticality

Action required

Has Fixup

No

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Scope

`INSTANCE`

Description

The Fusion Middleware Schema Version Registry is in the `SYSTEM` schema. It must be moved out of the `SYSTEM` schema before you start the migration.

Effect

If the Fusion Middleware Version Registry is not moved, then after upgrade, vital information regarding what Fusion Middleware applications are installed will be lost.

Action

Before migration, run the Fusion Middleware Upgrade Assistant command `ua -moveRegistry`.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.40 has\_ilm\_ado\_policies

The Premigration Advisor Tool check `has_ilm_ado_policies` indicates that Information Lifestyle Management (ILM) Automatic Data Optimization Policies (ADO) will not migrate.

Result Criticality

Review required

Has Fixup

No

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Scope

`SCHEMA`

Description

Tables exist with ILM Automatic Data Optimization Policies. These policies will not migrate to Oracle Autonomous Database.

Effect

Tables with ILM ADO Policies (Release 12c and later) will be created without the `ILM ADO` Policy in Oracle Autonomous Transaction Processing (ATP) and Oracle Autonomous Data Warehouse (ADW).

Action

No action is required.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.41 has\_incompatible\_jobs

The Premigration Advisor Tool check `has_incompatible_jobs` indicates that Information Lifestyle Management (ILM) Automatic Data Optimization Policies (ADO) will not migrate.

Result Criticality

Review required

Has Fixup

No

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Scope

`SCHEMA`

Description

Scheduler Jobs and Programs other than `PLSQL_BLOCK` or `STORED_PROCEDURE` are present on the source, but not supported on Oracle Autonomous Database (ADB).

Effect

Scheduler Jobs and Programs types such as `EXECUTABLE` and `EXTERNAL_SCRIPT` will not run on Oracle Autonomous Database.

Action

Databases using unsupported Job or Program types should be modified before migrating to Oracle Autonomous Database. Recreate required Job or Programs using types allowed in ADB

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.42 has\_index\_organized\_tables

The Premigration Advisor Tool check `has_index_organized_tables` indicates that Index Organized tables are present in the source database.

Result Criticality

Review suggested

Has Fixup

No

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Scope

`SCHEMA`

Description

Index-organized tables are not allowed in Oracle Autonomous Database (ADB). However, attempting to create one does not generate an error. Instead, a heap-organized table with a primary key index is created.

Effect

The recreated tables can perform differently, so you should review them.

Action

Tables in the target database are created as non-index-organized tables (that is, as regular tables).

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.43 has\_java\_objects

The Premigration Advisor Tool check `has_java_objects` indicates that there are Java objects present in the source database.

Result Criticality

Action required

Has Fixup

Yes

Target Cloud

- ADWS Autonomous Data Warehouse Shared
- ATPS Autonomous Transaction Processing Shared

Scope

`SCHEMA`

Description

Java objects will not migrate by default.

Effect

When the Java virtual machine (`JAVAVM`) feature is not enabled on the target system, any applications relying on Java objects will fail after migration.

Action

Non-essential Java Objects should be excluded from the migration process. Enable the `JAVAVM` feature on the target system, as described in "Using Oracle Java on Autonomous Database" in Oracle Autonomous Database Using Oracle Autonomous Database on Shared Exadata Infrastructure.

#### 19.10.44 has\_java\_source

The Premigration Advisor Tool check `has_java_source` indicates that there are Java sources present in the source database.

Result Criticality

Action required

Has Fixup

Yes

Scope

`SCHEMA`

Target Cloud

- ADWS Autonomous Data Warehouse Shared
- ATPS Autonomous Transaction Processing Shared

Description

Java sources will not migrate by default.

Effect

When the Java virtual machine (`JAVAVM`) feature is not enabled on the target system, any applications relying on Java objects will fail after migration.

Action

Non-essential Java Objects should be excluded from the migration process. Enable the `JAVAVM` feature on the target system, as described in "Using Oracle Java on Autonomous Database" in Oracle Autonomous Database Using Oracle Autonomous Database on Shared Exadata Infrastructure

#### 19.10.45 has\_libraries

The Premigration Advisor Tool check `has_libraries` indicates that there are applications that require the `CREATE LIBRARY` statement.

Result Criticality

Action required

Has Fixup

No

Scope

`SCHEMA`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Description

The `CREATE LIBRARY` statement is not allowed on Oracle Autonomous Database.

Effect

Applications that depend on these libraries will fail, because the libraries will not be created on the target instance.

Action

Applications must be updated to remove their dependencies on any listed libraries.

Consider using Functions for business logic previously implemented in external libraries.

#### 19.10.46 has\_logging\_off\_for\_partitions

The Premigration Advisor Tool check `has_logging_off_for_partitions` indicates that there are Partitions using the `NOLOGGING` storage attribute.

Result Criticality

Review suggested

Has Fixup

No

Scope

`SCHEMA`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Description

Partitions with the `NOLOGGING` storage attribute are be changed to `LOGGING` during migration.

Effect

Partitions created with `NOLOGGING` will automatically be created in Oracle Autonomous Database as partitions with `LOGGING`. Check the `LOGGING` attribute in `DBA_TAB_PARTITIONS`.

Action

No action required.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.47 has\_logging\_off\_for\_subpartitions

The Premigration Advisor Tool check `has_logging_off_for_subpartitions` indicates that there are Partitions using the `NOLOGGING` storage attribute.

Result Criticality

Review suggested

Has Fixup

No

Scope

`SCHEMA`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Description

Subpartitions with the `NOLOGGING` storage attribute are be changed to `LOGGING` during migration.

Effect

Subpartitions created with `NOLOGGING` will automatically be created in Oracle Autonomous Database as subpartitions with `LOGGING`. Check the `LOGGING` attribute in `DBA_TAB_SUBPARTITIONS`.

Action

No action required.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.48 has\_logging\_off\_for\_tables

The Premigration Advisor Tool check `has_logging_off_for_tables` indicates that there are tables using the `NOLOGGING` storage attribute.

Result Criticality

Review suggested

Has Fixup

No

Scope

`SCHEMA`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Description

Tables with the `NOLOGGING` storage attribute are be changed to `LOGGING` during migration.

Effect

Tables created with `NOLOGGING` will automatically be created in Oracle Autonomous Database as tables with `LOGGING`. Check the `LOGGING` attribute in `DBA_TABLES`.

Action

No action required.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.49 has\_low\_streams\_pool\_size

The Premigration Advisor Tool check `has_low_streams_pool_size` indicates that Mining Models with unexpected or incorrect attributes are detected.

Result Criticality

Action required

Has Fixup

No

Scope

`SCHEMA`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared
- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Description

Mining models are database schema objects that perform data mining. Mining models with unexpected or incorrect attributes are detected. These mining models will not migrate.

Effect

Mining models with issues will not be exported properly, and cause `ORA-39083` errors on import.

Action

Download and apply Patch ID 33270686

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.50 has\_noexport\_object\_grants

The Premigration Advisor Tool check `has_noexport_object_grants` indicates that Oracle Data Pump is unable to export all object grants.

Result Criticality

Review required

Has Fixup

Yes

Scope

`SCHEMA`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared
- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Description

Oracle Data Pump is unable to export all object grants.

Effect

Object grants required for your application may be missing on the target instance, preventing Oracle Data Pump from exporting them to the target instance.

Action

Recreate any required grants on the target instance. See My Oracle Support Document ID 1911151.1 for more information. Note that any `SELECT` grants on system objects will need to be replaced with `READ` grants, because `SELECT` is no longer allowed on system objects.

**Related Topics**

- [Data Pump: GRANTs On SYS Owned Objects Are Not Transferred With Data Pump And Are Missing In The Target Database (Doc ID 1911151.1)](https://support.oracle.com/rs?type=doc&id=1911151.1)

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.51 has\_oracle\_streams

The Premigration Advisor Tool check `has_oracle_streams` indicates that Oracle Streams is configured in the database.

Result Criticality

Review REQUIRED

Has Fixup

No

Scope

`INSTANCE`

Target Cloud

This is a default check. It applies to the following:

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Description

Starting with Oracle Database 19c, Oracle Streams is desupported. Oracle strongly advices you to remove any streams configuration manually.

Effect

Oracle Streams is a desupported feature. You must remove it.

Action

Remove the Oracle Streams configuration. For detailed steps, refer to the section Removing an Oracle Streams Configuration in the Oracle Streams Concepts and Administration Guide specific for the Oracle release from which you are removing. For Oracle Database releases earlier than 12.1 (12.1.0.2), the procedure `           dbms_streams_adm.remove_streams_configuration` must not be used, because it can lead to unwanted results. Instead, use the other procedures (`dbms_capture_adm.drop_capture`, `dbms_apply_adm.drop_apply`, `dbms_streams_adm.remove_queue`, and so on). For Oracle Database releases 12.1 (12.1.0.2) and higher, procedure `dbms_streams_adm.remove_streams_configuration` can be safely used. To avoid issues on import consider using the Oracle Data Pump option `'STREAMS_CONFIGURATION=N'`.

#### 19.10.52 has\_parallel\_indexes\_enabled

The Premigration Advisor Tool check `has_parallel_indexes_enabled` indicates that `PARALLEL` clause indexes exist.

Result Criticality

Review suggested

Has Fixup

No

Scope

`SCHEMA`

Target Cloud

- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Description

When Parallel `DEGREE` is specified greater than `1` on `INDEX`, this setting can result in unexpected behavior after migration.

Effect

When migrating to Oracle Autonomous Database Transaction Processing (ATP), if a `PARALLEL` clause is specified on the index in your source database, then the clause remains with the index when it is created on the target database, either by using Oracle Data Pump, or by using manual methods. When the `PARALLEL` degree is greater than `1`, this configuration can result in SQL statements running in parallel that are unknown to the end-user.

Action

To specify serial processing, either change the `INDEX` parallel clause to `NOPARALLEL`, or alter the `PARALLEL` degree to `1` before or after the migration.

**Related Topics**

- [Data Pump: GRANTs On SYS Owned Objects Are Not Transferred With Data Pump And Are Missing In The Target Database (Doc ID 1911151.1)](https://support.oracle.com/rs?type=doc&id=1911151.1)

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.53 has\_profile\_not\_default

The Premigration Advisor Tool check `has_profile_not_default` indicates that schemas exist whose `PROFILE` is not available on the target system.

Result Criticality

Action Required

Has Fixup

Yes

Scope

`SCHEMA`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared
- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Description

Identifies schemas whose `PROFILE` is not available on the target system.

Effect

Creation of the schema on the target system fails due to the missing `PROFILE`. This is a runtiume issue, unless there are profiles used that aren't available on the target instance. In that case, the severity is Action Required.

Action

Either use Oracle Data Pump in `FULL` mode, or create the needed profiles before migration on the target system, and then use the `--analysisprops` option with a properties file created by using CPAT with the `--gettargetprops` option.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.54 has\_public\_synonyms

The Premigration Advisor Tool check `has_public_synonyms` indicates that Public Synonyms exist in source system schemas.

Result Criticality

Review required

Has Fixup

No

Scope

`SCHEMA_ONLY`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared
- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Description

Identifies schemas whose that contain Public Synonyms. Oracle Data Pump does not migrate Public Synonyms in `SCHEMA` mode.

Effect

Applications relying on Public Synonyms will not work correctly until the Public Synonyms are recreated on the target instance.

Action

Either use Oracle Data Pump in `FULL` mode, or recreate the listed relevant objects on the target instance.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.55 has\_refs\_to\_restricted\_packages\_dedicated

The Premigration Advisor Tool check `has_refs_to_restricted_packages_dedicated` indicates that there are references to partially or completely unsupported packages.

Result Criticality

Review required

Has Fixup

No

Scope

`SCHEMA`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ATPD Autonomous Transaction Processing Dedicated

Description

Checks for references to packages that are not supported, or that are only partially supported.

Effect

Applications that reference unsupported or restricted use packages can fail.

Action

Applications that reference unsupported packages must be modified before migration to Oracle Autonomous Database Dedicated. Applications referencing partially supported packages require testing and validation to ensure that they only use unrestricted functions and procedures.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.56 has\_refs\_to\_restricted\_packages\_serverless

The Premigration Advisor Tool check `has_refs_to_restricted_packages_serverless` indicates that there are references to partially or completely unsupported packages.

Result Criticality

Review required

Has Fixup

No

Scope

`SCHEMA`

Target Cloud

- ADWS Autonomous Data Warehouse Shared
- ATPS Autonomous Transaction Processing Shared

Description

Checks for references to packages that are not supported, or that are only partially supported.

Effect

Applications that reference unsupported or restricted use packages can fail.

Action

Applications that reference unsupported packages must be modified before migration to Oracle Autonomous Database Serverless. Applications referencing partially supported packages require testing and validation to ensure that they only use unrestricted functions and procedures.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.57 has\_refs\_to\_user\_objects\_in\_sys

The Premigration Advisor Tool check `has_refs_to_user_objects_in_sys` indicates that there are user schema objects dependent on `SYS` or `SYSTEM`.

Result Criticality

Action required

Has Fixup

No

Scope

`SCHEMA`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Description

Detects if objects in user schemas depend on user-defined objects in `SYS` or `SYSTEM` schemas.

Effect

Migration will fail for schemas that depend on user-defined objects in `SYS` or `SYSTEM`.

Action

Oracle recommends that you move user-defined objects in `SYS` and `SYSTEM` schemas before migration, and update the references. Consider dropping any user-defined objects that are no longer required.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.58 has\_role\_privileges

The Premigration Advisor Tool check `has_role_privileges` indicates that some role privileges used in the source database are not available in the target database

Result Criticality

Action required

Has Fixup

No

Scope

`SCHEMA`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Description

Detects the presence of role privileges used in the source database that are not available on the target Oracle Autonomous Database.

Effect

After migration, applications can encounter operation failures due to role privilege issues.

Action

Find alternatives for those roles granted in the source database that are not available in the target Oracle Autonomous Database instance. For example, you may want to substitute the `PDB_DBA` role for some schemas granted the DBA role on the source instance. Similarly, you may want to substitute the `DATAPUMP_CLOUD_IMP` role on the target instance for schemas granted `DATAPUMP_IMP_FULL_DATABASE` or `IMP_FULL_DATABASE` on the source instance. Whether such alternatives are appropriate can only be determined with testing, and by experts familiar with the applications where these role privileges occur.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.59 has\_sqlt\_objects\_adb

The Premigration Advisor Tool check `has_sqlt_objects_adb` indicates that `SQLTXPLAIN` objects are detected.

Result Criticality

Review suggested

Has Fixup

No

Scope

`UNIVERSAL`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Description

Detects the presence of `SQLTXPLAIN` (SQLT) objects, which are not supported on Oracle Autonomous Database.

Effect

Objects related to `SQLTXPLAIN` will fail on import to Oracle Autonomous Database (ADB), which can cause import errors.

Action

Oracle recommends that administrators migrating a source database to Oracle Autonomous Database apply `sqdrop.sql` in the installation directory under the `SQLTXPLAIN` installation to drop all `SQLTXPLAIN` and `SQLTXADMIN` objects. See My Oracle Support Document ID 1614107.1 for more information.

#### 19.10.60 has\_sqlt\_objects\_default

The Premigration Advisor Tool check `has_sqlt_objects_default` indicates that ` SQLTXPLAIN` objects are detected that Oracle Data Pump does not export.

Result Criticality

Review suggested

Has Fixup

No

Scope

`UNIVERSAL`

Target Cloud

- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Description

Detects the presence of `SQLTXPLAIN` (SQLT) objects that are not exported by Oracle Data Pump.

Effect

Some objects related to `SQLTXPLAIN` will not be imported on the target instance, possibly causing import errors.

Action

Oracle recommends that `SQLTXPLAIN` users run `sqcreate.sql` in the target environment after the import is complete. The `sqcreate.sql` script runs `sqdrop.sql`, and then reinstalls all required objects. For more information, see My Oracle Support Document ID 1614107.1.

#### 19.10.61 has\_sys\_privileges

The Premigration Advisor Tool check `has_sys_privileges` indicates that some system privileges in the source database are not available in the target database.

Result Criticality

Action required

Has Fixup

No

Scope

`SCHEMA`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Description

Detects that there are some system privileges used in the source database that are not available on the Oracle Autonomous Database.

Effect

Operation failures can occur on the Oracle Autonomous Database, because of system privilege issues.

Action

Verify whether all system privileges will be needed on the Oracle Autonomous Database, and remove the grants for those privileges that are no longer needed. Find alternatives for the granted system privileges that are not available in the target Oracle Autonomous Database (ADB). For example, with schemas in ADB instances, replace `GRANT           CREATE JOB` to `USER-WHO-HAD-CREATE-ANY-JOB` Whether such alternatives are appropriate can only be determined by experts familiar with the applications in question and with testing.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.62 has\_tables\_that\_fail\_with\_dblink

The Premigration Advisor Tool check `has_tables_that_fail_with_dblink` indicates that there are tables with `LONG` or `LONG RAW` data types

Result Criticality

Action required

Has Fixup

No

Scope

`SCHEMA`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared
- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Description

Tables with `LONG` or `LONG RAW` data types will not migrate over a `DBLINK` with Oracle Data Pump.

All forms of `LONG` data types (`LONG`, `LONG RAW`, `LONG VARCHAR`, `LONG VARRAW`) were deprecated in Oracle8i Release 8.1.6. For succeeding releases, the `LONG` data type was provided for backward compatibility with existing applications. In new applications developed with later releases, Oracle strongly recommends that you use `CLOB` and `NCLOB` data types for large amounts of character data.

Effect

Any applications relying on tables with `LONG` or `LONG           RAW` data types will fail.

Action

Use Oracle Data Pump without `DBLINK`, or exclude the schemas and tables that have columns with `LONG` or `LONG RAW` data types.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.63 has\_tables\_with\_long\_raw\_datatype

The Premigration Advisor Tool check `has_tables_with_long_raw_datatype` indicates that there are tables with `LONG` or `LONG RAW` data types

Result Criticality

Action required

Has Fixup

No

Scope

`SCHEMA`

Target Cloud

- ADWS Autonomous Data Warehouse Shared

Description

ADWS does not support tables with `LONG` or `LONGRAW` data where the table has the Oracle Hybrid Columnar Compression (`HCC`) compression clause, or where compression is `DISABLED`.

Effect

Tables with `LONG` or `LONG RAW` data types will not migrate.

In Oracle Autonomous Data Warehouse (ADW), tables with `LONG` or `LONG RAW` data types are not created when the table has either an HCC compression clause, or compression is `DISABLED`, which would result with tables being compressed by default with HCC compressed by default on ADW.

All forms of `LONG` data types (`LONG`, `LONG RAW`, `LONG VARCHAR`, `LONG VARRAW`) were deprecated in Oracle8i Release 8.1.6. For succeeding releases, the `LONG` data type was provided for backward compatibility with existing applications. In new applications developed with later releases, Oracle strongly recommends that you use `CLOB` and `NCLOB` data types for large amounts of character data.

Action

Oracle recommends that you you create the table manually on ADW with compression enabled.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.64 has\_tables\_with\_xmltype\_column

The Premigration Advisor Tool check `has_tables_with_xmltype_column` indicates that there are tables with `XMLTYPE` columns.

Result Criticality

Action required

Has Fixup

No

Scope

`SCHEMA`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Description

Tables with `XMLType` column will not migrate unless the `STORAGE_TYPE` setting is `BINARY`.

Effect

Any applications relying on `XMLType` columns that are not stored as `BINARY` will fail.

Action

Tables with `XMLType` columns defined with CLOB or Object-Relational storage are not supported in Oracle Autonomous Database. When the relevant objects column `XMLSCHEMA` is not empty, this indicates that your application uses XML Schema Objects, and additional work may be required. For non-schema types, the `BINARY` storage option must be used. See Oracle Support Document ID 1581065.1 for information about how to convert `CLOB` columns to `BINARY`.

**Related Topics**

- [How to Convert Basicfile CLOB to Securfile Binary XML (Doc ID 1581065.1)](https://support.oracle.com/rs?type=doc&id=1581065.1)

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.65 has\_trusted\_server\_entries

The Premigration Advisor Tool check `has_trusted_server_entries` indicates that there are `TRUSTED_SERVER` entries that cannot be recreated on Oracle Autonomous Database.

Result Criticality

Runtime

Has Fixup

No

Scope

`INSTANCE`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Description

Checks for `TRUSTED_SERVER` entries. These entries cannot be recreated on Oracle Autonomous Database (ADB).

Effect

The `DBMS_DISTRIBUTED_TRUST_ADMIN` package is not available on Oracle Autonomous Database (ADB). As a result, any `TRUSTED_SERVER` entries other than the default (Trusted:All) will not be recreated on the target ADB instance.

Action

To avoid any exceptions reported by Oracle Data Pump during migration from the source database to the target database, specify `exclude=trusted_db_link`. To control access to your ADB instance, use Oracle Cloud Infrastructure firewall features to control access to your ADB instance.

#### 19.10.66 has\_unstructured\_xml\_indexes Check

The Premigration Advisor Tool check `has_unstructured_xml_indexes` indicates that there are Unstructured XML Indexes.

Result Criticality

Review required

Has Fixup

No

Scope

`SCHEMA`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Description

This check indicates that unstructured XML indexes are present. Unstructured indexes are not supported on ADB

Effect

Attempting to create an unstructured XML index will fail. Import errors should be expected when migrating unstructured XML indexes.

Action

Before migration, recreate the indexes using XML Search Index, as described in Oracle XML DB Developer’s Guide

#### 19.10.67 has\_user\_defined\_objects\_in\_sys

The Premigration Advisor Tool check `has_user_defined_objects_in_sys` indicates that there are User-defined objects in the `SYS` schema.

Result Criticality

Action required

Has Fixup

No

Scope

`INSTANCE`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Description

This check indicates that user-defined objects exist in the `SYS` schema.

Effect

User-defined objects in the `SYS` schema will not migrate. Any applications relying on user-defined objects in `SYS` will fail.

Action

Before migration, Oracle recommends that you move out of `SYS` any user-defined objects. Update any hardcoded references to those objects. Consider dropping any user-defined objects that are no longer required.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.68 has\_user\_defined\_objects\_in\_system

The Premigration Advisor Tool check `has_user_defined_objects_in_system` indicates that there are User-defined objects in the `SYSTEM` schema.

Result Criticality

Action required

Has Fixup

No

Scope

`INSTANCE`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Description

This check indicates that user-defined objects exist in the `SYSTEM` schema.

Effect

User-defined objects in the `SYSTEM` schema will not migrate. Any applications relying on user-defined objects in `SYSTEM` will fail.

Action

Before migration, Oracle recommends that you recreate required user-defined objects in SYSTEM schemas, or use Oracle Data Pump schema mapping parameters such as `REMAP_SCHEMA=SYSTEM:xxx` where `xxx` is an existing user in ADB. In either case, any hardcoded references to the user-defined objects from `SYSTEM` must be updated. Consider dropping any user-defined objects that are no longer required.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.69 has\_user\_defined\_objects\_no\_quota

The Premigration Advisor Tool check `has_user_defined_objects_no_quota` indicates that there are are objects in the source database that belong to users without quota.

Result Criticality

Runtime

Has Fixup

No

Scope

`INSTANCE`

Target Cloud

This is a default check. It applies to the following:

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared
- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Description

This check indicates that there are objects in the source database that belong to users without relevant tablespace quota (or who have not been granted `UNLIMITED           TABLESPACE`). These objects will not be migrated to the target environment.

Effect

The objects belonging to these users may fail to transfer due to `ORA-01536` errors, leading to incomplete migration and potential data loss in the target database.

Action

\\

To complete transfer of all user data to the target environment. before you initiate the migration, assign an appropriate quota to all listed users (or grant those users `UNILIMITED TABLESPACE`).

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.70 has\_user\_defined\_pvfs

The Premigration Advisor Tool check `has_user_defined_pvfs` indicates that there are User-defined Password Verification Functions.

Result Criticality

Runtime

Has Fixup

No

Scope

`INSTANCE`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Description

This check indicates that user-defined Password Verification Functions (PVFs) exist.

Effect

User-defined objects in the `SYS` or `SYSTEM` schemas can't be imported into Oracle Autonomous Database (ADB). Attempts to import a `PROFILE` that uses user-defined Password Verification Functions will result in ORA-39460 errors.

Action

\\

Use a profile with a Password Verification Function provided by Oracle.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.71 has\_users\_with\_10g\_password\_version

The Premigration Advisor Tool check `has_users_with_10g_password_version` indicates that there are user accounts using `10G` password version.

Result Criticality

Review required.

Has Fixup

No

Scope

`SCHEMA`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared
- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Description

This check indicates that there are users on the source database that are using the 10G password version. This password version is desupported. After migration, users verified by the `10G` password version will not be able to log in.

Effect

After migration, users identified by the 10G password version fail to connect to the database, and receive ORA-1017 errors. During Oracle Data Pump migration ORA-39384 warnings are generated.

Action

To avoid Oracle Data Pump migration warnings, before migration, Oracle recommends that you change the passwords for any users listed as using the `10G` password version. Alternatively, you can modify these users' passwords after migration to avoid login failures. See Oracle Support Document ID 2289453.1 for more information.

**Related Topics**

- [ORA-39384: Warning: User \<USERNAME> Has Been Locked And The Password Expired During Import (Doc ID 2289453.1)](https://support.oracle.com/rs?type=doc&id=2289453.1)

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.72 has\_xmlschema\_objects

The Premigration Advisor Tool check `has_xmlschema_objects` indicates that there are XML Schema Objects in the source database.

Result Criticality

Action required

Has Fixup

No

Scope

`UNIVERSAL`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Description

This check indicates that XML Schema Objects are in the source database. These objects will not migrate.

Effect

XML Schemas are not supported in Oracle Autonomous Database.

Action

Modify your application to not use XML Schema Objects.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.73 has\_xmltype\_tables

The Premigration Advisor Tool check `has_xmltype_tables` indicates that there are `XMLType` tables in the source database.

Result Criticality

Action required

Has Fixup

No

Scope

`SCHEMA`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Description

This check indicates that there are XMLType Tables in the source database. These tables will not migrate unless the `STORAGE_TYPE` is `BINARY`.

Effect

Any applications relying on `XMLType` tables not stored as `BINARY` will fail.

Action

`XMLType` tables with `CLOB` or Object-Relational storage are not supported in Oracle Autonomous Database. Change the `XMLType` storage option to `BINARY`.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.74 modified\_db\_parameters\_dedicated

The Premigration Advisor Tool check `modified_db_parameters_dedicated` indicates that restricted initialization parameters are modified.

Result Criticality

Review suggested

Has Fixup

No

Scope

`INSTANCE`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ATPD Autonomous Transaction Processing Dedicated

Description

This check indicates that there are Oracle Database parameters on the source database instance whose modification is not allowed in Oracle Autonomous Database (Dedicated Infrastructure).

Effect

You are provided with a list of initialization parameters that have been modified in your database, but cannot be modified in Oracle Autonomous Database.

Action

To undersetand what parameters you are permitted to modify, refer to the Oracle Autonomous Database documentation.

#### 19.10.75 modified\_db\_parameters\_serverless

The Premigration Advisor Tool check `modified_db_parameters_serverless` indicates that restricted initialization parameters are modified.

Result Criticality

Review suggested

Has Fixup

No

Scope

`INSTANCE`

Target Cloud

This is a default check. It applies to the following:

- ADWS Autonomous Data Warehouse Shared
- ATPS Autonomous Transaction Processing Shared

Description

This check indicates that there are Oracle Database parameters on the source database instance whose modification is not allowed in Oracle Autonomous Database (Shared Infrastructure).

Effect

You are provided with a list of initialization parameters that have been modified in your database, but cannot be modified in Oracle Autonomous Database.

Action

To understand what parameters you are permitted to modify, refer to the Oracle Autonomous Database documentation.

#### 19.10.76 nls\_character\_set\_conversion

The Premigration Advisor Tool check `nls_character_set_conversion` indicates that there are character codes on the source database that are invalid in Oracle Autonomous Database.

Result Criticality

Runtime

Has Fixup

No

Scope

`SCHEMA`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared
- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Description

This check warns of issues caused by conversion of character data from the source to the target database character set, such as expansion of character values beyond column length or loss of invalid character codes.

Effect

During migration you can encounter ORA-1401 or loss of invalid character codes due to character set conversion from the source to the target database character set.

Action

Correct the issue as needed. Possible solutions include the following:

- Use Database Migration Assistant for Unicode (DMU) to scan the schemas that you want to migrate, and analyze all possible convertibility issues
- Create a new target instance using the same character set as the source instance. See the Oracle Cloud Infrastructure Documentation for information on choosing a character set when creating a database instance.

See the Oracle Cloud Infrastructure documentation for information on choosing a character set when creating a database instance.

Note:

Oracle recommends that you use the default database character set, `AL32UTF8`

**Related Topics**

- [The Database Migration Assistant for Unicode (DMU) Tool (Doc ID 1272374.1)](https://support.oracle.com/rs?type=doc&id=1272374.1)

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.77 nls\_national\_character\_set

The Premigration Advisor Tool check `nls_national_character_set` indicates that the `NCHAR` and `NVARCHAR2` lengths are different on the source and target databases.

Result Criticality

Review required

Has Fixup

No

Scope

`UNIVERSAL`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared
- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Description

This check indicates that the `NCHAR` and `NVARCHAR2` lengths are different on the source and target databases.

Check for issues caused by the conversion of character data from the source to the target national character set, such as expansion of character values beyond data type limits or loss of invalid character codes.

Effect

During migration you can encounter `ORA-01401` or loss of invalid character codes due to character set conversion from the source to the target national character set.

Action

If possible, provision the target database on Oracle Cloud Infrastructure with the same national character set as the source database, and enable extended data types in the target cloud database. See the Oracle Cloud Infrastructure documentation for information on choosing a national character set when creating a database instance.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.78 nls\_nchar\_ora\_910

The Premigration Advisor Tool check `nls_nchar_ora_910` indicates that the `NCHAR` and `NVARCHAR2` lengths are greater than the maximum length on the target databases.

Result Criticality

Action required

Has Fixup

No

Scope

`SCHEMA`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared
- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Description

This check indicates that the `NCHAR` and `NVARCHAR2` lengths are greater than the maximum permitted length on the target database.

Determine the maximum column length for the national database character set on the target database, and check for `NCHAR` and `NVARCHAR2` columns on the source database whose character length exceeds the limit on the target database.

Effect

During migration you can encounter `ORA-00910` errors due to the difference of the maximum character length of `NCHAR` and `NVARCHAR2` columns between the source and the target database.

Action

If possible, provision the target database on Oracle Cloud Infrastructure with the same national character set as the source database, and enable extended data types in the target cloud database. See the Oracle Cloud Infrastructure documentation for information on choosing a national character set when creating a database instance.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.79 options\_in\_use\_not\_available\_dedicated

The Premigration Advisor Tool check `options_in_use_not_available_dedicated` indicates that unavailable database options are present on the source database.

Result Criticality

Review suggested

Has Fixup

No

Scope

`INSTANCE`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ATPD Autonomous Transaction Processing Dedicated

Description

Generates a list of database options that are in use on the source, but not available in Oracle Autonomous Database (Dedicated Infrastructure).

Effect

If the database that you are migrating has applications or schemas in your database that use options that are not available on Oracle Autonomous Database, then it is possible that these applications will not work after migration.

Action

Verify that the applications or schemas in your source database depend on the options that are not supported on Oracle Autonomous Database (Dedicated Infrastructure), and plan accordingly.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.80 options\_in\_use\_not\_available\_serverless

The Premigration Advisor Tool check `options_in_use_not_available_serverless` indicates that unavailable database options are present on the source database.

Result Criticality

Review suggested

Has Fixup

No

Scope

`INSTANCE`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ATPD Autonomous Transaction Processing Dedicated

Description

Generates a list of database options that are in use on the source, but not available in Oracle Autonomous Database (Shared Infrastructure).

Effect

If the database that you are migrating has applications or schemas in your database that use options that are not available on Oracle Autonomous Database, then it is possible that these applications will not work after migration.

Action

Verify that the applications or schemas in your source database depend on the options that are not supported on Oracle Autonomous Database (Shared Infrastructure), and plan accordingly.

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.81 standard\_traditional\_audit\_adb

The Premigration Advisor Tool check `standard_traditional_audit_adb` indicates that Traditional Audit configurations are detected in the database.

Result Criticality

Review suggested

Has Fixup

No

Scope

`INSTANCE`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Description

Traditional audit, which was deprecated in Oracle Database 21c, is desupported starting with Oracle Database 23c. Traditional Audit configurations have been detected in this database.

Effect

Traditional Auditing is desupported in Oracle Database 23c. Oracle strongly recommends that you start using Unified Auditing.

Action

Delete the Traditional Auditing configurations. To assist you, use the instructions in Oracle Support Document ID 2909718.1.

**Related Topics**

- [Traditional to Unified Audit Syntax Converter - Generate Unified Audit Policies from Current Traditional Audit Configuration (Doc ID 2909718.1)](https://support.oracle.com/rs?type=doc&id=2909718.1)

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.82 standard\_traditional\_audit\_default

The Premigration Advisor Tool check `standard_traditional_audit_default` indicates that Traditional Audit configurations are detected in the database.

Result Criticality

Review suggested

Has Fixup

No

Scope

`INSTANCE`

Target Cloud

- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Description

Traditional audit, which was deprecated in Oracle Database 21c, is desupported starting with Oracle Database 23c. Traditional Audit configurations have been detected in this database.

Effect

Traditional Auditing is desupported in Oracle Database 23c. Oracle strongly recommends that you start using Unified Auditing.

Action

Delete the traditional auditing configurations using the instructions found in Oracle Support Document ID 2909718.1. Ensure that the following `init.ora` parameter values are set in `CDB$ROOT`, and restart the database:

```
AUDIT_TRAIL=none 
AUDIT_SYS_OPERATIONS=false
```

**Related Topics**

- [Traditional to Unified Audit Syntax Converter - Generate Unified Audit Policies from Current Traditional Audit Configuration (Doc ID 2909718.1)](https://support.oracle.com/rs?type=doc&id=2909718.1)

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.83 timezone\_table\_compatibility\_higher\_dedicated

The Premigration Advisor Tool check `timezone_table_compatibility_higher_dedicated` indicates that the timezone setting is a more recent version on the source than on the target database.

Result Criticality

Runtime

Has Fixup

No

Scope

`UNIVERSAL`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ATPD Autonomous Transaction Processing Dedicated

Description

The source database `TZ_VERSION` cannot be higher than the target `TZ_VERSION`.

Effect

Migration is not possible until the target `TZ_VERSION` is the same or higher than the source database `TZ_VERSION`.

Action

Use the "Enable time-zone update" option of the Schedule maintenance dialog for the Quarterly Maintenance Update to update the time zone version on your target instance.

#### 19.10.84 timezone\_table\_compatibility\_higher\_default

The Premigration Advisor Tool check `timezone_table_compatibility_higher_default` indicates that the timezone setting is a more recent version on the source than on the target database.

Result Criticality

Runtime

Has Fixup

No

Scope

`UNIVERSAL`

Target Cloud

- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Description

The source database `TZ_VERSION` cannot be higher than the target `TZ_VERSION`.

Effect

Migration is not possible until the target `TZ_VERSION` is the same or higher than the source database `TZ_VERSION`.

Action

Ensure the target instance has a time zone version equal or greater than the source instance by downloading and installing an appropriate patch from Oracle Support Document ID 412160.1

**Related Topics**

- [Primary Note DST FAQ: Updated DST Transitions and New Time Zones in Oracle RDBMS and OJVM Time Zone File Patches (Doc ID 412160.1)](https://support.oracle.com/rs?type=doc&id=412160.1)

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.85 timezone\_table\_compatibility\_higher\_serverless

The Premigration Advisor Tool check `timezone_table_compatibility_higher_serverless` indicates that the timezone setting is a more recent version on the source than on the target database.

Result Criticality

Runtime

Has Fixup

No

Scope

`UNIVERSAL`

Target Cloud

- ADWS Autonomous Data Warehouse Shared
- ATPS Autonomous Transaction Processing Shared

Description

The source database `TZ_VERSION` cannot be higher than the target `TZ_VERSION`.

Effect

Migration is not possible until the target `TZ_VERSION` is the same or higher than the source database `TZ_VERSION`.

Action

Update the Time Zone File Version. Refer to "Manage Time Zone File Version on Autonomous Database"

#### 19.10.86 unified\_and\_standard\_traditional\_audit\_adb

The Premigration Advisor Tool check `unified_and_standard_traditional_audit_adb` indicates that Traditional Audit configurations are detected in the database.

Result Criticality

Runtime

Has Fixup

No

Scope

`INSTANCE`

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared

Description

Traditional audit, which was deprecated in Oracle Database 21c, is desupported starting with Oracle Database 23c. Traditional Audit configurations have been detected in this database, which is configured to use only Unified Auditing.

Effect

Performance can degrade unless the traditional audit configurations in the database are deleted.

Action

Oracle strongly recommends that you delete the Traditional Auditing configurations

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.87 unified\_and\_standard\_traditional\_audit\_default

The Premigration Advisor Tool check `unified_and_standard_traditional_audit_default` indicates that Traditional Audit configurations are detected in the database.

Result Criticality

Runtime

Has Fixup

No

Scope

`INSTANCE`

Target Cloud

- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Description

Traditional audit, which was deprecated in Oracle Database 21c, is desupported starting with Oracle Database 23c. Traditional Audit configurations have been detected in this database, which is configured to use only Unified Auditing..

Effect

Performance can degrade unless the traditional audit configurations in the database are deleted.

Action

Delete the traditional auditing configurations using the instructions found in Oracle Support Document ID 2909718.1. Ensure that the following `init.ora` parameter values are set in `CDB$ROOT`, and restart the database:

```
AUDIT_TRAIL=none 
AUDIT_SYS_OPERATIONS=false
```

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

#### 19.10.88 xdb\_resource\_view\_has\_entries Check

The Premigration Advisor Tool check `xdb_resource_view_has_entries       Check` indicates that there is an XDB Repository that is not supported in Oracle Autonomous Database. Entries in `RESOURCE_VIEW` will not migrate.

Result Criticality

Review required

Has Fixup

No

Target Cloud

- ADWD Autonomous Data Warehouse Dedicated
- ADWS Autonomous Data Warehouse Shared
- ATPD Autonomous Transaction Processing Dedicated
- ATPS Autonomous Transaction Processing Shared
- Default (an Oracle Database instance that is not Oracle Autonomous Database)

Description

This check applies to source schema for Oracle Data Pump and Oracle GoldenGate migrations, and Oracle Data Pump database links. When there is an Oracle XML DB repository (XDB Repository) that is not supported in Oracle Autonomous Database (ADB), entries in `RESOURCE_VIEW` will not migrate.

Effect

Applications relying on entries in the XDB Repository `RESOURCE_VIEW` may not function as expected.

Action

Applications must be updated to remove their dependencies on the XDB Repository. For more information on determining if XDB is being used in your database see Oracle Support Document ID 733667.1

**Related Topics**

- [How to Determine if XDB is Being Used in the Database? (Doc ID 733667.1)](https://support.oracle.com/rs?type=doc&id=733667.1)

**Parent topic:** List of Checks Performed By the Premigration Advisor Tool

### 19.11 Best Practices for Using the Premigration Advisor Tool

These Cloud Premigration Advisor Tool (CPAT) tips can help you use CPAT more effectively.

- Generate Properties File on the Target Database Instance  
	Oracle recommends that you generate a Premigration Advisor Tool (CPAT) properties file on the target database instance.
- Focus the CPAT Analysis  
	Oracle recommends that you focus the Premigration Advisor Tool (CPAT) analysis to restrict what schemas CPAT will examine.
- Reduce the Amount of Data in Reports  
	Some Cloud Premigration Advisor tool checks can return thousands of objects with the same concern. Here's how you can reduce the report size.
- Generate the JSON Report and Save Logs  
	Even if you only plan to use the text report, Oracle suggests you also generate a JSON output file with the Cloud Premigration Advisor tool (CPAT), and save the log files for diagnosis.
- Use Output Prefixes to Record Different Migration Scenarios  
	To keep track of reports for different migration options, use the `--outfileprefix` and `--outdir` properties on the CPAT command line.

**Parent topic:** Cloud Premigration Advisor Tool

#### 19.11.1 Generate Properties File on the Target Database Instance

Oracle recommends that you generate a Premigration Advisor Tool (CPAT) properties file on the target database instance.

To perform the most complete and targeted analysis of the source database instance, certain properties of the target database instance are required. For this reason, you should generate your CPAT properties file on the database instance that you want to migrate. To perform this function, the `--gettargetprops` property is intended to be used with the other connection-related properties.

In the following example, the CPAT script is run by the user `ADMIN` on the target database instance:

```
./premigration.sh --gettargetprops -username ADMIN --connectstring 'jdbc:oracle:thin:@service-name?TNS_ADMIN=path-to-wallet'
```

The command generates a properties file, `premigration_advisor_analysis.properties`, which you can use to analyze a source instance.

If necessary, you can copy the properties file generated on the target to the host where the source database analysis will be performed, and provide the file to CPAT using the `--analysisprops` property.

For example:

```
./premigration.sh --connectstring jdbc:oracle:oci:@ --targetcloud ATPD --sysdba --analysisprops premigration_advisor_analysis.properties
```

If you know that you (or Oracle Zero Downtime Migration (ZDM) or Oracle Database Migration Service (DMS) will be mapping (or precreating) all needed tablespaces, then append the property `MigrationMethodProp.ALL_METHODS.TABLESPACE_MAPPING=ALL` to the properties file you provide to CPAT. This property setting causes CPAT to PASS most (if not all) of its tablespace-related checks. However, if you choose this option, then be aware that there can still be migration issues related to quotas with tablespace mapping.

**Parent topic:** Best Practices for Using the Premigration Advisor Tool

#### 19.11.2 Focus the CPAT Analysis

Oracle recommends that you focus the Premigration Advisor Tool (CPAT) analysis to restrict what schemas CPAT will examine.

Consider using the `--schema` switch property to restrict what schemas you want CPAT to examine during its analysis. When you start CPAT using `--schemas list`, where `list` is a space-delimited list of schemas, CPAT performs checks only on those schemas. Without the `--schemas` switch, CPAT will analyze all schemas in the source instance (excluding Oracle-maintained schemas), which can result in problems being found in schemas that you do not intend to migrate. Using the `--schemas ` property to restrict scope can be particularly useful if the source instance is hosting multiple applications, each of which could potentially be migrated to different Oracle Autonomous Database instances.

In the following example, the CPAT script is run by the user `ADMIN` on the target database instance to perform analysis on the schemas `schema1` and `schema2`:

```
./premigration.sh -username SYSTEM --connectstring 'jdbc:oracle:thin:@service-name?TNS_ADMIN=path-to-wallet' --schemas schema1 schema2
```

The `--schemas` switch property provides a space-separated list of schemas (schema1 and schema2) to CPAT, so that the checks it performs are restricted only to those two schemas.

**Parent topic:** Best Practices for Using the Premigration Advisor Tool

#### 19.11.3 Reduce the Amount of Data in Reports

Some Cloud Premigration Advisor tool checks can return thousands of objects with the same concern. Here's how you can reduce the report size.

Depending on the checks you run, some CPAT checks can return results for the same issue in multiple objects in the text report. To reduce the number of results, you can use the `--maxtextdatarows n` function, where n is an integer that specifies the number of rows that you want to view.

The `--maxrelevantobjects n` property performs the same function for reports, but limiting the size of JSON reports is typically not necessary.

In the following example, the CPAT script is run by the user `SYSTEM` on the target database instance, with the output set to return a maximum of 10 rows of text file data:

```
./premigration.sh --username SYSTEM --connectstring 'jdbc:oracle:thin:@service-name?TNS_ADMIN=path-to-wallet --maxtextdatarows 10"
```

**Parent topic:** Best Practices for Using the Premigration Advisor Tool

#### 19.11.4 Generate the JSON Report and Save Logs

Even if you only plan to use the text report, Oracle suggests you also generate a JSON output file with the Cloud Premigration Advisor tool (CPAT), and save the log files for diagnosis.

Oracle recommends generating the JSON report as well as the text report, and always save your log report files. Why? If you encounter an issue while using CPAT, and need to contact Oracle Support, then you can provide all possible information to assist Oracle Support with resolving your issue. You can assist Oracle Support by being prepared to submit both the text and JSON reports, as well as the `.log` reports generated by CPAT. The `--reportformat` property accepts one or more space-delimited report formats. The permitted values for the `--reportformat` switch are `json` and `text`.

For example:

```
./premigration.sh -username SYSTEM --connectstring 'jdbc:oracle:thin:@service-name --reportformat json text
```

**Parent topic:** Best Practices for Using the Premigration Advisor Tool

#### 19.11.5 Use Output Prefixes to Record Different Migration Scenarios

To keep track of reports for different migration options, use the `--outfileprefix` and `--outdir` properties on the CPAT command line.

To generate reports for different Cloud migration options, you can use the Cloud Premigration Advisor Tool (CPAT) with the `--outfileprefix`, so that you place a prefix on reports and log files that can organize the report options that you have generated. You can also use the `--outdir` property to organize reports for different instances, or to organize reports for different scenarios.

Note:

The `--outdir` property accepts either an absolute or a relative folder path. Using this property specifies a particular location where CPAT creates the log files, report files, and any properties files that you generate. If `--outdir` is omitted from the command line, then the log file and other generated files are created in the user's current folder, which can lead to files being overwritten when multiple analyses are performed.

For example:

```
./premigration.sh --outfileprefix ATPS_RUN_01 --outdir /path/CPAT_output --reportformat TEXT JSON ...
```

**Parent topic:** Best Practices for Using the Premigration Advisor Tool