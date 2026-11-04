---
title: CREATE PACKAGE Statement
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/create_package.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

The `CREATE` `PACKAGE` statement creates or replaces the specification for a stored package, which is an encapsulated collection of related procedures, functions, and other program objects stored as a unit in the database. The package specification declares these objects. The package body, specified subsequently, defines these objects.

Topics

Prerequisites

To create or replace a package in your schema, you must have the `CREATE` `PROCEDURE` system privilege. To create or replace a package in another user's schema, you must have the `CREATE` `ANY` `PROCEDURE` system privilege.

To embed a `CREATE` `PACKAGE` statement inside an the database precompiler program, you must terminate the statement with the keyword `END-EXEC` followed by the embedded SQL statement terminator for the specific language.

Semantics

OR REPLACE

Re-creates the package if it exists, and recompiles it.

Users who were granted privileges on the package before it was redefined can still access the package without being regranted the privileges.

If any function-based indexes depend on the package, then the database marks the indexes `DISABLED`.

schema

Name of the schema containing the package. Default: your schema.

package\_name

A package stored in the database. For naming conventions, see ["Identifiers"](fundamentals.md).

invoker\_rights\_clause

Specifies the `AUTHID` property of the functions and procedures in the package, and of the explicit cursors declared in the package specification. For information about the `AUTHID` property, see ["Invoker's Rights and Definer's Rights (AUTHID Property)"](subprograms.md).

item\_list\_1

Defines every type in the package and declares every cursor and subprogram in the package. Every declaration must have a corresponding definition in the package body. The headings of corresponding declarations and definitions must match word for word, except for white space.

Restriction on item\_list\_1 The `AUTONOMOUS_TRANSACTION` pragma cannot appear here.

Example

Creating a Package: Example This statement creates the specification of the `emp_mgmt` package.

```
CREATE OR REPLACE PACKAGE emp_mgmt AS 
   FUNCTION hire (last_name VARCHAR2, job_id VARCHAR2, 
      manager_id NUMBER, salary NUMBER, 
      commission_pct NUMBER, department_id NUMBER) 
      RETURN NUMBER; 
   FUNCTION create_dept(department_id NUMBER, location_id NUMBER) 
      RETURN NUMBER; 
   PROCEDURE remove_emp(employee_id NUMBER); 
   PROCEDURE remove_dept(department_id NUMBER); 
   PROCEDURE increase_sal(employee_id NUMBER, salary_incr NUMBER); 
   PROCEDURE increase_comm(employee_id NUMBER, comm_incr NUMBER); 
   no_comm EXCEPTION; 
   no_sal EXCEPTION; 
END emp_mgmt; 
/
```

The specification for the `emp_mgmt` package declares these public program objects:

- The functions `hire` and `create_dept`
- The procedures `remove_emp`, `remove_dept`, `increase_sal`, and `increase_comm`
- The exceptions `no_comm` and `no_sal`

All of these objects are available to users who have access to the package. After creating the package, you can develop applications that invoke any of these public procedures or functions or raise any of the public exceptions of the package.

Before you can invoke this package's procedures and functions, you must define these procedures and functions in the package body. For an example of a `CREATE` `PACKAGE` `BODY` statement that creates the body of the `emp_mgmt` package, see ["CREATE PACKAGE BODY Statement"](create_package_body.md).

Related Topics

In this chapter:

- ["ALTER PACKAGE Statement"](alter_package.md)
- "CREATE PACKAGE Statement"
- ["CREATE PACKAGE BODY Statement"](create_package_body.md)
- ["DROP PACKAGE Statement"](drop_package.md)

In other chapters:

- [Chapter 10, "PL/SQL Packages"](packages.md)
- ["Package Specification"](packages.md)
- ["Function Declaration and Definition"](function.md)
- ["Procedure Declaration and Definition"](procedure.md)