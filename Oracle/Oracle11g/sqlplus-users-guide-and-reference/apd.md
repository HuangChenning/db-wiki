---
title: "SQL*Plus Instant Client"
book: "SQL*Plus User's Guide and Reference"
doc_id: E16604-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e16604/apd.htm
tags:
  - oracle
  - 11g
  - sqlplus-users-guide-and-reference
---

## D SQL\*Plus Instant Client

SQL\*Plus Instant Client is a standalone product with all the functionality of SQL\*Plus command-line. It connects to existing remote Oracle databases, but does not include its own database. It is easy to install and uses significantly less disk space than the full Oracle Database Client installation required to use SQL\*Plus command-line.

SQL\*Plus Instant Client is available on platforms that support the OCI Instant Client. See the [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/toc.htm) for more information on the OCI Instant Client.

To install SQL\*Plus Instant Client, you need two packages:

- SQL\*Plus Instant Client package.
- Either the Basic OCI Instant Client package, or the lightweight OCI Instant Client package.

## Choosing the SQL\*Plus Instant Client to Install

SQL\*Plus Instant Client can be installed in two ways:

- Download the packages from the Oracle Technology Network (OTN).
- Copy the same files that are in the packages from an Oracle Database 11g Client Administrator installation.

Both the SQL\*Plus and OCI packages must be from the same Oracle Database version, for example, 11.1.0.6.

### Basic Instant Client

SQL\*Plus Instant Client using the Basic OCI package works with any NLS\_LANG setting supported by the Oracle Database. It supports all character sets and language settings available in the Oracle Database.

### Lightweight Instant Client

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

See the [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm), and [NLS\_LANG Environment Variable](ch_eleven.md) for more information about NLS settings.

#### Lightweight SQL\*Plus Instant Client Error with Unsupported Character Set

Attempting to start SQL\*Plus Instant Client with an unsupported character set will fail with the following error:

```
Error 5 initializing SQL*Plus
NLS initialization error
```

## Installing SQL\*Plus Instant Client by Downloading from OTN

The OTN downloads for Linux are RPM packages. The OTN downloads for UNIX and Windows are zip files.

The SQL\*Plus Instant Client package should never be installed on an ORACLE\_HOME.

### Installing SQL\*Plus Instant Client from Linux RPM Packages

1. Download the RPM packages containing the SQL\*Plus Instant Client package, and the OCI package from the OTN Instant Client page at [`http://www.oracle.com/technology/tech/oci/instantclient/instantclient.html`](http://www.oracle.com/technology/tech/oci/instantclient/instantclient.html). Both packages must be from the same version such as 11.1.0.6.
2. Use rpm -i for the initial install of the RPM packages, or rpm -u to upgrade to a newer version of the packages.
3. Configure SQL\*Plus Instant Client. See Configuring SQL\*Plus Instant Client.

### Installing SQL\*Plus Instant Client from the UNIX or Windows Zip Files

1. Download the zip files containing the SQL\*Plus Instant Client package, and the OCI package from the OTN Instant Client page at [`http://www.oracle.com/technology/tech/oci/instantclient/instantclient.html`](http://www.oracle.com/technology/tech/oci/instantclient/instantclient.html). Both packages must be from the same version such as 11.1.0.6.
2. Create a new directory, for example, /home/instantclient11\_2 on UNIX or c:\\instantclient11\_2 on Windows.
3. Unzip the two packages into the new directory.
4. Configure SQL\*Plus Instant Client. See Configuring SQL\*Plus Instant Client.

### List of Files Required for SQL\*Plus Instant Client

Tables E-1, E-2 and E-3 list the required files from each of the SQL\*Plus and OCI packages. The files from only one of the OCI packages are required. Other files installed that are not listed here can be ignored, or can be removed to save disk space.

Table D-1 Instant Client Files in the SQL\*Plus Package

| Linux and UNIX | Windows | Description |
| --- | --- | --- |
| sqlplus | sqlplus.exe | SQL\*Plus executable |
| libsqlplus.so | not applicable | SQL\*Plus library |
| libsqlplusic.so | orasqlplusic11.dll | SQL\*Plus data shared library |

Table D-2 Instant Client Files in the Basic OCI Package

| Linux and UNIX | Windows | Description |
| --- | --- | --- |
| libclntsh.so.11.1 | oci.dll | Client code library |
| libociei.so | oraociei11.dll | OCI Instant Client data shared library |
| libnnz11.so | orannzsbb11.dll | Security library |

Table D-3 Instant Client Files in the Lightweight OCI Package

| Linux and UNIX | Windows | Description |
| --- | --- | --- |
| libclntsh.so.11.1 | oci.dll | Client code library |
| libociicus.so | oraociicus11.dll | OCI Instant Client data shared library (English only) |
| libnnz11.so | orannzsbb11.dll | Security library |

## Installing SQL\*Plus Instant Client from the 11g Client Release Media

1. Run the installer on the Oracle Database 11g Client Release media and choose the Administrator option.
2. Create a new directory, for example, /home/instantclient11\_2 on UNIX and Linux, or c:\\instantclient11\_2 on Windows.
3. Copy the SQL\*Plus Instant Client and the OCI Instant Client files to the new directory. All files must be copied from the same ORACLE\_HOME.
	See Installing SQL\*Plus Instant Client on UNIX or Linux or Installing SQL\*Plus Instant Client on Windows for a list of the files to copy.
4. Configure SQL\*Plus Instant Client. See Configuring SQL\*Plus Instant Client.

### Installing SQL\*Plus Instant Client on UNIX or Linux

To install SQL\*Plus Instant Client using the Basic OCI package on UNIX and Linux, copy the following files:

```
$ORACLE_HOME/instantclient/libociei.so
$ORACLE_HOME/lib/libclntsh.so.11.1
$ORACLE_HOME/lib/libnnz11.so
$ORACLE_HOME/lib/libsqlplus.so
$ORACLE_HOME/lib/libsqlplusic.so
$ORACLE_HOME/bin/sqlplus
```

To install SQL\*Plus Instant Client using the lightweight OCI package on UNIX and Linux, copy the following files:

```
$ORACLE_HOME/instantclient/light/libociicus.so
$ORACLE_HOME/lib/libclntsh.so.11.1
$ORACLE_HOME/lib/libnnz11.so
$ORACLE_HOME/lib/libsqlplus.so
$ORACLE_HOME/lib/libsqlplusic.so
$ORACLE_HOME/bin/sqlplus
```

### Installing SQL\*Plus Instant Client on Windows

To install SQL\*Plus Instant Client using the Basic OCI package on Windows, copy the following files:

```
ORACLE_HOME\instantclient\oraociei11.dll
ORACLE_HOME\bin\oci.dll
ORACLE_HOME\bin\orannzsbb11.dll
ORACLE_HOME\bin\orasqlplusic11.dll
ORACLE_HOME\bin\sqlplus.exe
```

To install SQL\*Plus Instant Client using the lightweight OCI package on Windows, copy the following files:

```
ORACLE_HOME\instantclient\light\oraociicus11.dll
ORACLE_HOME\bin\oci.dll
ORACLE_HOME\bin\orannzsbb11.dll
ORACLE_HOME\bin\orasqlplusic11.dll
ORACLE_HOME\bin\sqlplus.exe
```

## Configuring SQL\*Plus Instant Client

The SQL\*Plus Instant Client executable should only be used with the matching version of the OCI Instant Client.

Note that no ORACLE\_HOME or ORACLE\_SID environment variables need to be set.

### Configuring SQL\*Plus Instant Client on Linux (from RPMs)

The RPMs downloaded from OTN install into Oracle specific sub-directories in the /usr file system. The sub-directory structure enables multiple versions of Instant Client to be available.

1. Add the name of the directory containing the Instant Client libraries to LD\_LIBRARY\_PATH. Remove any other Oracle directories.
	For example, to set LD\_LIBRARY\_PATH on Solaris in the Bourne or Korn shells:
	```
	LD_LIBRARY_PATH=/usr/lib/oracle/11.2.0.1/client/lib:${LD_LIBRARY_PATH}
	export LD_LIBRARY_PATH
	```
2. Make sure the sqlplus executable installed from the RPM is the first found in your PATH. To test, enter which sqlplus which should return /usr/bin/sqlplus. If not, remove any other Oracle directories from PATH, or put /usr/bin before other SQL\*Plus executables in PATH, or use an absolute or relative path to start SQL\*Plus.
	For example, to set PATH in the bash shell:
	```
	PATH=/usr/bin:${PATH}
	export PATH
	```
	If you install multiple versions of SQL\*Plus, you may need to change the symbolic link /usr/bin/sqlplus to the version of SQL\*Plus matching the libraries in LD\_LIBRARY\_PATH. For 11.2.0.1, /usr/bin/sqlplus is a symbolic link to the SQL\*Plus binary at /usr/lib/oracle/11.2.0.1/client/bin/sqlplus.
3. Set Oracle globalization variables required for your locale. A default locale will be assumed if no variables are set. See the [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm) for more information.
	For example:
	```
	NLS_LANG=AMERICAN_AMERICA.UTF8
	export NLS_LANG
	```

### Configuring SQL\*Plus Instant Client on Linux (from Client Media or Zip File) and UNIX

1. Add the name of the directory containing the Instant Client files to the appropriate shared library path LD\_LIBRARY\_PATH, LIBPATH or SHLIB\_PATH. Remove any other Oracle directories.
	For example on Solaris in the Bourne or Korn shells:
	```
	LD_LIBRARY_PATH=/home/instantclient11_2:${LD_LIBRARY_PATH}
	export LD_LIBRARY_PATH
	```
2. Add the directory containing the Instant Client files to the PATH environment variable. If it is not set, then an absolute or relative path must be used to start SQL\*Plus. Remove any other Oracle directories from PATH. For example:
	```
	PATH=/home/instantclient11_2:${PATH}
	export PATH
	```
3. Set Oracle globalization variables required for your locale. A default locale will be assumed if no variables are set. See the [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm) for more information.
	For example:
	```
	NLS_LANG=AMERICAN_AMERICA.UTF8
	export NLS_LANG
	```

### Configuring SQL\*Plus Instant Client on Windows

The environment may be configured using SET commands in a Windows command prompt or made permanent by setting Environment Variables in System Properties.

For example, to set environment variables in Windows 2000 using System Properties, open System from the Control Panel, click the Advanced tab and then click Environment Variables.

1. Add the directory containing the Instant Client files to the PATH system environment variable. Remove any other Oracle directories from PATH.
	For example, add c:\\instantclient11\_2 to the beginning of PATH.
2. Set Oracle globalization variables required for your locale. A default locale will be assumed if no variables are set. See the [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm) for more information. For example, to set NLS\_LANG for a Japanese environment, create a user environment variable NLS\_LANG set to JAPANESE\_JAPAN.JA16EUC.
	If you have installed the lightweight Instant Client, see Lightweight Instant Client for information about supported NLS\_LANG settings.

## Connecting to a Database with SQL\*Plus Instant Client

SQL\*Plus Instant Client is always 'remote' from any database server. To connect to a database you must specify the database using an Oracle Net connection identifier.

An example using an Easy Connection identifier to connect to the HR schema in the MYDB database running on mymachine is:

```
sqlplus hr/your_password@\"//mymachine.mydomain:port/MYDB\"
```

Alternatively you can use a Net Service Name:

```
sqlplus hr/your_password@MYDB
```

Net Service Names can be stored in a number of places, including LDAP. The use of LDAP is recommended to take advantage of the new features of Oracle Database 11g. See the [Oracle Database Net Services Reference](https://docs.oracle.com/cd/E11882_01/network.112/e10835/toc.htm) for more information.

If you want to use Net Service Names configured in a local Oracle Net tnsnames.ora file, then set the environment variable TNS\_ADMIN to the directory containing the tnsnames.ora file. For example, on UNIX, if your tnsnames.ora file is in /home/user1 and it defines the Net Service Name MYDB2:

```
TNS_ADMIN=/home/user1
export TNS_ADMIN
sqlplus hr@MYDB2
```

If TNS\_ADMIN is not set, then an operating system dependent set of directories is examined to find tnsnames.ora. This search path includes looking in the directory specified by the ORACLE\_HOME environment variable for network/admin/tnsnames.ora. This is the only reason to set the ORACLE\_HOME environment variable for SQL\*Plus Instant Client. If ORACLE\_HOME is set when running Instant Client applications, it must be set to a directory that exists.

This example assumes the ORACLE\_HOME environment variable is set, and the $ORACLE\_HOME/network/admin/tnsnames.ora or ORACLE\_HOME\\network\\admin\\tnsnames.ora file defines the Net Service Name MYDB3:

```
sqlplus hr@MYDB3
```

The TWO\_TASK (on UNIX) or LOCAL (on Windows) environment variable can be set to a connection identifier. This removes the need to explicitly enter the connection identifier whenever a connection is made in SQL\*Plus or SQL\*Plus Instant Client. This UNIX example connects to the database known as MYDB4:

```
TNS_ADMIN=/home/user1
export TNS_ADMIN
TWO_TASK=MYDB4
export TWO_TASK
sqlplus hr
```

On Windows, TNS\_ADMIN and LOCAL may be set in the System Properties. See Configuring SQL\*Plus Instant Client on Windows.

## AS SYSDBA or AS SYSOPER Connections with SQL\*Plus Instant Client

To connect AS SYSDBA or AS SYSOPER to perform DBA tasks, you need to set up an Oracle password file on the database server using the database's orapwd utility. Once this is configured, your SQL\*Plus Instant Client connection string might look something like:

```
sqlplus sys@MYDB AS SYSDBA
```

See the [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for information on Oracle password files.

## Uninstalling Instant Client

The SQL\*Plus Instant Client package can be removed separately from the OCI Instant Client. After uninstalling the SQL\*Plus Instant Client package, the remaining OCI Instant Client libraries enable custom written OCI programs or third party database utilities to connect to a database.

### Uninstalling SQL\*Plus Instant Client

1. For installations on Linux from RPM packages, use rpm -e only on the SQL\*Plus Instant Client package
	or
	For installations on UNIX and Windows, and installations on Linux from the Client Release media, manually remove the following SQL\*Plus specific files:
	Table D-4 Instant Client Files in the SQL\*Plus Package
	| UNIX | Windows | Description |
	| --- | --- | --- |
	| sqlplus | sqlplus.exe | SQL\*Plus executable |
	| libsqlplus.so | not applicable | SQL\*Plus library |
	| libsqlplusic.so | orasqlplusic11.dll | SQL\*Plus data shared library |
2. Reset environment variables and remove tnsnames.ora if necessary.

### Uninstalling the Complete Instant Client

1. For installations on Linux from RPM packages, use rpm -qa to find the SQL\*Plus Instant Client and Basic OCI package names and run rpm -e to remove them
	or
	For installations on UNIX and Windows, and installations on Linux from the Client Release media, manually delete the directory containing the SQL\*Plus executable and Oracle libraries.
	See Installing SQL\*Plus Instant Client from the 11g Client Release Media for a list of the files you copied to the directory.
2. Reset environment variables such as PATH, SQLPATH, LD\_LIBRARY\_PATH and TNS\_ADMIN.
3. Remove tnsnames.ora if necessary.