---
title: PL/SQL Predefined Data Types
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/predefined.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

## E PL/SQL Predefined Data Types

This appendix groups by data type family the data types and subtypes that the package `STANDARD` predefines.

BFILE Data Type Family

```
type BFILE is BFILE_BASE;
```

BLOB Data Type Family

```
type BLOB is BLOB_BASE;

subtype "BINARY LARGE OBJECT" is BLOB;
```

BOOLEAN Data Type Family

```
type BOOLEAN is (FALSE, TRUE);
```

CHAR Data Type Family

```
type VARCHAR2 is new CHAR_BASE;
type MLSLABEL is new CHAR_BASE;
type UROWID   is new CHAR_BASE;

subtype VARCHAR              is VARCHAR2;
subtype STRING               is VARCHAR2;
subtype LONG                 is VARCHAR2(32760);
subtype RAW                  is VARCHAR2;
subtype "LONG RAW"           is RAW(32760);
subtype ROWID                is VARCHAR2(256);
subtype CHAR                 is VARCHAR2;
subtype CHARACTER            is CHAR;
subtype "CHARACTER VARYING"  is VARCHAR;
subtype "CHAR VARYING"       is VARCHAR;
subtype "NATIONAL CHARACTER" is CHAR CHARACTER SET NCHAR_CS;
subtype "NATIONAL CHAR"      is CHAR CHARACTER SET NCHAR_CS;
subtype "NCHAR"              is CHAR CHARACTER SET NCHAR_CS;
subtype "NVARCHAR2"          is VARCHAR2 CHARACTER SET NCHAR_CS;
```

CLOB Data Type Family

```
type CLOB is CLOB_BASE;

subtype "CHARACTER LARGE OBJECT"          is CLOB;
subtype "CHAR LARGE OBJECT"               is CLOB;
subtype "NATIONAL CHARACTER LARGE OBJECT" is CLOB CHARACTER SET NCHAR_CS;
subtype "NCHAR LARGE OBJECT"              is CLOB CHARACTER SET NCHAR_CS;
subtype "NCLOB"                           is CLOB CHARACTER SET NCHAR_CS;
```

DATE Data Type Family

```
type DATE                             is     DATE_BASE;
type TIMESTAMP                        is new DATE_BASE;
type "TIMESTAMP WITH TIME ZONE"       is new DATE_BASE;
type "INTERVAL YEAR TO MONTH"         is new DATE_BASE;
type "INTERVAL DAY TO SECOND"         is new DATE_BASE;
type "TIMESTAMP WITH LOCAL TIME ZONE" is new DATE_BASE;

subtype TIME_UNCONSTRAINED          is TIME(9);
subtype TIME_TZ_UNCONSTRAINED       is TIME(9) WITH TIME ZONE;
subtype TIMESTAMP_UNCONSTRAINED     is TIMESTAMP(9);
subtype TIMESTAMP_TZ_UNCONSTRAINED  is TIMESTAMP(9) WITH TIME ZONE;
subtype YMINTERVAL_UNCONSTRAINED    is INTERVAL YEAR(9) TO MONTH;
subtype DSINTERVAL_UNCONSTRAINED    is INTERVAL DAY(9) TO SECOND (9);
subtype TIMESTAMP_LTZ_UNCONSTRAINED is TIMESTAMP(9) WITH LOCAL TIME ZONE;
```

NUMBER Data Type Family

```
type NUMBER is NUMBER_BASE;

subtype FLOAT              is NUMBER; -- NUMBER(126)
subtype REAL               is FLOAT;   -- FLOAT(63)
subtype "DOUBLE PRECISION" is FLOAT;

subtype INTEGER  is NUMBER(38,0);
subtype INT      is INTEGER;
subtype SMALLINT is NUMBER(38,0);

subtype DECIMAL is NUMBER(38,0);
subtype NUMERIC is DECIMAL;
subtype DEC     is DECIMAL;

subtype BINARY_INTEGER is INTEGER range '-2147483647'..2147483647;
subtype NATURAL        is BINARY_INTEGER range 0..2147483647;
subtype NATURALN       is NATURAL not null;
subtype POSITIVE       is BINARY_INTEGER range 1..2147483647;
subtype POSITIVEN      is POSITIVE not null;
subtype SIGNTYPE       is BINARY_INTEGER range '-1'..1;  -- for SIGN functions
subtype PLS_INTEGER    is BINARY_INTEGER;

type BINARY_FLOAT  is NUMBER;
type BINARY_DOUBLE is NUMBER;

subtype SIMPLE_INTEGER is BINARY_INTEGER NOT NULL;
subtype SIMPLE_FLOAT   is BINARY_FLOAT   NOT NULL;
subtype SIMPLE_DOUBLE  is BINARY_DOUBLE  NOT NULL;
```

See Also:

- [Chapter 3, "PL/SQL Data Types"](datatypes.md) for more information about PL/SQL data types
- ["User-Defined PL/SQL Subtypes"](datatypes.md) for information that also applies to predefined subtypes