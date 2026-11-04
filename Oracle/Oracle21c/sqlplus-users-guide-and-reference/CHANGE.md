---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/CHANGE.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
C[HANGE] sepchar old [sepchar [new [sepchar]]]
```

Changes the first occurrence of the specified text on the current line in the buffer.

Terms

```
sepchar
```

Represents any non-alphanumeric character such as "/" or "!". Use a sepchar that does not appear in old or new.

```
old
```

Represents the text you wish to change. CHANGE ignores case in searching for old. For example,

```
CHANGE /aq/aw
```

finds the first occurrence of "aq", "AQ", "aQ", or "Aq" and changes it to "aw". SQL\*Plus inserts the new text exactly as you specify it.

If old is prefixed with "...", it matches everything up to and including the first occurrence of old. If it is suffixed with "...", it matches the first occurrence of old and everything that follows on that line. If it contains an embedded "...", it matches everything from the preceding part of old through the following part of old.

```
new
```

Represents the text with which you wish to replace old. If you omit new and, optionally, the second and third sepchars, CHANGE deletes old from the current line of the buffer.

Usage

CHANGE changes the first occurrence of the existing specified text on the current line of the buffer to the new specified text. The current line is marked with an asterisk (\*) in the LIST output.

You can also use CHANGE to modify a line in the buffer that has generated an Oracle Database error. SQL\*Plus sets the buffer's current line to the line containing the error so that you can make modifications.

To reenter an entire line, you can type the line number followed by the new contents of the line. If you specify a line number larger than the number of lines in the buffer and follow the number with text, SQL\*Plus adds the text in a new line at the end of the buffer. If you specify zero ("0") for the line number and follow the zero with text, SQL\*Plus inserts the line at the beginning of the buffer (that line becomes line 1).

Examples

Enter 3 so the current line of the buffer contains the following text:

```
3
```
```
3* WHERE JOB_ID IS IN ('CLERK', 'SA_MAN')
```

Enter the following command:

```
CHANGE /CLERK/SH_CLERK/
```

The text in the buffer changes as follows:

```
3* WHERE JOB_ID IS IN ('SH_CLERK', 'SA_MAN')
```

Or enter the following command:

```
CHANGE /'CLERK',... /'SH_CLERK'/
```

The original line changes to

```
3* WHERE JOB_ID IS IN ('SH_CLERK')
```

Or enter the following command:

```
CHANGE /(...)/('SA_MAN')/
```

The original line changes to

```
3* WHERE JOB_ID IS IN ('SA_MAN')
```

You can replace the contents of an entire line using the line number. This entry

```
3  WHERE JOB_ID IS IN ('SH_CLERK')
```

causes the second line of the buffer to be replaced with

```
WHERE JOB_ID IS IN ('SH_CLERK')
```

Note that entering a line number followed by a string will replace the line regardless of what text follows the line number. For example,

```
2  CHANGE/OLD/NEW/
```

will change the second line of the buffer to be

```
2* C/OLD/NEW/
```