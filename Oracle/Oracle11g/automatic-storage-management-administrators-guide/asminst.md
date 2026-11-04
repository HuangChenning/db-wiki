---
title: Administering Oracle ASM Instances
book: "Automatic Storage Management Administrator's Guide"
doc_id: E18951-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e18951/asminst.htm
tags:
  - oracle
  - 11g
  - automatic-storage-management-administrators-guide
---

## 3 Administering Oracle ASM Instances

This chapter describes how to administer Automatic Storage Management (Oracle ASM) instances. It explains how to configure Oracle ASM instance parameters and how to set Oracle Database parameters for use with Oracle ASM. The chapter also describes Oracle ASM upgrading, patching, and authentication for Oracle ASM instance access. You can also use procedures in this chapter to migrate a database to use Oracle ASM.

Administering an Oracle ASM instance is similar to administering an Oracle Database instance, but the process requires fewer procedures. You can use Oracle Enterprise Manager and SQL\*Plus to perform Oracle ASM instance administration tasks.

Oracle ASM is installed in the Oracle Grid Infrastructure home separate from the Oracle Database home. Only one Oracle ASM instance is supported on a server. When managing an Oracle ASM instance, the administration activity must be performed in the Oracle Grid Infrastructure home.

This chapter contains the following topics:

For a description of an Oracle ASM instance, see ["About Oracle ASM Instances"](asmcon.md). For information about using Oracle Enterprise Manager to administer Oracle ASM, see [Chapter 9, "Administering Oracle ASM with Oracle Enterprise Manager"](asm_em.md).

## Operating with Different Releases of Oracle ASM and Database Instances Simultaneously

Oracle Automatic Storage Management (Oracle ASM) in Oracle Database 11g Release 2 (11.2) supports 11g Release 2 (11.2) or older software versions of Oracle database instances, including Oracle Database 10g. For compatibility between Oracle Clusterware and Oracle ASM, the Oracle Clusterware release must be greater than or equal to the Oracle ASM release.

Notes:

- An Oracle ASM instance must be at 11g Release 2 (11.2) to support an 11g Release 2 (11.2) Oracle Database.
- See Oracle Exadata documentation for information about the Oracle Database versions that Oracle ASM 11g Release 2 (11.2) supports when Oracle Exadata storage is present.

There are additional compatibility considerations when using disk groups with different releases of Oracle ASM and database instances. For information about disk group compatibility attributes settings, see ["Disk Group Compatibility"](asmdiskgrps.md).

When using different software versions, the database instance supports Oracle ASM functionality of the earliest release in use. For example, a 10.1 database instance operating with an 11.2 Oracle ASM instance supports only Oracle ASM 10.1 features.

The `V$ASM_CLIENT` view contains the `SOFTWARE_VERSION` and `COMPATIBLE_VERSION` columns with information about the software version number and instance compatibility level.

- The `SOFTWARE_VERSION` column of `V$ASM_CLIENT` contains the software version number of the database or Oracle ASM instance for the selected disk group connection.
- The `COMPATIBLE_VERSION` column contains the setting of the `COMPATIBLE` parameter of the database or Oracle ASM instance for the selected disk group connection.

You can query the `V$ASM_CLIENT` view on both Oracle ASM and database instances. For an example showing a query on the `V$ASM_CLIENT` view, see [Example 6-4, "Viewing disk group clients with V$ASM\_CLIENT"](asmviews.md). For more information about the `V$ASM_CLIENT` and `V$ASM_*` views, see ["Views Containing Oracle ASM Disk Group Information"](asmviews.md).

## Configuring Initialization Parameters for Oracle ASM Instances

This section discusses initialization parameter files and parameter settings for Oracle ASM instances. To install and initially configure an Oracle ASM instance, use Oracle Universal Installer (OUI) and Oracle ASM Configuration Assistant (ASMCA). Refer to your platform-specific [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for details about installing and configuring Oracle ASM.

After an Oracle ASM instance has been installed on a single-instance Oracle Database or in an Oracle Real Application Clusters (Oracle RAC) environment, the final Oracle ASM configuration can be performed. Only a few Oracle ASM-specific instance initialization parameters must be configured. The default values are usually sufficient.

See Also:

The Oracle Cloud Storage page on the Oracle Technology Network Web site at `http://www.oracle.com/technetwork/database/cloud-storage/index.html` for more information about Oracle ASM best practices

This section contains the following topics:

- Initialization Parameter Files for an Oracle ASM Instance
- Backing Up, Copying, and Moving an Oracle ASM Initialization Parameter File
- Setting Oracle ASM Initialization Parameters
- Oracle ASM Parameter Setting Recommendations
- Setting Database Initialization Parameters for Use with Oracle ASM

See Also:

- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams_part.htm#REFRN001) for information about initialization parameters
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN002) for information about initialization parameter files

### Initialization Parameter Files for an Oracle ASM Instance

When installing Oracle ASM in an Oracle Restart (standalone) configuration, Oracle Universal Installer (OUI) creates a separate server parameter file (SPFILE) and password file for the Oracle ASM instance. The ASM SPFILE is stored in a disk group during installation.

When installing Oracle ASM in a clustered Oracle ASM environment, OUI creates a single, shared SPFILE for Oracle ASM in a disk group.

When upgrading an Oracle ASM instance, if the ASM SPFILE was originally in a shared file system, then the upgraded Oracle ASM instance retains the SPFILE in the same location. If the original Oracle ASM instance used a PFILE, after an upgrade the instance continues to use a PFILE.

You can use an SPFILE or a text-based initialization parameter file (PFILE) as the Oracle ASM instance parameter file. If you use an SPFILE in a clustered Oracle ASM environment, then you must place the SPFILE in a disk group, on a shared raw device, or on a cluster file system. Oracle recommends that the Oracle ASM SPFILE is placed in a disk group. You cannot use a new alias created on an existing Oracle ASM SPFILE to start the Oracle ASM instance

If you do not use a shared Oracle Grid Infrastructure home, then the Oracle ASM instance can use a PFILE. The same rules for file name, default location, and search order that apply to database initialization parameter files also apply to Oracle ASM initialization parameter files.

When an Oracle ASM instance searches for an initialization parameter file, the search order is:

1. The location of the initialization parameter file specified in the Grid Plug and Play (GPnP) profile
2. If the location has not been set in the GPnP profile, then the search order changes to:
	1. SPFILE in the Oracle ASM instance home
		For example, the SPFILE for Oracle ASM has the following default path in the Oracle Grid Infrastructure home in a Linux environment:
		`$ORACLE_HOME/dbs/spfile+ASM.ora`
		2. PFILE in the Oracle ASM instance home

Note:

A PFILE or SPFILE is required if your configuration uses non-default initialization parameters for the Oracle ASM instance.

You can administer Oracle ASM initialization parameter files with SQL\*Plus, Oracle Enterprise Manager, ASMCA, and ASMCMD commands. For information about Oracle Enterprise Manager, see ["Configuring Oracle ASM Initialization Parameters with Oracle Enterprise Manager"](asm_em.md). For information about ASMCA, see [Chapter 11, "Oracle ASM Configuration Assistant"](asmca.md). For information about ASMCMD commands, see ["ASMCMD Instance Management Commands"](asm_util002.md).

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN002) for more information about creating and maintaining initialization parameter files
- [Oracle Database 2 Day DBA](https://docs.oracle.com/cd/E11882_01/server.112/e10897/instance.htm#ADMQS053) for information about viewing and modifying initialization parameters
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_6016.htm#SQLRF01315) for information about creating an SPFILE with the [`CREATE SPFILE`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_6016.htm#SQLRF01315) SQL statement

### Backing Up, Copying, and Moving an Oracle ASM Initialization Parameter File

You can back up, copy, or move an Oracle ASM SPFILE with the ASMCMD `spbackup`, `spcopy` or `spmove` commands. For information about these ASMCMD commands, see ["spbackup"](asm_util002.md), ["spcopy"](asm_util002.md), and ["spmove"](asm_util002.md).

You can also use the SQL `CREATE` `SPFILE` to create an Oracle ASM SPFILE when connected to the Oracle ASM instance.

You can copy and move an Oracle ASM PFILE with the commands available on the specific platform, such as `cp` for Linux.

After copying or moving an SPFILE or PFILE, you must restart the instance with the SPFILE or PFILE in the new location to use that SPFILE or PFILE.

If the `COMPATIBLE.ASM` disk group attribute is set to 11.2 or greater for a disk group, you can create, copy, or move an Oracle ASM SPFILE into the disk group.

For example, after upgrading an Oracle ASM instance from 11g release 1 (11.1) to 11g release 2 (11.2), you could place the Oracle ASM SPFILE in a disk group that has `COMPATIBLE.ASM` set to 11.2.

In the following steps, assume an Oracle ASM 11g release 2 (11.2) instance is using a PFILE stored in `$ORACLE_HOME/dbs/asmspfile.ora`. You can use the SQL `CREATE` `SPFILE` statement to create an SPFILE from a PFILE stored in a local or shared file system. If a PFILE does not exist, then it could be created with the SQL `CREATE` `PFILE` statement.

To create an SPFILE in a disk group, perform the following steps:

1. Connect to the Oracle ASM instance.
	For example:
	```
	$ sqlplus / as sysasm
	```
2. Create an SPFILE in a disk group that has `COMPATIBLE.ASM` set to 11.2 with the SQL `CREATE` `SPFILE` statement.
	For example, create an Oracle ASM SPFILE from the existing `PFILE`.
	```
	SQL> CREATE SPFILE = '+DATA/asmspfile.ora' 
	       FROM PFILE = '$ORACLE_HOME/dbs/asmpfile.ora';
	```
	The `CREATE` `SPFILE` statement also updates the Grid Plug and Play (GPnP) profile. You can check the location of the Oracle ASM SPFILE in the GPnP profile with the ASMCMD `spget` command. See ["spget"](asm_util002.md).
3. Restart the Oracle ASM instance so that the instance reads the SPFILE in the new location.
	For information on shutting down and starting up an Oracle ASM instance, see "Starting Up an Oracle ASM Instance" and "Shutting Down an Oracle ASM Instance".

For information about disk group compatibility attributes, see ["Disk Group Compatibility"](asmdiskgrps.md). For information about upgrading an Oracle ASM instance, see "Upgrading an Oracle ASM Instance in an Oracle Restart Configuration with Oracle Universal Installer".

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN002) for more information about creating and maintaining initialization parameter files
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_6016.htm#SQLRF01315) for information about creating an SPFILE with the [`CREATE SPFILE`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_6016.htm#SQLRF01315) SQL statement
- [Oracle Real Application Clusters Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for information about Grid Plug and Play (GPnP)

### Setting Oracle ASM Initialization Parameters

There are several initialization parameters that you must set for an Oracle ASM instance. You can set these parameters with Oracle ASM Configuration Assistant (ASMCA). You can also set some parameters after database creation using Oracle Enterprise Manager or SQL `ALTER` `SYSTEM` or `ALTER` `SESSION` statements.

The `INSTANCE_TYPE` initialization parameter is the only required parameter in the Oracle ASM instance parameter file. The Oracle ASM\* parameters use suitable defaults for most environments. You cannot use parameters with names that are prefixed with Oracle ASM\* in database instance parameter files.

Some database initialization parameters are also valid for an Oracle ASM instance initialization file. In general, Oracle ASM selects the appropriate defaults for database parameters that are relevant to an Oracle ASM instance.

For information about setting Oracle ASM parameters with Oracle Enterprise Manager, see ["Configuring Oracle ASM Initialization Parameters with Oracle Enterprise Manager"](asm_em.md).

#### Automatic Memory Management for Oracle ASM

Automatic memory management automatically manages the memory-related parameters for both Oracle ASM and database instances with the `MEMORY_TARGET` parameter. Automatic memory management is enabled by default on an Oracle ASM instance, even when the `MEMORY_TARGET` parameter is not explicitly set. The default value used for `MEMORY_TARGET` is acceptable for most environments. This is the only parameter that you must set for complete Oracle ASM memory management. Oracle strongly recommends that you use automatic memory management for Oracle ASM.

If you do not set a value for `MEMORY_TARGET`, but you do set values for other memory related parameters, Oracle internally calculates the optimum value for `MEMORY_TARGET` based on those memory parameter values. You can also increase `MEMORY_TARGET` dynamically, up to the value of the `MEMORY_MAX_TARGET` parameter, just as you can do for the database instance.

Although it is not recommended, you can disable automatic memory management by either setting the value for `MEMORY_TARGET` to `0` in the Oracle ASM parameter file or by running an `ALTER` `SYSTEM` `SET` `MEMORY_TARGET` `=0` statement. When you disable automatic memory management, Oracle reverts to auto shared memory management and automatic PGA memory management. To revert to Oracle Database 10g release 2 (10.2) functionality to manually manage Oracle ASM SGA memory, also run the `ALTER` `SYSTEM` `SET` `SGA_TARGET=0` statement. You can then manually manage Oracle ASM memory using the information in "Oracle ASM Parameter Setting Recommendations", that discusses Oracle ASM memory-based parameter settings. Unless specified, the behaviors of the automatic memory management parameters in Oracle ASM instances behave the same as in Oracle Database instances.

Notes:

- For a Linux environment, automatic memory management cannot work if `/dev/shm` is not available or is undersized. For more information, see [Oracle Database Administrator's Reference for Linux and UNIX-Based Operating Systems](https://docs.oracle.com/cd/E11882_01/server.112/e10839/toc.htm). For information about platforms that support automatic memory management, see [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/memory.htm#ADMIN11236).
- The minimum `MEMORY_TARGET` for Oracle ASM is 256 MB. If you set `MEMORY_TARGET` to 100 MB, then Oracle increases the value for `MEMORY_TARGET` to 256 MB automatically.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/memory.htm#ADMIN11197) for more information about the functionality of automatic memory management for database instances, which varies from Oracle ASM
- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/cncptdba.htm#CNCPT1244) for an overview of memory management methods

### Oracle ASM Parameter Setting Recommendations

This section contains information about the following parameters for Oracle ASM:

- ASM\_DISKGROUPS
- ASM\_DISKSTRING
- ASM\_POWER\_LIMIT
- ASM\_PREFERRED\_READ\_FAILURE\_GROUPS
- DB\_CACHE\_SIZE
- DIAGNOSTIC\_DEST
- INSTANCE\_TYPE
- LARGE\_POOL\_SIZE
- PROCESSES
- REMOTE\_LOGIN\_PASSWORDFILE
- SHARED\_POOL\_SIZE

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN002) for more information about creating and maintaining an initialization parameter file
- [Oracle Database 2 Day DBA](https://docs.oracle.com/cd/E11882_01/server.112/e10897/instance.htm#ADMQS053) for information about viewing and modifying initialization parameters

#### ASM\_DISKGROUPS

The `ASM_DISKGROUPS` initialization parameter specifies a list of the names of disk groups that an Oracle ASM instance mounts at startup. Oracle ignores the value that you set for `ASM_DISKGROUPS` when you specify the `NOMOUNT` option at startup or when you run the `ALTER` `DISKGROUP` `ALL` `MOUNT` statement. The default value of the `ASM_DISKGROUPS` parameter is a `NULL` string. For information about disk groups that are mounted at startup time, see "About Mounting Disk Groups at Startup".

The `ASM_DISKGROUPS` parameter is dynamic. If you are using a server parameter file (SPFILE), then you do not have to manually alter the value of `ASM_DISKGROUPS`. Oracle ASM automatically adds a disk group to this parameter when the disk group is successfully created or mounted. Oracle ASM also automatically removes a disk group from this parameter when the disk group is dropped or dismounted.

The following is an example of setting the `ASM_DISKGROUPS` parameter dynamically:

```
SQL> ALTER SYSTEM SET ASM_DISKGROUPS = DATA, FRA;
```

When using a text initialization parameter file (PFILE), you may edit the initialization parameter file to add the name of any disk group so that it is mounted automatically at instance startup. You must remove the name of any disk group that you no longer want automatically mounted.

The following is an example of the `ASM_DISKGROUPS` parameter in the initialization file:

`ASM_DISKGROUPS` `=` `DATA,` `FRA`

Note:

Issuing the `ALTER DISKGROUP`...`ALL MOUNT` or `ALTER DISKGROUP`...`ALL DISMOUNT` commands does not affect the value of `ASM_DISKGROUPS`.

For additional information about mounting Oracle ASM disk groups, see ["Mounting and Dismounting Disk Groups"](asmdiskgrps.md).

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams010.htm#REFRN10247) for more information about the `ASM_DISKGROUPS` initialization parameter

#### ASM\_DISKSTRING

The `ASM_DISKSTRING` initialization parameter specifies a comma-delimited list of strings that limits the set of disks that an Oracle ASM instance discovers. The discovery strings can include wildcard characters. Only disks that match one of the strings are discovered. The same disk cannot be discovered twice.

The discovery string format depends on the Oracle ASM library and the operating system that are in use. Pattern matching is supported. Refer to your operating system-specific installation guide for information about the default pattern matching.

For example, on a Linux server that does not use ASMLib, to limit the discovery process to only include disks that are in the `/dev/rdsk/mydisks` directory, set the `ASM_DISKSTRING` initialization parameter to:

`/dev/rdsk/mydisks/*`

The asterisk is required. To limit the discovery process to only include disks that have a name that ends in `disk3` or `disk4`, set `ASM_DISKSTRING` to:

`/dev/rdsk/*disk3`, `/dev/rdsk/*disk4`

The `?` character, when used as the first character of a path, expands to the Oracle home directory. Depending on the operating system, when you use the `?` character elsewhere in the path, it is a wildcard for one character.

The default value of the `ASM_DISKSTRING` parameter is a `NULL` string. A `NULL` value causes Oracle ASM to search a default path for all disks in the system to which the Oracle ASM instance has read and write access. The default search path is platform-specific. Refer to your operating system specific installation guide for more information about the default search path.

Oracle ASM cannot use a disk unless all of the Oracle ASM instances in the cluster can discover the disk through one of their own discovery strings. The names do not have to be the same on every node, but all disks must be discoverable by all of the nodes in the cluster. This may require dynamically changing the initialization parameter to enable adding new storage.

For additional information about discovering disks, see ["Oracle ASM Disk Discovery"](asmdiskgrps.md).

See Also:

- Oracle Exadata documentation for information about the Oracle ASM discovery string format for Oracle Exadata
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams011.htm#REFRN10248) for more information about the `ASM_DISKSTRING` initialization parameter

#### ASM\_POWER\_LIMIT

The `ASM_POWER_LIMIT` initialization parameter specifies the default power for disk rebalancing in a disk group. The range of values is `0` to `1024`. The default value is `1`. A value of `0` disables rebalancing. Higher numeric values enable the rebalancing operation to complete more quickly, but might result in higher I/O overhead and more rebalancing processes.

- For disk groups that have the disk group ASM compatibility set to `11.2.0.2` or greater (for example, `COMPATIBLE.ASM` = `11.2.0.2`), the operational range of values is `0` to `1024` for the rebalance power.
- For disk groups that have the disk group ASM compatibility set to less than `11.2.0.2`, the operational range of values is `0` to `11` inclusive. If the value for `ASM_POWER_LIMIT` is larger than `11`, a value of `11` is used for these disk groups.

You can also specify the power of the rebalancing operation in a disk group with the `POWER` clause of the SQL `ALTER` `DISKGROUP`... `REBALANCE` statement. The range of allowable values for the `POWER` clause is the same for the `ASM_POWER_LIMIT` initialization parameter. If the value of the `POWER` clause is specified larger than `11` for a disk group with ASM compatibility set to less than `11.2.0.2`, then a warning is displayed and a `POWER` value equal to `11` is used for rebalancing.

For information about the `ASM_POWER_LIMIT` unitization parameter, and the `POWER` clause, refer to ["Manually Rebalancing Disk Groups"](asmdiskgrps.md) and ["Tuning Rebalance Operations"](asmdiskgrps.md). For information about disk group compatibility, see ["Disk Group Compatibility"](asmdiskgrps.md).

See Also:

- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams012.htm#REFRN10246) for more information about the `ASM_POWER_LIMIT` initialization parameter
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1007.htm#SQLRF01113) for more information about the `POWER` clause of the SQL `ALTER` `DISKGROUP` `REBALANCE` statement

#### ASM\_PREFERRED\_READ\_FAILURE\_GROUPS

The `ASM_PREFERRED_READ_FAILURE_GROUPS` initialization parameter value is a comma-delimited list of strings that specifies the failure groups that should be preferentially read by the given instance. The `ASM_PREFERRED_READ_FAILURE_GROUPS` parameter setting is instance specific. The default value is `NULL`. This parameter is generally used for clustered Oracle ASM instances and its value can be different on different nodes.

For example:

`diskgroup_name1`.`failure_group_name1`,...

For more information about `ASM_PREFERRED_READ_FAILURE_GROUPS`, refer to ["Preferred Read Failure Groups"](asmdiskgrps.md).

See Also:

- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/storage.htm#RACAD820) for more information about configuring preferred disks in extended clusters
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams013.htm#REFRN10279) for more information about the `ASM_PREFERRED_READ_FAILURE_GROUPS` initialization parameter

#### DB\_CACHE\_SIZE

You do not have to set a value for the `DB_CACHE_SIZE` initialization parameter if you use automatic memory management. The setting for the `DB_CACHE_SIZE` parameter determines the size of the buffer cache. This buffer cache is used to store metadata blocks. The default value for this parameter is suitable for most environments.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/memory.htm#ADMIN00207) for more information about setting the `DB_CACHE_SIZE` initialization parameter
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/memory.htm#PFGRF014) for more information about memory configuration
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams052.htm#REFRN10033) for more information about the `DB_CACHE_SIZE` parameter

#### DIAGNOSTIC\_DEST

The `DIAGNOSTIC_DEST` initialization parameter specifies the directory where diagnostics for an instance are located. The default value for an Oracle ASM instance is the `$ORACLE_BASE` directory for the Oracle Grid Infrastructure installation.

Example 3-1 shows an example of the diagnostic directory for an Oracle ASM instance.

Example 3-1 Sample diagnostic directory for an Oracle ASM instance

```
$ ls $ORACLE_BASE/diag/asm/+asm/+ASM
alert  cdump  hm  incident  incpkg  ir  lck  metadata  stage  sweep  trace
```

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/diag.htm#ADMIN11008) for more information about the `DIAGNOSTIC_DEST` initialization parameter and the fault diagnosability infrastructure.
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams078.htm#REFRN10280) for more information about the `DIAGNOSTIC_DEST` parameter

#### INSTANCE\_TYPE

The `INSTANCE_TYPE` initialization parameter is optional for an Oracle ASM instance in an Oracle Grid Infrastructure home.

The following is an example of the `INSTANCE_TYPE` parameter in the initialization file:

`INSTANCE_TYPE` `=` `ASM`

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams107.htm#REFRN10244) for more information about the `INSTANCE_TYPE` parameter

#### LARGE\_POOL\_SIZE

You do not have to set a value for the `LARGE_POOL_SIZE` initialization parameter if you use automatic memory management.

The setting for the `LARGE_POOL_SIZE` parameter is used for large allocations. The default value for this parameter is suitable for most environments.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/memory.htm#ADMIN00207) for more information about setting the `LARGE_POOL_SIZE` initialization parameter
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/memory.htm#PFGRF014) for more information about memory configuration
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams113.htm#REFRN10078) for more information about the `LARGE_POOL_SIZE` parameter

#### PROCESSES

The `PROCESSES` initialization parameter affects Oracle ASM, but the default value is usually suitable. However, if multiple database instances are connected to an Oracle ASM instance, you can use the following formula:

`PROCESSES` = 50 + 50\*n

where `n` is the number database instances connecting to the Oracle ASM instance.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN11108) for more information about setting the `PROCESSES` initialization parameter
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams202.htm#REFRN10175) for more information about the `PROCESSES` parameter

### Setting Database Initialization Parameters for Use with Oracle ASM

When you do not use automatic memory management in a database instance, the SGA parameter settings for a database instance may require minor modifications to support Oracle ASM. When you use automatic memory management, the sizing data discussed in this section can be treated as informational only or as supplemental information to help determine the appropriate values that you should use for the SGA. Oracle highly recommends using automatic memory management.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/memory.htm#ADMIN00207) for information about managing memory allocation in an Oracle Database instance
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/memory.htm#PFGRF014) for more information about memory configuration and use

The following are configuration guidelines for SGA sizing on the database instance:

- `PROCESSES` initialization parameter—Add 16 to the current value
- `LARGE_POOL_SIZE` initialization parameter—Add an additional 600K to the current value
- `SHARED_POOL_SIZE` initialization parameter—Aggregate the values from the following queries to obtain the current database storage size that is either on Oracle ASM or stored in Oracle ASM. Next, determine the redundancy type and calculate the `SHARED_POOL_SIZE` using the aggregated value as input.
	```
	SELECT SUM(bytes)/(1024*1024*1024) FROM V$DATAFILE;
	SELECT SUM(bytes)/(1024*1024*1024) FROM V$LOGFILE a, V$LOG b
	       WHERE a.group#=b.group#;
	SELECT SUM(bytes)/(1024*1024*1024) FROM V$TEMPFILE 
	       WHERE status='ONLINE';
	```
	- For disk groups using external redundancy, every 100 GB of space needs 1 MB of extra shared pool plus 2 MB
		- For disk groups using normal redundancy, every 50 GB of space needs 1 MB of extra shared pool plus 4 MB
		- For disk groups using high redundancy, every 33 GB of space needs 1 MB of extra shared pool plus 6 MB

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/memory.htm#ADMIN00207) for information about managing memory allocation in an Oracle Database instance
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/memory.htm#PFGRF014) for more information about memory configuration and use

## Managing Oracle ASM Instances

This section describes how to administer Oracle ASM instances under the following topics:

- Administering Oracle ASM Instances with Server Control Utility
- Using Oracle Restart
- Starting Up an Oracle ASM Instance
- Shutting Down an Oracle ASM Instance
- Upgrading an Oracle ASM Instance in an Oracle Restart Configuration with Oracle Universal Installer
- Downgrading an Oracle ASM Instance in an Oracle Restart Configuration
- Out of Place Upgrades
- Configuring Oracle Grid Infrastructure with the Configuration Wizard
- Active Session History Sampling for Oracle ASM

### Administering Oracle ASM Instances with Server Control Utility

In addition to the Oracle ASM administration procedures that this section describes, you can use Server Control Utility (SRVCTL) in clustered Oracle ASM environments to perform the following Oracle ASM administration tasks:

- Add and remove the Oracle ASM CRS resource in Oracle Cluster Registry (OCR)
- Enable, disable, start, and stop Oracle ASM instances
- Display the Oracle ASM instance configuration and status

See Also:

The [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/storage.htm#RACAD826) for information about administering Oracle ASM instances with `SRVCTL`

### Using Oracle Restart

Oracle Restart improves the availability of your Oracle database. When you install the Oracle Grid Infrastructure for a standalone server, it includes both Oracle ASM and Oracle Restart. Oracle Restart runs out of the Oracle Grid Infrastructure home, which you install separately from Oracle Database homes.

Oracle Restart provides managed startup and restart of a single-instance (non-clustered) Oracle Database, Oracle ASM instance, service, listener, and any other process running on the server. If an interruption of a service occurs after a hardware or software failure, Oracle Restart automatically takes the necessary steps to restart the component.

With Server Control Utility (SRVCTL) you can add a component, such as an Oracle ASM instance, to Oracle Restart. You then enable Oracle Restart protection for the Oracle ASM instance. With SRVCTL, you also remove or disable Oracle Restart protection.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/restart.htm#ADMIN12708) for information about configuring and administering Oracle Restart
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/srvctladmin.htm#RACAD005) for information about automatically restarting single-instance databases residing on an Oracle RAC node
- [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for information about installation of Oracle Grid Infrastructure

### Starting Up an Oracle ASM Instance

This section describes how to start Oracle ASM instances under the following topics:

- Connecting To and Starting Up an Oracle ASM Instance
- Starting Up an Oracle ASM instance with an Incorrect SPFILE Path
- About Mounting Disk Groups at Startup
- About Restricted Mode

#### Connecting To and Starting Up an Oracle ASM Instance

You start an Oracle ASM instance similarly to the way in which you start an Oracle database instance with some minor differences.

When starting an Oracle ASM instance, note the following:

- To connect to a local Oracle ASM instance with SQL\*Plus, set the `ORACLE_SID` environment variable to the Oracle ASM system identifier (SID).
	The default Oracle ASM SID for a single-instance database is `+ASM`, and the default SID for Oracle ASM for an Oracle RAC node is `+ASM` `node_number` where `node_number` is the number of the node. The `ORACLE_HOME` environment variable must be set to the Grid Infrastructure home where Oracle ASM was installed.
	Note:
	Oracle recommends that you do not change the default Oracle ASM SID name.
- The initialization parameter file must contain the following entry:
	`INSTANCE_TYPE = ASM`
	This parameter indicates that an Oracle ASM instance, not a database instance, is starting.
- When you run the `STARTUP` command, rather than trying to mount and open a database, this command attempts to mount Oracle ASM disk groups.
	For information about disk groups that are mounted at startup time, see "About Mounting Disk Groups at Startup".
	After the Oracle ASM instance has started, you can mount disk groups with the `ALTER DISKGROUP...MOUNT` command. See ["Mounting and Dismounting Disk Groups"](asmdiskgrps.md) for more information.
- The associated Oracle database instance does not have to be running when you start the associated Oracle ASM instance.

The following list describes how Oracle ASM interprets SQL\*Plus `STARTUP` command parameters.

- `FORCE` Parameter
	Issues a `SHUTDOWN ABORT` to the Oracle ASM instance before restarting it.
	If an Oracle Automatic Storage Management Cluster File System (Oracle ACFS) file system is currently mounted on Oracle ADVM volumes, the file system should first be dismounted. Otherwise, applications encounter I/O errors and Oracle ACFS user data and metadata may not be written to storage before the Oracle ASM storage is fenced. For information about dismounting an Oracle ACFS file system, see ["Deregistering, Dismounting, and Disabling Volumes and Oracle ACFS File Systems"](asmfs_util001.md).
- `MOUNT` or `OPEN` Parameter
	Mounts the disk groups specified in the `ASM_DISKGROUPS` initialization parameter. This is the default if no command parameter is specified.
- `NOMOUNT` Parameter
	Starts up the Oracle ASM instance without mounting any disk groups.
- `RESTRICT` Parameter
	Starts up an instance in restricted mode that enables access only to users with both the `CREATE` `SESSION` and `RESTRICTED` `SESSION` system privileges. You can use the `RESTRICT` clause in combination with the `MOUNT`, `NOMOUNT`, and `OPEN` clauses.
	See Also:
	"About Restricted Mode" for more information
	In restricted mode, database instances cannot use the disk groups. In other words, databases cannot open files that are in that disk group. Also, the disk group cannot be mounted by any other instance in the cluster. Mounting the disk group in restricted mode enables only one Oracle ASM instance to mount the disk group. This mode is useful to mount the disk group for repairing configuration issues.

The following is a sample SQL\*Plus session for starting an Oracle ASM instance.

  
`SQLPLUS` `/NOLOG`  
`SQL>` `CONNECT` `SYS` `AS` `SYSASM`  
`Enter` `password:` `sys_password`  
`Connected` `to` `an` `idle` `instance.`  
  
`SQL>` `STARTUP`  
`ASM` `instance` `started`  
  
`Total System Global Area   71303168 bytes`  
`Fixed Size                 1069292 bytes`  
`Variable Size              45068052 bytes`  
`ASM Cache                  25165824 bytes`  
`ASM disk groups mounted`  

For more information about user authentication, see "Authentication for Accessing Oracle ASM Instances".

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/dba.htm#ADMIN00102) for more information about using environment variables to select instances
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/start.htm#ADMIN004) for more information about starting up and shutting down Oracle instances
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/storage.htm#RACAD826) for information about starting an Oracle ASM instance with `SRVCTL` in Oracle RAC
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/intro.htm#CWADD1111) for information about Oracle Clusterware Cluster subcomponent processes and background processes
- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/process.htm#CNCPT1249) for information about Oracle database background processes
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/bgprocesses.htm#REFRN104) for a description of the Oracle background processes

#### Starting Up an Oracle ASM instance with an Incorrect SPFILE Path

If the SPFILE path in the GPNP profile is incorrect, you can start the Oracle ASM instance as follows:

1. Create a PFILE with one line in it that identifies the path to the SPFILE.
	For example:
	Create the `/u01/oracle/dbs/spfileasm_init.ora` file that contains:
	`SPFILE='+DATA/asm/asmparameterfile/asmspfile.ora'`
2. Start up the instance using the initialization parameter file.
	For example:
	`SQL>` `STARTUP` `PFILE=/u01/oracle/dbs/spfileasm_init.ora`
3. After the instance is running, use the ASMCMD `spset` command to update the SPFILE path in the GPNP profile. See ["spset"](asm_util002.md).
	For example:
	`ASMCMD>` `spset` `+DATA/asm/asmparameterfile/asmspfile.ora`

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/start.htm#ADMIN12828) for more information about using `STARTUP` with a non-default server parameter file

#### About Mounting Disk Groups at Startup

At startup, the Oracle ASM instance attempts to mount the following disk groups:

- Disk groups specified in the `ASM_DISKGROUPS` initialization parameter
- Disk group used by Cluster Synchronization Services (CSS) for voting files
- Disk groups used by Oracle Clusterware for Oracle Cluster Registry (OCR)
- Disk group used by the Oracle ASM instance to store the ASM server parameter file (SPFILE)

If no disk groups are found in the previous list, then the Oracle ASM instance does not mount any disk groups at startup. After the Oracle ASM instance has started, you can mount disk groups with the `ALTER DISKGROUP...MOUNT` command. For more information, see ["Mounting and Dismounting Disk Groups"](asmdiskgrps.md).

#### About Restricted Mode

You can use the `STARTUP` `RESTRICT` command to control access to an Oracle ASM instance while you perform maintenance. When an Oracle ASM instance is active in this mode, all of the disk groups that are defined in the `ASM_DISKGROUPS` parameter are mounted in `RESTRICTED` mode. This prevents databases from connecting to the Oracle ASM instance. In addition, the restricted clause of the `ALTER` `SYSTEM` statement is disabled for the Oracle ASM instance. The `ALTER` `DISKGROUP` `diskgroup` `MOUNT` statement is extended to enable Oracle ASM to mount a disk group in restricted mode.

When you mount a disk group in `RESTRICTED` mode, the disk group can only be mounted by one instance. Clients of Oracle ASM on that node cannot access that disk group while the disk group is mounted in `RESTRICTED` mode. The `RESTRICTED` mode enables you to perform maintenance tasks on a disk group in the Oracle ASM instance without interference from clients.

Rebalance operations that occur while a disk group is in `RESTRICTED` mode eliminate the lock and unlock extent map messaging that occurs between Oracle ASM instances in an Oracle RAC environment. This improves the overall rebalance throughput. At the end of a maintenance period, you must explicitly dismount the disk group and remount it in normal mode.

### Shutting Down an Oracle ASM Instance

The Oracle ASM shutdown process is initiated when you run the `SHUTDOWN` command in SQL\*Plus. Before you run this command, ensure that the `ORACLE_SID` environment variable is set to the Oracle ASM SID so that you can connect to the local Oracle ASM instance. The default Oracle ASM SID for a single-instance database is `+ASM`, and the default SID for Oracle ASM for an Oracle RAC node is `+ASM` `node_number` where `node_number` is the number of the node. The `ORACLE_HOME` environment variable must be set to the Grid Infrastructure home where Oracle ASM was installed.

Oracle strongly recommends that you shut down all database instances that use the Oracle ASM instance and dismount all file systems mounted on Oracle ASM Dynamic Volume Manager (Oracle ADVM) volumes before attempting to shut down the Oracle ASM instance.

If Oracle Cluster Registry (OCR) or voting files are stored in a disk group, the disk group can only be dismounted by shutting down the Oracle ASM instance as part of shutting down the clusterware on a node. To shut down the clusterware, run `crsctl` `stop` `crs`.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/dba.htm#ADMIN00102) for more information about using environment variables to select instances
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/start.htm#ADMIN004) for more information about starting up and shutting down Oracle instances
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/votocr.htm#CWADD70700) for information about managing voting files, Oracle Cluster Registry (OCR), and Oracle Local Registry (OLR)

To shut down an Oracle ASM instance, perform the following steps:

  
`SQLPLUS /NOLOG`  
`SQL> CONNECT SYS` `AS SYSASM`  
`Enter` `password:` `sys_password`  
`Connected.`  
`SQL> SHUTDOWN NORMAL`  

For more information about user authentication, see "Authentication for Accessing Oracle ASM Instances".

The following list describes the `SHUTDOWN` modes and the behavior of the Oracle ASM instance in each mode.

- `NORMAL` Clause
	Oracle ASM waits for any in-progress SQL to complete before performing an orderly dismount of all of the disk groups and shutting down the Oracle ASM instance. Before the instance is shut down, Oracle ASM waits for all of the currently connected users to disconnect from the instance. If any database instances are connected to the Oracle ASM instance, then the `SHUTDOWN` command returns an error and leaves the Oracle ASM instance running. `NORMAL` is the default shutdown mode.
- `IMMEDIATE` or `TRANSACTIONAL` Clause
	Oracle ASM waits for any in-progress SQL to complete before performing an orderly dismount of all of the disk groups and shutting down the Oracle ASM instance. Oracle ASM does not wait for users currently connected to the instance to disconnect. If any database instances are connected to the Oracle ASM instance, then the `SHUTDOWN` command returns an error and leaves the Oracle ASM instance running. Because the Oracle ASM instance does not contain any transactions, the `TRANSACTIONAL` mode behaves the same as `IMMEDIATE` mode.
- `ABORT` Clause
	The Oracle ASM instance immediately shuts down without the orderly dismount of disk groups. This causes recovery to occur upon the next Oracle ASM startup.
	If any database instance is connected to the Oracle ASM instance, then the database instance aborts.
	If any Oracle Automatic Storage Management Cluster File System (Oracle ACFS) file systems are currently mounted on Oracle ADVM volumes, those file systems should first be dismounted. Otherwise, applications encounter I/O errors and Oracle ACFS user data and metadata may not be written to storage before the Oracle ASM storage is fenced. For information about dismounting an Oracle ACFS file system, see ["Deregistering, Dismounting, and Disabling Volumes and Oracle ACFS File Systems"](asmfs_util001.md). For more information about user authentication on Oracle ASM instance, see "Authentication for Accessing Oracle ASM Instances".

### Upgrading an Oracle ASM Instance in an Oracle Restart Configuration with Oracle Universal Installer

This section discusses the process to upgrade an Oracle ASM instance to an Oracle Restart 11g release 2 (11.2) configuration. The recommended practice is to upgrade an Oracle ASM instance with Oracle Universal Installer (OUI). OUI automatically defaults to upgrade mode when it detects an Oracle ASM instance at a previous release level.

This section discusses the following topics:

- Upgrading an Oracle ASM Instance from 11.1 to 11.2 in an Oracle Restart Configuration with Oracle Universal Installer
- Upgrading an Oracle ASM Instance from 11.2.0.x to 11.2.0.3 in an Oracle Restart Configuration with Oracle Universal Installer

Notes:

- For information about performing an Oracle ASM Rolling Upgrade from 11.1.0.6 to 11.2.0.1, refer to Oracle Database Readme.
- For information about upgrading Oracle ASM from version 11.2.0.1 to 11.2.0.2, see "Out of Place Upgrades".
- In an Oracle Clusterware configuration, the Oracle ASM instance is upgraded as part of the Oracle Clusterware upgrade.
- If you are making any changes to Oracle software, Oracle recommends that you create a backup of the Oracle software.

See Also:

- [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for information about installing and upgrading Oracle Grid Infrastructure
- Articles at [My Oracle Support](https://support.oracle.com/) (`https://support.oracle.com`) for information about upgrading Oracle ASM

For information about copying and moving an Oracle ASM instance initialization parameter file after upgrading, see "Backing Up, Copying, and Moving an Oracle ASM Initialization Parameter File".

Note:

The procedures described in this section upgrade the Oracle ASM instance and Oracle Restart (standalone) configuration. To upgrade Oracle Database and Oracle Enterprise Manager, see [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/upgrade.htm#UPGRD003).

#### Upgrading an Oracle ASM Instance from 11.1 to 11.2 in an Oracle Restart Configuration with Oracle Universal Installer

The following procedure describes how to upgrade an Oracle ASM instance from 11g release 1 (11.1) to 11g release 2 (11.2) in an Oracle Restart (standalone) configuration. In this scenario:

- The Oracle ASM and Oracle Database 11g release 1 (11.1) instances exist in separate homes.
- The Oracle Grid Infrastructure 11g release 2 (11.2) is to be installed in a separate home and the Oracle ASM instance 11g release 2 (11.2) is to be set up as an Oracle Restart (single-instance) configuration.
1. Shut down the Oracle Enterprise Manager agent, Oracle Database instances, Oracle ASM instance, and the listener in the older database and Oracle ASM homes.
	- Run `emctl` `stop` `dbconsole` to stop the Oracle Enterprise Manager agent.
		- Connect to the database instances with SQL\*Plus as a privileged user and run the `SHUTDOWN` command.
		- Connect to the Oracle ASM instance with SQL\*Plus as a privileged user and run the `SHUTDOWN` command.
		- Run `lsnrctl` and enter the `STOP` command to stop the listener.
	For information about shutting down an Oracle ASM instance, see "Shutting Down an Oracle ASM Instance".
	See Also:
	- Oracle Enterprise Manager manuals and online help for information about starting and stopping the Oracle Enterprise Manager agent
	- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/start.htm#ADMIN004) for more information about starting up and shutting down Oracle instances
	- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/listenercfg.htm#NETAG010) for information about configuring a listener
2. Start the Oracle Grid Infrastructure OUI and select the Upgrade Oracle Grid Infrastructure option.
3. Complete the screens in the OUI installer and run the scripts as prompted by the OUI installer.
	For example, on Linux you must run the `root.sh` script as the `root` user.
	```
	# GRID_HOME/root.sh
	```
4. Confirm that the listener and Oracle ASM instance are running in the Oracle Grid Infrastructure home and ensure that the Oracle Database instance and Oracle Enterprise Manager agent are running in the old database home.
	- Confirm that the listener is running.
		Otherwise, start the listener with Server Control Utility (SRVCTL).
		For example:
		```
		$ srvctl start listener
		```
		- Confirm that the Oracle ASM instance is running.
		For example:
		```
		$ srvctl status listener
		$ srvctl status asm
		```
		Otherwise, start the Oracle ASM instance with SRVCTL.
		For example:
		```
		$ srvctl start asm
		```
		- Ensure that the database instances are running. Otherwise, connect to the database instances with SQL\*Plus as a privileged user and run the `STARTUP` command.
		- Ensure that the Oracle Enterprise Manager agent is running. Otherwise start the Oracle Enterprise Manager agent with `emctl` `start` `dbconsole`.

#### Upgrading an Oracle ASM Instance from 11.2.0.x to 11.2.0.3 in an Oracle Restart Configuration with Oracle Universal Installer

The following procedure describes how to upgrade an Oracle ASM instance from 11g release 2 (11.2.0.x) to 11g release 2 (11.2.0.3) in an Oracle Restart (standalone) configuration. In this scenario:

- The Oracle ASM and Oracle Database 11g release 2 instances exist in separate homes.
- The Oracle Grid Infrastructure 11g release 2 (11.2.0.3) is to be installed in a separate home and the Oracle ASM instance 11g release 2 (11.2.0.3) is to be set up as an Oracle Restart (single-instance) configuration.
1. Shut down the Oracle Enterprise Manager agent, Oracle Database instances, and the listener in the older database home.
	- Run `emctl` `stop` `dbconsole` to stop the Oracle Enterprise Manager agent.
		- Connect to the database instances with SQL\*Plus as a privileged user and run the `SHUTDOWN` command.
		See Also:
		- Oracle Enterprise Manager manuals and online help for information about starting and stopping the Oracle Enterprise Manager agent
		- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/start.htm#ADMIN004) for more information about starting up and shutting down Oracle instances
2. Start the Oracle Grid Infrastructure OUI and select the Upgrade Oracle Grid Infrastructure option.
3. Complete the screens in the OUI installer and run the scripts as prompted by the OUI installer.
	For example, on Linux you must run the `rootupgrade.sh` script as the `root` user:
	```
	# GRID_HOME/rootupgrade.sh
	```
4. Confirm that the listener and Oracle ASM instance are running in the Oracle Grid Infrastructure home and ensure that the Oracle Database instance and Oracle Enterprise Manager agent are running in the old database home.
	- Confirm that the listener is running.
		Otherwise, start the listener with Server Control Utility (SRVCTL).
		For example:
		```
		$ srvctl start listener
		```
		- Confirm that the Oracle ASM instance is running.
		For example:
		```
		$ srvctl status listener
		$ srvctl status asm
		```
		Otherwise, start the Oracle ASM instance with SRVCTL.
		For example:
		```
		$ srvctl start asm
		```
		- Ensure that the database instances are running. Otherwise, connect to the database instances with SQL\*Plus as a privileged user and run the `STARTUP` command.
		- Ensure that the Oracle Enterprise Manager agent is running. Otherwise start the Oracle Enterprise Manager agent with `emctl` `start` `dbconsole`.

### Downgrading an Oracle ASM Instance in an Oracle Restart Configuration

This section discusses the process to downgrade an Oracle ASM instance that has been upgraded to an Oracle Restart (standalone) configuration.

Notes:

- In an Oracle Clusterware configuration, the Oracle ASM instance is downgraded as part of the Oracle Clusterware downgrade.
- If you are making any changes to Oracle software, Oracle recommends that you create a backup of the Oracle software.

See Also:

- [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for information about downgrading Oracle Clusterware
- Articles at [My Oracle Support](https://support.oracle.com/) (`https://support.oracle.com`) for information about downgrading Oracle ASM

The following procedure describes how to downgrade an Oracle ASM instance from Oracle 11g release 2 (11.2) to Oracle 11g release 1 (11.1). In this scenario, the Oracle ASM instance was previously upgraded from an Oracle 11g release 1 (11.1) home to an Oracle Restart (standalone) 11g release 2 (11.2) configuration. The Oracle 11g release 1 (11.1) home was not removed.

1. Determine disk group compatibility attribute settings.
	If compatibility attributes have been advanced, then the disk groups must be re-created using compatibility attributes that allow access by the downgraded Oracle ASM and Oracle Database instances. A new disk group must be created with the old compatibility attributes and then you must restore the database files that were in the disk group.
	When you revert to a new disk group with the old compatibility attribute settings, the latest Oracle ASM features might not be available. For example, if you revert the disk group compatibility to a pre-11.2 value, Oracle ACFS functionality is not available.
	Copy or move an Oracle ASM SPFILE in a disk group to the file system before reverting disk group compatibility. Check the initialization parameters to ensure they are compatible with Oracle ASM 11g release 1 (11.1).
	For information about reverting disk group compatibility, see ["Reverting Disk Group Compatibility"](asmdiskgrps.md). For information about moving data files between disk groups, see ["Moving Data Files Between Oracle ASM Disk Groups Using RMAN"](asm_rman.md).
2. Downgrade any client databases from 11g release 2 (11.2) down to 11g release 1 (11.1).
	See Also:
	[Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/downgrade.htm#UPGRD007) for information about downgrading an Oracle Database and Oracle Enterprise Manager
3. Shut down the Oracle Enterprise Manager agent, Oracle Database instance, Oracle ASM instance, and the listener in the database and Oracle ASM homes.
	- Run `emctl` `stop` `dbconsole` to stop the Oracle Enterprise Manager agent.
		- Connect to the database instances with SQL\*Plus as a privileged user and run the `SHUTDOWN` command.
		- Shut down the Oracle ASM instance with Server Control Utility (SRVCTL).
		```
		$ srvctl stop asm
		```
		- Stop the listener with SRVCTL.
		```
		$ srvctl stop listener
		```
	For information about shutting down an Oracle ASM instance, see "Shutting Down an Oracle ASM Instance".
	See Also:
	- Oracle Enterprise Manager manuals and online help for information about starting and stopping the Oracle Enterprise Manager agent
	- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/start.htm#ADMIN004) for more information about starting up and shutting down Oracle instances
	- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for information about configuring a listener
	- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/srvctladmin.htm#RACAD005) for information about Server Control Utility (SRVCTL)
4. Deconfigure the Oracle Restart 11g release 2 (11.2) configuration.
	Run the `roothas.pl` script as `root`.
	For example, on Linux:
	```
	# GRID_HOME/crs/install/roothas.pl -deconfig
	```
	The Oracle 11g release 2 (11.2) `inittab` and `init*` scripts should be removed with the deconfiguration of Oracle Clusterware.
5. Unload the Oracle ACFS drivers.
	For example, on Linux run `acfsload` `stop` as `root`.
	```
	# GRID_HOME/bin/acfsload stop
	```
	For information about Oracle ACFS driver resource management, see ["Oracle ACFS Drivers Resource Management"](asmfs_extra.md).
6. Re-create the Oracle ASM 11g release 1 (11.1) resources.
	Run `localconfig` as `root` to add the resources to the Oracle ASM 11g release 1 (11.1) home.
	For example, on Linux:
	```
	# ORACLE_ASM_11.1_HOME/bin/localconfig add
	```
	If `localconfig` `add` fails, then use the `reset` option followed by the `ORACLE_HOME` to reset the existing resources.
	For example, on Linux:
	```
	# localconfig reset ORACLE_ASM_11.1_HOME
	```
7. Confirm that the Oracle ASM PFILE and `listerner.ora` files are present in the Oracle ASM 11g release 1 (11.1) home.
	If the Oracle ASM 11g release 1 (11.1) home has not been removed, then the files should be available.
8. Configure additional configuration files in the Oracle ASM 11g release 1 (11.1) home.
	For example, update files in the `/etc` directory on the Linux computer.
	Update the Oracle ASM entry in `/etc/oratab` to point to the Oracle ASM 11g release 1 (11.1) home, as shown in the following example:
	`+ASM:/` `ORACLE_ASM_11.1_HOME` `/product/11.1.0/asm_1:N`
	The 11g release 2 (11.2) `inittab` and `init*` scripts should be removed with the deconfiguration of Oracle Clusterware.
9. Ensure that the listener, Oracle ASM instance, Oracle Database instance, and Oracle Enterprise Manager agent are running in the 11g release 1 (11.1) Oracle ASM and database homes.
	- Start the listener with `lsnrctl` and enter the `START` option.
		If necessary, start Network Configuration Assistant (NETCA) in the Oracle ASM 11g release 1 (11.1) home with `netca`. Follow the prompts in the wizard to reconfigure the listener.
		- Connect to the Oracle ASM instance with SQL\*Plus as a privileged user and run the `STARTUP` command.
		- Connect to the database instances with SQL\*Plus as a privileged user and run the `STARTUP` command.
		- Start the Oracle Enterprise Manager agent with `emctl` `start` `dbconsole`.
		Oracle Enterprise Manager may require configuration after the Oracle ASM instance has been downgraded.

### Out of Place Upgrades

With an out-of-place upgrade, the installer installs the newer version of Oracle Grid Infrastructure in a separate Oracle Grid Infrastructure home.

An in-place upgrade of Oracle Grid Infrastructure 11g release 2 is not supported. For example, an upgrade of Oracle Grid Infrastructure 11.2.0.1 to 11.2.0.2 must be an out of place upgrade.

See Also:

[Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for information about installing Oracle Grid Infrastructure, out of place upgrades, and performing rolling upgrades of Oracle Grid Infrastructure and Oracle ASM

### Configuring Oracle Grid Infrastructure with the Configuration Wizard

The Oracle Grid Infrastructure configuration wizard can update the configuration of an Oracle Grid Infrastructure environment after the software has been installed. The configuration wizard accepts your input, validates the input, and populates the configuration data into the `CRSCONFIG_PARAMS` file. If additional scripts must be run, the configuration wizard directs you to run those scripts.

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD92094) for information about the Oracle Grid Infrastructure configuration wizard.

### Active Session History Sampling for Oracle ASM

Active Session History sampling is now available on Oracle ASM instances. This activity is exposed in the dynamic `V$ACTIVE_SESSION_HISTORY` view. Active Session History sampling requires a diagnostic pack license for the Oracle ASM instance.

See Also:

- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/autostat.htm#PFGRF027) for more information about gathering performance statistics
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1007.htm#REFRN30299) for a description of the `V$ACTIVE_SESSION_HISTORY` view

## Using Oracle ASM Rolling Upgrade

Note:

For information about performing an Oracle ASM Rolling Upgrade from 11.1.0.6 to 11.2.0.1, refer to Oracle Database Readme

Oracle ASM rolling upgrade enables you to independently upgrade or patch clustered Oracle ASM nodes without affecting database availability, thus providing greater uptime. Rolling upgrade means that some features of a clustered Oracle ASM environment continue to function when one or more of the nodes in the cluster uses different software versions. Oracle recommends that you perform an Oracle ASM rolling upgrade when performing an Oracle Clusterware rolling upgrade. Note that Oracle ASM is upgraded with Oracle Clusterware for Oracle 11g Release 2 (11.2) or later as both are in the Oracle Grid Infrastructure 11g Release 2 (11.2) home.

To perform a rolling upgrade from Oracle 11g Release 1 (11.1) to Oracle 11g Release 2 (11.2), your environment must be prepared. Oracle Clusterware must be fully upgraded to the next patch or release version before you start the Oracle ASM rolling upgrade. In addition, you should prepare your Oracle Clusterware in a rolling upgrade manner to ensure high availability and maximum uptime. Note that the rolling upgrade to Oracle 11g Release 2 (11.2) moves the Oracle ASM instance to Oracle Grid Infrastructure 11g Release 2 (11.2) home.

You can upgrade a single Oracle ASM instance with Oracle Universal Installer (OUI). For information, see "Upgrading an Oracle ASM Instance in an Oracle Restart Configuration with Oracle Universal Installer".

Notes:

- Rolling upgrades only apply to clustered Oracle ASM instances, and you can only perform rolling upgrades on environments with Oracle Database 11g or later. In other words, you cannot use this feature to upgrade from Oracle Database 10g to Oracle Database 11g.
- See Oracle Exadata documentation for information about performing a rolling upgrading of an Oracle ASM instance when Oracle Exadata storage is present.

See Also:

- [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for information about performing a rolling upgrade of Oracle ASM
- [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/upgrade.htm#UPGRD003) for information about upgrading Oracle Database
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_2014.htm#SQLRF00902) for information about the rolling migration clause of the `ALTER` `SYSTEM` commands

## Patching Oracle ASM Instances in Oracle RAC Environments

For Oracle RAC environments, ensure that your Oracle Clusterware version is at least equal to the version of the patch that you are applying to the Oracle Database. First apply the patch to the Oracle Grid Infrastructure home and then apply the patch to the Oracle Database home.

Note:

You must apply the patch to the Oracle Grid Infrastructure home before you apply it to the Oracle Database home.

## Authentication for Accessing Oracle ASM Instances

An Oracle ASM instance does not have a data dictionary, so the only way to connect to an Oracle ASM instance is by using one of three system privileges, `SYSASM`, `SYSDBA`, or `SYSOPER`. There are three modes of connecting to Oracle ASM instances:

- Local connection using operating system authentication
- Local connection using password authentication
- Remote connection by way of Oracle Net Services using password authentication

See Also:

Your operating system-specific [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for information about how to ensure that the Oracle ASM and database instances have member disk access

This section describes the following topics:

- About Privileges for Oracle ASM
- Creating Users with the SYSASM Privilege
- Operating System Authentication for Oracle ASM
- Password File Authentication for Oracle ASM

The Oracle ASM and database instances must have read/write operating system access rights to disk groups. For example, the Oracle ASM instance and the database instance must have identical read and write permissions for the disks that comprise the related Oracle ASM disk group. For Linux and UNIX systems, this is typically provided through shared Linux and UNIX group membership (OSASM group). On Windows systems, the Oracle ASM service must be run as Administrator. For information about file permissions and Oracle ASM File Access Control, see ["Managing Oracle ASM File Access Control for Disk Groups"](asmdiskgrps.md).

### About Privileges for Oracle ASM

During Oracle ASM installation, you can use one operating system group for all users or divide system privileges so that database administrators, storage administrators, and database operators each have distinct operating system privilege groups.

Whether you create separate operating system privilege groups or use one group to provide operating system authentication for all system privileges, you should use SYSASM to administer an Oracle ASM instance. The SYSDBA privilege cannot be used to administer an Oracle ASM instance. If you use the SYSDBA privilege to run administrative commands on an Oracle ASM instance, the operation results in an error. The SYSDBA privilege is intended to be used by the database to access disk groups.

Oracle also recommends the use of a less privileged user, such as ASMSNMP with SYSDBA privileges that is created during installation, for monitoring the Oracle ASM instance.

Operating system authentication using membership in the group or groups designated as OSDBA, OSOPER, and OSASM is valid on all Oracle platforms. Connecting to an Oracle ASM instance as SYSASM grants you full access to all of the available Oracle ASM disk groups and management functions.

This section contains these topics:

- Using One Operating System Group for Oracle ASM Users
- Using Separate Operating System Groups for Oracle ASM Users
- The SYSASM Privilege for Administering Oracle ASM
- The SYSDBA Privilege for Managing Oracle ASM Components

For information about privileges and Oracle ACFS, see ["Oracle ACFS and File Access and Administration Security"](asmfilesystem.md).

#### Using One Operating System Group for Oracle ASM Users

If you do not want to divide the privileges for system access into separate operating system groups, then you can designate one operating system group as the group whose members are granted access as OSDBA, OSOPER, and OSASM for Oracle ASM privileges. The default operating system group name for all of these is usually `dba` and that group is typically chosen for the default configuration.

Table 3-1 shows an example of a Linux deployment without separated privileges for Oracle ASM users.

Table 3-1 One operating system group and one set of privileges for all Oracle ASM users

| Role/Software Owner | User | Group/Privilege |
| --- | --- | --- |
| Oracle ASM administrator/Oracle Grid Infrastructure home | oracle | dba/SYSASM, SYSDBA, SYSOPER |
| Database administrator 1/Database home 1 | oracle | dba/SYSASM, SYSDBA, SYSOPER |
| Database administrator 2/Database home 2 | oracle | dba/SYSASM, SYSDBA, SYSOPER |
| Operating system disk device owner | oracle | dba |

#### Using Separate Operating System Groups for Oracle ASM Users

You can designate separate operating system groups as the operating system authentication groups for privileges on Oracle ASM. The following list describes the separate operating system authentication groups for Oracle ASM and the privileges that their members are granted.

- OSASM group
	This group is granted the SYSASM privilege, which provides full administrative privileges for the Oracle ASM instance. For example, the group could be `asmadmin`.
- OSDBA for Oracle ASM group
	This group is granted the SYSDBA privilege on the Oracle ASM instance, which grants access to data stored on Oracle ASM. This group has a subset of the privileges of the OSASM group.
	When you implement separate administrator privileges, choose an OSDBA group for the Oracle ASM instance that is different than the group that you select for the database instance, such as `dba`. For example, the group could be `asmdba`.
- OSOPER for Oracle ASM group
	This group is granted the SYSOPER privilege on the Oracle ASM instance, which provides operations such as startup, shutdown, mount, dismount, and check disk group. This group has a subset of the privileges of the OSASM group. For example, the group could be `asmoper`.

When you implement separate Oracle ASM and database administrator duties, this configuration requires different group and different software owners. Implicitly this implementation requires that the OSASM and OSDBA are different groups. For this configuration, you must create an OSDBA for Oracle ASM group and a database instance must be a member of that group to access the Oracle ASM instance.

In an installation that has been configured as Oracle Grid Infrastructure, the Oracle ASM user, such as `grid`, does not have to be a member of the Oracle Database OSDBA group, such as `dba1` or `dba2`, because the Oracle Clusterware database agent runs as the database owner and can use SYSDBA to connect to the database.

However, in an Oracle Restart configuration, the Oracle ASM user (`grid`) must be a member of the OSDBA group (`dba1`, `dba2`,...) of every database. This requirement is necessary because Oracle Restart software runs as the Oracle ASM user (`grid`) and this user must be able to start and stop the databases using the `CONNECT` `/` `AS` `SYSDBA` authentication.

Additionally, the owner of the operating system disk devices should be the same as the owner of the Oracle ASM software.

Table 3-2 shows an example of a Linux deployment using separate operating system privilege groups for Oracle ASM users.

Table 3-2 Separated operating system groups and privileges for Oracle ASM users

| Role/Software Owner | User | Group/Privilege |
| --- | --- | --- |
| Oracle ASM administrator/Oracle Grid Infrastructure home | grid | asmadmin (OSASM)/SYSASM  asmdba (OSDBA for ASM)/SYSDBA  asmoper (OSOPER for ASM)/SYSOPER  dba1, dba2,... (OSDBA for the databases when in an Oracle Restart configuration) |
| Database administrator 1/Database home 1 | oracle1 | asmdba (OSDBA for ASM)/SYSDBA  oper1 (OSOPER for database 1)/SYSOPER  dba1 (OSDBA for database 1)/SYSDBA |
| Database administrator 2/Database home 2 | oracle2 | asmdba (OSDBA for ASM)/SYSDBA  oper2 (OSOPER for database 2)/SYSOPER  dba2 (OSDBA for database 2)/SYSDBA |
| Operating system disk device owner | grid | asmadmin (OSASM) |

#### The SYSASM Privilege for Administering Oracle ASM

SYSASM is a system privilege that enables the separation of the SYSDBA database administration privilege from the Oracle ASM storage administration privilege. Access to the SYSASM privilege is granted by membership in an operating system group that is designated as the OSASM group. This is similar to SYSDBA and SYSOPER privileges, which are system privileges granted through membership in the groups designated as the OSDBA and OSOPER operating system groups. You can designate one group for all of these system privileges, or you can designate separate groups for each operating system privilege.

You can also grant the SYSASM privilege with password file authentication, as discussed in "Password File Authentication for Oracle ASM".

To connect locally as SYSASM using password authentication with SQL\*Plus, use the following statement:

```
sqlplus SYS AS SYSASM
...
Enter password:
```

To connect remotely as SYSASM using password authentication with SQL\*Plus, use the following statement:

```
sqlplus sys@\"myhost.mydomain.com:1521/+ASM\" AS SYSASM
...
Enter password:
```

In the previous example, `+ASM` is the service name of the Oracle ASM instance.

To connect locally as SYSASM to an Oracle ASM instance using operating system authentication with SQL\*Plus, use the following statement:

```
sqlplus / AS SYSASM
```

#### The SYSDBA Privilege for Managing Oracle ASM Components

You can connect as SYSDBA to use SQL\*Plus or ASMCMD commands to manage Oracle ASM components associated with the database. When running SQL or ASMCMD operations with the SYSDBA privilege, connect to the database instance rather than the Oracle ASM instance.

Connecting as SYSDBA to the database instance has a limited set of Oracle ASM privileges. For example, you cannot create a disk group when connected with the SYSDBA privilege.

When connected as SYSDBA to the database instance, the Oracle ASM operations are limited to:

- Create and delete files, aliases, directories, and templates
- Examine various Oracle ASM instance views
- Operate on files that were created by this user or only access files to which another user had explicitly granted access
- Granting Oracle ASM File Access Control to other users

### Creating Users with the SYSASM Privilege

When you are logged in to an Oracle ASM instance as SYSASM, you can use the combination of `CREATE` `USER` and `GRANT` SQL statements to create a user who has the SYSASM privilege. You also can revoke the SYSASM privilege from a user using the `REVOKE` command, and you can drop a user from the password file using the `DROP` `USER` command.

Note:

These commands update the password file for the local Oracle ASM instance only.

The following example describes how to perform these SQL operations for the user identified as `new_user`:

```
REM create a new user, then grant the SYSASM privilege
SQL> CREATE USER new_user IDENTIFIED by new_user_passwd;
SQL> GRANT SYSASM TO new_user;

REM connect the user to the ASM instance
SQL> CONNECT new_user AS SYSASM;
Enter password:

REM revoke the SYSASM privilege, then drop the user
SQL> REVOKE SYSASM FROM new_user;
SQL> DROP USER new_user;
```

When you revoke the last privilege of a user in an Oracle ASM password file, the user is not automatically deleted as is done in the Oracle Database password file. You need to run `DROP` `USER` to delete a user with no privileges in an Oracle ASM password file.

For information about creating a user with Oracle ASM command-line utility (ASMCMD), see ["orapwusr"](asm_util002.md). For information about creating a user with Oracle Enterprise Manager, see ["Managing Oracle ASM Users with Oracle Enterprise Manager"](asm_em.md).

### Operating System Authentication for Oracle ASM

Membership in the operating system group designated as the OSASM group provides operating system authentication for the SYSASM system privilege. OSASM is provided exclusively for Oracle ASM. Initially, only the user that installs ASM is a member of the OSASM group, if you use a separate operating system group for that privilege. However, you can add other users. Members of the OSASM group are authorized to connect using the SYSASM privilege and have full access to Oracle ASM, including administrative access to all disk groups that are managed by that Oracle ASM instance.

On Linux and UNIX systems, `dba` is the default operating system group designated as OSASM, OSOPER, and OSDBA for Oracle ASM. On Windows systems, `ora_dba` is the default name designated as OSASM, OSOPER, and OSDBA.

SQL\*Plus commands, ASMCMD commands, and ASMCA use operating system authentication.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/dba.htm#ADMIN001) for more information about using operating system authentication
- [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for information about installation of the Oracle Grid Infrastructure

### Password File Authentication for Oracle ASM

Password file authentication for Oracle ASM can work both locally and remotely. To enable password file authentication, you must create a password file for Oracle ASM. A password file is also required to enable Oracle Enterprise Manager to connect to Oracle ASM remotely.

If you select the Oracle ASM storage option, then ASMCA creates a password file for Oracle ASM with initial users (SYS and ASMSNMP) when ASMCA configures the Oracle ASM disk groups. To add other users to the password file, you can use the CREATE USER and GRANT commands as described previously in the section titled "About Privileges for Oracle ASM".

If you configure an Oracle ASM instance without using ASMCA, then you must manually create a password file and grant the SYSASM privilege to user SYS.

SQL\*Plus commands and Oracle Enterprise Manager use password file authentication.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/dba.htm#ADMIN10241) for information about creating and maintaining a password file
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for information about the [`CREATE` `USER`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_8003.htm#SQLRF01503) and [`GRANT`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_9013.htm#SQLRF01603) commands
- [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/intro.htm#DBSEG001) for information about database security
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2111.htm#REFRN30189) for information about the `V$PWFILE_USERS` view which lists users who have been granted `SYSASM`, `SYSDBA`, and `SYSOPER` privileges as derived from the password file.

## Migrating a Database to Use Oracle ASM

With a new installation of Oracle Database and Oracle ASM, you can initially create your database and select the Oracle ASM storage option. If you have an existing Oracle database that stores database files in the operating system file system or on raw devices, then you can migrate some or all of your data files to Oracle ASM storage.

Oracle provides several methods for migrating your database to Oracle ASM. Using Oracle ASM enables you to realize the benefits of automation and simplicity in managing your database storage. To migrate to Oracle ASM, you can use the methods described in the following sections:

- Using Oracle Enterprise Manager to Migrate Databases to Oracle ASM
- Using Oracle Recovery Manager to Migrate Databases to Oracle ASM
- Best Practices White Papers on Migrating to Oracle ASM

Note:

You must upgrade to at least Oracle Database 10g before migrating your database to Oracle ASM.

### Using Oracle Enterprise Manager to Migrate Databases to Oracle ASM

Oracle Enterprise Manager enables you to perform cold and hot database migration with a GUI. You can access the migration wizard from the Oracle Enterprise Manager Home page under the Change Database heading.

For more information about using Oracle Enterprise Manager to upgrade to Oracle ASM, see [Chapter 9, "Administering Oracle ASM with Oracle Enterprise Manager"](asm_em.md).

### Using Oracle Recovery Manager to Migrate Databases to Oracle ASM

You can use Oracle Recovery Manager (RMAN) to manually migrate to Oracle ASM. You can also use RMAN to migrate a single tablespace or data file to Oracle ASM.

For more information, see [Chapter 8, "Performing Oracle ASM Data Migration with RMAN"](asm_rman.md).

### Best Practices White Papers on Migrating to Oracle ASM

The Oracle Maximum Availability Architecture (MAA) Web site provides excellent best practices technical white papers based on different scenarios, such as:

- Minimal Downtime Migration to Oracle ASM
- Platform Migration using Transportable Tablespaces
- Platform Migration using Transportable Database

See Also:

For information about Oracle ASM best practices for migrating to Oracle ASM from environments that do not use Oracle ASM, refer to the documentation at the MAA link on Oracle Technology Network:

`http://www.oracle.com/technetwork/database/features/availability/maa-096107.html`