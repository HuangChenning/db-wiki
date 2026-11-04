---
title: Oracle Database Client Postinstallation Tasks
book: Database Client Installation Guide for  Linux
doc_id: E24322-14
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e24322/post_inst_task.htm
tags:
  - oracle
  - 11g
  - database-client-installation-guide-for-linux
---

## 4 Oracle Database Client Postinstallation Tasks

This chapter describes how to complete postinstallation tasks after you have installed the Oracle database client software. It includes information about the following topics:

You must perform the tasks listed in "Required Postinstallation Tasks". Oracle recommends that you perform the tasks listed in "Recommended Postinstallation Tasks" after all installations.

If you install and intend to use any of the products listed in "Required Product-Specific Postinstallation Tasks", then you must perform the tasks listed in the product-specific subsections.

Note:

This chapter describes basic configuration only. Refer to [Oracle Database Administrator's Reference for Linux and UNIX-Based Operating Systems](https://docs.oracle.com/cd/E11882_01/server.112/e10839/toc.htm), [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) and product-specific administration and tuning guides for exhaustive configuration and tuning information.

## 4.1 Required Postinstallation Tasks

You must perform the tasks described in the following sections after completing an installation:

- Downloading and Installing Patches
- Updating Instant Client
- Connecting with Instant Client

### 4.1.1 Downloading and Installing Patches

Check the My Oracle Support website for required patches for the installation.

Note:

You cannot update Instant Client by downloading a patch. Use the procedure under "Updating Instant Client" to update Instant Client.

To download required patches:

1. Use a web browser to view the My Oracle Support website:
	```
	https://support.oracle.com/
	```
2. Log in to My Oracle Support.
	Note:
	If you are not a My Oracle Support registered user, click Register here and follow the registration instructions.
3. On the main My Oracle Support page, click the Patches and Updates tab.
4. In the Patch Search group, select Product or Family (Advanced).
5. In the Product field, select Oracle Database.
6. In the Release field select the release number. For example, Oracle 11.2.0.3.1.
7. Click Search.
8. Any available patch updates are displayed in the Patch Search page.
9. Select the patch number and click ReadMe. The README page is displayed and contains information about the patch set and how to apply the patches to your installation.
10. Return to the Patch Search page, click Download, and save the file on your system.
11. Use the unzip utility provided with Oracle Database 11g release 1 (11.1) to uncompress the Oracle patch updates that you downloaded from My Oracle Support. The unzip utility is located in the `$ORACLE_HOME/bin` directory.

### 4.1.2 Updating Instant Client

To update Instant Client:

1. Download Instant Client from Oracle Technology Network:
	`http://www.oracle.com/technetwork/database/features/instant-client/index-097480.html`
2. If you want to place the files in the existing directory, then ensure that the directory is empty.
	If you want to place the files into a different directory (and remove the previous files), ensure that you update the `PATH` environment variable setting to reflect the new location.

Note:

A restriction on Instant Client or Instant Client Light is that you cannot perform patch upgrades using the `opatch` utility because the Instant Client installation does not create an inventory, which the patch upgrade process must access for patch upgrades. The absence of an inventory also means that the installed intern patch reporting and conflict detection before a patch attempt are not possible.

### 4.1.3 Connecting with Instant Client

If you installed the Instant Client installation type, you can configure users' environments to enable dynamically linked client applications to connect to a database as follows:

1. Set the appropriate shared library path environment variable for the platform to specify the directory that contains the Instant Client libraries. For the Instant Client installation type, this directory is the Oracle home directory that you specified during the installation, for example:
	```
	/u01/app/oracle/product/11.2.0/client_1
	```
2. Use one of the following methods to specify database connection information for the client application:
	- Specify a SQL connect URL string using the following format:
		```
		//host:port/service_name
		```
		- Set the `TNS_ADMIN` environment variable to specify the location of the `tnsnames.ora` file and specify a service name from that file.
		- Set the `TNS_ADMIN` environment variable and set the `TWO_TASK` environment variable to specify a service name from the `tnsnames.ora` file.

Note:

You do not have to specify the `ORACLE_HOME` environment variable.

## 4.2 Recommended Postinstallation Tasks

Oracle recommends that you perform the tasks described in the following section after completing an installation:

- Configuring Instant Client Light
- Creating a Backup of the root.sh Script
- Connecting Instant Client or Instant Client Light to an Oracle Database
- Setting Up User Accounts
- Setting the NLS\_LANG Environment Variable
- Generating the Client Static Library

### 4.2.1 Configuring Instant Client Light

When you install Instant Client, the Instant Client libraries are installed under the `ORACLE_HOME` directory and the Instant Client Light specific library is installed under the `ORACLE_HOME` `/light` directory. To configure Instant Client Light, you must replace the `ORACLE_HOME` `/libociei.``so` file with the `ORACLE_HOME/light` `/libociicus.``so` file.

After replacing the library file, you must set the `LD_LIBRARY_PATH` environment variable to point to the location of the Instant Client shared library files.

### 4.2.2 Creating a Backup of the root.sh Script

Oracle recommends that you back up the `root.sh` script after you complete an installation. If you install other products in the same Oracle home directory, then Oracle Universal Installer updates the contents of the existing `root.sh` script during the installation. If you require information contained in the original `root.sh` script, then you can recover it from the backed up `root.sh` file.

### 4.2.3 Connecting Instant Client or Instant Client Light to an Oracle Database

Before you can connect Instant Client (including Instant Client Light) to an Oracle database, ensure that the `LD_LIBRARY_PATH` environment variable specifies the directory that contains the Instant Client libraries. This directory is the `ORACLE_HOME` directory that you specified during installation.

For example, the shared libraries for Instant Client or Instant Client Light (if you have configured Instant Client Light), are in:

```
/u01/app/oracle/product/11.2.0/client_1
```

After you have checked the `LD_LIBRARY_PATH` environment variable, you can use any of the following methods to specify Oracle Database connection information for client applications:

- Specifying a Connection by Using the Easy Connect Naming Method
- Specifying a Connection by Configuring a tnsnames.ora File
- Specifying a Connection Using an Empty Connect String and TWO\_TASK

#### 4.2.3.1 Specifying a Connection by Using the Easy Connect Naming Method

You can specify a connection address to an Oracle Database directly from a client application, without having to configure a `tnsnames` setting for the Instant Client. This method is convenient as you do not have to create and manage a `tnsnames.ora` file. However, the application users must specify the host name and port number when they want to log in to the application.

For example, if you run SQL\*Plus on the client computer and want to connect to the `sales_us` database, which is located on a server whose host name is `shobeen` and port number is `1521`, then you can log in as follows:

```
sqlplus system/admin@//shobeen:1521/sales_us
```

Similarly, in the application code, you can use Oracle Call Interface net naming methods to create the Instant Client-to-Oracle Database connection. For example, the following formats in the `OCIServerAttach()` call specify the connection information:

- Specify a SQL connect URL string using the following format:
	```
	//host[:port][/service_name]
	```
	For example:
	```
	//shobeen:1521/sales_us
	```
- Alternatively, you can specify the SQL connect information as an Oracle Net keyword-value pair. For example:
	```
	"(DESCRIPTION=(ADDRESS=(PROTOCOL=tcp) (HOST=shobeen) (PORT=1521))
	(CONNECT_DATA=(SERVICE_NAME=sales_us)))"
	```
	See Also:
	Oracle Call Interface Programmer's Guide for more information on using Oracle Call Interface Instant Client

#### 4.2.3.2 Specifying a Connection by Configuring a tnsnames.ora File

By default, when you install Instant Client, Oracle Universal Installer does not include a sample `tnsnames.ora` file nor the Oracle Net Configuration Assistant utility normally used to create it. However, to shield users from having to specify actual host names and port numbers, consider using a `tnsnames.ora` file to set the Client-to-Oracle Database connection.

You can create the `tnsnames.ora` file manually by copying and modifying a version of this file from another Oracle installation, or you can use Oracle Net Configuration Assistant to create and manage it for you.

To install Oracle Net Configuration Assistant:

1. Run Oracle Universal Installer.
2. Select the Custom installation type.
3. In the Available Product Components screen, select Oracle Net Listener.
4. In the Summary screen, click Install, click Exit, and then click Yes to exit Oracle Universal Installer.

On each client computer, configure either of the following settings:

- Set the `TNS_ADMIN` environment variable to specify the location of the `tnsnames.ora` file and specify a service name from that file.
- Place the `tnsnames.ora` file in the `$ORACLE_HOME` `/network/admin` directory, and ensure that the `ORACLE_HOME` environment has been set to this Oracle home.
	See Also:
	[Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/toc.htm) for more information on Oracle Call Interface Instant Client connection strings

#### 4.2.3.3 Specifying a Connection Using an Empty Connect String and TWO\_TASK

You can set the connect string to an empty connect string (""), and then set the `TWO_TASK` environment variable to one of the following values:

- A direct address, as described under "Specifying a Connection by Using the Easy Connect Naming Method"
- Oracle Net keyword-value pair
- A `tnsnames.ora` entry and `TNS_ADMIN` is set to the location of `tnsnames.ora`
- A `tnsnames.ora` entry and the following:
	- `tnsnames.ora` file located in `$ORACLE_HOME` `/network/admin`
		- The `ORACLE_HOME` environment variable set to this Oracle home

This method allows the applications to specify internally a connection string if the application code itself uses an empty connection string. The benefit of an empty connect string is that the application itself does not have to specify the `tnsnames.ora` entry. Instead, when a user starts the application, the location of the database is determined by a script or the environment, depending on where you have set the `TWO_TASK` environment variable. The disadvantage of using empty strings is that you must configure this additional information in order for the application to connect to the database.

### 4.2.4 Setting Up User Accounts

For information about setting up additional user accounts, refer to Oracle Database Administrator's Reference for Linux and UNIX-Based Operating Systems.

### 4.2.5 Setting the NLS\_LANG Environment Variable

`NLS_LANG` is an environment variable that specifies the locale behavior for Oracle software. This variable sets the language and territory used by the client application and the database user session. It also declares the character set of the client, which is the character set of data entered or displayed by an Oracle client program, such as SQL\*Plus.

See Also:

[Appendix B, "Configuring Oracle Database Globalization Support"](app_gblsupp.md) for more information about the `NLS_LANG` environment variable

Note:

The character set of the data displayed is determined by the environment of the operating system, such as keyboard driver and fonts in use. The `NLS_LANG` character set should match the operating system.

### 4.2.6 Generating the Client Static Library

The client static library (`libclntst11.a`) is not generated during installation. If you want to link the applications to the client static library, you must first generate it as follows:

1. Switch user to `oracle`.
2. Set the `ORACLE_HOME` environment variable to specify the Oracle home directory used by the Oracle Database installation. For example:
	- Bourne, Bash, or Korn shell:
		```
		$ ORACLE_HOME=/u01/app/oracle/product/11.2.0/client_1 
		$ export ORACLE_HOME
		```
		- C shell:
		```
		% setenv ORACLE_HOME /u01/app/oracle/product/11.2.0/client_1
		```
3. Enter the following command:
	```
	$ $ORACLE_HOME/bin/genclntst
	```

## 4.3 Required Product-Specific Postinstallation Tasks

The following sections describe postinstallation tasks that you must perform if you install and intend to use the products mentioned:

- Configuring Oracle Net Services
- Configuring Oracle Precompilers

Note:

You must perform postinstallation tasks only for products that you intend to use.

### 4.3.1 Configuring Oracle Net Services

If you have an earlier release of Oracle software installed on this system, you might want to copy information from the Oracle Net `tnsnames.ora` and `listener.ora` configuration files from the earlier release to the corresponding files for the new release.

Note:

The default location for the `tnsnames.ora` and `listener.ora` files is the `$ORACLE_HOME/network/admin/` directory. However, you can also use a central location for these files.

If necessary, you can also add connection information for additional database instances to the new file.

### 4.3.2 Configuring Oracle Precompilers

This section describes postinstallation tasks for Oracle precompilers:

- Configuring Pro\*C/C++
- Configuring Pro\*FORTRAN

Note:

All precompiler configuration files are located in the `$ORACLE_HOME/precomp/admin` directory.

#### 4.3.2.1 Configuring Pro\*C/C++

Verify that the `PATH` environment variable setting includes the directory that contains the C compiler executable.

The following table shows the default directories and the appropriate command to verify the path setting of the compiler:

Table 4-1 C/C++ Compiler Directory

| Path | Command |
| --- | --- |
| `/usr/bin` | `$ which gcc` |
| `/opt/intel_cce_80/bin/icc` | `$ which icc` |

#### 4.3.2.2 Configuring Pro\*FORTRAN

Verify that the `PATH` environment variable setting includes the directory that contains the FORTRAN compiler executable. You can verify the path setting by using the `which` `xlf` command.