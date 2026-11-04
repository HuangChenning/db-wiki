---
title: KUP-00552 to KUP-11024
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/kupus.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 36 KUP-00552 to KUP-11024

KUP-00552: internal XAD package failed to load

Cause: An error was encountered while attempting to initialize the XAD package.

Action: This message should be accompanied by other error message(s) indicating the cause of the error.

KUP-00554: error encountered while parsing access parameters

Cause: The parser detected a syntax error.

Action: This message should be accompanied by other error message(s) indicating the cause of the error.

KUP-00561: invalid length for binary integer field string

Cause: An integer field was specified with an invalid length. The only supported lengths for binary integer fields are 1, 2, 4, and 8.

Action: None

KUP-00562: unknown escape sequence

Cause: An unknown escape sequence was specified to the parser. An escape sequence is a backslash followed by a character.

Action: Consult documentation for list of allowable control characters.

KUP-00600: internal error, arguments \[string\] \[string\] \[string\] \[string\] \[string\]

Cause: An internal XAD error occurred.

Action: Contact Oracle Support.

KUP-00601: fatal XAD error

Cause: A fatal error has occurred.

Action: This message should be accompanied by other error message(s) indicating the cause of the error.

KUP-01006: error signalled during parse of access parameters

Cause: An error was signalled during parsing of the access parameters.

Action: This message should be accompanied by other error message(s) indicating the cause of the error.

KUP-01007: at line number column number

Cause: This is an informational message indicating the line and column where a syntax error was detected.

Action: None

KUP-01008: the bad identifier was: string

Cause: This is an informational message indicating the identifier token that caused a syntax error.

Action: None

KUP-02000: wrong message file version (msg number not found)

Cause: The kupxx.msb file is not the correct version.

Action: Check that the installation was done correctly.

KUP-02001: unrecognized punctuation symbol "string"

Cause: An illegal punctuation character was encountered.

Action: Remove the illegal character.

KUP-02002: unexpected end of input file reached

Cause: This is probably caused by failure to supply the closing quote for a quoted string.

Action: Correct the input.

KUP-02003: unrecognized character: string

Cause: An input character that is neither an alpha, digit, or punctuation was encountered.

Action: Remove the character.

KUP-02004: quoted string too big

Cause: A quoted string longer than 2000 bytes was encountered.

Action: This may be caused by a missing close quote. If so, add the missing quote, otherwise shorten the string.

KUP-02005: token too big

Cause: A token longer than 1000 bytes was encountered

Action: Tokens must be separated by whitespace or punctuation. Either add the missing whitespace or punctuation, or shorten the token.

KUP-02006: script line too long

Cause: a line longer than 500 bytes was encountered

Action: break the line up into shorter lines

KUP-03001: fatal error during library cache pre-loading

Cause: This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

KUP-03002: end position (number) <= start position (number) for field: string

Cause: Error in specifying position for the specified field in the access parameters."

Action: Check that the specified end position is greater than the specified start position.

KUP-03003: absolute end(number) - start(number)!= fieldlength (number) for field string

Cause: The number of bytes occupied by the field as specified by the starting offset and ending offset of the field is not the same as the number of bytes specified for the datatype of the field.

Action: Verify the absolute begin/end position(s) specified match the length of the field.

KUP-03004: absolute end (number) specified with relative start (number) for field string

Cause: The position of field was specified with a relative start and an absolute end.

Action: Use relative end with relative start

KUP-03005: relative end (number) specified does not match fieldlen(number) for field string

Cause: The number of bytes specified by the relative end position for the field does not match the number of bytes in the datatype.

Action: Correct either the datatype length or the relative end position.

KUP-03006: error initializing handle for character set string

Cause: Error attempting to retrieve information for the character set.

Action: Verify that the character set name is valid.

KUP-03007: end position (number) is less than start position (number) for range

Cause: A byte range specified a start position that comes after the end position.

Action: Verify the start and end positions are correctly specified.

KUP-03008: OCI error getting column parameters.

Cause: An error occurred while trying to obtain column parameters.

Action: Contact Oracle Support.

KUP-03009: OCI error getting column name.

Cause: An error occurred while trying to obtain column name.

Action: Contact Oracle Support.

KUP-03010: OCI error getting database column type.

Cause: An error occurred while trying to obtain database column type.

Action: Contact Oracle Support.

KUP-03011: OCI error getting database column size.

Cause: An error occurred while trying to obtain database column size.

Action: Contact Oracle Support.

KUP-03012: OCI error getting database column precision.

Cause: An error occurred while trying to obtain database column precision.

Action: Contact Oracle Support.

KUP-03013: OCI error getting database column scale.

Cause: An error occurred while trying to obtain database column scale.

Action: Contact Oracle Support.

KUP-03014: OCI error getting datetime fsprecision.

Cause: An error occurred while trying to obtain a datetime column precision value."

Action: Contact Oracle Support.

KUP-03015: OCI error getting datetime lfprecision.

Cause: An error occurred while trying to obtain database column precision.

Action: Contact Oracle Support.

KUP-03016: length specified for FIXED records must be greater than 0

Cause: A record format of FIXED was specified with a length of 0.

Action: None

KUP-03017: length specified for VARIABLE records must be greater than 0

Cause: A record format of VARIABLE was specified with a length of 0.

Action: None

KUP-03018: invalid date mask "string" specified for column string

Cause: The date mask for the specified column is invalid.

Action: None

KUP-03019: directory object not specified in LOBFILE clause for field string

Cause: A LOBFILE clause was specified for the field, but no directory object was specified. When no directory object is specified, then the default directory specified for the external table is used, but no default directory was specified.

Action: Specify a directory object in the LOBFILE clause or specify a default directory for the external table.

KUP-03020: empty delimiter specified for record

Cause: An empty delimiter string was specified for a record delimiter.

Action: Specify the string used to delimiter records.

KUP-03021: clause references unknown field string

Cause: A WHEN, NULLIF or DEFAULTIF clause referenced a field that doesn't exist in the data file.

Action: None

KUP-03022: lob data could not be found for field string

Cause: The field specified in the data source that contains the name of the lob file for the record could not be identified.

Action: None

KUP-03023: string for TERMINATED BY or ENCLOSED BY clause for record is longer than maximum number

Cause: The string value for a TERMINATED BY or ENCLOSED BY clause is longer than the maximum number of bytes allowed. If the character set of the data file is different than the character set of the database, the string will be converted to the character set of the data file. If the length of the converted string is too large, then this error will also be returned.

Action: Use shorter delimiters in the data file and the access parameters.

KUP-03024: string for TERMINATED BY or ENCLOSED BY clause for column string is longer than maximum number

Cause: The string value for a TERMINATED BY or ENCLOSED BY clause for the columns is longer than the maximum number of bytes allowed. If the character set of the data file is different than the character set of the database, the string will be converted to the character set of the data file. If the length of the converted string is too large, then this error will also be returned.

Action: Use shorter delimiters in the data file and the access parameters.

KUP-03998: error number formatting KUP message number

Cause: error occured while attempting to format a KUP message.

Action: contact Oracle support.

KUP-03999: error occurred while processing a date format: ORA-number: string

Cause: Error converting a date format string into an internal representation.

Action: Verify that the date format strings specified in the access parameters are valid.

KUP-04000: error initializing IO state for file string in string

Cause: An unexpected error occurred while preparing the file.

Action: Contact Oracle support.

KUP-04001: error opening file string

Cause: An error occurred while attempting to open the specified file. This message should be followed by another message with more information about the error.

Action: See the error that follows to determine the action to be taken.

KUP-04002: error getting file size for file string

Cause: An error occurred while retrieving the number of bytes in the specified file.

Action: See the error that follows to determine the action to be taken.

KUP-04003: error while closing file string

Cause: An error occurred while closing the specified file.

Action: See the error that follows to determine the action to be taken.

KUP-04004: error while reading file string

Cause: An error occurred while reading the specified file.

Action: See the error that follows to determine the action to be taken.

KUP-04005: file operation successful

Cause: A file oepration succeeded.

Action: None

KUP-04006: file operation failed

Cause: An operation on a file failed. The file is named in the message preceeding this one.

Action: See subsequent message for more information about the error.

KUP-04007: end of file reached

Cause: The end of file was reached for a file. The file is named in the message preceding this one.

Action: See the message that follows this one for more information.

KUP-04008: access to file denied

Cause: Acess to a file was denied. The file is named in the message preceding this one.

Action: See the message that follows for more information. Verify that the correct files are being used and that the appropriate access is allowed to those files.

KUP-04009: invalid SLF handle

Cause: An internal error caused a data structure associated with the file to become corrupt.

Action: Contact Oracle support.

KUP-04010: file does not exist

Cause: A file operation failed because a file does not exist. The message preceding this message contains the name of the file.

Action: Verify that the correct file name was specified.

KUP-04011: file system is full

Cause: An operation on a file failed because the file system is full. The message preceding this one contains the name of the file.

Action: Free space on the file system or move the file to a different file system.

KUP-04012: file length is too large for output field

Cause: Size of a file is too large.

Action: Break the file up into smaller files.

KUP-04013: other system error

Cause: Internal component SLF was unable to complete an operation because of a system error.

Action: The message displayed before this message describes the operation that was being performed when the error occurred.

KUP-04014: invalid SLF parameter

Cause: An invalid parameter was passed in a call to internal component SLF.

Action: Contact Oracle support.

KUP-04015: internal SLF error

Cause: Internal component SLF encountered an internal error.

Action: Contact Oracle support.

KUP-04016: unknown SLF status code number

Cause: Internal component SLF returned an unknown error code.

Action: Contact Oracle support.

KUP-04017: OS message: string

Cause: An error occurred. This message contains the message associated with this error that was returned by the operating system. The message displayed before this one should indicate the operation that failed.

Action: None

KUP-04018: partial record at end of file string

Cause: An incomplete record was found at the end of the file.

Action: Verify the file is not corrupt or missing data.

KUP-04019: illegal length found for VAR record in file string

Cause: A record in a VAR file has an length field with either no numeric characters in it or with non numeric characters in it.

Action: Verify the records in the file have the correct length specified for them.

KUP-04020: found record longer than buffer size supported, number, in string

Cause: a record in the data source was longer than the maximum data size supported. The number reported is the maximum supported size of a record.

Action: None

KUP-04021: field formatting error for field string

Cause: There was an error trying to find the contents of the specified field in a record.

Action: This message should be followed by another message containing more specific information about the cause of the error.

KUP-04022: field start is before start of record

Cause: The position of the start of a field is before the start of a record. This can occur if a negative number is used to indicate the relative start of a field.

Action: Verify that the definition of the layout of fields in the data file is correct.

KUP-04023: field start is after end of record

Cause: This can happen when specifying either absolute or relative positioning for a field.

Action: Verify that the definition of the layout of fields in the data file is correct. If it is valid for fields at the end of the record to be missing, use the MISSING FIELD VALUES ARE NULL clause in the access parameters.

KUP-04024: field end is before field start

Cause: The end of the field comes after the start of the field. This can happen if the field is defined with a relative start position and an absolute end position.

Action: Verify that the definition of the layout of fields in the data file is correct.

KUP-04025: field extends beyond end of record

Cause: This can happen when specifying either absolute or relative positioning for a field.

Action: Verify that the definition of the layout of fields in the data file is correct.

KUP-04026: field too long for datatype

Cause: The character field in the record is larger than the maximum length specified.

Action: Make sure the definition of the layout of the fields in the data file is correct. Also make sure the correct maximum size was specified for a character datatype.

KUP-04027: file name check failed: string

Cause: The check of the filename failed. These checks are platform specific, but they can include verifying that there are no hard links in the file path, the file is not a soft link, the file specification includes a parent reference ("../" on Unix), or the file was modified between the time the check was made and the file was opened.

Action: Use a file location that does not violate any of the checks.

KUP-04028: conversion of character length to a number failed

Cause: The character length portion of the field could not be converted to a number. This message is followed by another message with information on why the conversion failed.

Action: Make sure the data is correct. Also verify the datatypes specified for the fields are correct.

KUP-04029: numeric field overflowed

Cause: An attempt to convert a character string to number failed because the value of the number in the string was too large.

Action: None

KUP-04030: invalid numeric data

Cause: An attempt to convert a character string to a number failed because non-numeric characters were found.

Action: None

KUP-04031: empty filename specified for LOB file in column string

Cause: The field in the data file that was supposed to contain the name of a LOB file was empty.

Action: Correct the data so that it contains a valid file name.

KUP-04032: internal error string while parsing field string:

Cause: An internal error occurred while parsing a field.

Action: Contact Oracle support.

KUP-04035: beginning enclosing delimiter not found

Cause: The beginning enclosure was not found for a field that is enclosed by delimiters.

Action: Verify that the data is correct. Also verify that the correct enclosing delimiters were specified and whether the enclosing delimiter should be optional.

KUP-04037: terminator not found

Cause: The terminator for the field is missing.

Action: Verify that the records are formatted correctly.

KUP-04038: internal error: string

Cause: an unexpected error condition was detected.

Action: contact Oracle customer support

KUP-04039: unexpected error while trying to find file string in string

Cause: An error occurred while trying to find path containing the file.

Action: This message should be followed by another message with more information about the error.

KUP-04040: file string in string not found

Cause: The file was not found in the directory specified

Action: Verify the correct file and directory names were specified.

KUP-04041: error generating full file name for string in string

Cause: Unexpected error occurred while trying to form a file name.

Action: None

KUP-04043: table column not found in external source: string

Cause: A column in the external table was not found in the access parameters that define the contents of the data source

Action: Verify that the external table is defined correctly and that the abstract parameters are also correct.

KUP-04044: error positioning file string

Cause: An attempt to position a file to an absolute file offset failed.

Action: See messages that follow for more information.

KUP-04045: unexpected OCI status string

Cause: An OCI call returned a status that cannot be handled.

Action: Contact Oracle support.

KUP-04047: error parsing record from external data source

Cause: An error occurred while trying to extract a record from the data source.

Action: Look in the log file for more messages about the error.

KUP-04048: internal error parsing record from external data source

Cause: An unexpected or unhandled error occurred while getting a record from the data source

Action: Contact Oracle support.

KUP-04049: record number discarded from file string

Cause: Informational message displayed whenever the WHEN clause has been satisfied. If a DISCARD file has been specified for the operation, the record will be written to that file.

Action: None

KUP-04050: error while attempting to allocate number bytes of memory

Cause: d by insufficient memory.

Action: Reconnect to the instance and retry the operation.

KUP-04051: error processing column string in row number for datafile string

Cause: an error occurred while trying to convert the data from the data file into the type of a column in the external table.

Action: See messages that follow for more details.

KUP-04052: error processing column string in a row for datafile string

Cause: an error occurred while trying to convert the data from the data file into the type of a column in the external table.

Action: See messages that follow for more details.

KUP-04053: record number number

Cause: This message identifies a record number in a file for a record that had an error. The message preceding this one contains information about the error and the name of the file.

Action: None

KUP-04054: internal error: invalid bad row number identified for bad column number

Cause: This is an internal error.

Action: Contact Oracle support.

KUP-04055: column string is both a field in the data file and a column transform

Cause: The specified column was in the list of fields in the data file and in the list of column transforms. The column should be in one list or the other, but not both.

Action: Determine whether the value for the field in the data file or the value for the field in the column transform should be loaded in to the table. If the value for the data file is to be loaded, then remove the column transform. If the value for the column transform is to be loaded, then rename the field in the data file so that it does not match the name of a field in the table.

KUP-04056: internal error: OCI error while fetching record: number

Cause: An OCI error occurred while processing the granule.

Action: Contact Oracle support.

KUP-04057: internal error: OCI error while fetching record.

Cause: An OCI error occurred while processing the granule.

Action: Contact Oracle support.

KUP-04058: unrecoverable error occurred, operation aborted.

Cause: An unrecoverable error occurred during processing.

Action: See preceding error messages for more information.

KUP-04059: found EOF in length portion of VARIABLE record in file string

Cause: The record parser was looking for the size portion of a file a record format of VARIABLE. It found EOF before finding all the bytes for the length.

Action: Correct the corruption in the file.

KUP-04060: field string referenced by lobfile column string not found

Cause: The LOBFILE transform for the named column referenced a field for either the directory object portion or the name portion of the LOBFILE. However, that field did not exist anywhere in the definition of the data file.

Action: Verify that the LOBFILE clause is specified correctly. Also verify that the field definitions for the data file are correct.

KUP-04061: directory object string specified for LOBFILE column string is not valid

Cause: The column being loaded from a LOBFILE specified the directory object containing the LOBFILE through another field in the data file. In this case, the LOBFILE clause in the access parameters must specify a list of all directory objects that will be used for this field. This error occurs because a field contains the name of a directory object that is not in this list.

Action: Verify that the data file contains the correct directory object and verify that the list of valid directory objects in the LOBFILE clause for this column is complete.

KUP-04062: no data source specified

Cause: No location for the data source of the external table was specified when the external table was created. An empty string is not valid.

Action: Specify the name of the data source in the LOCATION clause when creating an external table.

KUP-04063: unable to open log file string OS error string

Cause: An attempt to open the log file failed.

Action: Specify a different log file or use NO LOGFILE to disable logging.

KUP-04064: fatal error during initialization

Cause: An unexpected error occurred while initializing access to an external table.

Action: Contact Oracle support.

KUP-04065: error processing LOBFILE for field string

Cause: An error occured while opening or reading a LOBFILE for a column in a row.

Action: See message in log file for more information about the error.

KUP-04066: error initializing access to external table source

Cause: An error occurred while attempting to retrieve information about a data source.

Action: See messages preceding this one for more information about the error.

KUP-04067: internal error allocating handle type string

Cause: An attempt to create an internal object failed.

Action: Contact Oracle support.

KUP-04068: internal error fetching attribute string

Cause: An attempt to fetch information about an internal object failed.

Action: Contact Oracle support.

KUP-04069: error fetching data for external table

Cause: An error occurred while atempting to fetch data from an external table.

Action: See messages the precede this one for more information.

KUP-04070: field string referenced by column transform string not found

Cause: The column transform for the named column references a field that did not exist anywhere in the definition of the data file.

Action: Verify that the column transform clause is specified correctly. Also verify that the field definitions for the data file are correct.

KUP-04071: record discarded from file string

Cause: Informational message displayed whenever the WHEN clause has been satisfied. If a DISCARD file has been specified for the operation, the record will be written to that file. The record number in the source data file is not known because multiple servers are loading from the file.

Action: None

KUP-04072: error writing to file string

Cause: An error occurred while attempting to write to the named file.

Action: See messages that follow this message for more information about the error.

KUP-04073: record ignored because all referenced fields are null for a record

Cause: A record was rejected because all fields in the data file referenced by the query were NULL.

Action: None

KUP-04074: no write access to directory object string

Cause: The user does not have write access to the directory object used for a log, bad or reject file.

Action: None

KUP-04075: no read access to directory object string

Cause: The user does not have read access to the directory object used for a data file.

Action: None

KUP-04076: file name cannot contain a path specification: string

Cause: The name of a data file, log file, bad file or reject file contains a path specification.

Action: Use the name of a directory object to indicate where the file should be stored.

KUP-04077: unknown format specifier in file name string

Cause: A format specifier is a percent sign followed by a character. The percent sign and character are replaced by a value depending on the character. This error occurs when the character following the percent sign is not defined to have a value.

Action: See the documentation for information on valid format specifiers. If the file to be opened needs to have a percent sign in its name then use two pecent signs. They will get replaces by a single percent sign in the resulting file name.

KUP-04078: invalid file name specified: string

Cause: Attempt to parse the file name failed.

Action: Specify a valid file name.

KUP-04079: error fetching list of valid directories

Cause: An attempt to retrieve a list of valid directories that can be used by the user to open files failed. See messages that follow for more information.

Action: Contact Oracle support. As a workaround try specifing no log file, no discard files and no bad files.

KUP-04080: directory object string not found

Cause: The directory object specified for an input file or a log, bad or discard file does not exist in the database or the user has no privileges to access this directory.

Action: None

KUP-04081: field string used in concatenation for column string is not a character type

Cause: The specified field was part of a concatenation of strings used to create the value for the names column. However, the field was not of a character datatype. Only character fields may be used as part of concatenating fields.

Action: Verify the correct field was used in the CONCAT clause. Also verify that the correct datatype is specified for the field in the field list.

KUP-04082: error converting field string for LOBFILE column string

Cause: The LOBFILE column had either its directory object name or filename specified by a field in the data file and that field needed to be converted to the server's character set before it could be used. This message indicates that an attempt to convert the field failed.

Action: Verify that the data file has the correct value for the fields. Also verify that the correct character set was specified for the data file.

KUP-04083: no directory object specified in LOBFILE clause for column string

Cause: There was no directory object specified for the LOB files used to populate the named column and no default directory was specified for the external table.

Action: Either specify a directory name, or the name of a data field containing the name of the directory object that contains the files.

KUP-04084: The ORACLE\_DATAPUMP access driver does not support the ROWID column.

Cause: A query of an external table of type ORACLE\_DATAPUMP tried to reference the ROWID column. The ORACLE\_DATAPUMP access driver does not support ROWIDs.

Action: Remove the ROWID from the query. If that is not possible, create a table in the database with the same columns as the external table, copy the data from the external table into the newly created table, and use that new table for the query.

KUP-04085: duplicate directory object string and file string specified for unload

Cause: A CREATE TABLE AS SELECT statement was executed for an external table of type ORACLE\_DATAPUMP and the same directory object and filename combination was specified multiple times.

Action: Issue the CREATE TABLE AS SELECT command again but make sure the combination of directory objects and filenames is unique.

KUP-04086: length of file name exceeds platform maximum of number

Cause: The length of a filename is longer than the maximum length supported by Oracle on the server platform.

Action: Verify that the name is correct. If so, use a shorter file name.

KUP-04087: no execute access to directory object string

Cause: Execute access to the directory object used for a preprocessor file was not granted.

Action: Grant execute privilege on the directory object or specify a different directory which already has execute privilege enabled.

KUP-04088: data sampling is not supported by this access driver

Cause: A query of an external table requested a sample of the data returned. The access driver for the external table does not support sampling.

Action: Do not try to use sampling for this external table.

KUP-04089: column transform string is not the name of a table column

Cause: The specified column was in the list of column transforms but a column by that name does not exist in the table

Action: Verify that the correct name was specified in the column transform.

KUP-04090: big endian byte order mark found when little endian expected in string

Cause: A big endian byte order mark was found at the beginning of the specified file and either the access parameters specified the data was in little endian order or the byte order mark for a previous file was little endian.

Action: The file needs to be loaded separately. If a byte order was specified in the access parameters, make sure it is changed to be big endian.

KUP-04091: little endian byte order mark found when big endian expected in string

Cause: A little endian byte order mark was found at the beginning of the specified file and either the access parameters specified the data was in big endian order or the byte order mark for a previous file was big endian.

Action: The file needs to be loaded separately. If a byte order was specified in the access parameters, make sure it is changed to be little endian.

KUP-04092: attempt to audit directory object string returned internal error number

Cause: An error occurred while attempting to enable auditing for the specified directory object.

Action: Contact Oracle Support Services.

KUP-04094: preprocessing cannot be performed if Database Vault is installed

Cause: The Database Vault option did not permit the execution a program from an Oracle directory object.

Action: If preprocessing must be performed, then the Database Vault option must not be installed.

KUP-04095: preprocessor command string encountered error "string"

Cause: The specified preprocessor command encountered an error during execution.

Action: Verify that the preprocessor command along with any arguments are correct.

KUP-04097: RECORDS clause specified without a record format

Cause: The RECORDS clause was part of the external table access parameters but no record format type was provided.

Action: If the RECORDS clause is used, then it must be followed by one of the VARIABLE, FIXED, or DELIMITED BY clauses.

KUP-04100: record rejected in file string

Cause: A record in the data file was not loaded into the table because of an error while finding fields in the record. See the previous error for more information. The record will be written to the BAD file, if one is being used. The record number in the source data file is not known because multiple servers are loading from the file.

Action: None

KUP-04101: record number rejected in file string

Cause: A record in the data file was not loaded into the table because of an error while finding fields in the record. See the previous error for more information. The record will be written to the BAD file, if one is being used.

Action: None

KUP-04102: record number discarded from file string

Cause: Informational message displayed whenever the WHEN clause has been satisfied. If a DISCARD file has been specified for the operation, the record will be written to that file.

Action: None

KUP-04103: error converting zoned decimal field to number for string

Cause: An error occurred converting a zoned decimal number to an Oracle number.

Action: Verify that the zoned decimal number is formatted correctly.

KUP-04104: zoned decimal field has bad values for string

Cause: A zoned decimal number has an invalid format.

Action: Verify that the zoned decimal number is formatted correctly.

KUP-04105: zoned decimal to number conversion caused overflow for string

Cause: A zoned decimal number could not be converted to an Oracle number because the number is too big for an oracle number.

Action: Verify that the zoned decimal number is formatted correctly.

KUP-04106: precision for zoned decimal number is too large for string

Cause: The precision of a zoned decimal number is larger than the precision that can be stored in an Oracle number.

Action: Verify that the zoned decimal number is formatted correctly.

KUP-04108: unable to reread file string

Cause: The query that is executing requires that a data source for an external table be read multiple times. However, the data source is a sequential device that cannot be reread. Examples of this type of data source is a tape or pipe.

Action: There are a few ways around this problem. One is to rewrite the query so that the external table is referenced only once. Another option is to move the data source to a rereadable device such as a disk file. A third option is to load the data for the external table into a temporary table and change the query to reference the temporary table.

KUP-04109: specified path for directory object "string" is invalid

Cause: The default directory or a directory object specified for an input data file or an output dump, log, bad or discard file contains an invalid path name.

Action: Specify a valid path name for the directory object.

KUP-05004: Warning: Intra source concurrency disabled because parallel select was not requested.

Cause: Intra source concurrency can only be used when parallel select has been requested.

Action: No action is required this message is informational.

KUP-05005: Warning: Intra source concurrency disabled because a field of type RECNUM exists.

Cause: Intra source concurrency cannot be used with RECNUM fields.

Action: No action is required this message is informational.

KUP-05006: Warning: Intra source concurrency disabled because a complex terminator string is being used.

Cause: Intra source concurrency cannot be used with terminators where replicated substrings in the terminator could cause ambiguity during record parsing.\\n\\n"

Action: No action is required this message is informational.

KUP-05007: Warning: Intra source concurrency disabled because the preprocessor option is being used.

Cause: Intra source concurrency cannot be used with the PREPROCESSOR option.

Action: No action is required this message is informational.

KUP-05008: Warning: Intra source concurrency disabled because the input data is in DELIMITED record format and the characterset is neither fixed width nor UTF8.

Cause: Intra source concurrency cannot be used with the DELIMITED record format if the characterset is neither fixed width or UTF8.

Action: No action is required this message is informational.

KUP-05009: Warning: Intra source concurrency disabled because the input data is in VARIABLE record format.

Cause: Intra source concurrency cannot be used with the VARIABLE record format.

Action: No action is required this message is informational.

KUP-11000: file truncated error

Cause: A truncated file was used for the load operation.

Action: Verify unload operation completed successfully.

KUP-11001: files not from the same unload operation

Cause: Files used for the load operation were not from the same unload operation.

Action: Verify the files used are from the same unload operation.

KUP-11002: unable to read data chunk string

Cause: A read or seek to this data chunk was not possible. This chunk may not have existed.

Action: Verify the files used for the load operation are correct.

KUP-11003: bad data encountered while reading from file string

Cause: There was a datatype conversion error while attempting to convert the data in the data file to match the datatype of a column in the external table. The message that follows this one displays the name of the column and the start of the data for the column that could not be converted. The row containing the bad data is rejected and not included as a row in the external table.

Action: If the row containing the bad data should not be filtered out, then modify the definition of the external table so that the datatypes of the columns match the datatypes of the fields in the data file.

KUP-11004: requested version string not supported by ORACLE\_DATAPUMP

Cause: This database version (defaulted to COMPATIBLE if not user-specified) was not supported by ORACLE\_DATAPUMP external table access driver. Note: Database versions before 9.2 were not supported.

Action: Specify a supported version and rerun the operation.

KUP-11005: error seeking in file: string

Cause: An attempt to seek to the specified position in file failed.

Action: Review the error message. Resolve the problem and retry the the operation. Contact Oracle Support Services if the problem cannot be resolved.

KUP-11006: file truncated error in string

Cause: A truncated or incomplete file was used for the load operation.

Action: Verify unload operation completed successfully.

KUP-11007: conversion error loading table string.string

Cause: A row could not be loaded into the table because there was a conversion error for one or more columns in a row.

Action: See the message that follows for more information about the row that could not be loaded. To avoid this error, make sure the definition of the table being loaded matches the definition of the table being unloaded.

KUP-11008: conversion error loading table string.string partition string

Cause: A row could not be loaded into the table because there was a conversion error for one or more columns in a row.

Action: See the message that follows for more information about the row that could not be loaded. To avoid this error, make sure the definition of the table being loaded matches the definition of the table being unloaded.

KUP-11009: data for row: string

Cause: A conversion error occurred while loading data into a table. The message shows values for the field in the row that had the conversion error.

Action: None. This is only an informational message.

KUP-11010: unable to open at least one dump file for fetch

Cause: None of the files in the LOCATION clause can be opened for a fetch on an external table.

Action: A fetch operation on an external table in SQL mode requires that at least one file could be opened. Check that the directory object and file names to the dump files are correct.

KUP-11011: the following file is not valid for this load operation

Cause: This file could not be used for this load operation. See the following message for more information.

Action: Verify all the files in the LOCATION clause are from the same unload operation and that the unload was successful.

KUP-11012: file string in string already exists

Cause: The specified file could not be used for this unload because that would mean overwriting an existing file.

Action: Specify a file that does not currently exist.

KUP-11013: internal number in header in file string is not valid

Cause: The specified file could not be used for this operation because the internal number in the header was not valid.

Action: If the dump files were transferred over, verify the transfer operation was done correctly.

KUP-11014: internal metadata in file string is not valid

Cause: The specified file could not be used for this operation because the internal metadata stored in this file does not match the metadata stored in the first file piece set.

Action: Verify all the files in the LOCATION clause are the correct dump files to use.

KUP-11015: error in unloading or loading data

Cause: An error has occurred in a stream unload or load operation.

Action: Contact Oracle Support Services.

KUP-11016: database version in file string is not valid

Cause: The specified file could not be used for this fetch because its database version was not compatible with the database version in the other files in the LOCATION clause.

Action: Verify all the files in the LOCATION clause were populated with compatible database versions.

KUP-11017: file string not found

Cause: The file was not found.

Action: Verify the correct file (path and file name) was specified.

KUP-11018: file string not a valid dump file

Cause: This file did not have the correct file format. It could not be used for an external table fetch operation.

Action: Verify this file is from a SQL mode external table populate operation and that the operation was successful.

KUP-11019: the following file is not valid for this fetch operation

Cause: A file could not be used for this fetch. See the following message for more information.

Action: Verify all the files in the LOCATION clause are from successful populate operations. If the files were generated from various populate operations, then verify that those were done with common attributes such as with the same tables and compatible database versions.

KUP-11020: header in file string may not contain correct information

Action: Contact Oracle Support Servicess.

KUP-11021: header in file string has an incompatible version number

Cause: A dump file was specified for a load operation whose version number is incompatible with the dump file version currently produced by the Oracle server on the system. Usually this message indicates that the dump file was produced by a newer version of the Oracle server.

Action: Load this dump file using the same version of the Oracle server that created the file.

KUP-11022: specified file name "string" is invalid

Cause: The file name specified for a dump or log file was invalid or null.

Action: Specify a valid file name for the dump or log file.

KUP-11023: specified path for directory object "string" is invalid

Cause: The default directory or a directory object specified for a dump or log file contained an invalid path name or was null.

Action: Specify a valid path name for the directory object.

KUP-11024: This external table can only be accessed from within a Data Pump job.

Cause: An attempt was made to access a temporary external table that was created by Data Pump to be used internally during the execution of an export or import job.

Action: None