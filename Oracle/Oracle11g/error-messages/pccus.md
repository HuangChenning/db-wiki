---
title: PCC-00001 to PCC-01515
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/pccus.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 109 PCC-00001 to PCC-01515

PCC-00001: Unable to open file string

Cause: The precompiler was unable to open a temporary file for internal use. There might be insufficient disk space, too many open files, or read-only protection on the output directory.

Action: Check that there is enough disk space, that the limit for open files is set high enough (check with the system manager) and that protection on the directory allows opening a file for writing.

PCC-00002: Invalid syntax at column number in line number of file string

Cause: There is a syntax error in an EXEC statement or the statement is not properly terminated.

Action: Correct the syntax of the EXEC statement. If the error occurred at the end of the input file, check that the last EXEC statement is properly terminated.

PCC-00003: Invalid SQL Identifier at column number in line number of file string

Cause: The symbol in a conditional precompilation statement (such as EXEC ORACLE IFDEF) is invalid, or the name of a SQL descriptor, statement, or cursor is invalid or was not properly declared.

Action: Check the statement syntax and spelling of the identifier and check that a reserved word was not accidentally used. If necessary, define the identifier in a variable declaration or DECLARE statement ahead of the line in error.

PCC-00004: Mismatched IF/ELSE/ENDIF block at line number in file string

Cause: There is an EXEC ORACLE ELSE or EXEC ORACLE ENDIF statement without a matching EXEC ORACLE IFDEF statement.

Action: Add the missing EXEC ORACLE IFDEF statement or deletee or move the EXEC ORACLE ELSE or EXEC ORACLE ENDIF statement.

PCC-00005: Unsupported datatype in line number of file string

Cause: A host variable defined in the Declare Section has an unsupported datatype or has a scale or precision outside the supported range.

Action: Redefine the host variable using a supported datatype. Check that the scale and precision of a numeric variable are in the accepted range.

PCC-00007: Invalid WHENEVER condition at column number in line number of file string

Cause: A condition other than SQLERROR, SQLWARNING, or NOT FOUND was specified in an EXEC SQL WHENEVER statement, or one of these was used, but spelled incorrectly.

Action: Correct the spelling of the WHENEVER condition or use a host- language IF statement to test the special condition.

PCC-00008: Invalid WHENEVER action at column number in line number of file string

Cause: At lease one of the following:

o An action other than CONTINUE, DO, GOTO, or STOP was specified in an EXEC SQL WHENEVER statement.

o One of the specified actions was spelled incorrectly.

o The host language does not allow the action (STOP is illegal in Pro\*Pascal programs).

o A GOTO label is invalid.

Action: Check that the host language allows the specified WHENEVER action. If necessary, correct the spelling of the WHENEVER action or correct the GOTO label.

PCC-00009: Invalid host variable at column number in line number of file string

Cause: A host variable used in an EXEC SQL statement was not declared in the Declare Section or has an unsupported datatype.

Action: Declare the host variable in the Declare Section, making sure it has one of the supported datatypes.

PCC-00010: Statement out of place at line number in file string

Cause: An EXEC statement was not placed properly in the host program. For example, there might be a data manipulation statement in the Declare Section. In a Pro\*COBOL program, the Declare Section might be outside the WORKING-STORAGE or LINKAGE SECTION.

Action: Remove or relocate the statement.

PCC-00011: Already in a declare section at line number in file string

Cause: A BEGIN DECLARE SECTION statement was found inside a Declare Section.

Action: Remove the extra BEGIN DECLARE SECTION statement.

PCC-00012: Not in a declare section at line number in file string

Cause: An END DECLARE SECTION statement without a matching BEGIN DECLARE SECTION statement was found. Either the BEGIN DECLARE SECTION statement is missing or misspelled or the END DECLARE SECTION statement is an extra.

Action: Add or correct the BEGIN DECLARE SECTION statement or remove the extra END DECLARE SECTION statement.

PCC-00013: Unable to open include file "string" at line number in file string

Cause: The precompiler was unable to open the input file specified in the INCLUDE statement. Some possible causes follow:

o The filename is misspelled.

o The file does not exist.

o The search path to the file is incorrect.

o File access privileges are insufficient.

o There is not enough disk space.

o There are too many open files.

Action: Check that the file exists, that the search path to the file is correct, that sufficient privileges to access the file have been granted, and that it is not locked by another user. Also, check that there is enough disk space and that the limit for open files is set high enough (check with the system manager).

PCC-00014: Undeclared SQL Identifier "string" at line number in file string

Cause: The name of a descriptor, statement, or cursor was not declared or is misspelled.

Action: Add or correct the descriptor, statement, or cursor declaration.

PCC-00015: Unrecognized Host Language syntax ignored at line number in file string

Cause: The host language syntax used to define a host variable in the Declare Section is incorrect.

Action: Check the syntax and the spelling, then correct the declaration.

PCC-00016: Unable to open a cursor at line number in file string

Cause: The syntax in a SQL statement is faulty. The precompiler was expecting a host variable, but found something else.

Action: Check the syntax and the spelling, then correct the SQL statement.

PCC-00017: Unable to parse statement at line number in file string

Cause: There is a syntax error in an array declaration. The precompiler was expecting a right bracket (\]) but found something else.

Action: Check the syntax, then correct the array declaration.

PCC-00018: Expected "string", but found "string" at line number in file string

Cause: The syntax in a SQL statement is faulty. The precompiler found an unexpected or illegal token.

Action: Check the syntax and the spelling, then correct the SQL statement.

PCC-00019: Unable to obtain bind variables at line number in file string

Cause: The precompiler was unable to find information about an input host variable (bind variable) used in a SQL statement.

Action: Check that the input host variable is declared in the Declare Section and used properly in the SQL statement.

PCC-00020: Unable to obtain define variables at line number in file string

Cause: The precompiler was unable to find information about an output host variable (define variable) used in a SQL statement.

Action: Check that the output host variable is declared in the Declare Section and used properly in the SQL statement.

PCC-00021: Oracle Error: string

Cause: An Oracle error occurred.

Action: Refer to the indicated message in the ORA message chapters of this manual.

PCC-00022: Out of space - unable to allocate number bytes

Cause: The precompiler process ran out of memory.

Action: Allocate more memory to the process, then retry.

PCC-00023: Unable to log off from ORACLE

Cause: An Oracle connection error occurred while the precompiler was trying to log off, probably because ORACLE has been shut down.

Action: Check that ORACLE is available, then retry.

PCC-00024: Indicator variable "string" has wrong type or length at line number in file string

Cause: An indicator variable was not declared in the Declare Section as a 2-byte integer. Indicator variables must be defined as 2-byte integers.

Action: Redefine the indicator variable as a 2-byte integer.

PCC-00025: Undeclared indicator variable "string" at line number in file string

Cause: An indicator variable used in a SQL statement was not declared in the Declare Section or its name is misspelled.

Action: Add or correct the indicator variable declaration.

PCC-00026: Invalid host variable "string" at line number in file string

Cause: A host variable used in a SQL statement was not declared properly. Some possible causes follow:

o It was not declared in the Declare Section.

o Its datatype is not supported.

o Its name is misspelled.

o It is a COBOL group item; in Pro\*COBOL, only elementary items are allowed in a SQL statement.

Action: Add or correct the host variable declaration.

PCC-00027: Redeclared SQL Identifier "string" at line number in file string

Cause: The name of a SQL descriptor, statement, or cursor was re-declared (that is, declared twice)

Action: Check the spelling of the identifier, then, if necessary, remove the extra declaration.

PCC-00028: Option "string" not legal as EXEC ORACLE OPTION

Cause: A precompiler option was specified inline in an EXEC ORACLE statement. Some options can be specified only on the command line. For example, INAME cannot be specified inline.

Action: Respecify the precompiler option on the command line, instead of in an EXEC ORACLE statement. To see an online display of the precompiler options, enter the precompiler command (with no options) at the operating-system prompt.

PCC-00029: Ambiguous option "string"

Cause: The name of a precompiler option was abbreviated ambiguously. For example, MAX= might refer to MAXLITERAL or MAXOPENCURSORS.

Action: Respecify the full option name or an unambiguous abbreviation. To see an online display of the precompiler options, enter the precompiler command (with no options) at the operating-system prompt.

PCC-00031: Invalid value given for option "string"

Cause: The value specified for a precompiler option is invalid, probably because the value is misspelled (as in LTYPE=HORT) or out of range (as in PAGELEN=-55).

Action: Check the value, making sure it is spelled correctly and within the legal range.

PCC-00032: Invalid option "string"

Cause: The precompiler found an invalid precompiler option name. Some possible causes follow:

o The option name is misspelled.

o The specified option does not exist.

o The equal sign (=) between the option name and value is missing or has space around it.

Action: Check that the option exists and that its name is spelled correctly. To see an online display of the precompiler options, enter the precompiler command (with no options) at the operating- system prompt. Also check that there is an equal sign between the option name and value.

PCC-00033: Missing operand for option "string"

Cause: No value was specified for a precompiler option. Either the value is missing or there is space around the equal sign (as in LTYPE =SHORT).

Action: Check that a value for each option has been specified and there is no space around the equal sign.

PCC-00036: No input file name specified

Cause: The input file was not specified on the command line.

Action: Use the INAME command-line option to specify the input file.

PCC-00037: Unable to log on to ORACLE with "string". ORACLE error number: number

Cause: The precompiler was unable to log on to ORACLE with the specified username and password. An ORACLE error with given number occurred when the logon was attempted.

Action: Refer to the indicated message in the ORA message chapters of this manual.

PCC-00038: Unable to open a cursor

Cause: This is an internal error message not usually issued.

Action: Call customer support for assistance. If the application does not require syntactic or semantic checking of SQL statements and does not use PL/SQL, specify SQLCHECK=NONE on the command line.

PCC-00039: Unable to open input file "string"

Cause: The precompiler was unable to open the input file specified by the INAME precompiler option. Some possible causes follow:

o The filename is misspelled.

o The file does not exist.

o The search path to the file is incorrect.

o File access privileges are insufficient.

o Another user has locked the file.

o There is not enough disk space.

o There are too many open files.

Action: Check that the file exists, that the search path to the file is correct, that sufficient privileges have been granted to access the file, and that it is not locked by another user. Also check that there is enough disk space and that the limit for open files is set high enough (check with the system manager).

PCC-00040: Unable to open listing file "string"

Cause: The precompiler was unable to open the listing file specified by the LNAME precompiler option. Some possible causes follow:

o The filename is misspelled.

o The file does not exist.

o The search path to the file is incorrect.

o File acces privileges are insufficient.

o Another user has locked the file.

o There is not enough disk space.

o There are too many open files.

Action: Check that the file exists, that the search path to the file is correct, that sufficient privileges have been granted to access the file, and that it is not locked by another user. Also check that there is enough disk space and that the limit for open files is set high enough (check with the system manager). If a listing file is not needed, specify LTYPE=NONE on the command line.

PCC-00041: Unable to open output file "string"

Cause: The precompiler was unable to open the listing file specified by the ONAME precompiler option. Some possible causes follow:

o The filename is misspelled.

o The file does not exist.

o The search path to the file is incorrect.

o File acces privileges are insufficient.

o Another user has locked the file.

o There is not enough disk space.

o There are too many open files.

Action: Check that the file exists, that the search path to the file is correct, that sufficient privileges have been granted to access the file, and that it is not locked by another user. Also check that there is enough disk space and that the limit for open files is set high enough (check with the system manager).

PCC-00042: Must EXEC SQL INCLUDE SQLCA when mode=ANSI and WHENEVER SQLWARNING used

Cause: When MODE={ANSI | ANSI14}, an attempt was made to use the WHENEVER SQLWARNING statement without declaring the SQLCA. When MODE={ANSI | ANSI14}, declaring the SQLCA is optional, but to use the WHENEVER SQLWARNING statement, the SQLCA must be declared.

Action: Remove all WHENEVER SQLWARNING statements from the program or declare the SQLCA by hardcoding it or copying it into the program with the INCLUDE statement.

PCC-00044: Array size mismatch in INTO/USING. Minimum is: string(number:number)

Cause: The size of an array variable in an INTO/USING clause is too small for the number of rows processed.

Action: Declare all array variables in the INTO/USING clause to have at least the minimum dimension given.

PCC-00045: string clause inappropriate at line number in file string. Ignored.

Cause: There is a misplaced clause at the end of an EXEC SQL statement (an AT clause at the end of a SELECT statement, for example), or the

Action: Check the statement syntax, then relocate or correct the misplaced or invalid clause.

PCC-00047: Unterminated comment/string constant beginning near line number in file string

Cause: A string constant is missing an ending quotation mark, or a comment is missing an ending delimiter.

Action: Check that all comments are delimited and all string constants are enclosed by quotation marks.

PCC-00050: Unable to generate descriptor in program unit ending line number in file string

Cause: The precompiler was unable to generate a descriptor for the compilation unit. This can occur from either of the following:

o A non-existent or improperly implemented Declare Section

o Undetected syntax errors near the beginning of the source file or just before the END DECLARE SECTION statement

Action: Verify that the Declare Section is properly implemented. Then check for syntax errors at the beginning of the compilation unit and before any END DECLARE SECTION statement, and correct as appropriate.

PCC-00051: Size of VARCHAR string is larger than 65533 in line number in file string

Cause: The declared size of a VARCHAR host variable exceeds the precompiler limit of 65533 bytes.

Action: Check the Declare Section, making sure the size of each VARCHAR variable does not exceed the limit of 65533 bytes.

PCC-00053: FOR variable string is invalid type at line number in file string

Cause: The count variable in a FOR clause has the wrong datatype. The datatype must be NUMBER or LONG (or be compatible with NUMBER or LONG).

Action: Check the declaration and check that the count variable has a datatype of NUMBER or LONG (or a compatible Oracle or host-language datatype).

PCC-00054: Expected End-of-Statement at column number in line number of file string

Cause: The precompiler expected to find a statement terminator at the end of an EXEC statement but found something else. This can happen if tabs were embedded in the source code (because the precompiler has no way of knowing how many spaces a tab represents).

Action: If tabs are embedded in the source ocde, replace them with spaces. Check the statement syntax and check that each EXEC statement has a terminator. For embedded CREATE {FUNCTION | PROCEDURE | PACKAGE} statements and for embedded PL/SQL blocks, check that the statement terminator is END-EXEC.

PCC-00055: Array "string" not allowed as bind variable at line number in file string

Cause: A host array was used as a bind (input) variable in the WHERE clause of a SELECT statement. This is not allowed.

Action: Remove the host array or replace it with a simple host variable.

PCC-00056: FOR clause not allowed on SELECT statement at line number in file string.

Cause: A FOR clause was used with a SELECT statement. This is not allowed as data returned from the last loop in the execution of the SELECT overwrites data returned in a previous loop.

Action: Remove the FOR clause from the SELECT statement and use a host- language construct to iteratively execute the SELECT statement.

PCC-00060: Both CURSOR and STATEMENT have AT clauses at line number of file string.

Cause: Two AT clauses, one in a DECLARE STATEMENT statement, the other in a DECLARE CURSOR statement, pertain to the same SQL statement. The AT clause may be specified with either DECLARE STATEMENT or DECLARE CURSOR, but not with both.

Action: Remove the AT clause from one of the statements.

PCC-00061: Error at line number, column number. PLS-number: string

Cause: The precompiler found an error in an embedded SQL statement or PL/SQL block.

Action: Refer to the indicated PL/SQL error message to correct the SQL statement or embedded PL/SQL block.

PCC-00062: Must use option SQLCHECK=SEMANTICS(FULL) when there is embedded PL/SQL

Cause: The precompiler tried to parse an embedded PL/SQL block when SQLCHECK={SYNTAX | NONE}. PL/SQL blocks can be parsed only when SQLCHECK=SEMANTICS is specified.

Action: Remove the PL/SQL block or specify SQLCHECK=SEMANTICS.

PCC-00063: Reached end of file string before End-of-Statement at line number!

Cause: The precompiler encountered an end-of-file while parsing a PL/SQL block.

Action: Add the appropriate statement terminator (;) or end-of-block statement (END;) to the PL/SQL block.

PCC-00064: All uses of a given host variable must use identical indicator variables.

Cause: Two or more occurrences of a host variable in an EXEC SQL statement were associated with different indicator variables. This is not allowed.

Action: Rename the indicator variables so that each occurrence of the host variable is associated with the same indicator variable.

PCC-00065: Userid required, but not specified.

Cause: The SQLCHECK=SEMANTICS option was specified, but the USERID option on the command line was not specified.

Action: Specify USERID=username/password or enter a username and password when prompted or specify SQLCHECK={SYNTAX | NONE}.

PCC-00066: Userid only used when SQLCHECK = FULL, userid ignored.

Cause: The USERID option was specified when SQLCHECK={SYNTAX | NONE}. This is unnecessary.

Action: Specify the USERID option only when SQLCHECK=SEMANTICS.

PCC-00067: Ireclen exceeded. Line number in file string truncated.

Cause: While reading the input file, the precompiler found a line longer than IRECLEN.

Action: Either shorten the input line or specify a larger IRECLEN value on the command line.

PCC-00068: Host and indicator variables may not have the same name.

Cause: In an EXEC SQL statement, an indicator variable had the same name as a host variable. The names of a host variable and its associated indicator variable must be different. Also, an indicator variable cannot be used as a host variable.

Action: Rename the host or indicator variable.

PCC-00069: Host variable "string" has unsupported datatype at line number in file string

Cause: A host variable had an unsupported datatype. For a list of supported datatypes, see the language-specific supplement to the Programmer's Guide to the Oracle Precompilers.

Action: Redefine the host variable in the Declare Section, giving it a supported datatype.

PCC-00070: Illegal syntax, Exponential value in SQL statement: string

Cause: The precompiler found a syntax error while parsing a number coded in scientific notation. The precompiler expected to find a signed integer following the exponentiation indicator (E), but found something else.

Action: Reformat the number correctly.

PCC-00071: Unable to open message file.

Cause: The precompiler was unable to open the message file containing the messages that can be issued by the precompiler. This can happen if there are too many open files or if there were problems with installation of the precompiler.

Action: Check that the limit for open files is high enough (check with the system manager). Otherwise, contact customer support.

PCC-00072: Input file name length exceeds the maximum length

Cause: The file name length specified exceeded the maximum length. Some operating systems have a maximum file name length.

Action: Use a file name of length less than or equal to the maximum platform specific file name length.

PCC-00073: Cursor is declared but never OPENed at line number in file string.

Cause: A cursor was DECLAREd but was not referenced in an OPEN statement. This is only an informational message.

Action: Remove the cursor declaration or code an OPEN statement for the cursor.

PCC-00075: ":" expected before indicator variable

Cause: An indicator variable was not prefixed with a colon, as required.

Action: Prefix a colon to the indicator variable in question.

PCC-00076: DISPLAY type must be SIGN LEADING SEPARATE

Cause: This message is issued only by Pro\*COBOL. DISPLAY SIGN LEADING SEPARATE is the only DISPLAY type supported by Pro\*COBOL.

Action: Check the spelling of the variable declaration. If necessary, remove the reference to the unsupported DISPLAY type.

PCC-00077: Colon usage with numeric label in WHENEVER statement is not ANSI

Cause: An Oracle extenstion to the ANSI/ISO SQL standard was used. Specifically, a numeric WHENEVER... GOTO label was prefixed with a colon. For exammple the code might have looked like EXEC SQL WHENEVER SQLERROR GOTO:99; This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action required. However, for ANSI/ISO compliance, prefix alphanumeric (but not numeric) WHENEVER... GOTO labels with a colon.

PCC-00078: FIPS warning: Invalid ANSI SQL Identifier

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, the name given to a host variable:

o is longer than 18 characters,

o does not begin with a letter, or

o contains consecutive or trailing underscores. In the following Pro\*C example, the host variable name is 19 characters long and therefore non-compliant: EXEC SQL BEGIN DECLARE SECTION; int department\_location: -- not ANSI/ISO compliant EXEC SQL END DECLARE SECTION; This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action required. However, for ANSI/ISO compliance, change the host variable name so that it is <= 18 characters long, begins with a letter, and does not contain consecutive or trailing underscores.

PCC-00079: ANSI requires colon on label in WHENEVER statement

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, an alphanumeric WHENEVER... GOTO label was not prefixed with a colon. For example the offending code might look like: EXEC SSQL WHENEVER NOT FOUND GOTO no\_more; This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action required. However, for ANSI/ISO compliance, prefix alphanumeric (but not numeric) WHENEVER... GOTO labels with a colon.

PCC-00080: TYPE identifier already TYPEd

Cause: The identifier being TYPEd in an EXEC SQLY TYPE statement appeared in a previous EXEC SQL TYPE statement. A given identifier can appear in only one EXEC SQL TYPE statement.

Action: Check the spelling of the identifiers. Use different identifiers in the EXEC SQL TYPE statements, or remove one of the EXEC SQL TYPE statements.

PCC-00081: Scale specification not allowed for given datatype

Cause: The Oracle external datatype referenced in an EXEC SQL VAR or EXEC SQL TYPE statement does no allow a scale specification.

Action: Check the precision specification and remove the scale specification.

PCC-00082: Length and scale specifications must be an integer

Cause: A floating point number or a non-number to specify a length or scale was used. Only integers can be used.

Action: Correct or remove the length and/or scale specification.

PCC-00083: Bind and define variables not allowed in CREATE statement

Cause: Host variables cannot appear in a CREATE statement. If the makeup of a CREATE statement cannot be known until run time, a dynamic SQL statement must be used to execute it. That is, the program must accept or build the CREATE statement at run time, store it in a host string, then EXECUTE it.

Action: Correct or remove the erroneous CREATE statement.

PCC-00085: Error writing to file string

Cause: The precompiler was unable to write to the named output file. Some possible causes follow:

o Sufficient file access privileges were not defined.

o Another user has locked the file.

o There is not enough disk space.

o There are too many open files.

Action: Check that sufficient privileges exist to access the file and that it is not locked by another user. Also check that there is enough disk space and that the limit for open files is set high enough (check with system manager).

PCC-00086: Source file string has zero length

Cause: The source file specified on the command line contains no code. Consequently, there is nothing for the precompiler to process.

Action: Specify a valid source file containing embedded SQL statements.

PCC-00087: EXEC SQL TYPE statement not allowed for this host language

Cause: An EXEC SQL TYPE statement was used with a host language that does not support user-defined datatype equivalencing. This feature is available only in Pro\*C and Pro\*Pascal.

Action: Remove the offending EXEC SQL TYPE statement.

PCC-00088: User defined type identifier expected

Cause: The user-defined datatype name in an EXEC SQL TYPE statement is missing or misspelled, is a reserved word, is not a legal identifier in the host-language or conflicts with a base datatype in that language.

Action: Check the spelling of the user-defined datatype name. If necessary, declare a valid user-defined datatype. User-defined datatype equivalencing is available only in Pro\*C and Pro\*Pascal.

PCC-00089: Invalid Oracle TYPE specification

Cause: The Oracle external datatype name in an EXE SQL TYPE or EXEC SQL VAR statement is missing or misspelled.

Action: Check the spelling of the external datatype name. If necessary, supply the missing datatype name.

PCC-00090: Precision/scale specification must be given for DECIMAL datatype

Cause: A precision and/or scale specification for the Oracle external datatype DECIMAL in an EXEC SQL TYPE or EXEC SQL VAR statement was omitted.

Action: Add the precision and/or scale specification to the EXEC SQL TYPE or EXEC SQL VAR statement.

PCC-00091: TYPE statement requires format specification for this Oracle datatype

Cause: A length, precision, and/or scale specification for an Oracle external datatype in an EXEC SQL TYPE or EXEC SQL VAR statement was omitted.

Action: Add the length, precision, and/or scale specification for the external datatype to the EXEC SQL TYPE or EXEC SQL VAR statement.

PCC-00092: Length and/or scale incompatible with specified Oracle datatype

Cause: An invalid length or scale for an Oracle external datatype in an EXEC SQL TYPE or EXEC SQL VAR statement was specified.

Action: Check that a length large enough to accommodate the external datatype is specified. If a scale is specified, check that it lies in the range -84..99.

PCC-00093: Invalid or obsolete option, ignored

Cause: The precompiler found an option available in a prior version or different host language but not in the current version or host language.

Action: Remove the option specification.

PCC-00094: Array length for char\[n\] datatype must be >= 2

Cause: When MODE={ANSI | ANSI14}, a length of less than 2 characters for a char\[n\] host variable was specified or a simple char variable was specified. When MODE={ANSI | ANSI14}, the length must be at least 2 characters. This message is issued only by the Pro\*C precompiler.

Action: Correct the declaration so that it specifies a length of at least 2 characters.

PCC-00095: Missing PROGRAM, SUBROUTINE, FUNCTION, or BLOCK DATA statement

Cause: FORTRAN source files are expected to have at least one PROGRAM, SUBROUTINE, FUNCTION, or BLOCK DATA statement, which the precompiler uses to detect the beginning of a routine or compilation unit.

Action: Add one of these statements to the source file.

PCC-00096: Array FETCH not allowed for mode=ANSI14

Cause: When MODE=ANSI14, an array SELECT or FETCH was attempted. However, array operations are not allowed with MODE=ANSI14.

Action: If MODE=ANSI14 must be specified, place the SELECT or FETCH statement in a host-language loop, instead of using the array interface.

PCC-00097: Use of DECIMAL and DISPLAY types allowed only for COBOL and PL/I

Cause: The DECIMAL and DISPLAY external datatype was used in an EXEC SQL VAR or EXEC SQL TYPE statement with an Oracle precompiler other than Pro\*COBOL or PRO\*PL/I. These external datatypes are available only in Pro\*COBOL and PRO\*PL/I.

Action: Remove the reference to the DECIMAL or DISPLAY external datatype from the EXEC SQL TYPE or EXEC SQL VAR statement.

PCC-00098: Scale specification cannot be used in this context

Cause: In a Pro\*C, Pro\*FORTRAN, Pro\*Pascal program, scale in an EXEC SQL TYPE or EXEC SQL VAR statement in the current context cannot be specified.

Action: Remove the scale specification from the EXEC SQL TYPE or EXEC SQL VAR statement.

PCC-00099: Length cannot be given for types ROWID, DATE, or MLSLABEL

Cause: A length for the ROWID, DATE, or MLSLABEL external datatype was specified in an EXEC SQL TYPE or EXEC SQL VAR statement. This is unnecessary because those are fixed length types.

Action: Remove the length specification from the EXEC SQL TYPE or EXEC SQL VAR statement.

PCC-00100: Non integer label is not ANSI

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, a non-integer WHENEVER... GOTO label was in a Pro\*Pascal program. For example, the offending code might look like: EXEC SQL WHENEVER NOT FOUND GOTO quit; This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action required. However, for ANSI/ISO compliance, use only integer WHENEVER... GOTO labels in a Pro\*Pascal program.

PCC-00101: Lower case 'e' in floating point number is not ANSI

Cause: A Oracle extension to the ANSI/ISO SQL standard was used. Specifically, a lowercase 'e' was used in scientific notation. For example, the offending code might look like: maxnum = 10e38; This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action required. However, for ANSI/ISO compliance, use an uppercase 'E' in scientific notation.

PCC-00102: FOR UPDATE is an Oracle extension

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, the FOR UPDATE OF clause was used in a cursor declaration. For example, the offending code might look like: EXEC SQL DECLARE emp\_cursor CURSOR FOR SELECT ENAME, SAL FROM EMP WHERE DEPTNO =:dept\_number FOR UPDATE OF SAL; This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action required. However, for ANSI/ISO compliance, do not use the FOR UPDATE OF clause.

PCC-00103: AT clause is an Oracle extension

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, the AT <db\_name> clause was used in a SQL statement. For example, the offending code might look like: EXEC SQL AT oracle3 COMMIT RELEASE; This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action required. However, for ANSI/ISO compliance, do not use the AT <db\_name> clause.

PCC-00104: FOR clause is an Oracle extension

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, the FOR clause was used in an array-processing SQL statement. For example, the offending code might look like: EXEC SQL FOR:limit INSERT INTO EMP (EMPNO, JOB, DEPTNO) VALUES (:emp\_number,:job\_title,:dept\_number); This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action required. However, for ANSI/ISO compliance, do not use the FOR clause.

PCC-00105: Keyword WORK required here by ANSI

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, the keyword WORK was used in a COMMIT or ROLLBACK statement. For example, the offending code might look like: EXEC SQL COMMIT WORK RELEASE; This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action required. However, for ANSI/ISO compliance, do not use the keyword WORK.

PCC-00106: RELEASE is an Oracle extension to the COMMIT and ROLLBACK statements

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, the parameter RELEASE was used in a COMMIT or ROLLBACK statement. For example, the offending code might look like: EXEC SQL ROLLBACK RELEASE; This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action required. However, for ANSI/ISO compliance, do not use the parameter RELEASE;

PCC-00107: The CONNECT statement is Oracle implementation dependent

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, the CONNECT statement was used to log on to ORACLE. For example, the offending code might look like: EXEC SQL CONNECT:username IDENTIFIED BY:password; This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action required. However, for ANSI/ISO compliance, specify the AUTO\_CONNECT command-line option instead of using a CONNECT statement.

PCC-00108: This statement is not supported by ANSI

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, a nonconforming SQL statement such as PREPARE was used. For example, the offending code might look like: EXEC SQL PREPARE sql\_statement FROM:sql\_string; This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action required. However, for ANSI/ISO compliance, do not use the nonconforming statement.

PCC-00109: Dynamic SQL and PL/SQL are Oracle extensions to ANSI SQL

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, dynamic SQL or embedded PL/SQL was used. For example, the offending code might look like: EXEC SQL EXECUTE BEGIN SELECT... END; END-EXEC; This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action required. However, for ANSI/ISO compliance, do not use dynamic SQL or embedded PL/SQL.

PCC-00110: Oracle extension to the WHENEVER statement

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, a nonconforming keyword such as NOTFOUND, STOP, RAISE, or DO was used in the WHENEVER statement. (Note that NOT FOUND is ANSI-compliant.) For example, the offending code might look like: EXEC SQL WHENEVER SQLERROR STOP; This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action required. However, for ANSI/ISO compliance, do not use the nonconforming keyword.

PCC-00111: SQLCHECK value in EXEC ORACLE statement exceeds command line value

Cause: The SQLCHECK option was entered inline and specified a level of checking higher than the level specified (or accepted by default) on the command line. This is not allowed. For example, if SQLCHECK={SYNTAX | LIMITED} is specified on the command line, SQLCHECK={SEMANTICS | FULL} cannot be specified inline.

Action: Revise the EXEC ORACLE statement or specify a lower level of checking on the command line.

PCC-00112: Datatype not supported by ANSI

Cause: An Oracle extension to the ANSI/ISO standard was used. Specifically, aa pointer or nonconforming datatype such as VARCHAR was used. For example, the offending code might look like: EXEC SQL BEGIN DECLARE SECTION VARCHAR username\[20\]; EXEC SQL END DECLARE SECTION This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action required. However, for ANSI/ISO compliance, do not use pointers or nonconforming datatypes.

PCC-00113: Value of DBMS option invalid with given value of MODE option

Cause: When MODE={ANSI14 | ANSI13}, DBMS=V7 was specified, or when MODE=ANSI, DBMS=v6 was specified. These option settings are incompatible. Note that the DBMS option was not available before release 1.5 of the Oracle Precompilers.

Action: With DBMS=V7, instead of MODE={ANSI14 | ANSI13}, specify MODE={ANSI | ORACLE}. With DBMS=V6, instead of MODE=ANSI, specify MODE={ANSI14 | ANSI13 | ORACLE}, but MODE=ORACLE is recommended.

PCC-00114: Length spec required in EXEC SQL VAR statements for VARxxx types

Cause: In an EXEC SQL VAR statement, a VARCHAR or VARRAW external datatype was specified without a length. Unlike other types, the maximum length of the data field must be specified for VARCHAR and VARRAW.

Action: Add a length specification to the EXEC SQL VAR statement.

PCC-00115: Array required here

Cause: In an ARRAYLEN statement, the name of a previously declared host array was not specified. The first host variable in an ARRAYLEN statement must be an array. The second host variable, which specifies an array dimension, must be a 4-byte integer. The correct syntax follows: EXEC SQL ARRAYLEN host\_array (dimension); The ARRAYLEN statement must appear in the Declare Section along with, but somewhere after, the declarations of host\_array and dimension.

Action: Check the spelling of both identifiers in the ARRAYLEN statement. If necessary, supply the missing host array name.

PCC-00116: This array already given in an ARRAYLEN statement

Cause: The same host array was specified in two different ARRAYLEN statements. A given host array cannot be specified in more than one ARRAYLEN statement.

Action: Check the spelling of the host array names in both ARRAYLEN statements. Change one of the names so that they refer to different host arrays or remove one of the ARRAYLEN statements.

PCC-00117: Invalid ARRAYLEN length variable type

Cause: A valid array dimension was not specified in an ARRAYLEN statement. The array dimension must be specified using a previously declared 4-byte integer host variable, not a literal or expression. For example, the offending code might look like: EXEC SQL ARRAYLEN ename\_array (25); -- illegal dimension

Action: Supply a valid array dimension. If necessary, declare a 4-byte integer host variable for use in the ARRAYLEN statement.

PCC-00118: Use of host variable initialization not supported by ANSI SQL

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, a host variable was initialized in its declaration, as shown in the following Pro\*C example: EXEC SQL BEGIN DECLARE SECTION; int dept\_number = 20; -- not ANSI/ISO-compliant EXEC SQL END DECLARE SECTION; This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action required. However, for ANSI/ISO compliance, do not initialize host variables in their declarations.

PCC-00119: Value of const variable in INTO clause will be modified

Cause: A variable declared with the type specifier "const" was used in an INTO clause. Such variables should not be modified and should not be used in an INTO clause.

Action: Check the spelling of all identifiers in the INTO clause. If necessary, remove "const" from the host variable declaration or use a different host variable.

PCC-00120: File I/O error during code generation

Cause: d by insufficient disk space.

Action: Check that there is enough disk space.

PCC-00121: Arrays of VARCHAR pointers are not supported

Cause: An array of pointers was declared, which is not allowed. However, pointers to scalar types are allowed. With Pro\*C, declare pointers to char\[n\] and varchar\[n\] variables as pointers to CHAR or VARCHAR (with no length specification).

Action: Correct or remove the declaration.

PCC-00122: Input file name and output file name are identical

Cause: On the command line, the same pathname for INAME and ONAME was specified, which designates the precompiler input and output files, respectively.

Action: Change one of the path/filenames.

PCC-00123: Entire VARCHAR declaration must be on same line

Cause: In a Pro\*C program, a VARCHAR declaration spans more than one line, which is not allowed.

Action: Revise the declaration so that it uses only one line.

PCC-00124: COMMON\_NAME option is specified too late

Cause: In a FORTRAN program, subroutine, or function, the precompiler option COMMON\_NAME was mistakenly specified after the PROGRAM, SUBROUTINE, or FUNCTION statement. If COMMON\_NAME is specified inline, its EXEC ORACLE OPTION statement must precede the PROGRAM SUBROUTINE, or FUNCTION statement.

Action: Relocate the EXEC ORACLE OPTION statement or specify COMMON\_NAME on the command line.

PCC-00126: Could not find or open system configuration file

Cause: The precompiler was unable to find or open the system configuration file (a text file containing preset command-line options, which the precompiler uses by default). Some possible causes follow:

o The file does not exist.

o The search path to the file is incorrect.

o File access privileges are insufficient.

o There are too many open files. However, this message is just a warning. Processing continues even if the system configuration file does not exist.

Action: Check that the file exists, that the search path to the file is correct, and that sufficient privileges exist to access the file. Also check that the limit for open files is set high enough (check with the system manager).

PCC-00127: string

Cause: This is a generic error message from the command-line processor.

Action: Correct the indicated error.

PCC-00128: Command line processor severe error

Cause: The command line processor encountered a severe error.

Action: After making sure that all the command-line options are specified correctly, call customer support with a full account of all the options and configuration files used.

PCC-00129: Option "string" must be given

Cause: A required command-line option is missing. For example, the INAME option, which specifies the name of the input file, might be missing.

Action: Supply the missing command-line option.

PCC-00132: Indicator array size must not be less than its host variable

Cause: An host variable array was used with an indicator array declared with a smaller dimension. For example: EXEC SQL BEGIN DECLARE SECTION; int dept\_no\[20\]; short dept\_no\_ind\[10\]; EXEC SQL END DECLARE SECTION;... SELECT... INTO dept\_no:dept\_no\_ind...

Action: Increase the size of the indicator array.

PCC-00133: Command line option MODE=ANSI required with option NLS\_LOCAL=YES

Cause: The precompiler option NLS\_LOCAL=YES was used without also specifying MODE=ANSI. The precompiler option MODE=ANSI must be specifiied if NLS\_LOCAL=YES.

Action: Set the precompiler option MODE=ANSI in addition to NLS\_LOCAL=YES or do not set NLS\_LOCAL=YES.

PCC-00135: Result Set Cursor usage is not standard SQL

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, an Oracle Result Set Cursor has been used. This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action required. However, for ANSI/ISO compliance, do not use Result Set Cursors.

PCC-00136: Invalid SQL\_CURSOR declaration

Cause: An array of SQL\_CURSOR host variables was declared or, if Pro\*COBOL, a PICTURE clause was specified in the SQL-CURSOR declaration. In Pro\*FORTRAN, a length specification (i.e. "\*n") on the SQL\_CURSOR declaration could have been specified. These usages are not supported.

Action: Check that the SQL\_CURSOR variable is not declared as an array or, if Pro\*COBOL, that no PICTURE clause is specified for the SQL\_CURSOR. In Pro\*FORTRAN, check that there is no length specification (i.e. "\*n") for the SQL\_CURSOR.

PCC-00137: Invalid use of SQL cursor host variable

Cause: A SQL\_CURSOR variable was used in an INTO or WHERE clause. SQL\_CURSOR variables can be used only where ordinary cursor identifiers would be used or, in a PL/SQL block, where a cursor would normally be used.

Action: Remove the SQL cursor variable reference from the INTO clause or WHERE clause, or use a host variable of another type in the INTO or WHERE clause.

PCC-00138: Result Set Cursors are not implemented in this precompiler

Cause: There was an attempt to reference a host variable as a cursor reference. Cursor variables are not implemented in PRO\*Pascal or Pro\*PL/I.

Action: Rewrite your host-language code to use standard SQL cursors.

PCC-00139: Cannot change MAXLITERAL after an EXEC SQL statement

Cause: The MAXLITERAL option has been used in an inline EXEC ORACLE OPTION statement after and EXEC SQL, EXEC TOOLS, or EXEC IAF statement. This is not allowed.

Action: Use the MAXLITERAL option only on the command line or in an EXEC ORACLE OPTION statement placed at the beginning of the input source file.

PCC-00140: CREATE FUNCTION/PROCEDURE/PACKAGE/TRIGGER are Oracle extensions

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, one of the following statements was used:

o CREATE FUNCTION

o CREATE PROCEDURE

o CREATE PACKAGE

o CREATE TRIGGER These statements are Oracle extensions to the ANSI/ISO SQL standards. This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action is required. However, for ANSI/ISO compliance, do not use any of these statements.

PCC-00141: Thread Safety is not implemented in this precompiler

Cause: There has been an attempt to use CONTEXT sql statements. The thread safety feature is not implemented in PRO\*Pascal, Pro\*PL/I, or Pro\*C 1.x.

Action: Rewrite your host-language code to not use contexts.

PCC-00142: No EXEC SQL CONTEXT USE statement encountered

Cause: No EXEC SQL CONTEXT USE statement was encountered and the option threads=yes was requested.

Action: Ensure that the necessary context variable (of type sql\_context) has been declared, ALLOCATEd, and USEd prior to any executable SQL statements.

PCC-00143: Runtime context variable not of correct type

Cause: The runtime context variable referecned in an EXEC SQL CONTEXT USE statement is not of type sql\_context.

Action: Declare your runtime context variable of type sql\_context.

PCC-00144: UNSAFE\_NULL=YES must be used with DBMS=V7 and MODE=ORACLE

Cause: The option UNSAFE\_NULL=YES has been used with DBMS=V6 or DBMS=NATIVE (the default) or has been used with MODE=ANSI/ANSI14/ANSI13.

Action: Either specify DBMS=V7 and MODE=ORACLE (the default) when using UNSAFE\_NULL=YES or do not use UNSAFE\_NULL=YES.

PCC-00145: This statement can only be used with THREADS=YES

Cause: EXEC SQL ENABLE THREADS or one of the EXEC SQL CONTEXT statements has been used, even though option THREADS is set to NO.

Action: Specify option THREADS=YES or remove the EXEC ENABLE THREADS or EXEC SQL CONTEXT statement from the source code.

PCC-00146: Illegal value for host option, ignored

Cause: An invalid host language was specified using the command-line host option. The host option valid values are pro\* language specific. For example, for profor, the only valid value is FORTRAN. For procob, the only valid values are COBOL and COB74.

Action: Specify a valid host language with the host option.

PCC-00147: DBMS=V6 no longer supported; using DBMS=NATIVE

Cause: V6 compatibility is no longer supported. The precompiler will precompile as though DBMS=NATIVE was specified.

Action: Revise the specified DBMS option value from v6 to another value as desired.

PCC-01000: You are not authorized to run Pro\*COBOL

Cause: The authorization or license to run the Pro\*COBOL Precompiler has expired.

Action: Call customer support for assistance.

PCC-01001: Your Pro\*COBOL authorization is about to expire

Cause: The authorization or license to run the Pro\*COBOL Precompiler is about to expire.

Action: Call customer support for assistance.

PCC-01002: Invalid character "character" in indicator area at line number in file string

Cause: In a Pro\*COBOL Precompiler program, only a blank, hyphen (-), asterisk (\*), slash (/), or letter "D" is allowed in the indicator area, but the precompiler found another character.

Action: Remove or replace the invalid character. If the FORMAT=ANSI option is specified, check for an end-of-line in column 7.

PCC-01003: Invalid continuation at line number in file string

Cause: In a PRO\*COBOL program, a continuation line was completely blank, except for the continuation character.

Action: Remove or replace the empty continuation line.

PCC-01004: In an EXEC statement at end-of-file

Cause: In a Pro\*COBOL input file, the last EXEC statement was not terminated properly.

Action: Terminate the last EXEC statement with an END-EXEC.

PCC-01005: PROCEDURE DIVISION not found

Cause: The precompiler could not find the PROCEDURE DIVISION header in a Pro\*COBOL program. Some possible causes follow:

o A keyword in the header is missing or misspelled.

o There is an apostrophe in the REMARKS section (the precompiler mistook the apostrophe for the beginning of a string literal).

o There is an unterminated literal in the WORKING-STORAGE SECTION.

o The wrong value for the FORMAT option was specified.

Action: Check that the PROCEDURE DIVISION header is in place and spelled correctly, that there is no apostrophe in the REMARKS section, that all literals in the WORKING-STORAGE SECTION are terminated, and that the right value for the FORMAT option is specified.

PCC-01006: EXEC statement cannot begin in Area A at line number in file string

Cause: In a Pro\*COBOL program, EXEC statements must begin in Area B, but the precompiler found a statement beginning in Area A.

Action: Move the statement rightward so that it begins in Area B.

PCC-01007: WORKING-STORAGE SECTION not found

Cause: The precompiler could not find the WORKING-STORAGE SECTION header in a Pro\*COBOL program, probably because a keyword is missing or misspelled, or the wrong value for the FORMAT option might have been specified.

Action: Check that the WORKING-STORAGE SECTION header is in place and spelled correctly and that the right value for the FORMAT option is specified.

PCC-01008: Multiple element records not allowed in DECLARE section

Cause: A few COBOL compilers do not allow group items to be passed as parameters in a CALL statement. (Check the COBOL compiler user's guide.) If the compiler is one of these, group items within the Declare Section can contain only one elementary item.

Action: Assign each host variable its own group item.

PCC-01009: For hostlan = COB74, a SQL statement must be followed by ELSE or "."

Cause: In a Pro\*COBOL program, an EXEC SQL statement is followed by another statement in the same sentence. An EXEC SQL statement must be the last statement in a COBOL-74 sentence and so must be terminated by the keyword ELSE or a period.

Action: Change the program logic, making the EXEC SQL statement the last statement in the sentence.

PCC-01010: Invalid use of NULL character in character literal

Cause: A null character (binary zero) was found in a string literal. This is not allowed by Pro\*COBOL.

Action: Remove the null character from the string literal.

PCC-01011: USAGE IS BINARY clause must be terminated by "." on same line

Cause: The period terminating the USAGE IS BINARY clause must be on the same line as the USAGE clause. This message only occurs on systems that support the COMP5=YES command line option of Pro\*COBOL, where where COMP-5 is substituted for BINARY.

Action: Check that the period terminating the USAGE IS BINARY clause is on the same line as the USAGE clause.

PCC-01012: DATA DIVISION not found

Cause: The Pro\*COBOL precompiler did not find a DATA DIVISION in the input source file. Pro\*COBOL applications are required to have a DATA DIVISION.

Action: Add a DATA DIVISION to the input source file.

PCC-01013: Invalid use of PIC N array variable "string" at line number in file string

Cause: A PIC N variable was declared using an OCCURS clause. Tables of PIC N variables are not supported by the Pro\*COBOL precompiler.

Action: Declare the PIC N variable without an OCCURS clause or, if the PIC N variable is not used in any SQL statements, declare it outside the Declare Section.

PCC-01014: "VARYING" not supported with PIC N PICTURE clause

Cause: The keyword VARYING was used in a PIC N variable declaration.

Action: Remove the keyword VARYING from the variable declaration. If you want to declare a PIC N VARCHAR variable, specify the precompiler option VARCHAR=YES and declare the variable as an implicit VARCHAR group item as illustrated by the following example: EXEC SQL BEGIN DECLARE SECTION END-EXEC.... 01 ENAME. 05 ENAME-LEN PIC S9(4) COMP. 05 ENAME-ARR PIC N(20).... EXEC SQL END DECLARE SECTION END-EXEC.

PCC-01015: Cannot equivalence PIC N variable string

Cause: A PIC N variable or an implicit VARCHAR group item (with a PIC N variable as an elementary item) was used in an EXEC SQL VAR statement. This is not allowed.

Action: Do not use the PIC N variable in an EXEC SQL VAR statement. If you want an equivalence to an Oracle type using an EXEC SQL VAR statement, use a PIC X variable, instead of a PIC N variable.

PCC-01016: "N" character literals not supported in embedded PL/SQL

Cause: An "N" character literal was used within a PL/SQL block

Action: Remove the "N" character literal from the PL/SQL block.

PCC-01017: The SQLCA and a SQLCODE variable cannot both be used

Cause: The SQLCA has been included and a SQLCODE variable has been declared. This is not allowed as references to the SQLCODE variable are ambiguous and will result in COBOL compiler errors.

Action: Use either the SQLCA or the SQLCODE variable. Remove either the include of the SQLCA or the SQLCODE variable declaration.

PCC-01018: Conversion buffer size can only be specified for character types

Cause: A CONVBUFSZ clause has been used in an EXEC SQL VAR statement where the variable is not of a character datatype.

Action: Remove the CONVBUFSZ clause from the EXEC SQL VAR statement.

PCC-01019: Invalid conversion buffer size

Cause: The size specified in a CONVBUFSZ clause must be an integer in the range 1-32765. Either the size given is not an integer or is outside the required range.

Action: Specify an integer in the range 1-32765.

PCC-01100: You are not authorized to run Pro\*FORTRAN

Cause: The authorization or license to run the Pro\*FORTRAN Precompiler has expired.

Action: Call customer support for assistance.

PCC-01101: Your Pro\*FORTRAN authorization is about to expire

Cause: The authorization or license to run the Pro\*FORTRAN Precompiler is about to expire.

Action: Call customer support for assistance.

PCC-01102: Invalid label at line number in file string

Cause: The Pro\*FORTRAN Precompiler found an invalid FORTRAN statement label in columns 1 through 6.

Action: Correct or remove the statement label.

PCC-01200: You are not authorized to run Pro\*C

Cause: The authorization or license to run the Pro\*C Precompiler has expired.

Action: Call customer support for assistance.

PCC-01201: Your Pro\*C authorization is about to expire

Cause: The authorization or license to run the Pro\*C Precompiler is about to expire.

Action: Call customer support for assistance.

PCC-01202: Identifier "string" truncated to 31 characters

Cause: A host identifier (the name of a host variable, for example) was truncated to the maximum length (31 characters) allowed by the precompiler.

Action: No action required. This message is just informational.

PCC-01300: You are not authorized to run Pro\*PL/I

Cause: The authorization or license to run the Pro\*PL/I Precompiler has expired.

Action: Call customer support for assistance.

PCC-01301: Your Pro\*PL/I authorization is about to expire

Cause: The authorization or license to run the Pro\*PL/I Precompiler is about to expire.

Action: Call customer support for assistance.

PCC-01400: You are not authorized to run Pro\*Pascal

Cause: The authorization or license to run the Pro\*Pascal Precompiler has expired.

Action: Call customer support for assistance.

PCC-01401: Your Pro\*Pascal authorization is about to expire

Cause: The authorization or license to run the Pro\*Pascal Precompiler is about to expire.

Action: Call customer support for assistance.

PCC-01500: You are not authorized to run Pro\*Ada

Cause: The authorization or license to run the Pro\*Ada Precompiler has expired.

Action: Call customer support for assistance.

PCC-01501: Your Pro\*Ada authorization is about to expire

Cause: The authorization or license to run the Pro\*Ada Precompiler is about to expire.

Action: Call customer support for assistance.

PCC-01510: No Package, Procedure or Function statement seen in string

Cause: Every Ada source file must have a package, procedure, or function statement. The precompiler did not find one.

Action: Add the appropriate statement(s) to the source file and rerun Pro\*Ada.

PCC-01511: Identifier on line number in file string too long for code generated in file string

Cause: An identifier used in the host program is of a length that causes precompiler-generated code to exceed the length limitation on source lines.

Action: Use a shorter identifier or use the ORECLEN option to increase the allowed line length.

PCC-01512: Invalid EXEC SQL INCLUDE of file string found at line number in file string

Cause: The EXEC SQL INCLUDE statement is not allowed in Pro\*Ada.

Action: Embed required source text directly in the Pro\*Ada file. Use the "with" context clause to include required packages.

PCC-01513: FIPS warning: Unsupported datatype in line number of file string

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, a host variable was declared with a non-ANSI/ISO standard type.

Action: No action required. However, for ANSI/ISO compliance, use only ANSI/ISO standard types.

PCC-01515: FIPS warning: Undeclared host variable "string" at line number in file string

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, a host variable was declared outside of a Declare Section.

Action: No action required. However, for ANSI/ISO compliance, declare the host variable within a Declare Section.