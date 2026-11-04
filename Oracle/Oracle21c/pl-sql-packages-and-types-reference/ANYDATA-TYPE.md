---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/ANYDATA-TYPE.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 284 ANYDATA TYPE

An `ANYDATA` TYPE contains an instance of a given type, plus a description of the type. In this sense, an `ANYDATA` is self-describing. An `ANYDATA` can be persistently stored in the database.

This chapter contains the following topics:

### 284.1 ANYDATA TYPE Restrictions

Persistent storage of `ANYDATA` instances whose type contains embedded LOBs other than `BFILE` s is not currently supported.

### 284.2 ANYDATA TYPE Operational Notes

This section contains notes related to ANYDATA TYPE construction and access.

Construction

There are 2 ways to construct an `ANYDATA`. The `CONVERT*` calls enable construction of the `ANYDATA` in its entirety with a single call. They serve as explicit CAST functions from any type in the Oracle ORDBMS to `ANYDATA`.

```
STATIC FUNCTION ConvertBDouble(dbl IN BINARY_DOUBLE) return ANYDATA,
STATIC FUNCTION ConvertBfile(b IN BFILE) RETURN ANYDATA,
STATIC FUNCTION ConvertBFloat(fl IN BINARY_FLOAT) return ANYDATA,
STATIC FUNCTION ConvertBlob(b IN BLOB) RETURN ANYDATA,
STATIC FUNCTION ConvertChar(c IN CHAR) RETURN ANYDATA,
STATIC FUNCTION ConvertClob(c IN CLOB) RETURN ANYDATA,
STATIC FUNCTION ConvertCollection(col IN "collection_type") RETURN ANYDATA,
STATIC FUNCTION ConvertDate(dat IN DATE) RETURN ANYDATA,
STATIC FUNCTION ConvertIntervalDS(inv IN INTERVAL DAY TO SECOND) return ANYDATA,
STATIC FUNCTION ConvertIntervalYM(invIN INTERVAL YEAR TO MONTH) return ANYDATA,
STATIC FUNCTION ConvertNchar(nc IN NCHAR) return ANYDATA,
STATIC FUNCTION ConvertNClob(nc IN NCLOB) return ANYDATA,
STATIC FUNCTION ConvertNumber(num IN NUMBER) RETURN ANYDATA,
STATIC FUNCTION ConvertNVarchar2(nc IN NVARCHAR2) return ANYDATA,
STATIC FUNCTION ConvertObject(obj IN "<object_type>") RETURN ANYDATA,
STATIC FUNCTION ConvertRaw(r IN RAW) RETURN ANYDATA,
STATIC FUNCTION ConvertRef(rf IN REF "<object_type>") RETURN ANYDATA,
STATIC FUNCTION ConvertTimestamp(ts IN TIMESTAMP) return ANYDATA,
STATIC FUNCTION ConvertTimestampTZ(ts IN TIMESTAMP WITH TIMEZONE) return ANYDATA,
STATIC FUNCTION ConvertTimestampLTZ(ts IN TIMESTAMP WITH LOCAL TIMEZONE) return ANYDATA,
STATIC FUNCTION ConvertURowid(rid IN UROWID) return ANYDATA,
STATIC FUNCTION ConvertVarchar(c IN VARCHAR) RETURN ANYDATA,
STATIC FUNCTION ConvertVarchar2(c IN VARCHAR2) RETURN ANYDATA,
```

The second way to construct an `ANYDATA` is a piece by piece approach. The BEGINCREATE Static Procedure call begins the construction process and ENDCREATE Member Procedure call finishes the construction process. In between these two calls, the individual attributes of an object type or the elements of a collection can be set using `SET*` calls. For piece by piece access of the attributes of objects and elements of collections, the PIECEWISE Member Procedure should be invoked prior to `GET*` calls.

Note: The `ANYDATA` has to be constructed or accessed sequentially starting from its first attribute (or collection element). The `BEGINCREATE` call automatically begins the construction in a piece-wise mode. There is no need to call `PIECEWISE` immediately after `BEGINCREATE`. `ENDCREATE` should be called to finish the construction process (before which any access calls can be made).

Access

Access functions are available based on SQL. These functions do not throw exceptions on type-mismatch. Instead, they return `NULL` if the type of the `ANYDATA` does not correspond to the type of access. If you wish to use only `ANYDATA` functions of the appropriate types returned in a query, you should use a `WHERE` clause which uses `GETTYPENAME` and choose the type you are interested in (say " `SYS`.`NUMBER` "). Each of these functions returns the value of a specified datatype inside a `SYS.ANYDATA` wrapper.

```
MEMBER FUNCTION AccessBDouble(self IN ANYDATA) return BINARY_DOUBLE
   DETERMINISTIC,
MEMBER FUNCTION AccessBfile(self IN ANYDATA) return BFILE,
MEMBER FUNCTION AccessBFloat(self IN ANYDATA) return BINARY_FLOAT
   DETERMINISTIC,
MEMBER FUNCTION AccessBlob(self IN ANYDATA) return BLOB,
MEMBER FUNCTION AccessChar(self IN ANYDATA) return CHAR,
MEMBER FUNCTION AccessClob(self IN ANYDATA) return CLOB,
MEMBER FUNCTION AccessDate(self IN ANYDATA) return DATE,
MEMBER FUNCTION AccessIntervalYM(self IN ANYDATA) return INTERVAL YEAR TO MONTH,
MEMBER FUNCTION AccessIntervalDS(self IN ANYDATA) return INTERVAL DAY TO SECOND,
MEMBER FUNCTION AccessNchar(self IN ANYDATA) return NCHAR,
MEMBER FUNCTION AccessNClob(self IN ANYDATA) return NCLOB
MEMBER FUNCTION AccessNumber(self IN ANYDATA) return NUMBER,
MEMBER FUNCTION AccessNVarchar2(self IN ANYDATA) return NVARCHAR2,
MEMBER FUNCTION AccessRaw(self IN ANYDATA) return RAW,
MEMBER FUNCTION AccessTimestamp(self IN ANYDATA) return TIMESTAMP,
MEMBER FUNCTION AccessTimestampLTZ(self IN ANYDATA) return TIMESTAMP WITH LOCAL 
   TIMEZONE,
MEMBER FUNCTION AccessTimestampTZ(self IN ANYDATA) return TIMESTAMP WITH 
   TIMEZONE,
MEMBER FUNCTION AccessURowid(self IN ANYDATA) return UROWID DETERMINISTIC
MEMBER FUNCTION AccessVarchar(self IN ANYDATA) return VARCHAR,
MEMBER FUNCTION AccessVarchar2(self IN ANYDATA) return VARCHAR2,
```

### 284.3 Summary of ANYDATA Subprograms

This table lists the `ANYDATA` subprograms in alphabetical order and briefly describes them.

Table 284-1 ANYDATA Type Subprograms

| Subprogram | Description |
| --- | --- |
| BEGINCREATE Static Procedure | Begins creation process on a new `ANYDATA` |
| ENDCREATE Member Procedure | Ends creation of an `ANYDATA` |
| GET\* Member Functions | Gets the current data value (which should be of appropriate type) |
| GETTYPE Member Function | Gets the Type of the `ANYDATA` |
| GETTYPENAME Member Function | Get the fully qualified type name for the `ANYDATA` |
| PIECEWISE Member Procedure | Sets the `MODE` of access of the current data value to be an attribute at a time (if the data value is of `TYPECODE_OBJECT`) |
| SET\* Member Procedures | Sets the current data value. |

#### 284.3.1 BEGINCREATE Static Procedure

This procedure begins the creation process on a new `ANYDATA`.

Syntax

```
STATIC PROCEDURE BeginCreate(
   dtype          IN OUT NOCOPY AnyType,
   adata          OUT NOCOPY ANYDATA);
```

Parameters

Table 284-2 BEGINCREATE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `dtype` | The type of the `ANYDATA`. (Should correspond to `OCI_TYPECODE_OBJECT` or a Collection typecode.) |
| `adata` | ANYDATA being constructed. |

Exception

`DBMS_TYPES.INVALID_PARAMETERS`: dtype is invalid (not fully constructed, and similar deficits.)

Usage Notes

There is no need to call `PIECEWISE` immediately after this call. The construction process begins in a piece-wise manner automatically.

#### 284.3.2 ENDCREATE Member Procedure

This procedure ends creation of an `ANYDATA`. Other creation functions cannot be called after this call.

Syntax

```
MEMBER PROCEDURE EndCreate(
   self         IN OUT NOCOPY ANYDATA);
```

Parameters

Table 284-3 ENDCREATE Procedure Parameter

| Parameter | Description |
| --- | --- |
| `self` | An `ANYDATA`. |

#### 284.3.3 GET\* Member Functions

These functions get the current data value (which should be of appropriate type).

The type of the current data value depends on the MODE by which it is accessed (depending on whether the `PIECEWISE` call is invoked).

If `PIECEWISE` has NOT been called, the `ANYDATA` is accessed in its entirety and the type of the data value should match the type of the `ANYDATA`.

If `PIECEWISE` has been called, the `ANYDATA` is accessed piece-wise. The type of the data value should match the type of the attribute (or collection element) at the current position.

Syntax

```
MEMBER FUNCTION GetBDouble(
   self         IN ANYDATA,
   dbl          OUT NOCOPY BINARY_DOUBLE)
RETURN PLS_INTEGER;

MEMBER FUNCTION GetBfile(
   self         IN ANYDATA,
   b            OUT NOCOPY BFILE)
   RETURN       PLS_INTEGER;

MEMBER FUNCTION GetBFloat(
   self         IN ANYDATA,
   fl           OUT NOCOPY BINARY_FLOAT)
RETURN PLS_INTEGER;

MEMBER FUNCTION GetBlob(
   self         IN ANYDATA,
   b            OUT NOCOPY BLOB)
   RETURN       PLS_INTEGER;

MEMBER FUNCTION GetChar(
   self         IN ANYDATA,
   c            OUT NOCOPY CHAR)
   RETURN       PLS_INTEGER;

MEMBER FUNCTION GetClob(
   self         IN ANYDATA,
   c            OUT NOCOPY CLOB)
   RETURN       PLS_INTEGER;

MEMBER FUNCTION GetCollection(
   self         IN ANYDATA,
   col          OUT NOCOPY "<collection_type>")
   RETURN       PLS_INTEGER;

MEMBER FUNCTION GetDate(
   self         IN ANYDATA,
   dat          OUT NOCOPY DATE)
   RETURN       PLS_INTEGER;

MEMBER FUNCTION GetIntervalDS(
   self         IN ANYDATA,
   inv          OUT NOCOPY INTERVAL DAY TO SECOND) 
 RETURN         PLS_INTEGER;

MEMBER FUNCTION GetIntervalYM(
   self         IN ANYDATA,
   inv          OUT NOCOPY INTERVAL YEAR TO MONTH) 
 RETURN         PLS_INTEGER;

MEMBER FUNCTION GetNchar(
   self         IN ANYDATA, 
   nc           OUT NOCOPY NCHAR) 
 RETURN         PLS_INTEGER;

MEMBER FUNCTION GetNClob(
   self         IN ANYDATA, 
   nc           OUT NOCOPY NCLOB) 
 RETURN         PLS_INTEGER;

MEMBER FUNCTION GetNumber(
   self         IN ANYDATA,
   num          OUT NOCOPY NUMBER)
   RETURN       PLS_INTEGER;

MEMBER FUNCTION GetNVarchar2(
   self         IN ANYDATA, 
   nc           OUT NOCOPY NVARCHAR2) 
 RETURN         PLS_INTEGER;

MEMBER FUNCTION GetObject(
   self         IN ANYDATA,
   obj          OUT NOCOPY "<object_type>")
   RETURN       PLS_INTEGER;

MEMBER FUNCTION GetRaw(
   self         IN ANYDATA,
   r            OUT NOCOPY RAW)
   RETURN       PLS_INTEGER;

MMEMBER FUNCTION GetRef(
   self         IN ANYDATA,
   rf           OUT NOCOPY REF "<object_type>")
   RETURN       PLS_INTEGER;

MEMBER FUNCTION GetTimestamp(
   self         IN ANYDATA, 
   ts           OUT NOCOPY TIMESTAMP)
 RETURN PLS_INTEGER;

MEMBER FUNCTION GetTimestampTZ(
   self         IN ANYDATA, 
   ts           OUT NOCOPY TIMESTAMP WITH TIME ZONE) 
 RETURN PLS_INTEGER;

MEMBER FUNCTION GetTimestampLTZ(
   self         IN ANYDATA,
   ts           OUT NOCOPY TIMESTAMP WITH LOCAL TIME ZONE) 
 RETURN PLS_INTEGER;

MEMBER FUNCTION GetVarchar(
   self         IN ANYDATA,
   c            OUT NOCOPY VARCHAR)
   RETURN       PLS_INTEGER;

MEMBER FUNCTION GetVarchar2(
   self         IN ANYDATA,
   c            OUT NOCOPY VARCHAR2)
   RETURN       PLS_INTEGER;
```

Parameters

Table 284-4 GET\* Function Parameter

| Parameter | Description |
| --- | --- |
| `self` | An ANYDATA. |
| `num` | The number to be obtained. |

Return Values

`DBMS_TYPES`.`SUCCESS` or `DBMS_TYPES`.`NO_DATA`

The return value is relevant only if `PIECEWISE` has been already called (for a collection). In such a case, DBMS\_TYPES.NO\_DATA signifies the end of the collection when all elements have been accessed.

Exceptions

`DBMS_TYPES.TYPE_MISMATCH`: When the expected type is different from the passed in type.

`DBMS_TYPES.INVALID_PARAMETERS`: Invalid Parameters (if it is not appropriate to add a number at this point in the creation process).

`DBMS_TYPES.INCORRECT_USAGE`: Incorrect usage.

#### 284.3.4 GETTYPE Member Function

This function gets the typecode of the `ANYDATA`.

Syntax

```
MEMBER FUNCTION GETTYPE(
   self          IN ANYDATA,
   typ           OUT NOCOPY AnyType)
   RETURN        PLS_INTEGER;
```

Parameters

Table 284-5 GETTYPE Function Parameter

| Parameter | Description |
| --- | --- |
| `self` | An `ANYDATA`. |
| `typ` | The AnyType corresponding to the `ANYDATA`. May be `NULL` if it does not represent a user-defined type. |

Return Values

The typecode corresponding to the type of the `ANYDATA`.

#### 284.3.5 GETTYPENAME Member Function

This function gets the fully qualified type name for the `ANYDATA`.

If the `ANYDATA` is based on a built-in type, this function will return NUMBER and other relevant information.

If it is based on a user defined type, this function will return schema\_name.type\_name, for example, SCOTT.FOO.

If it is based on a transient anonymous type, this function will return NULL.

Syntax

```
MEMBER FUNCTION GETTYPENAME(
   self         IN ANYDATA)
   RETURN       VARCHAR2;
```

Parameters

Table 284-6 GETTYPENAME Function Parameter

| Parameter | Description |
| --- | --- |
| `self` | An `ANYDATA`. |

Return Values

Type name of the `ANYDATA`.

#### 284.3.6 PIECEWISE Member Procedure

This procedure sets the MODE of access of the current data value to be an attribute at a time (if the data value is of `TYPECODE_OBJECT`).

It sets the MODE of access of the data value to be a collection element at a time (if the data value is of collection type). Once this call has been made, subsequent calls to `SET*` and `GET*` will sequentially obtain individual attributes or collection elements.

Syntax

```
MEMBER PROCEDURE PIECEWISE(
   self         IN OUT NOCOPY ANYDATA);
```

Parameters

Table 284-7 PIECEWISE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `self` | The current data value. |

Exceptions

- `DBMS_TYPES.INVALID_PARAMETERS`
- `DBMS_TYPES.INCORRECT_USAGE`: On incorrect usage.

Usage Notes

The current data value must be of an `OBJECT` or `COLLECTION` type before this call can be made.

Piece-wise construction and access of nested attributes that are of object or collection types is not supported.

#### 284.3.7 SET\* Member Procedures

This procedure sets the current data value.

This is a list of procedures that should be called depending on the type of the current data value. The type of the data value should be the type of the attribute at the current position during the piece-wise construction process.

Syntax

```
MEMBER PROCEDURE SETBDOUBLE(
   self        IN OUT NOCOPY ANYDATA,
   dbl         IN BINARY_DOUBLE,
   last_elem   IN boolean DEFAULT FALSE);

MEMBER PROCEDURE SETBFILE(
   self        IN OUT NOCOPY ANYDATA,
   b           IN BFILE,
   last_elem   IN boolean DEFAULT FALSE);

MEMBER PROCEDURE SETBFLOAT(
   self        IN OUT NOCOPY ANYDATA, 
   fl          IN            BINARY_FLOAT,
   last_elem   IN            boolean DEFAULT FALSE);

MEMBER PROCEDURE SETBLOB(
   self        IN OUT NOCOPY ANYDATA, 
   b           IN BLOB,
   last_elem   IN boolean DEFAULT FALSE);

MEMBER PROCEDURE SETCHAR(
   self        IN OUT NOCOPY ANYDATA, 
   c           IN CHAR,
   last_elem   IN boolean DEFAULT FALSE);

MEMBER PROCEDURE SETCLOB(
   self        IN OUT NOCOPY ANYDATA,
   c           IN CLOB,
   last_elem   IN boolean DEFAULT FALSE);

MEMBER PROCEDURE SETCOLLECTION(
   self        IN OUT NOCOPY ANYDATA,
   col         IN "<collectyion_type>",
   last_elem   IN boolean DEFAULT FALSE);

MEMBER PROCEDURE SETDATE(
   self        IN OUT NOCOPY ANYDATA, 
   dat         IN DATE,
   last_elem   IN boolean DEFAULT FALSE);

MEMBER PROCEDURE SETINTERVALDS(
   self        IN OUT NOCOPY ANYDATA,
   inv         IN INTERVAL DAY TO SECOND,
   last_elem IN boolean DEFAULT FALSE);
  
MEMBER PROCEDURE SETINTERVALYM(
   self        IN OUT NOCOPY ANYDATA,
   inv         IN INTERVAL YEAR TO MONTH,
   last_elem   IN boolean DEFAULT FALSE);
  
MEMBER PROCEDURE SETNCHAR(
   self        IN OUT NOCOPY ANYDATA,
   nc          IN NCHAR, 
   last_elem   IN boolean DEFAULT FALSE);
  
MEMBER PROCEDURE SETNCLOB(
   self        IN OUT NOCOPY ANYDATA,
   nc          IN NClob, 
   last_elem   IN boolean DEFAULT FALSE);

MEMBER PROCEDURE SETNUMBER(
   self        IN OUT NOCOPY ANYDATA, 
   num         IN NUMBER,
   last_elem   IN boolean DEFAULT FALSE);

MEMBER PROCEDURE SETNVARCHAR2(
   self        IN OUT NOCOPY ANYDATA,
   nc          IN NVarchar2, 
   last_elem   IN boolean DEFAULT FALSE),
  
MEMBER PROCEDURE SETOBJECT(
   self        IN OUT NOCOPY ANYDATA,
   obj         IN "<object_type>",
   last_elem   IN boolean DEFAULT FALSE);

MEMBER PROCEDURE SETRAW(
   self        IN OUT NOCOPY ANYDATA, 
   r           IN RAW,
   last_elem   IN boolean DEFAULT FALSE);

MEMBER PROCEDURE SETREF(
   self        IN OUT NOCOPY ANYDATA,
   rf          IN REF "<object_type>",
   last_elem   IN boolean DEFAULT FALSE);

MEMBER PROCEDURE SETTIMESTAMP(
   self       IN OUT NOCOPY ANYDATA, 
   ts         IN TIMESTAMP,
   last_elem  IN BOOLEAN DEFAULT FALSE);
  
MEMBER PROCEDURE SETTIMESTAMPTZ(self IN OUT NOCOPY ANYDATA, 
   ts          IN TIMESTAMP WITH TIME ZONE,
   last_elem   IN BOOLEAN DEFAULT FALSE);
  
MEMBER PROCEDURE SETTIMESTAMPLTZ(
   self IN OUT NOCOPY ANYDATA,
   ts IN TIMESTAMP WITH LOCAL TIME ZONE,
   last_elem IN boolean DEFAULT FALSE),
  
MEMBER PROCEDURE SETVARCHAR(
   self        IN OUT NOCOPY ANYDATA, 
   c           IN VARCHAR,
   last_elem   IN boolean DEFAULT FALSE);

MEMBER PROCEDURE SETVARCHAR2(
   self        IN OUT NOCOPY ANYDATA,
   c           IN VARCHAR2, 
   last_elem   IN boolean DEFAULT FALSE);
```

Parameters

Table 284-8 SET\* Procedure Parameters

| Parameter | Description |
| --- | --- |
| `self` | An `ANYDATA`. |
| `num` | The number, and associated information, that is to be set. |
| `last_elem` | Relevant only if `ANYDATA` represents a collection.  Set to `TRUE` if it is the last element of the collection, `FALSE` otherwise. |

Exceptions

- `DBMS_TYPES.INVALID_PARAMETERS`: Invalid Parameters (if it is not appropriate to add a number at this point in the creation process).
- `DBMS_TYPES.INCORRECT_USAGE`: Incorrect usage.
- `DBMS_TYPES.TYPE_MISMATCH`: When the expected type is different from the passed in type.

Usage Notes

When `BEGINCREATE` is called, construction has already begun in a piece-wise fashion. Subsequent calls to `SET*` will set the successive attribute values.

If the `ANYDATA` is a standalone collection, the `SET*` call will set the successive collection elements.