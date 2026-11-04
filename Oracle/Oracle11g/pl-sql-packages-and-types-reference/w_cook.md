---
title: OWA_COOKIE
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/w_cook.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 188 OWA\_COOKIE

The OWA\_COOKIE package provides an interface for sending and retrieving HTTP cookies from the client's browser.

See Also:

For more information about implementation of this package:
- [Oracle Fusion Middleware Administrator's Guide for Oracle HTTP Server](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=HSADM)
- [Oracle Fusion Middleware User's Guide for mod\_plsql](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=YPMOD)

The chapter contains the following topics:

- Using OWA\_COOKIE
- Summary of OWA\_COOKIE Subprograms

---

## Using OWA\_COOKIE

---

### Overview

Cookies are opaque strings sent to the browser to maintain state between HTTP calls. State can be maintained throughout the client's sessions, or longer if an expiration date is included. The system date is calculated with reference to the information specified in the OWA\_CUSTOM package.

---

### Types

This data type contains cookie name-value pairs. Since the HTTP standard allows cookie names to be overloaded (that is, multiple values can be associated with the same cookie name), there is a PL/SQL `RECORD` holding all values associated with a given cookie name.

```
TYPE vc_arr IS TABLE OF VARCHAR2(4000) INDEX BY BINARY_INTEGER.

TYPE COOKIE IS RECORD (
   name           VARCHAR2(4000),
   vals           vc_arr,
   num_vals       INTEGER);
```

---

### Rules and Limits

All HTTP headers must be in English and the ASCII character set. If the headers are generated from the database, verify they are created in the English language.

---

## Summary of OWA\_COOKIE Subprograms

Table 188-1 OWA\_COOKIE Package Subprograms

| Subprogram | Description |
| --- | --- |
| GET Function | Gets the value of the specified cookie |
| GET\_ALL Procedure | Gets all cookie name-value pairs |
| REMOVE Procedure | Removes the specified cookie |
| SEND procedure | Generates a "Set-Cookie" line in the HTTP header |

---

### GET Function

This function returns the values associated with the specified cookie. The values are returned in a `OWA_COOKIE.COOKIE` `DATA` `TYPE`.

Syntax

```
OWA_COOKIE.GET(
    name           IN       VARCHAR2) 
  RETURN COOKIE;
```

Parameters

Table 188-2 GET Function Parameters

| Parameter | Description |
| --- | --- |
| `name` | The name of the cookie. |

---

### GET\_ALL Procedure

This procedure returns all cookie names and their values from the client's browser. The values appear in the order in which they were sent from the browser.

Syntax

```
OWA_COOKIE.GET_ALL(
   names          OUT      vc_arr,
   vals           OUT      vc_arr,
   num_vals       OUT      INTEGER);
```

Parameters

Table 188-3 GET\_ALL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `names` | The names of the cookies. |
| `vals` | The values of the cookies. |
| `num_vals` | The number of cookie-value pairs. |

---

### REMOVE Procedure

This procedure forces a cookie to expire immediately by setting the "expires" field of a Set-Cookie line in the HTTP header to "01-Jan-1990". This procedure must be called within the context of an HTTP header.

Syntax

```
OWA_COOKIE.REMOVE(
   name           IN       VARCHAR2,
   val            IN       VARCHAR2,
   path           IN       VARCHAR2   DEFAULT NULL);
```

Parameters

Table 188-4 REMOVE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | The name of the cookie to expire. |
| `val` | The value of the cookie. |
| `path` | \[Currently unused\] |

---

### SEND procedure

This procedure generates a Set-Cookie line, which transmits a cookie to the client. This procedure must occur in the context of an HTTP header.

Syntax

```
OWA_COOKIE.SEND(
   name           in       varchar2,
   value          in       varchar2,
   expires        in       date       DEFAULT NULL,
   path           in       varchar2   DEFAULT NULL,
   domain         in       varchar2   DEFAULT NULL,
   secure         in       varchar2   DEFAULT NULL);
```

Parameters

Table 188-5 SEND Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | The name of the cookie. |
| `value` | The value of the cookie. |
| `expires` | The date at which the cookie will expire |
| `path` | The value for the path field. |
| `domain` | The value for the domain field. |
| `secure` | If the value of this parameter is not `NULL`, the "secure" field is added to the line. |