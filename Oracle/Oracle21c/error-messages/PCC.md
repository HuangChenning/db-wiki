---
title: Database Error Messages
book: Database Error Messages
doc_id: F30283-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/errmg/PCC.html
tags:
  - oracle
  - 21c
  - error-messages
---

PCC-02010: found end-of-file while scanning string literal

Cause: A string in a SQL statement, which should be delimited by single quotation marks, was not terminated properly.

Action: Check that all strings are delimited.

PCC-02011: found identifier greater than 128 characters (truncated)

Cause: The precompiler found an identifier that was too long.

Action: Shorten the identifier. SQL identifiers should be limited to 128 characters.

PCC-02012: did not find matching quote for char constant

Cause: A character constant with a single quotation mark was not terminated.

Action: Terminate the character constant.

PCC-02013: unknown escape sequence

Cause: The precompiler found an escape sequence that it could not process inside a string literal. This error can arise when multibyte character strings that can contain shift-in or shift-out escape sequences are used.

Action: Correct the string representation.

PCC-02014: Syntax error at line number, column number, file string:\\n

Cause: The precompiler detected an errorin C or embedded SQL syntax. This message is followd by a more specific error message.

Action: Correct the syntax error.

PCC-02015: unable to open include file

Cause: The precompiler could not open a header file that was specified using the #include preprocessor directive or the EXEC SQL INCLUDE statement. This can happen if the file specification is inaccurate or if read permission or read access rights on the file or on one or more of the directories in the path were not granted.

Action: Recheck that the file specification is correct, that the file exists, and that read permission has been granted so that the file can be read.

PCC-02016: Absolute path to included file, "string" exceeds the limit of number characters

Cause: The file name length specified exceeded the maximum length. Some operating systems have a maximum file name length.

Action: Use a file name of length less than or equal to the maximum platform specific file name length.

PCC-02017: unable to open output file

Cause: The precompiler could not open an output file. This could be a generated code output file(.c file) or a listing file. This message can result from many causes. For example: o) A pathname for a specified output file contains a non-exixtent directory. o) An operating-system error occured because the file system or disk is full. o) Write permission on the specified directory or directories in the path do not exist.

Action: Track down the cause of the error, as suggested above, and correct it.

PCC-02018: found end-of-file while scanning comment

Cause: A C comment either in C code or in an embedded SQL statement, was not terminated.

Action: Find the unterminated comment and terminate it with \*/.

PCC-02019: Preprocessor warning at line number, column number, file string:\\n

Cause: This message indicates that a warning condition occured as the precompiler was doing the preprocessor pass. A more specific warning message will follow this message.

Action: Correct the condition according to the action specified for the message that follows.

PCC-02020: Preprocessor error at line number, column number, file string:\\n

Cause: This message indicates that an error condition occured as the precompiler was in the preprocessing phase. A more specific error message will follow this message.

Action: Correct the error according to the action specified for the message that follows.

PCC-02021: Found newline while scanning string literal

Cause: A string constant contains a newline character, For example char x\[\] = "Hello world";

Action: Remove the newline character.

PCC-02022: Found end of file while scanning a SQL statement

Cause: The precompiler encountered an end of file while parsing an EXEC SQL statement.

Action: Add statement terminator(;) or complete the EXEC SQL statement.

PCC-02023: Found end of file while scanning a PL/SQL statement

Cause: The precompiler encountered an end of file while parsing a PL/SQL statement (EXEC SQL EXECUTE...).

Action: Complete the PL/SQL statement.

PCC-02035: CMD-LINE: CONFIG= option is invalid in a config file

Cause: A user configuration file inside a user configuration file cannot be specified. That is, nested configuration files cannot be nested.

Action: If there are nested configuration files, move the options from the nested files to the top levels.

PCC-02040: CMD-LINE: Option selected, but no value provided

Cause: An option on the command line was specified, but a value for it was not included. For example, the offending code might look like: proc iname=sample1.pc oname=

Action: Provide a value for the option.

PCC-02041: CMD-LINE: Option does not exist:

Cause: A non existent option on the command line was specified.

Action: See the Programmer's Guide to the Oracle Precompilers, Release 2.2 for a list of the valid command line options and their possible values.

PCC-02043: CMD-LINE: Option syntax is incorrect

Cause: A value for a command line option was incorrectly specified.

Action: See the Programmer's Guide to the Oracle Precompilers, Release 2.2 for the correct syntax for specifying command line option values.

PCC-02044: CMD-LINE: Illegal or out of range value for option:

Cause: A value specified for a command line option was not within the accepted range. For example,, the range for the MAXOPENCURSORS option is 5 to 256. If a value outside the range is specified, the message is triggered.

Action: See the Programmer's Guide to the Oracle Precompilers for the ranges that option values can take.

PCC-02045: CMD-LINE: Option is not unique:

Cause: An option name was partially specified on the command line that made it non unique. For example, % proc in=t.pc the "in" option can imply either the INAME or INCLUDE option.

Action: Provide sufficient characters on the command line to make the option name unique.

PCC-02046: CMD-LINE: Unable to open config file:

Cause: A non-existent user configuration file was specified on the command line with the config option.

Action: Provide a valid filename for the configuration file.

PCC-02047: CMD-LINE: Option is not allowed inline:

Cause: An option was entered inline that can only be entered on the command line or in a configuration file. For example, the offending code might look like EXEC ORACLE OPTION (NLS\_CHAR=name); The NLS\_CHAR option can only be entered on the command line or in a configuration file.

Action: Remove the option from the source file, and specify it on the command line.

PCC-02066: CMD-LINE: Could not find or could not open system config file

Cause: The system configuration file has a standard name (pmscfg.h) and a location that is operating system dependent. On UNIX systems, it is located in the ORACLE\_HOME/proc directory. If a file named pmscfg.h is not found in the standard location, this warning message is issued.

Action: Create a system configuration file in the standard location. The file can be empty. See also the operating system specific Oracle documentation.

PCC-02081: CMD-LINE: Unterminated option value list or value list was truncated.

Cause: An option that takes a list of values was entered. The value list did not have a closing parenthesis. This error may also occur if the list of values entered on a single line was too long and Pro\*C truncated it.

Action: Ensure that all value lists are terminated with a closing parenthesis. Split long value lists into individual entries.

PCC-02100: Unable to initialize PL/SQL

Cause: The precompiler connected to Oracle but could not invoke the PL/SQL engine. This error can result if an earlier release of Oracle7 is used without the Procedural Option.

Action: To use PL/SQL, upgrade to a more recent release of Oracle7.

PCC-02101: Unable to open input file

Cause: The precompiler could not open the input file. This is the.pc file specified in the INAME=option. This means that the file does not exist, that a directory was incorrectly specified in the pathname, or that the person running the precompiler does not have read permission for the file. This message could also result from operating-system errors. For example, an unmounted file system or disk I/O errors, could trigger this error.

Action: Check that permission to read the file exists and that the full pathname has been specified correctly. Check for operating- system problems. See also the operating system-specific Oracle documentation.

PCC-02102: Fatal error while doing C preprocessing

Cause: The precompiler issues this message after a more specific message.

Action: Correct the problem specified in the previous message or messages.

PCC-02103: Password:

Cause: The username was specified on the command line without a password. For example, proc sqlcheck=full iname=sample1.pc userid=scott

Action: Re-enter the command line, and include the password or specify the password when prompted.

PCC-02104: Unable to connect to Oracle

Cause: The precompiler could not connect to Oracle with the username, password, and, if applicable, database link that was supplied. Note that this is a precompiler message, not a runtime message. This means that the USERID option value, either on the command line or in a configuration file, was incorrect.

Action: Check that the username and password are current and correct. Run SQL\*DBA or SQL\*PLUS and verify that connection can be made using that username and password.

PCC-02105: Unable to open list file

Cause: The precompiler could not open the listing file. This message can result from many causes. For example, o) A pathname for a specified listing file contains a non-existent directory. o) An operating-system error occured because the file system or disk is full. o) Write permission on the specified directory has not been granted.

Action: Track down the cause of the error, as suggested above, and correct it.

PCC-02106: Userid only used when SQLCHECK = FULL, userid ignored.

Cause: The USERID option was specified on the command line, but SQLCHECK was not equal to FULL or SEMANTICS. The USERID has no effect, unless SQLCHECK=FULL or SQLCHECK=SEMANTICS.

Action: This is a warning message only.

PCC-02107: You may not specify PARSE = FULL when CODE = CPP

Cause: The PARSE=FULL and CODE=CPP options were both specified on the command line. The PARSE=FULL option invokes the C parser which does not understand any C++ constructs generated by the precompiler with CODE=CPP option.

Action: Set the PARSE option to either NONE or PARTIAL if the CODE=CPP option is specified.

PCC-02108: UNSAFE\_NULL=YES allowed if MODE=ORACLE and DBMS=V7 or V8

Cause: UNSAFE\_NULL=YES was specified on the command line, but but either the MODE was not ORACLE or the DBMS was not V7 or V8.

Action: Specify MODE=ORACLE and DBMS=V7 or V8 when using UNSAFE\_NULL=YES.

PCC-02109: SQLCHECK=NONE is no longer supported.. using SYNTAX

Cause: SQLCHECK=NONE was specified on the command line but is no longer a supported option. SQLCHECK=SYNTAX was used instead.

Action: This is a warning message only. To avoid this warning, specify SQLCHECK=SYNTAX or SQLCHECK=SEMANTICS.

PCC-02110: DBMS=V6\_CHAR is deprecated. Use CHAR\_MAP=VARCHAR2, DBMS=V7 instead

Cause: DBMS=V6\_CHAR was specified on the command line but is no longer a supported option. The options CHAR\_MAP=VARCHAR2 and DBMS=V7 were used instead.

Action: This is a warning message only. To avoid this warning, specify CHAR\_MAP=VARCHAR2 and, if required, DBMS=V7.

PCC-02111: CHAR\_MAP option ignored. Only CHAR\_MAP=VARCHAR2 allowed for DBMS=V6

Cause: DBMS=V6 was specified, and CHAR\_MAP was specified with a value other than VARCHAR2. The CHAR\_MAP value is ignored.

Action: This is a warning message only. To avoid this warning, specify a DBMS value other than DBMS=V6 or use CHAR\_MAP=VARCHAR2.

PCC-02112: OBJECTS option ignored. OBJECTS=YES is not allowed for DBMS=V6 or V7.

Cause: OBJECTS=YES was specified on the Pro\*C command line, but the DBMS option value was not valid.

Action: This is a warning message only. To avoid this warning for OBJECTS=YES, use DBMS=V8 or DBMS=NATIVE with a V8 database.

PCC-02113: DBMS=V6 no longer supported; using DBMS=NATIVE, CHAR\_MAP=VARCHAR2.

Cause: DBMS=V6 was specified on the command line, but is no longer a supported option value. The options DBMS=NATIVE and CHAR\_MAP=VARCHAR2 were used instead.

Action: Check your program to verify that you are not depending on any V6 behavior. Please refer to the Programmer's Guide to the Pro\*C/C++ Precompiler for effects of specifying DBMS=V6.

PCC-02114: Command line argument MODE=ANSI may not be used with DBMS=V6

Cause: The semantics of certain operations (such as character comparison) in Oracle version ^ are not 100% compliant with the ANSI/ISO SQL standards. When V6 semantics are requested, using the DBMS=V6 or DBMS=V6\_CHAR option, precompilation with MODE=ANSI is not permitted.

Action: Do not use ANSI mode with V6 options.

PCC-02115: Unable to open output file for writing

Cause: An attempt was made to precompile a header file where the output data file could not be opened (or created) for writing.

Action: Check for appropriate permissions on the directory and possibly file objects (if a data file already exists) to make sure that write permissions have been granted.

PCC-02116: You must specify a file extension using the HEADER option

Cause: An attempt was made to precompile a header file without specifying the name of the extension to use when creating the generated data file.

Action: Use the HEADER option to specify the name of a file extension to use when creating a data file for a precompiled header.

PCC-02117: Semantic checking disabled by TimesTen.

Cause: Semantic checking is not supported by TimesTen

Action: This is a warning message only.

PCC-02129: CMD-LINE: Client supplied static options table is invalid

Cause: This is an internal error message not usually issued.

Action: Call Oracle customer support.

PCC-02132: CMD-LINE: Could not allocate memory

Cause: This is an internal error message not usually issued.

Action: Call Oracle customer support.

PCC-02133: CMD-LINE: Error in string processing function

Cause: This is an internal error message not usually issued. It indicates that a C string function, such as strcpy or strlen, returned an error.

Action: Call Oracle customer support.

PCC-02134: CMD-LINE: Null option supplied

Cause: A zero length option was specified on the command line.

Action: Re-enter the command line with a valid option.

PCC-02135: CMD-LINE: User asked for help

Cause: This is a final message that the precompiler issues when information about the command line options has been requested. For example, if the command proc? is issued to get a list of current default values for the command line options, this message appears at the end of the list.

Action: No action required.

PCC-02138: CMD-LINE: Internal consistency error

Cause: This is an internal message for program exceptions. An unexpected condition was encountered by the command-line processor and a consistency check failed. Some possible causes of this message include: --invalid command-line options --memory corruption

Action: Report this error to Worldwide Support after gathering the following information: --the events that led to the error --the attempted operations that led to the error --any unusual circumstances prior to this error

PCC-02144: CMD-LINE: Blank characters are not allowed on either side of an equal sign (=)

Cause: An equal sign (=) was either immediately preceded or followed by a blank character.

Action: Precompile your program again without blank characters on either side of any equal sign (=) on the command line.

PCC-02146: CMD-LINE: value of option too long

Cause: The length of the user option exceeded 1023 bytes

Action: Reduce the length of the user option

PCC-02150: Error at line number, column number in file string

Cause: An error was encounter at the given location.

Action: Check the named source file and correct the error using the additional information which follows this error message.

PCC-02151: Line number column number file string:

Cause: An error was encounter at the given location.

Action: Check the listed source file and correct the error using the additional information which follows this error message.

PCC-02152: Unable to open file string to display or list the source line number

Cause: The file contains an error, but could not be reopened to list or display the incorrect line.

Action: Check that the file is intact and it has read permission. Then rerun the operation.

PCC-02153: Open file: string

Cause: A new source file was opened while producing the list file.

Action: No action required; this is an informational message.

PCC-02154: Close file: string

Cause: A source file was closed while producing the list file.

Action: No action required; this is an informational message.

PCC-02200: found unrecognized punctuation sequence

Cause: The error indicates that the precompiler parser encountered a badly-formed identifier or keyword.

Action: Correct the syntax.

PCC-02201: Found syntax error

Cause: This general message precedes one or more specific messages that detail the nature of the error.

Action: No action required. Correct the errors diagnosed in the following message(s).

PCC-02202: No typedef name was given

Cause: The precompiler parser encountered a typedef statement that had no name after the type specification. For example, typedef int;

Action: Correct the syntax

PCC-02203: found end of file when not expected

Cause: The parser can emit this message when a general syntax error occurs, for example, an unmatched '{' or '('.

Action: Correct the syntax.

PCC-02204: EXEC SQL INCLUDE not permitted from within an included file

Cause: EXEC SQL INCLUDE statements cannot be nested. Also, EXEC SQL INCLUDE statement cannot be put inside a file that is included using the #include preprocessor command.

Action: Recode the program so that the nested include statement is not required.

PCC-02205: Parser error at line number, column number, file string:\\n

Cause: The precompiler parser encountered a syntax error, either in C code or in SQL code. A more specific message should follow.

Action: No action required for this message. Take the appropriate action for any following messages.

PCC-02206: Host variables are not permitted within a DDL statement

Cause: A Data Definition Language statement cannot use host variables. For example, the statement CREATE TABLE:table\_name (c1 char(10)); is illegal, because the name of the table in a CREATE TABLE statement cannot be represented using host variable.

Action: Use dynamic SQL to create the names of database objects (tables, views, columns, etc.) at runtime. See the Programmer's Guide to the Oracle Precompilers, Release2.2 for information about dynamic SQL.

PCC-02207: Invalid macro name

Cause: The precompiler parser encountered a #define directive that had no macro name associated with it. For example, #define

Action: Correct the syntax.

PCC-02208: No filename specified in #include statement

Cause: The precompiler parser encountered a #include directive that had no filename associated with it. For example, #include

Action: Specify appropriate filename with the #include directive, or correct the syntax.

PCC-02209: Macro invocation has incorrect number of arguments

Cause: A macro invocation in the source does not have the same number of arguments as the macro definition in the #define line.

Action: Correct the macro reference or the macro definition.

PCC-02210: C++ punctuation sequences are not permitted

Cause: C++ punctuation sequences are not supported by the ProC/C++ precompiler.

Action: Rewrite your C++ code without using punctuation sequences and precompile it again.

PCC-02301: cannot reopen input file for reading

Cause: The semantic analysis phase of the precompiler could not reopen the input file to generate the output code.

Action: Check that the input file and it's directory protection and priveleges do not change during precompilation.

PCC-02302: cannot open code generation output file "string"

Cause: Pro\*C was unable to open one or both temporary files required for code generation. The user executing the precompiler must have write permission (and/or the appropriate privileges) on the current directory.

Action: Check that permission exists to create files in the the directory where you precompile.

PCC-02303: cannot open include file

Cause: The precompiler was not able to open a header file specified using the #INCLUDE preprocessor directive or the EXEC SQL INCLUDE statement. This can happen if the file specification is inaccurate or if read permission or read-access rights on the file or on one or more of the directories in the path have not been granted.

Action: Recheck that the file specification is correct, that the file exists, and that read permission has been granted so that the file can be read.

PCC-02304: invalid declaration of C function

Cause: A C function using invalid syntax was declared.

Action: Consult a C programming manual and correct the declaration.

PCC-02305: illegal mixing of new and old style C function declarations

Cause: All C functions using either the traditional style (K&R style) function declarations or the new (ANSI) style must be declared; the two styles cannot be mixed.

Action: Adopt a consist declaration style for functions.

PCC-02306: illegal name of C function

Cause: A C function was declared with a name that is not a legal C identifier.

Action: Use legal C identifiers for all function names.

PCC-02307: void can only be used when single parameter

Cause: A function can be declared or defined using the following syntax: int func1(void) to indicate that the function has no parameters. void can be used only once in this case.

Action: Remove the extra voids in the function definition or declaration.

PCC-02308: identifier required in this function declaration

Cause: A function definition written in ANSI C must have both the name and the type for all parameters.

Action: Rewrite the function definition so that it contains the name of each parameter.

PCC-02309: illegal formal parameter declaration

Cause: A formal parameter to a function was specified without giving its type.

Action: Rewrite the function declaration and include types of all parameters in function declarations.

PCC-02310: formal parameter VARCHARs should be declared as pointers

Cause: Many C compilers allow structures to be passed to and returned from functions. Although a VARCHAR is implemented as a C struct, VARCHARs must be passed to a function as pointers.

Action: Take the address of a VARCHAR when it is passed to a function. See the example in the section "Referencing VARCHAR Variables" in the Programmer's Guide to the Oracle Precompilers.

PCC-02311: cannot have VARCHAR bit fields

Cause: Host variables cannot contain bit fields.

Action: Recode the application to remove the bit fields.

PCC-02312: arrays of VARCHAR greater than 2 dimensions not allowed

Cause: A VARCHAR variable having more that 2 dimensions was declared. Multidimensional arrays are not supported as host variables.

Action: Recode the application to remove multidimensional array usage.

PCC-02313: malformed VARCHAR declaration - missing length

Cause: When a VARCHAR is declared, a length specification is mandatory. For example, the following VARCHAR declaration is meaningless, hence illegal: VARCHAR v1\[\];

Action: Specify the length for each declared VARCHAR.

PCC-02314: cannot evaluate constant sizeof expression

Cause: A SIZEOF operator was used where a precompiler expression was expected. For example, as the length of a varchar.

Action: Eliminate the SIZEOF operator in this instance.

PCC-02315: cannot evaluate expression as constant

Cause: The specified expression does not evaluate to a constant. Such expressions are required, for example, as the length of a VARCHAR.

Action: Replace the expression with one that does evaluate to a constant integer.

PCC-02316: illegal operator in constant expression

Cause: A non-arithmetic operator was present in a constant expression.

Action: Rewrite the expression to eliminate the non-arithmetic operator.

PCC-02317: illegal cast type expression

Cause: An illegal cast is present in the expression.

Action: Remove the illegal cast.

PCC-02318: missing type expression

Cause: The specified expression is missing the declaration of a type.

Action: Specify a type for the expression.

PCC-02319: expression type does not match usage

Cause: The type of a variable does not match is usage. For example, in dynamic SQL, a host variable containing the text of a SQL statement must be declared as a C character type or be equivalenced to the SQL type STRING.

Action: Remove the declaration.

PCC-02320: arithmetic expression does not have correct operand types

Cause: The arithmetic expression must be specified with integral types.

Action: Rewrite the expression using integral types.

PCC-02321: only subtraction between two pointers is permitted

Cause: Pointer values cannot be added, multiplied, or divided. The only arithmetic operation permitted with pointers is subtraction.

Action: Recode to avoid this error message.

PCC-02322: found undefined identifier

Cause: An identifier used in a SQL statement was not defined. For example, a cursor name was referenced that had not been declared, or in a DECLARE CURSOR statement, a statement name was used that had not been PREPAREd.

Action: Check that all SQL identifiers, such as cursor names and statement names, have been defined before use. Provide a declaration for the variable and/or its type identifier.

PCC-02323: found typedef name used in an expression (expecting a value)

Cause: The name of a typedef was found where a variable was expected.

Action: Rewrite the expression and remove the reference to the typedef.

PCC-02324: found variable name used as a typedef name

Cause: The name of a variable was found where a typedef was expected.

Action: Rewrite the expression and specify the correct typedef reference.

PCC-02325: illegal indirection operation

Cause: An attempt was made to use a non-pointer type as a pointer.

Action: Rewrite the expression.

PCC-02326: illegal structure reference operation

Cause: A structure component using invalid syntax was referenced. For example, a -> operator was used instead of a required \`.' operator.

Action: Correct the invalid reference.

PCC-02327: struct or struct pointer required

Cause: A scalar host variable was used in a context where a structure (or its pointer) is required.

Action: Make the host variable a structure or add more scalar host variables to satisfy the SQL syntax requirements.

PCC-02328: undefined struct member

Cause: A structure component was referenced that was not declared as part of the structure.

Action: Redefine the structure member.

PCC-02329: found reference to undeclared function

Cause: A function was referenced that was not declared. All function references must be declared.

Action: Declare the function.

PCC-02330: expecting an expression of integer type

Cause: The expression does not evaluate to an integer. For example, a SQL FOR expression must evaluate to an integral type.

Action: Rewrite the expression.

PCC-02331: undefined SQL identifier

Cause: All SQL identifiers must be declared before they are used. This message can result when a CURSOR or STATEMENT is not declared (defined) before being referenced.

Action: Define the SQL identifier before it is used.

PCC-02332: attempted to redefine SQL identifier

Cause: A SQL identifier (such as a cursor name) can be defined only once.

Action: Do not redefine the SQL identifier.Use a different name.

PCC-02333: SQL identifier was not declared as a statement

Cause: A SQL statement identifier was referenced in a DECLARE... CURSOR statement that was not PREPAREd.

Action: Check that all SQL statement names have been declared. Remember that SQL statement names are identifiers, not variables, and that they are local to the precompilation unit.

PCC-02334: SQL identifier was not declared as a cursor

Cause: A cursor name was used in an OPEN, FETCH, or CLOSE statement that had not been DECLAREd.

Action: Check that all SQL cursor names have been declared. Remember that cursors are identifiers, not variables, and that they are local to the precompilation unit.

PCC-02335: body of cursor must name statement identifier

Cause: In a Dynamic SQL Method 4 application, the DECLARE... CURSOR statement must name a statement identifier that has been PREPAREd in a preceding statement. The PREPARE statement must physically (not logically) precede the DECLARE command.

Action: This error message is followed by another message that gives the line and column of the reference to the statement. Recode the application.

PCC-02336: host variable expression has invalid type

Cause: The host variable was declared using a C type that is not permitted as a host variable. See the Programmer's Guide to the Oracle Precompilers for a list of the permissible C types for host variables.

Action: Use a permissible host variable type.

PCC-02337: cannot declare multi-dimensioned array for this type

Cause: Host variable arrays of scalars with more than 1 dimension cannot be declared.The only host variables allowed to be multi-dimensioned are CHAR and VARCHAR.

Action: Rewrite the variable declaration.

PCC-02338: structure contains a nested struct or union

Cause: A structure used as a host variable may not have structures or unions nested within it.

Action: Rewrite the variable declaration.

PCC-02339: host variables cannot be of union types

Cause: A C union as a host variable cannot be used.

Action: This error message is followed by another message that gives the line and column of the reference to the illegal union. Recode, using a struct or individual scalar host variables.

PCC-02340: structure contains a bit field

Cause: Bit fields are not allowed in host variables because they are meaningless for database DML operations.

Action: This error message is followed by another message that gives the line and column of the reference to the offending host variable. Recode the application.

PCC-02341: host variable has illegal type

Cause: A host variable has an unpermitted type (i.e.; enum, void, etc).

Action: Rewrite the host variable declaration, using a permissible host variable type.

PCC-02342: using WHERE CURRENT OF on cursor defined without FOR UPDATE clause

Cause: When MODE=Oracle, a cursor defined with a WHERE CURRENT OF clause must also have a FOR UPDATE clause.

Action: Rewrite the cursor definition.

PCC-02343: body of cursor must be a query expression

Cause: A cursor definition must be a SELECT statement.

Action: Rewrite the cursor definition.

PCC-02344: Host variable array size mismatch. Using minimum: number

Cause: Host variable arrays in a single statement should all be of equal size.

Action: Redefine the bind variable array lengths to all be the same size.

PCC-02345: SQLCHECK=SEMANTICS must be given when embedded PL/SQL blocks are used

Cause: Embedded PL/SQL blocks require that the command-line flag SQLCHECK=SEMANTICS is used.

Action: Use the SQLCHECK=SEMANTICS option. This also requires that the USERID connect option be given.

PCC-02346: PL/SQL found semantic errors

Cause: A database entity, such as a table or column name, was referenced, that does not exist. This is a compile time error, not a runtime error.

Action: Check that all referenced objects in PL/SQL statements actually exist and that the necessary access permission on them have been granted.

PCC-02347: PL/SQL found syntax errors

Cause: A PL/SQL statement was used illegally.

Action: Check the PL/SQL User's Guide and Reference for the correct syntax.

PCC-02348: indicators are not allowed in EXEC IAF statements

Cause: Indicator variables associated with host variables cannot be used in EXECIAF statements such as GET and PUT in a user exit.

Action: Eliminate the indicator variabls. If feasible (for example with Forms V4), use EXEC TOOLS statements, which do allow indicator variables. See the Programmer's Guide to the Oracle Precompilers for more information of EXECIAF and EXEC TOOLS statements.

PCC-02349: precision must be specified for this type

Cause: In a VAR or TYPE statement, certain Oracle types require that the precision be specified. For example, VARCHAR2 or CHAR.

Action: Indicate the precision.

PCC-02350: cannot equivalence this SQL type

Cause: Datatype or variable equivalencing to the datatypes NUMBER or DECIMAL cannot be used. See the "Datatype Equivalencing" section in the Programmer's Guide to the Oracle Precompilers for more information.

Action: Use the appropriate datatype for the application.

PCC-02351: illegal datatype equivalencing operation

Cause: The datatype specified could not be equivalenced, or the syntax was incorrect in the VAR or TYPE statement.

Action: See the Programmer's Guide to the Oracle Precompilers for a list of the datatypes that can be equivalenced and the correct syntax of the VAR or TYPE statement.

PCC-02352: out of bounds bind position from PL/SQL

Cause: PL/SQL requested a bind position that does not exist.

Action: Contact ORACLE customer support.

PCC-02353: Semantic error at line number, column number, file string:\\n

Cause: This error message precedes a more specific error message.

Action: No action required. Correct the error(s) reported in the following message(s).

PCC-02354: A file included with #include may not contain SQL statements

Cause: The Pro\*C Precompiler reads header files referenced in #INCLUDE directives and uses the values defined in them. But the precompiler never generates code using statements in header files, so use of SQL statements in these files is illegal.

Action: Move the SQL statement(s) into the main body of the application or use EXEC SQL INCLUDE to check that the included file is precompiled.

PCC-02355: Invalid or obsolete option, ignored

Cause: A command-line option that is not used in Pro\*C Release 2.0 was specified. For example, the option AREASIZE is no longer valid with precompilers used with the Oracle7 Server.

Action: No action required. This is an informational message.

PCC-02356: Warning at line number, column number, file string:\\n

Cause: This is a generic warning message. It precedes a more specific warning.

Action: No action required. Correct the error(s) indicated in the following message(s).

PCC-02357: Function calls may not be used as host variable expressions

Cause: Only objects that are lvalues (that resolve to an address) can be host variables. Because a function call is not an lvalue, one cannot be used in place of a host variable.

Action: Recode the application.

PCC-02358: Identifier following ARRAYLEN must be the name of an array

Cause: A declared array must be specified as the argument for an ARRAYLEN statement. Declare the array textually before the ARRAYLEN statement. See the Programmer's Guide to the Oracle Precompilers for the syntax of the ARRAYLEN statement.

Action: Correct the statement, specifying a host array as the argument.

PCC-02359: Identifier specifying ARRAYLEN must be a 4-byte integer

Cause: The expression that specifies the ARRAYLEN dimension must evaluate to an integer. For example, the statement EXEC SQL ARRAYLEN my\_array(1,3) cannot be parsed.

Action: Correct the statement, using an integral dimesnsion.

PCC-02360: This array type is invalid for use with ARRAYLEN statement

Cause: Arrays of some host variables types are not allowed and hence also cannot be used in ARRAYLEN statements. VARCHAR and DATE are examples.

Action: Specify an array with a datatype that can be used in host arrays.

PCC-02361: Use of ARRAYLEN with SQL bind arrays is ignored

Cause: ARRAYLEN is only valid with arrays that can be bound in PL/SQL blocks.

Action: Use an appropriate array type.

PCC-02362: Host variable not declared within SQL DECLARE section

Cause: When MODE=ANSI is specified at precompile time, all host variables must be declared inside Declare Sections. Remember that MODE=ANSI refers to ANSI SQL, not ANSI C.

Action: Add the EXEC SQL BEGIN DECLARE SECTION... EXEC SQL END DECLARE SECTION statements around all host variable declarations.

PCC-02363: Indicator variable must be a structure

Cause: If a host variable is a structure, the associated indicator variable must also be a structure.

Action: Recode the application to create an indicator variable as a structure.

PCC-02364: Host struct and its indicator must have the same number of fields

Cause: When a structure containing indicator variables is declared and associated with a host structure, the indicator structure must contain the same number of fields as the host structure. This is so even when some of the indicators will not be used or even when it would not make sense to do so (for fields constrained as NON NULL, for example).

Action: Redeclare the indicator variable with the correct number of fields.

PCC-02365: Indicator array size cannot be smaller than host array size

Cause: An indicator array must have dimension greater than or equal to the corresponding host variable array dimension.

Action: Change the dimension of the indicator array.

PCC-02366: Command line argument MODE=ANSI may not be used with DBMS=V6

Cause: The semantics of certain operations (such as character comparison) in Oracle version ^ are not 100% compliant with the ANSI/ISO SQL standards. When V6 semantics are requested, using the DBMS=V6 or DBMS=V6\_CHAR option, precompilation with MODE=ANSI is not permitted.

Action: Do not use ANSI mode with V6 options.

PCC-02367: This indicator variable must be declared as type short

Cause: An indicator for a host variable of this type must have the C type short. An array of such indicators must be an array of shorts.

Action: Declare the indicator variable or indicator array as type short.

PCC-02368: An EXEC TOOLS host variable context name is not type char

Cause: If a host variable is used to define a context name in an EXEC TOOLS GET CONTEXT or EXEC TOOLS SET CONTEXT statement, that host variable must be of a character type.

Action: Redeclare the context name to a host variable of a char type.

PCC-02369: An EXEC TOOLS host pointer variable is not a pointer

Cause: The host variable specifying an EXEC TOOLS context must be a pointer type.

Action: Redeclare the variable, making sure that it is a pointer.

PCC-02370: An EXEC TOOLS MESSAGE host variable is not type char

Cause: f a host variable is used to define a context name in an EXEC TOOLS GET CONTEXT or EXEC TOOLS SET CONTEXT statement, that host variable must be of a character type.

Action: Declare the message to a host variable of a char type.

PCC-02371: Illegal FOR clause

Cause: The argument of a FOR clause must be specified as an integer or as an identifier containing an integer.

Action: Rewrite the FOR clause.

PCC-02372: FOR clause not allowed in SELECT statement

Cause: A SQL statement containing a SELECT command cannot contain a FOR clause. The meaning of such a statement would be unclear.

Action: Rephrase the SELECT statement, removing the FOR clause.

PCC-02373: Invalid declaration in EXEC SQL DECLARE section

Cause: An improper declaration was placed in a Declare Section. This message is usually caused by including an EXEC SQL TYPE or EXEC SQL VAR declaration in a Declare Section.

Action: Move the declaration outside of the SQL DECLARE section.

PCC-02374: SQLCHECK value exceeds command line value

Cause: The value given to the SQLCHECK option in an EXEC ORACLE statement in a program was greater than the value given either on the command line or greater than the default value if no SQLCHECK option was given on the command line. The order of the option values is SEMANTICS>SYNTAX>NONE. When this warning message is issued, the original value of SQLCHECK (the default or the command-line value) stays in effect.

Action: Remove or recode the EXEC Oracle option(s) in the.pc source file to avoid this warning message.

PCC-02375: SQL statement found outside the body of a function

Cause: A SQL statement other than a declarative, datatype equivalence or WHENEVER statement was found outside the body of a function when PARSE=FULL.

Action: Move the SQL statement inside the body of a function.

PCC-02376: You may not declare SQLCODE when DEF\_SQLCODE = TRUE

Cause: The DEF\_SQLCODE option may not be specified if a SQLCODE declaration already explicitely appears in the program.

Action: Remove the SQLCODE declaration from the program or specify DEF\_SQLCODE=NO (the default).

PCC-02377: Arrays of implicit varchars are not permitted

Cause: An array of implicit VARCHARS was declared when HOST\_VARCHAR=TRUE.

Action: Rewrite the implicit VARCHAR declaration without using arrays.

PCC-02378: Invalid type for National Language character variable

Cause: A variable declared as a National Language character using the NLS\_CHAR option was not declared as a char or implicit VARCHAR.

Action: Declare the variable as a char or implicit VARCHAR or do not specify using the NLS\_CHAR option.

PCC-02379: Cannot equivalence National Language character variables

Cause: A National Language character variable (specified using the NLS\_CHAR option) has undergone datatype equivalencing using either the EXEC SQL VAR or TYPE statements.

Action: Do not equivalence National Language character variables.

PCC-02380: Cannot specify a connect mode when altering a user password

Cause: An attempt was made to connect in either SYSOPER or SYSDBA mode while at the same time trying to change passwords using the ALTER AUTHORIZATION clause in the same CONNECT statement.

Action: Changing passwords while connecting in SYSOPER or SYSDBA mode is prohibited. Rewrite the connect statement by either removing the ALTER AUTHORIZATION cluase or the CONNECT MODE clause.

PCC-02382: You must specify MODE=ANSI when using NLS\_LOCAL=YES

Cause: NLS\_CHAR was used to specify NLS multi-byte character variables without specifying MODE=ANSI.

Action: Specify MODE=ANSI on the command line when using NLS\_LOCAL=TRUE.

PCC-02383: Expecting an expression of type OCIExtProcContext

Cause: The type of the bind variable given in a REGISTER CONNECT USING statement was not (pointer to) OCIExtProcContext.

Action: Declare a variable having type (pointer to) OCIExtProcContext and use it in the REGISTER CONNECT USING statement.

PCC-02384: Missing array length specifier

Cause: An array declaration was given without an array length specifier.

Action: Provide the length for the array declaration.

PCC-02385: CHAR\_MAP disallowed when using NLS\_CHAR and NLS\_LOCAL=TRUE

Cause: The CHAR\_MAP option was specified while indicating which host variables are to be treated by the precompiler as NLS multi-byte character variables. This mapping cannot be performed with the option NLS\_LOCAL=TRUE. This error also occurs when DBMS=V6 is used in conjunction with NLS\_CHAR and NLS\_LOCAL=TRUE.

Action: Remove either the CHAR\_MAP option or set NLS\_LOCAL=FALSE. Ensure that DBMS is not set to V6.

PCC-02386: Use of the AT clause is not permitted here

Cause: An explicit AT clause was used with an ALLOCATE statement or a FETCH/CLOSE statement also using a SQL\_CURSOR declaration.

Action: Remove the AT clause.

PCC-02387: Expecting an expression of type sql\_cursor

Cause: A host bind variable was used in an ALLOCATE, FETCH or CLOSE statement that was not declared as a result set SQL\_CURSOR.

Action: Declare the variable to be of type sql\_cursor.

PCC-02388: Arrays not allowed in FROM/WHERE clause of SELECT statement

Cause: A host array was used in the WHERE clause of a SELECT-INTO statement.

Action: Rewrite the SELECT statement without using arrays or use a cursor.

PCC-02389: Arrays not allowed as input bind variables in SELECT list

Cause: A host array was used in the SELECT list of a SELECT-INTO statement.

Action: Rewrite the SELECT statement without using arrays in SELECT list.

PCC-02390: No EXEC SQL CONTEXT USE statement encountered

Cause: No EXEC SQL CONTEXT USE statement was encountered and the option threads=yes was requested.

Action: Ensure that the necessary context variable (of type sql\_context) has been declared and that has been ALLOCATEd and USEd prior to any executable SQL statements.

PCC-02391: Runtime context variable not of correct type

Cause: The host variable in a EXEC SQL CONTEXT USE statement or in the RETURNING clause of a REGISTER CONNECT statement was not declared to be of type SQL\_CONTEXT.

Action: Declare the runtime context variable to be of type SQL\_CONTEXT.

PCC-02392: You are already in an EXEC SQL DECLARE SECTION

Cause: A SQL DECLARE SECTION appears nested inside another one.

Action: Do not nest DECLARE SECTIONS. Remove any nested inner ones.

PCC-02393: SQL statement found inside an EXEC SQL DECLARE SECTION

Cause: An executable SQL statement appears inside a DECLARE SECTION.

Action: Move the SQL statement into the body of a function.

PCC-02394: Input file name and output filename are identical

Cause: The values of INAME and ONAME are the same or the default output filename is the same as that specified by ONAME.

Action: Use ONAME to specify a different filename for the output file.

PCC-02395: Using arrays of structs requires that the struct be named

Cause: An array of some unnamed struct was used as a host variable. When using arrays of structs, the struct requires a name or tag.

Action: Provide a name for the struct.

PCC-02396: Illegal use of arrays inside an array of structs

Cause: An array of a struct that contained arrays of scalars or two-dimensional char or VARCHAR fields was used as a host variable.

Action: Rewrite the struct so that there are no scalar arrays or two-dimensional char or VARCHAR fields.

PCC-02397: VARCHAR declarations not permitted in #include file

Cause: A VARCHAR declaration was found in a file included using a #include form.

Action: Use the EXEC SQL INCLUDE form to include files with VARCHAR declarations instead.

PCC-02398: Indicator ignored in this statement for this type

Cause: An indicator variable was used in a host/indicator variable pair for some type in a statement that did not require or need one. Typically, indicator variables are not used in ALLOCATE and FREE statements for types other than object or collection types. They are also not used in OBJECT CREATE/DEREF statements for REF types.

Action: Remove the use of the indicator for the type in the specified statement. It will be ignored otherwise.

PCC-02399: Illegal CHAR\_MAP option value for DBMS=V6. Option ignored.

Cause: A CHAR\_MAP option other than CHAR\_MAP=VARCHAR2 was specified inline. Since DBMS=V6, this option is ignored for a character or string variable in the offending statement.

Action: Either set DBMS to something other than V6, or specify CHAR\_MAP=VARCHAR2.

PCC-02400: This host variable must be declared as a pointer type

Cause: The specified host variable was not declared as a pointer type.

Action: Declare the host variable to be a pointer type.

PCC-02401: Host variable arrays of this type are currently not supported

Cause: Host variable arrays of the specified type are not supported.

Action: Rewrite your program so that there are no arrays of this type.

PCC-02402: Pro\*C option OBJECTS=YES is required when using the object cache

Cause: The object cache will be used for this host variable, but OBJECTS=NO was specified on the Pro\*C command line.

Action: Specify OBJECTS=YES on the Pro\*C command line when using the object cache.

PCC-02403: Invalid indicator variable type for this host variable

Cause: The type of the indicator variable is not appropriate for the specified host variable.

Action: Change the type of the indicator variable to a valid type. Refer to the "Programmer's Guide to the ORACLE Pro\*C/C++ Precompiler" for a discussion of appropriate indicator variable declarations.

PCC-02404: This indicator variable must be declared as a pointer type

Cause: The specified indicator variable was not declared as pointer type.

Action: Declare the indicator variable to be a pointer type.

PCC-02405: Variable is of undefined type

Cause: No declaration was found for the type identifier of the variable.

Action: Provide a valid declaration for the type of the host variable. If using objects in your program, check that the OTT-generated header for the object type was #included and that the typefile was specified in the INTYPE option on the Pro\*C command line.

PCC-02406: Expecting the form 'RETURN\[ING\] REF INTO:ref' only

Cause: When using the RETURNING clause in an OBJECT CREATE statement, only a single 'REF INTO:host variable' is expected. This error occurs if the expression list to which REF belongs is greater than one or if there are more than one host variables supplied in the into list.

Action: Rewrite the RETURNING clause as per the given specification.

PCC-02407: Object and REF types do not match

Cause: In an OBJECT CREATE or DEREF statement, the types of the given Object and its associated REF do not match.

Action: Make sure that the Object and its REF have the same type. The type information is generated by OTT and should appear in the header file which OTT creates.

PCC-02408: Expecting an expression of some Object type

Cause: The expression is not an Object type. For example, many host variable expressions in the Navigational statements require that the variable be declared of some Object type.

Action: Rewrite the expression or declare the variable to be an Object.

PCC-02409: Expecting an expression of some REF type

Cause: The expression is not a REF type. For example, some host variables in the Navigational CREATE and DEREF statements are required to be declared of some REF type.

Action: Rewrite the expression or declare the variable to be a REF.

PCC-02410: Expecting an expression of some Collection type.

Cause: The expression is not a Collection type. A VARRAY or Nested Table object was expected, but the given host variable did not resolve to a valid Collection type.

Action: Check that the OTT-generated header for the Collection type was properly #included in the Pro\*C/C++ program and that the typefile was specified in the INTYPE option on the Pro\*C/C++ command line.

PCC-02411: Invalid type for INDICATOR descriptor item host variable

Cause: The type of the host variable paired with the INDICATOR descriptor item was invalid. The only permissable types for the INDICATOR item are a signed 2 byte numeric type or an indicator struct generated by the Object Type Translator for a user defined object type.

Action: Either replace the INDICATOR host variable with a valid one having an acceptable type or redeclare the existing host variable to be of a valid type.

PCC-02412: FOR clause not permitted in OBJECT GET or SET statement

Cause: An explicit FOR clause was used in an OBJECT GET or OBJECT SET statement. Use of the FOR clause is illegal for these statements.

Action: Remove the FOR clause.

PCC-02413: Number of attributes does not match number of host variables

Cause: The number of attributes supplied in the attribute list of an OBJECT SET of GET statement does not match the total number of host variables also supplied in that statement.

Action: Either remove some attributes or remove some host variables from the statement in order to make the total count for each the same.

PCC-02414: This attribute does not exist in the specified Object

Cause: An attribute given in the attribute list of an OBJECT SET or GET statement is not a member of the specified object in that statement.

Action: Remove the attribute from the list.

PCC-02415: Cannot manipulate Object attributes in an OBJECT GET or SET

Cause: An attempt was made to either GET or SET an attribute of an Object that itself was an Object or REF type.

Action: Remove the attribute from the attribute list in the statement.

PCC-02416: The Object in an OBJECT GET or SET must not be an array

Cause: The Object specified in an OBJECT GET or SET statement is an array which is illegal.

Action: Redeclare the Object so that it is not an array or subscript the Object so that only a single element of the Object array is specified.

PCC-02417: Illegal type conversion between attribute and host variable

Cause: An illegal type conversion was attempted in a Navigational GET or SET statement between the type of the Attribute and the type of the Host Variable.

Action: Change the type of either the Attribute or the Host Variable.

PCC-02418: Array size mismatch between Object and REF host variables

Cause: The array sizes of the Object and REF variables in an OBJECT CREATE or DEREF do not match.

Action: Adjust the array dimensions of the two host variables so that they are equal to one another.

PCC-02419: Host variable arrays not allowed in an OBJECT SET or GET

Cause: An array was found in the host variable list of an OBJECT SET or GET statement.

Action: Only scalars are allowed (except for single dimensioned char or varchar variables) in the host variable list of an OBJECT SET or GET. Make sure to use only scalars in these statements.

PCC-02420: Incomplete (or missing) type specification

Cause: An incomplete or perhaps missing type specification was given when declaring a host variable used in some SQL statement.

Action: Provide a complete type definition when declaring host variables intended for use inside any SQL statements.

PCC-02421: This host variable requires the use of an indicator variable

Cause: No indicator variable was provided (or matched) with a specific host variable where one was explicitely required.

Action: Provide an indicator variable for use with the specified host variable in the given SQL statement.

PCC-02422: Invalid value specified for the given context option

Cause: An illegal value was given for the specified runtime context option in the CONTEXT option OPTION SET (or GET) statement.

Action: Use a valid option value in the statement for the specified option being manipulated by the statement.

PCC-02423: Host variable has an invalid type for this option value

Cause: The type of the host variable corresponding to a specific option value in a CONTEXT option OPTION SET (or GET) statement is invalid for that particular value.

Action: Use a type suitable for the specific value being manipulated.

PCC-02424: The number of values and host variables does not match

Cause: There is a mismatch between the number of values specified and the number of valid host variables given in a CONTEXT option OPTION SET (or GET) statement.

Action: Use the same number of host variables as there are values given in that particular statement.

PCC-02425: An indicator variable is not required with this attribute

Cause: In a LOB or Collection DESCRIBE, an Indicator Variable was used with a Host Variable when retrieving a LOB attribute that doesn't require one.

Action: Remove the Indicator Variable.

PCC-02426: Incompatible LOB types

Cause: A LOB operation was attempted between LOBs whose types were not compatible. For example, When ASSIGNing one LOB to another, both LOBs must be of the same type. If they are not, this error results.

Action: Correct the LOB operation by having it function between LOBs of the same type. This may require a redeclaration of one of the LOBs used in the LOB statement performing the specified operation.

PCC-02427: Expression is not of the correct character string type

Cause: The given host variable expression was not declared to be of the required character type. In this case, one of several possible character types would have been accepted. However, the host variable type did not match any of them.

Action: Redeclare the problematic host variable, using one of the permitted character types.

PCC-02428: Buffer type is incompatible with LOB type

Cause: This error can occur in either of the following situations 1. An attempt to READ from a LOB into a buffer whose type was not compatible with the LOB type. 2. An attempt to WRITE a buffer into a LOB whose type was not compatible with the buffer type.

Action: Either the LOB type or the buffer type needs to be changed so that the LOB and buffer types become compatible for the specified operation.

PCC-02429: Expecting an expression of some internal LOB type

Cause: The given host variable was not declared to be an Internal LOB. BLOB, CLOB or NCLOB would have been accepted, however, the type of the host variable did not match any of these.

Action: Redeclare the host variable using one of the Internal LOB types.

PCC-02430: Expecting an expression of some arbitrary LOB type

Cause: The given host variable was not declared to be any type of LOB, Internal or External. In addition to any Internal LOB type, BFILE would also have been accepted, however, the type of the host variable did not match any of these.

Action: Redeclare the host variable using any of the LOB types, Internal or External.

PCC-02431: Expecting an expression of type external LOB (BFILE)

Cause: The given host variable was not declared to be an External LOB. Only BFILE would have been accepted in this case.

Action: Redeclare the host variable using an External LOB type (BFILE).

PCC-02432: Cannot open an external LOB (BFILE) in READ WRITE mode

Cause: An attempt was made to OPEN a BFILE in READ WRITE mode. Writable BFILEs are currently not supported so this operation is considered erroneous.

Action: Do not open BFILEs using READ WRITE mode. BFILEs can only be OPENed in READ ONLY mode.

PCC-02433: Invalid host variable and attribute pairing

Cause: The host variable and attribute pairing in a LOB or Collection DESCRIBE is invalid. Most likely, this was due to some problem with the host variable. For example, this error could occur if the host variable was not declared or is otherwise not provided.

Action: Usually, other, more specific, errors will accompany this one. Correcting some or all of those problems should resolve this error.

PCC-02434: FOR clause not permitted in any LOB statement

Cause: An explicit FOR clause was used in some LOB statement. The use of the FOR clause in LOB statements is erroneous.

Action: Remove the FOR clause.

PCC-02435: This attribute is only valid for internal LOB types

Cause: A request for a LOB attribute was made in a LOB DESCRIBE statement in which the given LOB was not of some Internal LOB type.

Action: Replace the LOB host variable in the LOB DESCRIBE with one that was declared to be an Internal LOB.

PCC-02436: This attribute is only valid for external LOB types (BFILEs)

Cause: A request for a LOB attribute was made in a LOB DESCRIBE statement in which the given LOB was not an External LOB type (BFILE).

Action: Use an External LOB (BFILE) host variable in the LOB DESCRIBE statement.

PCC-02437: Expecting an expression having binary integral type

Cause: A host variable was given that was not declared to be of some acceptable binary numberic integral type. Generally, when this error occurs, a signed or unsigned integral type was expected. Floating point or otherwise imprecise numeric types are considered erroneous.

Action: Replace the problematic host variable with one that was declared using a proper exact numeric integral type.

PCC-02438: Arrays of collection objects are not allowed

Cause: An array of collections was given in a COLLECTION statement. Only scalar (non-array) collection objects are allowed in any of the COLLECTION statements.

Action: Change the declaration of the Collection host variable so that it is not an array.

PCC-02439: FOR clause not allowed in this COLLECTION statement

Cause: An illegal FOR clause was used in a COLLECTION statement that did not allow one, particularly, one of either the TRIM or DESCRIBE COLLECTION statements.

Action: Remove the FOR clause from the statement.

PCC-02440: This attribute is valid for either internal or external LOBs

Cause: A request for a LOB attribute was made in a LOB DESCRIBE statement in which the given LOB host variable was neither an Internal an External LOB (BFILE) type.

Action: Use either an Internal or External LOB host variable in the LOB DESCRIBE statement.

PCC-02441: Number of attributes does not match number of host variables

Cause: There is a mismatch between the number of attributes and the number of valid host variables in the LOB or Collection DESCRIBE.

Action: Make sure that for each attribute being requested there is at most a single valid host variable given to hold its value.

PCC-02442: Expecting a value between 1 and 65535 inclusive

Cause: The value specified in the WITH MAX clause of an ALLOCATE DESCRIPTOR statement or the VALUE clause of a GET/SET DESCRIPTOR statement was either less than 1 or greater than 65535.

Action: Specify a value between 1 and 65535 inclusive.

PCC-02443: This usage is only valid when DYNAMIC=ANSI is specified

Cause: One of the following statements was used without specifying a DYNAMIC=ANSI command line option setting o EXEC SQL ALLOCATE/DEALLOCATE/GET/SET DESCRIPTOR o EXEC SQL DESCRIBE OUTPUT/INPUT... USING... descriptor o EXEC SQL EXECUTE... INTO... o EXEC SQL EXECUTE... USING... descriptor o EXEC SQL OPEN... INTO... o EXEC SQL OPEN... USING... descriptor

Action: Specify DYNAMIC=ANSI or remove statements like those above from the program.

PCC-02444: Invalid combination of descriptor and non-descriptor clauses

Cause: There was a mixing of descriptor and non-descriptor clauses in an ANSI Dynamic SQL statement.

Action: Do not mix descriptors and non-descriptors in the ANSI statement in question.

PCC-02445: USING clause valid only on a PREPAREd dynamic statement

Cause: The USING clause was used with an OPEN cursor statement where the cursor declaration was not for a PREPAREd statement. The correct sequence of statements should be as follows EXEC SQL PREPARE s FROM:stmt; EXEC SQL DECLARE c CURSOR FOR s; EXEC SQL OPEN c USING...;

Action: Use the PREPARE statement for the SQL statement and use that in the DECLARE CURSOR statement.

PCC-02446: FOR clause not allowed in a DEALLOCATE statement

Cause: An explicit FOR clause was used in a DEALLOCATE DESCRIPTOR statement.

Action: Remove the FOR clause from the statement.

PCC-02447: Cannot specify destination offset in a LOB WRITE APPEND

Cause: A destination offset was specified in a LOB WRITE APPEND statement. The destination offset is assumed to be the end of the LOB so specifying an explicit destination offset is erroneous.

Action: Remove the destination offset from the LOB WRITE APPEND statement.

PCC-02448: Cannot specify a UCS2 variable in the NLS\_NCHAR option

Cause: A variable declared as utext, uvarchar, or longuvarchar was specified in the NLS\_NCHAR command line option.

Action: Re-precompile without specifying the variable in an NLS\_NCHAR command line option.

PCC-02449: Cannot type equivalence a UCS2 type

Cause: A UCS2 type has been type equivalenced in an EXEC SQL TYPE statement or a variable of UCS2 type has been type equivalenced in an EXEC SQL VAR statement.

Action: Remove the EXEC SQL TYPE or EXEC SQL VAR statement.

PCC-02450: Cursor was not declared in scrollable mode

Cause: A cursor which was not DECLAREd in SCROLL mode was used in scrollable mode in the FETCH statement.

Action: Declare the cursor in scroll mode using the SCROLL keyword.

PCC-02451: Value of offset cannot be negative in ABSOLUTE orientation mode

Cause: The offset for the FETCH ABSOLUTE statement is negative.

Action: Value of offset should be positive.

PCC-02452: Common SQL Front End found semantic error

Cause: A database entity, such as a table or column name, was referenced, that does not exist. This is a compile time error, not a runtime error.

Action: Check that all referenced objects in the SQL statements actually exist and that the necessary access permission on them have been granted.

PCC-02453: Must use option SQLCHECK=SEMANTICS(FULL) when option OUTLINE is used

Cause: The precompiler option OUTLINE was used without specifying SQLCHECK=SEMANTICS(FULL).

Action: Set the precompiler option SQLCHECK=SEMANTICS(FULL).

PCC-02454: Must use option OUTLINE when option OUTLINPREFIX is used

Cause: The precompiler option OUTLINEPREFIX was used without specifying OUTLINE=YES|OUTLINENAME. The precompiler option OUTLINE must be specifiied if OUTLINPREFIX is used.

Action: Set the precompiler option OUTLINE=YES|OUTLINENAME.

PCC-02455: Must use option OUTLINE when option RUNOUTLINE is used

Cause: The precompiler option RUNOUTLINE was used without specifying OUTLINE=YES|OUTLINENAME. The precompiler option OUTLINE must be specifiied if RUNOUTLINE is used.

Action: Set the precompiler option OUTLINE=YES|OUTLINENAME.

PCC-02456: Unable to open Outline SQL file

Cause: Pro\*C was unable to open the OUTLINE SQL file. The user executing the precompiler must have write permission (and/or the appropriate privileges) on the current directory.

Action: Check that permission exists to create files.

PCC-02457: Unable to open Outline LOG file

Cause: Pro\*C was unable to open the OUTLINE LOG file. The user executing the precompiler must have write permission (and/or the appropriate privileges) on the current directory.

Action: Check that permission exists to create files.

PCC-02458: Outline name length exceeds the allowed limit

Cause: Outline name value of outline option\_filename\_ filetype\_seqno has exceeded the allowed limit.

Action: Use OUTLINPREFIX option to specify the outline name which will be well in the permitted limit.

PCC-02459: Number of outlines has exceeded the limit

Cause: Number of outlines that can be created has exceeded the file limit. Allowed outlines per file is 10000.

Action: Split the file so that each file can have not more than 10000 outlines.

PCC-02460: Outline cannot be created

Cause: Outline cannot be created as there is syntax error; or outlines are not supported on that statement.

Action: Correct the syntax error in the actual SQL used in the file or refer to "Performance Tuning Guide" for the list of supported statements.

PCC-02461: Must specify SQLCHECK=FULL along with option PLAN\_BASELINE

Cause: The precompiler option PLAN\_BASELINE was used without specifying SQLCHECK=FULL.

Action: Set the precompiler option SQLCHECK=FULL.

PCC-02462: Must use option PLAN\_BASELINE along with option PLAN\_PREFIX

Cause: The precompiler option PLAN\_PREFIX was used without specifying PLAN\_BASELINE=\[<module\_name>/yes\].

Action: Specify the option PLAN\_BASELINE=\[<module\_name>/yes\].

PCC-02463: Must use option PLAN\_BASELINE along with option PLAN\_RUN

Cause: The precompiler option PLAN\_RUN was used without specifying PLAN\_BASELINE=\[<module\_name>/yes\].

Action: Specify the option PLAN\_BASELINE=\[<module\_name>/yes\].

PCC-02464: Unable to open Plan Baseline SQL file

Cause: Pro\*C was unable to open the Plan Baseline SQL file. The user executing the precompiler must have write permission (or the appropriate privileges) on the current directory.

Action: Check that permission is granted to create files.

PCC-02465: Unable to open Plan Baseline LOG file

Cause: Pro\*C was unable to open the Plan Baseline LOG file. The user executing the precompiler must have write permission (and/or the appropriate privileges) on the current directory.

Action: Check that permission exists to create files.

PCC-02466: Length of Plan Baseline name exceeds the allowed limit

Cause: Plan Baseline name <module\_name>\_filename\_ filetype\_seqno exceeded the allowed limit.

Action: Use PLAN\_PREFIX option to specify the Plan Baseline prefix-name.

PCC-02467: Number of Plan Baselines has exceeded the limit per file

Cause: Number of Plan Baselines that can be created has exceeded the file limit. Allowed Plan Baselines per file is 10000.

Action: Split the file so that each file can have no more than 10000 Baselines.

PCC-02468: Plan Baseline cannot be created

Cause: Plan Baseline cannot be created, as there is a syntax error or Baselines are not supported on that statement.

Action: Correct the syntax error in the actual SQL used in the file or refer to the Oracle Database Performance Tuning Guide for the list of supported statements.

PCC-02469: Must use option PLAN\_BASELINE along with option PLAN\_ENABLED

Cause: Parameter required for Plan Baseline creation (PLAN\_ENABLED) was used without specifying the option PLAN\_BASELINE=\[<module\_name>/yes\].

Action: Specify the option PLAN\_BASELINE=\[<module\_name>/yes\].

PCC-02470: Must use option PLAN\_BASELINE along with option PLAN\_FIXED

Cause: Parameter required for Plan Baseline creation (PLAN\_FIXED) was used without specifying PLAN\_BASELINE=\[<module\_name>/yes\].

Action: Specify the option PLAN\_BASELINE=\[<module\_name>/yes\].

PCC-02471: Cannot use both PLAN\_BASELINE and OUTLINE simultaneously

Cause: Both PLAN\_BASELINE and OUTLINE options were specified. These options are not supported simultaneously.

Action: Specify either the PLAN\_BASELINE option or the OUTLINE option, but not both.

PCC-02472: Module name exceeds 30 bytes, will be truncated in database

Cause: SQL Plan Management (SPM) does not support module names greater than 30 bytes and the specified module name exceeded this limit.

Action: Shorten the module name to stay within this limit.

PCC-02473: program has EXEC SQL DECLARE TABLE, therefore PLAN\_RUN option is ignored

Cause: PLAN\_RUN was ignored because DECLARE TABLE was found. Baseline plans were not created during precompilation.

Action: Run the generated SQL manually.

PCC-02474: invalid numeric value

Cause: The numeric value was invalid.

Action: Specify a proper numeric value.