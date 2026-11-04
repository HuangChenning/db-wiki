---
title: STORE
book: "SQL*Plus User's Guide and Reference"
doc_id: E16604-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve046.htm
tags:
  - oracle
  - 11g
  - sqlplus-users-guide-and-reference
---

---

Syntax

STORE SET file\_name\[.ext\] \[ CRE\[ATE | REP\[LACE\] | APP\[END\]\]

Saves attributes of the current SQL\*Plus environment in a script.

Terms

See [SAVE](ch_twelve038.md) for information on the other terms and clauses in the STORE command syntax.

SET

Saves the values of the system variables.

Usage

This command creates a script which can be executed with the [START](ch_twelve044.md), [@ (at sign)](ch_twelve002.md) or [@@ (double at sign)](ch_twelve003.md) commands.

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