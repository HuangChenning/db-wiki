---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/PAUSE.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
PAU[SE] [text]
```

where text represents the text you wish to display.

Displays the specified text then waits for the user to press RETURN.

Enter PAUSE followed by no text to display two empty lines.

Usage

Because PAUSE always waits for the user's response, it is best to use a message that tells the user explicitly to press \[Return\].

PAUSE reads input from the terminal (if a terminal is available) even when you have designated the source of the command input as a file.

See [SET PAU\[SE\] {ON | OFF | text}](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/SET-system-variable-summary.html#GUID-62BF8A5F-DE6A-405C-AF3E-A287C900C71A) for information on pausing between pages of a report.

Examples

To print "Adjust paper and press RETURN to continue." and to have SQL\*Plus wait for the user to press \[Return\], you might include the following PAUSE command in a script:

```
SET PAUSE OFF
PAUSE Adjust paper and press RETURN to continue.
SELECT ...
```