---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_RANDOM.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 142 DBMS\_RANDOM

The `DBMS_RANDOM` package provides a built-in random number generator. `DBMS_RANDOM` is not intended for cryptography.

This chapter contains the following topics:

### 142.1 DBMS\_RANDOM Deprecated Subprograms

These subprograms are deprecated with Oracle Database 11g. Oracle recommends that you do not use deprecated procedures in new applications. Support for deprecated features is for backward compatibility only.

- INITIALIZE Procedure
- RANDOM Function
- TERMINATE Procedure

### 142.2 DBMS\_RANDOM Security Model

This package should be installed as `SYS`. By default, the package is initialized with the current user name, current time down to the second, and the current session. Oracle recommends that users who need to execute this package should be given `EXECUTE` privilege explicitly and should not rely on `PUBLIC EXECUTE` privilege.

### 142.3 DBMS\_RANDOM Operational Notes

These operational notes apply to DBMS\_RANDOM.

- `DBMS_RANDOM.RANDOM ` produces integers in \-2^^31, 2^^31).
- `DBMS_RANDOM.VALUE` produces numbers in \[0,1) with 38 digits of precision.

`DBMS_RANDOM` can be explicitly initialized, but does not need to be initialized before calling the random number generator. It will automatically initialize with the date, user ID, and process ID if no explicit initialization is performed.

If this package is seeded twice with the same seed, then accessed in the same way, it will produce the same results in both cases.

In some cases, such as when testing, you may want the sequence of random numbers to be the same on every run. In that case, you seed the generator with a constant value by calling one of the overloads of `DBMS_RANDOM.SEED`. To produce different output for every run, simply to omit the call to "Seed" and the system will choose a suitable seed for you.

### 142.4 Summary of DBMS\_RANDOM Subprograms

This table lists the `DBMS_RANDOM` subprograms and briefly describes them.

Table 142-1 DBMS\_RANDOM Package Subprograms

| Subprogram | Description |
| --- | --- |
| [INITIALIZE Procedure | Initializes the package with a seed value |
| NORMAL Function | Returns random numbers in a normal distribution |
| RANDOM Function | Generates a random number |
| SEED Procedures | Resets the seed |
| STRING Function | Gets a random string |
| TERMINATE Procedure | Terminates package |
| VALUE Functions | Gets a random number, greater than or equal to 0 and less than 1, with 38 digits to the right of the decimal (38-digit precision), while the overloaded function gets a random Oracle number x, where x is greater than or equal to `low` and less than `high` |

#### 142.4.1 INITIALIZE Procedure

This deprecated procedure initializes the generator.

Note:

This procedure is deprecated with Release 11gR1 and, although currently supported, it should not be used.

Syntax

```
DBMS_RANDOM.INITIALIZE (
   val  IN  BINARY_INTEGER);
```

Pragmas

```
PRAGMA restrict_references (initialize, WNDS);
```

Parameters

Table 142-2 INITIALIZE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `val` | Seed number used to generate a random number |

Usage Notes

This procedure is obsolete as it simply calls the SEED Procedures.

#### 142.4.2 NORMAL Function

This function returns random numbers in a standard normal distribution.

Syntax

```
DBMS_RANDOM.NORMAL
  RETURN NUMBER;
```

Pragmas

```
PRAGMA restrict_references (normal, WNDS);
```

Return Values

Table 142-3 NORMAL Function Parameters

| Parameter | Description |
| --- | --- |
| `number` | Returns a random number |

#### 142.4.3 RANDOM Function

This deprecated procedure generates a random number.

Note:

This function is deprecated with Release 11gR1 and, although currently supported, it should not be used.

Syntax

```
DBMS_RANDOM.RANDOM
   RETURN binary_integer;
```

Pragmas

```
PRAGMA restrict_references (random, WNDS);
```

Return Values

Table 142-4 RANDOM Function Parameters

| Parameter | Description |
| --- | --- |
| `binary_integer` | Returns a random integer greater or equal to -power(2,31) and less than power(2,31) |

#### 142.4.4 SEED Procedures

This procedure resets the seed.

Syntax

```
DBMS_RANDOM.SEED (
   val  IN  BINARY_INTEGER);

DBMS_RANDOM.SEED (
   val  IN  VARCHAR2);
```

Pragmas

```
PRAGMA restrict_references (seed, WNDS);
```

Parameters

Table 142-5 SEED Procedure Parameters

| Parameter | Description |
| --- | --- |
| `val` | Seed number or string used to generate a random number |

Usage Notes

The seed can be a string up to length 2000.

#### 142.4.5 STRING Function

This function gets a random string.

Syntax

```
DBMS_RANDOM.STRING
   opt  IN  CHAR,
   len  IN  NUMBER)
  RETURN VARCHAR2;
```

Pragmas

```
PRAGMA restrict_references (string, WNDS);
```

Parameters

Table 142-6 STRING Function Parameters

| Parameter | Description |
| --- | --- |
| `opt` | Specifies what the returning string looks like:  - 'u', 'U' - returning string in uppercase alpha characters - 'l', 'L' - returning string in lowercase alpha characters - 'a', 'A' - returning string in mixed case alpha characters - 'x', 'X' - returning string in uppercase alpha-numeric characters - 'p', 'P' - returning string in any printable characters.  Otherwise the returning string is in uppercase alpha characters. |
| `len` | Length of the returning string |

Return Values

Table 142-7 STRING Function Return Values

| Parameter | Description |
| --- | --- |
| `VARCHAR2` | Returns a `VARCHAR2` |

#### 142.4.6 TERMINATE Procedure

When you are finished with the package, call the `TERMINATE` procedure.

Note:

This procedure is deprecated with Release 11gR1 and, although currently supported, it should not be used.

Syntax

```
DBMS_RANDOM.TERMINATE;
```

#### 142.4.7 VALUE Functions

The basic function gets a random number, greater than or equal to 0 and less than 1, with 38 digits to the right of the decimal (38-digit precision). Alternatively, you can get a random Oracle number x, where x is greater than or equal to `low` and less than `high`.

Syntax

```
DBMS_RANDOM.VALUE
  RETURN NUMBER;

DBMS_RANDOM.VALUE(
  low  IN  NUMBER,
  high IN  NUMBER)
RETURN NUMBER;
```

Parameters

Table 142-8 VALUE Function Parameters

| Parameter | Description |
| --- | --- |
| `low` | Lowest number in a range from which to generate a random number. The number generated may be equal to `low` |
| `high` | Highest number below which to generate a random number. The number generated will be less than `high` |

Return Values

Table 142-9 VALUE Function Return Values

| Parameter | Description |
| --- | --- |
| `NUMBER` | Returns an Oracle Number |