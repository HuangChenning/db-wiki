---
title: AUD-00611 to AUD-00809
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/audus.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 112 AUD-00611 to AUD-00809

AUD-00611: unable to access the BLOB for reading

Cause: The BLOB could not be opened for reading.

Action: Contact Oracle Support Services.

AUD-00612: unable to open export destination file

Cause: The file could not be created or opened.

Action: Check that the file does not refer to an existing directory. Check that the file is not locked by another application.

AUD-00613: export destination access denied

Cause: Permission to write to destination file was denied.

Action: Refer to the Oracle Multimedia documentation for information on granting privileges for the export() method.

AUD-00614: I/O error during export

Cause: The export operation failed because of an I/O error.

Action: Check OS logs and contact Oracle Support Services.

AUD-00702: unable to initialize audio processing environment

Cause: The initalization of the audio processing procedure failed.

Action: See the database administrator to make sure that enough memory has been allocated to JServer. If JServer does have enough memory, contact Oracle Support Services.

AUD-00703: unable to read audio data

Cause: An error occurred while accessing the audio source.

Action: Make sure the audio source is valid. For external sources, make sure all access priviliges are granted.

AUD-00704: invalid input format or corrupted input data

Cause: The audio data in the source was not in the format specified by the format field of the audio object. In some unusual cases, the audio data is actually corrupted.

Action: Provide a correct value in the format field. If the correct value is unknown, put NULL in the format field to invoke the DEFAULT format plug-in.

AUD-00705: unsupported input format

Cause: The file format of the audio data was not supported. This error can only occur in the DEFAULT format plug-in package.

Action: Refer to the Oracle Multimedia documentation for supported formats.

AUD-00706: unsupported or corrupted input format

Cause: The audio data was either corrupted or the file format was not supported.

Action: Refer to the Oracle Multimedia documentation for supported formats. If the audio data is not corrupted and is in a supported file format, contact Oracle Support Services.

AUD-00707: unable to read empty audio data

Cause: There is no data in the audio object.

Action: Refer to the Oracle Multimedia documentation for information on how to populate the audio object with audio data.

AUD-00713: internal error while parsing audio data

Cause: An internal error occurred during parsing.

Action: Contact Oracle Support Services.

AUD-00714: internal error

Cause: An internal error occurred.

Action: Contact Oracle Support Services.

AUD-00721: unable to find format plug-in package ORDPLUGINS.ORDX\_string\_AUDIO

Cause: Custom audio plug-in for user-specified format was not found.

Action: Ensure correct audio format is specified or proper custom audio plug-in package is installed.

AUD-00802: name of index is limited to 22 characters

Cause: The user specified an index name that is more than 22 characters long.

Action: Drop this index, and issue the CREATE INDEX statement again with a name that is at most 22 characters long.

AUD-00803: internal error while processing WHERE clause

Cause: The WHERE clause could not be properly processed.

Action: Contact Oracle Support Services.

AUD-00806: first argument to SpeechContains must be a column

Cause: The first argument to SpeechContains is not a column. This is not allowed.

Action: Make sure that the first argument to SpeechContains is a column in a database table.

AUD-00807: SpeechContains: index of indextype ORDSpeechIndex is required

Cause: SpeechContains was used without an associated index of indextype ORDSpeechIndex.

Action: Make sure that SpeechContains is used in the context of an index of indextype ORDSpeechIndex. See the Oracle Multimedia documentation for sample usage scenarios.

AUD-00808: ORDSpeechIndex: unable to CREATE internal Text index

Cause: CREATE INDEX for ORDSpeechIndex failed when trying to create internal Text index.

Action: Make sure that you are supplying a valid parameter string. See SpeechIndexing and Oracle Text documentation for descriptions of a valid parameter string for CREATE INDEX. To return to a consistent state, issue a DROP INDEX command.

AUD-00809: ORDSpeechIndex: unable to ALTER REBUILD internal Text index

Cause: ALTER INDEX REBUILD for ORDSpeechIndex failed when trying to alter rebuild internal Text index.

Action: Make sure that you are supplying a valid parameter string. See SpeechIndexing and Oracle Text documentation for descriptions of a valid parameter string for ALTER INDEX REBUILD. To return to a consistent state, issue a ALTER INDEX REBUILD PARAMETERS('optimize full') command.