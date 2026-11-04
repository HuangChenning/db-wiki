---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/VARIABLE.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
VAR[IABLE] [variable [type [=value]]]
```

Declares a bind variable that can be referenced in PL/SQL, or lists the current display characteristics for a single variable or all variables.

type represents one of the following:

```
NUMBER CHAR CHAR (n [CHAR | BYTE]) NCHAR NCHAR (n) VARCHAR2 (n [CHAR | BYTE]) NVARCHAR2 (n) CLOB NCLOB REFCURSOR BINARY_FLOAT BINARY_DOUBLE
```

VARIABLE without arguments displays a list of all the variables declared in the session. VARIABLE followed only by a variable name lists that variable.

To free resources used by CLOB and NCLOB bind variables, you may need to manually free temporary LOBs with:

```
EXECUTE DBMS_LOB.FREETEMPORARY(:cv)
```

See [About Using Bind Variables](using-substitution-variables-sqlplus.md) for more information on bind variables. See your [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=LNPLS) for more information about PL/SQL.

Terms

```
variable
```

Represents the name of the bind variable you wish to create.

```
value
```

Allows you to assign a value to a variable for input binding.

```
NUMBER
```

Creates a variable of type NUMBER with fixed length.

```
CHAR
```

Creates a variable of type CHAR (character) with length one.

```
CHAR (n[CHAR | BYTE])
```

Creates a variable of type CHAR with length n bytes or n characters. The maximum that n can be is 2000 bytes, and the minimum is 1 byte or 1 character. The maximum n for a CHAR variable with character semantics is determined by the number of bytes required to store each character for the chosen character set, with an upper limit of 2000 bytes. The length semantics are determined by the length qualifiers CHAR or BYTE, and if not explicitly stated, the value of the NLS\_LENGTH\_SEMANTICS environment variable is applied to the bind variable. Explicitly stating the length semantics at variable definition stage will always take precedence over the NLS\_LENGTH\_SEMANTICS setting.

```
NCHAR
```

Creates a variable of type NCHAR (national character) with length one.

```
NCHAR (n)
```

Creates a variable of type NCHAR with length n characters. The maximum that n can be is determined by the number of bytes required to store each character for the chosen national character set, with an upper limit of 2000 bytes. The only exception to this is when a SQL\*Plus session is connected to a pre Oracle9i server, or the SQLPLUSCOMPATIBILITY system variable is set to a version less than 9.0.0. In this case the length n can be in bytes or characters depending on the chosen national character set, with the upper limit of 2000 bytes still retained.

```
VARCHAR2 (n[CHAR | BYTE])
```

Creates a variable of type VARCHAR2 with length of up to n bytes or n characters. The maximum that n can be is 32k bytes (see note), and the minimum is 1 byte or 1 character. The maximum n for a VARCHAR2 variable with character semantics is determined by the number of bytes required to store each character for the chosen character set, with an upper limit of 32k bytes. The length semantics are determined by the length qualifiers CHAR or BYTE, and if not explicitly stated, the value of the NLS\_LENGTH\_SEMANTICS environment variable is applied to the bind variable. Explicitly stating the length semantics at variable definition stage will always take precedence over the NLS\_LENGTH\_SEMANTICS setting.

Note:

By default, the maximum VARCHAR2 length is 4000 bytes. Attempting to use a maximum length greater than 4000 bytes raises ORA-01460: unimplemented or unreasonable conversion requested

To enable 32k maximum length, you must add the MAX\_STRING\_SIZE=extended parameter to your `init.ora` file.

```
NVARCHAR2 (n)
```

Creates a variable of type NVARCHAR2 with length of up to n characters. The maximum that n can be is determined by the number of bytes required to store each character for the chosen national character set, with an upper limit of 32k bytes (see note). The only exception to this is when a SQL\*Plus session is connected to a pre Oracle9i server, or the SQLPLUSCOMPATIBILITY system variable is set to a version less than 9.0.0. In this case the length n can be in bytes or characters depending on the chosen national character set, with the upper limit of 32k bytes still retained.

Note:

By default,, the maximum NVARCHAR2 length is 4000 bytes. Attempting to use a maximum length greater than 4000 bytes raises ORA-01460: unimplemented or unreasonable conversion requested

To enable 32k maximum length, you must add the MAX\_STRING\_SIZE=extended parameter to your `init.ora` file.

```
CLOB
```

Creates a variable of type CLOB.

```
NCLOB
```

Creates a variable of type NCLOB.

```
REFCURSOR
```

Creates a variable of type REF CURSOR.

```
BINARY_FLOAT
```

Creates a variable of type BINARY\_FLOAT. BINARY\_FLOAT is a floating-point number that conforms substantially with the Institute for Electrical and Electronics Engineers (IEEE) Standard for Binary Floating-Point Arithmetic, IEEE Standard 754-1985.

```
BINARY_DOUBLE
```

Creates a variable of type BINARY\_DOUBLE. BINARY\_DOUBLE is a floating-point number that conforms substantially with the Institute for Electrical and Electronics Engineers (IEEE) Standard for Binary Floating-Point Arithmetic, IEEE Standard 754-1985.

Usage

Bind variables may be used as parameters to stored procedures, or may be directly referenced in anonymous PL/SQL blocks.

To display the value of a bind variable created with VARIABLE, use the PRINT command. See [PRINT](PRINT.md) for more information.

To automatically display the value of a bind variable created with VARIABLE, use the SET AUTOPRINT command. See [SET AUTOP\[RINT\] {ON | OFF}](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/SET-system-variable-summary.html#GUID-82D529C1-ACF3-4A8C-A58C-9CCC6D12AC1D) for more information.

Bind variables cannot be used in the COPY command or SQL statements, except in PL/SQL blocks. Instead, use substitution variables.

When you execute a VARIABLE... CLOB or NCLOB command, SQL\*Plus associates a LOB locator with the bind variable. The LOB locator is automatically populated when you execute a SELECT clob\_column INTO:cv statement in a PL/SQL block. SQL\*Plus closes the LOB locator when you exit SQL\*Plus.

To free resources used by CLOB and NCLOB bind variables, you may need to manually free temporary LOBs with:

```
EXECUTE DBMS_LOB.FREETEMPORARY(:cv)
```

All temporary LOBs are freed when you exit SQL\*Plus.

SQL\*Plus SET commands such as SET LONG and SET LONGCHUNKSIZE and SET LOBOFFSET may be used to control the size of the buffer while PRINTing CLOB or NCLOB bind variables.

SQL\*Plus REFCURSOR bind variables may be used to reference PL/SQL 2.3 or higher Cursor Variables, allowing PL/SQL output to be formatted by SQL\*Plus. For more information on PL/SQL Cursor Variables, see [Cursor Variables](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=LNPLS-GUID-4A6E054A-4002-418D-A1CA-DE849CD7E6D5).

When you execute a VARIABLE... REFCURSOR command, SQL\*Plus creates a cursor bind variable. The cursor is automatically opened by an OPEN... FOR SELECT statement referencing the bind variable in a PL/SQL block. SQL\*Plus closes the cursor after completing a PRINT statement for that bind variable, or on exit.

SQL\*Plus formatting commands such as BREAK, COLUMN, COMPUTE and SET may be used to format the output from PRINTing a REFCURSOR.

A REFCURSOR bind variable may not be PRINTed more than once without re-executing the PL/SQL OPEN... FOR statement.

Examples

The following example illustrates creating a bind variable, changing its value, and displaying its current value.

To create a bind variable, enter:

```
VARIABLE ret_val NUMBER
```

To change this bind variable in SQL\*Plus, you must use a PL/SQL block:

```
BEGIN
 :ret_val:=4;
END;
/
```
```
PL/SQL procedure successfully completed.
```

To display the value of the bind variable in SQL\*Plus, enter:

```
PRINT ret_val
```
```
RET_VAL
----------
         4
```

The following example illustrates creating a bind variable and then setting it to the value returned by a function:

```
VARIABLE id NUMBER
BEGIN
  :id := EMP_MANAGEMENT.HIRE
  ('BLAKE','MANAGER','KING',2990,'SALES');
END;
/
```

The value returned by the stored procedure is being placed in the bind variable,:id. It can be displayed with the PRINT command or used in subsequent PL/SQL subprograms.

The following example illustrates automatically displaying a bind variable:

```
SET AUTOPRINT ON
VARIABLE a REFCURSOR
BEGIN
  OPEN :a FOR SELECT LAST_NAME, CITY, DEPARTMENT_ID
  FROM EMP_DETAILS_VIEW
  WHERE SALARY > 12000
  ORDER BY DEPARTMENT_ID;
END;
/
```
```
PL/SQL procedure successfully completed.
LAST_NAME                  CITY                            DEPARTMENT_ID
-------------------------  ------------------------------  -------------
Hartstein                  Toronto                                    20
Russell                    Oxford                                     80
Partners                   Oxford                                     80
King                       Seattle                                    90
Kochhar                    Seattle                                    90
De Haan                    Seattle                                    90

6 rows selected.
```

In the above example, there is no need to issue a PRINT command to display the variable.

The following example creates some variables:

```
VARIABLE id NUMBER
VARIABLE txt CHAR (20)
VARIABLE myvar REFCURSOR
```

Enter VARIABLE with no arguments to list the defined variables:

```
VARIABLE
```
```
variable id
datatype NUMBER

variable txt
datatype CHAR(20)

variable myvar
datatype REFCURSOR
```

The following example lists a single variable:

```
VARIABLE txt
```
```
variable txt
datatype CHAR(20)
```

The following example illustrates assigning a value to a variable for input binding:

```
VARIABLE tmp_var VARCHAR2(10)=Smith
```

The following example illustrates an alternate method to achieve the same result as the previous example:

```
VARIABLE tmp_var VARCHAR2(10)    
VARIABLE tmp_var=Smith    
EXECUTE DBMS_OUTPUT.PUT_LINE(:tmp_var)
```

The following example illustrates producing a report listing individual salaries and computing the departmental salary cost for employees who earn more than $12,000 per month:

```
VARIABLE rc REFCURSOR
BEGIN
  OPEN :rc FOR SELECT DEPARTMENT_NAME, LAST_NAME, SALARY
  FROM EMP_DETAILS_VIEW
  WHERE SALARY > 12000
  ORDER BY DEPARTMENT_NAME, LAST_NAME;
END;
/
```
```
PL/SQL procedure successfully completed.
```
```
SET PAGESIZE 100 FEEDBACK OFF
TTITLE LEFT '*** Departmental Salary Bill ***' SKIP 2
COLUMN SALARY FORMAT $999,990.99 HEADING 'Salary'
COLUMN DEPARTMENT_NAME HEADING 'Department'
COLUMN LAST_NAME HEADING 'Employee'
COMPUTE SUM LABEL 'Subtotal:' OF SALARY ON DEPARTMENT_NAME
COMPUTE SUM LABEL 'Total:' OF SALARY ON REPORT
BREAK ON DEPARTMENT_NAME SKIP 1 ON REPORT SKIP 1
PRINT rc
```
```
*** Departmental Salary Bill ***

DEPARTMENT_NAME                Employee                  Salary
------------------------------ ------------------------- ------------
Executive                      De Haan                     $17,000.00
                               King                        $24,000.00
                               Kochhar                     $17,000.00
******************************                           ------------
Subtotal:                                                  $58,000.00

Marketing                      Hartstein                   $13,000.00
******************************                           ------------
Subtotal:                                                  $13,000.00

Sales                          Partners                    $13,500.00
                               Russell                     $14,000.00
******************************                           ------------
Subtotal:                                                  $27,500.00

                                                         ------------
Total:                                                     $98,500.00
```

The following example illustrates how to create an input bind to insert CLOB data into a CLOB column:

```
SQL> create table xyz (col1 clob);

Table created.

SQL> var abc varchar2(100)="This is a clob input"
SQL> insert into xyz values(:abc);

1 row created.
```

The following example illustrates producing a report containing a CLOB column, and then displaying it with the SET LOBOFFSET command.

Assume you have already created a table named clob\_tab which contains a column named clob\_col of type CLOB. The clob\_col contains the following data:

```
Remember to run the Departmental Salary Bill report each month. This report
contains confidential information.
```

To produce a report listing the data in the col\_clob column, enter

```
VARIABLE T CLOB
BEGIN
  SELECT CLOB_COL INTO :T FROM CLOB_TAB;
END;
/
```
```
PL/SQL PROCEDURE SUCCESSFULLY COMPLETED
```

To print 200 characters from the column clob\_col, enter

```
SET LINESIZE 70
SET LONG 200
PRINT T
```
```
T
----------------------------------------------------------------------
Remember to run the Departmental Salary Bill report each month This r
eport contains confidential information.
```

To set the printing position to the 21st character, enter

```
SET LOBOFFSET 21
PRINT T
```
```
T
----------------------------------------------------------------------
Departmental Salary Bill report each month This report contains confi
dential information.
```