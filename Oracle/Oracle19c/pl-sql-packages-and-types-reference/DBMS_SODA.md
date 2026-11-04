---
title: DBMS_SODA
book: PL/SQL Packages and Types Reference
doc_id: E96430-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_SODA.html
tags:
  - oracle
  - 19c
  - pl-sql-packages-and-types-reference
---

The `DBMS_SODA` package is a `PL/SQL` package implementing Simple Oracle Document Access (`SODA`). `SODA` allows you to use the Oracle Database as a NoSQL document store. The core abstraction provided by `SODA` is that of document collections. The `DBMS_SODA` package allows you to create, list, and delete document collections from `PL/SQL`, and to perform CRUD (create, replace, update, delete) operations on documents. All `DDL` functions are encapsulated within this package.

This chapter contains the following topics:

- DBMS\_SODA Security Model
- Summary of DBMS\_SODA Subprograms

**See Also:**

- [*Oracle Database SODA for PL/SQL Developer’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADSDP-GUID-BE42F8D3-B86B-43B4-B2A3-5760A4DF79FB)
- [SODA Types](SODA_TYPES.md)

### DBMS\_SODA Security Model

This package is available to users with the `SODA_APP` role.

All SODA types (packages and types) are `SYS` types. `PUBLIC` is granted `EXECUTE` privilege on the `DBMS_SODA` described in this chapter.

### Summary of DBMS\_SODA Subprograms

This table lists the `DBMS_SODA` subprograms in alphabetical order and briefly describes them.

Table 1 DBMS\_SODA Package Subprograms

| Subprogram | Purpose |
| --- | --- |
| CREATE\_COLLECTION Function | Creates a collection using the collection name and metadata. |
| DROP\_COLLECTION Function | Drops an existing collection from the user’s schema. This also removes all the documents in the collection. |
| GET\_AS\_OF\_SCN Function | This function returns the current database SCN number. |
| GET\_AS\_OF\_TIMESTAMP Function | This function returns the current database timestamp value. |
| LIST\_COLLECTION\_NAMES Function | Lists the collection names in the user’s schema as a table of `NVARCHAR2`. |
| OPEN\_COLLECTION Function | Opens an existing collection. |
| TO\_UUID Function | This function is used to remap the version column of the collection table during Data Pump Import to UUID values. This function is only for use with the `REMAP_DATA` feature of Data Pump. |

### CREATE\_COLLECTION Function

Creates a collection using the collection name and metadata. Uses the settings specified in the metadata and auto-assigns the ones that are not, and returns the collection object. If the metadata argument is omitted or set to `NULL`, a collection is created with default metadata. The returned collection is open for `read` and/or `write` operations. If a collection already exists, the function just opens and returns the collection object.

**Syntax**

```md
DBMS_SODA.CREATE_COLLECTION (
     collection_Name      IN NVARCHAR2,
     metadata             IN VARCHAR2 DEFAULT NULL,
     create_Mode          IN PLS_INTEGER DEFAULT CREATE_MODE_DDL)
 RETURN SODA_Collection_T;
```

**Parameters**

Table 2 CREATE\_COLLECTION Parameters

| Parameter | Description |
| --- | --- |
| `collection_Name` | The name of the collection.  The value of `collection_Name` is case-sensitive. |
| `metadata` | The metadata of the collection in `VARCHAR2` format. |
| create\_Mode | Valid values are:  - `DBMS_SODA.CREATE_MODE_DDL` (default). First attempts to create a new table for the collection. If table exists already, tries to map that existing table to the collection. Minimal checking is performed to ensure the table shape matches supplied collection metadata (if not, then an error is returned). - `DBMS_SODA.CREATE_MODE_MAP`. Tries to map an existing table to the collection. Minimal checking is performed to ensure the table shape matches supplied collection metadata (if not, then an error is returned). |

**Return Values**

The function returns a `Soda_Collection_T` object representing the collection.

**Exceptions**

- `Descriptor Error` —if the input descriptor is invalid
- `Error` —if an error occurs while creating the collection

**See Also:** [*Oracle Database SODA for PL/SQL Developer’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADSDP-GUID-AC1A88D5-8C89-492D-AC57-E6F3694F6D96)

### DROP\_COLLECTION Function

Drops an existing collection from the user’s schema. This also removes all the documents in the collection.

**Syntax**

```md
DBMS_SODA.DROP_COLLECTION (
     collection_Name      IN NVARCHAR2,
     purge                IN BOOLEAN DEFAULT FALSE,
     drop_Mapped_Table    IN BOOLEAN DEFAULT FALSE)
 RETURN NUMBER;
```

**Parameters**

Table 3 DROP\_COLLECTION Parameters

| Parameter | Description |
| --- | --- |
| `collection_Name` | The name of the collection.  The value of `collection_Name` is case-sensitive. |
| `purge` | The default value is `FALSE`. |
| `drop_Mapped_Table` | The default value is `FALSE`. |

**Return values**

This function returns the following values:

- `1` —if the collection was dropped successfully
- `0` —if the collection does not exist

**Exceptions**

If an error occurs while dropping the collection, for example, due to uncommitted writes to the collection or privilege issues.

**See Also:** [*Oracle Database SODA for PL/SQL Developer’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADSDP-GUID-D29C4FFF-D093-4C1B-889A-5C29B63756C6)

### GET\_AS\_OF\_SCN Function

This function returns the current database SCN number.

**Syntax**

```md
DBMS_SODA.GET_AS_OF_SCN ( )
 RETURN NUMBER;
```

**Return values**

This function returns the current database SCN number.

### GET\_AS\_OF\_TIMESTAMP Function

This function returns the current database timestamp value.

**Syntax**

```md
DBMS_SODA.GET_AS_OF_TIMESTAMP ( )
 RETURN NUMBER;
```

**Return values**

This function returns the current database timestamp value.

### LIST\_COLLECTION\_NAMES Function

This function returns a list of collection names in the user’s schema as a table of `NVARCHAR2`.

**Syntax**

```md
DBMS_SODA.LIST_COLLECTION_NAMES ()
 RETURN SODA_CollName_List_T;
```

**Return Values**

This function returns a list of collection names as a table of `NVARCHAR2(255)`. The collection list is empty if there are no collections in the schema.

**Exceptions**

`Error` -if an error occurs while listing the collection names.

**See Also:** [*Oracle Database SODA for PL/SQL Developer’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADSDP-GUID-4568B14A-C54D-459B-B8B6-114A2148C4F1)

### OPEN\_COLLECTION Function

Opens an existing collection for `read` and/or `write` operations.

**Syntax**

```md
DBMS_SODA.OPEN_COLLECTION (
     collection_Name      IN NVARCHAR2)
 RETURN SODA_Collection_T;
```

**Parameters**

Table 4 OPEN\_COLLECTION Parameters

| Parameter | Description |
| --- | --- |
| `collection_Name` | The name of the collection.  The value of `collection_Name` is case-sensitive. |

**Return Values**

This function returns the following values:

- a collection object which is open
- `NULL`, if the collection does not exist

**Exceptions**

`Error` -if an error occurs while creating the collection

**See Also:**

- [Opening an Existing Document Collection with SODA for PL/SQL](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADSDP-GUID-04A5F0A1-3A3F-4DDE-AF85-324C8CE698DB)
- [Checking Whether a Given Collection Exists with SODA for PL/SQL](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADSDP-GUID-ECE58906-DD2A-4593-93B8-201946632054)

### TO\_UUID Function

This function is used to remap the version column of the collection table during Data Pump Import to UUID values. This function is only for use with the `REMAP_DATA` feature of Data Pump.

**Syntax**

```md
DBMS_SODA.TO_UUID (
     placeholder      IN   NVARCHAR2)
 RETURN VARCHAR2;
```

**Parameters**

Table 5 TO\_UUID Parameters

| Parameter | Description |
| --- | --- |
| `placeholder` | This parameter is not used and can be ignored. It is used due to the syntactic constraints for the Data Pump `REMAP_DATA` function. |

**Return values**

This function returns a hexadecimal string that can be used as a `UUID` value.

**See Also:** [REMAP\_DATA](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=SUTIL-GUID-B831E91E-E720-4492-B9FD-E5DA78CC3E36) in the *Oracle® Database Utilities Guide*.