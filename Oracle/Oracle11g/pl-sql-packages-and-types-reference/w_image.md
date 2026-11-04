---
title: OWA_IMAGE
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/w_image.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 190 OWA\_IMAGE

The `OWA_IMAGE` package provides an interface to access the coordinates where a user clicked on an image.

See Also:

For more information about implementation of this package:
- [Oracle Fusion Middleware Administrator's Guide for Oracle HTTP Server](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=HSADM)
- [Oracle Fusion Middleware User's Guide for mod\_plsql](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=YPMOD)

The chapter contains the following topics:

- Summary of OWA\_IMAGE Subprograms
- Summary of OWA\_IMAGE Subprograms

---

## Using OWA\_IMAGE

---

### Overview

Use this package when you have any image map whose destination links invoke the PL/SQL Gateway.

---

### Types

This data type (`point`) contain the `X` and `Y` values of a coordinate, and so provides the coordinates of a user's click on an imagemap. It is defined as:

```
TYPE POINT IS TABLE OF VARCHAR2(32767) INDEX BY BINARY_INTEGER
```

---

### Variables

This package variable (`null_point`) of `TYPE` `POINT` is used to default point parameters. Both the X and the Y fields of this variable are `NULL`.

---

### Examples

```
CREATE OR REPLACE PROCEDURE process_image
    (my_img in OWA_IMAGE.POINT)
    AS
    x integer := OWA_IMAGE.GET_X(my_img);
    y integer := OWA_IMAGE.GET_Y(my_img);
BEGIN
    /* process the coordinate */
END
```

---

## Summary of OWA\_IMAGE Subprograms

Table 190-1 OWA\_IMAGE Package Subprograms

| Subprogram | Description |
| --- | --- |
| GET\_X Function | Gets the X value of a point type |
| GET\_Y Function | Gets the Y value of a point type |

---

### GET\_X Function

This function returns the `X` coordinate of the point where the user clicked on an image map.

Syntax

```
OWA_IMAGE.GET_X(
   p        IN        point)
 RETURN INTEGER;
```

Parameters

Table 190-2 GET\_X Function Parameters

| Parameter | Description |
| --- | --- |
| `p` | The point where the user clicked. |

Return Values

The X coordinate as an integer.

---

### GET\_Y Function

This function returns the Y coordinate of the point where the user clicked on an image map.

Syntax

```
OWA_IMAGE.GET_Y(
   p        IN        point)
 RETURN INTEGER;
```

Parameters

Table 190-3 GET\_Y Function Parameters

| Parameter | Description |
| --- | --- |
| `p` | The point where the user clicked. |

Return Values

The Y coordinate as an integer.