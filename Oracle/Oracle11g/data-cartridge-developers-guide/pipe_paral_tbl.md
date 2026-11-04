---
title: Using Pipelined and Parallel Table Functions
book: "Data Cartridge Developer's Guide"
doc_id: E10765-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/pipe_paral_tbl.htm
tags:
  - oracle
  - 11g
  - data-cartridge-developers-guide
---

## 13 Using Pipelined and Parallel Table Functions

This chapter describes table functions. It also explains the generic data types `ANYTYPE`, `ANYDATA`, and `ANYDATASET`, which are likely to be used with table functions.

This chapter contains these topics:

## Overview of Table Functions

Table functions are functions that produce a collection of rows (either a nested table or a varray) that can be queried like a physical database table. You use a table function like the name of a database table, in the `FROM` clause of a query.

A table function can take a collection of rows as input. An input collection parameter can be either a collection type or a `REF CURSOR`.

Execution of a table function can be parallelized, and returned rows can be streamed directly to the next process without intermediate staging. Rows from a collection returned by a table function can also be pipelined; this means that they are iteratively returned as they are produced, instead of being returned in a single batch after all processing of the table function's input is completed.

Streaming, pipelining, and parallel execution of table functions can improve performance in the followingmanner:

- By enabling multithreaded, concurrent execution of table functions
- By eliminating intermediate staging between processes
- By improving query response time: With non-pipelined table functions, the entire collection returned by a table function must be constructed and returned to the server before the query can return a single result row. Pipelining enables rows to be returned iteratively, as they are produced. This also reduces the memory that a table function requires, as the object cache does not have to materialize the entire collection.
- By iteratively providing result rows from the collection returned by a table function as the rows are produced instead of waiting until the entire collection is staged in tables or memory and then returning the entire collection

Figure 13-1 shows a typical data-processing scenario in which data goes through several (in this case, three) transformations, implemented by table functions, before finally being loaded into a database. In this scenario, the table functions are not parallelized, and the entire result collection must be staged after each transformation.

Figure 13-1 Typical Data Processing with Unparallelized, Unpipelined Table Functions

![Description of Figure 13-1 follows](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img/addci044.gif "Description of Figure 13-1 follows")  
[Description of "Figure 13-1 Typical Data Processing with Unparallelized, Unpipelined Table Functions"](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img_text/addci044.htm)  

By contrast, Figure 13-2 shows how streaming and parallel execution can streamline the same scenario.

Figure 13-2 Data Processing Using Pipelining and Parallel Execution

![Description of Figure 13-2 follows](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img/addci045.gif "Description of Figure 13-2 follows")  
[Description of "Figure 13-2 Data Processing Using Pipelining and Parallel Execution"](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img_text/addci045.htm)  

## Table Function Concepts

This section describes table functions and introduces some concepts related to pipelining and parallel execution of table functions.

### Table Functions

Table functions return a collection type instance and can be queried like a table by calling the function in the `FROM` clause of a query. Table functions use the `TABLE` keyword.

The following example shows a table function `GetBooks` that takes a `CLOB` as input and returns an instance of the collection type `BookSet_t`. The `CLOB` column stores a catalog listing of books in some format (either proprietary or following a standard such as XML). The table function returns all the catalogs and their corresponding book listings. The collection type `BookSet_t` is defined in Example 13-1.

Example 13-1 Creating a Collection Type

```
CREATE TYPE Book_t AS OBJECT
( name VARCHAR2(100),
  author VARCHAR2(30),
  abstract VARCHAR2(1000));

CREATE TYPE BookSet_t AS TABLE OF Book_t;
```

The `CLOB` s are stored in a table `Catalogs`, as demonstrated in Example 13-2.

Example 13-2 Storing a Clob in a Table

```
CREATE TABLE Catalogs
( name VARCHAR2(30), 
  cat CLOB);
```

Function `GetBooks()` is defined in Example 13-3.

Example 13-3 Creating a Function that Returns a Collection Type

```
CREATE FUNCTION GetBooks(a CLOB) RETURN BookSet_t;
```

The query in Example 13-4 returns all the catalogs and their corresponding book listings.

Example 13-4 Using a Collection Type in a Query

```
SELECT c.name, Book.name, Book.author, Book.abstract
  FROM Catalogs c, TABLE(GetBooks(c.cat)) Book;
```

### Pipelined Table Functions

Data is said to be pipelined if it is consumed by a consumer (transformation) as soon as the producer (transformation) produces it, without being staged in tables or a cache before being input to the next transformation.

Pipelining enables a table function to return rows faster and can reduce the memory required to cache a table function's results.

A pipelined table function can return the table function's result collection in subsets. The returned collection behaves like a stream that can be fetched from on demand. This makes it possible to use a table function like a virtual table.

Pipelined table functions can be implemented in two ways:

- In the native PL/SQL approach, the consumer and producers can run on separate execution threads (either in the same or different process context) and communicate through a pipe or queuing mechanism. This approach is similar to co-routine execution.
- In the interface approach, the consumer and producers run on the same execution thread. Producer explicitly returns the control back to the consumer after producing a set of results. In addition, the producer caches the current state so that it can resume where it left off when the consumer invokes it again.
	The interface approach requires you to implement a set of well-defined interfaces in a procedural language.

The co-routine execution model provides a simpler, native PL/SQL mechanism for implementing pipelined table functions, but this model cannot be used for table functions written in C or Java. The interface approach, on the other hand, can. The interface approach requires the producer to save the current state information in a context object before returning so that this state can be restored on the next invocation.

In the rest of this chapter, the term table function is used to refer to a pipelined table function— a table function that returns a collection in an iterative, pipelined way.

### Pipelined Table Functions with REF CURSOR Arguments

A pipelined table function can accept any argument that regular functions accept. A table function that accepts a `REF CURSOR` as an argument can serve as a transformation function. That is, it can use the `REF CURSOR` to fetch the input rows, perform some transformation on them, and then pipeline the results out (using either the interface approach or the native PL/SQL approach).

For example, the following code sketches the declarations that define a `StockPivot` function. This function converts a row of the type (`Ticker, OpenPrice, ClosePrice`) into two rows of the form (`Ticker, PriceType, Price`). Calling `StockPivot` for the row (`"ORCL", 41, 42`) generates two rows: (`"ORCL", "O", 41`) and (`"ORCL", "C", 42`).

Input data for the table function might come from a source such as table `StockTable`:

```
CREATE TABLE StockTable (
  ticker VARCHAR(4),
  openprice NUMBER,
  closeprice NUMBER
);
```

The declarations are in Example 13-5.

Example 13-5 Declaring a Pipelined Table Function with REF CURSOR Arguments

```
-- Create the types for the table function's output collection 
-- and collection elements

CREATE TYPE TickerType AS OBJECT 
(
  ticker VARCHAR2(4),
  PriceType VARCHAR2(1),
  price NUMBER
);

CREATE TYPE TickerTypeSet AS TABLE OF TickerType;

-- Define the ref cursor type

CREATE PACKAGE refcur_pkg IS
  TYPE refcur_t IS REF CURSOR RETURN StockTable%ROWTYPE;
END refcur_pkg;
/

-- Create the table function

CREATE FUNCTION StockPivot(p refcur_pkg.refcur_t) RETURN TickerTypeSet
PIPELINED ... ;
/
```

Example 13-6 uses the `StockPivot` table function.

Example 13-6 Using a Pipelined Table Function with REF CURSOR Arguments

```
SELECT * FROM TABLE(StockPivot(CURSOR(SELECT * FROM StockTable)));
```

In the preceding query, the pipelined table function `StockPivot` fetches rows from the `CURSOR` subquery `SELECT * FROM StockTable`, performs the transformation, and pipelines the results back to the user as a table. The function produces two output rows (collection elements) for each input row.

Note that when a `CURSOR` subquery is passed from SQL to a `REF CURSOR` function argument as in the preceding example, the referenced cursor is open when the function begins executing.

See Also:

[Chapter 17, "Pipelined Table Functions: Interface Approach Example"](pipelined_example.md) for a complete implementation of this table function using the interface approach, in both C and Java.

#### Errors and Restrictions

These cursor operations are not allowed for `REF CURSOR` variables based on table functions: `SELECT FOR UPDATE`, and `WHERE CURRENT OF`.

### Parallel Execution of Table Functions

With parallel execution of a function that appears in the `SELECT` list, execution of the function is pushed down to and conducted by multiple slave scan processes. These each execute the function on a segment of the function's input data.

For example, the query

```
SELECT f(col1) FROM tab;
```

is parallelized if `f` is a pure function. The SQL executed by a slave scan process is similar to:

```
SELECT f(col1) FROM tab WHERE ROWID BETWEEN :b1 AND :b2;
```

Each slave scan operates on a range of rowids and applies function `f` to each contained row. Function `f` is then executed by the scan processes; it does not run independently of them.

Unlike a function that appears in the `SELECT` list, a table function is called in the `FROM` clause and returns a collection. This affects the way that table function input data is partitioned among slave scans because the partitioning approach must be appropriate for the operation that the table function performs. (For example, an `ORDER BY` operation requires input to be range-partitioned, whereas a `GROUP BY` operation requires input to be hash partitioned.)

A table function itself specifies in its declaration the partitioning approach that is appropriate for it, as described in "Input Data Partitioning". The function is then executed in a two-stage operation. First, one set of slave processes partitions the data as directed in the function's declaration; then a second set of slave scans executes the table function in parallel on the partitioned data. The table function in the following query has a `REF CURSOR` parameter:

```
SELECT * FROM TABLE(f(CURSOR(SELECT * FROM tab)));
```

The scan is performed by one set of slave processes, which redistributes the rows (based on the partitioning method specified in the function declaration) to a second set of slave processes that actually executes function `f` in parallel.

## Pipelined Table Functions

This section discusses issues involved in implementing pipelined table functions.

### Implementation Choices for Pipelined Table Functions

As noted previously, two approaches are supported for implementing pipelined table functions: the interface approach and the PL/SQL approach.

The interface approach requires the user to supply a type that implements a predefined Oracle interface consisting of start, fetch, and close operations. The type is associated with the table function when the table function is created. During query execution, the `fetch` method is invoked repeatedly to iteratively retrieve the results. With the interface approach, the methods of the implementation type associated with the table function can be implemented in any of the supported internal or external languages (including PL/SQL, C/C++, and Java).

With the PL/SQL approach, a single PL/SQL function includes a special instruction to pipeline results (single elements of the collection) out of the function instead of returning the whole collection as a single value. The native PL/SQL approach is simpler to implement because it requires writing only one PL/SQL function.

The approach used to implement pipelined table functions does not affect the way they are used. Pipelined table functions are used in SQL statements in exactly the same way regardless of the approach used to implement them.

### Declarations of Pipelined Table Functions

You declare a pipelined table function by specifying the `PIPELINED` keyword. This keyword indicates that the function returns rows iteratively. The return type of the pipelined table function must be a collection type (a nested table or a varray).

Example 13-7 shows declarations of pipelined table functions implemented using the interface approach. The interface routines for functions `GetBooks` and `StockPivot` have been implemented in the types `BookMethods` and `StockPivotImpl`, respectively.

Example 13-7 Declaring Pipelined Table Functions for the Interface Approach

```
CREATE FUNCTION GetBooks(cat CLOB) RETURN BookSet_t PIPELINED USING BookMethods;

CREATE FUNCTION StockPivot(p refcur_pkg.refcur_t) 
  RETURN TickerTypeSet PIPELINED USING StockPivotImpl;
```

Example 13-8 shows declarations of the same table functions implemented using the native PL/SQL approach:

Example 13-8 Declaring Pipelined Table Functions for the Native PL/SQL Approach

```
CREATE FUNCTION GetBooks(cat CLOB) RETURN BookSet_t PIPELINED IS ...;

CREATE FUNCTION StockPivot(p refcur_pkg.refcur_t) RETURN TickerTypeSet
PIPELINED IS...;
```

### Implementing the Native PL/SQL Approach

In PL/SQL, the `PIPE ROW` statement causes a table function to pipe a row and continue processing. The statement enables a PL/SQL table function to return rows as soon as they are produced. This is demonstrated in Example 13-9. For performance reasons, the PL/SQL run-time system provides the rows to the consumer in batches.

Example 13-9 Implementing a Pipelined Table Function for the Native PL/SQL Approach

```
CREATE FUNCTION StockPivot(p refcur_pkg.refcur_t) RETURN TickerTypeSet
PIPELINED IS
  out_rec TickerType := TickerType(NULL,NULL,NULL);
  in_rec p%ROWTYPE;
BEGIN
  LOOP
    FETCH p INTO in_rec; 
    EXIT WHEN p%NOTFOUND;
    -- first row
    out_rec.ticker := in_rec.Ticker;
    out_rec.PriceType := 'O';
    out_rec.price := in_rec.OpenPrice;
    PIPE ROW(out_rec);
    -- second row
    out_rec.PriceType := 'C';   
    out_rec.Price := in_rec.ClosePrice;
    PIPE ROW(out_rec);
  END LOOP;
  CLOSE p;
  RETURN;
END;
/
```

In Example 13-9, the `PIPE ROW(out_rec)` statement pipelines data out of the PL/SQL table function.

The `PIPE ROW` statement may be used only in the body of pipelined table functions; an error is raised if it is used anywhere else. The `PIPE ROW` statement can be omitted for a pipelined table function that returns no rows.

A pipelined table function must have a `RETURN` statement that does not return a value. The `RETURN` statement transfers the control back to the consumer and ensures that the next fetch gets a `NO_DATA_FOUND` exception.

### Pipelining Between PL/SQL Table Functions

With serial execution, results are pipelined from one PL/SQL table function to another using an approach similar to co-routine execution. Example 13-10 pipelines results from function `g` to function `f`.

Example 13-10 Pipelining Function Results from One Function to Another

```
SELECT * FROM TABLE(f(CURSOR(SELECT * FROM TABLE(g()))));
```

Parallel execution works similarly, except that each function executes in a different process or set of processes.

### Combining PIPE ROW with AUTONOMOUS\_TRANSACTION

Because table functions pass control back and forth to a calling routine as rows are produced, there is a restriction on combining table functions and `PRAGMA AUTONOMOUS_TRANSACTION` s. If a table function is part of an autonomous transaction, it must `COMMIT` or `ROLLBACK` before each `PIPE ROW` statement, to avoid an error in the calling subprogram.

### Implementing the Interface Approach

To use the interface approach, you must define an implementation type that implements the `ODCITable` interface. This interface consists of start, fetch, and close routines whose signatures are specified by Oracle and which you implement as methods of the type.

Oracle invokes the methods to perform the following steps in the execution of a query that contains a table function:

1. Start by initializing the scan context parameter, using the [ODCITableStart()](pipe_paral_tbl_ref.md) function.
2. Fetch to produce a subset of the rows in the result collection. The [ODCITableFetch()](pipe_paral_tbl_ref.md) method is invoked as many times as necessary to return the entire collection.
3. Close and clean up (release memory and so on) using [ODCITableClose()](pipe_paral_tbl_ref.md) after the last [ODCITableFetch()](pipe_paral_tbl_ref.md).

The `ODCITable` interface also defines two optional routines, [ODCITablePrepare()](pipe_paral_tbl_ref.md) and [ODCITableDescribe()](pipe_paral_tbl_ref.md), that are invoked at compilation time:

- [ODCITableDescribe()](pipe_paral_tbl_ref.md) determines the structure of the data type the table function returns, in situations where this cannot be defined in a static manner.
- [ODCITablePrepare()](pipe_paral_tbl_ref.md) initializes the scan context parameter. If this method is implemented, the scan context it prepares is passed to the [ODCITableStart()](pipe_paral_tbl_ref.md) routine, and the context is maintained between restarts of the table function. It also provides projection information and supports the return of transient anonymous types.

#### Scan Context

For the fetch method to produce the next set of rows, a table function must be able to maintain context between successive invocations of the interface routines to fetch another set of rows. This context, called the scan context, is defined by the attributes of the implementation type. A table function preserves the scan context by modeling it in an object instance of the implementation type.

#### Start Routine

The start routine [ODCITableStart()](pipe_paral_tbl_ref.md) is the first routine that is invoked to begin retrieving rows from a table function. This routine typically performs the setup needed for the scan, creating the scan context (as an object instance `sctx`) and returning it to Oracle. However, if [ODCITablePrepare()](pipe_paral_tbl_ref.md) is implemented, it creates the scan context, which is then passed to the [ODCITableStart()](pipe_paral_tbl_ref.md) routine. The arguments to the table function, specified by the user in the `SELECT` statement, are passed in as parameters to this routine.

Note that any `REF CURSOR` arguments of a table function must be declared as `SYS_REFCURSOR` type in the declaration of the [ODCITableStart()](pipe_paral_tbl_ref.md). Ordinary `REF CURSOR` types cannot be used as formal argument types in [ODCITableStart()](pipe_paral_tbl_ref.md). Ordinary `REF CURSOR` types can only be declared in a package, and types defined in a package cannot be used as formal argument types in a type method. To use a `REF CURSOR` type in [ODCITableStart()](pipe_paral_tbl_ref.md), you must use the system-defined `SYS_REFCURSOR` type.

#### Fetch Routine

The fetch routine [ODCITableFetch()](pipe_paral_tbl_ref.md) is invoked one or more times by Oracle to retrieve all the rows in the table function's result set. The scan context is passed in as a parameter. This routine returns the next subset of one or more rows.

The fetch routine is called by Oracle repeatedly until all the rows have been returned by the table function. Returning more rows in each invocation of [ODCITableFetch()](pipe_paral_tbl_ref.md) reduces the number of fetch calls that must be made and thus improves performance. The table function should return a null collection to indicate that all rows have been returned.

The `nrows` parameter indicates the number of rows that are required to satisfy the current OCI call. For example, if the current OCI call is an [ODCITableFetch()](pipe_paral_tbl_ref.md) that requested `100` rows, and `20` rows have been returned, then the `nrows` parameter is equal to `80`. The fetch function is allowed to return a different number of rows. The main purpose of this parameter is to prevent [ODCITableFetch()](pipe_paral_tbl_ref.md) from returning more rows than actually required. If [ODCITableFetch()](pipe_paral_tbl_ref.md) returns more rows than the value of this parameter, the rows are cached and returned in subsequent [ODCITableFetch()](pipe_paral_tbl_ref.md) calls, or they are discarded if the OCI statement handle is closed before they are all fetched.

#### Close Routine

The close routine [ODCITableClose()](pipe_paral_tbl_ref.md) is invoked by Oracle after the last fetch invocation. The scan context is passed in as a parameter. This routine performs the necessary cleanup operations.

Figure 13-3 Flowchart of Table Function Row Source Execution

![Description of Figure 13-3 follows](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img/addci046.gif "Description of Figure 13-3 follows")  
[Description of "Figure 13-3 Flowchart of Table Function Row Source Execution"](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img_text/addci046.htm)  

#### Describe Method

Sometimes it is not possible to define the structure of the return type from the table function statically. If the shape of the rows is different in different queries, it may depend on the actual arguments with which the table function is invoked. Such table functions can be declared to return `AnyDataSet`. `AnyDataSet` is a generic collection type. It can be used to model any collection (of any element type) and has an associated set of APIs (both PL/SQL and C) that enable you to construct `AnyDataSet` instances and access the elements.

The following example shows a table function declared to return an `AnyDataSet` collection whose structure is not fixed at function creation time:

```
CREATE FUNCTION AnyDocuments(VARCHAR2) RETURN ANYDATASET 
PIPELINED USING DocumentMethods;
```

You can implement a [ODCITableDescribe()](pipe_paral_tbl_ref.md) routine to determine the format of the elements in the result collection when the format depends on the actual parameters to the table function. [ODCITableDescribe()](pipe_paral_tbl_ref.md) is invoked by Oracle at query compilation time to retrieve the specific type information. Typically, the routine uses the user arguments to determine the shape of the return rows. The format of elements in the returned collection is conveyed to Oracle by returning an instance of `AnyType`.

The `AnyType` instance specifies the actual structure of the returned rows of the specific query. Like `AnyDataSet`, `AnyType` has an associated set of PL/SQL and C interfaces with which to construct and access the metadata information.

See Also:

"Transient and Generic Types" for information on `AnyDataSet` and `AnyType`

The query in Example 13-11, for an `AnyDocuments` function, returns information on either books or magazines.

Example 13-11 Querying for AnyType Data

```
SELECT * FROM 
  TABLE(AnyDocuments('http://.../documents.xml')) x
  WHERE x.Abstract like '%internet%';
```

Example 13-12 is an implementation of the [ODCITableDescribe()](pipe_paral_tbl_ref.md) method, which consults the DTD of the XML documents at the specified location to return the appropriate `AnyType` value, either a book or a magazine. The `AnyType` instance is constructed by invoking the constructor APIs with the field name and data type information.

Example 13-12 Implementing the ODCITableDescribe() Method

```
CREATE TYPE Mag_t AS OBJECT
(   name VARCHAR2(100),
    publisher VARCHAR2(30),
    abstract VARCHAR2(1000)
);

STATIC FUNCTION ODCITableDescribe(rtype OUT ANYTYPE, 
                                        url VARCHAR2)
IS BEGIN    
    Contact specified web server and retrieve document...
    Check XML doc schema to determine if books or mags...
    IF books THEN
        rtype=AnyType.AnyTypeGetPersistent('SYS','BOOK_T');
    ELSE
        rtype=AnyType.AnyTypeGetPersistent('SYS','MAG_T');
    END IF;
END;
```

When Oracle invokes [ODCITableDescribe()](pipe_paral_tbl_ref.md), it uses the type information that is returned in the `AnyType` `OUT` argument to resolve references in the command line, such as the reference to the `x.Abstract` attribute in Example 13-12. This functionality is applicable only when the returned type is a named type, and therefore has named attributes.

Another feature of [ODCITableDescribe()](pipe_paral_tbl_ref.md) is its ability to describe `SELECT` list parameters, such as using OCI interfaces, when executing a `SELECT *` query. The information retrieved reflects one `SELECT` list item for each top-level attribute of the type returned by [ODCITableDescribe()](pipe_paral_tbl_ref.md).

Because the [ODCITableDescribe()](pipe_paral_tbl_ref.md) method is called at compile time, the table function should have at least one argument that has a value at compile time, like a constant. By using the table function with different arguments, you can get different return types from the function, as demonstrated in Example 13-13.

Example 13-13 Using Functions that Return AnyType

```
-- Issue a query for books
SELECT x.Name, x.Author
FROM TABLE(AnyDocuments('Books.xml')) x;

-- Issue a query for magazines
SELECT x.Name, x.Publisher
FROM TABLE(AnyDocuments('Magazines.xml')) x;
```

The [ODCITableDescribe()](pipe_paral_tbl_ref.md) functionality is available only if the table function is implemented using the interface approach. A native PL/SQL implementation of a table function that returns `ANYDATASET` returns rows whose structure is opaque to the server.

#### Prepare Method

[ODCITablePrepare()](pipe_paral_tbl_ref.md) is invoked at query compilation time. It generates and saves information to decrease the execution time of the query.

If you do not implement [ODCITablePrepare()](pipe_paral_tbl_ref.md), [ODCITableStart()](pipe_paral_tbl_ref.md) initializes the context each time it is called. However, if you do implement [ODCITablePrepare()](pipe_paral_tbl_ref.md), it initializes the scan context, which is passed to the [ODCITableStart()](pipe_paral_tbl_ref.md) when the query is executed, reducing startup time. In addition, when [ODCITablePrepare()](pipe_paral_tbl_ref.md) is implemented, [ODCITableClose()](pipe_paral_tbl_ref.md) is called only one time during the query, rather than each time the table function is restarted. This has the following benefits:

- It decreases execution time by reducing the number of calls to [ODCITableClose()](pipe_paral_tbl_ref.md).
- It allows the scan context to be maintained between table function restarts.

[ODCITablePrepare()](pipe_paral_tbl_ref.md) also provides projection information to the table function. If you do not implement [ODCITablePrepare()](pipe_paral_tbl_ref.md) for table functions that return collections of user-defined types (UDTs), your table function must set every attribute of the UDT of each element, because it has no way of knowing which attributes are used. In contrast, selecting from a regular table fetches only the required columns, which is naturally faster in most cases. However, if you do implement [ODCITablePrepare()](pipe_paral_tbl_ref.md), it can build an array of attribute positions, record the return type information in an argument of type `ODCITabFuncInfo`, and save this information in the scan context, as described in Example 13-14.

Example 13-14 Building an Array of Attribute Positions and Save it in a Scan Context

```
CREATE TYPE SYS.ODCITabFuncInto AS OBJECT (
  Attrs SYS.ODCINumberList,
  RetType SYS.AnyType
);
```

Implementing [ODCITablePrepare()](pipe_paral_tbl_ref.md) also allows your table function to return transient anonymous types. [ODCITablePrepare()](pipe_paral_tbl_ref.md) is called at the end of query compilation, so it can be passed the table descriptor object (TDO) built by the describe method. The describe method can build and return a transient anonymous TDO. Oracle transforms this TDO so that it can be used during query execution, and passes the transformed TDO to the prepare method in the `RetType` attribute. If the describe method returns a TDO for a type that is not anonymous, that TDO is identical to the transformed TDO. Thus, if a table function returns:

- A named collection type, the `RetType` attribute contains the TDO of this type.
- `AnyDataSet`, and the describe method returns a named type, the `RetType` attribute contains the TDO of the named type.
- `AnyDataSet`, and the describe method returns an anonymous type, Oracle transforms this type, and `RetType` contains the transformed TDO.

### Querying Table Functions

Pipelined table functions are used in the `FROM` clause of `SELECT` statements independently from implementation, either in native PL/SQL or through the interface approach. The result rows are retrieved by Oracle iteratively from the table function implementation, as demonstrated in Example 13-15.

Example 13-15 Using a Table Function to Iteratively Retrieve Rows

```
SELECT x.Ticker, x.Price 
FROM TABLE(StockPivot(CURSOR(SELECT * FROM StockTable))) x
WHERE x.PriceType='C';
```

#### Multiple Calls to Table Functions

Multiple invocations of a table function, either within the same query or in separate queries result in multiple executions of the underlying implementation. That is, in general, there is no buffering or reuse of rows, as demonstrated in Example 13-16.

Example 13-16 Using Multiple Invokations of a Table Function

```
SELECT * FROM TABLE(f(...)) t1, TABLE(f(...)) t2 
  WHERE t1.id = t2.id;
  
SELECT * FROM TABLE(f());

SELECT * FROM TABLE(f());
```

However, if the output of a table function is determined solely by the values passed into it as arguments, such that the function always produces exactly the same result value for each respective combination of values passed in, you can declare the function `DETERMINISTIC`, and Oracle automatically buffers rows for it. Note, though, that the database has no way of knowing whether a function marked `DETERMINISTIC` really is `DETERMINISTIC`, and if one is not, results are unpredictable.

#### PL/SQL

PL/SQL `REF CURSOR` variables can be defined for queries over table functions, as demonstrated in Example 13-17.

Example 13-17 Defining REF CURSOR Variables for Table Function Queries

```
OPEN c FOR SELECT * FROM TABLE(f(...));
```

Cursors over table functions have the same fetch semantics as ordinary cursors. `REF CURSOR` assignments based on table functions do not have special semantics.

However, the SQL optimizer does not optimize across PL/SQL statements; therefore, Example 13-19 runs better than Example 13-18.

Example 13-18 Using a REF CURSOR Variable

```
BEGIN
    OPEN r FOR SELECT * FROM TABLE(f(CURSOR(SELECT * FROM tab)));
    SELECT * BULK COLLECT INTO rec_tab FROM TABLE(g(r));
END;
```

Example 13-19 Using a REF CURSOR Variable More Effectively

```
SELECT * FROM TABLE(g(CURSOR(SELECT * FROM
  TABLE(f(CURSOR(SELECT * FROM tab))))));
```

Additionally, Example 13-18 is slower because of the overhead associated with executing two SQL statements, and because it does not take advantage of efficiencies realized by pipelining results between two functions, as Example 13-19 does.

### Performing DML Operations Inside Table Functions

A table function must be declared with the autonomous transaction pragma in order for the function to execute DML statements. This pragma causes the function to execute in an autonomous transaction not shared by other processes, as demonstrated in Example 13-20.

Example 13-20 Declaring a Table Function with Autonomous Transaction Pragma

```
CREATE FUNCTION f(p SYS_REFCURSOR) return CollType PIPELINED IS
    PRAGMA AUTONOMOUS_TRANSACTION; 
BEGIN ... END;
```

During parallel execution, each instance of the table function creates an independent transaction.

### Performing DML Operations on Table Functions

Table functions cannot be the target table in `UPDATE`, `INSERT`, or `DELETE` statements. For example, the following statements raise an error:

```
UPDATE F(CURSOR(SELECT * FROM tab)) SET col = value; 
INSERT INTO f(...) VALUES ('any', 'thing');
```

However, you can create a view over a table function and use `INSTEAD OF` triggers to update it, as in Example 13-21.

Example 13-21 Creating a View over a Table

```
CREATE VIEW BookTable AS 
  SELECT x.Name, x.Author
  FROM TABLE(GetBooks('data.txt')) x;
```

Example 13-22 demonstrates how an `INSTEAD OF` trigger is fired when the user inserts a row into the `BookTable` view:.

Example 13-22 How an INSTEAD OF Trigger is Fired when a Row is Inserted into a View

```
CREATE TRIGGER BookTable_insert
INSTEAD OF INSERT ON BookTable
REFERENCING NEW AS n
FOR EACH ROW
BEGIN
  ...
END;
INSERT INTO BookTable VALUES (...);
```

`INSTEAD OF` triggers can be defined for all DML operations on a view built on a table function.

### Handling Exceptions in Table Functions

Exception handling in table functions works just as it does with ordinary user-defined functions.

Some languages, such as C and Java, provide a mechanism for user-supplied exception handling. If an exception raised within a table function is handled, the table function executes the exception handler and continues processing. Exiting the exception handler takes control to the enclosing scope. If the exception is cleared, execution proceeds normally.

An unhandled exception in a table function causes the parent transaction to roll back.

## Parallel Table Functions

For a table function to be executed in parallel, it must have a partitioned input parameter. Parallelism is turned on for a table function if, and only if, both the following conditions are met:

- The function has a `PARALLEL_ENABLE` clause in its declaration.
- Exactly one `REF CURSOR` is specified with a `PARTITION BY` clause.
	If the `PARTITION BY` clause is not specified for any input `REF CURSOR` as part of the `PARALLEL_ENABLE` clause, the SQL compiler cannot determine how to partition the data correctly.

### Inputting Data with Cursor Variables

You can pass a set of rows to a PL/SQL function in a `REF CURSOR` parameter, as demonstrated in Example 13-23.

Example 13-23 Passing a Set of Rows to a PL/SQL Function in a REF CURSOR

```
FUNCTION f(p1 IN SYS_REFCURSOR) RETURN ... ;
```

Results of a subquery can be passed to a function directly, as demonstrated in Example 13-24. The `CURSOR` keyword is required to indicate that the results of a subquery should be passed as a `REF CURSOR` parameter.

Example 13-24 Directly Passing Results from a Subquery to a Function

```
SELECT * FROM TABLE(f(CURSOR(SELECT empno FROM tab)));
```

#### Using Multiple REF CURSOR Input Variables

PL/SQL functions can accept multiple `REF CURSOR` input variables, as demonstrated in Example 13-25.

Example 13-25 Passing a Set of Rows to a PL/SQL Function Through REF CURSOR

```
CREATE FUNCTION g(p1 pkg.refcur_t1, p2 pkg.refcur_t2) RETURN...
  PIPELINED ... ;
```

Function `g` can be invoked as demonstrated in Example 13-26.

Example 13-26 Invoking a Function that Uses Several REF CURSOR Parameters

```
SELECT * FROM TABLE(g(CURSOR(SELECT empno FROM tab),
  CURSOR(SELECT * FROM emp));
```

You can pass table function return values to other table functions by creating a `REF CURSOR` that iterates over the returned data, as demonstrated in Example 13-27.

Example 13-27 Using REF CURSOR to Pass Return Values Between Table Functions

```
SELECT * FROM TABLE(f(CURSOR(SELECT * FROM TABLE(g(...)))));
```

#### Explicitly Opening a REF CURSOR for a Query

You can explicitly open a `REF CURSOR` for a query and pass it as a parameter to a table function, as demonstrated in Example 13-28.

Example 13-28 Explicitly Using a Query REF CURSOR as Table Function Parameter

```
BEGIN
  OPEN r FOR SELECT * FROM TABLE(f(...));
  -- Must return a single row result set.
  SELECT * INTO rec FROM TABLE(g(r));
END;
```

#### PL/SQL REF CURSOR Arguments to Java and C/C++ Functions

Parallel and pipelined table functions may be written in C/C++, Java, or PL/SQL. Unlike PL/SQL, C/C++ and Java do not support the `REF CURSOR` type, but you can still pass a `REF CURSOR` argument to C/C++ and Java functions.

If a table function is implemented as a C callout, then an `IN REF CURSOR` argument passed to the callout is automatically available as an executed OCI statement handle. You can use this handle like any other executed statement handle.

A `REF CURSOR` argument to a callout passed as an `IN OUT` parameter is converted to an executed statement handle on the way in to the callout, and the statement handle is converted back to a `REF CURSOR` on the way out. (The inbound and outbound statement handles may be different.)

If a `REF CURSOR` type is used as an `OUT` argument or a return type to a callout, then the callout must return the statement handle, which are converted to a `REF CURSOR` for the caller, as demonstrated in Example 13-28.

Example 13-29 Using a REF CURSOR in a Callout

```
CREATE OR replace PACKAGE p1 AS 
  TYPE rc IS REF cursor; 
  END; 

CREATE OR REPLACE LIBRARY MYLIB AS 'mylib.so'; 

CREATE OR REPLACE FUNCTION MyCallout (stmthp p1.rc) 
  RETURN binary_integer AS LANGUAGE C LIBRARY MYLIB 
  WITH CONTEXT 
  PARAMETERS (context, stmthp ocirefcursor, RETURN sb4); 

sb4 MyCallout (OCIExtProcContext *ctx, OCIStmt ** stmthp) 
  OCIEnv *envhp;                /* env. handle */ 
  OCISvcCtx *svchp;             /* service handle */ 
  OCIError *errhp;              /* error handle */ 
  OCISession *usrhp;            /* user handle */ 

  int errnum = 29400;           /* choose some oracle error number */ 
  char errmsg[512];             /* error message buffer */ 
  size_t errmsglen;             /* Length of error message */ 
  OCIDefine *defn1p = (OCIDefine *) 0; 
  OCINumber *val=(OCINumber *)0; 

  OCINumber *rval = (OCINumber *)0; 
  sword status =  0; 
  double num=0; 
  val = (OCINumber*) OCIExtProcAllocCallMemory(ctx, sizeof(OCINumber)); 
  /* Get OCI handles */ 
  if (GetHandles(ctx, &envhp, &svchp, &errhp, &usrhp,&rval)) 
    return -1; 
  /* Define the fetch buffer */ 
  psdro_checkerr(NULL, errhp, OCIDefineByPos(*stmthp, &defn1p, errhp, (ub4) 1, 
                                            (dvoid *) &num, (sb4) sizeof(num), 
                                            SQLT_FLT, (dvoid *) 0, (ub2 *)0, 
                                            (ub2 *)0, (ub4) OCI_DEFAULT)); 

  /* Fetch loop */ 
  while ((status = OCIStmtFetch(*stmthp, errhp, (ub4) 1,  (ub4) OCI_FETCH_NEXT, 
                                (ub4) OCI_DEFAULT)) == OCI_SUCCESS || 
         status == OCI_SUCCESS_WITH_INFO) 
  { 
    printf("val=%lf\n",num); 
  } 
  return 0; 
}
```

If the function is written as a Java callout, the `IN REF CURSOR` argument is automatically converted to an instance of the Java `ResultSet` class. The `IN REF CURSOR` to `ResultSet` mapping is available only if you use a fat JDBC driver based on OCI. This mapping is not available for a thin JDBC driver. As with an executed statement handle in a C callout, when a `REF CURSOR` is either an `IN OUT` argument, an `OUT` argument, or a return type for the function, a Java `ResultSet` is converted back to a PL/SQL `REF CURSOR` on its way out to the caller.

A predefined weak `REF CURSOR` type, `SYS_REFCURSOR`, is also supported. With `SYS_REFCURSOR`, you do not have to first create a `REF CURSOR` type in a package before you can use it. This weak `REF CURSOR` type can be used in the [ODCITableStart()](pipe_paral_tbl_ref.md) method, which, as a type method, cannot accept a package type.

To use a strong `REF CURSOR` type, you still must create a PL/SQL package and declare a strong `REF CURSOR` type in it. Also, if you are using a strong `REF CURSOR` type as an argument to a table function, then the actual type of the `REF CURSOR` argument must match the column type, or an error is generated.

To partition a weak `REF CURSOR` argument, you must partition by `ANY`, because a weak `REF CURSOR` argument cannot be partitioned by `RANGE` or `HASH`. Oracle recommends that you not use weak `REF CURSOR` arguments to table functions.

### Input Data Partitioning

The table function declaration can specify data partitioning for exactly one `REF CURSOR` parameter, as demonstrated in Example 13-30. The `PARTITION BY` phrase in the `PARALLEL_ENABLE` clause specifies which one of the input cursors to partition, and what columns to use for partitioning.

Example 13-30 Specifying Data Partitioning for a REF CURSOR Parameter

```
CREATE FUNCTION f(p ref_cursor_type) RETURN rec_tab_type PIPELINED
  PARALLEL_ENABLE(PARTITION p BY [{HASH | RANGE} (column_list) | ANY ]) IS
BEGIN ... END;
```

When explicit column names are specified in the column list, the partitioning method can be `RANGE` or `HASH`. The input rows are hash- or range-partitioned on the specified columns.

The `ANY` keyword enables you to indicate that the function behavior is independent of the partitioning of the input data. When this keyword is used, the run-time system randomly partitions the data among the slaves. This keyword is appropriate for use with functions that take in one row, manipulate its columns, and generate output row(s) based on the columns of this row only.

For example, the pivot-like function `StockPivot()` in Example 13-31 takes as input a row of the type `(Ticker varchar(4), OpenPrice number, ClosePrice number)`, and generates rows of the type `(Ticker varchar(4), PriceType varchar(1), Price number)`. In this manner, the row (`"ORCL", 41, 42`) generates two rows (`"ORCL", "O", 41`) and (`"ORCL", "C", 42`).

Example 13-31 Implementing the StockPivot() Function

```
CREATE FUNCTION StockPivot(p refcur_pkg.refcur_t) RETURN rec_tab_type PIPELINED
    PARALLEL_ENABLE(PARTITION p BY ANY) IS
  ret_rec rec_type;
BEGIN
  FOR rec IN p LOOP
    ret_rec.Ticker := rec.Ticker;
    ret_rec.PriceType := "O";
    ret_rec.Price := rec.OpenPrice;
    PIPE ROW(ret_rec);

    ret_rec.Ticker := rec.Ticker;   -- Redundant; not required
    ret_rec.PriceType := "C";
    ret_rec.Price := rec.ClosePrice;
    PIPE ROW ret_rec;
  END LOOP;
  RETURN;
END;
```

The function `f()` can be used to generate another table from `Stocks` table, as shown in Example 13-32.

Example 13-32 Using a REF CURSOR to Generate a Table from Another Table

```
INSERT INTO AlternateStockTable
  SELECT * FROM 
  TABLE(StockPivot(CURSOR(SELECT * FROM StockTable)));
```

If `StockTable` is scanned in parallel and partitioned on `OpenPrice`, then the function `StockPivot()` is combined with the data-flow operator that scans `StockTable` and therefore sees the same partitioning.

If `StockTable` is not partitioned, and the scan on it does not execute in parallel, the insert into `AlternateStockTable` also runs sequentially, as demonstrated in Example 13-33.

Example 13-33 Using a REF CURSOR to Scan and Insert

```
CREATE FUNCTION g(p refcur_pkg.refcur_t) RETURN ... PIPELINED
  PARALLEL_ENABLE (PARTITION p BY ANY)
BEGIN 
  ... 
END;

INSERT INTO AlternateStockTable
  SELECT * FROM TABLE(f(CURSOR(SELECT * FROM Stocks))), TABLE(g(CURSOR( ... )))
    WHERE join_condition;
```

If function `g()` runs in parallel and is partitioned by `ANY`, then the parallel insert can belong in the same data-flow operator as `g()`.

Whenever the `ANY` keyword is specified, the data is partitioned randomly among the slaves. This effectively means that the function is executed in the same slave set which does the scan associated with the input parameter.

No redistribution or repartitioning of the data is required here. In the case when the cursor `p` itself is not parallelized, the incoming data is randomly partitioned on the columns in the column list. The round-robin table queue is used for this partitioning.

### Parallel Execution of Leaf-level Table Functions

To use parallel execution with a leaf-level table function, a function to perform a unitary operation that does not involve a `REF CURSOR`, there must be a requirements for a `REF CURSOR`.

Consider a function for reading a set of external files in parallel, and returning the records they contain. To provide work for a `REF CURSOR`, you might first create a table and populate it with the filenames. A `REF CURSOR` over this table can then be passed as a parameter to the table function `readfiles()`, as demonstrated by Example 13-34.

Example 13-34 Using a REF CURSOR to Read a Set of External FIles

```
CREATE TABLE filetab(filename VARCHAR(20));

INSERT INTO filetab VALUES('file0');   
INSERT INTO filetab VALUES('file1');  
...
INSERT INTO filetab VALUES('fileN');

SELECT * FROM TABLE(readfiles(CURSOR(SELECT filename FROM filetab)));

CREATE FUNCTION readfiles(p pkg.rc_t) RETURN coll_type
  PARALLEL_ENABLE(PARTITION p BY ANY) IS
  ret_rec rec_type;
BEGIN
  FOR rec IN p LOOP
    done := FALSE;
    WHILE (done = FALSE) LOOP
         done := readfilerecord(rec.filename, ret_rec);
         PIPE ROW(ret_rec);
    END LOOP;
  END LOOP;
  RETURN;
END;
```

## Input Data Streaming for Table Functions

Data streaming is the manner in which a table function orders or clusters rows that it fetches from cursor arguments. A function can stream its input data in any of the following ways:

- Place no restriction on the ordering of the incoming rows.
- Order them on a particular key column or columns.
- Cluster them on a particular key.

Clustering causes rows that have the same key values to appear next to one another, but it does not otherwise do any ordering of rows.

To control the behavior of the input stream, use the syntax in Example 13-35.

Example 13-35 Controlling Input Data Streaming

```
FUNCTION f(p ref_cursor_type) RETURN tab_rec_type [PIPELINED]
         {[ORDER | CLUSTER] BY column_list}
         PARALLEL_ENABLE({PARTITION p BY 
           [ANY | (HASH | RANGE) column_list]} )
IS
BEGIN 
  ...
END;
```

Input streaming may be specified for either sequential or parallel execution of a function.

If an `ORDER BY` or `CLUSTER BY` clause is not specified, rows are input in a random order. The semantics of `ORDER BY` are different for parallel execution from the semantics of the `ORDER BY` clause in a SQL statement. In a SQL statement, the `ORDER BY` clause globally orders the entire data set. In a table function, the `ORDER BY` clause orders the respective rows local to each instance of the table function running on a slave.

Example 13-36 illustrates the syntax for ordering the input stream. In the example, function `f()` takes in rows of the kind `(Region, Sales)` and returns rows of the form `(Region, AvgSales)`, showing average sales for each region.

Example 13-36 Ordering the Input Stream

```
CREATE FUNCTION f(p ref_cursor_type) RETURN tab_rec_type PIPELINED
  CLUSTER BY Region 
  PARALLEL_ENABLE(PARTITION p BY Region) IS
  ret_rec rec_type;
  cnt number;
  sum number;
BEGIN
  FOR rec IN p LOOP
    IF (first rec in the group) THEN
        cnt := 1;
        sum := rec.Sales;
    ELSIF (last rec in the group) THEN
      IF (cnt <> 0) THEN
        ret_rec.Region := rec.Region;
          ret_rec.AvgSales := sum/cnt;
          PIPE ROW(ret_rec);
        END IF;
    ELSE
       cnt := cnt + 1;
      sum := sum + rec.Sales;
    END IF;
  END LOOP;
  RETURN;
END;
```

### Parallel Execution: Partitioning and Clustering

Partitioning and clustering are easily confused, but they do different things. Sometimes partitioning can be sufficient without clustering in parallel execution.

Consider a function `SmallAggr` that performs in-memory aggregation of salary for each `department_id`, where `department_id` can be either `1`, `2`, or `3`. The input rows to the function can be partitioned by `HASH` on `department_id` so that all rows with `department_id` equal to `1` go to one slave, all rows with `department_id` equal to `2` go to another slave, and so on.

The input rows do not have to be clustered on `department_id` to perform the aggregation in the function. Each slave could have a `1` by `3` array `SmallSum[1..3]`, in which the aggregate sum for each `department_id` is added in memory into `SmallSum[department_id]`. On the other hand, if the number of unique values of `department_id` were very large, you would want to use clustering to compute department aggregates and write them to disk one `department_id` at a time.

## Creating Domain Indexes in Parallel

Creating a domain index can be a lengthy process because of the large amount of data that a domain index typically handles. You can exploit the parallel-processing capabilities of table functions to alleviate this bottleneck by using table functions to create domain indexes in parallel.

Typically, the [ODCIIndexCreate()](ext_idx_ref.md) routine performs the following steps:

1. Creates tables for storing the index data
2. Fetches the relevant data, such as `keycols` and `rowid`, from the base table, transforms it, and inserts relevant transformed data into the table created for storing the index data.
3. Builds secondary indexes on the tables that store the index data, for faster access at query time.

Step 2 is the bottleneck in creating domain indexes. You can speed up this step by encapsulating these operations in a parallel table function and invoking the function from the [ODCIIndexCreate()](ext_idx_ref.md) function. In Example 13-37, a table function `IndexLoad()` is defined to do just that.

Example 13-37 Loading a Domain Index in Parallel

```
CREATE FUNCTION IndexLoad(ia ODCIIndexInfo, parms VARCHAR2,
                          p refcur-type)
RETURN status_code_type
PARALLEL_ENABLE(PARTITION p BY ANY)  
PRAGMA AUTONOMOUS_TRANSACTION
IS
BEGIN
  FOR rec IN p LOOP
    - process each rec and determine the index entry
    - derive name of index storage table from parameter ia
    - insert into table created in ODCIIndexCreate
  END LOOP;
  COMMIT; -- explicitly commit the autonomous txn
  RETURN ODCIConst.Success;
END;
```

where `p` is a cursor of the form:

```
SELECT /*+ PARALLEL (base_table, par_degree) */ keycols ,rowid 
  FROM base_table
```

The `par_degree` value can be explicitly specified; otherwise, it is derived from the parallel degree of the base table.

The function `IndexMerge()`, defined in Example 13-38, is needed to merge the results from the several instances of `IndexLoad()`.

Example 13-38 Merging the Results from Parallel Domain Index Loads

```
CREATE FUNCTION IndexMerge(p refcur-type) 
RETURN NUMBER
IS
BEGIN
  FOR rec IN p LOOP
    IF (rec != ODCIConst.Success)
      RETURN Error;
  END LOOP;
  RETURN Success; 
END;
```

The new steps in [ODCIIndexCreate()](ext_idx_ref.md) would be:

1. Create metadata structures for the index (tables to store the index data).
2. Explicitly commit the transaction so that the `IndexLoad()` function can access the committed data.
3. Invoke `IndexLoad()` in parallel, as shown in Example 13-39.
	Example 13-39 Invoking the Merging of Parallel Domain Index Loads
	```
	status := ODCIIndexMerge(CURSOR(
	  SELECT * FROM TABLE(ODCIIndexLoad(ia, parms, CURSOR(
	    SELECT key_cols, ROWID FROM basetable)))))
	```
4. Create secondary index structures.

## Transient and Generic Types

Table 13-1 lists Oracle's three special SQL data types that enable you to dynamically encapsulate and access type descriptions, data instances, and sets of data instances of any other SQL type, including object and collection types. You can also use these three special types to create anonymous, or unnamed, types, including anonymous collection types.

The three SQL types are implemented as opaque types; the internal structure of these types is not known to the database: their data can be queried only by implementing functions, typically 3GL routines. Oracle provides both an OCI and a PL/SQL API for implementing such functions.

Table 13-1 Generic SQL Types

| Type | Description |
| --- | --- |
| `SYS.ANYTYPE` | A type description type. A `SYS.ANYTYPE` can contain a type description of any SQL type, named or unnamed, including object types and collection types.  An `ANYTYPE` can contain a type description of a persistent type, but an `ANYTYPE` itself is transient: the value in an `ANYTYPE` itself is not automatically stored in the database. To create a persistent type, use a `CREATE TYPE` statement from SQL. |
| `SYS.ANYDATA` | A self-describing data instance type. A `SYS.ANYDATA` contains an instance of a given type, with data, plus a description of the type. In this sense, a `SYS.ANYDATA` is self-describing. An `ANYDATA` can be persistently stored in the database. |
| `SYS.ANYDATASET` | A self-describing data set type. A `SYS.ANYDATASET` type contains a description of a given type plus a set of data instances of that type. An `ANYDATASET` can be persistently stored in the database. |

Each of these three types can be used with any built-in type native to the database with object types and collection types, both named and unnamed. The types provide a generic way to work dynamically with type descriptions, lone instances, and sets of instances of other types. Using the APIs, you can create a transient `ANYTYPE` description of any kind of type. Similarly, you can create or convert (cast) a data value of any SQL type to an `ANYDATA` and can convert an `ANYDATA` (back) to a SQL type. And similarly again with sets of values and `ANYDATASET`.

The generic types simplify working with stored procedures. You can use the generic types to encapsulate descriptions and data of standard types and pass the encapsulated information into parameters of the generic types. In the body of the procedure, you can detail how to handle the encapsulated data and type descriptions of whatever type.

You can also store encapsulated data of a variety of underlying types in one table column of type `ANYDATA` or `ANYDATASET`. For example, you can use `ANYDATA` with advanced queuing to model queues of heterogeneous types of data. You can query the data of the underlying data types like any other data.

Corresponding to the three generic SQL types are three OCI types that model them. Each has a set of functions for creating and accessing the respective type:

- `OCIType`, corresponding to `SYS.ANYTYPE`
- `OCIAnyData`, corresponding to `SYS.ANYDATA`
- `OCIAnyDataSet`, corresponding to `SYS.ANYDATASET`

See Also:

- [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/toc.htm) for the `OCIType`, `OCIAnyData`, and `OCIAnyDataSet` APIs and details on how to use them
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for information about the interfaces to the `ANYTYPE`, `ANYDATA`, and `ANYDATASET` types and about the `DBMS_TYPES` package, which defines constants for built-in and user-defined types, for use with `ANYTYPE`, `ANYDATA`, and `ANYDATASET`