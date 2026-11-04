---
title: VID-00611 to VID-00721
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/vidus.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 114 VID-00611 to VID-00721

VID-00611: unable to access the BLOB for reading

Cause: The BLOB could not be opened for reading.

Action: Contact Oracle Support Services.

VID-00612: unable to open export destination file

Cause: The file could not be created or opened.

Action: Check that the file does not refer to an existing directory. Check that the file is not locked by another application.

VID-00613: export destination access denied

Cause: Permission to write to destination file was denied.

Action: Refer to the Oracle Multimedia documentation for information on granting privileges for the export() method.

VID-00614: I/O error during export

Cause: The export operation failed because of an I/O error.

Action: Check OS logs and contact Oracle Support Services.

VID-00702: unable to initialize video processing environment

Cause: The initalization of the video processing procedure failed.

Action: See the database administrator to make sure that enough memory has been allocated to JServer. If JServer does have enough memory, contact Oracle Support Services.

VID-00703: unable to read video data

Cause: An error occurred while accessing the video source.

Action: Make sure the video source is valid. For external sources, make sure all access priviliges are granted.

VID-00704: invalid input format or corrupted input data

Cause: The video data in the source was not in the format specified by the format field of the video object. In some unusal cases, the video data is actually corrupted.

Action: Provide a correct value in the format field. If the correct value is unknown, put NULL in the format field to invoke the DEFAULT format plug-in.

VID-00705: unsupported input format

Cause: The file format of the video data was not supported. This error can only occur in the DEFAULT format plug-in package.

Action: Refer to the Oracle Multimedia documentation for supported formats.

VID-00706: unsupported or corrupted input format

Cause: The video data was either corrupted or the file format was not supported.

Action: Refer to the Oracle Multimedia documentation for supported formats. If the video data is not corrupted and is in a supported file format, contact Oracle Support Services.

VID-00707: unable to read empty video data

Cause: There is no data in the video object.

Action: Refer to the Oracle Multimedia documentation for information on how to populate the video object with video data.

VID-00713: internal error while parsing video data

Cause: An internal error occurred during parsing.

Action: Contact Oracle Support Services.

VID-00714: internal error

Cause: An internal error occurred.

Action: Contact Oracle Support Services.

VID-00721: unable to find format plug-in package ORDPLUGINS.ORDX\_string\_VIDEO

Cause: Custom video plug-in for user-specified format was not found.

Action: Ensure correct video format is specified or proper custom video plug-in package is installed.