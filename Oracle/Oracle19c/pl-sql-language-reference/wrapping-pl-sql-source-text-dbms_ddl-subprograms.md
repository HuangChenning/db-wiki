---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/wrapping-pl-sql-source-text-dbms_ddl-subprograms.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Wrapping PL/SQL Source Text with DBMS\_DDL Subprograms

The `DBMS_DDL` package provides `WRAP` functions and `CREATE_WRAPPED` procedures, each of which wraps the PL/SQL source text of a single dynamically generated wrappable PL/SQL unit. The `DBMS_DDL` package also provides the exception `MALFORMED_WRAP_INPUT` (ORA-24230), which is raised if the input to `WRAP` or `CREATE_WRAPPED` is not a valid wrappable PL/SQL unit. (For the list of wrappable PL/SQL units, see the introduction to " [PL/SQL Source Text Wrapping](plsql-source-text-wrapping.md) ".)

Each `WRAP` function takes as input a single `CREATE` statement that creates a wrappable PL/SQL unit and returns an equivalent `CREATE` statement in which the PL/SQL source text is wrapped. For more information about the `WRAP` functions, see [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ARPLS66090).

Caution:

If you pass the statement that `DBMS_DDL`.`WRAP` returns to the `DBMS_SQL`.`PARSE` procedure whose formal parameter `statement` has data type `VARCHAR2A`, then you must set the `lfflg` parameter of `DBMS_SQL`.`PARSE` to `FALSE`. Otherwise, `DBMS_SQL`.`PARSE` adds lines to the wrapped PL/SQL unit, corrupting it. (For the syntax of `DBMS_SQL`.`PARSE`, see [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ARPLS68277).)

Each `CREATE_WRAPPED` procedure does what its corresponding `WRAP` function does and then runs the returned `CREATE` statement, creating the specified PL/SQL unit. For more information about the `CREATE_WRAPPED` procedures, see [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ARPLS66086).

Tip:

When invoking a `DBMS_DDL` subprogram, use the fully qualified package name, `SYS.DBMS_DDL`, to avoid name conflict if someone creates a local package named `DBMS_DDL` or defines the public synonym `DBMS_DDL`.

Note:

The `CREATE` statement that is input to a `WRAP` function or `CREATE_WRAPPED` procedure runs with the privileges of the user who invoked the subprogram.

Example A-4 dynamically creates a package specification (using the `EXECUTE` `IMMEDIATE` statement) and a wrapped package body, using a `CREATE_WRAPPED` procedure.

Example A-5 selects the text of the package that Example A-4 created, `emp_actions`, and then invokes the procedure `emp_actions.raise_salary`. If the package specification were wrapped, then the information needed to invoke the procedure would be unreadable, like the PL/SQL source text of the package body.

Example A-4 Creating Wrapped Package Body with CREATE\_WRAPPED Procedure

```
DECLARE
  package_text  VARCHAR2(32767); -- text for creating package spec and body
 
  FUNCTION generate_spec (pkgname VARCHAR2) RETURN VARCHAR2 AS
  BEGIN
    RETURN 'CREATE PACKAGE ' || pkgname || ' AUTHID CURRENT_USER AS
      PROCEDURE raise_salary (emp_id NUMBER, amount NUMBER);
      PROCEDURE fire_employee (emp_id NUMBER);
      END ' || pkgname || ';';
  END generate_spec;
 
  FUNCTION generate_body (pkgname VARCHAR2) RETURN VARCHAR2 AS
  BEGIN
    RETURN 'CREATE PACKAGE BODY ' || pkgname || ' AS
      PROCEDURE raise_salary (emp_id NUMBER, amount NUMBER) IS
      BEGIN
        UPDATE employees
          SET salary = salary + amount WHERE employee_id = emp_id;
      END raise_salary;
      PROCEDURE fire_employee (emp_id NUMBER) IS
      BEGIN
        DELETE FROM employees WHERE employee_id = emp_id;
      END fire_employee;
    END ' || pkgname || ';';
  END generate_body;
 
BEGIN
  package_text := generate_spec('emp_actions');  -- Generate package spec
  EXECUTE IMMEDIATE package_text;                -- Create package spec
  package_text := generate_body('emp_actions');  -- Generate package body
  SYS.DBMS_DDL.CREATE_WRAPPED(package_text);     -- Create wrapped package body
END;
/
```

Example A-5 Viewing Package with Wrapped Body and Invoking Package Procedure

Select text of package:

```
SELECT text FROM USER_SOURCE WHERE name = 'EMP_ACTIONS';
```

Result:

```
TEXT
------------------------------------------------------------------------
 
PACKAGE emp_actions AUTHID CURRENT_USER AS
      PROCEDURE raise_salary (emp_id NUMBER, amount NUMBER);
      PROCEDURE fire_employee (emp_id NUMBER);
      END emp_actions;
PACKAGE BODY emp_actions wrapped
a000000
1f
abcd
abcd
abcd
abcd
abcd
abcd
abcd
abcd
abcd
abcd
abcd
abcd
abcd
abcd
abcd
b
180 113
1fOVodewm7j9dBOmBsiEQz0BKCgwg/BKoZ4VZy/pTBIYo8Uj1sjpbEz08Ck3HMjYq/Mf0XZn
u9D0Kd+i89g9ZO61I6vZYjw2AuBidnLESyR63LHZpFD/7lyDTfF1eDY5vmNwLTXrFaxGy243
0lHKAzmOlwwfBWylkZZNi2UnpmSIe6z/BU2nhbwfpqd224p69FwYVXmFX2H5IMsdZ2/vWsK9
cDMCD1KEqOnPpbU2yXdpW3GIbGD8JFIbKAfpJLkoLfVxoRPXQfj0h1k=
```

Invoke `raised_salary` and show its effect:

```
DECLARE
  s employees.salary%TYPE;
BEGIN
  SELECT salary INTO s FROM employees WHERE employee_id=130;
  DBMS_OUTPUT.PUT_LINE('Old salary: ' || s);
  emp_actions.raise_salary(130, 100);
  SELECT salary INTO s FROM employees WHERE employee_id=130;
  DBMS_OUTPUT.PUT_LINE('New salary: ' || s);
END;
/
```

Result:

```
Old salary: 3557.4
New salary: 3657.4
 
PL/SQL procedure successfully completed.
```