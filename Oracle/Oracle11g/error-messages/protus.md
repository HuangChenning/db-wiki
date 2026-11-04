---
title: PROT-00001 to PROT-00811
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/protus.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 96 PROT-00001 to PROT-00811

PROT-00001: Failed to initialize ocrconfig

Cause: Unable to initialize and start ocrconfig.

Action: Check log file for details about the failure.

PROT-00002: Export file 'string' already exists

Cause: Requested export file exists in the given path.

Action: Change the location for export file or remove the old export file.

PROT-00003: Failed to create export file 'string'

Cause: Unable to create or open file for exporting cluster registry data.

Action: Check access privilege or disk space of the requested path.

PROT-00004: Failed to retrieve data from the cluster registry

Cause: Unable to retrieve necessary information from the cluster registry.

Action: Check the availability of the cluster registry and the details of the failure from the log file.

PROT-00005: Clusterware is not running properly

Cause: Unable to register with clusterware for access to the cluster registry.

Action: Check the status of clusterware running on the machine.

PROT-00006: The specified import file 'string' cannot be found

Cause: The import file did not exist.

Action: Check the file and its correct path and try again.

PROT-00007: Failed to open the specified import file 'string'

Cause: Unable to access the specified import file.

Action: Check access privilege of the import file.

PROT-00008: Failed to import data from specified file to the cluster registry

Cause: Unable to read data from the import file and import to the cluster registry.

Action: Check availability of the cluster registry and the details of the failure from the log file.

PROT-00010: Failed to open the specified source cluster registry

Cause: Unable to access the specified source cluster registry.

Action: Check access privilege and location of the source cluster registry, and the log file for more detail.

PROT-00011: Failed to open the specified destination cluster registry

Cause: Unable to access the specified destination cluster registry.

Action: Check access privilege and location of the destination cluster registry. Also check the log file for more details.

PROT-00012: Oracle Cluster Registry to be upgraded has an unsupported version

Cause: Oracle Cluster Registry to be upgraded had an unsupported version.

Action: Upgrade Oracle Cluster Registry to a version supported.

PROT-00013: Oracle Cluster Registry is in current version

Cause: Oracle Cluster Registry was in current version.

Action: No action required.

PROT-00014: Oracle Cluster Registry to be downgraded has an earlier version

Cause: Oracle Cluster Registry to be downgraded had an earlier version.

Action: No action required.

PROT-00015: Unimplemented feature

Cause: Requested feature has not been implemented in current release.

Action: Try the feature again in the next release.

PROT-00016: Internal Error

Cause: This is a generic internal error for ocrconfig.

Action: Contact Oracle Support Services.

PROT-00017: Fatal Error

Cause: This is a generic fatal error for ocrconfig.

Action: Contact Oracle Support Services.

PROT-00018: Failed to open the specified backup file 'string'

Cause: File did not exist or user did not have permission to open the file.

Action: Ensure that the file exists and its permissions are correct. Also check the log file for more details.

PROT-00019: Cannot proceed while the Cluster Ready Service is running

Cause: The Cluster Ready Service was running.

Action: Use the 'crsctl stop crs' command to shutdown the Cluster Ready Service on the local node.

PROT-00020: Insufficient permission to proceed. Require privileged user

Cause: User was not a privileged user.

Action: Run the command again using a privileged user.

PROT-00021: Invalid parameter

Cause: Input parameter was not valid.

Action: Check log file for more information.

PROT-00022: Storage too small

Cause: Specified storage was too small to mirror OCR content.

Action: Execute the 'ocrcheck' command to retrieve the total size, and ensure that the size of the device to be added is large enough for use by cluster registry.

PROT-00023: Failed to backup OCR

Cause: Unable to take a backup of OCR.

Action: Check availability of the cluster registry and the available free space on the file system where the manual backup will be stored. Use ocrconfig -backuploc to specify a new backup location if necessary. Check the CRS log file for more information.

PROT-00024: Auto backups for the Oracle Cluster Registry are not available

Cause: Auto backups for the Oracle Cluster Registry were not yet created. They are created once every four hours.

Action: No action required.

PROT-00025: Manual backups for the Oracle Cluster Registry are not available

Cause: Manual backups for the Oracle Cluster Registry were not yet created.

Action: Manual backups can be created using 'ocrconfig -manualbackup' command.

PROT-00026: Oracle Cluster Registry backup locations were retrieved from a local copy

Cause: The Oracle Cluster Registry files were not accessible. Information about the cluster registry backups is also maintained in the Oracle Local Registry. The information displayed has been retrieved from the Oracle Local Registry. This information may be outdated.

Action: Run 'ocrconfig -showbackup' command from another node in the cluster. Compare the output of the 'ocrconfig -showbackup' on this node with output of the same command from other nodes in the cluster to determine the latest backup copy.

PROT-00027: Cannot configure another Oracle Cluster Registry location because the maximum number of Oracle Cluster Registry locations (5) have been configured

Cause: The maximum number of Oracle Cluster Registry locations (5) had been configured.

Action: (Optional) Verify the configuration using the 'ocrcheck -config' command. Delete an Oracle Cluster Registry device by executing 'ocrconfig -delete \<existing location>' command, and retry the operation.

PROT-00028: Cannot delete or replace the only configured Oracle Cluster Registry location

Cause: A delete or replace operation was performed when there was only 1 configured Oracle Cluster Registry location. The above listed operation can only be performed when there are at least 2 configured Oracle Cluster Registry locations.

Action: Execute 'ocrconfig -add \<new location>' to add the new Oracle Cluster Registry location followed by 'ocrconfig -delete \<existing location>' command.

PROT-00029: The Oracle Cluster Registry location is already configured

Cause: The location to be added was identical to a configured Oracle Cluster Registry location.

Action: Verify the configuration using the 'ocrcheck -config' command. Ensure that the location to be added is not already configured.

PROT-00030: The Oracle Cluster Registry location to be added is not usable

Cause: The Oracle Cluster Registry location to be added did not exist, wasn't mounted correctly, did not have the required permissions, or did not have the sufficient disk space.

Action: Ensure that the location exists, that it is mounted correctly and visible to all nodes in the cluster, that its permissions are correct, and that it has sufficient disk space. If trying to add an ASM Oracle Cluster Registry location, check for related entries in the ASM alert log file for more details.

PROT-00031: The Oracle Cluster Registry location to be added is an ASM disk

Cause: The Oracle Cluster Registry location to be added is already in use by ASM.

Action: Specify a Oracle Cluster Registry location that is not currently in use. Use the 'crsctl query css votedisk' command to get the list of voting files used by CSS. Use the 'asmcmd lsdsk --member' command to get the list of disks used by ASM. Specify a location that is not in either list.

PROT-00032: The Oracle Cluster Registry location to be added is a CSS voting file

Cause: The Oracle Cluster Registry location to be added is already configured as a CSS voting file.

Action: Specify a Oracle Cluster Registry location that is not currently in use. Use the 'crsctl query css votedisk' command to get the list of voting files used by CSS. Use the 'asmcmd lsdsk --member' command to get the list of disks used by ASM. Specify a location that is not in either list.

PROT-00033: Oracle High Availability Services on the local node is not running

Cause: Oracle High Availability Services on the local node was not running

Action: Run 'crsctl start crs' command to start the Oracle High Availability Services on the local node.

PROT-00034: The Oracle Cluster Registry location to be deleted is not configured

Cause: The location to be deleted was not already configured as an Oracle Cluster Registry location.

Action: Run 'ocrcheck -config' command to get the list of configured Oracle Cluster Registry locations. Ensure that the location to be deleted is already configured.

PROT-00035: The configured OCR locations are not accessible.

Cause: The configured Oracle Cluster Registry (OCR) locations did not exist, were not mounted correctly, did not have the required permissions, or did not have sufficient disk space.

Action: Ensure that the locations exist, that they are mounted correctly and visible to all nodes in the cluster, that their permissions are correct, and that they have sufficient disk space. If using an Oracle Automatic Storage Management (Oracle ASM) OCR location, check for entries in the Oracle ASM alert log file for more details.

PROT-00036: Duplicate or previously used Oracle Cluster Registry location string cannot be added

Cause: The Oracle Cluster Registry location to be added had the same contents as that of currently configured locations. This might be due to the location to be added was either duplicate of one of the currently configured locations with a different path or previously used.

Action: Make sure that the location to be added is not currently configured with a different path. If the location was previously configured as an Oracle Cluster Registry location, ensure that the contents are erased before adding it again.

PROT-00037: The Oracle Cluster Registry location string cannot be deleted because it is required for the OCR to be available

Cause: A delete operation was requested when there were minimum configured Oracle Cluster Registry locations available. The above listed operation can only be performed when a majority of configured Oracle Cluster Registry locations are accessible and online.

Action: Run 'ocrcheck' command to get the current status of the configured Oracle Cluster Registry locations. Execute 'ocrconfig -add \<new location>' to add the new Oracle Cluster Registry location followed by 'ocrconfig -delete \<existing location>' command.

PROT-00038: The Oracle Cluster Registry location cannot be added because location string is offline

Cause: An add or replace operation was requested when there was at least one configured Oracle Cluster Registry location which was not accessible or online. The above listed operation can only be performed when the inaccessible Oracle Cluster Registry location has been deleted or replaced.

Action: Run 'ocrcheck' command to get the current status of the configured Oracle Cluster Registry locations. Execute 'ocrconfig -delete \<offline location>' command to delete the inaccessible Oracle Cluster Registry location followed by 'ocrconfig -add \<new location>' command.

PROT-00039: The specified file 'string' has an invalid format

Cause: The specified file was not a valid Oracle Cluster Registry export/import file.

Action: Specify a valid Oracle Cluster Registry file which was created using the 'ocrconfig -export' command.

PROT-00040: The specified file 'string' has an invalid format

Cause: The specified file was not a valid Oracle Cluster Registry backup file.

Action: Use the 'ocrconfig -showbackup' command to list all available backups. Specify a valid Oracle Cluster Registry backup file listed by the above command.

PROT-00041: The specified backup location 'string' is not accessible

Cause: The backup location did not exist or the required permissions were not granted.

Action: Ensure that the location exists and the required file creation permissions are granted.

PROT-00042: The specified backup location 'string' is not a directory or an ASM disk group

Cause: The specified backup location was not a directory or an ASM disk group.

Action: Specify a directory or an ASM disk group.

PROT-00044: Cannot change the Oracle Cluster Registry backup location to an ASM disk group.

Cause: An attempt was made to change the Oracle Cluster Registry backup location to an ASM disk group when the Oracle Cluster Registry was not configured on ASM.

Action: Migrate the Oracle Cluster Registry to ASM before changing the Oracle Cluster Registry backup location to an ASM disk group.

PROT-00045: The specified Oracle Cluster Registry backup location string is inaccessible.

Cause: Oracle Cluster Registry backup location did not exist, was not mounted correctly, or did not have the required permissions.

Action: Ensure that the backup location exists, that it is mounted correctly, and that its permissions are correct. Check the entries in the ASM alert log file for more details.

PROT-00046: Failed to repair the Oracle Cluster Registry configuration while adding the location 'string' on the local node.

Cause: The Oracle Cluster Registry location to be added did not exist, was not mounted correctly, did not have the required permissions, or the OCR file in the disk group did not exist.

Action: Ensure that the location exists with appropriate permissions. If the location is an ASM disk group, then the OCR file in the disk group must already exist, the disk group must be mounted correctly; also check the entries in the ASM alert log file for more details.

PROT-00047: Cannot change the Oracle Cluster Registry backup location to the specified ASM disk group string.

Cause: An attempt was made to change the Oracle Cluster Registry backup location to an ASM disk group which was the same as the only configured ASM Oracle Cluster Registry location.

Action: Add another ASM Oracle Cluster Registry location before changing the Oracle Cluster Registry backup location to the specified ASM disk group or specify a different ASM disk group for the Oracle Cluster Registry backup location.

PROT-00049: The Oracle Cluster Registry (OCR) integrity check failed.

Cause: The integrity check failed for one or more of the configured Oracle Cluster Registry locations.

Action: Use 'ocrcheck' command to validate the block integrity of the configured Oracle Cluster Registry locations. Delete the corrupt locations using the command 'ocrconfig -delete \<corrupt location>'. If all configured Oracle Cluster Registry locations are corrupted, check the availability of backups using the 'ocrconfig -showbackup' command and restore a compatible backup. If you are not able to resolve the problem, contact Oracle Support Services.

PROT-00124: \* Use option '-local' to indicate that the operation is to be performed on the Oracle Local Registry.

Cause: ocrconfig called with incorrect or missing options.

Action: Use ocrconfig with correct options.

PROT-00301: Dump is not feasible when clusterware is running

Cause: Unable to dump cluster registry data when clusterware is running.

Action: Stop the clusterware before retrying ocrdump.

PROT-00302: Failed to initialize ocrdump

Cause: Unable to initialize and start ocrdump.

Action: Check log file for details about the failure.

PROT-00303: Dump file already exists \[string\]

Cause: Requested dump file exists in the given path.

Action: Change the location for the dump file or remove the old dump file.

PROT-00304: Failed to create dump file \[string\]

Cause: Unable to create or open file for dumping cluster registry data.

Action: Check access privilege or disk space of the requested path.

PROT-00305: Failed to write to dump file \[string\]

Cause: Unable to write to dump file while dumping cluster registry data.

Action: Check access privilege or disk space of the requested path.

PROT-00306: Failed to retrieve cluster registry data

Cause: Unable to read cluster registry data.

Action: Check log file for details about the failure.

PROT-00307: The specified key does not exist in cluster registry

Cause: Unable to retrieve the specified key from cluster registry.

Action: Check log file for the key name.

PROT-00309: Failed to access the Oracle Cluster Registry backup file.

Cause: The Oracle Cluster Registry backup file either did not exist or the user did not have the permission to open the file.

Action: Ensure that the file exists and its permissions are correct.

PROT-00418: Use option '-local' to indicate that the operation is to be performed on the Oracle Local Registry.

Cause: ocrdump called with incorrect or missing options.

Action: Use ocrdump with correct options.

PROT-00601: Failed to initialize ocrcheck

Cause: Unable to initialize and start ocrcheck.

Action: Check log file for details about the failure.

PROT-00602: Failed to retrieve data from the cluster registry

Cause: Unable to retrieve necessary information from the cluster registry.

Action: Check the availability of the cluster registry and the details of the failure from the log file.

PROT-00603: Oracle Cluster Registry is logically corrupted

Cause: A logical corruption was detected in the Oracle Cluster Registry.

Action: Check the log file for more information. Check availability of backups using 'ocrconfig -showbackup' command. Restore a compatible backup, and verify using ocrcheck.

PROT-00604: Failed to retrieve the configured location(s) of the cluster registry.

Cause: Unable to retrieve the configured location(s) of the cluster registry.

Action: Check log file for details about the failure.

PROT-00724: Oracle Cluster Registry configuration is:

Cause: ocrcheck called.

Action: None

PROT-00811: when running this tool.

Cause: ocrcheck called with incorrect or missing options.

Action: Use ocrcheck with correct options.