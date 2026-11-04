---
title: PCB-00001 to PCB-00903
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/pcbus.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 108 PCB-00001 to PCB-00903

PCB-00001: string

Cause: This is a generic error message from the command-line processor.

Action: Correct the indicated error.

PCB-00002: Command line processor severe error

Cause: The command line processor encountered a severe error.

Action: After making sure that all the command-line options are specified correctly, call customer support with a full account of all the options and configuration files used.

PCB-00003: Value of DBMS option invalid with given value of MODE option

Cause: When MODE={ANSI14 | ANSI13}, DBMS=V7 or V8 was specified, or when MODE=ANSI, DBMS=v6 was specified. These option settings are incompatible. Note that the DBMS option was not available before release 1.5 of the Oracle Precompilers.

Action: With DBMS=V7 or V8, instead of MODE={ANSI14 | ANSI13}, specify MODE={ANSI | ORACLE}. With DBMS=V6, instead of MODE=ANSI, specify MODE={ANSI14 | ANSI13 | ORACLE}, but MODE=ORACLE is recommended.

PCB-00004: UNSAFE\_NULL=YES must be used with DBMS=V7 or V8 and MODE=ORACLE

Cause: The option UNSAFE\_NULL=YES has been used with DBMS=V6 or DBMS=NATIVE (the default) or has been used with MODE=ANSI/ANSI14/ANSI13.

Action: Use DBMS=V7 or V8 and MODE=ORACLE (the default) when using UNSAFE\_NULL=YES or do not use UNSAFE\_NULL=YES.

PCB-00005: Command line option MODE=ANSI required with option NLS\_LOCAL=YES

Cause: The precompiler option NLS\_LOCAL=YES was used without also specifying MODE=ANSI. The precompiler option MODE=ANSI must be specifiied if NLS\_LOCAL=YES.

Action: Set the precompiler option MODE=ANSI in addition to NLS\_LOCAL=YES or do not set NLS\_LOCAL=YES.

PCB-00006: Userid only used when SQLCHECK=FULL, userid ignored.

Cause: The USERID option was specified when SQLCHECK={SYNTAX | NONE}. This is unnecessary.

Action: Specify the USERID option only when SQLCHECK=SEMANTICS.

PCB-00007: string

Cause: This is a generic error message from the command-line processor.

Action: Correct the indicated error.

PCB-00008: Must use option SQLCHECK=SEMANTICS(FULL) when there is embedded PL/SQL

Cause: The precompiler tried to parse an embedded PL/SQL block when SQLCHECK={SYNTAX | NONE}. PL/SQL blocks can be parsed only when SQLCHECK=SEMANTICS is specified.

Action: Remove the PL/SQL block or specify SQLCHECK=SEMANTICS.

PCB-00009: Cannot change MAXLITERAL after an EXEC SQL statement

Cause: The MAXLITERAL option has been used in an inline EXEC ORACLE OPTION statement after and EXEC SQL, EXEC TOOLS, or EXEC IAF statement. This is not allowed.

Action: Use the MAXLITERAL option only on the command line or in an EXEC ORACLE OPTION statement placed at the beginning of the input source file.

PCB-00010: SQLCHECK value in EXEC ORACLE statement exceeds command line value

Cause: The SQLCHECK option was entered inline and specified a level of checking higher than the level specified (or accepted by default) on the command line. This is not allowed. For example, if SQLCHECK={SYNTAX | LIMITED} is specified on the command line, SQLCHECK={SEMANTICS | FULL} cannot be specified inline. This informational message is; the precompiler ignores the inline value and continues processing.

Action: Revise the EXEC ORACLE statement or specify a lower level of checking on the command line.

PCB-00011: DBMS=V6 no longer supported; using DBMS=NATIVE

Cause: V6 compatibility is no longer supported. The precompiler will precompile as though DBMS=NATIVE was specified.

Action: Revise the specified DBMS option value from v6 to another value as desired.

PCB-00012: Command line option DYNAMIC=ANSI required with option TYPE\_CODE=ANSI

Cause: The precompiler option TYPE\_CODE=ANSI was used without also specifying DYNAMIC=ANSI. The precompiler option DYNAMIC=ANSI must be specifiied if TYPE\_CODE=ANSI.

Action: Set the precompiler option DYNAMIC=ANSI in addition to TYPE\_CODE=ANSI or do not set TYPE\_CODE=ANSI.

PCB-00013: Must use option SQLCHECK=SEMANTICS(FULL) when option OUTLINE is used

Cause: The precompiler option OUTLINE was used without also specifying SQLCHECK=SEMANTICS(FULL).

Action: Set the precompiler option SQLCHECK=SEMANTICS(FULL).

PCB-00014: Must use option OUTLINE when option OUTLNPREFIX is used

Cause: The precompiler option OUTLNPREFIX was used without also specifying OUTLINE=YES|<category\_name>. The precompiler option OUTLINE must be specifiied if OUTLNPREFIX is used.

Action: Set the precompiler option OUTLINE=YES|<category\_name>

PCB-00015: Must use option OUTLINE when option RUNOUTLINE is used

Cause: The precompiler option RUNOUTLINE was used without also specifying OUTLINE=YES|<category\_name>. The precompiler option OUTLINE must be specifiied if RUNOUTLINE is used.

Action: Set the precompiler option OUTLINE=YES|<category\_name>

PCB-00016: Semantic checking disabled by TimesTen.

Cause: Semantic checking is not supported by TimesTen.

Action: This is an informational message only.

PCB-00100: Unable to reopen temporary file string

Cause: The precompiler was unable to reopen a temporary file. Some possible causes follow:

o File access privileges are insufficient.

o Another user has locked the file.

o There is not enough disk space.

o There are too many open files.

Action: Check that sufficient privileges have been granted to access the file, and that it is not locked by another user. Also check that there is enough disk space and that the limit for open files is set high enough (check with the system manager).

PCB-00101: Could not find or open system configuration file

Cause: The precompiler was unable to open the system configuration file. The system configuration file does not exist or is not in the proper directory.

Action: Check that the system configuration file is in the proper directory. See Oracle installation documentation for where this should be. Put a new copy of pcccob.cfg with desired default options in the proper directory.

PCB-00102: Input file name length exceeds the maximum length

Cause: The file name length specified exceeded the maximum length. Some operating systems have a maximum file name length.

Action: Use a file name of length less than or equal to the maximum platform specific file name length.

PCB-00103: Unable to open generated outline sql file "string"

Cause: The precompiler was unable to open the input file specified in the INCLUDE statement. Some possible causes follow:

o The filename is misspelled.

o The file does not exist.

o The search path to the file is incorrect.

o File access privileges are insufficient.

o There is not enough disk space.

o There are too many open files.

Action: Check that the file exists, that the search path to the file is correct, that sufficient privileges to access the file have been granted, and that it is not locked by another user. Also, check that there is enough disk space and that the limit for open files is set high enough (check with the system manager).

PCB-00104: Unable to open input file "string"

Cause: The precompiler was unable to open the input file specified by the INAME precompiler option. Some possible causes follow:

o The filename is misspelled.

o The file does not exist.

o The search path to the file is incorrect.

o File access privileges are insufficient.

o Another user has locked the file.

o There is not enough disk space.

o There are too many open files.

Action: Check that the file exists, that the search path to the file is correct, that sufficient privileges have been granted to access the file, and that it is not locked by another user. Also check that there is enough disk space and that the limit for open files is set high enough (check with the system manager).

PCB-00105: Included file name "string" exceeds name limit of number characters

Cause: The file name length specified exceeded the maximum length. Some operating systems have a maximum file name length.

Action: Use a file name of length less than or equal to the maximum platform specific file name length.

PCB-00106: Unable to open INCLUDE file "string"

Cause: The precompiler was unable to open the input file specified in the INCLUDE statement. Some possible causes follow:

o The filename is misspelled.

o The file does not exist.

o The search path to the file is incorrect.

o File access privileges are insufficient.

o There is not enough disk space.

o There are too many open files.

Action: Check that the file exists, that the search path to the file is correct, that sufficient privileges to access the file have been granted, and that it is not locked by another user. Also, check that there is enough disk space and that the limit for open files is set high enough (check with the system manager).

PCB-00107: Unable to open generated outline log file "string"

Cause: The precompiler was unable to open the input file specified in the INCLUDE statement. Some possible causes follow:

o The filename is misspelled.

o The file does not exist.

o The search path to the file is incorrect.

o File access privileges are insufficient.

o There is not enough disk space.

o There are too many open files.

Action: Check that the file exists, that the search path to the file is correct, that sufficient privileges to access the file have been granted, and that it is not locked by another user. Also, check that there is enough disk space and that the limit for open files is set high enough (check with the system manager).

PCB-00108: Unable to open list file "string"

Cause: The precompiler was unable to open the list file specified by the LNAME precompiler option. Some possible causes follow:

o The filename is misspelled.

o The file does not exist.

o The search path to the file is incorrect.

o File acces privileges are insufficient.

o Another user has locked the file.

o There is not enough disk space.

o There are too many open files.

Action: Check that the file exists, that the search path to the file is correct, that sufficient privileges have been granted to access the file, and that it is not locked by another user. Also check that there is enough disk space and that the limit for open files is set high enough (check with the system manager). If a listing file is not needed, specify LTYPE=NONE on the command line.

PCB-00109: Unable to open generated source file "string"

Cause: The precompiler was unable to open the output file specified by the ONAME precompiler option. Some possible causes follow:

o The filename is misspelled.

o The file does not exist.

o The search path to the file is incorrect.

o File acces privileges are insufficient.

o Another user has locked the file.

o There is not enough disk space.

o There are too many open files.

Action: Check that the file exists, that the search path to the file is correct, that sufficient privileges have been granted to access the file, and that it is not locked by another user. Also check that there is enough disk space and that the limit for open files is set high enough (check with the system manager).

PCB-00110: Unable to open temporary file "string"

Cause: The precompiler was unable to open a file for temporary use. Some possible causes follow:

o File acces privileges are insufficient.

o A file of the same name already exists and is locked.

o There is not enough disk space.

o There are too many open files.

Action: Check that the file exists, that sufficient privileges have been granted to access the file, and that it is not locked. Also check that there is enough disk space and that the limit for open files is set high enough (check with the system manager). "200 - 299, Host variable errors."

PCB-00200: Cannot equivalence PIC N or PIC G variable "string"

Cause: A PIC N/G variable, an implicit VARCHAR group item with a PIC N/G elementary item, or a group item with a PIC N/G elementary item was used in an EXEC SQL VAR statement. This is not allowed.

Action: Do not use the PIC N variable in an EXEC SQL VAR statement. If you want an equivalence to an Oracle type using an EXEC SQL VAR statement, use a PIC X variable, instead of a PIC N variable.

PCB-00201: Indicator variable string not a group item

Cause: The host variable is a group item containing tables. Indicator variables used with this type of host variable must be group items of tables of indicators corresponding the the tables in the group item host variable.

Action: Change the indicator variable to be a group item of indicator tables.

PCB-00202: Indicator variable string not a group item or table

Cause: The host variable is a group item. Indicator variables used with this type of host variable must be a group item or table of indicator variables.

Action: Use a group item or table of indicator variables.

PCB-00203: Nested group item "string" not supported

Cause: The variable used as a host variable was a group item which itself contained other group items.

Action: Remove any group items from the group item to be used as a host variable.

PCB-00204: Group items cannot be used except in INTO or VALUES clause

Cause: A group item host variable was used outside of an INTO or VALUES clause. A group item host variable may be used only in an INTO or VALUES clause.

Action: Do not use a group item outside of an INTO or VALUES clause.

PCB-00205: Cannot use PIC N or PIC G variable in PL/SQL when NLS\_LOCAL=YES

Cause: A PIC N or PIC G variable was used in an embedded PL/SQL block when the precompiler option NLS\_LOCAL=YES was used. A PIC N or PIC G variable is not supported in this situation.

Action: Do not use the PIC N or PIC G variable within the PL/SQL block or use precompiler option NLS\_LOCAL=NO.

PCB-00206: Cannot use N quoted literal in PL/SQL when NLS\_LOCAL=YES

Cause: A "N" literal (a literal of the form N'...') was used within a PL/SQL block when the precompiler option NLS\_LOCAL=YES was used. N literals are not supported in this situation.

Action: Use an ordinary literal (one without the "N") within the PL/SQL block or use precompiler option NLS\_LOCAL=NO.

PCB-00207: Invalid use of PIC N or PIC G table variable when NLS\_LOCAL=YES

Cause: A PIC N variable was declared using an OCCURS clause. Tables of PIC N variables are not supported when NLS\_LOCAL=YES.

Action: Declare the PIC N variable without an OCCURS clause or, do not use the PIC N variable in any SQL statements.

PCB-00208: Incorrect type for host variable "string"

Cause: A variable of unsupported datatype was used in a SQL statement or embedded PL/SQL block.

Action: Use a host variable of a supported datatype.

PCB-00209: Scale is not supported for host variable "string"

Cause: A variable whose format does not support scaling was used in a SQL statement or embedded PL/SQL block. The following formats do not support scaling: PIC S9(n) COMP PIC S9(n) COMP-4 PIC S9(n) COMP-5 PIC S9(n) BINARY PIC 9(n) COMP

Action: Remove the scale or use a datatype that support scaling.

PCB-00210: DISPLAY-1 only allowed with PIC G and PIC N variables "string"

Cause: A variable declared with DISPLAY-1 in the usage clause without PIC G or PIC N in the picture clause was used in a SQL statement.

Action: Replace DISPLAY-1 with DISPLAY or change the picture clause to use PIC N or PIC G.

PCB-00211: VARYING not supported with PIC N or PIC G variable "string"

Cause: The keyword VARYING was used in a PIC N variable declaration.

Action: Remove the keyword VARYING from the variable declaration. If you want to declare a PIC N VARCHAR variable, specify the precompiler option VARCHAR=YES and declare the variable as an implicit VARCHAR group item as illustrated by the following example: EXEC SQL BEGIN DECLARE SECTION END-EXEC.... 01 ENAME. 05 ENAME-LEN PIC S9(4) COMP. 05 ENAME-ARR PIC N(20).... EXEC SQL END DECLARE SECTION END-EXEC.

PCB-00212: PICTURE clause not allowed for host variable "string"

Cause: A variable declared with a PIC clause and COMP-1 or COMP-2 was used in a SQL statement or embedded PL/SQL block.

Action: Remove the PIC clause or use a datatype other than COMP-1 or COMP-2 in the declaration of the variable.

PCB-00214: JUSTIFIED clause not allowed for host variable "string"

Cause: A variable declared with a JUSTIFIED clause was used in a SQL statement or embedded PL/SQL block.

Action: Remove the JUSTIFIED clause from the variable declaration.

PCB-00215: OCCURS TO TIMES clause not allowed for host variable "string"

Cause: A variable declared with an OCCURS clause with the TO TIMES subclause was used in a SQL statement or embedded PL/SQL block.

Action: Remove the TO TIMES subclause from the variable declaration.

PCB-00216: OCCURS ASCENDING/DESCENDING clause not allowed for "string"

Cause: A variable declared with an OCCURS clause with the ASCENDING or DESCENDING KEY IS subclause was used in a SQL statement or embedded PL/SQL block.

Action: Remove the ASCENDING or DESCENDING KEY IS subclause from the variable declaration.

PCB-00217: OCCURS INDEXED clause not allowed for host variable "string"

Cause: A variable declared with an OCCURS INDEXED clause was used in a SQL statement or embedded PL/SQL block.

Action: Remove the OCCURS INDEXED clause from the variable declaration.

PCB-00218: RENAMES clause not allowed for host variable "string"

Cause: A variable declared with a RENAMES clause was used in a SQL statement or embedded PL/SQL block.

Action: Remove the RENAMES clause from the declaration.

PCB-00219: Invalid size specified in EXEC SQL VAR statement

Cause: A size which is specified which is not valid for the specified data type.

Action: Specify a size which is valid for the specified type.

PCB-00220: Invalid scale specified in EXEC SQL VAR statement

Cause: A scale which is specified which is not valid for the specified data type.

Action: Specify a scale which is valid for the specified type.

PCB-00221: OCCURS DEPENDING ON clause not allowed for host variable "string"

Cause: A variable declared with an OCCURS clause with the DEPENDING ON subclause was used in a SQL statement or embedded PL/SQL block.

Action: Remove the DEPENDING ON subclause from the variable declaration.

PCB-00222: Size for host variable string exceeds maximum size

Cause: A variable declared with PIC S9(n), with n greater than what is allowed on the given platform, was used in an embedded sql statement. On 32 bit machines n must not exceed 9, and on 64 bit machines, n must not exceed 18.

Action: Use a smaller number in the picture clause that does not exceed the maximum allowed size on your platform or use COMP-3.

PCB-00223: Undeclared variable "string"

Cause: A variable used in a SQL statement was not declared or its name is misspelled or if option DECLARE\_SECTION=YES the declaration was not in a DECLARE SECTION.

Action: Add or correct the variable declaration.

PCB-00224: Ambiguously referenced variable "string"

Cause: There is more than one variable of the same name and the qualification given was insufficient to determine which variable the reference was to.

Action: Use more complete qualification in the variable reference.

PCB-00225: Undeclared SQL identifier "string"

Cause: The name of a descriptor, statement, or cursor was not declared or is misspelled, or was declared as a different kind of SQL identifier.

Action: Add or correct the descriptor, statement, or cursor declaration.

PCB-00226: SQL identifier "string" already defined

Cause: The SQL identifier (cursor name, statement name, etc.) has already been defined in another way.

Action: Use a different name for this use of the name.

PCB-00227: Undeclared indicator variable "string"

Cause: An indicator variable used in a SQL statement was not declared in the Declare Section or its name is misspelled.

Action: Add or correct the indicator variable declaration.

PCB-00228: Invalid group item variable "string"

Cause: An unacceptable group item variable was used in a SQL statement. or its name is misspelled.

Action: Correct the group item variable declaration or its use in the SQL statement.

PCB-00229: Indicator variable "string" has wrong type or length

Cause: An indicator variable was not declared in the Declare Section as a 2-byte integer. Indicator variables must be defined as 2-byte integers.

Action: Redefine the indicator variable as a 2-byte integer.

PCB-00230: Indicator table size must not be less than its host variable

Cause: An host variable table was used with an indicator table declared with a smaller dimension. For example: EXEC SQL BEGIN DECLARE SECTION END-EXEC. 01 EMP-NUM OCCURS 4 TIMES PIC S9(4) COMP. 01 EMP-NUM-IND OCCURS 2 TIMES PIC S9(4) COMP. EXEC SQL END DECLARE SECTION END-EXEC.... SELECT... INTO EMP-NUM:EMP-NUM-IND...

Action: Increase the size of the indicator table.

PCB-00231: Host and indicator variables may not have the same name.

Cause: In an EXEC SQL statement, an indicator variable had the same name as a host variable. The names of a host variable and its associated indicator variable must be different. Also, an indicator variable cannot be used as a host variable.

Action: Rename the host or indicator variable.

PCB-00232: Tables not allowed as input bind variables in SELECT statement

Cause: A host table was used in the WHERE clause of a SELECT-INTO statement or in the SELECT list of a SELECT-INTO statement.

Action: Rewrite the SELECT statement without using tables or use a cursor.

PCB-00233: Table size mismatch in INTO/USING. Minimum is: number

Cause: The size of an table variable in an INTO/USING clause is too small for the number of rows processed.

Action: Declare all table variables in the INTO/USING clause to have at least the minimum dimension given.

PCB-00234: FOR variable "string" is invalid type

Cause: The count variable in a FOR clause has the wrong datatype. The datatype must be NUMBER or LONG (or be compatible with NUMBER or LONG).

Action: Check the declaration and check that the count variable has a datatype of NUMBER or LONG (or a compatible Oracle or host-language datatype).

PCB-00235: Table size mismatch in INTO/USING. Minimum is: number

Cause: The size of a table variable in an INTO/USING clause of a dynamic EXECUTE statement has been ARRAYLEN...EXECUTE'd while the other host variable has not and is not a table of dimension 1 or a plain non-table host variable. Example: 01 X PIC X(10) OCCURS 10. 01 Y PIC S9(4) COMP OCCURS 10. 01 Z PIC S9(4) COMP.... EXEC SQL ARRAYLEN X (DIM) EXECUTE END-EXEC.... EXEC SQL EXECUTE S1 USING:X,:Y END-EXEC. <-- error EXEC SQL EXECUTE S1 USING:X,:Z END-EXEC. <-- ok Please note that this error differs from 233 in that it is an ERROR not a WARNING.

Action: ARRAYLEN...EXECUTE all of the table variables in the INTO/USING clause or those host variables not ARRAYLEN...EXECUTEd need to be of dimension 1.

PCB-00236: Cannot use PIC N/G variable. NLS\_NCHAR not set or set incorrectly.

Cause: To use PIC N or PIC G variables as host variables, both of the environment variables NLS\_LANG and NLS\_NCHAR must be set with correct values. One of the following problems has occurred which prevents Pro\*COBOL from accepting PIC N and PIC G variables as host variables: 1) One or both of NLS\_LANG and NLS\_NCHAR are not set at all. 2) NLS\_LANG is not set with a valid language, territory, or character set. 3) NLS\_NCHAR is not set to a valid NCHAR character set. 4) The character set specified by NLS\_NCHAR is not a fixed width character set. Pro\*COBOL can only use fixed width character sets for PIC N or PIC G host variables.

Action: Set the NLS\_NCHAR environment variable to a valid fixed width character set name. Set NLS\_LANG with a valid language, territory, and character set.

PCB-00237: Declaration of "string" cannot have a level number greater than 48

Cause: A VARYING or SQL-CURSOR declaration has been encountered which has the level number greater than 48.

Action: Change the level to 48 or less.

PCB-00238: Element of this table group item host variable cannot be a table

Cause: A group item that is a table and having an element that is a table was used in a SQL statement.

Action: Remove the OCCURS clause from the element of the group item.

PCB-00239: Element of a table group item indicator cannot be table or group item

Cause: A group item that is a table and used as an indicator has an element that is a table or group item.

Action: Change the nested table or group item in the indicator so that it is an elementary item.

PCB-00240: Group item containing this host variable cannot be table

Cause: An elementary item belonging to a group item with an OCCURS clause has been referenced. This is not allowed.

Action: Change the elementary item used to an item that is not an element of a table of group items.

PCB-00241: A host variable is required here

Cause: The COUNT item in the dynamic SQL statement must be a host variable but is not.

Action: Use a host variable in the COUNT item of the dynamic SQL statement.

PCB-00242: A host variable or exact numeric constant is required here

Cause: The particular item in the dynamic SQL statement is required to be a host variable or exact numeric (integer) constant, but is not.

Action: Change the item in the dynamic SQL statement to use a host variable or exact numeric constant. "300 - 399: FIPS flagging error messages."

PCB-00300: Datatype for host variable not supported by ANSI "string"

Cause: An Oracle extension to the ANSI/ISO standard was used. Specifically, aa pointer or nonconforming datatype such as VARCHAR was used. For example, the offending code might look like: EXEC SQL BEGIN DECLARE SECTION END-EXEC. 01 USERNAME PIC X(10) VARYING. EXEC SQL END DECLARE SECTION END-EXEC. This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: None

PCB-00301: Use of non-ANSI function is an Oracle extension

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, a non-ANSI function was used. This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action is required. However, for ANSI/ISO compliance, do not use this function.

PCB-00302: This statement is not supported by ANSI

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, a nonconforming SQL statement such as PREPARE was used. For example, the offending code might look like: EXEC SQL PREPARE SQL-STMT FROM:HV END-EXEC. This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action required. However, for ANSI/ISO compliance, do not use the nonconforming statement.

PCB-00303: Dynamic SQL and PL/SQL are Oracle extensions to ANSI SQL

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, dynamic SQL or embedded PL/SQL was used. For example, the offending code might look like: EXEC SQL EXECUTE BEGIN SELECT... END; END-EXEC. This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action required. However, for ANSI/ISO compliance, do not use dynamic SQL or embedded PL/SQL.

PCB-00304: Oracle extension to the WHENEVER statement

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, a nonconforming keyword such as NOTFOUND, STOP, RAISE, or DO was used in the WHENEVER statement. (Note that NOT FOUND is ANSI-compliant.) For example, the offending code might look like: EXEC SQL WHENEVER SQLERROR STOP END-EXEC. This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action required. However, for ANSI/ISO compliance, do not use the nonconforming keyword.

PCB-00305: Oracle extension to the COMMIT and ROLLBACK statements

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, the parameter RELEASE, COMMENT, or FORCE were used in a COMMIT or ROLLBACK statement. For example, the offending code might look like: EXEC SQL ROLLBACK RELEASE END-EXEC. This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action required. However, for ANSI/ISO compliance, do not use the nonconforming parameter.

PCB-00306: CREATE FUNCTION/PROCEDURE/PACKAGE/TRIGGER are Oracle extensions

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, one of the following statements was used:

o CREATE FUNCTION

o CREATE PROCEDURE

o CREATE PACKAGE

o CREATE TRIGGER This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action is required. However, for ANSI/ISO compliance, do not use any of these statements.

PCB-00307: DROP TABLE statement is an Oracle extension

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, the DROP TABLE statement was used. This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action is required. However, for ANSI/ISO compliance, do not use the DROP statement.

PCB-00308: FOR clause is an Oracle extension

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, the FOR clause was used in an table-processing SQL statement. For example, the offending code might look like: EXEC SQL FOR:LIMIT INSERT INTO EMP (EMPNO, JOB, DEPTNO) VALUES (:EMPNUM,:JOB,:DEPTNO) END-EXEC. This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action required. However, for ANSI/ISO compliance, do not use the FOR clause.

PCB-00309: The CONNECT statement is Oracle implementation dependent

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, the CONNECT statement was used to log on to ORACLE. For example, the offending code might look like: EXEC SQL CONNECT:USERNAME IDENTIFIED BY:PSSWORD END-EXEC. This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action required. However, for ANSI/ISO compliance, specify the AUTO\_CONNECT command-line option instead of using a CONNECT statement.

PCB-00310: AT clause is an Oracle extension

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, the AT <db\_name> clause was used in a SQL statement. For example, the offending code might look like: EXEC SQL AT oracle3 COMMIT RELEASE END-EXEC. This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action required. However, for ANSI/ISO compliance, do not use the AT <db\_name> clause.

PCB-00311: Datatype equivalencing is an Oracle extension

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, the EXEC SQL VAR statement was used.

Action: No action required. However, for ANSI/ISO compliance, do not use the EXEC SQL VAR statement.

PCB-00312: Keyword WORK required here by ANSI

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, the keyword WORK was used in a COMMIT or ROLLBACK statement. For example, the offending code might look like: EXEC SQL COMMIT WORK RELEASE END-EXEC. This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action required. However, for ANSI/ISO compliance, do not use the keyword WORK.

PCB-00313: TO SAVEPOINT clause is an Oracle extension

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, the TO SAVEPOINT <save\_id> clause was used in a ROLLBACK statement.

Action: No action required. However, for ANSI/ISO compliance, do not use the TO SAVEPOINT clause.

PCB-00314: DECLARE DATABASE is an Oracle extension

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, the DECLARE DATABASE statement was used.

Action: No action required. However, for ANSI/ISO compliance, do not use this statement.

PCB-00315: DECLARE TABLE is an Oracle extension

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, the DECLARE TABLE statement was used.

Action: No action required. However, for ANSI/ISO compliance, do not use this statement.

PCB-00316: SQL FORMS statements are Oracle extensions

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, the one of the following statements was used:

o EXEC IAF GET

o EXEC IAF PUT

o EXEC TOOLS GET

o EXEC TOOLS SET This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action is required. However, for ANSI/ISO compliance, do not use any of these statements.

PCB-00317: Group item host variables are Oracle extensions

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, a group item variable was used as a host variable. This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action is required. However, for ANSI/ISO compliance, do not use group items as host variables.

PCB-00318: ARRAYLEN is an Oracle extension

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, the ARRAYLEN statement was used. This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action is required. However, for ANSI/ISO compliance, do not use this statement.

PCB-00319: EXEC ORACLE statements are an Oracle extension

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, an EXEC ORACLE statement was used. This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action is required. However, for ANSI/ISO compliance, do not use this statement.

PCB-00320: VARYING host variable "string" is an Oracle extension

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, a variable declared of VARYING type was used in a SQL statement. This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action is required. However, for ANSI/ISO compliance, do not use this statement.

PCB-00321: Implicit varchar host variables are an Oracle extension

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, an iimplicit varchar variable was used in a SQL statement. This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action is required. However, for ANSI/ISO compliance, do not use this statement.

PCB-00322: EXEC SQL LOB statements an Oracle extension

Cause: An Oracle extension to the ANSI/ISO SQL standard was used. Specifically, an EXEC SQL LOB statement was used. This informational message is issued by the FIPS Flagger when FIPS=YES.

Action: No action is required. However, for ANSI/ISO compliance, do not use this statement. "400 - 499, Tokenizer or parsing errors."

PCB-00400: string

Cause: A syntax error was found.

Action: Do the appropriate action to fix the indicated error.

PCB-00401: Character string not properly terminated

Cause: The character string was not terminated with a quote or apostrophe as appropriate or line continuation was not correct.

Action: Check that the character string is terminated properly and that line continuation syntax is correct.

PCB-00402: Pseudo-text not properly terminated

Cause: A block of pseudo-text has not been properly terminated with "==".

Action: Terminate the pseudo-text at the appropriate place with "==". "500 - 649, Other semantic errors grouped by these features: threads, result set cursors, miscellaneous, pl/sql (includes arraylen), exec tools and lobs."

PCB-00403: EXEC statement cannot begin in Area A

Cause: An EXEC statement began in Area A (before column 12).

Action: Shift the EXEC statement to the right to start it in Area B (in or after column 12).

PCB-00404: string

Cause: A syntax error was found.

Action: Do the appropriate action to fix the indicated error. "500 - 524, Threads"

PCB-00500: No EXEC SQL CONTEXT USE statement encountered

Cause: No EXEC SQL CONTEXT USE statement was encountered and the option threads=yes was requested.

Action: Ensure that the necessary context variable (of type sql-context) has been declared, ALLOCATEd, and USEd prior to any executable SQL statements.

PCB-00501: Runtime context variable "string" not of correct type

Cause: The runtime context variable referenced in an EXEC SQL CONTEXT USE statement is not of type sql\_context.

Action: Declare your runtime context variable of type sql\_context.

PCB-00502: This statement can only be used with THREADS=YES

Cause: EXEC SQL ENABLE THREADS has been used, even though option THREADS is set to NO.

Action: Specify option THREADS=YES or remove the EXEC ENABLE THREADS statement from the source code. "525 - 549, Result Set Cursors"

PCB-00525: Use of the AT clause is not permitted here

Cause: An explicit AT clause was used with an ALLOCATE statement or a FETCH/CLOSE statement also using a sql-cursor declaration.

Action: Remove the AT clause. "550 - 574, Miscellaneous"

PCB-00550: Unable to log on to ORACLE with "string". ORACLE error number: number

Cause: The precompiler was unable to log on to ORACLE with the specified username and password. An ORACLE error with given number occurred when the logon was attempted.

Action:.

PCB-00551: The SQLCA has already been included

Cause: The precompiler has encountered an include SQLCA statement after SQLCA has already been included. The SQLCA can only be included once.

Action: Remove the duplicate include SQLCA statement.

PCB-00552: The SQLCA and a SQLCODE variable cannot both be used

Cause: The SQLCA has been included and a SQLCODE variable has been declared. This is not allowed as references to the SQLCODE variable are ambiguous and will result in COBOL compiler errors.

Action: Use either the SQLCA or the SQLCODE variable. Remove either the include of the SQLCA or the SQLCODE variable declaration.

PCB-00553: FOR clause not allowed on this statement

Cause: A FOR clause was used with a SELECT, LOB, or DEALLOCATE DESCRIPTOR statement. A FOR clause cannot be used with these statements. In the case of a SELECT statement, data returned from the last loop in the execution of the SELECT would overwrite data returned in a previous loop.

Action: Remove the FOR clause from the statement. Use a host language construct to iteratively execute the statement.

PCB-00554: Must include SQLCA when mode=ANSI and WHENEVER SQLWARNING used

Cause: When MODE={ANSI | ANSI14}, an attempt was made to use the WHENEVER SQLWARNING statement without declaring the SQLCA. When MODE={ANSI | ANSI14}, declaring the SQLCA is optional, but to use the WHENEVER SQLWARNING statement, the SQLCA must be declared.

Action: Remove all WHENEVER SQLWARNING statements from the program or declare the SQLCA by hardcoding it or copying it into the program with the INCLUDE statement.

PCB-00555: Using WHERE CURRENT OF on cursor defined without FOR UPDATE clause

Cause: if mode=ORACLE, then a cursor defined with a WHERE CURRENT OF clause must also have a FOR UPDATE clause.

Action: Rewrite the cursor definition.

PCB-00556: Unrecoverable error. Fix previous errors and re-precompile

Cause: A fatal parsing error or token stack overflow error has been encountered.

Action: Fix the syntax error that is causing the parsing error.

PCB-00557: USING clause can only be used on a PREPAREd dynamic statement

Cause: A severe semantics error occurred because the USING clause was used with the OPEN cursor statement and the cursor declaration is not for a PREPAREd statement. The correct sequence of statements should be like: EXEC SQL prepare sv from:sel\_stmt END-EXEC. EXEC SQL declare csv cursor for sv END-EXEC. EXEC SQL open csv USING:hv1,:hv2 END-EXEC.

Action: Use the prepare statement for the sql statement and use that in the declare cursor statement.

PCB-00558: Invalid external datatype specified in EXEC SQL VAR statement

Cause: An invalid external datatype was specified in the EXEC SQL VAR statement.

Action: Specify a valid external datatype. "575 - 599, PL/SQL (including ARRAYLEN)"

PCB-00559: Cursor was not declared in scrollable mode

Cause: A cursor which was not DECLAREd in SCROLL mode was used in scrollable mode in the FETCH statement.

Action: Declare the cursor in scroll mode using the SCROLL keyword.

PCB-00560: Value of offset cannot be negative in ABSOLUTE orientation mode

Cause: The offset for the FETCH ABSOLUTE statement is negative.

Action: Value of offset should be positive.

PCB-00575: PLS-number: string

Cause: Refer to the indicated PL/SQL error message for the indicated condition.

Action: Refer to the indicated PL/SQL error message to correct the SQL statement or embedded PL/SQL block.

PCB-00576: PLS-number: string

Cause: The precompiler found an error in an embedded SQL statement or PL/SQL block.

Action: Refer to the indicated PL/SQL error message to correct the SQL statement or embedded PL/SQL block.

PCB-00577: Use of ARRAYLEN with host tables in SQL statements is ignored

Cause: ARRAYLEN is only valid with PL/SQL.

Action: Use an appropriate table type.

PCB-00578: Variable "string" must be a table

Cause: In an ARRAYLEN statement, the name of a previously declared host table was not specified. The first host variable in an ARRAYLEN statement must be a table. The second host variable, which specifies an array dimension, must be a 4-byte integer. The correct syntax follows: EXEC SQL ARRAYLEN HTABLE (DIM) END-EXEC. The ARRAYLEN statement must appear along with, but somewhere after, the declarations of host\_table and dimension.

Action: Check the spelling of both identifiers in the ARRAYLEN statement. If necessary, supply the missing host table name.

PCB-00579: Invalid ARRAYLEN length variable type for "string"

Cause: A valid table dimension was not specified in an ARRAYLEN statement. The table dimension must be specified using a previously declared 4-byte integer host variable, not a literal or expression. For example, the offending code might look like: EXEC SQL ARRAYLEN ETABLE (25) END-EXEC. -- illegal dimension

Action: Supply a valid table dimension. If necessary, declare a 4-byte integer host variable for use in the ARRAYLEN statement.

PCB-00580: Previous use of host variable "string" uses different indicator

Cause: Within a PL/SQL statement, a host variable was used with two different indicator variables or was used with an indicator variable in one instance and without an indicator in another instance.

Action: Change all references to the host variable so that they all use the same indicator variable or all use no indicator variable.

PCB-00581: "string" used as both host variable and indicator

Cause: Within a PL/SQL statement, the variable was used as both a host variable and an indicator variable.

Action: Use different variables for host variables and indicator variables. "600 - 624, EXEC TOOLS"

PCB-00600: indicators are not allowed in EXEC IAF statements

Cause: Indicator variables associated with host variables cannot be used in EXEC IAF statements such as GET and PUT in a user exit.

Action: Eliminate the indicator variables. If feasible (for example with Forms V4), use EXEC TOOLS statements, which do allow indicator variables. See the Programmer's Guide to the Oracle Precompilers for more information of EXEC IAF and EXEC TOOLS statements.

PCB-00603: An EXEC TOOLS MESSAGE host variable is not a character type

Cause: If a host variable is used to specify the message in an EXEC TOOLS MESSAGE statement, that host variable must be of a character type.

Action: Declare the message to a host variable of a char type. "625 - 649, EXEC SQL LOB statements"

PCB-00625: An indicator variable is not required with this attribute

Cause: In a LOB DESCRIBE, an indicator variable was used with a host variable when retrieving a LOB attribute that does not require one.

Action: Remove the indicator variable.

PCB-00626: Incompatible LOB types

Cause: A LOB operation was attempted between LOBs whose types were not compatible. For example, When ASSIGNing one LOB to another, both LOBs must be of the same type. If they are not, this error results.

Action: Correct the LOB operation by having it function between LOBs of the same type. This may require a redeclaration of one of the LOBs used in the LOB statement performing the specified operation.

PCB-00627: Host variable is not of character type

Cause: The given host variable was not declared to be of the required character type. In this case, one of several possible character types would have been accepted. However, the host variable type did not match any of them.

Action: Redeclare the problematic host variable, using one of the permitted character types.

PCB-00628: Buffer type is incompatible with LOB type

Cause: This error can occur in either of the following situations

1\. An attempt to READ from a LOB into a buffer whose type was not compatible with the LOB type.

2\. An attempt to WRITE a buffer into a LOB whose type was not compatible with the buffer type.

Action: Either the LOB type or the buffer type needs to be changed so that the LOB and buffer types become compatible for the specified operation.

PCB-00629: Host variable is not of Internal LOB type

Cause: The given host variable was not declared to be an internal LOB. BLOB, CLOB or NCLOB are internal lob types.

Action: Redeclare the host variable using one of the internal LOB types.

PCB-00630: Host variable is not of LOB type

Cause: The given host variable was not declared to be any type of LOB, Internal or External. BLOB, CLOB or NCLOB are internal lob types. BFILE is an external type.

Action: Redeclare the host variable using any of the LOB types, Internal or External.

PCB-00631: Host variable is not an External LOB

Cause: The given host variable was not declared to be an External LOB. BFILE is an external type.

Action: Redeclare the host variable using an External LOB type (BFILE).

PCB-00632: Cannot open an External LOB in READ WRITE mode

Cause: An attempt was made to OPEN a BFILE in READ WRITE mode. Writable BFILEs are currently not supported so this operation is considered erroneous.

Action: Do not open BFILEs using READ WRITE mode. BFILEs can only be OPENed in READ ONLY mode.

PCB-00633: Invalid host variable and attribute pairing

Cause: The host variable and attribute pairing in a LOB DESCRIBE was invalid. Most likely, this was due to some problem with the host variable. For example, this error could occur if the host variable was not declared.

Action: Usually, other, more specific, errors will accompany this one. Correcting some or all of those problems should resolve this error.

PCB-00635: This attribute is only valid for Internal LOB types

Cause: A request for a LOB attribute was made in a LOB DESCRIBE statement in which the given LOB was not of some Internal LOB type.

Action: Replace the LOB host variable in the LOB DESCRIBE with one that was declared to be an Internal LOB.

PCB-00636: This attribute is only valid for External LOB types

Cause: A request for a LOB attribute was made in a LOB DESCRIBE statement in which the given LOB was not an External LOB type (BFILE).

Action: Use an External LOB (BFILE) host variable in the LOB DESCRIBE statement.

PCB-00637: Host variable is not an exact binary integer

Cause: A host variable was given that was not declared to be of some acceptable exact binary integer type. Generally, when this error occurs, a signed or unsigned integer type was expected. Floating point or otherwise imprecise numeric types are considered erroneous.

Action: Replace the problematic host variable with one that was declared using a proper binary integer type.

PCB-00638: This attribute is only valid for internal or external LOB types

Cause: A request for a LOB attribute was made in a LOB DESCRIBE statement in which the given source was not an internal or external LOB type.

Action: Use a LOB host variable in the LOB DESCRIBE statement.

PCB-00639: Cannot specify destination offset in a LOB WRITE APPEND

Cause: A destination offset was specified in a LOB WRITE APPEND statement. The destination offset is assumed to be the end of the LOB so specifying an explicit destination offset is erroneous.

Action: Remove the destination offset from the LOB WRITE APPEND statement. "700 - 725, Dynamic SQL error conditions"

PCB-00700: This statement can only be used with DYNAMIC=ANSI

Cause: One of the following statements was used without specifying DYNAMIC=ANSI:

o EXEC SQL ALLOCATE/DEALLOCATE/GET/SET DESCRIPTOR

o EXEC SQL DESCRIBE OUTPUT/INPUT... USING... \<descriptor name>

o EXEC SQL EXECUTE... INTO...

o EXEC SQL EXECUTE... USING... \<descriptor name>

o EXEC SQL OPEN... INTO...

o EXEC SQL OPEN... USING... \<descriptor name>

o SCROLL in DECLARE CURSOR

o EXEC SQL FETCH \<orientation>... where \<orientation> is NEXT, PRIOR, FIRST, LAST, ABSOLUTE, or RELATIVE

Action: Specify DYNAMIC=ANSI or remove statement(s) like those above.

PCB-00701: MAX OCCURRANCES must be between 1 and 65535

Cause: The value specified in the WITH MAX clause of an EXEC SQL ALLOCATE DESCRIPTOR statement was less than 1 or greater than 65535

Action: Specifiy a value between 1 and 65535 inclusive

PCB-00702: Out-of-range item number

Cause: The value specified in the VALUES clause of an EXEC SQL GET/SET DESCRIPTOR statement was less than one or greater than 65535.

Action: Specify a value between 1 and 65535.

PCB-00725: Outline name length exceeds the allowed limit of number characters

Cause: Outline name <category\_name>\_\<filename>\_\<filetype>\_\<seqno> has exceeded the allowed limit.

Action: Use OUTLNPREFIX option to specify the outline name which will be well in the permitted limit.

PCB-00726: Number of outlines has exceeded the limit

Cause: Number of outlines that can be created has exceeded the file limit. Allowed outlines per file is 10000.

Action: Split the file so that each file can have not more than 10000 outlines.

PCB-00727: Outline cannot be created on statement at line number, column number

Cause: Outline cannot be created as there is a syntax error or outlines are not supported on that statement.

Action: Correct the syntax error in the actual SQL used in the file or refer to "Performance Tuning Guide" for the list of supported statements.

PCB-00901: Pro\*COBOL internal error condition detected (Code = number)

Cause: Pro\*COBOL had detected an abnormal condition in its internal data structures. This error message should not normally ever be produced. Customer service should be contacted to report the error.

Action: Correct any other errors which have been reported. If the internal error still exist, examine the source code where the condition was detected and try modifying in some way. Possibly this will alleviate the internal error condition.

PCB-00902: Unable to read message file, facility PCB

Cause: Pro\*COBOL was unable to access the message file containing message text. The file is possibly corrupt.

Action: Contact customer support for information on reinstalling the Pro\*COBOL message files.

PCB-00903: Pro\*COBOL is unable to initialize its parser function

Cause: Pro\*COBOL was unable to access the message file containing message text. The file is possibly corrupt.

Action: Contact customer support for information on reinstalling the Pro\*COBOL message files.