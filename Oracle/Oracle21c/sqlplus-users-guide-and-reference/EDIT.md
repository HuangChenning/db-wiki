---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/EDIT.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
ED[IT] [file_name[.ext]]
```

where file\_name\[.ext\] represents the file you wish to edit (typically a script).

Invokes an operating system text editor on the contents of the specified file or on the contents of the buffer.

Enter EDIT with no filename to edit the contents of the SQL buffer with the operating system text editor.

Usage

If you omit the file extension, SQL\*Plus assumes the default command-file extension (normally SQL). For information on changing the default extension, see the SUFFIX variable of the SET command.

If you specify a filename, SQL\*Plus searches for the file in the directory set by ORACLE\_PATH. If SQL\*Plus cannot find the file in ORACLE\_PATH, or if ORACLE\_PATH is not set, it searches for the file in the current working directory. If SQL\*Plus cannot find the file in either directory, it creates a file with the specified name.

The substitution variable, \_EDITOR, contains the name of the text editor invoked by EDIT. You can change the text editor by changing the value of \_EDITOR. For information about changing the value of a substitution variable, see [DEFINE](DEFINE.md). EDIT attempts to run the default operating system editor if \_EDITOR is undefined.

EDIT places the contents of the SQL buffer in a file named AFIEDT.BUF by default (in your current working directory) and runs the text editor on the contents of the file. If the file AFIEDT.BUF already exists, it is overwritten with the contents of the buffer. You can change the default filename by using the SET EDITFILE command. For more information about setting a default filename for the EDIT command, see the EDITFILE variable of the SET command.

Note:

The default file, AFIEDT.BUF, may have a different name on some operating systems.

If you do not specify a filename and the buffer is empty, EDIT returns an error message.

In SQL\*Plus 9.0 and earlier versions on Windows, the command `EDIT *` opened a blank file after giving an invalid filename warning. In SQL\*Plus 10 and later versions on Windows, `EDIT *` gives an invalid filename warning and does not open a blank file. To retain the SQL\*Plus 9.0 behavior, enter the set command,

`SET SQLPLUSCOMPATIBILITY 9.0`

To leave the editing session and return to SQL\*Plus, terminate the editing session in the way customary for the text editor. When you leave the editor, SQL\*Plus loads the contents of the file into the buffer.

Note:

In Windows, if you use WordPad as your editor (\_EDITOR=write.exe), the buffer is not reloaded when you exit WordPad. In this case, use GET to reload the buffer.

Examples

To edit the file REPORT with the extension SQL using your operating system text editor, enter

```
EDIT REPORT
```