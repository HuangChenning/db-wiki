---
title: DBMS_CDC_PUBLISH
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_cdcpub.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 33 DBMS\_CDC\_PUBLISH

Note:

Oracle Change Data Capture will be de-supported in a future release of Oracle Database and will be replaced with Oracle GoldenGate. Therefore, Oracle strongly recommends that you use Oracle GoldenGate for new applications.

For Oracle Database 11g Release 2 (11.2), Change Data Capture continues to function as in earlier releases. If you are currently using Change Data Capture, then you will be able to continue to do so for the foreseeable future. However, Change Data Capture will not be further enhanced, and will only be supported based on the current, documented functionality.

The `DBMS_CDC_PUBLISH` package, one of a set of Change Data Capture packages, is used by a publisher to set up an Oracle Change Data Capture system to capture and publish change data from one or more Oracle relational source tables.

Change Data Capture captures and publishes only committed data. Oracle Change Data Capture identifies new data that has been added to, updated in, or removed from relational tables, and publishes the change data in a form that is usable by subscribers.

Typically, a Change Data Capture system has one publisher who captures and publishes changes for any number of Oracle relational source tables. The publisher then provides subscribers (applications or individuals) with access to the published data. Subscribers access the published data using the `DBMS_CDC_SUBSCRIBE` package.

See Also:

[Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/cdc.htm#DWHSG016) for information regarding Oracle Change Data Capture

This chapter contains the following topics:

- Using DBMS\_CDC\_PUBLISH
	- Overview
		- Deprecated Subprograms
		- Security Model
		- Views
- Summary of DBMS\_CDC\_PUBLISH Subprograms

---

## Using DBMS\_CDC\_PUBLISH

This section contains the following topics, which relate to using the `DBMS_CDC_PUBLISH` package:

---

### Overview

Through the `DBMS_CDC_PUBLISH` package, the publisher creates and maintains change sources, change sets, and change tables, and eventually drops them when they are no longer useful.

The publisher, typically a database administrator, is concerned primarily with the source of the data and with creating the schema objects that describe the structure of the capture system: change sources, change sets, and change tables.

Most Change Data Capture systems have one publisher and many subscribers. The publisher accomplishes the following main objectives:

1. Determines which source table changes need to be published.
2. Decides whether to capture changes asynchronously or synchronously.
3. Uses the subprograms in the `DBMS_CDC_PUBLISH` package to capture change data from the source tables and make it available by creating and administering the change source, change set, and change table objects.
4. Allows controlled access to subscribers by using the SQL `GRANT` and `REVOKE` statements to grant and revoke the `SELECT` privilege on change tables for users and roles. (This is necessary to allow the subscribers to subscribe to the change data using the `DBMS_CDC_SUBSCRIBE` package.)

---

### Deprecated Subprograms

Note:

Oracle recommends that you do not use deprecated procedures in new applications. Support for deprecated features is for backward compatibility only.

The following subprograms are deprecated with Oracle Database 11g:

- `DBMS_CDC_PUBLISH.DROP_SUBSCRIPTION` with a subscription handle
	When dropping a subscription, the publisher should now specify the name of the subscription to be dropped, not the subscription handle.
- `DBMS_CDC_PUBLISH.DROP_SUBSCRIBER_VIEW`
	Dropping a subscriber view is now performed automatically by Change Data Capture.

---

### Security Model

You must have the `EXECUTE_CATALOG_ROLE` role to use the `DBMS_CDC_PUBLISH` package. Additional privileges and roles are required depending on the publishing mode and whether the publisher is on the source or staging database. See the section on Granting Privileges and Roles to the Publisher in [Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/cdc.htm#DWHSG016) for details.

---

### Views

The `DBMS_CDC_PUBLISH` package uses the views listed in the section on Getting Information About the Change Data Capture Environment in [Oracle Database Data Warehousing Guide.](https://docs.oracle.com/cd/E11882_01/server.112/e25554/cdc.htm#DWHSG016)

---

## Summary of DBMS\_CDC\_PUBLISH Subprograms

Table 33-1 describes the subprograms in the `DBMS_CDC_PUBLISH` supplied package and the mode or modes with which each can be used. A value of All in the Mode column indicates that the subprogram can be used with synchronous and all modes of asynchronous Change Data Capture, a value of Asynchronous in the Mode column indicates that the subprogram can be used with all modes of asynchronous Change Data Capture (HotLog, Distributed HotLog, and AutoLog).

Table 33-1 DBMS\_CDC\_PUBLISH Package Subprograms

| Subprogram | Mode | Description |
| --- | --- | --- |
| ALTER\_AUTOLOG\_CHANGE\_SOURCE Procedure | Asynchronous AutoLog | Changes one or more properties of an existing AutoLog change source |
| ALTER\_CHANGE\_SET Procedure | All | Changes one or more of the properties of an existing change set |
| ALTER\_CHANGE\_TABLE Procedure | All | Adds or drops columns for an existing change table, or changes the properties of an existing change table |
| ALTER\_HOTLOG\_CHANGE\_SOURCE Procedure | Asynchronous Distributed HotLog | Changes one or more properties of an existing Distributed HotLog change source |
| CREATE\_AUTOLOG\_CHANGE\_SOURCE Procedure | Asynchronous AutoLog | Creates an AutoLog change source |
| CREATE\_CHANGE\_SET Procedure | All | Creates a change set |
| CREATE\_CHANGE\_TABLE Procedure | All | Creates a change table in a specified schema |
| CREATE\_HOTLOG\_CHANGE\_SOURCE Procedure | Asynchronous Distributed HotLog | Creates a Distributed HotLog change source |
| DROP\_CHANGE\_SET Procedure | All | Drops an existing change set |
| DROP\_CHANGE\_SOURCE Procedure | Asynchronous Autolog and Asynchronous Distributed Hotlog | Drops an existing AutoLog or Distributed HotLog change source |
| DROP\_CHANGE\_TABLE Procedure | All | Drops an existing change table |
| DROP\_SUBSCRIPTION Procedure | All | Allows a publisher to drop a subscription that was created by a subscriber |
| GET\_DDLOPER Function | All | Converts a binary integer into a user friendly string that describes the DDL operation that actually took place |
| PURGE Procedure | All | Removes unneeded rows from all change tables in the staging database |
| PURGE\_CHANGE\_SET Procedure | All | Removes unneeded rows from all change tables in a specified change set |
| PURGE\_CHANGE\_TABLE Procedure | All | Removes unneeded rows from a specified change table |

---

### ALTER\_AUTOLOG\_CHANGE\_SOURCE Procedure

This procedure changes the properties of an existing AutoLog change source.

Syntax

```
DBMS_CDC_PUBLISH.ALTER_AUTOLOG_CHANGE_SOURCE(
     change_source_name  IN VARCHAR2,
     description         IN VARCHAR2 DEFAULT NULL,
     remove_description  IN CHAR DEFAULT 'N',
     first_scn           IN NUMBER DEFAULT NULL);
```

Parameters

Table 33-2 ALTER\_AUTOLOG\_CHANGE\_SOURCE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `change_source_name` | Name of an existing AutoLog change source. Change source names follow Oracle schema object naming rules. |
| `description` | New description of the change source. The description must be specified using 255 or fewer characters. |
| `remove_description` | A value of `'Y'` or `'N'.`  If the value is `'Y',` then the current description is changed to `NULL`. If the value is `'N'`, then the current description is unchanged.  Do not specify the description parameter with this parameter. |
| `first_scn` | New first SCN. |

Exceptions

Table 33-3 ALTER\_AUTOLOG\_CHANGE\_SOURCE Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-31401` | Specified change source is not an existing change source |
| `ORA-31445` | Invalid lock handle while acquiring lock on string |
| `ORA-31452` | Invalid value for parameter, expecting: `Y` or `N` |
| `ORA-31497` | Invalid value specified for `first_scn` |
| `ORA-31498` | The `description` and `remove_description` parameters cannot both be specified |
| `ORA-31499` | Null value specified for required parameter |
| `ORA-31501` | Specified change source is not an AutoLog change source |
| `ORA-31504` | Cannot alter or drop predefined change source |
| `ORA-31507` | Specified parameter value longer than maximum length |

Usage Notes

- Properties supplied to this procedure with a `NULL` value are unchanged.
- This procedure can be used to change more than one property at a time.
- This procedure can be used in making SCN adjustments after determining which redo logs are no longer needed for an asynchronous AutoLog change set.

See Also:

The section on asynchronous Change Data Capture and redo log files in [Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/cdc.htm#DWHSG016) for information on how the publisher can use the `ALTER_AUTOLOG_CHANGE_SOURCE` procedure in making SCN adjustments after determining which redo logs are no longer needed for an asynchronous AutoLog change set.

---

### ALTER\_CHANGE\_SET Procedure

This procedure changes the properties of an existing change set that was created with the `CREATE_CHANGE_SET` procedure.

Syntax

```
DBMS_CDC_PUBLISH.ALTER_CHANGE_SET(
     change_set_name         IN VARCHAR2,
     description             IN VARCHAR2 DEFAULT NULL,
     remove_description      IN CHAR DEFAULT 'N',
     enable_capture          IN CHAR DEFAULT NULL,
     recover_after_error     IN CHAR DEFAULT NULL,
     remove_ddl              IN CHAR DEFAULT NULL,
     stop_on_ddl             IN CHAR DEFAULT NULL);
```

Parameters

Table 33-4 ALTER\_CHANGE\_SET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `change_set_name` | Name of an existing change set. Change set names follow the Oracle schema object naming rules. |
| `description` | New description of the change set. Specify using 255 or fewer characters. |
| `remove_description` | A value of `'Y'` or `'N'`.  If the value is `'Y'`, then the current description is changed to `NULL`. If the value is `'N'`, then the current description is unchanged.  Do not specify the `description` parameter with this parameter. |
| `enable_capture` | A value of `'Y'` or `'N'`.  If the value is `'Y'`, then change data capture is enabled for this change set.  If the value is `'N'`, then change data capture is disabled for this change set.  Synchronous change sets are created with change data capture enabled.  Asynchronous change sets are created with change data capture disabled. |
| `recover_after_error` | A value of `'Y'` or `'N'`.  If the value is `'Y'`, then Change Data Capture will attempt to recover from earlier capture errors.  If the value is `'N'`, then Change Data Capture will not attempt to recover from earlier capture errors. |
| `remove_ddl` | A value of `'Y'` or `'N'.`  If the value is `'Y'` and the value of the `recover_after_error` parameter is `'Y'`, then any DDL records that may have caused capture errors will be filtered out during recovery.  If the value is `'N'`, then DDL records that may have caused capture errors will not be filtered out during recovery.  This parameter has meaning only when the `recover_after_error` parameter is specified with a value of `'Y'`. |
| `stop_on_ddl` | A value of `'Y'` or `'N'`.  If the value is `'Y',` then Change Data Capture stops when a DDL event is detected.  If the value is `'N',` then Change Data Capture continues when a DDL event is detected.  See the Usage Notes for additional information about this parameter. |

Exceptions

Table 33-5 ALTER\_CHANGE\_SET Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-31410` | Specified change set is not an existing change set |
| `ORA-31452` | Invalid value for parameter, expecting: `Y` or `N` |
| `ORA-31445` | Invalid lock handle while acquiring lock on string |
| `ORA-31468` | Cannot process DDL change record |
| `ORA-31469` | Cannot enable Change Data Capture for change set |
| `ORA-31485` | Invalid database link |
| `ORA-31498` | The `description` and `remove_description` parameters cannot both be specified |
| `ORA-31499` | Null value specified for required parameter |
| `ORA-31505` | Cannot alter or drop predefined change set |
| `ORA-31507` | Specified parameter value longer than maximum length |
| `ORA-31508` | Invalid parameter value for synchronous change set |
| `ORA-31514` | Change set disabled due to capture error |

Usage Notes

- The publisher can use this procedure for asynchronous and synchronous Change Data Capture. However, the predefined synchronous change set, `SYNC_SET`, cannot be altered, and the following parameters cannot be altered for publisher-defined synchronous change sets: `enable_capture`, `recover_after_error`, `remove_ddl`, and `stop_on_ddl`.
- Properties supplied to this procedure with a `NULL` value are unchanged.
- This procedure can alter more than one parameter at a time.
- Enabling or disabling an asynchronous HotLog or AutoLog change set starts or stops the Oracle Streams capture process and apply process underlying the change set. Enabling or disabling an asynchronous Distributed HotLog change set starts or stops the Oracle Streams apply process underlying the change set.
- The effect of the `stop_on_ddl` parameter is as follows:
	- When the `stop_on_ddl` parameter is set to `'Y'`, asynchronous Change Data Capture stops if DDL is encountered during change data capture. Some DDL statements can adversely affect capture, such as a statement that drops a source table column that is being captured. The publisher has an opportunity to analyze and adjust to DDL changes that may adversely affect change tables while capture is stopped, thereby preventing possible errors during capture.
		Because these statements do not affect the column data itself, Change Data Capture does not stop capturing change data when the `stop_on_ddl` parameter is set to `'Y'` and any of the following statements is encountered:
		- `ANALYZE TABLE`
				- `LOCK TABLE`
				- `GRANT` privileges to access a table
				- `REVOKE` privileges to access a table
				- `COMMENT` on a table
				- `COMMENT` on a column
		These statements can be issued on the source database without concern for their impact on Change Data Capture processing.
		- When the `stop_on_ddl` parameter is set to `'N'`, Change Data Capture does not stop if DDL is encountered during change data capture. If a change set does not stop on DDL, but a DDL change occurs that affects change tables, that change can result in a capture error. There are also system conditions that can cause capture errors, such as being out of disk space.
		See Also:
		[Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/toc.htm) for information on the effects of, and how to recover from, a capture error
	Whenever a DDL statement causes processing to stop, a message is written to the alert log indicating for which change set processing has been stopped and the DDL statement that caused it to be stopped. Similarly, whenever DDL statements are ignored by Change Data Capture and processing continues, a message is written to the alert log indicating which DDL statement was ignored.
- The publisher can attempt to recover an asynchronous change set after a capture error by specifying `'Y'` for the `recover_after_error` parameter. Capture errors can occur when any of the following is true:
	- The `stop_on_ddl` parameter is set to `'Y'` and there is a DDL record in the change data. In this case, to recover from the error, the publisher must also specify `'Y'` for the `remove_ddl` parameter.
		- The `stop_on_ddl` parameter is set to `'N'` and there is a DDL record that affects capture. For example, if the publisher drops and re-creates a change table, it causes an error the next time that Change Data Capture attempts to add change data to the named change table.
		- A miscellaneous error occurs, such as running out of disk space, or a redo log file error (such as ORA-01688: unable to extend table string.string partition string by string in tablespace string).
		See Also:
		[Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/cdc.htm#DWHSG016) for more information on how to recover from a capture error.

---

### ALTER\_CHANGE\_TABLE Procedure

This procedure adds columns to, or drops columns from, or changes the properties of, a change table that was created with the `CREATE_CHANGE_TABLE` procedure.

Syntax

```
DBMS_CDC_PUBLISH.ALTER_CHANGE_TABLE(
     owner                  IN VARCHAR2,
     change_table_name      IN VARCHAR2,
     operation              IN VARCHAR2,
     column_list            IN VARCHAR2,
     rs_id                  IN CHAR,
     row_id                 IN CHAR,
     user_id                IN CHAR,
     timestamp              IN CHAR,
     object_id              IN CHAR,
     source_colmap          IN CHAR,
     target_colmap          IN CHAR,
     ddl_markers            IN CHAR  DEFAULT NULL);
```

Parameters

Table 33-6 ALTER\_CHANGE\_TABLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `owner` | The schema that owns the change table. |
| `change_table_name` | The change table that is being altered. Change table names follow the Oracle schema object naming rules. |
| `operation` | Either the value `ADD` or `DROP` to indicate whether to add or drop the user columns specified with the `column_list` parameter and any control columns specified by other parameters. |
| `column_list` | User column names and datatypes for each column of the source table that should be added to, or dropped from, the change table. The list is comma-delimited. |
| `rs_id`  `row_id`  `user_id`  `timestamp`  `object_id`  `source_colmap`  `target_colmap`  `ddl_markers` | Each listed parameter specifies a particular control column, as follows:  - The `rs_id` parameter specifies the `RSID$` control column. - The `row_id` parameter specifies the `ROW_ID$` control column. - The `user_id` parameter specifies the `USERNAME$` control column. - The `timestamp` parameter specifies the `TIMESTAMP$` control column. - The `object_id` parameter specifies the `SYS_NC_OID$` control column. - The `source_colmap` parameter specifies the `SOURCE_COLMAP$` control column. - The `target_colmap` parameter specifies the `TARGET_COLMAP$` control column. - The `ddl_markers` parameter tracks all DDL operations on the source table and stores information about those operations in the change table. These are the three additional control columns you get when `ddl_markers` is enabled. There are three values: `DDLOPER$` is a bit vector that indicates what kind of DDL operation happened. (Use the procedure `DBMS_CDC_PUBLISH.GET_DDLOPER(ddloper$)` to get the name of the DDL operation.) `DDLDESC$` is a CLOB containing the actual DDL statement executed. `DDLPDOBJN$` is not used in this release.  Each parameter must have a value of either `'Y'` or `'N'`, where:  - `'Y'`: Adds the specified control column to, or drops it from the change table, as indicated by the `operation` parameter. - `'N'`: Neither adds the specified control column, nor drops it from the change table. |

See Also:

[Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/cdc.htm#DWHSG016) for a complete description of control columns.

Exceptions

Table 33-7 ALTER\_CHANGE\_TABLE Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-31403` | Specified change table already contains the specified column |
| `ORA-31409` | One or more values for input parameters are incorrect |
| `ORA-31415` | Specified change set does not exist |
| `ORA-31416` | Invalid `SOURCE_COLMAP` value |
| `ORA-31417` | Column list contains control column control-column-name |
| `ORA-31421` | Change table does not exist |
| `ORA-31422` | Specified owner schema does not exist |
| `ORA-31423` | Specified change table does not contain the specified column |
| `ORA-31454` | Invalid value specified for operation parameter, expecting `ADD` or `DROP` |
| `ORA-31455` | Nothing to alter |
| `ORA-31456` | Error executing a procedure in the `DBMS_CDC_UTILITY` package |
| `ORA-31459` | System triggers for `DBMS_CDC_PUBLISH` package are not installed |
| `ORA-31471` | Invalid `OBJECT_ID` value |

Usage Notes

- The publisher can use this procedure for asynchronous and synchronous Change Data Capture.
- The publisher cannot add and drop user columns in the same call to the `ALTER_CHANGE_TABLE` procedure; these schema changes require separate calls.
- The publisher must not specify the name of the control columns in the `column_ list` parameter.
- When altering an asynchronous change table, the publisher must accept the default value or specify ' `N` ' for the `source_colmap` and `object_id` parameters. In addition, for the asynchronous Distributed HotLog mode, the publisher also must accept the default value or specify ' `N` ' for the `row_id` and `username` parameters when the change source is 9.2 or 10.1.
	See Also:
	[Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/cdc.htm#DWHSG016) for information about the impact on subscriptions when a publisher adds a column to a change table.

---

### ALTER\_HOTLOG\_CHANGE\_SOURCE Procedure

This procedure changes the properties of an existing Distributed HotLog change source.

Syntax

```
DBMS_CDC_PUBLISH.ALTER_HOTLOG_CHANGE_SOURCE(
     change_source_name  IN VARCHAR2,
     description         IN VARCHAR2 DEFAULT NULL,
     remove_description  IN CHAR DEFAULT 'N',
     enable_source       IN CHAR DEFAULT NULL);
```

Parameters

Table 33-8 ALTER\_HOTLOG\_CHANGE\_SOURCE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `change_source_name` | Name of an existing Distributed HotLog change source. Change source names follow Oracle schema object naming rules. |
| `description` | New description of the change source. The description must be specified using 255 or fewer characters. |
| `remove_description` | A value of `'Y'` or `'N'`.  If the value is `'Y'`, then the current description is changed to `NULL`. If the value is `'N'`, then the current description is unchanged.  Do not specify the description parameter with this parameter. |
| `enable_source` | A value of `'Y'` or `'N'`.  If the value is `'Y',` then the change source is enabled. If the value is `'N'`, then the change source is disabled. |

Exceptions

Table 33-9 ALTER\_HOTLOG\_CHANGE\_SOURCE Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-` `31401` | Change source is not an existing change source |
| `ORA-31455` | Nothing to `ALTER` |
| `ORA-31480` | Staging database and source database cannot be the same |
| `ORA-31481` | Change source is not a HotLog change source |
| `ORA-31482` | Invalid option for non-distributed HotLog change source |
| `ORA-31484` | Source database must be at least 9.2.0.6 or greater |
| `ORA-31485` | Invalid database link |
| `ORA-31498` | The `description` and `remove_description` parameters cannot both be specified |
| `ORA-31499` | Null value specified for required parameter |
| `ORA-31504` | Cannot alter or drop predefined change source |
| `ORA-31507` | Parameter value longer than maximum length |
| `ORA-31532` | Cannot enable change source |
| `ORA-31534` | Change Data Capture publisher is missing DBA role |

Usage Notes

- Properties supplied to this procedure with a `NULL` value are unchanged.
- This procedure can be used to change more than one property at a time.
- Enabling or disabling a Distributed HotLog change source starts or stops the Oracle Streams capture process that underlies the change source.
- This procedure cannot be used to alter the change source for the asynchronous HotLog mode of Change Database Capture. The change source for the asynchronous HotLog mode is the predefined change source, HOTLOG\_SOURCE, which cannot be altered.

---

### CREATE\_AUTOLOG\_CHANGE\_SOURCE Procedure

This procedure creates an AutoLog change source. An AutoLog change source is based on of a set of redo log files automatically copied by redo transport services to the system on which the staging database resides.

Syntax

```
DBMS_CDC_PUBLISH.CREATE_AUTOLOG_CHANGE_SOURCE(
     change_source_name  IN VARCHAR2,
     description         IN VARCHAR2 DEFAULT NULL,
     source_database     IN VARCHAR2,
     first_scn           IN NUMBER,
     online_log          IN CHAR DEFAULT 'N');
```

Parameters

Table 33-10 CREATE\_AUTOLOG\_CHANGE\_SOURCE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `change_source_name` | Name of the change source. Change source names follow the Oracle schema object naming rules. |
| `description` | Description of the change source. Specify using 255 or fewer characters. |
| `source_database` | Global name of the change source's source database instance. |
| `first_scn` | The SCN of the start of a LogMiner dictionary that is in the change source's archived redo log files. |
| `online_log` | A value of `'Y'` or `'N'` If the value is `'Y'`, then the change source uses the AutoLog online option to hot-mine the source database online redo log to gather change data. There can only be one change source with `online_log='Y'` on a given staging database.  If the value is `'N'`, then the change source uses the AutoLog archive option to get change data from archived redo log files. There can be one or more change sources with `online_log='N'` on a given staging database. |

Exceptions

Table 33-11 CREATE\_AUTOLOG\_CHANGE\_SOURCE Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-31436` | Duplicate change source specified |
| `ORA-31497` | Invalid value specified for `first_scn` |
| `ORA-31499` | Null value specified for required parameter |
| `ORA-31507` | Specified parameter value is longer than the maximum length |
| `ORA-31508` | Invalid parameter value for synchronous change set |
| `ORA-31535` | Cannot support change source in this configuration |

Usage Notes

- The publisher can use this procedure for asynchronous Change Data Capture only.
- The publisher must take care when specifying a value for the `source_database` parameter. Change Data Capture does not validate this value when creating the change source. The publisher can query the `GLOBAL_NAME` column in the `GLOBAL_NAME` view at the source database for the `source_database` parameter value.
- The publisher must configure redo transport services to automatically copy the log files to the system on which the staging database resides.
	See Also:
	The section on performing asynchronous AutoLog publishing in [Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/cdc.htm#DWHSG016) for information on configuring redo transport services to automatically copy the log files to the system on which the staging database resides.
- An AutoLog change source must begin with an archived redo log file that contains a LogMiner dictionary. The `CREATE_AUTOLOG_CHANGE_SOURCE` `first_scn` parameter indicates the SCN for this dictionary extraction and is the point at which the change source can begin capturing changes. The publisher can determine the value for the `first_scn` parameter using either of the following methods:
	- Direct `DBMS_CAPTURE_ADM.BUILD` to return the value when the dictionary is built:
		```
		SET SERVEROUTPUT ON
		VARIABLE FSCN NUMBER;
		BEGIN
		 :FSCN := 0;
		 DBMS_CAPTURE_ADM.BUILD(:FSCN);
		 DBMS_OUTPUT.PUT_LINE('The first_scn value is ' || :FSCN);
		END;
		/
		The first_scn value is 207722
		```
		- Make the following query on the source database. If this query returns multiple distinct values for `first_change#`, then the data dictionary has been extracted more than once and the publisher should choose the `first_change#` value that is the most appropriate to the change source.
		```
		SELECT DISTINCT FIRST_CHANGE#, NAME 
		   FROM V$ARCHIVED_LOG
		   WHERE DICTIONARY_BEGIN = 'YES';
		```
		See Also:
		The section on performing asynchronous AutoLog publishing in [Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/cdc.htm#DWHSG016) for information on archived redo log files and the LogMiner dictionary.
- For the asynchronous mode of Change Data Capture, the amount of change data captured is dependent on the level of supplemental logging enabled at the source database.
	See Also:
	[Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/cdc.htm#DWHSG016) for information about supplemental logging.

---

### CREATE\_CHANGE\_SET Procedure

This procedure allows the publisher to create a change set. For asynchronous HotLog and AutoLog Change Data Capture, the publisher can optionally provide beginning and ending date values at which to begin and end change data capture.

Syntax

```
DBMS_CDC_PUBLISH.CREATE_CHANGE_SET(
     change_set_name        IN VARCHAR2,
     description            IN VARCHAR2 DEFAULT NULL,
     change_source_name     IN VARCHAR2,
     stop_on_ddl            IN CHAR DEFAULT 'N',
     begin_date             IN DATE DEFAULT NULL,
     end_date               IN DATE DEFAULT NULL);
```

Parameters

Table 33-12 CREATE\_CHANGE\_SET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `change_set_name` | Name of the change set. Change set names follow the Oracle schema object naming rules. |
| `description` | Description of the change set. Specify using 255 or fewer characters. |
| `change_source_name` | Name of the existing change source to contain this change set. |
| `stop_on_ddl` | A value of `'Y'` or `'N'`.  If the value is `'Y'`, then Change Data Capture stops when a DDL event is detected.  If the value is `'N'`, then Change Data Capture continues when a DDL event is detected.  See the Usage Notes for additional information about this parameter. |
| `begin_date` | Date on which the publisher wants the change set to begin capturing changes. A value for this parameter is valid for the asynchronous HotLog and AutoLog modes of Change Data Capture only. |
| `end_date` | Date on which the publisher wants the change set to stop capturing changes. A value for this parameter is valid for the asynchronous HotLog and AutoLog modes of Change Data Capture only. |

Exceptions

Table 33-13 CREATE\_CHANGE\_SET Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-31401` | Specified change source is not an existing change source |
| `ORA-31407` | The `end_date` must be greater than the `begin_date` |
| `ORA-31408` | Invalid value specified for begin\_scn or end\_scn |
| `ORA-31437` | Duplicate change set specified |
| `ORA-31452` | Invalid value for parameter, expecting: `Y` or `N` |
| `ORA-31483` | Cannot have spaces in the parameter |
| `ORA-31485` | Invalid database link |
| `ORA-31487` | Cannot support begin dates or end dates in this configuration |
| `ORA-31488` | Cannot support change set in this configuration |
| `ORA-31499` | Null value specified for required parameter |
| `ORA-31503` | Invalid date supplied for `begin_date` or `end_date` |
| `ORA-31507` | Specified parameter value longer than maximum length |
| `ORA-31508` | Invalid parameter value for synchronous change set |

Usage Notes

- The publisher can use this procedure for asynchronous and synchronous Change Data Capture. However, the default values for the following parameters are the only supported values for synchronous change sets: `begin_date`, `end_date`, and `stop_on_ddl`. The default values for the following parameters are the only supported values for asynchronous Distributed HotLog change sets: `begin_date` and `end_date`.
- When the change source is Distributed HotLog on a release of Oracle Database earlier than 10.2, Change Data Capture inserts rows into the `CHANGE_PROPAGATION` and `CHANGE_PROPAGATION_SETS` views on the staging database.
- An AutoLog online change source (created with `online_log='Y'`) can only contain one change set.
- The `begin_date` and `end_date` parameters are optional. The publisher can specify neither of them, one of them, or both. The effect of these parameters is as follows:
	- When a `begin_date` is specified, changes from transactions that begin on or after that date are captured.
		- When a `begin_date` is not specified, capture starts with the earliest available change data.
		- When an `end_date` is specified, changes from transactions that are committed on or before that date are captured.
		- When an `end_date` is not specified, Change Data Capture continues indefinitely.
- The effect of the `stop_on_ddl` parameter is as follows:
	- When the `stop_on_ddl` parameter is set to `'Y'`, asynchronous Change Data Capture stops if DDL is encountered during change data capture. Some DDL statements can adversely affect capture, such as a statement that drops a source table column that is being captured. The publisher has an opportunity to analyze and adjust to DDL changes that may adversely affect change tables while capture is stopped, thereby preventing possible errors during capture.
		Because these statements do not affect the column data itself, Change Data Capture does not stop capturing change data when the `stop_on_ddl` parameter is set to `'Y'` and any of the following statements is encountered:
		- `ANALYZE TABLE`
				- `LOCK TABLE`
				- `GRANT` privileges to access a table
				- `REVOKE` privileges to access a table
				- `COMMENT` on a table
				- `COMMENT` on a column
		These statements can be issued on the source database without concern for their impact on Change Data Capture processing.
		- When the `stop_on_ddl` parameter is set to `'N'`, Change Data Capture does not stop if DDL is encountered during change data capture. If a change set does not stop on DDL, but a DDL change occurs that affects capture, that change can result in a capture error.
		See Also:
		[Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/cdc.htm#DWHSG016) for information on the effects of, and how to recover from, a capture error.
	Whenever a DDL statement causes processing to stop, a message is written to the alert log indicating for which change set processing has been terminated and the DDL statement that caused it to be terminated. Similarly, whenever DDL statements are ignored by Change Data Capture and processing continues, a message is written to the alert log indicating which DDL statement was ignored.

---

### CREATE\_CHANGE\_TABLE Procedure

This procedure creates a change table in a specified schema.

Note:

Oracle recommends that the publisher be certain that the source table that will be referenced in a `CREATE_CHANGE_TABLE` procedure has been created prior to calling this procedure, particularly if the change set that will be specified in the procedure has the `stop_on_ddl` parameter set to `'Y'`.

Syntax

```
DBMS_CDC_PUBLISH.CREATE_CHANGE_TABLE(
     owner                  IN VARCHAR2,
     change_table_name      IN VARCHAR2,
     change_set_name        IN VARCHAR2,
     source_schema          IN VARCHAR2,
     source_table           IN VARCHAR2,
     column_type_list       IN VARCHAR2,
     capture_values         IN VARCHAR2,
     rs_id                  IN CHAR,
     row_id                 IN CHAR,
     user_id                IN CHAR,
     timestamp              IN CHAR,
     object_id              IN CHAR,
     source_colmap          IN CHAR,
     target_colmap          IN CHAR,
     options_string         IN VARCHAR2,
     ddl_markers            IN CHAR  DEFAULT 'Y');
```

Parameters

Table 33-14 CREATE\_CHANGE\_TABLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `owner` | Name of the schema that owns the change table. |
| `change_table_name` | Name of the change table that is being created. Change table names follow the Oracle schema object naming rules. |
| `change_set_name` | Name of the change set in which this change table resides. |
| `source_schema` | The schema where the source table is located. |
| `source_table` | The source table from which the change records are captured. |
| `column_type_list` | The user columns and datatypes that are being tracked. Specify using a comma-delimited list. |
| `capture_values` | One of the following capture values for update operations:  - `OLD`: Captures the original values from the source table. - `NEW`: Captures the changed values from the source table. - `BOTH`: Captures the original and changed values from the source table. |
| `rs_id`  `row_id`  `user_id`  `timestamp`  `object_id`  `source_colmap`  `target_colmap`  `ddl_markers` | Each listed parameter specifies a particular control column as follows:  - The `rs_id` parameter specifies the `RSID$` control column. - The `row_id` parameter specifies the `ROW_ID$` control column. - The `user_id` parameter specifies the `USERNAME$` control column. - The `timestamp` parameter specifies the `TIMESTAMP$` control column. - The `object_id` parameter specifies the `SYS_NC_OID$` control column. - The `source_colmap` parameter specifies the `SOURCE_COLMAP$` control column. - The `target_colmap` parameter specifies the `TARGET_COLMAP$` control column. - The `ddl_markers` parameter tracks all DDL operations on the source table and stores information about those operations in the change table. There are three values: `DDLOPER$` is a bit vector that indicates what kind of DDL operation happened. (Use the procedure `DBMS_CDC_PUBLISH.GET_DDLOPER(ddloper$)` to get the name of the DDL operation.) `DDLDESC$` is a CLOB containing the actual DDL statement executed. `DDLPDOBJN$` is not used in this release.  Each parameter can have a value of `'Y'` or `'N'`, where:  - `'Y'`: Adds the specified control column to the change table. - `'N'`: Does not add the specified control column to the change table. |
| `options_string` | The syntactically correct options to be passed to a `CREATE TABLE` DDL statement. The options string is appended to the generated `CREATE TABLE` DDL statement after the closing parenthesis that defines the columns of the table. See the Usage Notes for more information. |

See Also:

[Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/cdc.htm#DWHSG016) for a complete description of control columns

Exceptions

Table 33-15 CREATE\_CHANGE\_TABLE Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-31402` | Unrecognized parameter specified |
| `ORA-31409` | One or more values for input parameters are incorrect |
| `ORA-31415` | Specified change set does not exist |
| `ORA-31416` | Invalid `SOURCE_COLMAP` value |
| `ORA-31417` | Column list contains control column control-column-name |
| `ORA-31418` | Specified source schema does not exist |
| `ORA-31419` | Specified source table does not exist |
| `ORA-31420` | Unable to submit the purge job |
| `ORA-31421` | Change table does not exist |
| `ORA-31422` | Owner schema does not exist |
| `ORA-31438` | Duplicate change table |
| `ORA-31447` | Cannot create change tables in the `SYS` schema |
| `ORA-31450` | Invalid value for `change_table_name` |
| `ORA-31451` | Invalid value for `capture_values`, expecting: `OLD`, `NEW`, or `BOTH` |
| `ORA-31452` | Invalid value for parameter, expecting: `Y` or `N` |
| `ORA-31459` | System triggers for `DBMS_CDC_PUBLISH` package are not installed |
| `ORA-31467` | No column found in the source table |
| `ORA-31471` | Invalid `OBJECT_ID` value |

Usage Notes

- The publisher can use this procedure for asynchronous and synchronous Change Data Capture.
- A change table is a database table that contains the change data resulting from DML statements (`INSERT`, `UPDATE,` and `DELETE`) made to a source table. A given change table can capture changes from only one source table.
- A change table is a database table that contains two types of columns:
	- User columns, which are copies of actual columns of source tables that reside in the change table.
		- Control columns, which maintain special metadata for each change row in the change table. Information such as the DML operation performed, the capture time (time stamp), and changed column vectors are examples of control columns. The publisher must not specify the name of the control columns in the user column list.
- If there are multiple publishers on the staging database for the Distributed HotLog mode of Change Data capture, and one publisher defines a change table in another publisher's Distributed HotLog change set, then Change Data Capture uses the database link established by the publisher who created the change set to access the source database. Therefore, the database link to the source database established by the publisher who created the change set must be intact for the change table to be successfully created. If the change set publisher's database link is not present when creating a change table, an error is returned indicating that the connection description for the remote database was not found.
- The publisher must not attempt to control a change table's partitioning properties. Change Data Capture automatically manages the change table partitioning as part of its change table management.
- When creating a change table for any mode of asynchronous Change Data Capture, the publisher must accept the default value or specify ' `N` ' for the `source_colmap` and `object_id` parameters. In addition, for the asynchronous Distributed HotLog mode of Change Data Capture, the publisher also must accept the default value or specify ' `N` ' for the `row_id` and `username` parameters when the change source is 9.2 or 10.1.
- When the publisher specifies the `rs_id` parameter, the `RSID$` column is added to the change table. The `RSID$` column value reflects an operation's capture order within a transaction, but not across transactions. The publisher cannot use the `RSID$` column value by itself to order committed operations across transactions; it must be used in conjunction with the `CSCN$` column value.
- The publisher can control a change table's physical properties, tablespace properties, and so on, by specifying the `options_string` parameter. With the `options_string` parameter, the publisher can set any option that is valid for the `CREATE TABLE` DDL statement (except for partitioning properties).
	Note:
	How the publisher defines the `options_string` parameter can have an effect on the performance and operations in a Change Data Capture system. For example, if the publisher places several constraints in the options column, it can have a noticeable effect on performance. Also, if the publisher uses `NOT` `NULL` constraints and a particular column is not changed in an incoming change row, then the constraint can cause the `INSERT` operation to fail and the transaction that contains the `INSERT` operation to be rolled back.
- Oracle recommends that change tables not be created in system tablespaces. This can be accomplished if the publisher's default tablespace is not the system tablespace or if the publisher specifies a tablespace in the `options_string` parameter. If a tablespace is not specified by the publisher, and the publisher's default table space is the system tablespace, then Change Data Capture creates change tables in the system tablespace.
	See Also:
	[Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/cdc.htm#DWHSG016) for more information on, and examples of, creating change tables in tablespaces managed by the publisher.

---

### CREATE\_HOTLOG\_CHANGE\_SOURCE Procedure

This procedure creates a Distributed HotLog change source on the source database when the publisher runs this procedure from the staging database. A Distributed HotLog change source is based on data in the online redo log files that is automatically transferred to the staging database by Oracle Streams propagation.

Syntax

```
DBMS_CDC_PUBLISH.CREATE_HOTLOG_CHANGE_SOURCE(
     change_source_name     IN VARCHAR2,
     description            IN VARCHAR2 DEFAULT NULL,
     source_database        IN VARCHAR2);
```

Parameters

Table 33-16 CREATE\_HOTLOG\_CHANGE\_SOURCE Procedure Parameters

| Parameters | Description |
| --- | --- |
| `change_source_name` | Name of the Distributed HotLog change source to be created. Each change source name must be unique and must follow the Oracle schema object naming rules. |
| `description` | Description of the change source. Specify using 255 or fewer characters. |
| `source_database` | The name of the database link defined from the staging database to the source database, where the source database is Oracle9i Database, Database 10g Release 1, Oracle Database 10g Release 2, or Oracle Database 11g Release 1. See [Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/cdc.htm#DWHSG016) for information on creating database links for the Distributed HotLog mode of Change Data Capture. |

Exceptions

Table 33-17 CREATE\_HOTLOG\_CHANGE\_SOURCE Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-31436` | Duplicate change source |
| `ORA-31480` | Staging database and source database cannot be the same |
| `ORA-31483` | Cannot have spaces in the parameter |
| `ORA-31484` | Source database must be at least 9.2.0.6 or greater |
| `ORA-31485` | Invalid database link |
| `ORA-31499` | Null value specified for required parameter |
| `ORA-31507` | Parameter value longer than the maximum length |
| `ORA-31534` | Change Data Capture publisher is missing DBA role |

Usage Notes

- The publisher can use this procedure for the asynchronous Distributed HotLog mode of Change Data Capture only.
	This procedure cannot be used to create a change source for the asynchronous HotLog mode of Change Database Capture. The publisher must use the predefined change source, HOTLOG\_SOURCE, for the asynchronous HotLog mode of Change Data Capture.
- A Distributed HotLog change source can contain one or more change sets, but they must all be on the same staging database.
- A staging database publisher cannot create multiple Distributed HotLog change sources with the same name, even when those change sources are on different source databases.
- When the publisher creates a change source on a release of Oracle Database earlier than 10.2, Change Data Capture:
	- Generates names for the Streams capture process, capture queue, and propagation based on the change source name. If a generated name is already in use, an error indicating that the capture process, queue, or propagation cannot be created is returned.
		- Inserts a row into the `CHANGE_SOURCES` view on the staging database where the `SOURCE_TYPE` column of the inserted row indicates that the source Oracle Database release is earlier than 10.2.
- Note that the database link indicated by the `source_database` parameter must exist when creating, altering, or dropping a Distributed HotLog change source and the change sets and change tables it contains. However, this database link is not required for change capture to occur. Once the required Distributed HotLog change sources, change sets and change tables are in place and enabled, this database link can be dropped without interrupting change capture. This database link would need to be recreated to create, alter, or drop Distributed HotLog change sources, change sets and change tables.

---

### DROP\_CHANGE\_SET Procedure

This procedure drops an existing change set that was created with the `CREATE_CHANGE_SET` procedure.

Syntax

```
DBMS_CDC_PUBLISH.DROP_CHANGE_SET(
     change_set_name     IN VARCHAR2);
```

Parameters

Table 33-18 DROP\_CHANGE\_SET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `change_set_name` | Name of the change set to be dropped. Change set names follow the Oracle schema object naming rules. |

Exceptions

Table 33-19 DROP\_CHANGE\_SET Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-31410` | Specified change set is not an existing change set |
| `ORA-31411` | Specified change set is referenced by a change table |
| `ORA-31485` | Invalid database link |
| `ORA-31499` | Null value specified for required parameter |
| `ORA-31505` | Cannot alter or drop predefined change set |
| `ORA-31507` | Specified parameter value is longer than maximum length |

Usage Notes

- The publisher can use this procedure for asynchronous and synchronous Change Data Capture.
- The change set to be dropped cannot contain any change tables.
- The predefined synchronous change set, `SYNC_SET`, cannot be dropped.

---

### DROP\_CHANGE\_SOURCE Procedure

This procedure drops an existing AutoLog change source that was created with the `CREATE_AUTOLOG_CHANGE_SOURCE` procedure or an existing Distributed HotLog change source that was created with the `CREATE_HOTLOG_CHANGE_SOURCE` procedure.

Syntax

```
DBMS_CDC_PUBLISH.DROP_CHANGE_SOURCE(
     change_source_name    IN VARCHAR2);
```

Parameters

Table 33-20 DROP\_CHANGE\_SOURCE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `change_source_name` | Name of the change source to be dropped. Change source names follow the Oracle schema object naming rules. |

Exceptions

Table 33-21 DROP\_CHANGE\_SOURCE Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-31401` | Specified change source is not an existing change source |
| `ORA-31406` | Specified change source is referenced by a change set |
| `ORA-31499` | Null value specified for required parameter |
| `ORA-31504` | Cannot alter or drop predefined change source |
| `ORA-31507` | Specified parameter value longer than maximum length |

Usage Notes

- The change source to be dropped cannot contain any change sets.
- The predefined change sources, `HOTLOG_SOURCE` and `SYNC_SOURCE,` cannot be dropped.

---

### DROP\_CHANGE\_TABLE Procedure

This procedure drops an existing change table that was created with the `CREATE_CHANGE_TABLE` procedure.

Syntax

```
DBMS_CDC_PUBLISH.DROP_CHANGE_TABLE(
     owner              IN VARCHAR2,
     change_table_name  IN VARCHAR2,
     force_flag         IN CHAR);
```

Parameters

Table 33-22 DROP\_CHANGE\_TABLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `owner` | Name of the schema that owns the change table. |
| `change_table_name` | Name of the change table to be dropped. Change table names follow the Oracle schema object naming rules. |
| `force_flag` | Drops the change table, depending on whether or not there are subscriptions to it, as follows:  - `'Y'`: Drops the change table even if there are subscriptions to it. - `'N'`: Drops the change table only if there are no subscriptions to it. |

Exceptions

Table 33-23 DROP\_CHANGE\_TABLE Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-31421` | Change table does not exist |
| `ORA-31422` | Specified owner schema does not exist |
| `ORA-31424` | Change table has active subscriptions |
| `ORA-31441` | Table is not a change table |

Usage Notes

- The publisher can use this procedure for asynchronous and synchronous Change Data Capture.
- If the publisher wants to drop a change table while there are active subscriptions to that table, he or she must call the `DROP_CHANGE_TABLE` procedure using the `force_flag => 'Y'` parameter. This tells Change Data Capture to override its normal safeguards and allow the change table to be dropped despite active subscriptions. The subscriptions that include the dropped table will no longer be valid, and subscribers will lose access to the change data.

---

### DROP\_SUBSCRIPTION Procedure

This procedure allows a publisher to drop a subscription that was created by a subscriber with a prior call to the `DBMS_CDC_SUBSCRIBE.CREATE_SUBSCRIPTION` procedure.

Syntax

```
DBMS_CDC_PUBLISH.DROP_SUBSCRIPTION(
     subscription_name  IN VARCHAR2);
```

Parameters

Table 33-24 DROP\_SUBSCRIPTION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `subscription_name` | Name of the subscription that was specified by a previous call to the `DBMS_CDC_SUBSCRIBE.CREATE_SUBSCRIPTION` procedure. Subscription names follow the Oracle schema object naming rules. |

Exceptions

Table 33-25 DROP\_SUBSCRIPTION Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-31409` | One or more values for input parameters are incorrect |
| `ORA-31425` | Subscription does not exist |
| `ORA-31432` | Invalid source table |

Usage Notes

- The publisher can use this procedure for asynchronous and synchronous Change Data Capture.
- This procedure works the same way as the `DBMS_CDC_SUBSCRIBE.DROP_SUBSCRIPTION` procedure.
- This procedure provides the publisher with a way to drop subscriptions that have not been dropped by the subscriber. It is possible that a subscription that is no longer needed still exists and is holding change data in a change table indefinitely. The publisher can use this procedure to remove such a subscription so that a purge operation can clean up its change data. Oracle recommends that the publisher attempt to verify that the subscription is not needed prior to dropping it. If that is not possible, the publisher should inform the subscription owner that the subscription has been dropped. Ideally, subscribers drop subscriptions that are no longer needed using the `DBMS_CDC_SUBSCRIBE.DROP_SUBSCRIPTION` procedure and the publisher need not use the `DBMS_CDC_SUBSCRIBE.DROP_SUBSCRIPTION` procedure.

---

### GET\_DDLOPER Function

This function converts a binary integer into a user friendly string that describes the DDL operation that actually took place.

#### Syntax

```
DBMS_CDC_PUBLISH.GET_DDLOPER (ddloper IN BINARY_INTEGER)
     RETURN VARCHAR2;
```

#### Parameters

Table 33-26 Function Parameters

| Parameter | Description |
| --- | --- |
| `ddloper` | An integer value representing what DDL operation actually occurred. This value is obtained from the `ddloper$` column in the subscriber's view. |

#### Example

The following illustrates how to use change markers. First, you execute a DDL statement and then verify that it has been captured.

```
ALTER TABLE cdc_psales DROP PARTITION Dec_06;

SELECT ddloper$, DECODE(ddloper$, NULL, 'NULL',
       DBMS_CDC_PUBLISH.GET_DDLOPER(ddloper$)) 
          AS DDL_OPER
FROM cdc_psales_act
WHERE DDLOPER$ IS NOT NULL
ORDER BY cscn$;

ddloper$            DDL_OPER
---------------------------------
512                 Drop Partition
1 row selected.

SELECT ddldesc$
FROM cdc_psales_act
WHERE ddloper$
IS NOT NULL 
ORDER BY cscn;

DDLDESC$
------------------------
alter table cdc_psales drop partition Dec_06
1 row selected.
```

#### Usage Notes

- If an invalid value for `ddloper` is given, then `'Invalid value for DDLOPR$'` will be returned by this function.
- This function only works for asynchronous Change Data Capture.

---

### PURGE Procedure

This procedure monitors change table usage by all subscriptions, determines which rows are no longer needed by any subscriptions, and removes the unneeded rows to prevent change tables from growing indefinitely. When called, this procedure purges all change tables on the staging database.

Syntax

```
DBMS_CDC_PUBLISH.PURGE;
```

Exceptions

Only standard Oracle exceptions (for example, a privilege violation) are returned during a purge operation.

Usage Notes

- The publisher can use this procedure for asynchronous and synchronous Change Data Capture.
- The publisher can run this procedure manually or automatically:
	- The publisher can run this procedure manually from the command line to purge data from change tables.
		- The publisher can run this procedure in a script to routinely perform a purge operation and control the growth of change tables.
- Note that the `DBMS_CDC_PUBLISH.PURGE` procedure (used by the publisher and the Change Data Capture default purge job) is distinct from the `DBMS_CDC_SUBSCRIBE.PURGE_WINDOW` procedure (used by subscribers). A call to the `DBMS_CDC_PUBLISH.PURGE` procedure physically removes unneeded rows from change tables. A call to the `DBMS_CDC_SUBSCRIBE.PURGE_WINDOW` procedure, logically removes change rows from a subscription window, but does not physically remove rows from the underlying change tables.

---

### PURGE\_CHANGE\_SET Procedure

This procedure removes unneeded rows from all change tables in the named change set. This procedure allows a finer granularity purge operation than the basic `PURGE` procedure.

Syntax

```
DBMS_CDC_PUBLISH.PURGE_CHANGE_SET(
```
```
change_set_name IN VARCHAR2,
force           IN CHAR DEFAULT 'Y',
purge_date      IN DATE DEFAULT NULL);
```

Parameters

Table 33-27 PURGE\_CHANGE\_SET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `change_set_name` | Name of an existing change set. Change set names follow the Oracle schema object naming rules. |
| `force` | If `'Y'`, try to use partition split/drop, but if the required lock cannot be acquired, use a delete statement to purge. If `'N'`, only use split/drop partition statements to purge. If a lock cannot be acquired, then no data will be purged. |
| `purge_date` | All records that have a `commit_timestamp` of less than or equal to this date will be purged. |

Exceptions

Table 33-28 PURGE\_CHANGE\_SET Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-31410` | Change set is not an existing change set |

Usage Notes

- The publisher can use this procedure for asynchronous and synchronous Change Data Capture.
- The publisher can run this procedure manually from the command line or in a script to purge unneeded rows from change tables in a specific change set.
- Note that the `DBMS_CDC_PUBLISH.PURGE_CHANGE_SET` procedure (used by the publisher) is distinct from the `DBMS_CDC_SUBSCRIBE.PURGE_WINDOW` procedure (used by subscribers). A call to the `DBMS_CDC_PUBLISH.PURGE_CHANGE_SET` procedure physically removes unneeded rows from change tables in the specified change set. A call to the `DBMS_CDC_SUBSCRIBE.PURGE_WINDOW` procedure, logically removes change rows from a subscription window, but does not physically remove rows from the underlying change tables.

---

### PURGE\_CHANGE\_TABLE Procedure

This procedure removes unneeded rows from the named change table. This procedure allows a finer granularity purge operation than the basic `PURGE` procedure or the `PURGE_CHANGE_SET` procedure.

Syntax

```
DBMS_CDC_PUBLISH.PURGE_CHANGE_TABLE(
     owner               IN VARCHAR2,
     change_table_name   IN VARCHAR2,
     force               IN CHAR DEFAULT 'Y',
     purge_date          IN DATE DEFAULT NULL);
```

Parameters

Table 33-29 PURGE\_CHANGE\_TABLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `owner` | Owner of the named change table. |
| `change_table_name` | Name of an existing change table. Change table names follow the Oracle schema object naming rules. |
| `force` | If `'Y'`, try to use partition split/drop, but if the required lock cannot be acquired, use a delete statement to purge. If `'N'`, only use split/drop partition statements to purge. If a lock cannot be acquired, then no data will be purged. |
| `purge_date` | All records that have a `commit_timestamp` of less than or equal to this date will be purged. |

Exceptions

Table 33-30 PURGE\_CHANGE\_TABLE Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-31421` | Change table does not exist |

Usage Notes

- The publisher can use this procedure for asynchronous and synchronous Change Data Capture.
- The publisher can run this procedure manually from the command line or in a script to purge unneeded rows from a specified change table.
- Note that the `DBMS_CDC_PUBLISH.PURGE_CHANGE_TABLE` procedure (used by the publisher) is distinct from the `DBMS_CDC_SUBSCRIBE.PURGE_WINDOW` procedure (used by subscribers). A call to the `DBMS_CDC_PUBLISH.PURGE_CHANGE_TABLE` procedure physically removes unneeded rows from the specified change table. A call to the `DBMS_CDC_SUBSCRIBE.PURGE_WINDOW` procedure, logically removes change rows from a subscription window, but does not physically remove rows from the underlying change tables.