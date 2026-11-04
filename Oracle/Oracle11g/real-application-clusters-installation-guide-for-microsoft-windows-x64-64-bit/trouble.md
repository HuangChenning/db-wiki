---
title: Troubleshooting Oracle Real Application Clusters Installations
book: Real Application Clusters Installation Guide for Microsoft Windows x64 (64-Bit)
doc_id: E48195-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e48195/trouble.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-microsoft-windows-x64-64-bit
---

## A Troubleshooting Oracle Real Application Clusters Installations

This appendix provides troubleshooting information for installing Oracle Real Application Clusters (Oracle RAC).

See Also:

The Oracle Database 11g release 2 (11.2) Oracle Real Application Clusters documentation set included with the installation media in the Documentation directory:

This appendix contains the following topics:

## A.1 Troubleshooting Oracle RAC Installation Errors

The following information explains how to proceed if you encounter an error during installation of Oracle RAC.

### A.1.1 Verifying Requirements

Before you try any of the troubleshooting steps in this appendix, do the following:

- Check [Chapter 1, "Preinstallation Checklist"](chklist.md) to ensure that your system meets the requirements and that you have completed all of the preinstallation tasks.
- Read the release notes for the product on your platform before installing it. The release notes are available on the Oracle Database installation media. You can find the latest version of the release notes on the Oracle Technology Network web site:
	```
	http://www.oracle.com/technetwork/indexes/documentation/
	```

### A.1.2 Understanding How To Resolve Installation Errors

If you encounter an error during installation:

- Do not exit Oracle Universal Installer (OUI).
- If you clicked Next after you entered incorrect information in an installation window, then click Back to return to the window and correct the information.
- If you encounter an error while OUI is copying files, then see Section A.1.3, "Locating the Log File For an Installation Session" for interactive installations or Section A.4, "Troubleshooting Silent or Noninteractive Installations" for more information.
- If you encounter an error while a configuration assistant is running, then see the Section A.3, "Troubleshooting Configuration Assistant Errors" section.
- If you cannot resolve the problem, then remove the failed installation by following the steps listed in Section A.6, "Cleaning Up After a Failed Installation.".

### A.1.3 Locating the Log File For an Installation Session

During an installation, OUI records all the actions that it performs in a log file. If you encounter problems during the installation, then review the log file for information about possible causes of the problem.

By default, the log files are located in the following directory:

```
%SYSTEMDRIVE%\Program Files\Oracle\Inventory\logs
```

Log file names from interactive installations have the form:

```
installActionsdate_time.log
```

For example, if an interactive installation occurred at 9:00:56 a.m. on October 14, 2009, then the log file would be named:

```
installActions2009-10-14_09-00-56AM.log
```

Note:

Do not delete or manually alter the `Inventory` directory or its contents. Doing so can prevent OUI from locating products that you install on your system.

See Also:

Section A.4, "Troubleshooting Silent or Noninteractive Installations"

## A.2 Resolving Oracle RAC Installations Errors

This section contains the following topics:

- General Installation Issues
- Performing Cluster Diagnostics During Oracle RAC Installations
- Reviewing the Log of an Installation Session

### A.2.1 General Installation Issues

The following list contains examples of the types of errors that can occur during installation:

- Nodes unavailable for selection from the OUI Node Selection screen
- Node nodename is unreachable
- PROT-8: Failed to import data from specified file to the cluster registry
- Time stamp is in the future
- Administrative user unable to log in to SQL\*Plus using the SYSDBA privilege

Nodes unavailable for selection from the OUI Node Selection screen

Cause: Oracle Clusterware was either not installed, or the Oracle Clusterware services were not active or started.

Action: Install Oracle Clusterware, or review the status of your Oracle Clusterware. Consider restarting the nodes, because doing so may resolve the problem.

Node nodename is unreachable

Cause: The IP host was unavailable.

Action: Attempt the following:
1. Run the command `ipconfig /all`. Compare the output of this command with the contents of the `C:\WINDOWS\system32\drivers\etc\hosts` file to ensure that the node IP is listed.
2. Run the command `nslookup` to verify that the host is reachable.

PROT-8: Failed to import data from specified file to the cluster registry

Cause: Insufficient space in an existing Oracle Cluster Registry raw device partition, which caused a migration failure at the end of the installation. To confirm this issue, look for the error "Not enough space in the backing store" in the log file `Grid_home` `\log\` `hostname` `\client\ocrconfig_` `pid``.log`.

Action: Identify a raw disk partition that has 280 MB or more available space. Copy the contents of the existing raw partition from to the new device using the command `XCOPY`.

Time stamp is in the future

One or more nodes had a different clock time than the local node. If this was the case, then you may see output similar to the following:
```
time stamp 2019-04-04 14:49:49 is 106 s in the future
```

Action: Ensure that all member nodes of the cluster have the same clock time.

Administrative user unable to log in to SQL\*Plus using the SYSDBA privilege

Cause: When Oracle Database on Microsoft Windows was installed, Oracle Universal Installer created a Windows local group called `ORA_DBA`, and then added the user name of the user performing the installation to this group. Members of `ORA_DBA` automatically receive the SYSDBA privilege. However, for cluster installations, OUI does not add the user to `ORA_DBA` if they have performed the installation remotely. As a result, this user could not log in to SQL\*Plus using the SYSDBA privilege.

Action: Manually add remote users to `ORA_DBA`.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/dba.htm#ADMIN00102) for information about connecting to the database using SQL\*Plus

### A.2.2 Performing Cluster Diagnostics During Oracle RAC Installations

When installing Oracle RAC, if OUI does not display the Node Selection page, then perform clusterware diagnostics by running the `olsnodes` `-v` command from the binary directory in your Oracle Clusterware home (`Grid_home` `\bin`) and analyzing its output. See [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/intro.htm#CWADD90958) if the detailed output indicates that your clusterware is not running.

In addition, use the following command to check the integrity of the Cluster Manager, where the variable `node_list` is the list of nodes in your cluster, separated by commas:

```
cluvfy comp clumgr -n node_list -verbose
```

### A.2.3 Reviewing the Log of an Installation Session

During an installation, OUI records all of the actions that it performs in a log file. If you encounter problems during the installation, then review the log file for information about possible causes of the problem.

To view the log file, follow these steps:

1. Go to the `logs` subdirectory of the Oracle Inventory directory:
	```
	C:\> cd Program Files\Oracle\Inventory\logs
	```
2. View the file details for the folder to determine the most recent file. Installer log files have names similar to the following, where `date_time` indicates the date and time that the installation started:
	```
	installActionsdate_time.log
	```
3. Use a text editor to view the most recent entries in the log file, where information about a problem is most likely to appear.

## A.3 Troubleshooting Configuration Assistant Errors

To troubleshoot an installation error that occurs when a configuration assistant is running, do the following:

- Review the installation log files listed in the section Section A.3.1, "Reviewing Configuration Assistant Errors.".
- Review the specific configuration assistant log file located in the Oracle base directory, in the path `%ORACLE_BASE%\cfgtoollogs`. Try to fix the issue that caused the error.
- If you see the "Fatal Error. Reinstall" message, then look for the cause of the problem by reviewing the log files. See the section Section A.3.3, "Resolving Irrecoverable Errors Reported by Configuration Assistants" for further instructions.

### A.3.1 Reviewing Configuration Assistant Errors

To troubleshoot an installation error that occurs when a configuration assistant, such as Oracle Net Configuration Assistant (NETCA), is running:

1. Review the installation log files as described in the section Section A.2.3, "Reviewing the Log of an Installation Session."
2. Review the specific configuration assistant log file as described in Section A.3.2, "Identifying Configuration Assistant Failures." Try to fix the issue that caused the error.
3. If you see the "Fatal Error. Reinstall" message, then look for the cause of the problem by reviewing the log files. See Section A.3.3, "Resolving Irrecoverable Errors Reported by Configuration Assistants" for more information.

### A.3.2 Identifying Configuration Assistant Failures

If an Oracle configuration assistant is not able to complete its configuration tasks, then it reports a status of 'Failed'. Oracle configuration assistant failures are noted at the bottom of the installation screen. The configuration assistant interface displays additional information, if available.

The configuration assistant execution status is stored in the following file:

```
C:\Program Files\Oracle\Inventory\logs\installActionsdate_time.log
```

Completion status codes are listed in the following table:

| Status | Result Code |
| --- | --- |
| Configuration assistant succeeded | 0 |
| Configuration assistant failed | 1 |
| Configuration assistant canceled | \-1 |

More information about errors related to the configuration assistant can be found in the following directory, where the `ORACLE_BASE` directory is the Oracle base for the user performing the Oracle RAC installation:

```
ORACLE_BASE\cfgtoollogs
```

### A.3.3 Resolving Irrecoverable Errors Reported by Configuration Assistants

If you receive an irrecoverable (or fatal) error while a configuration assistant is running, then you must complete the following tasks:

1. Remove the failed installation as described in Section A.6, "Cleaning Up After a Failed Installation."
2. Correct the cause of the irrecoverable error.
3. Reinstall the Oracle software.

See Also:

[Chapter 8, "Removing Oracle Real Application Clusters Software"](rem_orcl.md)

## A.4 Troubleshooting Silent or Noninteractive Installations

To determine whether a silent or noninteractive installation succeeds or fails, check the `silentInstallActions` `date_time``.log` file, located in `DRIVE_LETTER``:\Program Files\Oracle\Inventory\logs`, as described in Section A.2.3, "Reviewing the Log of an Installation Session."

A silent or noninteractive installation fails if:

- You do not specify a response file.
- You specify an incorrect or incomplete response file.
	For example, a common problem is that while all the product-specific data is correct, the staging area location may be incorrect. If this is the case, then check the `FROM_LOCATION` variable and ensure that it points to the `products.xml` file in the installation media. In the installation media, this `products.xml` is in `database\stage`.
- OUI encounters an error, such as insufficient disk space.

OUI or a configuration assistant validates the response file at run time. If the validation fails, then the silent or noninteractive installation or configuration process ends. OUI treats values for parameters that are of the wrong context, format, or type as if no value had been specified in the file.

See Also:

Section A.1.3, "Locating the Log File For an Installation Session"

## A.5 About Using CVU Cluster Healthchecks After Installation

Starting with Oracle Grid Infrastructure 11g release 2 (11.2.0.3) and later, you can use the CVU `healthcheck` command option to check your Oracle Clusterware and Oracle Database installations for their compliance with mandatory requirements and best practices guidelines, and to ensure that they are functioning properly.

Use the following syntax to run the healthcheck command option:

cluvfy comp healthcheck \[-collect {cluster|database}\] \[-db db\_unique\_name\] \[-bestpractice|-mandatory\] \[-deviations\] \[-html\] \[-save \[-savedir directory\_path\]

For example:

```
$ cd /home/grid/cvu_home/bin
$ ./cluvfy comp healthcheck -collect cluster -bestpractice -deviations -html
```

The options are:

- `-collect [cluster|database]`
	Use this flag to specify that you want to perform checks for Oracle Clusterware (cluster) or Oracle Database (database). If you do not use the collect flag with the healthcheck option, then `cluvfy comp healthcheck` performs checks for both Oracle Clusterware and Oracle Database.
- `-db` `db_unique_name`
	Use this flag to specify checks on the database unique name that you enter after the `db` flag.
	CVU uses JDBC to connect to the database as the user `cvusys` to verify various database parameters. For this reason, if you want checks to be performed for the database you specify with the `-db` flag, then you must first create the `cvusys` user on that database, and grant that user the CVU-specific role, CVUSAPP. You must also grant members of the CVUSAPP role SELECT permissions on system tables.The SQL script cvusys.sql is included in the CVU\_home `/cv/admin` directory to facilitate the creation of this user. Use this SQL script to create the `cvusys` user on all the databases that you want to verify using CVU.
	If you use the `db` flag but do not provide a database unique name, then CVU discovers all the Oracle Databases on the cluster. If you want to perform best practices checks on these databases, then you must create the `cvusys` user on each database, and grant that user the CVUSAPP role with the SELECT privileges needed to perform the best practice checks.
- `[-bestpractice | -mandatory] [-deviations`\]
	Use the `bestpractice` flag to specify best practice checks, and the `mandatory` flag to specify mandatory checks. Add the `deviations` flag to specify that you want to see only the deviations from either the best practice recommendations or the mandatory requirements. You can specify either the `-bestpractice` or `-mandatory` flag, but not both flags. If you specify neither `-bestpractice` or `-mandatory`, then both best practices and mandatory requirements are displayed.
- `-html`
	Use the `html` flag to generate a detailed report in HTML format.
	If you specify the `html` flag, and a browser CVU recognizes is available on the system, then the browser is started and the report is displayed on the browser when the checks are complete.
	If you do not specify the html flag, then the detailed report is generated in a text file.
- `-save [-savedir` `dir_path`\]
	Use the `save` or `-save -savedir` flags to save validation reports (`cvuchecdkreport_` `timestamp``.txt` and `cvucheckreport_` `timestamp``.htm`), where `timestamp` is the time and date of the validation report.
	If you use the `save` flag by itself, then the reports are saved in the path `CVU_home` `/cv/report`, where `CVU_home` is the location of the CVU binaries.
	If you use the flags `-save -savedir`, and enter a path where you want the CVU reports saved, then the CVU reports are saved in the path you specify.

## A.6 Cleaning Up After a Failed Installation

If an installation fails, then you must remove the Oracle home directory and remove all files that OUI created during the attempted installation. Perform the following steps to clean up the failed installation:

1. Follow the instructions in [Chapter 8, "Removing Oracle Real Application Clusters Software"](rem_orcl.md) to run OUI to deinstall Oracle RAC.
2. Manually remove the directory that was used as the Oracle home directory during the installation.
3. Remove the following Windows Registry keys created by OUI during the previous installation attempt:
	```
	HKEY_LOCAL_MACHINE\SOFTWARE\ODBC\ODBCINST.INI
	HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Oracle11\Performance
	 \KEY_ORACLE_HOME_NAME
	```

After you have completed these steps, you can start the installation again.