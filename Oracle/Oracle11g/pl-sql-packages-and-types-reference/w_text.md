---
title: OWA_TEXT
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/w_text.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 194 OWA\_TEXT

The `OWA_TEXT` package contains subprograms used by `OWA_PATTERN` for manipulating strings. They are externalized so you can use them directly.

See Also:

For more information about implementation of this package:
- [Oracle Fusion Middleware Administrator's Guide for Oracle HTTP Server](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=HSADM)
- [Oracle Fusion Middleware User's Guide for mod\_plsql](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=YPMOD)

The chapter contains the following topics:

- Using OWA\_TEXT
	- Types
- Summary of OWA\_TEXT Subprograms

---

## Using OWA\_TEXT

- Types

---

### Types

#### MULTI\_LINE DATA TYPE

This data type is a PL/SQL record that holds large amounts of text. The rows field, of type `OWA_TEXT`.`VC_ARR` `DATA` `TYPE`, contains the text data in the record.

```
TYPE multi_line IS RECORD (
   rows           vc_arr,
   num_rows       INTEGER,
   partial_row    BOOLEAN);
```

#### ROW\_LIST DATA TYPE

This is the data type for holding data to be processed.

```
TYPE row_list IS RECORD (
   rows           int_arr,
   num_rows       INTEGER);

int_arr IS DEFINED AS:
```

TYPE int\_arr IS TABLE OF INTEGER INDEX BY BINARY\_INTEGER;

#### VC\_ARR DATA TYPE

This is a component of the MULTI\_LINE DATA TYPE and is used for holding large amounts of text.

```
TYPE vc_arr IS TABLE OF VARCHAR2(32767) INDEX BY BINARY_INTEGER;
```

---

## Summary of OWA\_TEXT Subprograms

Table 194-1 OWA\_TEXT Package Subprograms

| Subprogram | Description |
| --- | --- |
| ADD2MULTI Procedure | Adds text to an existing `multi_line` type |
| NEW\_ROW\_LIST Function and Procedure | Creates a new `row_list` |
| PRINT\_MULTI Procedure | Prints out the contents of a `multi_list` |
| PRINT\_ROW\_LIST Procedure | Prints out the contents of a `row_list` |
| STREAM2MULTI Procedure | Converts a varchar2 to a `multi_line` type |

---

### ADD2MULTI Procedure

This procedure adds content to an existing MULTI\_LINE DATA TYPE.

Syntax

```
OWA_TEXT.ADD2MULTI(
   stream         IN       VARCHAR2,
   mline          IN OUT   multi_line,
```

continue IN BOOLEAN DEFAULT TRUE);

Parameters

Table 194-2 ADD2MULTI Procedure Parameters

| Parameter | Description |
| --- | --- |
| `stream` | The text to add. |
| `mline` | The `OWA_TEXT.MULTI_LINE DATA TYPE`. The output of this parameter contains stream. |
| `continue` | If `TRUE`, the procedure appends stream within the previous final row (assuming it is less than 32K). If `FALSE`, the procedure places stream in a new row. |

---

### NEW\_ROW\_LIST Function and Procedure

This function or procedure creates a new `OWA_TEXT`.`ROW_LIST` `DATA` `TYPE`. The function version uses no parameters and returns a new empty `row_list`. The procedure version creates the `row_list` data type as an output parameter.

Syntax

```
OWA_TEXT.NEW_ROW_LIST 
  RETURN ROW_LIST;

OWA_TEXT.NEW_ROW_LIST(
  rlist    OUT     row_list);
```

Parameters

Table 194-3 NEW\_ROW\_LIST Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rlist` | This is an output parameter containing the new `row_list` data type |

Return Values

The function version returns the new `row_list` data type.

---

### PRINT\_MULTI Procedure

This procedure uses the [PRINT Procedures](w_htp.md) or the [PRN Procedures](w_htp.md) to print the "rows" field of the `OWA_TEXT`.`MULTI_LINE` `DATA` `TYPE`.

Syntax

```
OWA_TEXT.PRINT_MULTI(
   mline       IN       multi_line);
```

Parameters

Table 194-4 PRINT\_MULTI Procedure Parameters

| Parameter | Description |
| --- | --- |
| `mline` | The multi\_line data type to print. |

Return Values

The contents of the `multi_line`.

---

### PRINT\_ROW\_LIST Procedure

This procedure uses the [PRINT Procedures](w_htp.md) or the [PRN Procedures](w_htp.md) to print the "rows" field of the `OWA_TEXT`.`ROW_LIST` `DATA` `TYPE`.

Syntax

```
OWA_TEXT.PRINT_ROW_LIST(
   rlist       IN       multi_line);
```

Parameters

Table 194-5 PRINT\_ROW\_LIST Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rlist` | The row\_list data type to print. |

Return Values

The contents of the `row_list`.

---

### STREAM2MULTI Procedure

This procedure converts a string to a `multi_line` data type.

Syntax

```
OWA_TEXT.STREAM2MULTI(
   stream         IN       VARCHAR2
   mline          OUT      multi_line);
```

Parameters

Table 194-6 STREAM2MULTI Procedure Parameters

| Parameter | Description |
| --- | --- |
| `stream` | The string to convert. |
| `mline` | The stream in `OWA_TEXT.MULTI_LINE DATA TYPE` format |