---
title: Converting to Oracle RAC and Oracle RAC One Node from Single-Instance Oracle Databases
book: Real Application Clusters Installation Guide for Microsoft Windows x64 (64-Bit)
doc_id: E48195-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e48195/cvrt2rac.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-microsoft-windows-x64-64-bit
---

## C Converting to Oracle RAC and Oracle RAC One Node from Single-Instance Oracle Databases

This appendix describes the procedures for converting from Oracle Database 11g release 2 (11.2) single-instance databases to Oracle Real Application Clusters (Oracle RAC) and Oracle RAC One Node databases.

The procedures in this appendix assume that your original single-instance database and the target Oracle RAC database are using the same release, and running on the same platform. If you are upgrading from an earlier release of Oracle RAC to Oracle RAC 11g release 2, then use the Oracle Database Upgrade Assistant (DBUA).

This appendix contains the following topics:

Note:

You must use clustered Oracle Automatic Storage Management (Oracle ASM) instances for Oracle RAC databases.

See Also:

[Oracle Database Licensing Information](https://docs.oracle.com/cd/E11882_01/license.112/e47877/toc.htm) for compliance requirements that apply to the license you have purchased

## C.1 Administrative Issues for Converting Databases to Oracle RAC

Note the following administrative considerations before converting single-instance databases to Oracle RAC:

- Backup procedures should be available before converting from a single-instance Oracle Database to Oracle RAC. This includes taking a backup of your existing database before converting to Oracle RAC and being prepared to backup your Oracle RAC database immediately following the conversion.
- For archiving with Oracle RAC environments, the archive file format requires a thread number.
- The archived logs from all instances of an Oracle RAC database are required for media recovery. Because of this, if you archive to a file and you do not use a cluster file system, or some other means to provide shared file systems, then you require a method of accessing the archive logs from all nodes on which the cluster database has instances.
- By default, all database files are migrated to Oracle Managed Files (OMF). This feature simplifies tablespace creation, ensures data file location consistency and compliance with Oracle Flexible Architecture (OFA) rules, and reduces human error with data file management.

See Also:

[Oracle Database 2 Day + Real Application Clusters Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/adminrac.htm#TDPRC217) for information about redo logs and redo threads

## C.2 Converting to Oracle RAC and Oracle RAC One Node Using DBCA

You can use Oracle Database Configuration Assistant (DBCA) to convert from single-instance Oracle databases to Oracle RAC or Oracle RAC One Node databases. DBCA automates the configuration of the control file attributes, creates the undo tablespaces and the redo logs, and creates the initialization parameter file entries for cluster-enabled environments. DBCA also configures Oracle Net Services, Oracle Clusterware resources, and the configuration for Oracle RAC database management for use by Oracle Enterprise Manager or the Server Control utility (SRVCTL).

Before you use DBCA to convert a single-instance database to an Oracle RAC or an Oracle RAC One Node database, ensure that your system meets the following conditions:

- Your system uses supported hardware and operating system software. Your system is configured properly to support an Oracle RAC database.
- The nodes have access to shared storage; either Oracle Cluster File System for Windows (OCFS for Windows) or Oracle ASM is available and accessible from all nodes.
- Your applications have no design characteristics that preclude their use with cluster database processing.

If your platform supports a cluster file system, then you can use it for Oracle RAC. You can also convert to Oracle RAC and use a nonshared file system. In either case, Oracle strongly recommends that you use Oracle Universal Installer (OUI) to perform an Oracle Database 11g release 2 (11.2) installation that sets up the Oracle home and inventory in an identical location on each of the selected nodes in your cluster.

This section describes the following scenarios:

- Converting Oracle Database 11g Installations to Oracle RAC Using DBCA
- Converting Single Instance on a Cluster to Oracle RAC One Node Using DBCA
- Converting Single Instance on a Cluster to Oracle RAC Using DBCA
- Converting an Oracle RAC One Node Database to an Oracle RAC Database

### C.2.1 Converting Oracle Database 11g Installations to Oracle RAC Using DBCA

To convert from a single-instance Oracle Database that is on a nonclustered computer to Oracle RAC, perform the procedures described in the following sections, and in the order shown:

- Use DBCA to Create an Image of the Single-Instance Database
- Complete the Oracle Clusterware Installation
- Validate the Cluster
- Copy the Preconfigured Database Image
- Install Oracle Database 11g Software with Oracle RAC

#### C.2.1.1 Use DBCA to Create an Image of the Single-Instance Database

Use DBCA to create a preconfigured image of your single-instance database by using the following procedure:

1. Go to the `bin` directory in `%ORACLE_HOME%`, and start DBCA.
2. At the Welcome page, click Next.
3. On the Operations page, select Manage Templates, and click Next.
4. On the Template Management page, select Create a database template and From an existing database (structure as well as data), and click Next.
5. On the Source Database page, select the database name in the Database instance list, and click Next.
6. On the Template Properties page, enter a name for your template in the Name field. Oracle recommends that you use the database name.
	By default, the template files are generated in the directory `%ORACLE_HOME%` `\assistants\dbca\templates`. You can enter a description of the file in the Description field and change the template file location in the Template data file field.
	When you have completed the entries, click Next.
7. On the Location of Database Related Files page, select Maintain the file locations, so that you can restore the database to the current directory structure, and click Finish.

DBCA generates two files: a database structure file (`template_name``.dbc`), and a database preconfigured image file (`template_name``.dfb`).

#### C.2.1.2 Complete the Oracle Clusterware Installation

Complete the installation of Oracle Clusterware, as described in [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for your platform.

#### C.2.1.3 Validate the Cluster

Validate the cluster configuration using Cluster Verification Utility (CVU). See [Section 1.6, "Confirming Cluster Readiness Using Cluster Verification Utility"](chklist.md) for instructions on how to use CVU.

#### C.2.1.4 Copy the Preconfigured Database Image

Copy the preconfigured database image. This includes copying the database structure `*.dbc` file and the database preconfigured image `*.dfb` file that DBCA created in Section C.2.1.1, "Use DBCA to Create an Image of the Single-Instance Database" to a temporary location on the node in the cluster from which you plan to run DBCA.

#### C.2.1.5 Install Oracle Database 11g Software with Oracle RAC

1. Run OUI to perform an Oracle Database installation with Oracle RAC.
2. Select Cluster Installation Mode on the Specify Hardware Cluster Installation page of OUI, and select the nodes to include in your Oracle RAC database.
3. On the OUI Database Configuration Types page, select the Advanced installation type.
	After installing the Oracle Database software, OUI runs postinstallation configuration tools, such as Oracle Net Configuration Assistant (NETCA), DBCA, and so on.
4. On the DBCA Template Selection page, use the template that you copied to a temporary location in Section C.2.1.4, "Copy the Preconfigured Database Image." Use the browse option to select the template location.
	Select the option that you want to deploy. Your choices are the following: Oracle RAC database; Oracle RAC One Node database; or Oracle single instance database.
5. After creating the Oracle RAC database, DBCA displays the Password Management page on which you must change the passwords for database users who have SYSDBA and SYSOPER privileges. When DBCA exits, the conversion process is complete.

Note:

Raw devices are not supported with OUI or DBCA in Oracle Database 11g release 2 (11.2). To use raw storage for your database, you must follow the instructions in Section C.2.3.1.2, "Manual Conversion Procedure."

See Also:

- [Oracle Database Platform Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/win.112/e10845/external.htm#NTQRF130) for more information about configuring user roles
- [Chapter 3, "Creating Oracle Real Application Clusters Databases with Oracle Database Configuration Assistant"](dbcacrea.md) for more information about using DBCA

### C.2.2 Converting Single Instance on a Cluster to Oracle RAC One Node Using DBCA

Use DBCA to convert a single-instance Oracle Database to Oracle RAC One Node by using the following procedure:

1. Go to the directory `%ORACLE_HOME%\bin`.
2. Start DBCA:
	```
	C:\..\bin> dbca
	```
3. From the Welcome window, select Oracle Real Application Clusters database.
4. Use the template that you selected to deploy in Section C.2.1.5, "Install Oracle Database 11g Software with Oracle RAC."

### C.2.3 Converting Single Instance on a Cluster to Oracle RAC Using DBCA

There are three scenarios in which a single-instance database can exist on a server that is a node in a cluster:

- Scenario 1: The Oracle home for the single-instance database was installed on a cluster node and has Oracle RAC enabled. The steps to perform a conversion to Oracle RAC in this scenario are described in Section C.2.3.1, "Single-Instance Database an Oracle RAC-Enabled Home".
- Scenario 2: The Oracle home for the single-instance database was installed on a cluster node, but the Oracle RAC feature is disabled for this Oracle home. Refer to Section C.2.3.2, "Single-Instance Database Using an Oracle RAC-Disabled Home" for instructions on how to convert the database to Oracle RAC in this environment.
- Scenario 3: The Oracle home for the single-instance database was installed on only the local node in a cluster. This happens when you select the Local Installation option on the OUI Specify Hardware Cluster Installation page during the Oracle Database 11g release 2 (11.2) installation. The procedure to convert the single-instance database to Oracle RAC in this scenario is the same as that described in Section C.2.1, "Converting Oracle Database 11g Installations to Oracle RAC Using DBCA." In the last step, "Install Oracle Database 11g Software with Oracle RAC", make sure that you select a new Oracle home, not the one from which the single-instance database is running.

#### C.2.3.1 Single-Instance Database an Oracle RAC-Enabled Home

Perform the following procedures to convert a single-instance database on a cluster node running from an Oracle home that has the Oracle RAC option enabled.

1. Use DBCA to create a preconfigured image of your single-instance database as described in Section C.2.1.1, "Use DBCA to Create an Image of the Single-Instance Database." To perform the conversion manually, shut down the single-instance database.
2. To add nodes to your cluster, follow the instructions to add and connect these nodes to the cluster as described in "Adding a Node to a Cluster on Windows Systems" in the [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/adddelclusterware.htm#CWADD90996). Ensure that all nodes can access the shared storage used by Oracle Clusterware and Oracle RAC.
3. From the existing Oracle home, extend this home to the new nodes using the procedure "Adding Oracle RAC to Nodes with Oracle Clusterware Installed" as described in the [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/adddelwin.htm#RACAD8196).
4. From a newly added node, configure the listeners on the additional nodes using Oracle Net Configuration Assistant (NETCA). Choose the same port number and protocol that you used on the existing node. If NETCA displays the existing node in the node list page, then do not select this node, because the listener is already configured on it.
5. Convert the database using one of the following procedures:
	- Automated Conversion Procedure Using DBCA
		- Manual Conversion Procedure

##### C.2.3.1.1 Automated Conversion Procedure Using DBCA

If you used DBCA to create a preconfigured image of your single-instance database as described in Section C.2.1.1, "Use DBCA to Create an Image of the Single-Instance Database," then perform the following steps to complete the conversion:

1. Start DBCA from the initial node. Select the names of the nodes to include as part of your cluster database. On the Template Selection page, select the preconfigured template that you created. Enter the database name and respond to the remaining DBCA prompts.
2. Specify the shared storage location for the Oracle Database data files. To use raw devices for the data files, you cannot use DBCA. Instead, follow the steps documented in Section C.2.3.1.2, "Manual Conversion Procedure."

After creating the Oracle RAC database, DBCA displays the Password Management page on which you must change the passwords for the database users who have SYSDBA and SYSOPER privileges. When DBCA exits, the conversion process is complete.

##### C.2.3.1.2 Manual Conversion Procedure

If you did not use DBCA to create a preconfigured image of your single-instance database as described in Section C.2.1.1, "Use DBCA to Create an Image of the Single-Instance Database," then perform the following steps to complete the conversion:

1. Create the OFA directory structure on each of the nodes that you have added.
	See Also:
	[Section D.2, "Directory Structures for Oracle RAC"](apa.md) for more information about OFA
2. If you are converting single-instance database files on a file system to raw devices, then copy the database data files, control files, redo logs, and SPFILE to their corresponding raw devices using the `ocopy` command. Otherwise, continue to the next step.
3. Re-create the control files by running the `CREATE CONTROLFILE` SQL statement with the `REUSE` keyword and specify `MAXINSTANCES` and `MAXLOGFILES`, and so on, as needed for your Oracle RAC configuration. The `MAXINSTANCES` recommended default is 32.
4. Shut down the database instance.
5. If your single-instance database was using an SPFILE, then create a temporary parameter file (PFILE) from the SPFILE using the following SQL statement:
	```
	CREATE PFILE='pfile_name' from spfile='spfile_name'
	```
6. Set the `CLUSTER_DATABASE` parameter to `TRUE`, set the `INSTANCE_NUMBER` parameter to a unique value for each instance, using the `sid``.``parameter` `=` `value` syntax.
	If you optimized memory usage on your single-instance database, then adjust the size of the System Global Area (SGA) to avoid swapping and paging when you convert to Oracle RAC. You should make this adjustment because Oracle RAC requires about 350 bytes for each buffer to accommodate the Global Cache Service (GCS). For example, if you have 10,000 buffers, then Oracle RAC requires about 350 multiplied by 10,000 bytes more memory. Therefore, adjust the size of the SGA by changing the `DB_CACHE_SIZE` and `DB_nK_CACHE_SIZE` parameters accordingly.
7. Start the database instance using the PFILE created in Step [^2].
8. If your single-instance database was using automatic undo management, then create an undo tablespace for each additional instance using the `CREATE UNDO TABLESPACE` SQL statement. If you are using raw devices, then ensure that the data file for the undo tablespace is on the raw device.
9. Create redo threads that have at least two redo logs for each additional instance. If you are using raw devices, then ensure that the redo log files are on raw devices. Enable the new redo threads by using an `ALTER DATABASE` SQL statement. Then, shut down the database instance.
10. Copy the Oracle password file from the initial node, or from the node on which you are working, to the corresponding location on the additional nodes on which the cluster database will have an instance. Replace the `ORACLE_SID` name in each password file appropriately for each additional instance.
11. Set the `REMOTE_LISTENER` parameter to the single client access name (SCAN) and port.
12. Configure the net service entries for the database and instances, and address entries for the `LOCAL_LISTENER` for each instance and for the `REMOTE_LISTENER` in the `tnsnames.ora` file. When you have done this, copy the `tnsnames.ora` file to all nodes.
13. Create the SPFILE from the PFILE using the procedures in [Section 5.5, "Migrating to an SPFILE in Oracle RAC Environments."](params.md) If you are not using Oracle ASM or a cluster file system, then ensure that the SPFILE is on a raw device that is accessible from every node in the cluster.
14. Create the `Oracle_home` `\database\init` `sid``.ora` file that contains the following entry, where `spfile_path_name` is the complete path name of the SPFILE:
	```
	spfile='spfile_path_name'
	```
15. On the local node, use SQL\*Plus to run `catclust.sql`. This script creates the dictionary views needed for Oracle RAC databases. For example:
	```
	SQL> start %ORACLE_HOME%\rdbms\admin\catclust.sql
	```
16. Add the configuration for the Oracle RAC or Oracle RAC One Node database and its instance-to-node mapping using SRVCTL.
	1. To add the configuration of an Oracle RAC database, use the following commands:
		```
		srvctl add database -d db_name -o Oracle_home -p spfile_path_name
		srvctl add instance -d db_name -i inst1_name -n node1_name
		srvctl add instance -d db_name -i inst2_name -n node2_name
		...
		```
		2. To add the configuration of an Oracle RAC One Node database, use the following command:
		```
		srvctl add database -d db_name -c RACONENODE -o Oracle_home
		-p spfile_path_name
		```
17. Start the Oracle RAC or Oracle RAC One Node database using SRVCTL:
	```
	C:\> srvctl start database -d db_name
	```

After starting the database with SRVCTL, your conversion process is complete. You can run the following SQL statement to see the status of all the instances in your Oracle RAC database:

```
SQL> select * from v$active_instances;
```

#### C.2.3.2 Single-Instance Database Using an Oracle RAC-Disabled Home

You can create a single-instance database on a cluster using an Oracle home with the Oracle RAC option disabled. To create an Oracle home on a cluster with Oracle RAC disabled, you can select local and non-cluster on the Node Selection Page of Oracle Universal Installer (OUI) when installing the Oracle Database software. You can also performed a one-node cluster (with Oracle RAC) installation, but later disable the Oracle RAC option.

Perform the following procedures to convert this type of single-instance database to an Oracle RAC or Oracle RAC One Node database:

1. Use DBCA to create a preconfigured image of your single-instance database as described in Section C.2.1.1, "Use DBCA to Create an Image of the Single-Instance Database." To perform the conversion manually, shut down the single-instance database.
2. Go to the `bin` subdirectory in the Oracle home.
3. Enable the Oracle RAC option by renaming the `orarac11.dll.dbl` file using the following command:
	```
	C:\..\bin> copy /Y orarac11.dll.dbl orarac11.dll
	```
4. Continue with step [^1] in Section C.2.3.1, "Single-Instance Database an Oracle RAC-Enabled Home."

### C.2.4 Converting an Oracle RAC One Node Database to an Oracle RAC Database

You can convert an Oracle RAC One Node database to an Oracle RAC database by logging in as the Oracle RAC One Node database owner and entering the following SRVCTL command:

```
C:\> srvctl convert database -c RAC
```

Caution:

By default, any named user may create a server pool. To restrict the operating system users that have this privilege, Oracle strongly recommends that you add specific users to the CRS Administrators list. See [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD91105) for more information about adding users to the CRS Administrators list.

After you run this command, you must create server pools for each database service, in addition to the database server pool. The values for `SERVER_NAMES` for the server pools used by the database services must be set to the node that you converted from an Oracle RAC One Node to an Oracle RAC node. You can use the CRSCTL utility or Oracle Enterprise Manager to create and configure the server pools.

Converting an administrator-managed Oracle RAC One Node database to an Oracle RAC database configures all database services so that the single instance is the preferred instance for that service. After you convert the database, you can add instances to your database by using the SRVCTL `add` `instance` command.

Converting a policy-managed Oracle RAC One Node database to an Oracle RAC database sets all database services to UNIFORM cardinality. It also results in reusing the server pool in which the database currently runs. The conversion reconfigures the database to run on all of the nodes in the server pool. The command does not start any additional instances but executing the SRVCTL `start` `database` command starts the database on all of the nodes in the server pool.

See Also:

The [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/toc.htm) for more information about policy-managed and administrator-managed databases, server pools, and database services.

## C.3 Preparing to Convert with rconfig and Oracle Enterprise Manager

You can use `rconfig`, or Oracle Enterprise Manager to assist with converting a single-instance database installation to an Oracle RAC database. The first of these, `rconfig`, is a command-line utility. Oracle Enterprise Manager Grid Control database administration option, Convert to Cluster Database, provides a GUI-based conversion tool. The following sections describe how to use these conversion tools:

- Prerequisites for Converting to Oracle RAC Databases
- Configuration Changes During Oracle RAC Conversion Using rconfig
- Converting Databases to Oracle RAC Using rconfig or Enterprise Manager
- Converting Databases to Oracle RAC Using Oracle Enterprise Manager

Note:

Before you start the conversion, back up your existing database; you should take a backup of your database before starting any major change.

### C.3.1 Prerequisites for Converting to Oracle RAC Databases

Before you convert a single-instance database to an Oracle RAC database, ensure that the following conditions are met for each cluster node that you intend to make an Oracle RAC database node:

- Oracle Clusterware 11g release 2 (11.2) is installed, configured, and running.
- Oracle RAC 11g release 2 (11.2) software is installed.
- The Oracle software has the Oracle RAC option enabled.
- Shared storage, either Oracle Cluster File System or Oracle ASM, is available and accessible from all nodes.
- User equivalence exists for the `oracle` account, or the user account used to install the Oracle software.
- If you intend to use Oracle Enterprise Manager, then the Oracle Management Agent on each node is configured and running, and is configured with cluster and host information.
- You have backed up your existing database.

Note:

You must use clustered Oracle ASM instances for Oracle RAC databases. Oracle ASM is installed with the Oracle Grid Infrastructure software.

### C.3.2 Configuration Changes During Oracle RAC Conversion Using rconfig

The following changes occur when you convert a single-instance database to Oracle RAC using the `rconfig` utility"

- During the conversion, `rconfig` places the target Oracle RAC database into archive log mode, and enables archiving for the database. If you do not plan to use archive log space, then you can disable archive logging after the conversion has completed.
- For the Shared Storage Type value, if you enter CFS, and you use a cluster file system for your single-instance database storage, then `rconfig` converts the environment to use Oracle Managed Files (OMF) for database storage, and places the data files in a subdirectory located under the shared storage location.
- During the conversion, `rconfig` moves database files to a specified shared location, and configures them using OMF.
	To avoid using OMF with your converted database, the single-instance database files must be located in a shared file system, and you must indicate that `rconfig` should not move the files.

### C.3.3 Converting Databases to Oracle RAC Using rconfig or Enterprise Manager

The following list describes scenarios for converting a single-instance Oracle database to an Oracle RAC database:

- Converting a single-instance Oracle Database 11g release 2 (11.2) database to an Oracle RAC 11g release 2 (11.2) database, running out of the same Oracle home and using the same data files as the single-instance database.
	In this scenario, run the `rconfig` utility from the Oracle RAC database home, or use the Convert to RAC option on the single-instance database target of Oracle Enterprise Manager Grid Control.
- Converting a single-instance database that uses a release of Oracle Database earlier than Oracle Database 11g release 2 (11.2) to an Oracle RAC 11g release 2 (11.2) database, running out of the same Oracle home and using the same data files as the single-instance database
	In this scenario, use OUI and DBUA to update the single-instance database to Oracle Database 11g release 2 (11.2). Then, use `rconfig` or the Oracle Enterprise Manager Convert to RAC option, as described in the preceding scenario.
- Converting a single-instance Oracle Database 11g release 2 (11.2) to an Oracle RAC 11g release 2 (11.2) database, running out of a different Oracle home and using the same data files as the single-instance database.
	In this scenario, run the `rconfig` utility in the target database home, or use the Convert to RAC option in the single-instance database target of Oracle Enterprise Manager Grid Control. Provide the file storage location when prompted.
- Converting a single-instance Oracle Database 11g release 2 (11.2) database to an Oracle RAC 11g release 2 (11.2) database, running out of a different Oracle home, and where the host on which the single-instance database runs is not a node used by the Oracle RAC database.
	In this scenario, create a clone image of the single-instance database, and move the clone image to a host that is one of the nodes used by the Oracle RAC database. Then, use `rconfig` or the Oracle Enterprise Manager Convert to RAC option, as described in the preceding scenario.

### C.3.4 Converting Databases to Oracle RAC Using Oracle Enterprise Manager

You can use Oracle Enterprise Manager Grid Control to convert a single-instance database to an Oracle RAC database. To use this feature, complete the following steps:

See Also:

[Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm) for information about upgrading existing Oracle Database installations

1. Log in to Grid Control. From the Grid Control Home page, click the Targets tab.
2. On the Targets page, click the Databases secondary tab, and click the link in the Names column of the database to convert to Oracle RAC.
3. On the Database Instance Home page, click the Change Database secondary tab.
4. On the Administration page, in the Database Administration Change Database section, click Convert to Cluster Database.
5. Log in as the database user SYS with SYSDBA privileges to the database you want to convert, and click Next.
6. On the Convert to Cluster Database: Cluster Credentials page, provide a user name and password for the `oracle` user and password of the target database to be converted. If the target database is using Oracle ASM, then also provide the SYSASM user and password, and click Next.
7. On the Hosts page, select the host nodes in the cluster to be cluster members in the installed Oracle RAC database. When you have completed your selection, click Next.
8. On the Convert to Database: Options page, select whether you want to use the existing listener and port number, or specify a new listener and port number for the cluster. Also provide a prefix for cluster database instances on the cluster.
	When you have finished entering information, click Next, or click Help if you need assistance in deciding how to enter information.
9. On the Convert to Cluster Database: Shared Storage page, either select the option to use your existing shared storage area, or select the option to have your database files copied to a new shared storage location. Also, decide if you want to use your existing fast recovery area, or copy your recovery files to a new fast recovery area using files managed by Oracle Database.
	If you use Oracle ASM, then Oracle recommends that you place the data files and the recovery files in separate failure groups. A failure group is defined by shared hardware, such as a controller shared between two disks, or two disks that are on the same spindle. If two disks share hardware that could fail, making both disks unavailable, then theses disks are said to be in the same failure group. If you do not use Oracle ASM, then Oracle recommends that the data files and the recovery files are stored in separate locations, as with separate Oracle ASM failure groups, so that a hardware failure does not affect availability.
	See Also:
	[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmdiskgrps.htm#OSTMG10046) for more information about failure groups
	When you have finished entering information, click Next, or click Help if you need assistance in deciding how to enter information.
10. On the Convert to Cluster Database: Review page, review the options you have selected. Click Submit Job to proceed with the conversion. To change any of the options you have selected, click Back. To cancel the conversion, click Cancel.
11. On the Confirmation page, click View Job to check the status of the conversion.

## C.4 Converting Databases to Oracle RAC Using rconfig

You can use the command-line utility `rconfig` to convert a single-instance database to an Oracle RAC database, or to convert it to an Oracle RAC One Node database, depending on the values you provide in the `ConvertToRAC.xml` file. To use this feature, complete the following steps:

See Also:

[Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm) for information about upgrading existing Oracle Database installations

1. As the `oracle` user, go to the directory `%ORACLE_HOME%` `\assistants\rconfig\sampleXMLs`, and open the file `ConvertToRAC.xml` using a text editor.
2. Review the `ConvertToRAC.xml` file, and modify the parameters as required for your system. The XML sample file contains comments that provide instructions for how to configure the file.
	Caution:
	Set the convert option `Convert verify="ONLY"` to perform a test conversion to ensure that a conversion can be completed successfully.
	When you have finished modifying parameters, save the file with the a name of the format `filename``.xml`. Make a note of the name you select.
3. Go to the directory %ORACLE\_HOME% `\bin`, and use the following command to run `rconfig`, where `input.xml` is the name of the XML input file you configured in Step [^3]:
	```
	C:\..\bin> rconfig input.xml
	```
	For example, if you create an input XML file called `convert.xml`, then you would use the following command
	```
	C:\...\bin> rconfig.bat convert.xml
	```

Note:

The `Convert verify` option in the `ConvertToRAC.xml` file has three options:
- `Convert verify="YES"`: `rconfig` performs checks to ensure that the prerequisites for single-instance to Oracle RAC conversion have been met before it starts conversion
- `Convert verify="NO"`: `rconfig` does not perform prerequisite checks, and starts conversion
- `Convert verify="ONLY"` `rconfig` only performs prerequisite checks; it does not start conversion after completing prerequisite checks

If performing the conversion fails, then use the following procedure to recover and reattempt the conversion:

1. Attempt to delete the database using the DBCA delete database option.
2. Restore the source database.
3. Review the conversion log, and fix any problems reported by `rconfig` that may have caused the conversion failure. The `rconfig` log files are under the `rconfig` directory in `%ORACLE_BASE%\cfgtoollogs`.
4. Reattempt the conversion.

## C.5 Example of rconfig XML Input Files for ConvertToRAC

The following are two examples of an XML `ConvertToRAC` input file for the `rconfig` utility. Example C-1 is an XML input file to convert a single-instance database with Oracle ASM to a policy-managed Oracle RAC database (using server pools) on Oracle ASM storage. Example C-2 is an XML input file to convert a single-instance database with Oracle ASM to an administrator-managed Oracle RAC database.

Example C-1 Example rconfig ConvertToRAC XML file for Policy-Managed Databases

```
<?xml version="1.0" encoding="UTF-8"?>
<n:RConfig xmlns:n="http://www.oracle.com/rconfig/"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://www.oracle.com/rconfig/">
    <n:ConvertToRAC>   
<!-- Verify does a precheck to ensure all pre-requisites are met, before the
conversion is attempted. Allowable values are: YES|NO|ONLY -->
        <n:Convert verify="YES">
<!--Specify current OracleHome of non-rac database for SourceDBHome -->
              <n:SourceDBHome>C:\app\oracle\product\11.2.0\db_1</n:SourceDBHome>
<!--Specify OracleHome where the rac database should be configured. It can be same
as SourceDBHome -->
              <n:TargetDBHome>C:\app\oracle\product\11.2.0\db_1</n:TargetDBHome>
<!--Specify SID of non-rac database and credential. User with sysdba role is
required to perform conversion -->
              <n:SourceDBInfo SID="sales">
                <n:Credentials>
                  <n:User>sys</n:User>
                  <n:Password>oracle</n:Password>
                  <n:Role>sysdba</n:Role>
                </n:Credentials>
              </n:SourceDBInfo>
<!--Specify the list of existing or new server pools which are used by the Policy
Managed Cluster Database. -->
              <n:ServerPoolList>
                <n:ExistingServerPool name="custom"/>
                <n:NewServerPool name="newpool" cardinality="2"/>
              </n:ServerPoolList>
<!--Specify RacOneNode along with servicename to convert database to RACOne Node
-->
 <!--n:RacOneNode  servicename="salesrac1service"/-->
<!--InstancePrefix is not required for Policy Managed database. If specified, it
will be ignored. Instance names are generated automatically based on db_unique_
name for Policy Managed dababase.-->
<!-- Listener details are no longer needed starting 11.2. Database is registered
with default listener and SCAN listener running from Oracle Grid Infrastructure
home. -->
<!--Specify the type of storage to be used by rac database. Allowable values are
CFS|ASM. The non-rac database should have same storage type. ASM credentials are
not needed for conversion. -->
              <n:SharedStorage type="ASM">
<!--Specify Database Area Location to be configured for rac database.If this field
is left empty, current storage will be used for rac database. For CFS, this field
will have directory path. -->
                <n:TargetDatabaseArea>+ASMDG</n:TargetDatabaseArea>
<!--Specify Fast Recovery Area to be configured for rac database. If this field
is left empty, current recovery area of non-rac database will be configured for
rac database. If current database is not using recovery Area, the resulting rac
database will not have a recovery area. -->
                <n:TargetFlashRecoveryArea>+ASMDG</n:TargetFlashRecoveryArea>
              </n:SharedStorage>
        </n:Convert>
    </n:ConvertToRAC>
</n:RConfig>
```

Example C-2 Example rconfig ConvertToRAC XML file for Administrator-Managed Databases

```
<?xml version="1.0" encoding="UTF-8"?>
<n:RConfig xmlns:n="http://www.oracle.com/rconfig/"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://www.oracle.com/rconfig rconfig.xsd">
    <n:ConvertToRAC>   
<!-- Verify does a precheck to ensure all pre-requisites are met, before the
conversion is attempted. Allowable values are: YES|NO|ONLY -->
        <n:Convert verify="YES">
<!--Specify current OracleHome of non-rac database for SourceDBHome -->
              <n:SourceDBHome>C:\app\oracle\product\11.2.0\db_1</n:SourceDBHome>
<!--Specify OracleHome where the rac database should be configured. It can be same
as SourceDBHome -->
              <n:TargetDBHome>C:\app\oracle\product\11.2.0\db_1</n:TargetDBHome>
<!--Specify SID of non-rac database and credential. User with sysdba role is
required to perform conversion -->
              <n:SourceDBInfo SID="sales">
                <n:Credentials>
                  <n:User>sys</n:User>
                  <n:Password>oracle</n:Password>
                  <n:Role>sysdba</n:Role>
                </n:Credentials>
              </n:SourceDBInfo>
<!--Specify the list of nodes that should have rac instances running for the Admin
Managed Cluster Database. LocalNode should be the first node in this nodelist. -->
              <n:NodeList>        
                <n:Node name="node1"/>
                <n:Node name="node2"/>
              </n:NodeList>
<!--Specify RacOneNode along with servicename to convert database to RACOne Node
-->
<!--n:RacOneNode  servicename="salesrac1service"/-->
<!--Instance Prefix tag is optional starting with 11.2. If left empty, it is
derived from db_unique_name.-->
              <n:InstancePrefix>sales</n:InstancePrefix>
<!-- Listener details are no longer needed starting 11.2. Database is registered
with default listener and SCAN listener running from Oracle Grid Infrastructure
home. -->
<!--Specify the type of storage to be used by rac database. Allowable values are
CFS|ASM. The non-rac database should have same storage type. ASM credentials are
no needed for conversion. -->
              <n:SharedStorage type="ASM">
<!--Specify Database Area Location to be configured for rac database.If this field
is left empty, current storage will be used for rac database. For CFS, this field
will have directory path. -->
                <n:TargetDatabaseArea>+ASMDG</n:TargetDatabaseArea>
<!--Specify Fast Recovery Area to be configured for rac database. If this field
is left empty, current recovery area of non-rac database will be configured for
rac database. If current database is not using recovery Area, the resulting rac
database will not have a recovery area. -->
                <n:TargetFlashRecoveryArea>+ASMDG</n:TargetFlashRecoveryArea>
              </n:SharedStorage>
        </n:Convert>
    </n:ConvertToRAC>
</n:RConfig>
```

## C.6 Postconversion Steps

After completing the conversion, note the following recommendations for Oracle RAC environments, as described in the Oracle RAC documentation:

- Follow the recommendations for using load balancing and transparent application failover, as described in [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/hafeats.htm#RACAD076).
- Use locally managed tablespaces instead of dictionary managed tablespaces to reduce contention and manage sequences in Oracle RAC as described in [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/design.htm#RACAD755).
- Follow the guidelines for using automatic segment space management as described in [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/storage.htm#RACAD802).

The buffer cache and shared pool capacity requirements in Oracle RAC are slightly greater than the requirements for single-instance Oracle databases. Therefore, you should increase the size of the buffer cache by about 10%, and the size of the shared pool by about 15%.

[^1]: To add nodes to your cluster, follow the instructions to add and connect these nodes to the cluster as described in "Adding a Node to a Cluster on Windows Systems" in the [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/adddelclusterware.htm#CWADD90996). Ensure that all nodes can access the shared storage used by Oracle Clusterware and Oracle RAC.

[^undefined]: From the existing Oracle home, extend this home to the new nodes using the procedure "Adding Oracle RAC to Nodes with Oracle Clusterware Installed" as described in the [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/adddelwin.htm#RACAD8196).

[^undefined]: From a newly added node, configure the listeners on the additional nodes using Oracle Net Configuration Assistant (NETCA). Choose the same port number and protocol that you used on the existing node. If NETCA displays the existing node in the node list page, then do not select this node, because the listener is already configured on it.

[^undefined]: Convert the database using one of the following procedures:

- Automated Conversion Procedure Using DBCA
- Manual Conversion Procedure

[^2]: If your single-instance database was using an SPFILE, then create a temporary parameter file (PFILE) from the SPFILE using the following SQL statement:

```
CREATE PFILE='pfile_name' from spfile='spfile_name'
```

[^undefined]: Set the `CLUSTER_DATABASE` parameter to `TRUE`, set the `INSTANCE_NUMBER` parameter to a unique value for each instance, using the `sid``.``parameter` `=` `value` syntax.

If you optimized memory usage on your single-instance database, then adjust the size of the System Global Area (SGA) to avoid swapping and paging when you convert to Oracle RAC. You should make this adjustment because Oracle RAC requires about 350 bytes for each buffer to accommodate the Global Cache Service (GCS). For example, if you have 10,000 buffers, then Oracle RAC requires about 350 multiplied by 10,000 bytes more memory. Therefore, adjust the size of the SGA by changing the `DB_CACHE_SIZE` and `DB_nK_CACHE_SIZE` parameters accordingly.

[^undefined]: Start the database instance using the PFILE created in Step 5.

[^undefined]: If your single-instance database was using automatic undo management, then create an undo tablespace for each additional instance using the `CREATE UNDO TABLESPACE` SQL statement. If you are using raw devices, then ensure that the data file for the undo tablespace is on the raw device.

[^undefined]: Create redo threads that have at least two redo logs for each additional instance. If you are using raw devices, then ensure that the redo log files are on raw devices. Enable the new redo threads by using an `ALTER DATABASE` SQL statement. Then, shut down the database instance.

[^undefined]: Copy the Oracle password file from the initial node, or from the node on which you are working, to the corresponding location on the additional nodes on which the cluster database will have an instance. Replace the `ORACLE_SID` name in each password file appropriately for each additional instance.

[^undefined]: Set the `REMOTE_LISTENER` parameter to the single client access name (SCAN) and port.

[^undefined]: Configure the net service entries for the database and instances, and address entries for the `LOCAL_LISTENER` for each instance and for the `REMOTE_LISTENER` in the `tnsnames.ora` file. When you have done this, copy the `tnsnames.ora` file to all nodes.

[^undefined]: Create the SPFILE from the PFILE using the procedures in [Section 5.5, "Migrating to an SPFILE in Oracle RAC Environments."](params.md) If you are not using Oracle ASM or a cluster file system, then ensure that the SPFILE is on a raw device that is accessible from every node in the cluster.

[^undefined]: Create the `Oracle_home` `\database\init` `sid``.ora` file that contains the following entry, where `spfile_path_name` is the complete path name of the SPFILE:

```
spfile='spfile_path_name'
```

[^undefined]: On the local node, use SQL\*Plus to run `catclust.sql`. This script creates the dictionary views needed for Oracle RAC databases. For example:

```
SQL> start %ORACLE_HOME%\rdbms\admin\catclust.sql
```

[^undefined]: Add the configuration for the Oracle RAC or Oracle RAC One Node database and its instance-to-node mapping using SRVCTL.

1. To add the configuration of an Oracle RAC database, use the following commands:
	```
	srvctl add database -d db_name -o Oracle_home -p spfile_path_name
	srvctl add instance -d db_name -i inst1_name -n node1_name
	srvctl add instance -d db_name -i inst2_name -n node2_name
	...
	```
2. To add the configuration of an Oracle RAC One Node database, use the following command:
	```
	srvctl add database -d db_name -c RACONENODE -o Oracle_home
	-p spfile_path_name
	```

[^undefined]: Start the Oracle RAC or Oracle RAC One Node database using SRVCTL:

```
C:\> srvctl start database -d db_name
```

[^3]: Review the `ConvertToRAC.xml` file, and modify the parameters as required for your system. The XML sample file contains comments that provide instructions for how to configure the file.

Caution:

Set the convert option `Convert verify="ONLY"` to perform a test conversion to ensure that a conversion can be completed successfully.

When you have finished modifying parameters, save the file with the a name of the format `filename``.xml`. Make a note of the name you select.

[^undefined]: Go to the directory %ORACLE\_HOME% `\bin`, and use the following command to run `rconfig`, where `input.xml` is the name of the XML input file you configured in Step 2:

```
C:\..\bin> rconfig input.xml
```

For example, if you create an input XML file called `convert.xml`, then you would use the following command

```
C:\...\bin> rconfig.bat convert.xml
```