---
title: "SQL*Loader-00100 to SQL*Loader-03120"
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/ulus.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 35 SQL\*Loader-00100 to SQL\*Loader-03120

SQL\*Loader-00100: Syntax error on command-line

Cause: Possible causes for this error include: placing a positional argument after keyword arguments, misspelling a keyword, not balancing parentheses or quotes, or leaving space between the operator, '=', and an argument.

Action: Check the command syntax and the spelling, then retry.

SQL\*Loader-00101: Invalid argument for username/password

Cause: The username/password argument specified on the command line was not recognized. Another argument (not identified by a keyword) could be in the position where username/password is expected.

Action: Check the format of the username/password argument, which is the first argument on the command line, if arguments are given without keywords.

SQL\*Loader-00102: Invalid control file name on command line

Cause: is the existence of a space between username and password. See error 101, above.

Action: Check the spelling and position of the arguments on the command line.

SQL\*Loader-00103: Invalid log file name on command line

Cause: The log file name specified on the command line was not recognized. It could be misspelled, or another argument (not identified by a keyword) could be in its place.

Action: Check the spelling and position of the arguments on the command line.

SQL\*Loader-00104: Invalid bad file name on command line

Cause: The bad file name specified on the command line was not recognized. It could be misspelled, or another argument (not identified by a keyword) could be in its place.

Action: Correct it.

SQL\*Loader-00105: Invalid data file name on command line

Cause: The datafile name specified on the command line was not recognized. It could be misspelled, or another argument (not identified by a keyword) could be in its place.

Action: Check the spelling and position of the arguments on the command line.

SQL\*Loader-00106: Invalid discard file name on command line

Cause: The discard file name specified on the command line was not recognized. It could be misspelled, or another argument (not identified by a keyword) could be in its place.

Action: Check the spelling and position of the arguments on the command line.

SQL\*Loader-00107: Invalid maximum number of discards

Cause: The argument's value is inappropriate, or another argument (not identified by a keyword) is in its place.

Action: Check the command line and retry.

SQL\*Loader-00108: Invalid number of logical records to load

Cause: The argument's value is inappropriate, or another argument (not identified by a keyword) is in its place.

Action: Check the command line and retry.

SQL\*Loader-00109: Invalid number of logical records to skip

Cause: The argument's value is inappropriate, or another argument (not identified by a keyword) is in its place.

Action: Check the command line and retry.

SQL\*Loader-00110: Invalid maximum number of errors

Cause: The argument's value is inappropriate, or another argument (not identified by a keyword) is in its place.

Action: Check the command line and retry.

SQL\*Loader-00111: Invalid number of rows for bind array or data saves

Cause: The argument's value is inappropriate, or another argument (not identified by a keyword) is in its place.

Action: Check the command line and retry.

SQL\*Loader-00112: Invalid maximum bind array size

Cause: The argument's value is inappropriate, or another argument (not identified by a keyword) is in its place.

Action: Check the command line and retry.

SQL\*Loader-00113: Invalid silent mode option

Cause: The only valid options for the SILENT command-line argument are ALL, ERROR, FEEDBACK, or HEADER. The argument could be misspelled, or another argument (not identified by a keyword) could be in its place.

Action: Check the command line and retry.

SQL\*Loader-00114: Error in OPTIONS statement

Cause: Command line options specified in the SQL\*Loader control file with the OPTIONS clause were found to be incorrect.

Action: Check the format of the OPTIONS clause in the SQL\*Loader control file.

SQL\*Loader-00115: Invalid direct path option

Cause: The only valid options for the DIRECT command-line argument are TRUE or FALSE. The argument could be misspelled, or another argument (not identified by a keyword) could be in its place.

Action: Check the command line and retry.

SQL\*Loader-00116: Error prompting for password

Cause: An internal error has occurred.

Action: Contact customer support.

SQL\*Loader-00118: Invalid parallel load option

Cause: The command-line argument used for the parallel load is incorrect.

Action: Use only TRUE or FALSE as the value for the parallel load option.

SQL\*Loader-00119: Invalid parallel file (data file) name on command line

Cause: The command-line argument for the parallel file was entered incorrectly.

Action: Check the command line argument and retry the operation.

SQL\*Loader-00120: Invalid \_synchro option string

Cause: The command-line argument \_synchro is incorrect.

Action: Use only one of the allowed modes: see ulminv\[\].

SQL\*Loader-00121: Invalid skip\_unusable\_indexes option

Cause: The command line argument for skip\_unusable\_indexes is incorrect.

Action: Use only TRUE or FALSE as the value for the skip\_unusable\_indexes option.

SQL\*Loader-00122: Invalid skip\_index\_maintenance option

Cause: The command line argument for skip\_index\_maintenance is incorrect.

Action: Use only true or falseas the value for the skip\_index\_maintenance option. (Note: only on direct loads!)

SQL\*Loader-00123: specified value for bindsize(number) less than readsize(number)

Cause: The command line argument specified for bindsize was less than the value of readsize.

Action: No action is required. SQL\*Loader automatically adjusts the value of bindsize to equal the value of readsize.

SQL\*Loader-00124: specified value for readsize(number) less than bindsize(number)

Cause: The command line argument specified for readsize was less than the value of bindsize.

Action: No action is required. SQL\*Loader automatically adjusts the value of readsize to equal the value of bindsize.

SQL\*Loader-00125: specified value for readsize(number) less than max\_record\_size(number)

Cause: The command line argument specified for readsize was less than the value of max\_record\_size.

Action: No action is required. SQL\*Loader automatically adjusts the value of readsize to equal the value of max\_record\_size.

SQL\*Loader-00126: Invalid read size

Cause: The argument's value is inappropriate, or another argument (not identified by a keyword) is in its place.

Action: Check the command line and retry.

SQL\*Loader-00127: Invalid maximum record size

Cause: The argument's value is inappropriate, or another argument (not identified by a keyword) is in its place.

Action: Check the command line and retry.

SQL\*Loader-00128: unable to begin a session

Cause: An error occurred when attempting to start a session on the database.

Action: See the message that follows this message for information on the cause of the error.

SQL\*Loader-00129: Invalid number of rows for direct path column array

Cause: The argument's value is inappropriate

Action: Check the command line and retry.

SQL\*Loader-00130: Invalid direct path stream size

Cause: The argument's value is inappropriate

Action: Check the command line and retry.

SQL\*Loader-00131: Invalid multithreading option

Cause: The only valid options for the MULTITHREADING command-line argument are TRUE or FALSE. The argument could be misspelled, or another argument (not identified by a keyword) could be in its place.

Action: Check the command line and retry.

SQL\*Loader-00132: invalid argument for external table option

Cause: The command line argument specified for external\_tables was not TRUE or FALSE

Action: Check the command line and retry.

SQL\*Loader-00133: Can't specify both direct path and external tables

Cause: Both options for direct path and exrernal tables were indicated. Only one of these can be applied at a time.

Action: Change at least one of the parameters to enable only one.

SQL\*Loader-00134: invalid option specified for EXTERNAL\_TABLE parameter

Cause: An invalid value was specified for the EXTERNAL\_TABLE parameter.

Action: Specify one of the following values. NOT\_USED disables use of external tables. GENERATE\_ONLY generates the SQL statements that will use external tables to load the data. EXECUTE both generates the SQL statements and then executes them.

SQL\*Loader-00135: Invalid argument for RESUMABLE

Cause: The command line argument specified for RESUMABLE was not TRUE or FALSE.

Action: Check the command line and retry.

SQL\*Loader-00136: Invalid argument for RESUMABLE\_NAME

Cause: The command line argument specified for RESUMABLE\_NAME was not a valid string.

Action: Check the command line and retry.

SQL\*Loader-00137: Invalid value for RESUMABLE\_TIMEOUT

Cause: The command line argument specified for RESUMABLE\_TIMEOUT was not a valid positive integer.

Action: Check the command line and retry.

SQL\*Loader-00138: Invalid value for DATE\_CACHE

Cause: The command line argument specified for DATE\_CACHE was not a valid positive integer.

Action: Check the command line and retry.

SQL\*Loader-00144: Conflicting load methods: string/string specified.

Cause: External table mode and direct path mode were both specified.

Action: Specify only one load method.

SQL\*Loader-00145: Invalid value for NO\_INDEX\_ERRORS

Cause: The command line argument specified was not a valid boolean.

Action: Check the command line and retry.

SQL\*Loader-00146: Invalid value for \_PARTITION\_MEMORY

Cause: The command line argument specified was not -1, 0, or positive.

Action: Check the command line and retry.

SQL\*Loader-00147: Warning: The NO\_INDEX\_ERRORS parameter is ignored for direct path parallel loads.

Cause: The NO\_INDEX\_ERRORS parameter was specified for a parallel load.

Action: Do not use the NO\_INDEX\_ERRORS parameter for parallel loads.

SQL\*Loader-00200: FORMAT clause should not be present - flat data files only

Cause: SQL/DS FORMAT clause is not supported.

Action: Remove the FORMAT command from the SQL\*Loader control file or

SQL\*Loader-00250: Work data sets are not used by SQL\*Loader

Cause: The SQL\*Loader control file contains a WRKDDN statement. SQL\*Loader ignores this clause.

Action: No action required. This is an informational message.

SQL\*Loader-00251: Sort devices are not used by SQL\*Loader

Cause: The SQL\*Loader control file contains a SORTDEVT statement. SQL\*Loader ignores this clause.

Action: No action required. This is an informational message.

SQL\*Loader-00252: Sort data sets are not used by SQL\*Loader

Cause: The SQL\*Loader control file contains a SORTNUM statement. SQL\*Loader ignores this clause.

Action: No action required. This is an informational message.

SQL\*Loader-00253: DB2 partition number has no significance -- ignored

Cause: The SQL\*Loader control file contains a PART statement. SQL\*Loader ignores this clause.

Action: No action required. This is an informational message.

SQL\*Loader-00254: Cannot have DISCARDFILE specs here when multiple data files

Cause: The SQL\*Loader control file contained multiple INFILE statements and a DISCARDFILE statement was found below the RESUME clause.

Action: Move the DISCARDFILE statement above the RESUME clause, so it is adjacent to one of the INFILE statements.

SQL\*Loader-00255: Log file for error recovery not used by SQL\*Loader

Cause: The SQL\*Loader control file contains a LOG statement. SQL\*Loader ignores this clause.

Action: No action required. This is an informational message.

SQL\*Loader-00256: SORTED INDEXES option allowed only for direct path

Cause: The SQL\*Loader control file contains a SORTED INDEXES statement, but it was not used in a direct path load.

Action: Specify a direct path load with DIRECT=TRUE on the command line, remove the statement from the SQL\*Loader control file, or

SQL\*Loader-00257: TERMINATED BY EOF option not valid with ENCLOSED BY option

Cause: A field description in the SQL\*Loader control file contains both the TERMINATED BY EOF and the ENCLOSED BY options. These options are mutually exclusive.

Action: Remove either or both of the clauses.

SQL\*Loader-00258: Maximum number of SORTED INDEXES (number) exceeded on table string

Cause: There are too many indexes in the SORTED INDEX clause. The message displays the maximum number that are permitted.

Action: Reduce the number of indexes specified in the SORTED INDEX clause or use the conventional path load instead of the direct path load.

SQL\*Loader-00259: Could not escalate DDL share lock to exclusive on table string

Cause: This error occurs when another user has a parse lock on the table, for example, when another user is doing a select on the table. The parse lock should clear momentarily.

Action: Give the parse lock a chance to clear and then retry or else use the conventional path load.

SQL\*Loader-00260: TERMINATED BY EOF option available only with LOBFILE option

Cause: The TERMINATED BY EOF option can be used only when describing data to be loaded from a LOBFILE. It cannot be specified at the table level and it cannot be for data in "regular" data files.

Action: Verify that you have specified the correct option for TERMINATED BY and verify that the TERMINATED BY option is specified for the correct fields.

SQL\*Loader-00261: illegal use of TERMINATED BY for RAW field

Cause: The TERMINATED BY option cannot be used for loading data of type RAW from the data file. The only exception is when loading RAW data from LOBFILES. In that case, you may specify the TERMINATED BY EOF option.

Action: Remove the TERMINATED BY option from the RAW field in the SQL\*Loader control file.

SQL\*Loader-00262: PIECED keyword (on column string) allowed only when path is direct

Cause: The PIECED keyword cannot be used in a conventional path load.

Action: Remove the PIECED keyword or use the direct path load.

SQL\*Loader-00263: PIECED column string must be last specified column in table string

Cause: A column that is not the last column was specified as PIECED.

Action: Remove the PIECED keyword or place the column last.

SQL\*Loader-00264: File mode token string parsed but ignored

Cause: An obsolete file mode token was used in the SQL\*Loader control file. As of Release 1.1 of SQL\*Loader, the file-processing options string is used to control file processing, rather than keywords like STREAM, RECORD, FIXED, and VARIABLE.

Action: No action required. This message is informational. Removing the obsolete keywords will eliminate the message without changing the way in which the datafile is processed.

SQL\*Loader-00265: Unable to get default character set name.

Cause: SQL\*Loader was unable to locate the default character set name for the environment.

Action: Supply a character set name with the CHARACTERSET keyword.

SQL\*Loader-00266: Unable to locate character set handle for string.

Cause: SQL\*Loader could not find the character set handle for the named character set.

Action: Correct the character set name.

SQL\*Loader-00267: Control file must be first data file.

Cause: The SQL\*Loader control file is specified as containing data using the INFILE "\*" clause, but other datafiles were named first.

Action: Move the INFILE "\*" clause so that it is the first datafile declared in the SQL\*Loader control file.

SQL\*Loader-00268: UNRECOVERABLE keyword may be used only in direct path.

Cause: The UNRECOVERABLE keyword can only be specified in the direct path load.

Action: Use the direct path load or remove the keyword. (Conventional path loads are always recoverable).

SQL\*Loader-00269: Null string not allowed as clause comparison text.

Cause: A clause is being compared to a null string.

Action: Modify the clause to compare to at least one character.

SQL\*Loader-00270: TERMINATED BY EOF valid only for CHAR or RAW datatypes

Cause: A field description in the SQL\*Loader control file used the TERMINATED BY EOF option when the field was not a RAW or CHAR datatype.

Action: Modify the SQL\*Loader control file to either remove the TERMINATED BY EOF clause or change the datatype for the field to be CHAR or RAW.

SQL\*Loader-00271: Not a Parallel load. Table level OPTIONS statement ignored.

Cause: A table-level OPTIONS statement was specified for a non-parallel load.

Action: Remove the OPTIONS statement from the SQL\*Loader control file.

SQL\*Loader-00272: Table level OPTIONS statement ignored.

Cause: In the parallel load option, the file specified on the command line overrides the file specified in the SQL\*Loader control file.

Action: Remove the OPTIONS statement from the SQL\*Loader control file.

SQL\*Loader-00273: READBUFFERS may be used only in direct path.

Cause: The READBUFFERS specification was not entered as part of a direct path.

Action: Use the direct path or remove the READBUFFERS specification from the SQL\*Loader control file.

SQL\*Loader-00274: At least 2 read buffers have to be specified.

Cause: Fewer than 2 read buffers have been specified.

Action: Specify at least 2 read buffers in the READBUFFERS statement, in the SQL\*Loader control file.

SQL\*Loader-00275: Data is in control file but "INFILE \*" has not been specified.

Cause: The INFILE specification was not entered in the SQL\*Loader control file.

Action: If data in the SQL\*Loader control file is to be read, specify INFILE \* in the SQL\*Loader control file.

SQL\*Loader-00276: Local storage option overrides global storage.

Cause: A storage clause has been specified in the table level options statement and also in the global options statement.

Action: This is only a warning message. Table level options take precedence over global options. Drop the table level options statement if this is not the intent.

SQL\*Loader-00277: Local file specification overrides global file specification.

Cause: A filename has been specified in the table level options statement and also in the global options statement.

Action: This is only a warning message. Table level options take precedence over global options. Drop the table level options statement if this is not the intent.

SQL\*Loader-00278: Incorrect file specification for parallel load.

Cause: The filename used to perform the parallel load was entered incorrectly.

Action: Correct the filename and re-invoke parallel loader.

SQL\*Loader-00279: Only APPEND mode allowed when parallel load specified.

Cause: INSERT, REPLACE, or TRUNCATE mode was used in a parallel load specification.

Action: Change the SQL\*Loader control file to use the APPEND keyword and re-invoke the parallel loader.

SQL\*Loader-00280: table string is a temporary table

Cause: The sqlldr utility does not load temporary tables. Note that if sqlldr did allow loading of temporary tables, the data would disappear after the load completed.

Action: Load the data into a non-temporary table.

SQL\*Loader-00281: Warning: ROWS parameter ignored in parallel mode.

Cause: Specifying save points using the ROWS parameter is not supported for parallel loads.

Action: Remove the ROWS parameter from the command-line arguments or specify a non-parallel direct load to have save points performed.

SQL\*Loader-00282: Unable to locate character set handle for character set ID (number).

Cause: SQL\*Loader could not find the character set handle for the given character set ID.

Action: The character set ID was obtained from the database server, the SQL\*Loader client does not have knowledge of the given character set ID. Possible mis-match of NLS data on the client and server side.

SQL\*Loader-00283: file processing string "string" ignored for INFILE \*

Cause: The SQL\*Loader control file specified INFILE \* for a load data file along with an optional file processing string. This message is a warning that the file processing string will be ignored since SQLLDR will expect the data to have the same record format as the SQL\*Loader control file.

Action: If the data in the SQL\*Loader control file is in the same format as the rest of the SQL\*Loader control file, then you don't need to do anything. Removing the file processing string will get rid of this error message. If the data in the SQL\*Loader control file has a different record format, then you need to copy the data into a separate file and use that file's name in the INFILE clause.

SQL\*Loader-00284: Warning: Input data file string specified multiple times.

Cause: The same input datafile is loaded multiple times. This can occur if the INFILE keyword is placed out of order in the load syntax statement, which causes the filename of the first datafile loaded to default to the name of the control file with an extension or file type of DAT.

Action: Check that INFILE keyword is not placed after one of these - BADFILE/BADDN/DISCARDFILE/DISCARDDN/DISCARDS.

SQL\*Loader-00285: string may be used only in conventional path.

Cause: HIDDEN can only be specified in the conventional path load.

Action: Use the conventional path load.

SQL\*Loader-00286: ROWS parameter is not supported when loading an IOT.

Cause: Specifying save points using the ROWS parameter is not supported when loading an IOT.

Action: Remove the ROWS parameter from the command-line arguments.

SQL\*Loader-00287: No control file name specified.

Cause: No control file name was provided at the control prompt.

Action: Provide the name of a valid control file at the prompt or on the command line.

SQL\*Loader-00288: Delimiters may not be specified for collections stored in SDF.

Cause: A TERMINATED BY or ENCLOSED BY clause was found along with an SDF (secondary data files) clause for a nested table or varray field.

Action: The TERMINATED BY or ENCLOSED BY clauses may be specified only if the nested table or VARRAY data is stored in the record in the main data file. If you are loading nested table or VARRAY data from a secondary data file, then you must use COUNT to indicate the number of elements in the secondary data file that are stored in the file.

SQL\*Loader-00289: SQL string for column string occludes SQL string for column string.

Cause: A SQL string has been associated with both a column object and one of its attributes in the control file. Because the SQL string of the column object will replace the entire column object in the VALUE clause of the INSERT statement, the SQL string of the attribute is ignored. This could cause unexpected or incorrect values to be loaded.

Action: Correct the control file so that only the column object or its attribute has a SQL string, but not both.

SQL\*Loader-00290: PIECED keyword (on column string) allowed only for lob or long columns

Cause: The PIECED keyword cannot be used for non lob or long columns.

Action: Remove the PIECED keyword or use lob or long column type.

SQL\*Loader-00291: Invalid bind variable string in SQL string for column string.

Cause: A bind variable may not refer to a filler field or to a non-existent field. Also, when running in direct-path mode, a bind variable may not refer to field that represents a LOB stored in a secondary file or a collection.

Action: Remove the offending bind variable from the SQL string.

SQL\*Loader-00292: ROWS parameter ignored when an XML, LOB or VARRAY column is loaded

Cause: Command-line arguments contained a ROWS parameter. Specifying save points using the ROWS parameter is not supported when any table being loaded contains a LOB or a column stored as a LOB. XML and VARRAY columns may be stored as a LOB.

Action: Remove the ROWS parameter from the command-line arguments.

SQL\*Loader-00293: Missing XMLTYPE directive in control file for table string

Cause: A table of sys.xmltype must specify the XMLTYPE directive.

Action: Add XMLTYPE directive to control file.

SQL\*Loader-00294: invalid name % specified in TREAT AS clause

Cause: The type name specified in a TREAT AS clause is invalid. It might contain characters that are not valid in the client character set or a quoted string might not be terminated or the name might be too long to contain a valid schema name and type name.

Action: Verify that the type name has valid characters and is not too long. Also, ensure that all quoted strings are terminated.

SQL\*Loader-00295: Warning: Table string, Column string - Quoting rule of object attribute bind variables has changed.

Cause: The quoting rule of bind variables consisting of full object attribute names changed. The old quoting rule is incorrect because it can lead to ambiguous column references. For backward compatibility, current load will continue unless ambiguous column references are detected.

Action: This is only a warning message. Because the quoting rule of object attribute bind variables has changed, it is recommended that the control file be replaced with the new rule. With the new rule, a full object attribute bind variable name is not enclosed in its entirety in double quotes. Instead, each attribute name in the bind variable should be independently quoted as needed. Note that each attribute name is actually an identifier on its own and thus should follow the quoting rules for an identifier. For example, bind variable ':A.B.C' here consists of 3 attribute names (or identifiers): 'A', 'B', and 'C'.

SQL\*Loader-00296: Bind variable string for column string is ambiguous.

Cause: A bind variable can only refer to one column in the control file. Current load could not continue due to ambiguous column references.

Action: Fix the bind variable. If this bind variable consists of quotes, check that the quotes are used correctly. For example, the old quoting rule of bind variables consisting of full object attribute names was incorrect because it can lead to ambiguous column references. Let's say we have an expression "LTRIM(:"A.B.C")". Using the old quoting rule, this bind variable can refer to object attribute columns '"A"."B"."C"', '"A.B".C', and '"A"."B.C"'. To avoid this confusion, use the new quoting rule for object attribute bind variables, which is to quote each attribute name independently as needed. In the preceding example, if the intended object attribute column is 'A.B.C', then the expression rewritten as "LTRIM(:A.B.C)" or "LTRIM(:"A"."B"."C") will not lead to ambiguities.

SQL\*Loader-00297: Invalid syntax or bind variable in SQL string for column string.

Cause: See following error message for more information. A SQL string cannot have quoted strings improperly terminated. A bind variable in a SQL string cannot have a length of 0, cannot exceed maximum length of 30 characters, and cannot be missing a double quote.

Action: Fix the SQL string. See following error for more information.

SQL\*Loader-00298: Filler field name is too long

Cause: The specified filler field name exceeded the maximum of 30 characters.

Action: Specify at most 30 characters.

SQL\*Loader-00299: Virtual column string in table string.string cannot be loaded.

Cause: Virtual columns were specified in the control file.

Action: Virtual columns cannot be specified in the control file. Remove the virtual column from the SQL\*Loader control file.

SQL\*Loader-00300: error while attempting to enable tracing

Cause: An error occurred while executing an ALTER SESSION statement to enable tracing. This message will be followed by the error returned from ALTER SESSION.

Action: No action required.

SQL\*Loader-00301: string for TERMINATED BY or ENCLOSED BY clause is longer than number bytes

Cause: The size of a string literal is longer than the maximum number of bytes allowed for an ENCLOSED BY or TERMINATED BY string. This error can also occur if the string needs to be converted to the character set of the data file and the resulting string is too long.

Action: Use shorter strings for the TERMINATED BY and ENCLOSED BY clauses.

SQL\*Loader-00303: Non-hex character encountered where hex char expected

Cause: A non-hex character was found in a hexadecimal string.

Action: Change it to the intended hexadecimal character.

SQL\*Loader-00304: Illegal combination of non-alphanumeric characters

Cause: The SQL\*Loader control file contains a combination of non-alphanumeric characters that SQL\*Loader does not recognize. For example, the combination!= is recognized as "not equal", but the combination =! is not valid.

Action: Remove the unrecognized characters from the control file.

SQL\*Loader-00305: More than one end of file character encountered

Cause: The file contains multiple end-of-file marks.

Action: Remove the excess end-of-file characters.

SQL\*Loader-00306: Token longer than max allowable length of number chars

Cause: The SQL\*Loader control file contains a single word or combination of characters (a token) that is longer than the maximum permissible value. The maximum possible value is shown. This error could result from missing spaces, so that multiple tokens are joined.

Action: Check that the proper SQL\*Loader control file is being executed Separate tokens, if joined, or shorten the token.

SQL\*Loader-00307: Warning: conflicting lengths number and number specified for column string table string

Cause: The SQL\*Loader control file specifies two different lengths for the named column. There are three ways to specify the length of a field: --with the POSITION keyword: POSITION(1:3) -- with the length specifier: CHAR(6) -- with the implied length of a datatype; for example, INTEGER -- A conflict could occur between any two of these specifications (or among all three, but only two are shown). A common cause of this error is the specification of some numeric datatype, such as INTEGER, when the numeric external form is intended (INTEGER EXTERNAL). The external form consists of character data, so it is considerably longer than the numeric form, which consists of binary data.

Action: No action is necessarily required, because SQL\*Loader uses only one of the lengths. Check the log file under the heading "Len" in the table-description section to see which length was used. Adjusting the SQL\*Loader control file to produce uniform length specifications will remove the warning.

SQL\*Loader-00308: string SQL string of column string must be in double quotes.

Cause: A SQL string was found that was not quoted or in single quotes.

Action: Use double quotes for the SQL string, rather than single quotes.

SQL\*Loader-00309: No SQL string allowed as part of string field specification

Cause: Particular field types do not allow SQL strings as part of their field specification (e.g. field corresponding to a LOB column). This was violated and needs to be corrected.

Action: Remove the SQL string from the particular field specification.

SQL\*Loader-00310: Interval partition values of table string must be in double quotes.

Cause: A string specified for interval partitioning was found that was not quoted or in single quotes.

Action: Use double quotes for the interval partitioning values string, rather than single quotes.

SQL\*Loader-00350: Syntax error at line number.

Cause: num identifies the line in the SQL\*Loader control file at which the error occurred. This message is followed by another of the form -- Expecting str1, found str2 where str1 is a description of what SQL\*Loader expected in the SQL\*Loader control file, and str2 is what was found. Then SQL\*Loader displays the offending line from the SQL\*Loader control file, indicating the location of the error in the line by a carat (^) or an asterisk (\*). An example follows: -- SQL\*Loa er-350: Syntax error at line 28 -- Expecting column name, found keyword CHAR -- col3 ENCLOSED BY '"', CHAR ENCLOSED "'",

Action: Compare the DDL syntax against the syntax diagrams in Oracle7 Server Utilities and make any necessary corrections.

SQL\*Loader-00401: End field position number must be greater than or equal to start number

Cause: The named field contains a (start:end) clause in which end is less than start.

Action: Modify the clause so that end is greater than or equal to start.

SQL\*Loader-00402: Unable to determine length of column string from specification

Cause: The specified datatype does not have an implied length (for example, a numeric external or RAW datatype), it is not specified with delimiters, no length was specified, and a length cannot be determined from a POSITION clause.

Action: If a POSITION clause is specified, adding an end location to it produces a length specification. This clause then has the form POSITION(start:end) A length can also specified after the datatype, as in INTEGER EXTERNAL (6) Finally, the field could be specified with delimiters, or the datatype changed to one that has an implied length.

SQL\*Loader-00403: Referenced column string not present in table string.

Cause: The named column is not present in the given table.

Action: Correct the column name or table name.

SQL\*Loader-00404: Column string present more than once in string's INTO TABLE block.

Cause: The named column is specified more than once in a single INTO TABLE statement.

Action: Remove the extraneous column specification.

SQL\*Loader-00405: Need termination delim with optional enclosure delim: column string table string

Cause: The named column was specified with an optional enclosure delimiter, but no termination delimiter. Enclosure delimiters can only be optional when termination delimiters are present.

Action: Specify a termination delimiter or make the enclosure delimiters non-optional.

SQL\*Loader-00406: If data is all generated, number to load cannot be ALL

Cause: When only generated data is loaded, a number to load must be given so SQL\*Loader knows when to stop.

Action: Specify a number to load.

SQL\*Loader-00407: If data is all generated, number to skip is meaningless

Cause: When all data is generated, no file is read, and there are no records to skip.

Action: Remove the number to skip.

SQL\*Loader-00408: Physical record stack overflow

Cause: An internal error has occurred.

Action: Contact customer support.

SQL\*Loader-00409: Number to skip must be table-level, not load-level on continued loads

Cause: The SKIP parameter was specified on the command line or in the OPTIONS statement, but the load was specified as continued with CONTINUE\_LOAD. When a multiple-table direct load is interrupted, it is possible that a different number of records were loaded into each table. As a result, the number of records to skip must be specified for each table when continuing the load. In this case, the load is specified as continued with the CONTINUE\_LOAD statement, and the number of records to skip is given in each INTO TABLE statement. See also messages 410 and 411 for more information.

Action: Check the log file to determine the appropriate number of records to skip for each table and specify this number in the INTO TABLE statement for each table in a continued load or with the command-line SKIP parameter in a standard load.

SQL\*Loader-00410: Number to skip must be load-level, not table-level

Cause: A SKIP clause was found in the INTO TABLE statement of a standard (non-continued) load. In a standard load, specified with LOAD DATA, it is not possible to skip a different number of records for each table. The number of records to skip must be specified for the entire load by using the SKIP parameter on the command line or in the OPTIONS clause. If table-level skip is required, because a different number of records were loaded into each table (only possible for a multiple- table direct load), then specify a continued load with the CONTINUE\_LOAD statement. See also messages 409 and 411 for more information.

Action: If the load was not a multiple-table, direct path load, then move the SKIP clause from the INTO TABLE statements to the command line or to the OPTIONS clause. Otherwise, specify the load as continued with CONTINUE\_LOAD.

SQL\*Loader-00411: Only a direct path load may be continued

Cause: The load is specified with CONTINUE\_LOAD, but DIRECT=FALSE. CONTINUE\_LOAD is only possible for a direct path load and is only necessary for a multiple-table, direct path load when a different number of records have been loaded into each table. See also messages 409 and 410 for more information.

Action: If CONTINUE\_LOAD is necessary, specify a direct load and put the number of records to skip in each INTO TABLE statement. Otherwise, use the command line or OPTIONS clause to specify the number of records to skip and use LOAD DATA instead of CONTINUE\_LOAD.

SQL\*Loader-00412: More columns specified for table string than the maximum (number)

Cause: More columns were specified for the table than the maximum number allowed by the database.

Action: Remove the extraneous columns.

SQL\*Loader-00413: NULLIF or DEFAULTIF clause specified for filler field string in table string.

Cause: A NULLIF or DEFAULTIF clause was specified in the SQL\*Loader control file for the named filler field. These options cannot be specified for filler fields.

Action: Remove the NULLIF or DEFAULTIF clause from the field definition.

SQL\*Loader-00414: no columns to load for table string

Cause: There were no fields in the data file to be loaded for the table. Probably all fields were identified as FILLER fields.

Action: Verify that the FILLER attribute was set correctly for the fields.

SQL\*Loader-00415: column string in table string cannot use and be the object of an SDF or LOBFILE

Cause: The named column is identified as the target of a secondary data file (SDF) or LOBFILE clause. However, the column also gets it's value from an SDF or LOBFILE. If a field name is named in an SDF or LOBFILE clause, then that field cannot have an SDF or LOBFILE clause.

Action: Verify that the SDF and LOBFILE clauses in the SQL\*Loader control file name the correct fields. Also verify that the SDF and LOBFILE clauses are specified for the correct field.

SQL\*Loader-00416: SDF clause for field string in table string references a non existent field.

Cause: The secondary data file clause for the field identified another field that doesn't exist in the table definition for the SQL\*Loader control file.

Action: Verify the definition of the secondary data file to make sure it identifies the intended field.

SQL\*Loader-00417: SQL string (on column string) not allowed in direct path.

Cause: Because the direct path bypasses SQL processing, the SQL string cannot be used.

Action: Remove the SQL string or use the conventional path.

SQL\*Loader-00418: Bad datafile datatype for column string

Cause: The datatype in the data file specified for the column cannot be used to load the column. This message is often displayed for columns that need to be loaded with special features. For example, BFILE columns can only be loaded via the BFILE directive in the control file; same goes for REF fields. in the SQL\*Loader control file. Similarly, REF columns can only be loaded with theREF datatype in the SQL\*Loader control file.

Action: Determine the datatype of the column in the database check the documentation for the correct mechanisms to use to load columns of that type.

SQL\*Loader-00419: input datatype for column string is not supported when loading varrays

Cause: The datatype in the SQL\*Loader control file for the column is cannot be used to load data in a varray.

Action: Use a different datatype.

SQL\*Loader-00420: unsupported datatype conversion requested for column string in table string

Cause: The colummn needs to have it's data converted to another datatype before loading the data. The required conversion cannot be done by sqlldr.

Action: Verify that the correct datatype was specified for the column.

SQL\*Loader-00421: error converting data

Cause: This message can be displayed as one of the reasons for rejecting a row. The sqlldr utility was attempting to convert data for the column from its datatype in the data file to the datatype for the column in the database. This message should be followed with another message describing the conversion error.

Action: Correct the data in the data file so that it can be converted.

SQL\*Loader-00422: constant element count of number for column string is greater than maximum, number

Cause: The number of elements specified for a varray column in a table is greater than the maximum number of elements allowed for the type of the varray column.

Action: Increase the number of elements allowed for the type or remove unwanted elements from the data file.

SQL\*Loader-00423: element count is greater than maximum allowed for the column

Cause: When building a varray from the data file, SQL\*Loader encountered more varray elements than are allowed for the column.

Action: The previous error messages contain the name of the column and the row number containing the bad data.

SQL\*Loader-00424: table string makes illegal reference to collection field string

Cause: A WHEN, OID or SID clause for the table refers to a field declared inside of a collection.

Action: Move the data containing the value for a SID or OID clause outside of the collection definition.

SQL\*Loader-00425: column string makes illegal reference to collection field string

Cause: A clause, such as NULLIF or BFILE clause, for the column refers to a field declared inside of a collection.

Action: Move the data containing the value for a SID or OID clause outside of the collection definition.

SQL\*Loader-00426: count of elements in VARRAY string comes after the data for the varray

Cause: The COUNT clause for a VARRAY field indicates that the count of elements in the varray is stored in another data field. However, that data field comes after the varray data in the data file. Since finding the count field would require SQL\*Loader to know the number of elements in the VARRAY first, SQL\*Loader requires that the count field come before the VARRAY data.

Action: Move the count field to be before the collection data in the data file.

SQL\*Loader-00427: a field condition references a non-scalar field or a LOB field string

Cause: The field condition is referencing a field which is either a nested table, varray, column object, LOB or BILE field. These fields with these typescannot be references by other field.

Action: Correct the NULLIF, DEFAULTIF, or WHEN clauses to reference only non-LOB scalar data fields.

SQL\*Loader-00428: count for field string not stored in character or integer field

Cause: The count clause for a field references another field, but the referenced field is not a character or integer datatype.

Action: Modify the count field so that it reference a a data field that has the count in an integere or character format.

SQL\*Loader-00429: insufficient number of elements found for varray

Cause: The COUNT directive was specified for a varray, but the number of elements found is less than the number specified by the COUNT directive.

Action: Correct the data so that the count and the number of elements agree.

SQL\*Loader-00430: NULL nested table element is not allowed

Cause: A row in a nested table was set to NULL. Nested tables cannot contain NULL fields.

Action: Correct the data so that there are no NULL rows in the nested table.

SQL\*Loader-00431: illegal NULLIF or DEFAULTIF clause specified for nested table column string

Cause: Rows in a nested table cannot be set to NULL. SQLLDR displays this error when a NULLIF clause was specified for the element that defines the row that make up a nested table. SQLLDR also displays this error if a DEFAULTIF clause is specified for an element that is a named type, since SQLLDR will set a named type to NULL if the DEFAULTIF evaluates to TRUE.

Action: None

SQL\*Loader-00432: converted data too large

Cause: This message is preceded by a message identifying a row and column. It is displayed when there is insufficient room to convert the data from the datatype in the input file to the datatype for the column in the database.

Action: Modify the data so that it fits in the database field.

SQL\*Loader-00433: no attributes found for column object string in table string

Cause: No attributes are to be loaded for a column object named in the control file. This can happen if all fields in the definition for the column object in the control are designated as FILLER fields.

Action: Either specify attributes to load for the column object or remove the column object from the control file.

SQL\*Loader-00434: Can not load LOB/XML in a nested table along with the parent table.

Cause: Loading LOBs and XML data within a nested table at the same time as the parent table is not supported.

Action: Load the nested table with the LOB or XML column separately from the parent table.

SQL\*Loader-00435: invalid constant value string for nested table column string

Cause: A constant value was specified for the SETID of a nested table column. An error occured while translating the character constant into a SETID.

Action: Make sure the constant string contains valid hexadecimal characters and that there are 32 hexadecimal characters.

SQL\*Loader-00436: error converting GUID

Cause: The value of the field named in the message is used to populate the column named in the messsage. Because column is a Set ID or an Object ID, the field needs to be converted. This message indicates that there was a conversion error. If the field is a character field, then the conversion error could be caused by too many or too few haxeadecimal charactersI. Also, one or more of the characters in the field might not be a valid hexadecimal character. If the field contains RAW data, then either too many or to few bytes were specified for the field.

Action: Fix the data and reload the row.

SQL\*Loader-00440: Invalid table specified as scope of a REF

Cause: As part of the REF directive one specifies the table name or another fields name which contains the table name of the table which the REF references.

Action: Make sure that the right referenced table name is specified.

SQL\*Loader-00456: end of collection found after number elements when looking for number elements

Cause: A count value was specified for a varray or nested table column and the number of rows found is less than the number of rows specified

Action: Verify that the count field has the correct value and that there is no missing data for the collection.

SQL\*Loader-00457: Comparison text of CONTINUEIF LAST must have length 1 not number

Cause: The comparison text is too long. It can only be one character.

Action: Reduce the comparison text to one character.

SQL\*Loader-00458: Comparison text ('string') of CONTINUEIF LAST must be non-whitespace

Cause: The comparison text is a whitespace character (blank or tab).

Action: Change the comparison text to a non-whitespace character.

SQL\*Loader-00459: error fetching numeric value for sequence on column (string)

Cause: An attempt was made to retrieve a non-numeric value for a sequenced column.

Action: Verify that the data for the sequenced column is numeric. Then retry the operation.

SQL\*Loader-00460: Column (string), form of use (number) does not match char set id of (number)

Cause: The given column with the given form of use does not have the same character set ID as a previous column with the same form of use.

Action: This should not happen. Contact ORACLE support and supply the following information: DDL for the table being loaded, and the SQL\*Loader control file. ADDED in 8.1

SQL\*Loader-00461: direct path loading of datatype for column string not supported

Cause: The datatype for the specified column is one that cannot be loaded with direct path.

Action: If the datatype is supported with conventional path, load the table using conventional path.

SQL\*Loader-00462: error inserting LOB into column string, row number, table string

Cause: An error occurred while attempting to write a lob into a row.

Action: See accompanying messages describing why the LOB could not be loaded, what actions sqlldr took (if any), and where the errors may be in order to reload.

SQL\*Loader-00463: secondary data file for LOB is string

Cause: The secondary data file that was in use for populating the LOB when an error occured.

Action: None

SQL\*Loader-00464: file offset for beginning of lob is string

Cause: The offset into the secondary data file that contains the start of the LOB that was being written when an error occured.

Action: None

SQL\*Loader-00465: string directive expects number arguments, number found.

Cause: You specified a directive such as COUNT() or BFILE() in the SQL\*Loader control file. This directive specifies a fixed number of arguments, but the SQL\*Loader control file contains a different number of arguments.

Action: Correct the SQL\*Loader control file so that the directive contains the correct number of arguments.

SQL\*Loader-00466: Column string does not exist in table string.

Cause: The SQL\*Loader control file specified a table column that does not exist.

Action: None

SQL\*Loader-00467: attribute string does not exist in type string for table string.

Cause: The SQL\*Loader control file specified an attribute that does not exist for the specified type. The table that contains the type is also identified in the error message.

Action: Verify that the correct table in the correct schema is named in the SQL\*Loader control file. Also verify that the column name is spelled correctly.

SQL\*Loader-00468: OID directive expects 1 argument, number found.

Cause: More than one argument was specified for an OID clause.

Action: Specify the name of the field containing the value to use for the OID. If the OID for the table is user-defined, then do not use the OID clause in the control file.

SQL\*Loader-00469: SID directive expects 1 argument, number found.

Cause: More than one argument was specified for a SID clause.

Action: Only specify the name of the field containing the value to use for the SID in the SID clause.

SQL\*Loader-00470: table string does not have system generated OID

Cause: You specified an OID clause for a table but the table is either not an object table or the table is an object table but the OIDs for the rows are not system generated.

Action: Verify that the you are loading the correct table. If you are, then you must not specify the OID clause for this table. You should use the OID clause only when the table is an object table, has system generated OIDs and when you want to specify OIDs to be assigned to each row of the table.

SQL\*Loader-00471: OID or SID clause has an argument that is CONSTANT

Cause: You specified a CONSTANT as an argument in an OID clause for an object table or in the SID clause for a nested table column. Since these columns must have unique values, SQL Loader does not allow the a constant to be specified for their values.

Action: Store the OID for each row in a filler field and specify the name of the filler field as an argument.

SQL\*Loader-00472: collections can contain only one non FILLER field specification

Cause: More than one non filler field specification is found in a collection field's member field list.

Action: See correct syntax in the Utilities Manual. If indeed there is more than one attribute that makes up the particular collection, then it must be a collection of a object type which needs to be specified using the COLUMN OBJECT field specification syntax.

SQL\*Loader-00473: nesting of collections is not allowed.

Cause: Nesting of one collection type field description within another is not allowed.

Action: Verify that collection nesting is attempted in the SQL\*Loader control file. Correct the mistake.

SQL\*Loader-00474: no value set for dynamic file for column string in table string row number

Cause: The data for the named column is in a dynamic LOBFILE or secondary data file. This message is returned when the field containing the name of the file with the data for this field has not been set or is NULL. This could be because the record in the data file does not match the format described by the SQL\*Loader control file.

Action: Correct any errors in the data file or the SQL\*Loader control file.

SQL\*Loader-00475: field for dynamic file name is string in table string

Cause: This message is always displayed after message 474.

Action: None

SQL\*Loader-00476: count of elements for collection is not set or null, 0 will be used

Cause: This message is displayed following a message that identifies the column and row that contained the problem. The message indicates that the collection field named in the previous message has the count of elements in the collection stored in another field. This message is displayed if the field containing the count does not have a value or is set to NULL. When this happens, SQL\*Loader uses 0 as the number of elements.

Action: If 0 is not the count of elementsfor the collection, correct the data in the data file.

SQL\*Loader-00477: REF directive for field string requires at least two arguments

Cause: The SQL Loader control file contains a REF directive for the field, but only one argument was supplied for the directive. The REF directive always requires at least two arguments.

Action: Supply the missing argument to the REF directive. Remember that you must always supply a table name to the REF directive even if the REF is scoped.

SQL\*Loader-00478: unable to continue due to missing filename for LOBFILE or SDF

Cause: The name for a LOBFILE or secondary data file is either missing or NULL for the current row. SQL\*Loader is unable to continue loading since it can't determine how to get the LOB for the next row.

Action: Correct the data file so that there are valid values for all fields containing the names of LOBFILEs and secondary data files.

SQL\*Loader-00479: REF directive for column string expects number arguments; found number.

Cause: The number of arguments in the REF directive for the column is incorrect.

Action: Specify the correct number of arguments for REF. Remember that the REF directive always requires a table name. Also, primary key REFs require one arguments for each field in the primary key.

SQL\*Loader-00480: EXPRESSION may not be used with elements of a collection.

Cause: The EXPRESSION keyword is followed by a required SQL string expression and is used to load a column with the result of the SQL string expression instead of with a value from the input data file. However, this capability is not allowed with elements of a collection.

Action: Remove the EXPRESSION keyword and associated SQL string from the collection element in the control file.

SQL\*Loader-00481: HIDDEN may not be used with non-scalar fields.

Cause: The HIDDEN keyword is only allowed for scalar fields.

Action: Remove the HIDDEN keyword from the non-scalar field in the control file.

SQL\*Loader-00486: sql-strings may not be specified for collection field string

Cause: A sql-string was specified as part of the description of the field that is inside a nested table or varray. Sql-strings cannot be used to load a field in a varrary or nested tables.

Action: Remove the sql-string from the field description. Modify the data file so that it contains the values to be loaded into the column in the collection.

SQL\*Loader-00487: COUNT clause required for collection string

Cause: A VARRAY or NESTED TABLE was defined in the SQL Loader control file and all of the fields in the VARRAY or NESTED TABLE are generated by SQL Loader and do not come from a data file. SQL Loader requires a COUNT clause be specified so that it knows how many elements to add to the VARRAY or NESTED TABLE for each row.

Action: Add a COUNT clause to the VARRAY or NESTED TABLE definition.

SQL\*Loader-00488: string not a named collection type for filler field string

Cause: The FILLER option was specified for a VARRAY or NESTED TABLE field in the SQL Loader control file. However, the type name specified for the field is not the name of a VARRAY or NESTED TABLE type.

Action: Verify that the correct type name was specified. If the type is defined in a different schema, also verify that the correct schema name is specified.

SQL\*Loader-00489: cannot insert NULL object into object table string, row number

Cause: There was no data specified in the control file, a lob file, or a secondary data file for this object column.

Action: Place valid data for this column in the appropriate file prior to invoking SQL\*Loader to load data into this table.

SQL\*Loader-00490: absolute position is not allowed for inline collections

Cause: The absolute position specification was used for inline collections. Specifying the absolute position for inline collections is not supported.

Action: Use relative positioning for inline collections.

SQL\*Loader-00500: Unable to open file (string)

Cause: SQL\*Loader could not open the named file.

Action: Check the operating system messages below this one in the log file.

SQL\*Loader-00501: Unable to read file (string)

Cause: SQL\*Loader could not read the named file.

Action: Check the operating system messages following this message in the log file.

SQL\*Loader-00502: unable to open data file 'string' for field string table string

Cause: An attempt to open a LOBFILE or secondary data file failed.

Action: Check the operating system messages following this message for information on why the open failed. Verify that the correct name is specified for the LOBFILE or secondary data file.

SQL\*Loader-00503: Error appending extension to file (string)

Cause: SQL\*Loader could not append the default extension to create the filename. The given name could be too long or contain illegal characters.

Action: Check the specified filename.

SQL\*Loader-00504: Error skipping records in file (string)

Cause: SQL\*Loader could not open the file or could not read from it.

Action: Check that the file is where it is expected and that read access has been granted.

SQL\*Loader-00505: error reading LOBFILE

Cause: An attempt to read a secondary data file failed.

Action: Check the operating system message that follows this message for more information.

SQL\*Loader-00506: formatting error reading SDF or LOBFILE string for column string in table string

Cause: The the record format of the named LOBFILE or SDF file is incorrect.

Action: Fix the record formatting problems in the file.

SQL\*Loader-00507: unexpected EOF reading SDF or LOBFILE string for column string in table string

Cause: The end of file was reached for a secondary data file or LOBFILE before the data for the current row was found.

Action: If the file is a LOBFILE, verify the correct datatype was specified for the field. If the file is a secondary data file, make sure the record format is specified correctly in the SQL\*Loader control file.

SQL\*Loader-00508: record formating error in data file string

Cause: The data found in the data file does not correspond to the record format in the SQL\*Loader control file.

Action: Verify that all records in the data file match the format as described in the SQL\*Loader control file.

SQL\*Loader-00509: System error: string

Cause: A platform-specific error was returned during an operation. This message is used to display the text of the error.

Action: None

SQL\*Loader-00510: Physical record in data file (string) is longer than the maximum(number)

Cause: The datafile has a physical record that is too long.

Action: Use CONCATENATE or CONTINUEIF. Break up the physical records.

SQL\*Loader-00511: Unable to initialize read functions

Cause: SQL\*Loader could not initialize the read functions.

Action: Check the errors below this message in the log file for more information.

SQL\*Loader-00512: Unable to free read buffer

Cause: An internal error has occurred.

Action: Contact customer support.

SQL\*Loader-00513: Unable to close file (string)

Cause: SQL\*Loader could not close the named file.

Action: Check the errors below this message in the log file for more information.

SQL\*Loader-00514: Error getting elapsed time

Cause: SQL\*Loader could not get the elapsed time from the system.

Action: No action required.

SQL\*Loader-00515: Error getting CPU time

Cause: SQL\*Loader could not get the CPU time from the system.

Action: No action required.

SQL\*Loader-00516: Control file (string) has no contents

Cause: The named file was found to be empty.

Action: Check that the intended file was referenced and that it is not empty.

SQL\*Loader-00517: Error decomposing file name (string)

Cause: SQL\*Loader could not break down the filename into its component parts.

Action: Check the filename for illegal characters.

SQL\*Loader-00518: Error reassembling file name (string)

Cause: SQL\*Loader could not put the filename back together again from its components.

Action: Check the filename for illegal characters.

SQL\*Loader-00520: lfimknam failed for file (string)

Cause: LFI failed to make a name object for the file.

Action: Contact Oracle Worldwide Support.

SQL\*Loader-00521: lfilini failed for file (string)

Cause: LFI failed to create or initialize a file object for the file.

Action: Contact Oracle Worldwide Support.

SQL\*Loader-00522: lfiopn failed for file (string)

Cause: LFI failed to open the file.

Action: Check for any possible operating system errors and/or potential memory problems.

SQL\*Loader-00523: error number writing to file (string)

Cause: Could not write to specified file.

Action: Check the following: the file actually resides in the specified location you have write privileges on the file you have sufficient disk space you have not exceeded your disk quota If all of these conditions are satisfied, then retry the operation.

SQL\*Loader-00524: partial record found at end of datafile (string)

Cause: An incomplete record was found at the end of the indicated datafile.

Action: Make sure the last record in the datafile is complete and has the correct terminating character(s). Also, if fixed-length records are in use, verify that no record exceeds the platform-specific length for a single record.

SQL\*Loader-00525: OCI return status: success

Cause: The message describes the status code returned by an OCI call.

Action: See surrounding messages for more information.

SQL\*Loader-00526: OCI return status: success with info

Cause: The message describes the status code returned by an OCI call.

Action: See surrounding messages for more information.

SQL\*Loader-00527: OCI return status: no data

Cause: The message describes the status code returned by an OCI call.

Action: See surrounding messages for more information.

SQL\*Loader-00528: OCI return status: error

Cause: The message describes the status code returned by an OCI call.

Action: See surrounding messages for more information.

SQL\*Loader-00529: OCI return status: invalid handle

Cause: The message describes the status code returned by an OCI call.

Action: See surrounding messages for more information.

SQL\*Loader-00530: OCI return status: need data

Cause: The message describes the status code returned by an OCI call.

Action: See surrounding messages for more information.

SQL\*Loader-00531: OCI return status: still executing

Cause: The message describes the status code returned by an OCI call.

Action: See surrounding messages for more information.

SQL\*Loader-00532: OCI return status: continue

Cause: The message describes the status code returned by an OCI call.

Action: See surrounding messages for more information.

SQL\*Loader-00533: OCI return status: unknown, value is number

Cause: An unknown status was returned by an OCI call.

Action: See surrounding messages for more information.

SQL\*Loader-00551: internal error: error initializing slf

Cause: An internal error occured while trying to initialize the file I/O component.

Action: Call customer support.

SQL\*Loader-00552: insufficient privilege to open file

Cause: SQL\*Loader does not have the previleges required to open the file.

Action: Verify that the correct file was specified and that the file has the appropriate permissions.

SQL\*Loader-00553: file not found

Cause: The specified file cannot be found.

Action: verify that the correct name exists and whether the file is in the intended location.

SQL\*Loader-00554: error opening file

Cause: An error occurred while trying to open the file. No further information is available.

Action: Verify that the file is accessible.

SQL\*Loader-00555: unrecognized processing option

Cause: The processing option specified for the file cannot be processed.

Action: Verify that the processing options specified for the file contain legal syntax for the platform where SQL\*Loader is running.

SQL\*Loader-00556: unable to allocate read buffer

Cause: Attempt to allocate the read buffer failed.

Action: If possible, try specifying a smaller size for the read buffer.

SQL\*Loader-00557: unable to allocate memory

Cause: An attempt to allocate some memory to track I/O for the file failed.

Action: Contact customer support.

SQL\*Loader-00558: attempt to use SKIP parameter with linked-in loader

Cause: SKIP parameter was specified with a linked-in file processor.

Action: Do not use the SKIP parameter in this case.

SQL\*Loader-00559: error closing file

Cause: An error occured while closing the file.

Action: Contact customer support.

SQL\*Loader-00560: error reading file

Cause: An error occurred while reading the file.

Action: Make sure the file is still accessible.

SQL\*Loader-00561: end of file

Cause: End of file reached.

Action: None

SQL\*Loader-00562: record too big

Cause: A record in the file is larder than the read buffer.

Action: Verify that the file is not corrupt. If not, try specifying a larger size for the read buffer.

SQL\*Loader-00563: bad length for VAR record

Cause: The length protion of a VAR record contains non-numeric data.

Action: Fix the data in the file.

SQL\*Loader-00564: illegal hexadecimal literal specified for record delimiter

Cause: A hexadecimal literal that contains the record delimiter for the file does not contain a valid hexadecimal string.

Action: Verify that the correct hexadecimal value was specified in the processing options for the file.

SQL\*Loader-00565: unexpected error during skip.

Cause: an unexpected error occured while attempting to skip records.

Action: This message should be followed by another message giving more specific information about the error

SQL\*Loader-00566: partial record found at end of datafile

Cause: An incomplete record was found at the end of file.

Action: Make sure the last record in the datafile is complete and has the correct terminating character(s).

SQL\*Loader-00567: unable to derive file name

Cause: An error occured while attempting to build a name for a data file, bad file, discard file or log file.

Action: Instead of relying on SQL Loader to build these file names, try specifying full file specifications for these files in the control file or on the SQL Loader command line.

SQL\*Loader-00568: error writing to file

Cause: Unexpected error occured while writing to a file. This message is followed by another message with more information about the error.

Action: None

SQL\*Loader-00569: READSIZE parameter exceeds maximum value string for platform

Cause: The value specified for the READSIZE parameter on the SQL Loader command line was larger than the maximum size allowed on the platform executing the SQL Loader command

Action: Decrease the size of the READSIZE parameter to be less than the maximum size allowed on the platform.

SQL\*Loader-00600: Bind size of number bytes increased to number bytes to hold 1 row.

Cause: The space needed to contain a single row is longer than the specified bind size. The value used for the bind size will be increased to handle the larger size

Action: No action is required. This message will go away if the new value in the error message is specified for the bind size.

SQL\*Loader-00601: For INSERT option, table must be empty. Error on table string

Cause: A non-empty table is being loaded with the INSERT option.

Action: Use the REPLACE keyword to empty the old table and store the new data in its place. Use the APPEND keyword to leave the table's contents intact and add the new data to it.

SQL\*Loader-00602: Maximum converted length number of column string is too big for bind array

Cause: The named column cannot undergo the specified character set conversion and still be placed in a contiguous piece of memory on the system.

Action: Specify a shorter data column or eliminate the conversion.

SQL\*Loader-00603: Maximum length number of column string is too big for bind array

Cause: The named column cannot be put in a contiguous piece of memory on the system.

Action: Specify a shorter data column.

SQL\*Loader-00604: Error occurred on an attempt to commit

Cause: An error occurred while trying to commit changes to the database.

Action: Look at the message listed below this one in the log file for more information.

SQL\*Loader-00605: Non-data dependent ORACLE error occurred -- load discontinued.

Cause: An error occurred that is independent of the data. For example, an out-of-space condition. Because all further rows will be rejected, the load is discontinued. (If the error were data dependent, then other rows might succeed.)

Action: See the errors below this one in the log file for more information.

SQL\*Loader-00606: Object string in INTO TABLE clause is not a local table

Cause: The synonym specified in the INTO TABLE clause in the SQL\*Loader control file specifies a remote object via a database link. Only a synonym for an existing local table can be specified in the INTO TABLE clause.

Action: Ensure that a local table name or a synonym for a local table is fully specified in the INTO TABLE clause. The table must already exist.

SQL\*Loader-00607: partition not empty for INSERT option; table string, partition string

Cause: An attempt was made to use the INSERT option on a non-empty partition.

Action: Empty the partition, or use the REPLACE or TRUNCATE option.

SQL\*Loader-00608: subpartition not empty for INSERT option; table string, subpartition string

Cause: An attempt was made to use the INSERT option on a non-empty subpartition.

Action: Empty the subpartition, or use the REPLACE or TRUNCATE option.

SQL\*Loader-00609: value used for ROWS parameter changed from number to number

Cause: SQL Loader adjusted the value it was using for the ROWS parameter to the new value reported. This is an informational message and not an error. SQL Loader will adjust the value of the ROWS parameter if the amount of memory specified by BINDSIZE is not large enough to hold data for the number of rows specified. SQL Loader will also change the value of the ROWS parameter for conventional path loads if the value is larger than 65534. Conventional path load can load at most 65534 rows at a time.

Action: If the limit of 65534 rows for conventional path load is not being reached, then try increasing the value of BINDSIZE.

SQL\*Loader-00610: cannot load system partitioned table string; partition name(s) required

Cause: An attempt was made to load a system partitioned table with no partitioning clause specified in the SQL\*Loader control file.

Action: Specify the partition name(s) in the SQL\*Loader control file.

SQL\*Loader-00620: Initial enclosure character not found

Cause: A mandatory initial enclosure delimiter was not present. Either it is missing on the current field or the previous field is missing an identical closing delimiter.

Action: Supply the missing delimiters.

SQL\*Loader-00621: Field in data file exceeds maximum length

Cause: A field exceeded its maximum allowable length. The maximum length is either the length specified in the SQL\*Loader control file, or, for delimitable fields without a length specified, the default maximum length (255 bytes).

Action: Check for missing delimiters and/or shorten the field.

SQL\*Loader-00622: Column not found before end of logical record (use TRAILING NULLCOLS)

Cause: The logical record ended before all specified fields were found.

Action: If the missing fields should be loaded as null, use the TRAILING NULLCOLS clause. Otherwise, correct the data.

SQL\*Loader-00623: second enclosure string not present

Cause: The logical end of record or the end of a LOBFILE was reached before a second enclosure delimiter was found.

Action: Correct the data file to include the missing delimiter.

SQL\*Loader-00624: no terminator found after TERMINATED and ENCLOSED field

Cause: No termination delimiter was found after the enclosed field ended.

Action: Supply the missing termination delimiter.

SQL\*Loader-00625: Multibyte character error in control file.

Cause: Incomplete multi-byte character strings were found in the SQL\*Loader control file.

Action: Edit the SQL\*Loader control file to check that all multi-byte character data is valid.

SQL\*Loader-00626: Character set conversion buffer overflow.

Cause: A conversion from the datafile character set to the client character set required more space than that allocated for the conversion buffer. The size of the conversion buffer is limited by the maximum size of a varchar2 column.

Action: The input record is rejected. The data will not fit into the column.

SQL\*Loader-00627: Character set conversion graph not available.

Cause: A conversion from the datafile character set to the client character failed due to the conversion graph not being available.

Action: Contact Oracle support. Check NLSRTL installation.

SQL\*Loader-00628: Character set conversion error.

Cause: A character set conversion error occurred.

Action: Contact Oracle support. Check NLSRTL installation. Provide a reproduceable test case.

SQL\*Loader-00640: Variable length field was truncated.

Cause: The end of the logical record was encountered before the end of a variable length field. The length of each variable-length field is embedded in the field, so SQL\*Loader knows that more data should have been present.

Action: Check the data for inadvertent truncation and verify the SQL\*Loader control file specifications against the log file; the field may be starting in the wrong place.

SQL\*Loader-00641: Invalid packed decimal nibble.

Cause: Each byte in a packed decimal field contains two 4-bit nibbles. Each nibble must have a valid value.

Action: Check the SQL\*Loader control file's specifications against the log file to ensure that the field location was specified correctly. Check the contents of the field.

SQL\*Loader-00642: Relative start position > absolute field end position.

Cause: A field specified as POSITION(\*+n:y) had its relative start occur after the absolute position y.

Action: Check that a delimiter is not missing and that the values of n and y are correct.

SQL\*Loader-00643: error executing INSERT statement for table string

Cause: A fatal error occured while attempting to insert data into the table.

Action: Refer to the messages that follow for more information. If you specified SQL stings for any of your columns, verify that strings are correct. Specifcally, check for balanced parenthesis and correct use of quotation marks. Another format error

SQL\*Loader-00644: end of logical record found when reading length of varying length field

Cause: While attempting to read the length portion of a varying length field, then end of the logical record was reached.

Action: Verify that the SQL\*Loader control file describes the data correctly and that the data in the data file matches the description in the SQL\*Loader control file

SQL\*Loader-00645: error converting character length field to a number

Cause: An error occurred while attempting to convert the characters containing the count portion of a VARCHARC or VARRAWC field.

Action: Verify that the count portion for the column has the correct value.

SQL\*Loader-00646: lob set to EMPTY in column string, row number, table string

Cause: Encountered errors (e.g. parsing errors in LOBFILE) while loading LOBs. The row will remain in the table and its LOB column will be initialized to empty. Loading of other records will continue.

Action: Correct the data file (see accompanying messages) and reload.

SQL\*Loader-00647: Integer to number conversion error

Cause: An error occurred while attempting to convert an integer to an Oracle number format.

Action: Verify that the integer field in the data file is a valid integer. If the INTEGER(N) syntax was used, then verify that the length specified is valid.

SQL\*Loader-00649: Quoted string missing closing quote

Cause: A quoted string in the control file is missing a closing quote.

Action: Insert the closing quote as appropriate.

SQL\*Loader-00650: incomplete lob data written for column string, row number, table string

Cause: Encountered errors (e.g. parsing errors in LOBFILE) while loading LOBs using direct path. The row will remain in the table and its LOB column may not be complete. Loading of other records will continue.

Action: Correct the data file (see accompanying messages) and reload.

SQL\*Loader-00651: error skipping lob for column string, row number, table string

Cause: Encountered errors (e.g. parsing errors in LOBFILE) while skipping LOBs.

Action: Correct the data file (see accompanying messages) and reload.

SQL\*Loader-00652: Invalid zoned decimal byte.

Cause: Each byte of a zoned decimal field must have a valid value based on the character set encoding used. ASCII-based zoned decimals must follow the formats specified in the VAX Architecture Reference Manual. EBCDIC-based zoned decimals must follow the formats specified in the ESA/390 Principles of Operations, version 8.1.

Action: Check the SQL\*Loader control file's specifications against the log file to ensure that the field location was specified correctly. Check the contents of the field.

SQL\*Loader-00653: XML data set to NULL in column string, row number, table string

Cause: Encountered errors (e.g. parsing errors in LOBFILE) while loading LOBs into an XML column. The row will remain in the table and its XML column will be initialized to null. Loading of other records will continue.

Action: Correct the data file (see accompanying messages) and reload.

SQL\*Loader-00654: Variable length field exceeds maximum length.

Cause: A variable length field (with a leading length subfield) exceeded its maximum allowable length. The maximum length is either the length specified in the SQL\*Loader control file, or, the default if not specified (4kb).

Action: Shorten the field and its length.

SQL\*Loader-00655: cannot load object-relational XML attribute using direct path

Cause: The table being loaded contains a column object which contains an XML attribute with a storage type of object-relational. This type of attribute cannot be loaded with direct path.

Action: Perform the load with conventional path mode.

SQL\*Loader-00656: position specification for column string is not allowed in external table loads

Cause: Use of a position specification was present in an external table load.

Action: Either remove the position specification, change the position specification to a field name reference, use direct path, or use conventional path.

SQL\*Loader-00700: Out of memory while performing essential allocations \[number\]

Cause: SQL\*Loader could not allocate the memory it needs.

Action: Check the operating system and process memory. Increase memory available to SQL\*Loader, if possible. If using direct path, try lowering the columnarrayrows option (see log file for current default value).

SQL\*Loader-00702: Internal error - string

Cause: An internal error has occurred.

Action: Make a note of the message and contact customer support.

SQL\*Loader-00703: Internal error: argument number

Cause: An internal error has occurred.

Action: Make a note of the message and the number, then contact customer support.

SQL\*Loader-00704: Internal error: string \[number\]

Cause: An internal error has occurred.

Action: Make a note of the message and the number, then contact customer support.

SQL\*Loader-00705: Internal error

Cause: An internal error has occurred.

Action: Contact customer support.

SQL\*Loader-00706: Bad argument to ulerr \[number\].

Cause: An internal error has occurred.

Action: Contact customer support.

SQL\*Loader-00708: Internal error: unknown status number returned from sllf layer

Cause: An unknown status was returned by a call to the sllf layer.

Action: Contact customer support.

SQL\*Loader-00709: Internal error calling SLTS layer: string failed

Cause: A nonsuccess status was returned by a call to the SLTS layer.

Action: Contact customer support.

SQL\*Loader-00710: Internal error: direct path stream buffer not loaded

Cause: A direct path stream buffer was built but not loaded.

Action: Contact customer support.

SQL\*Loader-00711: Internal error: bad address for little endian UTF16 conversion

Cause: Address for little endian UTF16 data not in a valid buffer.

Action: Contact customer support.

SQL\*Loader-00712: Internal error: bad address for big endian UTF16 conversion

Cause: Address for big endian UTF16 data not in a valid buffer.

Action: Contact customer support.

SQL\*Loader-00713: Internal error calling SLTS layer: string failed with return code \[number\].

Cause: A nonsuccess status was returned by a call to the SLTS layer.

Action: Contact customer support.

SQL\*Loader-00800: string specified and ignored

Cause: An option was specified that is not supported by External Table load.

Action: Do not specify the unsupported option or do not use External Table load.

SQL\*Loader-00801: all INTO TABLE clauses must have the same options (string)

Cause: At least two INTO TABLE clauses have different options set.

Action: Set the options to be the same or do the loads separately.

SQL\*Loader-00802: numeric EXTERNAL with DEFAULTIF clause not supported by External Table

Cause: A numeric EXTERNAL type was specified with a DEFAULTIF clause and that is not supported by External Table Load.

Action: Remove the clause if possible or do not use External Table Load.

SQL\*Loader-00803: string field type not supported by External Table

Cause: The specified field type is not supported by External Table Load.

Action: Remove the specified field type or do not use External Table Load.

SQL\*Loader-00804: SEQUENCES with intervals are not supported by External Table Load.

Cause: A sequence with an interval is specified and is not supported by External Table Load.

Action: Remove the interval from the sequence, or the the sequence itself, or do not use External Table Load.

SQL\*Loader-00805: string not supported by External Table

Cause: The specified option is not supported by External Table Load.

Action: Remove the specified option or do not use External Table Load.

SQL\*Loader-00806: unknown record format specified for data file

Cause: The osd string containing file processing options in the control file specified an unknown file processing option.

Action: Verify the correct options are specified for the platform being used.

SQL\*Loader-00807: error loading table

Cause: An INSERT statement used to load a table from an external table or a temporary internal table failed. The statement that failed is shown immediately preceding this mesage.

Action: See subsequent messages for more information about the error.

SQL\*Loader-00808: error creating sequence: string

Cause: An attempt to create a sequence needed for the load failed.

Action: See messages that follow this one for information about the failure.

SQL\*Loader-00809: error dropping sequence: string

Cause: A sequence needed to be dropped either because SQL Loader found a sequence with the same name it is trying to create or because SQL Loader is cleaning up from sequences it created at the beginning of the load.

Action: See messages that follow this one for information about why the attampt to drop the sequence failed.

SQL\*Loader-00810: error creating external table: string

Cause: An attempt to create the external table sued for the load failed.

Action: See messages that follow for more information about the failure.

SQL\*Loader-00811: error dropping external table: string

Cause: An error occurred when trying to drop an external table. Note that the table may have been left from a previous load.

Action: None

SQL\*Loader-00812: error creating internal table: string

Cause: An error was encountered trying to create a temporary internal table. The internal table is used only when loading multiple tables from the same data file. The internal table is loaded once and the target tables are loaded from the internal table.

Action: None

SQL\*Loader-00813: error dropping internal table: string

Cause: An error was encountered trying to drop a temporary internal table. The internal table is used only when loading multiple tables from the same data file. The internal table is loaded once and the target tables are loaded from the internal table. The internal table may have been left from a previous build.

Action: None

SQL\*Loader-00816: error creating temporary directory object string for file string

Cause: No existing directory object was found in the database for the directory containing the file. Since all files loaded by external tables must be in a directory named by a directory object, SQL Loader tried to create a directory object for the file.

Action: See error messages that follow this message for more information.

SQL\*Loader-00817: error dropping directory object string

Cause: SQL Loader created a directory object as part of an external table load. An attempt to cleanup the directory object failed.

Action: See messages following this one for more information about the error.

SQL\*Loader-00820: cannot create where clause with range for table string

Cause: The EXTERNAL\_TABLE parameter was specified for a multi-table load, and a WHEN clause for one of the tables contains a reference to a range of bytes in the record. SQL Loader uses the WHEN clause from the control file to generate the WHERE clause in the INSERT statement. If the WHERE clause contains a reference to a range of bytes in the table, then a valid WHERE clause can not be generated. Note that SQL Loader will proceed as if GENERATE\_ONLY was specified for the EXTERNAL\_TABLE parameter.

Action: Modify the control file to only use field references in the WHEN clause. Note that this may require creating a filler field. Another alternative is to create one control file for each table to be loaded and load the table separately.

SQL\*Loader-00821: switching to GENERATE\_ONLY

Cause: SQL Loader is not able to execute the SQL statements it generated for loading the data using external tables. See previous messages for more information.

Action: None

SQL\*Loader-00822: operation not supported on external organized table

Cause: User attempted on operation on an external table which is not supported.

Action: Don't do that!

SQL\*Loader-00823: TREAT AS clause for object tables not supported for external tables

Cause: A TREAT AS clause was specified in the INTO TABLE clause for an object table in the SQL\*Loader control file and the EXTERNAL\_TABLES command line parameter was set to either EXECUTE or GENERATE\_ONLY. External tables can be used to load the data, but SQL\*Loader does not generate the correct SQL statements to do this.

Action: Use SQL\*Loader direct path or SQL\*Loader conventional path to load the table.

SQL\*Loader-00901: Error logging on to ORACLE:

Cause: An attempt was made to log on to Oracle in direct path load mode.

Action: Ensure that the instance is up and running. Check the Oracle messages below this one in the log file for more information.

SQL\*Loader-00902: Error opening cursor: \[number\]

Cause: An internal error has occurred.

Action: Check the Oracle messages below this one in the log file and contact customer support.

SQL\*Loader-00903: Database must be at least version number.number.number.number.number for direct path

Cause: The direct path load mode is being used with an incompatible database.

Action: Upgrade the database to the specified version or else use the conventional path load.

SQL\*Loader-00904: You cannot used the direct path when linked with v5 of the database

Cause: The direct path mode is being used after SQL\*Loader has been linked with a Version 5 database.

Action: Use the conventional path.

SQL\*Loader-00905: Error parsing SQL statement for upi: \[number\]

Action: Check the message below this one in the log file for more information.

SQL\*Loader-00906: Error executing SQL statement for upi: \[number\]

Cause: An internal error has occurred.

Action: Check the message below this one in the log file for more information.

SQL\*Loader-00909: Loader views must be loaded (as SYS) for direct path to be used

Cause: Database views required for the direct path mode are not present.

Action: The Oracle7 Server Administrator's Guide details how to run the required scripts as user SYS for loading the required views.

SQL\*Loader-00910: Error binding input variables for upi: \[number\]

Action: Check the message below this one in the log file for more information.

SQL\*Loader-00911: Error defining output variable(s) for upi: \[number\]

Action: Check the message below this one in the log file for more information.

SQL\*Loader-00913: Error fetching results of select statement (upi): \[number\]

Action: Check the message below this one in the log file for more information.

SQL\*Loader-00914: Error locking table string in exclusive mode.

Cause: The direct path mode could not lock the named table.

Action: Check the message below this one in the log file for more information. Check that the necessary privileges have been granted.

SQL\*Loader-00915: Error closing cursor: \[number\]

Action: CCheck the message below this one in the log file for more information.

SQL\*Loader-00916: Error checking path homogeneity

Cause: To do a direct path load load when the front end and back end of the database are on separate hardware systems, the systems must be identical, using the same machine, operating system, and character set. This error occurs when SQL\*Loader detects a difference between the systems that will prevent a direct load from operating properly.

Action: Use a conventional path load for this configuration.

SQL\*Loader-00918: The catalog must be loaded (as SYS) for SQL\*Loader to be used

Cause: The catalog is not loaded.

Action: Logon as user SYS and load the Oracle7 catalog and the views in the script ULVIEW.SQL.

SQL\*Loader-00919: Error during upi fetch: \[number\]

Cause: An internal error has occurred.

Action: Check the message below this one in the log file for more information.

SQL\*Loader-00925: Error while string

Cause: An internal error has occurred.

Action: Check the message below this one in the log file for more information. The table or column referenced may not be accessible.

SQL\*Loader-00926: OCI error while string for table string

Cause: An OCI error has occurred.

Action: Check the message below this one in the log file for more information. The table or column referenced may not be accessible.

SQL\*Loader-00929: Error parsing insert statement for table string.

Cause: The table's insert statement caused a parse error.

Action: Check all SQL strings that were used.

SQL\*Loader-00930: Error parsing insert statement for table string column string.

Cause: The named column's INSERT statement caused a parse error.

Action: Check the message below this one in the log file for more information. Check the SQL string used for this column.

SQL\*Loader-00931: OCI error while binding variable for column string in table string

Cause: An OCI error has occurred.

Action: Check the errors below it for more information. The SQL string for this column may be in error.

SQL\*Loader-00932: Could not truncate table string.

Cause: Truncation of the table was attempted and failed.

Action: Check the following errors for more information. Truncation due to referential constraints should not occur.

SQL\*Loader-00933: Specified file string not part of database

Cause: The specified filename to load the table is not a database file.

Action: Specify a valid datafile.

SQL\*Loader-00934: Incorrect data file string specified for table string

Cause: A datafile name was given to load the table that is not a part of the tablespace in which the table resides.

Action: Specify a valid datafile.

SQL\*Loader-00935: Error verifying required option for parallel load.

Cause: An error was encountered because a required option was not found or was invalid.

Action: Correct the problem as described in the accompanying Oracle message.

SQL\*Loader-00937: parallel load requested and string has enabled triggers or constraints

Cause: A request was made for a parallel direct load, but the object to be loaded has an enabled constraint (check, referential) and/or enabled triggers.

Action: Disable the offending enabled constraints and/or triggers and retry the parallel direct load.

SQL\*Loader-00938: partition load requested and string has enabled triggers or constraints

Cause: A request was made for a direct load of a single partition, but the object to be loaded has an enabled constraint (check, referential) and/or enabled triggers.

Action: Disable the offending enabled constraints and/or triggers and retry the parallel direct load.

SQL\*Loader-00939: OCI error while string for table string partition string

Action: Check the following errors for more information. The table or partition referenced may not be accessible.

SQL\*Loader-00940: UPI error while setting NCHAR bind attributes for column string table string

Cause: An error occured while setting the charsetform attribute of an NCHAR column.

Action: This is an internal error. Report to ORACLE support.

SQL\*Loader-00941: Error during describe of table string

Cause: Error while executing a describe of a select list on the given table. Check the error immediately preceding this error.

Action: None

SQL\*Loader-00942: partition string not part of table string

Cause: the specified partition is not part of the specified table

Action: None

SQL\*Loader-00943: incorrect datafile string specified for table string partition string

Cause: The specified datafile is not in the tablespace of the specified partition. Due to use of FILE= keyword on a partitioned table. When loading all partitions of a partitioned table, the partitions must be in the same tablespace. When loading a single partition, the tablespace of the partition being loaded must be the same as the tablespace in which the specified datafile file resides.

Action: None

SQL\*Loader-00944: error preparing insert statement for table string.

Cause: A call to OCIStmtPrepare for the table's insert statement returned an error.

Action: Refer to the message that follows for information about the error returned by OCIStmtPrepare. Make sure the syntax is correct for all SQL strings specified in the SQL\*Loader control file.

SQL\*Loader-00945: record size number too large for direct path

Cause: The maximum size of records in the data file is larger than the maximum size supported by direct path, which is 65535

Action: Load the data file using conventional path.

SQL\*Loader-00946: OCI error while string for table string subpartition string

Action: Check the following errors for more information. The table or subpartition referenced may not be accessible.

SQL\*Loader-00947: subpartition load requested and string has enabled triggers or constraints

Cause: A request was made for a direct load of a single subpartition, but the object to be loaded has an enabled constraint (check, referential) and/or enabled triggers.

Action: Disable the offending enabled constraints and/or triggers and retry the parallel direct load.

SQL\*Loader-00948: subpartition string not part of table string

Cause: the specified subpartition is not part of the specified table

Action: None

SQL\*Loader-00949: incorrect datafile string specified for table string subpartition string

Cause: The specified datafile is not in the tablespace of the specified subpartition. Due to use of FILE= keyword on a subpartitioned table. When loading all subpartitions of a subpartitioned table, the subpartitions must be in the same tablespace. When loading a single subpartition, the tablespace of the subpartition being loaded must be the same as the tablespace in which the specified datafile file resides.

Action: None

SQL\*Loader-00950: Error shipping data structures across 2-task

Action: Check the error(s) below it for more information.

SQL\*Loader-00951: Error calling once/load initialization

Action: Check the error(s) below it for more information.

SQL\*Loader-00952: Error calling once/data file initialization

Action: Check the error(s) below it for more information.

SQL\*Loader-00953: Error shipping read buffer across 2-task

Action: Check the error(s) below it for more information.

SQL\*Loader-00954: Error shipping index to read buffer across 2-task

Action: Check the error(s) below it for more information.

SQL\*Loader-00955: Error calling col array build, block formatter

Action: Check the error(s) below it for more information.

SQL\*Loader-00956: Error calling once/data file finishing

Action: Check the error(s) below it for more information.

SQL\*Loader-00957: Error shipping text string across 2-task

Action: Check the error(s) below it for more information.

SQL\*Loader-00958: Error popping data relocation address stack

Action: Check the error(s) below it for more information.

SQL\*Loader-00959: Error shipping buffer across 2-task

Action: Check the error(s) below it for more information.

SQL\*Loader-00961: Error calling once/load finishing for table string

Action: Check the error(s) below it for more information.

SQL\*Loader-00962: Error setting user-side Ctrl-C handler

Action: Check the error(s) below it for more information.

SQL\*Loader-00963: Error clearing user-side Ctrl-C handler

Action: Check the error(s) below it for more information.

SQL\*Loader-00965: Error number disabling constraint string on table string

Action: Check the error(s) below it for more information.

SQL\*Loader-00966: Error number disabling all triggers on table string

Action: Check the error(s) below it for more information.

SQL\*Loader-00969: Error performing file name translation on kernel side

Cause: File specified for parallel load is probably not a valid database file.

Action: Specify a valid database file.

SQL\*Loader-00970: enabled constraint on an XML column not allowed in direct path

Cause: An enabled check constraint existed on an XML column.

Action: Disable the check constraint before attempting to load the table data using the direct path mode, or leave the constraint enabled but use the conventional path mode instead.

SQL\*Loader-00971: parallel load option not allowed when loading lob columns

Cause: An attempt was made to load lob columns using parallel=true. This error will also be issued when loading columns stored as lobs (such as varrays and xml types)

Action: Do not use the parallel option when loading lob columns.

SQL\*Loader-00972: Warning: ROWS parameter ignored when NO\_INDEX\_ERRORS is used.

Cause: Specifying save points using the ROWS parameter was not supported with NO\_INDEX\_ERRORS=TRUE.

Action: Remove the ROWS parameter from the command-line arguments or do not specify NO\_INDEX\_ERRORS=TRUE.

SQL\*Loader-00973: Warning: ROWS parameter ignored when PARTITION\_MEMORY is used.

Cause: Specifying save points using the ROWS parameter was not supported with PARTITION\_MEMORY=n.

Action: Remove the ROWS parameter from the command-line arguments or do not specify PARTITION\_MEMORY=n.

SQL\*Loader-02026: the load was aborted because SQL Loader cannot continue.

Cause: The load cannot continue. See the error message before this

\* message for the cause of the error.

Action: See the action for the error message that precedes this one.

SQL\*Loader-02050: Multibyte character error.

Cause: Text specified by POSITION or terminated by newlines is invalid.

Action: Edit the SQL\*Loader control file or the data file to fix alignment of column.

SQL\*Loader-03120: Resumable parameters ignored -- current session not resumable

Cause: Current session is not resumable.

Action: Must specify RESUMABLE=TRUE to enable resumable session in order for the RESUMABLE\_NAME and RESUMABLE\_TIMEOUT parameters to take effect.