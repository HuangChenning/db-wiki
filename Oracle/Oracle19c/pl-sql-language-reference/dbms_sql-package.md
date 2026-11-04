---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/dbms_sql-package.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## DBMS\_SQL Package

The DBMS\_SQL package defines an entity called a SQL cursor number. Because the SQL cursor number is a PL/SQL integer, you can pass it across call boundaries and store it.

You must use the `DBMS_SQL` package to run a dynamic SQL statement if any of the following are true:

- You do not know the `SELECT` list until run time.
- You do not know until run time what placeholders in a `SELECT` or DML statement must be bound.
- You want a stored subprogram to return a query result implicitly (not through an `OUT` `REF` `CURSOR` parameter), which requires the `DBMS_SQL`.`RETURN_RESULT` procedure.

In these situations, you must use native dynamic SQL instead of the `DBMS_SQL` package:

- The dynamic SQL statement retrieves rows into records.
- You want to use the SQL cursor attribute `%FOUND`, `%ISOPEN`, `%NOTFOUND`, or `%ROWCOUNT` after issuing a dynamic SQL statement that is an `INSERT`, `UPDATE`, `DELETE`, `MERGE`, or single-row `SELECT` statement.

When you need both the `DBMS_SQL` package and native dynamic SQL, you can switch between them, using the functions `DBMS_SQL`.`TO_REFCURSOR` and `DBMS_SQL`.`TO_CURSOR_NUMBER`.

Topics

Note:

You can invoke `DBMS_SQL` subprograms remotely.

See Also:

- " [Native Dynamic SQL](native-dynamic-sql.md) "for information about native dynamic SQL
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ARPLS058) for more information about the `DBMS_SQL` package, including instructions for running a dynamic SQL statement that has an unknown number of input or output variables ("Method 4")

### DBMS\_SQL.RETURN\_RESULT Procedure

The `DBMS_SQL`.`RETURN_RESULT` procedure lets a stored subprogram return a query result implicitly to either the client program (which invokes the subprogram indirectly) or the immediate caller of the subprogram. After `DBMS_SQL`.`RETURN_RESULT` returns the result, only the recipient can access it.

The `DBMS_SQL`.`RETURN_RESULT` has two overloads:

```
PROCEDURE RETURN_RESULT (rc IN OUT SYS_REFCURSOR,
                         to_client IN BOOLEAN DEFAULT TRUE);

PROCEDURE RETURN_RESULT (rc IN OUT INTEGER,
                         to_client IN BOOLEAN DEFAULT TRUE);
```

The `rc` parameter is either an open cursor variable (`SYS_REFCURSOR`) or the cursor number (`INTEGER`) of an open cursor. To open a cursor and get its cursor number, invoke the `DBMS_SQL`.`OPEN_CURSOR` function, described in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ARPLS68275).

When the `to_client` parameter is `TRUE` (the default), the `DBMS_SQL`.`RETURN_RESULT` procedure returns the query result to the client program (which invokes the subprogram indirectly); when this parameter is `FALSE`, the procedure returns the query result to the subprogram's immediate caller.

See Also:

- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ARPLS73893) for more information about `DBMS_SQL`.`RETURN_RESULT`
- [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=LNOCI73008) for information about C and.NET support for implicit query results
- [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQPUG200) for information about SQL\*Plus support for implicit query results

Example 7-11 DBMS\_SQL.RETURN\_RESULT Procedure

In this example, the procedure `p` invokes `DBMS_SQL`.`RETURN_RESULT` without the optional `to_client` parameter (which is `TRUE` by default). Therefore, `DBMS_SQL`.`RETURN_RESULT` returns the query result to the subprogram client (the anonymous block that invokes `p`). After `p` returns a result to the anonymous block, only the anonymous block can access that result.

```
CREATE OR REPLACE PROCEDURE p AUTHID DEFINER AS
  c1 SYS_REFCURSOR;
  c2 SYS_REFCURSOR;
BEGIN
  OPEN c1 FOR
    SELECT first_name, last_name
    FROM employees
    WHERE employee_id = 176;
 
  DBMS_SQL.RETURN_RESULT (c1);
  -- Now p cannot access the result.
 
  OPEN c2 FOR
    SELECT city, state_province
    FROM locations
    WHERE country_id = 'AU';
 
  DBMS_SQL.RETURN_RESULT (c2);
  -- Now p cannot access the result.
END;
/
BEGIN
  p;
END;
/
```

Result:

```
ResultSet #1

FIRST_NAME           LAST_NAME
-------------------- -------------------------
Jonathon             Taylor

ResultSet #2

CITY                           STATE_PROVINCE
------------------------------ -------------------------
Sydney                         New South Wales
```

### DBMS\_SQL.GET\_NEXT\_RESULT Procedure

The `DBMS_SQL`.`GET_NEXT_RESULT` procedure gets the next result that the `DBMS_SQL`.`RETURN_RESULT` procedure returned to the recipient. The two procedures return results in the same order.

The `DBMS_SQL`.`GET_NEXT_RESULT` has two overloads:

```
PROCEDURE GET_NEXT_RESULT (c IN INTEGER, rc OUT SYS_REFCURSOR);

PROCEDURE GET_NEXT_RESULT (c IN INTEGER, rc OUT INTEGER);
```

The `c` parameter is the cursor number of an open cursor that directly or indirectly invokes a subprogram that uses the `DBMS_SQL`.`RETURN_RESULT` procedure to return a query result implicitly.

To open a cursor and get its cursor number, invoke the `DBMS_SQL`.`OPEN_CURSOR` function. `DBMS_SQL`.`OPEN_CURSOR` has an optional parameter, `treat_as_client_for_results`. When this parameter is `FALSE` (the default), the caller that opens this cursor (to invoke a subprogram) is not treated as the client that receives query results for the client from the subprogram that uses `DBMS_SQL`.`RETURN_RESULT` —those query results are returned to the client in a upper tier instead. When this parameter is `TRUE`, the caller is treated as the client. For more information about the `DBMS_SQL`.`OPEN_CURSOR` function, see [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ARPLS68275).

The `rc` parameter is either a cursor variable (`SYS_REFCURSOR`) or the cursor number (`INTEGER`) of an open cursor.

In Example 7-12, the procedure `get_employee_info` uses `DBMS_SQL`.`RETURN_RESULT` to return two query results to a client program and is invoked dynamically by the anonymous block `<<main>>`. Because `<<main>>` needs to receive the two query results that `get_employee_info` returns, `<<main>>` opens a cursor to invoke `get_employee_info` using `DBMS_SQL`.`OPEN_CURSOR` with the parameter `treat_as_client_for_results` set to `TRUE`. Therefore, `DBMS_SQL`.`GET_NEXT_RESULT` returns its results to `<<main>>`, which uses the cursor `rc` to fetch them.

Example 7-12 DBMS\_SQL.GET\_NEXT\_RESULT Procedure

```
CREATE OR REPLACE PROCEDURE get_employee_info (id IN VARCHAR2) AUTHID DEFINER AS
  rc  SYS_REFCURSOR;
BEGIN
  -- Return employee info
 
  OPEN rc FOR SELECT first_name, last_name, email, phone_number
              FROM employees
              WHERE employee_id = id;
  DBMS_SQL.RETURN_RESULT(rc);
 
  -- Return employee job history
 
  OPEN RC FOR SELECT job_title, start_date, end_date
              FROM job_history jh, jobs j
              WHERE jh.employee_id = id AND
                    jh.job_id = j.job_id
              ORDER BY start_date DESC;
  DBMS_SQL.RETURN_RESULT(rc);
END;
/
<<main>>
DECLARE
  c            INTEGER;
  rc           SYS_REFCURSOR;
  n            NUMBER;
 
  first_name   VARCHAR2(20);
  last_name    VARCHAR2(25);
  email        VARCHAR2(25);
  phone_number VARCHAR2(20);
 
  job_title    VARCHAR2(35);
  start_date   DATE;
  end_date     DATE;
 
BEGIN
 
  c := DBMS_SQL.OPEN_CURSOR(true);
  DBMS_SQL.PARSE(c, 'BEGIN get_employee_info(:id); END;', DBMS_SQL.NATIVE);
  DBMS_SQL.BIND_VARIABLE(c, ':id', 176);
  n := DBMS_SQL.EXECUTE(c);
 
  -- Get employee info
 
  dbms_sql.get_next_result(c, rc);
  FETCH rc INTO first_name, last_name, email, phone_number;
 
  DBMS_OUTPUT.PUT_LINE('Employee: '||first_name || ' ' || last_name);
  DBMS_OUTPUT.PUT_LINE('Email: ' ||email);
  DBMS_OUTPUT.PUT_LINE('Phone: ' ||phone_number);
 
  -- Get employee job history
 
  DBMS_OUTPUT.PUT_LINE('Titles:');
  DBMS_SQL.GET_NEXT_RESULT(c, rc);
  LOOP
    FETCH rc INTO job_title, start_date, end_date;
    EXIT WHEN rc%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE
      ('- '||job_title||' ('||start_date||' - ' ||end_date||')');
  END LOOP;
 
  DBMS_SQL.CLOSE_CURSOR(c);
END main;
/
```

Result:

```
Employee: Jonathon Taylor
Email: JTAYLOR
Phone: 011.44.1644.429265
Titles:
- Sales Manager (01-JAN-07 - 31-DEC-07)
- Sales Representative (24-MAR-06 - 31-DEC-06)
 
PL/SQL procedure successfully completed.
```

### DBMS\_SQL.TO\_REFCURSOR Function

The `DBMS_SQL`.`TO_REFCURSOR` function converts a SQL cursor number to a weak cursor variable, which you can use in native dynamic SQL statements.

Before passing a SQL cursor number to the `DBMS_SQL`.`TO_REFCURSOR` function, you must `OPEN`, `PARSE`, and `EXECUTE` it (otherwise an error occurs).

After you convert a SQL cursor number to a `REF` `CURSOR` variable, `DBMS_SQL` operations can access it only as the `REF` `CURSOR` variable, not as the SQL cursor number. For example, using the `DBMS_SQL`.`IS_OPEN` function to see if a converted SQL cursor number is still open causes an error.

Example 7-13 uses the `DBMS_SQL`.`TO_REFCURSOR` function to switch from the `DBMS_SQL` package to native dynamic SQL.

Example 7-13 Switching from DBMS\_SQL Package to Native Dynamic SQL

```
CREATE OR REPLACE TYPE vc_array IS TABLE OF VARCHAR2(200);
/
CREATE OR REPLACE TYPE numlist IS TABLE OF NUMBER;
/
CREATE OR REPLACE PROCEDURE do_query_1 (
  placeholder vc_array,
  bindvars vc_array,
  sql_stmt VARCHAR2
) AUTHID DEFINER
IS
  TYPE curtype IS REF CURSOR;
  src_cur     curtype;
  curid       NUMBER;
  bindnames   vc_array;
  empnos      numlist;
  depts       numlist;
  ret         NUMBER;
  isopen      BOOLEAN;
BEGIN
  -- Open SQL cursor number:
  curid := DBMS_SQL.OPEN_CURSOR;

  -- Parse SQL cursor number:
  DBMS_SQL.PARSE(curid, sql_stmt, DBMS_SQL.NATIVE);

  bindnames := placeholder;

  -- Bind variables:
  FOR i IN 1 .. bindnames.COUNT LOOP
    DBMS_SQL.BIND_VARIABLE(curid, bindnames(i), bindvars(i));
  END LOOP;

  -- Run SQL cursor number:
  ret := DBMS_SQL.EXECUTE(curid);

  -- Switch from DBMS_SQL to native dynamic SQL:
  src_cur := DBMS_SQL.TO_REFCURSOR(curid);
  FETCH src_cur BULK COLLECT INTO empnos, depts;

  -- This would cause an error because curid was converted to a REF CURSOR:
  -- isopen := DBMS_SQL.IS_OPEN(curid);

  CLOSE src_cur;
END;
/
```

### DBMS\_SQL.TO\_CURSOR\_NUMBER Function

The `DBMS_SQL`.`TO_CURSOR_NUMBER` function converts a `REF` `CURSOR` variable (either strong or weak) to a SQL cursor number, which you can pass to `DBMS_SQL` subprograms.

Before passing a `REF` `CURSOR` variable to the `DBMS_SQL`.`TO_CURSOR_NUMBER` function, you must `OPEN` it.

After you convert a `REF` `CURSOR` variable to a SQL cursor number, native dynamic SQL operations cannot access it.

Example 7-14 uses the `DBMS_SQL`.`TO_CURSOR_NUMBER` function to switch from native dynamic SQL to the `DBMS_SQL` package.

Example 7-14 Switching from Native Dynamic SQL to DBMS\_SQL Package

```
CREATE OR REPLACE PROCEDURE do_query_2 (
  sql_stmt VARCHAR2
) AUTHID DEFINER
IS
  TYPE curtype IS REF CURSOR;
  src_cur   curtype;
  curid     NUMBER;
  desctab   DBMS_SQL.DESC_TAB;
  colcnt    NUMBER;
  namevar   VARCHAR2(50);
  numvar    NUMBER;
  datevar   DATE;
  empno     NUMBER := 100;
BEGIN
  -- sql_stmt := SELECT ... FROM employees WHERE employee_id = :b1';

  -- Open REF CURSOR variable:
  OPEN src_cur FOR sql_stmt USING empno;

  -- Switch from native dynamic SQL to DBMS_SQL package:
  curid := DBMS_SQL.TO_CURSOR_NUMBER(src_cur);
  DBMS_SQL.DESCRIBE_COLUMNS(curid, colcnt, desctab);

  -- Define columns:
  FOR i IN 1 .. colcnt LOOP
    IF desctab(i).col_type = 2 THEN
      DBMS_SQL.DEFINE_COLUMN(curid, i, numvar);
    ELSIF desctab(i).col_type = 12 THEN
      DBMS_SQL.DEFINE_COLUMN(curid, i, datevar);
      -- statements
    ELSE
      DBMS_SQL.DEFINE_COLUMN(curid, i, namevar, 50);
    END IF;
  END LOOP;

  -- Fetch rows with DBMS_SQL package:
  WHILE DBMS_SQL.FETCH_ROWS(curid) > 0 LOOP
    FOR i IN 1 .. colcnt LOOP
      IF (desctab(i).col_type = 1) THEN
        DBMS_SQL.COLUMN_VALUE(curid, i, namevar);
      ELSIF (desctab(i).col_type = 2) THEN
        DBMS_SQL.COLUMN_VALUE(curid, i, numvar);
      ELSIF (desctab(i).col_type = 12) THEN
        DBMS_SQL.COLUMN_VALUE(curid, i, datevar);
        -- statements
      END IF;
    END LOOP;
  END LOOP;

  DBMS_SQL.CLOSE_CURSOR(curid);
END;
/
```