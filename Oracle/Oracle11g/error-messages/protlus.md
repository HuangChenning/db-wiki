---
title: PROTL-00001 to PROTL-00811
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/protlus.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 95 PROTL-00001 to PROTL-00811

PROTL-00001: Failed to initialize ocrconfig

Cause: Unable to initialize and start ocrconfig.

Action: Check log file for details about the failure.

PROTL-00002: Export file 'string' already exists

Cause: Requested export file exists in the given path.

Action: Change the location for export file or remove the old export file.

PROTL-00003: Failed to create export file 'string'

Cause: Unable to create or open file for exporting local registry data.

Action: Check access privilege or disk space of the requested path.

PROTL-00004: Failed to retrieve data from the local registry

Cause: Unable to retrieve necessary information from the local registry.

Action: Check the availability of the local registry and the details of the failure from the log file.

PROTL-00006: The specified import file 'string' cannot be found

Cause: The import file did not exist.

Action: Check the file and its correct path and try again.

PROTL-00007: Failed to open the specified import file 'string'

Cause: Unable to access the specified import file.

Action: Check access privilege of the import file.

PROTL-00008: Failed to import data from specified file to the local registry

Cause: Unable to read data from the import file and import to the local registry.

Action: Check availability of the local registry and the details of the failure from the log file.

PROTL-00010: Failed to open the specified source local registry

Cause: Unable to access the specified source local registry.

Action: Check access privilege and location of the source local registry, and the log file for more detail.

PROTL-00011: Failed to open the specified destination local registry

Cause: Unable to access the specified destination local registry.

Action: Check access privilege and location of the destination local registry. Also check the log file for more details.

PROTL-00012: Oracle Local Registry to be upgraded has an unsupported version

Cause: Oracle Local Registry to be upgraded had an unsupported version.

Action: Upgrade Oracle Local Registry to a version supported.

PROTL-00013: Oracle Local Registry is in current version

Cause: Oracle Local Registry was in current version.

Action: No action required.

PROTL-00015: Unimplemented feature

Cause: Requested feature has not been implemented in current release.

Action: Try the feature again in the next release.

PROTL-00016: Internal Error

Cause: This is a generic internal error for ocrconfig.

Action: Contact Oracle Support Services.

PROTL-00017: Fatal Error

Cause: This is a generic fatal error for ocrconfig.

Action: Contact Oracle Support Services.

PROTL-00018: Failed to open the specified backup file 'string'

Cause: File did not exist or user did not have permission to open the file.

Action: Ensure that the file exists and its permissions are correct. Also check the log file for more details.

PROTL-00019: Cannot proceed while the Oracle High Availability Service is running

Cause: The Oracle High Availability Service was running.

Action: Use the 'crsctl stop crs' command to shutdown the Oracle High Availability Service on the local node.

PROTL-00020: Insufficient permission to proceed. Require privileged user

Cause: User was not a privileged user.

Action: Run the command again using a privileged user.

PROTL-00021: Invalid parameter

Cause: Input parameter was not valid.

Action: Check log file for more information.

PROTL-00025: Manual backups for the Oracle Local Registry are not available

Cause: Manual backups for the Oracle Local Registry were not yet created.

Action: Manual backups can be created using 'ocrconfig -local -manualbackup' command.

PROTL-00035: The configured OLR location is not accessible.

Cause: The configured Oracle Local Registry (OLR) location did not exist, did not have the required permissions, or did not have sufficient disk space.

Action: Ensure that the location exists, that its permissions are correct, and that it has sufficient disk space. Also check the Clusterware alert log file for more details.

PROTL-00039: The specified file 'string' has an invalid format

Cause: The specified file was not a valid Oracle Local Registry export/import file.

Action: Specify a valid Oracle Local Registry file which was created using the 'ocrconfig -local -export' command.

PROTL-00040: The specified file 'string' has an invalid format

Cause: The specified file was not a valid Oracle Local Registry backup file.

Action: Use the 'ocrconfig -local -showbackup' command to list all available backups. Specify a valid Oracle Local Registry backup file listed by the above command.

PROTL-00041: The specified backup location 'string' is not accessible

Cause: The backup location did not exist or the required permissions were not granted.

Action: Ensure that the location exists and the required file creation permissions are granted.

PROTL-00042: The specified backup location 'string' is not a directory

Cause: The specified backup location was not a directory.

Action: Specify a directory.

PROTL-00049: The Oracle Local Registry (OLR) integrity check failed.

Cause: The integrity check failed for the configured Oracle Local Registry location.

Action: Check availability of backups using 'ocrconfig -local -showbackup' command and restore a compatible backup. If you are not able to resolve the problem, contact Oracle Support Services.

PROTL-00124: \* Use option '-local' to indicate that the operation is to be performed on the Oracle Local Registry.

Cause: ocrconfig called with incorrect or missing options.

Action: Use ocrconfig with correct options.

PROTL-00302: Failed to initialize ocrdump

Cause: Unable to initialize and start ocrdump.

Action: Check log file for details about the failure.

PROTL-00303: Dump file already exists \[string\]

Cause: Requested dump file exists in the given path.

Action: Change the location for the dump file or remove the old dump file.

PROTL-00304: Failed to create dump file \[string\]

Cause: Unable to create or open file for dumping local registry data.

Action: Check access privilege or disk space of the requested path.

PROTL-00305: Failed to write to dump file \[string\]

Cause: Unable to write to dump file while dumping local registry data.

Action: Check access privilege or disk space of the requested path.

PROTL-00306: Failed to retrieve local registry data

Cause: Unable to read local registry data.

Action: Check log file for details about the failure.

PROTL-00307: The specified key does not exist in local registry

Cause: Unable to retrieve the specified key from local registry.

Action: Check log file for the key name.

PROTL-00309: Failed to access the Oracle Local Registry backup file.

Cause: The Oracle Local Registry backup file either did not exist or the user did not have the permission to open the file.

Action: Ensure that the file exists and its permissions are correct.

PROTL-00418: Use option '-local' to indicate that the operation is to be performed on the Oracle Local Registry.

Cause: ocrdump called with incorrect or missing options.

Action: Use ocrdump with correct options.

PROTL-00601: Failed to initialize ocrcheck

Cause: Unable to initialize and start ocrcheck.

Action: Check log file for details about the failure.

PROTL-00602: Failed to retrieve data from the local registry

Cause: Unable to retrieve necessary information from the local registry.

Action: Check the availability of the local registry and the details of the failure from the log file.

PROTL-00603: Oracle Local Registry is logically corrupted

Cause: A logical corruption was detected in the Oracle Local Registry.

Action: Check the log file for more information.

PROTL-00604: Failed to retrieve the configured location of the local registry

Cause: Unable to retrieve the location of local registry.

Action: Check log file for details about the failure.

PROTL-00724: Oracle Local Registry configuration is:

Cause: ocrcheck called.

Action: None

PROTL-00811: when running this tool.

Cause: ocrcheck called with incorrect or missing options.

Action: Use ocrcheck with correct options.