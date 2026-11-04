---
title: Working with Multimedia Data Types
book: "Data Cartridge Developer's Guide"
doc_id: E10765-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/lobs.htm
tags:
  - oracle
  - 11g
  - data-cartridge-developers-guide
---

## 6 Working with Multimedia Data Types

This chapter describes how to work with multimedia data types, which are represented in Oracle Database as Large Objects (LOBs). The discussion provides a brief theoretical overview of LOB types, and then focuses on their practical use, through PL/SQ and OCI implementation for Data Cartridges.

This chapter contains these topics:

## Overview of Cartridges and Multimedia Data Types

Some data cartridges must handle large amounts of raw binary data, such as graphic images or sound waveforms, or character data, such as text or streams of numbers. Oracle supports large objects, `LOB` s, to handle these kinds of data.

- Internal LOBs are stored in the database tablespaces in a way that optimizes space and provides efficient access. Internal `LOB` s participate in the transactional model of the server.
	Internal `LOBs` can store binary data (`BLOB` s), single-byte character data (`CLOB` s), or fixed-width single-byte or multibyte character data (`NCLOB` s). An `NCLOB` consists of character data that corresponds to the national character set defined for the Oracle database. Varying width character data is not supported in Oracle.
- External `LOBs` are stored in operating system files outside the database tablespaces as `BFILE` s, binary data. They cannot participate in transactions.

Both internal `LOB` s and in `BFILE` s provide considerable flexibility in handling large amounts of data.

Data stored in a `LOB` is called the `LOB` 's value. To the Oracle server, a `LOB` 's value is unstructured and cannot be queried. You must unpack and interpret a `LOB` 's value in cartridge-specific ways.

`LOB` s can be manipulated using the Oracle Call Interface, OCI, or the PL/SQL `DBMS_LOB` package. You can write functions, including methods on object types that can contain `LOB` s, to manipulate parts of `LOB` s.

See Also:

[Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e18294/toc.htm). for details on `LOBs`

## DDL for LOBs

LOB definition can involve the `CREATE` `TYPE` and the `CREATE` `TABLE` statements. Example 6-1 specifies a `CLOB` within a data type named `lob_type`.

Example 6-1 Creating a CLOB Attribute of a Type

```
CREATE OR REPLACE TYPE lob_type AS OBJECT ( 
  id  INTEGER, 
  data CLOB );
```

Example 6-2 creates an object table, `lob_table`, in which each row is an instance of `lob_type` data:

Example 6-2 Creating a LOB Object Table

```
CREATE TABLE lob_table OF lob_type;
```

Example 6-3 shows how to store `LOBs` in a regular table, as opposed to an object table as in Example 6-2.

Example 6-3 Creating LOB Columns in a Table

```
CREATE TABLE lob_table1  (
  id  INTEGER,
  b_lob   BLOB,
  c_lob   CLOB,
  nc_lob  NCLOB,
  b_file  BFILE );
```

When creating LOBs in tables, you can set the LOB storage, buffering, and caching properties.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) manual and the [Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e18294/toc.htm) for information about using LOBs in `CREATE TABLE`, `ALTER TABLE`, `CREATE TYPE` and `ALTER TYPE` statements

## LOB Locators

`LOBs` can be stored with other row data or separate from row data. Regardless of the storage location, each `LOB` has a locator, which can be viewed as a handle or pointer to the actual location. Selecting a `LOB` returns the `LOB` locator instead of the `LOB` value.

Example 6-4 selects the `LOB` locator for `b_lob` and places it a PL/SQL local variable named `image1`.

Example 6-4 Selecting a LOB Locator and Assigning it to a Local Variable

```
DECLARE
       image1  BLOB;
       image_no  INTEGER := 101;
BEGIN
       SELECT b_lob  INTO image1 FROM lob_table
                  WHERE key_value = image_no;
             ...
END;
```

When you use an API function to manipulate the `LOB` value, you refer to the `LOB` using the locator. The PL/SQL `DBMS_LOB` package contains useful routines to manipulate `LOBs`, such as `PUT_LINE()` and `GETLENGTH()`, as in Example 6-5.

Example 6-5 Manipulating LOBs with PUT\_LINE() and GETLENGTH()

```
BEGIN
     DBMS_OUTPUT.PUT_LINE('Size of the Image is: ', 
                       DBMS_LOB.GETLENGTH(image1));
END;
```

In the OCI, `LOB` locators are mapped to `LOBLocatorPointers`, such as `OCILobLocator *`.

The OCI `LOB` interface and the PL/SQL `DBMS_LOB` package are described briefly in this chapter.

For a `BFILE`, the `LOB` column has its own distinct locator, which refers to the `LOB's` value that is stored in an external file in the server's file system. This implies that two rows in a table with a `BFILE` column may refer to the same file or two distinct files. A `BFILE` locator variable in a PL/SQL or OCI program behaves like any other automatic variable. With respect to file operations, it behaves like a file descriptor available as part of the standard I/O library of most conventional programming languages.

See Also:

- [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/toc.htm)
- [Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e18294/toc.htm). for `DBMS_LOB` API

## EMPTY\_BLOB and EMPTY\_CLOB Functions

You can use the special functions `EMPTY_BLOB` and EMPTY\_CLOB in `INSERT` or `UPDATE` statements of SQL DML to initialize a `NULL` or non- `NULL` internal `LOB` to empty. These are available as special functions in Oracle SQL DML, and are not part of the `DBMS_LOB` package.

Before you can start writing data to an internal `LOB` using OCI or the `DBMS_LOB` package, the `LOB` column must be made non-null, that is, it must contain a locator that points to an empty or populated `LOB` value. You can initialize a `BLOB` column's value to empty by using the function `EMPTY_BLOB` in the `VALUES` clause of an `INSERT` statement. Similarly, a `CLOB` or `NCLOB` column's value can be initialized by using the function `EMPTY_CLOB`. The syntax of the functions is demonstrated in.

Example 6-6 Syntax of EMPTY\_CLOB() and EMPTY\_CLOB() Functions

```
FUNCTION EMPTY_BLOB() RETURN BLOB;
FUNCTION EMPTY_CLOB() RETURN CLOB;
```

`EMPTY_BLOB` returns an empty locator of type `BLOB` and `EMPTY_CLOB` returns an empty locator of type `CLOB`, which can also be used for `NCLOBs`. The functions don't have an associated pragma.

An exception is raised if you use these functions anywhere but in the `VALUES` clause of a SQL `INSERT` statement or as the source of the `SET` clause in a SQL `UPDATE` statement.

Example 6-7 shows `EMPTY_BLOB()` used with SQL DML.

Example 6-7 Using EMPTY\_BLOB() with SQL DML

```
INSERT INTO lob_table VALUES (1001, EMPTY_BLOB(), 'abcde', NULL);
UPDATE lob_table SET c_lob = EMPTY_CLOB() WHERE key_value = 1001;
INSERT INTO lob_table VALUES (1002, NULL, NULL, NULL);
```

Example 6-8 shows how to use `EMPTY_CLOB()` in PL/SQL programs.

Example 6-8 Using EMPTY\_CLOB() in PL/SQL Programs

```
DECLARE 
  lobb         CLOB; 
  read_offset  INTEGER; 
  read_amount  INTEGER; 
  rawbuf       RAW(20); 
  charbuf      VARCHAR2(20);
BEGIN
  read_amount := 10; read_offset := 1;
  UPDATE lob_table SET c_lob = EMPTY_CLOB() 
  WHERE key_value = 1002 RETURNING c_lob INTO lobb;
  dbms_lob.read(lobb, read_amount, read_offset, charbuf); 
  dbms_output.put_line('lobb value: ' || charbuf);
END
```

## Using the OCI to Manipulate LOBs

The OCI includes functions that enable access to data stored in `BLOB` s, `CLOB` s, `NCLOB` s, and `BFILE` s. These functions are introduced in Table 6-1.

See Also:

[Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/toc.htm). for detailed documentation, including parameters, parameter types, return values, and example code

Table 6-1 Summary of OCI Functions for Manipulating LOBs

| Function | Description |
| --- | --- |
| ``` OCILobAppend() ``` | Appends `LOB` value to another `LOB`. |
| ``` OCILobAssign() ``` | Assigns one `LOB` locator to another. |
| ``` OCILobCharSetForm() ``` | Returns the character set form of a `LOB`. |
| ``` OCILobCharSetId() ``` | Returns the character set ID of a `LOB`. |
| ``` OCILobCopy() ``` | Copies a portion of a `LOB` into another `LOB`. |
| ``` OCILobDisableBuffering() ``` | Disables the buffering subsystem use. |
| ``` OCILobEnableBuffering() ``` | Uses the `LOB` buffering subsystem for subsequent read and write operations of `LOB` data. |
| ``` OCILobErase() ``` | Erases part of a `LOB`, starting at a specified offset. |
| ``` OCILobFileClose() ``` | Closes an open `BFILE`. |
| ``` OCILobFileCloseAll() ``` | Closes all open `BFILEs`. |
| ``` OCILobFileExists() ``` | Tests to see if a `BFILE` exists. |
| ``` OCILobFileGetName() ``` | Returns the name of a `BFILE`. |
| ``` OCILobFileIsOpen() ``` | Tests to see if a `BFILE` is open. |
| ``` OCILobFileOpen() ``` | Opens a `BFILE`. |
| ``` OCILobFileSetName() ``` | Sets the name of a `BFILE` in a locator. |
| ``` OCILobFlushBuffer() ``` | Flushes changes made to the `LOB` buffering subsystem to the database (server) |
| ``` OCILobGetLength() ``` | Returns the length of a `LOB` or a `BFILE`. |
| ``` OCILobIsEqual() ``` | Tests to see if two `LOB` locators refer to the same `LOB`. |
| ``` OCILobLoadFromFile() ``` | Loads `BFILE` data into an internal `LOB`. |
| ``` OCILobLocatorIsInit() ``` | Tests to see if a `LOB` locator is initialized. |
| ``` OCILobLocatorSize() ``` | Returns the size of a `LOB` locator. |
| ``` OCILobRead() ``` | Reads a specified portion of a non-null `LOB` or a `BFILE` into a buffer. |
| ``` OCILobTrim() ``` | Truncates a `LOB`. |
| ``` OCILobWrite() ``` | Writes data from a buffer into a `LOB`, writing over existing data. |

Table 6-2 compares the OCI and PL/SQL (`DBMS_LOB` package) interfaces in terms of `LOB` access.

Table 6-2 OCI and PL/SQL (DBMS\_LOB) Interfaces Compared

| OCI (ociap.h) | PL/SQL DBMS\_LOB (dbmslob.sql) |
| --- | --- |
| N/A | ``` DBMS_LOB.COMPARE() ``` |
| N/A | ``` DBMS_LOB.INSTR() ``` |
| N/A | ``` DBMS_LOB.SUBSTR() ``` |
| ``` OCILobAppend() ``` | ``` DBMS_LOB.APPEND() ``` |
| ``` OCILobAssign() ``` | N/A \[use PL/SQL assign operator\] |
| ``` OCILobCharSetForm() ``` | N/A |
| ``` OCILobCharSetId() ``` | N/A |
| ``` OCILobCopy() ``` | ``` DBMS_LOB.COPY() ``` |
| ``` OCILobDisableBuffering() ``` | N/A |
| ``` OCILobEnableBuffering() ``` | N/A |
| ``` OCILobErase() ``` | ``` DBMS_LOB.ERASE() ``` |
| ``` OCILobFileClose() ``` | ``` DBMS_LOB.FILECLOSE() ``` |
| ``` OCILobFileCloseAll() ``` | ``` DBMS_LOB.FILECLOSEALL() ``` |
| ``` OCILobFileExists() ``` | ``` DBMS_LOB.FILEEXISTS() ``` |
| ``` OCILobFileGetName() ``` | ``` DBMS_LOB.FILEGETNAME() ``` |
| ``` OCILobFileIsOpen() ``` | ``` DBMS_LOB.FILEISOPEN() ``` |
| ``` OCILobFileOpen() ``` | ``` DBMS_LOB.FILEOPEN() ``` |
| ``` OCILobFileSetName() ``` | N/A (use `BFILENAME` operator) |
| ``` OCILobFlushBuffer() ``` | N/A |
| ``` OCILobGetLength() ``` | ``` DBMS_LOB.GETLENGTH() ``` |
| ``` OCILobIsEqual() ``` | N/A \[use PL/SQL equal operator\] |
| ``` OCILobLoadFromFile ``` | ``` DBMS_LOB.LOADFROMFILE() ``` |
| ``` OCILobLocatorIsInit ``` | N/A \[always initialize\] |
| ``` OCILobRead ``` | ``` DBMS_LOB.READ() ``` |
| ``` OCILobTrim ``` | ``` DBMS_LOB.TRIM() ``` |
| ``` OCILobWrite ``` | ``` DBMS_LOB.WRITE() ``` |

Example 6-9 shows how to select a `LOB` from the database into a locator. It assumes that the type `lob_type` has two attributes, `id` of type `INTEGER` and `data` of type `CLOB`, and that a table, `lob_table`, of type `lob_type`, exists.

Example 6-9 Selecting a LOB from the Database into a Locator

```
/*-----------------------------------------------------------------------*/ 
/* Select lob locators from a CLOB column                                */ 
/* Use the 'FOR UPDATE' clause for writing to the LOBs.                  */ 
/*-----------------------------------------------------------------------*/ 
static OCIEnv        *envhp;
static OCIServer     *srvhp;
static OCISvcCtx     *svchp;
static OCIError      *errhp;
static OCISession    *authp;
static OCIStmt       *stmthp;
static OCIDefine     *defnp1;
static OCIBind       *bndhp;
 
sb4 select_locator(int rowind) 
{ 
  sword retval; 
  boolean flag; 
  int colc = rowind; 
  OCILobLocator *clob;
  text  *sqlstmt = (text *)"SELECT DATA FROM LOB_TABLE WHERE ID = :1 FOR UPDATE"; 

  if (OCIStmtPrepare(stmthp, errhp, sqlstmt, (ub4) strlen((char *)sqlstmt), 
      (ub4) OCI_NTV_SYNTAX, (ub4) OCI_DEFAULT)) 
  { 
    (void) printf("FAILED: OCIStmtPrepare() sqlstmt\n"); 
    return OCI_ERROR; 
  } 

  if (OCIStmtBindByPos(stmthp, bndhp, errhp, (ub4) 1, (dvoid *) &colc, 
      (sb4) sizeof(colc), SQLT_INT, (dvoid *) 0, (ub2 *)0, (ub2 *)0, (ub4) 0, 
      (ub4 *) 0, (ub4) OCI_DEFAULT)) 
  {
    (void) printf("FAILED: OCIStmtBindByPos()\n"); 
    return OCI_ERROR; 
  }
  
  if (OCIDefineByPos(stmthp, &defnp1, errhp, (ub4) 1, (dvoid *) &clob, (sb4) -1,
      (ub2) SQLT_CLOB, (dvoid *) 0, (ub2 *) 0, (ub2 *) 0, (ub4) OCI_DEFAULT)) 
  { 
    (void) printf("FAILED: OCIDefineByPos()\n"); 
    return OCI_ERROR; 
  } 

  /* Execute the select and fetch one row */ 
  if (OCIStmtExecute(svchp, stmthp, errhp, (ub4) 1, (ub4) 0, 
      (CONST OCISnapshot*) 0, (OCISnapshot*) 0, (ub4) OCI_DEFAULT)) 
  { 
    (void) printf("FAILED: OCIStmtExecute() sqlstmt\n"); 
    report_error(); 
    return OCI_ERROR; 
  } 
 
  /* Now test to see if the LOB locator is initialized */ 
  retval = OCILobLocatorIsInit(envhp, errhp, clob, &flag); 
  if ((retval != OCI_SUCCESS) && (retval != OCI_SUCCESS_WITH_INFO)) 
  { 
    (void) printf("Select_Locator --ERROR: OCILobLocatorIsInit(), 
        retval = %d\n", retval); 
    report_error(); 
    checkerr(errhp, retval); 
    return OCI_ERROR; 
  } 

  if (!flag) 
  { 
    (void) printf("Select_Locator --ERROR: LOB Locator is not initialized.\n"); 
    return OCI_ERROR;  
  } 

  return OCI_SUCCESS; 
}
```

A sample program, `populate.c`, uses the OCI to populate a `CLOB` with the contents of a file is included on the disk.

## Using DBMS\_LOB to Manipulate LOBs

The `DBMS_LOB` package can be used to manipulate `LOBs` from PL/SQL. Table 6-3 introduces its routines.

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_lob.htm#ARPLS600) provides full details on using the routines of the `DBMS_LOB` package.

Table 6-3 Summary of DBMS\_LOB Package Routines

| Routine | Description |
| --- | --- |
| ``` APPEND() ``` | Appends the contents of the source `LOB` to the destination `LOB`. |
| ``` COPY() ``` | Copies all or part of the source `LOB` to the destination `LOB`. |
| ``` ERASE() ``` | Erases all or part of a `LOB`. |
| ``` LOADFROMFILE() ``` | Loads `BFILE` data into an internal `LOB`. |
| ``` TRIM() ``` | Trims the `LOB` value to the specified shorter length. |
| ``` WRITE() ``` | Write data to the `LOB` from a specified offsets |
| ``` GETLENGTH ``` | Gets the length of the `LOB` value. |
| ``` INSTR() ``` | Return the matching position of the n <sup>th</sup> occurrence of the pattern in the `LOB`. |
| ``` READ() ``` | Reads data from the `LOB` starting at the specified offset |
| ``` SUBSTR() ``` | Returns part of the `LOB` value starting at the specified offset. |
| ``` FILECLOSE() ``` | Closes the file. |
| ``` FILECLOSEALL() ``` | Closes all previously opened files. |
| ``` FILEEXISTS() ``` | Tests if the file exists on the server. |
| ``` FILEGETNAME() ``` | Gets the directory alias and file name. |
| ``` FILEISOPEN() ``` | Tests the file was opened using the input `BFILE` locators. |
| ``` FILEOPEN() ``` | Opens a file. |

Example 6-10 calls the `TRIM` procedure to trim a `CLOB` value to a smaller length. It assumes that the type `lob_type` has two attributes, `id` of type `INTEGER` and `data` of type `CLOB`, and that a table, `lob_table`, of type `lob_type`, exists. Because this example deals with `CLOB` data, the second argument to `DBMS_LOB`.`TRIM`, the literal `834004`, specifies the number of characters. If the example dealt with `BLOB` data, this argument would be interpreted as a number of bytes.

Example 6-10 Trimming a CLOB

```
PROCEDURE Trim_Clob IS
        clob_loc  CLOB;
BEGIN
 -- get the LOB Locator
       SELECT data into clob_loc  FROM lob_table
       WHERE id  =  179 FOR UPDATE;
   -- call the TRIM Routine
       DBMS_LOB.TRIM(clob_loc, 834004);
       COMMIT;
END;
```

## LOBs in External Procedures

LOB locators can be passed as arguments to an external procedure, as defined in Example 6-1.

Example 6-11 Defining a PL/SQL External Procedure

```
FUNCTION DS_Findmin(data CLOB) RETURN PLS_INTEGER IS EXTERNAL 
                   NAME "c_findmin" LIBRARY DS_Lib LANGUAGE C;
```

The corresponding C function gets an argument of type `OCILobLocator` \*. When the function defined in Table 6-3 is called, it invokes a c routine, `c_findmin()`, with the signature `int c_findmin(OCILobLocator*)`.

The routine `c_findmin` is in a shared library associated with `DS_Lib`. To use the pointer `OCILobLocator*` to get data from the `LOB`, you must reconnect to the database by making a callback.

## LOBs and Triggers

You cannot write to a `LOB` (`:old` or `:new` value) in any kind of trigger.

In regular triggers, you can read the `:old` value, but you cannot read the `:new` value. In `INSTEAD` `OF` triggers, you can read both the `:old` and the `:new` values.

You cannot specify `LOB` type columns in an `OF` clause, because `BFILE` types can be updated without updating the underlying table on which the trigger is defined.

Using OCI functions or the `DBMS_LOB` package to update `LOB` values or `LOB` attributes of object columns does not fire triggers defined on the tablethat contains the columns or attributes.

## Using Open/Close as Bracketing Operations for Efficient Performance

The `Open/Close` functions let you indicate the beginning and end of a series of LOB operations, so that large-scale operations, such updating indexes, can be performed when the `Close` function is called. This means that when the `Open` call is made, the index would not be updated each time the LOB is modified, and that such updating would not resume until the `Close` call.

You do not have to wrap all `LOB` operations inside the `Open/Close` operations, but code block can be very valueable for the following reasons:

- If you do not wrap `LOB` operations inside an `Open/Close` call, then each modification to the `LOB` implicitly opens and closes the `LOB,` thereby firing all triggers. If you do wrap the `LOB` operations inside a pair of `Open...Close` operations, then the triggers are not fired for each `LOB` modification. Instead, one trigger is fired when the `Close` call is made. Likewise, extensible indexes are not updated until the `Close` call. This means that any extensible indexes on the `LOB` are not valid between the `Open...Close` calls.
- You must apply this technology carefully because state, which reflects the changes to the `LOB`, is not saved between the `Open` and the `Close` operations. When you have called `Open`, Oracle no longer keeps track of what portions of the `LOB` value were modified, nor of the old and new values of the `LOB` that result from any modifications. The `LOB` value is still updated directly for each `OCILob*` or `DBMS_LOB` operation, and the usual read consistency mechanism is still in place. You may also want extensible indexes on the `LOB` to be updated, as `LOB` modifications are made because the extensible `LOB` indexes are always valid and may be used at any time.
- The API enables you to determine if the `LOB` is open. In all cases, openness is associated with the `LOB`, not the locator. The locator does not save any state information.

### Errors and Restrictions Regarding Open/Close Operations

It is an error to commit the transaction before closing all previously opened `LOB` s. At transaction rollback time, all `LOB` s that are still open are discarded, which means that they are not closed, which fires the triggers.

It is an error to `Open/Close` the same `LOB` twice, either with different locators or with the same locator. It is an error to close a `LOB` that has not been opened.

Example 6-12 assumes that `loc1` is refers to an open `LOB`, and is assigned to `loc2`. If `loc2` is subsequently used to modify the `LOB` value, the modification is grouped with `loc1` 's modifications. This means that there is only one entry in the `LOB` manager's state, not one for each locator. When the `LOB` is closed, either through `loc1` or `loc2`, the triggers are fired, so all updates made to the `LOB` through either locator are committed. After the close of the `LOB`, if the user tries to use either locator to modify the `LOB`, the operation performs an implicit `Open()` and `Close()`, as `Open() ...` `operation` `... Close()`. Note that consistent read is still maintained for each locator. Remember that it is the `LOB`, not the locator, that is opened and closed. No matter how many copies of the locator are made, the triggers for the `LOB` are fired only one time on the first `Close()` call.

Example 6-12 Using Open() and Close() Code Block

```
open (loc1);
loc2 := loc1;
write (loc1);
write (loc2); 
open (loc2);  /* error because the LOB is open */
close (loc1); /* triggers are fired and all LOB updates made before this 
                 statement by any locator are incorporated in the extensible
                 index */
write (loc2); /* implicit open, write, implicit close */
```