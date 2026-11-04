---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/OWA_OPT_LOCK.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 230 OWA\_OPT\_LOCK

The `OWA_OPT_LOCK` package contains subprograms that impose optimistic locking strategies so as to prevent lost updates.

This chapter contains the following topics:

See Also:

For more information about implementation of this package:

- [Oracle Fusion Middleware Administrator's Guide for Oracle HTTP Server](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=HSADM)
- [Oracle Fusion Middleware User's Guide for mod\_plsql](https://docs.oracle.com/cd/E23943_01/portal.1111/e12041/toc.htm)

### 230.1 OWA\_OPT\_LOCK Overview

The OWA\_OPT\_LOCK package contains subprograms that impose optimistic locking strategies, so as to prevent lost updates.

It checks if the row that the user is interested in updating has been changed by someone else in the meantime.

The PL/SQL Gateway cannot use conventional database locking schemes because HTTP is a stateless protocol. The `OWA_OPT_LOCK` package gives you two ways of dealing with the lost update problem:

- The hidden fields method stores the previous values in hidden fields in the HTML page. When the user requests an update, the PL/SQL Gateway checks these values against the current state of the database. The update operation is performed only if the values match. To use this method, call the owa\_opt\_lock.store\_values procedure.
- The checksum method stores a checksum rather than the values themselves. To use this method, call the owa\_opt\_lock.checksum function.

These methods are optimistic. They do not prevent other users from performing updates, but they do reject the current update if an intervening update has occurred.

### 230.2 OWA\_TEXT Types

This datatype is a PL/SQL table intended to hold ROWIDs.

```
TYPE VCARRAY IS TABLE OF VARCHAR2(2000) INDEX BY BINARY_INTEGER
```

Note that this is different from the `OWA_TEXT`.`VC_ARR DATA TYPE`.

### 230.3 Summary of OWA\_OPT\_LOCK Subprograms

This table lists the `OWA_OPT_LOCK` subprograms and briefly describes them.

Table 230-1 OWA\_OPT\_LOCK Package Subprograms

| Subprogram | Description |
| --- | --- |
| CHECKSUM Functions | Returns the checksum value |
| GET\_ROWID Function | Returns the ROWID value |
| STORE\_VALUES Procedure | Stores unmodified values in hidden fields for later verification |
| VERIFY\_VALUES Function | Verifies the stored values against modified values |

#### 230.3.1 CHECKSUM Functions

This function returns a `checksum` value for a specified string, or for a row in a table. For a row in a table, the function calculates the `checksum` value based on the values of the columns in the row. This function comes in two versions.

The first version returns a `checksum` based on the specified string. This is a "pure" 32-bit `checksum` executed by the database and based on the Internet 1 protocol.

The second version returns a `checksum` based on the values of a row in a table. This is a "impure" 32-bit checksum based on the Internet 1 protocol.

Syntax

```
OWA_OPT_LOCK.CHECKSUM(
   p_buff        IN       VARCHAR2) 
 RETURN NUMBER;

OWA_OPT_LOCK.CHECKSUM(
   p_buff        IN       VARCHAR2) 
 RETURN NUMBER PARALLEL_ENABLE DETERMINISTIC;

OWA_OPT_LOCK.CHECKSUM(
   p_owner       IN      VARCHAR2,
   p_tname       IN       VARCHAR2,
   p_rowid       IN       ROWID) 
  RETURN NUMBER;
```

Parameters

Table 230-2 CHECKSUM Function Parameters

| Parameter | Description |
| --- | --- |
| `p_buff` | The nstring where you want to calculate the `checksum`. |
| `p_owner` | The owner of the table. |
| `p_tname` | The table name. |
| `p_rowid` | The row in `p_tname` where you want to calculate the `checksum` value. Use the GET\_ROWID Function to convert `VCARRAY` values to proper rowids. |

#### 230.3.2 GET\_ROWID Function

This function returns the `ROWID` datatype from the specified `OWA_OPT_LOCK.VCARRAY` `DATA` `TYPE.`

Syntax

```
OWA_OPT_LOCK.GET_ROWID(
   p_old_values      IN      vcarray) 
 RETURN ROWID;

OWA_OPT_LOCK.GET_ROWID(
   p_old_values      IN      vcarray) 
 RETURN ROWID PARALLEL_ENABLE DETERMINISTIC;
```

Parameters

Table 230-3 GET\_ROWID Function Parameters

| Parameter | Description |
| --- | --- |
| `p_old_values` | This parameter is usually passed in from an HTML form. |

#### 230.3.3 STORE\_VALUES Procedure

This procedure stores the column values of the row that you want to update later. The values are stored in hidden HTML form elements.

Syntax

```
OWA_OPT_LOCK.STORE_VALUES(
   p_owner        IN       VARCHAR2,
   p_tname        IN       VARCHAR2,
   p_rowid        IN       ROWID);
```

Parameters

Table 230-4 STORE\_VALUES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `p_owner` | The owner of the table. |
| `p_tname` | The name of the table. |
| `p_rowid` | The row where you want to store values. |

Usage Notes

Before updating the row, compare these values with the current row values to ensure that the values in the row have not been changed. If the values have changed, you can warn the users and let them decide if the update should take place.

The procedure generates series of hidden form elements:

- One hidden form element is created for the table owner. The name of the element is " `old` `_p_tname` ", where `p_tname` is the name of the table. The value of the element is the owner name.
- One hidden form element is created for the table name. The name of the element is " `old` `_p_tname` ", where `p_tname` is the name of the table. The value of the element is the table name.
- One element is created for each column in the row. The name of the element is " `old` `_p_tname` ", where `p_tname` is the name of the table. The value of the element is the column value.

See also the VERIFY\_VALUES Function.

#### 230.3.4 VERIFY\_VALUES Function

This function verifies whether values in the specified row have been updated since the last query.

Use this function with the STORE\_VALUES Procedure.

Syntax

```
OWA_OPT_LOCK.VERIFY_VALUES(
   p_old_values IN vcarray) 
 RETURN BOOLEAN;
```

Parameters

Table 230-5 VERIFY\_VALUES Function Parameters

| Parameter | Description |
| --- | --- |
| `p_old_values` | A PL/SQL table containing the following information:  - `p_old_values(1)` specifies the owner of the table. - `p_old_values(2)` specifies the table. - `p_old_values(3)` specifies the rowid of the row to verify.  The remaining indexes contain values for the columns in the table.  Typically, this parameter is passed in from the HTML form, where you have previously called the STORE\_VALUES Procedure to store the row values on hidden form elements. |

Return Values

`TRUE` if no other update has been performed, otherwise `FALSE`.