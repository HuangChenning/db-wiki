---
title: Utilities
book: Oracle AI Database Utilities Guide
doc_id: F30732-30
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sutil/oracle_loader-access-driver.html
tags:
  - oracle
  - 21c
  - utilities
---

## 15 The ORACLE\_LOADER Access Driver

Learn how to control the way external tables are accessed by using the ORACLE\_LOADER access driver parameters to modify the default behavior of the access driver.

- About the ORACLE\_LOADER Access Driver  
	The `ORACLE_LOADER` access driver provides a set of access parameters unique to external tables of the type `ORACLE_LOADER`.
- access\_parameters Clause  
	The `access_parameters` clause contains comments, record formatting, and field formatting information.
- record\_format\_info Clause  
	Learn how to parse, label and manage record information with the `record_format_info` clause and its subclauses.
- field\_definitions Clause  
	Learn how to name the fields in the data file and specify how to find them in records using the `field_definitions` clause.
- column\_transforms Clause  
	The optional `ORACLE_LOADER` access drive `COLUMN             TRANSFORMS` clause provides transforms that you can use to describe how to load columns in the external table that do not map directly to columns in the data file.
- Parallel Loading Considerations for the ORACLE\_LOADER Access Driver  
	The `ORACLE_LOADER` access driver attempts to divide large data files into chunks that can be processed separately.
- Performance Hints When Using the ORACLE\_LOADER Access Driver  
	This topic describes some performance hints when using the `ORACLE_LOADER` access driver.
- Restrictions When Using the ORACLE\_LOADER Access Driver  
	This section lists restrictions to be aware of when you use the `ORACLE_LOADER` access driver.
- Reserved Words for the ORACLE\_LOADER Access Driver  
	When identifiers (for example, column or table names) are specified in the external table access parameters, certain values are considered to be reserved words by the access parameter parser.

**Parent topic:** [External Tables](oracle-external-tables.md)

### 15.1 About the ORACLE\_LOADER Access Driver

The `ORACLE_LOADER` access driver provides a set of access parameters unique to external tables of the type `ORACLE_LOADER`.

You can use the access parameters to modify the default behavior of the access driver. The information you provide through the access driver ensures that data from the data source is processed so that it matches the definition of the external table.

To use the external table management features that the ORACLE\_LOADER access parameters provide, you must have some knowledge of the file format and record format (including character sets and field data types) of the data files on your platform. You must also know enough about SQL to be able to create an external table, and to perform queries against it.

You can find it helpful to use the `EXTERNAL_TABLE=GENERATE_ONLY` parameter in SQL\*Loader to obtain the proper access parameters for a given SQL\*Loader control file. When you specify `GENERATE_ONLY`, all the SQL statements needed to do the load using external tables, as described in the control file, are placed in the SQL\*Loader log file. You can edit and customize these SQL statements. You can perform the actual load later without the use of SQL\*Loader by executing these statements in SQL\*Plus.

Note:

- It is sometimes difficult to understand `ORACLE_LOADER` access driver parameter syntax without reference to other `ORACLE_LOADER` access driver parameters. If you have difficulty understanding the syntax of a particular parameter, then refer to it in context with other referenced parameters.
- Be aware that in ORACLE\_LOADER access driver parameter examples that show a `CREATE TABLE...ORGANIZATION EXTERNAL` statement, followed by an example of contents of the data file for the external table, the contents of the data file in the example are not part of the `CREATE TABLE` statement. They are present in the example only to help complete the example.
- When identifiers (for example, column or table names) are specified in the external table access parameters, certain values are considered to be reserved words by the access parameter parser. If a reserved word is used as an identifier, then it must be enclosed in double quotation marks.

### 15.2 access\_parameters Clause

The `access_parameters` clause contains comments, record formatting, and field formatting information.

Default

None.

Syntax

The syntax for the `access_parameters` clause is as follows:

![et_access_param](img/et_access_param.gif)

> et\_access\_param::=
>
> \[comments\] \[record\_format\_info\] \[field\_definitions\] \[column\_transforms\]
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 2002, 2026, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Purpose

The description of the data in the data source is separate from the definition of the external table. This means that:

- The source file can contain more or fewer fields than there are columns in the external table
- The data types for fields in the data source can be different from the columns in the external table

The access driver ensures that data from the data source is processed so that it matches the definition of the external table.

Note:

These access parameters are collectively referred to as the `opaque_format_spec` in the SQL `CREATE                         TABLE...ORGANIZATION EXTERNAL` statement.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sutil&id=SQLRF01402) for information about specifying `opaque_format_spec` when using the SQL `CREATE                         TABLE...ORGANIZATION EXTERNAL` statement