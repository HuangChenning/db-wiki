---
title: Pipelined and Parallel Table Functions
book: "Data Cartridge Developer's Guide"
doc_id: E10765-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/pipe_paral_tbl_ref.htm
tags:
  - oracle
  - 11g
  - data-cartridge-developers-guide
---

## 23 Pipelined and Parallel Table Functions

This chapter describes the routines that must be implemented to define pipelined and parallel table functions in C.

This chapter contains this topic:

- Routines for Pipelined and Parallel Table Functions in C

See Also:

[Chapter 13](pipe_paral_tbl.md) for an overall explanation of pipelined and parallel table functions

## Routines for Pipelined and Parallel Table Functions in C

The following C methods, summarized in support parallel and pipelined table functions.

Table 23-1 Summary of Pipelined and Parallel Table Functions for C

| Function | Description |
| --- | --- |
| ODCITableClose() | Performs cleanup operations after scanning a table function. |
| ODCITableDescribe() | Returns describe information for a table function whose return type is `ANYDATASET`. |
| ODCITableFetch() | returns the next batch of rows from a table function. |
| ODCITablePrepare() | Prepares the scan context and other query information at compile time. |
| ODCITableStart() | initializes the scan of a table function. |

### ODCITableClose()

`ODCITableClose` performs cleanup operations after scanning a table function.

Syntax

```
MEMBER FUNCTION ODCITableClose(
   self IN <imptype>) 
RETURN NUMBER;
```

| Parameter | In/Out | Description |
| --- | --- | --- |
| ``` self ``` | ``` IN ``` | The scan context set up by previous scan routine invocation |

Returns

`ODCIConst.Success` on success, `ODCIConst.Error` otherwise.

Usage Notes

- Oracle invokes `ODCITableClose` after the last fetch call. The scan context is passed in as a parameter. `ODCITableClose` then performs any necessary cleanup operations, such as freeing memory.
- If ODCITablePrepare is implemented, this routine is only called one time, at the end of query execution, rather than each time the table function exits.

### ODCITableDescribe()

`ODCITableDescribe` returns describe information for a table function whose return type is `ANYDATASET`.

Syntax

```
STATIC FUNCTION ODCITableDescribe(
   rtype OUT ANYTYPE, 
   <args>) 
RETURN NUMBER;
```

| Parameter | In/Out | Description |
| --- | --- | --- |
| ``` rtype ``` | ``` OUT ``` | The `AnyType` value that describes the returned rows from the table function |
| ``` args ``` | ``` IN ``` | The set of zero or more user specified arguments for the table function. |

Returns

`ODCIConst.Success` on success, `ODCIConst.Error` otherwise.

Usage Notes

- If the optional routine `ODCITableDescribe` is implemented, Oracle invokes it at query compilation time to retrieve the specific type information.
- This interface is applicable only for table functions whose return type is `ANYDATASET`. The format of elements within the returned collection is conveyed to Oracle by returning an instance of `ANYTYPE`. The `ANYTYPE` instance specifies the actual structure of the returned rows of the specific query.
- `ANYTYPE` provides a data type to model the metadata of a row: the names and data types of all the columns (fields) comprising the row. It also provides a set of PL/SQL and C interfaces for users to construct and access the metadata information. `ANYDATASET`, like `ANYTYPE`, contains a description of a given type, but `ANYDATASET` also contains a set of data instances of that type
- The following example shows a query on a table function that uses the `ANYDATASET` type:
	```
	SELECT * FROM 
	TABLE(CAST(AnyBooks('http://.../books.xml') AS ANYDATASET));
	```
	At query compilation time, Oracle invokes the `ODCITableDescribe` routine. The routine typically uses the user arguments to figure out the nature of the return rows. In this example, `ODCITableDescribe` consults the DTD of the XML documents at the specified location to determine the appropriate `ANYTYPE` value to return. Each `ANYTYPE` instance is constructed by invoking the constructor APIs with this field name and data type information.
- Any arguments of the table function that are not constants are passed to `ODCITableDescribe` as `NULL` s because their values are not known at compile time.

See Also:

Section ["Transient and Generic Types"](pipe_paral_tbl.md) for a discussion of `ANYTYPE`, `ANYDATA`, and `ANYDATASET`

### ODCITableFetch()

`ODCITableFetch` returns the next batch of rows from a table function.

Syntax

```
MEMBER FUNCTION ODCITableFetch(
   self IN OUT <imptype>, 
   nrows IN NUMBER, 
   rws OUT <coll-type>) 
RETURN NUMBER;
```

| Parameter | In/Out | Description |
| --- | --- | --- |
| ``` self ``` | ``` IN OUT ``` | The in-bound is the scan context set up by previous scan routine invocation; the outbound is the scan context to be passed to later scan routine invocations. |
| ``` nrows ``` | ``` IN ``` | The number of rows the system expects in the current fetch cycle. The method can ignore this value and return a different number of rows. If fewer rows are returned, the method is called again; if more rows are returned, they are processed in the next cycle. |
| ``` rws ``` | ``` OUT ``` | The next batch of rows from the table function. This is returned as an instance of the same collection type as the return type of the table function. |

Returns

`ODCIConst.Success` on success, `ODCIConst.Error` otherwise.

Usage Notes

- `ODCITableFetch` is invoked one or more times by Oracle to retrieve all the rows in the collection returned by the table function. The scan context is passed in as a parameter. Typically `ODCITableFetch` uses the input scan context and computes the next set of rows to be returned to Oracle. In addition, it may update the scan context accordingly.
- Returning more rows in each invocation of `fetch()` reduces the number of fetch calls that must be made and thus improves performance.
- Oracle calls `ODCITableFetch` repeatedly until all rows in the table function's collection have been returned. When all rows have been returned, `ODCITableFetch` should return a null collection.

### ODCITablePrepare()

Prepares the scan context and other query information at compile time.

Syntax

```
STATIC FUNCTION ODCITablePrepare(
   sctx OUT <imptype>, 
   tf_info SYS.ODCITabFuncInfo,
   args);
```

| Parameter | In/Out | Description |
| --- | --- | --- |
| ``` sctx ``` | ``` OUT ``` | The scan context returned by this routine. This value is passed in as a parameter to the later scan routines. The scan context is an instance of the object type containing the implementation of the `ODCITable` routines. |
| ``` tf_info ``` |  | Contains the projection information and the return type's table descriptor object (TDO): - Attrs (`SYS.ODCINumberList`): lists the positions of the referenced attributes of the table function's output collection type - RefType (`SYS.AnyType`): for `AnyDataSet` table functions, this is the actual return type expected to be returned in the `AnyDataSet` collection. |
| ``` args ``` | ``` IN ``` | The arguments that are passed to the table function. This method is invoked at compile time; thus, only literal arguments have values. Column and expression arguments are passed as null values. |

Usage Notes

- This method prepares the scan context based on the information known at compile time. This scan context is passed to `ODCITableStart` when it is called at the beginning of query execution.
- If this optional method is implemented, `ODCITableClose` is only called one time, at the end of query execution. Each time the table function is restarted, `ODCITableStart` is called and passed the scan context. This allows the table function to maintain context between restarts, and to perform cleanup operations only one time at the end of query execution.

### ODCITableStart()

`ODCITableStart` initializes the scan of a table function.

Syntax

```
STATIC FUNCTION ODCITableStart(
   sctx IN OUT <imptype>, 
   <args>) 
RETURN NUMBER;
```

| Parameter | In/Out | Description |
| --- | --- | --- |
| ``` self ``` | ``` IN OUT ``` | The scan context returned by this routine. This value is passed in as a parameter to the later scan routines. The scan context is an instance of the object type containing the implementation of the `ODCITable` routines. If `ODCITablePrepare` is implemented, the scan context it creates is passed in to `ODCITableStart`. |
| ``` args ``` | ``` IN ``` | Set of zero or more arguments specified by the user for the table function |
| ``` rws ``` | ``` OUT ``` | The next batch of rows from the table function. This is returned as an instance of the same collection type as the return type of the table function. |

Returns

`ODCIConst.Success` on success, `ODCIConst.Error` otherwise.

Usage Notes

- If `ODCITablePrepare` is not implemented, this is the first routine that is invoked to begin retrieving rows from a table function. This routine typically performs the setup needed for the scan. The scan context is created (as an object instance `sctx`) and returned to Oracle. The arguments to the table function, specified by the user in the `SELECT` statement, are passed in as parameters to this routine. If `ODCITablePrepare` is implemented, it creates the scan context at compile time, and that scan context is passed in to this routine.
- Any `REF CURSOR` arguments of the table function must be declared as `SYS_REFCURSOR` type in the declaration of the `ODCITableStart` method.