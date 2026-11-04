---
title: Administering Oracle Database on Linux
book: "Administrator's Reference for Linux and UNIX-Based Operating Systems"
doc_id: E10839-25
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e10839/appc_linux.htm
tags:
  - oracle
  - 11g
  - administrators-reference-for-linux-and-unix-based-operating-systems
---

## B Administering Oracle Database on Linux

This appendix contains information about administering Oracle Database on Linux.

It contains the following topics:

Note:

Starting with Oracle Database 11g release 2 (11.2), Linux x86-64 media does not contain Linux x86 binaries. You must use Linux x86 media to install 32-bit Oracle home.

## B.1 Extended Buffer Cache Support

Note:

This section applies to Linux x86 only.

Oracle Database can allocate and use more than 4 GB of memory for the database buffer cache. This section describes the limitations and requirements of the extended buffer cache feature on Linux x86 systems.

See Also:

[Very Large Memory on Linux x86](appi_vlm.md) for more information.

See Also:

[Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm) for more information about the extended buffer cache feature.

In-Memory File System

To use the extended buffer cache feature, create an in-memory file system on the `/dev/shm` mount point equal in size or larger than the amount of memory that you intend to use for the database buffer cache. For example, to create an 8 GB file system on the `/dev/shm` mount point:

1. Run the following command as the `root` user:
	```
	# mount -t tmpfs shmfs -o size=8g /dev/shm
	```
2. To ensure that the in-memory file system is mounted when the system restarts, add an entry in the `/etc/fstab` file similar to the following:
	```
	shmfs /dev/shm tmpfs size=8g 0 0
	```

When Oracle Database starts with the extended buffer cache feature enabled, it creates a file in the `/dev/shm` directory that corresponds to the Oracle buffer cache.

Note:

If an in-memory file system is mounted on the `/dev/shm` mount point, then ensure that its size equals or is larger than the amount of memory that is used for the database buffer cache.

USE\_INDIRECT\_DATA\_BUFFERS Initialization Parameter

To enable the extended buffer cache feature, set the `USE_INDIRECT_DATA_BUFFERS` initialization parameter to TRUE in the parameter file. This enables Oracle Database to specify a larger buffer cache.

Dynamic Cache Parameters

If the extended cache feature is enabled, then you must use the `DB_BLOCK_BUFFERS` parameter to specify the database cache size.

Do not use the following dynamic cache parameters while the extended buffer cache feature is enabled:

- `DB_CACHE_SIZE`
- `DB_2K_CACHE_SIZE`
- `DB_4K_CACHE_SIZE`
- `DB_8K_CACHE_SIZE`
- `DB_16K_CACHE_SIZE`

Limitations

The following limitations apply to the extended buffer cache feature:

- You cannot create or use tablespaces with nondefault block sizes. You can create tablespaces using only the block size specified by the `DB_BLOCK_SIZE` parameter.
- You cannot change the size of the buffer cache while the instance is running.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for more information about the default block size used by the `CREATE TABLESPACE` command.

Note:

The default VLM window size is 512 MB. This memory size is allocated to the address space of the process. To increase or decrease this value, set the `VLM_WINDOW_SIZE` environment variable to the new size in bytes. For example, to set the `VLM_WINDOW_SIZE` to 256 MB, run the following command:
```
$ export VLM_WINDOW_SIZE=268435456
```

The value that you specify for the `VLM_WINDOW_SIZE` environment variable must be a multiple of 64 KB.

## B.2 Using HugePages on Linux

To enable Oracle Database to use large pages (sometimes called HugePages) on Linux, set the value of the `vm.nr_hugepages` kernel parameter to specify the number of large pages that you want to reserve. You must specify a enough large pages to hold the entire SGA for the database instance. To determine the required parameter value, divide the SGA size for the instance by the size of a large page, then round up the result to the nearest integer.

To determine the default large page size, run the following command:

```
# grep Hugepagesize /proc/meminfo
```

For example, if `/proc/meminfo` lists the large page size as 2 MB, and the total SGA size for the instance is 1.6 GB, then set the value for the `vm.nr_hugepages` kernel parameter to 820 (1.6 GB / 2 MB = 819.2).

See Also:

[Overview of HugePages](appi_vlm.md) for more information on tuning SGA with hugepages, configuring hugepages, and hugepages configuration restrictions.

## B.3 Asynchronous Input-Output Support

Oracle Database supports kernel asynchronous Input-Output. Asynchronous Input-Output is enabled by default on raw volumes. Automatic Storage Management uses asynchronous Input-Output by default.

By default, the `DISK_ASYNCH_IO` initialization parameter in the parameter file is set to TRUE. To enable asynchronous Input-Output on file system files:

1. Ensure that all Oracle Database files are located on file systems that support asynchronous Input-Output.
2. Set the `FILESYSTEMIO_OPTIONS` initialization parameter in the parameter file to `ASYNCH` or `SETALL`.
	Note:
	If the file system files are managed through ODM library interface or dNFS, asynchronous Input-Output is enabled by default. There is no need to set `FILESYSTEMIO_OPTIONS` to enable asynchronous Input-Output in these environments.

## B.4 Direct Input-Output Support

Direct Input-Output support is available and supported on Linux.

To enable direct Input-Output support:

- Set the `FILESYSTEMIO_OPTIONS` initialization parameter to `DIRECTIO`.
- Set the `FILESYSTEMIO_OPTIONS` initialization parameter in the parameter file to `SETALL`, which will enable both asynchronous Input-Output and direct Input-Output.

## B.5 Simultaneous Multithreading

If Simultaneous Multithreading is enabled, then the `v$osstat` view reports two additional rows corresponding to the online logical (`NUM_LCPUS`) and virtual CPUs (`NUM_VCPUS`).

## B.6 Allocating Shared Resources

To use the `MEMORY_TARGET` or `MEMORY_MAX_TARGET` feature, the following kernel parameters must be modified.

- `/dev/shm` mount point should be equal in size or larger than the value of `SGA_MAX_SIZE`, if set, or should be set to be at least `MEMORY_TARGET` or `MEMORY_MAX_TARGET`, whichever is larger. For example, with `MEMORY_MAX_TARGET=4GB` only set, to create a 4GB system on the `/dev/shm` mount point:
	- Run the following command as the `root` user:
		```
		# mount -t tmpfs shmfs -o size=4g /dev/shm
		```
		- Ensure that the in-memory file system is mounted when the system restarts, add an entry in the `/etc/fstab` file similar to the following:
		```
		tmpfs /dev/shm tmpfs size=4g 0
		```
- The number of file descriptors for each Oracle instance are increased by 512\* `PROCESSES`. Therefore, the maximum number of file descriptors should be at least this value, plus some more for the operating system requirements. For example, if the `cat /proc/sys/fs/file-max` command returns 32768 and `PROCESSES` are 100, you can set it to 6815744 or higher as `root`, to have 51200 available for Oracle. Use one of the following options to set the value for the `file-max` descriptor.
	- Run the following command:
		```
		echo 6815744 > /proc/sys/fs/file-max
		```
		OR
		- Modify the following entry in the `/etc/sysctl.conf` file and restart the system as `root`.
		```
		fs.file-max = 6815744
		```
- Per-process number of file descriptors must be at least 512. For example, as `root` run the following command.
	- On bash and sh:
		```
		# ulimit -n
		```
		- On csh:
		```
		# limit descriptors
		```
	If the preceding command returns 200, then run the following command to set the value for the per processor file descriptors limit, for example to 1000:
	- On bash and sh:
		```
		# sudo sh
		# ulimit -n 1000
		```
		- On csh:
		```
		# sudo sh
		# limit descriptors 1000
		```
- `MEMORY_TARGET` and `MEMORY_MAX_TARGET` cannot be used when `LOCK_SGA` is enabled. `MEMORY_TARGE` `T` and `MEMORY_MAX_TARGET` also cannot be used with huge pages on Linux.

## B.7 Database Migration from 32-Bit Linux to 64-Bit Linux

To migrate an Oracle Database 11g Release 2 (11.2) for 32-bit Linux to an Oracle Database 11g Release 2 (11.2) for 64-bit Linux, you must perform the following steps:

- Online Backup of Database With RMAN
- Migrating 32-Bit Linux Database to 64-Bit Linux Database
- Migrating Data To and From ASM

### B.7.1 Online Backup of Database With RMAN

Online backup enables to take a backup of the database without having to shutdown the database. To achieve this, perform the following steps:

1. Connect to the database instance as `SYSDBA`:
	```
	SQL> CONNECT / AS SYSDBA;
	```
2. Run the following commands to ensure that the database is in `ARCHIVELOG` mode:
	```
	SQL> SHUTDOWN IMMEDIATE
	Database closed
	Database dismounted
	Oracle instance shutdown
	SQL> STARTUP MOUNT
	Oracle instance started
	Total System Global Area  272629760 bytes
	Fixed Size                   788472 bytes
	Variable Size             103806984 bytes
	Database Buffers          167772160 bytes
	Redo Buffers                 262144 bytes
	Database mounted
	SQL>ALTER DATABASE ARCHIVELOG;
	Database altered
	SQL> ALTER DATABASE OPEN;
	Database altered
	```
3. Run the following command to start RMAN, which is located under `$ORACLE_HOME/bin` directory:
	```
	RMAN>connect target
	```
4. To backup the 32-bit database and all the archived redo log files, run the following command:
	```
	RMAN>backup database plus archivelog delete input;
	```
	Note:
	Archive redo logs are very important to recover the database. Oracle recommends that you back them up along with your database. You can backup the archive redo logs from time to time by issuing the following command:
	```
	RMAN>backup archivelog all delete input;
	```

### B.7.2 Migrating 32-Bit Linux Database to 64-Bit Linux Database

This section covers the following topics:

- Migrating 32-Bit Database to 64-Bit Database With the Same Directory Structure for Data Files
- Migrating 32-Bit Database to 64-Bit Database With Different Directory Structure for Data Files

#### B.7.2.1 Migrating 32-Bit Database to 64-Bit Database With the Same Directory Structure for Data Files

If the control file, data file, redo log files have the same structure on the target computer as in the source computer, then perform the following steps:

1. Perform an online backup of the database before starting the migration process. Refer to Online Backup of Database With RMAN for more information.
2. Install Oracle Database 11g Release 2 (11.2) for 64-bit Linux in a new Oracle Database home. It is recommended that you use the same version of Oracle Database home as on the 32-bit computer.
	See Also:
	[Oracle Database Installation Guide for Linux](https://docs.oracle.com/cd/E11882_01/install.112/e47689/toc.htm)
3. Copy `init.ora`, data files, control file, and the redo log files from the 32-bit Linux computer to the corresponding locations on the 64-bit Linux computer.
4. Edit `init.ora` file to include the following changes:
	- Update the memory requirements included in the file.
		- Edit the control file location if necessary.
	Note:
	Oracle recommends that you double the values of shared pool, java pool, `sga_target` and large pool listed in the `init.ora` file.
5. Connect to the database instance as `SYSDBA`:
	```
	SQL> CONNECT / AS SYSDBA;
	```
6. Set the system to spool results to a log file for later verification of success. For example:
	```
	SQL> SPOOL /tmp/utlirp.log
	```
7. Start the 64-bit Oracle Database as follows:
	```
	SQL> STARTUP UPGRADE pfile=init.ora;
	```
	Note:
	[Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/intro.htm#UPGRD12354) for more information on changing from 32-bit to 64-bit
8. Run the following command on the 64-bit Oracle Database, to invalidate all the PL/SQL modules:
	```
	SQL> @$ORACLE_HOME/rdbms/admin/utlirp.sql
	```
9. Shut down the 64-bit Oracle Database:
	```
	SQL>shutdown immediate;
	```
10. Start the 64-bit Oracle Database:
	```
	SQL> STARTUP pfile=init.ora;
	```
11. If the JServer JAVA Virtual Machine component is installed, perform the following steps after connecting as `SYS`:
	```
	begin
	  update obj$ set status=5 where obj#=(select obj# from obj$,javasnm$
	    where owner#=0 and type#=29 and short(+)=name and
	    nvl(longdbcs,name)='oracle/aurora/rdbms/Compiler');
	  commit;
	  declare
	    cursor C1 is select
	       'DROP JAVA DATA "' || u.name || '"."' || o.name || '"'
	       from obj$ o,user$ u where o.type#=56 and u.user#=o.owner#;
	    ddl_statement varchar2(200);
	    iterations number;
	    previous_iterations number;
	    loop_count number;
	    my_err     number;
	  begin
	    previous_iterations := 10000000;
	    loop
	      -- To make sure we eventually stop, pick a max number of iterations
	      select count(*) into iterations from obj$ where type#=56;
	      exit when iterations=0 or iterations >= previous_iterations;
	      previous_iterations := iterations;
	      loop_count := 0;
	      open C1;
	     loop
	       begin
	         fetch C1 into ddl_statement;
	         exit when C1%NOTFOUND or loop_count > iterations;
	      exception when others then
	         my_err := sqlcode;
	         if my_err = -1555 then -- snapshot too old, re-execute fetch query
	           exit;
	         else
	           raise;
	        end if;
	      end;
	      initjvmaux.exec(ddl_statement);
	      loop_count := loop_count + 1;
	     end loop;
	     close C1;
	    end loop;
	  end;
	  commit;
	  initjvmaux.drp('delete from java$policy$shared$table');
	  update obj$ set status=1 where obj#=(select obj# from obj$,javasnm$ 
	    where owner#=0 and type#=29 and short(+)=name and
	    nvl(longdbcs,name)='oracle/aurora/rdbms/Compiler');
	  commit;
	end;
	/
	create or replace java system;
	/
	```
12. Revalidate all the existing PL/SQL modules in the format required by the 64-bit Oracle Database:
	```
	SQL>$ORACLE_HOME/rdbms/admin/utlrp.sql;
	```

#### B.7.2.2 Migrating 32-Bit Database to 64-Bit Database With Different Directory Structure for Data Files

If the control file, data file, redo log files have different structure on the target computer as compared to the source computer, then perform the following steps:

1. Perform an online backup of the database before starting the migration process. Refer to Online Backup of Database With RMAN for more information.
2. Install Oracle Database 11g Release 2 (11.2) for 64-bit Linux in a new Oracle Database home. It is recommended that you use the same version of Oracle Database home as on the 32-bit computer.
	See Also:
	Oracle Database Installation Guide for Linux
3. Edit `init.ora` file on the 64-bit computer to include the following changes:
	- Update the memory requirements included in the file.
		- The `init.ora` file still contains the 32-bit control file path. You must manually update `control_files` parameter value to include the 64-bit control file location.
	Note:
	Oracle recommends that you double the values of shared pool, java pool, `sga_target` and large pool listed in the `init.ora` file.
4. If the 64-bit target computer contains a different structure for data files, then you must re-create the control file or mount database on 64-bit computer. Refer to Re-aligning Data File Path and Name for more information.
	Note:
	Oracle recommends not to use the `RESETLOGS` option to re-create control files.
5. Set the system to spool results to a log file for later verification of success. For example:
	```
	SQL> SPOOL /tmp/utlirp.log
	```
6. Run the following command on the 64-bit Oracle Database, to invalidate all the PL/SQL modules:
	```
	SQL> @$ORACLE_HOME/rdbms/admin/utlirp.sql
	```
7. Turn off the spooling of script results to the log file:
	```
	SQL> SPOOL OFF;
	```
8. Shut down the 64-bit Oracle Database:
	```
	SQL>shutdown immediate;
	```
9. Start the 64-bit Oracle Database:
	```
	SQL> STARTUP pfile=init.ora;
	```
10. If the JServer JAVA Virtual Machine component is installed, perform the following steps after connecting as `SYS`:
	```
	begin
	  update obj$ set status=5 where obj#=(select obj# from obj$,javasnm$
	    where owner#=0 and type#=29 and short(+)=name and
	    nvl(longdbcs,name)='oracle/aurora/rdbms/Compiler');
	  commit;
	  declare
	    cursor C1 is select
	       'DROP JAVA DATA "' || u.name || '"."' || o.name || '"'
	       from obj$ o,user$ u where o.type#=56 and u.user#=o.owner#;
	    ddl_statement varchar2(200);
	    iterations number;
	    previous_iterations number;
	    loop_count number;
	    my_err     number;
	  begin
	    previous_iterations := 10000000;
	    loop
	      -- To make sure we eventually stop, pick a max number of iterations
	      select count(*) into iterations from obj$ where type#=56;
	      exit when iterations=0 or iterations >= previous_iterations;
	      previous_iterations := iterations;
	      loop_count := 0;
	      open C1;
	     loop
	       begin
	         fetch C1 into ddl_statement;
	         exit when C1%NOTFOUND or loop_count > iterations;
	      exception when others then
	         my_err := sqlcode;
	         if my_err = -1555 then -- snapshot too old, re-execute fetch query
	           exit;
	         else
	           raise;
	        end if;
	      end;
	      initjvmaux.exec(ddl_statement);
	      loop_count := loop_count + 1;
	     end loop;
	     close C1;
	    end loop;
	  end;
	  commit;
	  initjvmaux.drp('delete from java$policy$shared$table');
	  update obj$ set status=1 where obj#=(select obj# from obj$,javasnm$ 
	    where owner#=0 and type#=29 and short(+)=name and
	    nvl(longdbcs,name)='oracle/aurora/rdbms/Compiler');
	  commit;
	end;
	/
	create or replace java system;
	/
	```
11. Revalidate all the existing PL/SQL modules in the format required by the 64-bit Oracle Database:
	```
	SQL>$ORACLE_HOME/rdbms/admin/utlrp.sql;
	```

Re-aligning Data File Path and Name

The following are some methods to realign the data file names and path to point to the correct location:

- Re-creating Control File
- Mounting Database on a 64-Bit Computer

Re-creating Control File

Perform the following steps to re-create the control file:

1. Run the following command to backup the control file to trace. The trace file is located under the `diagnostic_dest` directory on the 32-bit Linux computer. The following command generates a trace file which contains the necessary sql to re-create the control file:
	```
	SQL> alter database backup controlfile to trace;
	```
	Note:
	Ensure that you open the Oracle Database in the `UPGRADE` mode after the control file is created.
2. Rename the trace file generated into `.sql` format on the 32-bit Linux computer. For example:
	```
	$ cp trace.ora control.sql
	```
	The contents of the control file are as follows, for example:
	- Re-creating control files with `NORESETLOGS` option.
		32-bit control file with `NORESETLOGS` option:
		```
		STARTUP NOMOUNT pfile=t_init1.ora
		CREATE CONTROLFILE REUSE DATABASE "L32" NORESETLOGS  NOARCHIVELOG
		    MAXLOGFILES 32
		    MAXLOGMEMBERS 2
		    MAXDATAFILES 32
		    MAXINSTANCES 1
		    MAXLOGHISTORY 454
		LOGFILE
		     GROUP 1 '/ade/aime_l32/oracle/dbs/t_log1.f'  SIZE 25M,
		     GROUP 2 '/ade/aime_l32/oracle/dbs/t_log2.f'  SIZE 25M
		DATAFILE
		     '/ade/aime_l32/oracle/dbs/t_db1.f'
		     '/ade/aime_l32/oracle/dbs/t_ax1.f'
		     '/ade/aime_l32/oracle/dbs/t_undo1.f'
		CHARACTER SET AL32UTF8;
		RECOVER DATABASE;
		ALTER DATABASE OPEN UPGRADE;
		ALTER TABLESPACE TEMP ADD TEMPFILE '/ade/aime_l32/oracle/dbs/t_tmp1.f' SIZE 41943040  REUSE AUTOEXTEND ON NEXT 8192  MAXSIZE 32767M;
		```
		Now, let us consider the modified 64-bit control file:
		```
		STARTUP NOMOUNT pfile=t_init1.ora
		CREATE CONTROLFILE REUSE DATABASE "L32" NORESETLOGS  NOARCHIVELOG
		    MAXLOGFILES 32
		    MAXLOGMEMBERS 2
		    MAXDATAFILES 32
		    MAXINSTANCES 1
		    MAXLOGHISTORY 454
		LOGFILE
		     GROUP 1 '/ade/aime_l64/oracle/dbs/t_log1.f'  SIZE 25M,
		     GROUP 2 '/ade/aime_l64/oracle/dbs/t_log2.f'  SIZE 25M
		DATAFILE
		     '/ade/aime_l64/oracle/dbs/t_db1.f'
		     '/ade/aime_l64/oracle/dbs/t_ax1.f'
		     '/ade/aime_l64/oracle/dbs/t_undo1.f'
		CHARACTER SET AL32UTF8;
		RECOVER DATABASE;
		ALTER DATABASE OPEN UPGRADE;
		ALTER TABLESPACE TEMP ADD TEMPFILE '/ade/aime_l64/oracle/dbs/t_tmp1.f' SIZE 41943040  REUSE AUTOEXTEND ON NEXT 8192  MAXSIZE 32767M;
		```
		- Re-creating control files with `RESETLOGS` option:
		32-bit control file with `RESETLOGS` option:
		```
		STARTUP NOMOUNT pfile=t_init1.ora
		CREATE CONTROLFILE REUSE DATABASE "L32" RESETLOGS  NOARCHIVELOG
		    MAXLOGFILES 32
		    MAXLOGMEMBERS 2
		    MAXDATAFILES 32
		    MAXINSTANCES 1
		    MAXLOGHISTORY 454
		LOGFILE
		     GROUP 1 '/ade/aime_l32/oracle/dbs/t_log1.f'  SIZE 25M,
		     GROUP 2 '/ade/aime_l32/oracle/dbs/t_log2.f'  SIZE 25M
		DATAFILE
		     '/ade/aime_l32/oracle/dbs/t_db1.f'
		     '/ade/aime_l32/oracle/dbs/t_ax1.f'
		     '/ade/aime_l32/oracle/dbs/t_undo1.f'
		CHARACTER SET AL32UTF8;
		RECOVER DATABASE USING BACKUP CONTROLFILE;
		ALTER DATABASE OPEN RESETLOGS UPGRADE;
		ALTER TABLESPACE TEMP ADD TEMPFILE '/ade/aime_l32/oracle/dbs/t_tmp1.f' SIZE 41943040  REUSE AUTOEXTEND ON NEXT 8192  MAXSIZE 32767M;
		```
		Now, let us consider the modified 64-bit control file:
		```
		STARTUP NOMOUNT pfile=t_init1.ora
		CREATE CONTROLFILE REUSE DATABASE "L32" RESETLOGS  NOARCHIVELOG
		    MAXLOGFILES 32
		    MAXLOGMEMBERS 2
		    MAXDATAFILES 32
		    MAXINSTANCES 1
		    MAXLOGHISTORY 454
		LOGFILE
		     GROUP 1 '/ade/aime_l64/oracle/dbs/t_log1.f'  SIZE 25M,
		     GROUP 2 '/ade/aime_l64/oracle/dbs/t_log2.f'  SIZE 25M
		DATAFILE
		     '/ade/aime_l64/oracle/dbs/t_db1.f'
		     '/ade/aime_l64/oracle/dbs/t_ax1.f'
		     '/ade/aime_l64/oracle/dbs/t_undo1.f'
		CHARACTER SET AL32UTF8;
		RECOVER DATABASE USING BACKUP CONTROLFILE;
		ALTER DATABASE OPEN RESETLOGS UPGRADE;
		ALTER TABLESPACE TEMP ADD TEMPFILE '/ade/aime_l64/oracle/dbs/t_tmp1.f' SIZE 41943040  REUSE AUTOEXTEND ON NEXT 8192  MAXSIZE 32767M;
		```
3. Based on the method employed to realign the file paths to point to the correct locations, you must copy the necessary files from the source 32-bit Linux computer to the target 64-bit Linux computer:
	- `NORESETLOGS` option: Copy `init.ora`, data files, re-created control files (`control.sql`), and the redo log files from the 32-bit Linux computer to the corresponding locations on the 64-bit Linux computer
		- `RESETLOGS` option: Copy `init.ora`, data files, and re-created control files (`control.sql`) from the 32-bit Linux computer to the corresponding locations on the 64-bit Linux computer
4. Connect to the database instance as `SYSDBA`:
	```
	SQL> CONNECT / AS SYSDBA;
	```
5. To change from 32-bit to 64-bit, run the following command from the Linux 64-bit Oracle Database home:
	```
	sql>set echo on
	sql>@control.sql
	```

Mounting Database on a 64-Bit Computer

Perform the following steps to mount the database on a 64-bit computer:

1. Copy `init.ora`, data files, control file and the redo log files from the 32-bit Linux computer to the corresponding locations on the 64-bit Linux computer
2. Connect to the database instance as `SYSDBA`:
	```
	SQL> CONNECT / AS SYSDBA;
	```
3. Start the 64-bit Oracle Database as follows:
	```
	SQL> STARTUP mount pfile=init.ora;
	```
4. Update all the 32-bit data file locations to include the 64-bit data file locations. For example:
	```
	sql> alter database rename file '/ade/aime_l32/oracle/dbs/t_db1.f' to '/ade/aime_l64/oracle/dbs/t_db1.f'
	sql> Database altered.
	```
5. Update all the 32-bit log file locations to include the 64-bit log file locations. For example:
	```
	sql> alter database rename file '/ade/aime_l32/oracle/dbs/t_log.f' to '/ade/aime_l64/oracle/dbs/t_log.f'
	sql> Database altered.
	```
6. To change from 32-bit to 64-bit, run the following command from the Linux 64-bit Oracle Database home:
	```
	sql> ALTER DATABASE OPEN UPGRADE;
	```
	Note:
	Refer to [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/intro.htm#UPGRD12354) for more information on changing from 32-bit to 64-bit

### B.7.3 Migrating Data To and From ASM

To take advantage of Automatic Storage Management (ASM), you can migrate an Oracle 11g Release 2 (11.2) database into and out of an ASM disk group using Recovery Manager (RMAN). This migration is performed using RMAN even if you are not using RMAN for your primary backup and recovery strategy.

See Also:

Chapter 8, "Performing ASM Data Migration with RMAN", in [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asm_rman.htm#OSTMG12000) for more information on migrating databases.