---
title: "Administrator’s Guide"
book: "Multitenant Administrator's Guide"
doc_id: E96136-19
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/multi/using-database-utilities-in-a-cdb.html
tags:
  - oracle
  - 19c
  - multitenant-administrators-guide
---

## 21 Using Database Utilities in a Multitenant Environment

You can use utilities such as Oracle Data Pump, DBNEWID, and Oracle LogMiner in a multitenant environment.

- Importing and Exporting Data in a CDB  
	Oracle Data Pump technology enables very high-speed movement of data and metadata from one database to another.
- Using LogMiner in a CDB  
	You can use LogMiner in a multitenant container database (CDB).
- DBNEWID Considerations for CDBs and PDBs  
	The DBNEWID parameter `PDB` allows you to change the DBID on pluggable databases (PDBs).

**Parent topic:** [Using Oracle Features in a Multitenant Environment](using-oracle-features-in-a-multitenant-environment.md)

### Importing and Exporting Data in a CDB

Oracle Data Pump technology enables very high-speed movement of data and metadata from one database to another.

**Parent topic:** Using Database Utilities in a Multitenant Environment

#### About Using Data Pump in a Multitenant Environment

In general, using Data Pump with PDBs is identical to using Data Pump with a non-CDB.

A multitenant container database (CDB) is an Oracle database that includes zero, one, or many user-created pluggable databases (PDBs). A PDB is a portable set of schemas, schema objects, and nonschema objects that appear to an Oracle Net client as a non-CDB. A non-CDB is an Oracle database that is not a CDB.

You can use Data Pump to migrate all or some of a database in the following scenarios:

- From a non-CDB into a PDB
- Between PDBs within the same or different CDBs
- From a PDB into a non-CDB

Note:

Data Pump does not support any CDB-wide operations. If you are connected to the root or seed database of a CDB, then Data Pump issues the following warning:

```
ORA-39357: Warning: Oracle Data Pump operations are not typically needed when connected to the root or seed of a container database.
```

**Parent topic:** Importing and Exporting Data in a CDB

#### Using Data Pump to Move Data Into a CDB

After you create an empty PDB, you can use an Oracle Data Pump full-mode export and import operation to move data into the PDB.

You can import data with or without the transportable option. If you use the transportable option on a full mode export or import, then it is referred to as a full transportable export/import.

When the transportable option is used, export and import use both transportable tablespace data movement and conventional data movement; the latter for those tables that reside in non-transportable tablespaces such as `SYSTEM` and `SYSAUX`. Using the transportable option can reduce the export time and especially, the import time, because table data does not need to be unloaded and reloaded and index structures in user tablespaces do not need to be recreated.

Note the following requirements when using Data Pump to move data into a CDB:

- To administer a multitenant environment, you must have the `CDB_DBA` role.
- Full database exports from Oracle Database 11.2.0.2 and earlier can be imported into Oracle Database 12c (CDB or non-CDB). However, Oracle recommends that you first upgrade the source database to Oracle Database 11g release 2 (11.2.0.3 or later), so that information about registered options and components is included in the export.
- When migrating Oracle Database 11g release 2 (11.2.0.3 or later) to a CDB (or to a non-CDB) using either full database export or full transportable database export, you must set the Data Pump Export parameter `VERSION=12` in order to generate a dump file that is ready for import into Oracle Database 12c. If you do not set `VERSION=12`, then the export file that is generated does not contain complete information about registered database options and components.
- Network-based full transportable imports require use of the `FULL=YES`, `TRANSPORTABLE=ALWAYS`, and `TRANSPORT_DATAFILES=datafile_name` parameters. When the source database is Oracle Database 11g release 11.2.0.3 or later, but earlier than Oracle Database 12c Release 1 (12.1), the `VERSION=12` parameter is also required.
- File-based full transportable imports only require use of the `TRANSPORT_DATAFILES=datafile_name` parameter. Data Pump Import infers the presence of the `TRANSPORTABLE=ALWAYS` and `FULL=YES` parameters.
- As of Oracle Database 12c release 2 (12.2), in a multitenant container database (CDB) environment, the default Data Pump directory object, `DATA_PUMP_DIR`, is defined as a unique path for each PDB in the CDB. This unique path is defined whether the `PATH_PREFIX` clause of the `CREATE PLUGGABLE DATABASE` statement is defined or is not defined for relative paths.
- Starting in Oracle Database 19c, the `credential` parameter of `impdp` specifies the name of the credential object that contains the user name and password required to access an object store bucket. You can also specify a default credential using the PDB property named `DEFAULT_CREDENTIAL`. When you run `impdb` with then default credential, you prefix the dump file name with `DEFAULT_CREDENTIAL:` and you do not specify the `credential` parameter.

Example 21-1 Importing a Table into a PDB

To specify a particular PDB for the export/import operation, supply a connect identifier in the connect string when you start Data Pump. For example, to import data to a PDB named `pdb1`, you could enter the following on the Data Pump command line:

```
impdp hr@pdb1 DIRECTORY=dpump_dir1 DUMPFILE=hr.dmp TABLES=employees
```

Example 21-2 Specifying a Credential When Importing Data

This example assumes that you created a credential named `HR_CRED` using `DBMS_CREDENTIAL.CREATE_CREDENTIAL` as follows:

```
BEGIN
  DBMS_CLOUD.CREATE_CREDENTIAL(
    credential_name => 'HR_CRED',
    username => 'atpc_user@oracle.com',
    password => 'password'
  );
END;
/
```

The following command specifies credential `HR_CRED`, and specifies the a file stored in an object store. The URL of the file is `https://example.com/ostore/dnfs/myt.dmp`.

```
impdp hr@pdb1 \
      table_exists_action=replace \
      credential=HR_CRED \
      parallel=16 \
      dumpfile=https://example.com/ostore/dnfs/myt.dmp
```

Example 21-3 Importing Data Using a Default Credential

1. You create a credential named `HR_CRED` using `DBMS_CREDENTIAL.CREATE_CREDENTIAL` as follows:
	```
	BEGIN
	  DBMS_CLOUD.CREATE_CREDENTIAL(
	    credential_name => 'HR_CRED',
	    username => 'atpc_user@oracle.com',
	    password => 'password'
	  );
	END;
	/
	```
2. You set the PDB property `DEFAULT_CREDENTIAL` as follows:
	```
	ALTER DATABASE PROPERTY SET DEFAULT_CREDENTIAL = 'ADMIN.HR_CRED'
	```
3. The following command specifies the default credential as a prefix to the dump file location `https://example.com/ostore/dnfs/myt.dmp`:
	```
	impdp hr@pdb1 \
	      table_exists_action=replace \
	      parallel=16 \
	      dumpfile=default_credential:https://example.com/ostore/dnfs/myt.dmp
	```
	Note that the `credential` parameter is not specified.

See Also:

- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=DBSEG-GUID-6AD89576-526F-4D6B-A539-ADF4B840819F) to learn how to configure SSL authentication, which is necessary for object store access
- [Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SUTIL-GUID-D11E340E-14C6-43B8-AB09-6335F0C1F71B) to learn about using Data Pump Import to load files to the object store

**Parent topic:** Importing and Exporting Data in a CDB

#### Using Data Pump to Move PDBs Within Or Between CDBs

Data Pump export and import operations on PDBs are identical to those on non-CDBs, with the exception of how common users are handled.

If you have created a common user in a CDB, then a full database or privileged schema export of that user from within any PDB in the CDB results in a standard `CREATE USER C##common name` DDL statement being performed upon import. The statement will fail because of the common user prefix `C##` on the user name. The following error message will be returned:

```
ORA-65094:invalid local user or role name
```

In the PDB being exported, if you have created local objects in that user's schema and you want to import them, then either make sure a common user of the same name already exists in the target CDB instance or use the Data Pump Import `REMAP_SCHEMA` parameter on the `impdp` command, as follows:

```
REMAP_SCHEMA=C##common name:local user name
```

### Using LogMiner in a CDB

You can use LogMiner in a multitenant container database (CDB).

The following sections discuss some differences to be aware of when using LogMiner in a CDB versus a non-CDB:

LogMiner supports CDBs that have PDBs of different character sets provided the root container has a character set that is a superset of all the PDBs.

To administer a multitenant environment you must have the `CDB_DBA` role.

- LogMiner V$ Views and DBA Views in a CDB  
	In a CDB, views used by LogMiner to show information about LogMiner sessions running in the system contain an additional column named `CON_ID`.
- The V$LOGMNR\_CONTENTS View in a CDB  
	In a CDB, the `V$LOGMNR_CONTENTS` view and its associated functions are restricted to the root database. Several new columns exist in `V$LOGMNR_CONTENTS` in support of CDBs.
- Enabling Supplemental Logging in a CDB  
	In a CDB, the syntax for enabling and disabling database-wide supplemental logging using the `ALTER DATABASE` command.
- Using a Flat File Dictionary in a CDB  
	You cannot take a dictionary snapshot for an entire CDB in a single flat file. You must be connected to a distinct PDB, and can take a snapshot of only that PDB in a flat file.

**Parent topic:** Using Database Utilities in a Multitenant Environment

#### LogMiner V$ Views and DBA Views in a CDB

In a CDB, views used by LogMiner to show information about LogMiner sessions running in the system contain an additional column named `CON_ID`.

The `CON_ID` column identifies the container ID associated with the session for which information is being displayed. When you query the view from a pluggable database (PDB), only information associated with the database is displayed. The following views are affected by this new behavior:

- `V$LOGMNR_DICTIONARY_LOAD`
- `V$LOGMNR_LATCH`
- `V$LOGMNR_PROCESS`
- `V$LOGMNR_SESSION`
- `V$LOGMNR_STATS`

Note:

To support CDBs, the `V$LOGMNR_CONTENTS` view has several other new columns in addition to `CON_ID`.

The following DBA views have analogous CDB views whose names begin with CDB.

| Type of Log View | DBA View | CDB View |
| --- | --- | --- |
| LogMiner Log Views | `DBA_LOGMNR_LOG` | `CDB_LOGMNR_LOG` |
| LogMiner Purged Log Views | `DBA_LOGMNR_PURGED_LOG` | `CDB_LOGMNR_PURGED_LOG` |
| LogMiner Session Log Views | `DBA_LOGMNR_SESSION` | `CDB_LOGMNR_SESSION` |

The DBA views show only information related to sessions defined in the container in which they are queried.

The CDB views contain an additional `CON_ID` column, which identifies the container whose data a given row represents. When CDB views are queried from the root, they can be used to see information about all containers.

**Parent topic:** Using LogMiner in a CDB

#### The V$LOGMNR\_CONTENTS View in a CDB

In a CDB, the `V$LOGMNR_CONTENTS` view and its associated functions are restricted to the root database. Several new columns exist in `V$LOGMNR_CONTENTS` in support of CDBs.

- `CON_ID` — contains the ID associated with the container from which the query is executed. Because `V$LOGMNR_CONTENTS` is restricted to the root database, this column returns a value of 1 when a query is done on a CDB.
- `SRC_CON_NAME` — the PDB name. This information is available only when mining is performed with a LogMiner dictionary.
- `SRC_CON_ID` — the container ID of the PDB that generated the redo record. This information is available only when mining is performed with a LogMiner dictionary.
- `SRC_CON_DBID` — the PDB identifier. This information is available only when mining is performed with a current LogMiner dictionary.
- `SRC_CON_GUID` — contains the GUID associated with the PDB. This information is available only when mining is performed with a current LogMiner dictionary.

**Parent topic:** Using LogMiner in a CDB

#### Enabling Supplemental Logging in a CDB

In a CDB, the syntax for enabling and disabling database-wide supplemental logging using the `ALTER DATABASE` command.

For example, use the following syntax when adding or dropping supplemental log data:

```
ALTER DATABASE [ADD|DROP] SUPPLEMENTAL LOG DATA ...
```

Note the following:

- In a CDB, supplemental logging levels that are enabled from `CDB$ROOT` are enabled across the CDB.
- If at least minimal supplemental logging is enabled in `CDB$ROOT`, then additional supplemental logging levels can be enabled at the PDB level.
- Supplemental logging levels enabled at the CDB level from `CDB$ROOT` cannot be disabled at the PDB level.
- Dropping all supplemental logging from `CDB$ROOT` disables all supplemental logging across the CDB regardless of previous PDB level settings.

Supplemental logging operations started with `CREATE TABLE` and `ALTER TABLE` statements can be executed from either the CDB root or a PDB. They affect only the table to which they are applied.

**Parent topic:** Using LogMiner in a CDB

#### Using a Flat File Dictionary in a CDB

You cannot take a dictionary snapshot for an entire CDB in a single flat file. You must be connected to a distinct PDB, and can take a snapshot of only that PDB in a flat file.

Thus, when using a flat file dictionary, you can only mine the redo logs for the changes associated with the PDB whose data dictionary is contained within the flat file.

**Parent topic:** Using LogMiner in a CDB

### DBNEWID Considerations for CDBs and PDBs

The DBNEWID parameter `PDB` allows you to change the DBID on pluggable databases (PDBs).

By default, when you run the DBNEWID utility on a container database (CDB) it changes the DBID of only the CDB; the DBIDs of the pluggable databases (PDBs) comprising the CDB remain the same. This could cause problems with duplicate DBIDs for PDBs in some cases, such as when a CDB is cloned.

As of Oracle Database 12c Release 2 (12.2), you can change the DBID on the PDBs by using the new DBNEWID `PDB` parameter. You cannot specify a particular PDB; either all of them or none of them will have new DBIDs. The `PDB` parameter is applicable only in a CDB environment. It has the following format:

```
PDB=[ALL | NONE]
```
- If you specify `ALL`, then in addition to the DBID for the CDB changing, the DBIDs for all PDBs comprising the CDB are also changed.
- Specifying `NONE` (the default) leaves the PDB DBIDs the same, even if the CDB DBID is changed.

Oracle recommends that you use `PDB=ALL`, but `PDB=NONE` is the default for backward compatibility reasons.

**Parent topic:** Using Database Utilities in a Multitenant Environment