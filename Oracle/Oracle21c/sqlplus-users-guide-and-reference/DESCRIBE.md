---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/DESCRIBE.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
DESC[RIBE] {[schema.]object[@db_link]}
```

Lists the column definitions for the specified table, view or synonym, or the specifications for the specified function or procedure.

Terms

```
schema
```

Represents the schema where the object or permission to describe the object resides. If you omit schema and the object is not a public synonym, SQL\*Plus assumes you own object.

```
object
```

Represents the table, view, type, procedure, function, package or synonym you wish to describe.

```
@db_link
```

Consists of the database link name corresponding to the database where object exists. For more information on which privileges allow access to another table in a different schema, refer to the [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=SQLRF).

Usage

The description for tables, views, types and synonyms contains the following information:

- each column's name
- whether or not null values are allowed (NULL or NOT NULL) for each column
- datatype of columns, for example, CHAR, DATE, LONG, LONGRAW, NUMBER, RAW, ROWID, VARCHAR2 (VARCHAR), or XMLType
- precision of columns (and scale, if any, for a numeric column)

When you do a DESCRIBE, VARCHAR columns are returned with a type of VARCHAR2.

The DESCRIBE command enables you to describe objects recursively to the depth level set in the SET DESCRIBE command. You can also display the line number and indentation of the attribute or column name when an object contains multiple object types. For more information, see the SET command.

To control the width of the data displayed, use the SET LINESIZE command.

Columns output for the DESCRIBE command are typically allocated a proportion of the linesize currently specified. Decreasing or increasing the linesize with the SET LINESIZE command usually makes each column proportionally smaller or larger. This may give unexpected text wrapping in your display. For more information, see the SET command.

The description for functions and procedures contains the following information:

- the type of PL/SQL object (function or procedure)
- the name of the function or procedure
- the type of value returned (for functions)
- the argument names, types, whether input or output, and default values, if any
- the ENCRYPT keyword to indicate whether or not data in a column is encrypted

Examples

To describe the view EMP\_DETAILS\_VIEW, enter

```
DESCRIBE EMP_DETAILS_VIEW
```
```
Name                                      Null?    Type
----------------------------------------- -------- ----------------
EMPLOYEE_ID                               NOT NULL NUMBER(6)
JOB_ID                                    NOT NULL VARCHAR2(10)
MANAGER_ID                                         NUMBER(6)
DEPARTMENT_ID                                      NUMBER(4)
LOCATION_ID                                        NUMBER(4)
COUNTRY_ID                                         CHAR(2)
FIRST_NAME                                         VARCHAR2(20)
LAST_NAME                                 NOT NULL VARCHAR2(25)
SALARY                                             NUMBER(8,2)
COMMISSION_PCT                                     NUMBER(2,2)
DEPARTMENT_NAME                           NOT NULL VARCHAR2(30)
JOB_TITLE                                 NOT NULL VARCHAR2(35)
CITY                                      NOT NULL VARCHAR2(30)
STATE_PROVINCE                                     VARCHAR2(25)
COUNTRY_NAME                                       VARCHAR2(40)
REGION_NAME                                        VARCHAR2(25)
```

To describe a procedure called CUSTOMER\_LOOKUP, enter

```
DESCRIBE customer_lookup
```
```
PROCEDURE customer_lookup
Argument Name           Type     In/Out   Default?
----------------------  -------- -------- ---------
CUST_ID                 NUMBER   IN
CUST_NAME               VARCHAR2 OUT
```

To create and describe the package APACK that contains the procedures aproc and bproc, enter

```
CREATE PACKAGE apack AS
PROCEDURE aproc(P1 CHAR, P2 NUMBER);
PROCEDURE bproc(P1 CHAR, P2 NUMBER);
END apack;
/
```
```
Package created.
```
```
DESCRIBE apack
```
```
PROCEDURE APROC
 Argument Name                  Type                    In/Out Default?
 ------------------------------ ----------------------- ------ --------
 P1                             CHAR                    IN
 P2                             NUMBER                  IN
PROCEDURE BPROC
 Argument Name                  Type                    In/Out Default?
 ------------------------------ ----------------------- ------ --------
 P1                             CHAR                    IN
 P2                             NUMBER                  IN
```

To create and describe the object type ADDRESS that contains the attributes STREET and CITY, enter

```
CREATE TYPE ADDRESS AS OBJECT
  ( STREET  VARCHAR2(20),
    CITY    VARCHAR2(20)
  );
/
```
```
Type created.
```
```
DESCRIBE address
```
```
Name                                      Null?    Type
----------------------------------------- -------- ----------------------
STREET                                             VARCHAR2(20)
CITY                                               VARCHAR2(20)
```

To create and describe the object type EMPLOYEE that contains the attributes LAST\_NAME, EMPADDR, JOB\_ID and SALARY, enter

```
CREATE TYPE EMPLOYEE AS OBJECT
(LAST_NAME VARCHAR2(30),
EMPADDR ADDRESS,
JOB_ID VARCHAR2(20),
SALARY NUMBER(7,2)
);
/
```
```
Type created.
```
```
DESCRIBE employee
```
```
Name                                      Null?    Type
----------------------------------------- -------- ----------------------
LAST_NAME                                          VARCHAR2(30)
EMPADDR                                            ADDRESS
JOB_ID                                             VARCHAR2(20)
SALARY                                             NUMBER(7,2)
```

To create and describe the object type addr\_type as a table of the object type ADDRESS, enter

```
CREATE TYPE addr_type IS TABLE OF ADDRESS;
/
```
```
Type created.
```
```
DESCRIBE addr_type
```
```
addr_type TABLE OF ADDRESS
Name                                      Null?    Type
----------------------------------------- -------- ----------------------
STREET                                             VARCHAR2(20)
CITY                                               VARCHAR2(20)
```

To create and describe the object type addr\_varray as a varray of the object type ADDRESS, enter

```
CREATE TYPE addr_varray AS VARRAY(10) OF ADDRESS;
/
```
```
Type created.
```
```
DESCRIBE addr_varray
```
```
addr_varray VARRAY(10) OF ADDRESS
Name                                      Null?    Type
----------------------------------------- -------- ----------------------
STREET                                             VARCHAR2(20)
CITY                                               VARCHAR2(20)
```

To create and describe the table department that contains the columns DEPARTMENT\_ID, PERSON and LOC, enter

```
CREATE TABLE department
(DEPARTMENT_ID NUMBER,
PERSON EMPLOYEE,
LOC NUMBER
);
/
```
```
Table created.
```
```
DESCRIBE department
```
```
Name                                      Null?    Type
----------------------------------------- -------- ----------------------
DEPARTMENT_ID                                      NUMBER
PERSON                                             EMPLOYEE
LOC                                                NUMBER
```

To create and describe the object type rational that contains the attributes NUMERATOR and DENOMINATOR, and the METHOD rational\_order, enter

```
CREATE OR REPLACE TYPE rational AS OBJECT
(NUMERATOR NUMBER,
DENOMINATOR NUMBER,
MAP MEMBER FUNCTION rational_order - 
RETURN DOUBLE PRECISION,
PRAGMA RESTRICT_REFERENCES
(rational_order, RNDS, WNDS, RNPS, WNPS) );
/
```
```
CREATE OR REPLACE TYPE BODY rational AS OBJECT
MAP MEMBER FUNCTION rational_order - 
RETURN DOUBLE PRECISION IS 
BEGIN
  RETURN NUMERATOR/DENOMINATOR;
END;
END;
/
DESCRIBE rational
```
```
Name                             Null?      Type
------------------------------   --------   ------------
NUMERATOR                                   NUMBER
DENOMINATOR                                 NUMBER

METHOD
------
MAP MEMBER FUNCTION RATIONAL_ORDER RETURNS NUMBER
```

To create a table which contains a column of XMLType, and describe it, enter

```
CREATE TABLE PROPERTY (Price NUMBER, Description SYS.XMLTYPE);
```
```
Table created
```
```
DESCRIBE PROPERTY;
```
```
Name                                       Null?     Type
-----------------------------------------  --------  ----------------------
PRICE                                                NUMBER
DESCRIPTION                                          SYS.XMLTYPE
```

To format the DESCRIBE output use the SET command as follows:

```
SET LINESIZE 80
SET DESCRIBE DEPTH 2
SET DESCRIBE INDENT ON
SET DESCRIBE LINE OFF
```

To display the settings for the object, use the SHOW command as follows:

```
SHOW DESCRIBE
```
```
DESCRIBE DEPTH 2 LINENUM OFF INDENT ON
```
```
DESCRIBE employee
```
```
Name                                      Null?    Type
----------------------------------------- -------- ----------------------
FIRST_NAME                                         VARCHAR2(30)
EMPADDR                                            ADDRESS
  STREET                                           VARCHAR2(20)
  CITY                                             VARCHAR2(20)
JOB_ID                                             VARCHAR2(20)
SALARY                                             NUMBER(7,2)
```

To create and describe the table des2\_table which contains an encrypted column col2, enter

```
CREATE TABLE des2_table (
col1 VARCHAR2(10),
col2 VARCHAR2(15) ENCRYPT,
col3 CHAR(5),
col4 CHAR(20));
```
```
Table created
```
```
DESCRIBE des2_table;
```
```
Name                                       Null?     Type
-----------------------------------------  --------  ----------------------
COL1                                                 VARCHAR2(10)
COL2                                                 VARCHAR2(15) ENCRYPT
COL3                                                 CHAR(5)
COL4                                                 CHAR(20)
```

For more information on using the CREATE TYPE command, see your [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=SQLRF).

For information about using the SET DESCRIBE and SHOW DESCRIBE commands, see the [SET](SET.md) and [SHOW](SHOW.md) commands.