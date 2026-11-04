---
title: "Administrator's Guide"
book: "Advanced Cluster File System Administrator's Guide"
doc_id: F30297-04
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/acfsg/acfs-advanced-topics.html
tags:
  - oracle
  - 21c
  - advanced-cluster-file-system-administrators-guide
---

Oracle ACFS advanced topics include discussions about more complex administrative issues.

This appendix discusses Oracle Advanced Cluster File System (Oracle ACFS) advanced topics, including limits, advanced administration, troubleshooting, and patching.

See Also:

Articles available at My Oracle Support ([`https://support.oracle.com`](https://support.oracle.com/)) for information about Oracle ACFS and Oracle ADVM.

This appendix contains the following topics:

For an overview of Oracle ACFS, see [Introducing Oracle ACFS and Oracle ADVM](intro-acfs-advm.md).

### Limits of Oracle ACFS

The limits of Oracle ACFS are discussed in this section.

The topics contained in this section are:

- Oracle ACFS Disk Space Usage
- Oracle ACFS Error Handling
- Oracle ACFS and NFS

Note:

Oracle ACFS does not support hard links on directories.

#### Oracle ACFS Disk Space Usage

Oracle ACFS supports 64 mounted file systems on 32-bit systems, and 256 mounts on 64-bit systems. However, more file systems can be mounted if there is adequate memory.

Oracle ACFS supports 2^40 (1 trillion) files in a file system. More than 4 billion files have been tested. There is no absolute limit to the number of directories in a file system; the limit is based on hardware resources.

Oracle ACFS preallocates large user files to improve performance when writing data. This storage is not returned when the file is closed, but it is returned when the file is deleted. Oracle ACFS also allocates local metadata files as nodes mount the file system for the first time. This can result in a mount failing due to an out of space error, and much of this storage must be contiguous. This storage is approximately 64-128 megabytes per node.

Oracle ACFS also keeps local bitmaps available to reduce contention on the global storage bitmap when searching for free space. This disk space is reported as `in` `use` by tools such as the Linux `df` command even though some space may not actually be allocated yet. This local storage pool can be as large as 128 megabytes per node and can allow space allocations to succeed, even though commands, such as `df`, report less space available than what is being allocated.

The maximum sizes that can be allocated to an Oracle ACFS file system are shown in Table 7-1. The storage limits for Oracle ACFS and Oracle ASM are dependent on disk group compatibility attributes.

Table 7-1 Maximum file sizes for Oracle ACFS file systems/Oracle ADVM volumes

| Redundancy | Disk Group with COMPATIBLE.ASM < 12.2.0.1 | Disk Group with COMPATIBLE.ASM >= 12.2.0.1 |
| --- | --- | --- |
| External | 128 TB | 128 TB |
| Normal | 64 TB | 128 TB |
| High | 42.6 TB | 128 TB |

See Also:

- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=OSTMG-GUID-3DACEBE2-A29A-46F5-A954-B6C39B88B5DA) for information about file size limits and disk group compatibility settings
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=OSTMG-GUID-5AC1176D-D331-4C1C-978F-0ECA43E0900F) for information about storage limits for Oracle ASM files and disk groups

#### Oracle ACFS Error Handling

Oracle ASM instance failure or forced shutdown while Oracle ACFS or another file system is using an Oracle ADVM volume results in I/O failures. The volumes must be closed and re-opened to access the volume again. This requires dismounting any file systems that were mounted when the local Oracle ASM instance failed. After the instance is restarted, the corresponding disk group must be mounted with the volume enabled followed by a remount of the file system. See " [Deregistering, Dismounting, and Disabling Volumes and Oracle ACFS File Systems](steps-manage-acfs.md) ".

If any file systems are currently mounted on Oracle ADVM volume files, the `SHUTDOWN` `ABORT` command should not be used to terminate the Oracle ASM instance without first dismounting those file systems. Otherwise, applications encounter I/O errors and Oracle ACFS user data and metadata being written at the time of the termination may not be flushed to storage before the Oracle ASM storage is fenced. If there is not time to permit the file system to dismount, then you should run two `sync` (1) commands to flush cached file system data and metadata to persistent storage before issuing the `SHUTDOWN` `ABORT` operation.

Oracle ACFS does not interrupt the operating system environment when a metadata write fails, whether due to Oracle ASM instance failure or storage failure. Instead, Oracle ACFS isolates errors to a specific file system, putting it in an offline error state. The only operation that succeeds on that node for that file system from that point forward is a dismount operation. Another node recovers any outstanding metadata transactions, assuming it can write the metadata out to the storage. It is possible to remount the file system on the offlined node after the I/O condition is resolved.

It might not be possible for an administrator to dismount a file system while it is in the offline error state if there are processes referencing the file system, such as a directory of the file system being the current working directory for a process. To dismount the file system in this case it would be necessary to identify all processes on that node with references to files and directories on the file system and cause them to exit. The Linux `fuser` or `lsof` commands list information about processes and open files.

If Oracle ACFS detects inconsistent file metadata returned from a read operation, based on checksum or expected type comparisons, Oracle ACFS takes the appropriate action to isolate the affected file system components and generate a notification that `fsck` should be run as soon as possible. Each time the file system is mounted a notification is generated with a system event logger message until `fsck` is run.

#### Oracle ACFS and NFS

When exporting file systems through NFS on Linux, use the `-fsid=num` exports option. This option forces the file system identification portion of the file handle used to communicate with NFS clients to be the specified number instead of a number derived from the major and minor number of the block device on which the file system is mounted. You can use any 32-bit number for `num`, but it must be unique among all the exported file systems. In addition, `num` must be unique among members of the cluster and must be the same `num` on each member of the cluster for a given file system. This is needed because Oracle ASM DVM block device major numbers are not guaranteed to be the same across restarts of the same node or across different nodes in the cluster.

When using High Availability NFS for Grid Home Clusters (HANFS), HANFS automatically handles the situation described in the previous paragraph. For information about HANFS, refer to " [High Availability Network File Storage for Oracle Grid Infrastructure](understand-acfs-admin.md) ".

### Limits of Oracle ADVM

The limits of Oracle ADVM are discussed in this topic.

The default configuration for an Oracle ADVM volume is 8 columns and a 1 MB stripe width. The default volume extent size (64 MB).

Setting the number of columns on an Oracle ADVM dynamic volume to `1` effectively turns off striping for the Oracle ADVM volume. Setting the columns to 8 (the default) is recommended to achieve optimal performance with database data files and other files.

On Linux platforms Oracle ASM Dynamic Volume Manager (Oracle ADVM) volume devices are created as block devices regardless of the configuration of the underlying storage in the Oracle ASM disk group. Do not use `raw` `(8)` to map Oracle ADVM volume block devices into raw volume devices.

For information about ASMCMD commands to manage Oracle ADVM volumes, refer to [Managing Oracle ADVM with ASMCMD](manage-advm-asmcmd.md).

### How to Clone a Full Database (non-CDB or CDB) with ACFS Snapshots

ACFS snapshots are sparse, point-in-time copies of the filesystem and this can be used to create full DB clones as well as clones of PDBs using PDB snapshot cloning when the DB is on ACFS ([User Interface for PDB Cloning](https://docs.oracle.com/en/database/oracle/oracle-database/19/multi/cloning-a-pdb.html#GUID-B00A0E48-C892-4DC8-8455-C6F2ABC8EF91)). ACFS snapshots can be used in test and development environments to create quick and space efficient clones of a test master. This section explains the steps required to create a full DB clone using ACFS snaps with an example.

Test setup: We have a single test master CDB called `SOURCE` that will be cloned. The CDB has ten PDBs by name `sourcepdb[1-10]` and each of them is loaded with a OLTP schema. This is a Real Application Cluster database (RAC) and the instances are running on both the nodes. The datafiles, redo logs and controlfiles are stored in ACFS mounted at " `/mnt/dbvol` ". This filesystem is created on `DATA` diskgroup. Recovery logs and archive logs are stored on a filesystem mounted at " `/mnt/rvol` " that is created on top of the `RECO` diskgroup. Note that ACFS snaps will be contained within the filesystem and can be accessed through the same mountpoint.

Oracle highly recommends periodically creating backups of the test master database to provide a recovery method in case of issues.

For more detailed information regarding the configuration of ACFS Spanpshots on Exadata, see [Setting up Oracle Exadata Storage Snapshots](https://docs.oracle.com/en/engineered-systems/exadata-database-machine/sagug/exadata-storage-server-snapshots.html#GUID-78F67DD0-93C8-4944-A8F0-900D910A06A0)

For more information about different ACFS Snapshot use cases, please see My Oracle Support (MOS) note Oracle ACFS Snapshot Use Cases on Exadata (Doc ID 2761360.1).

#### Steps to Create and Use the Clone

1. Make sure that the database is in archive log mode:
	```
	SQL> archive log list
	Database log mode              Archive Mode
	Automatic archival             Enabled
	Archive destination            /mnt/rvol/archive
	Oldest online log sequence     488
	Next log sequence to archive   489
	Current log sequence           489
	SQL>
	```
2. Take a SQL trace backup of the control file for the test master database, the script generated will be used as the basis for creating controlfiles for each snapshot of this test master. This backup is created in the location specified in the AS clause. Specifying the RESETLOGS argument ensures only the RESETLOGS version of the create controlfile statement is generated in the trace file.
	```
	SQL> ALTER DATABASE BACKUP CONTROLFILE TO TRACE AS '/tmp/source1_ctlfile_bkup.sql' RESETLOGS;
	Database altered.
	[oracle@machine ~]$ ls -lrt /tmp/source1_ctlfile_bkup.sql
	-rw-r----- 1 oracle oinstall 32874 Jun 16 04:01 /tmp/source1_ctlfile_bkup.sql
	```
3. Create a pfile from the spfile if the DB instance currently uses an spfile:
	```
	SQL> CREATE PFILE=’/tmp/clone_pfile.ora’ FROM SPFILE;
	 
	File created.
	 
	SQL>
	```
	The pfile is saved to the location specified by the `PFILE=` clause.
4. Stop the test master database and create RW snap of the datafile filesystem:
	```
	[oracle@machine ~]$ srvctl stop database -db source
	[oracle@machine ~]$ /sbin/acfsutil  snap create -w clone /mnt/dbvol/
	acfsutil snap create: Snapshot operation is complete.
	[oracle@machine ~]$ /sbin/acfsutil snap info clone /mnt/dbvol/
	snapshot name:               clone
	snapshot location:           /mnt/dbvol/.ACFS/snaps/clone
	RO snapshot or RW snapshot:  RW
	parent name:                 /mnt/dbvol/
	snapshot creation time:      Tue Jun 16 04:09:10 2020
	file entry table allocation: 17170432   (  16.38 MB )
	storage added to snapshot:   17170432   (  16.38 MB )
	$
	```
5. Modify the trace file generated in step 2.
	The following block in the backed up trace file:
	```
	STARTUP NOMOUNT
	CREATE CONTROLFILE REUSE DATABASE "SOURCE" RESETLOGS  ARCHIVELOG
	    MAXLOGFILES 192
	    MAXLOGMEMBERS 3
	    MAXDATAFILES 1024
	    MAXINSTANCES 32
	    MAXLOGHISTORY 2254
	LOGFILE
	  GROUP 5 (
	    '/mnt/dbvol/oradata/SOURCE/onlinelog/o1_mf_5_hfh27gq1_.log',
	    '/mnt/rvol/fast_recovery_area/SOURCE/onlinelog/o1_mf_5_hfh27jgv_.log'
	  ) SIZE 2048M BLOCKSIZE 512,
	  GROUP 6 (
	    '/mnt/dbvol/oradata/SOURCE/onlinelog/o1_mf_6_hfh27ymp_.log',
	    '/mnt/rvol/fast_recovery_area/SOURCE/onlinelog/o1_mf_6_hfh280cb_.log'
	  ) SIZE 2048M BLOCKSIZE 512
	```
	Needs to be changed to:
	```
	CREATE CONTROLFILE  DATABASE "SOURCE" RESETLOGS ARCHIVELOG
	    MAXLOGFILES 192
	    MAXLOGMEMBERS 3
	    MAXDATAFILES 1024
	    MAXINSTANCES 32
	    MAXLOGHISTORY 2254
	LOGFILE
	  GROUP 5  SIZE 2048M BLOCKSIZE 512,
	  GROUP 6  SIZE 2048M BLOCKSIZE 512
	```
	Note that you will be creating new redo log files and hence the `db_create_online_log_dest_1` parameter will be picked by the DB instance to create the target files. No need to name them in the above statements, let Oracle use Oracle Managed Files (OMF) for naming.
	The `DATABASE` name specified in the `CREATE CONTROLFILE` statement must match the database name of the test master. The `DB_UNIQUE_NAME` parameter will be used to make this into a distinct database from the test master.
	The file names in the `DATAFILE` block need their directory structures changed to point to the files created in the snapshot.
	NOTE: Failure to change these file names could allow the snapshot to start using the parent files directly there by corrupting them. Ensure all the datafile names are modified to point to the snapshot location.
	A file named
	`/mnt/dbvol/oradata/source/datafile/o1_mf_system_hkp8q4l0_.dbf`
	would need to be renamed to
	`/mnt/dbvol/.ACFS/snaps/clone/oradata/source/datafile/o1_mf_system_hkp8q4l0_.dbf`
	Ensure all snapshot datafiles exist prior to attempting to create the controlfile.
	Since the TEMP files are all going to be created new, the corresponding statements need to change.
	- Old TEMP file clauses:
		```
		ALTER TABLESPACE TEMP ADD TEMPFILE '/mnt/dbvol/oradata/SOURCE/datafile/o1_mf_temp_hf9ck61d_.tmp'
		     SIZE 1377M REUSE AUTOEXTEND ON NEXT 655360  MAXSIZE 32767M;
		ALTER SESSION SET CONTAINER = "PDB$SEED";
		ALTER TABLESPACE TEMP ADD TEMPFILE '/mnt/dbvol/oradata/SOURCE/datafile/temp012020-06-01_03-40-57-522-AM.dbf'
		     SIZE 37748736  REUSE AUTOEXTEND ON NEXT 655360  MAXSIZE 32767M;
		ALTER SESSION SET CONTAINER = "SOURCEPDB1";
		ALTER TABLESPACE TEMP ADD TEMPFILE '/mnt/dbvol/oradata/SOURCE/A70228A28B4EB481E053DFB2980A90DF/datafile/o1_mf_temp_hf9f8yxz_.dbf'
		     SIZE 37748736  REUSE AUTOEXTEND ON NEXT 655360  MAXSIZE 32767M;
		ALTER SESSION SET CONTAINER = "SOURCEPDB2";
		ALTER TABLESPACE TEMP ADD TEMPFILE '/mnt/dbvol/oradata/SOURCE/A70229825B448EF3E053E0B2980AA4D4/datafile/o1_mf_temp_hf9f9goq_.dbf'
		     SIZE 37748736  REUSE AUTOEXTEND ON NEXT 655360  MAXSIZE 32767M;
		...........................................
		...........................................
		...........................................
		```
	- New TEMP file clauses:
		```
		ALTER TABLESPACE TEMP ADD TEMPFILE SIZE 1377M AUTOEXTEND ON NEXT 655360 MAXSIZE 32767M;
		ALTER SESSION SET CONTAINER = "PDB$SEED";
		ALTER TABLESPACE TEMP ADD TEMPFILE SIZE 37748736   AUTOEXTEND ON NEXT 655360  MAXSIZE 32767M;
		ALTER SESSION SET CONTAINER = "SOURCEPDB1";
		ALTER TABLESPACE TEMP ADD TEMPFILE SIZE 37748736   AUTOEXTEND ON NEXT 655360  MAXSIZE 32767M;
		ALTER SESSION SET CONTAINER = "SOURCEPDB2";
		ALTER TABLESPACE TEMP ADD TEMPFILE SIZE 37748736   AUTOEXTEND ON NEXT 655360  MAXSIZE 32767M;
		...........................................
		...........................................
		...........................................
		```
	Note:
	OMF is being used for naming the temp files, there is no need to specify a file name.
	- Other changes:
		- Remove the `REUSE` statement throughout.
			- Remove the `RECOVER DATABASE` command.
			- Remove commands to enable block change tracking.
	Following is an example of a full create controlfile statement:
	```
	STARTUP NOMOUNT
	CREATE CONTROLFILE  DATABASE "SOURCE" RESETLOGS  ARCHIVELOG
	    MAXLOGFILES 1024
	    MAXLOGMEMBERS 5
	    MAXDATAFILES 32767
	    MAXINSTANCES 32
	    MAXLOGHISTORY 33012
	LOGFILE
	GROUP 1 SIZE 4096M BLOCKSIZE 512, 
	GROUP 2 SIZE 4096M BLOCKSIZE 512, 
	GROUP 5 SIZE 4096M BLOCKSIZE 512, 
	GROUP 6 SIZE 4096M BLOCKSIZE 512 
	'/mnt/dbvol/.ACFS/snaps/clone/oradata/datafile/o1_mf_system_hkpjm4lh_.dbf',
	'/mnt/dbvol/.ACFS/snaps/clone/oradata/AAFDB0C85C03151AE053FE5E1F0AA61D/datafile/o1_mf_system_hkpjm4rf_.dbf',
	'/mnt/dbvol/.ACFS/snaps/clone/oradata/datafile/o1_mf_sysaux_hkpjm56t_.dbf',  
	'/mnt/dbvol/.ACFS/snaps/clone/oradata/AAFDB0C85C03151AE053FE5E1F0AA61D/datafile/o1_mf_sysaux_hkpjm6x4_.dbf',  
	'/mnt/dbvol/.ACFS/snaps/clone/oradata/datafile/o1_mf_undotbs1_hkpjm6x0_.dbf',  
	'/mnt/dbvol/.ACFS/snaps/clone/oradata/AAFDB0C85C03151AE053FE5E1F0AA61D/datafile/o1_mf_undotbs1_hkpjm6w5_.dbf',  
	'/mnt/dbvol/.ACFS/snaps/clone/oradata/datafile/o1_mf_undotbs2_hkpjm6tx_.dbf',  
	'/mnt/dbvol/.ACFS/snaps/clone/oradata/datafile/o1_mf_users_hkpjm722_.dbf',  
	'/mnt/dbvol/.ACFS/snaps/clone/oradata/AAFE1E09C8245CC2E053FE5E1F0A5632/datafile/o1_mf_system_hkpjmqds_.dbf',  
	'/mnt/dbvol/.ACFS/snaps/clone/oradata/AAFE1E09C8245CC2E053FE5E1F0A5632/datafile/o1_mf_sysaux_hkpjmqoc_.dbf',  
	'/mnt/dbvol/.ACFS/snaps/clone/oradata/AAFE1E09C8245CC2E053FE5E1F0A5632/datafile/o1_mf_undotbs1_hkpjmtl7_.dbf',  
	'/mnt/dbvol/.ACFS/snaps/clone/oradata/AAFE1E09C8245CC2E053FE5E1F0A5632/datafile/o1_mf_undo_2_hkpjn03d_.dbf',  
	'/mnt/dbvol/.ACFS/snaps/clone/oradata/AAFE1E09C8245CC2E053FE5E1F0A5632/datafile/o1_mf_users_hkpjn16b_.dbf',  
	'/mnt/dbvol/.ACFS/snaps/clone/oradata/AAFE1E09C8245CC2E053FE5E1F0A5632/datafile/o1_mf_soe_hkpjn1ft_.dbf',  
	'/mnt/dbvol/.ACFS/snaps/clone/oradata/AB1122BDE19EF370E053FE5E1F0A4E77/datafile/o1_mf_system_hkpjn8h4_.dbf',  
	'/mnt/dbvol/.ACFS/snaps/clone/oradata/AB1122BDE19EF370E053FE5E1F0A4E77/datafile/o1_mf_sysaux_hkpjn8nt_.dbf',  
	'/mnt/dbvol/.ACFS/snaps/clone/oradata/AB1122BDE19EF370E053FE5E1F0A4E77/datafile/o1_mf_undotbs1_hkpjn8qq_.dbf',  
	'/mnt/dbvol/.ACFS/snaps/clone/oradata/AB1122BDE19EF370E053FE5E1F0A4E77/datafile/o1_mf_undo_2_hkpjnf2p_.dbf',  
	'/mnt/dbvol/.ACFS/snaps/clone/oradata/AB1122BDE19EF370E053FE5E1F0A4E77/datafile/o1_mf_users_hkpjnglw_.dbf',  
	'/mnt/dbvol/.ACFS/snaps/clone/oradata/AB1122BDE19EF370E053FE5E1F0A4E77/datafile/o1_mf_soe_hkpjnkm6_.dbf',  
	'/mnt/dbvol/.ACFS/snaps/clone/oradata/AB112685643A0B77E053FE5E1F0A7BDD/datafile/o1_mf_system_hkpjnl8v_.dbf',  
	'/mnt/dbvol/.ACFS/snaps/clone/oradata/AB112685643A0B77E053FE5E1F0A7BDD/datafile/o1_mf_sysaux_hkpjnmfm_.dbf',  
	'/mnt/dbvol/.ACFS/snaps/clone/oradata/AB112685643A0B77E053FE5E1F0A7BDD/datafile/o1_mf_undotbs1_hkpjnqjz_.dbf',  
	'/mnt/dbvol/.ACFS/snaps/clone/oradata/AB112685643A0B77E053FE5E1F0A7BDD/datafile/o1_mf_undo_2_hkpjnqk7_.dbf',  
	'/mnt/dbvol/.ACFS/snaps/clone/oradata/AB112685643A0B77E053FE5E1F0A7BDD/datafile/o1_mf_users_hkpjnygh_.dbf',  
	'/mnt/dbvol/.ACFS/snaps/clone/oradata/AB112685643A0B77E053FE5E1F0A7BDD/datafile/o1_mf_soe_hkpjnyv6_.dbf'
	CHARACTER SET AL32UTF8;
	-- 
	-- 
	-- Create log files for threads other than thread one.
	ALTER DATABASE ADD LOGFILE THREAD 2
	GROUP 3 SIZE 4096M BLOCKSIZE 512 ,
	GROUP 4 SIZE 4096M BLOCKSIZE 512 ,
	GROUP 7 SIZE 4096M BLOCKSIZE 512 ,
	GROUP 8 SIZE 4096M BLOCKSIZE 512 ;
	-- Database can now be opened zeroing the online logs.
	ALTER DATABASE OPEN RESETLOGS;
	-- Open all the PDBs.
	ALTER PLUGGABLE DATABASE ALL OPEN;
	-- Commands to add tempfiles to temporary tablespaces.
	-- Online tempfiles have complete space information.
	-- Other tempfiles may require adjustment.
	ALTER TABLESPACE TEMP ADD TEMPFILE
	     SIZE 32768M  AUTOEXTEND ON NEXT 16384M MAXSIZE 524288M;
	ALTER SESSION SET CONTAINER = PDB$SEED;
	ALTER TABLESPACE TEMP ADD TEMPFILE
	     SIZE 32767M  AUTOEXTEND OFF;
	ALTER SESSION SET CONTAINER = PDB201;
	ALTER TABLESPACE TEMP ADD TEMPFILE
	     SIZE 32768M  AUTOEXTEND ON NEXT 16384M MAXSIZE 524288M;
	ALTER SESSION SET CONTAINER = PDB202;
	ALTER TABLESPACE TEMP ADD TEMPFILE
	     SIZE 32768M  AUTOEXTEND ON NEXT 16384M MAXSIZE 524288M;
	ALTER SESSION SET CONTAINER = PDB203;
	ALTER TABLESPACE TEMP ADD TEMPFILE
	     SIZE 32768M  AUTOEXTEND ON NEXT 16384M MAXSIZE 524288M;
	ALTER SESSION SET CONTAINER = CDB$ROOT;
	-- End of tempfile additions.
	shutdown immediate
	exit
	```
6. Edit the PFILE backed up in step 3 above. Note that the `db_name` will remain the same for the database clone as well but `db_unique_name` needs to be different. The RAC instances too should derive their names from `db_unique_name`. Make sure that the file paths are pointing the corresponding locations inside the snaps. The required changes are summarized below:
	- New parameter to be added:
		```
		*.db_unique_name='clone'
		```
	- Change existing instance names to new ones:
		- Old:
			```
			source1.instance_number=1
			source2.instance_number=2
			source1.thread=1
			source2.thread=2
			source1.undo_tablespace='UNDOTBS1'
			source2.undo_tablespace='UNDOTBS2'
			```
			- New:
			```
			clone1.instance_number=1
			clone2.instance_number=2
			clone1.thread=1
			clone2.thread=2
			clone1.undo_tablespace='UNDOTBS1'
			clone2.undo_tablespace='UNDOTBS2'
			```
	Make similar changes to all occurrences of instance names.
	Note that in the case of RAC databases, the clone instance should first be started in exclusive mode and then restarted in clustered mode after the clone has been created. In such cases, comment out the `CLUSTER_DATABASE` parameter in the PFILE:
	```
	*.cluster_database=true
	```
	Change parameters in the pfile to account for new datafile, archive log and controlfile locations in the snapshot:
	- Old:
		```
		*.db_create_file_dest='/mnt/dbvol/oradata'
		*.log_archive_dest_1='LOCATION=/mnt/rvol/archive1'
		*.control_files='/mnt/dbvol/oradata/SOURCE/controlfile/o1_mf_hf9cjtv0_.ctl','/mnt/rvol/fast_recovery_area/SOURCE/controlfile/o1_mf_hf9cjtxr_.ctl'
		```
	- New:
		```
		*.db_create_file_dest='/mnt/dbvol/.ACFS/snaps/clone/oradata'
		*.log_archive_dest_1='LOCATION=/mnt/rvol/archive1'
		*.control_files='/mnt/dbvol/.ACFS/snaps/clone/oradata1/ctrl_1_.ctl'
		```
	Give a new location for the audit trace files for the clone:
	```
	*.audit_file_dest='/u01/app/oracle/admin/clone/adump'
	```
	Create the above directory if not present already.
	```
	$ mkdir –p /u01/app/oracle/admin/clone/adump
	```
7. Copy the modified PFILE from the `$ORACLE_HOME/dbs` directory and rename it as an ` init.ora` file to match the local clone database instance name. For example: `$ cp /tmp/clone_pfile.ora                         $ORACLE_HOME/dbs/initclone1.ora`
8. Copy the password file from the source database to a new file name for the clone:
	```
	$ cp <Directory where password file is stored>/orapwsource /mnt/dbvol/.ACFS/snaps/clone/orapwclone
	```
9. Set `ORACLE_SID` to point to the new SID and run the SQL script that you generated in step 5.
	```
	[oracle@machine dbclone]$ export ORACLE_SID=clone1
	[oracle@machine dbclone]$ sqlplus / as sysdba
	 
	SQL*Plus: Release 19.0.0.0.0 - Production on Tue Jun 16 04:50:21 2020
	Version 19.7.0.0.0
	 
	Copyright (c) 1982, 2020, Oracle.  All rights reserved.
	 
	Connected to an idle instance.
	 
	SQL> spool startup.log
	SQL> @ctlfile
	ORACLE instance started.
	 
	Total System Global Area 8.1068E+10 bytes
	Fixed Size                 30383424 bytes
	Variable Size            1.1006E+10 bytes
	Database Buffers         6.9793E+10 bytes
	Redo Buffers              238051328 bytes
	 
	Control file created.
	System altered.
	Database altered.
	Pluggable database altered.
	Tablespace altered.
	Session altered.
	Tablespace altered.
	Session altered.
	Tablespace altered.
	Session altered.
	Tablespace altered.
	.........................
	.........................
	.........................
	.........................
	```
10. The DB is now mounted in exclusive mode on the first node. If the test master database is a RAC database and you wish to enable RAC on the snapshot, shutdown the database and restart the instance with " `cluster_database=true` " parameter set in the pfile. Create an spfile and store it in the the ACFS database file system. Once this is done, we can start both the RAC instances and have the DB running on all the nodes.
	```
	SQL> create spfile=’/mnt/dbvol/.ACFS/snaps/clone/oradata/spfileclone.ora’ from pfile=”<ORACLE_HOME>/dbs/initclone1.ora’
	```
	Add the database and its properties to Cluster Ready Services (CRS)
	```
	$ srvctl add database -db clone -oraclehome $ORACLE_HOME -dbtype RAC -spfile /mnt/dbvol/.ACFS/snaps/clone/oradata/spfileclone.ora -pwfile /mnt/dbvol/.ACFS/snaps/clone/orapwclone -dbname source -acfspath "/mnt/dbvol,/mnt/rvol" -policy AUTOMATIC -role PRIMARY
	```
	Add the instances for each node/instance of the cluster:
	```
	$ srvctl add instance -db clone -instance clone -node <node hostname>
	```
11. Check the archive logs are using the new destination:
	```
	SQL> archive log list
	Database log mode              Archive Mode
	Automatic archival             Enabled
	Archive destination            /mnt/rvol/archive1
	Oldest online log sequence     489
	Next log sequence to archive   490
	Current log sequence           490
	SQL>
	```
	Check if clustered database mode is used:
	```
	SQL> SHOW PARAMETER cluster_database
	 
	NAME                                 TYPE        VALUE
	------------------------------------ ----------- ------------------------------
	cluster_database                     boolean     TRUE
	cluster_database_instances           integer     2
	SQL>
	```
	For RAC environments, be sure to use the srvctl start database and stop database commands as appropriate to help ensure the database is configured correctly.
12. Make sure that all PDBs in the clone can be opened and used.
	```
	SQL> SELECT open_mode FROM v$pdbs;
	 
	OPEN_MODE
	----------
	READ ONLY
	READ WRITE
	READ WRITE
	READ WRITE
	READ WRITE
	READ WRITE
	READ WRITE
	READ WRITE
	READ WRITE
	READ WRITE
	READ WRITE
	 
	11 rows selected.
	 
	 
	SQL> ALTER SESSION SET CONTAINER=SOURCEPDB1;
	 
	Session altered.
	 
	SQL> SELECT name FROM v$tablespace;
	 
	NAME
	------------------------------
	SYSTEM
	SYSAUX
	UNDOTBS1
	UNDO_2
	USERS
	USER_TBS
	LOB_TBS
	FLASHBACK_TBS
	TEMP
	USER_TEMP
	 
	10 rows selected.
	 
	SQL>
	```

The DB clone is now fully ready and can be used for running tests. While the clone is up and running, additional clones can be created from this or from the test master. This way, any number of DB clones can be easily created using ACFS snapshot technology.

It is also recommended to add services for these new DB clones similar to what is used for the parent (or as needed by your applications).

### Oracle ACFS Loopback Support

Oracle ACFS supports loopback functionality on the Linux operating system, enabling Oracle ACFS files to be accessed as devices.

An Oracle ACFS loopback device is an operating system pseudo-device that enables an Oracle ACFS file to be accessed as a block device. This functionality can be used with Oracle Virtual Machines (OVM) in support of OVM images, templates, and virtual disks (vdisks) created in Oracle ACFS file systems and presented through Oracle ACFS loopback devices.

Oracle ACFS loopback functionality provides performance gains over NFS. Files can be sparse or non-sparse.

In addition to general loopback support, Oracle ACFS also provides support for loopback direct I/O (DIO) on sparse images.

### Oracle ACFS Drivers Resource Management

Oracle ACFS, Oracle ADVM, and OKS drivers are loaded during the start of the Oracle Grid Infrastructure stack, except in an Oracle Restart configuration. The drivers remain loaded until the system is rebooted, at which point, they are loaded again when the Oracle Grid Infrastructure stack restarts.

For information about commands to manage Oracle ACFS, Oracle ADVM, and OKS drivers, refer to " Oracle ACFS Driver Commands ".

### Oracle ACFS Registry Resource Management

The Oracle ACFS registry resource is supported only for Oracle Grid Infrastructure cluster configurations; it is not supported for Oracle Restart configurations. See " Oracle ACFS and Oracle Restart ".

With Oracle ASM 12c Release 1 (12.1), the Oracle ACFS registry uses the standard single file system resource available through the SRVCTL file system interface. For more information, refer to " Oracle ACFS File System Resource Management ". Using SRVCTL enables applications to depend on registered file systems, such as for management of the registered file systems using `srvctl` `filesystem`. By default, `acfsutil` `registry` shows only file systems that are set to be always mounted, with the `AUTO_START` attribute set to `always`.

The Oracle ACFS registry requires root privileges to register and delete file systems, however, other users can be entitled to start and stop (mount and unmount) the file systems by use of the `user` option.

### Oracle ACFS File System Resource Management

The Oracle ACFS file system resource is supported only for Oracle Grid Infrastructure cluster configurations; it is not supported for Oracle Restart configurations. See " Oracle ACFS and Oracle Restart ".

Oracle ASM Configuration Assistant (ASMCA) facilitates the creation of Oracle ACFS file system resources (`ora.``diskgroup``.``volume``.acfs`). During database creation with Database Configuration Assistant (DBCA), the Oracle ACFS file system resource is included in the dependency list of its associated disk group so that stopping the disk group also attempts to stop any dependent Oracle ACFS file systems.

An Oracle ACFS file system resource is typically created for use with application resource dependency lists. For example, if an Oracle ACFS file system is configured for use as an Oracle Database home, then a resource created for the file system can be included in the resource dependency list of the Oracle Database application. This dependency causes the file system and stack to be automatically mounted due to the start action of the database application.

The start action for an Oracle ACFS file system resource is to mount the file system. This Oracle ACFS file system resource action includes confirming that the associated file system storage stack is active and mounting the disk group, enabling the volume file, and creating the mount point if necessary to complete the mount operation. If the file system is successfully mounted, the state of the resource is set to `online`; otherwise, it is set to `offline`.

The check action for an Oracle ACFS file system resource verifies that the file system is mounted. It sets the state of the resource to `online` status if mounted, otherwise the status is set to `offline`.

The stop action for an Oracle ACFS file system resource attempts to dismount the file system. If the file system cannot be dismounted due to open references, the stop action displays and logs the process identifiers for any processes holding a reference.

Use of the `srvctl` `start` and `stop` actions to manage the Oracle ACFS file system resources maintains their correct resource state.

### Oracle ACFS and Oracle Restart

Oracle Restart does not support root-based Oracle ACFS resources for this release. Consequently, the following operations are not automatically performed:

- Loading Oracle ACFS drivers
	On Linux, drivers are automatically loaded and unloaded at system boot time and system shutdown time. If an action is required while the system is running or the system is running on other operating system (OS) versions, you can load or unload the drivers manually with the `acfsload` command. However, if the drivers are loaded manually,then the Oracle ACFS drivers must be loaded before the Oracle Restart stack is started.
	For more information, refer to acfsload.
- Mounting Oracle ACFS file systems listed in the Oracle ACFS mount registry
	The Oracle ACFS mount registry is not supported in Oracle Restart. However, Linux entries in the `/etc/fstab` file with a valid Oracle ASM device do have the associated volume enabled and are automatically mounted on system startup and unmounted on system shutdown. Note that high availability (HA) recovery is not applied after the file system is mounted; that functionality is a one time action.
	A valid `fstab` entry has the following format:
	```
	device mount_point acfs noauto 0 0
	```
	For example:
	```
	/dev/asm/dev1-123 /mntpoint acfs noauto 0 0
	```
	The last three fields in the previous example prevent Linux from attempting to automatically mount the device and from attempting to run other system tools on the device. This action prevents errors when the Oracle ASM instance is not available at times during the system startup. Additional standard `fstab` syntax options may be added for the file system mount.
	Should a mount or unmount operation be required on other OS versions, or after the system is started, you can mount Oracle ACFS file systems manually with the `mount` command. For information, refer to [Managing Oracle ACFS with Command-Line Tools](manage-acfs-advm-commands.md).
- Mounting resource-based Oracle ACFS database home file systems
	The Oracle ACFS resources associated with these actions are not created for Oracle Restart configurations. While Oracle ACFS resource management is fully supported for Oracle Grid Infrastructure configurations, the Oracle ACFS resource-based management actions must be replaced with alternative, sometimes manual, operations in Oracle Restart configurations. During an attempt to use commands, such as `srvctl`, that register a root-based resource in Oracle Restart configurations, an appropriate error is displayed.

### Oracle ACFS Driver Commands

This section describes the Oracle ACFS driver commands that are used during installation to manage Oracle ACFS, Oracle ADVM, and Oracle Kernel Services Driver (OKS) drivers. These commands are located in the `/bin` directory of the Oracle Grid Infrastructure home.

- acfsload
- acfsdriverstate

#### acfsload

Purpose

`acfsload` loads or unloads Oracle ACFS, Oracle ADVM, and Oracle Kernel Services Driver (OKS) drivers.

Syntax

```
acfsload { start | stop  } [ -s ]
```

`acfsload` `—h` displays help text and exits.

Table 7-2 contains the options available with the `acfsload` command.

Table 7-2 Options for the acfsload command

| Option | Description |
| --- | --- |
| `start` | Loads the Oracle ACFS, Oracle ADVM, and OKS drivers. |
| `stop` | Unloads the Oracle ACFS, Oracle ADVM, and OKS drivers. |
| `-s` | Operate in silent mode. |

Description

You can use `acfsload` to manually load or unload the Oracle ACFS, Oracle ADVM, and OKS drivers.

Before unloading drivers with the `stop` option, you must dismount Oracle ACFS file systems and shut down Oracle ASM. For information about dismounting Oracle ACFS file systems, refer to [Deregistering, Dismounting, and Disabling Volumes and Oracle ACFS File Systems](steps-manage-acfs.md).

`root` or administrator privilege is required to run `acfsload`.

Examples

The following is an example of the use of `acfsload` to stop (unload) all drivers.

```
# acfsload stop
```

#### acfsdriverstate

Purpose

`acfsdriverstate` provides information on the current state of the Oracle ACFS, Oracle ADVM, and Oracle Kernel Services Driver (OKS) drivers.

Syntax

```
acfsdriverstate [-orahome ORACLE_HOME ] 
    { installed | loaded | version [-v] | supported [-v]} [-s]
```

`acfsdriverstate` `—h` displays help text and exits.

Table 7-3 contains the options available with the `acfsdriverstate` command.

Table 7-3 Options for the acfsdriverstate command

| Option | Description |
| --- | --- |
| `-orahome` `ORACLE_HOME` | Specifies the Oracle Grid Infrastructure home in which the user has permission to execute the `acfsdriverstate` command. |
| `installed` | Determines whether Oracle ACFS is installed on the system. |
| `loaded` | Determines whether the Oracle ADVM, Oracle ACFS, and OKS drivers are loaded in memory. |
| `version` | Reports the currently installed version of the Oracle ACFS system software. |
| `supported` | Reports whether the system is a supported kernel for Oracle ACFS. |
| `-s` | Specifies silent mode when running the command. |
| `-v` | Specifies verbose mode for additional details. |

Description

You can use `acfsdriverstate` to display detailed information on the current state of the Oracle ACFS, Oracle ADVM, and OKS drivers.

Examples

The following is an example of the use of `acfsdriverstate`.

```
$ acfsdriverstate version
ACFS-9325:     Driver OS kernel version = 3.8.13-13.el6uek.x86_64.
ACFS-9326:     Driver build number = 171126.
ACFS-9212:     Driver build version = 18.1.0.0 ()..
ACFS-9547:     Driver available build number = 171126.
ACFS-9548:     Driver available build version = 18.1.0.0 ()..
```

### Oracle ACFS Plug-in Generic Application Programming Interface

Oracle ACFS plug-in operations are supported through a common, operating system (OS) independent file plug-in (C library) application programming interface (API).

The topics contained in this section are:

- Oracle ACFS Pre-defined Metric Types
- Oracle ACFS Plug-in APIs

For more information about Oracle ACFS plug-ins, refer to " [Oracle ACFS Plugins](understand-acfs-admin.md) ".

#### Oracle ACFS Pre-defined Metric Types

Oracle ACFS provides the `ACFSMETRIC1_T` and `ACFSMETRIC2_T` pre-defined metric types.

The `ACFSMETRIC1_T` metric set is defined for the storage virtualization model. The metrics are maintained as a summary record for either a selected set of tagged files or all files in the file system. Oracle ACFS file metrics include: number of reads, number of writes, average read size, average write size, minimum and maximum read size, minimum and maximum write size, and read cache (VM page cache) hits and misses.

Example:

```
typedef struct _ACFS_METRIC1 {
    ub2      acfs_version;
    ub2      acfs_type;
    ub4      acfs_seqno;
    ub8      acfs_nreads;
    ub8      acfs_nwrites;
    ub8      acfs_rcachehits;
    ub4      acfs_avgrsize;
    ub4      acfs_avgwsize;
    ub4      acfs_minrsize;
    ub4      acfs_maxrsize;
    ub4      acfs_minwsize;
    ub4      acfs_maxwsize;
    ub4      acfs_rbytes_per_sec;
    ub4      acfs_wbytes_per_sec;
    ub8      acfs_timestamp;
    ub8      acfs_elapsed_secs;
} ACFS_METRIC1;
```

The `ACFSMETRIC2_T` is a list of Oracle ACFS write description records containing the `fileID`, starting offset, size, and sequence number of each write. The sequence number preserves the Oracle ACFS write record order as preserved by the plug-in driver. The sequence number provides a way for applications to order multiple message buffers returned from the API. It also provides detection of dropped write records due to the application not draining the message buffers fast enough through the API.

The write records are contained within multiple in-memory arrays. Each array of records may be fetched with the API with a buffer size currently set to 1 M. At the beginning of the fetched `ioctl` buffer is a `struct` which describes the array, including the number of records it contains. The kernel buffers drop the oldest write records if the buffers are filled because the buffers are not being read quickly enough.

Example:

```
typedef struct _ACFS_METRIC2 {
  ub2              acfs_version;
  ub2              acfs_type;
  ub4              acfs_num_recs;
  ub8              acfs_timestamp;
  ACFS_METRIC2_REC acfs_recs[1];
} ACFS_METRIC2;

typedef struct _ACFS_FILE_ID {
  ub8              acfs_fenum;
  ub4              acfs_genum;
  ub4              acfs_reserved1;
}

typedef struct _ACFS_METRIC2_REC {
  ACFS_FILE_ID     acfs_file_id;
  ub8              acfs_start_offset;
  ub8              acfs_size;
  ub8              acfs_seq_num;
} ACFS_METRIC2_rec;
```

#### Oracle ACFS Plug-in APIs

Purpose

The Oracle ACFS plug-in application programming interface (API) sends and receives messages to and from the local plug-in enabled Oracle ACFS driver from the application plug-in module.

Syntax

```
sb8 acfsplugin_metrics(ub4 metric_type,
  ub1 *metrics,
  ub4 metric_buf_len,
  oratext *mountp );
```
```
sb8 acfsfileid_lookup(ACFS_FILEID file_id,
  oratext *full_path,
  oratext *mountp );
```

Description

The `acfsplugin_metrics` API is used by an Oracle ACFS application plug-in module to retrieve metrics from the Oracle ACFS driver. The Oracle ACFS driver must first be enabled for plug-in communication using the `acfsutil` `plugin` `enable` command. The selected application plug-in metric type model must match the plug-in configuration defined with the Oracle ACFS plug-in enable command. For information about the `acfsutil` `plugin` `enable` command, refer to " [acfsutil plugin enable](acfs-commands-utilities.md) ". The application must provide a buffer large enough to store the metric structures described in " Oracle ACFS Pre-defined Metric Types ".

If the provided buffer is `NULL` and `metric_buf_len` `=` `0`, the return value is the size required to hold all the currently collected metrics. The application can first query Oracle ACFS to see how big a buffer is required, then allocate a buffer of the necessary size to pass back to Oracle ACFS.

The mount path must be provided to the API to identify the plug-in enabled Oracle ACFS file system that is being referenced.

A nonnegative value is returned for success: `0` for success with no more metrics to collect, `1` to indicate that more metrics are available, or `2` to indicate that no new metrics were collected during the interval. In the case of an error, a negative value is returned and `errno` is set on Linux environments.

When using metric type #2, the returned metrics include an `ACFS_FILE_ID`, which contains the fenum and genum pair. In order to translate from the fenum and genum pair to a file path, the application can use `acfsfileid_lookup`. The application must provide a buffer of length `ACFS_FILEID_MAX_PATH_LEN` to hold the path. If there are multiple hard links to a file, the returned path is the first one. This is same behavior when using `acfsutil info id`.

System administrator or Oracle ASM administrator privileges are required to send and receive messages to and from the plug-in enabled Oracle ACFS file system driver.

Writing Applications

To use the plugin API, applications must include the C header file `acfslib.h` which defines the API functions and structures.

```
#include <acfslib.h>
```

When building the application executable, the application must be linked with the `acfs12` library. Check the platform-specific documentation for information about environment variables that must be defined. For example:

```
export LD_LIBRARY_PATH=${ORACLE_HOME}/lib:$
{LD_LIBRARY_PATH}
```

Then when linking, add the `-lacfs12` flag.

Examples

In Example 7-1, the command enables an Oracle ACFS file system mounted on `/humanresources` for the plug-in service.

Example 7-1 Application Plug-in for Storage Visibility: Poll Model

```
$ /sbin/acfsutil plugin enable -m acfsmetric1 -t HRDATA /humanresources
```

With this command, the application plug-in polls the Oracle ACFS plug-in enabled driver for summary metrics associated with files tagged with `HRDATA`. The application code includes the following:

```
#include <acfslib.h>
...
/* allocate message buffers */
ACFS_METRIC1 *metrics = malloc (sizeof(ACFS_METRIC1));
/* poll for metric1 data */
while (condition) {
  /* read next summary message from ACFS driver */
   if ((rc = acfsplugin_metrics(ACFS_METRIC_TYPE1,(ub1*)metrics,sizeof(*metrics),
        mountp)) < 0) {
        perror("….Receive failure … ");
        break;
   }
   /* print message data */
   printf ("reads %8llu ", metrics->acfs_nreads);
   printf("writes %8llu ", metrics->acfs_nwrites);
   printf("avg read size %8u ", metrics->acfs_avgrsize);
   printf("avg write size %8u ", metrics->acfs_avgwsize);
   printf("min read size %8u ", metrics->acfs_minrsize);
   printf("max read size %8u ", metrics->acfs_maxrsize);
   ...
   sleep (timebeforenextpoll);
}
```

In Example 7-2, the command enables an Oracle ACFS file system mounted on `/humanresources` for the plug-in service.

Example 7-2 Application Plug-in for File Content: Post Model

```
$ /sbin/acfsutil plugin enable -m acfsmetric1 -t HRDATA -i 5m /humanresources
```

With this command, every 5 minutes the Oracle ACFS plug-in enabled driver posts file content metrics associated with files tagged with `HRDATA`. In the application code, the call to `acfsplugin_metrics()` is blocked until the metrics are posted. The application code includes the following:

```
#include <acfslib.h>
...
 ACFS_METRIC1 *metrics = malloc (sizeof(ACFS_METRIC1));
 
 /* Wait for metric Data */
  while (condition) {
    /* Wait for next file content posting from ACFS driver */
    rc = ACFS_PLUGIN_MORE_AVAIL;
    /* A return code of 1 indicates that more metrics are available
    * in the current set of metrics.
    */
    while( rc == ACFS_PLUGIN_MORE_AVAIL) {
      /* This call blocks until metrics are available. */
      rc = acfsplugin_metrics(ACFS_METRIC_TYPE1,(ub1*)metrics,sizeof(*metrics),
           mountp);
      if (rc < 0) {
        perror("….Receive failure … ");
        break;
      } else if (rc == ACFS_PLUGIN_NO_NEW_METRICS) {
        printf("No new metrics available.");
        break;
     }
     if (last_seqno != metrics->acfs_seqno-1 ) {
       printf("Warning: Unable to keep up with metrics collection.");
       printf("Missed %d sets of posted metrics.",
              (metrics->acfs_seqno-1)-last_seqno);
     }

      /* print message data */ 
      printf ("reads %8llu ", metrics->acfs_nreads);
      printf("writes %8llu ", metrics->acfs_nwrites);
      printf("avg read size %8u ", metrics->acfs_avgrsize);
      printf("avg write size %8u ", metrics->acfs_avgwsize);
      printf("min read size %8u ", metrics->acfs_minrsize);
      printf("max read size %8u ", metrics->acfs_maxrsize);
      ...
 
      last_seqno = metrics->acfs_seqno;
    }
  }
 
  free(metrics);
```

Example 7-3 Application for Resolving the File Path from a Fenum and Genum Pair

### Oracle ACFS Tagging Generic Application Programming Interface

Oracle ACFS tagging operations are supported through a common operating system (OS) independent file tag (C library) application programming interface (API).

An Oracle ACFS tagging API demonstration utility is provided. The demo provides instructions to build the utility with a makefile on each supported platform.

On Solaris, Oracle ACFS tagging APIs can set tag names on symbolic link files, but backup and restore utilities do not save the tag names that are explicitly set on the symbolic link files. Also, symbolic link files lose explicitly set tag names if they have been moved, copied, tarred, or paxed.

The following files are included:

- `$ORACLE_HOME/usm/public/acfslib.h`
- `$ORACLE_HOME/usm/demo/acfstagsdemo.c`
- `$ORACLE_HOME/usm/demo/Makefile`
	Linux, Solaris, or AIX makefile for creating the demo utility.

The topics contained in this section are:

- Oracle ACFS Tag Name Specifications
- Oracle ACFS Tagging Error Values
- acfsgettag
- acfslisttags
- acfsremovetag
- acfssettag

#### Oracle ACFS Tag Name Specifications

An Oracle ACFS tag name can be from 1 to 32 characters in length and consist of a combination of the following set of characters only:

- uppercase and lowercase alphabetic characters (A-Z, a-z)
- numbers (0-9)
- hyphen (-)
- underscore (\_)
- blank (space)

#### Oracle ACFS Tagging Error Values

The following are the values for Linux, Solaris, or AIX `errno` in case of failure:

- `EINVAL` – The tag name syntax is invalid or too long.
- `ENODATA` – The tag name does not exist for this file or directory.
- `ERANGE` - The value buffer is too small to hold the returned value.
- `EACCES` – Search permission denied for a directory in the path prefix of path; or the user does not have permission on the file to read tag names.
- `ENAMETOOLONG` – The file name is too long.
- `ENOENT` – A component of path does not exist.

#### acfsgettag

Purpose

Retrieves the value associated with an Oracle ACFS file tag name.

Syntax

```
sb8 acfsgettag(const oratext *path, const oratext *tagname, oratext *value, 
               size_t size, ub4 flags);
```

Table 7-4 contains the options available with the `acfsgettag` command.

Table 7-4 Options for the acfsgettag command

| Option | Description |
| --- | --- |
| `path` | Specifies a pointer to a file or directory path name. |
| `tagname` | Specifies a pointer to a NULL-terminated Oracle ACFS tag name in the format of a valid tag name for regular files and directories. |
| `value` | Specifies the memory buffer to retrieve the Oracle ACFS tag value. |
| `size` | Specifies the byte size of the memory buffer that holds the returned Oracle ACFS tag value. |
| `flags` | Reserved for future use. Must be set to 0. |

Description

The `acfsgettag` library call retrieves the value string of the Oracle ACFS tag name. The return value is the nonzero byte length of the output `value` string on success or `ACFS_TAG_FAIL` on failure. For information about operating system-specific extended error information values that may be obtained when an `ACFS_TAG_FAIL` is returned, refer to " Oracle ACFS Tagging Error Values ".

Because Oracle ACFS tag names currently use a fixed value string of `0` (the number zero character with a byte length of one) the value is the same for all Oracle ACFS tag name entries. The size of the `value` buffer can be determined by calling `acfsgettag` with a NULL `value` and `0` `size`. The library call returns the byte size necessary to hold the value string of the tag name. `acfsgettag` returns an `ENODATA` error when the tag name is not set on the file.

Examples

Example 7-4 is an example of the use of the `acfsgettag` function call.

Example 7-4 Retrieving a file tag value

```
sb8 rc;
size_t size;
oratext value[2];
const oratext *path = "/mnt/dir1/dir2/file2";
const oratext *tagname = "patch_set_11_1";
size = 1; (byte)
memset((void *)value, 0, 2*sizeof(oratext));
rc = acfsgettag (path, tagname, value, size, 0);
If (rc == ACFS_TAG_FAIL)
  /* check errno or GetLastError() to process error returns /*
```

#### acfslisttags

Purpose

Lists the tag names assigned to an Oracle ACFS file. For additional information, refer to " [acfsutil tag info](acfs-commands-tagging.md) ".

Syntax

```
sb8 acfslisttags(const oratext *path, oratext *list, size_t size, ub4 flags);
```

Table 7-4 contains the options available with the `acfslisttags` command.

Table 7-5 Options for the acfslisttags command

| Option | Description |
| --- | --- |
| `path` | Specifies a pointer to a file or directory path name. |
| `list` | Specifies a pointer to a memory buffer containing the list of Oracle ACFS tag names. |
| `size` | Specifies the size (bytes) of the memory buffer that holds the returned Oracle ACFS tag name list. |
| `flags` | Reserved for future use. Must be set to 0. |

Description

The `acfslisttags` library call retrieves all the tag names assigned to an Oracle ACFS file. `acfslisttags` returns a list of tag names into the `list` memory buffer. Each tag name in the list is terminated with a NULL. If a file has no tag names then the list is empty. The memory buffer must be large enough to hold all of the tag names assigned to an Oracle ACFS file.

An application must allocate a buffer and specify a list size large enough to hold all of the tag names assigned to an Oracle ACFS file. An application can optionally obtain the list buffer size needed by first calling `acfslisttags` with a zero value buffer size and NULL list buffer. The application then checks for nonzero, positive list size return values to allocate a list buffer and call `acfslisttags` to retrieve the actual tag name list.

On success, the return value is a positive byte size of the tag name list or `0` when the file has no tag names. On failure, the return value is `ACFS_TAG_FAIL`. For information about operating system-specific extended error information values that may be obtained when an `ACFS_TAG_FAIL` is returned, refer to " Oracle ACFS Tagging Error Values ".

Examples

Example 7-5 is an example of the use of the `acfslisttags` function call.

Example 7-5 Listing file tags

```
sb8 listsize;
sb8 listsize2;
const oratext *path = "/mnt/dir1/dir2/file2";
oratext *list;
/* Determine size of buffer to store list */
listsize = acfslisttags (path, NULL, 0, 0);
if (listsize == ACFS_TAG_FAIL)
/* retrieve the error code and return */

if (listsize)
{
    list = malloc(listsize)
    /* Retrieve list of tag names */
    listsize2 = acfslisttags (path, list, listsize, 0);
    if (listsize2 == ACFS_TAG_FAIL)
        /* check errno or GetLastError() to process error returns */
    if (listsize2 > 0)
        /* file has a list of tag names to process */
    else
        /* file has no tag names. */
}
else
/* file has no tag names. */
```

#### acfsremovetag

Purpose

Removes the tag name on an Oracle ACFS file.

Syntax

```
sb8 acfsremovetag(const oratext *path, const oratext *tagname, ub4 flags);
```

Table 7-6 contains the options available with the `acfsremovetag` command.

Table 7-6 Options for the acfsremovetag command

| Option | Description |
| --- | --- |
| `path` | Specifies a pointer to a file or directory path name. |
| `tagname` | Specifies a pointer to a NULL-terminated Oracle ACFS tag name in the format of a valid tag name for regular files and directories. |
| `flags` | Reserved for future use. Must be set to `0`. |

Description

The `acfsremovetag` library call removes a tag name on an Oracle ACFS file. The return value is `ACFS_TAG_SUCCESS` or `ACFS_TAG_FAIL`. For information about operating system-specific extended error information values that may be obtained when an `ACFS_TAG_FAIL` is returned, refer to " Oracle ACFS Tagging Error Values ".

Examples

Example 7-6 is an example of the use of the `acfsremovetag` function call.

Example 7-6 Removing file tags

```
sb8 rc;
const oratext *path= "/mnt/dir1/dir2/file2";
const oratext *tagname = "patch_set_11_1";
rc = acfsremovetag (path, tagname, 0);
If (rc == ACFS_TAG_FAIL)
  /* check errno or GetLastError() to process error returns */
```

#### acfssettag

Purpose

Sets the tag name on an Oracle ACFS file. For additional information, refer to " [acfsutil tag set](acfs-commands-tagging.md) ".

Syntax

```
sb8 acfssettag(const oratext *path, const oratext *tagname, oratext *value, 
               size_t size, ub4 flags);
```

Table 7-7 contains the options available with the `acfssettag` command.

Table 7-7 Options for the acfssettag command

| Option | Description |
| --- | --- |
| `path` | Specifies a pointer to a file or directory path name. |
| `tagname` | Specifies a pointer to a NULL-terminated Oracle ACFS tag name in the format of a valid tag name for regular files and directories. |
| `value` | Specifies the memory buffer to set the Oracle ACFS tag value. |
| `size` | Specifies the byte size of the Oracle ACFS tag value. |
| `flags` | Reserved for future use. Must be set to 0. |

Description

The `acfssettag` library call sets a tag name on an Oracle ACFS file. The return value is `ACFS_TAG_SUCCESS` or `ACFS_TAG_FAIL`. For information about operating system-specific extended error information values that may be obtained when an `ACFS_TAG_FAIL` is returned, refer to " Oracle ACFS Tagging Error Values ".

Because Oracle ACFS tag names currently use a fixed value string of `0` (the number zero character with a byte length of one) the `value` is the same for all Oracle ACFS tag name entries.

Examples

Example 7-7 is an example of the use of the `acfssettag` function call.

Example 7-7 Setting file tags

```
sb8 rc;
size_t size;
const oratext *value ;
const oratext *path= "/mnt/dir1/dir2/file2";
const oratext *tagname = "patch_set_11_1";
value = "0"; /* zero */
size = 1; (byte)
rc = acfssettag (path, tagname, (oratext *)value, size, 0);
If (rc == ACFS_TAG_FAIL)
  /* check errno and GetLastError() to process error returns */
```

### Oracle ACFS Diagnostic Commands

This topic provides a summary of the Oracle ACFS command-line utilities for diagnostic purposes.

Oracle ACFS provides various `acfsutil` command-line utilities for diagnostic purposes.

Note:

Run the diagnostic commands only when Oracle Support requests diagnostic data for analysis.

The following table lists the Oracle ACFS utilities with brief descriptions.

For information about running Oracle ACFS `acfsutil` commands, refer to [About Using Oracle ACFS Command-Line Tools](steps-manage-acfs.md).

Table 7-8 Summary of Oracle ACFS diagnostic commands

| Command | Description |
| --- | --- |
| acfsdbg | Debugs an Oracle ACFS file system. |
| acfsutil blog | Writes text to a blog file. |
| acfsutil dumpstate | Collects internal Oracle ACFS state information. |
| acfsutil info ftrace | Display the trace entries for open files. |
| acfsutil lockstats | Displays lock contention statistics. |
| acfsutil log | Retrieves memory diagnostic log files and manages debug settings. |
| acfsutil meta | Copies metadata from an Oracle ACFS file system into a separate output file. |
| acfsutil plogconfig | Manages Oracle ACFS persistent logging configuration settings. |
| acfsutil tune | Modifies or displays Oracle ACFS tunable parameters. |
| advmutil tune | Modifies or displays Oracle ADVM parameters. |

#### acfsdbg

Purpose

Debugs an Oracle ACFS file system.

Syntax and Description

```
acfsdbg [-r] [-l] [-x] volume_device
acfsdbg -h
```

For information about running Oracle ACFS `acfsutil` commands, refer to [About Using Oracle ACFS Command-Line Tools](steps-manage-acfs.md).

The following table contains the options available with the `acfsdbg` command.

Table 7-9 Options for the acfsdbg command

| Option | Description |
| --- | --- |
| `-h` | Prints out the usage message which displays the various options that are available when invoking the `acfsdbg` command, then exits. |
| `-r` | Operates in read-only mode. No data is modified on the file system and all write commands are disabled. If the device is mounted anywhere, `acfsdbg` may not display the latest data because some data is cached by the file system mounts. |
| `-l` | Processes kernel log files. The default is to not process the log files. |
| `—x file_name` | Specified for accelerator data collected by `acfsutil meta`. Only used for this type of data. |
| `volume_device` | Specifies the device name of the volume. |

You must be the administrator or a member of the Oracle ASM administrator group to run `acfsdbg`.

Subcommands

Table 7-10 lists the subcommands of `acfsdbg`.

Table 7-10 Subcommands for acfsdbg

| Option | Description | Syntax |
| --- | --- | --- |
| `calculate` | Calculates simple arithmetic expressions  Valid operators: + - \* / % & \| ^ ~ << >>  White space starts a new expression  0-1 represents a negative 1 | `calculate` \[`-v`\] `expr` \[…\]  - `-v` Verbose mode - `expr` Simple 2+2 expression |
| `cksum` | Generates and replaces checksum in header  Header offset can be an expression as used by the `calculate` subcommand  White space starts a new header offset  Command is disabled in read-only mode | `cksum` \[`-C` \| `-CE`\] `header_offset` \[…\]  - `-C` Regenerate for normal structure checksum - `-CE` Re-generate for Extent structure checksum - `header_offset` Offset of the on disk structure header. The value can be an expression as used by the `calculate` subcommand |
| `close` | Closes the open handle to the device | `close` |
| `echo` | Echoes text on command line to stdout | `echo` |
| `fenum` | Displays the specified File Entry TAble (FETA) entry | `fenum` \[`-f` \| `-e` \| `-d`\] `FETA_entry_number`  - `-f` Displays all on disk structures related to this structure - `-e` Displays all on disk extent information related to this structure - `-d` Casts the structure as a directory and displays its contents - `FETA_entry_number` The File Entry Table number used to identify a file on the file system |
| `help` | Displays help message | `help` |
| `offset` | Displays structure at disk offset | `offset` \[`-c cast`\] \[`-f` \| `-d`\] `disk_offset`  - `-f` Displays all on disk structures related to this structure - `-d` Casts the structure as a directory and displays its contents - `disk_offset` Disk offset to display. The value can be an expression as used by the `calculate` subcommand |
| `open` | Opens a handle to a device. The default is the volume device name entered on the command line | `open` \[`volume_device`\] |
| `primary` | Sets the context of commands to the primary file system | `primary` |
| `prompt` | Sets the prompt to the specified string | `prompt` " `prompt_string` " |
| `quit` | Exits the `acfsdbg` debugger command | `quit` |
| `read` | Reads value from offset  The default size to read in is 8 bytes  The default count to read is 1 | `read` \[`-1` \| `-2` \| `-4` \| `-8` \| `-s`\] \[`count`\] `offset`  - `-1` Read byte value - `-2` Read 2 byte (short) value - `-4` Read 4 byte (int) value - `-8` Read 8 byte (long) value - `-s` Read null- terminated string - `count` Number of values to read. If not specified, the default is 1 - `offset` Disk offset to read. The value can be an expression as used by the `calculate` subcommand |
| `snapshot` | Sets the context of commands to the specified snapshot | `snapshot` `snapshot_name` |
| `write` | Writes hexadecimal, octal, or decimal values at the disk offset, estimating how many bytes to write based on value size or number of digits in leading 0 hexadecimal values  The disk offset can be an expression used by the `calculate` subcommand  Numeric values can also be an expression as used by the `calculate` subcommand  This command is disabled in read-only mode | `write` \[`-1` \| `-2` \| `-4` \| `-8` \| `-c` \| `-s`\] \[`-C` \| `-CE`\] `offset` `value`  - `-1` Write byte value - `-2` Write 2 byte (short) value - `-4` Write 4 byte (int) value - `-8` Write 8 byte (long) value - `-c` Write text (no null termination). Enclose string in single-quotes (') - `-s ` Write null-terminated string. Enclose string in quotes (") - `-C` Regenerate normal structure checksum - `-CE` Regenerate extent structure checksum - `offset` Disk offset to write. The value can be an expression used by the `calculate` subcommand - `value` The value to write. If numeric, the value can be an expression as used by the `calculate` subcommand |

Examples

Example 7-8 shows the use of the `acfsdbg` subcommand.

Example 7-8 Using the acfsdbg command

```
$ /sbin/acfsdbg /dev/asm/voume1-123
acfsdbg: version                   = 11.2.0.3.0
Oracle ASM Cluster File System (ACFS) On-Disk Structure Version: 39.0
The ACFS volume was created at  Mon Mar  2 14:57:45 2011
acfsdbg> 

acfsbdg> calculate 60*1024
    61,440
    61440
    61440
    0xf000
    0170000
    1111:0000:0000:0000

acfsdbg> prompt "acfsdbg test>"
acfsdbg test>

echo "offset 64*1024" | acfsdbg /dev/asm/volume1-123
```

#### acfsutil blog

Purpose

Writes text to the blog file.

Syntax and Description

```
acfsutil [-h] blog

acfsutil blog {-t text | -u} mount_point
```

For information about running Oracle ACFS `acfsutil` commands, refer to [About Using Oracle ACFS Command-Line Tools](steps-manage-acfs.md).

The following table contains the options available with the `acfsutil` `blog` command.

Table 7-11 Options for the acfsutil blog command

| Option | Description |
| --- | --- |
| `-t text` | Writes text to the blog file at the specified mount point. |
| `-u` | Updates blog debug levels from `dbg` file. |
| `mount_point` | Specifies the mount point. |

The `acfsutil` `blog` command enables you to write text to a blog file.

.

Examples

The following example illustrates how to run the `acfsutil` `blog` command. Running `acfsutil` `blog` with the `—h` option displays help.

Example 7-9 Using acfsutil blog

```
$ /sbin/acfsutil -h

$ /sbin/acfsutil -t "this is a blog test" blog my_mount_point

$ /sbin/acfsutil -u blog my_mount_point
```

#### acfsutil dumpstate

Purpose

Collects internal Oracle ACFS state information for diagnosis by Oracle support.

Syntax and Description

```
acfsutil [-h] dumpstate 
acfsutil dumpstate {acfs_path | [-d [-p {file_name | -}]] [-z] [acfs_path]}
```

`acfsutil` `-h` `dumpstate` displays help text and exits.

For information about running Oracle ACFS `acfsutil` commands, refer to [About Using Oracle ACFS Command-Line Tools](steps-manage-acfs.md).

The following table contains the options available with the `acfsutil` `dumpstate` command.

Table 7-12 Options for the acfsutil dumpstate command

| Option | Description |
| --- | --- |
| acfs\_path | Specifies the directory path to an Oracle ACFS file system. |
| `-d` | Dump statistics to `acfs.dumpstats` in the current directory or the output specified by the `-p` option. |
| `-p` `{ file_name \| - }` | Modifies the `-d` option to specify a file name instead of `acfs.dumpstats`. You can also specify `-` in place of a file name to display the output instead of writing to a file. |
| `-z` | Clears all current statistics. |

The `acfsutil` `dumpstate` command collects internal Oracle ACFS state information for a specified file system. The state information is written to a binary incident file in a logging directory. The binary log incident file is specific to the file system mounted at the specified path. The `acfs.dumpstats` statistics file, or the specified alternate output, contains statistics for the entire Oracle ACFS kernel module.

Note:

Run the `acfsutil` `dumpstate` command only when Oracle Support requests diagnostic and debugging data for analysis.

Examples

The following example shows the use of the `acfsutil` `dumpstate` command.

Example 7-10 Using the acfsutil dumpstate command

The following command execution creates a binary incident file for the specified file system.

```
$ /sbin/acfsutil dumpstate /acfsmounts/acfs1/
```

The following command execution dumps file system statistics to `acfs.dumpstats` and creates a binary incident file for the specified file system.

```
$ /sbin/acfsutil dumpstate -d /acfsmounts/acfs1/
```

The following command execution clears statistics for all file systems.

```
$ /sbin/acfsutil dumpstate -z
```

The following command execution dumps file system statistics to `acfs.dumpstats`, creates a binary incident file, and clears all file system statistics for the specified file system.

```
$ /sbin/acfsutil dumpstate -d -z /acfsmounts/acfs1/
```

#### acfsutil info ftrace

Purpose

Display the trace entries for open files associated with the Oracle ACFS file system specified by the mount point.

Syntax and Description

```
acfsutil info ftrace -h
acfsutil info ftrace [-s] mount_point
```

`acfsutil info ftrace —h` displays help text and exits.

For information about running Oracle ACFS `acfsutil` commands, refer to [About Using Oracle ACFS Command-Line Tools](steps-manage-acfs.md).

The following table contains the options available with the `acfsutil info ftrace` command.

Table 7-13 Options for the acfsutil info ftrace command

| Option | Description |
| --- | --- |
| `—s` | Display only file IDs of open files. |
| `mount_point` | Specifies the directory where the file system is mounted. |

The `acfsutil` `info` `ftrace` command displays a list of open files on a mounted Oracle ACFS file system.

The Oracle ACFS kernel driver keeps track of which files are loaded in memory. These files may not have an active open and may just be cached. The open file tracing is able to determine which of those cached File Control Blocks (FCBs) have an active open or reference. The intent of this command is to enable you to determine if, and which, files are still being referenced that could prevent a file system unmount from occuring.

When `acfsutil` `info` `ftrace` initially runs, the command attempts to purge any cached files that are no longer referenced. This operation may require some time to complete because the modified metadata and user data for each file has to be flushed to disk.

The following describes the output of the `acfsutil` `info` `ftrace` command. Note that a file can refer to a regular file or directory.

The basic format of the output is:

```
Fileid: %ID%, Pathname: %PATH%
          [%OP%] Pid:  %PID% Ppid:   %PPID% Elapsed time: %TIME% Cmd: %CMD%
          ...
```

The fields are described in the following list.

- `%ID%`: The numeric file identifier. This is the same number that is used with `acfsutil` `info` `id`. This value is also known as the inode number on Linux.
- `%PATH%`: The generated pathname for the file based on the `%ID%`. `N/A` may be displayed if it is not available.
- `%OP%:` The type of operation that accessed the file. The values may be the following:
	- `LOOKUP`: The specified process looked up this file via the pathname.
		- `CREATE`: The specified process created the file.
		- `NFS`: A NFS process has accessed the file on behalf of client.
		- `OPEN`: The specified process opened the file.
		- `MAP`: The specified process mapped the file into memory.
- `%PID%`: The process id `%PPID%`: The parent process id. This output item may not be available.
- `%TIME%`: The elapsed time from when the operation occurred. The format is: d (days), h (hours), m (minutes), s (seconds)
- `%CMD%`: The name of the process that performed the operation.

Each file listed may have more than one operation listed depending on the system workload. The amount of operations displayed is limited to conserve memory. The Oracle ACFS driver keeps a rotating log for each operation and the operation entries may wrap. As a result, the oldest operation may not be the first one displayed.

Examples

The following example shows the `acfsutil` `info` `ftrace` command run on the `/mnt` mount point.

Example 7-11 Using the acfsutil info ftrace command

```
$ acfsutil info ftrace /mnt
Fileid: 42, Pathname: /mnt/yum.conf
        [LOOKUP] Pid:  27009 Ppid:  14999 Elapsed time: 0d 00h 00m 03s Cmd: tail
        [OPEN  ] Pid:  27009 Ppid:  14999 Elapsed time: 0d 00h 00m 03s Cmd: tail

Fileid: 155, Pathname: /mnt/bash
        [LOOKUP] Pid:   9731 Ppid:  19588 Elapsed time: 0d 00h 00m 08s Cmd: cp
        [OPEN  ] Pid:   9731 Ppid:  19588 Elapsed time: 0d 00h 00m 08s Cmd: cp
        [OPEN  ] Pid:   9735 Ppid:  19588 Elapsed time: 0d 00h 00m 05s Cmd: bash
        [MAP   ] Pid:   9735 Ppid:  19588 Elapsed time: 0d 00h 00m 05s Cmd: bash
        [MAP   ] Pid:   9735 Ppid:  19588 Elapsed time: 0d 00h 00m 05s Cmd: bash
        [MAP   ] Pid:   9735 Ppid:  19588 Elapsed time: 0d 00h 00m 05s Cmd: bash

Fileid: 43, Pathname: /mnt/dir1
        [LOOKUP] Pid:  14485 Ppid:   7829 Elapsed time: 0d 12h 20m 13s Cmd: mkdir
        [LOOKUP] Pid:   7829 Ppid:   7828 Elapsed time: 0d 12h 20m 06s Cmd: bash
        [LOOKUP] Pid:   7829 Ppid:   7828 Elapsed time: 0d 12h 20m 06s Cmd: bash
```

#### acfsutil lockstats

Purpose

Displays lock contention statistics.

Syntax and Description

```
acfsutil lockstats lh -h
acfsutil lockstats lh [-b] [-e] [-z] [-t top_n] [-s sort_column]
```

`acfsutil lockstats lh —h` displays help text and exits.

For information about running Oracle ACFS `acfsutil` commands, refer to [About Using Oracle ACFS Command-Line Tools](steps-manage-acfs.md).

The following table contains the options available with the `acfsutil lockstats` command.

Table 7-14 Options for the acfsutil lockstats command

| Option | Description |
| --- | --- |
| `—b` | Begins (enables) collecting lock statistics. |
| `—e` | Stops (disables) collecting lock statistics. |
| `—z` | Zeroes out (clears) the current collected lock statistics. |
| `—t top_n` | Displays the top n lock statistics. |
| `—s sort_column` | Sorts the lock statistics on the specified sort column.  Valid sort column values are: `acquires`, `totalwait`, and `maxwait`.  By default, the statistics are sorted by ` Total Wait`. |

The command’s output is displayed in a tabular format with four columns.
- The first column is the lock hierarchy group name.
- The second column is the number of locks acquired in that particular group.
- The third column is the maximum time waited among all the lock acquires.
- The fourth column is the cumulative time waited for all the lock acquires.

Examples

The following example shows multiple ways to use of the `acfsutil` `lockstats` command.

Example 7-12 Using the acfsutil lockstats command

```
# Enable lock statistics collection in the kernel. No data is displayed.
$ acfsutil lockstats lh -b

# Zero out any and all the lock statistics collected. No data is displayed.
$ acfsutil lockstats lh -z

# Disable lock statistics collection in the kernel. No data is displayed.
$ acfsutil lockstats lh -e

# Displays all of the lock statistics, sorted on the total wait column.
$ acfutil lockstats lh

+-------------------------------------+--------------+------------+------------+
|              Lock Type              |   Acquires   |  Max Wait  | Total Wait |
+-------------------------------------+--------------+------------+------------+
| LH_MetabufLock                      |       608763 |          1 |        176 |
| LH_FcbMCBLock                       |       605578 |          1 |         83 |
| LH_IgnoreCompletely                 |      7002105 |          1 |         41 |
| LH_SnapDIOCowLock                   |          295 |          6 |          6 |
| LH_DLM_hash_chain_lock              |       312581 |          1 |          5 |
| LH_OFSBUFHashChain                  |       610118 |          1 |          5 |
| LH_SnapMapLockDLMLock               |          297 |          1 |          1 |
| LH_RemapTableDLMLock                |            3 |          1 |          1 |
| LH_TrackOnly                        |       348954 |          0 |          0 |
| LH_KS_feature_lock                  |           12 |          0 |          0 |
| LH_DLM_rbld_stall_lock              |          199 |          0 |          0 |
| LH_DLM_rsb_incarn_lock              |           68 |          0 |          0 |
| LH_DLM_rsb_lock                     |           81 |          0 |          0 |
| LH_DLM_lkb_lock                     |           83 |          0 |          0 |
| LH_DLM_lkid_lock                    |          194 |          0 |          0 |
| LH_KCSS_comm_lock                   |           11 |          0 |          0 |
| LH_KSS_asm_exit_lock                |           10 |          0 |          0 |
| LH_KCSS_rac_mode_lock               |           21 |          0 |          0 |
| LH_ADVM_hd_lock                     |            1 |          0 |          0 |
| LH_ADVM_rootSpin                    |           90 |          0 |          0 |
| LH_ADVM_root_stateLock              |            1 |          0 |          0 |
.
.
.
| LH_GlobalMntResource                |            4 |          0 |          0 |
| LH_KS_PlogConfigLock                |          587 |          0 |          0 |
+-------------------------------------+--------------+------------+------------+

# Displays only the top 10 lock statistics.
$ acfsutil lockstats lh -t 10

+-------------------------------------+--------------+------------+------------+
|              Lock Type              |   Acquires   |  Max Wait  | Total Wait |
+-------------------------------------+--------------+------------+------------+
| LH_MetabufLock                      |       802244 |          1 |        230 |
| LH_FcbMCBLock                       |       798135 |          1 |        113 |
| LH_IgnoreCompletely                 |      9214061 |          1 |         54 |
| LH_OFSBUFHashChain                  |       803599 |          1 |          7 |
| LH_SnapDIOCowLock                   |          389 |          6 |          6 |
+-------------------------------------+--------------+------------+------------+

# Displays all of the lock statistics, sorted on the ‘Acquires’ column.
$ acfsutil lockstats -s acquires

+-------------------------------------+--------------+------------+------------+
|              Lock Type              |   Acquires   |  Max Wait  | Total Wait |
+-------------------------------------+--------------+------------+------------+
| LH_IgnoreCompletely                 |      9263483 |          1 |         54 |
| LH_OFSBUFHashChain                  |       807734 |          1 |          7 |
| LH_MetabufLock                      |       806379 |          1 |        231 |
| LH_FcbMCBLock                       |       802234 |          1 |        114 |
| LH_TrackOnly                        |       461656 |          0 |          0 |
| LH_DLM_hash_chain_lock              |       312581 |          1 |          5 |
| LH_DLMSpinLock                      |        15982 |          0 |          0 |
| LH_AutoResizeLock                   |         3880 |          0 |          0 |
| LH_SnapMapMetaDataLock              |         2725 |          0 |          0 |
| LH_RecoverySpinLock                 |         2722 |          0 |          0 |
| LH_clean_ofsBufl_lock               |         2580 |          0 |          0 |
| LH_ResizeVOPsLock                   |         2333 |          0 |          0 |
| LH_SBMetaDataLock                   |         2145 |          0 |          0 |
| LH_SBDLMLock                        |         2145 |          0 |          0 |
| LH_FcbListLock                      |         1980 |          0 |          0 |
| LH_VcbDIOSpinLock                   |         1940 |          0 |          0 |
| LH_McbLock                          |         1863 |          0 |          0 |
| LH_UnmountFCBRefLock                |         1552 |          0 |          0 |
| LH_AuditThreadResource              |          783 |          0 |          0 |
| LH_KS_PlogConfigLock                |          779 |          0 |          0 |
.
.
.
| LH_ShrinkAccelLock1                 |            1 |          0 |          0 |
| LH_ShrinkLock1                      |            1 |          0 |          0 |
| LH_VolResizeLock                    |            1 |          0 |          0 |
+-------------------------------------+--------------+------------+------------+

# Displays all of the lock statistics, sorted on the ‘Max Wait’ column.
$ acfsutil lockstats -s maxwait

+-------------------------------------+--------------+------------+------------+
|              Lock Type              |   Acquires   |  Max Wait  | Total Wait |
+-------------------------------------+--------------+------------+------------+
| LH_SnapDIOCowLock                   |          397 |          6 |          6 |
| LH_IgnoreCompletely                 |      9405112 |          1 |         55 |
| LH_DLM_hash_chain_lock              |       312581 |          1 |          5 |
| LH_OFSBUFHashChain                  |       820083 |          1 |          7 |
| LH_FcbMCBLock                       |       814524 |          1 |        116 |
| LH_MetabufLock                      |       818728 |          1 |        234 |
| LH_SnapMapLockDLMLock               |          399 |          1 |          1 |
| LH_RemapTableDLMLock                |            3 |          1 |          1 |
| LH_TrackOnly                        |       468690 |          0 |          0 |
| LH_KS_feature_lock                  |           12 |          0 |          0 |
| LH_DLM_rbld_stall_lock              |          199 |          0 |          0 |
| LH_DLM_rsb_incarn_lock              |           68 |          0 |          0 |
| LH_DLM_rsb_lock                     |           81 |          0 |          0 |
| LH_DLM_lkb_lock                     |           83 |          0 |          0 |
| LH_DLM_lkid_lock                    |          194 |          0 |          0 |
| LH_KCSS_comm_lock                   |           11 |          0 |          0 |
.
.
.
| LH_GlobalMntResource                |            4 |          0 |          0 |
| LH_KS_PlogConfigLock                |          790 |          0 |          0 |
+-------------------------------------+--------------+------------+------------+

# Displays all of the lock statistics, sorted on the ’Total Wait’ column.
$ acfsutil lockstats -s total wait

+-------------------------------------+--------------+------------+------------+
|              Lock Type              |   Acquires   |  Max Wait  | Total Wait |
+-------------------------------------+--------------+------------+------------+
| LH_MetabufLock                      |       608763 |          1 |        176 |
| LH_FcbMCBLock                       |       605578 |          1 |         83 |
| LH_IgnoreCompletely                 |      7002105 |          1 |         41 |
| LH_SnapDIOCowLock                   |          295 |          6 |          6 |
| LH_DLM_hash_chain_lock              |       312581 |          1 |          5 |
| LH_OFSBUFHashChain                  |       610118 |          1 |          5 |
| LH_SnapMapLockDLMLock               |          297 |          1 |          1 |
| LH_RemapTableDLMLock                |            3 |          1 |          1 |
| LH_TrackOnly                        |       348954 |          0 |          0 |
| LH_KS_feature_lock                  |           12 |          0 |          0 |
| LH_DLM_rbld_stall_lock              |          199 |          0 |          0 |
| LH_DLM_rsb_incarn_lock              |           68 |          0 |          0 |
| LH_DLM_rsb_lock                     |           81 |          0 |          0 |
| LH_DLM_lkb_lock                     |           83 |          0 |          0 |
| LH_DLM_lkid_lock                    |          194 |          0 |          0 |
| LH_KCSS_comm_lock                   |           11 |          0 |          0 |
| LH_KSS_asm_exit_lock                |           10 |          0 |          0 |
| LH_KCSS_rac_mode_lock               |           21 |          0 |          0 |
| LH_ADVM_hd_lock                     |            1 |          0 |          0 |
| LH_ADVM_rootSpin                    |           90 |          0 |          0 |
| LH_ADVM_root_stateLock              |            1 |          0 |          0 |
  .  
  .
  .
| LH_GlobalMntResource                |            4 |          0 |          0 |
| LH_KS_PlogConfigLock                |          587 |          0 |          0 |
+-------------------------------------+--------------+------------+------------+

# Displays the top 10 lock statistics, sorted on the ’Acquires’ column.
$ acfsutil lockstats lh -s acquires -t 10

+-------------------------------------+--------------+------------+------------+
|              Lock Type              |   Acquires   |  Max Wait  | Total Wait |
+-------------------------------------+--------------+------------+------------+
| LH_IgnoreCompletely                 |      9874904 |          1 |         58 |
| LH_OFSBUFHashChain                  |       861237 |          1 |          8 |
| LH_MetabufLock                      |       859882 |          1 |        248 |
| LH_FcbMCBLock                       |       855493 |          1 |        127 |
| LH_TrackOnly                        |       491920 |          0 |          0 |
| LH_DLM_hash_chain_lock              |       312581 |          1 |          5 |
| LH_DLMSpinLock                      |        16870 |          0 |          0 |
| LH_AutoResizeLock                   |         4122 |          0 |          0 |
| LH_SnapMapMetaDataLock              |         2898 |          0 |          0 |
| LH_RecoverySpinLock                 |         2884 |          0 |          0 |
+-------------------------------------+--------------+------------+------------+
```

#### acfsutil log

Purpose

Retrieves memory diagnostic log files and manages debug settings.

Syntax and Description

```
acfsutil [-h] log

acfsutil log [-f filename] [-s] [-r n{K|M|G|T|P}] [-p {avd|ofs|oks}] [-l debuglevel] 
         [-n consolelevel] [-o wait_time] [-q] [-c debugcontext] [-T file_type] 
         [-m mount_point] [-a] [-C] [-t]
```

For information about running Oracle ACFS `acfsutil` commands, refer to [About Using Oracle ACFS Command-Line Tools](steps-manage-acfs.md).

The following table contains the options available with the `acfsutil` `log` command.

Table 7-15 Options for the acfsutil log command

| Option | Description |
| --- | --- |
| `-f filename` | Write the in-memory log to the specified file. The default file is `oks.log` in the current directory. |
| `-s` | Shows the size of the in-memory log file. |
| `-r n{K\|M\|G\|T\|P}` | Sets the size of the in-memory log file. |
| `-p {avd\|ofs\|oks}` | Specifies the product for setting the level or querying settings. The is default all products: Oracle ADVM (`avd`), Oracle ACFS (`ofs`), and Oracle Kernel Services (`oks`) |
| `-l debuglevel` | Sets the in-memory debug level. The default debug level is `2`. Valid values are `0` - `6`. |
| `-n consolelevel` | Sets the debug level for persistent logging. Other persistent log configuration settings are managed by the `acfsutil` `plogconfig` command. |
| `-o wait_time` | Sets the log size, the debug level, and the product values on all nodes; waits for the number of seconds specified by wait\_time; dumps in the memory log on all nodes; and then resets the debug level and the log size. |
| `-q` | Queries the debug settings for a specified product.  For example: `acfsutil log —p avd —q` |
| `-c debugcontext` | Sets the debug context, internal only. |
| `-T file_type` | Sets the debug file type, internal only. |
| `—m mount_point` | Specifies to debug only the file system at the specified mount point. |
| `-a` | Resets the debug logging to log for all file systems. |
| `-C` | Dumps a memory log on all cluster nodes, and also can be added to `-t` option. |
| `-t` | Dumps all Hang Manager thread information to in-memory and persistent logs. |

The `acfsutil` `log` command enables you to manage memory diagnostic log files. With none of the options specified, the `acfsutil` `log` command retrieves and writes the `./oks.log` memory log by default.

The `-o` option performs the following:

1. Sets the log size to `500M`, the log level to `5`, and the product to `ofs` (acfs) for the in-memory log on all nodes
2. Displays an informational message, such as Blocking for 180 seconds, reproduce problem now
3. After waiting for the specified number of seconds, then displays Dumping log on all nodes
4. Initiates a clusterwide dump of logs
5. Resets the log level to `2` and resets the log size to the default

The `-o` option can be combined with the - `p`, `-l,` and `-r` options if the default product, debug level, or log size settings should be changed.

You must be the `root` user or an Oracle ASM administrator user to run this command.

Examples

The following example shows various ways to run the `acfsutil` `log` command.

Example 7-13 Using acfsutil log

```
#increase internal log size to 100Mb
$ acfsutil log -r 100M

#increase log level for acfs to 5
$ acfsutil log -l 5 -p ofs

#increase log level for oks to 5
$ acfsutil log -l 5 -p oks

#collect in memory log and place it into /tmp/logfile
$ acfsutil log -f /tmp/logfile

#put trace level back to default, level 2
$ acfsutil log -l 2 -p ofs
$ acfsutil log -l 2 -p oks

# increase log level to 5, wait 3 seconds, and then automatically dump a log on all nodes, 
# log will be in a dated file in directory specified by acfsutil plog -q
$ acfsutil log -l 5 -o 3
Blocking for 3 seconds, reproduce problem now
Dumping log on all nodes

# dump out the stacks of all acfs threads running on the system on all nodes into log files 
# in the directory specified by acfsutil plog -q
$ acfsutil log -t
$ acfsutil log -C
```

#### acfsutil meta

Purpose

Copies metadata from an Oracle ACFS file system into a separate output file.

Syntax and Description

```
acfsutil meta -h
acfsutil meta  [-v] 
               [-g] 
               [-g -O -C -S]
               [-O]
               [-C COW_filepath]
               [-S COW_size]
               [-q nn[K|M|G|T]]  
               [-l log_file_path] 
               [-o acfs_extent_offsets]      
               {-f record_oriented_metadata_output_file} [-a accel_device] volume_device

acfsutil meta  {-e record_oriented_metadata_input_file [-i]}
               {-f output_filesystem_meta_file_prefix_name}
```

`acfsutil meta` `-h` displays help text and exits.

For information about running Oracle ACFS `acfsutil` commands, refer to [About Using Oracle ACFS Command-Line Tools](steps-manage-acfs.md).

The following table contains the options available with the `acfsutil` `meta` command. The options are shown in Linux format (also AIX and Solaris format).

Table 7-16 Options for the acfsutil meta command

| Option | Description |
| --- | --- |
| `—f record_oriented_metadata_output_file` | Specifies the path name of the output file into which the metadata is copied. |
| `—g` | Do not perform a block scan looking for lost metadata on the entire volume. Instead, only reads the known metadata blocks. This option is only recommended for file systems in good health. |
| `—g -O -C -S` | Same as the `-g` option, except also run Oracle ACFS online checker (`fsck` on Linux). |
| `-O` | Specifies to run the Oracle ACFS online checker (`fsck` on Linux). |
| `-C COW_filepath` | Specifies the path to the Copy-On-Write (COW) file for the Oracle ACFS online checker. The path must be on a different Oracle ACFS file system. |
| `-S COW_size` | Specifies the size of the Copy-On-Write (COW) file for Oracle ACFS online checker. The size must be large enough so the original blocks can be preserved when the file system modifications are made. |
| `volume_device` | Specifies a volume device name of the file system which is to be copied. |
| `—v` | Specifies verbose mode to generate additional diagnostic messages. |
| `—q nn[K\|M\|G\|T]` | Invokes the metadata collector in quick sccan mode. The scanning of the volume stops at the specified size. The number specified must be a positive integer and the value must be at least 200 M.  The units are K (Kilobytes), M (Megabytes), G (Gigabytes), or T (Terabytes). If the unit indicator is specified, then it must be appended to the integer. If omitted, the default unit is bytes. |
| `-l` `log_file_path` | Specifies the path to the log file. If not specified, the log file is generated in the current directory with a default name of `acfs.meta.log`. |
| `—o acfs_extent_offsets` | Specifies a list of comma separated file offsets from which the meta collector additionally copies data. |
| `—a accel_device` | Specifies the location of any associated accelerator device, to be used if the file system is unmountable. |
| `—e record_oriented_metadata_input_file` | Expands the specified record-oriented metadata file into files that can be used with `fsck` or `acfschkdsk`. |
| `—i` | The `-i` option with the -e option lists the metadata record headers (flags, volume, offset, size) for each record-oriented metadata file. |
| `—f output_filesystem_meta_file_prefix_name` | Specifies the path name of the output file from `—e` option operation. |

The `acfsutil` `meta` command operates as a metadata collector to partially copy an Oracle ACFS file system into a separate specified record-oriented output file. The metadata collector reads the contents of the file system specified by the volume device name of an Oracle ACFS file system. This input file system is searched for Oracle ACFS metadata and then all metadata found is written into the specified record-oriented output file. The generated record-oriented output file can be easily transferred to a another system, where it can expanded for diagnostics and analysis, without impact to the original file system at the customer site.

The `-g` option collects only the known good metadata. The `-g` option should not be used with a corrupted file system because the `-g` option does not find lost metadata. Any lost metadata may be important in diagnosing a file system corruption. If the file system is in good repair, the `-g` option may collect the metadata much faster because it does not need to scan the entire physical volume looking for lost metadata blocks.

When the `acfsutil` `meta` `-g` command is run on Linux, the Oracle ACFS online checker (`fsck`) runs automatically. The Oracle ACFS online checker, running on behalf of `acfsutil` `meta` `-g`, transverses the Oracle ACFS file system metadata using the metadata on-disk pointers, and writes metadata that has been read into the `acfsutil` `meta` `-g` metadata collection file. For information about the online `fsck` command on Linux, refer to [Oracle ACFS Command-Line Tools for Linux Environments](acfs-commands-linux.md).

To obtain the best copy of the file system with `acfsutil meta`, dismount the file system before running `acfsutil meta`. If it is not possible to dismount the file system, avoid modifying the contents or performing a volume resizing operation while `acfsutil meta` is running.

If the original file system is very large, then the output file can also be very large. Compress the output file when possible to reduce storage space and transmission time.

If the file system has an accelerator device associated with it, `acfsutil meta` also copies the accelerator device data into the record-oriented output file. This operation occurs automatically.

In most circumstances, `acfsutil meta` automatically copies the accelerator device into the record-oriented output file. However, if you have think that the meta collector is not able to find the accelerator device on its own, you can specify the name on the command line with the `-a` option. For example, this situation could occur if the file system is corrupt. Note that using the `-a` option overrides how the meta collector operates automatically, so `-a` should be used carefully.

The output file should not be placed on the Oracle ACFS device that is specified as the input device because the metadata command might process the output file also. The output file should be placed on a file system that can support an output file which is the size of the Oracle ACFS input volume device. The output file should not need all that storage unless the file system is full and contains all metadata and almost no user data, which is unlikely, but not impossible.

The `-q` flag should be used with caution. When `-q` is specified, the meta collector does not scan and copy the entire input file system. Instead, it only scans and copies a predetermined number of bytes and certain data structures which are considered important. The primary use for the `-q` flag is for situations where there is not sufficient time to run the full version of the metadata collector. The `-q` flag should not be used unless it is recommended by the support personnel investigating the problem.

Expanding the record-oriented output file should be performed on the system where diagnosis and analyzes is to be performed. For example, the following command expands record-oriented metadata file on another file system that has adequate storage space.

```
acfsutil meta -e record_oriented_metadata_input_file -f output_filesystem_meta_file_prefix_name
```

The output of the command provides sparse files suitable for use with `fsck` or `acfschkdsk`. If the record oriented metadata input file includes an accelerator volume, a second sparse output file is created using the same output file name prefix with `.acc` suffix appended. The file system used for the expanded files should support sparse files. Otherwise, the resulting expanded files could be extremely large containing useless zeros where sparse holes could be saving space.

The `acfsutil meta` expanded output file can be read by the `fsck` command in most cases. However, the Oracle ACFS specific `fsck` command on some OS platforms might not access the output file correctly or might not work with a specified flag. You can use a slightly modified `fsck` command form in these cases. For example:

- On Linux, run the command in this format if you are using the `—x` flag:
	```
	/sbin/fsck.acfs -x filesystem_meta_file.acc filesystem_meta_file
	```
- On Solaris, run the command in this format if you are using the `—o` `x` flag:
	```
	/usr/lib/fs/acfs/fsck -o x=filesystem_meta_file.acc filesystem_meta_file
	```
- On AIX, run the command in this format:
	```
	/sbin/helpers/acfs/fsck filesystem_meta_file
	```

Examples

Example 7-14 shows the use of the `acfsutil meta` command to copy and expand metadata into output files.

Example 7-14 Using the acfsutil meta command

```
$ /sbin/acfsutil meta -f /acfsmounts/critical_apps/record_oriented_metadata_file /dev/asm/volume1-123
```

You can then expand the output file on the system where diagnostics and analysis are performed.

```
$ /sbin/acfsutil meta -e record_oriented_metadata_file -f filesystem_meta_file
```

#### acfsutil plogconfig

Purpose

Manages Oracle ACFS persistent logging configuration settings.

Syntax and Description

```
acfsutil plogconfig [-h] [-d persistent_log_directory] [-t] [-q ] [-i seconds] 
                    [-s buffer_size] [-l low_water_percent] [-u high_water_percent] 
                    [-m max_logfile_size] [-n max_logfile_number]
```

`acfsutil` `-h` `plogconfig` displays help and exits.

For information about running Oracle ACFS `acfsutil` commands, refer to [About Using Oracle ACFS Command-Line Tools](steps-manage-acfs.md).

The following table contains the options available with the `acfsutil` `plogconfig` command.

Table 7-17 Options for the acfsutil plogconfig command

| Option | Description |
| --- | --- |
| `-d persistent_log_directory` | Specifies an alternative logging directory. If not specified, the default directory is `$ORACLE_BASE/crsdata/hostname/acfs`. |
| `-t` | Terminates logging. |
| `-q ` | Queries for and then displays the persistent logging configuration settings. |
| `-i seconds` | Specifies the number of seconds for the interval timer. |
| `-s buffer_size` | Sets the log buffer size in kilobytes. |
| `-l low_water_pecent` | Sets the file write trigger as a percentage. |
| `-u high_water_pecent` | Sets the file write throttle as a percentage. |
| `-m max_logfile_size` | Sets the maximum log file size in megabytes. |
| `-n max_logfile_number` | Sets the maximum number of log files. |

The `acfsutil` `plogconfig` command provides a diagnostic tool to manage configuration settings for persistent logging.

All command arguments are optional, but at least one argument must be specified.

Note:

Run the `acfsutil` `plogconfig` command only when Oracle Support requests configuration of persistent logging settings.

You must be the `root` user or an Oracle ASM administrator user to run this command.

Examples

The following example illustrates the use of the `acfsutil` `plogconfig` command to display the current configuration settings.

Example 7-15 Using the Oracle ACFS acfsutil plogconfig command

```
# /sbin/acfsutil plogconfig -q

Log Directory Name : /oracle/crsdata/my_host/acfs 
Buffer Size (KB) : 64
Low Water Level (percent) : 50
High Water Level (percent) : 75
Timer Interval (Seconds) : 5
Maximum Number of Log Files : 10
Maximum Log File Size (MB) : 100
```

#### acfsutil tune

Purpose

The `acfsutil` `tune` command displays or sets the value of Oracle ACFS tunable parameters.

Syntax and Description

```
acfsutil tune -h
acfsutil tune [tunable_name]
acfsutil tune tunable_name=value
```

`acfsutil` `tune` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `tune` command.

Table 7-18 Options for the acfsutil tune command

| Option | Description |
| --- | --- |
| `tunable_name` | Specifies the name of the tunable parameter. |
| `value` | Specifies the value for a tunable parameter. |

If a tunable parameter and value are specified, the `acfsutil` `tune` command sets the value of the tunable parameter in a persistent manner on a particular node.

If a tunable parameter is specified without a value, the `acfsutil` `tune` command displays the value that is currently assigned to the specified tunable parameter.

If no options are specified, the `acfsutil` `tune` command displays the tunable parameter values that are currently assigned.

The Oracle ACFS tunable parameter `AcfsMaxOpenFiles` limits the number of open Oracle ACFS files on AIX. Normally you do not have to change the value of this tunable parameter; however, you may want to consider increasing the value if you have a large working set of files in your Oracle ACFS file systems.

The Oracle ACFS tunable parameter `AcfsMaxCachedFiles` sets the maximum number of closed files that remain cached in memory on AIX. Normally you do not have to change value of this tunable parameter; however, you many to consider changing the value to get better performance.

Changing a tunable parameter has an immediate effect and persists across restarts.

You must be a root user to change the value of a tunable parameter.

Examples

The first command displays Oracle ACFS tunable parameters with their values. The second command changes the value of the `AcfsHMTimeOutIntervalSecs` parameter.

Example 7-16 Using the acfsutil tune command

```
$ /sbin/acfsutil tune
AcfsHMTimeOutIntervalSecs   = 60 (0x3c)
AcfsHMSilenceIntervalMins   = 240 (0xf0)

# /sbin/acfsutil tune AcfsHMTimeOutIntervalSecs=120
```

#### advmutil tune

Purpose

`advmutil` `tune` displays or sets the value of an Oracle ADVM parameter.

Syntax and Description

```
advmutil -h
advmutil tune [parameter]
advmutil tune parameter=value
```

`advmutil` `-h` displays help text and exits.

The following table contains the options available with the `advmutil` `tune` command.

Table 7-19 Options for the advmutil tune command

| Option | Description |
| --- | --- |
| `parameter` | Specifies the parameter for which you want to set or display the value. |
| `value` | Specifies the value of the specified parameter. |

If no options are specified, the `advmutil` `tune` command displays the parameter values that are currently assigned.

If a parameter is specified without a value, the `advmutil` `tune` command displays the value that is currently assigned to the specified parameter.

You must be a privileged user to set a parameter.

Note:

Parameters should be set with caution and usually only by Oracle Support Services.

Examples

A parameter that can be specified with `advmutil` `tune` is the maximum time in minutes for the deadlock timer (`deadlock_timer`). The first command in the example changes the maximum time in minutes for the `deadlock_timer` parameter. The second command displays the current settings of the Oracle ADVM parameters.

Example 7-17 Using advmutil tune

```
$ /sbin/advmutil tune deadlock_timer=20

$ /sbin/advmutil tune
deadlock_timer        = 20 (0x14)
resilver_power        = 8 (0x8)
resilver_regio        = 32 (0x20)
```

### Understanding Oracle ACFS I/O Failure Console Messages

Oracle ACFS logs information for I/O failures in the operating-specific system event log.

A console message has the following format:

```
[Oracle ACFS]: I/O failure (error_code) with device device_name during a operation_name op_type.
file_entry_num Starting offset: offset. Length of data transfer: io_length bytes.
Impact: acfs_type   Object: object_type   Oper.Context: operation_context 
Snapshot?: yes_or_no AcfsObjectID: acfs_object_id . Internal ACFS Location: code_location.
```

The italicized variables in the console message syntax correspond to the following:

- I/O failure
	The operating system-specific error code, in Hex, seen by Oracle ACFS for a failed I/O. This may indicate a hardware problem, or it might indicate a failure to initiate the I/O for some other reason.
- Device
	The device involved, usually the ADVM device file, but under some circumstances it might be a string indicating the device minor number
- Operation name
	The kind of operation involved:
	`user` `data`, `metadata`, or `paging`
- Operation type
	The type of operation involved:
	`synch` `read`, `synch` `write`, `asynch` `read`, or `asynch` `write`
- File entry number
	The Oracle ACFS File entry number of the file system object involved, as a decimal number. The `acfsutil` `info` `fileid` tool finds the corresponding file name.
- Offset
	The disk offset of the I/O, as a decimal number.
- Length of I/O
	The length of the I/O in bytes, as decimal number.
- File system object impacted
	An indication that the file system object involved is either node-local, or is a resource accessed clusterwide. For example:
	`Node` or `Cluster`
- Type of object impacted
	A string indicating the kind of file system object involved, when possible. For example:
	`Unknown`, `User` `Dir.`, `User` `Symlink`, `User` `File`, `Sys.Dir`, `Sys.File`, or `MetaData`
	- `Sys.Dir.`
		Oracle ACFS-administered directory within the visible namespace
		- `sys.File`
		Oracle ACFS-administered file within the visible namespace
		- `MetaData`
		Oracle ACFS-administered resources outside of the visible namespace
- Operational context
	A higher-level view of what code context was issuing the I/O. This is for use by Oracle Support Services. For example:
	`Unknown`, `Read`, `Write`, `Grow`, `Shrink`, `Commit`, or `Recovery`
- Snapshot
	An indication of whether, if possible to determine, the data involved was from a Snapshot. For example:
	`Yes`, `No`, or `?`
- Object type of the file system
	An internal identifier for the type of file system object. For use by Oracle Support Services.
- Location of the code
	An internal identifier of the code location issuing this message. For use by Oracle Support Services.

The following is an example from `/var/log/messages` in a Linux environment:

```
[Oracle ACFS]: I/O failure (0xc0000001) with device /dev/sdb during a metadata synch write .
Fenum Unknown. Starting offset: 67113984. Length of data transfer: 2560 bytes.
Impact: Node   Object: MetaData   Oper.Context: Write
Snapshot?: ?  AcfsObjectID: 8  . Internal ACFS Location: 5 .
```

### Configuring Oracle ACFS Snapshot-Based Replication

The requirements for Oracle ACFS snapshot-based replication are discussed in this section.

This section describes how to configure Oracle ACFS snapshot-based replication available with release 12.2 or higher. As with Oracle ACFS replication installations before release 12.2, the overall functional goal of snapshot-based replication is to ensure that updates from a primary cluster are replicated to a standby cluster. However, the snapshot based replication technology uses snapshots of the primary storage location and transfers the differences between successive snapshots to the standby storage location using the standard `ssh` command. Oracle ACFS replication functionality before release 12.2 replicated changes continuously, building on Oracle networking technologies, notably Network Foundation Technologies (NFT), to ensure connectivity between the primary and standby clusters.

This change in the design and implementation of Oracle ACFS replication introduces some differences in how replication is configured and used. For example, the use of `ssh` requires setting up host and user keys appropriately on the primary and standby nodes where replication is performed.

Oracle ACFS replication also provides role reversal and failover capabilites that you can configure by enabling both the primary cluster and the standby cluster to communicate with each other as required. In role reversal, the standby assumes the role of the primary and the primary becomes the standby. Failover may involve either role reversal or the establishment of a new standby for the new primary to use.

This section contains the following topics:

- Configuring ssh for Use With Oracle ACFS Replication

See Also:

- [Oracle ACFS Replication](understand-acfs-admin.md) for an overview of Oracle ACFS replication
- [Oracle ACFS Command-Line Tools for Replication](acfs-commands-replication.md) for information about Oracle ACFS replication commands
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=OSTMG-GUID-7396FD18-628B-4026-AA55-79C6D6205EAE) for information about Oracle ASM privileges

#### Configuring ssh for Use With Oracle ACFS Replication

This topic describes how to configure `ssh` for use by Oracle ACFS snapshot-based replication available with release 12.2 or higher.

Oracle ACFS snapshot-based replication uses `ssh` as the transport between the primary and standby clusters. To support the full capabilities of replication, `ssh` must be usable in either direction between the clusters — from the primary cluster to the standby cluster and from the standby to the primary.

The procedures in this topic describe how to configure `ssh` for replication in one direction — from the primary to the standby. To configure `ssh` completely, you must perform the instructions a second time with the primary and standby roles reversed. When you perform the instructions the first time, complete the steps as written for the primary cluster and the standby cluster. The second time, reverse the primary and standby roles. Perform the steps marked as necessary on the primary cluster on your standby cluster and perform the steps marked as necessary on the standby cluster on your primary cluster. The procedures that must be performed twice are described in:

- Choosing an Oracle ACFS replication user
- Distributing keys for Oracle ACFS replication
- Getting a public key for repluser from the primary cluster
- Getting host keys for the standby cluster
- Notes on permissions for ssh-related files
- Notes on sshd configuration
- Validating your ssh-related key configuration

After you have completed all the necessary procedures, you can use the instructions described in Validating your ssh-related key configuration to confirm that you have configured `ssh` correctly in both directions.

Choosing an Oracle ACFS replication user

Oracle ACFS snapshot-based replication uses `ssh` as the transport between the primary and standby clusters, so the user identity under which replication is performed on the standby must be carefully managed. In the replication process, the replication user (repluser) on the primary node where replication is running uses `ssh` to log in to the standby node involved in replication.

The user chosen as repluser should have Oracle ASM administrator privileges. The user specified to the Oracle installer when the Oracle software was first installed usually belongs to the needed groups, so it is convenient to choose the replication user. In this discussion, the replication user is identified as repluser; however, you would replace repluser with the actual user name that you have selected. For information about running Oracle ACFS `acfsutil` commands, refer to [About Using Oracle ACFS Command-Line Tools](steps-manage-acfs.md).

Note:

The same user and group identities must be specified for repluser on both your primary cluster and your standby cluster. Additionally, the mappings between user names and numeric `uids`, and between group names and numeric `gids`, must be identical on both the primary cluster and the standby cluster. This is required to ensure that the numeric values are used in the same manner on both clusters because replication transfers only the numeric values from the primary to standby.

Distributing keys for Oracle ACFS replication

The process of distributing keys for Oracle ACFS replication includes getting a public key from the primary cluster, getting host keys for the standby cluster, ensuring permissions are configured properly for `ssh` -related files, configuring `sshd` as necessary, and lastly validating the `ssh` configuration.

Note:

When creating host keys, ensure that you create keys for both fully-qualified domain hostnames and the local hostnames.

Getting a public key for repluser from the primary cluster

A public key for repluser defined on each node of your primary cluster must be known to repluser on each node of your standby cluster.

To make this key known, the directory `~repluser/.ssh` must exist on each standby node. If this directory does not exist, then create it with access only for repluser. Ensure that an `ls` command for the `.ssh` directory displays output similar to:

```
repluser@standby $ ls -ld ~/.ssh
drwx------ 2 repluser dba 4096 Jan 27 17:01 .ssh
```

If a public key file for repluser exists on a given primary node, then add its contents to the set of keys authorized to log in as repluser on each node of the standby where replication is run. Append the key to the file `~repluser/.ssh/authorized_keys2` on each standby node, creating this file if necessary.

If a public key file does not exist, generate a public and private key pair on the primary by running the following command as repluser.

```
$ ssh-keygen -t rsa
```

You can press the enter key in response to each prompt issued by the command. Copy the resulting `.pub` file to each standby node.

You have the option to share the same public/private key pair for repluser across all of the nodes in your primary cluster, or to establish a different key pair for each primary node. If the same public key is valid for repluser across all nodes in your primary cluster, then only that key must be added to the file `~repluser/.ssh/authorized_keys2` on each node of your standby cluster. If each primary node has its own public key for repluser, then all the public keys must be added to the file. In either case, you can minimize work by copying the updated `authorized_keys2` file on a given node of the standby to the other nodes of the cluster.

Getting host keys for the standby cluster

A host key for each standby node where replication may run must be known on each primary node where replication may run. One way to generate the correct key is to run `ssh` manually as repluser from each primary node to each standby node. If the correct host key is not known already, then a warning displays and you can enable `ssh` to add the key.

The following is an example of obtaining a host key:

```
[repluser@primary data]$ ssh repluser@standby date
The authenticity of host 'standby (10.137.13.85)' can't be established.
RSA key fingerprint is 1b:a9:c6:68:47:b4:ec:7c:df:3a:f0:2a:6f:cf:a7:0a.
Are you sure you want to continue connecting (yes/no)?
```

If you respond with `yes`, then the `ssh` setup is complete. A host key for host standby is stored in the `known_hosts` file (`~repluser/.ssh/known_hosts`) on the host primary for the user repluser.

After the host key setup for standby nodes is complete on a given primary node, you need to perform an additional step if you use a Virtual IP address (VIP) to communicate with your standby cluster. You must add the VIP name or address at the start of each line of the `known_hosts` file that refers to a host in the standby cluster. For example, if you use a VIP with the name `standby12_vip`, and your `known_hosts` file contains the following two lines that refer to your standby:

```
standby1,10.242.20.22 ssh-rsa
AAAAB3NzaC1yc2EAAAADAQABAAABAQC3pM2YTd4UUiEWEoCKDGgaTgsmPkQToDrdtU+JtVIq/96muivU
BaJUK83aqzeNIQkh+hUULsUdgKoKT5bxrWYqhY6AlTEqNgBHjBrJt9C73BbQd9y48jsc2G+WQWyuI/
+s1Q+hIJdBNMxvMBQAfisPWWUcaIx9Y/JzlPgF6lRP2cbfqAzixDot9fqRrAKL3G6A75A/6TbwmEW07d1zqOv
l7ZGyeDYf5zQ72F/V0P9UgMEt/5DmcYTn3kTVGjOTbnRBe4A4lY4rVw5c+nZBDFre66XtORfQgwQB5ztW/Pi
08GYbcIszKoZx2HST9AZxYIAgcrnNYG2Ae0K6QLxxxScP
standby2,10.242.20.23 ssh-rsa
AAAAB3NzaC1yc2EAAAADAQABAAABAQDIszcjzNtKN03SY8Kl846skFTVP1HF/ykswbmkctEjL6KTWTW+NR
U4MGbvkBqqdXxuPCR7aoGO2U3PEOg1UVf3DWUoux8IRvqKU+dJcdTibMFkDAIhTnzb14gZ/lRTjn+GYsuP5
Qz2vgL/U0ki887mZCRjWVL1b5FNH8sXBUV2QcD7bjF98VXF6n4gd5UiIC3jv6l2nVTKDwtNHpUTS1dQAi+1D
tr0AieZTsuxXMaDdUZHgKDotjciMB3mCkKm/u3IFoioDqdZE4+vITX9G7DBN4CVPXawp+b5Kg8X9P+08Eehu
tMlBJ5lafy1bxoVlXUDLVIIFBJNKrsqBvxxxpS7
```

To enable the use of the VIP, you would modify these two lines to read as follows:

```
standby12_vip,standby1,10.242.20.22 ssh-rsa
AAAAB3NzaC1yc2EAAAADAQABAAABAQC3pM2YTd4UUiEWEoCKDGgaTgsmPkQToDrdtU+JtVIq/96muivU
BaJUK83aqzeNIQkh+hUULsUdgKoKT5bxrWYqhY6AlTEqNgBHjBrJt9C73BbQd9y48jsc2G+WQWyuI/
+s1Q+hIJdBNMxvMBQAfisPWWUcaIx9Y/JzlPgF6lRP2cbfqAzixDot9fqRrAKL3G6A75A/6TbwmEW07d1zqOv
l7ZGyeDYf5zQ72F/V0P9UgMEt/5DmcYTn3kTVGjOTbnRBe4A4lY4rVw5c+nZBDFre66XtORfQgwQB5ztW/Pi
08GYbcIszKoZx2HST9AZxYIAgcrnNYG2Ae0K6QLxxxScP
standby12_vip,standby2,10.242.20.23 ssh-rsa
AAAAB3NzaC1yc2EAAAADAQABAAABAQDIszcjzNtKN03SY8Kl846skFTVP1HF/ykswbmkctEjL6KTWTW+NR
U4MGbvkBqqdXxuPCR7aoGO2U3PEOg1UVf3DWUoux8IRvqKU+dJcdTibMFkDAIhTnzb14gZ/lRTjn+GYsuP5
Qz2vgL/U0ki887mZCRjWVL1b5FNH8sXBUV2QcD7bjF98VXF6n4gd5UiIC3jv6l2nVTKDwtNHpUTS1dQAi+1D
tr0AieZTsuxXMaDdUZHgKDotjciMB3mCkKm/u3IFoioDqdZE4+vITX9G7DBN4CVPXawp+b5Kg8X9P+08Eehu
tMlBJ5lafy1bxoVlXUDLVIIFBJNKrsqBvxxxpS7
```

Ultimately, the host key configuration performed on this first node of your primary cluster must be performed on every node in your primary cluster; the result of the above sequence, or an equivalent, must exist on each primary node. One way to minimize the manual effort required to achieve this configuration is to update the `known_hosts` file on one node of the primary cluster, then copy the updated file to the other nodes of the cluster.

Note:

By default, replication enables strict host key checking by `ssh`, to ensure that the primary node connects to the intended standby node or cluster when it runs `ssh`. However, if you are certain that this checking is unneeded, such as the case when the primary and standby clusters communicate over a private network, the use of strict host key checking by `ssh` can be disabled. For information about disabling strict host key checking, refer to the `-o sshStrictKey=no` option of the `acfsutil` `repl` `init` `primary` command. If strict host key checking is disabled, then no host key setup is required. For information about the `acfsutil` `repl` `init` command, refer to [acfsutil repl init](acfs-commands-replication.md).

Notes on sshd configuration

After you begin using replication, `ssh` is started frequently to perform replication operations. On some platforms, the `ssh` daemon `sshd` may be configured to log a message through `syslog` or a similar facility each time an `ssh` connection is established. To avoid this, the server configuration file `/etc/ssh/sshd_config` can be modified to specify a lower frequency of logging. The parameter that controls logging is called `LogLevel`. Connection messages are issued at level `INFO`. Any lower `LogLevel` setting, such as `ERROR`, suppresses those messages. For example, you can suppress log messages by adding the following line to the file:

```
LogLevel ERROR
```

Validating your ssh-related key configuration

After you have established the host and user keys for `ssh` on both your primary and your standby clusters, you can use the command `acfsutil` `repl` `info` `-c` `-u` to validate the keys. You run this command as repluser on each node of each cluster. It takes as arguments all the hostnames or addresses on the remote cluster that the local cluster may use in the future to perform replication.

If you are not using a VIP to connect to your remote cluster, then for a given replication relationship, only one remote hostname or address is provided to `acfsutil` `repl` `init` `primary`. However, if future relationships involve other remote host addresses, specify the complete set of remote addresses when running the `acfsutil repl info -c -u` command.

If you are using a VIP to connect to your remote cluster, then you should specify the names or host-specific addresses of all remote hosts on which the VIP may be active. Do not specify the VIP name or an address associated with the VIP. When replication uses `ssh` to connect to a VIP, the host key returned is the key associated with the host where the VIP is currently active. Only the hostnames or addresses of individual remote nodes are used by `ssh` in this situation.

The validation command to run on each node of your primary cluster has the following format:

```
$ acfsutil repl info -c -u repluser standby1 [standby2 ...] [snap_shot@]primary-mountpoint
```

In the command, `standbyn` specifies the standby cluster hostname or address. The validation command confirms that user repluser can use `ssh` to connect to each standby hostname or address given, in the same manner as replication initialization. Use the same command format if you are using a VIP, such as `standby12_vip`, to connect to the cluster. Do not specify the name of the VIP.

If you plan to disable strict host key checking, you can skip this checking by adding the `-o sshStrictKey=no` option to the command line.

After you have confirmed that each node of your primary cluster can connect to all nodes of your standby cluster, run the validation command again. This time run the command on each node of your standby cluster. Specify a hostname or IP address for all nodes of your primary cluster using the following format:

```
$ acfsutil repl info -c -u repluser primary1 [primary2 ...] [snap_shot@]standby-mountpoint
```

In the command, `primaryn` specifies the primary cluster hostname or address.

### Oracle Patching and Oracle ACFS

This section discusses patching with Oracle ACFS in a Grid Infrastructure environment.

- Overview of Oracle ACFS Patching
- Updating Oracle Grid Infrastructure Files
- Verifying Oracle ACFS Patching

#### Overview of Oracle ACFS Patching

Oracle ACFS is installed as part of Oracle Grid Infrastructure. However, Oracle ACFS runs from various system locations, such as `/lib/modules` and `/sbin` on Linux.

Oracle ACFS integrates with the Oracle Grid Infrastructure delivery and patch mechanisms: OUI and OPatch. Regardless of the delivery mechanism; Oracle Release, Oracle Patchset, Oracle Release Update, or Oracle One-off; Oracle ACFS content is delivered in patches.

When updating the Oracle Grid Infrastructure, without Oracle Zero Downtime Grid Infrastructure Patching, Oracle ACFS is also updated in the system locations, ensuring seamless operation of the Oracle Grid software. During the updates; whether Release, Release Update, Patchset, or One-off; the Oracle Clusterware stack is stopped on a local node and services are migrated to other nodes. The Oracle Grid Software is then patched and services are restarted on the local node.

Patching Without Oracle Zero Downtime Oracle Grid Infrastructure Patching

During the patch operation, Oracle ACFS software is updated first in the Grid Home by the OPatch or OUI file placement operation, and then later moved to the appropriate system locations and loaded into memory while Oracle Clusterware is down. The restart of Oracle Clusterware has the side effect of freeing up in operating system (OS) kernel references so that Oracle ACFS can be updated in the OS Kernel.

Patching With Zero Downtime Oracle Grid Infrastructure

When using Zero Downtime Oracle Grid Infrastructure Patching, only the Oracle Grid Infrastructure user space binaries in the Oracle Grid Home are patched. Commands which run out of the Oracle Grid Home immediately use the latest versions. Oracle Grid Infrastructure components that are installed outside of the Oracle Grid Home; such as ACFS, AFD, OLFS, and OKA OS system software (OS kernel modules and system tools); are updated in the Grid Home, but not installed to the system locations. They continue to run the version previous to the patch version. After patching, this results in the OPatch inventory displaying the new patch number in the OPatch inventory. However, the running software does not contain these changes, only the software that is available in the Grid Home. Until the newly available software is loaded into memory and accompanying user tools are copied to system locations, the system does not utilize the available fixes that are in the Oracle Grid Infrastructure Home.

To determine which Oracle ACFS system software is running and installed, the following commands can be used:

- `crsctl` `query` `driver` `activeversion` `-all`
	This command shows the Active Version of Oracle ACFS on all nodes of the cluster. The Active Version is the version of the Oracle ACFS Driver that is currently loaded and running on the system. This also implicitly indicates the ACFS system tools version. The `crsctl` `query` command, available from 18c and onwards, shows data from all nodes of the cluster.
	In the following example, 19.4 is available in the Oracle Home, but 19.2 is the current running version. OPatch `lsinventory` reports 19.4 as the patched version. Oracle Grid Infrastructure OS drivers are only running 19.2.
	```
	crsctl query driver activeversion -all
	Node Name : node1
	Driver Name : ACFS
	BuildNumber : 200114
	BuildVersion : 19.0.0.0.0 (19.2.0.0.0)
	```
- `crsctl` `query` `driver` `softwareversion` `-all`
	This command shows the available Software Version of the Oracle Grid Infrastructure software (and by extension, the available Software Version of the Oracle ACFS Software) that is currently installed in the Oracle Grid Home. The `crsctl` `query` command, available from 18c and onwards, shows data from all nodes of the cluster.
	```
	crsctl query driver softwareversion -all
	Node Name : node1
	Driver Name : ACFS
	BuildNumber : 200628
	BuildVersion : 19.0.0.0.0 (19.4.0.0.0)
	```
- `acfsdriverstate` `version` `-v`
	This command shows the full information on the running Oracle ACFS modules on the local node. The ACFS-9548 and ACFS-9547 messages displays the version of the Oracle ACFS software that is available in the Oracle Grid Infrastructure home. `acfsdriverstate` reports on the local node only. Bug numbers are only available when running one-off patches.
	```
	acfsdriverstate version -v
	ACFS-9325: Driver OS kernel version = 4.1.12-112.16.4.el7uek.x86_64.
	ACFS-9326: Driver build number = 200114.
	ACFS-9212: Driver build version = 19.0.0.0.0 (19.2.0.0.0).
	ACFS-9547: Driver available build number = 200628.
	ACFS-9548: Driver available build version = 19.0.0.0.0 (19.2.0.0.0)
	ACFS-9549: Kernel and command versions.
	Kernel:
	 Build version: 19.0.0.0.0
	 Build full version: 19.2.0.0.0
	 Build hash: 9256567290
	 Bug numbers: NoTransactionInformation
	Commands:
	 Build version: 19.0.0.0.0
	 Build full version: 19.2.0.0.0
	 Build hash: 9256567290
	 Bug numbers: NoTransactionInformation
	```

#### Updating Oracle Grid Infrastructure Files

Until the Oracle Clusterware stack is stopped and the Oracle ACFS driver modules are updated, Oracle ACFS fixes are not loaded into memory. The process that loads the Oracle ACFS fixes into system memory also installs the required tools for Oracle ACFS operation into system locations.

You can perform one of the following procedures:

1. To load Oracle ACFS fixes into memory and system locations, the following commands must be issued on a node by node basis:
	- `crsctl` `stop` `crs` `-f`
		Stops the CRS stack and all applications on the local node
		- `root.sh` `-updateosfiles`
		Updates Oracle ACFS and other Oracle Grid Infrastructure Kernel modules on the system to the latest version
		- `crsctl` `start` `crs` - `wait`
		Restarts CRS on the node
2. Alternatively, if a node reboots with a kernel version change, then newer drivers are automatically loaded and newer system tools installed into the system directories. It is assumed that all nodes in the cluster change kernel versions at the same time.

After one of these events has occurred, the `crsctl` `query` `activeversion` and `crsctl` `query` `softwareversion` commands report the same information: the loaded and running operating system (OS) software is the same as the latest available in the Oracle Grid Infrastructure Home. You can run other Oracle ACFS version commands as described in Verifying Oracle ACFS Patching.

#### Verifying Oracle ACFS Patching

When using standard OPatch patches to apply Oracle Release Updates and Patches, the inventory accurately reflects what is installed in the Grid Infrastructure home and on the system. For example:

```
[grid@racnode1]$ opatch lsinventory
...
..
Oracle Grid Infrastructure 19c                                       19.0.0.0.0
There are 1 products installed in this Oracle Home.

Interim patches (5) :

Patch  30501910: applied on Sat Mar 07 15:42:08 AEDT 2020
Unique Patch ID:  23299902
Patch description:  "Grid Infrastructure Jan 2020 Release Update : 19.4.0.0.200628 (30501910)"
   Created on 28 Dec 2019, 10:44:46 hrs PST8PDT
   Bugs fixed:
```

The output in the `lsinventory` example lists the OPatch RU and other patches that are applied, as well as the bug numbers and other information. These patches are applied to the Grid Infrastructure home. During normal patching operations, they are also applied to the operating system (OS) locations and loaded into memory, ensuring that Oracle Grid Infrastructure OS system software fixes are in sync with the Grid Infrastructure home. However, when using Zero Downtime Grid Infrastructure Patching, the content for Oracle Grid Infrastructure system software installed on the system, such as Oracle ACFS, is not updated at the same time.

The `crsctl` `query` `driver` and `acfsdriverstate` commands can be used to verify whether the installed Oracle Grid Infrastructure system software level is the same as the software level of the Grid Infrastructure home. Refer to the discussion about Zero Downtime Oracle Grid Infrastructure patching in Overview of Oracle ACFS Patching.

For patching and update operations applied without Zero Downtime Oracle Grid Infrastructure Patching, the active and software version should always be the same.

If it is necessary to install updated Oracle Grid Infrastructure OS system software, refer to the procedures in Updating Oracle Grid Infrastructure Files.

After all the Oracle Grid Infrastructure OS system software is updated, the version should be the same as the Opatch `lsinventory` output displayed for any patches or updates to the Grid Infrastructure home, in this case, 19.4.0.0.0. Additionally, the Oracle Grid Infrastructure OS system software that is available and active should have the same version number displayed. For example:

```
Output from the lsinventory command:   
Patch description:  "Grid Infrastructure Jan 2020 Release Update : 19.4.0.0.0.200628 (30501910)"

crsctl query driver activeversion -all
Node Name : node1
Driver Name : ACFS
BuildNumber : 200628
BuildVersion : 19.0.0.0.0 (19.4.0.0.0)

crsctl query driver softwareversion -all
Node Name : node1
Driver Name : ACFS
BuildNumber : 200628
BuildVersion : 19.0.0.0.0 (19.4.0.0.0)
```

You can run the `acfsdriverstate` `version` command for additional Oracle ACFS information on the local node, including information on commands and utilities. For example:

```
acfsdriverstate version 
 ACFS-9325: Driver OS kernel version = 4.1.12-112.16.4.el7uek.x86_64.
 ACFS-9326: Driver build number = 200628.
 ACFS-9212: Driver build version = 19.0.0.0.0 (19.4.0.0.0)
 ACFS-9547: Driver available build number = 200628.
 ACFS-9548: Driver available build version = 19.0.0.0.0 (19.4.0.0.0).
```