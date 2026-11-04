---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/DEFINE.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
DEF[INE] [variable] | [variable = text]
```

Specifies a user or predefined variable and assigns a CHAR value to it, or lists the value and variable type of a single variable or all variables.

Terms

```
variable
```

Represents the user or predefined variable whose value you wish to assign or list.

```
text
```

Represents the CHAR value you wish to assign to variable. Enclose text in single quotes if it contains punctuation or blanks.

```
variable = text
```

Defines (names) a substitution variable and assigns it a CHAR value.

Enter DEFINE followed by variable to list the value and type of variable. Enter DEFINE with no clauses to list the values and types of all substitution variables.

Usage

Defined variables retain their values until you:

- enter a new DEFINE command referencing the variable
- enter an UNDEFINE command referencing the variable
- enter an ACCEPT command referencing the variable
- reference the variable in the NEW\_VALUE or OLD\_VALUE clause of a COLUMN command and then reference the column in a SELECT command
- EXIT SQL\*Plus

Whenever you run a stored query or script, SQL\*Plus substitutes the value of variable for each substitution variable referencing variable (in the form &variable or &&variable). SQL\*Plus will not prompt you for the value of variable in this session until you UNDEFINE variable.

If the value of a defined variable extends over multiple lines (using the SQL\*Plus command continuation character), SQL\*Plus replaces each continuation character and carriage return with a space. For example, SQL\*Plus interprets

```
DEFINE TEXT = 'ONE-
TWO-
THREE'
```

as

```
DEFINE TEXT = 'ONE TWO THREE'
```

You should avoid defining variables with names that may be identical to values that you will pass to them, as unexpected results can occur. If a value supplied for a defined variable matches a variable name, then the contents of the matching variable are used instead of the supplied value.

Some variables are predefined when SQL\*Plus starts. Enter DEFINE to see their definitions.

Examples

To assign the value MANAGER to the variable POS, type:

```
DEFINE POS = MANAGER
```

If you execute a command containing a reference to &POS, SQL\*Plus substitutes the value MANAGER for &POS and will not prompt you for a POS value.

To assign the CHAR value 20 to the variable DEPARTMENT\_ID, type:

```
DEFINE DEPARTMENT_ID = 20
```

Even though you enter the number 20, SQL\*Plus assigns a CHAR value to DEPARTMENT\_ID consisting of two characters, 2 and 0.

To list the definition of DEPARTMENT\_ID, enter

```
DEFINE DEPARTMENT_ID
```
```
DEFINE DEPARTMENT_ID = "20" (CHAR)
```

This result shows that the value of DEPARTMENT\_ID is 20.

### 13.17.1 Predefined Variables

There are nine variables defined during SQL\*Plus installation. These variables only differ from user-defined variables by having predefined values.

Table 13-3 Variables Predefined at SQL\*Plus Installation

| Variable Name | Contains |
| --- | --- |
| \_CONNECT\_IDENTIFIER | Connection identifier used to make connection, where available. |
| \_DATE | Current date, or a user defined fixed string. |
| \_EDITOR | Specifies the editor used by the EDIT command. |
| \_O\_VERSION | Current version of the installed Oracle Database. |
| \_O\_RELEASE | Full release number of the installed Oracle Database. |
| \_PRIVILEGE | Privilege level of the current connection. |
| \_SQLPLUS\_RELEASE | Full release number of installed SQL\*Plus component. |
| \_USER | User name used to make connection. |
| \_SQL\_ID | sql\_id of the SQL statement executed. |

\_CONNECT\_IDENTIFIER

Contains the `INSTANCE_NAME, SERVICE_NAME` or `ORACLE_SID` from the connection identifier. If a connection identifier is not supplied by the user during connection, the `_CONNECT_IDENTIFIER` contains the `ORACLE_SID`.

\_DATE

Contains either the current date as a dynamic variable, or a fixed string. The current date is the default and is formatted using the value of NLS\_DATE\_FORMAT.

Because \_DATE can be used as a normal substitution variable, users may put it in TTITLE. If \_DATE is dynamic and is used in TTITLE it will have all the normal variable semantics. If it is used with an ampersand than the value will be set to the time when the TTITLE command is executed. If it is used without an ampersand prefix, it will be re-evaluated for each page. For long reports with \_DATE in the TTITLE or with multiple references to &\_DATE, different times may be displayed for each occurrence of the variable.

Users using \_DATE in TTITLEs will almost certainly want to use an ampersand: &\_DATE, so that each page of the report has exactly the same timestamp. This is especially true when the current date format contains a "seconds" component.

A DEFINE (with no arguments) or dereference using &\_DATE will give the current date.

The \_DATE value can be UNDEFINED, or set to a fixed string with an explicit DEFINE \_DATE.

You can re-enable the default dynamic date behavior with:

```
DEFINE _DATE = "" (an empty string)
```

\_DATE enables time values to be included in your SQL\*Plus prompt.

\_EDITOR

Specifies the default editor used by the EDIT command.

During SQL\*Plus installation on Windows operating systems, it is set to Notepad. On UNIX operating systems, it is set to the value of the UNIX environment variable, EDITOR, if it exists, otherwise it is set to Ed.

You can use the DEFINE command to redefine \_EDITOR, to hold the name of your preferred text editor. For example, to define the editor used by EDIT to be vi, enter the following command:

```
DEFINE _EDITOR = vi
```

\_O\_VERSION

Contains the current version of the installed Oracle Database.

\_O\_RELEASE

Contains the full release number of the installed Oracle Database in the form:

1801000000

\_PRIVILEGE

Contains a value indicating the privilege level of the current connection. It contains one of the following values:

- AS SYSASM
- AS SYSBACKUP
- AS SYSDBA
- AS SYSDG
- AS SYSOPER
- AS SYSRAC
- An empty string for normal-user connections or when there is no connection.

AS SYSASM, AS SYSBACKUP, AS SYSDBA, AS SYSDG, AS SYSOPER and AS SYSRAC are database administrator level privileges.

See Also:

[GRANT](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=SQLRF-GUID-20B4E2C0-A7F8-4BC8-A5E8-BE61BDC41AC3) for information on AS SYSDBA and AS SYSOPER privileges.

\_SQLPLUS\_RELEASE

Contains the full release number of the installed SQL\*Plus component in the form:

1801000000

\_USER

Contains the user name connected to the current connection.

\_SQL\_ID

Contains the sql\_id for the currently executed SQL or PL/SQL statements.

You can view the value of each of these variables with the DEFINE command.

These variables can be accessed and redefined like any other substitution variable. They can be used in TTITLE, in '&' substitution variables, or in your SQL\*Plus command-line prompt.

You can use the DEFINE command to view the definitions of these nine predefined variables in the same way as you view other DEFINE definitions. You can also use the DEFINE command to redefine their values, or you can use the UNDEFINE command to remove their definitions and make them unavailable.

To view a specific variable definition, enter

```
DEFINE variable
```

where variable is the name of the substitution variable whose definition you want to view.

To view all predefined and user defined variable definitions, enter

```
DEFINE
```

All predefined and all user defined variable definitions are displayed.

You can use UNDEFINE to remove a substitution variable definition and make it unavailable.

Examples of Use of Predefined Variables

To change your SQL\*Plus prompt to display your connection identifier, enter:

```
SET SQLPROMPT '_CONNECT_IDENTIFIER > '
```

To view the predefined value of the \_SQLPLUS\_RELEASE substitution variable, enter

```
DEFINE _SQLPLUS_RELEASE
```

The value of the predefined variable \_SQLPLUS\_RELEASE is displayed.

```
DEFINE _SQLPLUS_RELEASE = "1801000000" (CHAR)
```