---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/overview-polymorphic-table-functions.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Overview of Polymorphic Table Functions

Polymorphic table functions (PTF) are table functions whose operands can have more than one type. The return type is determined by the PTF invocation arguments list. The actual arguments to the table type usually determines the row output shape, but not always.

Introduction to Polymorphic Table Functions

Polymorphic Table Functions (PTF) are user-defined functions that can be invoked in the `FROM` clause of a SQL query block. They are capable of processing tables whose row type is not declared at definition time and producing a result table whose row type may or may not be declared at definition time. Polymorphic table functions leverage dynamic SQL capabilities to create powerful and complex custom functions. This is useful for applications demanding an interface with generic extensions which work for arbitrary input tables or queries.

A PTF author creates an interface to a procedural mechanism that defines a table. The PTF author defines, documents, and implements the PTF.

The query author can only describe the published interface and invoke the PTF function in queries.

The database is the PTF conductor. It manages the compilation and execution states of the PTF. The database and the PTF author can see a family of related SQL invoked procedures, called the PTF component procedures, and possibly additional private data (such as variables and cursors).

Types of Polymorphic Table Functions

The polymorphic table function type is specified based on their formal arguments list semantics:
- If an input `TABLE` argument has `Row Semantics`, the input is a single row.
- If an input `TABLE` argument has `Table Semantics`, the input is a set of rows. When a `Table Semantics` PTF is called from a query, the table argument can optionally be extended with either a `PARTITION BY` clause or an `ORDER BY` clause or both.

### Polymorphic Table Function Definition

The PTF author defines, documents, and implements the Polymorphic Table Function (PTF).

A PTF has two parts:

1\. The PL/SQL package which contains the client interface for the PTF implementation.

2\. The standalone or package function naming the PTF and its associated implementation package.

### Polymorphic Table Function Implementation

The Polymorphic Table Function (PTF) implementation client interface is a set of subprograms with fixed names that every PTF must provide.

Steps to Implement a Polymorphic Table Function

1. Create the implementation package containing the `DESCRIBE` function (required) and the `OPEN`, `FETCH_ROWS`, and `CLOSE` procedures (optional).
2. Create the function specification naming the PTF. The function can be created at the top-level after the package has been created, or as a package function in the implementation package (the package created in the first step). Polymorphic table functions do not have a function definition (a `FUNCTION` `BODY`), the definition is encapsulated in the associated implementation package.
	The function definition specifies:
	- The Polymorphic Table Function (PTF) name
		- Exactly one formal argument of type `TABLE` and any number of non `TABLE` arguments
		- The return type of the PTF as `TABLE`
		- The type of PTF function (`row` or `table semantics` )
		- The PTF implementation package name

See Also:

- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ARPLS-GUID-6E589F68-6693-42A1-8766-61AF1476DE1C) for information about a `DESCRIBE` Only polymorphic table function
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ARPLS-GUID-47E8026F-B66B-4F8D-A2E2-D4324AAB2CED) for more information about how to specify the PTF implementation package and use the `DBMS_TF` utilities
- [PIPELINED Clause](PIPELINED-clause.md) for the standalone or package polymorphic table function creation syntax and semantic

### Polymorphic Table Function Invocation

A polymorphic table function is invoked by specifying its name followed by the argument list in the `FROM` clause of a SQL query block.

The PTF arguments can be the standard scalar arguments that can be passed to a regular table function, but PTF's can additionally take a table argument. A table argument is either a `WITH` clause query or a schema-level object that is allowed in a `FROM` clause (such as tables, views, or table functions).

Syntax

table\_argument::= table \[ PARTITION BY column\_list \] \[ORDER BY order\_column\_list\]

column\_list::= identifier | ( identifier\[, identifier…\])

order\_column\_list::= order\_column\_name | (order\_column\_name \[, order\_column\_name…\])

order\_column\_name::= identifier \[ ASC | DESC \]\[ NULLS FIRST | NULLS LAST \]

Semantics

Each identifier is a column in the corresponding table.

The PTF has `Table Semantics`.

Query can optionally partition and order `Table Semantics` PTF input. This is disallowed for `Row Semantics` PTF input.

A polymorphic table function (PTF) cannot be the target of a DML statement. Any table argument of a PTF is passed in by name.

For example, the noop PTF can be used in a query such as:

```
SELECT * 
FROM noop(emp);
```

or

```
WITH e AS 
 (SELECT * FROM emp NATURAL JOIN dept)
SELECT t.* FROM noop(e) t;
```

The input table argument must be a basic table name.

The name resolution rules of the table identifier are (in priority order) as follows:
1. Identifier is resolved as a column name (such as a correlated column from an outer query block).
2. Identifier is resolved as a Common Table Expression (CTE) name in the current or some outer query-block. CTE is commonly known as the `WITH` clause.
3. Identifier is resolved as a schema-level table, view, or table-function (regular or polymorphic, and defined either at the schema-level or inside a package).

Many types of table expressions otherwise allowed in the `FROM` clause cannot be directly used as a table argument for a PTF (such as ANSI Joins, bind-variables, in-line views, `CURSOR` operators, `TABLE` operators). To use such table expressions as a PTF argument, these table expressions must be passed indirectly into a PTF by wrapping them in a CTE and then passing the CTE name into the PTF.

A PTF can be used as a table reference in the `FROM` clause and thus can be part of the ANSI Join and LATERAL syntax. Additionally, a PTF can be the source table for PIVOT/UNPIVOT and MATCH\_RECOGNIZE. Some table modification clauses that are meant for tables and views (such as SAMPLING, PARTITION, CONTAINERS) are disallowed for PTF.

Direct function composition of PTF is allowed (such as nested PTF cursor expression invocation or PTF(TF()) nesting). However, nested PTF is disallowed (such as PTF(PTF()) nesting).

The scalar arguments of a PTF can be any SQL scalar expression. While the constant scalar values are passed as-is to the `DESCRIBE` function, all other values are passed as NULLs. This is usually not a problem for the PTF implementation if these values are not row shape determining, but otherwise the `DESCRIBE` function can raise an error; typically the documentation accompanying the PTF will state which scalar parameters, if any, are shape defining and thus must have constant non-null values. Note, that during query execution (during `OPEN`, `FETCH_ROWS`, `CLOSE`) the expressions are evaluated and their actual values are passed to these PTF execution procedures. The return type is determined by the PTF invocation arguments list.

Query arguments are passed to PTF using a `WITH` clause.

The `TABLE` operator is optional when the table function arguments list or empty list () appears.

#### Variadic Pseudo-Operators

A variadic pseudo-operator operates with a variable number of operands.

Starting with Oracle Database Release 18c, we introduce the concept of variadic pseudo-operator into the SQL expression language to support Polymorphic Table Functions (PTF). A pseudo-operator can be used to pass list of identifiers (such as column name) to a PTF. A pseudo-operator can only appear as arguments to PTFs, and are parsed by the SQL compiler like other SQL operators or PL/SQL function invocation. A pseudo-operator has a variable number of arguments but must have at least one. The pseudo-operator does not have any execution function associated with it, and they are completely removed from the SQL cursor after the PTF compilation is finished. During SQL compilation, the pseudo-operators are converted to corresponding DBMS\_TF types and then passed to the `DESCRIBE` method. There is no output type associated with these operators. It is not possible to embed a pseudo-operator inside a general SQL expression.

#### COLUMNS Pseudo-Operator

You can use the COLUMNS pseudo-operator to specify arguments to a Polymorphic Table Function (PTF) invocation in the FROM clause of a SQL query block.

The `COLUMNS` pseudo-operator arguments specify the list of column names, or the list of column names with associated types.

Syntax

column\_operator::= COLUMNS ( column\_list )

column\_list::= column\_name\_list | column\_type\_list

column\_name\_list::= identifier \[, identifier... \]

column\_type\_list::= identifier column\_type \[, identifier column\_type…\]

Semantics

The `COLUMNS` pseudo-operator can only appear as an argument to a PTF. It cannot appear in any other SQL expression than the PTF expression itself.

The column\_type must be a scalar type.

### Polymorphic Table Function Compilation and Execution

The database fulfills the Polymorphic Table Functions (PTF) conductor role. As such, it is responsible for the PTF compilation, execution and its related states.

The database manages:
- The compilation state: This is the immutable state that is generated by `DESCRIBE` which is needed before execution.
- The execution state: This is the state used by the execution procedures of a `Table semantics` PTF.
.

See Also:

- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ARPLS-GUID-EAC49A1C-F4EB-48C8-B726-A143643A479C) for more information about how the database manages the compilation and execution states of the PTFs

### Polymorphic Table Function Optimization

A polymorphic table function (PTF) provides an efficient and scalable mechanism to extend the analytical capabilities of the database.

The key benefits are:

- Minimal data-movement: Only columns of interest are passed to PTF
- Predicates/Projections/Partitioning are/is pushed into underlying table/query (where semantically possible)
- Bulk data transfer into and out of PTF
- Parallelism is based on type of PTF and query specified partitioning (if any)

### Skip\_col Polymorphic Table Function Example

This PTF example demonstrates Row Semantics, Describe Only, package table function, and overloading features.

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ARPLS-GUID-2D97C0CD-6AD9-4F86-86E6-C806D688C57A) for more Polymorphic Table Function (PTF) examples

Example 12-36 Skip\_col Polymorphic Table Function Example

The skip\_col Polymorphic Table Function (PTF) returns all the columns in a table except the columns specified in the PTF input argument. The skip\_col PTF skips columns based on column names (overload 1) or columns data type (overload 2).

Live SQL:

You can view and run this example on Oracle Live SQL at [18c Skip\_col Polymorphic Table Function](https://livesql.oracle.com/apex/livesql/docs/lnpls/ptf/ptfskpcol.html)

Create the implementation package named skip\_col\_pkg containing the `DESCRIBE` function for the skip\_col polymorphic table function (PTF). The `DESCRIBE` function is invoked to determine the row shape produced by the PTF. It returns a `DBMS_TF.DESCRIBE_T` table. It is overloaded. The `FETCH_ROWS` procedure is not required because it does need to produce associated new column values for a given subset of rows.

```
CREATE PACKAGE skip_col_pkg AS

  -- OVERLOAD 1: Skip by name --
  FUNCTION skip_col(tab TABLE, 
                    col COLUMNS)
           RETURN TABLE PIPELINED ROW POLYMORPHIC USING skip_col_pkg;

  FUNCTION describe(tab IN OUT DBMS_TF.TABLE_T, 
                    col        DBMS_TF.COLUMNS_T)
           RETURN DBMS_TF.DESCRIBE_T;

  -- OVERLOAD 2: Skip by type --
  FUNCTION skip_col(tab       TABLE, 
                    type_name VARCHAR2,
                    flip      VARCHAR2 DEFAULT 'False') 
           RETURN TABLE PIPELINED ROW POLYMORPHIC USING skip_col_pkg;

  FUNCTION describe(tab       IN OUT DBMS_TF.TABLE_T, 
                    type_name        VARCHAR2, 
                    flip             VARCHAR2 DEFAULT 'False') 
           RETURN DBMS_TF.DESCRIBE_T;

END skip_col_pkg;
```

Create the implementation package body which contains the polymorphic table function definition.

```
CREATE PACKAGE BODY skip_col_pkg AS

/* OVERLOAD 1: Skip by name 
 * Package PTF name:  skip_col_pkg.skip_col
 * Standalone PTF name: skip_col_by_name
 *
 * PARAMETERS:
 * tab - The input table
 * col - The name of the columns to drop from the output
 *
 * DESCRIPTION:
 *   This PTF removes all the input columns listed in col from the output
 *   of the PTF.
*/  
 FUNCTION  describe(tab IN OUT DBMS_TF.TABLE_T, 
                    col        DBMS_TF.COLUMNS_T)
            RETURN DBMS_TF.DESCRIBE_T
  AS 
    new_cols DBMS_TF.COLUMNS_NEW_T;
    col_id   PLS_INTEGER := 1;
  BEGIN 
    FOR i IN 1 .. tab.column.count() LOOP
      FOR j IN 1 .. col.count() LOOP
        tab.column(i).PASS_THROUGH := tab.column(i).DESCRIPTION.NAME != col(j);
        EXIT WHEN NOT tab.column(i).PASS_THROUGH;
      END LOOP;
    END LOOP;

    RETURN NULL;
  END;  

/* OVERLOAD 2: Skip by type
 * Package PTF name:  skip_col_pkg.skip_col
 * Standalone PTF name: skip_col_by_type
 *
 * PARAMETERS:
 *   tab       - Input table
 *   type_name - A string representing the type of columns to skip
 *   flip      - 'False' [default] => Match columns with given type_name
 *               otherwise         => Ignore columns with given type_name
 *
 * DESCRIPTION:
 *   This PTF removes the given type of columns from the given table. 
*/ 
  FUNCTION describe(tab       IN OUT DBMS_TF.TABLE_T, 
                    type_name        VARCHAR2, 
                    flip             VARCHAR2 DEFAULT 'False') 
           RETURN DBMS_TF.DESCRIBE_T 
  AS 
    typ CONSTANT VARCHAR2(1024) := UPPER(TRIM(type_name));
  BEGIN 
    FOR i IN 1 .. tab.column.count() LOOP
       tab.column(i).PASS_THROUGH := 
         CASE UPPER(SUBSTR(flip,1,1))
           WHEN 'F' THEN DBMS_TF.column_type_name(tab.column(i).DESCRIPTION)!=typ
           ELSE          DBMS_TF.column_type_name(tab.column(i).DESCRIPTION) =typ
         END /* case */;
    END LOOP;

    RETURN NULL;
  END;

END skip_col_pkg;
```

Create a standalone polymorphic table function named skip\_col\_by\_name for overload 1. Specify exactly one formal argument of type `TABLE`, specify the return type of the PTF as `TABLE`, specify a `Row Semantics` PTF type, and indicate the PTF implementation package to use is skip\_col\_pkg.

```
CREATE FUNCTION skip_col_by_name(tab TABLE, 
                                 col COLUMNS)
                  RETURN TABLE PIPELINED ROW POLYMORPHIC USING skip_col_pkg;
```

Create a standalone polymorphic table function named skip\_col\_by\_type for overload 2. Specify exactly one formal argument of type `TABLE`, specify the return type of the PTF as `TABLE`, specify a `Row Semantics` PTF type, and indicate the PTF implementation package to use is skip\_col\_pkg.

```
CREATE FUNCTION skip_col_by_type(tab TABLE, 
                                 type_name VARCHAR2,
                                 flip VARCHAR2 DEFAULT 'False')
                  RETURN TABLE PIPELINED ROW POLYMORPHIC USING skip_col_pkg;
```

Invoke the package skip\_col PTF (overload 1) to report from the `SCOTT.DEPT` table only columns whose type is not `NUMBER`.

```
SELECT * FROM skip_col_pkg.skip_col(scott.dept, 'number');
```
```
DNAME          LOC
-------------- -------------
ACCOUNTING     NEW YORK
RESEARCH       DALLAS
SALES          CHICAGO
OPERATIONS     BOSTON
```

The same result can be achieved by invoking the standalone skip\_col\_by\_type PTF to report from the `SCOTT.DEPT` table only columns whose type is not `NUMBER`.

```
SELECT * FROM skip_col_by_type(scott.dept, 'number');
```
```
DNAME          LOC
-------------- -------------
ACCOUNTING     NEW YORK
RESEARCH       DALLAS
SALES          CHICAGO
OPERATIONS     BOSTON
```

Invoke the package skip\_col PTF (overload 2) to report from the `SCOTT.DEPT` table only columns whose type is `NUMBER`.

```
SELECT * FROM skip_col_pkg.skip_col(scott.dept, 'number', flip => 'True');
```
```
DEPTNO
----------
        10
        20
        30
        40
```

The same result can be achieved by invoking the standalone skip\_col\_by\_type PTF to report from the `SCOTT.DEPT` table only columns whose type is `NUMBER`.

```
SELECT * FROM skip_col_by_type(scott.dept, 'number', flip => 'True');
```
```
DEPTNO
----------
        10
        20
        30
        40
```

Invoke the package skip\_col PTF to report all employees in department 20 from the `SCOTT.EMP` table all columns except `COMM`, `HIREDATE` and `MGR`.

```
SELECT *
FROM skip_col_pkg.skip_col(scott.emp, COLUMNS(comm, hiredate, mgr))
WHERE deptno = 20;
```
```
EMPNO ENAME      JOB              SAL     DEPTNO
---------- ---------- --------- ---------- ----------
      7369 SMITH      CLERK            800         20
      7566 JONES      MANAGER         2975         20
      7788 SCOTT      ANALYST         3000         20
      7876 ADAMS      CLERK           1100         20
      7902 FORD       ANALYST         3000         20
```

### To\_doc Polymorphic Table Function Example

The to\_doc PTF example combines a list of specified columns into a single document column.

Example 12-37 To\_doc Polymorphic Table Function Example

The to\_doc PTF combines a list of columns into a document column constructed like a JSON object.

Live SQL:

You can view and run this example on Oracle Live SQL at [18c To\_doc Polymorphic Table Function](https://livesql.oracle.com/apex/livesql/docs/lnpls/ptf/ptftodoc.html)

Create the implementation package to\_doc\_p containing the `DESCRIBE` function and `FETCH_ROWS` procedure for the to\_doc polymorphic table function (PTF).

The PTF parameters are:
- tab: The input table (The tab parameter is of type `DBMS_TF`.`TABLE_T`, a table descriptor record type)
- cols (optional): The list of columns to convert to document. (The cols parameter is type `DBMS_TF`.`COLUMNS_T`, a column descriptor record type)

```
CREATE PACKAGE to_doc_p AS
   FUNCTION describe(tab      IN OUT DBMS_TF.TABLE_T,
                     cols     IN     DBMS_TF.COLUMNS_T DEFAULT NULL)
               RETURN DBMS_TF.DESCRIBE_T;
   
   PROCEDURE fetch_rows;
END to_doc_p;
```

Create the package containing the `DESCRIBE` function and `FETCH_ROWS` procedure. The `FETCH_ROWS` procedure is required to produce a new column named DOCUMENT in the output rowset. The `DESCRIBE` function indicates the read columns by annotating them in the input table descriptor, `TABLE_T`. Only the indicated read columns will be fetched and thus available for processing during `FETCH_ROWS`. The PTF invocation in a query can use the COLUMNS pseudo-operator to indicate which columns the query wants the PTF to read, and this information is passed to the `DESCRIBE` function which then in turn sets the `COLUMN_T`.`FOR_READ` boolean flag. Only scalar SQL data types are allowed for the read columns. The `COLUMN_T`.`PASS_THROUGH` boolean flag indicates columns that are passed from the input table of the PTF to the output, without any modifications.

```
CREATE PACKAGE BODY to_doc_p AS
   
FUNCTION describe(tab      IN OUT DBMS_TF.TABLE_T,
                  cols     IN     DBMS_TF.COLUMNS_T DEFAULT NULL)
            RETURN DBMS_TF.DESCRIBE_T AS
BEGIN
  FOR i IN 1 .. tab.column.count LOOP 
     CONTINUE WHEN NOT DBMS_TF.SUPPORTED_TYPE(tab.column(i).DESCRIPTION.TYPE);
     
      IF cols IS NULL THEN
         tab.column(i).FOR_READ     := TRUE;
         tab.column(i).PASS_THROUGH := FALSE;
         CONTINUE;
       END IF;
     
      FOR j IN 1 .. cols.count LOOP
        IF (tab.column(i).DESCRIPTION.NAME = cols(j)) THEN
            tab.column(i).FOR_READ     := TRUE;
            tab.column(i).PASS_THROUGH := FALSE;
        END IF;
      END LOOP;
     
  END LOOP;
      
  RETURN DBMS_TF.describe_t(new_columns => DBMS_TF.COLUMNS_NEW_T(1 =>
                              DBMS_TF.COLUMN_METADATA_T(name =>'DOCUMENT')));   
END;
   
 PROCEDURE fetch_rows AS 
      rst DBMS_TF.ROW_SET_T;
      col DBMS_TF.TAB_VARCHAR2_T;
      rct PLS_INTEGER;
 BEGIN
      DBMS_TF.GET_ROW_SET(rst, row_count => rct);
      FOR rid IN 1 .. rct LOOP 
           col(rid) := DBMS_TF.ROW_TO_CHAR(rst, rid); 
      END LOOP;
      DBMS_TF.PUT_COL(1, col);
 END; 
   
END to_doc_p;
```

Create the standalone to\_doc PTF. Specify exactly one formal argument of type `TABLE`, specify the return type of the PTF as `TABLE`, specify a Row Semantics PTF type, and indicate the PTF implementation package to use is to\_doc\_p.

```
CREATE FUNCTION to_doc(
                 tab  TABLE, 
                       cols  COLUMNS DEFAULT NULL) 
                       RETURN TABLE
    PIPELINED ROW POLYMORPHIC USING to_doc_p;
```

Invoke the to\_doc PTF to display all columns of table `SCOTT`.`DEPT` as one combined `DOCUMENT` column.

```
SELECT * FROM to_doc(scott.dept);
```
```
DOCUMENT
--------------------------------------------------
{"DEPTNO":10, "DNAME":"ACCOUNTING", "LOC":"NEW YORK"}
{"DEPTNO":20, "DNAME":"RESEARCH", "LOC":"DALLAS"}
{"DEPTNO":30, "DNAME":"SALES", "LOC":"CHICAGO"}
{"DEPTNO":40, "DNAME":"OPERATIONS", "LOC":"BOSTON"}
```

For all employees in departments 10 and 30, display the `DEPTNO`, `ENAME` and `DOCUMENT` columns ordered by `DEPTNO` and `ENAME`. Invoke the to\_doc PTF with the `COLUMNS` pseudo-operator to select columns `EMPNO`, `JOB`, `MGR`, `HIREDATE`, `SAL` and `COMM` of table `SCOTT`.`EMP`. The PTF combines these columns into the `DOCUMENT` column.

```
SELECT deptno, ename, document 
FROM   to_doc(scott.emp, COLUMNS(empno,job,mgr,hiredate,sal,comm))
WHERE  deptno IN (10, 30) 
ORDER BY 1, 2;
```
```
DEPTNO ENAME      DOCUMENT
------ ---------- ---------------------------------------------------------------------------------
    10 CLARK      {"EMPNO":7782, "JOB":"MANAGER", "MGR":7839, "HIREDATE":"09-JUN-81", "SAL":2450}
    10 KING       {"EMPNO":7839, "JOB":"PRESIDENT", "HIREDATE":"17-NOV-81", "SAL":5000}
    10 MILLER     {"EMPNO":7934, "JOB":"CLERK", "MGR":7782, "HIREDATE":"23-JAN-82", "SAL":1300}
    30 ALLEN      {"EMPNO":7499, "JOB":"SALESMAN", "MGR":7698, "HIREDATE":"20-FEB-81", "SAL":1600, "COMM":300}
    30 BLAKE      {"EMPNO":7698, "JOB":"MANAGER", "MGR":7839, "HIREDATE":"01-MAY-81", "SAL":2850}
    30 JAMES      {"EMPNO":7900, "JOB":"CLERK", "MGR":7698, "HIREDATE":"03-DEC-81", "SAL":950}
    30 MARTIN     {"EMPNO":7654, "JOB":"SALESMAN", "MGR":7698, "HIREDATE":"28-SEP-81", "SAL":1250, "COMM":1400}
    30 TURNER     {"EMPNO":7844, "JOB":"SALESMAN", "MGR":7698, "HIREDATE":"08-SEP-81", "SAL":1500, "COMM":0}
    30 WARD       {"EMPNO":7521, "JOB":"SALESMAN", "MGR":7698, "HIREDATE":"22-FEB-81", "SAL":1250, "COMM":500}
```

With the subquery named `E`, display the `DOC_ID` and `DOCUMENT` columns. Report all clerk employees, their salary, department and department location. Use the to\_doc PTF to combine the `NAME`, `SAL`, `DEPTNO` and `LOC` columns into the `DOCUMENT` column.

```
WITH e AS (
       SELECT ename name, sal, deptno, loc 
         FROM scott.emp NATURAL JOIN scott.dept 
        WHERE job = 'CLERK')
      SELECT ROWNUM doc_id, t.*
        FROM to_doc(e) t;
```
```
DOC_ID DOCUMENT
---------- -------------------------------------------------------
         1 {"NAME":"MILLER", "SAL":1300, "DEPTNO":10, "LOC":"NEW YORK"}
         2 {"NAME":"SMITH", "SAL":800, "DEPTNO":20, "LOC":"DALLAS"}
         3 {"NAME":"ADAMS", "SAL":1100, "DEPTNO":20, "LOC":"DALLAS"}
         4 {"NAME":"JAMES", "SAL":950, "DEPTNO":30, "LOC":"CHICAGO"}
```

Use a subquery block to display c1, c2, c3 column values converted into the `DOCUMENT` column.

```
WITH t(c1,c2,c3)  AS (
    SELECT NULL, NULL, NULL FROM dual 
    UNION ALL
    SELECT    1, NULL, NULL FROM dual 
    UNION ALL
    SELECT NULL,    2, NULL FROM dual 
    UNION ALL
    SELECT    0, NULL,    3 FROM dual)
  SELECT * 
    FROM to_doc(t);
```
```
DOCUMENT
---------------
{}
{"C1":1}
{"C2":2}
{"C1":0, "C3":3}
```

For all employees in department 30, display the values of the member with property names `ENAME` and `COMM`. The PTF invocation reporting from the `SCOTT`.`EMP` table produces the `DOCUMENT` column which can be used as input to the `JSON_VALUE` function. This function selects a scalar value from some JSON data.

```
SELECT JSON_VALUE(document, '$.ENAME') ename, 
       JSON_VALUE(document, '$.COMM')  comm 
FROM   to_doc(scott.emp)
WHERE  JSON_VALUE(document, '$.DEPTNO') = 30;
```
```
ENAME      COMM
---------- ----
ALLEN      300
WARD       500
MARTIN     1400
BLAKE
TURNER     0
JAMES
```

### Implicit\_echo Polymorphic Table Function Example

The implicit\_echo PTF example demonstrates that the USING clause is optional when the Polymorphic Table Function and the DESCRIBE function are defined in the same package.

Example 12-38 Implicit\_echo Polymorphic Table Function Example

The `implicit_echo` PTF, takes in a table and a column and produces a new column with the same value.

This PTF returns the column in the input table tab, and adds to it the column listed in cols but with the column names prefixed with `"ECHO_"`.

Create the implementation package `implicit_echo_package` containing the `DESCRIBE` function, `implicit_echo` polymorphic table function (PTF) and `FETCH_ROWS` procedure.

```
CREATE PACKAGE implicit_echo_package AS
  prefix   DBMS_ID := '"ECHO_';

  FUNCTION DESCRIBE(tab   IN OUT DBMS_TF.TABLE_T,
                    cols  IN     DBMS_TF.COLUMNS_T)
           RETURN DBMS_TF.DESCRIBE_T;
  
  PROCEDURE FETCH_ROWS;

  -- PTF FUNCTION: WITHOUT USING CLAUSE --
  FUNCTION implicit_echo(tab TABLE, cols COLUMNS)
           RETURN TABLE PIPELINED ROW POLYMORPHIC;

END implicit_echo_package;
```

Create the package containing the `DESCRIBE` function containing the input table parameter and the column parameter to be read. This function is invoked to determine the type of rows produced by the Polymorphic Table Function. The function returns a table `DBMS_TF.DESCRIBE_T`. The `FETCH_ROWS` procedure is required to produce the indicated read column along with a new column prefixed with `"ECHO_"` in the output rowset. The `implicit_echo` is the PTF function and contains two arguments, `tab` and `cols`, whose values are obtained from the query and this information is passed to the `DESCRIBE` function. The Row semantics specifies a PTF type but without the `USING` clause. This function is invoked from the SQL query.

Create the implementation package body `implicit_echo_package` which contains the PTF definition.

```
CREATE PACKAGE BODY implicit_echo_package AS

FUNCTION DESCRIBE(tab  IN  OUT DBMS_TF.TABLE_T,
                  cols IN      DBMS_TF.COLUMNS_T)
          RETURN DBMS_TF.DESCRIBE_T
AS
  new_cols DBMS_TF.COLUMNS_NEW_T;
  col_id   PLS_INTEGER := 1;

BEGIN
 FOR i in 1 .. tab.column.COUNT LOOP
 
   FOR j in 1 .. cols.COUNT LOOP
    
     IF (tab.column(i).description.name = cols(j)) THEN
       
       IF (NOT DBMS_TF.SUPPORTED_TYPE(tab.column(i).description.type)) THEN
            RAISE_APPLICATION_ERROR(-20102, 'Unsupported column type['||
                                    tab.column(i).description.type||']');
       END IF;

       tab.column(i).for_read := TRUE;
       new_cols(col_id)       := tab.column(i).description;
       new_cols(col_id).name  := prefix||
                                 REGEXP_REPLACE(tab.column(i).description.name,
                                                                      '^"|"$');
       col_id                 := col_id + 1;
       EXIT;

     END IF;

    END LOOP;

 END LOOP;

/* VERIFY ALL COLUMNS WERE FOUND */
 IF (col_id - 1 != cols.COUNT) then
    RAISE_APPLICATION_ERROR(-20101,'Column mismatch['||col_id-1||'],
                                                   ['||cols.COUNT||']');
 END IF;

 RETURN DBMS_TF.DESCRIBE_T(new_columns => new_cols);

END;

 PROCEDURE FETCH_ROWS AS
     rowset DBMS_TF.ROW_SET_T;
 BEGIN
         DBMS_TF.GET_ROW_SET(rowset);
         DBMS_TF.PUT_ROW_SET(rowset);
 END;

END implicit_echo_package;
```

Invoke the PTF to display ENAME column of table `SCOTT`.`EMP` and display it along with another column `ECHO_ENAME` having the same value.

```
SELECT ENAME, ECHO_ENAME
FROM implicit_echo_package.implicit_echo(SCOTT.EMP, COLUMNS(SCOTT.ENAME));
```
```
ENAME      ECHO_ENAME
---------- ----------
SMITH      SMITH
ALLEN      ALLEN
WARD       WARD
JONES      JONES
MARTIN     MARTIN
BLAKE      BLAKE
CLARK      CLARK
SCOTT      SCOTT
KING       KING
TURNER     TURNER
ADAMS      ADAMS
JAMES      JAMES
FORD       FORD
MILLER     MILLER
```