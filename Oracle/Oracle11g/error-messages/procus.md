---
title: PROC-00001 to PROC-00109
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/procus.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 94 PROC-00001 to PROC-00109

PROC-00001: Oracle Cluster Registry cannot be initialized.

Cause: An invalid init level was passed to initialize Oracle Cluster Registry.

Action: Initialize Oracle Cluster Registry with a valid init level.

PROC-00002: Cannot perform cluster registry operation at the current init level.

Cause: Program tried a cluster registry operation which is not permitted at the init level.

Action: Initialize Oracle Cluster Registry with an appropriate init level.

PROC-00003: Cannot perform cluster registry operation because context is invalid.

Cause: The Oracle Cluster Registry context passed was invalid.

Action: This is an internal error. Contact Oracle Support Services.

PROC-00004: The cluster registry key to be operated on does not exist.

Cause: Program tried a cluster registry operation on a key which does not exist.

Action: Check to see if the key exists and try the operation again.

PROC-00005: User does not have permission to perform a cluster registry operation on this key.

Cause: Program tried an operation on a cluster registry key for which it does not have permission.

Action: Check to see if program is run as the correct user.

PROC-00006: User does not have permission to perform a cluster registry operation on this key.

Cause: Program tried a cluster registry operation on a key for which it does not have permission.

Action: Check to see if program is run as the correct user.

PROC-00007: Cannot perform cluster registry operation because key or batch handle is invalid.

Cause: The cluster registry key or batch handle passed was invalid.

Action: This is an internal error. Contact Oracle Support Services.

PROC-00008: Cannot perform cluster registry operation because one of the parameters is invalid.

Cause: Program tried a cluster registry operation using an invalid parameter.

Action: This is an internal error. Contact Oracle Support Services.

PROC-00009: Cannot perform cluster registry operation because the buffer passed is too small.

Cause: The amount of memory allocated for the buffer was insufficient.

Action: This is an internal error. Contact Oracle Support Services.

PROC-00010: Cannot delete the cluster registry key as subkeys exist.

Cause: The program tried to delete a key for which subkeys exist.

Action: This is an internal error. Contact Oracle Support Services.

PROC-00011: Cannot perform cluster registry operation because key is NULL.

Cause: The cluster registry key passed was NULL.

Action: This is an internal error. Contact Oracle Support Services.

PROC-00012: Out of heap memory.

Cause: The program ran out of heap memory.

Action: Contact Oracle Support Services.

PROC-00013: Cannot perform cluster registry operation because one of the parameters is NULL.

Cause: Program tried a cluster registry operation using an NULL parameter.

Action: This is an internal error. Contact Oracle Support Services.

PROC-00014: Unknown error occurred

Cause: This is generic internal error for Oracle Cluster Registry.

Action: This is an internal error. Contact Oracle Support Services.

PROC-00015: Failed to initialize the cluster registry

Cause: The Oracle Cluster Registry could not be accessed. The possible causes are:

1\. The cluster registry has not been formatted.

2\. The cluster registry location is not accessible.

3\. The cluster registry location has incorrect permissions.

4\. Oracle Clusterware is not running.

Action:

1\. Run the 'ocrcheck' command to confirm that the OCR is formatted and usable.

2\. Run 'ocrcheck -config' command to retrieve the configured locations, and verify that each location is accessible and has the correct permissions via native platform or OS methods. If a location is an ASM disk group, verify that the disk group exists and is mounted.

3\. Run 'crsctl check crs' command to verify that Oracle Clusterware is running.

PROC-00016: Cannot retrieve any more subkeys for the given keyhandle

Cause: The key has no more subkeys to enumerate.

Action: This is an internal error. Contact Oracle Support Services.

PROC-00017: Unimplemented feature

Cause: Requested feature has not been implemented in the current release.

Action: Try the feature again in the upcoming Oracle release.

PROC-00018: The value size passed is too large

Cause: Cannot set a value of the given size.

Action: This is an internal error. Contact Oracle Support Services.

PROC-00019: Cannot create more subkeys for the key

Cause: An attempt was made to create more subkeys under a key that is not permitted by the cluster registry.

Action: This is an internal error. Contact Oracle Support Services.

PROC-00020: ORACLE\_HOME environment not set

Cause: ORACLE\_HOME environment not set.

Action: Make sure that the ORACLE\_HOME environment variable has been properly set and exported.

PROC-00021: Maximum permitted depth of the OCR tree is reached

Cause: An attempt was made to create subkeys under a key which is already at depth PROCR\_MAX\_KEY\_DEPTH

Action: This is an internal error. Contact Oracle Support Services.

PROC-00022: The OCR backend has an invalid format

Cause: An attempt was made to use OCR before initializing it.

Action: Use the root.sh script. The 'ocrconfig -upgrade' command will initialize OCR.

PROC-00023: Error in cluster services layer

Cause: An error occurred in the cluster services layer while performing a cluster registry operation.

Action: Contact Oracle Support Services.

PROC-00024: Error in the messaging layer

Cause: An error occurred in the messaging layer while performing a cluster registry operation.

Action: This is an internal error. Contact Oracle Support Services.

PROC-00025: Error in the NLS services

Cause: An error occurred in the NLS services while performing a cluster registry operation.

Action: This is an internal error. Contact Oracle Support Services.

PROC-00026: Error while accessing the physical storage

Cause: The Oracle Cluster Registry could not be accessed. The possible causes are:

1\. The cluster registry has not been formatted.

2\. The cluster registry location is not accessible.

3\. The cluster registry location has incorrect permissions.

4\. Oracle Clusterware is not running.

Action:

1\. Run the 'ocrcheck' command to confirm that the OCR is formatted and usable.

2\. Run 'ocrcheck -config' command to retrieve the configured locations, and verify that each location is accessible and has the correct permissions via native platform or OS methods. If a location is an ASM disk group, verify that the disk group exists and is mounted.

3\. Run 'crsctl check crs' command to verify that Oracle Clusterware is running.

PROC-00027: Error in authentication layer

Cause: An error occurred in the authentication layer while performing a cluster registry operation.

Action: Contact Oracle Support Services.

PROC-00028: Oracle Cluster Registry already in current version

Cause: An attempt to upgrade the cluster registry which has already been upgraded.

Action: No action required.

PROC-00029: Error in logging layer

Cause: An error occurred in the logging layer while performing a cluster registry operation.

Action: This is an internal error. Contact Oracle Support Services.

PROC-00030: Oracle Cluster Registry IDs do not match

Cause: The cluster registry storage seen by the client was not the same as the one seen by the server. This may be caused by a misconfiguration.

Action: Contact Oracle Support Services.

PROC-00031: Storage device for the cluster registry is too small

Cause: The configured storage device or the storage device to be newly added to the cluster registry was too small.

Action: Refer to the documentation and configure a storage device that is large enough for use by cluster registry. In case the cluster registry is already configured, execute the 'ocrcheck' command to retrieve the total size, and ensure that the size of the device to be added is large enough for use by cluster registry.

PROC-00032: Cluster Ready Services on the local node is not running

Cause: The Cluster Ready Services on the local node was not running.

Action: Use the 'crsctl start crs' command to start the Cluster Ready Services on the local node.

PROC-00033: Oracle Cluster Registry is not configured

Cause: Oracle Cluster Registry configuration was not present on the node.

Action: Install and configure Oracle Clusterware.

PROC-00034: Oracle Cluster Registry configurations are not compatible

Cause: Cluster registry configuration on this node did not match with another node in the cluster.

Action: Retrieve the cluster registry configuration using 'ocrcheck -config' command on all nodes in the cluster. Fix the configuration on this node and make it consistent using 'ocrconfig -repair' command.

PROC-00035: Cannot perform cluster registry operation due to invalid version

Cause: The operation cannot be performed for this cluster active version

Action: Complete the upgrade before retrying the operation

PROC-00036: No free space to perform this operation

Cause: There is no free space left to perform the requested operation.

Action: Free up space and retry the operation.

PROC-00037: Oracle Cluster Registry does not support the storage type configured

Cause: The configured storage type for cluster registry is not supported

Action: Change the configuration of the cluster registry to a supported storage type. Refer to Oracle documentation for an exhaustive list for each platform.

PROC-00038: Requested block number is not allocated from Oracle Cluster Registry

Cause: The requested block number is not allocated from Oracle Cluster Registry.

Action: Retry the operation with another block number.

PROC-00039: Requested block has an invalid header

Action: Retry the operation with another block number.

PROC-00040: Cannot add more operations to the batch

Cause: An attempt was made to add an operation to a batch that already has the maximum allowed operations.

Action: This is an internal error. Contact Oracle Support Services.

PROC-00041: Oracle Cluster Registry is incorrectly configured

Cause: The cluster registry is incorrectly configured.

Action: Correct the cluster registry configuration.

PROC-00042: User cannot access Oracle Cluster Registry configuration

Cause: Program encountered an error accessing the cluster registry configuration.

Action: Check to see if program is run as the correct user. Check that the cluster registry configuration has the correct permissions.

PROC-00043: Error in the ASM access layer

Cause: An error occurred in the layer used to access OCR when configured on ASM managed storage.

Action: Contact Oracle Support Services.

PROC-00044: Error in network address and interface operations

Cause: An error occurred in the network address and interface operations layer while performing a cluster registry operation.

Action: Contact Oracle Support Services.

PROC-00045: Error in the Oracle Clusterware API layer

Cause: An error occurred in the Oracle Clusterware API layer.

Action: Contact Oracle Support Services.

PROC-00046: Cannot perform cluster registry operation because the batch is empty.

Cause: An attempt was made to execute the batch without any operations in it.

Action: This is an internal error. Contact Oracle Support Services.

PROC-00047: Cannot proceed while the Oracle Cluster Registry format upgrade is in progress.

Cause: An Oracle Cluster Registry operation was requested, but found that an Oracle Cluster Registry format upgrade was in progress.

Action: Retry the operation after the format upgrade completes.

PROC-00048: Cannot perform the Oracle Cluster Registry operation due to a transient error.

Cause: A transient error occurred while performing the requested Oracle Cluster Registry operation. The operation was aborted without retrying, as requested by the client.

Action: Retry the operation.

PROC-00049: The specified Oracle Cluster Registry backup location is inaccessible on nodes string.

Cause: The Oracle Cluster Registry backup location did not exist, was not mounted correctly or did not have the required permissions on the above listed nodes.

Action: Ensure that the backup location exists with appropriate permissions on the above listed nodes. If the backup location is an ASM disk group, the disk group must be mounted correctly; also check the entries in the ASM alert log file for more details.

PROC-00050: The Oracle Cluster Registry location to be added is inaccessible on nodes string.

Cause: The Oracle Cluster Registry location to be added did not exist, was not mounted correctly or did not have the required permissions on the above listed nodes.

Action: Ensure that the location exists with appropriate permissions on the above listed nodes. If the location is an ASM disk group, the disk group must be mounted correctly; also check the entries in the ASM alert log file for more details.

PROC-00101: Operating System error \[string\]

Cause: An error occurred in the operating system layer while performing a cluster registry operation

Action: Contact Oracle Support Services.

PROC-00102: Cluster services error \[string\]

Cause: An error occurred in the cluster services layer while performing a cluster registry operation.

Action: Contact Oracle Support Services.

PROC-00103: Messaging error \[string\]

Cause: An error occurred in the messaging layer while performing a cluster registry operation.

Action: Contact Oracle Support Services.

PROC-00104: Authentication error \[string\]

Cause: An error occurred in the authentication layer while performing a cluster registry operation.

Action: Contact Oracle Support Services.

PROC-00105: Logging error

Cause: An error occurred in the logging layer while while performing a cluster registry operation.

Action: Contact Oracle Support Services.

PROC-00106: Unidentified component error

Cause: An error occurred in an unidentified layer while performing a cluster registry operation.

Action: Contact Oracle Support Services.

PROC-00107: Storage layer error \[string\]

Cause: An error occurred in the storage layer while performing a cluster registry operation.

Action: Contact Oracle Support Services.

PROC-00108: ASM error \[string\]

Cause: An error occurred in the asm layer while performing a cluster registry operation.

Action: Contact Oracle Support Services.

PROC-00109: Network address and interface operations error

Cause: An error occurred in the network address and interface operations layer while performing a cluster registry operation.

Action: Contact Oracle Support Services.