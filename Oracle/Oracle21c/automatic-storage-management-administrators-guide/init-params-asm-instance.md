---
title: "Administrator's Guide"
book: "Automatic Storage Management Administrator's Guide"
doc_id: F30296-05
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/ostmg/init-params-asm-instance.html
tags:
  - oracle
  - 21c
  - automatic-storage-management-administrators-guide
---

Settings for Oracle ASM instance initialization parameters are discussed in this topic.

To install and initially configure an Oracle ASM instance, use Oracle Universal Installer (OUI) and Oracle ASM Configuration Assistant (ASMCA).

After an Oracle ASM instance has been installed on a single-instance Oracle Database or in an Oracle Real Application Clusters (Oracle RAC) environment, the final Oracle ASM configuration can be performed. Only a few Oracle ASM-specific instance initialization parameters must be configured. The default values are usually sufficient.

The following topics are discussed:

See Also:

- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN-GUID-6F1C3203-0AA0-4AF1-921C-A027DD7CB6A9) for information about initialization parameters
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ADMIN-GUID-E31FC459-3208-4390-9A27-2FB626520EC4) for information about initialization parameter files
- [Oracle Grid Infrastructure Installation and Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWGEN) for information about installing and configuring Oracle ASM

### About Initialization Parameter Files for an Oracle ASM Instance

When installing Oracle ASM in an Oracle Restart (standalone) configuration, Oracle Universal Installer (OUI) creates a separate server parameter file (SPFILE) and password file for the Oracle ASM instance. The ASM SPFILE is stored in a disk group during installation.

When installing Oracle ASM in a clustered Oracle ASM environment, OUI creates a single, shared SPFILE for Oracle ASM in a disk group.

When upgrading an Oracle ASM instance, if the ASM SPFILE was originally in a shared file system, then the upgraded Oracle ASM instance retains the SPFILE in the same location. If the original Oracle ASM instance used a PFILE, then after an upgrade the instance continues to use a PFILE.

You can use an SPFILE or a text-based initialization parameter file (PFILE) as the Oracle ASM instance parameter file. If you use an SPFILE in a clustered Oracle ASM environment, then you must place the SPFILE in a disk group or on a cluster file system. Oracle recommends that the Oracle ASM SPFILE is placed in a disk group. You cannot use a new alias created on an existing Oracle ASM SPFILE to start the Oracle ASM instance

If you do not use a shared Oracle Grid Infrastructure home, then the Oracle ASM instance can use a PFILE. The same rules for file name, default location, and search order that apply to database initialization parameter files also apply to Oracle ASM initialization parameter files.

When an Oracle ASM instance searches for an initialization parameter file, the search order is:

1. The location of the initialization parameter file specified in the Grid Plug and Play (GPnP) profile
2. If the location has not been set in the GPnP profile, then the search order changes to:
	1. SPFILE in the Oracle ASM instance home
		For example, the SPFILE for Oracle ASM has the following default path in the Oracle Grid Infrastructure home in a Linux environment:
		`$ORACLE_HOME/dbs/spfile+ASM.ora`
		2. PFILE in the Oracle ASM instance home

Note:

A PFILE or SPFILE is required if your configuration uses nondefault initialization parameters for the Oracle ASM instance.

You can administer Oracle ASM initialization parameter files with SQL\*Plus, ASMCA, and ASMCMD commands.

See Also:

- [Managing Oracle ASM With ASMCA](manage-asm-asmca.md) for information about the ASMCA GUI and command-line interfaces
- [ASMCMD Instance Management Commands](asmcmd-instance-commands.md) for information about ASMCMD commands for managing an Oracle ASM SPFILE; such as `spbackup`, `spcopy`, and `spmove`
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ADMIN002) for more information about creating and maintaining initialization parameter files
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=SQLRF01315) for information about creating an SPFILE with the `CREATE` `SPFILE` SQL statement

### About Backing Up, Copying, and Moving an Oracle ASM Initialization Parameter File

You can back up, copy, or move an Oracle ASM SPFILE with the ASMCMD `spbackup`, `spcopy`, or `spmove` commands.

In addition, you can use the SQL `CREATE` `SPFILE` to create an Oracle ASM SPFILE when connected to the Oracle ASM instance.

You can also copy and move an Oracle ASM PFILE with the commands available on the specific platform, such as `cp` for Linux.

After copying or moving an SPFILE or PFILE, you must restart the instance with the SPFILE or PFILE in the new location to use that SPFILE or PFILE.

The following topics are discussed:

- Creating, Copying, and Moving an SPFILE Into a Disk Group
- Making a Back Up Copy of an Oracle ASM SPFILE in a Disk Group

See Also:

- [spbackup](asmcmd-instance-commands.md), [spcopy](asmcmd-instance-commands.md), and [spmove](asmcmd-instance-commands.md) for information about ASMCMD commands for managing an SPFILE
- [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ADMIN002) for more information about creating and maintaining initialization parameter files
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=SQLRF01315) for information about creating an SPFILE with the `CREATE` `SPFILE` SQL statement
- [Oracle Real Application Clusters Installation Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=GINST) for information about Grid Plug and Play (GPnP)

#### Creating, Copying, and Moving an SPFILE Into a Disk Group

If the `COMPATIBLE.ASM` disk group attribute is set to `11.2` or greater for a disk group, you can create, copy, or move an Oracle ASM SPFILE into the disk group.

For example, after upgrading an instance from Oracle ASM 11g Release 1 (11.1) to Oracle ASM 11g Release 2 (11.2), you could place the Oracle ASM SPFILE in a disk group that has `COMPATIBLE.ASM` set to `11.2`. For information about disk group compatibility attributes, see [Disk Group Compatibility](diskgroup-compatibility.md).

In the following steps, assume an Oracle ASM 11g Release 2 (11.2) instance is using a PFILE stored in `$ORACLE_HOME/dbs/asmpfile.ora`. You can use the SQL `CREATE` `SPFILE` statement to create an SPFILE from a PFILE stored in a local or shared file system. If a PFILE does not exist, then it could be created with the SQL `CREATE` `PFILE` statement.

To create an SPFILE in a disk group, perform the following steps:

1. Connect to the Oracle ASM instance.
	For example:
	```
	$ sqlplus / as sysasm
	```
2. Create an SPFILE in a disk group that has `COMPATIBLE.ASM` set to `11.2` with the SQL `CREATE` `SPFILE` statement.
	For example, create an Oracle ASM SPFILE from the existing `PFILE`.
	```
	SQL> CREATE SPFILE = '+DATA/asmspfile.ora' 
	       FROM PFILE = '$ORACLE_HOME/dbs/asmpfile.ora';
	```
	The `CREATE` `SPFILE` statement also updates the Grid Plug and Play (GPnP) profile. You can check the location of the Oracle ASM SPFILE in the GPnP profile with the ASMCMD `spget` command. See [spget](asmcmd-instance-commands.md).
	Note:
	If you include the `AS` `COPY` option, then the `CREATE` `SPFILE` `FROM` `PFILE` statement does not update the clusterwide SPFILE location.
3. Restart the Oracle ASM instance so that the instance reads the SPFILE in the new location.
	For information on shutting down and starting up an Oracle ASM instance, see [About Starting Up an Oracle ASM Instance](admin-asm-instance.md) and [About Shutting Down an Oracle ASM Instance](admin-asm-instance.md).

#### Making a Back Up Copy of an Oracle ASM SPFILE in a Disk Group

This section describes the steps to make a back up copy of an Oracle ASM SPFILE in another disk group using the ASMCMD commands. If necessary, then the backup copy can be used to restore the Oracle ASM SPFILE.

The source and target disk groups must have the disk group attribute `COMPATIBLE.ASM` set to `11.2` or higher.

To make a copy of the Oracle ASM SPFILE in another disk group with the `spcopy` command perform the following steps:

1. Locate the Oracle ASM SPFILE using the ASMCMD `spget` command.
	For example:
	```
	ASMCMD [+] > spget
	+DATA/ASM/ASMPARAMETERFILE/registry.253.849343867
	```
2. Copy the Oracle ASM SPFILE to another disk group with `spcopy` command.
	For example:
	```
	ASMCMD [+] > spcopy +DATA/ASM/ASMPARAMETERFILE/registry.253.849343867 +FRA/spfileCopyASM.ora
	```
	Running `spcopy` without the `-u` option does not update the location of the Oracle ASM SPFILE. You can use `spset` to set the location of the Oracle ASM SPFILE in the Grid Plug and Play (GPnP) profile.
3. List all the copies of the Oracle ASM SPFILE file contained in the FRA disk group using the ASMCMD `ls` command.
	For example:
	```
	ASMCMD [+] > ls -l --absolutepath FRA/ASM/ASMPARAMETERFILE
	Type              Redund  Striped  Time             Sys  Name
	ASMPARAMETERFILE  MIRROR  COARSE   JUN 06 13:00:00  Y    +FRA/spfileCopyASM.ora => REGISTRY.253.849533009
	```
4. Verify the current location of the Oracle ASM SPFILE file with the `spget` command.
	For example:
	```
	ASMCMD [+] > spget
	+DATA/ASM/ASMPARAMETERFILE/registry.253.849343867
	```

In the event that the current Oracle ASM SPFILE file in a disk group has been corrupted or that disk group is not accessible, you can use `spset` or `spcopy` with the `-u` option to restore the Oracle ASM SPFILE file using the backup copy that you have previously created.

For example:

```
ASMCMD [+] > spcopy -u +FRA/spfileCopyASM.ora +DATA2/ASM/spfileASM.ora
```

### About Oracle ASM Initialization Parameter Settings

There are several initialization parameters that you must set for an Oracle ASM instance. You can set these parameters with Oracle ASM Configuration Assistant (ASMCA). You can also set some parameters after database creation using SQL `ALTER` `SYSTEM` or `ALTER` `SESSION` statements.

The Oracle ASM parameters use suitable defaults for most environments. You cannot use parameters with names that are prefixed with `ASM_*` in database instance parameter files.

### About Automatic Memory Management for Oracle ASM

Automatic memory management automatically manages the memory-related parameters for both Oracle ASM and database instances with the `MEMORY_TARGET` parameter. Automatic memory management is enabled by default on an Oracle ASM instance, even when the `MEMORY_TARGET` parameter is not explicitly set. The default value used for `MEMORY_TARGET` is acceptable for most environments. This is the only parameter that you must set for complete Oracle ASM memory management. Oracle strongly recommends that you use automatic memory management for Oracle ASM.

An Oracle ASM instance can automatically increase the values set for `MEMORY_TARGET` and `MEMORY_MAX_TARGET` if an ORA-04031 error is raised and automatic memory management is enabled. If `MEMORY_MAX_TARGET` has been explicitly set to a value, then every time ORA-04031 is raised, the `MEMORY_TARGET` value is increased by 10% of the existing `MEMORY_TARGET` value or 128 MB, whichever is greater, but not greater than the customer specified `MEMORY_MAX_TARGET` value. If `MEMORY_MAX_TARGET` is not explicitly set, then both `MEMORY_TARGET` and `MEMORY_MAX_TARGET` are increased by 10% of the existing `MEMORY_TARGET` value or 128 MB, whichever is greater, for a maximum of five increases. The Oracle ASM instance must be rebooted to use the new `MEMORY_TARGET` and `MEMORY_MAX_TARGET` settings.

If you do not set a value for `MEMORY_TARGET`, but you do set values for other memory related parameters, Oracle internally calculates the optimum value for `MEMORY_TARGET` based on those memory parameter values. You can also increase `MEMORY_TARGET` dynamically, up to the value of the `MEMORY_MAX_TARGET` parameter, just as you can do for the database instance.

Although it is not recommended, you can disable automatic memory management by either setting the value for `MEMORY_TARGET` to `0` in the Oracle ASM parameter file or by running an `ALTER` `SYSTEM` `SET` `MEMORY_TARGET` `=0` statement. When you disable automatic memory management, Oracle reverts to automatic shared memory management and automatic PGA memory management. To revert to Oracle Database 10g Release 2 (10.2) functionality to manually manage Oracle ASM SGA memory, also run the `ALTER` `SYSTEM` `SET` `SGA_TARGET=0` statement. Unless specified, the behaviors of the automatic memory management parameters in Oracle ASM instances behave the same as in Oracle Database instances.

Note:

- For a Linux environment, automatic memory management cannot work if `/dev/shm` is not available or is undersized. For more information, see [Oracle Database Administrator's Reference for Linux and UNIX-Based Operating Systems](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=UNXAR). For information about platforms that support automatic memory management, see [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ADMIN11236).
- The minimum `MEMORY_TARGET` for Oracle ASM is 1 GB. If you set `MEMORY_TARGET` lower, then Oracle increases the value for `MEMORY_TARGET` to 1 GB automatically.
- For the recommended settings of memory initialization parameters in an Oracle Exadata environment, refer to the Oracle Exadata documentation.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ADMIN11197) for more information about the functionality of automatic memory management for database instances, which varies from Oracle ASM
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CNCPT1244) for an overview of memory management methods

### Recommended Settings for Oracle ASM Initialization Parameters

This section contains information about the following initialization parameters for Oracle ASM:

- ASM\_DISKGROUPS
- ASM\_DISKSTRING
- ASM\_IO\_PROCESSES
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

- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN-GUID-FD266F6F-D047-4EBB-8D96-B51B1DCA2D61) for more information about initialization parameters
- [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ADMIN002) for more information about creating and maintaining an initialization parameter file

#### ASM\_DISKGROUPS

The `ASM_DISKGROUPS` initialization parameter specifies a list of disk group names that an Oracle ASM instance mounts at startup when the SQL `ALTER` `DISKGROUP` `ALL` `MOUNT` statement is issued.

The Oracle ASM instance startup process executes `ALTER` `DISKGROUP` `ALL` `MOUNT` unless the `NOMOUNT` startup option is specified.

The default value of the `ASM_DISKGROUPS` parameter is a `NULL` string.

The `ASM_DISKGROUPS` parameter is dynamic. If you are using a server parameter file (SPFILE), then you do not have to manually alter the value of `ASM_DISKGROUPS` in most situations. Oracle ASM automatically adds a disk group to the parameter when the disk group is successfully created or mounted. Oracle ASM also automatically removes a disk group from the parameter when the disk group is dropped. However, the SPFILE is not updated on a manual dismount.

Note:

In Oracle Flex ASM configurations, disk groups are not removed from the SPFILE on dismount. Disk groups must always be auto-mounted so that remote instances can access them. A remote instance is an Oracle Database, Oracle IOServer, or Oracle ASM proxy instance located on a different node than the Oracle ASM instance.

The following is an example of setting the `ASM_DISKGROUPS` parameter dynamically:

```
SQL> ALTER SYSTEM SET ASM_DISKGROUPS = DATA, FRA;
```

When using a text initialization parameter file (PFILE), you may edit the initialization parameter file to add the name of any disk group so that it is mounted automatically at instance startup. You must remove the name of any disk group that you no longer want automatically mounted.

The following is an example of the `ASM_DISKGROUPS` parameter in the initialization file:

`ASM_DISKGROUPS` `=` `DATA,` `FRA`

Note:

Issuing the `ALTER DISKGROUP`...`ALL MOUNT` or `ALTER DISKGROUP`...`ALL DISMOUNT` commands does not affect the value of `ASM_DISKGROUPS`.

For Oracle Database 12c Release 1 or later, Oracle ASM configurations support up to 511 disk groups. Oracle ASM configurations with Oracle Database releases before 12c Release 1 can only support up to 63 disk groups.

See Also:

- [About Mounting Disk Groups at Startup](admin-asm-instance.md) for information about disk groups that are mounted at startup time
- [Mounting and Dismounting Disk Groups](maintain-diskgroups.md) for additional information about mounting Oracle ASM disk groups
- [Managing Oracle Flex ASM](manage-flex-asm.md) for information about Oracle Flex ASM
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN10247) for more information about the `ASM_DISKGROUPS` initialization parameter

#### ASM\_DISKSTRING

The `ASM_DISKSTRING` initialization parameter specifies a comma-delimited list of strings that limits the set of disks that an Oracle ASM instance discovers.

The discovery strings can include wildcard characters. Only disks that match one of the strings are discovered. The same disk cannot be discovered twice.

The discovery string format depends on the Oracle ASM library and the operating system that are in use. Pattern matching is supported. Refer to your operating system-specific installation guide for information about the default pattern matching.

For example on a Linux server, to limit the discovery process to only include disks that are in the `/dev/rdsk/mydisks` directory for an Oracle ASM instance that does not use Oracle ASM Filter Driver (Oracle ASMFD) or ASMLIB, set the `ASM_DISKSTRING` initialization parameter to:

`/dev/rdsk/mydisks/*`

The asterisk is required.

To limit the discovery process to only include disks that have a name that ends in `disk3` or `disk4`, you could set `ASM_DISKSTRING` as follows on a Linux system:

`ASM_DISKSTRING` `=` `'/dev/rdsk/*disk3'`, `'/dev/rdsk/*disk4'`

The `?` character, when used as the first character of a path, expands to the Oracle home directory. Depending on the operating system, when you use the `?` character elsewhere in the path, it is a wildcard for one character.

The default value of the `ASM_DISKSTRING` parameter is a `NULL` string. A `NULL` value causes Oracle ASM to search a default path for all disks in the system to which the Oracle ASM instance has read and write access. The default search path is platform-specific. Refer to your operating system-specific installation guide for more information about the default search path.

Oracle ASM cannot use a disk unless all of the Oracle ASM instances in the cluster can discover the disk through one of their own discovery strings. The names do not have to be the same on every node, but all disks must be discoverable by all of the nodes in the cluster. This may require dynamically changing the initialization parameter to enable adding new storage.

Note that the `ASM_DISKSTRING` initialization parameter value may also include strings that include prefixes. For example:

- `afd:` - Oracle ASM filter driver
- `o:` - Oracle Exadata
- `orcl:` - Oracle ASMLIB

See Also:

- [Oracle ASM Disk Discovery](asm-disk-discovery.md) for more information about discovering disks
- [Oracle Grid Infrastructure Installation and Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWGEN) for information about configuring storage with NVMe devices, Oracle ASM Filter Driver, and Oracle ASMLIB
- [Administering Oracle ASM Filter Driver](administer-filter-driver.md) for information about Oracle ASM Filter Driver
- Oracle Exadata documentation for information about the Oracle ASM discovery string format for Oracle Exadata
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN10248) for more information about the `ASM_DISKSTRING` initialization parameter

#### ASM\_IO\_PROCESSES

The `ASM_IO_PROCESSES` initialization parameter specifies the number of IO worker processes to be started in an Oracle IOServer (IOS) server instance.

This parameter is only applicable for an Oracle IOServer instance, which runs in an Oracle Grid Infrastructure home.

IOServer instances are started automatically in the Oracle Grid Infrastructure configuration when generating the credential file for a client cluster. You can configure the number of IOServer instances running in the client cluster.

The default value should work in most cases. However, under heavy IO loads a higher value than the default may be appropriate.

See Also:

- [Overview of Oracle Flex ASM](manage-flex-asm.md) for information about Oracle IOServer and Oracle Flex ASM
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN-GUID-25CB85C7-6371-4AEC-A79F-2DC1E0D4370D) for more information about the `ASM_IO_PROCESSES` initialization parameter

#### ASM\_POWER\_LIMIT

The `ASM_POWER_LIMIT` initialization parameter specifies the default power for disk rebalancing in a disk group.

The range of values is `0` to `1024`. The default value is `1`. A value of `0` disables rebalancing. Higher numeric values enable the rebalancing operation to complete more quickly, but might result in higher I/O overhead and more rebalancing processes.

- For disk groups that have the disk group ASM compatibility set to `11.2.0.2` or higher (for example, `COMPATIBLE.ASM` = `11.2.0.2`), the operational range of values is `0` to `1024` for the rebalance power.
- For disk groups that have the disk group ASM compatibility set to less than `11.2.0.2`, the operational range of values is `0` to `11` inclusive. If the value for `ASM_POWER_LIMIT` is larger than `11`, a value of `11` is used for these disk groups.

You can also specify the power of the rebalancing operation in a disk group with the `POWER` clause of the SQL `ALTER` `DISKGROUP`.. `REBALANCE` statement. The range of allowable values for the `POWER` clause is the same for the `ASM_POWER_LIMIT` initialization parameter. If the value of the `POWER` clause is specified larger than `11` for a disk group with ASM compatibility set to less than `11.2.0.2`, then a warning is displayed and a `POWER` value equal to `11` is used for rebalancing.

The specification of the power of the rebalancing operation in a disk group only affects rebalance operations, not new allocations to a disk group.

Note:

- Oracle recommends that you do not set the `ASM_POWER_LIMIT` initialization parameter to `0`.
- You cannot set the `ASM_POWER_LIMIT` initialization parameter to `0` in an Oracle Exadata or Oracle Data Appliance environment.

See Also:

- [Manually Rebalancing Disk Groups](alter-diskgroups.md) and [Tuning Rebalance Operations](alter-diskgroups.md) for information about the `ASM_POWER_LIMIT` initialization parameter, and the `POWER` clause
- [Disk Group Compatibility](diskgroup-compatibility.md) for information about disk group compatibility
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN10246) for more information about the `ASM_POWER_LIMIT` initialization parameter
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=SQLRF01113) for more information about the `POWER` clause of the SQL `ALTER` `DISKGROUP` `REBALANCE` statement

#### ASM\_PREFERRED\_READ\_FAILURE\_GROUPS

The `ASM_PREFERRED_READ_FAILURE_GROUPS` initialization parameter value is a comma-delimited list of strings that specifies the failure groups that should be preferentially read by the given instance.

Note:

The `ASM_PREFERRED_READ_FAILURE_GROUPS` initialization parameter has been deprecated in Oracle ASM 12c Release 2 (12.2) and may be desupported in a future release.

The `ASM_PREFERRED_READ_FAILURE_GROUPS` parameter setting is instance specific. The default value is `NULL`. This parameter is generally used for clustered Oracle ASM instances and its value can be different on different nodes.

For example:

`diskgroup_name1`.`failure_group_name1`,...

Note:

In an Oracle extended cluster, which contains nodes that span multiple physically separated sites, the `PREFERRED_READ.ENABLED` disk group attribute controls whether preferred read functionality is enabled for a disk group. If preferred read functionality is enabled, then this functionality enables an instance to determine and read from disks at the same site as itself, which can improve performance. Whether or not `PREFERRED_READ.ENABLED` has been enabled, preferred read can be set at the failure group level on an Oracle ASM instance or a client instance in a cluster with the `ASM_PREFERRED_READ_FAILURE_GROUPS` initialization parameter, which is available for backward compatibility.

The failure group values set by `ASM_PREFERRED_READ_FAILURE_GROUPS` take precedence over the `PREFERRED_READ.ENABLED` site values. The values of `ASM_PREFERRED_READ_FAILURE_GROUPS` on the client instances take precedence over the values on the Oracle ASM instances.

See Also:

- [Preferred Read Failure Groups](mirroring-diskgroup-redundancy.md) for more information about preferred read failure groups
- [PREFERRED\_READ.ENABLED](manage-diskgroup-attributes.md) for information about the `PREFERRED_READ.ENABLED` disk group attribute
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=RACAD820) for more information about configuring preferred disks in extended clusters
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN10279) for more information about the `ASM_PREFERRED_READ_FAILURE_GROUPS` initialization parameter

#### DB\_CACHE\_SIZE

The setting for the `DB_CACHE_SIZE` parameter determines the size of the buffer cache.

You do not have to set a value for the `DB_CACHE_SIZE` initialization parameter if you use automatic memory management.

This buffer cache stores metadata blocks. The default value for this parameter is suitable for most environments.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ADMIN00207) for more information about setting the `DB_CACHE_SIZE` initialization parameter
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=TGDBA290) for more information about memory configuration
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN10033) for more information about the `DB_CACHE_SIZE` parameter

#### DIAGNOSTIC\_DEST

The `DIAGNOSTIC_DEST` initialization parameter specifies the directory where diagnostics for an instance are located.

The default value for an Oracle ASM instance is the `$ORACLE_BASE` directory for the Oracle Grid Infrastructure installation.

Example 3-1 shows an example of the diagnostic directory for an Oracle ASM instance.

Example 3-1 Sample diagnostic directory for an Oracle ASM instance

```
$ ls $ORACLE_BASE/diag/asm/+asm/+ASM
alert  cdump  hm  incident  incpkg  ir  lck  metadata  stage  sweep  trace
```

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ADMIN11008) for more information about the `DIAGNOSTIC_DEST` initialization parameter and the fault diagnosability infrastructure.
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN10280) for more information about the `DIAGNOSTIC_DEST` parameter

#### INSTANCE\_TYPE

The `INSTANCE_TYPE` initialization parameter specifies whether the instance is a database instance, an Oracle Automatic Storage Management (Oracle ASM) instance, or an Oracle ASM Proxy instance.

The following is an example of the `INSTANCE_TYPE` parameter in the initialization file:

`INSTANCE_TYPE` `=` `ASM`

In addition to values `asm` and `rdbms`, `INSTANCE_TYPE` can be set to `asmproxy` in an Oracle Flex ASM configuration.

See Also:

- [Managing Oracle Flex ASM](manage-flex-asm.md) for information about Oracle Flex ASM
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN10244) for more information about the `INSTANCE_TYPE` parameter

#### LARGE\_POOL\_SIZE

The setting for the `LARGE_POOL_SIZE` parameter is used for large allocations.

You do not have to set a value for the `LARGE_POOL_SIZE` initialization parameter if you use automatic memory management.

The default value for this parameter is suitable for most environments.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ADMIN00207) for more information about setting the `LARGE_POOL_SIZE` initialization parameter
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=TGDBA290) for more information about memory configuration
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN10078) for more information about the `LARGE_POOL_SIZE` parameter

#### PROCESSES

The `PROCESSES` initialization parameter affects Oracle ASM, but the default value is usually suitable.

However, if multiple database instances are connected to an Oracle ASM instance, then you can use the following formulas, where `n` is the number of database instances connecting to the Oracle ASM instance.

In a non-Exadata environment, the recommended settings are:

- For `n` < 10, `PROCESSES` = 50\* `n` + 50
- For `n` >= 10, `PROCESSES` = 10\* `n` + 450

In an Oracle Exadata environment, the recommended setting is `PROCESSES` = `MAX` (450 + 10\* `n`, 1024).

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ADMIN11108) for more information about setting the `PROCESSES` initialization parameter
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN10175) for more information about the `PROCESSES` parameter

#### REMOTE\_LOGIN\_PASSWORDFILE

The `REMOTE_LOGIN_PASSWORDFILE` initialization parameter specifies whether the Oracle ASM instance checks for a password file.

This parameter operates the same for Oracle ASM and database instances.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ADMIN001) for more information about setting the `REMOTE_LOGIN_PASSWORDFILE` initialization parameter
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN10184) for more information about the `REMOTE_LOGIN_PASSWORDFILE` parameter

### About Setting Database Initialization Parameters for Use with Oracle ASM

When you do not use automatic memory management in a database instance, the SGA parameter settings for a database instance may require minor modifications to support Oracle ASM. When you use automatic memory management, the sizing data discussed in this section can be treated as informational only or as supplemental information to help determine the appropriate values that you should use for the SGA. Oracle highly recommends using automatic memory management.

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

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ADMIN00207) for information about managing memory allocation in an Oracle Database instance
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=TGDBA290) for more information about memory configuration and use