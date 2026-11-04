---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: F31827-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/lnpls/SHARING-clause.html
tags:
  - oracle
  - 21c
  - pl-sql-language-reference
---

The `SHARING` clause applies only when creating an object in an application root in the context of an application maintenance. This type of object is called an application common object and it can be shared with the application PDBs that belong to the application root.

The `SHARING` clause can appear in the context of creating application common PL/SQL and SQL objects with these SQL statements.

Table 14-2 Summary of Possible Sharing Attributes by Application Common Object Type

| Application Common Object Statement | Possible SHARING Attributes | Syntax and Semantics |
| --- | --- | --- |
| CREATE ANALYTIC VIEW | METADATA, NONE | [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=SQLRF-GUID-EBA7E9BC-3F49-4AA7-9EF6-9255FE7AE466) |
| CREATE ATTRIBUTE DIMENSION | METADATA, NONE | [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=SQLRF-GUID-62722AB0-2136-4BC9-8E76-CBEA13C15196) |
| CREATE CLUSTER | METADATA, NONE | [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=SQLRF-GUID-4DBC701F-AFC3-486D-AA32-B5CB1D6946F7) |
| CREATE CONTEXT | METADATA, NONE | [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=SQLRF-GUID-FDF62812-A884-479C-9C1B-5BD6DDEFE7FA) |
| CREATE DIRECTORY | METADATA, NONE | [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=SQLRF-GUID-8E9C569A-1B06-42C4-9586-0EF83437001A) |
| CREATE FUNCTION | METADATA, NONE | [CREATE FUNCTION Statement](CREATE-FUNCTION-statement.md) |
| CREATE HIERARCHY | METADATA, NONE | [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=SQLRF-GUID-73925877-992B-4624-AA28-8F565E9C3F0D) |
| CREATE INDEXTYPE | METADATA, NONE | [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=SQLRF-GUID-4A7BD0EC-B3E5-4D1D-95C5-C8B52D01D8CE) |
| CREATE JAVA | METADATA, NONE | [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=SQLRF-GUID-69E13452-1F91-4F98-B154-CF5B1C198387) |
| CREATE LIBRARY | METADATA, NONE | [CREATE LIBRARY Statement](CREATE-LIBRARY-statement.md) |
| CREATE MATERIALIZED VIEW LOG | METADATA, NONE | [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=SQLRF-GUID-13902019-D044-4B79-9EB4-1F60652D037B) |
| CREATE OPERATOR | METADATA, NONE | [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=SQLRF-GUID-62676C58-6F57-4572-8C09-7984A8E3EE9F) |
| CREATE PROCEDURE | METADATA, NONE | [CREATE PROCEDURE Statement](CREATE-PROCEDURE-statement.md) |
| CREATE PACKAGE | METADATA, NONE | [CREATE PACKAGE Statement](CREATE-PACKAGE-statement.md) |
| CREATE PACKAGE BODY | METADATA, NONE | [CREATE PACKAGE BODY Statement](CREATE-PACKAGE-BODY-statement.md) |
| CREATE SEQUENCE | METADATA, DATA, NONE | [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=SQLRF-GUID-E9C78A8C-615A-4757-B2A8-5E6EFB130571) |
| CREATE SYNONYM | METADATA, NONE | [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=SQLRF-GUID-A806C82F-1171-478E-A910-F9C6C42739B2) |
| CREATE TABLE | METADATA, DATA, EXTENDED DATA, NONE | [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=SQLRF-GUID-F9CE0CC3-13AE-4744-A43C-EAC7A71AAAB6) |
| CREATE TRIGGER | METADATA, NONE | [CREATE TRIGGER Statement](CREATE-TRIGGER-statement.md) |
| CREATE TYPE | METADATA, NONE | [CREATE TYPE Statement](CREATE-TYPE-statement.md) |
| CREATE TYPE BODY | METADATA, NONE | [CREATE TYPE BODY Statement](CREATE-TYPE-BODY-statement.md) |
| CREATE VIEW | METADATA, DATA, EXTENDED DATA, NONE | [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=SQLRF-GUID-61D2D2B4-DACC-4C7C-89EB-7E50D9594D30) |

Syntax

Semantics

sharing\_clause

Specifies how the object is shared using one of the following sharing attributes:

- `METADATA` - A metadata link shares the metadata, but its data is unique to each container. This type of object is referred to as a metadata-linked application common object.
- `NONE` - The object is not shared and can only be accessed in the application root.

If you omit this clause during an application operation, then the database uses the value of the `DEFAULT_SHARING` initialization parameter to determine the sharing attribute of the object. If the `DEFAULT_SHARING` initialization parameter does not have a value, then the default is `METADATA`.

Restrictions on `SHARING` clause

The sharing clause may only appear during an application installation, upgrade or patch in an application root. You must issue an ` ALTER PLUGGABLE DATABASE APPLICATION ... BEGIN` statement to start the operation and an `ALTER PLUGGABLE DATABASE APPLICATION ... END` statement to end the operation. The sharing\_clause is illegal outside this context and this implies the object is not shared.

You cannot change the sharing attribute of an object after it is created.

Generally, common objects cannot depend on local objects. The exceptions to this rule are:

- the common object being created is a synonym
- the common object being created depends on a local operator

If you try to create a common object that depends on local objects other than these two exceptions, it will result in the creation of a local object.