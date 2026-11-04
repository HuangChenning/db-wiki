---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_STORAGE_MAP.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 178 DBMS\_STORAGE\_MAP

With the `DBMS_STORAGE_MAP` package, you can communicate with the Oracle background process FMON to invoke mapping operations that populate mapping views. FMON communicates with operating and storage system vendor-supplied mapping libraries.

This chapter contains the following topics:

### 178.1 DBMS\_STORAGE\_MAP Overview

This terminology and descriptions will help you understand the `DBMS_STORAGE_MAP` API.

- Mapping libraries
	Mapping libraries help you map the components of I/O processing stack elements. Examples of I/O processing components include files, logical volumes, and storage array I/O targets. The mapping libraries are identified in `filemap.ora`.
- Mapping files
	A mapping file is a mapping structure that describes a file. It provides a set of attributes, including file size, number of extents that the file is composed of, and file type.
- Mapping elements and sub-elements
	A mapping element is the abstract mapping structure that describes a storage component within the I/O stack. Examples of elements include mirrors, stripes, partitions, raid5, concatenated elements, and disks—structures that are the mapping building blocks. A mapping sub-element describes the link between an element and the next elements in the I/O mapping stack
- Mapping file extents
	A mapping file extent describes a contiguous chunk of blocks residing on one element. This includes the device offset, the extent size, the file offset, the type (data or parity), and the name of the element where the extent resides. In the case of a raw device or volume, the file is composed of only one file extent component. A mapping file extent is different from Oracle extents.
	See Also:
	- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADMIN-GUID-3348410C-246D-4100-A41E-814E1BD9C541) for more information
	- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=REFRN-GUID-B200B2D6-08D4-49B0-9FD9-8AF6AED37202) for `V$MAP` views, including `V$MAP_FILE`, `V$MAP_ELEMENT`, `V$MAP_SUBELEMENT`, `V$MAP_FILE_EXTENT`

### 178.2 DBMS\_STORAGE\_MAP Operational Notes

Invoking the `MAP_ELEMENT`, `MAP_FILE`, and `MAP_ALL` functions when mapping information already exists will refresh the mapping, if configuration IDs are supported. If configuration IDs are not supported, invoking these functions again will rebuild the mapping.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADMIN-GUID-A5B2943B-1272-4333-9F86-FF4430DE6161) for a discussion of the configuration ID, an attribute of the element or file that is changed.

### 178.3 Summary of DBMS\_STORAGE\_MAP Subprograms

This table lists the `DBMS_STORAGE_MAP` subprograms and briefly describes them.

Table 178-1 DBMS\_STORAGE\_MAP Package Subprograms

| Subprogram | Description |
| --- | --- |
| DROP\_ALL Function | Drops all mapping information in the shared memory of the instance |
| DROP\_ELEMENT Function | Drops the mapping information for the element defined by `elemname` |
| DROP\_FILE Function | Drops the file mapping information defined by `filename` |
| LOCK\_MAP Procedure | Locks the mapping information in the shared memory of the instance |
| MAP\_ALL Function | Builds the entire mapping information for all types of Oracle files (except archive logs), including all directed acyclic graph (DAG) elements |
| MAP\_ELEMENT Function | Builds mapping information for the element identified by `elemname` |
| MAP\_FILE Function | Builds mapping information for the file identified by `filename` |
| MAP\_OBJECT Function | Builds the mapping information for the Oracle object identified by the object name, owner, and type |
| RESTORE Function | Loads the entire mapping information from the data dictionary into the shared memory of the instance |
| SAVE Function | Saves information needed to regenerate the entire mapping into the data dictionary |
| UNLOCK\_MAP Procedure | Unlocks the mapping information in the shared memory of the instance. |

#### 178.3.1 DROP\_ALL Function

This function drops all mapping information in the shared memory of the instance.

Syntax

```
DBMS_STORAGE_MAP.DROP_ALL(
      dictionary_update IN BOOLEAN DEFAULT TRUE);
```

Parameters

Table 178-2 DROP\_ALL Function Parameters

| Parameter | Description |
| --- | --- |
| `dictionary_update` | If `TRUE`, mapping information in the data dictionary is updated to reflect the changes. The default value is `TRUE`; `dictionary_update` is an overloaded argument. |

#### 178.3.2 DROP\_ELEMENT Function

This function drops the mapping information for the element defined by `elemname`.

Syntax

```
DBMS_STORAGE_MAP.DROP_ELEMENT(
   elemname          IN VARCHAR2,
   cascade           IN BOOLEAN,
   dictionary_update IN BOOLEAN DEFAULT TRUE);
```

Parameters

Table 178-3 DROP\_ELEMENT Function Parameters

| Parameter | Description |
| --- | --- |
| `elemname` | The element for which mapping information is dropped. |
| `cascade` | If `TRUE`, then `DROP_ELEMENT` is invoked recursively on all elements of the DAG defined by `elemname,` if possible. |
| `dictionary_update` | If `TRUE`, mapping information in the data dictionary is updated to reflect the changes. The default value is `TRUE`; `dictionary_update` is an overloaded argument. |

#### 178.3.3 DROP\_FILE Function

This function drops the file mapping information defined by `filename`.

Syntax

```
DBMS_STORAGE_MAP.DROP_FILE(
   filename          IN VARCHAR2,
   cascade           IN BOOLEAN,
   dictionary_update IN BOOLEAN DEFAULT TRUE);
```

Parameters

Table 178-4 DROP\_FILE Function Parameters

| Parameter | Description |
| --- | --- |
| `filename` | The file for which file mapping information is dropped. |
| `cascade` | If `TRUE`, then the mapping DAGs for the elements where the file resides are also dropped, if possible. |
| `dictionary_update` | If `TRUE`, mapping information in the data dictionary is updated to reflect the changes. The default value is `TRUE`; `dictionary_update` is an overloaded argument. |

#### 178.3.4 LOCK\_MAP Procedure

This procedure locks the mapping information in the shared memory of the instance.

This is useful when you need a consistent snapshot of the V$MAP tables. Without locking the mapping information, `V$MAP_ELEMENT` and `V$MAP_SUBELEMENT`, for example, may be inconsistent.

Syntax

```
DBMS_STORAGE_MAP.LOCK_MAP;
```

#### 178.3.5 MAP\_ALL Function

This function builds the entire mapping information for all types of Oracle files (except archive logs), including all directed acyclic graph (DAG) elements. It obtains the latest mapping information because it explicitly synchronizes all mapping libraries.

Syntax

```
DBMS_STORAGE_MAP.MAP_ALL(
   max_num_fileext   IN NUMBER DEFAULT 100,
   dictionary_update IN BOOLEAN DEFAULT TRUE);
```

Parameters

Table 178-5 MAP\_ALL Function Parameters

| Parameter | Description |
| --- | --- |
| `max_num_fileext` | Defines the maximum number of file extents to be mapped. This limits the amount of memory used when mapping file extents. The default value is `100`; `max_num_fileextent` is an overloaded argument. |
| `dictionary_update` | If `TRUE`, mapping information in the data dictionary is updated to reflect the changes. The default value is `TRUE`; `dictionary_update` is an overloaded argument. |

Usage Notes

You must explicitly call `MAP_ALL` in a cold startup scenario.

#### 178.3.6 MAP\_ELEMENT Function

This function builds mapping information for the element identified by `elemname`. It may not obtain the latest mapping information if the element being mapped, or any one of the elements within its I/O stack (if `cascade` is `TRUE`), is owned by a library that must be explicitly synchronized.

Syntax

```
DBMS_STORAGE_MAP.MAP_ELEMENT(
   elemname          IN VARCHAR2,
   cascade           IN BOOLEAN,
   dictionary_update IN BOOLEAN DEFAULT TRUE);
```

Parameters

Table 178-6 MAP\_ELEMENT Function Parameters

| Parameter | Description |
| --- | --- |
| `elemname` | The element for which mapping information is built. |
| `cascade` | If `TRUE`, all elements within the elemname I/O stack DAG are mapped. |
| `dictionary_update` | If `TRUE`, mapping information in the data dictionary is updated to reflect the changes. The default value is `TRUE`; `dictionary_update` is an overloaded argument. |

#### 178.3.7 MAP\_FILE Function

This function builds mapping information for the file identified by `filename`. Use this function if the mapping of one particular file has changed. The Oracle database server does not have to rebuild the entire mapping.

Syntax

```
DBMS_STORAGE_MAP.MAP_FILE(
   filename           IN VARCHAR2, 
   filetype           IN VARCHAR2,
   cascade            IN BOOLEAN,
   max_num_fileextent IN NUMBER DEFAULT 100,
   dictionary_update  IN BOOLEAN DEFAULT TRUE);
```

Parameters

Table 178-7 MAP\_FILE Function Parameters

| Parameter | Description |
| --- | --- |
| `filename` | The file for which mapping information is built. |
| `filetype` | Defines the type of the file to be mapped. It can be " `DATAFILE", "SPFILE", "TEMPFILE", "CONTROLFILE", "LOGFILE",` or `"ARCHIVEFILE"`. |
| `cascade` | Should be `TRUE` only if a storage reconfiguration occurred. For all other instances, such as file resizing (either through an `ALTER SYSTEM` command or DML operations on extended files), `cascade` can be set to `FALSE` because the mapping changes are limited to the file extents only.  If `TRUE`, mapping DAGs are also built for the elements where the file resides. |
| `max_num_fileextent` | Defines the maximum number of file extents to be mapped. This limits the amount of memory used when mapping file extents. The default value is `100`; `max_num_fileextent` is an overloaded argument. |
| `dictionary_update` | If `TRUE`, mapping information in the data dictionary is updated to reflect the changes. The default value is `TRUE`; `dictionary_update` is an overloaded argument. |

Usage Notes

This function may not obtain the latest mapping information if the file being mapped, or any one of the elements within its I/O stack (if `cascade` is `TRUE`), is owned by a library that must be explicitly synchronized.

#### 178.3.8 MAP\_OBJECT Function

This function builds the mapping information for the Oracle object identified by the object name, owner, and type.

Syntax

```
DBMS_STORAGE_MAP.MAP_OBJECT(
   objname  IN  VARCHAR2,
   owner    IN  VARCHAR2,
   objtype  IN  VARCHAR2);
```

Parameters

Table 178-8 MAP\_OBJECT Function Parameters

| Parameter | Description |
| --- | --- |
| `objname` | The name of the object. |
| `owner` | The owner of the object. |
| `objtype` | The type of the object. |

#### 178.3.9 RESTORE Function

This function loads the entire mapping information from the data dictionary into the shared memory of the instance.

You can invoke `RESTORE` only after a `SAVE` operation. You must explicitly call `RESTORE` in a warm startup scenario.

Syntax

```
DBMS_STORAGE_MAP.RESTORE;
```

#### 178.3.10 SAVE Function

This function saves information needed to regenerate the entire mapping into the data dictionary.

Syntax

```
DBMS_STORAGE_MAP.SAVE;
```

#### 178.3.11 UNLOCK\_MAP Procedure

This procedure unlocks the mapping information in the shared memory of the instance.

Syntax

```
DBMS_STORAGE_MAP.UNLOCK_MAP;
```