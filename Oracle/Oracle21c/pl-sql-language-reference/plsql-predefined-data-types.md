---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: F31827-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/lnpls/plsql-predefined-data-types.html
tags:
  - oracle
  - 21c
  - pl-sql-language-reference
---

This appendix groups by data type family the data types and subtypes that the package `STANDARD` predefines.

Constants

This constant defines the maximum name length possible.

```
ORA_MAX_NAME_LEN CONSTANT PLS_INTEGER := 128;
```

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

DBMS_ID and DBMS_QUOTED_ID define the length of identifiers in objects for SQL, PL/SQL and users.
subtype DBMS_ID              is VARCHAR2(ORA_MAX_NAME_LEN);
subtype DBMS_QUOTED_ID       is VARCHAR2(ORA_MAX_NAME_LEN+2);

DBMS_ID_30 and DBMS_QUOTED_ID_30 define the length of SQL objects whose limits is 30 bytes.
subtype DBMS_ID_30           is VARCHAR2(30);
subtype DBMS_QUOTED_ID_30    is VARCHAR2(32);

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
```
```
type TIMESTAMP                        is new DATE_BASE;
```
```
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

JSON Data Type Family

```
type JSON is BLOB_BASE;
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

- [PL/SQL Data Types](plsql-data-types.md) for more information about PL/SQL data types
- " [User-Defined PL/SQL Subtypes](plsql-data-types.md) " for information that also applies to predefined subtypes