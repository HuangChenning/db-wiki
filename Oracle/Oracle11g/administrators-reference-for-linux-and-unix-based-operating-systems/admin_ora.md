---
title: Administering Oracle Database
book: "Administrator's Reference for Linux and UNIX-Based Operating Systems"
doc_id: E10839-25
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e10839/admin_ora.htm
tags:
  - oracle
  - 11g
  - administrators-reference-for-linux-and-unix-based-operating-systems
---

## 1 Administering Oracle Database

This chapter provides information about administering Oracle Database on UNIX-based operating systems. It contains the following sections:

See Also:

The appropriate appendix in this guide for platform-specific information about administering Oracle Database

## 1.1 Overview

You must set Oracle Database environment variables, parameters, and user settings for Oracle Database to work. This chapter describes the various settings for Oracle Database.

In Oracle Database files and programs, a question mark (?) represents the value of the `ORACLE_HOME` environment variable. For example, Oracle Database expands the question mark in the following SQL statement to the full path of the Oracle home directory:

```
SQL> ALTER TABLESPACE TEMP ADD DATAFILE '?/dbs/temp02.dbf' SIZE 200M
```

Similarly, the at sign (@) represents the `ORACLE_SID` environment variable. For example, to indicate a file that belongs to the current instance, run the following command:

```
SQL> ALTER TABLESPACE tablespace_name ADD DATAFILE tempfile@.dbf
```

You can create a syslog audit trail to track administrative activities.

See Also:

"Using the Syslog Audit Trail to Audit System Administrators on UNIX Systems" in [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/auditing.htm#DBSEG66112) for more information on audit trails.

## 1.2 Environment Variables

This section describes the most commonly used Oracle Database and operating system environment variables. You must define some environment variables before installing Oracle Database. This section covers the following topics:

- Oracle Database Environment Variables
- UNIX Environment Variables
- Setting a Common Environment
- Setting the System Time Zone

To display the current value of an environment variable, use the `env` command. For example, to display the value of the `ORACLE_SID` environment variable, run the following command:

```
$ env | grep ORACLE_SID
```

To display the current value of all environment variables, run the `env` command as follows:

```
$ env | more
```

### 1.2.1 Oracle Database Environment Variables

Table 1-1 describes some environment variables used with Oracle Database.

Table 1-1 Oracle Database Environment Variables

| Variable | Detail | Definition |
| --- | --- | --- |
| `NLS_LANG` | Function | Specifies the language, territory, and character set of the client environment. The client character set specified by `NLS_LANG` must match the character set of the terminal or terminal emulator. If required, `NLS_LANG` can be temporarily reset to another character set before starting a non-interactive batch program to match the character set of files and scripts processed by this program. The character set specified by `NLS_LANG` can be different from the database character set, in which case the character set is automatically converted.  Refer to [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm) for a list of values for this variable. |
|  | Syntax | `language_territory.characterset` |
|  | Example | `french_france.we8iso8859p15` |
| `ORA_NLS10` | Function | Specifies the directory where the language, territory, character set, and linguistic definition files are stored. |
|  | Syntax | `directory_path` |
|  | Example | `$ORACLE_HOME/nls/data` |
| `ORA_TZFILE` | Function | Specifies the full path and file name of the time zone file. The Oracle Database Server always uses the large time zone file (`$ORACLE_HOME/oracore/zoneinfo/timezlrg_` `number``.dat`). If you want to use the small time zone file on the client side, you must set this environment variable to the full path of the small time zone file (`$ORACLE_HOME/oracore/zoneinfo/timezone_` `number``.dat`). If you use the small time zone file on the client side, you must ensure that the database you access contains data only in the time zone regions recognized by the small time zone file. |
|  | Syntax | `directory_path` |
|  | Example | `$ORACLE_HOME/oracore/zoneinfo/timezlrg_11.dat` |
| `ORACLE_BASE` | Function | Specifies the base of the Oracle directory structure for Optimal Flexible Architecture compliant installations. |
|  | Syntax | `directory_path` |
|  | Example | `/u01/app/oracle` |
| `ORACLE_HOME` | Function | Specifies the directory containing the Oracle software. |
|  | Syntax | `directory_path` |
|  | Example | `$ORACLE_BASE/product/11.2.0/dbhome_1` |
| `ORACLE_PATH` | Function | Specifies the search path for files used by Oracle applications such as SQL\*Plus. If the full path to the file is not specified, or if the file is not in the current directory, then the Oracle application uses `ORACLE_PATH` to locate the file. |
|  | Syntax | Colon-separated list of directories:  ``` directory1:directory2:directory3 ``` |
|  | Example | `/u01/app/oracle/product/11.2.0/dbhome_1/bin:.`  Note: The period adds the current working directory to the search path. |
| `ORACLE_SID` | Function | Specifies the Oracle system identifier. |
|  | Syntax | A string of numbers and letters that must begin with a letter. Oracle recommends a maximum of 8 characters for system identifiers. For more information about this environment variable, refer to [Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST). |
|  | Example | SAL1 |
| `ORACLE_TRACE` | Function | Enables the tracing of shell scripts during an installation. If it is set to `T`, then many Oracle shell scripts use the `set -x` command, which prints commands and their arguments as they are run. If it is set to any other value, or no value, then the scripts do not use the `set -x` command. |
|  | Syntax | `T` or not `T` |
|  | Example | `T` |
| `ORAENV_ASK` | Function | Controls whether the `oraenv` or `coraenv` script prompts or does not prompt for the value of the `ORACLE_SID` environment variable. If it is set to `NO`, then the scripts do not prompt for the value of the `ORACLE_SID` environment variable. If it is set to any other value, or no value, then the scripts prompt for a value for the `ORACLE_SID` environment variable. |
|  | Syntax | `NO` or not `NO` |
|  | Example | `NO` |
| `SQLPATH` | Function | Specifies the directory or list of directories that SQL\*Plus searches for a `login.sql` file. |
|  | Syntax | Colon-separated list of directories: `directory1:directory2:directory3` |
|  | Example | `/home:/home/oracle:/u01/oracle` |
| `TNS_ADMIN` | Function | Specifies the directory containing the Oracle Net Services configuration files. |
|  | Syntax | `directory_path` |
|  | Example | `$ORACLE_HOME/network/admin` |
| `TWO_TASK` | Function | Specifies the default connect identifier to use in the connect string. If this environment variable is set, then do not specify the connect identifier in the connect string. For example, if the `TWO_TASK` environment variable is set to `sales`, then you can connect to a database by using the following command:  ``` SQL> CONNECT USERNAME Enter password: password ``` |
|  | Syntax | Any connect identifier. |
|  | Range of Values | Any valid connect identifier that can be resolved by using a naming method, such as a `tnsnames.ora` file or a directory server. |
|  | Example | `PRODDB_TCP` |
| `NLS_OS_CHARSET` | Function | Specifies the Oracle character set name corresponding to the UNIX locale character set in which the file names and user names are encoded by the operating system. You must set the environment variable `NLS_OS_CHARSET,` if the UNIX locale character set is different from the Oracle client character set. These two character sets may differ, for example, if `NLS_LANG` is set to a particular character set used to encode an SQL script, which is to be executed in an SQL\*Plus session. Usually, the Oracle client character set and the operating system character set are the same and `NLS_OS_CHARSET` must not be set. |
|  | Syntax | `characterset` |
|  | Example | `WE8ISO8859P1` |

Note:

To prevent conflicts, do not define environment variables with names that are identical to the names of Oracle Database server processes, for example `ARCH`, `PMON`, and `DBWR`.

### 1.2.2 UNIX Environment Variables

Table 1-2 describes UNIX environment variables used with Oracle Database.

Table 1-2 Environment Variables Used with Oracle Database

| Variable | Detail | Definition |
| --- | --- | --- |
| `ADA_PATH` (AIX only) | Function | Specifies the directory containing the Ada compiler |
|  | Syntax | `directory_path` |
|  | Example | `/usr/lpp/powerada` |
| `ORA_FPU_PRECISION` (Linux x86 only) | Function | For all precompiled applications where calculations are done using the extended precision of the x86 Floating Point Unit, this variable must be set to `EXTENDED` before running the application.  Note: Setting this variable results in non-IEEE compliant floating point results. Hence, `ORA_FPU_PRECISION` should not be set if you are using either `BINARY_FLOAT` or `BINARY_DOUBLE` datatypes, documented as note 246916.1 in My Oracle Support (formerly OracleMetaLink) Web site:  `https://support.oracle.com` |
| `CLASSPATH` | Function | Used with Java applications. The required setting for this variable depends on the Java application. Refer to the product documentation for Java application for more information. |
|  | Syntax | Colon-separated list of directories or files: `directory1:directory2:file1:file2` |
|  | Example | There is no default setting. `CLASSPATH` must include the following directories:  `$ORACLE_HOME/jdk/jre/lib:$ORACLE_HOME/jlib` |
| `DISPLAY` | Function | Used by X-based tools. Specifies the display device used for input and output. Refer to the X Window System documentation for information. |
|  | Syntax | ``` hostname:server[.screen] ```  where `hostname` is the system name (either IP address or alias), `server` is the sequential code number for the server, and `screen` is the sequential code number for the screen. If you use a single monitor, then use the value `0` for both server and screen (`0.0`).  Note: If you use a single monitor, then `screen` is optional. |
|  | Example | ``` 135.287.222.12:0.0 bambi:0 ``` |
| `HOME` | Function | The home directory of the user. |
|  | Syntax | `directory_path` |
|  | Example | `/home/oracle` |
| `LANG` or `LC_ALL` | Function | Specifies the language and character set used by the operating system for messages and other output. Oracle tools that are programmed in Java, such as Oracle Universal Installer and Oracle Database Configuration Assistant, may also use this variable to determine the language of their user interface. Refer to the operating system documentation for more information. |
| `LD_OPTIONS` | Function | Specifies the default linker options. Refer to the `ld` man page for more information about this environment variable. |
| `LPDEST` (Solaris only) | Function | Specifies the name of the default printer. |
|  | Syntax | `string` |
|  | Example | `docprinter` |
| `LD_LIBRARY_PATH` | Function | Environment variable to specify the path used to search for libraries on UNIX and Linux. The environment variable may have a different name on some operating systems, such as `LIBPATH` on AIX, and `SHLIB_PATH` on HP-UX. |
|  | Syntax | Colon-separated list of directories: `directory1:directory2:directory3` |
|  | Example | `/usr/dt/lib:$ORACLE_HOME/lib` |
| `PATH` | Function | Used by the shell to locate executable programs; must include the `$ORACLE_HOME/bin` directory. |
|  | Syntax | Colon-separated list of directories: `directory1:directory2:directory3` |
|  | Example | `/bin:/usr/bin:/usr/local/bin:/usr/bin/X11:$ORACLE_HOME/bin:   $HOME/bin:.`  Note: The period adds the current working directory to the search path. |
| `PRINTER` | Function | Specifies the name of the default printer. |
|  | Syntax | `string` |
|  | Example | `docprinter` |
| `TEMP`, `TMP`, and `TMPDIR` | Function | Specifies the default directories for temporary files; if set, tools that create temporary files create them in one of these directories. |
|  | Syntax | `directory_path` |
|  | Example | `/u02/oracle/tmp` |
| `USER` (when using telnet to connect on HP-UX Itanium systems) | Function | Specifies the name of the user logging in. |
|  | Syntax | `string` |
|  | Example | `oracle` |

### 1.2.3 Setting a Common Environment

This section describes how to set a common operating system environment by using the `oraenv` or `coraenv` scripts, depending on the default shell:

- For the Bourne, Bash, or Korn shell, use the `oraenv` command.
- For the C shell, use the `coraenv` command.

oraenv and coraenv Script Files

The `oraenv` and `coraenv` scripts are created during installation. These scripts set environment variables based on the contents of the `oratab` file and provide:

- A central means of updating all user accounts with database changes
- A mechanism for switching between databases specified in the `oratab` file

You may find yourself frequently adding and removing databases from the development system or your users may be switching between several different Oracle Databases installed on the same system. You can use the `oraenv` or `coraenv` script to ensure that user accounts are updated and to switch between databases.

Note:

Do not call the `oraenv` or `coraenv` script from the Oracle software owner (typically, `oracle`) user's shell startup script. Because these scripts prompt for values, they can prevent the `dbstart` script from starting a database automatically when the system starts.

The `oraenv` or `coraenv` script is usually called from the user's shell startup file (for example, `.profile` or`.login`). It sets the `ORACLE_SID` and `ORACLE_HOME` environment variables and includes the `$ORACLE_HOME/bin` directory in the `PATH` environment variable setting. When switching between databases, users can run the `oraenv` or `coraenv` script to set these environment variables.

Note:

To run one of these scripts, use the appropriate command:
- `coraenv` script:
	```
	% source /usr/local/bin/coraenv
	```
- `oraenv` script:
	```
	$ . /usr/local/bin/oraenv
	```

Local bin Directory

The directory that contains the `oraenv`, `coraenv`, and `dbhome` scripts is called the local `bin` directory. All database users must have read access to this directory. Include the path of the local bin directory `PATH` environment variable setting for the users. When you run the `root.sh` script after installation, the script prompts you for the path of the local `bin` directory and automatically copies the `oraenv`, `coraenv`, and `dbhome` scripts to the directory that you specify. The default local `bin` directory is `/usr/local/bin`. If you do not run the `root.sh` script, then you can manually copy the `oraenv` or `coraenv` and `dbhome` scripts from the `$ORACLE_HOME/bin` directory to the local `bin` directory.

### 1.2.4 Setting the System Time Zone

The `TZ` environment variable sets the time zone. It enables you to adjust the clock for daylight saving time changes or different time zones.

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/ch3globenv.htm#NLSPG003) and [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN11094) for more information about setting the database time zone

## 1.3 Initialization Parameters

The following sections provide information about Oracle Database initialization parameters:

- DB\_BLOCK\_SIZE Initialization Parameter
- ASM\_DISKSTRING Initialization Parameter
- LOG\_ARCHIVE\_DEST\_n Initialization Parameter
- DISK\_ASYNCH\_IO Initialization Parameter (HP-UX)

### 1.3.1 DB\_BLOCK\_SIZE Initialization Parameter

The `DB_BLOCK_SIZE` initialization parameter specifies the standard block size for the database. This block size is used for the `SYSTEM` tablespace and by default in other tablespaces.

The maximum value to which you can set the `DB_BLOCK_SIZE` is 16 KB on Linux x86. It is 32 KB on other platforms.

Note:

You cannot change the value of the `DB_BLOCK_SIZE` initialization parameter after you create a database.

### 1.3.2 ASM\_DISKSTRING Initialization Parameter

Note:

Only Automatic Storage Management instances support the `ASM_DISKSTRING` initialization parameter.

The syntax for assigning a value to the `ASM_DISKSTRING` initialization parameter is as follows:

```
ASM_DISKSTRING = 'path1'[,'path2', . . .]
```

In this syntax, `pathn` is the path to a raw device. You can use wildcard characters when specifying the path.

Table 1-3 lists the platform-specific default values for the `ASM_DISKSTRING` initialization parameter.

Table 1-3 Default Values of the ASM\_DISKSTRING Initialization Parameter

| Platform | Default Search String |
| --- | --- |
| AIX | `/dev/rhdisk*` |
| HP-UX | `/dev/rdisk/*` |
| Solaris | `/dev/rdsk/*` |
| Linux | `/dev/raw/*` |

### 1.3.3 LOG\_ARCHIVE\_DEST\_n Initialization Parameter

The maximum value that you can set for `ASYNC` in the `LOG_ARCHIVE_DEST_` n initialization parameter differs on UNIX platforms as listed in the following table:

| Platform | Maximum Value |
| --- | --- |
| HP-UX | 51200 |
| Other operating systems | 102400 |

### 1.3.4 DISK\_ASYNCH\_IO Initialization Parameter (HP-UX)

The `DISK_ASYNCH_IO` initialization parameter determines whether the database files reside on raw disks or file systems. Asynchronous I/O is available only with Automatic Storage Management disk group which uses raw partitions as the storage option for database files. The `DISK_ASYNCH_IO` parameter can be set to `TRUE` or `FALSE` depending on where the files reside. By default, the value is set to `TRUE`.

Note:

The `DISK_ASYNCH_IO` parameter must be set to `FALSE` when the database files reside on file system. This parameter must be set to `TRUE` only when the database files reside on raw partitions.

## 1.4 Operating System Accounts and Groups

This section describes the following special operating system accounts and groups that are required by Oracle Database:

- Creating Additional Operating System Accounts
- Configuring the Accounts of Oracle Users

### 1.4.1 Creating Additional Operating System Accounts

If required, create additional operating system accounts. Users must be members of the OSDBA or OSOPER groups to connect to the database with administrator privileges.

### 1.4.2 Configuring the Accounts of Oracle Users

Update the startup files of the `oracle` user and the operating system accounts of Oracle users, specifying the appropriate environment variables in the environment file.

For the Bourne, Bash, or Korn shell, add the environment variables to the `.profile` file, or the `.bash_profile` file for the Bash shell on Red Hat Enterprise Linux.

For the C shell, add the environment variables to the `.login` file.

Note:

You can use the `oraenv` or `coraenv` script to ensure that Oracle user accounts are updated.

## 1.5 Using Trace Files

This section describes the trace (or dump) that Oracle Database creates to help you diagnose and resolve operating problems.

Each server and background process writes to a trace file. When a process detects an internal error, it writes information about the error to its trace file. The file name format of a trace file is `sid_processname_unixpid``.trc`, where:

- `sid` is the instance system identifier
- `processname` is a three or four-character abbreviated process name identifying the Oracle Database process that generated the file (for example, `pmon`, `dbwr`, `ora`, or `reco`)
- `unixpid` is the operating system process ID number

The following is a sample trace file name:

```
$ORACLE_BASE/diag/rdbms/mydb/mydb/trace/test_lgwr_1237.trc
```

The size of the trace file is limited by the `MAX_DUMP_FILE_SIZE` initialization parameter. By default, it is set to `UNLIMITED`, which allows the trace file to grow indefinitely. If you set it to an explicit value other than `UNLIMITED`, the trace file splits into multiple segments.