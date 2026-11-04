---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/OWA_TEXT.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 233 OWA\_TEXT

The `OWA_TEXT` package contains subprograms used by `OWA_PATTERN` for manipulating strings. They are externalized so you can use them directly.

See Also:

For more information about implementation of this package:

- [Oracle Fusion Middleware Administrator's Guide for Oracle HTTP Server](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=HSADM)
- [Oracle Fusion Middleware User's Guide for mod\_plsql](https://docs.oracle.com/cd/E23943_01/portal.1111/e12041/toc.htm)

The chapter contains the following topics:

- Types
- Summary of OWA\_TEXT Subprograms

### 233.1 OWA\_OPT\_LOCK Types

There are three OWA\_OPT\_LOCK lock types.

#### 233.1.1 MULTI\_LINE DATA TYPE

This datatype is a PL/SQL record that holds large amounts of text. The rows field, of type `OWA_TEXT`.`VC_ARR` `DATA` `TYPE`, contains the text data in the record.

```
TYPE multi_line IS RECORD (
   rows           vc_arr,
   num_rows       INTEGER,
   partial_row    BOOLEAN);
```

#### 233.1.2 ROW\_LIST DATA TYPE

This is the datatype for holding data to be processed.

```
TYPE row_list IS RECORD (
   rows           int_arr,
   num_rows       INTEGER);

int_arr IS DEFINED AS:

TYPE int_arr IS TABLE OF INTEGER INDEX BY BINARY_INTEGER;
```

#### 233.1.3 VC\_ARR DATA TYPE

This is a component of the MULTI\_LINE DATA TYPE and is used for holding large amounts of text.

```
TYPE vc_arr IS TABLE OF VARCHAR2(32767) INDEX BY BINARY_INTEGER;
```

### 233.2 Summary of OWA\_TEXT Subprograms

This table lists the `OWA_TEXT` subprograms and briefly describes them.

Table 233-1 OWA\_TEXT Package Subprograms

| Subprogram | Description |
| --- | --- |
| ADD2MULTI Procedure | Adds text to an existing `multi_line` type |
| NEW\_ROW\_LIST Function and Procedure | Creates a new `row_list` |
| [PRINT\_MULTI Procedure](https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/OWA_TEXT.html#GUID-C72B2B3F-1466-4A23-BCC0-7815157C041C "This procedure uses the PRINT Procedures or the PRN Procedures to print the \"rows\" field of the OWA_TEXT.MULTI_LINE DATA TYPE.") | Prints out the contents of a `multi_list` |
| [PRINT\_ROW\_LIST Procedure](https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/OWA_TEXT.html#GUID-091F0E80-6DD5-43A5-9DC0-8793A02B4697 "This procedure uses the PRINT Procedures or the PRN Procedures to print the \"rows\" field of the OWA_TEXT.ROW_LIST DATA TYPE.") | Prints out the contents of a `row_list` |
| STREAM2MULTI Procedure | Converts a varchar2 to a `multi_line` type |

#### 233.2.1 ADD2MULTI Procedure

This procedure adds content to an existing Multi\_Line Data Type

Syntax

```
OWA_TEXT.ADD2MULTI(
   stream         IN       VARCHAR2,
   mline          IN OUT   multi_line,
```

continue IN BOOLEAN DEFAULT TRUE);

Parameters

Table 233-2 ADD2MULTI Procedure Parameters

| Parameter | Description |
| --- | --- |
| `stream` | The text to add. |
| `mline` | The `OWA_TEXT.MULTI_LINE DATA TYPE`. The output of this parameter contains stream. |
| `continue` | If `TRUE`, the procedure appends stream within the previous final row (assuming it is less than 32K). If `FALSE`, the procedure places stream in a new row. |

#### 233.2.2 NEW\_ROW\_LIST Function and Procedure

This function or procedure creates a new `OWA_TEX.ROW_LIST DATA TYPE`.

The function version uses no parameters and returns a new empty `row_list`. The procedure version creates the `row_list` datatype as an output parameter.

Syntax

```
OWA_TEXT.NEW_ROW_LIST 
  RETURN ROW_LIST;

OWA_TEXT.NEW_ROW_LIST(
  rlist    OUT     row_list);
```

Parameters

Table 233-3 NEW\_ROW\_LIST Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rlist` | This is an output parameter containing the new `row_list` datatype |

Return Values

The function version returns the new `row_list` datatype.

#### 233.2.3 PRINT\_MULTI Procedure

This procedure uses the PRINT Procedures or the PRN Procedures to print the "rows" field of the `OWA_TEXT`.`MULTI_LINE` `DATA` `TYPE`.

Syntax

```
OWA_TEXT.PRINT_MULTI(
   mline       IN       multi_line);
```

Parameters

Table 233-4 PRINT\_MULTIProcedure Parameters

| Parameter | Description |
| --- | --- |
| `mline` | The multi\_line datatype to print. |

Return Values

The contents of the `multi_line`.

#### 233.2.4 PRINT\_ROW\_LIST Procedure

This procedure uses the PRINT Procedures or the PRN Procedures to print the "rows" field of the `OWA_TEXT`.`ROW_LIST` `DATA` `TYPE`.

Syntax

```
OWA_TEXT.PRINT_ROW_LIST(
   rlist       IN       multi_line);
```

Parameters

Table 233-5 PRINT\_ROW\_LIST Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rlist` | The row\_list datatype to print. |

Return Values

The contents of the `row_list`.

#### 233.2.5 STREAM2MULTI Procedure

This procedure converts a string to a `multi_line` datatype.

Syntax

```
OWA_TEXT.STREAM2MULTI(
   stream         IN       VARCHAR2
   mline          OUT      multi_line);
```

Parameters

Table 233-6 STREAM2MULTI Procedure Parameters

| Parameter | Description |
| --- | --- |
| `stream` | The string to convert. |
| `mline` | The stream in `OWA_TEXT.MULTI_LINE DATA TYPE` format |