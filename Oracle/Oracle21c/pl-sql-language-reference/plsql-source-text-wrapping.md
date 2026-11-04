---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: F31827-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/lnpls/plsql-source-text-wrapping.html
tags:
  - oracle
  - 21c
  - pl-sql-language-reference
---

You can wrap the PL/SQL source text for any of these stored PL/SQL units, thereby preventing anyone from displaying that text with the static data dictionary views `*_SOURCE`:

- Package specification
- Package body
- Type specification
- Type body
- Function
- Procedure

Note:

Wrapping text is low-assurance security. For high-assurance security, use Oracle Database Vault, described in [Oracle Database Vault Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=DVADM-GUID-0C8AF1B2-6CE9-4408-BFB3-7B2C7F9E7284).

A file containing wrapped PL/SQL source text is called a wrapped file. A wrapped file can be moved, backed up, or processed by SQL\*Plus or the Import and Export utilities.

To produce a wrapped file, use either the PL/SQL Wrapper utility or a `DBMS_DDL` subprogram. The PL/SQL Wrapper utility wraps the source text of every wrappable PL/SQL unit created by a specified SQL file. The `DBMS_DDL` subprograms wrap the source text of single dynamically generated wrappable PL/SQL units.

Both the PL/SQL Wrapper utility and `DBMS_DDL` subprograms detect tokenization errors (for example, runaway strings), but not syntax or semantic errors (for example, nonexistent tables or views).

By default, the 12.2 PL/SQL compiler can use wrapped packages that were compiled with the 9.2 PL/SQL compiler. To prevent the 12.2 PL/SQL compiler from using wrapped packages that were compiled with the 9.2 PL/SQL compiler, set the PL/SQL compilation parameter `PERMIT_92_WRAP_FORMAT` to `FALSE`. For more information about `PERMIT_92_WRAP_FORMAT`, see [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=REFRN10317). For more information about PL/SQL compilation parameters, see " [PL/SQL Units and Compilation Parameters](overview.md) ".

Topics

### A.1 PL/SQL Source Text Wrapping Limitations

- Wrapped files are not downward-compatible between Oracle Database releases.
	For example, you cannot load files produced by the version n.1 PL/SQL Wrapper utility into a version (n-1).2 Oracle Database. Nor can you load files produced by the version n.2 PL/SQL Wrapper utility into a version n.1 Oracle Database. Wrapped files are both upward- and downward-compatible across patch sets.
- Wrapping PL/SQL source text is not a secure way to hide passwords or table names.
	For high-assurance security, use Oracle Database Vault, described in [Oracle Database Vault Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=DVADM-GUID-0C8AF1B2-6CE9-4408-BFB3-7B2C7F9E7284).
- You cannot wrap the PL/SQL source text of triggers.
	To hide the implementation details of a trigger, put them in a stored subprogram, wrap the subprogram, and write a one-line trigger that invokes the subprogram.

### A.2 PL/SQL Source Text Wrapping Guidelines

- Wrap only the body of a package or type, not the specification.
	Leaving the specification unwrapped allows other developers to see the information needed to use the package or type (see Example A-5). Wrapping the body prevents them from seeing the package or type implementation.
- Wrap files only after you have finished editing them.
	You cannot edit wrapped files. If a wrapped file needs changes, you must edit the original unwrapped file and then wrap it.
- Before distributing a wrapped file, view it in a text editor and ensure that all important parts are wrapped.

### A.3 Wrapping PL/SQL Source Text with PL/SQL Wrapper Utility

The PL/SQL Wrapper utility takes a single SQL file (such as a SQL\*Plus script) and produces an equivalent text file in which the PL/SQL source text of each wrappable PL/SQL unit is wrapped.

Note:

Oracle recommends using PL/SQL Wrapper Utility version 10 or later.

For the list of wrappable PL/SQL units, see the introduction to " PL/SQL Source Text Wrapping ".

The PL/SQL Wrapper utility cannot connect to Oracle Database. To run the PL/SQL Wrapper utility, enter this command at the operating system prompt (with no spaces around the equal signs):

```
wrap iname=input_file [ oname=output_file ] [ keep_comments=yes ]
```

`input_file` is the name of an existing file that contains any combination of SQL statements. `output_file` is the name of the file that the PL/SQL Wrapper utility creates—the wrapped file.

Note:

`input_file` cannot include substitution variables specified with the SQL\*Plus `DEFINE` notation, because `output_file` is parsed by the PL/SQL compiler, not by SQL\*Plus.

The PL/SQL Wrapper utility deletes all comments from the wrapped file unless `keep_comments=yes` is specified. When `keep_comments=yes` is specified, only the comments outside the source are kept.

Note:

If `input_file` is a wrapped file, then `input_file` and `output_file` have identical contents.

The default file extension for `input_file` is `sql`. The default name of `output_file` is `input_file``.plb`. Therefore, these commands are equivalent:

```
wrap iname=/mydir/myfile
wrap iname=/mydir/myfile.sql oname=/mydir/myfile.plb
```

This example specifies a different file extension for `input_file` and a different name for `output_file`:

```
wrap iname=/mydir/myfile.src oname=/yourdir/yourfile.out keep_comments=yes
```

You can run `output_file` as a script in SQL\*Plus. For example:

```
SQL> @myfile.plb;
```

Example A-1 SQL File with Two Wrappable PL/SQL Units

This example shows the text of a SQL file, `wraptest2.sql`, that contains two wrappable PL/SQL units—the procedure `wraptest` and the function `fibonacci`. The file also contains comments and a SQL `SELECT` statement.

```
-- The following statement will not change.
 
SELECT COUNT(*) FROM EMPLOYEES
/
 
/* The PL/SQL source text of the following two CREATE statements will be wrapped. */
 
CREATE PROCEDURE wraptest AUTHID CURRENT_USER /* C style comment in procedure declaration */ IS
  TYPE emp_tab IS TABLE OF employees%ROWTYPE INDEX BY PLS_INTEGER;
  all_emps  emp_tab;
BEGIN
  SELECT * BULK COLLECT INTO all_emps FROM employees;
  FOR i IN 1..10 LOOP /* C style in pl/sql source */
    DBMS_OUTPUT.PUT_LINE('Emp Id: ' || all_emps(i).employee_id);
  END LOOP;
END;
/
 
CREATE OR REPLACE FUNCTION fibonacci (
  n PLS_INTEGER
) RETURN PLS_INTEGER
AUTHID CURRENT_USER -- PL/SQL style comment inside fibonacci function spec
IS
  fib_1 PLS_INTEGER := 0;
  fib_2 PLS_INTEGER := 1;
BEGIN
  IF n = 1 THEN                              -- terminating condition
    RETURN fib_1;
  ELSIF n = 2 THEN
    RETURN fib_2;                           -- terminating condition
  ELSE
    RETURN fibonacci(n-2) + fibonacci(n-1);  -- recursive invocations
  END IF;
END;
/
```

Example A-2 Wrapping File with PL/SQL Wrapper Utility

This example uses the PL/SQL Wrapper utility to wrap `wraptest2.sql` and shows the wrapped file, `wraptest2.plb`. The wrapped file shows that the utility deleted the comments inside the code and wrapped (made unreadable) the PL/SQL source text of the procedure `wraptest` and the function `fibonacci`, but kept the comments outside the wrapped source.

Assume that the operating system prompt is `>`. Wrap the file `wraptest.sql`:

```
> wrap keep_comments=yes iname=wraptest2.sql
```

Result:

```
Processing wraptest2.sql to wraptest2.plb
```

Contents of `wraptest.plb`:

```
-- The following statement will not change. 
 
SELECT COUNT(*) FROM EMPLOYEES
/
 
/* The PL/SQL source text of the following two CREATE statements will be wrapped. */
CREATE OR REPLACE PROCEDURE wraptest wrapped 
a000000
1
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
7
129 138
qf4HggDBeNMPlWAsPn6pGf+2LGwwg+nwJK5qZ3SVWE4+GayDZaL1bF7RwYm2/zr1qjZY3FrN
48M1bKc/MG5aY9YB+DrtT4SJN370Rpq7ck5D0sc1D5sKAwTyX13HYvRmjwkdXa0vEZ4q/mCU
EQusX23UZbZjxha7CtlCDCx8guGw/M/oHZXc8wDHXL8V8OsqQMv/Hj7z68gINl7OstalRScr
uSZ/l/W1YaaA9Lj8Fbx5/nJw96ZNy1SCY8VsB/G6O5f/65+EDxdThpnfU4e1vrrE9iB3/IpI
+7fE1Tv29fwc+aZq3S7O

/
 
CREATE OR REPLACE FUNCTION fibonacci wrapped 
a000000
1
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
8
150 ff
BFDvTL9OR04SJbx+qOy5H/h8IcwwgxDcAJnWZ3TNz51mjAmegdQcpNJfq8hUuQtv1Y5xg7Wd
KqMH/HBANhnZ+E1mBWekavYjPxlqV9zIFqZAgB4SBqkqe42sai9Vb0cLEU02/ZCEyxDSfWf3
H1Lp6U9ztRXNy+oDZSNykWCUVLaZro0UmeFrNUBqzE6j9mI3AyRhPw1QbZX5oRMLgLOG3OtS
SGJsz7M+bnhnp+xP4ww+SIlxx5LhDtnyPw==

/
```

Example A-3 Running Wrapped File and Viewing Wrapped PL/SQL Units

In SQL\*Plus, this example runs the wrapped file `wraptest.plb`, creating the procedure `wraptest` and the function `fibonacci`; selects the text of the subprograms (which is wrapped and therefore unreadable), and then invokes the subprograms.

```
SQL> -- Run wrapped file:
SQL> 
SQL> @wraptest2.plb
SQL> -- The following statement will not change.
SQL> 
SQL> SELECT COUNT(*) FROM EMPLOYEES
  2  /
 
  COUNT(*)
----------
       107
 
1 row selected.

SQL> /* The PL/SQL source text of the following two CREATE statements will be wrapped. */
 
SQL> CREATE PROCEDURE wraptest wrapped
   2  a000000
  3  1
  4  abcd
  5  abcd
  6  abcd
  7  abcd
  8  abcd
  9  abcd
 10  abcd
 11  abcd
 12  abcd
 13  abcd
 14  abcd
 15  abcd
 16  abcd
 17  abcd
 18  abcd
 19  7
 20  129 138
 21  qf4HggDBeNMPlWAsPn6pGf+2LGwwg+nwJK5qZ3SVWE4+GayDZaL1bF7RwYm2/zr1qjZY3FrN
 22  48M1bKc/MG5aY9YB+DrtT4SJN370Rpq7ck5D0sc1D5sKAwTyX13HYvRmjwkdXa0vEZ4q/mCU
 23  EQusX23UZbZjxha7CtlCDCx8guGw/M/oHZXc8wDHXL8V8OsqQMv/Hj7z68gINl7OstalRScr
 24  uSZ/l/W1YaaA9Lj8Fbx5/nJw96ZNy1SCY8VsB/G6O5f/65+EDxdThpnfU4e1vrrE9iB3/IpI
 25  +7fE1Tv29fwc+aZq3S7O
 26  
 27  /
 
Procedure created.
 
SQL> CREATE OR REPLACE FUNCTION fibonacci wrapped
 2  a000000
  3  1
  4  abcd
  5  abcd
  6  abcd
  7  abcd
  8  abcd
  9  abcd
 10  abcd
 11  abcd
 12  abcd
 13  abcd
 14  abcd
 15  abcd
 16  abcd
 17  abcd
 18  abcd
 19  8
 20  150 ff
 21  BFDvTL9OR04SJbx+qOy5H/h8IcwwgxDcAJnWZ3TNz51mjAmegdQcpNJfq8hUuQtv1Y5xg7Wd
 22  KqMH/HBANhnZ+E1mBWekavYjPxlqV9zIFqZAgB4SBqkqe42sai9Vb0cLEU02/ZCEyxDSfWf3
 23  H1Lp6U9ztRXNy+oDZSNykWCUVLaZro0UmeFrNUBqzE6j9mI3AyRhPw1QbZX5oRMLgLOG3OtS
 24  SGJsz7M+bnhnp+xP4ww+SIlxx5LhDtnyPw==
 25  
 26  /
 
Function created.
 
SQL> 
SQL> -- Try to display procedure source text:
SQL> 
SQL> SELECT text FROM USER_SOURCE WHERE name='WRAPTEST';
 
TEXT
--------------------------------------------------------------------------------
PROCEDURE wraptest wrapped
a000000
1
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
7
129 138
qf4HggDBeNMPlWAsPn6pGf+2LGwwg+nwJK5qZ3SVWE4+GayDZaL1bF7RwYm2/zr1qjZY3FrN
48M1bKc/MG5aY9YB+DrtT4SJN370Rpq7ck5D0sc1D5sKAwTyX13HYvRmjwkdXa0vEZ4q/mCU
EQusX23UZbZjxha7CtlCDCx8guGw/M/oHZXc8wDHXL8V8OsqQMv/Hj7z68gINl7OstalRScr
uSZ/l/W1YaaA9Lj8Fbx5/nJw96ZNy1SCY8VsB/G6O5f/65+EDxdThpnfU4e1vrrE9iB3/IpI
+7fE1Tv29fwc+aZq3S7O
 
 
1 row selected.
 
SQL> 
SQL> -- Try to display function source text:
SQL> 
SQL> SELECT text FROM USER_SOURCE WHERE name='FIBONACCI';
 
TEXT
--------------------------------------------------------------------------------
FUNCTION fibonacci wrapped
a000000
1
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
8
150 ff
BFDvTL9OR04SJbx+qOy5H/h8IcwwgxDcAJnWZ3TNz51mjAmegdQcpNJfq8hUuQtv1Y5xg7Wd
KqMH/HBANhnZ+E1mBWekavYjPxlqV9zIFqZAgB4SBqkqe42sai9Vb0cLEU02/ZCEyxDSfWf3
H1Lp6U9ztRXNy+oDZSNykWCUVLaZro0UmeFrNUBqzE6j9mI3AyRhPw1QbZX5oRMLgLOG3OtS
SGJsz7M+bnhnp+xP4ww+SIlxx5LhDtnyPw==
 
 
1 row selected.
 
SQL> 
SQL> BEGIN
  2    wraptest;  -- invoke procedure
  3    DBMS_OUTPUT.PUT_LINE('fibonacci(5) = ' || fibonacci(5));
  4  END;
  5  /
Emp Id: 100
Emp Id: 101
Emp Id: 102
Emp Id: 103
Emp Id: 104
Emp Id: 105
Emp Id: 106
Emp Id: 107
Emp Id: 108
Emp Id: 109
fibonacci(5) = 3
 
PL/SQL procedure successfully completed.
 
SQL>
```

### A.4 Wrapping PL/SQL Source Text with DBMS\_DDL Subprograms

The `DBMS_DDL` package provides `WRAP` functions and `CREATE_WRAPPED` procedures, each of which wraps the PL/SQL source text of a single dynamically generated wrappable PL/SQL unit. The `DBMS_DDL` package also provides the exception `MALFORMED_WRAP_INPUT` (ORA-24230), which is raised if the input to `WRAP` or `CREATE_WRAPPED` is not a valid wrappable PL/SQL unit. (For the list of wrappable PL/SQL units, see the introduction to " PL/SQL Source Text Wrapping ".)

Each `WRAP` function takes as input a single `CREATE` statement that creates a wrappable PL/SQL unit and returns an equivalent `CREATE` statement in which the PL/SQL source text is wrapped. For more information about the `WRAP` functions, see [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=ARPLS66090).

Caution:

If you pass the statement that `DBMS_DDL`.`WRAP` returns to the `DBMS_SQL`.`PARSE` procedure whose formal parameter `statement` has data type `VARCHAR2A`, then you must set the `lfflg` parameter of `DBMS_SQL`.`PARSE` to `FALSE`. Otherwise, `DBMS_SQL`.`PARSE` adds lines to the wrapped PL/SQL unit, corrupting it. (For the syntax of `DBMS_SQL`.`PARSE`, see [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=ARPLS68277).)

Each `CREATE_WRAPPED` procedure does what its corresponding `WRAP` function does and then runs the returned `CREATE` statement, creating the specified PL/SQL unit. For more information about the `CREATE_WRAPPED` procedures, see [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=ARPLS66086).

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