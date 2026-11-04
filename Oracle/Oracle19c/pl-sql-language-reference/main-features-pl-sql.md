---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/main-features-pl-sql.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Main Features of PL/SQL

PL/SQL combines the data-manipulating power of SQL with the processing power of procedural languages.

When you can solve a problem with SQL, you can issue SQL statements from your PL/SQL program, without learning new APIs.

Like other procedural programming languages, PL/SQL lets you declare constants and variables, control program flow, define subprograms, and trap runtime errors.

You can break complex problems into easily understandable subprograms, which you can reuse in multiple applications.

Topics

### Error Handling

PL/SQL makes it easy to detect and handle errors.

When an error occurs, PL/SQL raises an exception. Normal execution stops and control transfers to the exception-handling part of the PL/SQL block. You do not have to check every operation to ensure that it succeeded, as in a C program.

For more information, see [PL/SQL Error Handling](plsql-error-handling.md).

### Blocks

The basic unit of a PL/SQL source program is the block, which groups related declarations and statements.

A PL/SQL block is defined by the keywords `DECLARE`, `BEGIN`, `EXCEPTION`, and `END`. These keywords divide the block into a declarative part, an executable part, and an exception-handling part. Only the executable part is required. A block can have a label.

Declarations are local to the block and cease to exist when the block completes execution, helping to avoid cluttered namespaces for variables and subprograms.

Blocks can be nested: Because a block is an executable statement, it can appear in another block wherever an executable statement is allowed.

You can submit a block to an interactive tool (such as SQL\*Plus or Enterprise Manager) or embed it in an Oracle Precompiler or OCI program. The interactive tool or program runs the block one time. The block is not stored in the database, and for that reason, it is called an anonymous block (even if it has a label).

An anonymous block is compiled each time it is loaded into memory, and its compilation has three stages:

1. Syntax checking: PL/SQL syntax is checked, and a parse tree is generated.
2. Semantic checking: Type checking and further processing on the parse tree.
3. Code generation

Note:

An anonymous block is a SQL statement.

For syntax details, see " [Block](block.md) ".

Example 1-1 PL/SQL Block Structure

This example shows the basic structure of a PL/SQL block.

```
<< label >> (optional)
DECLARE    -- Declarative part (optional)
  -- Declarations of local types, variables, & subprograms

BEGIN      -- Executable part (required)
  -- Statements (which can use items declared in declarative part)

[EXCEPTION -- Exception-handling part (optional)
  -- Exception handlers for exceptions (errors) raised in executable part]
END;
```

### Variables and Constants

PL/SQL lets you declare variables and constants, and then use them wherever you can use an expression.

As the program runs, the values of variables can change, but the values of constants cannot.

For more information, see " [Declarations](declarations.md) " and " [Assigning Values to Variables](assigning-values-variables.md) ".

### Subprograms

A PL/SQL subprogram is a named PL/SQL block that can be invoked repeatedly.

If the subprogram has parameters, their values can differ for each invocation. PL/SQL has two types of subprograms, procedures and functions. A function returns a result.

For more information about PL/SQL subprograms, see [PL/SQL Subprograms](plsql-subprograms.md).

PL/SQL also lets you invoke external programs written in other languages.

For more information, see " [External Subprograms](external-subprograms.md) ".

### Packages

A package is a schema object that groups logically related PL/SQL types, variables, constants, subprograms, cursors, and exceptions.

A package is compiled and stored in the database, where many applications can share its contents. You can think of a package as an application.

You can write your own packages—for details, see [PL/SQL Packages](plsql-packages.md). You can also use the many product-specific packages that Oracle Database supplies. For information about these, see [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ARPLS-GUID-4AA6AA30-CAEE-4DCD-B214-9AD51D0229B4).

### Triggers

A trigger is a named PL/SQL unit that is stored in the database and run in response to an event that occurs in the database.

You can specify the event, whether the trigger fires before or after the event, and whether the trigger runs for each event or for each row affected by the event. For example, you can create a trigger that runs every time an `INSERT` statement affects the `EMPLOYEES` table.

For more information about triggers, see [PL/SQL Triggers](plsql-triggers.md).

### Input and Output

Most PL/SQL input and output (I/O) is done with SQL statements that store data in database tables or query those tables. All other PL/SQL I/O is done with PL/SQL packages that Oracle Database supplies.

Table 1-1 PL/SQL I/O-Processing Packages

| Package | Description | More Information |
| --- | --- | --- |
| `DBMS_OUTPUT` | Lets PL/SQL blocks, subprograms, packages, and triggers display output. Especially useful for displaying PL/SQL debugging information. | [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ARPLS036) |
| `HTF` | Has hypertext functions that generate HTML tags (for example, the `HTF`.`ANCHOR` function generates the HTML anchor tag `<A>`). | [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ARPLS390) |
| `HTP` | Has hypertext procedures that generate HTML tags. | [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ARPLS391) |
| `DBMS_PIPE` | Lets two or more sessions in the same instance communicate. | [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ARPLS038) |
| `UTL_FILE` | Lets PL/SQL programs read and write operating system files. | [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ARPLS069) |
| `UTL_HTTP` | Lets PL/SQL programs make Hypertext Transfer Protocol (HTTP) callouts, and access data on the Internet over HTTP. | [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ARPLS070) |
| `UTL_SMTP` | Sends electronic mails (emails) over Simple Mail Transfer Protocol (SMTP) as specified by RFC821. | [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ARPLS074) |

To display output passed to `DBMS_OUTPUT`, you need another program, such as SQL\*Plus. To see `DBMS_OUTPUT` output with SQL\*Plus, you must first issue the SQL\*Plus command `SET` `SERVEROUTPUT` `ON`.

Some subprograms in the packages in Table 1-1 can both accept input and display output, but they cannot accept data directly from the keyboard. To accept data directly from the keyboard, use the SQL\*Plus commands `PROMPT` and `ACCEPT`.

See Also:

- [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQPUG099) for information about the SQL\*Plus command `SET` `SERVEROUTPUT` `ON`
- [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQPUG052) for information about the SQL\*Plus command `PROMPT`
- [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQPUG026) for information about the SQL\*Plus command `ACCEPT`
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF-GUID-04D8EBB3-583D-4969-8344-E221000E9CD9) for information about SQL statements

### Data Abstraction

Data abstraction lets you work with the essential properties of data without being too involved with details.

You can design a data structure first, and then design algorithms that manipulate it.

Topics

#### Cursors

A cursor is a pointer to a private SQL area that stores information about processing a specific SQL statement or PL/SQL `SELECT` `INTO` statement.

You can use the cursor to retrieve the rows of the result set one at a time. You can use cursor attributes to get information about the state of the cursor—for example, how many rows the statement has affected so far.

For more information about cursors, see " [Cursors Overview](cursors-overview.md) ".

#### Composite Variables

A composite variable has internal components, which you can access individually.

You can pass entire composite variables to subprograms as parameters. PL/SQL has two kinds of composite variables, collections and records.

In a collection, the internal components are always of the same data type, and are called elements. You access each element by its unique index. Lists and arrays are classic examples of collections.

In a record, the internal components can be of different data types, and are called fields. You access each field by its name. A record variable can hold a table row, or some columns from a table row.

For more information about composite variables, see [PL/SQL Collections and Records](plsql-collections-and-records.md).

#### Using the %ROWTYPE Attribute

The `%ROWTYPE` attribute lets you declare a record that represents either a full or partial row of a database table or view.

For every column of the full or partial row, the record has a field with the same name and data type. If the structure of the row changes, then the structure of the record changes accordingly.

For more information about `%ROWTYPE` syntax and semantics, see " [%ROWTYPE Attribute](ROWTYPE-attribute.md) ". For more details about its usage, see " [Declaring Items using the %ROWTYPE Attribute](record-variables.md) ".

#### Using the %TYPE Attribute

The `%TYPE` attribute lets you declare a data item of the same data type as a previously declared variable or column (without knowing what that type is).

If the declaration of the referenced item changes, then the declaration of the referencing item changes accordingly. The `%TYPE` attribute is particularly useful when declaring variables to hold database values. For more information about `%TYPE` syntax and semantics, see " [%TYPE Attribute](TYPE-attribute.md) ". For more details about its usage, see " [Declaring Items using the %TYPE Attribute](declarations.md) ".

#### Abstract Data Types

An Abstract Data Type (ADT) consists of a data structure and subprograms that manipulate the data.

The variables that form the data structure are called attributes. The subprograms that manipulate the attributes are called methods.

ADTs are stored in the database. Instances of ADTs can be stored in tables and used as PL/SQL variables.

ADTs let you reduce complexity by separating a large system into logical components, which you can reuse.

In the static data dictionary view `*_OBJECTS`, the `OBJECT_TYPE` of an ADT is `TYPE`. In the static data dictionary view `*_TYPES`, the `TYPECODE` of an ADT is `OBJECT`.

For more information about ADTs, see " [CREATE TYPE Statement](CREATE-TYPE-statement.md) ".

Note:

ADTs are also called user-defined types and object types.

See Also:

[Oracle Database Object-Relational Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ADOBJ001) for information about ADTs (which it calls object types)

### Control Statements

Control statements are the most important PL/SQL extension to SQL.

PL/SQL has three categories of control statements:

- Conditional selection statements, which let you run different statements for different data values.
	For more information, see " [Conditional Selection Statements](conditional-selection-statements.md) ".
- Loop statements, which let you repeat the same statements with a series of different data values.
	For more information, see " [LOOP Statements](loop-statements.md) ".
- Sequential control statements, which allow you to go to a specified, labeled statement, or to do nothing.
	For more information, see " [Sequential Control Statements](sequential-control-statements.md) ".

### Conditional Compilation

Conditional compilation lets you customize the functionality in a PL/SQL application without removing source text.

For example, you can:

- Use new features with the latest database release, and disable them when running the application in an older database release.
- Activate debugging or tracing statements in the development environment, and hide them when running the application at a production site.

For more information, see " [Conditional Compilation](conditional-compilation1.md) ".

### Processing a Query Result Set One Row at a Time

PL/SQL lets you issue a SQL query and process the rows of the result set one at a time.

You can use a basic loop, or you can control the process precisely by using individual statements to run the query, retrieve the results, and finish processing.

Example 1-2 Processing Query Result Rows One at a Time

This example uses a basic loop.

```
BEGIN
  FOR someone IN (
    SELECT * FROM employees
    WHERE employee_id < 120
    ORDER BY employee_id
  )
  LOOP
    DBMS_OUTPUT.PUT_LINE('First name = ' || someone.first_name ||
                         ', Last name = ' || someone.last_name);
  END LOOP;
END;
/
```

Result:

```
First name = Steven, Last name = King
First name = Neena, Last name = Kochhar
First name = Lex, Last name = De Haan
First name = Alexander, Last name = Hunold
First name = Bruce, Last name = Ernst
First name = David, Last name = Austin
First name = Valli, Last name = Pataballa
First name = Diana, Last name = Lorentz
First name = Nancy, Last name = Greenberg
First name = Daniel, Last name = Faviet
First name = John, Last name = Chen
First name = Ismael, Last name = Sciarra
First name = Jose Manuel, Last name = Urman
First name = Luis, Last name = Popp
First name = Den, Last name = Raphaely
First name = Alexander, Last name = Khoo
First name = Shelli, Last name = Baida
First name = Sigal, Last name = Tobias
First name = Guy, Last name = Himuro
First name = Karen, Last name = Colmenares
```