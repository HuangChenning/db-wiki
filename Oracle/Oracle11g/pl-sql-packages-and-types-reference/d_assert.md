---
title: DBMS_ASSERT
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_assert.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 26 DBMS\_ASSERT

The DBMS\_ASSERT package provides an interface to validate properties of the input value.

See Also:

Oracle Database PL/SQL Language Reference for more information about ["Avoiding SQL Injection in PL/SQL"](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/dynamic.htm#LNPLS01109)

This chapter contains the following topics:

- Using DBMS\_ASSERT
	- Operational Notes
- Summary of DBMS\_ASSERT Subprograms

---

## Using DBMS\_ASSERT

- Operational Notes

---

### Operational Notes

If the condition which determines the property asserted in a function is not met then a value error is raised. Otherwise the input value is returned through the return value. Most functions return the value unchanged, however, several functions modify the value.

---

## Summary of DBMS\_ASSERT Subprograms

Table 26-1 DBMS\_APPLICATION\_INFO Package Subprograms

| Subprogram | Description |
| --- | --- |
| ENQUOTE\_LITERAL Function | Enquotes a string literal |
| ENQUOTE\_NAME Function | Encloses a name in double quotes |
| NOOP Functions | Returns the value without any checking |
| QUALIFIED\_SQL\_NAME Function | Verifies that the input string is a qualified SQL name |
| SCHEMA\_NAME Function | Verifies that the input string is an existing schema name |
| SIMPLE\_SQL\_NAME Function | Verifies that the input string is a simple SQL name |
| SQL\_OBJECT\_NAME Function | Verifies that the input parameter string is a qualified SQL identifier of an existing SQL object |

---

### ENQUOTE\_LITERAL Function

This function adds leading and trailing single quotes to a string literal.

Syntax

```
DBMS_ASSERT.ENQUOTE_LITERAL (
   str            VARCHAR2) 
RETURN VARCHAR2;
```

Parameters

Table 26-2 ENQUOTE\_LITERAL Function Parameters

| Parameter | Description |
| --- | --- |
| `str` | String to enquote |

Usage Notes

- Verify that all single quotes except leading and trailing characters are paired with adjacent single quotes.
- No additional quotes are added if the name was already in quotes.

---

### ENQUOTE\_NAME Function

This function encloses a name in double quotes.

Syntax

```
DBMS_ASSERT.ENQUOTE_NAME (
   str            VARCHAR2, 
   capitalize     BOOLEAN DEFAULT TRUE)
RETURN VARCHAR2;
```

Parameters

Table 26-3 ENQUOTE\_NAME Function Parameters

| Parameter | Description |
| --- | --- |
| `str` | String to enquote |
| `capitalize` | If `TRUE` or defaulted, alphabetic characters of `str` which was not in quotes are translated to upper case |

Usage Notes

- No additional quotes are added if the name was already in quotes.
- Verify that all other double quotes in the string are adjacent pairs of double quotes.

---

### NOOP Functions

This function returns the value without any checking.

Syntax

```
DBMS_ASSERT.NOOP (
   str      VARCHAR2 CHARACTER SET ANY_CS)
 RETURN     VARCHAR2 CHARACTER SET str%CHARSET;
```
```
DBMS_ASSERT.NOOP (
   str      CLOB CHARACTER SET ANY_CS)
 RETURN     CLOB CHARACTER SET str%CHARSET;
```

Parameters

Table 26-4 NOOP Function Parameters

| Parameter | Description |
| --- | --- |
| `str` | Input value |

---

### QUALIFIED\_SQL\_NAME Function

This function verifies that the input string is a qualified SQL name.

Syntax

```
DBMS_ASSERT.QUALIFIED_SQL_NAME (
   str      VARCHAR2 CHARACTER SET ANY_CS)
 RETURN     VARCHAR2 CHARACTER SET str%CHARSET;
```

Parameters

Table 26-5 QUALIFIED\_SQL\_NAME Function Parameters

| Parameter | Description |
| --- | --- |
| `str` | Input value |

Exceptions

`ORA44004`: string is not a qualified SQL name

Usage Notes

A qualified SQL name \<qualified name> can be expressed by the following grammar:

```
<local qualified name> ::= <simple name> {'.' <simple name>}
<database link name> ::= <local qualified name> ['@' <connection string>]
<connection string> ::= <simple name>
<qualified name> ::= <local qualified name> ['@' <database link name>]
```

---

### SCHEMA\_NAME Function

This function verifies that the input string is an existing schema name.

Syntax

```
DBMS_ASSERT.SCHEMA_NAME (
   str      VARCHAR2 CHARACTER SET ANY_CS)
 RETURN     VARCHAR2 CHARACTER SET str%CHARSET;
```

Parameters

Table 26-6 SCHEMA\_NAME Function Parameters

| Parameter | Description |
| --- | --- |
| `str` | Input value |

Exceptions

`ORA44001`: Invalid schema name

Usage Notes

By definition, a schema name need not be just a simple SQL name. For example, " `FIRST` `LAST` " is a valid schema name. As a consequence, care must be taken to quote the output of schema name before concatenating it with SQL text.

---

### SIMPLE\_SQL\_NAME Function

This function verifies that the input string is a simple SQL name.

Syntax

```
DBMS_ASSERT.SIMPLE_SQL_NAME (
   str      VARCHAR2 CHARACTER SET ANY_CS)
 RETURN     VARCHAR2 CHARACTER SET str%CHARSET;
```

Parameters

Table 26-7 SIMPLE\_SQL\_NAME Function Parameters

| Parameter | Description |
| --- | --- |
| `str` | Input value |

Exceptions

`ORA44003`: string is not a simple SQL name

Usage Notes

- The input value must be meet the following conditions:
	- The name must begin with an alphabetic character. It may contain alphanumeric characters as well as the characters \_, $, and # in the second and subsequent character positions.
		- Quoted SQL names are also allowed.
		- Quoted names must be enclosed in double quotes.
		- Quoted names allow any characters between the quotes.
		- Quotes inside the name are represented by two quote characters in a row, for example, "a name with "" inside" is a valid quoted name.
		- The input parameter may have any number of leading and/or trailing white space characters.
- The length of the name is not checked.

---

### SQL\_OBJECT\_NAME Function

This function verifies that the input parameter string is a qualified SQL identifier of an existing SQL object.

Syntax

```
DBMS_ASSERT.SQL_OBJECT_NAME (
   str      VARCHAR2 CHARACTER SET ANY_CS)
 RETURN     VARCHAR2 CHARACTER SET str%CHARSET;
```

Parameters

Table 26-8 SQL\_OBJECT\_NAME Function Parameters

| Parameter | Description |
| --- | --- |
| `str` | Input value |

Exceptions

`ORA44002`: Invalid object name

Usage Notes

The use of synonyms requires that the base object exists.