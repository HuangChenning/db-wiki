---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/wrapping-pl-sql-source-text-pl-sql-wrapper-utility.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Wrapping PL/SQL Source Text with PL/SQL Wrapper Utility

The PL/SQL Wrapper utility takes a single SQL file (such as a SQL\*Plus script) and produces an equivalent text file in which the PL/SQL source text of each wrappable PL/SQL unit is wrapped.

Note:

Oracle recommends using PL/SQL Wrapper Utility version 10 or later.

For the list of wrappable PL/SQL units, see the introduction to " [PL/SQL Source Text Wrapping](plsql-source-text-wrapping.md) ".

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