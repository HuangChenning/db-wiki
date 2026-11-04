---
title: GET
book: "SQL*Plus User's Guide and Reference"
doc_id: E16604-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve024.htm
tags:
  - oracle
  - 11g
  - sqlplus-users-guide-and-reference
---

---

Syntax

GET \[FILE\] file\_name\[.ext\] \[LIST | NOLIST\]

Loads an operating system file into the SQL buffer.

The buffer has no command history list and does not record SQL\*Plus commands.

Terms

FILE

Keyword to specify that the following argument is the name of the script you want to load. This optional keyword is usually omitted.

If you want to load a script with the name file, because it is a command keyword, you need to put the name file in single quotes.

file\_name\[.ext\]

Represents the file you wish to load (typically a script).

LIST

Lists the contents of the file after it is loaded. This is the default.

NOLIST

Suppresses the listing.

Usage

If you do not specify a file extension, SQL\*Plus assumes the default command-file extension (normally SQL). For information on changing the default extension, see [SET SUF\[FIX\] {SQL | text}](https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve040.htm#i2683419).

If the filename you specify contains the word list or the word file, the name must be in double quotes. SQL\*Plus searches for the file in the current working directory.

The operating system file should contain a single SQL statement or PL/SQL block. The statement should not be terminated with a semicolon. If a SQL\*Plus command or more than one SQL statement or PL/SQL block is loaded into the SQL buffer from an operating system file, an error occurs when the RUN or slash (/) command is used to execute the buffer.

The GET command can be used to load files created with the SAVE command. See [SAVE](ch_twelve038.md) for more information.

Examples

To load a file called YEARENDRPT with the extension SQL into the buffer, enter

```
GET YEARENDRPT
```