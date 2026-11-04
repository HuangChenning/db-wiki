---
title: Database Error Messages
book: Database Error Messages
doc_id: F30283-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/errmg/SQL-Loader-00100.html
tags:
  - oracle
  - 21c
  - error-messages
---

SQL\*Loader-00100: Syntax error on command-line\\n

Cause: Possible causes for this error include: placing a positional argument after keyword arguments, misspelling a keyword, not balancing parentheses or quotes, or leaving space between the operator, '=', and an argument.

Action: Check the command syntax and the spelling, then retry.

SQL\*Loader-00101: Invalid argument for username/password\\n

Cause: The username/password argument specified on the command line was not recognized. Another argument (not identified by a keyword) could be in the position where username/password is expected.

Action: Check the format of the username/password argument, which is the first argument on the command line, if arguments are given without keywords.

SQL\*Loader-00102: Invalid control file name on command line\\n

Cause: The control file name specified on the command line was not recognized. It could be misspelled, or another argument (not identified by a keyword) could be in its place. One possible cause is the existence of a space between username and password. See error 101, above. Another is that the specified file name caused an overflow of the output buffer.

Action: Check the spelling and position of the arguments on the command line.

SQL\*Loader-00103: Invalid log file name on command line\\n

Cause: The log file name specified on the command line was not recognized. It could be misspelled, or another argument (not identified by a keyword) could be in its place. Another possible cause is that the specified file name caused an overflow of the output buffer.

Action: Check the spelling and position of the arguments on the command line.

SQL\*Loader-00104: Invalid bad file name on command line\\n

Cause: The bad file name specified on the command line was not recognized. It could be misspelled, or another argument (not identified by a keyword) could be in its place. Another possible cause is that the specified file name caused an overflow of the output buffer.

Action: Correct it.

SQL\*Loader-00105: Invalid data file name on command line\\n

Cause: The datafile name specified on the command line was not recognized. It could be misspelled, or another argument (not identified by a keyword) could be in its place. Another possible cause is that the specified file name caused an overflow of the output buffer.

Action: Check the spelling and position of the arguments on the command line.

SQL\*Loader-00106: Invalid discard file name on command line\\n

Cause: The discard file name specified on the command line was not recognized. It could be misspelled, or another argument (not identified by a keyword) could be in its place. Another possible cause is that the specified file name caused an overflow of the output buffer.

Action: Check the spelling and position of the arguments on the command line.

SQL\*Loader-00107: Invalid maximum number of discards\\n

Cause: The argument's value is inappropriate, or another argument (not identified by a keyword) is in its place.

Action: Check the command line and retry.

SQL\*Loader-00108: Invalid number of logical records to load\\n

Cause: The argument's value is inappropriate, or another argument (not identified by a keyword) is in its place.

Action: Check the command line and retry.

SQL\*Loader-00109: Invalid number of logical records to skip\\n

Cause: The argument's value is inappropriate, or another argument (not identified by a keyword) is in its place.

Action: Check the command line and retry.

SQL\*Loader-00110: Invalid maximum number of errors\\n

Cause: The argument's value is inappropriate, or another argument (not identified by a keyword) is in its place.

Action: Check the command line and retry.

SQL\*Loader-00111: Invalid number of rows for bind array or data saves\\n

Cause: The argument's value is inappropriate, or another argument (not identified by a keyword) is in its place.

Action: Check the command line and retry.

SQL\*Loader-00112: Invalid maximum bind array size\\n

Cause: The argument's value is inappropriate, or another argument (not identified by a keyword) is in its place.

Action: Check the command line and retry.

SQL\*Loader-00113: Invalid silent mode option\\n

Cause: The only valid options for the SILENT command-line argument are ALL, ERROR, FEEDBACK, or HEADER. The argument could be misspelled, or another argument (not identified by a keyword) could be in its place.

Action: Check the command line and retry.

SQL\*Loader-00114: Error in OPTIONS statement\\n

Cause: Command line options specified in the SQL\*Loader control file with the OPTIONS clause were found to be incorrect.

Action: Check the format of the OPTIONS clause in the SQL\*Loader control file.

SQL\*Loader-00115: Invalid direct path option\\n

Cause: The only valid options for the DIRECT command-line argument are TRUE or FALSE. The argument could be misspelled, or another argument (not identified by a keyword) could be in its place.

Action: Check the command line and retry.

SQL\*Loader-00116: Error prompting for password\\n

Cause: An internal error has occurred.

Action: Contact customer support.

SQL\*Loader-00118: Invalid parallel load option\\n

Cause: The command-line argument used for the parallel load is incorrect.

Action: Use only TRUE or FALSE as the value for the parallel load option.

SQL\*Loader-00119: Invalid parallel file (data file) name on command line\\n

Cause: The command-line argument for the parallel file was entered incorrectly. One possible cause is that the specified file name caused an overflow of the output buffer.

Action: Check the command line argument and retry the operation.

SQL\*Loader-00120: Invalid \_synchro option string\\n

Cause: The command-line argument \_synchro is incorrect.

Action: Use only one of the allowed modes: see ulminv\[\].

SQL\*Loader-00121: Invalid skip\_unusable\_indexes option\\n

Cause: The command line argument for skip\_unusable\_indexes is incorrect.

Action: Use only TRUE or FALSE as the value for the skip\_unusable\_indexes option.

SQL\*Loader-00122: Invalid skip\_index\_maintenance option\\n

Cause: The command line argument for skip\_index\_maintenance is incorrect.

Action: Use only true or falseas the value for the skip\_index\_maintenance option. (Note: only on direct loads!)

SQL\*Loader-00123: specified value for bindsize(number) less than readsize(number)\\n

Cause: The command line argument specified for bindsize was less than the value of readsize.

Action: No action is required. SQL\*Loader automatically adjusts the value of bindsize to equal the value of readsize.

SQL\*Loader-00124: specified value for readsize(number) less than bindsize(number)\\n

Cause: The command line argument specified for readsize was less than the value of bindsize.

Action: No action is required. SQL\*Loader automatically adjusts the value of readsize to equal the value of bindsize.

SQL\*Loader-00125: specified value for readsize(number) less than max\_record\_size(number)\\n

Cause: The command line argument specified for readsize was less than the value of max\_record\_size.

Action: No action is required. SQL\*Loader automatically adjusts the value of readsize to equal the value of max\_record\_size.

SQL\*Loader-00126: Invalid read size\\n

Cause: The argument's value is inappropriate, or another argument (not identified by a keyword) is in its place.

Action: Check the command line and retry.

SQL\*Loader-00127: Invalid maximum record size\\n

Cause: The argument's value is inappropriate, or another argument (not identified by a keyword) is in its place.

Action: Check the command line and retry.

SQL\*Loader-00128: unable to begin a session\\n

Cause: An error occurred when attempting to start a session on the database.

Action: See the message that follows this message for information on the cause of the error.

SQL\*Loader-00129: Invalid number of rows for direct path column array\\n

Cause: The argument's value is inappropriate

Action: Check the command line and retry.

SQL\*Loader-00130: Invalid direct path stream size\\n

Cause: The argument's value is inappropriate

Action: Check the command line and retry.

SQL\*Loader-00131: Invalid multithreading option\\n

Cause: The only valid options for the MULTITHREADING command-line argument are TRUE or FALSE. The argument could be misspelled, or another argument (not identified by a keyword) could be in its place.

Action: Check the command line and retry.

SQL\*Loader-00132: invalid argument for external table option\\n

Cause: The command line argument specified for external\_tables was not TRUE or FALSE

Action: Check the command line and retry.

SQL\*Loader-00133: Can't specify both direct path and external tables\\n

Cause: Both options for direct path and exrernal tables were indicated. Only one of these can be applied at a time.

Action: Change at least one of the parameters to enable only one.

SQL\*Loader-00134: invalid option specified for EXTERNAL\_TABLE parameter\\n

Cause: An invalid value was specified for the EXTERNAL\_TABLE parameter.

Action: Specify one of the following values. NOT\_USED disables use of external tables. GENERATE\_ONLY generates the SQL statements that will use external tables to load the data. EXECUTE both generates the SQL statements and then executes them.

SQL\*Loader-00135: Invalid argument for RESUMABLE\\n

Cause: The command line argument specified for RESUMABLE was not TRUE or FALSE.

Action: Check the command line and retry.

SQL\*Loader-00136: Invalid argument for RESUMABLE\_NAME\\n

Cause: The command line argument specified for RESUMABLE\_NAME was not a valid string.

Action: Check the command line and retry.

SQL\*Loader-00137: Invalid value for RESUMABLE\_TIMEOUT\\n

Cause: The command line argument specified for RESUMABLE\_TIMEOUT was not a valid positive integer.

Action: Check the command line and retry.

SQL\*Loader-00138: Invalid value for DATE\_CACHE\\n

Cause: The command line argument specified for DATE\_CACHE was not a valid positive integer.

Action: Check the command line and retry.

SQL\*Loader-00144: Conflicting load methods: string/string specified.\\n

Cause: External table mode and direct path mode were both specified.

Action: Specify only one load method.

SQL\*Loader-00145: Invalid value for NO\_INDEX\_ERRORS\\n

Cause: The command line argument specified was not a valid boolean.

Action: Check the command line and retry.

SQL\*Loader-00146: Invalid value for PARTITION\_MEMORY\\n

Cause: The command line argument specified was not -1, 0, or positive.

Action: Check the command line and retry.

SQL\*Loader-00147: Warning: The NO\_INDEX\_ERRORS parameter is ignored for direct path parallel loads.\\n

Cause: The NO\_INDEX\_ERRORS parameter was specified for a parallel load.

Action: Do not use the NO\_INDEX\_ERRORS parameter for parallel loads.

SQL\*Loader-00148: Invalid value for the TABLE parameter.\\n

Cause: The command line argument specified for the TABLE parameter was not a valid string. It is also possible that the schema name or the table name overflowed the output buffer which allows for the maximum identifier size in the database character set.

Action: Check the command line and retry.

SQL\*Loader-00149: Control file cannot be specified with the TABLE parameter.\\n

Cause: A control file was specified along with the TABLE parameter.

Action: Check the command line and retry. If you are doing an express mode load, omit the control file. If you are not doing an express mode load, omit the TABLE parameter.

SQL\*Loader-00170: invalid value for EMPTY\_LOBS\_ARE\_NULL\\n

Cause: The command line argument specified was not a valid boolean.

Action: Check the command line and retry.

SQL\*Loader-00172: invalid value for DIRECT\_PATH\_LOCK\_WAIT\\n

Cause: The command line argument specified was not a valid boolean.

Action: Check the command line and retry.

SQL\*Loader-00173: invalid value for DNFS\_ENABLE\\n

Cause: The command line argument specified was not a valid boolean.

Action: Check the command line and retry.

SQL\*Loader-00174: conflicting values for PARALLEL and DEGREE\_OF\_PARALLELISM parameters\\n

Cause: Conflicting values were specified for the parallel setting. This could be caused by: 1) having PARALLEL=TRUE and DEGREE\_OF\_PARALLELISM=NONE(or 1) 2) PARALLEL=FALSE and DEGREE\_OF\_PARALLELISM being set to a value other than NONE or 1.

Action: Verify the values for PARALLEL and DEGREE\_OF\_PARALLELISM.

SQL\*Loader-00175: invalid number of Direct NFS (dNFS) read buffers\\n

Cause: The argument's value was inappropriate.

Action: Check the command line and retry.

SQL\*Loader-00176: Invalid value for the DATE\_FORMAT parameter.\\n

Cause: The command line argument specified for the DATE\_FORMAT parameter was not a valid string.

Action: Check the command line and retry.

SQL\*Loader-00177: The DATE\_FORMAT parameter can only be specified with the TABLE parameter.\\n

Cause: A control file was specified along with the DATE\_FORMAT parameter.

Action: Check the command line and retry. If you are doing an express mode load, omit the control file. If you are not doing an express mode load, omit the DATE\_FORMAT parameter.

SQL\*Loader-00178: Invalid value for the TERMINATED\_BY parameter.\\n

Cause: The command line argument specified for the TERMINATED\_BY parameter was not a valid string.

Action: Check the command line and retry.

SQL\*Loader-00179: Invalid hexadecimal value for the TERMINATED\_BY parameter.\\n

Cause: The command line argument specified for the TERMINATED\_BY parameter was not a valid hexadecimal string.

Action: Check the command line and retry.

SQL\*Loader-00180: Invalid hexadecimal value for the table-level NULLIF parameter.\\n

Cause: The command line argument specified for the table-level NULLIF parameter was not a valid hexadecimal string.

Action: Check the command line and retry.

SQL\*Loader-00181: The TERMINATED\_BY parameter cannot be specified without the TABLE parameter.\\n

Cause: The TERMINATED\_BY parameter was specified without the TABLE parameter.

Action: Check the command line and retry. If you are doing an express mode load, include the TABLE parameter and omit the control file. If you are not doing an express mode load, omit the TERMINATED\_BY parameter.

SQL\*Loader-00182: Invalid value for the ENCLOSED\_BY parameter.\\n

Cause: The command line argument specified for the ENCLOSED\_BY parameter was not a valid string.

Action: Check the command line and retry.

SQL\*Loader-00183: invalid hexadecimal value for the ENCLOSED\_BY parameter: string\\n

Cause: The command line argument specified for the ENCLOSED\_BY parameter was not a valid hexadecimal string.

Action: Check the command line and retry.

SQL\*Loader-00184: The ENCLOSED\_BY parameter cannot be specified with the OPTIONALLY\_ENCLOSED\_BY parameter.\\n

Cause: Both the ENCLOSED\_BY parameter and the OPTIONALLY\_ENCLOSED\_BY parameter were specified.

Action: Check the command line and retry. Specify only the ENCLOSED\_BY parameter or the OPTIONALLY\_ENCLOSED\_BY parameter.

SQL\*Loader-00185: The ENCLOSED\_BY parameter cannot be specified without the TABLE parameter.\\n

Cause: The ENCLOSED\_BY parameter was specified without the TABLE parameter.

Action: Check the command line and retry. If you are doing an express mode load, include the TABLE parameter and omit the control file. If you are not doing an express mode load, omit the ENCLOSED\_BY parameter.

SQL\*Loader-00186: Invalid value for the OPTIONALLY\_ENCLOSED\_BY parameter.\\n

Cause: The command line argument specified for the OPTIONALLY\_ENCLOSED\_BY parameter was not a valid string.

Action: Check the command line and retry.

SQL\*Loader-00187: invalid hexadecimal value for the OPTIONALLY\_ENCLOSED\_BY parameter: string\\n

Cause: The command line argument specified for the OPTIONALLY\_ENCLOSED\_BY parameter was not a valid hexadecimal string.

Action: Check the command line and retry.

SQL\*Loader-00188: The OPTIONALLY\_ENCLOSED\_BY parameter cannot be specified with the ENCLOSED\_BY parameter.\\n

Cause: Both the OPTIONALLY\_ENCLOSED\_BY parameter and the ENCLOSED\_BY parameter were specified.

Action: Check the command line and retry. Specify only the OPTIONALLY\_ENCLOSED\_BY parameter or the ENCLOSED\_BY parameter.

SQL\*Loader-00189: The OPTIONALLY\_ENCLOSED\_BY parameter cannot be specified without the TABLE parameter.\\n

Cause: The OPTIONALLY\_ENCLOSED\_BY parameter was specified without the TABLE parameter.

Action: Check the command line and retry. If you are doing an express mode load, include the TABLE parameter and omit the control file. If you are not doing an express mode load, omit the OPTIONALLY\_ENCLOSED\_BY parameter.

SQL\*Loader-00190: Invalid value for the CHARACTERSET parameter.\\n

Cause: The command line argument specified for the CHARACTERSET parameter was not a valid string.

Action: Check the command line and retry.

SQL\*Loader-00191: The CHARACTERSET parameter can only be specified with the TABLE parameter.\\n

Cause: A control file was specified along with the CHARACTERSET parameter.

Action: Check the command line and retry. If you are doing an express mode load, omit the control file. If you are not doing an express mode load, omit the CHARACTERSET parameter.

SQL\*Loader-00192: The CHARACTERSET parameter cannot be specified without the TABLE parameter.\\n

Cause: The CHARACTERSET parameter was specified without the TABLE parameter.

Action: Check the command line and retry. If you are doing an express mode load, include the TABLE parameter and omit the control file. If you are not doing an express mode load, omit the CHARACTERSET parameter.

SQL\*Loader-00193: Invalid value for the DEGREE\_OF\_PARALLELISM parameter.\\n

Cause: The command line argument specified for the DEGREE\_OF\_PARALLELISM parameter was not a valid string.

Action: Check the command line and retry.

SQL\*Loader-00194: Option string specified and ignored for string path load.\\n

Cause: An option was specified that is not supported for conventional path or direct path.

Action: Do not specify the unsupported option or do not use conventional path or direct path load.

SQL\*Loader-00195: Invalid value for the TRIM parameter.\\n

Cause: The command line argument specified for the TRIM parameter was not a valid string.

Action: Check the command line and retry.

SQL\*Loader-00196: Invalid value for the CSV parameter.\\n

Cause: The command line argument specified for the CSV parameter was not a valid string.

Action: Check the command line and retry.

SQL\*Loader-00197: Invalid value for the TIMESTAMP\_FORMAT parameter.\\n

Cause: The command line argument specified for the TIMESTAMP\_FORMAT parameter was not a valid string.

Action: Check the command line and retry.

SQL\*Loader-00198: The TIMESTAMP\_FORMAT parameter can only be specified with the TABLE parameter.\\n

Cause: A control file was specified along with the TIMESTAMP\_FORMAT parameter.

Action: Check the command line and retry. If you are doing an express mode load, omit the control file. If you are not doing an express mode load, omit the TIMESTAMP\_FORMAT parameter.

SQL\*Loader-00199: Invalid value for the NULLIF parameter.\\n

Cause: The command line argument specified for the NULLIF parameter was not a valid string.

Action: Check the command line and retry.

SQL\*Loader-00200: FORMAT clause should not be present - flat data files only\\n

Cause: SQL/DS FORMAT clause is not supported.

Action: Remove the FORMAT command from the SQL\*Loader control file or

SQL\*Loader-00201: There is an invalid value for the CSV clause.\\n

Cause: The control file clause specified for CSV was neither CSV WITH EMBEDDED or CSV WITHOUT EMBEDDED.

Action: Check the control file CSV clause syntax and retry.

SQL\*Loader-00202: shift-based character sets not supported with CSV format files with embedded record terminators\\n

Cause: A CSV format file with embedded record terminators was specified with a shift-based character set.

Action: Either use a nonshift-based character set or do not use CSV format files with embedded record terminators.

SQL\*Loader-00203: The NULLIF parameter can only be specified with the TABLE parameter.\\n

Cause: A control file was specified along with the NULLIF parameter.

Action: Check the command line and retry. If you are doing an express mode load, omit the control file. If you are not doing an express mode load, omit the NULLIF parameter.

SQL\*Loader-00204: Invalid value for the FIELD\_NAMES parameter.\\n

Cause: The command line argument specified for the FIELD\_NAMES parameter was not a valid string. You must specify FIRST, FIRST\_IGNORE, ALL, ALL\_IGNORE, or NONE.

Action: Check the command line and retry.

SQL\*Loader-00205: The FIELD\_NAMES parameter can only be specified with the TABLE parameter.\\n

Cause: A control file was specified along with the FIELD\_NAMES parameter.

Action: Check the command line and retry. If you are doing an express mode load, omit the control file. If you are not doing an express mode load, omit the FIELD\_NAMES parameter.

SQL\*Loader-00206: Empty field name for field number in the FIELD NAMES record in data file\\n

Cause: A field name in the FIELD NAMES record was empty.

Action: Specify a valid field name and retry the operation.

SQL\*Loader-00207: Missing one or more field names in the FIELD NAMES record in the data file. Found number fields, there should be number fields.\\n

Cause: One or more field names was not listed in the FIELD NAMES record. However, it was listed in the access parameter list for the external table.

Action: Include all field names in the data file and retry the operation.

SQL\*Loader-00208: Error on the FIELD NAMES record for table string, field stringstringstring was not found in the control file.\\n

Cause: The listed field was not found in the control file field list. The next error message lists the name of the data file where the error was found.

Action: Check the listed field and fix it. Then retry the operation.

SQL\*Loader-00209: error processing the FIELD NAMES record in data file string.\\n

Cause: An error occurred while processing the FIELD NAMES record for the data file.

Action: See messages that preceed this one for more details. Fix the error and retry the operation.

SQL\*Loader-00210: first data file is empty, cannot process the FIELD NAMES record\\n

Cause: The data file listed in the next message was empty. Therefore, the FIELD NAMES FIRST FILE directive could not be processed.

Action: Check the listed data file and fix it. Then retry the operation.

SQL\*Loader-00211: Field name stringstringstring in the FIELD NAMES record in the data file is too long.\\n

Cause: The field name exceeded the maximum of 30 characters.

Action: Specify at most 30 characters.

SQL\*Loader-00212: The field level ENCLOSED BY clause is not allowed with the CSV WITH EMBEDDED clause.\\n

Cause: A field level ENCLOSED BY clause was specified with the CSV WITH EMBEDDED clause. All fields must use the same ENCLOSED BY or OPTIONALLY ENCLOSED BY clause for CSV files with embedded record terminators.

Action: Either remove the field level ENCLOSED BY clause, or, if the data file does not contain embedded record terminators, change CSV WITH EMBEDDED to CSV WITHOUT EMBEDDED.

SQL\*Loader-00213: Invalid value for the table parameter\\n

Cause: The table name specified on the command line was not recognized. It could be misspelled, or another argument (not identified by a keyword) could be in its place. The schema name or the table name may have been too long for a valid database identifier in the database character set.

Action: Check the spelling and position of the arguments on the command line.

SQL\*Loader-00214: Invalid value for the table name in the INTO TABLE clause\\n

Cause: The table name specified in the INTO TABLE clause was not recognized. The schema name or the table name may have been too long for a valid database identifier in the database character set.

Action: Check the name and try again with a valid table name.

SQL\*Loader-00215: Invalid data file name in INFILE statement\\n

Cause: The datafile name specified in INFILE statement was not recognized. It could be misspelled, or the length may exceed the maximum file specification allowed on the platform.

Action: Check the spelling and length of the data file specification.

SQL\*Loader-00216: Invalid bad file name in BADFILE statement\\n

Cause: The bad file name specified in the BADFILE statement was not recognized. It could be misspelled, or the length may exceed the maximum file specification allowed on the platform.

Action: Check the spelling and length of the bad file specification.

SQL\*Loader-00217: Invalid discard file name in DISCARDFILE statement\\n

Cause: The discard file name specified in the DISCARDFILE statement was not recognized. It could be misspelled, or the length may exceed the maximum file specification allowed on the platform.

Action: Check the spelling and length of the discard file specification.

SQL\*Loader-00218: Specified command-line parameter string ignored since not an express mode load.\\n

Cause: A command-line parameter was specified that is supported only for express mode and not for loads which use a control file.

Action: Omit the option which is not supported if the option is not needed or use the control file syntax for the option. For example, use the CSV WITH EMBEDDED or CSV WITHOUT EMBEDDED control file syntax.

SQL\*Loader-00219: Invalid value for parameter SDF\_PREFIX\\n

Cause: The value for the SDF\_PREFIX parameter was not recognized or the value of the parameter was too long.

Action: Verify the value specified and shorten it if possible.

SQL\*Loader-00220: invalid value for the exceptions table name in the REENABLE clause\\n

Cause: The table name specified for the exceptions table in the REENABLE disabled constraints clause was not recognized. The schema name or the table name may have been too long for a valid database identifier in the database character set.

Action: Check the name and try again with a valid table name.

SQL\*Loader-00221: invalid value for the partition or subpartition name\\n

Cause: The name specified for the partition or subpartition was not recognized. The name may have been too long for a valid database identifier in the database character set.

Action: Check the name and try again with a valid partition or subpartition name.

SQL\*Loader-00222: invalid option specified for DEFAULTS parameter\\n

Cause: An invalid value was specified for the DEFAULTS parameter.

Action: Specify one of the following values: - IGNORE to disable loading of default values. - EVALUATE\_ONCE to load default values, but evaluate default expressions once at the beginning of the load. - EVALUATE\_EVERY\_ROW to load default values and evaluate default expressions for each row. - IGNORE\_UNSUPPORTED\_EVALUTE\_ONCE to load default values where supported, ignore otherwise. Evaluate defaults once. - IGNORE\_UNSUPPORTED\_EVALUTE\_EVERY\_ROW to load default values where supported, ignore otherwise. Evaluate defaults every row.

SQL\*Loader-00223: Warning: The DEFAULTS parameter is ignored for non-direct path loads.\\n

Cause: The DEFAULTS parameter was specified for a non-direct path load.

Action: Do not use the DEFAULTS parameter for non-direct path loads.

SQL\*Loader-00225: invalid value for the CREDENTIAL parameter\\n

Cause: The command line argument specified for the CREDENTIAL parameter was not a valid string.

Action: Check the command line and retry.

SQL\*Loader-00227: invalid value for the wallet parameter\\n

Cause: The command line argument specified for the wallet parameter was not a valid string.

Action: Check the command line and retry.

SQL\*Loader-00228: could not initialize the client wallet\\n

Cause: SQL\*Loader could not initialize the client wallet.

Action: Ensure that a valid wallet exists in the default or specified wallet location.

SQL\*Loader-00229: could not open the client wallet\\n

Cause: SQL\*Loader could not open the client wallet.

Action: Ensure that a valid wallet exists in the default or specified wallet location.

SQL\*Loader-00230: object store password not found in the client wallet\\n

Cause: SQL\*Loader could not load the password from the client wallet.

Action: Ensure that a valid wallet exists in the default or specified wallet location and that it contains the expected credential.

SQL\*Loader-00231: object store username not found in the client wallet\\n

Cause: SQL\*Loader could not load the username from the client wallet.

Action: Ensure that a valid wallet exists in the default or specified wallet location and that it contains the expected credential.

SQL\*Loader-00232: could not read from the client wallet\\n

Cause: SQL\*Loader could not load the username or password from the client wallet.

Action: Ensure that a valid wallet exists in the default or specified wallet location and that it contains the expected credential.

SQL\*Loader-00233: invalid value for the PROXY parameter\\n

Cause: The command line argument specified for the PROXY parameter was not a valid string.

Action: Check the command line and retry.

SQL\*Loader-00234: The proxy value could not be found.\\n

Cause: The database property for the http proxy was not set.

Action: Set the http proxy database attribute.

SQL\*Loader-00235: External table mode was not used when loading from an object store.\\n

Cause: SQL\*Loader could not use the external table mode to load from an object store.

Action: None. This is an informational message issued when external table mode would have been used if not loading from an object store.

SQL\*Loader-00236: unable to create credential used internally by SQL\*Loader\\n

Cause: An internal error occurred.

Action: Contact Oracle Support Services.

SQL\*Loader-00237: unable to drop credential used internally by SQL\*Loader\\n

Cause: An internal error has occurred.

Action: Contact Oracle Support Services.

SQL\*Loader-00238: invalid value for the GSM\_NAME parameter\\n

Cause: The command line argument specified for the GSM\_NAME parameter was not a valid string.

Action: Check the command line and retry.

SQL\*Loader-00239: invalid value for the GSM\_HOST parameter\\n

Cause: The command line argument specified for the GSM\_HOST parameter was not a valid string.

Action: Check the command line and retry.

SQL\*Loader-00240: invalid value for the GSM\_PORT parameter\\n

Cause: The command line argument specified for the GSM\_PORT parameter was not a valid string.

Action: Check the command line and retry.

SQL\*Loader-00241: invalid value for the READER\_COUNT parameter\\n

Cause: The command line argument specified for the READER\_COUNT parameter was not a valid number.

Action: Check the command line and retry.

SQL\*Loader-00242: invalid value for the LOAD\_SHARD parameter\\n

Cause: The command line argument specified for the LOAD\_SHARD parameter was not a valid string.

Action: Check the command line and retry.

SQL\*Loader-00243: invalid value for the COMPRESS\_STREAM parameter\\n

Cause: The command line argument specified for the COMPRESS\_STREAM parameter was not a valid boolean value.

Action: Check the command line and retry.

SQL\*Loader-00244: Column references in the sequence expression for column string are not supported.\\n

Cause: The sequence expression for the specified column contained column references.

Action: Remove the column references and retry.

SQL\*Loader-00245: invalid value for the OPTIMIZE\_PARALLEL parameter\\n

Cause: The command line argument specified for the OPTIMIZE\_PARALLEL parameter was not a valid boolean value.

Action: Check the command line and retry.

SQL\*Loader-00246: The dnfs\_enable parameter must be set for object store loads.\\n\\n

Cause: The dnfs\_enable parameter was not set when a credential was specified for an object store load. The dnfs\_enable parameter allows I/O to the object store.

Action: Set the dnfs\_enable parameter to a value of TRUE when doing object store loads.

SQL\*Loader-00248: multiple string format masks specified at table level for table string\\n

Cause: Multiple format masks were specified for the listed datetime data type at the table level for the listed table.

Action: Remove one of the mask specifications and try the operation again.

SQL\*Loader-00249: Unexpected error occurred while processing datetime format mask (string).\\n

Cause: An unexpected error occurred while processing the datetime format mask.

Action: Check the mask and try the operation again with a correct mask. If the problem still occurs, contact Oracle Support Services.

SQL\*Loader-00250: Work data sets are not used by SQL\*Loader\\n

Cause: The SQL\*Loader control file contains a WRKDDN statement. SQL\*Loader ignores this clause.

Action: No action required. This is an informational message.

SQL\*Loader-00251: Sort devices are not used by SQL\*Loader\\n

Cause: The SQL\*Loader control file contains a SORTDEVT statement. SQL\*Loader ignores this clause.

Action: No action required. This is an informational message.

SQL\*Loader-00252: Sort data sets are not used by SQL\*Loader\\n

Cause: The SQL\*Loader control file contains a SORTNUM statement. SQL\*Loader ignores this clause.

Action: No action required. This is an informational message.

SQL\*Loader-00253: DB2 partition number has no significance -- ignored\\n

Cause: The SQL\*Loader control file contains a PART statement. SQL\*Loader ignores this clause.

Action: No action required. This is an informational message.

SQL\*Loader-00254: Cannot have DISCARDFILE specs here when multiple data files\\n

Cause: The SQL\*Loader control file contained multiple INFILE statements and a DISCARDFILE statement was found below the RESUME clause.

Action: Move the DISCARDFILE statement above the RESUME clause, so it is adjacent to one of the INFILE statements.

SQL\*Loader-00255: Log file for error recovery not used by SQL\*Loader\\n

Cause: The SQL\*Loader control file contains a LOG statement. SQL\*Loader ignores this clause.

Action: No action required. This is an informational message.

SQL\*Loader-00256: SORTED INDEXES option allowed only for non-parallel direct path.\\n

Cause: The SQL\*Loader control file contained a SORTED INDEXES statement, but it was not used in a non-parallel direct path load.

Action: Specify a direct path load with DIRECT=TRUE on the command line, remove the statement from the SQL\*Loader control file, or

SQL\*Loader-00257: TERMINATED BY EOF option not valid with ENCLOSED BY option\\n

Cause: A field description in the SQL\*Loader control file contains both the TERMINATED BY EOF and the ENCLOSED BY options. These options are mutually exclusive.

Action: Remove either or both of the clauses.

SQL\*Loader-00258: Maximum number of SORTED INDEXES (number) exceeded on table string\\n

Cause: There are too many indexes in the SORTED INDEX clause. The message displays the maximum number that are permitted.

Action: Reduce the number of indexes specified in the SORTED INDEX clause or use the conventional path load instead of the direct path load.

SQL\*Loader-00259: Could not escalate DDL share lock to exclusive on table string\\n

Cause: This error occurs when another user has a parse lock on the table, for example, when another user is doing a select on the table. The parse lock should clear momentarily.

Action: Give the parse lock a chance to clear and then retry or else use the conventional path load.

SQL\*Loader-00260: TERMINATED BY EOF option available only with LOBFILE option\\n

Cause: The TERMINATED BY EOF option can be used only when describing data to be loaded from a LOBFILE. It cannot be specified at the table level and it cannot be for data in "regular" data files.

Action: Verify that you have specified the correct option for TERMINATED BY and verify that the TERMINATED BY option is specified for the correct fields.

SQL\*Loader-00261: illegal use of TERMINATED BY for RAW field\\n

Cause: The TERMINATED BY option cannot be used for loading data of type RAW from the data file. The only exception is when loading RAW data from LOBFILES. In that case, you may specify the TERMINATED BY EOF option.

Action: Remove the TERMINATED BY option from the RAW field in the SQL\*Loader control file.

SQL\*Loader-00262: PIECED keyword (on column string) allowed only when path is direct\\n

Cause: The PIECED keyword cannot be used in a conventional path load.

Action: Remove the PIECED keyword or use the direct path load.

SQL\*Loader-00263: PIECED column string must be last specified column in table string\\n

Cause: A column that is not the last column was specified as PIECED.

Action: Remove the PIECED keyword or place the column last.

SQL\*Loader-00264: File mode token string parsed but ignored\\n

Cause: An obsolete file mode token was used in the SQL\*Loader control file. As of Release 1.1 of SQL\*Loader, the file-processing options string is used to control file processing, rather than keywords like STREAM, RECORD, FIXED, and VARIABLE.

Action: No action required. This message is informational. Removing the obsolete keywords will eliminate the message without changing the way in which the datafile is processed.

SQL\*Loader-00265: Unable to get default character set name.\\n

Cause: SQL\*Loader was unable to locate the default character set name for the environment.

Action: Supply a character set name with the CHARACTERSET keyword.

SQL\*Loader-00266: Unable to locate character set handle for string.\\n

Cause: SQL\*Loader could not find the character set handle for the named character set.

Action: Correct the character set name.

SQL\*Loader-00267: Control file must be first data file.\\n

Cause: The SQL\*Loader control file is specified as containing data using the INFILE "\*" clause, but other datafiles were named first.

Action: Move the INFILE "\*" clause so that it is the first datafile declared in the SQL\*Loader control file.

SQL\*Loader-00268: UNRECOVERABLE keyword may be used only in direct path.\\n

Cause: The UNRECOVERABLE keyword can only be specified in the direct path load.

Action: Use the direct path load or remove the keyword. (Conventional path loads are always recoverable).

SQL\*Loader-00269: Null string not allowed as clause comparison text.\\n

Cause: A clause is being compared to a null string.

Action: Modify the clause to compare to at least one character.

SQL\*Loader-00270: TERMINATED BY EOF valid only for CHAR or RAW datatypes\\n

Cause: A field description in the SQL\*Loader control file used the TERMINATED BY EOF option when the field was not a RAW or CHAR datatype.

Action: Modify the SQL\*Loader control file to either remove the TERMINATED BY EOF clause or change the datatype for the field to be CHAR or RAW.

SQL\*Loader-00271: Not a Parallel load. Table level OPTIONS statement ignored.\\n

Cause: A table-level OPTIONS statement was specified for a non-parallel load.

Action: Remove the OPTIONS statement from the SQL\*Loader control file.

SQL\*Loader-00272: Table level OPTIONS statement ignored.\\n

Cause: In the parallel load option, the file specified on the command line overrides the file specified in the SQL\*Loader control file.

Action: Remove the OPTIONS statement from the SQL\*Loader control file.

SQL\*Loader-00273: READBUFFERS may be used only in direct path.\\n

Cause: The READBUFFERS specification was not entered as part of a direct path.

Action: Use the direct path or remove the READBUFFERS specification from the SQL\*Loader control file.

SQL\*Loader-00274: At least 2 read buffers have to be specified.\\n

Cause: Fewer than 2 read buffers have been specified.

Action: Specify at least 2 read buffers in the READBUFFERS statement, in the SQL\*Loader control file.

SQL\*Loader-00275: Data is in control file but "INFILE \*" has not been specified.\\n\\n

Cause: The INFILE specification was not entered in the SQL\*Loader control file.

Action: If data in the SQL\*Loader control file is to be read, specify INFILE \* in the SQL\*Loader control file.

SQL\*Loader-00276: Local storage option overrides global storage.\\n

Cause: A storage clause has been specified in the table level options statement and also in the global options statement.

Action: This is only a warning message. Table level options take precedence over global options. Drop the table level options statement if this is not the intent.

SQL\*Loader-00277: Local file specification overrides global file specification.\\n

Cause: A filename has been specified in the table level options statement and also in the global options statement.

Action: This is only a warning message. Table level options take precedence over global options. Drop the table level options statement if this is not the intent.

SQL\*Loader-00278: Incorrect file specification for parallel load.\\n

Cause: The filename used to perform the parallel load was entered incorrectly.

Action: Correct the filename and re-invoke parallel loader.

SQL\*Loader-00279: Only APPEND mode allowed when parallel load specified.\\n

Cause: INSERT, REPLACE, or TRUNCATE mode was used in a parallel load specification.

Action: Change the SQL\*Loader control file to use the APPEND keyword and re-invoke the parallel loader.

SQL\*Loader-00280: table string is a temporary table\\n

Cause: The sqlldr utility does not load temporary tables. Note that if sqlldr did allow loading of temporary tables, the data would disappear after the load completed.

Action: Load the data into a non-temporary table.

SQL\*Loader-00281: Warning: ROWS parameter ignored in parallel mode.\\n

Cause: Specifying save points using the ROWS parameter is not supported for parallel loads.

Action: Remove the ROWS parameter from the command-line arguments or specify a non-parallel direct load to have save points performed.

SQL\*Loader-00282: Unable to locate character set handle for character set ID (number).\\n

Cause: SQL\*Loader could not find the character set handle for the given character set ID.

Action: The character set ID was obtained from the database server, the SQL\*Loader client does not have knowledge of the given character set ID. Possible mis-match of NLS data on the client and server side.

SQL\*Loader-00283: file processing string "string" ignored for INFILE \*\\n

Cause: The SQL\*Loader control file specified INFILE \* for a load data file along with an optional file processing string. This message is a warning that the file processing string will be ignored since SQLLDR will expect the data to have the same record format as the SQL\*Loader control file.

Action: If the data in the SQL\*Loader control file is in the same format as the rest of the SQL\*Loader control file, then you don't need to do anything. Removing the file processing string will get rid of this error message. If the data in the SQL\*Loader control file has a different record format, then you need to copy the data into a separate file and use that file's name in the INFILE clause.

SQL\*Loader-00284: Warning: Input data file string specified multiple times.\\n

Cause: The same input datafile is loaded multiple times. This can occur if the INFILE keyword is placed out of order in the load syntax statement, which causes the filename of the first datafile loaded to default to the name of the control file with an extension or file type of DAT.

Action: Check that INFILE keyword is not placed after one of these - BADFILE/BADDN/DISCARDFILE/DISCARDDN/DISCARDS.

SQL\*Loader-00285: string may be used only in conventional path.\\n

Cause: HIDDEN can only be specified in the conventional path load.

Action: Use the conventional path load.

SQL\*Loader-00286: ROWS parameter is not supported when loading an IOT.\\n

Cause: Specifying save points using the ROWS parameter is not supported when loading an IOT.

Action: Remove the ROWS parameter from the command-line arguments.

SQL\*Loader-00287: No control file name specified.\\n

Cause: No control file name was provided at the control prompt.

Action: Provide the name of a valid control file at the prompt or on the command line.

SQL\*Loader-00288: Delimiters may not be specified for collections stored in SDF.\\n

Cause: A TERMINATED BY or ENCLOSED BY clause was found along with an SDF (secondary data files) clause for a nested table or varray field.

Action: The TERMINATED BY or ENCLOSED BY clauses may be specified only if the nested table or VARRAY data is stored in the record in the main data file. If you are loading nested table or VARRAY data from a secondary data file, then you must use COUNT to indicate the number of elements in the secondary data file that are stored in the file.

SQL\*Loader-00289: SQL string for column string occludes SQL string for column string.\\n

Cause: A SQL string has been associated with both a column object and one of its attributes in the control file. Because the SQL string of the column object will replace the entire column object in the VALUE clause of the INSERT statement, the SQL string of the attribute is ignored. This could cause unexpected or incorrect values to be loaded.

Action: Correct the control file so that only the column object or its attribute has a SQL string, but not both.

SQL\*Loader-00290: PIECED keyword (on column string) allowed only for lob or long columns\\n

Cause: The PIECED keyword cannot be used for non lob or long columns.

Action: Remove the PIECED keyword or use lob or long column type.

SQL\*Loader-00291: Invalid bind variable string in SQL string for column string.\\n

Cause: A bind variable may not refer to a filler field or to a non-existent field. Also, when running in direct-path mode, a bind variable may not refer to field that represents a LOB stored in a secondary file or a collection.

Action: Remove the offending bind variable from the SQL string.

SQL\*Loader-00292: ROWS parameter ignored when an XML, LOB or VARRAY column is loaded\\n

Cause: Command-line arguments contained a ROWS parameter. Specifying save points using the ROWS parameter is not supported when any table being loaded contains a LOB or a column stored as a LOB. XML and VARRAY columns may be stored as a LOB.

Action: Remove the ROWS parameter from the command-line arguments.

SQL\*Loader-00293: Missing XMLTYPE directive in control file for table string\\n

Cause: A table of sys.xmltype must specify the XMLTYPE directive.

Action: Add XMLTYPE directive to control file.

SQL\*Loader-00294: invalid name % specified in TREAT AS clause\\n

Cause: The type name specified in a TREAT AS clause is invalid. It might contain characters that are not valid in the client character set or a quoted string might not be terminated or the name might be too long to contain a valid schema name and type name.

Action: Verify that the type name has valid characters and is not too long. Also, ensure that all quoted strings are terminated.

SQL\*Loader-00295: Warning: Table string, Column string - Quoting rule of object attribute bind variables has changed.\\n\\n

Cause: The quoting rule of bind variables consisting of full object attribute names changed. The old quoting rule is incorrect because it can lead to ambiguous column references. For backward compatibility, current load will continue unless ambiguous column references are detected.

Action: This is only a warning message. Because the quoting rule of object attribute bind variables has changed, it is recommended that the control file be replaced with the new rule. With the new rule, a full object attribute bind variable name is not enclosed in its entirety in double quotes. Instead, each attribute name in the bind variable should be independently quoted as needed. Note that each attribute name is actually an identifier on its own and thus should follow the quoting rules for an identifier. For example, bind variable ':A.B.C' here consists of 3 attribute names (or identifiers): 'A', 'B', and 'C'.

SQL\*Loader-00296: Bind variable string for column string is ambiguous.\\n

Cause: A bind variable can only refer to one column in the control file. Current load could not continue due to ambiguous column references.

Action: Fix the bind variable. If this bind variable consists of quotes, check that the quotes are used correctly. For example, the old quoting rule of bind variables consisting of full object attribute names was incorrect because it can lead to ambiguous column references. Let's say we have an expression "LTRIM(:"A.B.C")". Using the old quoting rule, this bind variable can refer to object attribute columns '"A"."B"."C"', '"A.B".C', and '"A"."B.C"'. To avoid this confusion, use the new quoting rule for object attribute bind variables, which is to quote each attribute name independently as needed. In the preceding example, if the intended object attribute column is 'A.B.C', then the expression rewritten as "LTRIM(:A.B.C)" or "LTRIM(:"A"."B"."C") will not lead to ambiguities.

SQL\*Loader-00297: Invalid syntax or bind variable in SQL string for column string.\\n

Cause: See following error message for more information. A SQL string cannot have quoted strings improperly terminated. A bind variable in a SQL string cannot have a length of 0, cannot exceed maximum length of 30 characters, and cannot be missing a double quote.

Action: Fix the SQL string. See following error for more information.

SQL\*Loader-00298: Filler field name is too long\\n

Cause: The specified filler field name exceeded the maximum of 30 characters.

Action: Specify at most 30 characters.

SQL\*Loader-00299: Virtual column string in table string.string cannot be loaded.\\n

Cause: Virtual columns were specified in the control file.

Action: Virtual columns cannot be specified in the control file. Remove the virtual column from the SQL\*Loader control file.

SQL\*Loader-00300: error while attempting to enable tracing\\n

Cause: An error occurred while executing an ALTER SESSION statement to enable tracing. This message will be followed by the error returned from ALTER SESSION.

Action: No action required.

SQL\*Loader-00301: string for TERMINATED BY or ENCLOSED BY clause is longer than number bytes\\n

Cause: The size of a string literal is longer than the maximum number of bytes allowed for an ENCLOSED BY or TERMINATED BY string. This error can also occur if the string needs to be converted to the character set of the data file and the resulting string is too long.

Action: Use shorter strings for the TERMINATED BY and ENCLOSED BY clauses.

SQL\*Loader-00303: Non-hex character encountered where hex char expected\\n

Cause: A non-hex character was found in a hexadecimal string.

Action: Change it to the intended hexadecimal character.

SQL\*Loader-00304: Illegal combination of non-alphanumeric characters\\n

Cause: The SQL\*Loader control file contains a combination of non-alphanumeric characters that SQL\*Loader does not recognize. For example, the combination!= is recognized as "not equal", but the combination =! is not valid.

Action: Remove the unrecognized characters from the control file.

SQL\*Loader-00305: More than one end of file character encountered\\n

Cause: The file contains multiple end-of-file marks.

Action: Remove the excess end-of-file characters.

SQL\*Loader-00306: Token longer than max allowable length of number chars\\n

Cause: The SQL\*Loader control file contains a single word or combination of characters (a token) that is longer than the maximum permissible value. The maximum possible value is shown. This error could result from missing spaces, so that multiple tokens are joined.

Action: Check that the proper SQL\*Loader control file is being executed Separate tokens, if joined, or shorten the token.

SQL\*Loader-00307: Warning: conflicting lengths number and number specified for column string table string\\n

Cause: The SQL\*Loader control file specifies two different lengths for the named column. There are three ways to specify the length of a field: --with the POSITION keyword: POSITION(1:3) -- with the length specifier: CHAR(6) -- with the implied length of a datatype; for example, INTEGER -- A conflict could occur between any two of these specifications (or among all three, but only two are shown). A common cause of this error is the specification of some numeric datatype, such as INTEGER, when the numeric external form is intended (INTEGER EXTERNAL). The external form consists of character data, so it is considerably longer than the numeric form, which consists of binary data.

Action: No action is necessarily required, because SQL\*Loader uses only one of the lengths. Check the log file under the heading "Len" in the table-description section to see which length was used. Adjusting the SQL\*Loader control file to produce uniform length specifications will remove the warning.

SQL\*Loader-00308: string SQL string of column string must be in double quotes.\\n

Cause: A SQL string was found that was not quoted or in single quotes.

Action: Use double quotes for the SQL string, rather than single quotes.

SQL\*Loader-00309: No SQL string allowed as part of string field specification\\n

Cause: Particular field types do not allow SQL strings as part of their field specification (e.g. field corresponding to a LOB column). This was violated and needs to be corrected.

Action: Remove the SQL string from the particular field specification.

SQL\*Loader-00310: Interval partition values of table string must be in double quotes.\\n

Cause: A string specified for interval partitioning was found that was not quoted or in single quotes.

Action: Use double quotes for the interval partitioning values string, rather than single quotes.

SQL\*Loader-00311: Cannot load a sharded table when connected to a shard catalog database: string.string\\n

Cause: SQL\*Loader is connected to a database that is acting as the catalog database for a sharded database and the table identified by the message is a sharded table. SQL\*Loader does not support loading sharded tables in a shard catalog database.

Action: Connect to each of the shard database.

SQL\*Loader-00312: Multiple INTO clauses are not supported for this type of parallel load.\\n

Cause: Multiple INTO clauses were specified when using the DEGREE\_OF\_PARALLELISM parameter for a direct or conventional path load.

Action: Load one table at a time for this type of parallel load.

SQL\*Loader-00350: Syntax error at line number.\\n

Cause: num identifies the line in the SQL\*Loader control file at which the error occurred. This message is followed by another of the form -- Expecting str1, found str2 where str1 is a description of what SQL\*Loader expected in the SQL\*Loader control file, and str2 is what was found. Then SQL\*Loader displays the offending line from the SQL\*Loader control file, indicating the location of the error in the line by a carat (^) or an asterisk (\*). An example follows: -- SQL\*Loa er-350: Syntax error at line 28 -- Expecting column name, found keyword CHAR -- col3 ENCLOSED BY '"', CHAR ENCLOSED "'",

Action: Compare the DDL syntax against the syntax diagrams in Oracle7 Server Utilities and make any necessary corrections.

SQL\*Loader-00351: invalid identifier name\\n

Cause: An invalid identifier name was specified.

Action: Make sure a valid identifier name is specified.

SQL\*Loader-00401: End field position number must be greater than or equal to start number\\n

Cause: The named field contains a (start:end) clause in which end is less than start.

Action: Modify the clause so that end is greater than or equal to start.

SQL\*Loader-00402: Unable to determine length of column string from specification\\n

Cause: The specified datatype does not have an implied length (for example, a numeric external or RAW datatype), it is not specified with delimiters, no length was specified, and a length cannot be determined from a POSITION clause.

Action: If a POSITION clause is specified, adding an end location to it produces a length specification. This clause then has the form POSITION(start:end) A length can also specified after the datatype, as in INTEGER EXTERNAL (6) Finally, the field could be specified with delimiters, or the datatype changed to one that has an implied length.

SQL\*Loader-00403: Referenced column string not present in table string.\\n

Cause: The named column is not present in the given table.

Action: Correct the column name or table name.

SQL\*Loader-00404: Column string present more than once in string's INTO TABLE block.\\n

Cause: The named column is specified more than once in a single INTO TABLE statement.

Action: Remove the extraneous column specification.

SQL\*Loader-00405: Need termination delim with optional enclosure delim: column string table string\\n

Cause: The named column was specified with an optional enclosure delimiter, but no termination delimiter. Enclosure delimiters can only be optional when termination delimiters are present.

Action: Specify a termination delimiter or make the enclosure delimiters non-optional.

SQL\*Loader-00406: If data is all generated, number to load cannot be ALL\\n

Cause: When only generated data is loaded, a number to load must be given so SQL\*Loader knows when to stop.

Action: Specify a number to load.

SQL\*Loader-00407: If data is all generated, number to skip is meaningless\\n

Cause: When all data is generated, no file is read, and there are no records to skip.

Action: Remove the number to skip.

SQL\*Loader-00408: Physical record stack overflow\\n

Cause: An internal error has occurred.

Action: Contact customer support.

SQL\*Loader-00409: Number to skip must be table-level, not load-level on continued loads\\n

Cause: The SKIP parameter was specified on the command line or in the OPTIONS statement, but the load was specified as continued with CONTINUE\_LOAD. When a multiple-table direct load is interrupted, it is possible that a different number of records were loaded into each table. As a result, the number of records to skip must be specified for each table when continuing the load. In this case, the load is specified as continued with the CONTINUE\_LOAD statement, and the number of records to skip is given in each INTO TABLE statement. See also messages 410 and 411 for more information.

Action: Check the log file to determine the appropriate number of records to skip for each table and specify this number in the INTO TABLE statement for each table in a continued load or with the command-line SKIP parameter in a standard load.

SQL\*Loader-00410: Number to skip must be load-level, not table-level\\n

Cause: A SKIP clause was found in the INTO TABLE statement of a standard (non-continued) load. In a standard load, specified with LOAD DATA, it is not possible to skip a different number of records for each table. The number of records to skip must be specified for the entire load by using the SKIP parameter on the command line or in the OPTIONS clause. If table-level skip is required, because a different number of records were loaded into each table (only possible for a multiple- table direct load), then specify a continued load with the CONTINUE\_LOAD statement. See also messages 409 and 411 for more information.

Action: If the load was not a multiple-table, direct path load, then move the SKIP clause from the INTO TABLE statements to the command line or to the OPTIONS clause. Otherwise, specify the load as continued with CONTINUE\_LOAD.

SQL\*Loader-00411: Only a direct path load may be continued\\n

Cause: The load is specified with CONTINUE\_LOAD, but DIRECT=FALSE. CONTINUE\_LOAD is only possible for a direct path load and is only necessary for a multiple-table, direct path load when a different number of records have been loaded into each table. See also messages 409 and 410 for more information.

Action: If CONTINUE\_LOAD is necessary, specify a direct load and put the number of records to skip in each INTO TABLE statement. Otherwise, use the command line or OPTIONS clause to specify the number of records to skip and use LOAD DATA instead of CONTINUE\_LOAD.

SQL\*Loader-00412: More columns specified for table string than the maximum (number)\\n

Cause: More columns were specified for the table than the maximum number allowed by the database.

Action: Remove the extraneous columns.

SQL\*Loader-00413: NULLIF or DEFAULTIF clause specified for filler field string in table string.\\n

Cause: A NULLIF or DEFAULTIF clause was specified in the SQL\*Loader control file for the named filler field. These options cannot be specified for filler fields.

Action: Remove the NULLIF or DEFAULTIF clause from the field definition.

SQL\*Loader-00414: no columns to load for table string\\n

Cause: There were no fields in the data file to be loaded for the table. Probably all fields were identified as FILLER fields.

Action: Verify that the FILLER attribute was set correctly for the fields.

SQL\*Loader-00415: column string in table string cannot use and be the object of an SDF or LOBFILE\\n

Cause: The named column is identified as the target of a secondary data file (SDF) or LOBFILE clause. However, the column also gets it's value from an SDF or LOBFILE. If a field name is named in an SDF or LOBFILE clause, then that field cannot have an SDF or LOBFILE clause.

Action: Verify that the SDF and LOBFILE clauses in the SQL\*Loader control file name the correct fields. Also verify that the SDF and LOBFILE clauses are specified for the correct field.

SQL\*Loader-00416: SDF clause for field string in table string references a non existent field.\\n

Cause: The secondary data file clause for the field identified another field that doesn't exist in the table definition for the SQL\*Loader control file.

Action: Verify the definition of the secondary data file to make sure it identifies the intended field.

SQL\*Loader-00417: SQL string (on column string) not allowed in direct path.\\n

Cause: Because the direct path bypasses SQL processing, the SQL string cannot be used.

Action: Remove the SQL string or use the conventional path.

SQL\*Loader-00418: Bad datafile datatype for column string\\n

Cause: The datatype in the data file specified for the column cannot be used to load the column. This message is often displayed for columns that need to be loaded with special features. For example, BFILE columns can only be loaded via the BFILE directive in the control file; same goes for REF fields. in the SQL\*Loader control file. Similarly, REF columns can only be loaded with theREF datatype in the SQL\*Loader control file.

Action: Determine the datatype of the column in the database check the documentation for the correct mechanisms to use to load columns of that type.

SQL\*Loader-00419: input datatype for column string is not supported when loading varrays\\n

Cause: The datatype in the SQL\*Loader control file for the column is cannot be used to load data in a varray.

Action: Use a different datatype.

SQL\*Loader-00420: unsupported datatype conversion requested for column string in table string\\n

Cause: The colummn needs to have it's data converted to another datatype before loading the data. The required conversion cannot be done by sqlldr.

Action: Verify that the correct datatype was specified for the column.

SQL\*Loader-00421: error converting data\\n

Cause: This message can be displayed as one of the reasons for rejecting a row. The sqlldr utility was attempting to convert data for the column from its datatype in the data file to the datatype for the column in the database. This message should be followed with another message describing the conversion error.

Action: Correct the data in the data file so that it can be converted.

SQL\*Loader-00422: constant element count of number for column string is greater than maximum, number\\n

Cause: The number of elements specified for a varray column in a table is greater than the maximum number of elements allowed for the type of the varray column.

Action: Increase the number of elements allowed for the type or remove unwanted elements from the data file.

SQL\*Loader-00423: element count is greater than maximum allowed for the column\\n

Cause: When building a varray from the data file, SQL\*Loader encountered more varray elements than are allowed for the column.

Action: The previous error messages contain the name of the column and the row number containing the bad data.

SQL\*Loader-00424: table string makes illegal reference to collection field string\\n

Cause: A WHEN, OID or SID clause for the table refers to a field declared inside of a collection.

Action: Move the data containing the value for a SID or OID clause outside of the collection definition.

SQL\*Loader-00425: column string makes illegal reference to collection field string\\n

Cause: A clause, such as NULLIF or BFILE clause, for the column refers to a field declared inside of a collection.

Action: Move the data containing the value for a SID or OID clause outside of the collection definition.

SQL\*Loader-00426: count of elements in VARRAY string comes after the data for the varray\\n

Cause: The COUNT clause for a VARRAY field indicates that the count of elements in the varray is stored in another data field. However, that data field comes after the varray data in the data file. Since finding the count field would require SQL\*Loader to know the number of elements in the VARRAY first, SQL\*Loader requires that the count field come before the VARRAY data.

Action: Move the count field to be before the collection data in the data file.

SQL\*Loader-00427: invalid reference to a non-scalar field, expression or a LOB field string\\n

Cause: The field condition referenced a field which is either a nested table, varray, column object, LOB, expression, or BFILE field. Fields with these types cannot be referenced by other fields.

Action: Correct the NULLIF, DEFAULTIF, REF, or WHEN clause to reference only non-LOB scalar data fields.

SQL\*Loader-00428: count for field string not stored in character or integer field\\n

Cause: The count clause for a field references another field, but the referenced field is not a character or integer datatype.

Action: Modify the count field so that it reference a a data field that has the count in an integere or character format.

SQL\*Loader-00429: insufficient number of elements found for varray\\n

Cause: The COUNT directive was specified for a varray, but the number of elements found is less than the number specified by the COUNT directive.

Action: Correct the data so that the count and the number of elements agree.

SQL\*Loader-00430: NULL nested table element is not allowed\\n

Cause: A row in a nested table was set to NULL. Nested tables cannot contain NULL fields.

Action: Correct the data so that there are no NULL rows in the nested table.

SQL\*Loader-00431: illegal NULLIF or DEFAULTIF clause specified for nested table column string\\n

Cause: Rows in a nested table cannot be set to NULL. SQLLDR displays this error when a NULLIF clause was specified for the element that defines the row that make up a nested table. SQLLDR also displays this error if a DEFAULTIF clause is specified for an element that is a named type, since SQLLDR will set a named type to NULL if the DEFAULTIF evaluates to TRUE.

Action: n/a

SQL\*Loader-00432: converted data too large\\n

Cause: This message is preceded by a message identifying a row and column. It is displayed when there is insufficient room to convert the data from the datatype in the input file to the datatype for the column in the database.

Action: Modify the data so that it fits in the database field.

SQL\*Loader-00433: no attributes found for column object string in table string\\n

Cause: No attributes are to be loaded for a column object named in the control file. This can happen if all fields in the definition for the column object in the control are designated as FILLER fields.

Action: Either specify attributes to load for the column object or remove the column object from the control file.

SQL\*Loader-00434: Can not load LOB/XML in a nested table along with the parent table.\\n

Cause: Loading LOBs and XML data within a nested table at the same time as the parent table is not supported.

Action: Load the nested table with the LOB or XML column separately from the parent table.

SQL\*Loader-00435: invalid constant value string for nested table column string\\n

Cause: A constant value was specified for the SETID of a nested table column. An error occurred while translating the character constant into a SETID.

Action: Make sure the constant string contains valid hexadecimal characters and that there are 32 hexadecimal characters.

SQL\*Loader-00436: error converting GUID\\n

Cause: The value of the field named in the message is used to populate the column named in the messsage. Because column is a Set ID or an Object ID, the field needs to be converted. This message indicates that there was a conversion error. If the field is a character field, then the conversion error could be caused by too many or too few haxeadecimal charactersI. Also, one or more of the characters in the field might not be a valid hexadecimal character. If the field contains RAW data, then either too many or to few bytes were specified for the field.

Action: Fix the data and reload the row.

SQL\*Loader-00437: enabled constraint not allowed on LOB column string\\n

Cause: An enabled constraint was present on a LOB column.

Action: Disable the constraint and try again.

SQL\*Loader-00440: Invalid table specified as scope of a REF\\n

Cause: As part of the REF directive one specifies the table name or another fields name which contains the table name of the table which the REF references.

Action: Make sure that the right referenced table name is specified.

SQL\*Loader-00456: end of collection found after number elements when looking for number elements\\n

Cause: A count value was specified for a varray or nested table column and the number of rows found is less than the number of rows specified

Action: Verify that the count field has the correct value and that there is no missing data for the collection.

SQL\*Loader-00457: Comparison text of CONTINUEIF LAST must have length 1 not number\\n

Cause: The comparison text is too long. It can only be one character.

Action: Reduce the comparison text to one character.

SQL\*Loader-00458: Comparison text ('string') of CONTINUEIF LAST must be non-whitespace\\n

Cause: The comparison text is a whitespace character (blank or tab).

Action: Change the comparison text to a non-whitespace character.

SQL\*Loader-00459: error fetching numeric value for sequence on column (string)\\n

Cause: An attempt was made to retrieve a non-numeric value for a sequenced column.

Action: Verify that the data for the sequenced column is numeric. Then retry the operation.

SQL\*Loader-00460: Column (string), form of use (number) does not match char set id of (number)\\n

Cause: The given column with the given form of use does not have the same character set ID as a previous column with the same form of use.

Action: This should not happen. Contact ORACLE support and supply the following information: DDL for the table being loaded, and the SQL\*Loader control file. ADDED in 8.1

SQL\*Loader-00461: direct path loading of datatype for column string not supported\\n

Cause: The datatype for the specified column is one that cannot be loaded with direct path.

Action: If the datatype is supported with conventional path, load the table using conventional path.

SQL\*Loader-00462: error inserting LOB into column string, row %lld, table string\\n

Cause: An error occurred while attempting to write a LOB into a row.

Action: See accompanying messages describing why the LOB could not be loaded, what actions sqlldr took (if any), and where the errors may be in order to reload.

SQL\*Loader-00463: secondary data file for LOB is string\\n

Cause: The secondary data file that was in use for populating the LOB when an error occurred.

Action: n/a

SQL\*Loader-00464: file offset for beginning of lob is string\\n

Cause: The offset into the secondary data file that contains the start of the LOB that was being written when an error occurred.

Action: n/a

SQL\*Loader-00465: string directive expects number arguments, number found.\\n

Cause: You specified a directive such as COUNT() or BFILE() in the SQL\*Loader control file. This directive specifies a fixed number of arguments, but the SQL\*Loader control file contains a different number of arguments.

Action: Correct the SQL\*Loader control file so that the directive contains the correct number of arguments.

SQL\*Loader-00466: Column string does not exist in table string.\\n

Cause: The SQL\*Loader control file specified a table column that does not exist.

Action: n/a

SQL\*Loader-00467: attribute string does not exist in type string for table string.\\n

Cause: The SQL\*Loader control file specified an attribute that does not exist for the specified type. The table that contains the type is also identified in the error message.

Action: Verify that the correct table in the correct schema is named in the SQL\*Loader control file. Also verify that the column name is spelled correctly.

SQL\*Loader-00468: OID directive expects 1 argument, number found.\\n

Cause: More than one argument was specified for an OID clause.

Action: Specify the name of the field containing the value to use for the OID. If the OID for the table is user-defined, then do not use the OID clause in the control file.

SQL\*Loader-00469: SID directive expects 1 argument, number found.\\n

Cause: More than one argument was specified for a SID clause.

Action: Only specify the name of the field containing the value to use for the SID in the SID clause.

SQL\*Loader-00470: table string does not have system generated OID\\n

Cause: You specified an OID clause for a table but the table is either not an object table or the table is an object table but the OIDs for the rows are not system generated.

Action: Verify that the you are loading the correct table. If you are, then you must not specify the OID clause for this table. You should use the OID clause only when the table is an object table, has system generated OIDs and when you want to specify OIDs to be assigned to each row of the table.

SQL\*Loader-00471: OID or SID clause has an argument that is CONSTANT\\n

Cause: You specified a CONSTANT as an argument in an OID clause for an object table or in the SID clause for a nested table column. Since these columns must have unique values, SQL Loader does not allow the a constant to be specified for their values.

Action: Store the OID for each row in a filler field and specify the name of the filler field as an argument.

SQL\*Loader-00472: collections can contain only one non FILLER field specification\\n

Cause: More than one non filler field specification is found in a collection field's member field list.

Action: See correct syntax in the Utilities Manual. If indeed there is more than one attribute that makes up the particular collection, then it must be a collection of a object type which needs to be specified using the COLUMN OBJECT field specification syntax.

SQL\*Loader-00473: nesting of collections is not allowed.\\n

Cause: Nesting of one collection type field description within another is not allowed.

Action: Verify that collection nesting is attempted in the SQL\*Loader control file. Correct the mistake.

SQL\*Loader-00474: no value set for dynamic file for column string in table string row number\\n

Cause: The data for the named column was in a dynamic LOBFILE or secondary data file. This message is returned when the field containing the name of the file with the data for this field has not been set or is NULL. This could be because the record in the data file does not match the format described by the SQL\*Loader control file.

Action: Correct any errors in the data file or the SQL\*Loader control file.

SQL\*Loader-00475: field for dynamic file name is string in table string\\n

Cause: This message is always displayed after message 474.

Action: n/a

SQL\*Loader-00476: count of elements for collection is not set or null, 0 will be used\\n

Cause: This message is displayed following a message that identifies the column and row that contained the problem. The message indicates that the collection field named in the previous message has the count of elements in the collection stored in another field. This message is displayed if the field containing the count does not have a value or is set to NULL. When this happens, SQL\*Loader uses 0 as the number of elements.

Action: If 0 is not the count of elementsfor the collection, correct the data in the data file.

SQL\*Loader-00477: REF directive for field string requires at least two arguments\\n

Cause: The SQL Loader control file contains a REF directive for the field, but only one argument was supplied for the directive. The REF directive always requires at least two arguments.

Action: Supply the missing argument to the REF directive. Remember that you must always supply a table name to the REF directive even if the REF is scoped.

SQL\*Loader-00478: unable to continue due to missing filename for LOBFILE or SDF\\n

Cause: The name for a LOBFILE or secondary data file is either missing or NULL for the current row. SQL\*Loader is unable to continue loading since it can't determine how to get the LOB for the next row.

Action: Correct the data file so that there are valid values for all fields containing the names of LOBFILEs and secondary data files.

SQL\*Loader-00479: REF directive for column string expects number arguments; found number.\\n

Cause: The number of arguments in the REF directive for the column is incorrect.

Action: Specify the correct number of arguments for REF. Remember that the REF directive always requires a table name. Also, primary key REFs require one arguments for each field in the primary key.

SQL\*Loader-00480: EXPRESSION may not be used with elements of a collection.\\n

Cause: The EXPRESSION keyword is followed by a required SQL string expression and is used to load a column with the result of the SQL string expression instead of with a value from the input data file. However, this capability is not allowed with elements of a collection.

Action: Remove the EXPRESSION keyword and associated SQL string from the collection element in the control file.

SQL\*Loader-00481: HIDDEN may not be used with non-scalar fields.\\n

Cause: The HIDDEN keyword is only allowed for scalar fields.

Action: Remove the HIDDEN keyword from the non-scalar field in the control file.

SQL\*Loader-00486: sql-strings may not be specified for collection field string\\n

Cause: A sql-string was specified as part of the description of the field that is inside a nested table or varray. Sql-strings cannot be used to load a field in a varrary or nested tables.

Action: Remove the sql-string from the field description. Modify the data file so that it contains the values to be loaded into the column in the collection.

SQL\*Loader-00487: COUNT clause required for collection string\\n

Cause: A VARRAY or NESTED TABLE was defined in the SQL Loader control file and all of the fields in the VARRAY or NESTED TABLE are generated by SQL Loader and do not come from a data file. SQL Loader requires a COUNT clause be specified so that it knows how many elements to add to the VARRAY or NESTED TABLE for each row.

Action: Add a COUNT clause to the VARRAY or NESTED TABLE definition.

SQL\*Loader-00488: string not a named collection type for filler field string\\n

Cause: The FILLER option was specified for a VARRAY or NESTED TABLE field in the SQL Loader control file. However, the type name specified for the field is not the name of a VARRAY or NESTED TABLE type.

Action: Verify that the correct type name was specified. If the type is defined in a different schema, also verify that the correct schema name is specified.

SQL\*Loader-00489: cannot insert NULL object into object table string, row %llu \\n

Cause: There was no data specified in the control file, a LOB file, or a secondary data file for this object column.

Action: Place valid data for this column in the appropriate file prior to invoking SQL\*Loader to load data into this table.

SQL\*Loader-00490: absolute position is not allowed for inline collections\\n

Cause: The absolute position specification was used for inline collections. Specifying the absolute position for inline collections is not supported.

Action: Use relative positioning for inline collections.

SQL\*Loader-00500: Unable to open file (string)\\n

Cause: SQL\*Loader could not open the named file.

Action: Check the operating system messages below this one in the log file.

SQL\*Loader-00501: Unable to read file (string)\\n

Cause: SQL\*Loader could not read the named file.

Action: Check the operating system messages following this message in the log file.

SQL\*Loader-00502: unable to open data file 'string' for field string table string\\n

Cause: An attempt to open a LOBFILE or secondary data file failed.

Action: Check the operating system messages following this message for information on why the open failed. Verify that the correct name is specified for the LOBFILE or secondary data file.

SQL\*Loader-00503: Error appending extension to file (string)\\n

Cause: SQL\*Loader could not append the default extension to create the filename. The given name could be too long or contain illegal characters.

Action: Check the specified filename.

SQL\*Loader-00504: Error skipping records in file (string)\\n

Cause: SQL\*Loader could not open the file or could not read from it.

Action: Check that the file is where it is expected and that read access has been granted.

SQL\*Loader-00505: error reading LOBFILE\\n

Cause: An attempt to read a secondary data file failed.

Action: Check the operating system message that follows this message for more information.

SQL\*Loader-00506: formatting error reading SDF or LOBFILE string for column string in table string\\n

Cause: The the record format of the named LOBFILE or SDF file is incorrect.

Action: Fix the record formatting problems in the file.

SQL\*Loader-00507: unexpected EOF reading SDF or LOBFILE string for column string in table string\\n

Cause: The end of file was reached for a secondary data file or LOBFILE before the data for the current row was found.

Action: If the file is a LOBFILE, verify the correct datatype was specified for the field. If the file is a secondary data file, make sure the record format is specified correctly in the SQL\*Loader control file.

SQL\*Loader-00508: record formating error in data file string\\n

Cause: The data found in the data file does not correspond to the record format in the SQL\*Loader control file.

Action: Verify that all records in the data file match the format as described in the SQL\*Loader control file.

SQL\*Loader-00509: System error: string\\n

Cause: A platform-specific error was returned during an operation. This message is used to display the text of the error.

Action: n/a

SQL\*Loader-00510: Physical record in data file (string) is longer than the maximum(number)\\n

Cause: The datafile has a physical record that is too long.

Action: Use CONCATENATE or CONTINUEIF. Break up the physical records.

SQL\*Loader-00511: Unable to initialize read functions\\n

Cause: SQL\*Loader could not initialize the read functions.

Action: Check the errors below this message in the log file for more information.

SQL\*Loader-00512: Unable to free read buffer\\n

Cause: An internal error has occurred.

Action: Contact customer support.

SQL\*Loader-00513: Unable to close file (string)\\n

Cause: SQL\*Loader could not close the named file.

Action: Check the errors below this message in the log file for more information.

SQL\*Loader-00514: Error getting elapsed time\\n

Cause: SQL\*Loader could not get the elapsed time from the system.

Action: No action required.

SQL\*Loader-00515: Error getting CPU time\\n

Cause: SQL\*Loader could not get the CPU time from the system.

Action: No action required.

SQL\*Loader-00516: Control file (string) has no contents\\n

Cause: The named file was found to be empty.

Action: Check that the intended file was referenced and that it is not empty.

SQL\*Loader-00517: Error decomposing file name (string)\\n

Cause: SQL\*Loader could not break down the filename into its component parts.

Action: Check the filename for illegal characters.

SQL\*Loader-00518: Error reassembling file name (string)\\n

Cause: SQL\*Loader could not put the filename back together again from its components.

Action: Check the filename for illegal characters.

SQL\*Loader-00520: lfimknam failed for file (string)\\n

Cause: LFI failed to make a name object for the file.

Action: Contact Oracle Worldwide Support.

SQL\*Loader-00521: lfilini failed for file (string)\\n

Cause: LFI failed to create or initialize a file object for the file.

Action: Contact Oracle Worldwide Support.

SQL\*Loader-00522: lfiopn failed for file (string)\\n

Cause: LFI failed to open the file.

Action: Check for any possible operating system errors and/or potential memory problems.

SQL\*Loader-00523: error number writing to file (string)\\n

Cause: Could not write to specified file.

Action: Check the following: the file actually resides in the specified location you have write privileges on the file you have sufficient disk space you have not exceeded your disk quota If all of these conditions are satisfied, then retry the operation.

SQL\*Loader-00524: partial record found at end of datafile (string)\\n

Cause: An incomplete record was found at the end of the indicated datafile.

Action: Make sure the last record in the datafile is complete and has the correct terminating character(s). Also, if fixed-length records are in use, verify that no record exceeds the platform-specific length for a single record.

SQL\*Loader-00525: OCI return status: success\\n

Cause: The message describes the status code returned by an OCI call.

Action: See surrounding messages for more information.

SQL\*Loader-00526: OCI return status: success with info\\n

Cause: The message describes the status code returned by an OCI call.

Action: See surrounding messages for more information.

SQL\*Loader-00527: OCI return status: no data\\n

Cause: The message describes the status code returned by an OCI call.

Action: See surrounding messages for more information.

SQL\*Loader-00528: OCI return status: error\\n

Cause: The message describes the status code returned by an OCI call.

Action: See surrounding messages for more information.

SQL\*Loader-00529: OCI return status: invalid handle\\n

Cause: The message describes the status code returned by an OCI call.

Action: See surrounding messages for more information.

SQL\*Loader-00530: OCI return status: need data\\n

Cause: The message describes the status code returned by an OCI call.

Action: See surrounding messages for more information.

SQL\*Loader-00531: OCI return status: still executing\\n

Cause: The message describes the status code returned by an OCI call.

Action: See surrounding messages for more information.

SQL\*Loader-00532: OCI return status: continue\\n

Cause: The message describes the status code returned by an OCI call.

Action: See surrounding messages for more information.

SQL\*Loader-00533: OCI return status: unknown, value is number\\n

Cause: An unknown status was returned by an OCI call.

Action: See surrounding messages for more information.

SQL\*Loader-00534: Warning: no files found for INFILE wildcard specification (string).\\n

Cause: SQL\*Loader could not find a file which matched the INFILE wildcard specification.

Action: Check to make sure that the files exist in order for them to be loaded.

SQL\*Loader-00535: Warning: no files found for INFILE subdirectory search specification (string).\\n

Cause: SQL\*Loader could not find a file which matched the INFILE subdirectory search specification.

Action: Check to make sure that the files exist in order for them to be loaded.

SQL\*Loader-00536: No files found for any data parameter specification or INFILE specification.\\n

Cause: SQL\*Loader could not find a file which matched any of the data parameter specifications or INFILE specifications.

Action: Check to make sure that the files exist in order for them to be loaded.

SQL\*Loader-00537: Warning: no files found for data parameter wildcard specification (string).\\n

Cause: SQL\*Loader could not find a file which matched the data parameter wildcard specification.

Action: Check to make sure that the files exist in order for them to be loaded.

SQL\*Loader-00538: Warning: no files found for data parameter subdirectory search specification (string).\\n

Cause: SQL\*Loader could not find a file which matched the data parameter subdirectory search specification.

Action: Check to make sure that the files exist in order for them to be loaded.

SQL\*Loader-00539: No files found for any data parameter specification in express mode.\\n

Cause: SQL\*Loader could not find a file which matched any of the data parameter specifications. Since there is no control file for express mode, there are no INFILE specifications.

Action: Check to make sure that the files exist in order for them to be loaded.

SQL\*Loader-00551: internal error: error initializing slf\\n

Cause: An internal error occurred while trying to initialize the file I/O component.

Action: Call customer support.

SQL\*Loader-00552: insufficient privilege to open file\\n

Cause: SQL\*Loader does not have the previleges required to open the file.

Action: Verify that the correct file was specified and that the file has the appropriate permissions.

SQL\*Loader-00553: file not found\\n

Cause: The specified file cannot be found.

Action: verify that the correct name exists and whether the file is in the intended location.

SQL\*Loader-00554: error opening file\\n

Cause: An error occurred while trying to open the file. No further information is available.

Action: Verify that the file is accessible.

SQL\*Loader-00555: unrecognized processing option\\n

Cause: The processing option specified for the file cannot be processed.

Action: Verify that the processing options specified for the file contain legal syntax for the platform where SQL\*Loader is running.

SQL\*Loader-00556: unable to allocate read buffer\\n

Cause: Attempt to allocate the read buffer failed.

Action: If possible, try specifying a smaller size for the read buffer.

SQL\*Loader-00557: unable to allocate memory\\n

Cause: An attempt to allocate some memory to track I/O for the file failed.

Action: Contact customer support.

SQL\*Loader-00558: attempt to use SKIP parameter with linked-in loader\\n

Cause: SKIP parameter was specified with a linked-in file processor.

Action: Do not use the SKIP parameter in this case.

SQL\*Loader-00559: error closing file\\n

Cause: An error occurred while closing the file.

Action: Contact customer support.

SQL\*Loader-00560: error reading file\\n

Cause: An error occurred while reading the file.

Action: Make sure the file is still accessible.

SQL\*Loader-00561: end of file\\n

Cause: End of file reached.

Action: n/a

SQL\*Loader-00562: record too big\\n

Cause: A record in the file is larder than the read buffer.

Action: Verify that the file is not corrupt. If not, try specifying a larger size for the read buffer.

SQL\*Loader-00563: bad length for VAR record\\n

Cause: The length protion of a VAR record contains non-numeric data.

Action: Fix the data in the file.

SQL\*Loader-00564: illegal hexadecimal literal specified for record delimiter\\n

Cause: A hexadecimal literal that contains the record delimiter for the file does not contain a valid hexadecimal string.

Action: Verify that the correct hexadecimal value was specified in the processing options for the file.

SQL\*Loader-00565: unexpected error during skip\\n.

Cause: an unexpected error occurred while attempting to skip records.

Action: This message should be followed by another message giving more specific information about the error

SQL\*Loader-00566: partial record found at end of datafile\\n

Cause: An incomplete record was found at the end of file.

Action: Make sure the last record in the datafile is complete and has the correct terminating character(s).

SQL\*Loader-00567: unable to derive file name\\n

Cause: An error occurred while attempting to build a name for a data file, bad file, discard file or log file.

Action: Instead of relying on SQL Loader to build these file names, try specifying full file specifications for these files in the control file or on the SQL Loader command line.

SQL\*Loader-00568: error writing to file\\n

Cause: Unexpected error occurred while writing to a file. This message is followed by another message with more information about the error.

Action: n/a

SQL\*Loader-00569: READSIZE parameter exceeds maximum value string for platform\\n

Cause: The value specified for the READSIZE parameter on the SQL Loader command line was larger than the maximum size allowed on the platform executing the SQL Loader command

Action: Decrease the size of the READSIZE parameter to be less than the maximum size allowed on the platform.

SQL\*Loader-00570: Warning: single bad file specification with multiple data files using string file may get overwritten.\\n

Cause: The value specified for the BADFILE parameter contained something other than a directory specification (for example, it contained a file name). The INFILE specification had wildcards or the data command line parameter specification contained a comma-separated list or wildcards and the result was more than one data file. In that case, the BADFILE specification or the BAD command line parameter value should be a directory specification only and should not contain a file name.

Action: No action is needed. This is a warning. However, for a parallel load with external tables or express mode, the file may get overwritten or may get corrupted due to contention on the file by multiple parallel query slaves. Try the operation again with a directory only or omit the parameter and use the default bad file name.

SQL\*Loader-00571: Warning: single discard file specification with multiple data files, using string, but file may get overwritten.\\n

Cause: The value specified for the DISCARDFILE parameter contained something other than a directory specification (for example, it contained a file name). The INFILE specification had wildcards or the data command line parameter specification contained a comma-separated list or wildcards and the result was more than one data file. In that case, the DISCARDFILE specification or the DISCARD command line parameter value should be a directory specification only and should not contain a file name.

Action: No action is needed. This is a warning. However, for a parallel load with external tables or express mode, the file may get overwritten or may get corrupted due to contention on the file by multiple parallel query slaves. Try the operation again with a directory only or omit the parameter and use the default discard file name.

SQL\*Loader-00572: Warning: cannot add "\_\\%p" to string for file string. Using file name as is.\\n

Cause: SQL\*Loader could not add "\_%p" to the file name. The name specified or the derived name may be too long.

Action: No action is needed. This is a warning. However, for a parallel load with external tables or express mode, the file may be overwritten or may get corrupted due to contention on the file by multiple parallel query slaves. Try the operation again with a shorter file name.

SQL\*Loader-00573: Error opening the directory (string), failed with return code \[number\].\\n

Cause: An error occurred while trying to open the directory (see accompanying error code).

Action: Verify that the directory is accessible.

SQL\*Loader-00574: \\nCheck the log file:\\n string\\nfor more information about the load.\\n

Cause: Informational only.

Action: No action is needed.

SQL\*Loader-00575: \\nCheck the log files:\\n string\\n string\\nfor more information about the load.\\n

Cause: Informational only.

Action: No action is needed.

SQL\*Loader-00576: Error getting count of entries for directory (string), failed with return code \[number\].\\n

Cause: An error occurred while trying to get the count of directory entries (see accompanying error code).

Action: Verify that the directory is accessible.

SQL\*Loader-00577: Error reading the directory (string), failed with return code \[number\].\\n

Cause: An error occurred while trying to read the directory (see accompanying error code).

Action: Verify that the directory is accessible.

SQL\*Loader-00578: Error finishing wild card search in directory (string), failed with return code \[number\].\\n

Cause: An error occurred while trying to finish a search for files in a directory that match a wild card specification (see accompanying error code).

Action: This is an informational message. No action is needed.

SQL\*Loader-00579: switching to direct path for the load\\n

Cause: SQL\*Loader could not use the external tables load method for the express mode load. Therefore SQL\*Loader tried to use direct path for the load instead of external tables. See any previous messages for more information.

Action: No action is needed. This is an informational message.

SQL\*Loader-00582: Warning: cannot remove "\_\\%p" from string for file string. Using file name as is.\\n

Cause: SQL\*Loader could not remove "\_%p" from the file name.

Action: No action is needed. This is a warning. The file name was used as is.

SQL\*Loader-00583: ignoring trim setting with string, using value of LDRTRIM\\n

Cause: SQL\*Loader was doing a direct path or conventional path load. SQL\*Loader only supports LDRTRIM for direct path and conventional path. Therefore, LDRTRIM trimming was used for the load. You can get the equivalent of NOTRIM trimming if you use a control file and use the PRESERVE BLANKS clause.

Action: No action is needed. This is an informational message.

SQL\*Loader-00584: ignoring DEGREE\_OF\_PARALLELISM setting with string, using value of NONE\\n

Cause: DEGREE\_OF\_PARALLELISM was not supported by SQL\*Loader for direct path and conventional path loads. Therefore, the DEGREE\_OF\_PARALLELISM setting was ignored for the load and treated as a value of NONE.

Action: No action is needed. This is an informational message.

SQL\*Loader-00585: defaulting DEGREE\_OF\_PARALLELISM to NONE since load=number was specified\\n

Cause: DEGREE\_OF\_PARALLELISM was defaulted to NONE by SQL\*Loader because load=n was specified. This assures consistency in the records which get loaded with load=n.

Action: No action is needed. This is an informational message.

SQL\*Loader-00586: OID directive not allowed for table string\\n

Cause: The OID directive was specified but the table is not a type table. The OID directive can be specified only for type tables.

Action: Verify that the name of the table is correct. If so, then remove the OID directive.

SQL\*Loader-00587: SID directive not allowed for table string\\n

Cause: The SID directive was specified but the table is not a nested table. The SID directive can be specified only for nested tables.

Action: Verify that the name of the table is correct. If so, then remove the SID directive.

SQL\*Loader-00588: XMLTYPE directive not allowed for table string\\n

Cause: The XMLTYPE directive was specified but the table is not an XML type table. The XMLTYPE directive can be specified only for XMLTYPE tables.

Action: Verify that the name of the table is correct. If so, then remove the XMLTYPE directive.

SQL\*Loader-00600: Bind size of number bytes increased to number bytes to hold 1 row.\\n

Cause: The space needed to contain a single row is longer than the specified bind size. The value used for the bind size will be increased to handle the larger size

Action: No action is required. This message will go away if the new value in the error message is specified for the bind size.

SQL\*Loader-00601: For INSERT option, table must be empty. Error on table string\\n

Cause: A non-empty table is being loaded with the INSERT option.

Action: Use the REPLACE keyword to empty the old table and store the new data in its place. Use the APPEND keyword to leave the table's contents intact and add the new data to it.

SQL\*Loader-00602: Maximum converted length number of column string is too big for bind array\\n

Cause: The named column cannot undergo the specified character set conversion and still be placed in a contiguous piece of memory on the system.

Action: Specify a shorter data column or eliminate the conversion.

SQL\*Loader-00603: Maximum length number of column string is too big for bind array\\n

Cause: The named column cannot be put in a contiguous piece of memory on the system.

Action: Specify a shorter data column.

SQL\*Loader-00604: Error occurred on an attempt to commit\\n

Cause: An error occurred while trying to commit changes to the database.

Action: Look at the message listed below this one in the log file for more information.

SQL\*Loader-00605: Non-data dependent ORACLE error occurred -- load discontinued.\\n\\n

Cause: An error occurred that is independent of the data. For example, an out-of-space condition. Because all further rows will be rejected, the load is discontinued. (If the error were data dependent, then other rows might succeed.)

Action: See the errors below this one in the log file for more information.

SQL\*Loader-00606: Object string in INTO TABLE clause is not a local table\\n

Cause: The synonym specified in the INTO TABLE clause in the SQL\*Loader control file specifies a remote object via a database link. Only a synonym for an existing local table can be specified in the INTO TABLE clause.

Action: Ensure that a local table name or a synonym for a local table is fully specified in the INTO TABLE clause. The table must already exist.

SQL\*Loader-00607: partition not empty for INSERT option; table string, partition string\\n

Cause: An attempt was made to use the INSERT option on a non-empty partition.

Action: Empty the partition, or use the REPLACE or TRUNCATE option.

SQL\*Loader-00608: subpartition not empty for INSERT option; table string, subpartition string\\n

Cause: An attempt was made to use the INSERT option on a non-empty subpartition.

Action: Empty the subpartition, or use the REPLACE or TRUNCATE option.

SQL\*Loader-00609: value used for ROWS parameter changed from number to number\\n

Cause: SQL Loader adjusted the value it was using for the ROWS parameter to the new value reported. This is an informational message and not an error. SQL Loader will adjust the value of the ROWS parameter if the amount of memory specified by BINDSIZE is not large enough to hold data for the number of rows specified. SQL Loader will also change the value of the ROWS parameter for conventional path loads if the value is larger than 65534. Conventional path load can load at most 65534 rows at a time.

Action: If the limit of 65534 rows for conventional path load is not being reached, then try increasing the value of BINDSIZE.

SQL\*Loader-00610: cannot load system partitioned table string; partition name(s) required\\n

Cause: An attempt was made to load a system partitioned table with no partitioning clause specified in the SQL\*Loader control file.

Action: Specify the partition name(s) in the SQL\*Loader control file.

SQL\*Loader-00620: Initial enclosure character not found\\n

Cause: A mandatory initial enclosure delimiter was not present. Either it is missing on the current field or the previous field is missing an identical closing delimiter.

Action: Supply the missing delimiters.

SQL\*Loader-00621: Field in data file exceeds maximum length\\n

Cause: A field exceeded its maximum allowable length. The maximum length is either the length specified in the SQL\*Loader control file, or, for delimitable fields without a length specified, the default maximum length (255 bytes).

Action: Check for missing delimiters and/or shorten the field.

SQL\*Loader-00622: Column not found before end of logical record (use TRAILING NULLCOLS)\\n

Cause: The logical record ended before all specified fields were found.

Action: If the missing fields should be loaded as null, use the TRAILING NULLCOLS clause. Otherwise, correct the data.

SQL\*Loader-00623: second enclosure string not present\\n

Cause: The logical end of record or the end of a LOBFILE was reached before a second enclosure delimiter was found.

Action: Correct the data file to include the missing delimiter.

SQL\*Loader-00624: no terminator found after TERMINATED and ENCLOSED field\\n

Cause: No termination delimiter was found after the enclosed field ended.

Action: Supply the missing termination delimiter.

SQL\*Loader-00625: Multibyte character error in control file.\\n

Cause: Incomplete multi-byte character strings were found in the SQL\*Loader control file.

Action: Edit the SQL\*Loader control file to check that all multi-byte character data is valid.

SQL\*Loader-00626: Character set conversion buffer overflow.\\n

Cause: A conversion from the datafile character set to the client character set required more space than that allocated for the conversion buffer. The size of the conversion buffer is limited by the maximum size of a varchar2 column.

Action: The input record is rejected. The data will not fit into the column.

SQL\*Loader-00627: Character set conversion graph not available.\\n

Cause: A conversion from the datafile character set to the client character failed due to the conversion graph not being available.

Action: Contact Oracle support. Check NLSRTL installation.

SQL\*Loader-00628: Character set conversion error.\\n

Cause: A character set conversion error occurred.

Action: Contact Oracle support. Check NLSRTL installation. Provide a reproduceable test case.

SQL\*Loader-00640: Variable length field was truncated.\\n

Cause: The end of the logical record was encountered before the end of a variable length field. The length of each variable-length field is embedded in the field, so SQL\*Loader knows that more data should have been present.

Action: Check the data for inadvertent truncation and verify the SQL\*Loader control file specifications against the log file; the field may be starting in the wrong place.

SQL\*Loader-00641: Invalid packed decimal nibble.\\n

Cause: Each byte in a packed decimal field contains two 4-bit nibbles. Each nibble must have a valid value.

Action: Check the SQL\*Loader control file's specifications against the log file to ensure that the field location was specified correctly. Check the contents of the field.

SQL\*Loader-00642: Relative start position > absolute field end position.\\n

Cause: A field specified as POSITION(\*+n:y) had its relative start occur after the absolute position y.

Action: Check that a delimiter is not missing and that the values of n and y are correct.

SQL\*Loader-00643: error executing INSERT statement for table string\\n

Cause: A fatal error occurred while attempting to insert data into the table.

Action: Refer to the messages that follow for more information. If you specified SQL stings for any of your columns, verify that strings are correct. Specifcally, check for balanced parenthesis and correct use of quotation marks. Another format error

SQL\*Loader-00644: end of logical record found when reading length of varying length field\\n

Cause: While attempting to read the length portion of a varying length field, then end of the logical record was reached.

Action: Verify that the SQL\*Loader control file describes the data correctly and that the data in the data file matches the description in the SQL\*Loader control file

SQL\*Loader-00645: error converting character length field to a number\\n

Cause: An error occurred while attempting to convert the characters containing the count portion of a VARCHARC or VARRAWC field.

Action: Verify that the count portion for the column has the correct value.

SQL\*Loader-00646: lob set to EMPTY in column string, row %lld, table string\\n

Cause: Encountered errors (for example, parsing errors in LOBFILE) while loading LOBs. The row will remain in the table and its LOB column will be initialized to empty. Loading of other records will continue.

Action: Correct the data file (see accompanying messages) and reload.

SQL\*Loader-00647: Integer to number conversion error\\n

Cause: An error occurred while attempting to convert an integer to an Oracle number format.

Action: Verify that the integer field in the data file is a valid integer. If the INTEGER(N) syntax was used, then verify that the length specified is valid.

SQL\*Loader-00649: Quoted string missing closing quote\\n

Cause: A quoted string in the control file is missing a closing quote.

Action: Insert the closing quote as appropriate.

SQL\*Loader-00650: incomplete lob data written for column string, row %lld, table string\\n

Cause: Encountered errors (for example, parsing errors in LOBFILE) while loading LOBs using direct path. The row will remain in the table and its LOB column may not be complete. Loading of other records will continue.

Action: Correct the data file (see accompanying messages) and reload.

SQL\*Loader-00651: error skipping lob for column string, row %lld, table string\\n

Cause: Encountered errors (for example, parsing errors in LOBFILE) while skipping LOBs.

Action: Correct the data file (see accompanying messages) and reload.

SQL\*Loader-00652: Invalid zoned decimal byte.\\n

Cause: Each byte of a zoned decimal field must have a valid value based on the character set encoding used. ASCII-based zoned decimals must follow the formats specified in the VAX Architecture Reference Manual. EBCDIC-based zoned decimals must follow the formats specified in the ESA/390 Principles of Operations, version 8.1.

Action: Check the SQL\*Loader control file's specifications against the log file to ensure that the field location was specified correctly. Check the contents of the field.

SQL\*Loader-00653: XML data set to NULL in column string, row %lld, table string\\n

Cause: Encountered errors (for example, parsing errors in LOBFILE) while loading LOBs into an XML column. The row will remain in the table and its XML column will be initialized to null. Loading of other records will continue.

Action: Correct the data file (see accompanying messages) and reload.

SQL\*Loader-00654: Variable length field exceeds maximum length.\\n

Cause: A variable length field (with a leading length subfield) exceeded its maximum allowable length. The maximum length is either the length specified in the SQL\*Loader control file, or, the default if not specified (4kb).

Action: Shorten the field and its length.

SQL\*Loader-00655: cannot load object-relational XML attribute using direct path \\n

Cause: The table being loaded contains a column object which contains an XML attribute with a storage type of object-relational. This type of attribute cannot be loaded with direct path.

Action: Perform the load with conventional path mode.

SQL\*Loader-00656: position specification for column string is not allowed in external table loads\\n

Cause: Use of a position specification was present in an external table load.

Action: Either remove the position specification, change the position specification to a field name reference, use direct path, or use conventional path.

SQL\*Loader-00657: table string loaded using number passes, partition memory limit was numberkb, any data saves possibly ignored\\n

Cause: Due to memory use, multiple passes were used to load some partitions.

Action: To decrease the number of passes, consider increasing the partition memory limit using the PARTITION\_MEMORY command line option, or by increasing PGA\_AGGREGATE\_TARGET. Note that increasing the limit too much can cause the load to run out of memory.

SQL\*Loader-00658: parallel append loads must specify APPEND\_PARALLEL\\n

Cause: The table being loaded in parallel append mode did not use APPEND\_PARALLEL. Automatic parallel loads cannot use skip=n to continue loads because the order of record loading differs from run to run. Consider this when loading a table in parallel, especially when loading into a nonempty table.

Action: Replace APPEND with APPEND\_PARALLEL in the control file.

SQL\*Loader-00700: Out of memory while performing essential allocations \[number\]\\n

Cause: SQL\*Loader could not allocate the memory it needs.

Action: Check the operating system and process memory. Increase memory available to SQL\*Loader, if possible. If using direct path, try lowering the columnarrayrows option (see log file for current default value).

SQL\*Loader-00702: Internal error - string\\n

Cause: An internal error has occurred.

Action: Make a note of the message and contact customer support.

SQL\*Loader-00703: Internal error: argument number\\n

Cause: An internal error has occurred.

Action: Make a note of the message and the number, then contact customer support.

SQL\*Loader-00704: Internal error: string \[number\]\\n

Cause: An internal error has occurred.

Action: Make a note of the message and the number, then contact customer support.

SQL\*Loader-00705: Internal error\\n

Cause: An internal error has occurred.

Action: Contact customer support.

SQL\*Loader-00706: Bad argument to ulerr \[number\].\\n

Cause: An internal error has occurred.

Action: Contact customer support.

SQL\*Loader-00708: Internal error: unknown status number returned from sllf layer\\n

Cause: An unknown status was returned by a call to the sllf layer.

Action: Contact customer support.

SQL\*Loader-00709: Internal error calling SLTS layer: string failed\\n

Cause: A nonsuccess status was returned by a call to the SLTS layer.

Action: Contact customer support.

SQL\*Loader-00710: Internal error: direct path stream buffer not loaded\\n

Cause: A direct path stream buffer was built but not loaded.

Action: Contact customer support.

SQL\*Loader-00711: Internal error: bad address for little endian UTF16 conversion\\n

Cause: Address for little endian UTF16 data not in a valid buffer.

Action: Contact customer support.

SQL\*Loader-00712: Internal error: bad address for big endian UTF16 conversion\\n

Cause: Address for big endian UTF16 data not in a valid buffer.

Action: Contact customer support.

SQL\*Loader-00713: Internal error calling SLTS layer: string failed with return code \[number\].\\n

Cause: A nonsuccess status was returned by a call to the SLTS layer.

Action: Contact customer support.

SQL\*Loader-00714: Internal error - string file: string line: number\\n

Cause: An internal error occurred.

Action: Make a note of the message and contact Oracle Support Services.

SQL\*Loader-00800: string specified and ignored\\n

Cause: An option was specified that is not supported by External Table load.

Action: Do not specify the unsupported option or do not use External Table load.

SQL\*Loader-00801: all INTO TABLE clauses must have the same options (string)\\n

Cause: At least two INTO TABLE clauses have different options set.

Action: Set the options to be the same or do the loads separately.

SQL\*Loader-00802: numeric EXTERNAL with DEFAULTIF clause not supported by External Table\\n

Cause: A numeric EXTERNAL type was specified with a DEFAULTIF clause which is not supported by external table load.

Action: Remove the clause if possible or do not use external table load.

SQL\*Loader-00803: Field type string not supported by External Table\\n

Cause: The specified field type is not supported by external table.

Action: Remove the specified field type or do not use external table load.

SQL\*Loader-00804: SEQUENCES with intervals are not supported by External Table Load.\\n

Cause: A sequence with an interval was specified which is not supported by external table load.

Action: Remove the interval from the sequence, or remove the sequence itself, or do not use external table load.

SQL\*Loader-00805: Option string not supported by string\\n

Cause: The specified option is not supported by external table or express mode load.

Action: Remove the specified option or do not use external table load or express mode load.

SQL\*Loader-00806: unknown record format specified for data file\\n

Cause: The osd string containing file processing options in the control file specified an unknown file processing option.

Action: Verify the correct options are specified for the platform being used.

SQL\*Loader-00807: error loading table\\n

Cause: An INSERT statement used to load a table from an external table or a temporary internal table failed. The statement that failed is shown immediately preceding this mesage.

Action: See subsequent messages for more information about the error.

SQL\*Loader-00808: error creating sequence: string\\n

Cause: An attempt to create a sequence needed for the load failed.

Action: See messages that follow this one for information about the failure.

SQL\*Loader-00809: error dropping sequence: string\\n

Cause: A sequence needed to be dropped either because SQL Loader found a sequence with the same name it is trying to create or because SQL Loader is cleaning up from sequences it created at the beginning of the load.

Action: See messages that follow this one for information about why the attampt to drop the sequence failed.

SQL\*Loader-00810: error creating external table: string\\n

Cause: An attempt to create the external table sued for the load failed.

Action: See messages that follow for more information about the failure.

SQL\*Loader-00811: error dropping external table: string\\n

Cause: An error occurred when trying to drop an external table. Note that the table may have been left from a previous load.

Action: n/a

SQL\*Loader-00812: error creating internal table: string\\n

Cause: An error was encountered trying to create a temporary internal table. The internal table is used only when loading multiple tables from the same data file. The internal table is loaded once and the target tables are loaded from the internal table.

Action: n/a

SQL\*Loader-00813: error dropping internal table: string\\n

Cause: An error was encountered trying to drop a temporary internal table. The internal table is used only when loading multiple tables from the same data file. The internal table is loaded once and the target tables are loaded from the internal table. The internal table may have been left from a previous build.

Action: n/a

SQL\*Loader-00816: error creating temporary directory object string for file string\\n

Cause: No existing directory object was found in the database for the directory containing the file. Since all files loaded by external tables must be in a directory named by a directory object, SQL Loader tried to create a directory object for the file.

Action: See error messages that follow this message for more information.

SQL\*Loader-00817: error dropping directory object string\\n

Cause: SQL Loader created a directory object as part of an external table load. An attempt to cleanup the directory object failed.

Action: See messages following this one for more information about the error.

SQL\*Loader-00820: cannot create WHERE clause with POSITION syntax for table string\\n

Cause: The EXTERNAL\_TABLE parameter was specified for a multi-table load, and a WHEN clause for one of the tables contained a reference to a range of bytes in the record using POSITION syntax. SQL\*Loader uses the WHEN clause from the control file to generate the WHERE clause in the INSERT statement. If the WHERE clause contains a reference to a range of bytes in the table, then a valid WHERE clause cannot be generated. Note that SQL\*Loader will proceed as if GENERATE\_ONLY was specified for the EXTERNAL\_TABLE parameter.

Action: Modify the control file to only use field name references in the WHEN clause. Note that this may require creating a filler field. Another alternative is to create one control file for each table to be loaded and load the tables separately. In that case, SQL\*Loader can use the access parameter list LOAD WHEN syntax to specify the range of bytes using POSITION syntax for a single table.

SQL\*Loader-00821: switching to GENERATE\_ONLY\\n

Cause: SQL Loader is not able to execute the SQL statements it generated for loading the data using external tables. See previous messages for more information.

Action: n/a

SQL\*Loader-00822: operation not supported on external organized table\\n

Cause: User attempted on operation on an external table which is not supported.

Action: Don't do that!

SQL\*Loader-00823: TREAT AS clause for object tables not supported for external tables\\n

Cause: A TREAT AS clause was specified in the INTO TABLE clause for an object table in the SQL\*Loader control file and the EXTERNAL\_TABLES command line parameter was set to either EXECUTE or GENERATE\_ONLY. External tables can be used to load the data, but SQL\*Loader does not generate the correct SQL statements to do this.

Action: Use SQL\*Loader direct path or SQL\*Loader conventional path to load the table.

SQL\*Loader-00824: column type string not supported by string\\n

Cause: The column type was not supported by external table or express mode using the external table load method.

Action: Do not use external table or express mode using the external table load method. Try the load using conventional path or direct path as the load method.

SQL\*Loader-00825: The database server does not support the load of Primary Key Reference column string by SQL\*Loader.\\n

Cause: An attempt was made to load a primary key reference column.

Action: Do not use primary key reference columns.

SQL\*Loader-00826: ROWS parameter is not supported for parallel direct path loading using degree\_of\_parallelism parameter.\\n

Cause: An attempt was made to specify save points with the ROWS parameter when using degree\_of\_parallelism for a direct path parallel load.

Action: Remove the ROWS parameter from the command line arguments or do not specify the degree\_of\_parallelism parameter.

SQL\*Loader-00827: unable to connect to Global Service Manager(GSM) due to missing or invalid GSM parameters.\\n

Cause: An attempt was made to connect to the Global Service Manager sharding library.

Action: Check the values specified for 'gsm\_name', 'gsm\_host' and 'gsm\_port'. All three values must be specified and valid.

SQL\*Loader-00828: The commit\_discontinued parameter is not supported for parallel loading using degree\_of\_parallelism parameter.\\n

Cause: An attempt was made to specify partial saves with the commit\_discontinued parameter when using degree\_of\_parallelism for a parallel load.

Action: Remove the commit\_discontinued parameter from the command line arguments or do not specify the degree\_of\_parallelism parameter.

SQL\*Loader-00901: Error logging on to ORACLE:\\n

Cause: An attempt was made to log on to Oracle in direct path load mode.

Action: Ensure that the instance is up and running. Check the Oracle messages below this one in the log file for more information.

SQL\*Loader-00902: Error opening cursor: \[number\] \\n

Cause: An internal error has occurred.

Action: Check the Oracle messages below this one in the log file and contact customer support.

SQL\*Loader-00903: Database must be at least version number.number.number.number.number for direct path\\n

Cause: The direct path load mode is being used with an incompatible database.

Action: Upgrade the database to the specified version or else use the conventional path load.

SQL\*Loader-00904: You cannot used the direct path when linked with v5 of the database\\n

Cause: The direct path mode is being used after SQL\*Loader has been linked with a Version 5 database.

Action: Use the conventional path.

SQL\*Loader-00905: Error parsing SQL statement for upi: \[number\] \\n

Cause: Header message.

Action: Check the message below this one in the log file for more information.

SQL\*Loader-00906: Error executing SQL statement for upi: \[number\] \\n

Cause: An internal error has occurred.

Action: Check the message below this one in the log file for more information.

SQL\*Loader-00909: Loader views must be loaded (as SYS) for direct path to be used\\n

Cause: Database views required for the direct path mode are not present.

Action: The Oracle7 Server Administrator's Guide details how to run the required scripts as user SYS for loading the required views.

SQL\*Loader-00910: Error binding input variables for upi: \[number\] \\n

Cause: Header message.

Action: Check the message below this one in the log file for more information.

SQL\*Loader-00911: Error defining output variable(s) for upi: \[number\] \\n

Cause: Header message.

Action: Check the message below this one in the log file for more information.

SQL\*Loader-00913: Error fetching results of select statement (upi): \[number\] \\n

Cause: Header message.

Action: Check the message below this one in the log file for more information.

SQL\*Loader-00914: Error locking table string in exclusive mode.\\n

Cause: The direct path mode could not lock the named table.

Action: Check the message below this one in the log file for more information. Check that the necessary privileges have been granted.

SQL\*Loader-00915: Error closing cursor: \[number\] \\n

Cause: Header message.

Action: CCheck the message below this one in the log file for more information.

SQL\*Loader-00916: Error checking path homogeneity\\n

Cause: To do a direct path load load when the front end and back end of the database are on separate hardware systems, the systems must be identical, using the same machine, operating system, and character set. This error occurs when SQL\*Loader detects a difference between the systems that will prevent a direct load from operating properly.

Action: Use a conventional path load for this configuration.

SQL\*Loader-00918: The catalog must be loaded (as SYS) for SQL\*Loader to be used\\n

Cause: The catalog is not loaded.

Action: Logon as user SYS and load the Oracle7 catalog and the views in the script ULVIEW.SQL.

SQL\*Loader-00919: Error during upi fetch: \[number\] \\n

Cause: An internal error has occurred.

Action: Check the message below this one in the log file for more information.

SQL\*Loader-00925: Error while string\\n

Cause: An internal error has occurred.

Action: Check the message below this one in the log file for more information. The table or column referenced may not be accessible.

SQL\*Loader-00926: OCI error while string for table string\\n

Cause: An OCI error has occurred.

Action: Check the message below this one in the log file for more information. The table or column referenced may not be accessible.

SQL\*Loader-00929: Error parsing insert statement for table string.\\n

Cause: The table's insert statement caused a parse error.

Action: Check all SQL strings that were used.

SQL\*Loader-00930: Error parsing insert statement for table string column string.\\n

Cause: The named column's INSERT statement caused a parse error.

Action: Check the message below this one in the log file for more information. Check the SQL string used for this column.

SQL\*Loader-00931: OCI error while binding variable for column string in table string\\n

Cause: An OCI error has occurred.

Action: Check the errors below it for more information. The SQL string for this column may be in error.

SQL\*Loader-00932: Could not truncate table string.\\n

Cause: Truncation of the table was attempted and failed.

Action: Check the following errors for more information. Truncation due to referential constraints should not occur.

SQL\*Loader-00933: Specified file string not part of database\\n

Cause: The specified filename to load the table is not a database file.

Action: Specify a valid datafile.

SQL\*Loader-00934: Incorrect data file string specified for table string\\n

Cause: A datafile name was given to load the table that is not a part of the tablespace in which the table resides.

Action: Specify a valid datafile.

SQL\*Loader-00935: Error verifying required option for parallel load.\\n

Cause: An error was encountered because a required option was not found or was invalid.

Action: Correct the problem as described in the accompanying Oracle message.

SQL\*Loader-00937: parallel load requested and string has enabled triggers or constraints\\n

Cause: A request was made for a parallel direct load, but the object to be loaded has an enabled constraint (check, referential) and/or enabled triggers.

Action: Disable the offending enabled constraints and/or triggers and retry the parallel direct load.

SQL\*Loader-00938: partition load requested and string has enabled triggers or constraints\\n

Cause: A request was made for a direct load of a single partition, but the object to be loaded has an enabled constraint (check, referential) and/or enabled triggers.

Action: Disable the offending enabled constraints and/or triggers and retry the parallel direct load.

SQL\*Loader-00939: OCI error while string for table string partition string\\n

Cause: Header message.

Action: Check the following errors for more information. The table or partition referenced may not be accessible.

SQL\*Loader-00940: UPI error while setting NCHAR bind attributes for column string table string\\n

Cause: An error occurred while setting the charsetform attribute of an NCHAR column.

Action: This is an internal error. Report to ORACLE support.

SQL\*Loader-00941: Error during describe of table string\\n

Cause: Error while executing a describe of a select list on the given table. Check the error immediately preceding this error.

Action: n/a

SQL\*Loader-00942: partition string not part of table string\\n

Cause: the specified partition is not part of the specified table

Action: n/a

SQL\*Loader-00943: incorrect datafile string specified for table string partition string\\n

Cause: The specified datafile is not in the tablespace of the specified partition. Due to use of FILE= keyword on a partitioned table. When loading all partitions of a partitioned table, the partitions must be in the same tablespace. When loading a single partition, the tablespace of the partition being loaded must be the same as the tablespace in which the specified datafile file resides.

Action: n/a

SQL\*Loader-00944: error preparing insert statement for table string.\\n

Cause: A call to OCIStmtPrepare for the table's insert statement returned an error.

Action: Refer to the message that follows for information about the error returned by OCIStmtPrepare. Make sure the syntax is correct for all SQL strings specified in the SQL\*Loader control file.

SQL\*Loader-00945: record size number too large for direct path \\n

Cause: The maximum size of records in the data file is larger than the maximum size supported by direct path, which is 65535

Action: Load the data file using conventional path.

SQL\*Loader-00946: OCI error while string for table string subpartition string\\n

Cause: Header message.

Action: Check the following errors for more information. The table or subpartition referenced may not be accessible.

SQL\*Loader-00947: subpartition load requested and string has enabled triggers or constraints\\n

Cause: A request was made for a direct load of a single subpartition, but the object to be loaded has an enabled constraint (check, referential) and/or enabled triggers.

Action: Disable the offending enabled constraints and/or triggers and retry the parallel direct load.

SQL\*Loader-00948: subpartition string not part of table string\\n

Cause: the specified subpartition is not part of the specified table

Action: n/a

SQL\*Loader-00949: incorrect datafile string specified for table string subpartition string\\n

Cause: The specified datafile is not in the tablespace of the specified subpartition. Due to use of FILE= keyword on a subpartitioned table. When loading all subpartitions of a subpartitioned table, the subpartitions must be in the same tablespace. When loading a single subpartition, the tablespace of the subpartition being loaded must be the same as the tablespace in which the specified datafile file resides.

Action: n/a

SQL\*Loader-00950: Error shipping data structures across 2-task\\n

Cause: Header message.

Action: Check the error(s) below it for more information.

SQL\*Loader-00951: Error calling once/load initialization\\n

Cause: Header message.

Action: Check the error(s) below it for more information.

SQL\*Loader-00952: Error calling once/data file initialization\\n

Cause: Header message.

Action: Check the error(s) below it for more information.

SQL\*Loader-00953: Error shipping read buffer across 2-task\\n

Cause: Header message.

Action: Check the error(s) below it for more information.

SQL\*Loader-00954: Error shipping index to read buffer across 2-task\\n

Cause: Header message.

Action: Check the error(s) below it for more information.

SQL\*Loader-00955: Error calling col array build, block formatter\\n

Cause: Header message.

Action: Check the error(s) below it for more information.

SQL\*Loader-00956: Error calling once/data file finishing\\n

Cause: Header message.

Action: Check the error(s) below it for more information.

SQL\*Loader-00957: Error shipping text string across 2-task\\n

Cause: Header message.

Action: Check the error(s) below it for more information.

SQL\*Loader-00958: Error popping data relocation address stack\\n

Cause: Header message.

Action: Check the error(s) below it for more information.

SQL\*Loader-00959: Error shipping buffer across 2-task\\n

Cause: Header message.

Action: Check the error(s) below it for more information.

SQL\*Loader-00961: Error calling once/load finishing for table string\\n

Cause: Header message.

Action: Check the error(s) below it for more information.

SQL\*Loader-00962: Error setting user-side Ctrl-C handler\\n

Cause: Header message.

Action: Check the error(s) below it for more information.

SQL\*Loader-00963: Error clearing user-side Ctrl-C handler\\n

Cause: Header message.

Action: Check the error(s) below it for more information.

SQL\*Loader-00965: Error ORA-number disabling constraint string on table string

Cause: Header message.

Action: Check the error(s) below it for more information.

SQL\*Loader-00966: Error ORA-number disabling all triggers on table string

Cause: Header message.

Action: Check the error(s) below it for more information.

SQL\*Loader-00969: Error performing file name translation on kernel side\\n

Cause: File specified for parallel load is probably not a valid database file.

Action: Specify a valid database file.

SQL\*Loader-00970: enabled constraint on an XML column not allowed in direct path\\n

Cause: An enabled check constraint existed on an XML column.

Action: Disable the check constraint before attempting to load the table data using the direct path mode, or leave the constraint enabled but use the conventional path mode instead.

SQL\*Loader-00971: parallel load option not allowed when loading lob columns\\n

Cause: An attempt was made to load lob columns using parallel=true. This error will also be issued when loading columns stored as lobs (such as varrays and xml types)

Action: Do not use the parallel option when loading lob columns.

SQL\*Loader-00972: Warning: ROWS parameter ignored when NO\_INDEX\_ERRORS is used.\\n

Cause: Specifying save points using the ROWS parameter was not supported with NO\_INDEX\_ERRORS=TRUE.

Action: Remove the ROWS parameter from the command-line arguments or do not specify NO\_INDEX\_ERRORS=TRUE.

SQL\*Loader-00973: Warning: ROWS parameter ignored when PARTITION\_MEMORY is used.\\n

Cause: Specifying save points using the ROWS parameter was not supported with PARTITION\_MEMORY=n.

Action: Remove the ROWS parameter from the command-line arguments or do not specify PARTITION\_MEMORY=n.

SQL\*Loader-00974: database is not available for update\\n

Cause: The database was not opened for read/write access. SQL\*Loader requires that the database be opened for read/write access.

Action: Verify that the database is opened for read/write access. Then retry the operation.

SQL\*Loader-02026: the load was aborted because SQL Loader cannot continue.\\n

Cause: The load cannot continue. See the error message before this \* message for the cause of the error.

Action: See the action for the error message that precedes this one.

SQL\*Loader-02027: This shard load thread was aborted because SQL Loader cannot continue.\\n

Cause: A shard load thread could not continue. See the error message before \* this message for the cause of the error.

Action: See the action for the error message that precedes this one.

SQL\*Loader-02050: Multibyte character error.\\n

Cause: Text specified by POSITION or terminated by newlines is invalid.

Action: Edit the SQL\*Loader control file or the data file to fix alignment of column.

SQL\*Loader-02300: For CSV format files, all fields must be delimited fields. Field string is not delimited.\\n

Cause: CSV format files did not have delimited fields. CSV format files must have all delimited fields so that SQL\*Loader can process the fields.

Action: Make all of the fields delimited or remove the CSV specification and retry.

SQL\*Loader-02301: For FIELD NAMES, all fields must be delimited fields. Field string is not delimited.\\n

Cause: Data files with a FIELD NAMES record did not have delimited fields. Data files with a FIELD NAMES record must have all delimited fields so that SQL\*Loader can process the field names.

Action: Make all of the fields delimited and retry.

SQL\*Loader-02302: Data in the control file not supported with CSV format files.\\n

Cause: CSV format file was specified with INFILE \* indicating that there was data in the control file.

Action: Move the data to a separate data file and retry.

SQL\*Loader-02303: Unable to process LOB Location Specifier field string.\\n

Cause: The LOB Location Specifier field was not processed correctly.

Action: Make sure the LOB Location Specifier is formatted correctly.

SQL\*Loader-02304: LOB Location Specifier for column string must be loaded into a LOB column.\\n

Cause: The destination column for a LOB Location Specifier field was not a LOB data type.

Action: Make sure the destination column is a LOB data type.

SQL\*Loader-02305: LOB Location Specifier for column string - invalid offset or length.\\n

Cause: The LOB Location Specifier contained an invalid offset or length.

Action: The offset must not be a negative value. The length can only be negative if a value of -1 (for a NULL LOB) is specified.

SQL\*Loader-02306: LOB Location Specifier for column string failed to read LOB file string.\\n

Cause: The destination column for a LOB Location Specifier field was not a LOB data type.

Action: Make sure the LOB data file contains valid data.

SQL\*Loader-02307: LOB Location Specifier for column string failed to read entire length request of number bytes from LOB file string.\\n

Cause: The LOB Location Specifier length request exceeded the length of the lob file. The entire length requested could not be satisfied and will be less than the amount specified.

Action: Make sure the LOB Location Specifier length is correct.

SQL\*Loader-02308: LOB Location Specifier failure seeking to offset number in LOB file string

Cause: The LOB Location Specifier specified an offset in the LOB file which resulted in a seek failure.

Action: Contact Oracle Support Services.

SQL\*Loader-02309: error setting session parameter string\\n

Cause: An error occurred while attempting to alter the user session with the parameter specified.

Action: See subsequent messages for more information about the error.

SQL\*Loader-02310: The container map constraint for table string was ignored by direct path load.\\n

Cause: The container map constraint was detected but was not verified or enforced during a direct path load.

Action: Use conventional path to enforce the container map constraint.

SQL\*Loader-02311: The unique constraint for table string was ignored by direct path load for the Application Root rows.\\n

Cause: The unique constraint was detected but was not verified or enforced for Application Root rows during a direct path load when the sharing level was extended data-linked.

Action: Use conventional path load to enforce the unique constraint including Application Root rows.

SQL\*Loader-02312: Sharding key string was not being loaded.\\n

Cause: The sharding key in the error message was not being loaded.

Action: Include all sharding keys in the SQLLDR control file when loading a sharded table.

SQL\*Loader-02313: Conversion of the sharding key failed.\\n

Cause: The sharding key value in the error message could not be converted to the column type of the key.

Action: Check to be sure the key value can be converted to the column type of the key.

SQL\*Loader-02314: Sharding key was NULL.\\n

Cause: The sharding key in the error message contained a NULL value.

Action: Do not attempt to load sharing keys with NULL values.

SQL\*Loader-02315: Sharding key string cannot be a SQL expression or filler.\\n

Cause: The sharding key in the error message was invalid.

Action: Do not specify sharding keys as expressions or fillers.

SQL\*Loader-02316: Parallel loading is not allowed.\\n

Cause: Parallel loading was not allowed because one reader must be used when loading with LOBFILEs that were not terminated by EOF. One reader must be used when SKIP, LOAD, BOM checking, field names, RECNUM, sequences or max discards are specified.

Action: Do not specify the DEGREE\_OF\_PARALLELISM parameter for this case.

SQL\*Loader-02317: Shard string to load was not found or is a duplicate.\\n

Cause: The shard name in the list of shards to be loaded was not found or was specified multiple times.

Action: Only specify distinct and valid shard names in the list of shards to be loaded.

SQL\*Loader-02318: Sharding key string was non-character type.\\n

Cause: The sharding key in the error message was not a character type.

Action: Do not attempt to load sharing keys with non-character types.

SQL\*Loader-02319: Table string.string is not a sharded table on a catalog.\\n

Cause: An attempt was made to load a table that was not sharded and not on a catalog using automatic parallel shard loading.

Action: Do not attempt to load a table that is not sharded and not on a catalog using parallel shard loading.

SQL\*Loader-02320: Sharded table string.string is not present on all shards.\\n

Cause: Attempt to load a sharded table on catalog when table is not on all shards.

Action: Do not attempt to load a sharded table using parallel shard loading when the table is not on all shards.

SQL\*Loader-02321: The \[SUB\]PARTITION clause is not allowed when loading a sharded table.\\n

Cause: Attempt to load a sharded table using the \[SUB\]PARTITION clause.

Action: Do not attempt to load a sharded table using the \[SUB\]PARTITION clause.

SQL\*Loader-02322: Record does not map to a shard partition.\\n

Cause: Sharding key did not map to any partition.

Action: Check data and table definition for correct mapping.

SQL\*Loader-02323: Topology fetch from server encountered unexpected error.\\n

Cause: An error occurred on the server side with Sharding metadata.

Action: Try the load again. If it still fails, contact Oracle Support Services.

SQL\*Loader-02324: Bad data format recieved from server.\\n

Cause: An error occurred on the server side with Sharding metadata.

Action: Try the load again, if still fails contact Oracle Support Services.

SQL\*Loader-02325: Service role is not a primary service.\\n

Cause: Service role was not a primary service.

Action: Create and use a primary service only using parallel load of shards.

SQL\*Loader-02326: Global context not initialized.\\n

Cause: Internal error.

Action: Contact Oracle Support Services.

SQL\*Loader-02327: Record does not map to a shard partition.\\n

Cause: Key did not map to any partition.

Action: Check data and table definition for correct mapping.

SQL\*Loader-02328: Invalid key type.\\n

Cause: The key type did not match the key metadata.

Action: Provide a key type that matches the key metadata.

SQL\*Loader-02329: Unsupported key type.\\n

Cause: Column type is not a supported key type.

Action: Column type must be a supported type.

SQL\*Loader-02330: Timestamp formatting error.\\n

Cause: Invalid timestamp format.

Action: Check and fix data with invalid timestamp format.

SQL\*Loader-02331: Sharding key character set conversion error.\\n

Cause: Invalid character data.

Action: Check and fix data with invalid character data.

SQL\*Loader-02332: The database type of the instance does not match that of the SDB context. \\n

Cause: Internal error.

Action: Check that the sharding configurtion is valid. If valid and still fails, Contact Oracle Support Services.

SQL\*Loader-02333: OCI call error.\\n

Cause: Internal error.

Action: Contact Oracle Support Services.

SQL\*Loader-02334: Global Service Manager (GSM) internal error.\\n

Cause: GSM internal error.

Action: Contact Oracle Support Services.

SQL\*Loader-02335: Shard data not initialized.\\n

Cause: Internal error.

Action: Contact Oracle Support Services.

SQL\*Loader-03120: Resumable parameters ignored -- current session not resumable\\n

Cause: Current session is not resumable.

Action: Must specify RESUMABLE=TRUE to enable resumable session in order for the RESUMABLE\_NAME and RESUMABLE\_TIMEOUT parameters to take effect.