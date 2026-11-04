---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/ATTRIBUTE.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
ATTR[IBUTE] [type_name.attribute_name [option ...]]
```

where option represents one of the following clauses:

```
ALI[AS] alias CLE[AR] FOR[MAT] format LIKE {type_name.attribute_name | alias} ON
 | OFF
```

Specifies display characteristics for a given attribute of an Object Type column, such as the format of NUMBER data. Columns and attributes should not have the same names as they share a common namespace.

Also lists the current display characteristics for a single attribute or all attributes.

Enter ATTRIBUTE followed by type\_name.attribute\_name and no other clauses to list the current display characteristics for only the specified attribute. Enter ATTRIBUTE with no clauses to list all current attribute display characteristics.

Terms

```
type_name.attribute_name
```

Identifies the data item (typically the name of an attribute) within the set of attributes for a given object of Object Type, type\_name.

If you select objects of the same Object Type, an ATTRIBUTE command for that type\_name.attribute\_name applies to all such objects you reference in that session.

```
ALI[AS] alias
```

Assigns a specified alias to a type\_name.attribute\_name, which can be used to refer to the type\_name.attribute\_name in other ATTRIBUTE commands.

```
CLE[AR]
```

Resets the display characteristics for the attribute\_name. The format specification must be a text constant such as A10 or $9,999—not a variable.

```
FOR[MAT] format
```

Specifies the display format of the column. The format specification must be a text constant such as A10 or $9,999—not a variable.

```
LIKE {type_name.attribute_name | alias}
```

Copies the display characteristics of another attribute. LIKE copies only characteristics not defined by another clause in the current ATTRIBUTE command.

```
ON | OFF
```

Controls the status of display characteristics for a column. OFF disables the characteristics for an attribute without affecting the characteristics' definition. ON reinstates the characteristics.

Usage

You can enter any number of ATTRIBUTE commands for one or more attributes. All attribute characteristics set for each attribute remain in effect for the remainder of the session, until you turn the attribute OFF, or until you use the CLEAR COLUMN command. Thus, the ATTRIBUTE commands you enter can control an attribute's display characteristics for multiple SQL SELECT commands.

When you enter multiple ATTRIBUTE commands for the same attribute, SQL\*Plus applies their clauses collectively. If several ATTRIBUTE commands apply the same clause to the same attribute, the last one entered will control the output.

Examples

To make the LAST\_NAME attribute of the Object Type EMPLOYEE\_TYPE twenty characters wide, enter

```
ATTRIBUTE EMPLOYEE_TYPE.LAST_NAME FORMAT A20
```

To format the SALARY attribute of the Object Type EMPLOYEE\_TYPE so that it shows millions of dollars, rounds to cents, uses commas to separate thousands, and displays $0.00 when a value is zero, enter

```
ATTRIBUTE EMPLOYEE_TYPE.SALARY FORMAT $9,999,990.99
```