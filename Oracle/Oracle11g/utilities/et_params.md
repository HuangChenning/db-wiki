---
title: The ORACLE_LOADER Access Driver
book: Utilities
doc_id: E22490-08
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e22490/et_params.htm
tags:
  - oracle
  - 11g
  - utilities
---

## 14 The ORACLE\_LOADER Access Driver

This chapter describes the `ORACLE_LOADER` access driver which provides a set of access parameters unique to external tables of the type `ORACLE_LOADER`. You can use the access parameters to modify the default behavior of the access driver. The information you provide through the access driver ensures that data from the data source is processed so that it matches the definition of the external table.

The following topics are discussed in this chapter:

To use the information in this chapter, you must have some knowledge of the file format and record format (including character sets and field datatypes) of the data files on your platform. You must also know enough about SQL to be able to create an external table and perform queries against it.

You may find it helpful to use the `EXTERNAL_TABLE=` `GENERATE_ONLY` parameter in SQL\*Loader to get the proper access parameters for a given SQL\*Loader control file. When you specify `GENERATE_ONLY`, all the SQL statements needed to do the load using external tables, as described in the control file, are placed in the SQL\*Loader log file. These SQL statements can be edited and customized. The actual load can be done later without the use of SQL\*Loader by executing these statements in SQL\*Plus.

See Also:

["EXTERNAL\_TABLE"](ldr_params.md)

Notes:

- It is sometimes difficult to describe syntax without using other syntax that is not documented until later in the chapter. If it is not clear what some syntax is supposed to do, then you might want to skip ahead and read about that particular element.
- Many examples in this chapter show a `CREATE TABLE...ORGANIZATION EXTERNAL` statement followed by a sample of contents of the data file for the external table. These contents are not part of the `CREATE TABLE` statement, but are shown to help complete the example.
- When identifiers (for example, column or table names) are specified in the external table access parameters, certain values are considered to be reserved words by the access parameter parser. If a reserved word is used as an identifier, then it must be enclosed in double quotation marks. See "Reserved Words for the ORACLE\_LOADER Access Driver".

## access\_parameters Clause

The access parameters clause contains comments, record formatting, and field formatting information.

The description of the data in the data source is separate from the definition of the external table. This means that:

- The source file can contain more or fewer fields than there are columns in the external table
- The datatypes for fields in the data source can be different from the columns in the external table

The access driver ensures that data from the data source is processed so that it matches the definition of the external table.

The syntax for the `access_parameters` clause is as follows:

![et_access_param](img/et_access_param.gif)

> et\_access\_param::=
>
> \[comments\] \[record\_format\_info\] \[field\_definitions\] \[column\_transforms\]
>
> [Copyright © 1996, 2018, Oracle and/or its affiliates. All rights reserved.](https://docs.oracle.com/cd/E11882_01/dcommon/html/cpyr.htm)
  
  

Note:

These access parameters are collectively referred to as the `opaque_format_spec` in the SQL `CREATE TABLE...ORGANIZATION EXTERNAL` statement.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_7002.htm#SQLRF01402) for information about specifying `opaque_format_spec` when using the SQL `CREATE TABLE...ORGANIZATION EXTERNAL` statement