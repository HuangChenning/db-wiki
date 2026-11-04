---
title: OWA_IMAGE
book: PL/SQL Packages and Types Reference
doc_id: E96430-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/OWA_IMAGE.html
tags:
  - oracle
  - 19c
  - pl-sql-packages-and-types-reference
---

The `OWA_IMAGE` package provides an interface to access the coordinates where a user clicked on an image.

The chapter contains the following topics:

**See Also:**

For more information about implementation of this package:

[*Oracle Fusion Middleware Administrator’s Guide for Oracle HTTP Server*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=HSADM)

[*Oracle Fusion Middleware User’s Guide for mod\_plsql*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=YPMOD)

### OWA\_IMAGE Overview

Use this package when you have any image map whose destination links invoke the PL/SQL Gateway.

### OWA\_IMAGE Types

This datatype (`point`) contain the `X` and `Y` values of a coordinate, and so provides the coordinates of a user’s click on an imagemap.

It is defined as:

```md
TYPE POINT IS TABLE OF VARCHAR2(32767) INDEX BY BINARY_INTEGER
```

### OWA\_IMAGE Variables

This package variable (`null_point`) of `TYPE` `POINT` is used to default point parameters. Both the X and the Y fields of this variable are `NULL`.

### OWA\_IMAGE Examples

This example shows use of `OWA_IMAGE`.

```md
CREATE OR REPLACE PROCEDURE process_image
    (my_img in OWA_IMAGE.POINT)
    AS
    x integer := OWA_IMAGE.GET_X(my_img);
    y integer := OWA_IMAGE.GET_Y(my_img);
BEGIN
    /* process the coordinate */
END
```

### Summary of OWA\_IMAGE Subprograms

This table lists the OWA\_IMAGE subprograms and briefly describes them.

Table 1 *OWA\_IMAGE Package Subprograms*

| Subprogram | Description |
| --- | --- |
| GET\_X Function | Gets the X value of a point type |
| GET\_Y Function | Gets the Y value of a point type |

### GET\_X Function

This function returns the `X` coordinate of the point where the user clicked on an image map.

**Syntax**

```md
OWA_IMAGE.GET_X(
   p        IN        point)
 RETURN INTEGER;
```

**Parameters**

Table 2 GET\_X Function Parameters

| Parameter | Description |
| --- | --- |
| `p` | The point where the user clicked. |

**Return Values**

The X coordinate as an integer.

### GET\_Y Function

This function returns the Y coordinate of the point where the user clicked on an image map.

**Syntax**

```md
OWA_IMAGE.GET_Y(
   p        IN        point)
 RETURN INTEGER;
```

**Parameters**

Table 3 GET\_Y Function Parameters

| Parameter | Description |
| --- | --- |
| `p` | The point where the user clicked. |

**Return Values**

The Y coordinate as an integer.