---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/obsolete-SQL-Plus-commands.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

This appendix covers earlier versions of some SQL\*Plus commands. While these older commands still function in SQL\*Plus, they are not supported. It is recommended that you use the alternative SQL\*Plus commands listed in the following table.

### C.1 SQL\*Plus Obsolete Command Alternatives

Obsolete commands are available in current releases of SQL\*Plus. In future releases, they may only be available by setting the SQLPLUSCOMPATIBILITY variable. You should modify scripts using obsolete commands to use the alternative commands.

| Obsolete Command | Alternative Command | Description of Alternative Command |
| --- | --- | --- |
| ``` BTITLE (old form) ``` | ``` BTITLE ``` | Places and formats a title at the bottom of each report page or lists the current BTITLE definition. |
| ``` COLUMN DEFAULT ``` | ``` COLUMN CLEAR ``` | Resets column display attributes to default values. |
| ``` DOCUMENT ``` | ``` REMARK ``` | Places a comment which SQL\*Plus does not interpret as a command. |
| ``` NEWPAGE ``` | ``` SET NEWP[AGE] {1 \| n \| NONE} ``` | Sets the number of blank lines to be printed from the top of each page to the top title. |
| ``` SET BUFFER ``` | ``` EDIT ``` | Enables the editing of the SQL\*Plus command buffer, or the contents of a saved file. Use the SQL\*Plus SAVE, GET, @ and START commands to create and use external files. |
| ``` SET COMPATIBILITY ``` | ``` none ``` | Obsolete |
| ``` SET CLOSECURSOR ``` | ``` none ``` | Obsolete |
| ``` SET DOCUMENT ``` | ``` none ``` | Obsolete |
| ``` SET MAXDATA ``` | ``` none ``` | Obsolete |
| ``` SET SCAN ``` | ``` SET DEF[INE] {& \| c \| ON \| OFF} ``` | Sets the character used to prefix substitution variables. |
| ``` SET SPACE ``` | ``` SET COLSEP {  \| text} ``` | Sets the text to be printed between SELECTed columns. |
| ``` SET TRUNCATE ``` | ``` SET WRA[P] {ON \| OFF} ``` | Controls whether SQL\*Plus truncates a SELECTed row if it is too long for the current line width. |
| ``` SHOW LABEL ``` | ``` none ``` | Obsolete |
| ``` TTITLE (old form) ``` | ``` TTITLE ``` | Places and formats a title at the top of each report page or lists the current TTITLE definition. |

### C.2 BTITLE (old form)

Syntax

```
BTI[TLE] text
```

Displays a title at the bottom of each report page.

The old form of BTITLE offers formatting features more limited than those of the new form, but provides compatibility with UFI (a predecessor of SQL\*Plus). The old form defines the bottom title as an empty line followed by a line with centered text. See [TTI\[TLE\] text (obsolete old form)](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/obsolete-SQL-Plus-commands.html#GUID-865E4EF3-21ED-4C12-AFF0-3DA3EC2C4EE3) for more details.

### C.3 COLUMN DEFAULT

Syntax

```
COL[UMN] {column|expr} DEF[AULT] (obsolete)
```

Resets the display attributes for a given column to default values.

Has the same effect as COLUMN CLEAR.

### C.4 DOCUMENT

Syntax

```
DOC[UMENT]
```

Begins a block of documentation in a script.

For information on the current method of inserting comments in a script, see the section [About Placing Comments in Scripts](using-scripts-in-SQL-Plus.md) and the [REMARK](REMARK.md) command.

After you type DOCUMENT and enter \[Return\], SQL\*Plus displays the prompt DOC> in place of SQL> until you end the documentation. The "pound" character (#) on a line by itself ends the documentation.

If you have set DOCUMENT to OFF, SQL\*Plus suppresses the display of the block of documentation created by the DOCUMENT command. For more information, see [SET DOC\[UMENT\] {ON|OFF} (obsolete)](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/obsolete-SQL-Plus-commands.html#GUID-231A07A0-33DD-43CD-A324-24927DA61386).

### C.5 NEWPAGE

Syntax

```
NEWPAGE [1|n]
```

Advances spooled output n lines beyond the beginning of the next page.

See [SET NEWP\[AGE\] {1 | n | NONE}](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/SET-system-variable-summary.html#GUID-B7D1FFE5-9FFE-43C3-B52B-6DCCBCC3AA03) for information on the current method for advancing spooled output.

### C.6 SET BUFFER

Syntax

```
SET BUF[FER] {buffer|SQL}
```

Makes the specified buffer the current buffer.

Initially, the SQL buffer is the current buffer. SQL\*Plus does not require the use of multiple buffers; the SQL buffer alone should meet your needs.

If the buffer name you enter does not exist, SET BUFFER defines (creates and names) the buffer. SQL\*Plus deletes the buffer and its contents when you exit SQL\*Plus.

Running a query automatically makes the SQL buffer the current buffer. To copy text from one buffer to another, use the GET and SAVE commands. To clear text from the current buffer, use CLEAR BUFFER. To clear text from the SQL buffer while using a different buffer, use CLEAR SQL.

### C.7 SET COMPATIBILITY

Syntax

```
SET COM[PATIBILITY]{V7 | V8 | NATIVE
}
```

Specifies the version of the SQL language parsing syntax to use.

Set COMPATIBILITY to V7 for Oracle7, or to V8 for Oracle8 or later. COMPATIBILITY always defaults to NATIVE. Set COMPATIBILITY for the version of Oracle Database SQL syntax you want to use on the connected database, otherwise.

The default compatibility setting, NATIVE, is the most relevant setting for modern Oracle databases.

For information about SQL\*Plus version compatibility settings, see [SET SQLPLUSCOMPAT\[IBILITY\] {x.y\[.z\]}](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/SET-system-variable-summary.html#GUID-B78B8F90-AD6C-48CA-B0A8-D657F6FBFC38).

Example

To run a script, SALARY.SQL, created with Oracle7 SQL syntax, enter

```
SET COMPATIBILITY V7
START SALARY
```

After running the file, reset compatibility to NATIVE to run scripts created for Oracle Database 10g:

```
SET COMPATIBILITY NATIVE
```

Alternatively, you can add the command SET COMPATIBILITY V7 to the beginning of the script, and reset COMPATIBILITY to NATIVE at the end of the file.

### C.8 SET CLOSECURSOR

Syntax

```
SET CLOSECUR[SOR] {ON|OFF}
```

Sets the cursor usage behavior.

On or OFF sets whether or not the cursor will close and reopen after each SQL statement. This feature may be useful in some circumstances to release resources in the database server.

### C.9 SET DOCUMENT

Syntax

```
SET DOC[UMENT] {ON|OFF}
```

Displays or suppresses blocks of documentation created by the DOCUMENT command.

SET DOCUMENT ON causes blocks of documentation to be echoed to the screen. Set DOCUMENT OFF suppresses the display of blocks of documentation.

See [DOC\[UMENT\] (obsolete)](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/obsolete-SQL-Plus-commands.html#GUID-2F8C7391-08A7-4A56-965B-03175662AC51) for information on the DOCUMENT command.

### C.10 SET MAXDATA

Syntax

```
SET MAXD[ATA] n
```

Sets the maximum total row width that SQL\*Plus can process.

In SQL\*Plus, the maximum row width is now unlimited. Any values you set using SET MAXDATA are ignored by SQL\*Plus.

### C.11 SET SCAN

Syntax

```
SET SCAN {ON|OFF}
```

Controls scanning for the presence of substitution variables and parameters. OFF suppresses processing of substitution variables and parameters; ON enables normal processing.

ON functions in the same manner as SET DEFINE ON.

### C.12 SET SPACE

Syntax

```
SET SPACE {1|n}
```

Sets the number of spaces between columns in output. The maximum value of n is 10.

The SET SPACE 0 and SET COLSEP " commands have the same effect. This command is obsoleted by SET COLSEP, but you can still use it for backward compatibility. You may prefer to use COLSEP because the SHOW command recognizes COLSEP and does not recognize SPACE.

### C.13 SET TRUNCATE

Syntax

```
SET TRU[NCATE] {ON|OFF}
```

Controls whether SQL\*Plus truncates or wraps a data item that is too long for the current line width.

ON functions in the same manner as SET WRAP OFF, and vice versa. You may prefer to use WRAP because the SHOW command recognizes WRAP and does not recognize TRUNCATE.

### C.14 TTITLE (old form)

Syntax

```
TTI[TLE] text
```

Displays a title at the top of each report page.

The old form of TTITLE offers formatting features more limited than those of the new form, but provides compatibility with UFI (a predecessor of SQL\*Plus). The old form defines the top title as a line with the date left-aligned and the page number right-aligned, followed by a line with centered text and then a blank line.

The text you enter defines the title TTITLE displays.

SQL\*Plus centers text based on the size of a line as determined by SET LINESIZE. A separator character (|) begins a new line; two line separator characters in a row (||) insert a blank line. You can change the line separator character with SET HEADSEP.

You can control the formatting of page numbers in the old forms of TTITLE and BTITLE by defining a variable named "\_page". The default value of \_page is the formatting string "page &P4". To alter the format, you can DEFINE \_page with a new formatting string as follows:

```
SET ESCAPE / SQL> DEFINE _page = 'Page /&P2'
```

This formatting string will print the word "page" with an initial capital letter and format the page number to a width of two. You can substitute any text for "page" and any number for the width. You must set escape so that SQL\*Plus does not interpret the ampersand (&) as a substitution variable. See [SET ERRORL\[OGGING\] {ON | OFF} \[TABLE \[schema.\]tablename\] \[TRUNCATE\] \[IDENTIFIER identifier\]](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/SET-system-variable-summary.html#GUID-C7521DA1-03D1-4C02-8458-449479724F3E) for more information on setting the escape character.

SQL\*Plus interprets TTITLE in the old form if a valid new-form clause does not immediately follow the command name.

If you want to use CENTER with TTITLE and put more than one word on a line, you should use the new form of TTITLE. For more information see the [TTITLE](TTITLE.md) command.

Example

To use the old form of TTITLE to set a top title with a left-aligned date and right-aligned page number on one line followed by SALES DEPARTMENT on the next line and PERSONNEL REPORT on a third line, enter

```
TTITLE 'SALES DEPARTMENT|PERSONNEL REPORT'
```