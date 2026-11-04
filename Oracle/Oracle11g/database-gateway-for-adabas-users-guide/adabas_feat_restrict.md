---
title: Gateway Features and Restrictions
book: "Database Gateway for Adabas User's Guide"
doc_id: E12074-01
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/gateways.112/e12074/adabas_feat_restrict.htm
tags:
  - oracle
  - 11g
  - database-gateway-for-adabas-users-guide
---

## 2 Gateway Features and Restrictions

After the gateway is installed and configured, you can use the gateway to access Adabas data, pass Adabas commands from applications to the Adabas database, perform distributed queries, and copy data.

This chapter contains the following sections:

## Accessing Adabas Data

Oracle Connect for IMS, VSAM, and Adabas Gateways supports the following types of Adabas data sources:

- Adabas (Predict): The Adabas (Predict) data source uses Predict metadata.
- ADD-Adabas: The ADD-Adabas data source uses Oracle's internal repository (ADD), which is usually imported from Natural Data Definition Module (DDM) files. Alternatively, Predict metadata can be exported and subsequently imported into the ADD-Adabas data source.

For details on importing metadata, see the [Oracle Database Gateway for IMS, VSAM, and Adabas Installation and Configuration Guide for AIX 5L Based Systems (64-Bit), HP-UX Itanium, Solaris Operating System (SPARC 64-Bit), Linux x86, and Linux x86-64](https://docs.oracle.com/cd/E11882_01/gateways.112/e12076/toc.htm) or the [Oracle Database Gateway for IMS, VSAM, and Adabas Installation and Configuration Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/gateways.112/e12077/toc.htm).

Both Adabas data sources provide very similar functions. The Adabas (Predict) data source supports one-phase transactions only. The ADD-Adabas data sources enjoys some added flexibility and functions resulting from the ability to customize the metadata in the ADD. Unless explicitly stated, all features and procedures described apply to both data sources.

Oracle supports data from Adabas version 6.2 and later on IBM z/OS platforms.

### Exporting Predict Metadata into Adabas ADD

Some users who have Predict still prefer to use ADD to store metadata. The process of moving metadata from Predict to ADD is simple, although manual. It involves exporting from Predict and importing to ADD. The process is carried out using the NAV\_UTIL command-line interface.

In the following procedure, for the purposes of the example, note that the native qualifier is required. On the export side, the procedure generates all table definitions from a Predict data source called `adapredict` to an XML file. On the import side, the exported metadata is imported to a data source call `adaadd`.

Perform the following procedure to export Predict metadata into Adabas ADD.

1. After executing the NAVCMD Rexx script in USERLIB, execute the following NAV\_UTIL command to export:
	`Local> export table -native adapredict * 'ORACLE.XML.ADAPRED'`
2. After executing the NAVCMD Ress script in USERLIB, execute the following NAV\_UTIL command to import:
	`Local> import adaadd 'ORACLE.XML.ADAPRED'`

## SQL Support

Oracle Database Gateway for Adabas supports SQL-based data access, allowing developers and applications to use this common and standard syntax for retrieving and updating Adabas data, and for using SELECT, INSERT, UPDATE, and DELETE statements.

While SQL is supported by relational database management systems, it is not available for legacy, non-relational data such as Adabas data. This means that Oracle Database Gateway for Adabas goes beyond the functionality provided by other Oracle gateways that connect to relational databases, as those merely deal with the translation and delegation of SQL to the target database. Oracle Database Gateway for Adabas takes care of the translation of the SQL statements into system and file specific access primitives, and their execution in an optimized manner, effectively serving as the SQL processor for the non-relational system.

In terms of SQL support, the gateway supports a wide range of SQL capabilities, from basic SQL statements to statements that include advanced features, such as joining of data from multiple Adabas sources, use of subselects, and support of data manipulation functions. In addition, the gateway optimizes query performance by supporting such advanced capabilities in where clauses, processing most of them before returning the data to Oracle.

Because Adabas is a non-relational system, its data model is not normalized. The gateway provides a complete normalization process that imports existing legacy metadata and produces a relational format that can be used by Oracle users. A key consideration in the normalization process takes care of the hierarchical data structures that are common in Adabas, such as arrays.

Going through the import process, the gateway translates the hierarchical structures and embedded arrays into a relational model that maps the hierarchy to several tables. In addition, the process automatically generates the necessary foreign constraints that can later be retrieved using regular Oracle Data Dictionary queries.

In respect to the data dictionary, the gateway provides all the necessary information although the actual data dictionary is not located in the Oracle database. The gateway supports standard data dictionary queries, making the interaction with the non-Oracle data completely transparent to the user, and taking care of translating the non-Oracle model into the Oracle standard data dictionary format including joins across non-Oracle data dictionary tables.

While the typical use case only supports the retrieval of information using SELECT statements, the gateway also supports data manipulation using INSERT, UPDATE, and DELETE statements. Furthermore, it supports advanced options such as distributed transactions.

To summarize, Oracle Database Gateway for Adabas offers robust SQL support and relational access to non-relational, proprietary, legacy Adabas data. The following topics provide more information about specific SQL features and their support by the gateway.

This section includes the following topics:

- Pass-Through Feature
- Naming Rules
- Data Types
- SQL Execution
- Locking

See Also:

[Supported SQL Syntax and Functions](adabas_sql_syntax.md) for details; SQL Restrictions for restrictions.

### Pass-Through Feature

Adabas commands cannot be issued using the pass-through feature.

### Naming Rules

Naming rule issues include the following:

- Rules for Naming Objects
- Case Sensitivity

#### Rules for Naming Objects

The concept of owner does not exist for objects from Adabas data sources. The userid of the dblink is not used to qualify the object. The owner field in the data dictionary tables (see [Appendix C, "Data Dictionary"](adabas_data_dictionary.md) for details) is hardcoded as `ADABAS`. You must not use an explicit owner qualifier to reference Adabas tables. Using an explicit owner name results in a message like the following:

`ORA-00942: table or view does not exist`

See Also:

Oracle Database Reference and Adabas documentation for more information on naming objects and [Oracle Database Error Messages](https://docs.oracle.com/cd/E11882_01/server.112/e17766/toc.htm) for more information on error messages.

#### Case Sensitivity

Object names are not case sensitive. Both Oracle Studio for IMS, VSAM, and Adabas Gateways and the gateway automatically use upper case for data source metadata.

### Data Types

Data type issues include the following:

- Binary Literal Notation
- Data Type Conversion

#### Binary Literal Notation

Oracle SQL uses hexadecimal digits surrounded by single quotes to express literal values being compared or inserted into columns defined as data type RAW.

This notation is not converted to syntax compatible with the Adabas VARBINARY and BINARY data types (a 0x followed by hexadecimal digits, surrounded by single quotes).

For example, the following statement is not supported:

```
SQL> INSERT INTO BINARY_TAB@Adabas VALUES ('0xff')
```

Where `BINARY_TAB` contains a column of data type VARBINARY or BINARY. Use bind variables when inserting into or updating VARBINARY and BINARY data types.

#### Data Type Conversion

Adabas does not support implicit date conversions. Such conversions must be explicit.

For example, the gateway issues an error for the following `SELECT` statement:

```
SELECT DATE_COL FROM TEST@Adabas WHERE DATE_COL = "1-JAN-2001";
```

To avoid problems with implicit conversions, add explicit conversions, as in the following:

```
SELECT DATE_COL FROM TEST@Adabas WHERE DATE_COL = TO_DATE("1-JAN-2001")
```

See Also:

[Appendix A, "Data Type Conversion"](adabas_datatype_conv.md) for more information about restrictions on data types and [Oracle Database Error Messages](https://docs.oracle.com/cd/E11882_01/server.112/e17766/toc.htm) for more information on error messages.

### SQL Execution

Query issues include the following:

- Row Selection
- Empty Strings
- Empty Bind Variables

#### Row Selection

Adabas evaluates a query condition for all selected rows before returning any of the rows. If there is an error in the evaluation process for one or more rows, no rows are returned even though the remaining rows satisfy the condition.

Oracle evaluates the query condition row-by-row and returns a row when the evaluation is successful. Rows are returned until a row fails the evaluation.

See Also:

[Oracle Database Error Messages](https://docs.oracle.com/cd/E11882_01/server.112/e17766/toc.htm) for more information on error messages.

#### Empty Strings

Oracle processes an empty string in a SQL statement as a null value. Adabas processes an empty string as an empty string.

Comparing to an empty string

The Gateway passes literal empty strings to the Adabas database without any conversion. If you intended an empty string to represent a null value, Adabas does not process the statement that way; it uses the empty string.

You can avoid this problem by using NULL or IS NULL in the SQL statement instead of the empty string syntax, as in the following example:

```
SELECT * from "emp"@Adabas where "ename" IS NULL;
```

Selecting an empty string

For VARCHAR columns, the gateway returns an empty string to the Oracle Database as NULL value.

For CHAR columns, the gateway returns the full size of the column with each character as empty space (' ').

#### Empty Bind Variables

For VARCHAR bind variables, the gateway passes empty bind variables to the Adabas database as a NULL value.

### Locking

The locking model for an Adabas database differs significantly from the Oracle model. The gateway depends on the underlying Adabas behavior, so Oracle applications that access Adabas through the gateway can be affected by the following possible scenarios:

- Read access may block write access.
- Write access may block read access.
- Statement-level read consistency is not guaranteed.
	See Also:
	Adabas documentation for information about the Adabas locking model.

## Handling Non-Relational Data

Non-relational data sources (excluding Adabas when Predict metadata is used) require metadata, which is kept separately from the data itself. This metadata is stored as a data source definition in a data source repository, on the machine where the data source is defined. It lets you access the data from a non-relational database with SQL commands.

When the non-relational data contains arrays, these arrays can be exposed as follows:

Once the metadata is imported, the data from the non-relational data source can be normalized to maintain transparency.

- As virtual views. This method generates a virtual view for every array in the parent record that contains all the array members.
- As a single table. This method maps all the record fields of the non-relational file to a single table that contains both parent and child records.

## Restrictions

The following sections describe the restrictions and include suggestions for dealing with them if possible:

- SQL Restrictions
- Adabas Restrictions

### SQL Restrictions

Restrictions related to SQL are described in the following sections:

- Unsupported SQL Functions
- SQL Syntax
- Transaction Capability
- COMMIT or ROLLBACK in PL/SQL Cursor Loops
- Pass-Through Feature
- Database Links
- Data Types
- Encrypted Format Login
- Data Dictionary Views and PL/SQL

#### Unsupported SQL Functions

When an unsupported SQL function is used in an UPDATE, DELETE, or INSERT statement, an error occurs.

See [Supported SQL Syntax and Functions](adabas_sql_syntax.md) for a list of the supported functions.

#### SQL Syntax

Table 2-1 lists the restrictions that apply to SQL syntax.

Table 2-1 SQL Syntax Restrictions

| Syntax | Restriction |
| --- | --- |
| WHERE CURRENT OF clause | `UPDATE` and `DELETE` statements with the `WHERE CURRENT OF` clause are not supported by the gateway because they rely on the Oracle ROWID implementation. To update or delete a specific row through the gateway, a condition style `WHERE` clause must be used. |
| CONNECT BY clause | The gateway does not support the `CONNECT BY` clause in a `SELECT` statement. |
| ROWID | The Oracle ROWID implementation is not supported. |
| Subqueries in INSERT statement | Subqueries of `INSERT` statements cannot use multiple aliases for the same table. For example, the following statement is not supported:  ``` SQL> INSERT INTO "emp_target"@Adabas          SELECT a."empno" FROM "emp_source"@Adabas a,             "emp_source"@Adabas b WHERE b."empno"=9999 ``` |
| EXPLAIN PLAN statement | The `EXPLAIN PLAN` statement is not supported. |
| Date arithmetic | The following SQL expressions do not function correctly with the gateway:  ``` date + numbernumber + datedate - numberdate1 - date2 ```  Statements with the preceding expressions are sent to the Adabas database without any translation. Since Adabas does not support these date arithmetic functions, the statements return an error.  See Also: [Oracle Database Error Messages](https://docs.oracle.com/cd/E11882_01/server.112/e17766/toc.htm) for more information on error messages. |
| String functions | If you concatenate numeric literals using the "\|\|" operator when using the gateway to query a Adabas database, the result is an arithmetic addition. For example, the result of the following statement is 18:  ``` SQL> SELECT 9 \|\| 9 FROM DUAL@Adabas; ```  The result is 99 when using Oracle to query an Oracle database. |
| Schema names and PL/SQL | If you do not prefix a Adabas database object with its schema name in a SQL statement within a PL/SQL block, the following error message occurs:  ``` ORA-6550 PLS-201 Identifier table_name must be declared. ```  Change the SQL statement to include the schema name of the object.  See Also: [Oracle Database Error Messages](https://docs.oracle.com/cd/E11882_01/server.112/e17766/toc.htm) for more information on error messages. |

#### Transaction Capability

The gateway does not support savepoints. If a distributed update transaction is under way involving the gateway and a user attempts to create a savepoint, the following error occurs:

```
ORA-02070: database dblink does not support savepoint in this context
```

The Adabas data source supports only local transactions.

See Also:

[Oracle Database Error Messages](https://docs.oracle.com/cd/E11882_01/server.112/e17766/toc.htm) for more information on error messages.

#### COMMIT or ROLLBACK in PL/SQL Cursor Loops

Any COMMIT or ROLLBACK issued in a PL/SQL cursor loop closes all open cursors, which can result in the following error:

```
ORA-1002:  fetch out of sequence
```

To prevent this error, move the COMMIT or ROLLBACK statement outside the cursor loop.

See Also:

[Oracle Database Error Messages](https://docs.oracle.com/cd/E11882_01/server.112/e17766/toc.htm) for more information on error messages.

#### Pass-Through Feature

Adabas commands cannot be issued using the pass-through feature.

#### Database Links

The gateway is not multithreaded and cannot support shared database links. Each gateway session spawns a separate gateway process and connections cannot be shared.

#### Data Types

The FLOAT data type precision is (7).

#### Data Dictionary Views and PL/SQL

You cannot refer to data dictionary views in SQL statements that are inside a PL/SQL block.

### Adabas Restrictions

When accessing Adabas data, the following restrictions apply:

- UPDATE operations on arrays are not supported. See [Normalizing Non-Relational Data](c_array_handling.md) for details on handling arrays.
- When you perform an INSERT operation with an incomplete list of values, the columns that are described as NOT NULL take on the default value of the specific data type. The following table lists the default value for each data type.
	| Data Type | Default Value |
	| --- | --- |
	| numeric | 0 |
	| char | spaces |
	| date | 1-1-0000 |