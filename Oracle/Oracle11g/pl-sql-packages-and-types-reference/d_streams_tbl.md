---
title: DBMS_STREAMS_TABLESPACE_ADM
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_streams_tbl.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 150 DBMS\_STREAMS\_TABLESPACE\_ADM

The `DBMS_STREAMS_TABLESPACE_ADM` package, one of a set of Oracle Streams packages, provides administrative interfaces for copying tablespaces between databases and moving tablespaces from one database to another. This package uses transportable tablespaces, Data Pump, the `DBMS_FILE_TRANSFER` package, and the `DBMS_FILE_GROUP` package.

This chapter contains the following topics:

See Also:

[Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_ipro.htm#STRMS159) and [Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/toc.htm) for more information about this package and Oracle Streams

---

## Using DBMS\_STREAMS\_TABLESPACE\_ADM

This section contains topics which relate to using the `DBMS_STREAMS_TABLESPACE_ADM` package.

---

### Overview

Either a simple tablespace or a self-contained tablespace set must be specified in each procedure in this package.

A self-contained tablespace has no references from the tablespace pointing outside of the tablespace. For example, if an index in the tablespace is for a table in a different tablespace, then the tablespace is not self-contained. A simple tablespace is a self-contained tablespace that uses only one datafile.

A simple tablespace must be specified in the following procedures:

- ATTACH\_SIMPLE\_TABLESPACE Procedure
- CLONE\_SIMPLE\_TABLESPACE Procedure
- DETACH\_SIMPLE\_TABLESPACE Procedure
- PULL\_SIMPLE\_TABLESPACE Procedure

A self-contained tablespace set has no references from inside the set of tablespaces pointing outside of the set of tablespaces. For example, if a partitioned table is partially contained in the set of tablespaces, then the set of tablespaces is not self-contained.

A self-contained tablespace set must be specified in the following procedures:

- ATTACH\_TABLESPACES Procedure
- CLONE\_TABLESPACES Procedure
- DETACH\_TABLESPACES Procedure
- PULL\_TABLESPACES Procedure

To determine whether a set of tablespaces is self-contained, use the `TRANSPORT_SET_CHECK` procedure in the Oracle supplied package `DBMS_TTS`.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/tspaces.htm#ADMIN011) for more information about self-contained tablespaces and tablespace sets

---

### Security Model

Security on this package can be controlled in either of the following ways:

- Granting `EXECUTE` on this package to selected users or roles.
- Granting `EXECUTE_CATALOG_ROLE` to selected users or roles.

If subprograms in the package are run from within a stored procedure, then the user who runs the subprograms must be granted `EXECUTE` privilege on the package directly. It cannot be granted through a role.

---

## Data Structures

The `DBMS_STREAMS_TABLESPACE_ADM` package defines `RECORD` types and `TABLE` types.

RECORD Types

- FILE Record Type

---

### DIRECTORY\_OBJECT\_SET Table Type

Contains the names of one or more directory objects. Each name must be a directory object created using the SQL statement `CREATE` `DIRECTORY`.

#### Syntax

```
TYPE DIRECTORY_OBJECT_SET IS TABLE OF VARCHAR2(32) 
  INDEX BY BINARY_INTEGER;
```

---

### FILE Record Type

Contains the directory object associated with a directory and the name of the file in the directory.

#### Syntax

```
TYPE FILE IS RECORD(
   directory_object VARCHAR2(32),
   file_name        VARCHAR2(4000));
```

#### Fields

Table 150-1 FILE Fields

| Field | Description |
| --- | --- |
| `directory_object` | The name of a directory object. You must specify the name of a directory object created using the SQL statement `CREATE` `DIRECTORY`. |
| `file_name` | The name of the file in the corresponding directory associated with the directory object |

---

### FILE\_SET Table Type

Contains one or more files.

#### Syntax

```
TYPE FILE_SET IS TABLE OF FILE 
   INDEX BY BINARY_INTEGER;
```

---

### TABLESPACE\_SET Table Type

Contains the names of one or more tablespaces.

#### Syntax

```
TYPE TABLESPACE_SET IS TABLE OF VARCHAR2(32) 
   INDEX BY BINARY_INTEGER;
```

---

## Summary of DBMS\_STREAMS\_TABLESPACE\_ADM Subprograms

Table 150-2 DBMS\_STREAMS\_TABLESPACE\_ADM Package Subprograms

| Subprogram | Description |
| --- | --- |
| ATTACH\_SIMPLE\_TABLESPACE Procedure | Uses Data Pump to import a simple tablespace previously exported using the `DBMS_STREAMS_TABLESPACE_ADM` package or Data Pump export |
| ATTACH\_TABLESPACES Procedure | Uses Data Pump to import a self-contained tablespace set previously exported using the `DBMS_STREAMS_TABLESPACE_ADM` package, Data Pump export, or the Recovery Manager (RMAN) `TRANSPORT` `TABLESPACE` command |
| CLONE\_SIMPLE\_TABLESPACE Procedure | Clones a simple tablespace. The tablespace can later be attached to a database. |
| CLONE\_TABLESPACES Procedure | Clones a set of self-contained tablespaces. The tablespaces can later be attached to a database. |
| DETACH\_SIMPLE\_TABLESPACE Procedure | Detaches a simple tablespace. The tablespace can later be attached to a database. |
| DETACH\_TABLESPACES Procedure | Detaches a set of self-contained tablespaces. The tablespaces can later be attached to a database. |
| PULL\_SIMPLE\_TABLESPACE Procedure | Copies a simple tablespace from a remote database and attaches it to the current database |
| PULL\_TABLESPACES Procedure | Copies a set of self-contained tablespaces from a remote database and attaches the tablespaces to the current database |

Note:

All subprograms commit unless specified otherwise.

---

### ATTACH\_SIMPLE\_TABLESPACE Procedure

This procedure uses Data Pump to import a simple tablespace previously exported using the `DBMS_STREAMS_TABLESPACE_ADM` package, Data Pump export, or the Recovery Manager (RMAN) `TRANSPORT` `TABLESPACE` command.

Syntax

```
DBMS_STREAMS_TABLESPACE_ADM.ATTACH_SIMPLE_TABLESPACE(
   directory_object      IN  VARCHAR2,
   tablespace_file_name  IN  VARCHAR2,
   converted_file_name   IN  VARCHAR2  DEFAULT NULL,
   datafile_platform     IN  VARCHAR2  DEFAULT NULL,
   tablespace_name       OUT VARCHAR2);
```

Parameters

Table 150-3 ATTACH\_SIMPLE\_TABLESPACE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `directory_object` | The directory that contains the Data Pump dump file and the datafile for the tablespace. You must specify the name of a directory object created using the SQL statement `CREATE` `DIRECTORY`.  The name of the Data Pump export dump file must be the same as the data file name for the tablespace, except with a `.dmp` extension. If the `converted_file_name` is non- `NULL`, specify the dump file produced by the export database, not the file name after conversion.  The Data Pump import log file is written to this directory. The name of the log file is the same as the data file name for the tablespace, except with an `.alg` extension. If a file exists with the same name as the log file in the directory, then the procedure overwrites the file.  If `NULL`, then the procedure raises an error. |
| `tablespace_file_name` | The name of the datafile for the tablespace being imported.  If `NULL`, then the procedure raises an error. |
| `converted_file_name` | If the `datafile_platform` parameter is non- `NULL` and is different from the platform of the local import database, then specify a file name for the converted datafile. The datafile is converted to the platform of the local import database and copied to the new file name. The existing datafile is not modified nor deleted.  If non- `NULL` and the `datafile_platform` parameter is `NULL`, then the procedure ignores this parameter.  If non- `NULL` and the `datafile_platform` parameter specifies the same platform as the local import database, then the procedure ignores this parameter.  If `NULL` and the `datafile_platform` parameter is non- `NULL`, then the procedure raises an error. |
| `datafile_platform` | Specify `NULL` if the platform is the same for the export database and the current import database.  Specify the platform for the export database if the platform is different for the export database and the import database.  You can determine the platform of a database by querying the `PLATFORM_NAME` column in the `V$DATABASE` dynamic performance view. The `V$TRANSPORTABLE_PLATFORM` dynamic performance view lists all platforms that support cross-platform transportable tablespaces. |
| `tablespace_name` | Contains the name of the attached tablespace. The attached tablespace is read-only. Use an `ALTER` `TABLESPACE` statement to make the tablespace read/write if necessary. |

Usage Notes

To run this procedure, a user must meet the following requirements:

- Have `IMP_FULL_DATABASE` role
- Have `READ` and `WRITE` privilege on the directory object that contains the Data Pump export dump file and the datafiles for the tablespaces in the set, specified by the `directory_object` parameter

Automatic Storage Management (ASM) directories cannot be used with this procedure.

See Also:

Overview

---

### ATTACH\_TABLESPACES Procedure

This procedure uses Data Pump to import a self-contained tablespace set previously exported using the `DBMS_STREAMS_TABLESPACE_ADM` package, Data Pump export, or the Recovery Manager (RMAN) `TRANSPORT` `TABLESPACE` command.

This procedure is overloaded and consists of the following versions:

- One version of the procedure uses a Data Pump job name in the `datapump_job_name` parameter. This job performs the Data Pump import to complete the attach operation. In addition, if the platform at the export database is different than the local database platform, then this procedure optionally can create datafiles for the tablespace set that can be used with the local platform.
- The other version of the procedure uses a file group that can consist of multiple versions of the tablespace set in a tablespace repository. A tablespace repository is a collection of tablespace sets in a file group repository. When this version of the procedure is run, a Data Pump import is performed. This version of the procedure uses the files in a file group version and can copy the export dump file, export log file, and the datafiles that comprise the tablespace set into the specified directories. The file group and version are specified using the `file_group_name` and `version_name` parameters, respectively. This version of the procedure does not require a datafiles platform specification if the platform at the export database is different than the local database platform. Instead, the tablespace set is migrated automatically to the correct platform when it is attached.

Syntax

```
DBMS_STREAMS_TABLESPACE_ADM.ATTACH_TABLESPACES(
   datapump_job_name          IN OUT VARCHAR2,
   dump_file                  IN     FILE,
   tablespace_files           IN     FILE_SET,
   converted_files            IN     FILE_SET,
   datafiles_platform         IN     VARCHAR2  DEFAULT NULL,
   log_file                   IN     FILE      DEFAULT NULL,
   tablespace_names           OUT    TABLESPACE_SET);

DBMS_STREAMS_TABLESPACE_ADM.ATTACH_TABLESPACES(
   file_group_name            IN   VARCHAR2,
   version_name               IN   VARCHAR2  DEFAULT NULL,
   datafiles_directory_object IN   VARCHAR2  DEFAULT NULL,
   logfile_directory_object   IN   VARCHAR2  DEFAULT NULL,
   repository_db_link         IN   VARCHAR2  DEFAULT NULL,
   tablespace_names           OUT  TABLESPACE_SET);
```

Parameters

Table 150-4 ATTACH\_TABLESPACES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `data_pump_job_name` | The Data Pump job name. Specify a Data Pump job name to adhere to naming conventions or to track the job more easily.  If `NULL`, then the system generates a Data Pump job name. |
| `dump_file` | The file name of the Data Pump dump file to import.  If `NULL` or if a file attribute is `NULL`, then the procedure raises an error. |
| `tablespace_files` | The file set that contains the datafiles for the tablespace set being imported.  If `NULL`, then the procedure raises an error. |
| `converted_files` | If the `datafiles_platform` parameter is non- `NULL` and is different from the platform for the local import database, then specify a file set with the names of the converted datafiles. The datafiles are converted to the platform of the local import database and copied to the new file names. In this case, the number of files in the specified file set must match the number of files in the file set specified for the `tablespace_files` parameter. The existing datafiles are not modified nor deleted.  If non- `NULL` and the `datafiles_platform` parameter is `NULL`, then the procedure ignores this parameter.  If non- `NULL` and the `datafiles_platform` parameter specifies the same platform as the local import database, then the procedure ignores this parameter.  If `NULL` and the `datafiles_platform` parameter is non- `NULL`, then the procedure raises an error. |
| `datafiles_platform` | Specify `NULL` if the platform is the same for the export database and the current import database.  Specify the platform for the export database if the platform is different for the export database and the import database.  You can determine the platform of a database by querying the `PLATFORM_NAME` column in the `V$DATABASE` dynamic performance view. The `V$TRANSPORTABLE_PLATFORM` dynamic performance view lists all platforms that support cross-platform transportable tablespaces. |
| `log_file` | Specify the log file name for the Data Pump import.  If `NULL` or if at least one file parameter is `NULL`, then the system generates a log file name with the extension `.alg` and places it in the Data Pump export dump file directory.  If a file exists with the same name as the log file in the directory, then the procedure overwrites the file. |
| `file_group_name` | The name of the file group, specified as `[schema_name.]file_group_name`. For example, if the schema is `hq_dba` and the file group name is `sales`, then specify `hq_dba.sales`. If the schema is not specified, then the current user is the default. |
| `version_name` | The name of the file group version to attach.  If `NULL`, then the procedure uses the version with the latest creation time for the file group. |
| `datafiles_directory_object` | The directory object into which the datafiles and Data Pump export dump file are copied. The files are copied from the tablespace repository directories to this directory.  If non- `NULL`, the attached tablespaces use the files in specified directory. However, the file group version specified in the `version_name` parameter consists of the files in the original directory, not in the directory specified by this `datafiles_directory_object` parameter.  If `NULL`, then the procedure does not copy the datafiles and dump file. |
| `logfile_directory_object` | The directory object into which the Data Pump import log file is placed. The system generates a log file name with the extension `.alg`.  If `NULL`, then the procedure places the import log file in the same directory as the dump file. |
| `repository_db_link` | If the file group is in a different database, then specify the name of the database link to the database that contains the file group. The database link must be accessible to the user who runs the procedure.  If this parameter is non- `NULL`, then meet the following requirements:  - Each directory object that contains files in the version being attached must exist on both databases. - The corresponding directory objects must have the same names on both databases.  If `NULL`, then the procedure does not use a database link, and the procedure uses the file group in the local database. |
| `tablespace_names` | Contains the names of the attached tablespaces. The attached tablespaces are read-only. Use `ALTER` `TABLESPACE` statements to make the tablespaces read/write if necessary. |

Usage Notes

The following sections contain usage notes for this procedure:

- User Requirements
- Procedures Used to Clone or Detach a Tablespace Set
- When the Attach Database Is Different Than the Clone or Detach Database
- Automatic Storage Management Directories

See Also:

- Overview
- [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_ipro.htm#STRMS159)

User Requirements

To run either version of this procedure, a user must meet the following requirements:

- Have `IMP_FULL_DATABASE` role
- Have `READ` and `WRITE` privilege on the directory objects that contain the Data Pump export dump file and the datafiles for the tablespaces in the set, specified by the `dump_file` and `tablespace_files` parameters, or by the `datafiles_directory_object` parameter
- Have `WRITE` privilege on the directory object that will hold the Data Pump import log file, specified by the `log_file` parameter or `logfile_directory_object` parameter if it is non- `NULL`

If the Data Pump job version of the procedure is run, then the user must have `WRITE` privilege on the directory objects that will hold the converted datafiles for the tablespaces in the set if platform conversion is necessary. These directory objects are specified by the `converted_files` parameter if it is non- `NULL`.

If the file group version of the procedure is run, then the user must have the necessary privileges to manage the file group.

Procedures Used to Clone or Detach a Tablespace Set

After a tablespace set is cloned or detached using the `CLONE_TABLESPACES` or `DETACH_TABLEPSACES` procedure, respectively, the tablespace set can be attached to a database using the `ATTACH_TABLESPACES` procedure. If the Data Pump job version of the `CLONE_TABLESPACES` or `DETACH_TABLEPSACES` procedure was used, then use the Data Pump job version of the `ATTACH_TABLESPACES` procedure. If the file group version of the `CLONE_TABLESPACES` or `DETACH_TABLEPSACES` procedure was used, then use the file group version of the `ATTACH_TABLESPACES` procedure.

See Also:

- CLONE\_TABLESPACES Procedure
- DETACH\_TABLESPACES Procedure

When the Attach Database Is Different Than the Clone or Detach Database

You can attach a tablespace set to a different database than the database from which the tablespace set was cloned or detached. The two databases might or might not share a file system. If the two databases do not share a file system, then you must transfer the dump file and datafiles to the remote system using the `DBMS_FILE_TRANSFER` package, FTP, or some other method. You can attach the tablespace set in one of the following ways depending on the version of the `ATTACH_TABLESPACES` procedure you use:

- If you use the Data Pump job version of the procedure, then specify the relevant files on the file system. The directory object names can be different in the databases.
- If you use the file group version of the procedure, then you can use the `repository_db_link` parameter to specify the database where tablespace repository resides. The directory objects for the files must exist and must match in the databases.

See Also:

- CLONE\_TABLESPACES Procedure
- DETACH\_TABLESPACES Procedure
- [Chapter 67, "DBMS\_FILE\_GROUP"](d_filgrp.md) for more information about file groups

Automatic Storage Management Directories

Automatic Storage Management (ASM) directories can be specified for the directory objects that store datafiles and export dump files, but ASM directories cannot be specified for directory objects that store log files.

See Also:

[Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/dp_overview.htm#SUTIL100) for information about specifying ASM directories for directory objects

---

### CLONE\_SIMPLE\_TABLESPACE Procedure

This procedure clones a simple tablespace. The specified tablespace must be online.

Specifically, this procedure performs the following actions:

1. Makes the specified tablespace read-only if it is not read-only
2. Uses Data Pump to export the metadata for the tablespace and places the dump file in the specified directory
3. Places the datafile for the specified tablespace in the specified directory
4. If this procedure made the tablespace read-only, then makes the tablespace read/write

In addition, this procedure optionally can create a datafile for the tablespace that can be used with a platform that is different than the local database platform.

Syntax

```
DBMS_STREAMS_TABLESPACE_ADM.CLONE_SIMPLE_TABLESPACE(
   tablespace_name      IN  VARCHAR2,
   directory_object     IN  VARCHAR2,
   destination_platform IN  VARCHAR2  DEFAULT NULL,
   tablespace_file_name OUT VARCHAR2);
```

Parameters

Table 150-5 CLONE\_SIMPLE\_TABLESPACE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `tablespace_name` | The tablespace to be cloned.  If `NULL`, then the procedure raises an error. |
| `directory_object` | The directory where the Data Pump export dump file, the Data Pump export log file, and the datafile for the tablespace are placed. You must specify the name of a directory object created using the SQL statement `CREATE` `DIRECTORY`.  The name of the Data Pump export dump file is the same as the data file name for the tablespace, except with a `.dmp` extension. If a file exists with the same name as the dump file in the directory, then the procedure raises an error.  The name of the log file is the same as the data file name for the tablespace, except with a `.clg` extension. If a file exists with the same name as the log file in the directory, then the procedure overwrites the file.  If `NULL`, then the procedure raises an error. |
| `destination_platform` | Specify `NULL` if the platform is the same for the current export database and the intended import database.  Specify the platform for the intended import database if the platform is different for the export database and the import database.  You can determine the platform of a database by querying the `PLATFORM_NAME` column in the `V$DATABASE` dynamic performance view. The `V$TRANSPORTABLE_PLATFORM` dynamic performance view lists all platforms that support cross-platform transportable tablespaces. |
| `tablespace_file_name` | Contains the name of the cloned tablespace datafile. This datafile is placed in the directory specified by the parameter `directory_object`. |

Usage Notes

To run this procedure, a user must meet the following requirements:

- Have `EXP_FULL_DATABASE` role
- Have access to at least one data dictionary view that contains information about the tablespaces. These views include `DBA_TABLESPACES` and `USER_TABLESPACES`.
- Have `MANAGE` `TABLESPACE` or `ALTER` `TABLESPACE` on a tablespace if the tablespace must be made read-only
- Have `READ` privilege on the directory object for the directory that contains the datafile for the tablespace. The name of this tablespace is specified by the `tablespace_name` parameter. If a directory object does not exist for this directory, then create the directory object and grant the necessary privileges before you run this procedure.
- Have `READ` and `WRITE` privilege on the directory object that will contain the Data Pump export dump file, specified by the `directory_object` parameter
- If the file group version of the procedure is run, then the user must have the necessary privileges to manage file group.

After cloning a tablespace using this procedure, you can add the tablespace to a different database using the `ATTACH_SIMPLE_TABLESPACE` procedure. If the database is a remote database and you want to use the `ATTACH_SIMPLE_TABLESPACE` procedure, then you can transfer the dump file and datafile to the remote system using the `DBMS_FILE_TRANSFER` package, FTP, or some other method.

Automatic Storage Management (ASM) directories cannot be used with this procedure.

See Also:

- Overview
- ATTACH\_SIMPLE\_TABLESPACE Procedure and PULL\_SIMPLE\_TABLESPACE Procedure

---

### CLONE\_TABLESPACES Procedure

This procedure clones a set of self-contained tablespaces. All of the tablespaces in the specified tablespace set must be online.

Specifically, this procedure performs the following actions:

1. Makes any read/write tablespace in the specified tablespace set read-only
2. Uses Data Pump to export the metadata for the tablespaces in the tablespace set and places the dump file in the specified directory
3. Places the datafiles that comprise the specified tablespace set in the specified directory
4. If this procedure made a tablespace read-only, then makes the tablespace read/write

This procedure is overloaded and consists of the following versions:

- One version of the procedure uses a Data Pump job name in the `datapump_job_name` parameter. This job performs the Data Pump export. This version of the procedure completes the clone operation by placing the export dump file, export log file, and the datafiles that comprise the tablespace set in the specified directories, but the files are not added to a file group version. In addition, this version of the procedure optionally can create datafiles for the tablespace set that can be used with a platform that is different than the local database platform.
- The other version of the procedure uses a file group that can consist of multiple versions of the tablespace set in a tablespace repository. A tablespace repository is a collection of tablespace sets in a file group repository. When this version of the procedure is run, a Data Pump export is performed, and this version of the procedure completes the clone operation by placing the export dump file, export log file, and the datafiles that comprise the tablespace set in the appropriate file group version. The file group and version are specified using the `file_group_name` and `version_name` parameters, respectively. This version of the procedure does not require a destination platform specification if the destination platform is different. Instead, the tablespace set is migrated automatically to the correct platform when it is attached at the destination database using the file group version of the `ATTACH_TABLESPACES` procedure.

Syntax

```
DBMS_STREAMS_TABLESPACE_ADM.CLONE_TABLESPACES(
   datapump_job_name            IN OUT VARCHAR2,
   tablespace_names             IN     TABLESPACE_SET,
   dump_file                    IN     FILE,
   tablespace_directory_objects IN     DIRECTORY_OBJECT_SET,
   destination_platform         IN     VARCHAR2  DEFAULT NULL,
   log_file                     IN     FILE      DEFAULT NULL,
   tablespace_files             OUT    FILE_SET);

DBMS_STREAMS_TABLESPACE_ADM.CLONE_TABLESPACES(
   tablespace_names             IN  TABLESPACE_SET,
   tablespace_directory_object  IN  VARCHAR2  DEFAULT NULL,
   log_file_directory_object    IN  VARCHAR2  DEFAULT NULL,
   file_group_name              IN  VARCHAR2,
   version_name                 IN  VARCHAR2  DEFAULT NULL,
   repository_db_link           IN  VARCHAR2  DEFAULT NULL);
```

Parameters

Table 150-6 CLONE\_TABLESPACES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `data_pump_job_name` | The Data Pump job name. Specify a Data Pump job name to adhere to naming conventions or to track the job more easily.  If `NULL`, then the system generates a Data Pump job name. |
| `tablespace_names` | The tablespace set to be cloned.  If `NULL`, then the procedure raises an error. |
| `dump_file` | The file name of the Data Pump dump file that is exported.  If `NULL` or if a file attribute is `NULL`, then the procedure raises an error.  If the specified file exists, then the procedure raises an error. |
| `tablespace_directory_objects` | The set of directory objects into which the datafiles for the tablespaces are copied. If multiple directory objects are in the set, then the procedure copies a datafile to each directory object in the set in sequence. In this case, if the end of the directory object set is reached, then datafile copying starts again with the first directory object in the set.  If `NULL`, then the procedure copies datafiles for the tablespace set to the dump file directory. |
| `destination_platform` | Specify `NULL` if the platform is the same for the current export database and the intended import database.  Specify the platform for the intended import database if the platform is different for the export database and the import database.  You can determine the platform of a database by querying the `PLATFORM_NAME` column in the `V$DATABASE` dynamic performance view. The `V$TRANSPORTABLE_PLATFORM` dynamic performance view lists all platforms that support cross-platform transportable tablespaces. |
| `log_file` | Specify the log file name for the Data Pump export.  If `NULL` or if at least one file parameter is `NULL`, then the system generates a log file name with the extension `.clg` and places it in the dump file directory.  If a file exists with the same name as the log file in the directory, then the procedure overwrites the file. |
| `tablespace_directory_object` | The directory object into which the data files are copied and Data Pump export dump file is placed. The system generates a dump file name with the extension `.dmp`.  If `NULL`, then the procedure copies the datafiles to and places the dump file in the default directory object for the version. If the version does not have a default directory object, then the procedure uses the default directory object for the file group.  If `NULL` and no default directory object exists for the version or file group, then the procedure raises an error. |
| `log_file_directory_object` | The directory object into which the Data Pump export log file is placed. The system generates a log file name with the extension `.clg`.  If `NULL`, then the procedure uses the directory object specified in `tablespace_directory_object`. |
| `file_group_name` | The name of the file group, specified as `[schema_name.]file_group_name`. For example, if the schema is `hq_dba` and the file group name is `sales`, then specify `hq_dba.sales`. If the schema is not specified, then the current user is the default.  If the specified file group does not exist, then the procedure creates it. |
| `version_name` | The name of the version into which the cloned tablespace set is placed. The specified version name cannot be a positive integer.  If the specified version does not exist, then the procedure creates it.  If the specified version exists, then the procedure adds the tablespace set to the version. Only one Data Pump export dump file can exist in a version.  If `NULL`, then the procedure creates a new version, and the version number can be used to manage the version. |
| `repository_db_link` | If the file group is in a remote database, then specify the name of the database link to the database that contains the file group. The database link must be accessible to the user who runs the procedure.  If this parameter is non- `NULL`, then the directory object specified in `tablespace_directory_object` must exist on the local database and on the remote database. If `tablespace_directory_object` is `NULL`, then the default directory object must exist on both databases. The directory object must have the same name on each database and must correspond to the same directory on a shared file system.  If `NULL`, then the procedure does not use a database link, and the procedure uses the file group in the local database. |
| `tablespace_files` | Contains the datafiles for the cloned tablespace set. These datafiles are placed in the directories specified by the directory objects in the parameter `tablespace_directory_objects`. |

Usage Notes

To run either version of this procedure, a user must meet the following requirements:

- Have `EXP_FULL_DATABASE` role
- Have access to at least one data dictionary view that contains information about the tablespaces. These views include `DBA_TABLESPACES` and `USER_TABLESPACES`.
- Have `MANAGE` `TABLESPACE` or `ALTER` `TABLESPACE` on a tablespace if the tablespace must be made read-only
- Have `READ` privilege on the directory objects for the directories that contain the datafiles for the tablespace set. The names of these tablespaces are specified by the `tablespace_names` parameter. If a directory object does not exist for one or more of these directories, then create the directory objects and grant the necessary privileges before you run this procedure.
- Have `READ` and `WRITE` privilege on the directory object that will contain the Data Pump export dump file, specified by the `dump_file` parameter or the `tablespace_directory_object` parameter
- Have `WRITE` privilege on the directory objects that will contain the copied datafiles for the tablespaces in the set, specified by the `tablespace_directory_objects` parameter if non- `NULL` or the `tablespace_directory_object` parameter
- Have `WRITE` privilege on the directory object that will contain the Data Pump export log file, specified by the `log_file` parameter if non- `NULL` or the `log_file_directory_object` parameter if non- `NULL`

If the file group version of the procedure is run, then the user must have the necessary privileges to manage the file group.

Automatic Storage Management (ASM) directories can be specified for the directory objects that store datafiles and export dump files, but ASM directories cannot be specified for directory objects that store log files.

After cloning a tablespace set using this procedure, you can attach the tablespaces to a different database using the `ATTACH_TABLESPACES` procedure.

---

### DETACH\_SIMPLE\_TABLESPACE Procedure

This procedure detaches a simple tablespace. The specified tablespace must be online.

Specifically, this procedure performs the following actions:

1. Makes the specified tablespace read-only if it is not read-only
2. Uses Data Pump to export the metadata for the tablespace and places the dump file in the directory that contains the tablespace datafile
3. Drops the tablespace and its contents from the database

Syntax

```
DBMS_STREAMS_TABLESPACE_ADM.DETACH_SIMPLE_TABLESPACE(
   tablespace_name       IN  VARCHAR2,
   directory_object      OUT VARCHAR2,
   tablespace_file_name  OUT VARCHAR2);
```

Parameters

Table 150-7 DETACH\_SIMPLE\_TABLESPACE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `data_pump_job_name` | The Data Pump job name. Specify a Data Pump job name to adhere to naming conventions or to track the job more easily.  If `NULL`, then the system generates a Data Pump job name. |
| `directory_object` | Contains the directory where the Data Pump export dump file and the Data Pump export log file are placed. The procedure uses the directory of the datafile for the tablespace. Therefore, make sure a directory object created using the SQL statement `CREATE` `DIRECTORY` exists for this directory.  The name of the Data Pump export dump file is the same as the data file name for the tablespace, except with a `.dmp` extension. If a file exists with the same name as the dump file in the directory, then the procedure raises an error.  The name of the log file is the same as the data file name for the tablespace, except with a `.dlg` extension. If a file exists with the same name as the log file in the directory, then the procedure overwrites the file. |
| `tablespace_file_name` | Contains the name of the detached tablespace datafile. |

Usage Notes

To run this procedure, a user must meet the following requirements:

- Have `EXP_FULL_DATABASE` role
- Have access to at least one data dictionary view that contains information about the tablespaces. These views include `DBA_TABLESPACES` and `USER_TABLESPACES`.
- Have `DROP` `TABLESPACE` privilege
- Have `MANAGE` `TABLESPACE` or `ALTER` `TABLESPACE` on a tablespace if the tablespace must be made read-only
- Have `READ` and `WRITE` privilege on the directory object for the directory that contains the tablespace datafile. The name of this tablespace is specified by the `tablespace_name` parameter. If a directory object does not exist for this directory, then create the directory object and grant the necessary privileges before you run this procedure. This directory also will contain the Data Pump export dump file generated by this procedure.

After detaching a tablespace using this procedure, you can add the tablespace to a different database using the `ATTACH_SIMPLE_TABLESPACE` procedure. If the database is a remote database and you want to use the `ATTACH_SIMPLE_TABLESPACE` procedure, then you can transfer the dump file and datafile to the remote system using the `DBMS_FILE_TRANSFER` package, FTP, or some other method. You can use the two `OUT` parameters in this procedure to accomplish the attach or pull operation.

Automatic Storage Management (ASM) directories cannot be used with this procedure.

Note:

Do not use the `DETACH_SIMPLE_TABLESPACE` procedure on a tablespace if the tablespace is using the Oracle-managed files feature. If you do, then the datafile for the tablespace is dropped automatically when the tablespace is dropped.

---

### DETACH\_TABLESPACES Procedure

This procedure detaches a set of self-contained tablespaces. All of the tablespaces in the specified tablespace set must be online and any table partitions must not span tablespaces in the tablespace set.

Specifically, this procedure performs the following actions:

1. Makes any read/write tablespace in the specified tablespace set read-only
2. Uses Data Pump to export the metadata for the tablespace set and places the dump file in the specified directory
3. Drops the tablespaces in the specified tablespace set and their contents from the database

This procedure does not move or copy the datafiles that comprise the specified tablespace set.

This procedure is overloaded and consists of the following versions:

- One version of the procedure uses a Data Pump job name in the `datapump_job_name` parameter. This job performs the Data Pump export. This version of the procedure completes the detach operation by placing the export dump file and export log file in the specified directories, but the files are not added to a file group version.
- The other version of the procedure uses a file group that can consist of multiple versions of the tablespace set in a tablespace repository. A tablespace repository is a collection of tablespace sets in a file group repository. When this version of the procedure is run, a Data Pump export is performed, and this version of the procedure completes the detach operation by placing the export dump file and export log file in the appropriate file group version. The datafiles that comprise the tablespace set are not moved or copied, but they are referenced in the version that is detached. The file group and version are specified using the `file_group_name` and `version_name` parameters, respectively. Also, if the destination platform is different, then the tablespace set is migrated automatically to the correct platform when it is attached at the destination database using the file group version of the `ATTACH_TABLESPACES` procedure.

Note:

Do not use the `DETACH_TABLESPACES` procedure if any of the tablespaces in the tablespace set are using the Oracle-managed files feature. If you do, then the datafiles for these tablespaces are dropped automatically when the tablespaces are dropped.

Syntax

```
DBMS_STREAMS_TABLESPACE_ADM.DETACH_TABLESPACES(
   datapump_job_name         IN OUT VARCHAR2,
   tablespace_names          IN     TABLESPACE_SET,
   dump_file                 IN     FILE,
   log_file                  IN     FILE  DEFAULT NULL,
   tablespace_files          OUT    FILE_SET);

DBMS_STREAMS_TABLESPACE_ADM.DETACH_TABLESPACES(
   tablespace_names          IN TABLESPACE_SET,
   export_directory_object   IN VARCHAR2  DEFAULT NULL,
   log_file_directory_object IN VARCHAR2  DEFAULT NULL,
   file_group_name           IN VARCHAR2,
   version_name              IN VARCHAR2  DEFAULT NULL,
   repository_db_link        IN VARCHAR2  DEFAULT NULL);
```

Parameters

Table 150-8 DETACH\_TABLESPACES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `data_pump_job_name` | The Data Pump job name. Specify a Data Pump job name to adhere to naming conventions or to track the job more easily.  If `NULL`, then the system generates a Data Pump job name. |
| `tablespace_names` | The tablespace set to be detached.  If `NULL`, then the procedure raises an error. |
| `dump_file` | The file name of the Data Pump dump file that is exported.  If `NULL` or if a file attribute is `NULL`, then the procedure raises an error.  If the specified file exists, then the procedure raises an error. |
| `log_file` | Specify the log file name for the Data Pump export.  If `NULL` or if at least one file parameter is `NULL`, then the system generates a log file name with the extension `.dlg` and places it in the dump file directory.  If a file exists with the same name as the log file in the directory, then the procedure overwrites the file. |
| `tablespace_files` | Contains the names of the datafiles for the detached tablespace set. |
| `export_directory_object` | The directory object into which the Data Pump export dump file is placed. The system generates a dump file name with the extension `.dmp`.  If `NULL`, then procedure places the dump file in the default directory object for the version. If the version does not have a default directory object, then the procedure uses the default directory object for the file group.  If `NULL` and no default directory object exists for the version or file group, then the procedure raises an error. |
| `log_file_directory_object` | The directory object into which the Data Pump export log file is placed. The system generates a log file name with the extension `.dlg`.  If `NULL`, then the procedure places the export log file in the same directory as the export dump file. |
| `file_group_name` | The name of the file group, specified as `[schema_name.]file_group_name`. For example, if the schema is `hq_dba` and the file group name is `sales`, then specify `hq_dba.sales`. If the schema is not specified, then the current user is the default.  If the specified file group does not exist, then the procedure creates it. |
| `version_name` | The name of the version into which the detached tablespace set is placed. The specified version name cannot be a positive integer.  If the specified version does not exist, then the procedure creates it.  If the specified version exists, then procedure adds the tablespace set to the version. Only one Data Pump export dump file can exist in a version.  If `NULL`, then the procedure creates a new version, and the version number can be used to manage the version. |
| `repository_db_link` | If the file group is in a remote database, then specify the name of the database link to the database that contains the file group. The database link must be accessible to the user who runs the procedure.  If this parameter is non- `NULL`, then the directory object specified in `export_directory_object` must exist on the local database and on the remote database. If `export_directory_object` is `NULL`, then the default directory object must exist on both databases. The directory object must have the same name on each database and must correspond to the same directory on a shared file system.  If `NULL`, then the procedure does not use a database link, and the procedure uses the file group in the local database. |

Usage Notes

To run this either version of this procedure, a user must meet the following requirements:

- Have `EXP_FULL_DATABASE` role
- Have access to at least one data dictionary view that contains information about the tablespaces. These views include `DBA_TABLESPACES` and `USER_TABLESPACES`.
- Have `DROP` `TABLESPACE` privilege
- Have `MANAGE` `TABLESPACE` or `ALTER` `TABLESPACE` on a tablespace if the tablespace must be made read-only
- Have `READ` privilege on the directory objects for the directories that contain the datafiles for the tablespace set. The names of these tablespaces are specified by the `tablespace_names` parameter. If a directory object does not exist for one or more of these directories, then create the directory objects and grant the necessary privileges before you run this procedure.
- Have `READ` and `WRITE` privilege on the directory object that will contain the Data Pump export dump file, specified by the `dump_file` parameter or the `export_directory_object` parameter
- Have `WRITE` privilege on the directory object that will contain the Data Pump export the log file, specified by the `log_file` parameter if non- `NULL` or by the `log_file_directory_object` parameter if non- `NULL`

If the file group version of the procedure is run, then the user must have the necessary privileges to manage the file group.

Automatic Storage Management (ASM) directories can be specified for the directory objects that store datafiles and export dump files, but ASM directories cannot be specified for directory objects that store log files.

After detaching a tablespace set using this procedure, you can attach the tablespaces to a different database using the `ATTACH_TABLESPACES` procedure.

See Also:

- Overview
- ATTACH\_TABLESPACES Procedure
- [Chapter 67, "DBMS\_FILE\_GROUP"](d_filgrp.md) for more information about file groups
- [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_ipro.htm#STRMS159)
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/omf.htm#ADMIN003) for more information about the Oracle-managed files feature

---

### PULL\_SIMPLE\_TABLESPACE Procedure

This procedure copies a simple tablespace from a remote database and attaches it to the current database. The specified tablespace at the remote database must be online.

Specifically, this procedure performs the following actions:

1. Makes the specified tablespace read-only at the remote database if it is not read-only
2. Uses Data Pump to export the metadata for the tablespace
3. Uses a database link and the `DBMS_FILE_TRANSFER` package to transfer the datafile for the tablespace and the log file for the Data Pump export to the current database
4. Places the datafile for the specified tablespace and the log file for the Data Pump export in the specified directory at the local database
5. If this procedure made the tablespace read-only, then makes the tablespace read/write
6. Uses Data Pump to import the metadata for the tablespace in the local database

In addition, this procedure optionally can create a datafile for the tablespace that can be used with the local platform, if the platform at the remote database is different than the local database platform.

Syntax

```
DBMS_STREAMS_TABLESPACE_ADM.PULL_SIMPLE_TABLESPACE(
   tablespace_name          IN VARCHAR2,
   database_link            IN VARCHAR2,
   directory_object         IN VARCHAR2  DEFAULT NULL,
   conversion_extension     IN VARCHAR2  DEFAULT NULL,
   convert_directory_object IN VARCHAR2  DEFAULT NULL);
```

Parameters

Table 150-9 PULL\_SIMPLE\_TABLESPACE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `tablespace_name` | The tablespace to be pulled.  If `NULL`, then the procedure raises an error. |
| `database_link` | The name of the database link to the database that contains the tablespace to pull. The database link must be accessible to the user who runs the procedure.  If `NULL`, then the procedure raises an error. |
| `directory_object` | The directory object to which the datafile for the tablespace is copied on the local database. You must specify the name of a directory object created using the SQL statement `CREATE` `DIRECTORY`.  The Data Pump import log file is written to this directory. The name of the log file is the same as the data file name for the tablespace, except with a `.plg` extension. If a file exists with the same name as the log file in the directory, then the procedure overwrites the file.  If `NULL`, then the procedure raises an error. |
| `conversion_extension` | Specify `NULL` if the platform is the same for the remote export database and the current import database.  If the platform is different for the export database and the import database, then specify an extension for the tablespace datafile that is different than the extension for the tablespace datafile at the remote database. In this case, the procedure transfers the datafile to the import database and converts it to be compatible with the current import database platform automatically. After conversion is complete, the original datafile is deleted at the import database. |
| `convert_directory_object` | Specify `NULL` if the platform is the same for the remote export database and the current import database.  If the platform is different for the export database and the import database, then specify a directory object in the local export database. The procedure uses the directory object for platform conversion before it transfers the files to the remote database. You must specify the name of a directory object created using the SQL statement `CREATE` `DIRECTORY`. |

Usage Notes

To run this procedure, a user must meet the following requirements on the remote database:

- Have the `EXP_FULL_DATABASE` role
- Have `EXECUTE` privilege on the `DBMS_STREAMS_TABLESPACE_ADM` package
- Have access to at least one data dictionary view that contains information about the tablespaces. These views include `DBA_TABLESPACES` and `USER_TABLESPACES`.
- Have `MANAGE` `TABLESPACE` or `ALTER` `TABLESPACE` privilege on a tablespace if the tablespace must be made read-only
- Have `READ` privilege on the directory object for the directory that contains the datafile for the tablespace. The name of this tablespace is specified by the `tablespace_name` parameter. If a directory object does not exist for this directory, then create the directory object and grant the necessary privileges before you run this procedure.

To run this procedure, a user must meet the following requirements on the local database:

- Have the roles `IMP_FULL_DATABASE` and `EXECUTE_CATALOG_ROLE`
- Have `WRITE` privilege on the directory object that will contain the Data Pump export the log file, specified by the `log_file` parameter if non- `NULL`
- Have `WRITE` privilege on the directory object that will hold the datafile for the tablespace, specified by the `directory_object` parameter

Automatic Storage Management (ASM) directories cannot be used with this procedure.

See Also:

Overview

---

### PULL\_TABLESPACES Procedure

This procedure copies a set of self-contained tablespaces from a remote database and attaches the tablespaces to the current database. All of the tablespaces in the specified tablespace set at the remote database must be online.

Specifically, this procedure performs the following actions:

1. Makes any read/write tablespace in the specified tablespace set at the remote database read-only
2. Uses Data Pump to export the metadata for the tablespaces in the tablespace set
3. Uses a database link and the `DBMS_FILE_TRANSFER` package to transfer the datafiles for the tablespace set and the log file for the Data Pump export to the current database
4. Places the datafiles that comprise the specified tablespace set in the specified directories at the local database
5. Places the log file for the Data Pump export in the specified directory at the local database
6. If this procedure made a tablespace read-only, then makes the tablespace read/write
7. Uses Data Pump to import the metadata for the tablespaces in the tablespace set at the local database

In addition, this procedure optionally can create datafiles for the tablespace set that can be used with the local platform, if the platform at the remote database is different than the local database platform.

Syntax

```
DBMS_STREAMS_TABLESPACE_ADM.PULL_TABLESPACES(
   datapump_job_name            IN OUT VARCHAR2,
   database_link                IN     VARCHAR2,
   tablespace_names             IN     TABLESPACE_SET,
   tablespace_directory_objects IN     DIRECTORY_OBJECT_SET,
   log_file                     IN     FILE,
   conversion_extension         IN     VARCHAR2  DEFAULT NULL,
   convert_directory_object     IN     VARCHAR2  DEFAULT NULL);
```

Parameters

Table 150-10 PULL\_TABLESPACES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `data_pump_job_name` | The Data Pump job name. Specify a Data Pump job name to adhere to naming conventions or to track the job more easily.  If `NULL`, then the system generates a Data Pump job name. |
| `database_link` | The name of the database link to the database that contains the tablespace set to pull. The database link must be accessible to the user who runs the procedure.  If `NULL`, then the procedure raises an error. |
| `tablespace_names` | The tablespace set to be pulled.  If `NULL`, then the procedure raises an error. |
| `tablespace_directory_objects` | The set of directory objects to which the datafiles for the tablespaces are copied. If multiple directory objects are in the set, then the procedure copies a datafile to each directory object in the set in sequence. In this case, if the end of the directory object set is reached, then datafile copying starts again with the first directory object in the set.  If `NULL`, then the procedure raises an error. |
| `log_file` | Specify the log file name for the Data Pump export.  If `NULL` or if at least one file parameter is `NULL`, then the system generates a log file name with the extension `.plg` and places it in one of the data file directories.  If a file exists with the same name as the log file in the directory, then the procedure overwrites the file. |
| `conversion_extension` | Specify `NULL` if the platform is the same for the remote export database and the current import database.  If the platform is different for the export database and the import database, then specify an extension for the tablespace datafiles that is different than the extension for the tablespace datafiles at the remote database. In this case, the procedure transfers the datafiles to the import database and converts them to be compatible with the current import database platform automatically. After conversion is complete, the original datafiles are deleted at the import database. |
| `convert_directory_object` | Specify `NULL` if the platform is the same for the remote export database and the current import database.  If the platform is different for the export database and the import database, then specify a directory object in the local export database. The procedure uses the directory object for platform conversion before it transfers the files to the remote database. You must specify the name of a directory object created using the SQL statement `CREATE` `DIRECTORY`. |

Usage Notes

To run this procedure, a user must meet the following requirements on the remote database:

- Have the `EXP_FULL_DATABASE` role
- Have `EXECUTE` privilege on the `DBMS_STREAMS_TABLESPACE_ADM` package
- Have access to at least one data dictionary view that contains information about the tablespaces. These views include `DBA_TABLESPACES` and `USER_TABLESPACES`.
- Have `MANAGE` `TABLESPACE` or `ALTER` `TABLESPACE` privilege on a tablespace if the tablespace must be made read-only
- Have `READ` privilege on the directory objects for the directories that contain the datafiles for the tablespace set. The names of these tablespaces are specified by the `tablespace_names` parameter. If a directory object does not exist for one or more of these directories, then create the directory objects and grant the necessary privileges before you run this procedure.

To run this procedure, a user must meet the following requirements on the local database:

- Have the roles `IMP_FULL_DATABASE` and `EXECUTE_CATALOG_ROLE`
- Have `WRITE` privilege on the directory object that will contain the Data Pump export the log file, specified by the `log_file` parameter if non- `NULL`
- Have `WRITE` privilege on the directory objects that will hold the datafiles for the tablespaces in the set, specified by the `tablespace_directory_objects` parameter

Automatic Storage Management (ASM) directories can be specified for the directory objects that store datafiles and export dump files, but ASM directories cannot be specified for directory objects that store log files.

See Also:

Overview