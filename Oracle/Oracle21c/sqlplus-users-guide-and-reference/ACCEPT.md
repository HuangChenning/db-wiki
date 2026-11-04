---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/ACCEPT.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
ACC[EPT] variable [NUM[BER] | CHAR
 | DATE | BINARY_FLOAT | BINARY_DOUBLE] [FOR[MAT] format] [DEF[AULT] default] [PROMPT text|NOPR[OMPT
]] [HIDE]
```

Reads a line of input and stores it in a given substitution variable.

Terms

```
variable
```

Represents the name of the variable in which you wish to store a value. If variable does not exist, SQL\*Plus creates it.

```
NUM[BER]
```

Makes the variable a NUMBER datatype. If the reply does not match the datatype, ACCEPT gives an error message and prompts again.

```
CHAR
```

Makes the variable a CHAR datatype. The maximum CHAR length is 240 bytes. If a multi-byte character set is used, one CHAR may be more than one byte in size.

```
DATE
```

Makes reply a valid DATE format. If the reply is not a valid DATE format, ACCEPT gives an error message and prompts again. The datatype is CHAR.

```
BINARY_FLOAT
```

Makes the variable a BINARY\_FLOAT datatype. BINARY\_FLOAT is a floating-point number that conforms substantially with the Institute for Electrical and Electronics Engineers (IEEE) Standard for Binary Floating-Point Arithmetic, IEEE Standard 754-1985.

```
BINARY_DOUBLE
```

Makes the variable a BINARY\_DOUBLE datatype. BINARY\_DOUBLE is a floating-point number that conforms substantially with the Institute for Electrical and Electronics Engineers (IEEE) Standard for Binary Floating-Point Arithmetic, IEEE Standard 754-1985.

```
FOR[MAT]
```

Specifies the input format for the reply. If the reply does not match the specified format, ACCEPT gives an error message and prompts again. If an attempt is made to enter more characters than are specified by the char format, an error message is given and the value must be reentered. If an attempt is made to enter a greater number precision than is specified by the number format, an error message is given and the value must be reentered. The format element must be a text constant such as A10 or 9.999. See [COLUMN](COLUMN.md) FORMAT for a complete list of format elements.

Oracle Database date formats such as "dd/mm/yy" are valid when the datatype is DATE. DATE without a specified format defaults to the NLS\_DATE\_FORMAT of the current session. See [Format Models](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=SQLRF-GUID-DFB23985-2943-4C6A-96DF-DF0F664CED96) for information on Oracle Database date formats.

```
DEF[AULT]
```

Sets the default value if a reply is not given. The reply must be in the specified format if defined.

```
PROMPT text
```

Displays text on-screen before accepting the value of variable from the user.

```
NOPR[OMPT]
```

Skips a line and waits for input without displaying a prompt.

```
HIDE
```

Suppresses the display as you type the reply.

To display or reference variables, use the DEFINE command. See the [DEFINE](DEFINE.md) command for more information.

Examples

To display the prompt "Password: ", place the reply in a CHAR variable named PSWD, and suppress the display, enter

```
ACCEPT pswd CHAR PROMPT 'Password:  ' HIDE
```

To display the prompt "Enter weekly salary: " and place the reply in a NUMBER variable named SALARY with a default of 000.0, enter

```
ACCEPT salary NUMBER FORMAT '999.99' DEFAULT '000.0' -
PROMPT 'Enter weekly salary:  '
```

To display the prompt "Enter date hired: " and place the reply in a DATE variable, HIRED, with the format "dd/mm/yyyy" and a default of "01/01/2003", enter

```
ACCEPT hired DATE FORMAT 'dd/mm/yyyy' DEFAULT '01/01/2003'-
PROMPT 'Enter date hired:  '
```

To display the prompt "Enter employee lastname: " and place the reply in a CHAR variable named LASTNAME, enter

```
ACCEPT lastname CHAR FORMAT 'A20' -
PROMPT 'Enter employee lastname:  '
```