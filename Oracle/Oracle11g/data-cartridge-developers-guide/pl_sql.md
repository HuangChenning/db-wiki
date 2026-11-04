---
title: Implementing Data Cartridges in PL/SQL
book: "Data Cartridge Developer's Guide"
doc_id: E10765-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/pl_sql.htm
tags:
  - oracle
  - 11g
  - data-cartridge-developers-guide
---

## 4 Implementing Data Cartridges in PL/SQL

This chapter describes how to use PL/SQL to implement the methods of a data cartridge. Methods are procedures and functions that define the operations permitted on data defined using the data cartridge.

This chapter contains these topics:

## Methods

A method is procedure or function that is part of the object type definition, and that can operate on the attributes of the type. Such methods are also called member methods, and they take the keyword `MEMBER` when you specify them as a component of the object type.

The following sections show simple examples of implementing a method, invoking a method, and referencing an attribute in a method.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm) for information about method specifications, names, and overloading
- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/toc.htm). for further explanation and examples

### Implementing Methods

To implement a method, create the PL/SQL code and specify it within a `CREATE` `TYPE` `BODY` statement. If an object type has no methods, no `CREATE` `TYPE` `BODY` statement for that object type is required.

Example 4-1 demonstrates the definition of an object type `rational_type`:

Example 4-1 Defining an Object Type

```
CREATE TYPE rational_type AS OBJECT
( numerator INTEGER,
  denominator INTEGER,
  MAP MEMBER FUNCTION rat_to_real RETURN REAL,
  MEMBER PROCEDURE normalize,
  MEMBER FUNCTION plus (x rational_type)
       RETURN rational_type);
```

The definition in Example 4-2 defines the function `gcd`, which is used in the definition of the `normalize` method in the `CREATE` `TYPE` `BODY` statement later in this section.

Example 4-2 Defining a "Greatest Common Divisor" Function

```
CREATE FUNCTION gcd (x INTEGER, y INTEGER) RETURN INTEGER AS
-- Find greatest common divisor of x and y. For example, if
-- (8,12) is input, the greatest common divisor is 4.
-- This normalizes (simplifies) fractions.
-- (You need not try to understand how this code works, unless
--  you are a math wizard. It does.)
--
   ans INTEGER;
BEGIN
   IF (y <= x) AND (x MOD y = 0) THEN
      ans := y;
   ELSIF x < y THEN 
      ans := gcd(y, x);  -- Recursive call
   ELSE
      ans := gcd(y, x MOD y);  -- Recursive call
   END IF;
   RETURN ans;
END;
```

The statements in Example 4-3 implement the methods `rat_to_real`, `normalize`, and `plus` for the object type `rational_type`.

Example 4-3 Implementing Methods for an Object Type

```
CREATE TYPE BODY rational_type
( MAP MEMBER FUNCTION rat_to_real RETURN REAL IS
   -- The rat-to-real function converts a rational number to 
   -- a real number. For example, 6/8 = 0.75
   BEGIN
      RETURN numerator/denominator;
   END;

   -- The normalize procedure simplifies a fraction.
   -- For example, 6/8 = 3/4
   MEMBER PROCEDURE normalize IS
      divisor INTEGER := gcd(numerator, denominator);
   BEGIN
      numerator := numerator/divisor;
      denominator := denominator/divisor;
   END;

   -- The plus function adds a specified value to the
   -- current value and returns a normalized result.
   -- For example, 1/2 + 3/4 = 5/4
   -- 
   MEMBER FUNCTION plus(x rational_type)
            RETURN rational_type IS
            -- Return sum of SELF + x
   BEGIN
      r = rational_type(numerator*x.demonimator +
             x.numerator*denominator,
             denominator*x.denominator);
                 -- Example adding 1/2 to 3/4:
                 -- (3*2 + 1*4) / (4*2)
      -- Now normalize (simplify). Here, 10/8 = 5/4
      r.normalize;
      RETURN r;
   END;
END;
```

### Invoking Methods

To invoke a method, use the syntax in Example 4-4:

Example 4-4 Invoking Methods; General Syntax

```
object_name.method_name([parameter_list])
```

In SQL statements only, you can use the syntax in Example 4-5:

Example 4-5 Invoking Methods; SQL Syntax

```
correlation_variable.method_name([parameter_list])
```

Example 4-6 shows how to invoke a method named `get_emp_sal` in PL/SQL:

Example 4-6 Invoking Methods; General Syntax

```
DECLARE
   employee employee_type;
   salary number;
   ...
BEGIN
   salary := employee.get_emp_sal();
   ...
END;
```

An alternative way to invoke a method is by using the `SELF` built-in parameter. Because the implicit first parameter of each method is the name of the object on whose behalf the method is invoked, Example 4-7 performs the same action as the `salary := employee.get_emp_sal();` line in Example 4-6:

Example 4-7 Using the SELF Build-In Paramenter

```
salary := get_emp_sal(SELF => employee);
```

In this example, `employee` is the name of the object on whose behalf the `get_emp_sal()` method is invoked.

### Referencing Attributes in a Method

Because member methods can reference the attributes and member methods of the same object type without using a qualifier, a built-in reference, `SELF`, always identifies the object on whose behalf the method is invoked.

Consider Example 4-8, where two statements set the value of variable `var1` to `42`:

Example 4-8 Setting Variable Values

```
CREATE TYPE a_type AS OBJECT (
   var1 INTEGER,
   MEMBER PROCEDURE set_var1);
CREATE TYPE BODY a_type (
   MEMBER PROCEDURE set_var1 IS
   BEGIN
      var1 := 42;
      SELF.var1 := 42;
   END set_var1;
);
```

The statements `var1 := 42` and `SELF.var1 := 42` have the same effect. Because `var1` is the name of an attribute of the object type `a_type` and because `set_var1` is a member method of this object type, no qualification is required to access `var1` in the method code. However, for code readability and maintainability, you can use the keyword `SELF` in this context to make the reference to `var1` more clear.

## PL/SQL Packages

A package is a group of PL/SQL types, objects, and stored procedures and functions. The specification part of a package declares the public types, variables, constants, and subprograms that are visible outside the immediate scope of the package. The body of a package defines the objects declared in the specification, and private objects that are not visible to applications outside the package.

Example 4-9 shows the package specification for the package named `DS_package`. This package contains the two stored functions `ds_findmin` and `ds_findmax`, which implement the `DataStreamMin` and `DataStreamMax` functions defined for the `DataStream` object type.

Example 4-9 Creating a Package Specification

```
create or replace package DS_package as 
    function  ds_findmin(data clob) return pls_integer; 
    function  ds_findmax(data clob) return pls_integer; 
     pragma restrict_references(ds_findmin, WNDS, WNPS); 
     pragma restrict_references(ds_findmax, WNDS, WNPS); 
end;
```

See Also:

- [Chapter 2, "Roadmap to Building a Data Cartridge"](roadmap.md) for the DataStream type and type body definitions
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for more information about PL/SQL packages

## Pragma RESTRICT\_REFERENCES

To execute a SQL statement that calls a member function, Oracle must know the purity level of the function, or the extent to which the function is free of side effects. The term side effect, refers to accessing database tables, package variables, and so forth for reading or writing. It is important to control side effects because they can prevent the proper parallelization of a query, produce order-dependent and therefore indeterminate results, or require impermissible actions such as the maintenance of package state across user sessions.

A member function called from a SQL statement can be restricted so that it cannot:

- Insert into, update, or delete database tables
- Be executed remotely or in parallel if it reads or writes the values of packaged variables
- Write the values of packaged variables unless it is called from a `SELECT`, `VALUES`, or `SET` clause
- Call another method or subprogram that violates any of these rules
- Reference a view that violates any of these rules

You must use the pragma `RESTRICT_REFERENCES`, a compiler directive, to enforce these rules. In Example 4-10, the purity level of the `DataStreamMax` method of type `DataStream` is asserted to be `write no database state` (`WNDS`) and `write no package state` (`WNPS`).

Example 4-10 Asserting the Purity Level of a Type

```
CREATE TYPE DataStream AS OBJECT (
         ....
PRAGMA RESTRICT_REFERENCES (DataStreamMax, WNDS, WNPS)
         ... );
```

Member methods that call external procedures cannot do so directly but must route the calls through a package, because the arguments to external procedures cannot be object types. A member function automatically gets a `SELF` reference as its first argument. Therefore, member methods in objects types cannot call out directly to external procedures.

Collecting all external calls into a package makes for a better design. The purity level of the package must also be asserted. Therefore, when the package named `DS_Package` is declared and all external procedure calls from type `DataStream` are routed through this package, the purity level of the package is also declared, as demonstrated in Example 4-11:

Example 4-11 Asserting the Purity Level of a Package

```
CREATE OR REPLACE PACKAGE DS_Package AS
   ... 
PRAGMA RESTRICT_REFERENCES (ds_findmin, WNDS, WNPS)
   ...
end;
```

In addition to `WNDS` and `WNPS`, it is possible to specify two other constraints: `read no database state` (`RNDS`) and `read no package state` (`RNPS`). These two constraints are normally useful if you have parallel queries.

Each constraint is independent of the others, and does not imply another. Choose the set of constraints based on application-specific requirements.

You can also specify the keyword `DEFAULT` instead of a method or procedure name, in which case the pragma applies to all member functions of the type or procedures of the package, as demonstrated Example 4-12.

Example 4-12 Asserting a Default Purity Level for All Type Methods and Package Procedures

```
PRAGMA RESTRICT_REFERENCES (DEFAULT, WNDS, WNPS)
```

See Also:

- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/toc.htm). for more information about the rules governing purity levels and side effects
- [Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/toc.htm). for more information about controlling side effects using the `RESTRICT_REFERENCES` pragma

## Privileges Required to Create Procedures and Functions

To create a standalone procedure or function, or a package specification or a body, you must have the `CREATE` `PROCEDURE` system privilege to create a procedure or package in your schema, or the `CREATE` `ANY` `PROCEDURE` system privilege to create a procedure or package in another user's schema.

For the compilation of the procedure or package, the owner of the procedure or package must have been explicitly granted the necessary object privileges for all objects referenced within the body of the code. The owner cannot have obtained required privileges through roles.

For more information about privilege requirements for creating procedures and functions, see the chapter about using procedures and packages in the [Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/toc.htm).

## Debugging PL/SQL Code

One of the simplest ways to debug PL/SQL code is to try each method, block, or statement interactively using SQL\*Plus, and fix any problems before proceeding to the next statement. If you need more information on an error message, enter the statement `SHOW` `ERRORS`. Also. consider displaying statements for run-time debugging. You can debug stored procedures and packages using the `DBMS_OUTPUT` package, by inserting `PUT` and `PUTLINE` statements into the code to output the values of variables and expressions to your terminal, as demonstrated in Example 4-13.

Example 4-13 Outputing Variable Values to the Terminal, for Debugging

```
Location in module: location
Parameter name: name
Parameter value: value
```

A PL/SQL tracing tool provides more information about exception conditions in application code. You can use this tool to trace the execution of server-side PL/SQL statements. Object type methods cannot be traced directly, but you can trace any PL/SQL functions or procedures that a method calls. The tracing tool also provides information about exception conditions in the application code. The trace output is written to the Oracle server trace file. Note that only the database administrator has access to the file.

See Also:

- The [Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/toc.htm). describes the tracing tool
- The [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) and the [Oracle Database PL/SQL Language Reference.](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/toc.htm) describe the `DBMS_OUTPUT` package

### Notes for C and C++ Programmers

If you are a C or C++ programmer, several PL/SQL conventions and requirements may differ from your expectations

- \= means equal (not assign).
- := means assign (as in Algol).
- `VARRAYs` begin at index `1` (not `0`).
- Comments begin with two hyphens (--), not with `//` or `/*`.
- The `IF` statement requires the `THEN` keyword.
- The `IF` statement must be concluded with the `END` `IF` keyword (which comes after the `ELSE` clause, if there is one).
- There is no `PRINTF` statement. The comparable feature is the `DBMS_OUTPUT`.`PUT_LINE` statement. In this statement, literal and variable text is separated using the double vertical bar, `||`.
- A function must have a return value, and a procedure cannot have a return value.
- If you call a function, it must be on the right side of an assignment operator.
- Many PL/SQL keywords cannot be used as variable names.

### Common Potential Errors

This section presents several kinds of errors you may make in creating a data cartridge.

#### Signature Mismatches

```
13/19    PLS-00538: subprogram or cursor '<name>' is declared in an object
         type specification and must be defined in the object type body
15/19    PLS-00539: subprogram '<name>' is declared in an object type body
         and must be defined in the object type specification
```

If you see either or both of these messages, you have made an error with the signature for a procedure or function. In other words, you have a mismatch between the function or procedure prototype that you entered in the object specification, and the definition in the object body.

Ensure that parameter orders, parameter spelling (including case), and function returns are identical. Use copy-and-paste to avoid errors in typing.

#### RPC Time Out

```
ORA-28576: lost RPC connection to external procedure agent
ORA-06512: at "<name>", line <number>
ORA-06512: at "<name>", line <number>
ORA-06512: at line 34
```

This error might occur after you exit the debugger for the DLL. Restart the program outside the debugger.

#### Package Corruption

```
ERROR at line 1:
ORA-04068: existing state of packages has been discarded
ORA-04063: package body "<name>" has errors
ORA-06508: PL/SQL: could not find program unit being called
ORA-06512: at "<name>", line <number>
ORA-06512: at line <number>
```

This error might occur if you are extending an existing data cartridge; it indicates that the package has been corrupted and must be recompiled.

Before you can perform the recompilation, you must delete all tables and object types that depend upon the package that you are recompiling. To find the dependents on a Windows NT system, use the Oracle Administrator toolbar. Click the Schema button, log in as `sys\change_on_install`, and find packages and tables that you created. Drop these packages and tables by entering SQL statements in the SQL\*Plus interface, as shown in Example 4-14:

Example 4-14 Dropping Packages and Tables

```
Drop type type_name;
Drop table table_name cascade constraints;
```

The recompilation can then be done using the SQL statements in Example 4-15:

Example 4-15 Recompiling Packages

```
Alter type type_name compile body;
Alter type type_name compile specification;
```