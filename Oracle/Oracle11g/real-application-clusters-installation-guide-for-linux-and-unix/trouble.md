---
title: Troubleshooting Oracle Real Application Clusters Installations
book: Real Application Clusters Installation Guide for Linux and UNIX
doc_id: E41962-05
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41962/trouble.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-linux-and-unix
---

## A Troubleshooting Oracle Real Application Clusters Installations

This appendix provides troubleshooting information for installing Oracle Real Application Clusters (Oracle RAC). It contains the following sections:

- Troubleshooting Oracle Real Application Clusters Installations
- About Using CVU Cluster Healthchecks After Installation

See Also:

The Oracle Database 11g release 2 (11.2) Oracle Real Application Clusters documentation set included with the installation media in the Documentation directory:
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/toc.htm)
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/toc.htm)

## A.1 Troubleshooting Oracle Real Application Clusters Installations

This section contains the following topics:

### A.1.1 General Installation Issues

The following is a list of examples of the types of errors that can occur during installation. It contains the following issues:

- An error occurred while trying to get the disks
- Failed to connect to server, Connection refused by server, or Can't open display
- Nodes unavailable for selection from the OUI Node Selection screen
- Node nodename is unreachable
- PROT-8: Failed to import data from specified file to the cluster registry
- PRKP-1001: Error starting instance
- Time stamp is in the future
- YPBINDPROC\_DOMAIN: Domain not bound

An error occurred while trying to get the disks

Cause: There is an entry in `/etc/oratab` pointing to a non-existent Oracle home. The OUI error file should show the following error: " `java.io.IOException: /home/oracle/OraHome//bin/kfod: not found` "

Action: Remove the entry in `/etc/oratab` pointing to a non-existing Oracle home.

Failed to connect to server, Connection refused by server, or Can't open display

Cause: These are typical of X Window display errors on Windows or UNIX systems, where xhost is not properly configured.

Action: In a local terminal window, log in as the user that started the X Window session, and enter the following command:

`$ xhost` `fully_qualified_remote_host_name`

For example:

```
$ xhost somehost.example.com
```

Then, enter the following commands, where `workstation_name` is the host name or IP address of your workstation.

Bourne, Bash, or Korn shell:

```
$ DISPLAY=workstation_name:0.0
$ export DISPLAY
```

To determine if X Window applications display correctly on the local system, enter the following command:

```
$ xclock
```

The X clock should appear on your monitor. If this fails, then use of the `xhost` command may be restricted on the server.

If you are using a VNC client to access the server, then ensure that you are accessing the visual that is assigned to the user that you are trying to use for the installation. For example, if you used the `su` command to become the installation owner on another user visual, and the `xhost` command use is restricted, then you cannot use the `xhost` command to change the display. If you use the visual assigned to the installation owner, then the correct display will be available, and entering the `xclock` command will display the X clock.

Nodes unavailable for selection from the OUI Node Selection screen

Cause: Oracle Clusterware is either not installed, or the Oracle Clusterware services are not up and running.

Action: Install Oracle Clusterware, or review the status of your Oracle Clusterware. Consider restarting the nodes, as doing so may resolve the problem.

Node nodename is unreachable

Cause: Unavailable IP host

Action: Attempt the following:
1. Run the command `ifconfig -a`. Compare the output of this command with the contents of the `/etc/hosts` file to ensure that the node IP is listed.
2. Run the command `nslookup` to see if the host is reachable.
3. As the `oracle` user, attempt to connect to the node with `ssh` or `rsh`. If you are prompted for a password, then user equivalence is not set up properly. Contact your system administrator, or consult The [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN) for your platform to complete SSH configuration.

PROT-8: Failed to import data from specified file to the cluster registry

Cause: Insufficient space in an existing Oracle Cluster Registry raw device partition, which causes a migration failure while running `rootupgrade.sh`. To confirm, look for the error "utopen:12:Not enough space in the backing store" in the log file `$ORA_CRS_HOME/log/` `hostname` `/client/ocrconfig_` `pid``.log`.

Action: Identify a raw device that has 280 MB or more available space. Locate the existing raw device name from `/etc/oracle/srvConfig.lo` c (AIX, HP-UX, Linux) or `/var/opt/oracle/srvConfig.loc` (Solaris), and copy the contents of this raw device to the new device using the command `dd`.

PRKP-1001: Error starting instance

Cause: Missing ODBC Driver Manager. Associated message is CRS-0215: Could not start resource.

Action: Clean up installation, download and install the ODBC driver from `http://www.unixodbc.org`, and restart the installation. This is a requirement for Oracle RAC databases, documented in system requirements in the [Oracle Grid Infrastructure](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN) installation guide for your platform.

Time stamp is in the future

One or more nodes has a different clock time than the local node. If this is the case, then you may see output similar to the following:
```
time stamp 2005-04-04 14:49:49 is 106 s in the future
```

Action: Ensure that all member nodes of the cluster have the same clock time.

YPBINDPROC\_DOMAIN: Domain not bound

Cause: This error can occur during postinstallation testing when a node public network interconnect is pulled out, and the VIP does not fail over. Instead, the node hangs, and users are unable to log in to the system. This error occurs when the Oracle home, listener.ora, Oracle log files, or any action scripts are located on an NAS device or NFS mount, and the name service cache daemon `nscd` has not been activated.

Enter the following command on all nodes in the cluster to start the nscd service:
```
/sbin/service  nscd start
```

### A.1.2 Oracle RAC Installation Error Messages

Note that the user performing the Oracle RAC installation must have membership both in the oinstall group and the OSDBA group (typically `oinstall` and `dba`). If this is not the case, then the installation will fail.

For additional help in resolving error messages, refer to My Oracle Support. For example, the note with Doc ID 1372375.1 contains some of the most common installation issues for Oracle Real Application Clusters.

### A.1.3 Performing Cluster Diagnostics During Oracle Clusterware Installations

If Oracle Universal Installer (OUI) does not display the Node Selection page, then perform clusterware diagnostics by running the `olsnodes` `-v` command from the binary directory in your Oracle Clusterware home `(Grid_home` `/bin` on Linux and UNIX-based systems, and analyzing its output. Refer to your clusterware documentation if the detailed output indicates that your clusterware is not running.

In addition, use the following command syntax to check the integrity of the Cluster Manager:

```
cluvfy comp clumgr -n node_list -verbose
```

In the preceding syntax example, the variable `node_list` is the list of nodes in your cluster, separated by commas.

### A.1.4 Reviewing the Log of an Installation Session

During an installation, Oracle Universal Installer records all of the actions that it performs in a log file. If you encounter problems during the installation, then review the log file for information about possible causes of the problem.

To view the log file, follow these steps:

1. If necessary, enter the following command to determine the location of the oraInventory directory:
	```
	$ cat /opt/oracle/oraInst.loc
	$ cat /var/opt/oracle/oraInst.loc
	```
2. Enter the following command to determine the name of the log file:
	```
	$ ls -ltr
	```
	This command lists the files in the order of creation, with the most recent file shown last. Installer log files have names similar to the following, where `date_time` indicates the date and time that the installation started:
	```
	installActionsdate_time.log
	```
	To view the most recent entries in the log file, where information about a problem is most likely to appear, enter a command similar to the following:
	```
	$ tail -50 installActions2007-07-20_09-53-22AM.log | more
	```
	This command displays the last 50 lines in the log file, and enables you to page through them.
	If the error displayed by Oracle Universal Installer or listed in the log file indicates a relinking problem, then refer to the following file for more information:
	```
	$ORACLE_HOME/install/make.log
	```

### A.1.5 Configuration Assistant Errors

To troubleshoot an installation error that occurs when a configuration assistant is running:

Review the installation log files listed in the section" "Reviewing the Log of an Installation Session".

Review the specific configuration assistant log file located in the Oracle RAC installation owner Oracle base directory, in the path `$ORACLE_BASE/cfgtoollogs`. Try to fix the issue that caused the error.

If you see the "Fatal Error. Reinstall" message, then look for the cause of the problem by reviewing the log files. Refer to the section "Fatal Errors" for further instructions.

This section contains the following topics:

- Configuration Assistant Failures
- Fatal Errors

#### A.1.5.1 Configuration Assistant Failures

Oracle configuration assistant failures are noted at the bottom of the installation screen. The configuration assistant interface displays additional information, if available. The configuration assistant execution status is stored in the following file:

```
oraInventory_location/logs/installActionsdate_time.log
```

More details about errors related to the configuration assistant can be found in the following directory:

```
$ORACLE_BASE/cfgtoollogs
```

The Oracle base directory is the Oracle base for the Oracle RAC installation owner. Completion status codes are listed in the following table:

```
Status Result Code 
Configuration assistant succeeded 0 
Configuration assistant failed 1 
Configuration assistant cancelled -1
```

#### A.1.5.2 Fatal Errors

If you receive a fatal error while a configuration assistant is running, then you must complete the following tasks:

1. Deinstall Oracle software.
2. Correct the cause of the fatal error.
3. Reinstall the Oracle software.

## A.2 About Using CVU Cluster Healthchecks After Installation

Starting with Oracle Grid Infrastructure 11g release 2 (11.2.0.3) and later, you can use the CVU healthcheck command option to check your Oracle Clusterware and Oracle Database installations for their compliance with mandatory requirements and best practices guidelines, and to check to ensure that they are functioning properly.

Use the following syntax to run the healthcheck command option:

cluvfy comp healthcheck \[-collect {cluster|database}\] \[-db db\_unique\_name\] \[-bestpractice|-mandatory\] \[-deviations\] \[-html\] \[-save \[-savedir directory\_path\]

For example:

```
$ cd /home/grid/cvu_home/bin
$ ./cluvfy comp healthcheck -collect cluster -bestpractice -deviations -html
```

The options are:

- `-collect [cluster|database]`
	Use this flag to specify that you want to perform checks for Oracle Clusterware (cluster) or Oracle Database (database). If you do not use the collect flag with the healthcheck option, then cluvfy comp healthcheck performs checks for both Oracle Clusterware and Oracle Database.
- `-db` `db_unique_name`
	Use this flag to specify checks on the database unique name that you enter after the `db` flag.
	CVU uses JDBC to connect to the database as the user `cvusys` to verify various database parameters. For this reason, if you want checks to be performed for the database you specify with the `-db` flag, then you must first create the `cvusys` user on that database, and grant that user the CVU-specific role, `cvusapp`. You must also grant members of the `cvusapp` role `select` permissions on system tables.A SQL script is included in CVU\_home `/cv/admin/cvusys.sql` to facilitate the creation of this user. Use this SQL script to create the cvusys user on all the databases that you want to verify using CVU.
	If you use the `db` flag but do not provide a database unique name, then CVU discovers all the Oracle Databases on the cluster. If you want to perform best practices checks on these databases, then you must create the `cvusys` user on each database, and grant that user the `cvusapp` role with the `select` privileges needed to perform the best practice checks.
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