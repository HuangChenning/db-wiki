---
title: DBMS_LOGMNR_D
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_logmnrd.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 85 DBMS\_LOGMNR\_D

The `DBMS_LOGMNR_D` package, one of a set of LogMiner packages, contains two subprograms:

- The `BUILD` procedure extracts the LogMiner data dictionary to either the redo log files or to a flat file. This information is saved in preparation for future analysis of redo log files using the LogMiner tool.
- The `SET_TABLESPACE` procedure re-creates all LogMiner tables in an alternate tablespace.
	The LogMiner data dictionary consists of the memory data structures and the database tables that are used to store and retrieve information about objects and their versions. It is referred to as the LogMiner dictionary throughout the LogMiner documentation.

See Also:

[Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/logminer.htm#SUTIL019) for information regarding LogMiner.

This chapter contains the following topics:

- Using DBMS\_LOGMNR\_D
	- Overview
		- Security Model
- Summary of DBMS\_LOGMNR\_D Subprograms

---

## Using DBMS\_LOGMNR\_D

This section contains the following topics, which relate to using the `DBMS_LOGMNR_D` package:

- Overview
- Security Model

---

### Overview

LogMiner requires a dictionary to translate object IDs into object names when it returns redo data to you. LogMiner gives you three options for supplying the dictionary:

- Using the online catalog
- Extracting a LogMiner dictionary to the redo log files
- Extracting a LogMiner dictionary to a flat file

Use the `BUILD` procedure to extract the LogMiner dictionary to the redo log files or a flat file. If you want to specify the online catalog as the dictionary source, you do so when you start LogMiner with the `DBMS_LOGMNR.START_LOGMNR` package.

Use the `SET_TABLESPACE` procedure if you want LogMiner tables to use a tablespace other than the default `SYSAUX` tablespace.

See Also:

[DBMS\_LOGMNR](d_logmnr.md) for information on the package subprograms used in running a LogMiner session.

---

### Security Model

You must have the `EXECUTE_CATALOG_ROLE` role to use the `DBMS_LOGMNR_D` package.

---

## Summary of DBMS\_LOGMNR\_D Subprograms

Table 85-1 DBMS\_LOGMNR\_D Package Subprograms

| Subprogram | Description |
| --- | --- |
| BUILD Procedure | Extracts the LogMiner dictionary to either a flat file or one or more redo log files |
| SET\_TABLESPACE Procedure | Re-creates all LogMiner tables in an alternate tablespace |

---

### BUILD Procedure

This procedure extracts the LogMiner data dictionary to either the redo log files or to a flat file.

Syntax

```
DBMS_LOGMNR_D.BUILD (
     dictionary_filename  IN  VARCHAR2,
     dictionary_location  IN  VARCHAR2,
     options              IN  NUMBER);
```

Parameters

Table 85-2 BUILD Procedure Parameters

| Parameter | Description |
| --- | --- |
| `dictionary_filename` | Specifies the name of the LogMiner dictionary file. |
| `dictionary_location` | Specifies the path to the LogMiner dictionary file directory. |
| `options` | Specifies that the LogMiner dictionary is written to either a flat file (`STORE_IN_FLAT_FILE`) or the redo log files (`STORE_IN_REDO_LOGS`). |

Exceptions

Table 85-3 BUILD Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ora-01302` | Dictionary build options are missing or incorrect.  This error is returned under the following conditions:  - If the value of the `OPTIONS` parameter is not one of the supported values (`STORE_IN_REDO_LOGS`, `STORE_IN_FLAT_FILE)` or is not specified - If the `STORE_IN_REDO_LOGS` option is not specified and neither the `dictionary_filename` nor the `dictionary_location` parameter is specified - If the `STORE_IN_REDO_LOGS` option is specified and either the `dictionary_filename` or the `dictionary_location` parameter is specified |
| `ora-01308` | Initialization parameter `UTL_FILE_DIR` is not set. |
| `ora-01336` | Specified dictionary file cannot be opened.  This error is returned under the following conditions:  - The specified value for the `dictionary_location` does not exist. - `The UTL_FILE_DIR` initialization parameter is not set to have access to the `dictionary_location` - The dictionary file is read-only. |

Usage Notes

- To extract the LogMiner dictionary to a flat file, you must supply a filename and location.
	To extract the LogMiner dictionary to the redo log files, specify only the `STORE_IN_REDO_LOGS` option. The size of the LogMiner dictionary may cause it to be contained in multiple redo log files.
	The combinations of parameters used result in the following behavior:
	- If you do not specify any parameters, an error is returned.
		- If you specify a filename and location, without any options, the LogMiner dictionary is extracted to a flat file with that name.
		- If you specify a filename and location, as well as the `STORE_IN_FLAT_FILE` option, the LogMiner dictionary is extracted to a flat file with the specified name.
		- If you do not specify a filename and location, but do specify the `STORE_IN_REDO_LOGS` option, the LogMiner dictionary is extracted to the redo log files.
		- If you specify a filename and location, as well as the `STORE_IN_REDO_LOGS` option, an error is returned.
		- If you do not specify a filename and location, but do specify the `STORE_IN_FLAT_FILE` option, an error is returned.
- Ideally, the LogMiner dictionary file will be created after all database dictionary changes have been made and prior to the creation of any redo log files that are to be analyzed. As of Oracle9i release 1 (9.0.1), you can use LogMiner to dump the LogMiner dictionary to the redo log files or a flat file, perform DDL operations, and dynamically apply the DDL changes to the LogMiner dictionary.
- Do not run the `DBMS_LOGMNR_D.BUILD` procedure if there are any ongoing DDL operations.
- The database must be open when you run the `DBMS_LOGMNR_D.BUILD` procedure.
- When extracting a LogMiner dictionary to a flat file, the procedure queries the dictionary tables of the current database and creates a text-based file containing the contents of the tables. To extract a LogMiner dictionary to a flat file, the following conditions must be met:
	- You must specify a directory for use by the PL/SQL procedure. To do so, set the initialization parameter `UTL_FILE_DIR` in the initialization parameter file. For example:
		```
		UTL_FILE_DIR = /oracle/dictionary
		```
		After setting the parameter, you must shut down and restart the database for this parameter to take effect. If you do not set this parameter, the procedure will fail.
		- You must ensure that no DDL operations occur while the LogMiner dictionary build is running. Otherwise, the LogMiner dictionary file may not contain a consistent snapshot of the database dictionary.
	Be aware that the `DDL_DICT_TRACKING` option to the `DBMS_LOGMNR.START_LOGMNR` procedure is not supported for flat file dictionaries created prior to Oracle9i. If you attempt to use the `DDL_DICT_TRACKING` option with a LogMiner database extracted to a flat file prior to Oracle9i, the ORA-01330 error (problem loading a required build table) is returned.
- To extract a LogMiner dictionary file to the redo log files, the following conditions must be met:
	- The `DBMS_LOGMNR_D.BUILD` procedure must be run on a system that is running Oracle9i or later.
		- Archivelog mode must be enabled in order to generate usable redo log files.
		- The `COMPATIBLE` parameter in the initialization parameter file must be set to 9.2.0 or higher.
		- The database to which LogMiner is attached must be Oracle9i or later.
	In addition, supplemental logging (at least the minimum level) should be enabled to ensure that you can take advantage of all the features that LogMiner offers. See [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/toc.htm) for information about using supplemental logging with LogMiner.

Examples

Example 1: Extracting the LogMiner Dictionary to a Flat File

The following example extracts the LogMiner dictionary file to a flat file named `dictionary.ora` in a specified path (`/oracle/database`).

```
SQL> EXECUTE dbms_logmnr_d.build('dictionary.ora', - 
     '/oracle/database/', -
     options => dbms_logmnr_d.store_in_flat_file);
```

Example 2: Extracting the LogMiner Dictionary to the Redo Log Files

The following example extracts the LogMiner dictionary to the redo log files.

```
SQL> EXECUTE dbms_logmnr_d.build( -
     options => dbms_logmnr_d.store_in_redo_logs);
```

---

### SET\_TABLESPACE Procedure

By default, all LogMiner tables are created to use the `SYSAUX` tablespace. However, it may be desirable to have LogMiner tables use an alternate tablespace. Use this procedure to move LogMiner tables to an alternate tablespace.

Syntax

```
DBMS_LOGMNR_D.SET_TABLESPACE (
     new_tablespace        IN VARCHAR2);
```

Parameters

Table 85-4 SET\_TABLESPACE Parameter

| Parameter | Description |
| --- | --- |
| `new_tablespace` | A string naming a preexisting tablespace. To move all LogMiner tables to employ this tablespace, supply this parameter. |

Usage Notes

- Users upgrading from earlier versions of Oracle Database may find LogMiner tables in the `SYSTEM` tablespace. Oracle encourages such users to consider using the `SET_TABLESPACE` procedure to move the tables to the `SYSAUX` tablespace once they are confident that they will not be downgrading to an earlier version of Oracle Database.
- Users of this routine must supply an existing tablespace.
	See Also:
	[Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm) and [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for information about tablespaces and how to create them

Example: Using the DBMS\_LOGMNR\_D.SET\_TABLESPACE Procedure

The following example shows the creation of an alternate tablespace and execution of the `DBMS_LOGMNR_D`.`SET_TABLESPACE` procedure.

```
SQL> CREATE TABLESPACE  logmnrts$ datafile '/usr/oracle/dbs/logmnrts.f'
     SIZE 25 M REUSE AUTOEXTEND ON MAXSIZE UNLIMITED;

SQL> EXECUTE dbms_logmnr_d.set_tablespace('logmnrts$');
```