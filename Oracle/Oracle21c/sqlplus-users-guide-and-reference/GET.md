---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/GET.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
GET [FILE] file_name[.ext] [LIST
 | NOLIST]
```

Loads an operating system file into the SQL buffer.

Terms

```
FILE
```

Keyword to specify that the following argument is the name of the script you want to load. This optional keyword is usually omitted.

If you want to load a script with the name file, because it is a command keyword, you need to put the name file in single quotes.

```
file_name[.ext]
```

Represents the file you wish to load (typically a script).

```
LIST
```

Lists the contents of the file after it is loaded. This is the default.

```
NOLIST
```

Suppresses the listing.

Usage

If you do not specify a file extension, SQL\*Plus assumes the default command-file extension (normally SQL). For information on changing the default extension, see [SET SUF\[FIX\] {SQL | text}](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/SET-system-variable-summary.html#GUID-0DFB3D8C-0389-4F44-A68D-3FDBB9F962EA).

If the filename you specify contains the word list or the word file, the name must be in double quotes. SQL\*Plus searches for the file in the current working directory.

The operating system file should contain a single SQL statement or PL/SQL block. The statement should not be terminated with a semicolon. If a SQL\*Plus command or more than one SQL statement or PL/SQL block is loaded into the SQL buffer from an operating system file, an error occurs when the RUN or slash (/) command is used to execute the buffer.

The GET command can be used to load files created with the SAVE command. See [SAVE](SAVE.md) for more information.

Examples

To load a file called YEARENDRPT with the extension SQL into the buffer, enter

```
GET YEARENDRPT
```