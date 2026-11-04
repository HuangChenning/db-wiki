---
title: Expression Filter Types
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/t_expfilobj.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 248 Expression Filter Types

Note:

This functionality is deprecated with Oracle Database Release 11.2 and obsoleted with Release 12.1. For details regarding obsolescence, seeMy Oracle Support Note [ID 1244535.1](https://support.oracle.com/CSP/ui/flash.html#tab=KBHome%28page=KBHome&id=%28%29%29,%28page=KBNavigator&id=%28from=BOOKMARK&bmDocType=DESUPPORT&bmDocID=1244535.1&bmDocDsrc=KB&viewingMode=1143&bmDocTitle=Obsolescence%20Notice:%20Rules%20Manager%20Feature%20of%20Oracle%20Database%29%29)

The Expression Filter feature provides a set of predefined types and public synonyms for these types. Most of these types are used for configuring index parameters with the Expression Filter procedural APIs. The `EXF$TABLE_ALIAS` type is used to support expressions defined on one or more database tables.

See Also:

[Oracle Database Rules Manager and Expression Filter Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/toc.htm) for more information.

This chapter contains the following topics:

- Using Expression Filter Types
- Summary of Expression Filter Types

---

## Using Expression Filter Types

This section contains topics that relate to using the Expression Filter Types.

- Security Model

---

### Security Model

The Oracle Database installation runs the `catexf.sql` script to load the `DBMS_EXPFIL` package and create the required Expression Filter schema objects in the `EXFSYS` schema.

---

## Summary of Expression Filter Types

Table 248-1 describes the Expression Filter object types.

All the values and names passed to the types defined in this chapter are not case sensitive. To preserve the case, enclose the values with double quotation marks.

Table 248-1 Expression Filter Object Types

| Object Type Name | Description |
| --- | --- |
| EXF$ATTRIBUTE | Specifies the stored and indexed attributes for the Expression Filter indexes |
| EXF$ATTRIBUTE\_LIST | Specifies a list of stored and indexed attributes when configuring index parameters |
| EXF$INDEXOPER | Specifies a list of common operators in predicates with a stored or an indexed attribute |
| EXF$TABLE\_ALIAS | Indicates a special form of elementary attribute used to manage expressions defined on one or more database tables |
| EXF$TEXT | Associates preferences to a text attribute in an attribute set or an event structure |
| EXF$XPATH\_TAG | Configures an XML element or an XML attribute for indexing a set of XPath predicates |
| EXF$XPATH\_TAGS | Specifies a list of XML tags when configuring the Expression Filter index parameters |

---

### EXF$ATTRIBUTE

The `EXF$ATTRIBUTE` type is used to handle stored and indexed attributes for the Expression Filter indexes.

Syntax

```
CREATE or REPLACE TYPE EXF$ATTRIBUTE AS OBJECT attr_name    VARCHAR2(350),
                                               attr_oper    EXF$INDEXOPER,
                                               attr_indexed VARCHAR2(5);
```

Attributes

Table 248-2 EXF$ATTRIBUTE Attributes

| Attribute | Description |
| --- | --- |
| `attr_name` | The arithmetic expression that constitutes the stored or indexed attribute |
| `attr_oper` | The list of common operators in the predicates with the attribute. Default value: `EXF$INDEXOPER('all')` |
| `attr_indexed` | `TRUE` if the attribute is indexed, else `FALSE.` Default value: `FALSE`. |

Usage Notes

- The `EXF$ATTRIBUTE` type is used to specify the stored and indexed attributes for an Expression Filter index using the DBMS\_EXPFIL.DEFAULT\_INDEX\_ `PARAMETERS` procedure. When values for `attr_oper` and `attr_indexed` fields are omitted during `EXF$ATTRIBUTE` instantiation, it is considered a stored attribute with a default value for common operators (`EXF$INDEXOPER('all')`).

Examples

A stored attribute with no preference on the list of common operators is represented as follows:

```
exf$attribute (attr_name => 'HorsePower(Model, Year)')
```

An indexed attribute is represented as follows:

```
exf$attribute (attr_name => 'HorsePower(Model, Year)', 
               attr_indexed => 'TRUE')
```

An indexed attribute with a list of common operators is represented as follows:

```
exf$attribute (attr_name => 'HorsePower(Model, Year)', 
               attr_oper => exf$indexoper('=','<','>','>=','<='), 
               attr_indexed => 'TRUE')
```

---

### EXF$ATTRIBUTE\_LIST

The `EXF$ATTRIBUTE_LIST` type specifies a list of stored and indexed attributes while configuring the index parameters.

Syntax

```
CREATE or REPLACE TYPE EXF$ATTRIBUTE_LIST as VARRAY(490) of exf$attribute;
```

Attributes

None.

Usage Notes

- Also see the [DEFAULT\_INDEX\_PARAMETERS Procedure](d_expfilref.md) for more information

Examples

A list of stored and indexed attributes can be represented as follows:

```
exf$attribute_list (
       exf$attribute (attr_name => 'Model',            
                      attr_oper => exf$indexoper('='),
                      attr_indexed => 'TRUE'),         
       exf$attribute (attr_name => 'Price', 
                      attr_oper => exf$indexoper('all'), 
                      attr_indexed => 'TRUE'), 
       exf$attribute (attr_name => 'HorsePower(Model, Year)', 
                      attr_oper => exf$indexoper('=','<','>','>=','<='), 
                      attr_indexed => 'FALSE')         
    )
```

---

### EXF$INDEXOPER

The `EXF$INDEXOPER` type specifies the list of common operators in predicates with a stored or an indexed attribute.

Syntax

```
CREATE or REPLACE TYPE EXFSYS.EXF$INDEXOPER as VARRAY(20) of VARCHAR2(15);
```

The values for the `EXF$INDEXOPER` array are expected to be from the list in the following table:

| Value | Predicate Description |
| --- | --- |
| `=` | Equality predicates |
| `>` | Greater than predicates |
| `<` | Less than predicates |
| `>=` | Greater than or equal to predicates |
| `<=` | Less than or equal to predicates |
| `!=` or `<>` or `^=` | Not equal to predicates |
| `IS NULL` | `IS NULL` predicates |
| `IS NOT NULL` | `IS NOT NULL` predicates |
| `ALL` | All the operators listed in this table starting with the equality predicate through the `IS NOT NULL` predicate |
| `NVL` | Predicates with `NVL` (equality) operator |
| `LIKE` | Predicates with `LIKE` operator |
| `BETWEEN` | `BETWEEN` predicates |

Attributes

None.

Usage Notes

- A value of `ALL` for one of the `EXF$INDEXOPER` items implies that all the simple operators (`=`,`>`,`<`,`>=`,`<=`,`!=`, `IS NULL`, `IS NOT NULL`) are common in the predicates with an attribute. This value can be used along with one or more complex operators (`NVL`, `LIKE` and `BETWEEN`).
- A predicate with a `BETWEEN` operator is treated as two predicates with binary operators, one with ' `>=` ' operator and another with ' `<=` ' operator. By default, only one of these operators is indexed, and the other operator is evaluated by value substitution. However, if predicates with the `BETWEEN` operator are common for an attribute (stored or indexed), both the binary operators resulting from the `BETWEEN` operator can be indexed by specifying `BETWEEN` in the `EXF$INDEXOPER VARRAY`. However, because this uses additional space in the predicate table, this operator should be used only when majority of predicates with an attribute use the `BETWEEN` operator.
- When the `LIKE` operator is chosen as one of the common operators for an attribute, `LIKE` predicates on that attributes are indexed. Indexing a `LIKE` operator is beneficial only if the `VARCHAR2` constant on the right-hand side of the predicate does not lead with a wild-card character. For example, indexing a `LIKE` operator will filter the following predicates efficiently:
	```
	company LIKE 'General%'
	company LIKE 'Proctor%'
	```
	But, the following predicates are evaluated as sparse predicates in the last stage:
	```
	company LIKE '%Electric'
	company LIKE "%Gamble'
	```

Examples

An attribute with a list of common operators is represented as follows:

```
exf$attribute (attr_name => 'HorsePower(Model, Year)', 
               attr_oper => exf$indexoper('=','<','>','>=','<=', 'between'), 
               attr_indexed => 'TRUE')
```

---

### EXF$TABLE\_ALIAS

A `EXF$TABLE_ALIAS` type is a special form of elementary attribute that can be included in the attribute set. These attributes manage expressions defined on one or more database tables.

Syntax

```
CREATE or REPLACE TYPE EXF$TABLE_ALIAS AS OBJECT table_name VARCHAR2(70);
```

Attributes

Table 248-3 EXF$TABLE\_ALIAS Attribute

| Attribute | Description |
| --- | --- |
| `table_name` | Name of the table with a possible schema extension |

Usage Notes

- The concept of a table alias attribute is captured in the Expression Filter dictionary and the corresponding attribute in the attribute set's object type is created with a `VARCHAR2` data type. (Also see [Oracle Database Rules Manager and Expression Filter Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_app_a.htm#EXPRN111) and [ADD\_ELEMENTARY\_ATTRIBUTE Procedures](d_expfilref.md).)

Examples

For a set of expressions defined on database tables, the corresponding table alias attributes are configured as follows:

```
BEGIN
  DBMS_EXPFIL.ADD_ELEMENTARY_ATTRIBUTE (
                               attr_set  => 'HRAttrSet',
                               attr_name => 'EMP',
                               tab_alias => exf$table_alias('SCOTT.EMP'));
  DBMS_EXPFIL.ADD_ELEMENTARY_ATTRIBUTE (
                               attr_set  => 'HRAttrSet',
                               attr_name => 'DEPT',
                               tab_alias => exf$table_alias('DEPT'));
END;
/
```

The Expression column using the previous attribute set can store expressions of form `EMP.JOB = 'Clerk' and EMP.NAME = 'Joe'`, where `JOB` and `NAME` are the names of the columns in the `SCOTT.EMP` table.

---

### EXF$TEXT

A `EXF$TEXT` type associates preferences to a text attribute in an attribute set or an event structure.

Syntax

```
CREATE or REPLACE TYPE EXFSYS.EXF$TEXT AS OBJECT(preferences VARCHAR2(1000));
```

Attributes

Table 248-4 EXF$TEXT Attribute

| Attribute | Description |
| --- | --- |
| `preferences` | Text preference specification, such as LEXER, CLASSIFIER, and WORDLIST |

Usage Notes

- The `EXF$TEXT` attribute is used to specify the preferences for a text attribute at the time of creation. The preferences specified through the instance of `EXF$TEXT` type are used in creation of the `CTXRULE` index for the text predicates. The syntax for the text preference specification is similar to the `PARAMETERS` clause specified for a `CTXRULE` Indextype. \[See `CREATE INDEX` syntax for `CTXRULE` Indextype in [Oracle Text Reference](https://docs.oracle.com/cd/E11882_01/text.112/e24436/toc.htm), Release 10g Release 2.\]

Examples

A text predicate with a `LEXER` and `WORDLIST` preferences can be created using the following instance of `EXF$TEXT` object as follows:

```
EXF$TEXT ('LEXER insrpt_lexer WORDLIST insrpt_wordlist');
```

---

### EXF$XPATH\_TAG

The `EXF$XPATH_TAG` type configures an XML element or an XML attribute for indexing a set of XPath predicates.

Syntax

```
CREATE or REPLACE TYPE EXF$XPATH_TAG AS OBJECT tag_name    VARCHAR2(350),
                                               tag_indexed VARCHAR2(5),
                                               tag_type    VARCHAR2(30);
```

Attributes

Table 248-5 EXF$XPATH\_TAG Attributes

| Attribute | Description |
| --- | --- |
| `tag_name` | Name of the XML element or attribute. The name for an XML attribute is formatted as: `<ElementName>@<AttributeName>`. Optionally, the element name can be prefixed with its namespace URL as in \<Namespace URL>:\<ElementName>@\<AttributeName>. |
| `tag_indexed` | `TRUE` if XML tag is indexed; otherwise `FALSE`.  Default:  `TRUE` if the tag is a positional filter.  `FALSE` if the tag is a value filter. |
| `tag_type` | Datatype for the value in the case of value filter. `NULL` for positional filters. |

Usage Notes

- `EXF$XPATH_TAG` type configures an XML element or an attribute as a positional or a value filter for an Expression Filter index (see the section on index tuning for XPath predicates in [Oracle Database Rules Manager and Expression Filter Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_xpathpredicates.htm#EXPRN033)). An instance of the `EXF$XPATH_TAG` type with `NULL` value for `tag_type` configures the XML tag as a positional filter. In the current release, the only other possible values for the `tag_type` attribute are strings (`CHAR` or `VARCHAR`) and such tags are configured as value filters. By default, all positional filters are indexed and the value filters are not indexed. This behavior can be overridden by setting a `TRUE` or `FALSE` value for the `tag_indexed` attribute accordingly.

Examples

An XML element can be configured as a positional filter and be indexed using the following instance of the `EXF$XPATH_TAG` type.

```
exf$xpath_tag(tag_name    => 'stereo',       --- XML element
              tag_indexed => 'TRUE',         --- indexed predicate group
              tag_type    => null)           --- positional filter
```

An XML attribute can be configured as a value filter and be indexed using the following type instance.

```
exf$xpath_tag(tag_name    => 'stereo@make',  --- XML attribute
              tag_indexed => 'TRUE',         --- indexed predicate group
              tag_type    => 'VARCHAR(15)')  --- value filter
```

The following commands configure the two filters shown previously using the namespace URL for the corresponding elements.

```
exf$xpath_tag(tag_name => 'http://www.auto.com/car.xsd:stereo', 
              tag_indexed => 'TRUE', --- indexed predicate group
              tag_type => null)      --- positional filter

exf$xpath_tag(tag_name => 'http://www.auto.com/car.xsd:stereo@make'
              tag_indexed => 'TRUE',     --- indexed predicate group
              tag_type => 'VARCHAR(15)') --- value filter
```

---

### EXF$XPATH\_TAGS

The `EXF$XPATH_TAGS` type specifies a list of XML tags while configuring the Expression Filter index parameters.

Syntax

```
CREATE or REPLACE TYPE EXF$XPATH_TAGS as VARRAY(490) of EXF$XPATH_TAG;
```

Attributes

None.

Usage Notes

- `EXF$XPATH_TAGS` type specifies a list of XML tags while configuring the Expression Filter index parameters. (See [DEFAULT\_INDEX\_PARAMETERS Procedure](d_expfilref.md).)

Examples

A list of XML tags configured as positional and value filters can be represented as follows:

```
exf$xpath_tags(
           exf$xpath_tag(tag_name    => 'stereo@make',  --- XML attribute
                         tag_indexed => 'TRUE',
                         tag_type    => 'VARCHAR(15)'), --- value filter
           exf$xpath_tag(tag_name    => 'stereo',       --- XML element
                         tag_indexed => 'FALSE',
                         tag_type    => null),          --- positional filter
           exf$xpath_tag(tag_name    => 'memory',       --- XML element
                         tag_indexed => 'TRUE',
                         tag_type    => 'VARCHAR(10)')  --- value filter
          )
```