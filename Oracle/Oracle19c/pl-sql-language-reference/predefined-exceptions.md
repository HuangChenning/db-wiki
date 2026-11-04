---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/predefined-exceptions.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Predefined Exceptions

Predefined exceptions are internally defined exceptions that have predefined names, which PL/SQL declares globally in the package `STANDARD`. The runtime system raises predefined exceptions implicitly (automatically). Because predefined exceptions have names, you can write exception handlers specifically for them.

Table 11-3 lists the names and error codes of the predefined exceptions.

Table 11-3 PL/SQL Predefined Exceptions

| Exception Name | Error Code |
| --- | --- |
| `ACCESS_INTO_NULL` | `-6530` |
| `CASE_NOT_FOUND` | `-6592` |
| `COLLECTION_IS_NULL` | `-6531` |
| `CURSOR_ALREADY_OPEN` | `-6511` |
| `DUP_VAL_ON_INDEX` | `-1` |
| `INVALID_CURSOR` | `-1001` |
| `INVALID_NUMBER` | `-1722` |
| `LOGIN_DENIED` | `-1017` |
| `NO_DATA_FOUND` | `+100` |
| `NO_DATA_NEEDED` | `-6548` |
| `NOT_LOGGED_ON` | `-1012` |
| `PROGRAM_ERROR` | `-6501` |
| `ROWTYPE_MISMATCH` | `-6504` |
| `SELF_IS_NULL` | `-30625` |
| `STORAGE_ERROR` | `-6500` |
| `SUBSCRIPT_BEYOND_COUNT` | `-6533` |
| `SUBSCRIPT_OUTSIDE_LIMIT` | `-6532` |
| `SYS_INVALID_ROWID` | `-1410` |
| `TIMEOUT_ON_RESOURCE` | `-51` |
| `TOO_MANY_ROWS` | `-1422` |
| `VALUE_ERROR` | `-6502` |
| `ZERO_DIVIDE` | `-1476` |

Example 11-6 calculates a price-to-earnings ratio for a company. If the company has zero earnings, the division operation raises the predefined exception `ZERO_DIVIDE` and the executable part of the block transfers control to the exception-handling part.

Example 11-7 uses error-checking code to avoid the exception that Example 11-6 handles.

In Example 11-8, the procedure opens a cursor variable for either the `EMPLOYEES` table or the `DEPARTMENTS` table, depending on the value of the parameter `discrim`. The anonymous block invokes the procedure to open the cursor variable for the `EMPLOYEES` table, but fetches from the `DEPARTMENTS` table, which raises the predefined exception `ROWTYPE_MISMATCH`.

See Also:

" [Raising Internally Defined Exception with RAISE Statement](raising-exceptions-explicitly.md) "

Example 11-6 Anonymous Block Handles ZERO\_DIVIDE

```
DECLARE
  stock_price   NUMBER := 9.73;
  net_earnings  NUMBER := 0;
  pe_ratio      NUMBER;
BEGIN
  pe_ratio := stock_price / net_earnings;  -- raises ZERO_DIVIDE exception
  DBMS_OUTPUT.PUT_LINE('Price/earnings ratio = ' || pe_ratio);
EXCEPTION
  WHEN ZERO_DIVIDE THEN
    DBMS_OUTPUT.PUT_LINE('Company had zero earnings.');
    pe_ratio := NULL;
END;
/
```

Result:

```
Company had zero earnings.
```

Example 11-7 Anonymous Block Avoids ZERO\_DIVIDE

```
DECLARE
  stock_price   NUMBER := 9.73;
  net_earnings  NUMBER := 0;
  pe_ratio      NUMBER;
BEGIN
  pe_ratio :=
    CASE net_earnings
      WHEN 0 THEN NULL
      ELSE stock_price / net_earnings
    END;
END;
/
```

Example 11-8 Anonymous Block Handles ROWTYPE\_MISMATCH

```
CREATE OR REPLACE PACKAGE emp_dept_data AUTHID DEFINER AS
  TYPE cv_type IS REF CURSOR;
  
  PROCEDURE open_cv (
    cv       IN OUT cv_type,
    discrim  IN     POSITIVE
  );
  END emp_dept_data;
/
 
CREATE OR REPLACE PACKAGE BODY emp_dept_data AS
  PROCEDURE open_cv (
    cv      IN OUT cv_type,
    discrim IN     POSITIVE) IS
  BEGIN
    IF discrim = 1 THEN
    OPEN cv FOR
      SELECT * FROM EMPLOYEES ORDER BY employee_id;
    ELSIF discrim = 2 THEN
      OPEN cv FOR
        SELECT * FROM DEPARTMENTS ORDER BY department_id;
    END IF;
  END open_cv;
END emp_dept_data;
/
```

Invoke procedure `open_cv` from anonymous block:

```
DECLARE
  emp_rec   EMPLOYEES%ROWTYPE;
  dept_rec  DEPARTMENTS%ROWTYPE;
  cv        Emp_dept_data.CV_TYPE;
BEGIN
  emp_dept_data.open_cv(cv, 1);  -- Open cv for EMPLOYEES fetch.
  FETCH cv INTO dept_rec;        -- Fetch from DEPARTMENTS.
  DBMS_OUTPUT.PUT(dept_rec.DEPARTMENT_ID);
  DBMS_OUTPUT.PUT_LINE('  ' || dept_rec.LOCATION_ID);
EXCEPTION
  WHEN ROWTYPE_MISMATCH THEN
     BEGIN
       DBMS_OUTPUT.PUT_LINE
         ('Row type mismatch, fetching EMPLOYEES data ...');
       FETCH cv INTO emp_rec;
       DBMS_OUTPUT.PUT(emp_rec.DEPARTMENT_ID);
       DBMS_OUTPUT.PUT_LINE('  ' || emp_rec.LAST_NAME);
     END;
END;
/
```

Result:

```
Row type mismatch, fetching EMPLOYEES data ...
90  King
```