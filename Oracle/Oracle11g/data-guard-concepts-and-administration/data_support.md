---
title: Data Type and DDL Support on a Logical Standby Database
book: Data Guard Concepts and Administration
doc_id: E41134-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41134/data_support.htm
tags:
  - oracle
  - 11g
  - data-guard-concepts-and-administration
---

## C Data Type and DDL Support on a Logical Standby Database

When setting up a logical standby database, you must ensure the logical standby database can maintain the datatypes and tables in your primary database. This appendix lists the various database objects, storage types, and PL/SQL supplied packages that are supported and unsupported by logical standby databases. It contains the following topics:

## C.1 Datatype Considerations

The following sections list the supported and unsupported database objects:

- Supported Datatypes in a Logical Standby Database
- Unsupported Datatypes in a Logical Standby Database

### C.1.1 Supported Datatypes in a Logical Standby Database

Logical standby databases support the following datatypes:

- `BINARY_DOUBLE`
- `BINARY_FLOAT`
- `BLOB`
- `CHAR`
- `CLOB` and `NCLOB`
- `DATE`
- `INTERVAL YEAR TO MONTH`
- `INTERVAL DAY TO SECOND`
- `LONG`
- `LONG RAW`
- `NCHAR`
- `NUMBER`
- `NVARCHAR2`
- `RAW`
- `TIMESTAMP`
- `TIMESTAMP WITH TIMEZONE`
- `TIMESTAMP WITH LOCAL TIMEZONE`
- `VARCHAR` and `VARCHAR2`
- LOBs stored as SecureFiles (requires that the primary database be run at a compatibility of 11.2 or higher. See Section C.14, "Support for SecureFiles LOBs".)
- `XMLType` data for all storage models, assuming the following primary database compatibility requirements:
	- `XMLType` stored in `CLOB` format requires primary database to run at a compatibility of 11.1 or higher
		- `XMLType` stored in object-relational format or as binary XML requires that the primary database be running Oracle Database 11g Release 2 (11.2.0.3) or higher with a redo compatibility setting of 11.2.0.3 or higher

#### C.1.1.1 Compatibility Requirements

SQL Apply support for the following has compatibility requirements on the primary database:

- Multibyte `CLOB` support requires primary database to run at a compatibility of 10.1 or higher.
- IOT support without `LOB` s and Overflows requires primary database to run at a compatibility of 10.1 or higher.
- IOT support with `LOB` and Overflow requires primary database to run at a compatibility of 10.2 or higher.
- TDE support requires primary database to run at a compatibility of 11.1 or higher.
- Segment compression requires primary database to run at a compatibility of 11.1 or higher.
- Hybrid Columnar Compression support is dependent on the underlying storage system.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/tablecls.htm#CNCPT89198) for more information about Hybrid Columnar Compression

### C.1.2 Unsupported Datatypes in a Logical Standby Database

The following data types are not supported by Logical standby databases. If a table contains columns having any of these unsupported data types, then the entire table is ignored by SQL Apply.

  
`BFILE`  
Collections (including `VARRAYS` and nested tables)  
Multimedia data types (including Spatial, Image, and Oracle Text)  
`ROWID`, `UROWID`  
User-defined types

## C.2 Support for Transparent Data Encryption (TDE)

Data Guard SQL Apply can be used to provide data protection for a primary database with Transparent Data Encryption (TDE) enabled. Consider the following when using a logical standby database to provide data protection for applications with advanced security requirements:

- Tables with Transparent Data Encryption using server held keys are replicated on a logical standby database when both the primary and the standby databases are running at a compatibility level of 11.1 or higher.
- Transparent Data Encryption in the context of Hardware Security Modules is not supported for logical standby databases in 11g Release 1.

You must consider the following restrictions when, in the context of a logical standby database, you want to replicate tables that have encrypted columns:

1. To translate encrypted redo records, SQL Apply must have access to an open wallet containing the Transparent Data Encryption keys. Therefore, you must copy the wallet containing the keys from the primary database to the standby database after it has been created.
2. The wallet must be copied from the primary database to the logical standby database every time the master key is changed.
3. Oracle recommends that you not rekey the master key at the logical standby database while the logical standby database is replicating encrypted tables from the primary database. Doing so may cause SQL Apply to halt when it encounters an encrypted redo record.
4. You can rekey the encryption key of a replicated table at the logical standby database. This requires that you lower the guard setting to `NONE` before you issue the rekey command.
5. Replicated encrypted tables can use a different encryption scheme for columns than the one used in the primary database. For example, if the `SALARY` column of the `HR.EMPLOYEES` table is encrypted at the primary database using the AES192 encryption algorithm, it can be encrypted at the logical standby using the AES256 encryption algorithm. Or, the `SALARY` column can remain unencrypted at the logical standby database.

## C.3 Support for Tablespace Encryption

Data Guard SQL Apply can be used to provide data protection for a primary database that has tablespace encryption enabled. In such a case, restrictions 1, 2, and 3 listed in Section C.2, "Support for Transparent Data Encryption (TDE)" will apply.

Note:

In some cases, when SQL Apply mines and applies redo records for changes made to tables in encrypted tablespaces, records of user data in unencrypted form may be kept for a long period of time. If this is not acceptable, you should issue the following command to move all metadata tables pertaining to the mining component of SQL Apply to an encrypted tablespace:
```
SQL> DBMS_LOGMNR_D.SET_TABLESPACE(NEW_TABLESPACE => 'ENCRYPTED_LOGMNR_TS');
```

## C.4 Support For Row-level Security and Fine-Grained Auditing

As of Oracle Database 11g, Logical Standby can automatically replicate the security environment provided through the `DBMS_RLS` and `DBMS_FGA` PL/SQL packages. This support simplifies management of security considerations when a server fails over to the standby since the security environment will transparently be maintained. It also ensures that access control policies applied to the primary data can be automatically forwarded to the standby, and the standby data transparently given the same level of protection. If a standby server is newly created with 11g, this replication is enabled by default; otherwise it has to be enabled by the DBA at an appropriate time.

Support for the replication of these PL/SQL packages requires that both the primary and the standby be running with a compatibility setting of 11.1 or higher.

It also requires that the table referenced be a Logical Standby maintained object. For example, a table with a rowid column will not have its data maintained by Logical Standby, in which case `DBMS_RLS` and `DBMS_FGA` calls referencing that table will also not be maintained.

### C.4.1 Row-level Security

Row-Level Security, also known as Virtual Private Database (VPD), is a feature that enforces security at a fine level of granularity, when accessing tables, views, or synonyms. When a user directly or indirectly accesses a table, view, or synonym protected with a VPD policy, the server dynamically modifies the SQL statement of the user. The modification creates a `WHERE` condition (known as a predicate) returned by a function implementing the security policy. The statement is modified dynamically, transparently to the user, using any condition that can be expressed in, or returned by, a function. VPD policies can be applied to `SELECT`, `INSERT`, `UPDATE`, `INDEX`, and `DELETE` statements. VPD is implemented by using the `DBMS_RLS` package to apply security policies.

When a `DBMS_RLS` procedure is executed on the primary, additional information is captured in the redo that allows the procedure call to be logically reconstructed and executed on the standby. Logical Standby supports replication of ancillary objects for VPD such as Contexts, Database Logon Triggers, and their supporting packages. You must ensure that these objects are placed in maintained schemas and that no DDL skips have been configured that would stop their replication.

### C.4.2 Fine-Grained Auditing

Fine-grained auditing provides a way to audit select statements. The `DBMS_FGA` package enables all select statements that access a table to be captured, together with what data was accessed. An FGA policy may be applied to a particular column or even to only those select statements that return rows for which a specified predicate returns `TRUE`.

When a `DBMS_FGA` procedure is executed on the primary, additional information is captured to the redo that allows the procedure call to be logically reconstructed and executed on the standby.

### C.4.3 Skipping and Enabling PL/SQL Replication

PL/SQL can be configured with skip and skip\_error rules exactly as DDL statements except that wildcarding on the package and procedure are not supported. For example to skip all aspects of VPD, do the following:

```
DBMS_LOGSTDBY.Skip (
stmt => 'PL/SQL',
schema_name => 'SYS',
object_name =>'DBMS_RLS',
use_like => FALSE);
```

Note that the schema specified is the schema in which the package is defined. To skip an individual procedure in a package, the syntax would be as follows:

```
DBMS_LOGSTDBY.Skip (
stmt => 'PL/SQL',
schema_name => 'SYS',
object_name =>'DBMS_RLS.Add_Policy',
use_like => FALSE);
```

In order to skip VPD on certain schemas or tables, a skip procedure must be used. The skip procedure will be passed the fully qualified PL/SQL statement that is to be executed, for example:

```
DBMS_RLS.Drop_Policy(
object_schema => 'SCOTT, 
object_name  => 'EMP',
policy_name => 'MYPOLICY');
```

The procedure could then parse the statement to decide whether to skip it, to apply it, or to stop apply and let the DBA take a compensating action.

Unlike DDL, skip procedures on PL/SQL do not support returning a replacement statement.

## C.5 Oracle Label Security

Logical standby databases do not support Oracle Label Security. If Oracle Label Security is installed on the primary database, SQL Apply fails on the logical standby database with an internal error during startup.

## C.6 Oracle E-Business Suite

Logical standby databases do not fully support an Oracle E-Business Suite implementation because there are tables that contain unsupported data types. However, using `SKIP` rules, it is possible for you to replicate a subset of the E-Business Suite schemas and tables to offload applications to the logical standby.

See Also:

The My Oracle Support note 851603.1 at `http://support.oracle.com` for additional information about using Logical standby with Oracle E-Business Suite

## C.7 Supported Table Storage Types

Logical standby databases support the following table storage types:

- Cluster tables (including index clusters and heap clusters)
- Index-organized tables (partitioned and nonpartitioned, including overflow segments)
- Heap-organized tables (partitioned and nonpartitioned)
- OLTP table compression (`COMPRESS FOR OLTP`) and basic table compression (`COMPRESS BASIC`). OLTP table compression and basic table compression require that the compatibility setting of the primary database be set to 11.1.0 or higher.
- Tables with virtual columns (provided the table has no other columns or properties not supported by logical standby). This support is available only in Oracle Database 11g Release 2 (11.2.0.3) and higher.
- Tables using Hybrid Columnar Compression
	See Also:
	- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/tablecls.htm#CNCPT89198) for more information about Hybrid Columnar Compression

## C.8 Unsupported Table Storage Types

Logical standby does not support tables that contain only the following datatypes:

- `LOB` (`CLOB`, `NCLOB`, `BLOB`)
- `LONG`
- `LONG` `RAW`
- `OBJECT` `TYPE`
- `COLLECTIONS`
- `XML`

See Also:

Support for SecureFiles LOBs

## C.9 PL/SQL Supplied Packages Considerations

This section discusses the following considerations regarding PL/SQL supplied packages:

- Supported PL/SQL Supplied Packages
- Unsupported PL/SQL Supplied Packages
- Handling XML and XDB PL/SQL Packages in Logical Standby

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for more information about Oracle PL/SQL supplied packages

### C.9.1 Supported PL/SQL Supplied Packages

Oracle PL/SQL supplied packages that do not modify system metadata or user data leave no footprint in the archived redo log files, and hence are safe to use on the primary database. Examples of such packages are `DBMS_OUTPUT`, `DBMS_RANDOM`, `DBMS_PIPE`, `DBMS_DESCRIBE`, `DBMS_OBFUSCATION_TOOLKIT`, `DBMS_TRACE`, `DBMS_METADATA`, `DBMS_CRYPTO`.

Oracle PL/SQL supplied packages that do not modify system metadata but may modify user data are supported by SQL Apply, as long as the modified data belongs to the supported data types listed in Section C.1.1. Examples of such packages are `DBMS_LOB`, `DBMS_SQL`, and `DBMS_TRANSACTION`.

Data Guard logical standby supports replication of actions performed through the following packages: `DBMS_RLS`, `DBMS_FGA`, and `DBMS_REDEFINITION`.

### C.9.2 Unsupported PL/SQL Supplied Packages

Oracle PL/SQL supplied packages that modify system metadata typically are not supported by SQL Apply, and therefore their effects are not visible on the logical standby database. Examples of such packages are `DBMS_JAVA`, `DBMS_REGISTRY`, `DBMS_ALERT`, `DBMS_SPACE_ADMIN`, `DBMS_REFRESH`, `and DBMS_AQ`.

Specific support for `DBMS_JOB` has been provided. Jobs created on the primary database are replicated on the standby database, but will not be run as long as the standby maintains its standby role. In the event of a switchover or failover, jobs scheduled on the original primary database will automatically begin running on the new primary database.

You can also create jobs at the logical standby. These jobs will only run as long as the logical standby maintains it standby role.

Specific support for `DBMS_SCHEDULER` has been provided to allow jobs to be run on a standby database. A new attribute of a scheduler job has been created in 11g called `database_role` whose contents match the `database_role` attribute of `V$DATABASE`. When a scheduler job is created, it defaults to the local role (that is, a job created on the standby defaults to a `database_role` of `LOGICAL STANDBY`). The job scheduler executes only jobs specific to the current role. On switchover or failover, the scheduler automatically switches to running jobs specific to the new role.

Scheduler jobs are not replicated to the standby. However, existing jobs can be activated under the new role by using the `DBMS_SCHEDULER.Set_Attribute` procedure. Alternatively, jobs that should run in both roles can be cloned and the copy made specific to the other role. The `DBA_SCHEDULER_JOB_ROLES` view shows which jobs are specific to which role.

Scheduler jobs obey the database guard when they run on a logical standby database. Thus, in order to run jobs that need to modify unmaintained tables, the database guard should be set to `STANDBY`. (It is not possible to use the `ALTER SESSION DISABLE GUARD` statement inside a PL/SQL block and have it take effect.)

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for details about specific packages

### C.9.3 Handling XML and XDB PL/SQL Packages in Logical Standby

In Oracle Database 11g release 1 (11.1), Logical Standby supports XML when it is stored in CLOB format. However, there are several PL/SQL packages used in conjunction with XML that are not fully supported.

The PL/SQL packages and procedures that are supported by Logical Standby only modify in-memory structures; they do not modify data stored in the database. These packages do not generate redo and therefore are not replicated to a Logical Standby.

Certain PL/SQL packages and procedures related to XML and XDB that are not supported by Logical Standby, but that require corresponding invocations at the logical standby database for replication activities to continue, are instrumented such that invocations of these procedures at the primary database will generate additional redo records indicating procedure invocation. When SQL Apply encounters such redo records, it stops and writes an error message in the `DBA_LOGSTDBY_EVENTS` table, indicating the procedure name. This allows the DBA to invoke the corresponding procedure at the logical standby database at the appropriate time so that subsequent redo records generated at the primary database can be applied successfully at the logical standby database. See Section C.9.3.1 through Section C.9.3.6 for more information about dealing with these unsupported procedures.

The following packages contain unsupported procedures:

- `DBMS_XMLSCHEMA`
- `DBMS_XMLINDEX`

In addition to these packages, Logical Standby does not support any modifications to the XDB schema. The objects within the XDB schema are considered to be system metadata and direct modifications to them are not replicated.

Tables managed by the Oracle XML DB Repository, also known as hierarchy-enabled tables, are not supported by Logical Standby. These tables are used to store XML data and can be accessed using the FTP and HTTP protocols, as well as the normal SQL access. For more information on these tables, refer to the [Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/toc.htm).

#### C.9.3.1 The DBMS\_XMLSCHEMA Schema

The following procedures within the DBMS\_XMLSCHEMA package are unsupported and cannot be replicated by Logical Standby. Logical Standby stops when it encounters calls to these procedures to provide the user an opportunity to take a compensating action for these calls. Sections Section C.9.3.3 through Section C.9.3.6 provide more information on the alternatives available for dealing with these unsupported procedures.

- `REGISTERSCHEMA`
- `REGISTERURI`
- `DELETESCHEMA`
- `PURGESCHEMA`
- `COPYEVOLVE`
- `INPLACEEVOLVE`
- `COMPILESCHEMA`

The XDB schema is an Oracle managed schema. Any changes to this schema are automatically skipped by Logical Standby. The following procedure makes changes to the XDB schema which will not be replicated:

- `GENERATEBEAN`

The following procedures and functions do not generate redo and therefore do not stop Logical Standby:

- `GENERATESCHEMAS`
- `GENERATESCHEMA`

#### C.9.3.2 The DBMS\_XMLINDEX Package

The `SYNCINDEX` procedure within the `DBMS_XMLINDEX` package is marked as unsupported and cannot be replicated by Logical Standby. Logical Standby stops when it encounters calls to it.

The following functions and procedures do not generate redo and therefore do not stop Logical Standby:

- `NODEREFGETREF`
- `NODEREFGETVALUE`
- `NODEREFGETPARENTREF`
- `NODEREFGETNAME`
- `NODEREFGETNAMESPACE`

#### C.9.3.3 Dealing With Unsupported PL/SQL Procedures

There are a couple options for dealing with unsupported PL/SQL procedures. The first option is to allow the Logical Standby apply process to stop and to manually perform some compensating action. The second option is to take a preemptive action and to skip the unsupported PL/SQL either by using Logical Standby skip procedures. Each of these options is discussed in the following sections.

#### C.9.3.4 Manually Compensating for Unsupported PL/SQL

When Logical Standby encounters something that is unsupported, it stops the apply process and records an error in the `DBA_LOGSTDBY_EVENTS` table. You can query this table to determine what action caused the standby to stop and what action, if any, needs to be taken to compensate.

The following example shows a sample of what this query and its output might look like:

```
select status, event from dba_logstdby_events
          where commit_scn >= (select applied_scn from dba_logstdby_progress) and
          status_code = 16265
          order by commit_scn desc;
 
STATUS
--------------------------------------------------------------------------------
EVENT
--------------------------------------------------------------------------------
ORA-16265: Unsupported PL/SQL procedure encountered
begin
 "XDB"."DBMS_XMLSCHEMA"."REGISTERSCHEMA" (
   "SCHEMAURL" => 'xmlplsqlsch2
 
ORA-16265: Unsupported PL/SQL procedure encountered
begin
 "XDB"."DBMS_XMLSCHEMA"."REGISTERSCHEMA" (
   "SCHEMAURL" => 'xmlplsqlsch2
 
 
2 rows selected.
```

Two rows with the same information are returned because Logical Standby automatically retries the failed transaction. The results show that the standby was stopped when a call to `DBMS_XMLSCHEMA.REGISTERSCHEMA` was encountered for the `xmlplsqlsch2` schema. You can use this information to transfer any needed files from the primary and register the schema on the standby.

Once the schema has been successfully registered on the standby, the apply process on the Logical Standby can be restarted. This must be performed using the `SKIP FAILED TRANSACTION` option, for example:

```
alter database start logical standby apply skip failed transaction'
```

Logical Standby skips past the offending transaction and continues applying redo from the primary.

The general procedure for manually replicating unsupported PL/SQL follows these steps:

1. Some unsupported PL/SQL is executed on the primary database.
2. The standby database encounters the unsupported PL/SQL and stops Apply.
3. You examine the `DBA_LOGSTDBY_EVENTS` table to determine what caused Apply to stop.
4. You execute some compensating actions on the standby for the unsupported PL/SQL.
5. You restart apply on the standby.

#### C.9.3.5 Proactively Compensating for Unsupported PL/SQL

In certain cases, you know that an action you are going to perform on the primary database will cause the standby to halt. In those cases, you may want to take action ahead of time to either minimize or eliminate the time that the standby is not applying redo.

For example, suppose you know that a new application is going to be installed. Part of the installation requires a large number of XML schemas to be registered. You can register these schemas on the standby before they are registered on the primary. You can also install a skip procedure on the standby for the `DBMS_XMLSCHEMA.REGISTERSCHEMA` procedure which will check to see if the XML schema is registered and if so, it will tell Logical Standby to skip that PL/SQL call.

This approach can also be used for some of the other PL/SQL procedures that are unsupported. For example, `DBMS_XMLSCHEMA.DELETESCHEMA` can be handled in a similar way. A skip procedure can be written to see if the schema is installed on the standby and if it is not, then that PL/SQL can be safely skipped because it would not have had any meaningful affect on the standby.

#### C.9.3.6 Compensating for Ordering Sensitive Unsupported PL/SQL

Although the previous approach is useful, it cannot be used in all cases. It can only be safely used when the time that the PL/SQL is executed relative to other transactions is not critical. One case that this should not be used for is that of `DBMS_XMLSCHEMA.copyEvolve`.

This procedure evolves, or changes, a schema and can modify tables by adding and or removing columns and it can also change whether or not XML documents are valid. The timing of when this procedure should be executed on the Logical Standby is critical. The only time guaranteed to be safe is when apply has stopped on the Logical Standby when it sees that this procedure was executed on the primary database.

Before evolving a schema, it is also important to quiesce any traffic on the primary that may be using the schema. Otherwise, a transaction that is executed close in time to the evolveSchema on the primary may be executed in a different order on the Logical Standby because the dependency between the two transactions is not apparent to the Logical Standby. Therefore, when ordering sensitive PL/SQL is involved, you should follow these steps:

1. Quiesce changes to dependent tables on the primary.
2. Execute the CopyEvolve on the primary.
3. Wait for the standby to stop on the CopyEvolve PL/SQL.
4. Apply the compensating CopyEvolve on the standby.
5. Restart apply on the standby.

Example C-1 shows a sample of the procedures that could be used to determine how to handle RegisterSchema calls.

Example C-1 PL/SQL Skip Procedure for RegisterSchema

```
-- Procedures to determine how to handle registerSchema calls
 
-- This procedure extracts the schema URL, or name, from the statement
-- string that is passed into the skip procedure.
 
Create or replace procedure sec_mgr.parse_schema_str(
  statement             in varchar2,
  schema_name      out varchar2)
Is
  pos1 number;
  pos2 number;
  workingstr   varchar2(32767);
Begin
 
-- Find the correct argument
pos1 := instr(statement, '"SCHEMAURL" => ''');
workingstr := substr(statement, pos1 + 16);
 
-- Find the end of the schema name
pos1 := instr(workingstr, '''');
 
-- Get just the schema name
workingstr := substr(workingstr, 1, pos1 - 1);
 
schema_name := workingstr;
 
End parse_schema_str;
/
show errors
 
 
-- This procedure checks if a schema is already registered. If so,
-- it returns the value DBMS_LOGSTDBY.SKIP_ACTION_SKIP to indicate that
-- the PL/SQL should be skipped. Otherwise, the value 
-- DBMS_LOGSTDBY.SKIP_ACTION_SKIP is returned and Logical Standby apply 
-- will halt to allow the DBA to deal with the registerSchema call.
 
Create or replace procedure sec_mgr.skip_registerschema(
  statement             in varchar2,
  package_owner            in varchar2,
  package_name             in varchar2,
  procedure_name                 in varchar2,
  current_user                   in varchar2,
  xidusn                in number,
  xidslt                in number,
  xidsqn                in number, 
  exit_status            in number, 
  skip_action            out number)
Is
  schema_exists number;
  schemastr varchar2(2000);
Begin
 
  skip_action := DBMS_LOGSTDBY.SKIP_ACTION_SKIP;
 
  -- get the schame name from statement
  parse_schema_str(statement, schemastr);
 
  -- see if the schema is already registered
  select count(*) into schema_exists from sys.all_xml_schemas s 
                                     where s.schema_url = schemastr and
                                           s.owner = current_user;
 
  IF schema_exists = 0 THEN
      -- if the schema is not  registered, then we must stop apply
      skip_action := DBMS_LOGSTDBY.SKIP_ACTION_APPLY;     
  ELSE
      -- if the schema is already registered, then we can skip this statement
      skip_action := DBMS_LOGSTDBY.SKIP_ACTION_SKIP;     
  END IF;
 
End skip_registerschema;
/
show errors
 
-- Register the skip procedure to deal with the unsupported registerSchema 
-- PL/SQL.
Begin
   sys.dbms_logstdby.skip(stmt => 'PL/SQL', 
        schema_name => 'XDB', 
                                        object_name   => 'DBMS_XMLSCHEMA.REGISTERSCHEMA', 
                                        proc_name     => 'SEC_MGR.SKIP_REGISTERSCHEMA',
        use_like         => FALSE );
                  End;
    /
show errors
```

## C.10 Unsupported Tables

It is important to identify unsupported database objects on the primary database before you create a logical standby database because changes made to unsupported data types and tables on the primary database will be automatically skipped by SQL Apply on the logical standby database. Moreover, no error message will be returned.

There are three types of objects on a database, from the perspective of logical standby support:

- Objects that are explicitly maintained by SQL Apply
- Objects that are implicitly maintained by SQL Apply
- Objects that are not maintained by SQL Apply

Some schemas that ship with the Oracle database (for example, `SYSTEM`) contain objects that will be implicitly maintained by SQL Apply. However, if you put a user-defined table in `SYSTEM`, it will not be maintained even if it has columns of supported data types. To discover which objects are not maintained by SQL Apply, you must run two queries. The first query is as follows:

```
SQL> SELECT OWNER FROM DBA_LOGSTDBY_SKIP WHERE STATEMENT_OPT = 'INTERNAL SCHEMA';
```

This will return all schemas that are considered to be internal. User tables placed in these schemas will not be replicated on a logical standby database and will not show up in the `DBA_LOGSTDBY_UNSUPPORTED` view. Tables in these schemas that are created by Oracle will be maintained on a logical standby, if the feature implemented in the schema is supported in the context of logical standby.

The second query you must run is as follows. It returns tables that do not belong to internal schemas and will not be maintained by SQL Apply because of unsupported data types:

```
SQL> SELECT DISTINCT OWNER,TABLE_NAME FROM DBA_LOGSTDBY_UNSUPPORTED -
> ORDER BY OWNER,TABLE_NAME;

OWNER        TABLE_NAME
-----------  --------------------------
HR           COUNTRIES
OE           ORDERS
OE           CUSTOMERS
OE           WAREHOUSES
```

To view the column names and data types for one of the tables listed in the previous query, use a `SELECT` statement similar to the following:

```
SQL> SELECT COLUMN_NAME,DATA_TYPE FROM DBA_LOGSTDBY_UNSUPPORTED -
> WHERE OWNER='OE' AND TABLE_NAME = 'CUSTOMERS';

COLUMN_NAME                      DATA_TYPE
-------------------------------  -------------------
CUST_ADDRESS                     CUST_ADDRESS_TYP
PHONE_NUMBERS                    PHONE_LIST_TYP
CUST_GEO_LOCATION                SDO_GEOMETRY
```

If the primary database contains unsupported tables, SQL Apply automatically excludes these tables when applying redo data to the logical standby database.

Note:

If you determine that the critical tables in your primary database will not be supported on a logical standby database, then you might want to consider using a physical standby database. Physical standby databases do not have any such data type restrictions.

## C.11 Skipped SQL Statements on a Logical Standby Database

By default, the following SQL statements are automatically skipped by SQL Apply:

  
`ALTER DATABASE`  
`ALTER MATERIALIZED VIEW`  
`ALTER MATERIALIZED VIEW LOG`  
`ALTER SESSION`  
`ALTER SYSTEM`  
`CREATE CONTROL FILE`  
`CREATE DATABASE`  
`CREATE DATABASE LINK`  
`CREATE PFILE FROM SPFILE`  
`CREATE MATERIALIZED VIEW`  
`CREATE MATERIALIZED VIEW LOG`  
`CREATE SCHEMA AUTHORIZATION`  
`CREATE SPFILE FROM PFILE`  
`DROP DATABASE LINK`  
`DROP MATERIALIZED VIEW`  
`DROP MATERIALIZED VIEW LOG`  
`EXPLAIN`  
`LOCK TABLE`  
`SET CONSTRAINTS`  
`SET ROLE`  
`SET TRANSACTION`  

All other SQL statements executed on the primary database are applied to the logical standby database.

## C.12 DDL Statements Supported by a Logical Standby Database

Table C-1 lists the supported values for the `stmt` parameter of the `DBMS_LOGSTDBY.SKIP` procedure. The left column of the table lists the keywords that may be used to identify the set of SQL statements to the right of the keyword. In addition, any of the SQL statements listed in the `sys.audit_actions` table (shown in the right column of Table 1-13) are also valid values. Note that keywords are generally defined by database object.

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for complete information about the [`DBMS_LOGSTDBY`](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_lsbydb.htm#ARPLS363) package and [Section 10.5.3, "Setting up a Skip Handler for a DDL Statement"](manage_ls.md)

Table C-1 Values for stmt Parameter of the DBMS\_LOGSTDBY.SKIP procedure

| Keyword | Associated SQL Statements |
| --- | --- |
| There is no keyword for this group of SQL statements. | ``` GRANT REVOKE ANALYZE TABLE ANALYZE INDEX ANALYZE CLUSTER ``` |
| `CLUSTER` | ``` AUDIT CLUSTER CREATE CLUSTER DROP CLUSTER TRUNCATE CLUSTER ``` |
| `CONTEXT` | ``` CREATE CONTEXT DROP CONTEXT ``` |
| `DATABASE LINK` | ``` CREATE DATABASE LINK CREATE PUBLIC DATABASE LINK DROP DATABASE LINK DROP PUBLIC DATABASE LINK ``` |
| `DIMENSION` | ``` ALTER DIMENSION CREATE DIMENSION DROP DIMENSION ``` |
| `DIRECTORY` | ``` CREATE DIRECTORY DROP DIRECTORY ``` |
| `DML` | Includes DML statements on a table (for example: `INSERT`, `UPDATE`, and `DELETE`) |
| `INDEX` | ``` ALTER INDEX CREATE INDEX DROP INDEX ``` |
| `NON_SCHEMA_DDL` | All DDL that does not pertain to a particular schema  Note: `SCHEMA_NAME` and `OBJECT_NAME` must be null |
| `PROCEDURE` <sup>Foot 1</sup> | ``` ALTER FUNCTION ALTER PACKAGE ALTER PACKAGE BODY ALTER PROCEDURE CREATE FUNCTION CREATE LIBRARY CREATE PACKAGE CREATE PACKAGE BODY CREATE PROCEDURE DROP FUNCTION DROP LIBRARY DROP PACKAGE DROP PACKAGE BODY DROP PROCEDURE ``` |
| `PROFILE` | ``` ALTER PROFILE CREATE PROFILE DROP PROFILE ``` |
| `PUBLIC DATABASE LINK` | ``` CREATE PUBLIC DATABASE LINK DROP PUBLIC DATABASE LINK ``` |
| `PUBLIC SYNONYM` | ``` CREATE PUBLIC SYNONYM DROP PUBLIC SYNONYM ``` |
| `ROLE` | ``` ALTER ROLE CREATE ROLE DROP ROLE SET ROLE ``` |
| `ROLLBACK SEGMENT` | ``` ALTER ROLLBACK SEGMENT CREATE ROLLBACK SEGMENT DROP ROLLBACK SEGMENT ``` |
| `SCHEMA_DDL` | All DDL statements that create, modify, or drop schema objects (for example: tables, indexes, and columns)  Note: `SCHEMA_NAME` and `OBJECT_NAME` must not be null |
| `SEQUENCE` | ``` ALTER SEQUENCE CREATE SEQUENCE DROP SEQUENCE ``` |
| `SYNONYM` | ``` CREATE PUBLIC SYNONYM CREATE SYNONYM DROP PUBLIC SYNONYM DROP SYNONYM ``` |
| `SYSTEM AUDIT` | ``` AUDIT SQL_statements NOAUDIT SQL_statements ``` |
| `TABLE` | ``` CREATE TABLE ALTER TABLE DROP TABLE TRUNCATE TABLE ``` |
| `TABLESPACE` | ``` CREATE TABLESPACE DROP TABLESPACE ALTER TABLESPACE ``` |
| `TRIGGER` | ``` ALTER TRIGGER CREATE TRIGGER DISABLE ALL TRIGGERS DISABLE TRIGGER DROP TRIGGER ENABLE ALL TRIGGERS ENABLE TRIGGER ``` |
| `TYPE` | ``` ALTER TYPE ALTER TYPE BODY CREATE TYPE CREATE TYPE BODY DROP TYPE DROP TYPE BODY ``` |
| `USER` | ``` ALTER USER CREATE USER DROP USER ``` |
| `VIEW` | ``` CREATE VIEW DROP VIEW ``` |

<sup>Footnote 1</sup> Java schema objects (sources, classes, and resources) are considered the same as procedures for purposes of skipping (ignoring) SQL statements.

See Also:

The following sections that provide usage examples of the `SKIP` and `UNSKIP` options:
- [Section 10.5.2, "Using DBMS\_LOGSTDBY.SKIP to Prevent Changes to Specific Schema Objects"](manage_ls.md)
- [Section 10.5.3, "Setting up a Skip Handler for a DDL Statement"](manage_ls.md)
- [Section 10.5.4, "Modifying a Logical Standby Database"](manage_ls.md)
- [Section 10.5.5, "Adding or Re-Creating Tables On a Logical Standby Database"](manage_ls.md)

### C.12.1 DDL Statements that Use DBLINKS

SQL Apply may not correctly apply DDL statements such as the following, that reference a database link:

```
CREATE TABLE tablename AS SELECT * FROM bar@dblink
```

This is because the `dblink` at the logical standby database may not point to the same database as the primary database. If SQL Apply fails while executing such a DDL statement, you should use the `DBMS_LOGSTDBY.INSTANTIATE_TABLE` procedure for the table being created, and then restart SQL APPLY operations.

### C.12.2 Replication of AUD$ and FGA\_LOG$ on Logical Standbys

Auditing and fine-grained auditing are supported on logical standbys. Changes made to the `AUD$` and `FGA_AUD$` tables at the primary database are replicated at the logical standby.

Both the `AUD$` table and the `FGA_AUD$` table have a DBID column. If the DBID value is that of the primary database, then the row was replicated to the logical standby based on activities at the primary. If the DBID value is that of the logical standby database, then the row was inserted as a result of local activities at the logical standby.

After the logical standby database assumes the primary role as a result of a role transition (either a switchover or failover), the `AUD$` and `FGA_AUD$` tables at the new primary (originally the logical standby) and at the new logical standby (originally the primary) are not necessarily synchronized. Therefore, it is possible that not all rows in the `AUD$` or `FGA_AUD$` tables at the new primary database will be present in the new logical standby database. However, all rows in `AUD$` and `FGA_LOG$` that were inserted while the database was in a primary role are replicated and present in the logical standby database.

## C.13 Distributed transactions and XA Support

You can perform distributed transactions using either of the following methods:

- Modify tables in multiple databases in a coordinated manner using database links.
- Use the XA interface, as exposed by the `DBMS_XA` package in supplied PL/SQL packages or via OCI or JDBC libraries. The XA interface implements X/Open Distributed Transaction Processing (DTP) architecture.

Changes made to the primary database during a distributed transaction using either of these two methods are replicated to the logical standby database.

However, the distributed transaction state is not replicated. The logical standby database does not inherit the in-doubt or prepared state of such a transaction, and it does not replicate the changes using the same global transaction identifier used at the primary database for the XA transactions. As a result, if you fail over to a logical standby database before committing a distributed transaction, the changes are rolled back at the logical standby. This rollback occurs even if the distributed transaction on the primary database is in a prepared state and has successfully completed the first phase of the two-phased commit protocol. Switchover operations wait for all active distributed transactions to complete, and are not affected by this restriction.

XA transactions can be performed in two ways:

- tightly coupled, where different XA branches share locks
- loosely coupled, where different XA branches do not share locks

Replication of changes made by loosely coupled XA branches is supported regardless of the `COMPATIBLE` parameter value. Replication of changes made by tightly coupled branches on an Oracle RAC primary (introduced in 11g Release 1) is supported only with `COMPATIBLE=11.2` or higher.

## C.14 Support for SecureFiles LOBs

SecureFiles LOBs are supported when the database compatibility level is set to 11.2 or higher.

Transparent data encryption and data compression can be enabled on SecureFiles LOB columns at the primary database. De-duplication of SecureFiles LOB columns is not supported. Also, the following operations contained within the `DBMS_LOB` PL/SQL package are not supported on SecureFiles LOB columns:

`FRAGMENT_DELETE`, `FRAGMENT_INSERT`, `FRAGMENT_MOVE`, `FRAGMENT_REPLACE`, `COPY_FROM_DBFS_LINK`, `MOVE_TO_DBFS_LINK`, `SET_DBFS_LINK`, `COPY_DBFS_LINK`, `SETCONTENTTYPE`

If SQL Apply encounters redo generated by any of these operations, it stops with an `ORA-16211: Unsupported record found in the archived redo log` error. To continue, add a skip rule for the affected table using `DBMS_LOGSTDBY.SKIP` and restart SQL Apply.

## C.15 Character Set Considerations

Configurations are not supported in which the primary database and standby database have different character sets.