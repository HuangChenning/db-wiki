---
title: Converting to Oracle RAC and Oracle RAC One Node from Single-Instance Oracle Databases
book: Real Application Clusters Installation Guide for Linux and UNIX
doc_id: E41962-05
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41962/cvrt2rac.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-linux-and-unix
---

## C Converting to Oracle RAC and Oracle RAC One Node from Single-Instance Oracle Databases

This appendix describes the procedures for converting from Oracle Database 11g release 2 (11.2) single-instance databases to Oracle Real Application Clusters (Oracle RAC) and Oracle RAC One Node databases. This appendix contains the following topics:

If you are upgrading from Oracle Parallel Server to Oracle RAC, or from an earlier version of Oracle RAC, then use Oracle Database Upgrade Assistant (DBUA).

The procedures in this chapter assume that your original single-instance database and the target Oracle RAC database are using the same release and running on the same platform.

Note:

You must use clustered Oracle ASM instances for Oracle RAC databases.

See Also:

[Oracle Database Licensing Information](https://docs.oracle.com/cd/E11882_01/license.112/e47877/toc.htm) for compliance requirements that apply to the license you have purchased

## C.1 Administrative Issues for Converting Databases to Oracle RAC

Note the following administrative considerations before converting single-instance databases to Oracle RAC:

- Backup procedures should be available before converting from a single-instance Oracle Database to Oracle RAC.
- For archiving with Oracle RAC environments, the archive file format requires a thread number.
- The archived logs from all instances of an Oracle RAC database are required for media recovery. Because of this, if you archive to a file and you do not use a cluster file system, or some other means to provide shared file systems, then you require a method of accessing the archive logs from all nodes on which the cluster database has instances.
- By default, all database files are migrated to Oracle-Managed Files (OMF). This feature simplifies tablespace creation, ensures datafile location consistency and compliance with OFA rules, and reduces human error with data file management.

## C.2 Converting to Oracle RAC and Oracle RAC One Node with DBCA

You can use Database Configuration Assistant (DBCA) to convert from single-instance Oracle databases to Oracle RAC, or Oracle RAC One Node. DBCA automates the configuration of the control file attributes, creates the undo tablespaces and the redo logs, and makes the initialization parameter file entries for cluster-enabled environments. DBCA also configures Oracle Net Services, Oracle Clusterware resources, and the configuration for Oracle RAC database management for use by Oracle Enterprise Manager or the SRVCTL utility (SRVCTL).

Before you use DBCA to convert a single-instance database to an Oracle RAC or an Oracle RAC One Node database, ensure that your system meets the following conditions:

- It is a supported hardware and operating system software configuration.
- It has shared storage: either Oracle Cluster File System or Oracle ASM is available and accessible from all nodes. On Linux on POWER systems, ensure that GPFS is available and accessible from all nodes.
- Your applications have no design characteristics that preclude their use with cluster database processing.

If your platform supports a cluster file system, then you can use it for Oracle RAC. You can also convert to Oracle RAC and use a non-shared file system. In either case, Oracle strongly recommends that you use Oracle Universal Installer (OUI) to perform an Oracle Database 11g release 2 (11.2) installation that sets up the Oracle home and inventory in an identical location on each of the selected nodes in your cluster.

This section describes the following scenarios:

- Converting Oracle Database 11g Installations to Oracle RAC Using DBCA
- Converting Single Instance on a Cluster to Oracle RAC Using DBCA

### C.2.1 Converting Oracle Database 11g Installations to Oracle RAC Using DBCA

To convert from a single-instance Oracle Database that is on a non-cluster computer to Oracle RAC, perform the procedures described in the following sections, and in the order shown:

- Back Up the Original Single-Instance Database
- Complete Oracle Clusterware Installation
- Validate the Cluster
- Copy the Preconfigured Database Image
- Install Oracle Database 11g Software with Oracle RAC

#### C.2.1.1 Back Up the Original Single-Instance Database

Use DBCA to create a preconfigured image of your single-instance database by using the following procedure:

1. Navigate to the `bin` directory in `$ORACLE_HOME`, and start DBCA.
2. At the Welcome page, click Next.
3. On the Operations page, select Manage Templates, and click Next.
4. On the Template Management page, select Create a database template and From an existing database (structure as well as data), and click Next.
5. On the Source Database page, select the database name in the Database instance list, and click Next.
6. On the Template Properties page, enter a name for your template in the Name field. Oracle recommends that you use the database name.
	By default, the template files are generated in the directory `ORACLE_HOME/assistants/dbca/templates` If you choose to do so, you can enter a description of the file in the Description field, and change the template file location in the Template data file field.
	When you have completed the entries, click Next.
7. On the Location of Database Related Files page, select Maintain the file locations, so that you can restore the database to the current directory structure, and click Finish.

DBCA generates two files: a database structure file (`template_name``.dbc`), and a database preconfigured image file (`template_name``.dfb`).

#### C.2.1.2 Complete Oracle Clusterware Installation

Complete Oracle Clusterware installation, as described in the [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN) for your platform.

#### C.2.1.3 Validate the Cluster

Validate the cluster configuration using the Cluster Verification Utility (CVU).

#### C.2.1.4 Copy the Preconfigured Database Image

Copy the preconfigured database image. This includes copying the database structure `*.dbc` file and the database preconfigured image `*.dfb` file that DBCA created in the previous procedure "Back Up the Original Single-Instance Database" to a temporary location on the node in the cluster from which you plan to run DBCA.

#### C.2.1.5 Install Oracle Database 11g Software with Oracle RAC

1. Run OUI to perform an Oracle Database installation with Oracle RAC.
2. Select Cluster Installation Mode on the Specify Hardware Cluster Installation page of OUI, and select the nodes to include in your Oracle RAC database.
3. On the OUI Database Configuration Types page, select the Advanced install type.
	After installing the Oracle Database software, OUI runs postinstallation configuration tools, such as Network Configuration Assistant (NETCA), DBCA, and so on.
4. On the DBCA Template Selection page, use the template that you copied to a temporary location in the "Copy the Preconfigured Database Image" procedure. Use the browse option to select the template location.
	Select the option that you want to deploy. Your choices are the following: Oracle RAC database; Oracle RAC One Node database; or Oracle single instance database.
5. If you selected raw storage on the OUI Storage Options page, then on the DBCA File Locations Tab on the Initialization Parameters page, replace the data files, control files, and log files, and so on, with the corresponding raw device files if you have not set up the `DBCA_RAW_CONFIG` environment variable. You must also replace default database files with raw devices on the Storage page.
	See Also:
	[Chapter 3, "Creating Oracle Real Application Clusters Databases with Database Configuration Assistant"](dbcacrea.md) for more details about DBCA
6. After creating the Oracle RAC database, DBCA displays the Password Management page on which you must change the passwords for database privileged users who have `SYSDBA` and `SYSOPER` roles. When DBCA exits, the conversion process is complete.

### C.2.2 Converting Single Instance on a Cluster to Oracle RAC One Node Using DBCA

Use DBCA to convert a single-instance Oracle Database to Oracle RAC One Node by using the following procedure:

1. Change directory to $ORACLE\_HOME/bin
2. Start DBCA:
	```
	$ dbca
	```
3. From the Welcome window, select Oracle Real Application Clusters database.
4. Use the template that you selected to deploy in Section C.2.1.5, "Install Oracle Database 11g Software with Oracle RAC."

### C.2.3 Converting Single Instance on a Cluster to Oracle RAC Using DBCA

There are three scenarios in which a single-instance database can exist on a cluster computer:

- Scenario 1: The Oracle home from which the single-instance database is running is cluster-installed. The steps to perform a conversion to Oracle RAC in this scenario are described in "Single Instance on a Cluster Running from a Cluster-Enabled Oracle Home".
- Scenario 2: The Oracle home from which the single-instance database is running is cluster-installed, but the Oracle RAC feature is disabled. Refer to "Single Instance on a Cluster Running from an Oracle RAC-Disabled Oracle Home" for instructions on how to convert the database to Oracle RAC in this environment.
- Scenario 3: The Oracle home from which the single-instance database is running is not cluster-installed. The procedure to convert the single-instance database to Oracle RAC in this scenario is described in "Single Instance on a Cluster Running from a Single-Instance Installed Oracle Home".

#### C.2.3.1 Single Instance on a Cluster Running from a Cluster-Enabled Oracle Home

Perform the following procedures to convert a single-instance database on a cluster running from a cluster-installed (Oracle Database 11g with Oracle RAC) Oracle home.

1. Use DBCA to create a preconfigured image of your single-instance database as described in the section "Back Up the Original Single-Instance Database". To perform the conversion manually, shut down the single-instance database.
2. To add nodes to your cluster, add and connect these nodes to the cluster as described in the [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN) for your platform. Ensure that all of these nodes can access the shared storage. Also, extend the Oracle Clusterware home to the new nodes using the procedures for "Extending Clusterware and Oracle Software to New Nodes" as described in [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/toc.htm).
3. From the existing Oracle home, extend this home to the new nodes using the procedure "Adding Nodes at the Oracle RAC Database Layer" as described in Oracle Clusterware Administration and Deployment Guide.
4. From one of the newly added nodes, configure the listeners on the additional nodes using NETCA. Choose the same port number and protocol that you used on the existing node. If NETCA displays the existing node in the node list page, then do not select this node, because the listener is already configured on it.
5. Convert the database using one of the following procedures:
	- Automated Conversion Procedure Using DBCA
		- Manual Conversion Procedure

##### C.2.3.1.1 Automated Conversion Procedure Using DBCA

1. If you created the preconfigured image of the single instance database as described in the section "Back Up the Original Single-Instance Database", then use DBCA to complete the conversion to an Oracle RAC database.
2. Start DBCA from the initial node. Select the names of the nodes to include as part of your cluster database. On the Template Selection page, select the preconfigured template that you created in Step [^1]. Enter the database name and respond to the remaining DBCA prompts.
3. To use raw devices for the cluster database files: When the Initialization Parameters page appears, enter the raw device name for the SPFILE on the File Locations tab. On the Storage page, replace the default database file names with the raw devices for the control files, redo logs, and data files to create the cluster database. Click Finish, and create the database.

After creating the Oracle RAC database, DBCA displays the Password Management page on which you must change the passwords for the database privileged users who have `SYSDBA` and `SYSOPER` roles. When DBCA exits, the conversion process is complete.

##### C.2.3.1.2 Manual Conversion Procedure

Because you did not use DBCA to create a preconfigured image of your single-instance database in step [^1], perform the following steps to complete the conversion:

1. Create the Optimal Flexible Architecture (OFA) directory structure on each of the nodes that you have added.
	See Also:
	["Directory Structures for Oracle RAC"](apa.md) for more information about OFA
2. If you are converting single-instance database files on a file system to raw devices, then copy the database data files, control files, redo logs, and server parameter file to their corresponding raw devices using the `dd` command. Otherwise, continue to the next step.
3. Re-create the control files by running the `CREATE CONTROLFILE` SQL statement with the `REUSE` keyword and specify `MAXINSTANCES` and `MAXLOGFILES`, and so on, as needed for your Oracle RAC configuration. The `MAXINSTANCES` recommended default is 32.
4. Shut down the database instance.
5. If your single-instance database was using an SPFILE, then create a temporary PFILE from the SPFILE using the following SQL statement:
	```
	CREATE PFILE='pfile_name' from spfile='spfile_name'
	```
6. Set the `CLUSTER_DATABASE` parameter to `TRUE`, set the `INSTANCE_NUMBER` parameter to a unique value for each instance, using a `sid``.``parameter` `=` `value` syntax.
	If you optimized memory usage on your single-instance database, then adjust the size of the system global area (SGA) to avoid swapping and paging when you convert to Oracle RAC. you should make this adjustment because Oracle RAC requires about 350 bytes for each buffer to accommodate the Global Cache Service (GCS). For example, if you have 10,000 buffers, then Oracle RAC requires about 350 multiplied by 10,000 bytes more memory. Therefore, adjust the size of the SGA by changing the `DB_CACHE_SIZE` and `DB_nK_CACHE_SIZE` parameters accordingly.
7. Start up the database instance using the PFILE created in step [^3].
8. If your single-instance database was using automatic undo management, then create an undo tablespace for each additional instance using the `CREATE UNDO TABLESPACE` SQL statement. If you are using raw devices, then ensure that the data file for the undo tablespace is on the raw device.
9. Create redo threads that have at least two redo logs for each additional instance. If you are using raw devices, then ensure that the redo log files are on raw devices. Enable the new redo threads by using an `ALTER DATABASE` SQL statement. Then, shut down the database instance.
10. Copy the Oracle password file from the initial node, or from the node from which you are working, to the corresponding location on the additional nodes on which the cluster database will have an instance. Replace the `ORACLE_SID` name in each password file appropriately for each additional instance.
11. Add `REMOTE_LISTENER=LISTENER_` `DB_NAME` and `sid``.LOCAL_LISTENER=LISTENER_` `SID` parameters to the PFILE.
12. Configure the net service entries for the database and instances, and address entries for the `LOCAL_LISTENER` for each instance and for the `REMOTE_LISTENER` in the `tnsnames.ora` file. When you have done this, copy these to all nodes.
13. Create the SPFILE from the PFILE using the procedures in the section ["Procedures for Migrating to the Server Parameter File"](params.md). If you are not using a cluster file system, then ensure that the SPFILE is on a raw device.
14. Create the `$ORACLE_HOME/dbs/init` `sid``.ora` file that contains the following entry:
	```
	spfile='spfile_path_name'
	```
	The variable `spfile_path_name` is the complete path name of the SPFILE.
15. On the local node, run `catclust.sql`. This command creates the dictionary views needed for Oracle RAC databases. For example:
	```
	SQL> start ?/rdbms/admin/catclust.sql
	```
16. Add the configuration for the Oracle RAC or Oracle RAC One Node database and its instance-to-node mapping using SRVCTL.
17. Start the database using SRVCTL.

After starting the database with SRVCTL, your conversion process is complete and, for example, you can run the following SQL statement to see the status of all the instances in your Oracle RAC database:

```
SQL> select * from v$active_instances
```

#### C.2.3.2 Single Instance on a Cluster Running from an Oracle RAC-Disabled Oracle Home

You can install a single instance on a cluster running from an Oracle RAC Oracle home that is disabled if you performed a one-node cluster (with Oracle RAC) installation, but later disabled the Oracle RAC feature by unlinking it from the `oracle` binary before creating the single instance database. (However, you can also select the local and non-cluster selection on the Node Selection Page to create a single-instance home on a cluster with Oracle RAC disabled.) Perform the following procedures to convert this type of single-instance database to an Oracle RAC database:

1. Use DBCA to create a preconfigured image of your single-instance database as described in the section "Back Up the Original Single-Instance Database". To perform the conversion manually, shut down the single-instance database.
2. Change the directory to the `lib` subdirectory in the `rdbms` directory under the Oracle home.
3. Relink the `oracle` binary by running the following commands:
	```
	make -f ins_rdbms.mk rac_on
	make -f ins_rdbms.mk ioracle
	```
4. Continue with step [^2].

#### C.2.3.3 Single Instance on a Cluster Running from a Single-Instance Installed Oracle Home

You can only install a single instance on a cluster running from a single-instance installed Oracle home if you selected the local installation option on the OUI Specify Hardware Cluster Installation page during the single-instance Oracle Database 11g release 2 (11.2) installation.

To convert this type of database to an Oracle RAC database, perform the procedures described in the following sections:

1. "Back Up the Original Single-Instance Database".
2. "Complete Oracle Clusterware Installation".
3. "Validate the Cluster".
4. "Install Oracle Database 11g Software with Oracle RAC". In this step, make sure that you select a new Oracle home other than the one from which the single-instance database was running.

### C.2.4 Converting Oracle RAC One Node to Oracle RAC

You can convert an Oracle RAC One Node database to an Oracle RAC database by logging in as the Oracle RAC One Node database owner and entering the following SRVCTL command:

```
$ srvctl convert database -c RAC
```

After you run this command, you must create server pools for each service that the database has, in addition to the database server pool. The values for `SERVER_NAMES` of the service server pools must be set to the node that you converted from an Oracle RAC One Node to an Oracle RAC node.

Converting an administrator-managed Oracle RAC One Node database to an Oracle RAC database sets all database services so that the single instance is preferred. After you convert the database, you can add instances by running the SRVCTL `add` `instance` command.

Converting a policy-managed Oracle RAC One Node database to an Oracle RAC database sets all database services to UNIFORM cardinality. It also results in reusing the server pool in which the database currently runs. The conversion reconfigures the database to run on all of the nodes in the server pool. The command does not start any additional instances but running the SRVCTL `start` `database` command starts the database on all of the nodes in the server pool.

See Also:

The [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/toc.htm) for more information

## C.3 Preparing to Convert with rconfig and Oracle Enterprise Manager

You can use `rconfig`, or Oracle Enterprise Manager to assist with converting a single-instance database installation to an Oracle RAC database. The first of these, `rconfig`, is a command-line utility. Oracle Enterprise Manager Grid Control database administration option, Convert to Cluster Database, provides a GUI conversion tool. The following sections describe how to use these conversion tools:

- Prerequisites for Converting to Oracle RAC Databases
- Configuration Changes during Oracle RAC Conversion Using RCONFIG
- Converting Databases to Oracle RAC Using RCONFIG or Oracle Enterprise Manager
- Converting Databases to Oracle RAC Using Oracle Enterprise Manager

Note:

Before you start the conversion, as is always true before you start any major change to your database, always back up your existing database.

### C.3.1 Prerequisites for Converting to Oracle RAC Databases

Before you convert a single-instance database to an Oracle RAC database, ensure that the following conditions are met for each cluster node that you intend to make an Oracle RAC database node:

- Oracle Clusterware 11g release 2 (11.2) is installed, configured, and running.
- Oracle RAC 11g release 2 (11.2) software is installed.
- The Oracle binary is enabled for Oracle RAC.
- Shared storage, either Oracle Cluster File System or Oracle ASM, is available and accessible from all nodes.
- User equivalence exists for the `oracle` account.
- If you intend to use Oracle Enterprise Manager, then all Oracle Enterprise Manager agents are configured and running, and are configured with cluster and host information.
- You have backed up your existing database.

Note:

You must use clustered Oracle ASM instances for Oracle RAC databases.

### C.3.2 Configuration Changes during Oracle RAC Conversion Using RCONFIG

Note the following changes that occur when you convert a single-instance database to Oracle RAC using `rconfig`:

- During the conversion, `rconfig` places the target Oracle RAC database into archive log mode, and enables archiving for the database. If you do not plan to use archivelog space, then you can disable archive logging after the conversion has completed.
- For the Shared Storage Type value, if you enter CFS, and you use a cluster file system for your single-instance database storage, then rconfig converts the environment to use Oracle Managed Files (OMF) for database storage, and places the datafiles in a subdirectory located under the shared storage location.
- During the conversion, `rconfig` moves database files to a specified shared location, and configures them using OMF.
	If you want to avoid using OMF with your converted database, then the single-instance database files must already be located in a shared file system, and you must indicate that `rconfig` should not move the files.

### C.3.3 Converting Databases to Oracle RAC Using RCONFIG or Oracle Enterprise Manager

The following is a list of scenarios for converting a single-instance Oracle database to an Oracle RAC database:

- Converting a single-instance Oracle Database 11g release 2 (11.2) to an Oracle 11g release 2 (11.2) Oracle RAC database, running out of the same Oracle home and using the same data files as the single-instance database.
	In this scenario, run the `rconfig` utility from the Oracle RAC database home, or use the Convert to RAC option on the single-instance database target of Oracle Enterprise Manager Grid Control.
- Converting a single-instance Oracle Database version previous to Oracle Database 11g release 2 (11.2), running out of the same Oracle home and using the same data files as the single-instance database
	In this scenario, use OUI and Database Upgrade Assistant (DBUA) to update the single-instance database to Oracle Database 11g release 2 (11.2). Then use `rconfig` or the Oracle Enterprise Manager Convert to RAC option, as described in the preceding scenario.
- Converting a single-instance Oracle Database 11g release 2 (11.2) to an Oracle 11g release 2 (11.2) Oracle RAC database, running out of a different Oracle home and using the same data files as the single-instance database.
	In this scenario, run the `rconfig` utility in the target database home, or use the Convert to RAC option in the single-instance database target of Oracle Enterprise Manager Grid Control. Provide the file storage location when prompted.
- Converting a single-instance Oracle Database 11g release 2 (11.2) to an 11g release 2 (11.2) Oracle RAC database, running out of a different Oracle home, and where the host where the single-instance database is running is not one of the nodes of the Oracle RAC database.
	In this scenario, create a clone image of the single-instance database, and move the clone image to a host that is one of the nodes of the cluster. Then use `rconfig` or the Oracle Enterprise Manager Convert to RAC option, as described in the preceding scenario.

### C.3.4 Converting Databases to Oracle RAC Using Oracle Enterprise Manager

You can use Oracle Enterprise Manager Grid Control to convert a single-instance database to Oracle RAC. To use this feature, complete the following steps:

See Also:

The [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm) for information about upgrading existing Oracle Database installations

1. Log in to Grid Control. From the Grid Control Home page, click the Targets tab.
2. On the Targets page, click the Databases secondary tab, and click the link in the Names column of the database that you want to convert to Oracle RAC.
3. On the Database Instance Home page, click the Change Database secondary tab.
4. On the Administration page, in the Database Administration Change Database section, click Convert to Cluster Database.
5. Log in as the database user `SYS` with `SYSDBA` privileges to the database you want to convert, and click Next.
6. On the Convert to Cluster Database: Cluster Credentials page, provide a user name and password for the `oracle` user and password of the target database that you want to convert. If the target database is using Oracle ASM, then also provide the ASM `SYS` user and password, and click Next.
7. On the Hosts screen, select the host nodes in the cluster that you want to be cluster members in the Oracle RAC database installed. When you have completed your selection, click Next.
8. On the Convert to Database: Options page, select whether you want to use the existing listener and port number, or specify a new listener and port number for the cluster. Also provide a prefix for cluster database instances on the cluster.
	When you have finished entering information, click Next, or click Help if you need assistance in deciding how to enter information.
9. On the Convert to Cluster Database: Shared Storage page, either select the option to use your existing shared storage area, or select the option to have your database files copied to a new shared storage location. Also, decide if you want to use your existing Fast Recovery Area, or if you want to copy your recovery files to a new Fast Recovery Area using files managed by Oracle Database.
	If you use Oracle ASM, then Oracle recommends that you place the database area and the recovery area in separate failure groups. A failure group is defined by shared hardware, such as a controller shared between two disks, or two disks that are on the same spindle. If two disks share hardware that could fail, making both disks unavailable, then theses disks are said to be in the same failure group. If you do not use Oracle ASM, then Oracle recommends that the data files and the Fast Recovery Area are located on separate locations, as with separate Oracle ASM failure groups, so that a hardware failure does not affect availability.
	When you have finished entering information, click Next, or click Help if you need assistance in deciding how to enter information.
10. On the Convert to Cluster Database: Review page, review the options you have selected. Click Submit Job if you want to proceed to conversion. If you want to change options you have selected, click Back. To cancel the conversion, click Cancel.
11. On the Confirmation page, click View Job to check the status of the conversion.

## C.4 Converting Databases to Oracle RAC Using RCONFIG

You can use the command line utility `rconfig` to convert a single-instance database to Oracle RAC, or to convert it to Oracle RAC One Node, depending on the values you provide in the `ConvertToRAC.xml` file. To use this feature, complete the following steps:

See Also:

The [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm) for information about upgrading existing Oracle Database installations

1. As the `oracle` user, navigate to the directory `$ORACLE_HOME/assistants/rconfig/sampleXMLs`, and open the file `ConvertToRAC.xml` using a text editor, such as `vi`.
2. Review the `ConvertToRAC.xml` file, and modify the parameters as required for your system. The XML sample file contains comment lines that provide instructions for how to configure the file.
	Caution:
	Set the convert option `Convert verify="ONLY"` to perform a test conversion to ensure that a conversion can be completed successfully.
	When you have completed making changes, save the file with the syntax `filename``.xml`. Make a note of the name you select.
3. Navigate to the directory `$ORACLE_HOME/bin`, and use the following syntax to run the command `rconfig`:
	```
	rconfig input.xml
	```
	where `input.xml` is the name of the XML input file you configured in step [^4].
	For example, if you create an input XML file called `convert.xml`, then enter the following command
	```
	$ ./rconfig convert.xml
	```

Note:

The `Convert verify` option in the `ConvertToRAC.xml` file has three options:
- `Convert verify="YES"`: rconfig performs checks to ensure that the prerequisites for single-instance to Oracle RAC conversion have been met before it starts conversion
- `Convert verify="NO"`: rconfig does not perform prerequisite checks, and starts conversion
- `Convert verify="ONLY"` rconfig only performs prerequisite checks; it does not start conversion after completing prerequisite checks

If performing the conversion fails, then use the following procedure to recover and reattempt the conversion.:

1. Attempt to delete the database using the DBCA delete database option.
2. Restore the source database.
3. Review the conversion log, and fix any problems it reports that may have caused the conversion failure. The `rconfig` log files are under the `rconfig` directory in `$ORACLE_BASE/cfgtoollogs`.
4. Reattempt the conversion.

## C.5 Example of Rconfig XML Input Files for ConvertToRAC

The following are two examples of an XML `ConvertToRAC` input file for the `rconfig` utility. Example C-1 is an XML input file to convert a single-instance database with Oracle ASM to an Oracle RAC database using Policy Managed server pools on Oracle ASM storage. Example C-2 is an XML input file to convert a single-instance database with Oracle ASM to an Oracle RAC database using Administrator Managed server pools.

Example C-1 RConfig ConvertToRAC for Policy Managed Databases

```
<?xml version="1.0" encoding="UTF-8"?>
<n:RConfig xmlns:n="http://www.oracle.com/rconfig/"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://www.oracle.com/rconfig/">
    <n:ConvertToRAC>   
<!-- Verify does a precheck to ensure all pre-requisites are met, before the conversion is attempted. Allowable values are: YES|NO|ONLY -->
        <n:Convert verify="YES">
<!--Specify current OracleHome of non-rac database for SourceDBHome -->
              <n:SourceDBHome>/oracle/product/11.2.0/db_1</n:SourceDBHome>
<!--Specify OracleHome where the rac database should be configured. It can be same as SourceDBHome -->
              <n:TargetDBHome>/oracle/product/11.2.0/db_1</n:TargetDBHome>
<!--Specify SID of non-rac database and credential. User with sysdba role is required to perform conversion -->
              <n:SourceDBInfo SID="sales">
                <n:Credentials>
                  <n:User>sys</n:User>
                  <n:Password>oracle</n:Password>
                  <n:Role>sysdba</n:Role>
                </n:Credentials>
              </n:SourceDBInfo>
<!--Specify the list of existing or new server pools which will be used by the Policy Managed Cluster Database. -->
              <n:ServerPoolList>
                <n:ExistingServerPool name="custom"/>
                <n:NewServerPool name="newpool" cardinality="2"/>
              </n:ServerPoolList>
<!--Specify RacOneNode along with servicename to convert database to RACOne Node -->
              <!--n:RacOneNode  servicename="salesrac1service"/-->
<!--InstancePrefix is not required for Policy Managed database. If specified, it will be ignored. Instance names are generated automatically based on db_unique_name for Policy Managed dababase.-->
<!-- Listener details are no longer needed starting 11.2. Database is registered with default listener and SCAN listener running from Oracle Grid Infrastructure home. -->
<!--Specify the type of storage to be used by rac database. Allowable values are CFS|ASM. The non-rac database should have same storage type. ASM credentials are no needed for conversion. -->
              <n:SharedStorage type="ASM">
<!--Specify Database Area Location to be configured for rac database.If this field is left empty, current storage will be used for rac database. For CFS, this field will have directory path. -->
                <n:TargetDatabaseArea>+ASMDG</n:TargetDatabaseArea>
<!--Specify Fast Recovery Area to be configured for rac database. If this field is left empty, current recovery area of non-rac database will be configured for rac database. If current database is not using recovery Area, the resulting rac database will not have a recovery area. -->
                <n:TargetFlashRecoveryArea>+ASMDG</n:TargetFlashRecoveryArea>
              </n:SharedStorage>
        </n:Convert>
    </n:ConvertToRAC>
</n:RConfig>
```

Example C-2 Rconfig ConvertToRAC for Administrator Managed Databases

```
<?xml version="1.0" encoding="UTF-8"?>
<n:RConfig xmlns:n="http://www.oracle.com/rconfig/"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://www.oracle.com/rconfig rconfig.xsd">
    <n:ConvertToRAC>   
<!-- Verify does a precheck to ensure all pre-requisites are met, before the conversion is attempted. Allowable values are: YES|NO|ONLY -->
        <n:Convert verify="YES">
<!--Specify current OracleHome of non-rac database for SourceDBHome -->
              <n:SourceDBHome>/oracle/product/11.2.0/db_1</n:SourceDBHome>
<!--Specify OracleHome where the rac database should be configured. It can be same as SourceDBHome -->
              <n:TargetDBHome>/oracle/product/11.2.0/db_1</n:TargetDBHome>
<!--Specify SID of non-rac database and credential. User with sysdba role is required to perform conversion -->
              <n:SourceDBInfo SID="sales">
                <n:Credentials>
                  <n:User>sys</n:User>
                  <n:Password>oracle</n:Password>
                  <n:Role>sysdba</n:Role>
                </n:Credentials>
              </n:SourceDBInfo>
<!--Specify the list of nodes that should have rac instances running for the Admin Managed Cluster Database. LocalNode should be the first node in this nodelist. -->
              <n:NodeList>        
                <n:Node name="node1"/>
                <n:Node name="node2"/>
              </n:NodeList>
<!--Specify RacOneNode along with servicename to convert database to RACOne Node -->
<!--n:RacOneNode  servicename="salesrac1service"/-->
<!--Instance Prefix tag is optional starting with 11.2. If left empty, it is derived from db_unique_name.-->
              <n:InstancePrefix>sales</n:InstancePrefix>
<!-- Listener details are no longer needed starting 11.2. Database is registered with default listener and SCAN listener running from Oracle Grid Infrastructure home. -->
<!--Specify the type of storage to be used by rac database. Allowable values are CFS|ASM. The non-rac database should have same storage type. ASM credentials are no needed for conversion. -->
              <n:SharedStorage type="ASM">
<!--Specify Database Area Location to be configured for rac database.If this field is left empty, current storage will be used for rac database. For CFS, this field will have directory path. -->
                <n:TargetDatabaseArea>+ASMDG</n:TargetDatabaseArea>
<!--Specify Fast Recovery Area to be configured for rac database. If this field is left empty, current recovery area of non-rac database will be configured for rac database. If current database is not using recovery Area, the resulting rac database will not have a recovery area. -->
                <n:TargetFlashRecoveryArea>+ASMDG</n:TargetFlashRecoveryArea>
              </n:SharedStorage>
        </n:Convert>
    </n:ConvertToRAC>
</n:RConfig>
```

## C.6 Post-Conversion Steps

After completing the conversion, note the following recommendations for Oracle RAC environments, as described in the Oracle RAC documentation:

- Follow the recommendations for using load balancing and transparent application failover, as described in the Oracle Real Application Clusters Administration and Deployment Guide
- Use locally managed tablespaces instead of dictionary managed tablespaces to reduce contention and manage sequences in Oracle RAC as described in the Oracle Real Application Clusters Administration and Deployment Guide
- Follow the guidelines for using automatic segment space management as described in the Oracle Real Application Clusters Administration and Deployment Guide

The buffer cache and shared pool capacity requirements in Oracle RAC are slightly greater than the requirements for single-instance Oracle databases. Therefore, you should increase the size of the buffer cache by about 10%, and the size of the shared pool by about 15%.

[^1]: Use DBCA to create a preconfigured image of your single-instance database as described in the section "Back Up the Original Single-Instance Database". To perform the conversion manually, shut down the single-instance database.

[^2]: To add nodes to your cluster, add and connect these nodes to the cluster as described in the [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN) for your platform. Ensure that all of these nodes can access the shared storage. Also, extend the Oracle Clusterware home to the new nodes using the procedures for "Extending Clusterware and Oracle Software to New Nodes" as described in [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/toc.htm).

[^undefined]: From the existing Oracle home, extend this home to the new nodes using the procedure "Adding Nodes at the Oracle RAC Database Layer" as described in Oracle Clusterware Administration and Deployment Guide.

[^undefined]: From one of the newly added nodes, configure the listeners on the additional nodes using NETCA. Choose the same port number and protocol that you used on the existing node. If NETCA displays the existing node in the node list page, then do not select this node, because the listener is already configured on it.

[^undefined]: Convert the database using one of the following procedures:

- Automated Conversion Procedure Using DBCA
- Manual Conversion Procedure

[^3]: If your single-instance database was using an SPFILE, then create a temporary PFILE from the SPFILE using the following SQL statement:

```
CREATE PFILE='pfile_name' from spfile='spfile_name'
```

[^undefined]: Set the `CLUSTER_DATABASE` parameter to `TRUE`, set the `INSTANCE_NUMBER` parameter to a unique value for each instance, using a `sid``.``parameter` `=` `value` syntax.

If you optimized memory usage on your single-instance database, then adjust the size of the system global area (SGA) to avoid swapping and paging when you convert to Oracle RAC. you should make this adjustment because Oracle RAC requires about 350 bytes for each buffer to accommodate the Global Cache Service (GCS). For example, if you have 10,000 buffers, then Oracle RAC requires about 350 multiplied by 10,000 bytes more memory. Therefore, adjust the size of the SGA by changing the `DB_CACHE_SIZE` and `DB_nK_CACHE_SIZE` parameters accordingly.

[^undefined]: Start up the database instance using the PFILE created in step 5.

[^undefined]: If your single-instance database was using automatic undo management, then create an undo tablespace for each additional instance using the `CREATE UNDO TABLESPACE` SQL statement. If you are using raw devices, then ensure that the data file for the undo tablespace is on the raw device.

[^undefined]: Create redo threads that have at least two redo logs for each additional instance. If you are using raw devices, then ensure that the redo log files are on raw devices. Enable the new redo threads by using an `ALTER DATABASE` SQL statement. Then, shut down the database instance.

[^undefined]: Copy the Oracle password file from the initial node, or from the node from which you are working, to the corresponding location on the additional nodes on which the cluster database will have an instance. Replace the `ORACLE_SID` name in each password file appropriately for each additional instance.

[^undefined]: Add `REMOTE_LISTENER=LISTENER_` `DB_NAME` and `sid``.LOCAL_LISTENER=LISTENER_` `SID` parameters to the PFILE.

[^undefined]: Configure the net service entries for the database and instances, and address entries for the `LOCAL_LISTENER` for each instance and for the `REMOTE_LISTENER` in the `tnsnames.ora` file. When you have done this, copy these to all nodes.

[^undefined]: Create the SPFILE from the PFILE using the procedures in the section ["Procedures for Migrating to the Server Parameter File"](params.md). If you are not using a cluster file system, then ensure that the SPFILE is on a raw device.

[^undefined]: Create the `$ORACLE_HOME/dbs/init` `sid``.ora` file that contains the following entry:

```
spfile='spfile_path_name'
```

The variable `spfile_path_name` is the complete path name of the SPFILE.

[^undefined]: On the local node, run `catclust.sql`. This command creates the dictionary views needed for Oracle RAC databases. For example:

```
SQL> start ?/rdbms/admin/catclust.sql
```

[^undefined]: Add the configuration for the Oracle RAC or Oracle RAC One Node database and its instance-to-node mapping using SRVCTL.

[^undefined]: Start the database using SRVCTL.

[^4]: Review the `ConvertToRAC.xml` file, and modify the parameters as required for your system. The XML sample file contains comment lines that provide instructions for how to configure the file.

Caution:

Set the convert option `Convert verify="ONLY"` to perform a test conversion to ensure that a conversion can be completed successfully.

When you have completed making changes, save the file with the syntax `filename``.xml`. Make a note of the name you select.

[^undefined]: Navigate to the directory `$ORACLE_HOME/bin`, and use the following syntax to run the command `rconfig`:

```
rconfig input.xml
```

where `input.xml` is the name of the XML input file you configured in step 2.

For example, if you create an input XML file called `convert.xml`, then enter the following command

```
$ ./rconfig convert.xml
```