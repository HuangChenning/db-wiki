---
title: DBMS_EXPFIL
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_expfilref.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 65 DBMS\_EXPFIL

Note:

This functionality is deprecated with Oracle Database Release 11.2 and obsoleted with Release 12.1. For details regarding obsolescence, seeMy Oracle Support Note [ID 1244535.1](https://support.oracle.com/CSP/ui/flash.html#tab=KBHome%28page=KBHome&id=%28%29%29,%28page=KBNavigator&id=%28from=BOOKMARK&bmDocType=DESUPPORT&bmDocID=1244535.1&bmDocDsrc=KB&viewingMode=1143&bmDocTitle=Obsolescence%20Notice:%20Rules%20Manager%20Feature%20of%20Oracle%20Database%29%29)

The `DBMS_EXPFIL` package contains all the procedures used to manage attribute sets, expression sets, expression indexes, optimizer statistics, and privileges by Expression Filter.

See Also:

[Oracle Database Rules Manager and Expression Filter Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/toc.htm) for more information.

This chapter contains the following topics:

- Using DBMS\_EXPFIL
- Summary of Expression Filter Subprograms

---

## Using DBMS\_EXPFIL

This section contains topics that relate to using the Rules Manager `DBMS_EXPFIL` package.

- Security Model

---

### Security Model

The Oracle Database installation runs the `catexf.sql` script to load the `DBMS_EXPFIL` package and create the required Expression Filter schema objects in the `EXFSYS` schema.

`DBMS_EXPFIL` is an `EXFSYS` -owned package compiled with `AUTHID CURRENT_USER`. Any `DBMS_EXPFIL` subprogram called from an anonymous PL/SQL block is run using the privileges of the current user.

Before you issue `COPY_ATTRIBUTE_SET` procedure, the user must have the `EXECUTE` privilege for the object type associated with the original attribute set.

A user requires `SELECT` privileges on a table storing expressions to evaluate them. The `SQL EVALUATE` operator evaluates expressions with the privileges of the owner of the table that stores the expressions. The privileges of the user issuing the query are not considered. The owner of the table can insert, update, and delete expressions. Other users must have `INSERT` and `UPDATE` privileges for the table and `INSERT EXPRESSION` and `UPDATE EXPRESSION` privilege for a specific Expression column in the table to be able to make modifications to it.

Using the `GRANT_PRIVILEGE` procedure, the owner of the table can grant `INSERT EXPRESSION` or `UPDATE EXPRESSION` privileges on one or more Expression columns to other users. Both privileges can be granted to a user by specifying `ALL` for the privilege type.

A user with `CREATE INDEX` privileges on a table cannot create an Expression Filter index unless the user is the owner of the table.

A user must have `EXECUTE` privilege on the `CTX_DDL` package for successful synchronization of the text indexes using the `DBMS_EXPFIL.SYNC_TEXT_INDEXES` procedure.

The `USER_EXPFIL_PRIVILEGES` view lists the privileges of the current user on expression sets belonging to other schemas and the privileges of other users on the expression sets owned by the current user.

---

## Summary of Expression Filter Subprograms

Table 65-1 describes the subprograms in the `DBMS_EXPFIL` package.

All the values and names passed to the procedures defined in the `DBMS_EXPFIL` package are not case sensitive, unless otherwise mentioned. To preserve the case, you use double quotation marks around the values.

Table 65-1 DBMS\_EXPFIL Package Subprograms

| Subprogram | Description |
| --- | --- |
| ADD\_ELEMENTARY\_ATTRIBUTE Procedures | Adds the specified attribute to the attribute set |
| ADD\_FUNCTIONS Procedure | Adds a function, type, or package to the approved list of functions with an attribute set |
| ASSIGN\_ATTRIBUTE\_SET Procedure | Assigns an attribute set to a column storing expressions |
| BUILD\_EXCEPTIONS\_TABLE Procedure | Creates an exception table to hold references to invalid expressions |
| CLEAR\_EXPRSET\_STATS Procedure | Clears the predicate statistics for an expression set |
| COPY\_ATTRIBUTE\_SET Procedure | Makes a copy of the attribute set |
| CREATE\_ATTRIBUTE\_SET Procedure | Creates an attribute set |
| DEFAULT\_INDEX\_PARAMETERS Procedure | Assigns default index parameters to an attribute set |
| DEFAULT\_XPINDEX\_PARAMETERS Procedure | Assigns default XPath index parameters to an attribute set |
| DEFRAG\_INDEX Procedure | Rebuilds the bitmap indexes online to reduce fragmentation |
| DROP\_ATTRIBUTE\_SET Procedure | Drops an unused attribute set |
| GET\_EXPRSET\_STATS Procedure | Collects predicate statistics for an expression set |
| GRANT\_PRIVILEGE Procedure | Grants an expression DML privilege to a user |
| INDEX\_PARAMETERS Procedure | Assigns index parameters to an expression set |
| MODIFY\_OPERATOR\_LIST Procedure | Modifies the list of common operators used in predicates with a certain attribute |
| REVOKE\_PRIVILEGE Procedure | Revokes an expression DML privilege from a user |
| SYNC\_TEXT\_INDEXES Procedure | Synchronizes the indexes defined to process the predicates involving the `CONTAINS` operator in stored expressions |
| UNASSIGN\_ATTRIBUTE\_SET Procedure | Breaks the association between a column storing expressions and the attribute set |
| VALIDATE\_EXPRESSIONS Procedure | Validates expression metadata and the expressions stored in a column |
| XPINDEX\_PARAMETERS Procedure | Assigns XPath index parameters to an expression set |

---

### ADD\_ELEMENTARY\_ATTRIBUTE Procedures

This procedure adds the specified attribute to the attribute set. The procedure is overloaded. The different functionality of each form of syntax is presented along with the definitions.

Syntax

Adds the specified elementary attribute to the attribute set:

```
DBMS_EXPFIL.ADD_ELEMENTARY_ATTRIBUTE (
   attr_set   IN   VARCHAR2, 
   attr_name  IN   VARCHAR2, 
   attr_type  IN   VARCHAR2, 
   attr_defv1 IN   VARCHAR2 DEFAULT NULL);
```

Identifies the elementary attributes that are table aliases and adds them to the attribute set:

```
DBMS_EXPFIL.ADD_ELEMENTARY_ATTRIBUTE (
   attr_set   IN   VARCHAR2,
   attr_name  IN   VARCHAR2,
   tab_alias  IN   exf$table_alias);
```

Allows addition of text attributes to the attribute set:

```
DBMS_EXPFIL.ADD_ELEMENTARY_ATTRIBUTE (
   attr_set       IN   VARCHAR2,
   attr_name      IN   VARCHAR2,
   attr_type      IN   VARCHAR2,
   text_pref      IN   EXF$TEXT);
```

Parameters

Table 65-2 ADD\_ELEMENTARY\_ATTRIBUTE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `attr_set` | Name of the attribute set to which this attribute is added |
| `attr_name` | Name of the elementary attribute to be added. No two attributes in a set can have the same name. |
| `attr_type` | Datatype of the attribute. This argument accepts any standard SQL datatype or the name of an object type that is accessible to the current user. |
| `attr_defv1` | Default value for the elementary attribute |
| `tab_alias` | Type that identifies the database table to which the attribute is aliased |
| `text_pref` | Text preferences such as LEXER and WORDLIST specification. |

Usage Notes

- If the attribute set receiving the elementary attribute was originally created from an existing object type, then additional attributes cannot be added.
- One or more, or all elementary attributes in an attribute set can be table aliases. If an elementary attribute is a table alias, then the value assigned to the elementary attribute is a `ROWID` from the corresponding table. An attribute set with one or more table alias attributes cannot be created from an existing object type. For more information about table aliases, see [Oracle Database Rules Manager and Expression Filter Developer's Guide.](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_app_a.htm#EXPRN111)
- Elementary attributes cannot be added to an attribute set that is already assigned to a column storing expressions.
- The default value specification for an attribute is similar to a default value specification for a table column. The resulting default values should agree with the datatype of the attribute. For example, valid default values for an attribute of `DATE` datatype are `SYSDATE` and `to_date('01-01-2004','DD-MM-YYYY')`.
- See the section on defining attribute sets in [Oracle Database Rules Manager and Expression Filter Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_expconcepts.htm#EXPRN011) for more information about adding elementary attributes.
- Related views: [`USER_EXPFIL_ATTRIBUTE_SETS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN056) and [`USER_EXPFIL_ATTRIBUTES`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN055).
- This procedure with a text preference bound to the `text_pref` argument creates a text attribute in the attribute set. The data type for such an attribute should be a `VARCHAR2` or a `CLOB`. The preferences specified with this procedure are validated only when an Expression Filter index is created using this attribute set.
- These preferences are used in the creation of the `CTXRULE` index that processes the predicates involving `CONTAINS` operator. The valid preferences are those that are valid in the `PARAMETERS` clause of `CTXRULE` index creation. See [Oracle Text Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/text.112/e24435/toc.htm) for the syntax.

Examples

The following commands add two elementary attributes to an attribute set:

```
BEGIN
  DBMS_EXPFIL.ADD_ELEMENTARY_ATTRIBUTE (
                               attr_set   => 'HRAttrSet',
                               attr_name  => 'HRREP',
                               attr_type  => 'VARCHAR2(30)'
                               attr_defv1 => 'Betty Smith');
  DBMS_EXPFIL.ADD_ELEMENTARY_ATTRIBUTE (
                               attr_set  => 'HRAttrSet',
                               attr_name => 'DEPT',
                               tab_alias => exf$table_alias('DEPT'));
END;
/
```

The following commands define a CreationTime elementary attribute that takes the database time as the default value.

```
BEGIN
  DBMS_EXPFIL.ADD_ELEMENTARY_ATTRIBUTE (
                          attr_set   => 'PurchaseOrder',
                          attr_name  => 'CreationTime',
                          attr_type  => 'DATE',
                          attr_defvl => 'SYSDATE');
END;
/
```

Alternately, the following commands initialize the `CreationTime` attribute to a specific value when it is not explicitly specified in the data item passed to the EVALUATE operator.

```
BEGIN
  DBMS_EXPFIL.ADD_ELEMENTARY_ATTRIBUTE (
                          attr_set   => 'PurchaseOrder',
                          attr_name  => 'CreationTime',
                          attr_type  => 'DATE',
                          attr_defvl => 'to_date(''01-01-2004'',''DD-MM-YYYY'')');
END;
/
```

The following commands create an attribute set with a `Model` attribute of `VARCHAR2` data type and an InsReport attribute configured for text predicates.

```
BEGIN
   DBMS_EXPFIL.CREATE_EVENT_STRUT(event_struct => 'Car4Sale');
   // create scalar attributes
   DBMS_EXPFIL.ADD_ELEMENTARY_ATTRIBUTE(
                       attr_set  => 'Car4Sale',
                       attr_name => 'Model',
                       attr_type => 'VARCHAR2(30)');

   //create text attribute
   DBMS_EXPFIL.ADD_ELEMENTARY_ATTRIBUTE(
                       attr_set  => 'Car4Sale',
                       attr_name => 'InsReport',
                       attr_type => 'CLOB',
                       attr_type => exf$text(
                                    'LEXER insrpt_lexer
                                     WORDLIST insrpt_wordlist'));
END;
/
```

---

### ADD\_FUNCTIONS Procedure

This procedure adds a user-defined function, package, or type representing a set of functions to the attribute set.

Syntax

```
DBMS_EXPFIL.ADD_FUNCTIONS (
   attr_set   IN   VARCHAR2, 
   funcs_name IN   VARCHAR2);
```

Parameters

Table 65-3 ADD\_FUNCTIONS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `attr_set` | Name of the attribute set to which the functions are added |
| `funcs_name` | Name of a function, package, or type (representing a function set) or its synonyms |

Usage Notes

- By default, an attribute set implicitly allows references to all Oracle Database supplied SQL functions for use by the expression set. If the expression set refers to a user-defined function, the function must be explicitly added to the attribute set.
- The `ADD_FUNCTIONS` procedure adds a user-defined function or a package (or type) representing a set of functions to the attribute set. Any new or modified expressions are validated using this list. The function added to the attribute set, and thus used in the stored expressions, should not perform any DML or DDL (database state changing) operations. Oracle Database catches violations to this rule only at run-time while evaluating the expressions. Violations are not checked during the `ADD_FUNCTIONS` procedure call.
- The function or the package name can be specified with a schema extension. If a function name is specified without a schema extension, only such references in the expression set are considered valid. The expressions in a set can be restricted to use a synonym to a function or a package by adding the corresponding synonym to the attribute set. This preserves the portability of the expression set to other schemas.
- See the section on defining attribute sets in [Oracle Database Rules Manager and Expression Filter Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_expconcepts.htm#EXPRN012) for more information about adding functions to an attribute set.
- Related views: [`USER_EXPFIL_ATTRIBUTE_SETS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN056) and [`USER_EXPFIL_EXPRESSION_SETS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN058)

Examples

The following commands add two functions to the attribute set:

```
BEGIN 
  DBMS_EXPFIL.ADD_FUNCTIONS (
   attr_set   => 'Car4Sale', 
   funcs_name => 'HorsePower');
  DBMS_EXPFIL.ADD_FUNCTIONS (
   attr_set   => 'Car4Sale', 
   funcs_name => 'Scott.CrashTestRating');
END;
/
```

---

### ASSIGN\_ATTRIBUTE\_SET Procedure

This procedure assigns an attribute set to a `VARCHAR2` column in a user table to create an Expression column.

Syntax

```
DBMS_EXPFIL.ASSIGN_ATTRIBUTE_SET (
   attr_set   IN   VARCHAR2,
   expr_tab   IN   VARCHAR2,
   expr_col   IN   VARCHAR2,
   force      IN   VARCHAR2 DEFAULT 'FALSE');
```

Parameters

Table 65-4 ASSIGN\_ATTRIBUTE\_SET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `attr_set` | Name of the attribute set |
| `expr_tab` | Name of table storing the expression set |
| `expr_col` | Name of column in the table that stores the expressions |
| `force` | Argument used to trust the existing expressions in a table (and skip validation) |

Usage Notes

- The `ASSIGN_ATTRIBUTE_SET` procedure assigns an attribute set to a `VARCHAR2` column in a user table to create an Expression column. The attribute set contains the elementary attribute names and their data types and any functions used in the expressions. The Expression column, the column named by the `expr_col` parameter to store the expression, uses the attribute set to validate changes and additions to the expression set.
- An attribute set can be assigned only to a table column in the same schema as the attribute set. An attribute set can be assigned to one or more table columns. Assigning an attribute set to a column storing expressions implicitly creates methods for the associated object type. For this operation to succeed, the object type cannot have any dependent objects before the attribute set is assigned.
- By default, the column should not have any expressions at the time of association. However, if the values in the column are known to be valid expressions, you can use a value of `'TRUE'` for the `force` argument to assign the attribute set to a column containing expressions.
- See the information about defining Expression columns in [Oracle Database Rules Manager and Expression Filter Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_expconcepts.htm#EXPRN012) for more information about adding elementary attributes.
- Related views: [`USER_EXPFIL_ATTRIBUTE_SETS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN056) and [`USER_EXPFIL_EXPRESSION_SETS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN058)

Examples

The following command assigns the attribute set to a column storing expressions. The expression set should be empty at the time of association.

```
BEGIN
  DBMS_EXPFIL.ASSIGN_ATTRIBUTE_SET (attr_set => 'Car4Sale', 
                                    expr_tab => 'consumer',
                                    expr_col => 'interest');
END;
/
```

---

### BUILD\_EXCEPTIONS\_TABLE Procedure

This procedure creates the exception table, used in validation, in the current schema.

Syntax

```
DBMS_EXPFIL.BUILD_EXCEPTIONS_TABLE (
   exception_tab IN VARCHAR2);
```

Parameters

Table 65-5 BUILD\_EXCEPTIONS\_TABLE Procedure Parameter

| Parameter | Description |
| --- | --- |
| `exception_tab` | Name of the exception table |

Usage Notes

- During expression validation, you can optionally provide the name of the exception table in which the references to the invalid expressions are stored. The `BUILD_EXCEPTIONS_TABLE` procedure creates the exception table in the current schema.
- See the section on evaluation semantics in [Oracle Database Rules Manager and Expression Filter Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_expconcepts.htm#EXPRN015) and VALIDATE\_EXPRESSIONS Procedure for more information.
- Related view: `USER_TABLES`

Examples

The following command creates the exception table, `InterestExceptions`, in the current schema:

```
BEGIN
  DBMS_EXPFIL.BUILD_EXCEPTIONS_TABLE (exception_tab => 'InterestExceptions');
END;
/
```

---

### CLEAR\_EXPRSET\_STATS Procedure

This procedure clears the predicate statistics for the expression set stored in a table column.

Syntax

```
DBMS_EXPFIL.CLEAR_EXPRSET_STATS (
   expr_tab   IN   VARCHAR2,
   expr_col   IN   VARCHAR2);
```

Parameters

Table 65-6 CLEAR\_EXPRSET\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `expr_tab` | Name of table storing the expression set |
| `expr_col` | Name of column in the table that stores the expressions |

Examples

The following command clears the predicate statistics for the expression set stored in `interest` column of the `consumer` table:

```
BEGIN
  DBMS_EXPFIL.CLEAR_EXPRSET_STATS (expr_tab => 'consumer',
                                    expr_col => 'interest');
END;
/
```

---

### COPY\_ATTRIBUTE\_SET Procedure

This procedure copies an attribute set along with its user-defined function list and default index parameters to another set.

Syntax

```
DBMS_EXPFIL.COPY_ATTRIBUTE_SET (
   from_set   IN   VARCHAR2,
   to_set     IN   VARCHAR2);
```

Parameters

Table 65-7 COPY\_ATTRIBUTE\_SET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `from_set` | Name of an existing attribute set to be copied |
| `to_set` | Name of the new attribute set |

Usage Notes

- A schema-extended name can be used for the `from_set` argument to copy an attribute set across schemas. Before you issue this command, you must have the `EXECUTE` privilege for the object type associated with the original attribute set. Ensure that any references to schema objects (user-defined functions, tables, and embedded objects) are valid in the new schema.
- The default index parameters and the user-defined function list of the new set can be changed independent of the original set.
- Related views: `ALL_EXPFIL_ATTRIBUTE_SETS` and `ALL_EXPFIL_ATTRIBUTES`.

Examples

The following command makes a copy of the `Car4Sale` attribute set:

```
BEGIN
  DBMS_EXPFIL.COPY_ATTRIBUTE_SET (from_set => 'Car4Sale', 
                                  to_set   => 'Vehicle');
END;
/
```

---

### CREATE\_ATTRIBUTE\_SET Procedure

This procedure creates an empty attribute set or an attribute set with a complete set of elementary attributes derived from an object type with a matching name.

Syntax

```
DBMS_EXPFIL.CREATE_ATTRIBUTE_SET (
   attr_set   IN   VARCHAR2,
   from_type  IN   VARCHAR2 DEFAULT 'NO');
```

Parameters

Table 65-8 CREATE\_ATTRIBUTE\_SET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `attr_set` | Name of the attribute set to be created |
| `from_type` | `YES`, if the attributes for the attribute set should be derived from an existing object type |

Usage Notes

- The object type used for an attribute set cannot contain any user methods, and it should not be an evolved type (with the use of `ALTER TYPE` command). This object type should not have any dependent objects at the time of the attribute set creation. If the attribute set is not derived from an existing object type, this procedure creates an object type with a matching name.
- An attribute set with one or more table alias attributes cannot be derived from an object type. For this purpose, create an empty attribute set and add one elementary attribute at a time using the `DBMS_EXPFIL`.`ADD_ELEMENTARY_ATTRIBUTE` procedure. (See [Oracle Database Rules Manager and Expression Filter Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_app_a.htm#EXPRN111) for more information.)
- See the section on defining attribute sets in [Oracle Database Rules Manager and Expression Filter Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_expconcepts.htm#EXPRN011) and ADD\_ELEMENTARY\_ATTRIBUTE Procedures for more information.
- Related views: [`USER_EXPFIL_ATTRIBUTE_SETS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN056) and [`USER_EXPFIL_ATTRIBUTES`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN055).

Examples

The following commands create an attribute set with all the required elementary attributes derived from the `Car4Sale` type:

```
CREATE OR REPLACE TYPE Car4Sale AS OBJECT 
                                   (Model   VARCHAR2(20), 
                                    Year    NUMBER, 
                                    Price   NUMBER, 
                                    Mileage NUMBER);
/
 
BEGIN 
  DBMS_EXPFIL.CREATE_ATTRIBUTE_SET(attr_set  => 'Car4Sale',
                                   from_type => 'YES');
END;
/
```

Assuming that the `Car4Sale` type does not exist, the attribute set can be created from scratch as shown in the following example:

```
BEGIN
  DBMS_EXPFIL.CREATE_ATTRIBUTE_SET(attr_set => 'Car4Sale');
  DBMS_EXPFIL.ADD_ELEMENTARY_ATTRIBUTE( 
                               attr_set  => 'Car4Sale',
                               attr_name => 'Model',
                               attr_type => 'VARCHAR2(20)');
  DBMS_EXPFIL.ADD_ELEMENTARY_ATTRIBUTE(
                               attr_set  => 'Car4Sale',
                               attr_name => 'Year',
                               attr_type => 'NUMBER');
  DBMS_EXPFIL.ADD_ELEMENTARY_ATTRIBUTE(
                               attr_set  => 'Car4Sale',
                               attr_name => 'Price',
                               attr_type => 'NUMBER');
  DBMS_EXPFIL.ADD_ELEMENTARY_ATTRIBUTE(
                               attr_set  => 'Car4Sale',
                               attr_name => 'Mileage',
                               attr_type => 'NUMBER');
END;
/
```

---

### DEFAULT\_INDEX\_PARAMETERS Procedure

This procedure assigns default index parameters to an attribute set. It also adds or drops a partial list of stored and indexed attributes to or from the default list associated with the attribute list.

Syntax

```
DBMS_EXPFIL.DEFAULT_INDEX_PARAMETERS (
   attr_set   IN   VARCHAR2,
   attr_list  IN   EXF$ATTRIBUTE_LIST,
   operation  IN   VARCHAR2 DEFAULT 'ADD');
```

Parameters

Table 65-9 DEFAULT\_INDEX\_PARAMETERS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `attr_set` | Name of the attribute set |
| `attr_list` | An instance of `EXF$ATTRIBUTE_LIST` with a partial list of (default) stored and indexed attributes for an Expression Filter index |
| `operation` | Operation to be performed on the list of index parameters. Default value: `ADD`. Valid values: `ADD` and `DROP`. |

Usage Notes

- Existing Expression Filter indexes are not modified when the default parameters for the corresponding attribute set are changed. The new index defaults are used when a new Expression Filter index is created and when an existing index is rebuilt. (See the section on alter index rebuild in [Oracle Database Rules Manager and Expression Filter Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_sql.htm#EXPRN047) for more information about rebuilding indexes.)
- See the section on creating an index from default parameters in [Oracle Database Rules Manager and Expression Filter Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_indexexpressions.htm#EXPRN024) for more information about assigning default index parameters to an attribute set.
- Related views: [`USER_EXPFIL_ATTRIBUTE_SETS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN056) and [`USER_EXPFIL_DEF_INDEX_PARAMS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN057)

Examples

The following command adds the specified stored and indexed attributes to the attribute set's default index parameters list:

```
BEGIN
 DBMS_EXPFIL.DEFAULT_INDEX_PARAMETERs(
    attr_set  => 'Car4Sale', 
    attr_list => exf$attribute_list (
       exf$attribute (attr_name => 'Model',            
                      attr_oper => exf$indexoper('='),
                      attr_indexed => 'TRUE'),         
       exf$attribute (attr_name => 'Price', 
                      attr_oper => exf$indexoper('all'), 
                      attr_indexed => 'TRUE'), 
       exf$attribute (attr_name => 'HorsePower(Model, Year)', 
                      attr_oper => exf$indexoper('=','<','>','>=','<='), 
                      attr_indexed => 'FALSE'),
       exf$attribute (attr_name => 'CrashTestRating(Model, Year)', 
                      attr_oper => exf$indexoper('=','<','>','>=','<='), 
                      attr_indexed => 'FALSE')),
    operation => 'ADD');
END;
/
```

The following command drops the `CrashTestRating(Model, Year)` attribute (stored or indexed) from the previous list.

```
BEGIN
  DBMS_EXPFIL.DEFAULT_INDEX_PARAMETERS(
      attr_set  => 'Car4Sale', 
      attr_list => exf$attribute_list (
         exf$attribute (attr_name => 'CrashTestRating(Model, Year)')),
      operation => 'DROP');
END;
/
```

---

### DEFAULT\_XPINDEX\_PARAMETERS Procedure

This procedure adds (or drops) a partial list of XPath parameters to the default index parameters associated with the attribute set.

Syntax

```
DBMS_EXPFIL.DEFAULT_XPINDEX_PARAMETERS (
   attr_set   IN   VARCHAR2,
   xmlt_attr  IN   VARCHAR2,
   xptag_list IN   EXF$XPATH_TAGS,
   operation  IN   VARCHAR2 DEFAULT 'ADD');
```

Parameters

Table 65-10 DEFAULT\_XPINDEX\_PARAMETERS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `attr_set` | Name of the attribute set |
| `xmlt_attr` | Name of the attribute with the `XMLType` datatype |
| `xptag_list` | An instance of `EXF$XPATH_TAGS` type with a partial list of XML elements and attributes to be configured for the Expression Filter index |
| `operation` | Operation to be performed on the list of index parameters. Default value: `ADD`. Valid values: `ADD` and `DROP`. |

Usage Notes

- The attribute set used for an expression set may have one or more XML type attributes (defined with `XMLType` datatype) and the corresponding expressions may contain XPath predicates on these attributes. The Expression Filter index created for the expression set can be tuned to process these XPath predicates efficiently by using some XPath-specific index parameters (in addition to some non-XPath index parameters).
- The `DEFAULT_XPINDEX_PARAMETERS` procedure adds (or drops) a partial list of XPath parameters to the default index parameters associated with the attribute set. The XPath parameters are assigned to a specific `XMLType` attribute in the attribute set and this information can be viewed using the `USER_EXPFIL_DEF_INDEX_PARAMS` view. The `DEFAULT_INDEX_PARAMETERS` procedure and the `DEFAULT_XPINDEX_PARAMETERS` procedure can be used independent of each other. They maintain a common list of default index parameters for the attribute set.
- See the section on index tuning for XPath predicates in [Oracle Database Rules Manager and Expression Filter Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_xpathpredicates.htm#EXPRN033) for more information about XPath parameters to the default index parameters of an attribute set. See also DEFAULT\_INDEX\_PARAMETERS Procedure for more information about default index parameters.
- Related views: [`USER_EXPFIL_ATTRIBUTES`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN055) and [`USER_EXPFIL_DEF_INDEX_PARAMS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN057).

Note:

The values assigned to the `tag_name` argument of `exf$xpath_tag` type are case sensitive.

Examples

The following command adds the specified XML tags to the default index parameters list along with their preferences such as positional or value filter and indexed or stored predicate group:

```
BEGIN
  DBMS_EXPFIL.DEFAULT_XPINDEX_PARAMETERS(
       attr_set   => 'Car4Sale',
       xmlt_attr  => 'Details',
       xptag_list =>                                    --- XPath tag list 
         exf$xpath_tags(
           exf$xpath_tag(tag_name    => 'stereo@make',  --- XML attribute
                         tag_indexed => 'TRUE',
                         tag_type    => 'VARCHAR(15)'), --- value filter
           exf$xpath_tag(tag_name    => 'stereo',       --- XML element
                         tag_indexed => 'FALSE',
                         tag_type    => null),          --- positional filter
           exf$xpath_tag(tag_name    => 'memory',       --- XML element
                         tag_indexed => 'TRUE',
                         tag_type    => 'VARCHAR(10)'), --- value filter
           exf$xpath_tag(tag_name    => 'GPS',
                         tag_indexed => 'TRUE',
                         tag_type    => null)
          )
        );
END;
/
```

The following command drops the `stereo@make` tag from the default index parameters:

```
BEGIN
  DBMS_EXPFIL.DEFAULT_XPINDEX_PARAMETERS(
       attr_set   => 'Car4Sale',
       xmlt_attr  => 'Details',
       xptag_list =>                                    --- XPath tag list 
         exf$xpath_tags(
           exf$xpath_tag(tag_name    => 'stereo@make')
         ),
       operation => 'DROP'
       );
END;
/
```

---

### DEFRAG\_INDEX Procedure

This procedure rebuilds the bitmap indexes online and thus reduces the fragmentation.

Syntax

```
DBMS_EXPFIL.DEFRAG_INDEX (
   idx_name   IN  VARCHAR2);
```

Parameters

Table 65-11 DEFRAG\_INDEX Procedure Parameter

| Parameter | Description |
| --- | --- |
| `idx_name` | Name of the Expression Filter index |

Usage Notes

- The bitmap indexes defined for the indexed attributes of an Expression Filter index become fragmented as additions and updates are made to the expression set. This can affect performance. The `DEFRAG_INDEX` procedure rebuilds the bitmap indexes online and thus reduces the fragmentation.
- Indexes can be defragmented when the expression set is being modified. However, you should schedule defragmentation when the workload is relatively light, such as 2 a.m.
- See the section on index storage and maintenance in [Oracle Database Rules Manager and Expression Filter Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_indexexpressions.htm#EXPRN026) for more information about rebuilding indexes.
- Related views: [`USER_EXPFIL_INDEXES`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN061) and `USER_INDEXES`.

Examples

The following command is issued to defragment the bitmap indexes associated with the Expression Filter index:

```
BEGIN
  DBMS_EXPFIL.DEFRAG_INDEX (idx_name => 'InterestIndex');
END;
/
```

---

### DROP\_ATTRIBUTE\_SET Procedure

This procedure drops an attribute set not being used for any expression set.

Syntax

```
DBMS_EXPFIL.DROP_ATTRIBUTE_SET (
   attr_set   IN   VARCHAR2);
```

Parameters

Table 65-12 DROP\_ATTRIBUTE\_SET Procedure Parameter

| Parameter | Description |
| --- | --- |
| `attr_set` | Name of the attribute set to be dropped |

Usage Notes

- The `DROP_ATTRIBUTE_SET` procedure drops an attribute set not being used for any expression set. If the attribute set was initially created from an existing object type, the object type remains after dropping the attribute set. Otherwise, the object type is dropped with the attribute set.
- Related views: [`USER_EXPFIL_ATTRIBUTE_SETS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN056) and [`USER_EXPFIL_EXPRESSION_SETS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN058).

Examples

Assuming that the attribute set is not used by an Expression column, the following command drops the attribute set:

```
BEGIN
  DBMS_EXPFIL.DROP_ATTRIBUTE_SET(attr_set => 'Car4Sale');  
END;
/
```

---

### GET\_EXPRSET\_STATS Procedure

This procedure computes the predicate statistics for an expression set and stores them in the expression filter dictionary.

Syntax

```
DBMS_EXPFIL.GET_EXPRSET_STATS (
   expr_tab   IN   VARCHAR2,
   expr_col   IN   VARCHAR2);
```

Parameters

Table 65-13 GET\_EXPRSET\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `expr_tab` | Name of table storing the expression set |
| `expr_col` | Name of column in the table that stores the expressions |

Usage Notes

- When a representative set of expressions are stored in a table column, you can use predicate statistics for those expressions to configure the corresponding Expression Filter index (using the `TOP` parameters clause). The `GET_EXPRSET_STATS` procedure computes the predicate statistics for an expression set and stores them in the expression filter dictionary.
- See the section on creating an index from statistics in [Oracle Database Rules Manager and Expression Filter Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_indexexpressions.htm#EXPRN024) for more information about using predicate statistics.
- Related views: [`USER_EXPFIL_EXPRESSION_SETS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN058) and [`USER_EXPFIL_EXPRSET_STATS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN059).

Examples

The following command computes the predicate statistics for the expressions stored in the `interest` column of the `consumer` table:

```
BEGIN
  DBMS_EXPFIL.GET_EXPRSET_STATS (expr_tab => 'consumer',
                                 expr_col => 'interest');
END;
/
```

---

### GRANT\_PRIVILEGE Procedure

This procedure grants privileges on one or more Expression columns to other users.

Syntax

```
DBMS_EXPFIL.GRANT_PRIVILEGE (
   expr_tab   IN  VARCHAR2,
   expr_col   IN  VARCHAR2,
   priv_type  IN  VARCHAR2,
   to_user    IN  VARCHAR2);
```

Parameters

Table 65-14 GRANT\_PRIVILEGE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `expr_tab` | Name of table storing the expression set |
| `expr_col` | Name of column in the table that stores the expressions |
| `priv_type` | Type of the privilege to be granted. Valid values: INSERT EXPRESSION, UPDATE EXPRESSION, ALL. |
| `to_user` | User to whom the privilege is to be granted |

Usage Notes

- The SQL `EVALUATE` operator evaluates expressions with the privileges of the owner of the table that stores the expressions. The privileges of the user issuing the query are not considered. The owner of the table can insert, update, and delete expressions. Other users must have `INSERT` and `UPDATE` privileges for the table and `INSERT EXPRESSION` and `UPDATE EXPRESSION` privilege for a specific Expression column in the table.
- Using the `GRANT_PRIVILEGE` procedure, the owner of the table can grant `INSERT` `EXPRESSION` or `UPDATE` `EXPRESSION` privileges on one or more Expression columns to other users. Both the privileges can be granted to a user by specifying `ALL` for the privilege type.
- See REVOKE\_PRIVILEGE Procedure and the section on granting and revoking privileges in [Oracle Database Rules Manager and Expression Filter Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_expconcepts.htm#EXPRN016) for more information about granting and revoking privileges.
- Related views: [`USER_EXPFIL_EXPRESSION_SETS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN058) and [`USER_EXPFIL_PRIVILEGES`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN063).

Examples

The owner of `consumer` table can grant `INSERT` `EXPRESSION` privileges to user `SCOTT` with the following command. User `SCOTT` should also have `INSERT` privileges on the table so that he can add new expressions to the set.

```
BEGIN
  DBMS_EXPFIL.GRANT_PRIVILEGE (expr_tab  => 'consumer',
                               expr_col  => 'interest',
                               priv_type => 'INSERT EXPRESSION',
                               to_user   => 'SCOTT');
END;
```

---

### INDEX\_PARAMETERS Procedure

This procedure fine-tunes the index parameters for each expression set before index creation.

Syntax

```
DBMS_EXPFIL.INDEX_PARAMETERS (
   expr_tab   IN   VARCHAR2,
   expr_col   IN   VARCHAR2,
   attr_list  IN   EXF$ATTRIBUTE_LIST,
   operation  IN   VARCHAR2 DEFAULT 'ADD');
```

Parameters

Table 65-15 INDEX\_PARAMETERS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `expr_tab` | Name of table storing the expression set |
| `expr_col` | Name of column in the table that stores the expressions. |
| `attr_list` | An instance of `EXF$ATTRIBUTE_LIST` with a partial list of stored and indexed attributes |
| `operation` | Operation to be performed on the list of index parameters. Default value: `ADD`. Valid values: `ADD` and `DROP`. |

Usage Notes

- An attribute set can be used by multiple expression sets stored in different columns of user tables. By default, the index parameters associated with the attribute set are used to define an Expression Filter index on an expression set. If you need to fine-tune the index for each expression set, you can specify a small list of the index parameters in the `PARAMETERS` clause of the `CREATE` `INDEX` statement. However, when an Expression Filter index uses a large number of index parameters or if the index is configured for XPath predicates, fine-tuning the parameters with the `CREATE` `INDEX` statement is not possible.
- The `INDEX_PARAMETERS` procedure fine-tunes the index parameters for each expression set before index creation. This procedure can be used to copy the defaults from the corresponding attribute set and selectively add (or drop) additional index parameters for the expression set. (You use the `XPINDEX_PARAMETERS` procedure to add and drop XPath index parameters.) The Expression Filter index defined for an expression set with a non-empty list of index parameters always uses these parameters. The `INDEX_PARAMETERS` procedure cannot be used when the Expression Filter index is already defined for the column storing expressions.
- The operations allowed with this procedure include:
	- Deriving the current list of default index parameters (including any XPath-specific parameters) from the corresponding attribute set and assigning them to the specified expression set (a value of `DEFAULT` for the operation argument).
		- Adding (or dropping) one or more attributes to (or from) the current list of parameters assigned to the expression set (values of `ADD` or `DROP` for the operation argument).
		- Clearing the index parameters assigned to the expression set. This enables the user to start using default parameters or tune the parameters from scratch (a value of `CLEAR` for the operation argument).
	Note:
	This procedure is useful only when an attribute set is shared across multiple expression sets. In all other cases, the defaults assigned to the attribute set can be tuned for the expression set using it.
- See the section on creating an index from exact parameters in [Oracle Database Rules Manager and Expression Filter Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_indexexpressions.htm#EXPRN024) and XPINDEX\_PARAMETERS Procedure for more information.
- Related views: [`USER_EXPFIL_EXPRESSION_SETS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN058), [`USER_EXPFIL_DEF_INDEX_PARAMS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN057) and [`USER_EXPFIL_INDEX_PARAMS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN060).

Examples

The following command synchronizes the expression set's index parameters with the defaults associated with the corresponding attribute set:

```
BEGIN
  DBMS_EXPFIL.INDEX_PARAMETERS(expr_tab  => 'consumer',
                               expr_col  => 'interest',
                               attr_list => null, 
                               operation => 'DEFAULT');
END;
/
```

The following command adds a stored attribute to the expression set's index parameters.

```
BEGIN
  DBMS_EXPFIL.INDEX_PARAMETERS(expr_tab  => 'consumer',
                               expr_col  => 'interest',
                               attr_list =>
                                exf$attribute_list (
                                 exf$attribute (
                                   attr_name => 'CrashTestRating(Model, Year)',
                                   attr_oper => exf$indexoper('all'),
                                   attr_indexed => 'FALSE')),
                               operation => 'ADD');
END;
/
```

The following command clears the index parameters associated with the expression set:

```
BEGIN
  DBMS_EXPFIL.INDEX_PARAMETERS(expr_tab  => 'consumer',
                               expr_col  => 'interest',
                               attr_list => null, 
                               operation => 'CLEAR');
END;
/
```

A subsequent index creation will use the default index parameters assigned to the corresponding attribute set.

---

### MODIFY\_OPERATOR\_LIST Procedure

This procedure modifies the list of common operators associated with a certain attribute in the attribute set.

Syntax

```
DBMS_EXPFIL.MODIFY_OPERATOR_LIST (
   attr_set   IN   VARCHAR2,
   attr_name  IN   VARCHAR2,
   attr_oper  IN   EXF$INDEXOPER);
```

Parameters

Table 65-16 MODIFY\_OPERATOR\_LIST Procedure Parameters

| Parameter | Description |
| --- | --- |
| `attr_set` | Name of the attribute set |
| `attr_name` | Name of the stored or indexed attribute being modified |
| `attr_oper` | New list of operators that are frequently used in the predicates with the attribute |

Usage Notes

- The `MODIFY_OPERATOR_LIST` procedure modifies the operator list for the stored and indexed attributes defined in the default index parameters of the attribute set. Existing Expression Filter indexes are not affected when an attribute's operator list is modified. The updated index defaults are used when a new Expression Filter index is created or when an existing index is rebuilt.
- Related views: [`USER_EXPFIL_DEF_INDEX_PARAMS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN057)

Examples

The following command modifies the operator list associated with the `HorsePower(Model,Year)` attribute defined in the `Car4Sale` attribute set.

```
BEGIN
  DBMS_EXPFIL.MODIFY_OPERATOR_LIST (
    attr_set => 'Car4Sale',
    attr_name => 'HorsePower(Model, Year)',
    attr_oper => exf$indexoper('=','<','>', 'between'));
END;
/
```

---

### REVOKE\_PRIVILEGE Procedure

This procedure revokes an expression privilege previously granted by the owner.

Syntax

```
DBMS_EXPFIL.REVOKE_PRIVILEGE (
   expr_tab   IN  VARCHAR2,
   expr_col   IN  VARCHAR2,
   priv_type  IN  VARCHAR2,
   from_user  IN  VARCHAR2);
```

Parameters

Table 65-17 REVOKE\_PRIVILEGE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `expr_tab` | Name of table storing the expression set |
| `expr_col` | Name of column in the table that stores the expressions |
| `priv_type` | Type of privilege to be revoked |
| `from_user` | User from whom the privilege is to be revoked |

Usage Notes

- See GRANT\_PRIVILEGE Procedure and the section on granting and revoking privileges in [Oracle Database Rules Manager and Expression Filter Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_expconcepts.htm#EXPRN016) for more information about granting and revoking privileges.
- Related views: [`USER_EXPFIL_EXPRESSION_SETS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN058) and [`USER_EXPFIL_PRIVILEGES`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN063).

Examples

The following command revokes the `INSERT EXPRESSION` privilege on the `interest` column of the `consumer` table from user `SCOTT`:

```
BEGIN
  DBMS_EXPFIL.REVOKE_PRIVILEGE (expr_tab  => 'consumer',
                                expr_col  => 'interest',
                                priv_type => 'INSERT EXPRESSION',
                                 from_user => 'SCOTT');
END;/
```

---

### SYNC\_TEXT\_INDEXES Procedure

This procedure synchronizes the indexes defined to process the predicates involving the `CONTAINS` operator in stored expressions.

Syntax

```
DBMS_EXPFIL.SYNC_TEXT_INDEXES (
     expr_tab   IN   VARCHAR2);
```

Parameters

Table 65-18 SYNC\_TEXT\_INDEXES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `expr_tab` | Name of table with expression columns containing text predicates |

Usage Notes

- When an expression filter index is defined on a column storing expressions, any text predicates in the expressions are indexed using a `CTXRULE` index. Unlike the other types of indexes (bitmap for scalar and XML predicates or spatial for spatial predicates) used to process the predicates in the expression set, the `CTXRULE` index defined to process the text predicates is not transactional in nature. That is, when the text predicates are updated with DML operations on the table storing expressions, the new predicates are not automatically reflected in the corresponding `CTXRULE` index. This could result in inconsistent results until the `CTXRULE` index is synchronized. This procedure can be used to synchronize all the `CTXRULE` indexes associated with a table with one or more expression columns. This procedure identifies all the `CTXRULE` indexes and invokes the CTX\_DDL.SYNC\_INDEX procedure on each of these indexes.
	You must have the `EXECUTE` privilege on the CTX\_DDL package for successful synchronization of the text indexes.

Examples

The following command synchronizes the text indexes associated with the expression columns in the `consumer` table:

```
BEGIN
  DBMS_EXPFIL.SYNC_TEXT_INDEXES (expr_tab => 'consumer');
END;
/
```

---

### UNASSIGN\_ATTRIBUTE\_SET Procedure

This procedure unassigns an attribute set from a column storing expressions.

Syntax

```
DBMS_EXPFIL.UNASSIGN_ATTRIBUTE_SET (
   expr_tab   IN   VARCHAR2,
   expr_col   IN   VARCHAR2);
```

Parameters

Table 65-19 UNASSIGN\_ATTRIBUTE\_SET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `expr_tab` | Name of table storing the expression set |
| `expr_col` | Name of column in the table that stores the expressions |

Usage Notes

- A column of an expression data type can be converted back to a `VARCHAR2` type by unassigning the attribute set. You can unassign an attribute set from a column storing expressions if an Expression Filter index is not defined on the column.
- See ASSIGN\_ATTRIBUTE\_SET Procedure for information about assigning attribute sets.
- Related views: [`USER_EXPFIL_EXPRESSION_SETS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN058) and [`USER_EXPFIL_INDEXES`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN061).

Examples

The following command unassigns the attribute set previously assigned to the `interest` column of the `consumer` table. (See the section on bulk loading of expression data in [Oracle Database Rules Manager and Expression Filter Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_utilities.htm#EXPRN040).)

```
BEGIN
  DBMS_EXPFIL.UNASSIGN_ATTRIBUTE_SET (expr_tab => 'consumer',
                                      expr_col => 'interest');
END;
/
```

---

### VALIDATE\_EXPRESSIONS Procedure

This procedure validates all the expressions in a set.

Syntax

```
DBMS_EXPFIL.VALIDATE_EXPRESSIONS (
   expr_tab      IN  VARCHAR2,
   expr_col      IN  VARCHAR2,
   exception_tab IN  VARCHAR2 DEFAULT NULL);
```

Parameters

Table 65-20 VALIDATE\_EXPRESSIONS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `expr_tab` | Name of table storing the expression set |
| `expr_col` | Name of column in the table that stores the expressions |
| `exception_tab` | Name of the exception table. This table is created using the `BUILD_EXCEPTIONS_TABLE` procedure. |

Usage Notes

- The expressions stored in a table may have references to schema objects like user-defined functions and tables. When these schema objects are dropped or modified, the expressions could become invalid and the subsequent evaluation (query with `EVALUATE` operator) could fail.
- By default, the expression validation procedure fails on the first expression that is invalid. Optionally, the caller can pass an exception table to store references to all the invalid expressions. In addition to validating expressions in the set, this procedure validates the parameters (stored and indexed attributes) of the associated index and the approved list of user-defined functions. Any errors in the index parameters or the user-defined function list are immediately reported to the caller.
- See the section on evaluation semantics in [Oracle Database Rules Manager and Expression Filter Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_expconcepts.htm#EXPRN015) and BUILD\_EXCEPTIONS\_TABLE Procedure for more information.
- Related views: [`USER_EXPFIL_EXPRESSION_SETS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN058), [`USER_EXPFIL_ASET_FUNCTIONS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN054), and [`USER_EXPFIL_PREDTAB_ATTRIBUTES`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN062).

Examples

The following command validates the expressions stored in the `interest` column of the `consumer` table.

```
BEGIN
  DBMS_EXPFIL.VALIDATE_EXPRESSIONS (expr_tab => 'consumer',
                                    expr_col => 'interest');
END;
/
```

---

### XPINDEX\_PARAMETERS Procedure

This procedure is used in conjunction with the `INDEX_PARAMETERS` procedure to fine-tune the XPath-specific index parameters for each expression set.

Syntax

```
DBMS_EXPFIL.XPINDEX_PARAMETERS (
   expr_tab   IN   VARCHAR2,
   expr_col   IN   VARCHAR2,
   xmlt_attr  IN   VARCHAR2,
   xptag_list IN   EXF$XPATH_TAGS,
   operation  IN   VARCHAR2 DEFAULT 'ADD');
```

Parameters

Table 65-21 XPINDEX\_PARAMETERS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `exp_tab` | Name of table storing the expression set |
| `expr_col` | Name of column in the table that stores the expressions |
| `xmlt_attr` | Name of the attribute with the `XMLType` datatype |
| `xptag_list` | An instance of `EXF$XPATH_TAGS` type with a partial list of XML elements and attributes |
| `operation` | Operation to be performed on the list of index parameters. Default value: `ADD`. Valid values: `ADD` and `DROP`. |

Usage Notes

- When an attribute set is shared by multiple expression sets, the `INDEX_PARAMETERS` procedure can be used to tune the simple (non-XPath) index parameters for each expression set. The `XPINDEX_PARAMETERS` procedure is used in conjunction with the `INDEX_PARAMETERS` procedure to fine-tune the XPath-specific index parameters for each expression set.
- See also INDEX\_PARAMETERS Procedure and the section on index tuning for XPath predicates in [Oracle Database Rules Manager and Expression Filter Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_xpathpredicates.htm#EXPRN033) for more information.
- Related views: [`USER_EXPFIL_ATTRIBUTES`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN055), [`USER_EXPFIL_DEF_INDEX_PARAMS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN057), and [`USER_EXPFIL_INDEX_PARAMS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN060).
	Note:
	The values assigned to the `tag_name` argument of `exf$xpath_tag` type are case-sensitive.

Examples

The following command synchronizes the index parameters of the expression set (XPath and non-XPath) with the defaults associated with the corresponding attribute set:

```
BEGIN
  DBMS_EXPFIL.INDEX_PARAMETERS(expr_tab  => 'consumer',
                               expr_col  => 'interest',
                               attr_list => null, 
                               operation => 'DEFAULT');
END;
/
```

The following command adds an XPath-specific index parameter to the expression set:

```
BEGIN
  DBMS_EXPFIL.XPINDEX_PARAMETERS(expr_tab   => 'consumer',
                                 expr_col   => 'interest',
                                 xmlt_attr  => 'details',
                                 xptag_list =>
                                  exf$xpath_tags(
                                   exf$xpath_tag(tag_name    => 'GPS',
                                                 tag_indexed => 'TRUE',
                                                 tag_type    => NULL)),
                                 operation  => 'ADD');
END;
/
```