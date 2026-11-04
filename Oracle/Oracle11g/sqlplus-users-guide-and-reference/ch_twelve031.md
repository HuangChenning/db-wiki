---
title: PRINT
book: "SQL*Plus User's Guide and Reference"
doc_id: E16604-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve031.htm
tags:
  - oracle
  - 11g
  - sqlplus-users-guide-and-reference
---

---

Syntax

PRINT \[variable...\]

where variable... represents names of bind variables whose values you want to display.

Displays the current values of bind variables. For more information on bind variables, see your [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/toc.htm).

Enter PRINT with no variables to print all bind variables.

Usage

Bind variables are created using the VARIABLE command. See [VARIABLE](ch_twelve050.md) for more information and examples.

You can control the formatting of the PRINT output just as you would query output. For more information, see the formatting techniques described in [Formatting SQL\*Plus Reports](ch_six.md).

To automatically display bind variables referenced in a successful PL/SQL block or used in an EXECUTE command, use the AUTOPRINT clause of the SET command. See [SET](ch_twelve039.md) for more information.

Examples

The following example illustrates a PRINT command:

```
VARIABLE n NUMBER
BEGIN
:n := 1;
END;
/
```

```
PL/SQL procedure successfully completed.
```

```
PRINT n
```

```
N
----------
1
```