---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/STORE.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
STORE SET file_name[.ext] [ CRE[ATE
 | REP[LACE] | APP[END]]
```

Saves attributes of the current SQL\*Plus environment in a script.

Terms

See [SAVE](SAVE.md) for information on the other terms and clauses in the STORE command syntax.

```
SET
```

Saves the values of the system variables.

Usage

This command creates a script which can be executed with the [START](START.md), [@ (at sign)](at-sign.md) or [@@ (double at sign)](double-at-sign.md) commands.

If you want to store a file under a name identical to a STORE command clause (that is, CREATE, REPLACE or APPEND), you must put the name in single quotes or specify a file extension.

Examples

To store the current SQL\*Plus system variables in a file named DEFAULTENV with the default command-file extension, enter

```
STORE SET DEFAULTENV
```

To append the current SQL\*Plus system variables to an existing file called DEFAULTENV with the extension OLD, enter

```
STORE SET DEFAULTENV.OLD APPEND
```