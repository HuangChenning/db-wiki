---
title: "Obsolete SQL*Plus Commands"
book: "SQL*Plus User's Guide and Reference"
doc_id: E16604-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e16604/apc.htm
tags:
  - oracle
  - 11g
  - sqlplus-users-guide-and-reference
---

## C Obsolete SQL\*Plus Commands

This appendix covers earlier versions of some SQL\*Plus commands. While these older commands still function in SQL\*Plus, they are not supported. It is recommended that you use the alternative SQL\*Plus commands listed in the following table.

## SQL\*Plus Obsolete Command Alternatives

Obsolete commands are available in current releases of SQL\*Plus. In future releases, they may only be available by setting the SQLPLUSCOMPATIBILITY variable. You should modify scripts using obsolete commands to use the alternative commands.

| Obsolete Command | Alternative Command | Description of Alternative Command |
| --- | --- | --- |
| BTITLE (old form) | [BTITLE](ch_twelve010.md) | Places and formats a title at the bottom of each report page or lists the current BTITLE definition. |
| COLUMN DEFAULT | [COLUMN](ch_twelve013.md) CLEAR | Resets column display attributes to default values. |
| DOCUMENT | [REMARK](ch_twelve034.md) | Places a comment which SQL\*Plus does not interpret as a command. |
| NEWPAGE | [SET NEWP\[AGE\] {1 \| n \| NONE}](https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve040.htm#i2678637) | Sets the number of blank lines to be printed from the top of each page to the top title. |
| SET BUFFER | [EDIT](ch_twelve021.md) | Enables the editing of the SQL\*Plus command buffer, or the contents of a saved file. Use the SQL\*Plus SAVE, GET, @ and START commands to create and use external files. |
| SET COMPATIBILITY | none | Obsolete |
| SET CLOSECURSOR | none | Obsolete |
| SET DOCUMENT | none | Obsolete |
| SET MAXDATA | none | Obsolete |
| SET SCAN | [SET DEF\[INE\] {& \| c \| ON \| OFF}](https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve040.htm#i2698854) | Sets the character used to prefix substitution variables. |
| SET SPACE | [SET COLSEP { \| text}](ch_twelve040.md) | Sets the text to be printed between SELECTed columns. |
| SET TRUNCATE | [SET WRA\[P\] {ON \| OFF}](https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve040.htm#i2699438) | Controls whether SQL\*Plus truncates a SELECTed row if it is too long for the current line width. |
| SHOW LABEL | none | Obsolete |
| TTITLE (old form) | [TTITLE](ch_twelve048.md) | Places and formats a title at the top of each report page or lists the current TTITLE definition. |

## BTI\[TLE\] text (obsolete old form)

Displays a title at the bottom of each report page.

The old form of BTITLE offers formatting features more limited than those of the new form, but provides compatibility with UFI (a predecessor of SQL\*Plus). The old form defines the bottom title as an empty line followed by a line with centered text. See [TTI\[TLE\] text (obsolete old form)](#i656861) for more details.

## COL\[UMN\] {column|expr} DEF\[AULT\] (obsolete)

Resets the display attributes for a given column to default values.

Has the same effect as COLUMN CLEAR.

## DOC\[UMENT\] (obsolete)

Begins a block of documentation in a script.

For information on the current method of inserting comments in a script, see the section [Placing Comments in Scripts](ch_five.md) and the [REMARK](ch_twelve034.md) command.

After you type DOCUMENT and enter \[Return\], SQL\*Plus displays the prompt DOC> in place of SQL> until you end the documentation. The "pound" character (#) on a line by itself ends the documentation.

If you have set DOCUMENT to OFF, SQL\*Plus suppresses the display of the block of documentation created by the DOCUMENT command. For more information, see [SET DOC\[UMENT\] {ON|OFF} (obsolete)](#i656817).

## NEWPAGE \[1|n\] (obsolete)

Advances spooled output n lines beyond the beginning of the next page.

See [SET NEWP\[AGE\] {1 | n | NONE}](https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve040.htm#i2678637) for information on the current method for advancing spooled output.

## SET BUF\[FER\] {buffer|SQL} (obsolete)

Makes the specified buffer the current buffer.

Initially, the SQL buffer is the current buffer. SQL\*Plus does not require the use of multiple buffers; the SQL buffer alone should meet your needs.

If the buffer name you enter does not exist, SET BUFFER defines (creates and names) the buffer. SQL\*Plus deletes the buffer and its contents when you exit SQL\*Plus.

Running a query automatically makes the SQL buffer the current buffer. To copy text from one buffer to another, use the GET and SAVE commands. To clear text from the current buffer, use CLEAR BUFFER. To clear text from the SQL buffer while using a different buffer, use CLEAR SQL.

## SET COM\[PATIBILITY\]{V7 | V8 | NATIVE} (obsolete)

Specifies the version of the SQL language parsing syntax to use.

Set COMPATIBILITY to V7 for Oracle7, or to V8 for Oracle8 or later. COMPATIBILITY always defaults to NATIVE. Set COMPATIBILITY for the version of Oracle Database SQL syntax you want to use on the connected database, otherwise.

The default compatibility setting, NATIVE, is the most relevant setting for modern Oracle databases.

For information about SQL\*Plus version compatibility settings, see [SET SQLPLUSCOMPAT\[IBILITY\] {x.y\[.z\]}](https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve040.htm#i2699351).

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

## SET CLOSECUR\[SOR\] {ON|OFF} (obsolete)

Sets the cursor usage behavior.

On or OFF sets whether or not the cursor will close and reopen after each SQL statement. This feature may be useful in some circumstances to release resources in the database server.

## SET DOC\[UMENT\] {ON|OFF} (obsolete)

Displays or suppresses blocks of documentation created by the DOCUMENT command.

SET DOCUMENT ON causes blocks of documentation to be echoed to the screen. Set DOCUMENT OFF suppresses the display of blocks of documentation.

See [DOC\[UMENT\] (obsolete)](#i656750) for information on the DOCUMENT command.

## SET MAXD\[ATA\] n (obsolete)

Sets the maximum total row width that SQL\*Plus can process.

In SQL\*Plus, the maximum row width is now unlimited. Any values you set using SET MAXDATA are ignored by SQL\*Plus.

## SET SCAN {ON|OFF} (obsolete)

Controls scanning for the presence of substitution variables and parameters. OFF suppresses processing of substitution variables and parameters; ON enables normal processing.

ON functions in the same manner as SET DEFINE ON.

## SET SPACE {1|n} (obsolete)

Sets the number of spaces between columns in output. The maximum value of n is 10.

The SET SPACE 0 and SET COLSEP " commands have the same effect. This command is obsoleted by SET COLSEP, but you can still use it for backward compatibility. You may prefer to use COLSEP because the SHOW command recognizes COLSEP and does not recognize SPACE.

## SET TRU\[NCATE\] {ON|OFF} (obsolete)

Controls whether SQL\*Plus truncates or wraps a data item that is too long for the current line width.

ON functions in the same manner as SET WRAP OFF, and vice versa. You may prefer to use WRAP because the SHOW command recognizes WRAP and does not recognize TRUNCATE.

## TTI\[TLE\] text (obsolete old form)

Displays a title at the top of each report page.

The old form of TTITLE offers formatting features more limited than those of the new form, but provides compatibility with UFI (a predecessor of SQL\*Plus). The old form defines the top title as a line with the date left-aligned and the page number right-aligned, followed by a line with centered text and then a blank line.

The text you enter defines the title TTITLE displays.

SQL\*Plus centers text based on the size of a line as determined by SET LINESIZE. A separator character (|) begins a new line; two line separator characters in a row (||) insert a blank line. You can change the line separator character with SET HEADSEP.

You can control the formatting of page numbers in the old forms of TTITLE and BTITLE by defining a variable named "\_page". The default value of \_page is the formatting string "page &P4". To alter the format, you can DEFINE \_page with a new formatting string as follows:

```
SET ESCAPE / SQL> DEFINE _page = 'Page /&P2'
```

This formatting string will print the word "page" with an initial capital letter and format the page number to a width of two. You can substitute any text for "page" and any number for the width. You must set escape so that SQL\*Plus does not interpret the ampersand (&) as a substitution variable. See [SET ERRORL\[OGGING\] {ON | OFF} \[TABLE \[schema.\]tablename\] \[TRUNCATE\] \[IDENTIFIER identifier\]](https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve040.htm#i2698945) for more information on setting the escape character.

SQL\*Plus interprets TTITLE in the old form if a valid new-form clause does not immediately follow the command name.

If you want to use CENTER with TTITLE and put more than one word on a line, you should use the new form of TTITLE. For more information see the [TTITLE](ch_twelve048.md) command.

Example

To use the old form of TTITLE to set a top title with a left-aligned date and right-aligned page number on one line followed by SALES DEPARTMENT on the next line and PERSONNEL REPORT on a third line, enter

```
TTITLE 'SALES DEPARTMENT|PERSONNEL REPORT'
```