---
title: "Administrator’s Guide"
book: "Multitenant Administrator's Guide"
doc_id: F31734-10
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/multi/dbca-overview.html
tags:
  - oracle
  - 21c
  - multitenant-administrators-guide
---

**Parent topic:** [Database Configuration Assistant Command Reference for Silent Mode](dbca-reference.md)

### DBCA Command-Line Syntax Overview

This section provides an overview of the command-line syntax of DBCA in silent mode.

DBCA silent mode has the following command syntax:

```
dbca  [-silent] [command [options]] [-h|-help]
```

Note:

On Windows, you must run DBCA as an Administrator if user access control (UAC) is enabled.

The following table describes the DBCA silent mode command syntax.

Table 18-1 DBCA Silent Mode Command Syntax Description

| Option | Description |
| --- | --- |
| `-silent` | Specify `-silent` to run DBCA in silent mode.  In silent mode, DBCA uses values that you specify as command-line options to create or modify a database. |
| `command options` | Specify a DBCA command and valid options for the command. |
| `-h \| -help` | Displays help for DBCA.  You can display help for a specific command by entering the following:  ``` dbca command -help ```  For example, to display the help for the `-createDatabase` command, enter the following:  ``` dbca -createDatabase -help ``` |

The following example illustrates how to create a database with the silent mode of DBCA:

```
dbca -silent -createDatabase -templateName General_Purpose.dbc
                             -gdbname oradb.example.com 
                             -sid oradb
                             -characterSet AL32UTF8 
                             -memoryPercentage 30 
                             -emConfiguration DBEXPRESS

Enter SYSTEM user password:
password
Enter SYS user password:
password
Copying database files
1% complete
3% complete
...
```

To ensure completely silent operation, you can redirect stdout to a file. If you do this, however, you may have to supply passwords for the administrative users in command-line arguments or the response file.

Note:

If you use Oracle wallet as a secure external password store for storing passwords for the administrative users, then you do not have to supply passwords for these users in the command-line arguments or in the response file. See " Database User Authentication in DBCA Commands Using Oracle Wallet " for more information.

To view brief help for DBCA command-line arguments, enter the following command:

```
dbca -help
```

For more detailed argument information, including defaults, view the response file template found on your distribution media. See the Oracle Database installation guide for your platform to get information about the name and location of the response file template.

See Also:

" [DBCA Silent Mode Commands](dbca-command.md) "

**Parent topic:** DBCA Overview

### About DBCA Templates

You can use DBCA to create a database from a template supplied by Oracle or from a template that you create.

A DBCA template is an XML file that contains information required to create a database. Oracle ships templates for the following two workload types:

- General purpose OR online transaction processing
- Data warehouse

Select the template suited to the type of workload your database will support. If you are not sure which to choose, then use the "General purpose OR online transaction processing" template. You can also create custom templates to meet your specific workload requirements.

Note:

The General Purpose or online transaction processing template and the data Warehouse template create a database with the `COMPATIBLE` initialization parameter set to 12.1.0.2.0.

**Parent topic:** DBCA Overview

### Database User Authentication in DBCA Commands Using Oracle Wallet

You can use Oracle wallet as a secure external password store for authenticating database users in DBCA silent mode commands.

Oracle wallet is a secure software container external to Oracle Database, which can be used to store authentication credentials of Oracle Database users. You can use the following DBCA silent mode command parameters to use Oracle wallet for authenticating database users:

- `useWalletForDBCredentials`: Specify `true` to use Oracle wallet for database user authentication, else specify `false`. Default is `false`.
	If `true` is specified, then provide the following additional parameters:
	- `dbCredentialsWalletLocation`: Directory in which the Oracle wallet files are stored.
		- (Optional) `dbCredentialsWalletPassword`: Password for the Oracle wallet account user. If the Oracle wallet is auto-login enabled, then you need not specify this password.

You can store the following keys and associated passwords in the Oracle wallet that can be used by DBCA in silent mode for authenticating users:

- `oracle.dbsecurity.sysPassword`: `SYS` user password
- `oracle.dbsecurity.systemPassword`: `SYSTEM` user password
- `oracle.dbsecurity.pdbAdminPassword`: Pluggable database (PDB) administrator password
- `oracle.dbsecurity.dbsnmpPassword`: `DBSNMP` user password
- `oracle.dbsecurity.asmsnmpPassword`: `ASMSNMP` user password
- `oracle.dbsecurity.lbacsysPassword`: `LBACSYS` user password
- `oracle.dbsecurity.sysdbaUserPassword`: `SYSDBA` role user password for the database that you are creating or configuring
- `oracle.dbsecurity.oracleHomeUserPassword`: Oracle home user password
- `oracle.dbsecurity.dvUserPassword`: Oracle Data Vault user password
- `oracle.dbsecurity.dvAccountManagerPassword`: Oracle Data Vault account manager password
- `oracle.dbsecurity.emPassword`: Enterprise Manager administrator password
- `oracle.dbsecurity.asmPassword`: `ASM` user password
- `oracle.dbsecurity.asmsysPassword`: `ASMSYS` user password
- `oracle.dbsecurity.walletPassword`: Oracle wallet account user password for authenticating with a directory service
- `oracle.dbsecurity.userDNPassword`: Directory service user password
- `oracle.dbsecurity.srcDBsysdbaUserPassword`: `SYSDBA` role user password for the database that you are using as a source to perform certain operations, such as duplicating a database
- `oracle.dbsecurity.dbLinkUserPassword`: Database link user password

Note:

If you are using Oracle Unified Directory (OUD), then the OUD account passwords should be stored in the wallet using the following keys:

- `oracle.dbsecurity.walletPassword`
- `oracle.dbsecurity.userDNPassword`

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=DBSEG-GUID-803496D2-19C7-4F02-94EC-C13EDD8FB17B) for information about configuring Oracle wallet as a secure external password store using the `mkstore` command-line utility

**Parent topic:** DBCA Overview