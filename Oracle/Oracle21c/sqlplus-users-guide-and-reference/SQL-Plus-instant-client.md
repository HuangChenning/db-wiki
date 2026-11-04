---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/SQL-Plus-instant-client.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

SQL\*Plus Instant Client is a standalone product with all the functionality of SQL\*Plus command-line. It connects to existing remote Oracle databases, but does not include its own database. It is easy to install and uses significantly less disk space than the full Oracle Database Client installation required to use SQL\*Plus command-line.

SQL\*Plus Instant Client is available on platforms that support the OCI Instant Client. See [About OCI Instant Client](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=LNOCI-GUID-6895DB45-97AA-4738-9959-BD677D610186) for more information on the OCI Instant Client.

To install SQL\*Plus Instant Client, you need two packages:

- SQL\*Plus Instant Client package.
- Either the Basic OCI Instant Client package, or the lightweight OCI Instant Client package.

### D.1 About Choosing the SQL\*Plus Instant Client to Install

SQL\*Plus Instant Client can be installed in two ways:

- Download the packages from the Oracle Technology Network (OTN).
- Copy the same files that are in the packages from an Oracle Database 21c Client Administrator installation.

Both the SQL\*Plus and OCI packages must be from the same Oracle Database version.

#### D.1.1 Basic Instant Client

SQL\*Plus Instant Client using the Basic OCI package works with any NLS\_LANG setting supported by the Oracle Database. It supports all character sets and language settings available in the Oracle Database.

#### D.1.2 Lightweight Instant Client

SQL\*Plus Instant Client using the lightweight OCI package displays error messages in English only and supports only specific character sets. It is significantly smaller than SQL\*Plus Instant Client using the Basic OCI package.

Valid values for NLS\_LANG parameters with the lightweight Instant Client are:

- language can be any valid language supported by the Oracle Database, however, error messages are only reported in English.
- territory can be any valid territory supported by the Oracle Database.
- charset is one of the following character sets:
	- US7ASCII
		- WE8DEC
		- WE8MSWIN1252
		- WE8ISO8859P1
		- UTF8
		- AL16UTF16
		- AL32UTF8

For example:

```
NLS_LANG=AMERICAN_AMERICA.UTF8
```

See [Setting Up a Globalization Support Environment](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=NLSPG-GUID-D5C74C82-8622-46F4-8760-0F8ABA28A816), and [NLS\_LANG Environment Variable](SQL-Plus-globalization-support.md) for more information about NLS settings.

##### D.1.2.1 Lightweight SQL\*Plus Instant Client Error with Unsupported Character Set

Attempting to start SQL\*Plus Instant Client with an unsupported character set will fail with the following error:

```
Error 5 initializing SQL*Plus
NLS initialization error
```

### D.2 List of Files Required for SQL\*Plus Instant Client

This section lists the required files for installation of SQL\*Plus Instant Client for both the basic package and the lightweight package.

The files from only one of the OCI packages (either basic or lightweight) are required. Other files that get installed, which are not listed in this section, can be ignored or can be removed to save disk space.

Table D-1 Instant Client Files in the SQL\*Plus Package

| Linux and UNIX | Windows | Description |
| --- | --- | --- |
| sqlplus | sqlplus.exe | SQL\*Plus executable |
| libsqlplus.so | not applicable | SQL\*Plus library |
| libsqlplusic.so | orasqlplusic21.dll | SQL\*Plus data shared library |

Table D-2 Instant Client Files in the Basic OCI Package

| Linux and UNIX | Windows | Description |
| --- | --- | --- |
| libclntsh.so.21.1 | oci.dll | Client code library |
| libclntshcore.so | not applicable | OCI Instant Client data shared Library |
| libociei.so | oraociei21.dll | OCI Instant Client data shared library |
| libnnz21.so | orannzsbb21.dll | Security library |
| libons.so | oraons.dll | ONS library |

Table D-3 Instant Client Files in the Lightweight OCI Package

| Linux and UNIX | Windows | Description |
| --- | --- | --- |
| libclntsh.so.21.1 | oci.dll | Client code library |
| libociicus.so | oraociicus21.dll | OCI Instant Client data shared library (English only) |
| libnnz21.so | orannzsbb21.dll | Security library |

### D.3 Installing SQL\*Plus Instant Client by Downloading Installation Files from OTN

This section describes how to install SQL\*Plus Instant Client from OTN RPM packages for Linux and from OTN downloadable zip files for UNIX and Windows.

The SQL\*Plus Instant Client package should never be installed on an `ORACLE_HOME`.

1. Download the RPM packages containing the SQL\*Plus Instant Client package and the OCI package from the OTN Instant Client page. Both packages must be of the same version.
	See Also:
	[Oracle Instant Client Page](https://www.oracle.com/database/technologies/instant-client.html)
2. Use either the `rpm -i` command for the initial installation of the RPM packages, or the `rpm -u` command to upgrade to a newer version of the packages.
3. Configure SQL\*Plus Instant Client.
	See Also:
	Configuring SQL\*Plus Instant Client

1. Download the zip files containing the SQL\*Plus Instant Client package and the OCI package from the OTN Instant Client page. Both packages must be of the same version.
	See Also:
	[Oracle Instant Client Page](https://www.oracle.com/database/technologies/instant-client.html)
2. Create a new directory, for example, `/home/instantclient20_2` on UNIX or `c:\instantclient20_2` on Windows.
3. Unzip the two packages into the new directory.
4. Configure SQL\*Plus Instant Client.
	See Also:
	Configuring SQL\*Plus Instant Client

### D.4 Installing SQL\*Plus Instant Client from the 21c Client Release Media

This section describes how to install SQL\*Plus Instant Client on Unix, Linux, and Windows.

1. Run the installer on the Oracle Database 21c Client Release media and choose the Administrator option.
2. Create a new directory, for example, `/home/instantclient_21_1` on UNIX and Linux, or `c:\instantclient_21_1` on Windows.
3. Copy the SQL\*Plus Instant Client and the OCI Instant Client files to the new directory. All files must be copied from the same `ORACLE_HOME`.
	See Also:
	List of Files Required for SQL\*Plus Instant Client
4. Configure SQL\*Plus Instant Client.
	See Also:
	Configuring SQL\*Plus Instant Client

### D.5 Configuring SQL\*Plus Instant Client

You must use the SQL\*Plus Instant Client executable only with the matching version of the OCI Instant Client.

You must download the RPMs from OTN into Oracle specific sub-directories in the `/usr` file system. The sub-directory structure enables multiple versions of Instant Client to be available.

1. Add the name of the directory containing the Instant Client libraries to `LD_LIBRARY_PATH`. Remove any other Oracle directories.
	For example, use the following command to set `LD_LIBRARY_PATH` on Solaris in the Bourne or Korn shells:
	```
	LD_LIBRARY_PATH=/usr/lib/oracle/21.1/client/lib:${LD_LIBRARY_PATH}
	export LD_LIBRARY_PATH
	```
2. Make sure that the sqlplus executable installed from the RPM is the first entry in your `PATH`. To test, enter the which sqlplus command, which should return /usr/bin/sqlplus. If you do not see this output, then remove any other Oracle directories from `PATH`, or put /usr/bin before any other SQL\*Plus executables present in `PATH`, or use an absolute or relative path to start SQL\*Plus.
	For example, use the following command to set `PATH` in the bash shell:
	```
	PATH=/usr/bin:${PATH}
	export PATH
	```
	If you install multiple versions of SQL\*Plus, then you may need to change the symbolic link /usr/bin/sqlplus to the version of SQL\*Plus matching the libraries in `LD_LIBRARY_PATH`. For release 21.1, /usr/bin/sqlplus is a symbolic link to the SQL\*Plus binary at /usr/lib/oracle/21.1/client/bin/sqlplus.
3. Set Oracle globalization variables required for your locale. A default locale is assumed if no variables are set. See [Locale Data](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=NLSPG-GUID-A9E30C27-FD47-4552-B670-F41A95B11405) for more information.
	For example:
	```
	NLS_LANG=AMERICAN_AMERICA.UTF8
	export NLS_LANG
	```

1. Add the name of the directory containing the Instant Client files to the appropriate shared library path `LD_LIBRARY_PATH`, `LIBPATH` or `SHLIB_PATH`. Remove any other Oracle directories.
	For example, use the following command on Solaris in the Bourne or Korn shells:
	```
	LD_LIBRARY_PATH=/home/instantclient_21_1:${LD_LIBRARY_PATH}
	export LD_LIBRARY_PATH
	```
2. Add the directory containing the Instant Client files to the `PATH` environment variable. If it is not set, then an absolute or relative path must be used to start SQL\*Plus. Remove any other Oracle directories from `PATH`. For example:
	```
	PATH=/home/instantclient_21_1:${PATH}
	export PATH
	```
3. Set Oracle globalization variables required for your locale. A default locale will be assumed if no variables are set. See [Locale Data](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=NLSPG-GUID-A9E30C27-FD47-4552-B670-F41A95B11405) for more information. For example:
	```
	NLS_LANG=AMERICAN_AMERICA.UTF8
	export NLS_LANG
	```

You can configure the environment for a session using the `SET` commands in a Windows command prompt or globally by setting the Environment Variables in System Properties. For example, to set environment variables in Windows 2000 using System Properties, open System from the Control Panel, click the Advanced tab and then click Environment Variables.

Now, perform the following steps:

1. Add the directory containing the Instant Client files to the `PATH` system environment variable. Remove any other Oracle directories from `PATH`. For example, add c:\\instantclient20\_2 to the beginning of `PATH`.
2. Set Oracle globalization variables required for your locale. A default locale will be assumed if no variables are set. See [Locale Data](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=NLSPG-GUID-A9E30C27-FD47-4552-B670-F41A95B11405) for more information. For example, to set `NLS_LANG` for a Japanese environment, create a user environment variable `NLS_LANG` set to `JAPANESE_JAPAN.JA16EUC`.
	If you have installed the lightweight Instant Client, see Lightweight Instant Client for information about supported `NLS_LANG` settings.

### D.6 About Connecting to a Database with SQL\*Plus Instant Client

SQL\*Plus Instant Client is always remote from any database server. To connect to a database, you must specify the database using an Oracle Net connection identifier.

An example using an Easy Connection identifier for connecting to the HR schema in the MYDB database, running on mymachine, is:

```
sqlplus hr/your_password@\"//mymachine.mydomain:port/MYDB\"
```

Alternatively, you can use a Net Service Name:

```
sqlplus hr/your_password@MYDB
```

Net Service Names can be stored in a number of places, including LDAP. The use of LDAP is recommended to take advantage of the new features of Oracle Database 21c. See [Local Naming Parameters in the tnsnames.ora File](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=NETRF-GUID-A3F9D023-9CC4-445D-8921-6E40BD900EAD) for more information.

If you want to use Net Service Names configured in a local Oracle Net `tnsnames.ora` file, then set the environment variable `TNS_ADMIN` to the directory containing the `tnsnames.ora` file. For example, on UNIX, if your `tnsnames.ora` file is in `/home/user1` and it defines the Net Service Name `MYDB2`, then use the following commands:

```
TNS_ADMIN=/home/user1
export TNS_ADMIN
sqlplus hr@MYDB2
```

If `TNS_ADMIN` is not set, then an operating system dependent set of directories is examined to find `tnsnames.ora`. This search path includes looking in the directory specified by the `ORACLE_HOME` environment variable for `network/admin/tnsnames.ora`. This is the only reason to set the `ORACLE_HOME` environment variable for SQL\*Plus Instant Client. If `ORACLE_HOME` is set when running Instant Client applications, then it must be set to a directory that exists.

This example assumes the `ORACLE_HOME` environment variable is set, and the `$ORACLE_HOME/network/admin/tnsnames.ora` or `ORACLE_HOME\network\admin\tnsnames.ora` file defines the Net Service Name `MYDB3`:

```
sqlplus hr@MYDB3
```

You can set the `TWO_TASK` (on UNIX) or `LOCAL` (on Windows) environment variable to a connection identifier. This removes the need to explicitly enter the connection identifier whenever a connection is made in SQL\*Plus or SQL\*Plus Instant Client. This UNIX example connects to the database known as MYDB4:

```
TNS_ADMIN=/home/user1
export TNS_ADMIN
TWO_TASK=MYDB4
export TWO_TASK
sqlplus hr
```

On Windows, you can set the `TNS_ADMIN` and `LOCAL` variables in the System Properties.

Note:

Configuring SQL\*Plus Instant Client

### D.7 AS SYSDBA or AS SYSOPER Connections with SQL\*Plus Instant Client

To connect `AS SYSDBA` or `AS SYSOPER` to perform DBA tasks, you must set up an Oracle password file on the database server using the orapwd utility.

Once you configure the utility, your SQL\*Plus Instant Client connection string looks like the following:

```
sqlplus sys@MYDB AS SYSDBA
```

See [Using Password File Authentication](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=ADMIN-GUID-662ACF2E-546A-4EF0-89EA-35D4633A0996) for information on Oracle password files.

### D.8 About Uninstalling Instant Client

The SQL\*Plus Instant Client package can be removed separately from the OCI Instant Client. After uninstalling the SQL\*Plus Instant Client package, the remaining OCI Instant Client libraries enable custom written OCI programs or third party database utilities to connect to a database.

#### D.8.1 Uninstalling SQL\*Plus Instant Client

1. For installations on Linux from RPM packages, use rpm -e only on the SQL\*Plus Instant Client package
	or
	For installations on UNIX and Windows, and installations on Linux from the Client Release media, manually remove the following SQL\*Plus specific files:
	Table D-4 Instant Client Files in the SQL\*Plus Package
	| UNIX | Windows | Description |
	| --- | --- | --- |
	| sqlplus | sqlplus.exe | SQL\*Plus executable |
	| libsqlplus.so | not applicable | SQL\*Plus library |
	| libsqlplusic.so | orasqlplusic20.dll | SQL\*Plus data shared library |
2. Reset environment variables and remove tnsnames.ora if necessary.

#### D.8.2 Uninstalling the Complete Instant Client

1. For installations on Linux from RPM packages, use rpm -qa to find the SQL\*Plus Instant Client and Basic OCI package names and run rpm -e to remove them
	or
	For installations on UNIX and Windows, and installations on Linux from the Client Release media, manually delete the directory containing the SQL\*Plus executable and Oracle libraries.
	See Installing SQL\*Plus Instant Client from the 21c Client Release Media for a list of the files you copied to the directory.
2. Reset environment variables such as PATH, SQLPATH, LD\_LIBRARY\_PATH and TNS\_ADMIN.
3. Remove tnsnames.ora if necessary.