---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_SODA.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 162 DBMS\_SODA

The `DBMS_SODA` package is a `PL/SQL` package implementing Simple Oracle Document Access (`SODA`). `SODA` allows you to use the Oracle Database as a NoSQL document store. The core abstraction provided by `SODA` is that of document collections. The `DBMS_SODA` package allows you to create, list, and delete document collections from `PL/SQL`, and to perform CRUD (create, replace, update, delete) operations on documents. All `DDL` functions are encapsulated within this package.

This chapter contains the following topics:

See Also:

- [Oracle Database SODA for PL/SQL Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADSDP-GUID-BE42F8D3-B86B-43B4-B2A3-5760A4DF79FB)
- [SODA Types](SODA_TYPES.md)

### 162.1 DBMS\_SODA Security Model

This package is available to users with the `SODA_APP` role.

All SODA types (packages and types) are `SYS` types. `PUBLIC` is granted `EXECUTE` privilege on the `DBMS_SODA` described in this chapter.

### 162.2 Summary of DBMS\_SODA Subprograms

This table lists the `DBMS_SODA` subprograms in alphabetical order and briefly describes them.

Table 162-1 DBMS\_SODA Package Subprograms

| Subprogram | Purpose |
| --- | --- |
| CREATE\_COLLECTION Function | Creates a collection using the collection name and metadata. |
| DROP\_COLLECTION Function | Drops an existing collection from the user’s schema. This also removes all the documents in the collection. |
| GET\_AS\_OF\_SCN Function | This function returns the current database SCN number. |
| GET\_AS\_OF\_TIMESTAMP Function | This function returns the current database timestamp value. |
| GET\_DEFAULT\_METADATA\_AS\_CLOB Function | This function returns the default metadata. |
| GET\_DEFAULT\_METADATA\_AS\_VARCHAR2 Function | This function returns the default metadata. |
| LIST\_COLLECTION\_NAMES Function | Lists the collection names in the user's schema as a table of `NVARCHAR2`. |
| OPEN\_COLLECTION Function | Opens an existing collection. |

#### 162.2.1 CREATE\_COLLECTION Function

Creates a collection using the collection name and metadata. Uses the settings specified in the metadata and auto-assigns the ones that are not, and returns the collection object. If the metadata argument is omitted or set to `NULL`, a collection is created with default metadata. The returned collection is open for `read` and/or `write` operations. If a collection already exists, the function just opens and returns the collection object.

Syntax

```
DBMS_SODA.CREATE_COLLECTION (
     collection_Name      IN NVARCHAR2,
     metadata             IN VARCHAR2 DEFAULT NULL,
     create_Mode          IN PLS_INTEGER DEFAULT CREATE_MODE_DDL)
 RETURN SODA_Collection_T;
```

Parameters

Table 162-2 CREATE\_COLLECTION Parameters

| Parameter | Description |
| --- | --- |
| `collection_Name` | The name of the collection.  The value of `collection_Name` is case-sensitive. |
| `metadata` | The metadata of the collection in `VARCHAR2` format. |
| create\_Mode | Valid values are: - `DBMS_SODA.CREATE_MODE_DDL` (default). First attempts to create a new table for the collection. If table exists already, tries to map that existing table to the collection. Minimal checking is performed to ensure the table shape matches supplied collection metadata (if not, then an error is returned). - `DBMS_SODA.CREATE_MODE_MAP`. Tries to map an existing table to the collection. Minimal checking is performed to ensure the table shape matches supplied collection metadata (if not, then an error is returned). |

Return Values

The function returns a `Soda_Collection_T` object representing the collection.

Exceptions

- `Descriptor Error` —if the input descriptor is invalid
- `Error` —if an error occurs while creating the collection

See Also:

[Oracle Database SODA for PL/SQL Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADSDP-GUID-AC1A88D5-8C89-492D-AC57-E6F3694F6D96)

#### 162.2.2 DROP\_COLLECTION Function

Drops an existing collection from the user’s schema. This also removes all the documents in the collection.

Syntax

```
DBMS_SODA.DROP_COLLECTION (
     collection_Name      IN NVARCHAR2,
     purge                IN BOOLEAN DEFAULT FALSE,
     drop_Mapped_Table    IN BOOLEAN DEFAULT FALSE)
 RETURN NUMBER;
```

Parameters

Table 162-3 DROP\_COLLECTION Parameters

| Parameter | Description |
| --- | --- |
| `collection_Name` | The name of the collection.  The value of `collection_Name` is case-sensitive. |
| `purge` | The default value is `FALSE`. |
| `drop_Mapped_Table` | The default value is `FALSE`. |

Return values

This function returns the following values:

- `1` —if the collection was dropped successfully
- `0` —if the collection does not exist

Exceptions

If an error occurs while dropping the collection, for example, due to uncommitted writes to the collection or privilege issues.

See Also:

[Oracle Database SODA for PL/SQL Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADSDP-GUID-D29C4FFF-D093-4C1B-889A-5C29B63756C6)

#### 162.2.3 GET\_AS\_OF\_SCN Function

This function returns the current database SCN number.

Syntax

```
DBMS_SODA.GET_AS_OF_SCN ( )
 RETURN NUMBER;
```

Return values

This function returns the current database SCN number.

#### 162.2.4 GET\_AS\_OF\_TIMESTAMP Function

This function returns the current database timestamp value.

Syntax

```
DBMS_SODA.GET_AS_OF_TIMESTAMP ( )
 RETURN NUMBER;
```

Return values

This function returns the current database timestamp value.

#### 162.2.5 GET\_DEFAULT\_METADATA\_AS\_CLOB Function

This function returns the default metadata.

Syntax

```
DBMS_SODA.GET_DEFAULT_METADATA_AS_CLOB ( )
 RETURN CLOB;
```

Return Values

This function returns the default metadata using the `CLOB` datatype.

#### 162.2.6 GET\_DEFAULT\_METADATA\_AS\_VARCHAR2 Function

This function returns the default metadata.

Syntax

```
DBMS_SODA.GET_DEFAULT_METADATA_AS_VARCHAR2 ( )
 RETURN VARCHAR2;
```

Return Values

This function returns the default metadata using the `VARCHAR2` datatype.

#### 162.2.7 LIST\_COLLECTION\_NAMES Function

This function returns a list of collection names in the user’s schema as a table of `NVARCHAR2`.

Syntax

```
DBMS_SODA.LIST_COLLECTION_NAMES ()
 RETURN SODA_CollName_List_T;
```

Return Values

This function returns a list of collection names as a table of `NVARCHAR2(255)`. The collection list is empty if there are no collections in the schema.

Exceptions

`Error` —if an error occurs while listing the collection names.

See Also:

[Oracle Database SODA for PL/SQL Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADSDP-GUID-4568B14A-C54D-459B-B8B6-114A2148C4F1)

#### 162.2.8 OPEN\_COLLECTION Function

Opens an existing collection for `read` and/or `write` operations.

Syntax

```
DBMS_SODA.OPEN_COLLECTION (
     collection_Name      IN NVARCHAR2)
 RETURN SODA_Collection_T;
```

Parameters

Table 162-4 OPEN\_COLLECTION Parameters

| Parameter | Description |
| --- | --- |
| `collection_Name` | The name of the collection.  The value of `collection_Name` is case-sensitive. |

Return Values

This function returns the following values:

- a collection object which is open
- `NULL`, if the collection does not exist

Exceptions

`Error` —if an error occurs while creating the collection

See Also:

- [Opening an Existing Document Collection with SODA for PL/SQL](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADSDP-GUID-04A5F0A1-3A3F-4DDE-AF85-324C8CE698DB)
- [Checking Whether a Given Collection Exists with SODA for PL/SQL](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADSDP-GUID-ECE58906-DD2A-4593-93B8-201946632054)

### 162.3 Summary of SODA Online Redefinition Subprograms

This table lists the SODA Online Redefinition subprograms in alphabetical order and briefly describes them.

Table 162-5 SODA Online Redefinition Subprograms

| Subprogram | Purpose |
| --- | --- |
| ABORT\_REDEF\_COLLECTION Procedure | This procedure reverts the changes made to a collection if there are any errors in `CREATE_INTERIM_COLLECTION`, `START_REDEF_COLLECTION`, `COPY_COLLECTION_DEPENDENTS`, `SYNC_INTERIM_COLLETION`, or due to any other reasons. |
| CAN\_REDEF\_COLLECTION Procedure | This procedure checks if the data table can be redefined. If the data table cannot be redefined, errors are raised. |
| COPY\_COLLECTION\_DEPENDENTS Procedure | This procedure copies all the dependents that are defined on the original table to the interim table. However, if the interim table is JSON type, constraints like `IS JSON NOT                                         NULL` will not be copied because those are extraneous. |
| CREATE\_INTERIM\_COLLECTION Procedure | This procedure creates an interim `SODA` collection. The interim\_metadata specifies the changes the user needs to make. For example, a delta applied as a patch to the original matadata. |
| FINISH\_REDEF\_COLLECTION Procedure | This procedure performs the following tasks in one atomic transaction. It introduces a downtime. This can only be called after every dependent required for a `SODA` data table is present on the interim collection, otherwise an error is raised. |
| START\_REDEF\_COLLECTION Procedure | This procedure starts the redefinition process. Copies the existing data from the original table to the interim table and performs the required transformations on the redefined columns. |
| SYNC\_INTERIM\_COLLETION Procedure | This procedure syncronizes the changes to the interim table if the original data table was changed. This procedure can only be called after every dependent required for the `SODA` data table is present on the interim collection, otherwise, an error is raised. |
| TO\_UUID Function | This function is used to remap the version column of the collection table during Data Pump Import to UUID values. This function is only for use with the `REMAP_DATA` feature of Data Pump. |

#### 162.3.1 ABORT\_REDEF\_COLLECTION Procedure

This procedure reverts the changes made to a collection if there are any errors in `CREATE_INTERIM_COLLECTION`, `START_REDEF_COLLECTION`, `COPY_COLLECTION_DEPENDENTS`, `SYNC_INTERIM_COLLETION`, or due to any other reasons.

Syntax

```
DBMS_SODA.ABORT_REDEF_COLLECTION (
   collection_name         IN  NVARCHAR2,
   interim_collection_name IN  NVARCHAR2);
```

Parameters

Table 162-6 ABORT\_REDEF\_COLLECTION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `collection_name` | The name of the collection to be redefined. |
| `interim_collection_name` | The name used for the interim collection. |

#### 162.3.2 CAN\_REDEF\_COLLECTION Procedure

This procedure checks if the data table can be redefined. If the data table cannot be redefined, errors are raised.

Syntax

```
DBMS_SODA.CAN_REDEF_COLLECTION (
   collection_name   IN  NVARCHAR2);
```

Parameters

Table 162-7 CAN\_REDEF\_COLLECTION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `collection_name` | The name of the collection to be redefined. |

#### 162.3.3 COPY\_COLLECTION\_DEPENDENTS Procedure

This procedure copies all the dependents that are defined on the original table to the interim table.

Syntax

```
DBMS_SODA.COPY_COLLECTION_DEPENDENTS (
   collection_name         IN  NVARCHAR,
   interim_collection_name IN  NVARCHAR2,    
   ignore_error            IN  BOOLEAN DEFAULT NULL,
   num_errors              OUT PLS_INTEGER);
```

Parameters

Table 162-8 COPY\_COLLECTION\_DEPENDENTS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `collection_name` | The name of the collection to be redefined. |
| `interim_collection_name` | The name used for the interim collection. |
| `ignore_error` | Ignore the errors encountered in the process and proceed. |
| `num_errors` | The number of errors encountered in the process. |

#### 162.3.4 CREATE\_INTERIM\_COLLECTION Procedure

This procedure creates an interim `SODA` collection. The `interim_metadata` specifies the changes the user needs to make. For example, a delta applied as a patch to the original matadata.

Syntax

```
DBMS_SODA.CREATE_INTERIM_COLLECTION (
   collection_name            IN  NVARCHAR2,
   interim_collection_name    IN  NVARCHAR2,
   interim_metadata           IN  VARCHAR2);
```

Parameters

Table 162-9 CREATE\_INTERIM\_COLLECTION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `collection_name` | The name of the collection to be redefined. |
| `interim_collection_name` | The name used for the interim collection. |
| `interim_metadata` | The metadata snippet specifying the columns that need to be redefined and how they need to be redefined. |

Usage Notes

The `interim_metadata` parameter can contain the following fields. An error is raised if other fields are present and if the fields are not the same as those in the metadata for the original collection.

- Set `contentColumn.sqlType` to `JSON` in order to redefine the `CONTENT` column to `JSON` type, automatically generating the `VERSION` column if needed.
- Set `versionColumn.method` to `UUID` to redefine the `VERSION` column to use `UUID`.
- Set `tableName` to specify a name for the data table of this interim collection. If this field is not present, a default data table name will be generated according to the rules of table name defaulting outlined in [Default Naming of a Collection Table](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADSDI-GUID-9200BDAC-4BA3-4AD2-BF4B-81196278C064). However, if the table already exists, the collection is created using the `MAP` mode. In this scenario, make sure that the mapped table does not have any constraints defined.
- The user can combine the above fields in the supplied `interim_metadata` snippet. For example, the most common use case is to both redefine the content column to `JSON` type and redefine the version column to `UUID`, which can be achieved by setting the `interim_metadata` parameter to `{“contentColumn” :                   {“sqlType”: “JSON”}, “versionColumn” : {“method”: “UUID”}}`.

#### 162.3.5 FINISH\_REDEF\_COLLECTION Procedure

This procedure performs the following tasks in one atomic transaction. It introduces a downtime. This can only be called after every dependent required for a `SODA` data table is present on the interim collection, otherwise an error is raised.

Syntax

```
DBMS_SODA.FINISH_REDEF_COLLECTION (
   collection_name         IN  NVARCHAR,
   interim_collection_name IN  NVARCHAR2,
   dml_lock_timeout        IN  PLS_INTEGER DEFAULT NULL);
```

Parameters

Table 162-10 FINISH\_REDEF\_COLLECTION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `collection_name` | The name of the collection to be redefined. |
| `interim_collection_name` | The name used for the interim collection. |
| `dml_lock_timeout` | The wait period in seconds. If the lock is not acquired within this wait period, an error occurs. |

Usage Notes

This action cannot be undone. After this procedure is executed, you cannot perform `ROLLBACK` procedure provided by the `DBMS_REDEFINITION` package.

Caution:

Before calling `FINISH_REDEF_COLLECTION Procedure`, the interim collection should be tried out to make sure it can be accessed and is working as expected. In case of any issues, use ABORT\_REDEF\_COLLECTION Procedure.

It is very important to do this before calling `FINISH_REDEF_COLLECTION` because the latter cannot be reversed.

#### 162.3.6 START\_REDEF\_COLLECTION Procedure

This procedure starts the redefinition process. Copies the existing data from the original table to the interim table and performs the required transformations on the redefined columns.

Syntax

```
DBMS_SODA.START_REDEF_COLLECTION (
   collection_name         IN  NVARCHAR,
   interim_collection_name IN  NVARCHAR2,    
   copy_vpd_opt            IN  DEFAULT NULL,
   refresh_dep_mviews      IN  DEFAULT NULL);
```

Parameters

Table 162-11 START\_REDEF\_COLLECTION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `collection_name` | The name of the collection to be redefined. |
| `interim_collection_name` | The name used for the interim collection. |
| `copy_vpd_opt` | Can be either `DBMS_REDEFINITION.CONS_VPD_MANUAL` or `DBMS_REDEFINITION.CONS_VPD_NONE`.  `DBMS_REDEFINITION.CONS_VPD_MANUAL` is used to indicate to copy VPD policies manually. `DBMS_REDEFINITION.CONS_VPD_NONE` is used to indicate that there are no VPD policies on the original table. If `NULL`, `DBMS_REDEFINITION.CONS_VPD_NONE` is used. |
| `refresh_dep_mviews` | Can be `N` or `Y`. When set to `N`, fast refresh of dependent materialized views is performed when the `START_REDEF_TABLE` procedure is run, each time the `SYNC_INTERIM_TABLE` procedure is run, and when the `FINISH_REDEF_TABLE` procedure is run. If `NULL`, `N` is used. |

#### 162.3.7 SYNC\_INTERIM\_COLLETION Procedure

This procedure synchronizes the changes to the interim table if the original data table was changed. This procedure can only be called after every dependent required for the `SODA` data table is present on the interim collection, otherwise, an error is raised.

Syntax

```
DBMS_SODA.SYNC_INTERIM_COLLETION (
   collection_name         IN  NVARCHAR,
   interim_collection_name IN  NVARCHAR2);
```

Parameters

Table 162-12 SYNC\_INTERIM\_COLLETION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `collection_name` | The name of the collection to be redefined. |
| `interim_collection_name` | The name used for the interim collection. |

#### 162.3.8 TO\_UUID Function

This function is used to remap the version column of the collection table during Data Pump Import to UUID values. This function is only for use with the `REMAP_DATA` feature of Data Pump.

Syntax

```
DBMS_SODA.TO_UUID (
     placeholder      IN   NVARCHAR2)
 RETURN VARCHAR2;
```

Parameters

Table 162-13 TO\_UUID Parameters

| Parameter | Description |
| --- | --- |
| `placeholder` | This parameter is not used and can be ignored. It is used due to the syntactic constraints for the Data Pump `REMAP_DATA` function. |

Return values

This function returns a hexadecimal string that can be used as a `UUID` value.

See Also:

[REMAP\_DATA](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=SUTIL-GUID-B831E91E-E720-4492-B9FD-E5DA78CC3E36) in the Oracle® Database Utilities Guide.