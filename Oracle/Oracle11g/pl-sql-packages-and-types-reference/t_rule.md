---
title: Rule TYPEs
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/t_rule.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 257 Rule TYPEs

This chapter describes the types used with rules, rule sets, and evaluation contexts.

This chapter contains the following topics:

- Using Rule Types
- Summary of Rule Types

---

## Using Rule Types

This section contains topics that relate to using the types used with rules, rule sets, and evaluation contexts.

---

### Overview

This types in this chapter are used in rules and enable clients to evaluate rules with the rules engine.

See Also:

- [Chapter 127, "DBMS\_RULE"](d_rule.md)
- [Chapter 128, "DBMS\_RULE\_ADM"](d_rule_a.md)
- [Oracle Streams Extended Examples](https://docs.oracle.com/cd/E11882_01/server.112/e12862/rulesdemo.htm#STREX017) for examples that use rule types

---

### Security Model

`PUBLIC` is granted `EXECUTE` privilege on the types described in this chapter.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authorization.htm#DBSEG40048) for more information about user group `PUBLIC`

---

## Summary of Rule Types

Table 257-1 Rule Types

| Type | Description |
| --- | --- |
| RE$ATTRIBUTE\_VALUE Type | Specifies the value of a variable attribute |
| RE$ATTRIBUTE\_VALUE\_LIST Type | Identifies a list of attribute values |
| RE$COLUMN\_VALUE Type | Specifies the value of a table column |
| RE$COLUMN\_VALUE\_LIST Type | Identifies a list of column values |
| RE$NAME\_ARRAY Type | Identifies a list of names |
| RE$NAME\_ARRAY Type | Identifies a list of name-value pairs |
| RE$NV\_LIST Type | Identifies an object containing a list of name-value pairs and methods that operate on this list. This object type is used to represent the event context and the action context for a rule |
| RE$NV\_NODE Type | Identifies a name-value pair |
| RE$RULE\_HIT Type | Specifies a rule found because of evaluation |
| RE$RULE\_HIT\_LIST Type | Identifies a list of rules found because of evaluation |
| RE$TABLE\_ALIAS Type | Provides the table corresponding to an alias used in a rule evaluation context |
| RE$TABLE\_ALIAS\_LIST Type | Identifies a list of table aliases used in a rule evaluation context |
| RE$TABLE\_VALUE Type | Specifies the value of a table row using a `ROWID` |
| RE$TABLE\_VALUE\_LIST Type | Identifies a list of table values |
| RE$VARIABLE\_TYPE Type | Provides the type of a variable used in a rule evaluation context |
| RE$VARIABLE\_TYPE\_LIST Type | Identifies a list of variables and their types used in a rule evaluation context |
| RE$VARIABLE\_VALUE Type | Specifies the value of a variable |
| RE$VARIABLE\_VALUE\_LIST Type | Identifies a list of variable values |

Rule types are used with the following Oracle-supplied PL/SQL packages:

- `DBMS_RULE`
- `DBMS_RULE_ADM`

You can use the `DBMS_RULE_ADM` package to create and administer rules, rule sets, and evaluation contexts, and you can use the `DBMS_RULE` package to evaluate rules.

When you use Oracle Streams, rules determine which changes are captured by a capture process, which messages are propagated by a propagation, which messages are applied by an apply process, and which messages are dequeued by a messaging client. The following Oracle Streams packages use rules:

- `DBMS_APPLY_ADM`
- `DBMS_CAPTURE_ADM`
- `DBMS_PROPAGATION_ADM`
- `DBMS_STREAMS`
- `DBMS_STREAMS_ADM`
- `DBMS_STREAMS_AUTH`
	See Also:
	[Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_adrules.htm#STRMS005)

---

### RE$ATTRIBUTE\_VALUE Type

Specifies the value of a variable attribute.

Note:

Enclose the variable name and attribute name in double quotation marks (") if the name contains special characters.

Syntax

```
TYPE SYS.RE$ATTRIBUTE_VALUE (
   variable_name    VARCHAR2(32), 
   attribute_name   VARCHAR2(4000),
   attribute_value  ANYDATA);
```

Attributes

Table 257-2 RE$ATTRIBUTE\_VALUE Attributes

| Attribute | Description |
| --- | --- |
| `variable_name` | Specifies the variable used in a rule |
| `attribute_name` | Specifies the attribute name. The attribute name can be a multi-component name, such as `a1.b2.c3`. |
| `attribute_value` | Specifies the attribute value |

---

### RE$ATTRIBUTE\_VALUE\_LIST Type

Identifies a list of attribute values.

Syntax

```
TYPE SYS.RE$ATTRIBUTE_VALUE_LIST AS VARRAY(1024) OF SYS.RE$ATTRIBUTE_VALUE;
```

---

### RE$COLUMN\_VALUE Type

Specifies the value of a table column.

Note:

Enclose the column name in double quotation marks (") if the name contains special characters.

Syntax

```
TYPE SYS.RE$COLUMN_VALUE (
   table_alias   VARCHAR2(32), 
   column_name   VARCHAR2(4000),
   column_value  ANYDATA);
```

Attributes

Table 257-3 RE$COLUMN\_VALUE Attributes

| Attribute | Description |
| --- | --- |
| `table_alias` | Specifies the alias used for the table in a rule |
| `column_name` | Specifies the column name |
| `column_value` | Specifies the column value |

---

### RE$COLUMN\_VALUE\_LIST Type

Identifies a list of column values.

Syntax

```
TYPE SYS.RE$COLUMN_VALUE_LIST AS VARRAY(1024) OF SYS.RE$COLUMN_VALUE;
```

---

### RE$NAME\_ARRAY Type

Identifies a list of names.

Syntax

```
TYPE SYS.RE$NAME_ARRAY AS VARRAY(1024) OF VARCHAR2(30);
```

---

### RE$NV\_ARRAY Type

Identifies a list of name-value pairs.

#### Syntax

```
TYPE SYS.RE$NV_ARRAY AS VARRAY(1024) OF SYS.RE$NV_NODE;
```

---

### RE$NV\_LIST Type

Identifies an object containing a list of name-value pairs and methods that operate on this list. This object type is used to represent the event context for rule set evaluation and the action context for a rule.

Syntax

```
TYPE SYS.RE$NV_LIST AS OBJECT( 
   actx_list  SYS.RE$NV_ARRAY);
```

Attributes

Table 257-4 RE$NV\_LIST Attributes

| Attribute | Description |
| --- | --- |
| `actx_list` | The list of name-value pairs |

ADD\_PAIR Member Procedure

Adds a name-value pair to the list of name-value pairs.

Note:

Enclose the name in double quotation marks (") if the name contains special characters.

Syntax

```
MEMBER PROCEDURE ADD_PAIR(
   name   IN  VARCHAR2, 
   value  IN  ANYDATA);
```

Parameters

Table 257-5 ADD\_PAIR Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | The name in the name-value pair being added to the list. If the name exists in the list, then this procedure raises an error. |
| `value` | The value in the name-value pair being added to the list |

GET\_ALL\_NAMES Member Function

Returns a list of all the names in the name-value pair list.

Syntax

```
MEMBER FUNCTION GET_ALL_NAMES()
RETURN SYS.RE$NAME_ARRAY;
```

GET\_VALUE Member Function

Returns the value for the specified name in a name-value pair list.

Note:

Enclose the name in double quotation marks (") if the name contains special characters.

Syntax

```
MEMBER FUNCTION GET_VALUE(
   name  IN  VARCHAR2) 
RETURN ANYDATA;
```

Parameters

Table 257-6 GET\_VALUE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | The name whose value to return |

REMOVE\_PAIR Member Procedure

Removes the name-value pair with the specified name from the name-value pair list.

Note:

Enclose the name in double quotation marks (") if the name contains special characters.

Syntax

```
MEMBER PROCEDURE REMOVE_PAIR(
   name  IN  VARCHAR2);
```

Parameters

Table 257-7 REMOVE\_PAIR Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | The name of the pair to remove |

---

### RE$NV\_NODE Type

Identifies a name-value pair.

Note:

Enclose the name in double quotation marks (") if the name contains special characters.

Syntax

```
TYPE SYS.RE$NV_NODE (
   nvn_name   VARCHAR2(30), 
   nvn_value  ANYDATA);
```

Attributes

Table 257-8 RE$NV\_NODE Attributes

| Attribute | Description |
| --- | --- |
| `nvn_name` | Specifies the name in the name-value pair |
| `nvn_value` | Specifies the value in the name-value pair |

---

### RE$RULE\_HIT Type

Specifies a rule found because of an evaluation.

See Also:

- [CREATE\_RULE Procedure](d_rule_a.md)
- [ALTER\_RULE Procedure](d_rule_a.md)

Syntax

```
TYPE SYS.RE$RULE_HIT (
   rule_name            VARCHAR2(65),
   rule_action_context  RE$NV_LIST);
```

Attributes

Table 257-9 RE$RULE\_HIT Attributes

| Attribute | Description |
| --- | --- |
| `rule_name` | The rule name in the form `schema_name.rule_name`. For example, a rule named `employee_rule` in the `hr` schema is returned in the form " `hr"."employee_rule"`. |
| `rule_action_context` | The rule action context as specified in the `CREATE_RULE` or `ALTER_RULE` procedure of the `DBMS_RULE_ADM` package |

---

### RE$RULE\_HIT\_LIST Type

Identifies a list of rules found because of an evaluation.

Syntax

```
TYPE SYS.RE$RULE_HIT_LIST AS VARRAY(1024) OF SYS.RE$RULE_HIT;
```

---

### RE$TABLE\_ALIAS Type

Provides the table corresponding to an alias used in a rule evaluation context. A specified table name must satisfy the schema object naming rules.

Note:

Enclose the table name in double quotation marks (") if the name contains special characters.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/sql_elements.htm#SQLRF002) for information about schema object naming rules

Syntax

```
TYPE SYS.RE$TABLE_ALIAS IS OBJECT(
   table_alias  VARCHAR2(32),
   table_name   VARCHAR2(194));
```

Attributes

Table 257-10 RE$TABLE\_ALIAS Attributes

| Attribute | Description |
| --- | --- |
| `table_alias` | The alias used for the table in a rule |
| `table_name` | The table name referred to by the alias. A synonym can be specified. The table name is resolved in the evaluation context schema.  The format is one of the following:  ``` schema_name.table_name  table_name ```  For example, if the `schema_name` is `hr` and the `table_name` is `employees`, then enter the following:  ``` hr.employees ``` |

---

### RE$TABLE\_ALIAS\_LIST Type

Identifies a list of table aliases used in a rule evaluation context.

Syntax

```
TYPE SYS.RE$TABLE_ALIAS_LIST AS VARRAY(1024) OF SYS.RE$TABLE_ALIAS;
```

---

### RE$TABLE\_VALUE Type

Specifies the value of a table row using a `ROWID`.

Syntax

```
TYPE SYS.RE$TABLE_VALUE(
   table_alias  VARCHAR2(32), 
   table_rowid  VARCHAR2(18));
```

Attributes

Table 257-11 RE$TABLE\_VALUE Attributes

| Attribute | Description |
| --- | --- |
| `table_alias` | Specifies the alias used for the table in a rule |
| `table_rowid` | Specifies the rowid for the table row |

---

### RE$TABLE\_VALUE\_LIST Type

Identifies a list of table values.

Note:

Each table alias in the list in the list must be unique.

Syntax

```
TYPE SYS.RE$TABLE_VALUE_LIST AS VARRAY(1024) OF SYS.RE$TABLE_VALUE;
```

---

### RE$VARIABLE\_TYPE Type

Provides the type of a variable used in a rule evaluation context. A specified variable name must satisfy the schema object naming rules.

Note:

Enclose the variable name in double quotation marks (") if the name contains special characters.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/sql_elements.htm#SQLRF002) for information about schema object naming rules

Syntax

```
TYPE SYS.RE$VARIABLE_TYPE (
   variable_name             VARCHAR2(32),
   variable_type             VARCHAR2(4000),
   variable_value_function   VARCHAR2(228),
   variable_method_function  VARCHAR2(228));
```

Attributes

Table 257-12 RE$VARIABLE\_TYPE Attributes

| Attribute | Description |
| --- | --- |
| `variable_name` | The variable name used in a rule |
| `variable_type` | The type that is resolved in the evaluation context schema. Any valid Oracle built-in data type, user-defined type, or Oracle-supplied type can be specified. See the [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/sql_elements.htm#SQLRF002) for more information about these types. |
| `variable_value_function` | A value function that can be specified for implicit variables. A synonym can be specified. The function name is resolved in the evaluation context schema. It is executed on behalf of the owner of a rule set using the evaluation context or containing a rule that uses the evaluation context.  See the "Usage Notes" for more information. |
| `variable_method_function` | Specifies a value function, which can return the result of a method invocation. Specifying such a function can speed up evaluation, if there are many simple rules that invoke the method on the variable. The function can be a synonym or a remote function.  The function name is resolved in the evaluation context schema. It is executed on behalf of the owner of a rule set using the evaluation context or containing a rule that uses the evaluation context.  See the "Usage Notes" for more information. |

Usage Notes

The functions for both the for the `variable_value_function` parameter and `variable_method_function` parameter have the following format:

```
schema_name.package_name.function_name@dblink
```

Any of the following parts of the format can be omitted: `schema_name`, `package_name`, and `@dblink`.

For example, if the `schema_name` is `hr`, the `package_name` is `var_pac`, the `function_name` is `func_value`, and the `dblink` is `dbs1.net`, then enter the following:

```
hr.var_pac.func_value@dbs1.net
```

The following sections describe the signature of the functions.

Signature for variable\_value\_function

The function must have the following signature:

```
FUNCTION variable_value_function_name(
  evaluation_context_schema  IN VARCHAR2,       
  evaluation_context_name    IN VARCHAR2,
  variable_name              IN VARCHAR2,
  event_context              IN SYS.RE$NV_LIST )
RETURN SYS.RE$VARIABLE_VALUE;
```

Signature for variable\_method\_function

This function must have the following signature:

```
FUNCTION variable_method_function_name(    
  evaluation_context_schema  IN VARCHAR2, 
  evaluation_context_name    IN VARCHAR2, 
  variable_value             IN SYS.RE$VARIABLE_VALUE, 
  method_name                IN VARCHAR2, 
  event_context              IN SYS.RE$NV_LIST)
RETURN SYS.RE$ATTRIBUTE_VALUE;
```

---

### RE$VARIABLE\_TYPE\_LIST Type

Identifies a list of variables and their types used in a rule evaluation context.

Syntax

```
TYPE SYS.RE$VARIABLE_TYPE_LIST AS VARRAY(1024) OF SYS.RE$VARIABLE_TYPE;
```

---

### RE$VARIABLE\_VALUE Type

Specifies the value of a variable.

Note:

Enclose the variable name in double quotation marks (") if the name contains special characters.

Syntax

```
TYPE SYS.RE$VARIABLE_VALUE (
   variable_name  VARCHAR2(32), 
   variable_data  ANYDATA);
```

Attributes

Table 257-13 RE$VARIABLE\_VALUE Attributes

| Attribute | Description |
| --- | --- |
| `variable_name` | Specifies the variable name used in a rule |
| `variable_data` | Specifies the data for the variable value |

---

### RE$VARIABLE\_VALUE\_LIST Type

Identifies a list of variable values.

Syntax

```
TYPE SYS.RE$VARIABLE_VALUE_LIST AS VARRAY(1024) OF SYS.RE$VARIABLE_VALUE;
```