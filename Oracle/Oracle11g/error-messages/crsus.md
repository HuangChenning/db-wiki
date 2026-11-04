---
title: CRS-00001 to CRS-10250
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/crsus.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 64 CRS-00001 to CRS-10250

CRS-00001: Message ID string-number not found.

Cause: The messsage for the given message id is not found in any language.

Action: Make sure the product is setup correctly on the system.

CRS-00002: string:Internal list corruption. trace file: "string"

Cause: An internal error was detected during trace file flush processing.

Action: Contact Oracle Support Services.

CRS-00003: An error was encountered while attempting to open file "string". Additional diagnostics: string

Cause: An error was encountered while attempting to open the specified file.

Action: Examine the additional diagnostics, if available, and attempt to correct any file system environmental problems if indicated. Otherwise, contact Oracle Support Services.

CRS-00004: logging terminated for the process. log file: "string"

Cause: One or more file system errors were encountered which caused logging to be terminated for this process.

Action: Examine preceding Alert log messages for details on the error or errors that occurred. Restart the process to reenable logging.

CRS-00005: log file "string" deleted after close failure

Cause: This message is informational. An attempt to close the specified log file failed. The contents of the log file after a close error are undefined. The log file has been successfully deleted. Log data are lost.

Action: None

CRS-00006: file rotation processing continues for file: "string"

Cause: This message is informational and indicates only that a preceding error was not sufficiently severe to terminate file rotation which might otherwise be the case.

Action: None

CRS-00007: failed to open new log file "string\\

Cause: The file system encountered an error while attempting to open the specified file during log file rotation. Log data are lost.

Action: Review the preceding Alert log message CRS-0011 and attempt to resolve any file system environmental problems indicated. Otherwise, contact Oracle Support Services.

CRS-00008: opened new file "string" after close failure

Cause: This message is informational. Log data are lost.

Action: None

CRS-00009: log file "string" reopened

Cause: An error was encountered during rotation processing so that log file rotation could not proceed. The original log file, which had been closed, was successfully reopened.

Action: Review Alert log messages that precede this message that identify the file system error or errors encountered. If the additional diagnostic data in a preceding alert log message indicate a file system environmental problem, attempt to correct it. Otherwise contact Oracle Support Services.

CRS-00011: An error occurred while attempting to close file "string" during log file rotation. Additional diagnostics: string

Cause: An error was encountered when attempting to close the specified file.

Action: Examine the additional diagnostics, if any, and attempt to correct any file system environmental problems if indicated. Otherwise, contact Oracle Support Services.

CRS-00012: An error occurred while attempting to rename file "string" to "string" during log file rotation. Additional diagnostics: string

Cause: An error was encountered when attempting to rename the source file to the destination file.

Action: Examine the additional diagnostics, if any, and attempt to correct any file system environmental problems if indicated. Otherwise, contact Oracle Support Services.

CRS-00013: An error occurred while attempting to check for the existence of file "string" during log file rotation. Additional diagnostics: string

Cause: An error was encountered while attempting to determine if the specified file existed.

Action: Examine the additional diagnostics, if any, and attempt to correct any file system environmental problems if indicated. Otherwise, contact Oracle Support Services.

CRS-00014: An error occurred while attempting to delete file "string" during log file rotation. Additional diagnostics: string

Cause: An error was encountered while attempting to delete the specified file.

Action: Examine the additional diagnostics, if any, and attempt to correct any file system environmental problems if indicated. Otherwise, contact Oracle Support Services.

CRS-00015: An error occurred while attempting to flush file "string" during log file rotation. Additional diagnostics: string

Cause: An error was encountered while an attempting to flush the specified file.

Action: Examine the additional diagnostics, if any, and attempt to correct any file system environmental problems if indicated. Otherwise, contact Oracle Support Services.

CRS-00016: An error was encountered while attempting to free the file name object for file "string" during log file rotation. Additional diagnostics: string

Cause: An error was encountered while attempting to free the file name object for the specified file.

Action: Examine the additional diagnostics, if any, and attempt to correct any file system environmental problems if indicated. Otherwise, contact Oracle Support Services.

CRS-00017: An error occurred while attempting to create a file name object for file "string" during log file rotation. Additional diagnostics: string

Cause: An error was encountered while attempting to create a file name object for the specified file.

Action: Examine the additional diagnostics, if any, and attempt to correct any file system environmental problems if indicated. Otherwise, contact Oracle Support Services.

CRS-00018: An error occurred while attempting to reopen file "string" during log file rotation. Additional diagnostics: string

Cause: An error was encountered while attempting to reopen the specified file.

Action: Examine the additional diagnostics, if any, and attempt to correct any file system environmental problems if indicated. Otherwise, contact Oracle Support Services.

CRS-00019: file rotation terminated. log file: "string"

Cause: One or more file system errors were encountered which caused log file rotation to be terminated for the process. Although log file rotation has been terminated, logging continues.

Action: Review Alert log messages that precede this alert log message that identify the file system error or errors encountered. If the additional diagnostic data in a preceding alert log message indicate a file system environmental problem, attempt to correct it. Otherwise contact Oracle Support Services. To re-enable file rotation the process must be restarted.

CRS-00020: An error occurred while attempting to create a file name object for file "string" during file open processing. Additional diagnostics: string

Cause: An error was encountered while attempting to create a file name object for the specified file.

Action: Examine the additional diagnostics, if any, and attempt to correct any file system environmental problems if indicated. Otherwise, contact Oracle Support Services.

CRS-00021: An error occurred while attempting to check for the existence of file "string" during file open processing. Additional diagnostics: string

Cause: An error was encountered while attempting to determine if the specified file existed.

Action: Examine the additional diagnostics, if any, and attempt to correct any file system environmental problems if indicated. Otherwise, contact Oracle Support Services.

CRS-00022: An error occurred while attempting to change access permissions and privileges for file "string" during file open processing. Additional diagnostics: string

Cause: An error was encountered while attempting to change access permissions and privileges for the specified file.

Action: Examine the additional diagnostics, if any, and attempt to correct any file system environmental problems if indicated. Otherwise, contact Oracle Support Services.

CRS-00023: An error occurred while attempting to create default permissions for file "string" during file open processing. Additional diagnostics: string

Cause: An error was encountered while attempting to create default file permissions for the specified file.

Action: Examine the additional diagnostics, if any, and attempt to correct any file system environmental problems if indicated. Otherwise, contact Oracle Support Services.

CRS-00024: An error occurred while attempting to create a file name object for file "string" during file open processing. Additional diagnostics: string

Cause: An error was encountered while attempting to create a file name object for the specified file.

Action: Examine the additional diagnostics, if any, and attempt to correct any file system environmental problems if indicated. Otherwise, contact Oracle Support Services.

CRS-00025: An error occurred while attempting to create a file object for file "string" during file open processing. Additional diagnostics: string

Cause: An error was encountered while attempting to create a file object for the specified file.

Action: Examine the additional diagnostics, if any, and attempt to correct any file system environmental problems if indicated. Otherwise, contact Oracle Support Services.

CRS-00026: failed to create one or more file name objects to rename "string" to "string" during file rotation processing

Cause: An error was encountered while attempting to create one of more file name objects for the specified files.

Action: Contact Oracle Support Services.

CRS-00027: An error occurred while attempting to determine the size of file "string" during file open processing. Additional diagnostics: string

Cause: An error was encountered while attempting to determine the size of the specified file.

Action: Examine the additional diagnostics, if any, and attempt to correct any file system environmental problems if indicated. Otherwise, contact Oracle Support Services.

CRS-00036: An error was encountered while attempting to open log file "string".

Cause: An error was encountered while attempting to open the specified file. Logging is disabled for the process.

Action: Review the preceding Alert log messages and attempt to resolve any file system environmental problems indicated. Otherwise, contact Oracle Support Services

CRS-00184: Cannot communicate with the CRS daemon.

Cause: The CRS daemon on the local node is either not running or there was an internal communication error with the CRS daemon.

Action: Check if the CRS daemon process is running on the local node.

CRS-00210: Could not find resource 'string'.

Cause: An attempt was made to operate on a resource that is not registered.

Action: Ensure that the resource name is specified correctly using the command 'crsctl status resource'.

CRS-00211: Resource 'string' has already been registered.

Cause: An attempt was made to register a resource that is already registered.

Action: Ensure that the resource name is specified correctly and retry the command.

CRS-00213: Could not register resource 'string'.

Cause: There was an internal error while registering the resource.

Action: Check the CRS daemon log file.

CRS-00214: Could not unregister resource 'string'.

Cause: There was an internal error while unregistering the resource.

Action: Check the CRS daemon log file.

CRS-00215: Could not start resource 'string'.

Cause: There was an internal error while starting the resource.

Action: Check the CRS daemon log file.

CRS-00216: Could not stop resource 'string'.

Cause: There was an internal error while stopping the resource.

Action: Check the CRS daemon log file.

CRS-00217: Could not relocate resource 'string'.

Cause: There was an internal error while relocating the resource.

Action: Check the CRS daemon log file.

CRS-00218: Could not restart the resource 'string' on the original node.

Cause: There was an internal error while restarting the resource.

Action: Check the CRS daemon log file.

CRS-00219: Could not update resource 'string'.

Cause: There was an internal error while updating the resource.

Action: Check the CRS daemon log file.

CRS-00220: Resource 'string' has invalid resource profile.

Cause: Invalid attributes in the resource profile.

Action: Run the command 'crsctl status type' to identify the invalid attributes. Modify these attributes using the command 'crsctl modify type'.

CRS-00221: Resource 'string''s action script cannot be found.

Cause: The action script has been deleted from the file system.

Action: Run 'crsctl status resource -p' to determine the action script location, and check for its existence.

CRS-00223: Resource 'string' has placement error.

Cause: There was no host available to on which failover/start the resource based on the Placement Policy for the resource.

Action: Check the target host for the resource and restart the resource using the 'crsctl start resource' command.

CRS-00230: Member 'string' is not in the cluster.

Cause: The hostname was not found in the cluster.

Action: Check the hostnames in the cluster.

CRS-00232: Cluster member is down. Cannot perform operation.

Cause: The node on which CRS is attempting to start the resource is down.

Action: Start the node and retry the operation.

CRS-00233: Resource or relatives are currently involved with another operation.

Cause: Another CRS daemon was operating on the same resource.

Action: Wait for a minute and try the command or operation again.

CRS-00253: CRS configuration error, the CRS default directory is not set in Oracle Cluster Registry.

Cause: The Oracle Cluster Registry key which contains the user default CRS key is not initialised.

Action: Check the CRS configuration. If necessary reinstall CRS.

CRS-00254: authorization failure

Cause: The user permissions were insufficient to operate on the resource.

Action: Check the permissions associated with the resource using 'crsctl getperm resource' and set the appropriate user permissions using 'crsctl setperm resource'.

CRS-00255: CRSD is not running in privileged mode. Insufficient permissions to run this command.

Cause: The CRS daemon was not running as the privileged user.

Action: Check if the CRS daemon is running as root (Unix) or Administrator (Windows).

CRS-00256: Username conflicts with the owner of the resource.

Cause: An attempt was made to give separate user level permissions for the owner of the resource.

Action: Check the owner of the resource and the user being given permissions.

CRS-00257: Groupname conflicts with the primary group of the resource.

Cause: An attempt was made to give separate group level permissions for the primary group of the resource.

Action: Check the primary group of the resource and the group being given permissions.

CRS-00258: Invalid ACL string format.

Cause: An invalid permission string (ACL) was supplied.

Action: Check the syntax of the permission string (ACL).

CRS-00259: Owner of the resource does not belong to the group.

Cause: The owner of the resource does not belong to the expected group.

Action: If this resource is owned by the root user, check if the root user belongs to the dba group.

CRS-00271: CRSD shutdown is already in progress.

Cause: crsctl stop command is issued before waiting for a prior stop command to finish.

Action: Wait for the currently running shutdown command to complete before issuing subsequent command.

CRS-00272: This command remains for backward compatibility only

Cause: A deprecated command was issued.

Action: For all new use cases, please use the replacement.

CRS-00273: This command is deprecated and has been replaced by 'string'

Cause: A deprecated command was issued.

Action: For all new use cases, please use the replacement.

CRS-00274: This command is deprecated and its functionality incorporated into 'string'

Cause: A deprecated command was issued.

Action: For all new use cases, please use the replacement.

CRS-00402: Could not make safe directory('string')

Cause: Unable to create safe directory.

Action: Check if you have proper permissions and sufficient space on the disk to create the directory.

CRS-00403: Could not change working directory to safe directory('string')

Cause: Unable to change directory to safe directory.

Action: Please check if safe directory exists and if you have proper permissions.

CRS-00406: Could not create lock directory ('string')

Cause: Unable to create lock directory.

Action: Check if you have proper permissions and sufficient space on the disk to create the directory.

CRS-00407: Another CRSD may be running, could not obtain lock file 'string'.

Cause: Unable to obtain lock file as another CRSD may be running.

Action: Stop the existing CRSD before attempting to start CRSD again.

CRS-00413: Could not initialize the Cluster Synchronization Services context

Cause: Unable to communicate with the cluster services.

Action: Verify that the Cluster Synchronization Services Daemon is properly configured and is running.

CRS-00414: Could not establish Event Manager connection

Cause: Unable to communicate with Event Manager daemon.

Action: Run the 'crsctl check evmd' command to determine whether Event Manager daemon is properly configured and is running.

CRS-00451: CRS configuration error, unable to initialize Oracle Cluster Registry.

Cause: The Oracle Cluster Registry that contains information about the CRS configuration is unavailable.

Action: Check the OCR configuration using the ocrcheck utility and resolve any issues it reports. If the problem persists, contact Oracle Support Services.

CRS-00452: CRS configuration error, unable to find CRSD Connection Information in Oracle Cluster Registry.

Cause: The Oracle Cluster Registry key which contains the user default CRSD connection is not initialized.

Action: Check the OCR configuration using the ocrcheck utility and resolve any issues it reports. If the problem persists, contact Oracle Support Services.

CRS-00453: CRS configuration error, unable to find Instance Information in Oracle Cluster Registry.

Cause: The Oracle Cluster Registry key which contains the Instance's information is not initialized.

Action: Check the OCR configuration using the ocrcheck utility and resolve any issues it reports. If the problem persists, contact Oracle Support Services.

CRS-00471: Node number is not found

Cause: Cluster Synchronization Services is unable to retrieve the node name.

Action: Verify your cluster installation, including any vendor cluster ware. If necessary reinstall the cluster.

CRS-00472: Node name is not found

Cause: Cluster Services is unable to retrieve the node name.

Action: Verify your cluster installation, including any vendor cluster ware. If necessary reinstall the cluster.

CRS-00700: Oracle High Availability Service aborted due to failure to allocate memory. Details at string in string.

Cause: Memory allocation failed.

Action: Restart Cluster Ready Service using 'crsctl stop crs -f' followed by 'crsctl start crs'. If the problem persists, contact Oracle Support Services.

CRS-00701: Oracle High Availability Service aborted due to failure to obtain identity of the running process. Details at string in string.

Cause: Failed to retrieve user id.

Action: Check <crs\_home> owner and restart Cluster Ready Service using 'crsctl stop crs -f' followed by 'crsctl start crs'. If the problem persists, contact Oracle Support Services.

CRS-00702: Oracle High Availability Service aborted due to failure to run as privileged user. Details at string in string.

Cause: Oracle High Availability Service was not running as privileged user.

Action: On Unix, restart Cluster Ready Service as privileged user using 'crsctl stop crs -f' followed by 'crsctl start crs'. On Windows, check the privileges of the Oracle High Availability Service and restart Cluster Ready Service using 'crsctl stop crs -f' followed by 'crsctl start crs' If the problem persists, contact Oracle Support Services.

CRS-00703: Oracle High Availability Service aborted due to failure to initialize the communication context. Details at string in string.

Cause: The network layer initialization failed.

Action: Restart Cluster Ready Service using 'crsctl stop crs -f' followed by 'crsctl start crs'. If the problem persists, contact Oracle Support Services.

CRS-00704: Oracle High Availability Service aborted due to Oracle Local Registry error \[string\]. Details at string in string.

Cause: Oracle Local Registry aborted with an error. Look at the associated error message to determine the underlying issue.

Action: Solve the underlying issue and restart Cluster Ready Service using 'crsctl stop crs -f' followed by 'crsctl start crs'. If the problem persists, contact Oracle Support Services.

CRS-00708: Oracle High Availability Service aborted due to failure to retrieve ORA\_CRS\_HOME environment variable. Details at string in string.

Cause: An environment variable required by Oracle High Availability Service failed to be set at initialization.

Action: Run 'rootcrs.pl -unlock' followed by 'rootcrs.pl -patch' and restart Cluster Ready Service using 'crsctl stop crs -f' followed by 'crsctl start crs'. If the problem persists, contact Oracle Support Services.

CRS-00709: Oracle High Availability Service aborted due to failure to initialize ORA\_CRS\_HOME path. Details at string in string.

Cause: Oracle High Availability Service ORA\_CRS\_HOME path could not be initialized.

Action: Check for execute permissions on the Grid Infrastructure home or <crs\_home> and restart Cluster Ready Service using 'crsctl stop crs -f' followed by 'crsctl start crs'. If the problem persists, contact Oracle Support Services.

CRS-00712: Oracle High Availability Service aborted due to failure to initialize the network layer with error \[number\]. Details at string in string.

Cause: The network layer initialization failed.

Action: Restart Cluster Ready Service using 'crsctl stop crs -f' followed by 'crsctl start crs'. If the problem persists, contact Oracle Support Services.

CRS-00713: An error occurred initializing the Reboot Advisory Monitor: error code \[number\]. Details at string in string.

Cause: An error occurred initializing the Reboot Advisory Monitor component of Oracle High Availability Service. This error is not fatal; Oracle High Availability Service processing continues.

Action: Examine the Clusterware alert log for messages providing details of the error. If the error is correctable, do so and then restart Cluster Ready Service using 'crsctl stop crs -f' followed by 'crsctl start crs'. If no messages are found or you do not understand how to correct the problem, contact Oracle Support Services.

CRS-00715: Oracle High Availability Service has timed out waiting for init.ohasd to be started.

Cause: The Oracle High Availability Service requires that initd start init.ohasd to successfully initialize.

Action: 1. Check the run level to ensure that you are in the correct runlevel using cluvfy ("cluvfy stage -pre crsinst -n \<nodelist>"); 2. If the run level is correct, diagnose the reason for init.d not starting init.ohasd.

CRS-00800: Cluster Ready Service aborted due to failure to allocate memory. Details at string in string.

Cause: Memory allocation failed.

Action: Restart Cluster Ready Service using 'crsctl stop crs -f' followed by 'crsctl start crs'. If the problem persists, contact Oracle Support Services.

CRS-00801: Cluster Ready Service aborted due to failure to obtain identity of the running process. Details at string in string.

Cause: Failed to retrieve user id.

Action: Check <crs\_home> owner and restart Cluster Ready Service using 'crsctl stop crs -f' followed by 'crsctl start crs'. If the problem persists, contact Oracle Support Services.

CRS-00802: Cluster Ready Service aborted due to failure to run as privileged user. Details at string in string.

Cause: Cluster Ready Service was not running as privileged user.

Action: On Unix, restart Cluster Ready Service as privileged user using 'crsctl stop crs -f' followed by 'crsctl start crs'. On Windows, check the privileges of the Oracle High Availability Service and restart Cluster Ready Service using 'crsctl stop crs -f' followed by 'crsctl start crs' If the problem persists, contact Oracle Support Services.

CRS-00803: Cluster Ready Service aborted due to failure to initialize the communication context. Details at string in string.

Cause: The network layer initialization failed.

Action: Restart Cluster Ready Service using 'crsctl stop crs -f' followed by 'crsctl start crs'. If the problem persists, contact Oracle Support Services.

CRS-00804: Cluster Ready Service aborted due to Oracle Cluster Registry error \[string\]. Details at string in string.

Cause: Oracle Cluster Registry aborted with an error. Look at the associated error message to determine the underlying issue.

Action: Solve the underlying issue and restart Cluster Ready Service using 'crsctl stop crs -f' followed by 'crsctl start crs'. If the problem persists, contact Oracle Support Services.

CRS-00805: Cluster Ready Service aborted due to failure to communicate with Cluster Synchronization Service with error \[number\]. Details at string in string.

Cause: The Cluster Synchronization Service is unreachable.

Action: Restart Cluster Ready Service using 'crsctl stop crs -f' followed by 'crsctl start crs'. If the problem persists, contact Oracle Support Services.

CRS-00806: Cluster Ready Service aborted due to failure to retrieve the local node name. Details at string in string.

Cause: The Cluster Synchronization Service node name is not accessible.

Action: Restart Cluster Ready Service using 'crsctl stop crs -f' followed by 'crsctl start crs'. If the problem persists, contact Oracle Support Services.

CRS-00807: Cluster Ready Service aborted due to failure to check version compatibility. Details at string in string.

Cause: Oracle Cluster Registry content is not compatible with this version of Cluster Ready Service.

Action: Start the correct version of Cluster Ready Service. If the problem persists, contact Oracle Support Services.

CRS-00808: Cluster Ready Service aborted due to failure to retrieve ORA\_CRS\_HOME environment variable. Details at string in string.

Cause: An environment variable required by Cluster Ready Service failed to be set at initialization.

Action: Run 'rootcrs.pl -unlock' followed by 'rootcrs.pl -patch' and restart Cluster Ready Service using 'crsctl stop crs -f' followed by 'crsctl start crs'. If the problem persists, contact Oracle Support Services.

CRS-00809: Cluster Ready Service aborted due to failure to initialize ORA\_CRS\_HOME path. Details at string in string.

Cause: Cluster Ready Service ORA\_CRS\_HOME path could not be initialized.

Action: Check for execute permissions on the Grid Infrastructure home or <crs\_home> and restart Cluster Ready Service using 'crsctl stop crs -f' followed by 'crsctl start crs'. If the problem persists, contact Oracle Support Services.

CRS-00810: Cluster Ready Service aborted due to failure to communicate with Event Management Service with error \[number\]. Details at string in string.

Cause: The Event Management Service is unreachable.

Action: Restart Cluster Ready Service using 'crsctl stop crs -f' followed by 'crsctl start crs'. If the problem persists, contact Oracle Support Services.

CRS-00811: Cluster Ready Service aborted due to failure to build dependency graph. Details at string in string.

Cause: There exists inconsistencies in the resources dependencies.

Action: Check the resources dependencies and restart Cluster Ready Service using 'crsctl stop crs -f' followed by 'crsctl start crs'. If the problem persists, contact Oracle Support Services.

CRS-00812: Cluster Ready Service aborted due to failure to initialize the network layer with error \[number\]. Details at string in string.

Cause: The network layer initialization failed.

Action: Restart Cluster Ready Service using 'crsctl stop crs -f' followed by 'crsctl start crs'. If the problem persists, contact Oracle Support Services.

CRS-00813: Cluster Ready Service aborted due to failure to initialize the network layer with error \[string\]. Details at string in string.

Cause: The network layer initialization failed.

Action: Restart Cluster Ready Service using 'crsctl stop crs -f' followed by 'crsctl start crs'. If the problem persists, contact Oracle Support Services.

CRS-00814: Cluster Ready Service aborted due to failure to start thread with error \[number\]. Details at string in string.

Cause: Thread creation failed.

Action: Restart Cluster Ready Service using 'crsctl stop crs -f' followed by 'crsctl start crs'. If the problem persists, contact Oracle Support Services.

CRS-01001: The OCR was formatted using version number.

Cause: Successfully formatted the OCR location(s).

Action: None

CRS-01002: The OCR was restored from file string.

Cause: The OCR was successfully restored from a backup file as requested by the user.

Action: None

CRS-01003: The OCR format was downgraded to version number.

Cause: The OCR was successfully downgraded to an earlier block format as requested by the user.

Action: None

CRS-01004: The OCR was imported from string.

Cause: Successfully imported the OCR contents from a file as requested by the user.

Action: None

CRS-01005: The Oracle Clusterware upgrade was completed. Version has changed from \[number, string\] to \[number, string\]. Details in string.

Cause: The Oracle Clusterware was successfully upgraded to a version.

Action: None

CRS-01006: The OCR location string is inaccessible. Details in string.

Cause: An error occurred while accessing the OCR.

Action: Use the ocrcheck command to validate the accessibility of the device and its block integrity. Check that the OCR location in question has the correct permissions. Determine whether this behavior is limited to one node or whether it occurs across all of the nodes in the cluster. Use the ocrconfig command with the -replace option to replace the OCR location.

CRS-01007: The OCR/OCR mirror location was replaced by string.

Cause: The OCR location was successfully replaced as requested by the user.

Action: None

CRS-01008: Node string is not responding to OCR requests. Details in string.

Cause: Error in communicating to the OCR server on a peer node. This OCR did not receive a notification regarding its peer's death within the specified time.

Action: Contact Oracle Customer Support.

CRS-01009: The OCR configuration is invalid. Details in string.

Cause: The OCR configuration on this node does not match the OCR configuration on the other nodes in the cluster.

Action: Determine the OCR configuration on the other nodes in the cluster on which Oracle Clusterware is running by using the ocrcheck command. Run the ocrconfig command with the -repair option to correct the OCR configuration on this node.

CRS-01010: The OCR mirror location string was removed.

Cause: The OCR location was successfully removed as requested by the user.

Action: None

CRS-01011: OCR cannot determine that the OCR content contains the latest updates. Details in string.

Cause: The OCR could not be started. The OCR location configured on this node does not have the necessary votes and might not have the latest updates.

Action: Ensure that the other nodes in the cluster have the same OCR location configured. If the configuration on the other nodes in the cluster does not match, then run the ocrconfig command with the -repair option to correct the configuration on this node. If the configurations on all of the nodes match, use the ocrdump command to ensure that the existing OCR location has the latest updates. Run the ocrconfig command with the -overwrite option to correct the problem. If the se procedures do not correct the problem, then contact Oracle Customer Support.

CRS-01012: The OCR service started on node string.

Cause: The OCR was successfully started.

Action: None

CRS-01013: The OCR location in an ASM disk group is inaccessible. Details in string.

Cause: An error occurred while accessing the OCR file in an ASM disk group.

Action: Use the 'asmcmd' command to verify if the ASM instance is active. If the ASM instance aborted, it will be restarted automatically. Use 'ocrcheck -config' to discover the OCR locations configured, and verify using 'asmcmd' that the disk group in question is mounted. Mount the disk group if it is not mounted. Validate if the behavior is limited to one node or whether it occurs across all of the nodes in the cluster. If nothing works, use the 'ocrconfig' command with the '-replace' or '-delete' option to replace or remove the OCR location.

CRS-01014: Failed to import Oracle Cluster Registry from file string

Cause: Unable to read data from the import file and import to the cluster registry

Action: Check availability of the cluster registry and the details of the failure from the log file

CRS-01015: A request to terminate the Cluster Ready Service on node string completed successfully. Details at string in string.

Cause: The Cluster Ready Service on the above listed node did not respond to an earlier request within the specified time. The Cluster Ready Service will be terminated to prevent any possible cluster hangs.

Action: Check the Oracle Clusterware alert log on the listed node for any problems. Check for any reason that might not allow the Cluster Ready Service to run optimally on the listed node. Verify network accessibility to the listed node from other nodes in the cluster. If the problem persists, contact Oracle Support Services.

CRS-01016: The Cluster Ready Service on this node terminated because it detected a failure while upgrading the Oracle Cluster Registry format. Details at string in string.

Cause: The Cluster Ready Service on the node coordinating the upgrade of the Oracle Cluster Registry format terminated.

Action: The Oracle Cluster Registry format upgrade will be completed by another node in the cluster. The Cluster Ready Service on the node listed above will be automatically restarted, and will be able to function as soon as the upgrade completes. If the problem persists, contact Oracle Support Services.

CRS-01017: The Cluster Ready Service on this node terminated because it was unable to open the import file while upgrading the Oracle Cluster Registry format. Details at string in string.

Cause: There was a failure accessing the import file on this node. The Cluster Ready Service on this node may not have been active during the Oracle Cluster Registry format upgrade.

Action: The Oracle Cluster Registry format upgrade will be completed by another node in the cluster. The Cluster Ready Service on this node will be automatically restarted, and will be able to function as soon as the upgrade completes. If the problem persists, contact Oracle Support Services.

CRS-01018: The Cluster Ready Service on this node terminated because the OCR configuration on this node is invalid. Details at string in string.

Cause: The OCR configuration on this node did not match with the OCR configuration on the other nodes in the cluster.

Action: The OCR configuration on this node is automatically repaired and the Cluster Ready Service will be automatically restarted. If the problem persists, contact Oracle Support Services.

CRS-01019: The OCR Service exited on host string. Details in string

Cause: The OCR Service exited due to an internal error.

Action: Determine whether the service has restarted. Collect Clusterware alert log and the CRSD log indicated in the message and contact Oracle Support Services.

CRS-01020: The Oracle Cluster Registry has invalid contents. Details at string in string.

Cause: Some of the Oracle Cluster Registry contents were invalid.

Action: Check the log file indicated in the message for more details. Use the 'ocrcheck' command to detect errors, and the 'ocrdump' command to review the registry contents. If problems exist, the registry may need to be recovered or restored. If the problem persists, contact Oracle Support Services.

CRS-01021: The Oracle Cluster Registry backup file in an ASM disk group is inaccessible. Details in string.

Cause: Oracle Cluster Registry backup location did not exist, wasn't mounted correctly, or did not have the required permissions.

Action: Ensure that the backup location exists, that it is mounted correctly and visible to all nodes in the cluster, and that its permissions are correct. Check the entries in the ASM alert log file for more details.

CRS-01022: The Oracle Clusterware was forcibly upgraded without upgrading nodes string. Version has changed from \[number, string\] to \[number, string\]. Details in string.

Cause: Oracle Clusterware was forcibly upgraded when the above listed nodes were not upgraded.

Action: Delete the above listed nodes using the procedure in the Clusterware Administration and Deployment Guide. If the nodes later become accessible, they can be added back into the cluster.

CRS-01025: The Oracle Clusterware was upgraded to \[string\] on all nodes, but the cluster operating version is still \[string\]. Details in \[string\].

Cause: The cluster upgrade did not complete because the root upgrade script failed on the last node, the root upgrade script was interrupted by the user, or the cluster upgrade is ongoing.

Action: Check the Oracle Clusterware alert log on all nodes for any problems. Rerun the root upgrade script on the last node to completion, and ensure that the cluster operating version has changed using the 'crsctl query crs activeversion' command. If the problem persists, run diagcollection.pl and contact Oracle Support Services.

CRS-01110: The Oracle Clusterware upgrade is in unknown state \[number\].

Cause: There was an internal error upgrading the Oracle Clusterware.

Action: Retry the 'crsctl set crs activeversion' command. If the problem persists, contact Oracle Support Services.

CRS-01111: Error upgrading the Oracle Clusterware. Details \[string\].

Cause: There was an internal error upgrading the Oracle Clusterware.

Action: Verify using the 'crsctl check crs' command that the CRS Service running. Retry the 'crsctl set crs activeversion' command. If the problem persists, contact Oracle Support Services.

CRS-01112: Failed to set the Oracle Clusterware operating version string

Cause: There was an internal error upgrading the Oracle Clusterware.

Action: Retry the 'crsctl set crs activeversion' command. If the problem persists, contact Oracle Support Services.

CRS-01114: Invalid active version \[string\] passed

Cause: An invalid active version was passed.

Action: Use the 'crsctl query crs softwareversion' command to retrieve a valid active version.

CRS-01115: Oracle Clusterware has already been upgraded.

Cause: Oracle Clusterware is already running in highest possible operating version.

Action: None

CRS-01116: Oracle Clusterware upgrade has been aborted.

Cause: One of the Oracle Clusterware components have failed to upgrade within the expected time.

Action: Check the Oracle Clusterware alert log and the CRS daemon log for additional information.

CRS-01117: Error upgrading the Oracle Clusterware.

Cause: An attempt was made to change the Oracle Clusterware operating version before all nodes were upgraded.

Action: Run root.sh script on all nodes in the cluster. If the problem persists, contact Oracle Support Services.

CRS-01119: Unable to complete Oracle Clusterware upgrade while nodes string have not yet upgraded

Cause: An attempt was made to change the Oracle Clusterware operating version before all nodes were upgraded.

Action: Run root.sh script and upgrade all nodes in the cluster before retrying the 'crsctl set crs activeversion' command.

CRS-01121: Oracle Clusterware was forcibly upgraded without upgrading nodes string.

Cause: Oracle Clusterware was forcibly upgraded when the above listed nodes were not upgraded.

Action: Delete the above listed nodes using the procedure in the Clusterware Administration and Deployment Guide. If the nodes later become accessible, they can be added back into the cluster.

CRS-01201: CRSD started on node string.

Cause: CRSD has started, possibly due to a CRS start, or a node reboot or a CRSD restart.

Action: None Required. You can run the command 'crsctl check crsd' to validate the health of the CRSD.

CRS-01202: CRSD aborted on node string. Error \[string\]. Details in string.

Cause: Fatal Internal Error. Check the CRSD log file to determine the cause.

Action: Determine whether the CRSD gets auto-started.

CRS-01203: Failover failed for the CRS resource string. Details in string.

Cause: Failover failed due to an internal error. Examine the contents of the CRSD log file to determine the cause.

Action: None

CRS-01204: Recovering CRS resources for node string.

Cause: CRS resources are being recovered, possibly because the cluster node is starting up online.

Action: Check the status of the resources using the 'crsctl status resource' command.

CRS-01205: Auto-start failed for the CRS resource string. Details in string.

Cause: This message comes up when the auto-start for the resource has failed during a reboot of the cluster node.

Action: Start the resources using the 'crsctl start resource' command.

CRS-01206: Resource string is in the UNKNOWN state. Make sure the resource is completely stopped, then use the 'crsctl stop -f' command.

Cause: Resource went into an unknown state because the check or the stop

Action: Make sure the resource is completely stopped, then use the 'crsctl stop -f' command.

CRS-01207: There are no more restart attempts left for resource string. Restart the resource manually using the crsctl command.

Cause: The Oracle Clusterware is no longer attempting to restart the resource because the resource has failed and the Oracle Clusterware has exhausted the maximum number of restart attempts.

Action: Use the 'crsctl start' command to restart the resource manually.

CRS-01208: Cluster Ready Service terminating, unable to start successfully. Details at string in string.

Cause: Cluster Ready Service could not initialize successfully.

Action: Restart Cluster Ready Service using the command 'crsctl start clusterware'. If the problem persists, contact Oracle Support Services.

CRS-01209: Cluster Ready Service terminating, failed to register with group 'string'. Details at string in string.

Cause: Cluster Ready Service could not initialize successfully.

Action: Restart Cluster Ready Service using the command 'crsctl start clusterware'. If the problem persists, contact Oracle Support Services.

CRS-01210: Cluster Ready Service failed to update group data. Details at string in string.

Cause: Cluster Ready Service failed to update the group private data with new master.

Action: Restart Cluster Ready Service using the command 'crsctl start clusterware'. If the problem persists, contact Oracle Support Services.

CRS-01211: Cluster Ready Service noticed abnormal termination by Cluster Synchronization Service. Details at string in string.

Cause: Cluster Ready Service terminating due to abnormal termination of Cluster Synchronization Service layer.

Action: Contact Oracle Support Services.

CRS-01212: Cluster Ready Service received invalid update for group private data. Details at string in string.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CRS-01213: Cluster Ready Service failed to retrieve user information. Details at string in string.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CRS-01214: Cluster Ready Service failed to initialize OLR context. Details at string in string.

Cause: Cluster Ready Service unable to access local registry.

Action: Use the ocrcheck utility to detect errors in the OLR. If problems exist, the registry may need to be recovered or restored.

CRS-01215: Cluster Ready Service could not get the local node number. Details at string in string.

Cause: Cluster Ready Service could not retrieve the local node incarnation number.

Action: Contact Oracle Support Services.

CRS-01216: Cluster Ready Service could not determine node list. Details at string in string.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CRS-01217: Cluster Ready Service unable to get node name. Details at string in string.

Cause: Cluster Ready Service could not determine node name.

Action: Contact Oracle Support Services.

CRS-01218: Cluster Ready Service error during initialization. Details at string in string.

Cause: Cluster Ready Service could not initialize underlying layers successfully.

Action: Contact Oracle Support Services.

CRS-01219: Cluster Synchronization Service not available. Details at string in string.

Cause: Cluster Ready Service was unable to initialize access to CSS, which is required.

Action: Contact Oracle Support Services.

CRS-01220: Cluster Ready Service could not retrieve local node number. Details at string in string.

Cause: Cluster Ready Service could not retrieve node number for local node.

Action: Contact Oracle Support Services.

CRS-01221: Cluster Ready Service failed to retrieve local node name. Details at string in string.

Cause: Cluster Ready Service could not retrieve node name.

Action: Contact Oracle Support Services.

CRS-01222: Cluster Ready Service failed to retrieve maximum group size. Details at string in string.

Cause: Cluster Ready Service could not retrieve value for maximum group size.

Action: Contact Oracle Support Services.

CRS-01223: Cluster Ready Service error while reading cluster active version. Details at string in string.

Cause: Could not retrieve cluster active version.

Action: Contact Oracle Support Services.

CRS-01224: Server authentication exception encountered, exception text is 'string'. Details at string in string.

Cause: Cluster Ready Service encountered error while authenticating user.

Action: This is an internal error. Contact Oracle Support Services.

CRS-01225: Invalid identity exception encountered, exception text is 'string'. Details at string in string.

Cause: Cluster Ready Service could not verify user identity.

Action: This is an internal error. Contact Oracle Support Services.

CRS-01226: Failed to create message to send to policy engine. Details at string in string.

Cause: Cluster Ready Service encountered communication error.

Action: This is an internal error. Contact Oracle Support Services.

CRS-01227: Error during initialization of communication subsystem. Details at string in string.

Cause: Cluster Ready Service encountered communication error during initialization.

Action: This is an internal error. Contact Oracle Support Services.

CRS-01228: Error while setting up user interface server. Details at string in string.

Cause: Cluster Ready Service encountered communication error.

Action: This is an internal error. Contact Oracle Support Services.

CRS-01229: Error while listening for events. Details at string in string.

Cause: Cluster Ready Service encountered communication error.

Action: This is an internal error. Contact Oracle Support Services.

CRS-01231: Failed to open key 'string' in OCR. Details at string in string.

Cause: This is an internal error.

Action: This is an internal error. Contact Oracle Support Services.

CRS-01232: Could not get security attribute for system key 'string' in OCR. Details at string in string.

Cause: Encountered error while reading system key attributes in OCR.

Action: This is an internal error. Contact Oracle Support Services.

CRS-01233: Failed to initialize batch handler for OCR. Details at string in string.

Cause: Could not initialize batch handler for multiwrite in OCR.

Action: This is an internal error. Contact Oracle Support Services.

CRS-01234: Encountered error while setting key value for key 'string' in OCR. Details at string in string.

Cause: Encountered an error while executing a batch write in OCR.

Action: This is an internal error. Contact Oracle Support Services.

CRS-01235: Error while executing batch for multi writes in OCR. Details at string in string.

Cause: Encountered an error while executing a batch write in OCR.

Action: This is an internal error. Contact Oracle Support Services.

CRS-01236: Error enumerating subkeys for key 'string' in OCR. Details at string in string.

Cause: Encountered an error while reading subkey values in OCR.

Action: This is an internal error. Contact Oracle Support Services.

CRS-01237: Failed to retrieve the maximum value supported in OCR. Details at string in string.

Cause: Could not read the maximum value size from registry.

Action: This is an internal error. Contact Oracle Support Services.

CRS-01238: Failed to add a delete key operation for key 'string' to a batch in OCR. Details at string in string.

Cause: Encountered internal error while deleting key in OCR.

Action: This is an internal error. Contact Oracle Support Services.

CRS-01239: Cluster Ready Service aborted due to an unexpected error \[string\]. Details at string in string.

Cause: This is an unexpected error. Look at the associated error message to fix the underlying issue.

Action: If the problem persists, contact Oracle Support Services.

CRS-01301: Oracle High Availability Service started on node string.

Cause: Oracle High Availability Service has started, possibly due to a Clusterware start, or a node reboot.

Action: None Required.

CRS-01302: Oracle High Availability Service aborted on node string. Error \[string\]. Details in string.

Cause: Fatal Internal Error. Check the Oracle High Availability Service log file to determine the cause.

Action: Determine whether the Oracle High Availability Service gets auto-started.

CRS-01303: Failover failed for the OHAS resource string. Details in string.

Cause: Failover processing for the specified resource did not complete. Examine the contents of the Oracle High Availability Service log file to determine the cause.

Action: None

CRS-01304: Recovering OHAS resources for node string.

Cause: Oracle High Availability Service resources are being recovered, possibly because the cluster node is starting up online.

Action: Check the status of the resources using the crsctl command.

CRS-01305: Auto-start failed for the OHAS resource string. Details in string.

Cause: This message comes up when the auto-start for the resource has failed during a reboot of the cluster node.

Action: Start the resources using the 'crsctl start resource' command.

CRS-01306: Resource string is in an unknown state. Make sure the resource is completely stopped, then use the 'crsctl stop -f' command.

Cause: Resource went into an unknown state because the check or the stop

Action: Make sure the resource is completely stopped, then use the 'crsctl stop -f' command.

CRS-01307: There are no more restart attempts left for resource string. Restart the resource manually using the crsctl command.

Cause: The Oracle Clusterware is no longer attempting to restart the resource because the resource has failed and the Oracle Clusterware has exhausted the maximum number of restart attempts.

Action: Use the 'crsctl start resource' command to restart the resource manually.

CRS-01308: Oracle High Availability Service terminating, unable to start successfully. Details at string in string.

Cause: Oracle High Availability Service could not initialize successfully.

Action: Restart your clusterware installation. If the problem persists, contact Oracle Support Services.

CRS-01309: Oracle High Availability Service terminating, failed to register with group 'string'. Details at string in string.

Cause: Oracle High Availability Service could not initialize successfully.

Action: Restart your clusterware installation. If the problem persists, contact Oracle Support Services.

CRS-01310: Oracle High Availability Service failed to update group data. Details at string in string.

Cause: Oracle High Availability Service failed to update the group private data with new master.

Action: Restart your clusterware installation. If the problem persists, contact Oracle Support Services.

CRS-01311: Oracle High Availability Service noticed abnormal termination by Cluster Synchronization Service. Details at string in string.

Cause: Oracle High Availability Service terminating due to abnormal termination of Cluster Synchronization Service layer.

Action: Contact Oracle Support Services.

CRS-01312: Oracle High Availability Service received invalid update for group private data. Details at string in string.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CRS-01313: Oracle High Availability Service failed to retrieve user information. Details at string in string.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CRS-01314: Oracle High Availability Service failed to initialize OLR context. Details at string in string.

Cause: Oracle High Availability Service unable to access local registry.

Action: Use the ocrcheck utility to detect errors in the OLR. If problems exist, the registry may need to be recovered or restored.

CRS-01315: Oracle High Availability Service could not get the local node number. Details at string in string.

Cause: Oracle High Availability Service could not retrieve the local node incarnation number.

Action: Contact Oracle Support Services.

CRS-01316: Oracle High Availability Service could not determine node list. Details at string in string.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CRS-01317: Oracle High Availability Service unable to get node name. Details at string in string.

Cause: Oracle High Availability Service could not determine node name.

Action: Contact Oracle Support Services.

CRS-01318: Oracle High Availability Service error during initialization. Details at string in string.

Cause: Oracle High Availability Service could not initialize underlying layers successfully.

Action: Contact Oracle Support Services.

CRS-01319: Cluster Synchronization Service not available. Details at string in string.

Cause: Oracle High Availability Service was unable to initialize access to CSS, which is required.

Action: Contact Oracle Support Services.

CRS-01320: Oracle High Availability Service could not retrieve local node number. Details at string in string.

Cause: Oracle High Availability Service could not retrieve node number for local node.

Action: Contact Oracle Support Services.

CRS-01321: Oracle High Availability Service failed to retrieve local node name. Details at string in string.

Cause: Oracle High Availability Service could not retrieve node name.

Action: Contact Oracle Support Services.

CRS-01322: Oracle High Availability Service failed to retrieve maximum group size. Details at string in string.

Cause: Oracle High Availability Service could not retrieve value for maximum group size.

Action: Contact Oracle Support Services.

CRS-01323: Oracle High Availability Service error while reading cluster active version. Details at string in string.

Cause: Could not retrieve cluster active version.

Action: Contact Oracle Support Services.

CRS-01324: Server authentication exception encountered, exception text is 'string'. Details at string in string.

Cause: Oracle High Availability Service encountered error while authenticating user.

Action: This is an internal error. Contact Oracle Support Services.

CRS-01325: Invalid identity exception encountered, exception text is 'string'. Details at string in string.

Cause: Oracle High Availability Service could not verify user identity.

Action: This is an internal error. Contact Oracle Support Services.

CRS-01326: Failed to create message to send to policy engine. Details at string in string.

Cause: Oracle High Availability Service encountered communication error.

Action: This is an internal error. Contact Oracle Support Services.

CRS-01327: Error during initialization of communication subsystem. Details at string in string.

Cause: Oracle High Availability Service encountered communication error during initialization.

Action: This is an internal error. Contact Oracle Support Services.

CRS-01328: Error while setting up user interface server. Details at string in string.

Cause: Oracle High Availability Service encountered communication error.

Action: This is an internal error. Contact Oracle Support Services..

CRS-01329: Error while listening for events. Details at string in string.

Cause: Oracle High Availability Service encountered communication error.

Action: This is an internal error. Contact Oracle Support Services..

CRS-01330: Oracle High Availability Services aborted due to internal error.

Cause: Fatal Internal Error. Check the Oracle High Availability Service log file to determine the cause.

Action: Determine whether the Oracle High Availability Service gets auto-started.

CRS-01331: Failed to open key 'string' in OLR. Details at string in string.

Cause: This is an internal error.

Action: This is an internal error. Contact Oracle Support Services.

CRS-01332: Could not get security attribute for system key 'string' in OLR. Details at string in string.

Cause: Encountered error while reading system key attributes in OLR.

Action: This is an internal error. Contact Oracle Support Services.

CRS-01333: Failed to initialize batch handler for OLR. Details at string in string.

Cause: Could not initialize batch handler for multiwrite in OLR.

Action: This is an internal error. Contact Oracle Support Services.

CRS-01334: Encountered error while setting key value for key 'string' in OLR. Details at string in string.

Cause: Encountered an error while executing a batch write in OLR.

Action: This is an internal error. Contact Oracle Support Services.

CRS-01335: Error while executing batch for multi writes in OLR. Details at string in string.

Cause: Encountered an error while executing a batch write in OLR.

Action: This is an internal error. Contact Oracle Support Services.

CRS-01336: Error enumerating subkeys for key 'string' in OLR. Details at string in string.

Cause: Encountered an error while reading subkey values in OLR.

Action: This is an internal error. Contact Oracle Support Services.

CRS-01337: Failed to retrieve the maximum value supported in OLR. Details at string in string.

Cause: Could not read the maximum value size from registry.

Action: This is an internal error. Contact Oracle Support Services.

CRS-01338: Failed to add a delete key operation for key 'string' to a batch in OLR. Details at string in string.

Cause: Encountered internal error while deleting key in OLR.

Action: This is an internal error. Contact Oracle Support Services.

CRS-01339: Oracle High Availability Service aborted due to an unexpected error \[string\]. Details at string in string.

Cause: Look at the associated error message to fix the underlying issue.

Action: If the problem persists, contact Oracle Support Services.

CRS-01401: EVMD started on node string.

Cause: EVMD has started either because of a CRS start, a node reboot, or an EVMD restart.

Action: None required. You can run the 'crsctl check evmd' command to validate the health of EVMD.

CRS-01402: EVMD aborted on node string. Error \[string\]. Details in string.

Cause: EVMD has aborted due to an internal error. Check the EVMD log file to determine the cause.

Action: Determine whether the EVMD is auto-started and contact Oracle Support Services.

CRS-01403: The Event Management Service terminated on node string. Listening port number is in use by another application. Details in string.

Cause: The Event Management Service has aborted because the configured listening port is being used by another application on this node.

Action: Make the listening port listed above available. Restart the Event Management Service using 'crsctl start crs' or 'crsctl start cluster' command.

CRS-01601: CSSD Reconfiguration complete. Active nodes are string.

Cause: A node joined or left the cluster.

Action: None

CRS-01602: CSSD aborted on node string. Error \[string\]; details in string.

Cause: The CSS daemon aborted on the listed node with the listed return code.

Action: Collect the CSS daemon logs from all nodes and any CSS daemon core files and contact Oracle Support.

CRS-01603: CSSD on node string shutdown by user.

Cause: The CSS daemon on the listed node was terminated by a user.

Action: None

CRS-01604: CSSD voting file is offline: string; details at string in string.

Cause: The listed voting file became unusable on the local node.

Action: Verify that the filesystem containing the listed voting file is available on the local node.

CRS-01605: CSSD voting file is online: string; details in string.

Cause: The CSS daemon has detected a valid configured voting file.

Action: None

CRS-01606: The number of voting files available, number, is less than the minimum number of voting files required, number, resulting in CSSD termination to ensure data integrity; details at string in string

Cause: The number of voting files has decreased to a number of files that is insufficient.

Action: as indicated by those messages.

CRS-01607: Node string is being evicted in cluster incarnation number; details at string in string.

Cause: The local node has detected that the indicated node is still active, but not able to communicate with this node, so is forcibly removing the indicated node from the cluster.

Action: Collect the CSS daemon logs from all nodes and any CSS daemon core files and contact Oracle Support.

CRS-01608: This node was evicted by node number, string; details at string in string.

Cause: The local node was evicted by the indicated node.

Action: Collect the CSS daemon logs from all nodes and any CSS daemon core files and contact Oracle Support.

CRS-01609: This node is unable to communicate with other nodes in the cluster and is going down to preserve cluster integrity; details at string in string.

Cause: Communication was lost with some nodes of the cluster and this node detected that another sub-cluster was designated to be the surviving sub-cluster. This node went down to preserve data integrity.

Action: Verify all network connections between cluster nodes and repair any problematic connections. If there do not appear to be any network problems,

1\. collect the CSS daemon logs, system messages and any CSS daemon core files from all nodes and

2\. contact Oracle Support.

CRS-01610: Network communication with node string (number) missing for 90% of timeout interval. Removal of this node from cluster in number.number seconds

Cause: Did not receive heartbeat messages from the node. This could be due to network problems or failure of the listed node.

Action: Check if the private interconnect network used by cluster is functioning properly, including all the cables, network cards, switches/routers etc. between this node and listed node. Correct any problems discovered.

CRS-01611: Network communication with node string (number) missing for 75% of timeout interval. Removal of this node from cluster in number.number seconds

Cause: Did not receive heartbeat messages from the node. This could be due to network problems or failure of the listed node.

Action: Check if the private interconnect network used by cluster is functioning properly, including all the cables, network cards, switches/routers etc. between this node and listed node. Correct any problems discovered.

CRS-01612: Network communication with node string (number) missing for 50% of timeout interval. Removal of this node from cluster in number.number seconds

Cause: Did not receive heartbeat messages from the node. This could be due to network problems or failure of listed node.

Action: Check if the private interconnect network used by cluster is functioning properly, including all the cables, network cards, switches/routers etc. between this node and listed node. Correct any problems discovered.

CRS-01613: No I/O has completed after 90% of the maximum interval. Voting file string will be considered not functional in number milliseconds

Cause: Voting device I/O has not completed for a long time. This could be due some error with the device the voting file is on or in some element in the path of the I/O to the device.

Action: Verify that the device is working properly including all elements in the I/O path. The voting file listed will be considered inactive in the number of milliseconds specified. Failure of a majority of devices will result in node reboot.

CRS-01614: No I/O has completed after 75% of the maximum interval. Voting file string will be considered not functional in number milliseconds

Cause: Voting device I/O has not completed for a long time. This could be due some error with the device the voting file is on or in some element in the path of the I/O to the device.

Action: Verify that the device is working properly including all elements in the I/O path. The voting file listed will be considered inactive in the number of milliseconds specified. Failure of a majority of devices will result in node reboot.

CRS-01615: No I/O has completed after 50% of the maximum interval. Voting file string will be considered not functional in number milliseconds

Cause: Voting device I/O has not completed for a long time. This could be due some error with the device the voting file is on or in some element in the path of the I/O to the device.

Action: Verify that the device is working properly including all elements in the I/O path. The voting file listed will be considered inactive in the number of milliseconds specified. Failure of a majority of devices will result in node reboot.

CRS-01616: The BMC device used for IPMI at IP address string is not properly configured for ADMIN access; details at string in string

Cause: The IPMI BMC is not configured to support the ADMIN access methods required by Oracle Clusterware.

Action: Consult the clusterware admin manual for proper procedures in configuring BMC. Use the BMC configuration tool (ipmitool or ipmiutil) command to check and verify that the current configuration supports either MD5 or password validation for ADMIN access.

CRS-01617: The information required to do node kill for node string is incomplete; details at string in string

Cause: Incomplete config information stored in Cluster Registry for node kill.

Action: Make sure all the information pertaining to the node kill method

CRS-01618: The requested node kill information change could not be validated by node string; details at string in string

Cause: Unable to validate the node kill information for this node.

Action: Additional information can be found in the CRS alert log of the node that performed the validation.

CRS-01619: The node kill information of node string could not be validated by this node due to failure in connecting to the IPMI device; details at string in string

Cause: Unable to validate the node kill information for this node.

Action: Additional information can be found in the CSSD logs.

CRS-01620: The node kill information of node string could not be validated by this node due to invalid authorization information; details at string in string

Cause: Unable to validate the kill information for this node.

Action: Additional information can be found in the CSSD logs.

CRS-01621: The IPMI configuration data for this node stored in the Oracle registry is incomplete; details at string in string

Cause: All the necessary information such as IPMI username, password and IP address are not present.

Action: Make sure all the information(BMC IPMI username, password and IP address) are present. Use commands 'crsctl set css ipmiaddr' and 'crsctl set css ipmiadmin' for this.

CRS-01622: The IPMI node kill information could not be validated due to inability to connect to the IPMI device at BMC IP address provided string; details at string in string

Cause: Unable to validate the BMC IPMI IP address provided.

Action: Additional information can be found in the CSSD logs.

CRS-01623: The IPMI node kill information of BMC at IP address string could not be validated due to invalid authorization information. The BMC username provided is 'string'; details at string in string

Cause: Unable to validate the BMC IPMI UserName and password provided.

Action: Additional information can be found in the CSSD logs.

CRS-01624: The requested Node kill information change succeeds vacuously because there is no other node in cluster to validate.

Cause: Unable to validate the credentials because this is the sole node in the cluster.

Action: To complete the valdidation, shut down the clusterware stack on this node, start another node and restart the stack on this node.

CRS-01625: Node string, number number, was manually shut down

Cause: A Clustware stack shutdown command was issued for a node in the cluster and was observed by this node.

Action: None required.

CRS-01626: A Configuration change request completed successfully

Cause: A Configuration change request completed successfully.

Action: None required.

CRS-01627: A Configuration change request failed because another configuration change is in progress; Details at string in string

Cause: Another configuration change is in still in progress.

Action: Wait until the other command completes and reissue the command if necessary. Message 1626 would be printed if the command succeeds.

CRS-01628: A Configuration change request failed because read of existing voting files failed; Details at string in string

Cause: CSSD was not able to read the lease blocks of a majority of Voting files which is an indication of a problem with the voting files.

Action: Run the command 'crsctl query css votedisk' to get the list of currently working voting files. User may delete problematic voting file or use a different set.

CRS-01629: A Configuration change request failed because write to new voting files failed; Details at string in string

Cause: A voting file write failed, causing the associated configuration change to fail. This often results from adding a voting file that is not accessible to one or more nodes.

Action: Confirm that voting files added in a configuration change are accessible and writeable from all cluster nodes. If they are, contact Oracle Customer Support.

CRS-01630: A configuration change request failed because not all the new voting files were discovered; Details at string in string

Cause: One or more of the voting files being added were not discovered. Message 1638 identifies the unique ID(s) of the file(s) that could not be found.

Action: Verify if the discovery string is adequate to discover the new voting files. If not, modify discovery string using command 'crsctl replace discoverystring xxxxx'.

CRS-01631: A configuration change request failed because one or more nodes are not a sufficient Clusterware version level; Details at string in string

Cause: One ore more nodes are not a sufficient version level.

Action: Configuration change would not be successful until all nodes are at at the latest version. Try after all the nodes are upgraded.

CRS-01632: Node string is being removed from the cluster in cluster incarnation number

Cause: The local node is removing the indicated node from the cluster because it appears to be dead.

Action: Verify that the node that was removed, or the Oracle Clusterware on that node, was down. The CRS alert log of the node that was removed has information regarding why the node, or clusterware on the node, was no longer active. If the node was still up and Oracle Clusterware still active on that node, collect the CSS daemon logs from all nodes and any CSS daemon core files and contact Oracle Support.

CRS-01633: CSSD failed to register group string in vendor clusterware; details at string in string

Cause: The local node is not able to register the group of vendor clusterware.

Action: Verify that the vendor clusterware is installed and configured correctly.

CRS-01634: CSSD is unable to determine cluster name; details at string in string

Cause: Name of the cluster cannot be determined from configuration.

Action: Verify that Oracle Clusterware installation was successful.

CRS-01635: CSSSD failed to initialize vendor clusterware; details at string in string

Cause: The local node is not able to attach vendor clusterware.

Action: Verify that the vendor clusterware is installed and configured correctly.

CRS-01636: The CSS daemon was started in exclusive mode but found an active CSS daemon on node string and is terminating; details at string in string

Cause: The CSS daemon was started in exclusive mode, which requires that the clusterware stack is down on all other nodes to ensure data integrity. A CSS daemon was detected on another node, so the CSS daemon on this node is terminating.

Action: Stop the Oracle clusterware stack that is running on the indicated node.

CRS-01637: Unable to locate configured voting file with ID string; details at string in string

Cause: The voting file with unique the ID indicated in the message was not found during the voting file discovery phase of CSS initialization.

Action: Verify that all configured voting files are accessible on this node. Any voting files that are not accessible should be removed and replaced with accessible voting files using the appropriate 'crsctl' commands.

CRS-01638: Unable to locate voting file with ID string that is being added to the list of configured voting files; details at string in string

Cause: The voting file with the unique ID indicated in the message was not found during the voting file discovery phase of CSS initialization. This voting file is in the process of being added to the list of configured voting files.

Action: Verify that all voting files to be added are accessible on this node. Any voting files that are not accessible should be removed and replaced with accessible voting files using the appropriate 'crsctl' commands.

CRS-01639: Rejecting configuration change number:number because another configuration change is already in progress; details at string in string

Cause: A configuration change was requested, but another configuration change is already in progress and only one configuration change may be processed at a time.

Action: Wait for the current configuration change to complete, then resubmit this configuration change.

CRS-01640: Rejecting configuration change number:number because one or more new voting files in the new configuration could not be found; details at string in string

Cause: A configuration change that involved the addition of voting files is being rejected because some of the new voting files were not located.

Action: Verify that the voting file name is correct and that it is accessible on this node, if the voting files are not managed by ASM. Message number 1638 provides greater detail.

CRS-01641: Rejecting configuration change number:number because only number of the required number voting files of the new configuration were located; details at string in string

Cause: A configuration change that involved a change to the list of voting files is being rejected because a sufficient number of voting files in the new configuration could not be located.

Action: Verify that all voting files in the new configuration are accessible on this node.

CRS-01642: Node number is using a different CSS configuration from the one used by this node; this node is terminating to preserve integrity; details at string in string

Cause: Another node in the cluster is using a different set of CSS configuration values, such as misscount or voting files. Inconsistency can result in data corruption, so this node is terminating to avoid data corruption.

Action: Collect Clusterware alert log and the CSSD log indicated in the message as well as the CSS daemon logs of all other nodes in the cluster and contact Oracle Support Services.

CRS-01643: Failed to format the CSS voting disk string

Cause: Problems were encountered attempting to access the voting file.

Action: Verify that the voting file can be accessed, the file exists, has the proper ownership and permissions, etc.

CRS-01644: The initialization of the EXADATA fencing facility failed in start with error ORA-number; details at string in string

Cause: The start of the initialization of the EXADATA fencing facility failed with the error code shown.

Action: See the Action section of the error message shown.

CRS-01645: The initialization of the EXADATA fencing facility failed in completion with error ORA-number; details at string in string

Cause: The completion of the initialization of the EXADATA fencing facility failed with the error code shown.

Action: See the Action section of the error message shown.

CRS-01646: Creation of a EXADATA fence identifier failed with error ORA-number; details at string in string

Cause: An attempt to create an identifier for a fence to an EXADATA device failed with the error code shown.

Action: See the Action section of the error message shown.

CRS-01647: Initialization of a EXADATA fence failed with error ORA-number; details at string in string

Cause: An attempt to initiate a fence to an EXADATA device failed with the error code shown.

Action: See the Action section of the error message shown.

CRS-01648: Completion of queued EXADATA fence requests failed with error ORA-number; details at string in string

Cause: Previously queued fence requests to an EXADATA device failed with the error code shown.

Action: See the Action section of the error message shown.

CRS-01649: An I/O error occured for voting file: string; details at string in string.

Cause: The listed voting file became inaccessible.

Action: Verify that the filesystem containing the listed voting file is available on the local node.

CRS-01650: Configuration change number:number rejected by node number string; details at string in string

Cause: A new configuration change request from this node was not accepted due to another node rejecting the change.

Action: Check the CRS alert log of the node rejecting this configuration change for more details.

CRS-01651: Configuration change number:number rejected because it would make the active version of node number lower than the current setting string of this node; details at string in string

Cause: A new configuration change request from another node was not accepted because the new Active Version in the request is lower than this node's Active Version.

Action: Ensure that the new Active Version is not lower than the current Active Version of the nodes in the cluster.

CRS-01652: Starting clean up of CRSD resources.

Cause: Clean up of the resources registered in CRSD started.

Action: None

CRS-01653: The clean up of the CRSD resources failed.

Cause: Clean up of the resources registered in CRSD failed.

Action: Check the CRS alert log.

CRS-01654: Clean up of CRSD resources finished successfully.

Cause: Clean up of the resources registered in CRSD finished.

Action: None

CRS-01655: CSSD on node string detected a problem and started to shutdown.

Cause: The CSS daemon on the listed node detected a problem and started to shutdown.

Action: Check the CRS alert log.

CRS-01656: The CSS daemon is terminating due to a fatal error; Details at string in string

Cause: A fatal error occurred during CSS daemon processing.

Action: Check for prior errors logged in the alert log. Correct any errors that can be corrected. If there are no errors shown, or the errors cannot be resolved, contact Oracle support

CRS-01657: Unable to obtain the voting file discovery string; Details at string in string

Cause: An attempt to obtain the voting file discovery string from the profile failed, causing the CSS daemon to fail.

Action: Collect the Clusterware alert log and the CSSD log of this node as well as all CSS daemon logs of all other nodes in the cluster and contact Oracle Support Services.

CRS-01658: There is a mismatch of the initial cluster incarnation among the cluster nodes; Details at string in string

Cause: An internal error occurred.

Action: Collect the Clusterware alert log and the CSSD log of this node as well as all CSS daemon logs of all other nodes in the cluster and contact Oracle Support Services.

CRS-01659: An attempt to kill node string failed; Details at string in string

Cause: To protect data integrity a node kill was attempted for the indicated node, but it failed.

Action: Collect the Clusterware alert log and the CSSD log of this node as well as the CSS daemon logs of all other nodes in the cluster and contact Oracle Support Services.

CRS-01660: The CSS daemon shutdown has completed

Cause: A command to shut down the CSS daemon was issued by a user and the shutdown processing is completed. The CSS daemon is terminated.

Action: No action is required.

CRS-01661: The CSS daemon is not responding. Reboot will occur in number milliseconds; Details at string in string

Cause: The CSS daemon is failing to respond.

Action: Collect the Clusterware alert log and the CSSD log of this node as well as the CSS daemon logs of all other nodes in the cluster and contact Oracle Support Services.

CRS-01662: Member kill requested by node string for member number number, group string

Cause: A request to kill a member of the indicated group was issued by a process on the indicated node.

Action: No action is required.

CRS-01663: Member kill issued by PID string for number members, group string. Details at string in string.

Cause: A member kill request was issued by the indicated process for the members belonging to the indicated group.

Action: No action is required.

CRS-01701: Initialization of the required component GIPC failed; details at string in string

Cause: The initialization of the communications component GIPC failed, causing the CSSD startup to fail.

Action: Collect alert log and the CSSD log indicated in the message and contact Oracle Support Services.

CRS-01702: Initialization of the required component OLR failed; details at string in string

Cause: The initialization of the local repository component OLR failed, causing the CSSD startup to fail.

Action: Collect clusterware alert log and daemon logs and contact Oracle Support Services.

CRS-01703: Initialization of the required component GPNP failed because the GPNP server daemon is not up; details at string in string

Cause: The initialization of the configuration profile service failed because the associated server is not up, causing the CSSD startup to fail.

Action: Collect clusterware alert log and daemon logs and contact Oracle Support Services.

CRS-01704: Initialization of the required component string failed; details at string in string

Cause: The initialization of a component required by the CSS daemon failed, causing the CSSD startup to fail

Action: Collect clusterware alert log and daemon logs and contact Oracle Support Services.

CRS-01705: Found number configured voting files but number voting files are required, terminating to ensure data integrity; details at string in string

Cause: The voting file discovery was unable to locate a sufficient number of valid voting files to guarantee data integrity and is terminating to avoid potential data corruption.

Action: Delete the voting files that are no longer available, as indicated by message number 1637, using appropriate 'crsctl' commands, run either on another node where the clusterware stack is active, or by starting the clusterware stack in exclusive mode.

CRS-01706: Found number of number voting files in a pending configuration change but number voting files are required, terminating to ensure data integrity; details at string in string

Cause: The voting file discovery was unable to locate a sufficient number of voting files from the new configuration when a configuration change to add or delete voting files is in progress. The CSS daemon is terminating to avoid potential data corruption.

Action: Delete the voting files that are no longer available, as indicated by message number 1638, using appropriate 'crsctl' commands, run either on another node where the clusterware stack is active, or by starting the clusterware stack in exclusive mode.

CRS-01707: Lease acquisition for node string number number completed

Cause: CSSD acquired a node number through a lease acquisition procedure.

Action: None

CRS-01708: Lease acquisition failed for node string because all lease slots are in use; Details at string in string

Cause: The node failed to acquire a lease because all the lease slots were found to be occupied by other nodes.

Action: Using olsnodes command get the list of leased nodes. Delete the unused nodes using appropriate crsctl command.

CRS-01709: Lease acquisition failed for node string because no voting file has been configured; Details at string in string

Cause: At least one voting file is required for CSSD to function properly. No voting files have been configured.

Action: Add at lease one voting file using appropriate crsctl command.

CRS-01710: Lease acquisition failed for node string because CSSD failed to access majority of voting files; Details at string in string

Cause: A majority of the voting files are not accessible by a node.

Action: Delete the voting files that are no longer available, as indicated by message number 1637, using appropriate 'crsctl' commands, run either on another node where the Clusterware stack is active, or by starting the Clusterware stack in exclusive mode.

CRS-01711: Increasing the number of leases available for new nodes from number to number

Cause: All the currently available leases are being used. Hence the number of leases available are increased.

Action: None

CRS-01712: Failed to save the node number acquired for node string; Details at string in string

Cause: CSSD failed to save the node number acquired during startup. The node number is saved to speed up the subsequent startup. Hence this is not a real problem but just a performance degradation on the next startup.

Action: Collect Clusterware alert log, CSSD logs and OHASD logs indicated in the message and contact Oracle Support Services.

CRS-01713: CSSD daemon is started in string mode

Cause: CSSD has been started on the node.

Action: None

CRS-01714: Unable to discover any voting files, retrying discovery in number seconds; Details at string in string

Cause: No voting files were discovered. Possible reasons include:

\- The filesystems the voting files are on are not available

\- The voting files have been deleted

\- The voting files are corrupted

Action: Verify that the filesystems that the voting files are on are active and that the voting files have not been damaged. If necessary, start the clusterware stack in exclusive mode using 'crsctl start crs -excl' and add voting files using 'crsctl add css votedisk'

CRS-01715: A failure occurred in the CSS daemon during initialization; Details at string in string

Cause: A fatal error occurred during the initialization of the CSS daemon.

Action: Check for prior errors logged in the alert log. Correct any errors that can be corrected. If there are no errors shown, or the errors cannot be resolved, contact Oracle Support Services

CRS-01716: The CSS daemon cannot join the cluster because the software version string is lower than the active version string; Details at string in string

Cause: The cluster has been upgraded to the active version indicated. in the message, but this node is at a lower software version, as indicated in the message.

Action: Upgrade this node to the active version indicated in the message

CRS-01717: The CSS daemon has detected a voting file add during startup and is waiting for the add to complete; Details at string in string

Cause: A voting file add started on another node is in progress while this CSS daemon is starting. To avoid the potential for data corruption, the CSS daemon on this node must wait for the add to complete.

Action: This is normally a temporary condition that is automatically resolved. If the clusterware stack cannot start on any node, this condition may be corrected by starting the clusterware stack in exclusive mode using 'crsctl start crs -excl' followed by 'crsctl stop crs' on one node. This will automatically correct the condition and the clusterware can be started normally on all nodes.

CRS-01805: Unable to connect to the CSS daemon, return code number

Cause: Could not initialize the CSS connection.

Action: Verify that the CSS daemon is running and restart it if it is not up. Retry the operation.

CRS-01806: An error occurred when obtaining the node number of this host, return code number

Cause: The request for node number of this node failed.

Action: Verify that the CSS daemon is running and restart it if not Retry the operation that failed after restart. Look for error messages from the CSS daemon in the alert log indicating any problems.

CRS-01807: An internal cluster configuration command failed in an OCR/OLR operation. Details at string in string.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CRS-01809: The cluster configuration command failed to open OCR or OLR key string. Details at string in string.

Cause: An expected or required piece of configuration is missing from the cluster or local registry.

Action: Use the ocrcheck utility to detect errors, and the ocrdump utility to review the registry contents. If problems exist, the registry may need to be recovered or restored. If the problem persists, contact Oracle Support Services.

CRS-02001: memory allocation error when initiating the connection

Cause: failed to allocate memory for the connection with the target process.

Action: None

CRS-02002: connection by user string to string refused

Cause: User command cannot connect to the target process.

Action: The user may not have sufficient privilege to connect.

CRS-02003: error number encountered when connecting to string

Cause: Connection to the target process failed.

Action: Examine whether the connection is made properly. Retry again at a later time if necessary.

CRS-02004: error number encountered when sending messages to string

Cause: User command cannot communicate with the target process properly.

Action: Retry again at a later time.

CRS-02005: timed out when waiting for response from string

Cause: the target process does not return acknowledgment in time.

Action: Retry again at a later time.

CRS-02006: error number encountered when receiving messages from string

Cause: no meta or response message was received from the target process.

Action: Retry again at a later time.

CRS-02007: invalid component key name \<string> used

Cause: the given component key name could not be recognized.

Action: re-run the command with a valid component key name.

CRS-02008: invalid message type \<number> used

Cause: an unrecognized message type was sent.

Action: Retry with a valid command again.

CRS-02009: unable to get authentication for user string

Cause: current user was not authenticated for connection.

Action: Log in as another user and try again.

CRS-02010: invalid response message from string

Cause: Response message has incorrect format.

Action: Retry again at a later time.

CRS-02011: no response at index number in response message from string

Cause: Response message did not contain a response at the specified index.

Action: If this is an unexpected result, retry again at a later time.

CRS-02012: syntax error in command

Cause: The command syntax is not valid.

Action: Issue 'crsctl debug -h' to see command syntax details. Watch out for ',' vs. ';'.

CRS-02101: The OLR was formatted using version number.

Cause: Successfully formatted the OLR location(s).

Action: None

CRS-02102: The OLR was restored from file string.

Cause: The OLR was successfully restored from a backup file as requested by the user.

Action: None

CRS-02103: The OLR format was downgraded to version number.

Cause: The OLR was successfully downgraded to an earlier block format as requested by the user.

Action: None

CRS-02104: The OLR was imported from string.

Cause: Successfully imported the OLR contents from a file as requested by the user.

Action: None

CRS-02105: The OLR upgrade was completed. Version has changed from number to number. Details in string.

Cause: The OLR was successfully upgraded to a newer block format.

Action: None

CRS-02106: The OLR location string is inaccessible. Details in string.

Cause: An error occurred while accessing the OLR.

Action: Use the "ocrcheck -local" command to validate the accessibility of the device and its block integrity. Check that the OLR location in question has the correct permissions.

CRS-02112: The OLR service started on node string.

Cause: The OLR was successfully started.

Action: None

CRS-02114: Failed to import Oracle Local Registry from file string

Cause: Unable to read data from the import file and import to the local registry

Action: Check availability of the local registry and the details of the failure from the log file

CRS-02120: The Oracle Local Registry has invalid contents. Details at string in string.

Cause: Some of the Oracle Local Registry contents were invalid.

Action: Check the log file indicated in the message for more details. Use the 'ocrcheck -local' command to detect errors, and the 'ocrdump -local' command to review the registry contents. If problems exist, the registry may need to be recovered or restored. If the problem persists, contact Oracle Support Services.

CRS-02301: GPnP: string

Cause: This conveys a message from the GPnP layer to the alert log.

Action: Look up the imbedded message and respond accordingly.

CRS-02302: Cannot get GPnP profile. Error string (string).

Cause: Get GPnP profile operation failed.

Action: None

CRS-02303: GPNPD is not running on local node.

Cause: GPNPD is not running on local node. GPnP request cannot be completed.

Action: Make sure GPNPD is running and retry the operation.

CRS-02304: GPnP profile signature verification failed. string request aborted.

Cause: GPnP profile used in GPnP request or request result does not have a valid signature.

Action: If error persists, please contact Oracle Support Services.

CRS-02305: GPnP resource discovery (MDNSD) is not running on local node.

Cause: GPnP resource discovery failed.

Action: Make sure resource discovery service (MDNSD) runs on local node.

CRS-02306: GPnP service on host "string" not found.

Cause: Remote GPnP service on requested host were not found in resource discovery results.

Action: Make sure host is up, clusterware GPnP services (MDNSD and GPNPD) are up and running and network connection is operational.

CRS-02310: Fatal error: failed to initialize NZ security facility.

Cause: Error occurred while initializing GPnP security component.

Action: If the problem persists, contact Oracle Support Services.

CRS-02311: Fatal error: failed to initialize Resource Discovery. RD error: string (number). Make sure RD providers installed properly.

Cause: Error occurred while initializing GPnP Resource Discovery (RD).

Action: If the problem persists, contact Oracle Support Services.

CRS-02312: Fatal error: failed to initialize XDK. XDK error string (number).

Cause: Error occurred while initializing Xml Development Kit component (XDK).

Action: If the problem persists, contact Oracle Support Services.

CRS-02313: Fatal error: failed to initialize GIPC communication layer. GIPC error: string (number).

Cause: Error occurred while initializing GIPC communication layer.

Action: If the problem persists, contact Oracle Support Services.

CRS-02314: Fatal error: cannot initialize locking subsystem.

Cause: Error occurred while initializing locking subsystem.

Action: If the problem persists, contact Oracle Support Services.

CRS-02315: Fatal error: failed to initialize GPnP certkey providers.

Cause: GPnP certkey provider(s) data was not found or corrupt.

Action: If the problem persists, contact Oracle Support Services.

CRS-02316: Fatal error: cannot initialize GPnP, string (string).

Cause: General GPnP initialization failure.

Action: If the problem persists, contact Oracle Support Services.

CRS-02317: Fatal error: cannot get local GPnP security keys (wallet).

Cause: GPnP wallet(s) directory or files were not found or corrupt.

Action: If the problem persists, contact Oracle Support Services.

CRS-02318: GPNPD is not found.

Cause: Local GPnP service is not found.

Action: Make sure GPNPD is running.

CRS-02319: No cluster name found in GPnP profile.

Cause: Profile is invalid - it must specify a mandatory clustername parameter.

Action: Please contact Oracle Support Services.

CRS-02322: Fatal error: Cannot get local GPnP profile. Error initializing GPnP profile cache providers.

Cause: Local GPnP setup is invalid.

Action: Please contact Oracle Support Services.

CRS-02323: Error initializing one of the GPnP profile cache providers.

Cause: Local GPnP setup is invalid.

Action: Please contact Oracle Support Services.

CRS-02324: Errors occurred while trying to push GPnP profile.

Cause: GPnP profile update partially failed.

Action: Try to repeat the update. If the problem persists, contact Oracle Support Services.

CRS-02325: Unable to get GPnP profile from requested cluster nodes.

Cause: Get GPnP profile from remote nodes failed.

Action: Try to repeat the update. If the problem persists, contact Oracle Support Services.

CRS-02326: GPnP profile is different across cluster nodes. string.

Cause: GPnP profile is different across cluster nodes.

Action: Try to repeat the update. If the problem persists, contact Oracle Support Services.

CRS-02327: GPNPD already running on node string. Terminating.

Cause: GPnP service instance is already running on node.

Action: Bring down existing GPNPD instance first.

CRS-02328: GPNPD started on node string.

Cause: GPnP service started on node.

Action: None

CRS-02329: GPNPD on node string shutdown.

Cause: GPnP service was shutdown by request.

Action: None

CRS-02330: GPNPD failed to start listening for GPnP peers.

Cause: GPnP service failed to open server endpoint.

Action: Please check GPNPD logs for the cause. If the problem persists, contact Oracle Support Services.

CRS-02331: Error getting GPnP profile from "string".

Cause: Get remote GPnP profile from remote node operation failed.

Action: Retry request. If the problem persists, contact Oracle Support Services.

CRS-02332: Error pushing GPnP profile to "string".

Cause: Push GPnP profile to remote node operation failed.

Action: Retry request. If the problem persists, contact Oracle Support Services.

CRS-02333: Could not write GPnP profile to local cache.

Cause: GPNPD service cannot save GPnP profile to local cache.

Action: Make sure there is at least 10MB of free disk space in Clusterware home. If the problem persists, contact Oracle Support Services.

CRS-02334: Could not delete pending GPnP profile from local cache.

Cause: GPNPD service cannot delete GPnP profile from local cache.

Action: If the problem persists, contact Oracle Support Services.

CRS-02335: Could not write pending GPnP profile to local cache.

Cause: GPNPD service cannot save GPnP profile to local cache.

Action: Make sure there is at least 10MB of free disk space in Clusterware home. If the problem persists, contact Oracle Support Services.

CRS-02340: Errors occurred while processing received gpnp message.

Cause: Invalid GPnP message received.

Action: Please check gpnp client and GPNPD logs for details. If the problem persists, contact Oracle Support Services.

CRS-02341: GPNPD on node string shutting down on signal number.

Cause: GPnP service shutting down due to received signal.

Action: Please contact your cluster administrator.

CRS-02342: GPnP messaging received error: string (string).

Cause: GPnP message error received.

Action: If the problem persists, contact Oracle Support Services.

CRS-02401: The Cluster Time Synchronization Service started on host string.

Cause: The Cluster Time Synchronization Service successfully started on the listed node.

Action: None

CRS-02402: The Cluster Time Synchronization Service aborted on host string. Details at string in string.

Cause: The Cluster Time Synchronization Service aborted due to an internal error. Check the Cluster Time Synchronization Service log file to determine the cause.

Action: Determine whether the Cluster Time Synchronization Service has auto-started.

CRS-02403: The Cluster Time Synchronization Service on host string is in observer mode.

Cause: The Cluster Time Synchronization Service detected an active vendor time synchronization service on at least one node in the cluster.

Action: Oracle Clusterware requires a time synchronization service in active mode. Oracle Clusterware will work with a vendor service or the Cluster Time Synchronization Service. If you want to change the Cluster Time Synchronization Service to active mode, stop and deconfigure the vendor time synchronization service on all nodes.

CRS-02404: The Cluster Time Synchronization Service detects that the local time is significantly different from the mean cluster time. Details in string.

Cause: The difference between the local time and the time on the reference node was too much to be corrected.

Action: Shutdown the Oracle Clusterware on the local node. Adjust the clock via native platform or OS methods. Restart the Oracle Clusterware on the local node.

CRS-02405: The Cluster Time Synchronization Service on host string is shutdown by user

Cause: The Cluster Time Synchronization Service on listed node was terminated by a user.

Action: None

CRS-02406: The Cluster Time Synchronization Service timed out on host string. Details in string.

Cause: A Cluster Time Synchronization Service action failed. The information from the reference node was discarded.

Action: Verify all network connections between cluster nodes and repair any problematic connections. If no network problems are found,

1\. Run diagcollection.pl.

2\. Contact Oracle Support Services.

CRS-02407: The new Cluster Time Synchronization Service reference node is host string.

Cause: A new Cluster Time Synchronization Service reference node has been elected.

Action: None

CRS-02408: The clock on host string has been updated by the Cluster Time Synchronization Service to be synchronous with the mean cluster time.

Cause: The clock was updated to be in sync with the mean cluster time.

Action: None

CRS-02409: The clock on host string is not synchronous with the mean cluster time. No action has been taken as the Cluster Time Synchronization Service is running in observer mode.

Cause: The clock was not in sync with the mean cluster time. No action has been taken as Cluster Time Synchronization Service is running in observer mode.

Action: Verify correct operation of the vendor time synchronization service on the node.

CRS-02410: The Cluster Time Synchronization Service on host string is in active mode.

Cause: The Cluster Time Synchronization Service did not detect an active vendor time synchronization service on any node in the cluster.

Action: None. If a vendor time synchronization service is preferred to the Cluster Time Synchronization Service, then configure and start the vendor time synchronization service on all nodes to change the Cluster Time Synchronization Service to observer mode.

CRS-02411: The Cluster Time Synchronization Service will take a long time to perform time synchronization as local time is significantly different from mean cluster time. Details in string.

Cause: The difference between the local time and the time on the reference node was too much to be synchronized in a short period.

Action: (Optional) Shutdown and restart the Oracle Clusterware on this node to instantaneously synchronize the time with the reference node.

CRS-02412: The Cluster Time Synchronization Service detects that the local time is significantly different from the mean cluster time. Details in string.

Cause: The difference between the local time and the time on the reference node was too large. No action has been taken as the Cluster Time Synchronization Service was running in observer mode.

Action: Verify correct operation of the vendor time synchronization service on the node. Alternatively, if you want to change the Cluster Time Synchronization Service to active mode, stop and deconfigure the vendor time synchronization service on all nodes.

CRS-02413: The Cluster Time Synchronization Service is unable to perform step time synchronization due to high network latency with the reference node. The local time is not significantly different from the mean cluster time. The Cluster Time Synchronization Service is entering slew time synchronization mode.

Cause: The Cluster Time Synchronization Service experienced high network latency. The local time was not significantly different from the mean cluster time; therefore, the Cluster Time Synchronization Service will maintain the system time with slew time synchronization.

Action: Determine the root cause of high network latency, and perform appropriate repair if necessary.

CRS-02414: The Cluster Time Synchronization Service is unable to perform step time synchronization due to high network latency with the reference node. The local time is significantly different from the mean cluster time. The Cluster Time Synchronization Service is aborting.

Cause: The Cluster Time Synchronization Service experienced high network latency. The local time was significantly different from the mean cluster time; therefore, the Cluster Time Synchronization Service is aborting.

Action: Shut down the Oracle Clusterware on the local node. Determine the root cause of high network latency. Perform appropriate repair if necessary, then restart the Oracle Clusterware on the local node.

CRS-02500: Cannot stop resource 'string' as it is not running

Cause: A request to stop a resource that is not running was received.

Action: Check the current state of the resource, it should no longer be running.

CRS-02501: Resource 'string' is disabled

Cause: The resource is currently disabled and so may not be operated on.

Action: Enable the resource and re-submit your request.

CRS-02502: Resource 'string' has dependency error because of resource 'string'

Cause: The attempted operation has failed because of a dependency on the specified resource.

Action: Ensure that the intended operation is still desired. If so, the specified resource and its state need to be evaluated to decide on the corrective action.

CRS-02503: Resource 'string' is in UNKNOWN state and must be stopped first

Cause: The resource cannot be acted upon when it is in the UNKNOWN state.

Action: Stop the resource manually, make sure it is OFFLINE, and then re-submit the request.

CRS-02504: Resource 'string' cannot be placed on any online servers that satisfy its placement policy

Cause: The resource cannot be placed because of the constrains imposed by its placement policy.

Action: Either change the placement policy of the resource or re-evaluate the request.

CRS-02505: Another operation is being performed on 'string'. Please retry later

Cause: Another operation is being performed on the specified object.

Action: Typically, waiting and retrying or using a way to queue the request are the two choices to proceed.

CRS-02506: Operation on 'string' has been cancelled

Cause: A scheduled or running operation has been cancelled.

Action: None

CRS-02507: Unsupported modifier 'string' in dependency 'string'

Cause: The modifier is not a valid one.

Action: Check the specification of the dependency, fix the problem indicated, and resubmit the request.

CRS-02508: Incomplete specification of dependency 'string'

Cause: The specification does not have the dependent object specified.

Action: Check the specification of the dependency, fix the problem indicated, and resubmit the request.

CRS-02509: Resource type 'string' used in dependency 'string' does not exist or is not registered

Cause: The resource type referenced by the dependency specification is not found.

Action: Check the specification of the dependency, fix the problem indicated, and resubmit the request.

CRS-02510: Resource 'string' used in dependency 'string' does not exist or is not registered

Cause: The resource referenced by the dependency specification is not found.

Action: Check the specification of the dependency, fix the problem indicated, and resubmit the request.

CRS-02511: Attribute 'string' cannot be specified on per-X basis for resource 'string'

Cause: The specified attribute is specified on per-X basis, which is not allowed for this attribute.

Action: Remove the specification.

CRS-02512: Attribute format for 'string' is invalid in resource 'string'

Cause: The specification does not follow valid format.

Action: Correct the specification and re-submit the request.

CRS-02513: Attribute format for 'string' is invalid

Cause: The specification does not follow valid format.

Action: Correct the specification and re-submit the request.

CRS-02514: Dependency attribute specification 'string' is invalid in resource 'string'

Cause: The specification of relations does not follow valid format.

Action: Correct the specification and re-submit the request.

CRS-02515: Circular dependency found for resource 'string'

Cause: The resource dependency specification has a circular dependency.

Action: Circular dependencies are disallowed. Please change the profile and re-submit.

CRS-02516: Server pool is not specified for resource 'string'

Cause: The resource profile does not have server pool specified.

Action: Please either specify a an existing server pool or HOSTING\_MEMBERS in the profile and re-submit the request.

CRS-02517: Required attribute 'string' is not specified for resource 'string'

Cause: A required attribute is missing from the resource profile.

Action: Please add the attribute to the profile and re-submit the request.

CRS-02519: Either 'string' or 'string' must be specified when 'string' is 'string'

Cause: Neither or both of the parameters was specified.

Action: Please specify exactly one of the two and re-submit.

CRS-02520: Invalid value 'string' for attribute 'string'

Cause: The value specified for the attribute is inappropriate or invalid.

Action: Review the value, correct the problem and re-submit the request.

CRS-02521: Read-only attribute 'string' cannot be modified

Cause: An attempt was made to modify a read-only attribute.

Action: None

CRS-02522: No value is specified

Cause: There is nothing specified for the value.

Action: Provide a valid value.

CRS-02523: Invalid characters are used when specifying the value

Cause: 1 or more characters used to specify a value are inappropriate.

Action: Provide a valid value.

CRS-02524: Value specification may only contain 'string'/'string'/'string'/'string'/'string'/'string'

Cause: The value specified is not any of the allowed.

Action: The value must be one of the allowed ones, as specified. Provide a valid one.

CRS-02525: All instances of the resource 'string' are already running; relocate is not allowed because the force option was not specified

Cause: All instances of the resource are running and the start request does not have the force option specified.

Action: Either specify the force option or re-evaluate the need for the request.

CRS-02526: There are no available instances of resource 'string' to start on 'string'

Cause: All instances of the resource are already running or otherwise unavailable to be started on the specified server.

Action: Create more instances or re-evaluate the need for the request.

CRS-02527: Unable to start 'string' because it has a 'string' dependency on 'string'

Cause: Start/relocate of the resource is impossible because it has a dependency on another entity which prevents it from being able to start.

Action: This message will usually be coupled with another one that details the nature of the problem with the other resource. Please follow up on the action recommended for that message.

CRS-02528: Unable to place an instance of 'string' as all possible servers are occupied by the resource

Cause: Out of possible servers to place the resource on, all already host an instance of the resource.

Action: You need to add more servers or change the resource placement parameters to allow placement on additional servers.

CRS-02529: Unable to act on 'string' because that would require stopping or relocating 'string', but the force option was not specified

Cause: Acting on the resource requires stopping or relocating other resources, which requires that force option be specified, and it is not.

Action: Re-evaluate the request and if it makes sense, set the force option and re-submit.

CRS-02530: Unable to stop 'string' because 'string' has a stop-time 'string' dependency on it

Cause: Stopping the resource is impossible because it has a dependency on another resource and there is a problem with that other resource.

Action: This message will usually be coupled with another one that details the nature of the problem with the other resource. Please follow up on the action recommended for that message.

CRS-02531: Internal error while operating on 'string'

Cause: General-purpose message for highly unexpected internal errors.

Action: This message will usually be preceded by another one with a more specific problem description. Contact Oracle Support Services.

CRS-02532: OCR write failed for 'string'

Cause: Unknown, but would usually imply corruption or unavailability of the OCR or a lack of permissions to update keys or a software defect in the OCR code.

Action: Validate that OCR is accessible, validate that key permissions match. Contact Oracle Support Services.

CRS-02533: Server 'string' is down. Unable to perform the operation on 'string'

Cause: The server is down and therefore the operation cannot be performed.

Action: Try using a different server.

CRS-02534: Resource type 'string' is not registered

Cause: The specified resource type is not registered.

Action: Re-evaluate the request.

CRS-02535: Resource type 'string' does not have attribute 'string' and thus it cannot be updated

Cause: An non-existing attribute cannot be modified.

Action: Re-evaluate the request.

CRS-02536: Required attribute 'string' is not specified for 'string'

Cause: A required attribute is missing from the entity's profile.

Action: Add the attribute to the profile and re-submit the request.

CRS-02537: Resource type 'string' cannot be extended directly; use its extensions instead

Cause: The type cannot be extended.

Action: Use a type that extends this one.

CRS-02538: Value for attribute 'string' is of incorrect type (string is expected)

Cause: The type of the value is not correct.

Action: Re-submit the request with the value specified in proper type.

CRS-02539: A resource with the name 'string' is already registered

Cause: A resource with specified name is already registered.

Action: Use a unique name for the new resource.

CRS-02540: Value for attribute 'string' is of incorrect type (integer is expected)

Cause: The type of the value is not correct.

Action: Re-submit the request with the value specified in proper type.

CRS-02541: Server pool 'string' is not registered

Cause: The specified server pool is not registered.

Action: Re-evaluate the request.

CRS-02542: The tag 'string' is mentioned in both 'string' and 'string' attributes, which is conflicting

Cause: The same tag is used to specify exclusive as well as overlapping server pools. These requirements cannot be satisfied simultaneously.

Action: Remove the tag from one of the attributes.

CRS-02543: The type is not specified for attribute 'string'

Cause: Value type specification is missing for the attribute.

Action: Specify a proper type and re-submit.

CRS-02544: The name 'string' is longer than the allowed maximum of 'number' characters

Cause: The name is too long.

Action: Use a shorter name.

CRS-02545: Cannot operate on 'string'. string

Cause: The entity specified is currently locked as part of another operation.

Action: Re-submit the request later.

CRS-02546: Server 'string' is not online

Cause: Operation is invalid because the specified server is not online.

Action: Provide an online server name.

CRS-02547: Update of an internal or read-only attribute 'string' for resource 'string' is not allowed

Cause: Internal and read-only attributes may not be updated.

Action: Exclude internal and read-only attributes from your request.

CRS-02548: A cyclical dependency on 'string' is detected from 'string'

Cause: There is a cycle in the dependency graph. Cycles are disallowed.

Action: Re-evaluate the dependency graph.

CRS-02549: Resource 'string' cannot be placed on 'string' as it is not a valid candidate as per the placement policy

Cause: The resource cannot be placed because of the constrains imposed by its placement policy.

Action: Either change the placement policy of the resource or re-evaluate the request.

CRS-02550: Resource 'string' cannot be failed-over because it has other non-OFFLINE instances on the server 'string'

Cause: The resource cannot be failed-over from the specified server because has other non-OFFLINE instances still available on that server and fail-over can only be done on all instances of the resource on the server as a whole.

Action: None

CRS-02551: Resource 'string' cannot be failed-over because it is of type 'string', which cannot relocate

Cause: Local resources cannot be relocated from one server to another.

Action: None

CRS-02552: There are no available instances of resource 'string' to start.

Cause: All instances of the resource are in the ONLINE or UNKNOWN state.

Action: Re-evaluate the need for the request.

CRS-02553: Server pool 'string' cannot be unregistered as it does not exist

Cause: The server pool you are trying to remove does not exist.

Action: Make sure the server pool you are trying to remove exists.

CRS-02554: Server pool 'string' cannot be unregistered as it is referenced by resource 'string'

Cause: The server pool you are trying to remove has references to it.

Action: Make sure the server pool you are trying to remove is not referenced by other entities.

CRS-02555: Resource 'string' cannot be relocated as it is a local resource

Cause: The request is impossible to complete as local resources never relocate.

Action: Please re-evaluate the request.

CRS-02556: Resource 'string' cannot be restored to its original state after a failed relocate attempt

Cause: After an unsuccessful attempt to relocate a resource, crsd was unable to restore the resource.

Action: Manual intervention may be required. Re-try starting the resource.

CRS-02557: Server pool 'string' cannot be unregistered as it is referenced by server pool 'string'

Cause: The server pool you are trying to remove has references to it.

Action: Make sure the server pool you are trying to remove is not referenced by other entities.

CRS-02558: Resource type 'string' may not be unregistered as there are types that are based on it.

Cause: Types may not be unregistered if they have derived types.

Action: Remove derived types first, then remove this one.

CRS-02559: Resource type 'string' may not be unregistered as it has the following resources:string

Cause: Types may not be unregistered if they have resources registered.

Action: Remove the specified resources first, then remove the type.

CRS-02560: Resource type 'string' does not exist

Cause: The resource type referenced does not exist.

Action: Please specify a correct type.

CRS-02561: Resource type 'string' may not be unregistered as it is referenced by resource 'string'

Cause: Types may not be unregistered if they are referenced in resource dependencies.

Action: Make sure there are no existing resources that reference this type in their dependencies.

CRS-02562: Resource 'string' cannot be relocated as it is not running

Cause: Only currently running resources can be relocated.

Action: Make sure the resource is running before issuing the request.

CRS-02563: Attempt to start resource 'string' on 'string' has failed. Will re-retry on 'string' now.

Cause: Undirected (no target member) start of a resource has failed for the server; a retry is in progress.

Action: None, this is an informational message.

CRS-02564: Failed to relocate resource 'string'. Will attempt to restore it on 'string' now.

Cause: Resource relocate operation was unable to relocate the resource to any of the possible servers.

Action: None, this is an informational message.

CRS-02565: Attempt to relocate resource 'string' to 'string' has failed. Will re-retry on 'string' now.

Cause: Undirected (no target member) relocate of a resource has failed for the server; a retry is in progress.

Action: None, this is an informational message.

CRS-02566: User 'string' does not have sufficient permissions to operate on resource 'string', which is part of the dependency specification.

Cause: User does not have permissions to operate on the resource as it will prevent the current resource from starting or staying online in future.

Action: The user performing the operation must have access privileges to operate on the entire resource dependency tree. The user must either be given those privileges by modifying the dependent resources' access rights or another user having permissions should perform this operation.

CRS-02567: Error while parsing the default value for attribute 'string'

Cause: The default value specified is not proper.

Action: Make sure the value is proper for its type.

CRS-02568: Base resource type name 'string' does not exist

Cause: The name of a base type used is not valid.

Action: Use an existing type as a base.

CRS-02569: Unsupported value type is used in attribute 'string'

Cause: An unsupported value type was specified in the attribute's definition.

Action: Use one of the supported types.

CRS-02570: Internal Error: Number of objects 'number' is different from number of lists 'number'

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CRS-02571: Dependency kind 'string' is specified more than once for resource 'string'

Cause: A dependency kind is used more than once in the profile of the resource.

Action: Combine multiple specifications of the same dependency kind into a single clause.

CRS-02572: 'string' is not a supported Special Value

Cause: The specified identifier is not a valid Special Value.

Action: Check the value for correctness.

CRS-02573: ACL entry for owner field is missing.

Cause: The complete value for the ACL attribute has been provided but it is missing a mandatory entry specifying permissions for the owner.

Action: Include permissions for the owner in the value of ACL attribute.

CRS-02574: ACL entry for primary group field is missing.

Cause: The complete value for the ACL attribute has been provided but it is missing a mandatory entry specifying permissions for the primary group.

Action: Include permissions for the primary in the value of ACL attribute.

CRS-02575: ACL entry for users other than the owner and those belonging to primary group is missing.

Cause: The ACL attribute is missing a mandatory entry specifying permissions for users other than the owner and those belonging to the primary group.

Action: Include permissions for other users in the value of ACL attribute.

CRS-02576: User 'string' is not a member of group 'string'

Cause: The group that the caller claims to be a member of has no such user by configuration.

Action: Make sure the group is configured to have the calling user as a member.

CRS-02577: Use of 'string' in attributes and values is not allowed

Cause: A disallowed character was detected.

Action: Retry without the disallowed character.

CRS-02578: Value of 'string' (number) may not be greater than that of 'string' (number)

Cause: The specified values do not make sense - one may not be less than the other.

Action: Use valid values.

CRS-02579: Value 'number' may not be less than 'number'

Cause: The value is less than the allowed minimum.

Action: Use a proper value.

CRS-02580: Value 'number' is neither 'number' nor 'number'

Cause: The value must be one of the two and it is neither.

Action: Use a proper value.

CRS-02581: Value 'string' is not any of the following 'string', 'string', 'string'

Cause: The value must be one of the ones specified and it is not.

Action: Use a proper value.

CRS-02582: Value 'string' does not follow expected format: \<n>\[s|d|m|w|h\]

Cause: The value specification does not follow required format.

Action: Use a proper value.

CRS-02583: Value 'number' must be in the 'number' - 'number' range

Cause: The value is not within the allowed range.

Action: Use a proper value.

CRS-02584: Value 'string' is not allowed here

Cause: The value is not proper in this context.

Action: Use a proper value.

CRS-02585: Deletion of built-in resource types is not allowed

Cause: An attempt was made to delete a built-in resource type.

Action: Removal of built-in types is not allowed.

CRS-02586: Deletion of a running resource 'string' requires the force option

Cause: An attempt was made to delete a resource that is still running.

Action: Stop the resource first using the 'crsctl stop resource' command. If the resource cannot be stopped, specify the force option to the 'crsctl delete' command.

CRS-02587: Attribute 'string' is internal and thus may not be overridden in type 'string'

Cause: Attributes defined in built-in resource types that are internal to the subsystem may never be overridden in user-defined resource types.

Action: Do not specify this attribute in the new user-defined type.

CRS-02588: A cyclical dependency on 'string' is detected from 'string' via type 'string'

Cause: There is a cycle in the dependency graph, via a resource type. Cycles are disallowed.

Action: Re-evaluate the dependency graph.

CRS-02589: Relation modifier 'string' is invalid for relation kind 'string'

Cause: An unexpected relation modifier is specified.

Action: Use defined modifiers only.

CRS-02590: A resource name may not be empty or contain spaces

Cause: A name must not be empty or contain space character(s).

Action: Specify a valid name.

CRS-02591: A server pool name may not be empty or contain spaces

Cause: A name must not be empty or contain space character(s).

Action: Specify a valid name.

CRS-02592: A type name may not be empty or contain spaces

Cause: A name must not be empty or contain space character(s).

Action: Specify a valid name.

CRS-02593: Comparator value 'string' in the filter specification is not supported

Cause: An unsupported comparator was supplied.

Action: Use a supported value.

CRS-02594: Filter specification 'string' is invalid

Cause: The filter specification invalid or empty.

Action: Provide a valid filter or do not specify you have one.

CRS-02595: Server pool 'string' has already been registered

Cause: A server pool with this name has already been registered.

Action: Provide a name that is not currently in use.

CRS-02596: Modifications to the 'string' attribute of server pools are not supported

Cause: Changes to the value of the attribute are not allowed.

Action: Create a different pool with the desired value and use it.

CRS-02597: Server 'string' may not be moved to pool 'string'

Cause: Because of one or more of configuration-related constrains, the move of the server is not a valid operation at the time.

Action: Re-evaluate the request's validity in the context of the entire error stack.

CRS-02598: Server pool 'string' is already at its maximum size of 'number'

Cause: The pool is already at the maximum.

Action: The request is impossible to execute.

CRS-02599: Server 'string' is not in a parent pool of 'string'

Cause: The server is not in a parent pool of the pool in question.

Action: The request is impossible to execute.

CRS-02600: Server 'string' is already in another top-level server pool

Cause: The server is already consumed by a different top-level pool and all such pools are exclusive as far as server ownership.

Action: The request is impossible to execute.

CRS-02601: Server 'string' is not explicitly mentioned as a candidate by server pool 'string'

Cause: The server is not in the list of names the pool allows as candidates.

Action: Use a server that is in the specified group.

CRS-02602: Server 'string' is in server pool 'string' which is exclusive with server pool 'string'

Cause: The server is already in a pool that's configured to be exclusive with the one at hand.

Action: The request is impossible to execute.

CRS-02603: Server 'string' cannot be assigned to server pool 'string' because it is not a top-level pool

Cause: Server movement is only supported between top-level server pools.

Action: The request is impossible to execute as such an action is not supported.

CRS-02604: Server 'string' is already assigned to server pool 'string'

Cause: Server movement makes no sense: the server is already in the target pool.

Action: Check the request validity.

CRS-02605: Server 'string' may not be relocated from server pool 'string' as the pool disallows transfers

Cause: The server pool is configured not to allow server transfers.

Action: Check the request validity.

CRS-02606: Server 'string' may not be relocated from server pool 'string' because it is not above its minimum size

Cause: Server pools of identical or higher importance may not be used to steal servers from if they are not above their minimum size.

Action: Update the configuration of server pools by either changing the importance or the minimum size or both and then re-submit the request.

CRS-02607: Attribute 'string' has not been specified on per-X basis for resource 'string'

Cause: The specified attribute has not been specified on per-X basis for this resource.

Action: Check the per-X attribute for the resource, fix and resubmit.

CRS-02608: Attribute 'string' is not a per-X value and cannot be removed

Cause: The specified attribute is not a per-X value.

Action: Check the per-X attribute for the resource, fix and resubmit.

CRS-02609: Server 'string' may not be relocated to server pool 'string' as the pool disallows transfers

Cause: The server pool is configured not to allow server transfers.

Action: Check the request validity.

CRS-02610: Server 'string' is unavailable

Cause: The server is not available at the moment.

Action: Check available servers and rerun the request with an active server.

CRS-02611: Server pool 'string' is built-in and may not be deleted

Cause: Built-in server pools may never be deleted.

Action: None

CRS-02612: Server pools do not have attribute named 'string'

Cause: An unsupported attribute was provided as part of the register or update request.

Action: Please double check the attributes that are supplied.

CRS-02613: Could not find resource 'string'.

Cause: An attempt was made to operate on a resource that is not registered.

Action: Check if the resource is registered.

CRS-02614: Could not find resource type 'string'.

Cause: An attempt was made to operate on a resource type that is not registered.

Action: Check if the resource type is registered.

CRS-02615: Could not find server pool 'string'.

Cause: An attempt was made to operate on a server pool that is not registered.

Action: Check if the server pool is registered.

CRS-02616: The owner of resource type 'string' does not have sufficient permissions to operate on resource type 'string', from which it is directly or indirectly derived.

Cause: Update of a resource type in the current manner is not allowed as it will severely limit operations on the current resource type and will potentially prevent resources of derived types from starting or staying online in future.

Action: If access privileges must be changed, then they need to changed bottom-up in a dependency.

CRS-02617: Incorrect value of attribute flags has been specified for attribute string. Only READONLY flag can be changed for a type attribute.

Cause: Attempt was made to update the flag on a resource type attribute. The only change allowed is to the readonly property of the attribute.

Action: Provide correct value of the attribute flag.

CRS-02618: Cannot change data type string of existing attribute string to type string.

Cause: Attempt was made to update the data type of attribute value.

Action: Data type of the attribute cannot be changed.

CRS-02619: Server pool 'string' may not be edited

Cause: The pool's attributes may not be edited.

Action: None

CRS-02620: Attribute 'string' of server pool 'string' may not be edited

Cause: Editing of the attribute of the server pool is not allowed.

Action: None

CRS-02621: Server 'string' is assigned to 'string' to which you have no permission. The operation is not authorized.

Cause: The operation requires making the specified server a placement candidate for the resources owned by the requesting user. However, this is not allowed because the user is not authorized to utilize the server.

Action: Either specify another server that that's in the pool you are authorized to use or request that a cluster administrator gives you access to the pool to which the server is currently assigned.

CRS-02622: Server 'string' is not assigned to any server pool and thus may only be specified by a cluster administrator

Cause: The operation makes use of the server that's not currently assigned to a server pool and the requesting user is not a cluster administrator. Because of that use of the server cannot be authorized at the moment.

Action: Either request a cluster administrator to perform the operation for you or wait until the server has joined the cluster and is assigned to a pool to which you have an x-permission.

CRS-02623: Server pool 'string' cannot accept server 'string' because its name is not specified in 'string'

Cause: Only servers whose names are mentioned in the attribute may be assigned to the pool.

Action: None

CRS-02624: One of 'string', 'string' must be specified when 'string' is 'string'

Cause: Neither of the parameters was specified.

Action: Please specify either of the two and re-submit.

CRS-02625: Owner of resource 'string' does not have execute permission to pool 'string' and may not use it

Cause: Resource profile references a server pool to which the owner of the resource does not have the X-permission.

Action: Either have the pool's permission changed appropriately or use a different pool.

CRS-02626: Owner of server pool 'string' does not have execute permission to parent server pool 'string'

Cause: Parent pool does not have the X-permission for the pool's parent.

Action: Either have the desired parent pool's permission changed appropriately or use a different pool.

CRS-02627: You must have execute permission on pool 'string' to relocate server 'string'

Cause: The client requesting the operation does not have proper permissions to the specified pool.

Action: Acquire required permissions or use another server/pool. Permissions can be added by an authorized user using 'crsctl setperm' command.

CRS-02628: Server pool 'string' may not be a parent of itself

Cause: An attempt was made to make a server pool a parent of itself.

Action: Re-evaluate the server pool dependencies.

CRS-02629: Only cluster administrators are allowed to create top-level server pools

Cause: An attempt was made to create a server pool that has no parent pools. Creation of such pools is only allowed for cluster administrators.

Action: Either acquire the role of cluster administrator or have one create the pool for you.

CRS-02630: Only cluster administrators are allowed to create local resources

Cause: An attempt was made to create a local resource which is only allowed for cluster administrators.

Action: Either acquire the role of cluster administrator or have one create the resource for you.

CRS-02631: Only cluster administrators are allowed to create cluster resources that may run anywhere in the cluster

Cause: An attempt was made to create a cluster resource that may run anywhere in the cluster which is only for cluster administrators.

Action: Either acquire the role of cluster administrator or have one create the resource for you.

CRS-02632: There are no more servers to try to place resource 'string' on that would satisfy its placement policy

Cause: After one or more attempts, the system ran out of servers that can be used to place the resource and satisfy its placement policy.

Action: None

CRS-02640: Required resource 'string' is missing.

Cause: A resource that's configured as required is not registered.

Action: Register the missing resource or update the dependency specification so as to the missing resource is not required for start.

CRS-02641: The value of 'string' cannot override that defined in the resource's type: 'string'

Cause: Agent filename cannot be overridden on per-resource basis.

Action: Define a sub-type that uses the agent. Then create a resource of this new type.

CRS-02642: Relocate resource is not a valid command for this configuration

Cause: A relocate command was issued in the configuration where it is not possible in principle.

Action: None

CRS-02643: The server pool(s) where resource 'string' could run have no servers

Cause: All of the server pools the resource uses (and has permissions to use) have no servers assigned.

Action: Either make sure there are active servers in the pools or use different pools for the resource.

CRS-02644: No hosting members of 'string' are either online or are allowed to be used by the resource

Cause: No server out of the enumerated as hosting members is online or, if it is, may be used by the resource.

Action: You need to either add more servers into the cluster or request permission to pools to which currently available servers are assigned.

CRS-02645: Cannot create resources of type 'string'

Cause: The type is abstract.

Action: Only concrete extensions of the type can be created.

CRS-02646: 'string' must have a default value if specified

Cause: This attribute must have a default value if specified.

Action: Modify the type definition so that the attribute is removed or has a valid default value.

CRS-02647: Attribute 'string' may not be a negative value

Cause: A negative value was provided for an attribute which only accepts non-negative values.

Action: Specify a non-negative number.

CRS-02649: Attribute 'string' of 'string' is internally managed and may not be specified

Cause: An internal attribute was specified as part of an add/modify request.

Action: Re-execute the request without any internal attribute.

CRS-02650: Resource 'string' is configured to run only on 'string' and cannot be started on 'string'

Cause: An attempt was made to start a resource on a server where it cannot run given its placement configuration.

Action: Make sure you start resources where they are configured to run.

CRS-02651: Resource alias 'string' must use special values to be unique for each server

Cause: Resource alias name must resolve to a unique identifier for every server in the cluster. To achieve that, special values that yield different values on for each server must be used.

Action: You need to special an alias with special variables that will make it unique for every server.

CRS-02652: string is a resource and only resource instances can be relocated.

Cause: An attempt was made to relocate a resource.

Action: Make sure you supply a resource instance rather than a resource.

CRS-02653: Special value evaluation must be associated with a resource instance

Cause: Because some special values are per-server, each special value evaluation request must be associated with a resource instance.

Action: Please specify a server for the resource using -k or -n.

CRS-02660: Resource 'string' or all of its instances are disabled

Cause: This is an API return code for requests that cannot be performed because the resource is disabled.

Action: Look at the detailed error messages that should always accompany this error.

CRS-02661: All instances of resource 'string' are disabled

Cause: All instances of the resource instances are disabled.

Action: In order to change a resource state through CRS, its instances need to be enabled.

CRS-02662: Resource 'string' is disabled on server 'string'

Cause: The resource was disabled on the specified server.

Action: Either re-enable, or use a different server.

CRS-02663: Resource instance of 'string' with string=number, string=number is disabled

Cause: The resource instance whose cardinality/degree is specified is disabled.

Action: Either re-enable or use a different resource instance.

CRS-02664: Resource 'string' is already running on 'string'

Cause: The resource is already running everywhere it may run.

Action: None

CRS-02665: Resource 'string' is disabled on 'string'

Cause: The resource is disabled on every server it is configured to start on.

Action: None

CRS-02666: Resource 'string' is disabled on 'string' and is already running on 'string'

Cause: The resource is disabled on every server it is configured to start on.

Action: None

CRS-02667: Resource 'string' with string=string may only run on servers assigned to string and string, both of which are empty

Cause: The resource's placement policy only allows it to run on servers assigned to the specified pools, and they are all empty.

Action: Either change the placement policy of the resource, or change the cluster configuration so that there are servers in those pools.

CRS-02668: The value of attribute 'string' (number) may not not be above 'number'

Cause: Attribute value specified is above the allowed maximum.

Action: Use a value below the specified maximum.

CRS-02669: The value is out of range. Maximum allowed value is 'number'

Cause: Attribute value is out of the valid range.

Action: The value needs to be in a valid range.

CRS-02670: Unable to start/relocate 'string' because 'string' has a stop-time 'string' dependency on it

Cause: Start/relocate of the resource is impossible because another resource has a stop-time dependency on it and the action requires stopping that resources.

Action: This message will usually be coupled with another one that details the nature of the problem with the other resource. Please follow up on the action recommended for that message.

CRS-02671: Error processing attribute 'string': string

Cause: The value specified for the attribute is inappropriate or invalid.

Action: Review the value, correct the problem and re-submit the request.

CRS-02672: Attempting to start 'string' on 'string'

Cause: This is a status message.

Action: None

CRS-02673: Attempting to stop 'string' on 'string'

Cause: This is a status message.

Action: None

CRS-02674: Start of 'string' on 'string' failed

Cause: This is a status message.

Action: None

CRS-02675: Stop of 'string' on 'string' failed

Cause: This is a status message.

Action: None

CRS-02676: Start of 'string' on 'string' succeeded

Cause: This is a status message.

Action: None

CRS-02677: Stop of 'string' on 'string' succeeded

Cause: This is a status message.

Action: None

CRS-02678: 'string' on 'string' has experienced an unrecoverable failure

Cause: This is a status message.

Action: Perform whatever steps necessary to reset the state.

CRS-02679: Attempting to clean 'string' on 'string'

Cause: This is a status message.

Action: None

CRS-02680: Clean of 'string' on 'string' failed

Cause: This is a status message.

Action: None

CRS-02681: Clean of 'string' on 'string' succeeded

Cause: This is a status message.

Action: None

CRS-02682: It is locked by 'string' for command 'string' issued from 'string'

Cause: This message is generated for operations that have a locking conflict.

Action: None

CRS-02683: It is locked by 'string' for command 'string'

Cause: This message is generated for operations that have a locking conflict.

Action: None

CRS-02714: 'string' is specified multiple times in 'string' of 'string'

Cause: The specified value is specified multiple times.

Action: Remove duplicates and retry.

CRS-02715: Update to attribute AGENT\_FILENAME is not currently supported. Please recreate the resource type with new value.

Cause: Attempt was made to update AGENT\_FILENAME attribute.

Action: Delete existing resource type and add it back with the new value.

CRS-02716: Failure threshold exhausted for resource 'string'

Cause: The resource instance has failed more times than allowed in the specified time interval. It will not be restarted automatically.

Action: Please identify and fix the problem. Restart the resource manually thereafter.

CRS-02717: Server 'string' is not in any of the server pool(s) hosting resource 'string'

Cause: An attempt was made to start a resource on a server that is not currently an active server in any of the resource's server pool(s).

Action: Use a server name that is currently an active server of the resource's server pools(s).

CRS-02718: Server 'string' is not a hosting member of resource 'string'

Cause: An attempt was made to start the resource on a server not listed as a hosting member of the resource.

Action: Use a server name that is listed as a hosting member.

CRS-02719: Resource 'string' may not be started on server 'string' because the server is not in either 'string' or 'string' server pools

Cause: The resource's placement policy only allows it to run in the specified server pools. An attempt was made to start it on a server assigned to a different pool.

Action: Either use a different server or set the value of SERVER\_POOLS to \*, which will allow the resource to run on any server.

CRS-02720: 'string' is a resource alias for 'string' and cannot be updated

Cause: An attempt was made to update a resource as if it were a resource.

Action: Please update the resource which this alias refers to instead.

CRS-02721: 'string' is a resource alias for 'string' and cannot be unregistered

Cause: An attempt was made to unregister a resource alias as if it were a resource.

Action: Either unregister the resource which this alias refers to or modify its ALIAS\_NAME attribute to not have a resource alias.

CRS-02722: The instance of resource 'string' may only run on 'string'; check on 'string' is unnecessary

Cause: A check was issued on a server for a resource instance that may only run on a particular server.

Action: Please issue a check on the server where the resource instance is supposed to be run.

CRS-02723: No instance of resource 'string' found on 'string'

Cause: A check was issued on a server for a resource which does not have any offline instances and no running instances on that server.

Action: Please issue a check on a server where a resource instance might be running.

CRS-02724: Modifications to the built-in resource type 'string' are not allowed

Cause: An attempt was made to modify a built-in resource type.

Action: Modification of built-in resource types is not allowed.

CRS-02725: User string does not have permission to operate on resource string.

Cause: Access control list on the resource do not permit the user to operate on the resource.

Action: Access privileges on the resource must be honored or this user must be given appropriate permissions.

CRS-02726: Invalid permissions specified for access control.

Cause: Access permissions are specifies using 'r', 'w', 'x' and '-' characters to indicate read, write and execute permissions. '-' indicates no access of any kind.

Action: Check format for the permissions string and re-run the command with the correct string.

CRS-02727: Acl entry 'string' has been specified more than once.

Cause: Access permissions for the entry have been specified more than once.

Action: Specify permissions for each entry only once and rerun the command.

CRS-02728: A resource type with the name 'string' is already registered

Cause: A resource type with such name is already registered.

Action: Use a unique name for the new resource type.

CRS-02729: Attribute 'string' cannot be overridden for a resource type

Cause: An attribute was specified that is not allowed in a resource type.

Action: Do not use the attribute specified in the error message for a resource type.

CRS-02730: Resource 'string' depends on resource 'string'

Cause: An attempt was made to unregister a resource that is referenced by another resource in the dependency specification(s).

Action: Either remove the reference to this resource or the other resource first. Alternatively, the operation can be retried with a force option.

CRS-02731: Resource 'string' is already running on server 'string'

Cause: The resource is already running on the server; relocate is impossible.

Action: Select another server.

CRS-02732: Resource 'string' is already starting on server 'string'

Cause: The resource is currently starting on the server.

Action: Wait for the request to complete.

CRS-02733: Failed to stop all required resources on 'string'; the server will be restored into the original server pool(s)

Cause: In order to successfully relocate a server, all resources that cannot run in the new server pool(s) must be stopped. That did not happen and thus the server was placed back into the its original server pool(s).

Action: Manual intervention in stopping resources is required. The operation can be retried thereafter. Alternatively, another server can be used.

CRS-02734: Failed to stop all required resources on 'string'; the server will stay in RECONFIGURING state

Cause: In order to successfully relocate a server, all resources that cannot run in the new server pool(s) must be stopped. Since that did not happen, the server will be kept in the RECONFIGURING state until the resources that did not stop have been stopped or unregistered.

Action: Manually stop the resources that did not stop or unregister them.

CRS-02735: The operation requires relocating resource 'string' from server 'string'

Cause: The operation would end up relocating the resource and the force option is not specified.

Action: Add more servers to the cluster, stop or relocate the resource, or use the force option for the same command.

CRS-02736: The operation requires stopping resource 'string' on server 'string'

Cause: The operation would end up stopping the resource and the force option is not specified.

Action: Add more servers to the cluster, stop or relocate the resource, or use the force option for the same command.

CRS-02737: Unable to register server pool 'string' as this will affect running resources, but the force option was not specified

Cause: One or more running resources would be affected by the operation.

Action: Add more servers to the cluster, stop or relocate the resources mentioned right before this error, or use the force option for the same command.

CRS-02738: Unable to modify server pool 'string' as this will affect running resources, but the force option was not specified

Cause: One or more running resources would be affected by the operation.

Action: Add more servers to the cluster, stop or relocate the resources mentioned right before this error, or use the force option for the same command.

CRS-02739: Unable to relocate server 'string' as this will affect running resources, but the force option was not specified

Cause: One or more running resources would be affected by the operation.

Action: Add more servers to the cluster, stop or relocate the resources mentioned right before this error, use a different server, or use the force option for the same command.

CRS-02740: Failed to relocate server 'string' to server pool 'string'. The server has been restored to original server pool(s).

Cause: In order to successfully relocate a server, all resources that cannot run in the new server pool(s) must be stopped. That did not happen and thus the server was placed back into the its original server pool(s).

Action: Manual intervention in stopping or unregistering resources is required. The operation can be retried thereafter. Alternatively, another server can be used.

CRS-02741: A value must be specified for attribute 'string'

Cause: The attribute was not given a value.

Action: Provide a value and retry.

CRS-02742: The update of resource 'string' would lose track of one or more running instances

Cause: An attempt was made to modify the configuration of the resource such that one or more currently running instance will be lost track of (the new configuration would change the resource to have fewer instances).

Action: Stop the resource and resubmit.

CRS-02743: Unable to register resource 'string' as this will affect running resources, but the force option was not specified

Cause: One or more running resources would be affected by the operation.

Action: Add more servers to the cluster, stop or relocate the resources mentioned right before this error, or use the force option for the same command.

CRS-02744: Unable to modify resource 'string' as this will affect running resources, but the force option was not specified

Cause: One or more running resources would be affected by the operation.

Action: Add more servers to the cluster, stop or relocate the resources mentioned right before this error, or use the force option for the same command.

CRS-02745: Unable to relocate server string because it results in violation of a pool string constraint

Cause: The requested move was rejected because it would cause either the source or target pool (or both) to violate a pool size constraint, as indicated.

Action: Either change the pool size constraint(s) to accommodate your intent with this move, or choose a different server to move.

CRS-02746: Cannot act on the instance of resource 'string' which is last known to have run on 'string' where Cluster Ready Services are not properly functioning

Cause: The resource had been running on the server in the past but currently there's no way to know if it's still running there because the Cluster Ready Services daemon does not appear to be running on the server. To prevent possible configuration violation, any attempt to start the resource instance on another server is rejected.

Action: The underlying problem preventing Cluster Resource Services on the server from functioning properly must be addressed. Only then the resources that used to run there can be operated on again. Alternatively, the server may be shut down or the clusterware stack on it stopped completely.

CRS-02747: Server reconfiguration has failed to stop resources 'string' on server 'string'. Resources that did not stop must be stopped or unregistered manually. Details at string in string.

Cause: The specified resources could not be stopped.

Action: Stop the specified resources manually using and retry the last action.

CRS-02748: Failed to stop resource 'string' during server reconfiguration on server 'string'.

Cause: The specified resources could not be stopped.

Action: Stop the specified resources manually and retry the last action.

CRS-02749: A write of OCR server data 'string' failed. Details at string in string.

Cause: Could not persist data to OCR.

Action: Use the ocrconfig and ocrcheck utilities to detect errors in OCR. If problems exist, the registry may need to be recovered or restored.

CRS-02750: Cardinality violation detected on server 'string', resource 'string' is in unexpected state. Details at string in string.

Cause: The specified resource was in an unexpected state.

Action: Manually restart the resource.

CRS-02751: Cannot create new resource, the resource type 'string' is not supported. Details at string in string.

Cause: The specified resource had an incorrect base type.

Action: Check the attributes for the resource and add it using crsctl again.

CRS-02752: Unable to write event sequence number to OCR. Details at string in string.

Cause: Could not update OCR with event sequence number.

Action: Use the ocrconfig and ocrcheck utilities to detect errors in OCR. If problems exist, the registry may need to be recovered or restored.

CRS-02753: Timed out waiting for the server pools to be unfrozen.

Cause: Timed out while waiting for a client to unfreeze the pools it froze.

Action: If the problem persists, contact Oracle Support Services.

CRS-02754: Unable to change locks for a running operation 'string'. Details at string in string.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CRS-02755: Error reading type definition for type 'string'. Details at string in string.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CRS-02756: Invalid tag for command 'string'. Details at string in string.

Cause: An invalid command was received by the CRS daemon.

Action: Contact Oracle Support Services.

CRS-02757: Command 'string' timed out waiting for response from the resource 'string'. Details at string in string.

Cause: Timeout occurred while waiting for response to specified command.

Action: Check that the server targeted by the command is online and responsive.

CRS-02758: Resource 'string' is in an unknown state.

Cause: Unable to determine the current state of specified resource.

Action: Manually restart the resource.

CRS-02759: Failed to read repository key for NLS language 'string'. Details at string in string.

Cause: The key for the specified language could not be read from OCR.

Action: Use the ocrconfig and ocrcheck utilities to detect errors in OCR. If problems exist, the registry may need to be recovered or restored.

CRS-02760: Policy engine failed to initialize internal types. Details at string in string.

Cause: Error during initialization of internal data.

Action: If the problem persists, contact Oracle Support Services.

CRS-02761: Consistency problem in registry while processing resource 'string'. Details at string in string.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CRS-02762: Unable to find type 'string' in registry while processing resource 'string'. Details at string in string.

Cause: This is an internal error.

Action: Contact Oracle Support Services

CRS-02763: Error while reading resources. Details at string in string.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CRS-02764: CRSADMIN and CRSUSER keys are not in repository. Details at string in string.

Cause: Error with repository. Required keys are not present.

Action: Use the ocrconfig and ocrcheck utilities to detect errors in OCR. If problems exist, the registry may need to be recovered or restored.

CRS-02765: Resource 'string' has failed on server 'string'.

Cause: The specified resource was no longer running.

Action: The resource will be automatically brought back online. Use crsctl to confirm that it is online.

CRS-02766: Received state change for disabled resource 'string' from server 'string'.

Cause: Received command to change state for a resource that was disabled.

Action: None

CRS-02767: Resource state recovery not attempted for 'string' as its target state is OFFLINE

Cause: Target state for resource was OFFLINE. Clusterware will not attempt to recover it.

Action: None

CRS-02768: Failure threshold exhausted by resource 'string'.

Cause: The specified resource failed too many times. No further restart attempts will be made.

Action: Fix the underlying cause of resource failure and manually restart the resource.

CRS-02769: Unable to failover resource 'string'.

Cause: Could not failover the specified resource.

Action: Restart the resource manually.

CRS-02770: Resource target 'string' is offline; will not restart.

Cause: The target state of the specified resource was offline.

Action: None

CRS-02771: Maximum restart attempts reached for resource 'string'; will not restart.

Cause: Specified resource had been restarted too many times.

Action: Change the maximum restart parameter of the resource, and restart it manually.

CRS-02772: Server 'string' has been assigned to pool 'string'.

Cause: The specified server had been assigned to a server pool.

Action: None

CRS-02773: Server 'string' has been removed from pool 'string'.

Cause: The specified server had been removed from a server pool.

Action: None

CRS-02774: Failed to save resource 'string' to the repository. Details at string in string.

Cause: Could not update repository with resource details.

Action: Use the ocrcheck utility to detect errors in OCR. If problems exist, the registry may need to be recovered or restored.

CRS-02775: Failed to update resource 'string'. Details at string in string.

Cause: Could not update repository with resource details.

Action: Use the ocrcheck utility to detect errors in OCR. If problems exist, the registry may need to be recovered or restored.

CRS-02776: Failed to update server pool 'string'. Details at string in string.

Cause: Could not update repository with server pool details.

Action: Use the ocrcheck utility to detect errors in OCR. If problems exist, the registry may need to be recovered or restored.

CRS-02777: Failed to delete resource 'string' from repository. Details at string in string.

Cause: Unable to update resource details in repository.

Action: Use the ocrcheck utility to detect errors in OCR. If problems exist, the registry may need to be recovered or restored.

CRS-02778: Failed to delete server pool 'string' from repository. Details at string in string.

Cause: Could not update repository with server pool details.

Action: Use the ocrcheck utility to detect errors in OCR. If problems exist, the registry may need to be recovered or restored.

CRS-02779: Failed to delete type 'string' from repository. Details at string in string.

Cause: Failed to update repository.

Action: Use the ocrcheck utility to detect errors in OCR. If problems exist, the registry may need to be recovered or restored.

CRS-02780: Could not find Access Control List for resource 'string'. Details at string in string.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CRS-02781: Error during registration for resource 'string'. Details at string in string.

Cause: Error occurred during registration callback of new resource.

Action: Contact Oracle Support Services.

CRS-02782: Unable to find attributes for resource 'string'. Details at string in string.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CRS-02783: Internal error in local placement policy for resource 'string'. Details at string in string.

Cause: Internal error in CRS Policy Engine.

Action: Contact Oracle Support Services.

CRS-02784: Internal error, invalid server 'string' in local placement policy. Details at string in string.

Cause: Internal error in CRS Policy Engine.

Action: Contact Oracle Support Services.

CRS-02785: Failed to register resource 'string'. Details at string in string.

Cause: Could not update repository with resource details.

Action: Use the ocrcheck utility to detect errors in OCR. If problems exist, the registry may need to be recovered or restored.

CRS-02786: Failed to register server pool 'string'. Details at string in string.

Cause: Could not update repository with server pool details.

Action: Use the ocrcheck utility to detect errors in OCR. If problems exist, the registry may need to be recovered or restored.

CRS-02787: Server pool 'string' has fallen below its minimum size. Details at string in string.

Cause: The specified server pool has fallen below its minimum size and will be reconfigured.

Action: None

CRS-02788: Server reconfiguration failed to stop resources 'string'. The server 'string' has been restored into the original pool(s).

Cause: The specified resources could not be stopped.

Action: Stop the specified resources manually and retry the last action.

CRS-02789: Cannot stop resource 'string' as it is not running on server 'string'

Cause: An request to stop a resource on a server where it is not running was received

Action: Check the current state of the resource; it should no longer be running on that server.

CRS-02790: Starting shutdown of Cluster Ready Services-managed resources on 'string'

Cause: Shutdown of Cluster Ready Services and the resources it manages has started on the specified server.

Action: None

CRS-02791: Starting shutdown of Oracle High Availability Services-managed resources on 'string'

Cause: Shutdown of Oracle High Availability Services and the resources it manages has started on the indicated server.

Action: None

CRS-02792: Shutdown of Cluster Ready Services-managed resources on 'string' has completed

Cause: Shutdown of Cluster Ready Services and the resources it manages on the indicated server has completed.

Action: None

CRS-02793: Shutdown of Oracle High Availability Services-managed resources on 'string' has completed

Cause: Shutdown of Oracle High Availability Services and the resources it manages has completed on the indicated server.

Action: None

CRS-02794: Shutdown of Cluster Ready Services-managed resources on 'string' has failed

Cause: The failure is associated with one or more of the resources affected by this command on the indicated server."

Action: Error message(s) preceding this one should have the details about the resources that refused to shut down. Either manually stop those resources or retry with the force option.

CRS-02795: Shutdown of Oracle High Availability Services-managed resources on 'string' has failed

Cause: The failure is associated with one or more of the resources affected by this command on the indicated server."

Action: Error message(s) preceding this one should have the details about the resources that refused to shut down. Either manually stop those resources or retry with the force option.

CRS-02796: The command may not proceed when Cluster Ready Services is not running

Cause: This command must stop Cluster Ready Services-managed resources. However, Cluster Ready Services is not running, which does not mean its resources are not running.

Action: The underlying reason for Cluster Ready Services not running needs to be resolved and the command retried. Alternatively, the command can be retried with the force option.

CRS-02797: Shutdown is already in progress for 'string', waiting for it to complete

Cause: Another shutdown command was issued for the indicated server in the past and it is currently in progress. This command will wait until the original command completes and then complete as well.

Action: None

CRS-02798: State change received for resource 'string' from unexpected server 'string'. Details at 'string' in 'string'.

Cause: A state change was reported for an instance of the resource from a server where the resource was never started.

Action: Shutdown the resource on the unexpected server

CRS-02799: Failed to shut down resource 'string' on 'string'

Cause: Shut down failed because the listed resource failed to stop.

Action: Error message(s) preceding this one should have the details about the resources that refused to shut down. Either manually stop those resources or retry with the force option.

CRS-02800: Cannot start resource 'string' as it is already in the INTERMEDIATE state on server 'string'

Cause: An attempt was made to start a resource that is already in the INTERMEDIATE state.

Action: Determine why the resource is in the INTERMEDIATE state based on the value of the STATE\_DETAILS attribute. If it is due to a check timeout, no action is needed. Otherwise, manual intervention is required to bring the resource out of the INTERMEDIATE state.

CRS-02801: No instance of the resource 'string' should be running

Cause: An attempt was made to relocate resource and the resource's instances to be relocated have TARGET=OFFLINE.

Action: Restart the resource to change the value of the TARGET attribute to ONLINE. Examining the value of the INTERNAL\_STATE attribute can be used to determine if the instances are being operated on currently.

CRS-02802: Purging events not published within 15 minutes

Cause: The events could not be published to the Event Manager Daemon either because it is down or there are errors doing the publish.

Action: Check the status of the Event Manager Daemon.

CRS-02803: Attribute 'string' has already been declared in a derived type 'string'

Cause: An attempt was made to add a new attribute definition to a resource type that has an identically named attribute already defined in one or more derived types. Attributes declared in base types can be overridden in derived ones, but the opposite is not allowed.

Action: Pick a different attribute name or delete the derived type(s), resubmit, and then add derived types back.

CRS-02805: Unable to start 'string' because it has a 'string' dependency on resource type 'string' and no resource of that type can satisfy the dependency

Cause: Start/relocate of the resource is impossible because it has a dependency on a resource type no resource of which can currently be used to satisfy the dependency.

Action: This message will normally be coupled with one or more other messages that detail the nature of the problem for each existing resource of the type.

CRS-02806: Failed to create stop operation for resource 'string'

Cause: Creating the stop operation did not complete successfully.

Action: Error message(s) preceding this one should have more details about the problem. Try shutting down the resource manually, or retrying with the force option.

CRS-02807: Resource 'string' failed to start automatically.

Cause: This message comes up when the automatic start for the resource has failed during a reboot of the cluster node or restart of the clusterware stack. See previous resource specific messages for more details.

Action: Use 'crsctl start resource' to start the resource manually.

CRS-02847: Authorization failure: operating system user 'string' does not exist on server 'string'

Cause: The specified operating system user or group does not exist on the specified server. Cluster Ready Services requires that all users or groups used by the resource it manages exist on each server of the cluster.

Action: Add the specified operating system user or group on the specified server.

CRS-02848: Error while reading resources: Resource: 'string'. Error: string. Details at string in string.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CRS-02849: Authorization failure: Resource 'string'

Cause: A resource operation could not be performed because authorization checking failed. This may be due to inconsistency of user or group IDs across cluster nodes.

Action: Check the ownership, group, and permissions associated with the resource and ensure that the associated operating system user and group definitions are consistent on all cluster nodes.

CRS-02878: Failed to restart resource 'string'

Cause: An attempt to start the resource has failed.

Action: If failover is not enabled, try manually starting the resource on a different server. If failover is enabled, the resource has been failed over, and any problems are reported in subsequent messages.

CRS-02879: Cannot update the ALERT\_TEMPLATE attribute, because the input is not valid

Cause: A resource update operation could not be performed, because the input value is not valid.

Action: Ensure that valid attributes are specified in a space separated list.

CRS-02907: Resource 'string' is not completely configured and cannot be operated upon.

Cause: A request was made without specifying the PID\_FILES or EXECUTABLE\_NAMES attribute.

Action: Specify a value for the PID\_FILES or EXECUTABLE\_NAMES attribute, or specify values for STOP\_PROGRAM, CHECK\_PROGRAM and CLEAN\_PROGRAMS attributes.

CRS-04000: Command string failed, or completed with errors.

Cause: The specified command did not complete successfully. If the command performs multiple operations internally, one or more of those operations experienced an error that is reported in a previous message.

Action: Examine the error message(s) preceding this message and correct the problem(s) they describe.

CRS-04016: Key 'string' is missing in the OCR.

Cause: Internal error.

Action: Contact Oracle Support Services.

CRS-04017: Failed to get the value for key 'string' from OCR.

Cause: Internal error.

Action: Contact Oracle Support Services.

CRS-04038: Cannot delete invalid user 'string' from CRS Admin list.

Cause: An attempt was made to delete an invalid username from the CRS Admin list.

Action: Reissue the command with a valid username.

CRS-04044: CRS Administrator List: string

Cause: Output message, not an error.

Action: None

CRS-04046: Invalid Oracle Clusterware configuration.

Cause: The Oracle Clusterware configuration is invalid.

Action: Configure Oracle Clusterware or Oracle Restart.

CRS-04047: No Oracle Clusterware components configured.

Cause: No Oracle Clusterware components have been configured.

Action: Configure Oracle Clusterware or Oracle Restart.

CRS-04200: Failed to initialize a security context during wallet IPMI credentials creation.

Cause: Internal error.

Action: Contact Oracle Customer Support.

CRS-04201: Hash context initialization failure during wallet IPMI credentials creation

Cause: Internal error.

Action: Contact Oracle Customer Support.

CRS-04202: String hashing failed during wallet credentials creation

Cause: Internal error.

Action: Contact Oracle Customer Support.

CRS-04203: Hashing creation error during wallet credentials creation

Cause: Internal error.

Action: Contact Oracle Customer Support.

CRS-04204: Failed to initialize the IPMI credentials wallet: string

Cause: While trying to initialize the IPMI credentials wallet, the cluster wallet subsystem returned an unexpected error. The error is included with this message.

Action: See the documentation and follow the directions for the displayed error.

CRS-04205: Failed to open the IPMI credentials wallet. The wallet does not exist.

Cause: The wallet does not exist.

Action: Configure the wallet for the IPMI device using 'crsctl set'\\n"

CRS-04206: Error reading IPMI credentials wallet: 'string'

Cause: While trying to read the IPMI credentials wallet, the cluster wallet subsystem returned an unexpected error. The error is included with this message.

Action: See the documentation and follow the directions for the displayed error.

CRS-04207: Error writing IPMI credentials wallet: 'string'

Cause: While trying to write the IPMI credentials wallet, the cluster wallet subsystem returned an unexpected error. The error is included with this message.

Action: See the documentation and follow the directions for the displayed error.

CRS-04208: Unexpected error encountered during lookup of IPMI credentials in the wallet

Cause: Possible corruption in wallet or internal error.

Action: Reconfigure the IPMI wallet using 'crsctl set' and then retry the operation. If the retry fails call customer support.

CRS-04209: IPMI credentials not contained in the wallet

Cause: The wallet has not been configured.

Action: Configure the wallet for the IPMI device using 'crsctl set'\\n

CRS-04210: Failed to obtain the length of IPMI credentials while accessing the wallet.

Cause: Possible corruption in wallet or internal error.

Action: Reconfigure the IPMI wallet using "crsctl set" and then retry the operation. If the retry fails call customer support.

CRS-04211: Failed to allocate memory

Cause: Insufficient system memory resources.

Action: Correct the system memory resources problem and retry.

CRS-04212: Failed to obtain the secret from the wallet.

Cause: Possible corruption in wallet or internal error.

Action: Reconfigure the IPMI wallet using "crsctl set" and then retry the operation. If the retry fails call customer support.

CRS-04213: Secret from wallet has incorrect size

Cause: Possible corruption in wallet or internal error.

Action: Reconfigure the IPMI wallet using "crsctl set" and then retry the operation. If the retry fails call customer support.

CRS-04214: crsctl string and string wallet versions of IPMI do not match.

Cause: A mismatch occurred between the IPMI versions of crsctl and the Cluster Synchronization Services Daemon.

Action: Check proper installation and configuration of crsctl and the Cluster Synchronization Services Daemon.

CRS-04215: Wallet secret encoding error

Cause: Internal error.

Action: Contact Oracle Customer Support.

CRS-04216: Unexpected error configuring the wallet contents

Cause: Possible corruption in wallet or internal error.

Action: Reconfigure the IPMI wallet using "crsctl set" and then retry the operation. If the retry fails call customer support.

CRS-04217: Unexpected error saving IPMI credentials wallet: string

Cause: While trying to save the IPMI credentials wallet, the cluster wallet subsystem returned an unexpected error. The error is included with this message.

Action: See the documentation and follow the directions for the displayed error.

CRS-04218: Unable to access an IPMI device on this system

Cause: A test for the availability of an IPMI device failed. This can occur if:

\- the IPMI device driver is not installed,

\- the installed device driver is not supported by Oracle,

\- IPMI is not supported on this platform or operating system,

\- no IPMI device is present, or

\- an IPMI device is present but not configured.

Action: Verify that IPMI hardware supporting IPMI version 1.5 or greater is present and supported on this server, that the IPMI device is configured and the device driver is properly installed.

CRS-04219: Failed to open the wallet. User must be the creator of the wallet: string

Cause: Not the owner/creator of the wallet. The cluster wallet subsystem returned an error included with this message.

Action: Retry as the owner/creator of the wallet. If necessary, also see the documentation and follow the directions for the displayed error.

CRS-04221: Must specify a password

Cause: No password entered in response to password prompt.

Action: Specify a password which matches the local servers IPMI BMC password.

CRS-04222: Supplied password was greater than number bytes

Cause: The password specified was too long for the IPMI device.

Action: Supply a password with a length no greater than the indicated size while still matching the password used to configure the IPMI device. Retry.

CRS-04223: Username is greater than number bytes

Cause: The username specified was too long for the IPMI device.

Action: Supply a username with a length no greater than the indicated size while still matching the username used to configure the IPMI device. Retry.

CRS-04224: Unable to communicate with the Cluster Synchronization Services daemon to update IPMI values.

Cause: crsctl modified the IPMI credential wallet but could not notify the Cluster Synchronization Services Daemon.

Action: Retry after assuring the Cluster Synchronization Services Daemon is functioning by executing csscheck.

CRS-04225: Unexpected authorization error while creating the IPMI credentials wallet: string

Cause: Error creating the IPMI credentials wallet. The cluster wallet subsystem returned an unexpected error. The error is included with this message.

Action: See the documentation and follow the directions for the displayed error and retry.

CRS-04226: Unexpected authorization error while saving the IPMI credentials wallet: string

Cause: While attempting to save the IPMI credentials wallet, the cluster wallet sub-system returned an authorization error. The text of the authorization error text is included with this message. This error was unexpected, and might have been due to an internal error, because wallet creation should be authorized for anyone, and, if the wallet was pre-existing, it had already been read after proper authorization checks.

Action: Consult the documentation for the included message to investigate the root cause of the authorization error, and retry the "set" operation if indicated. If this fails, contact Oracle Support.

CRS-04227: Configuration data stored but IPMI IP address is required to complete the change. The change cannot be validated until the information is complete.

Cause: Not proceeding with Client's IPMI login change request because all information such as IPMI username, password and IP address need to be present.

Action: Please execute 'crsctl set css ipmiaddr' from crsctl.

CRS-04228: Value of attribute 'string' is missing

Cause: The user did not provide a value for the attribute.

Action: Provide a value using the format \<attrName>=\<value>, where \<value> may be empty single quotes.

CRS-04229: The IPMI information change was successful

Cause: The IPMI address and authorization information have been validated and the change completed.

Action: None required.

CRS-04230: A device was found where the IPMI device should be, but the device is not an IPMI device

Cause: The IPMI driver may not be configured or supported by this host.

Action: Check the configuration of the IPMI driver and verify the server's support of an IPMI version 1.5 or greater device.

CRS-04231: IPMI device and/or driver found

Cause: An IPMI device and/or device driver was identified on the machine. Detection mechanisms for IPMI hardware vary by platform.

Action: None required.

CRS-04232: Configuration data stored but IPMI authorization information is required to complete the change. The change cannot be validated until the information is complete.

Cause: Not proceeding with Client's IPMI login change request because all information (IPMI username, password and IP address) need to be present.

Action: Please execute 'crsctl set css ipmiadmin' from crsctl.

CRS-04233: New IPMI configuration data stored, but failed validation by remote node.

Cause: The supplied configuration data was stored in the Oracle registry, but the resulting configuration could not be used for IPMI access by a remote node. The stored IP address and/or IPMI admin credentials is/are incorrect.

Action: The validating node is identified in the CRS alert log, and further details can be found in the alert log on that node. Verify the credentials for the local IPMI device and reset the configuration using commands 'crsctl set css ipmiadmin' and 'crsctl set css ipmiaddr'

CRS-04234: IPMI configuration unset and registry entries deleted.

Cause: Requested operation successful. However, if the CRS stack was able to access and use the deleted configuration data, it will continue to do so until it is restarted.

Action: None required. Enter new configuration data or restart the CRS stack if desired.

CRS-04235: Failed to delete the IPMI configuration from the Oracle Registry: 'string'

Cause: An error was encountered in the Oracle registry sub-system while trying to clear IPMI configuration and delete the IPMI configuration entries. The detailed error message is included with this message.

Action: See the documentation and follow the directions for the displayed error.

CRS-04236: Oracle Clusterware configured to use IPMI

Cause: The Oracle Registry contains complete configuration data for IPMI.

Action: None required.

CRS-04237: Oracle Clusterware is not fully configured to use IPMI

Cause: The Oracle Registry does not contain complete configuration data for IPMI.

Action: None required.

CRS-04251: Failed to change the discovery string

Cause: An internal error happened during this operation.

Action: Please contact Oracle Support Services.

CRS-04252: Failed to update the profile with the new discovery string

Cause: An internal error happened when updating the discovery string in the profile.

Action: Please contact Oracle Support Services.

CRS-04253: The discovery string can not be changed because the voting files are on ASM

Cause: Changing the discovery string is allowed only if the voting files are not on ASM.

Action: None

CRS-04254: The discovery string has already been set to this value

Cause: The value being passed is the same as the current discovery string.

Action: Pass a different discovery string if necessary.

CRS-04255: Not able to find the current configured voting files with the provided discovery string

Cause: The supplied discovery string does not discover the voting files that are currently configured.

Action: Pass a different discovery string that includes the location of the current configured voting files.

CRS-04256: Updating the profile

Cause: An update to the profile is being performed.

Action: None

CRS-04257: Voting file discovery string successfully replaced

Cause: A request to replace a discovery string completed.

Action: None

CRS-04258: Addition and deletion of voting files are not allowed because the voting files are on ASM

Cause: A voting file add or delete request was issued, but voting files have been configured on ASM storage. Once voting files are configured for ASM, changes in the configuration can be made only with 'crsctl replace votedisk'.

Action: Use 'crsctl replace votedisk' to modify the voting file configuration.

CRS-04259: Only one ASM diskgroup may be specified

Cause: If the voting files will be on ASM, no more than one diskgroup should be specified.

Action: Specify the correct ASM diskgroup.

CRS-04260: Voting file string is already configured

Cause: The location provided is already configured as a voting file.

Action: Specify another location that is not a current voting file.

CRS-04261: Diskgroup string is already configured with voting files

Cause: The diskgroup name provided is already configured with voting files.

Action: Specify another location for the voting files.

CRS-04262: Failure when retrieving information from the GPnP profile

Cause: An internal error happened when accessing GPnP profile.

Action: Contact Oracle Support Services.

CRS-04263: This operation is not allowed

Cause: Replacing a list of non-ASM voting files with a different list of voting files is not supported.

Action: To change the list of non-ASM voting files and add new voting files, use 'crsctl add css votedisk \<vfile>... \<vfile>'.

CRS-04264: The operation could not be validated

Cause: An internal error happened during the validation of the discovery string.

Action: Contact Oracle Support Services.

CRS-04265: The operation cannot be performed because the profile is busy with another operation

Cause: Another operation on the profile is taking place.

Action: Let the other operation finish and retry.

CRS-04266: Voting file(s) successfully replaced

Cause: A request to replace a voting files(s) completed.

Action: None

CRS-04267: Error while updating the profile with ASM discovery string

Cause: An internal error happened while updating the ASM discovery string.

Action: Contact Oracle Support Services.

CRS-04268: '-name' option is supported only with APPQOSDB type wallets

Cause: The '-name' option was specified in a wallet command for APPQOSDB type wallet.

Action: Use the '-name' option only for actions on APPQOSDB type wallets.

CRS-04269: Successful get priority number string for Cluster Synchronization Services.

Cause: The 'get' operation was performed successfully.

Action: None

CRS-04402: The CSS daemon was started in exclusive mode but found an active CSS daemon on node string, number string, and is terminating

Cause: The CSS daemon was started in exclusive mode, which requires that the clusterware stack is down on all other nodes to ensure data integrity. A CSS daemon was detected on another node, so the CSS daemon on this node is terminating.

Action: is required, otherwise stop the Oracle clusterware stack that is running on the indicated node. The name and number of the active node may be unknown.

CRS-04404: The following nodes did not reply within the allotted time: string

Cause: The clusterized command timed out before the specified nodes responded to the command.

Action: Check if the nodes are online; also check for communications problems. Consider issuing the command locally on the specified node(s).

CRS-04405: The following nodes are unknown to Oracle High Availability Services: string

Cause: The local Oracle High Availability Services is not in contact with Oracle High Availability Services on the specified nodes.

Action: Check if the nodes are online and Oracle High Availability Services is running. Check for communications problems and consider issuing the command locally on the specified node(s).

CRS-04481: Unable to spawn a process.

Cause: There was an internal error while spawning a process.

Action: Report the error to Oracle Support.

CRS-04482: A child process terminated abnormally.

Cause: A child process exited due to an internal error.

Action: Report the error to Oracle Support.

CRS-04602: Failed number to add voting file string.

Cause: An attempt to add a voting file failed. The number following "Failed" is a return code, which can be: 1 - internal OCSSD server error; 8 - rejected by OCSSD; 15- insufficient privileges for this operation; 19- version incompatibility between client and server;

Action: Respond based on the return code as follows: 15 - adjust privileges or use a different userid 19 - ensure that compatible versions are installed others - report to Oracle Support Services

CRS-04608: Failure number with Cluster Synchronization Services while deleting voting disk.

Cause: An attempt to delete a voting disk failed. The number following "Failed" is a return code, which can be: 1 - internal OCSSD server error; 8 - rejected by OCSSD; 15- insufficient privileges for this operation; 16- either the specified voting disk does not exist or you tried to delete a majority of voting disks; 19- version incompatibility between client and server;

Action: Respond based on the return code as follows: 15 - adjust privileges or use a different userid 16 - review the voting disk configuration displayed by 'crsctl query css votedisk' and correct your request accordingly 19 - ensure that compatible versions are installed others - report to Oracle Support Services

CRS-04615: Failure number in clsvswversion for node string

Cause: Internal error.

Action: Contact Oracle Support Services.

CRS-04625: Failure to allocate number bytes for username.

Cause: System is out of memory.

Action: Free up memory on system and retry.

CRS-04626: The requested setting must be between number and number.

Cause: An attempt to change a setting to an out of bounds value.

Action: Retry with the setting within the proper limits.

CRS-04627: Unable to lock the configuration before making changes. number

Cause: Failure in a CSS API acquiring a lock.

Action: Retry or contact support for information on the error code.

CRS-04628: Change to configuration failed, but was successfully rolled back.

Cause: See accompanying messages for explanation of cause.

Action: No action is required. This indicates that no damage was done.

CRS-04629: Unable number to mark unformat information on voting file string

Cause: Probably an unreadable / unwritable voting file was being removed.

Action: If cause is correct, this is ignorable, but not ideal.

CRS-04630: Unable to apply correct permissions to new voting file string.

Cause: An attempt to set permissions on a new voting file failed. This message is accompanied by others that provide OS-specific details of the error.

Action: Examine the OS-specific error and correct it if possible; otherwise, specify a different voting file.

CRS-04631: Unable number to undo initialization of voting file.

Cause: Could not roll back format of voting file.

Action: Disk should be cleaned out before an attempt to add again.

CRS-04632: Unable number to roll back OCR settings for voting file.

Cause: Could not remove temporary changes to OCR adding voting file.

Action: Shut down the cluster and restart. New voting file must be removed with "crsctl delete css votedisk".

CRS-04633: This could take several minutes.

Cause: CRS daemons is engaged in an activity take could potentially take a long time.

Action: None

CRS-04634: Retrying stop resources.

Cause: crsctl command is trying again to stop resources.

Action: None

CRS-04635: Internal error 'number' while attempting to send shutdown request

Cause: This is an internal error.

Action: If retrying does not work, contact Oracle support

CRS-04636: Failure number in clsvrelversion

Cause: Internal error.

Action: Contact Oracle Support Services.

CRS-04637: Oracle High Availability Services release version on the local node is \[string\]

Cause: Output message, not an error.

Action: None

CRS-04651: No resources found on server 'string'.

Cause: The server has no resources associated with it.

Action: Provide a server with resources running.

CRS-04652: Failure number in clsvswversion for the local node

Cause: Internal error.

Action: Contact Oracle Support Services.

CRS-04653: Server name 'string' contains invalid characters.

Cause: The name provided contains invalid characters.

Action: Use a server name with only alphanumeric characters.

CRS-04654: Server 'string' could not be found.

Cause: The name provided is not a known server's name.

Action: Use a known server's name.

CRS-04655: Resource 'string' could not be found.

Cause: The name provided is not a known resource's name.

Action: Use a known resource's name.

CRS-04656: Resource 'string' is not running on server 'string'.

Cause: The resource is not on the server the user specified.

Action: User must type a known server.

CRS-04657: Source and destination servers are the same.

Cause: The source and destination servers may not be the same.

Action: Specify a different destination server.

CRS-04658: The clusterware stack on node string is not completely down.

Cause: There is indication that the clusterware stack is still up.

Action: Please shutdown the entire clusterware stack before deleting the node.

CRS-04659: Error while trying to unpin node string.

Cause: An internal error happened during this operation.

Action: Please contact Oracle Support Services.

CRS-04660: Could not find node string to delete.

Cause: The node to be deleted could not be found because it has not been a member of this cluster recently.

Action: Please check the name provided. If the name is correct, the node has been automatically deleted because it was inactive for a long time and no further action is required to delete the node from the cluster.

CRS-04661: Node string successfully deleted.

Cause: A request to delete a node completed.

Action: None

CRS-04662: Error while trying to delete node string.

Cause: Some internal error happened during this operation.

Action: Please contact Oracle Support Services.

CRS-04663: Could not find node string to pin.

Cause: The indicated node is not an active node in the cluster.

Action: Ensure that the node name is correct and that Oracle Clusterware is running on the node.

CRS-04664: Node string successfully pinned.

Cause: A request to pin a node completed.

Action: None

CRS-04665: Error while trying to pin node string.

Cause: An internal error happened during this operation.

Action: Please contact Oracle Support Services.

CRS-04666: Could not find node string to unpin.

Cause: The indicated node is not an active node in the cluster.

Action: Ensure that the node name is correct and that Oracle Clusterware is running on the node.

CRS-04667: Node string successfully unpinned.

Cause: A request to unpin a node completed.

Action: None

CRS-04668: This ASM diskgroup does not contain voting disks to be deleted

Cause: The ASM diskgroup name provided does not contain voting files.

Action: Provide the right ASM diskgroup name.

CRS-04669: Failed to set parameter string to number due to conflicting parameter string; the new value for string must be less than number.

Cause: An attempt was made to set a new value to a configuration parameter which conflicts with another parameter's current value.

Action: Set the value of this parameter to a lower value than what is indicated in the message.

CRS-04670: Failed to unset parameter string due to conflicting parameter string currently set to number.

Cause: An attempt was made to unset a configuration parameter which conflicts with another parameter's current value.

Action: Set the conflicting parameter to a value which can coexist with proposed parameter change before submitting this parameter change.

CRS-04671: This command is not supported for ASM diskgroups.

Cause: The command 'crsctl add css votedisk' contains one or more ASM diskgroups in the list of voting files. Voting files may be migrated to and from ASM, but diskgroups cannot be added or deleted.

Action: Use an appropriate 'crsctl set' command to add ASM diskgroups. Use 'crsctl replace votedisk' command to migrate voting files to ASM.

CRS-04672: Successfully backed up the Voting File for Cluster Synchronization Service.

Cause: The backup of the voting file completed successfully.

Action: None

CRS-04673: Oracle High Availability Services version on the local node is \[string\]

Cause: Output message, not an error.

Action: None

CRS-04674: Cannot add invalid user 'string' to CRS Admin list.

Cause: An attempt was made to add an invalid username to the CRS Admin list.

Action: Reissue the command with a valid username.

CRS-04675: Failed to get logfilesize for Cluster Synchronization Services.

Cause: An internal error happened during this operation for Cluster Synchronization Services.

Action: Please contact Oracle Support Services.

CRS-04676: Successful get logfilesize number for Cluster Synchronization Services.

Cause: The operation is done successfully for Cluster Synchronization Services.

Action: None

CRS-04677: Failed to get string for Cluster Synchronization Services.

Cause: An internal error happened during this operation for Cluster Synchronization Services.

Action: Please contact Oracle Support Services.

CRS-04678: Successful get string number for Cluster Synchronization Services.

Cause: The 'get' operation was performed successfully.

Action: None

CRS-04679: Failed to unset logfilesize for Cluster Synchronization Services.

Cause: An internal error happened during this operation for Cluster Synchronization Services.

Action: Please contact Oracle Support Services.

CRS-04680: Successful unset logfilesize for Cluster Synchronization Services.

Cause: The 'unset' operation was performed successfully.

Action: None

CRS-04681: Failed to unset priority for Cluster Synchronization Services.

Cause: An internal error happened during this operation for Cluster Synchronization Services.

Action: Please contact Oracle Support Services.

CRS-04682: Successful unset priority for Cluster Synchronization Services.

Cause: The 'unset' operation was performed successfully.

Action: None

CRS-04683: Failed to set parameter string to number for Cluster Synchronization Services.

Cause: An internal error happened during this operation for Cluster Synchronization Services.

Action: Please contact Oracle Support Services.

CRS-04684: Successful set of parameter string to number for Cluster Synchronization Services.

Cause: The 'set' operation was performed successfully for Cluster Synchronization Services.

Action: None

CRS-04685: Failed to set logfilesize number for Cluster Synchronization Services.

Cause: An internal error happened during this operation for Cluster Synchronization Services.

Action: Please contact Oracle Support Services.

CRS-04686: Successful set logfilesize number for Cluster Synchronization Services.

Cause: The 'set' operation was performed successfully for Cluster Synchronization Services.

Action: None

CRS-04687: Shutdown command has completed with errors.

Cause: Processing of a shutdown command has completed with errors.

Action: Refer to preceding error message(s) for information about the errors that occurred.

CRS-04688: Oracle Clusterware is already stopped on server 'string'

Cause: Oracle Clusterware is not running on the indicated server.

Action: None

CRS-04689: Oracle Clusterware is already stopped

Cause: Oracle Clusterware is not running.

Action: None

CRS-04690: Oracle Clusterware is already running on 'string'

Cause: Oracle Clusterware is already running on the indicated server.

Action: None

CRS-04691: Oracle Clusterware is already running

Cause: Oracle Clusterware is already running.

Action: None

CRS-04692: Cluster Ready Services is online in exclusive mode

Cause: Cluster Ready Services is limited to providing internal services to other Oracle Clusterware components. External Cluster Ready Services are not available.

Action: When in exclusive mode, Oracle Clusterware components are dedicated to the repair or reconfiguration of the Oracle Cluster Registry, voting files or both. Oracle Clusterware should be down and remain down on every other cluster node. Only commands that check or stop the stack, interact with Cluster Synchronization Services or aid in Clusterware repair or reconfiguration should be issued.

CRS-04693: Failed to back up the voting file for Cluster Synchronization Service.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CRS-04694: Number of voting files cannot exceed number. Failed to add voting files.

Cause: The request to add voting files would cause the maximum number allowed to be exceeded.

Action: Specify fewer voting files to add so that the maximum is not exceeded, or include the -purge option on 'crsctl add css votedisk' to replace the existing set of files with an allowable number of new files.

CRS-04695: Voting disk addition failed because this disk string is a duplicate of an existing voting disk with matching File Universal ID string.

Cause: This disk is already a part of the current cluster.

Action: None needed.

CRS-04696: Failed to set parameter string to number due to conflicting parameter string; the new value for string must be greater than number.

Cause: An attempt was made to set a new value to a configuration parameter which conflicts with another parameter's current value.

Action: Set the value of this parameter to a higher value than what is indicated in the message.

CRS-04697: This command must be executed by Operating System user 'string'.

Cause: A crsctl command was executed by the wrong Operating System user.

Action: The specified Operating System user should execute the command.

CRS-04700: The Cluster Time Synchronization Service is in Observer mode.

Cause: Vendor time synchronization software exists on at least one of the nodes in the cluster.

Action: None

CRS-04701: The Cluster Time Synchronization Service is in Active mode.

Cause: Vendor time synchronization software is not detected on any of the nodes in the cluster.

Action: None

CRS-04703: The Cluster Time Synchronization Service is Offline.

Cause: The Cluster Time Synchronization Service is not running on the current node.

Action: None

CRS-04704: Shutdown of Clusterware failed on node string.

Cause: The shutdown did not complete successfully. One or more of the internal operations experienced an error that is reported in previous messages.

Action: Examine the error message(s) preceding this message and correct the problem(s) they describe.

CRS-04705: Start of Clusterware failed on node string.

Cause: The start did not complete successfully. One or more of the internal operations experienced an error that is reported in previous messages.

Action: Examine the error message(s) preceding this message and correct the problem(s) they describe.

CRS-04730: Command aborted due to an internal error

Cause: An inconsistent internal state was detected.

Action: Call Oracle Support Services.

CRS-04731: Specified file string could not be created.

Cause: JAZN configuration file required by the OC4J container could not be created.

Action: Ensure that the directory path exists and that its permissions will allow the file to be created by oracle owner of clusterware home.

CRS-04732: Could not be open file string.

Cause: JAZN configuration file required by the OC4J container could not be opened.

Action: Ensure that the directory path exists and that its permissions will allow the file to be created by oracle owner of clusterware home.

CRS-04733: File string does not exist.

Cause: The JAZN configuration file required by the OC4J container does not exist.

Action: Ensure that the directory path exists and that its permissions will allow the file to be created oracle owner of the clusterware home.

CRS-04734: Filename was not specified.

Cause: filename was not supplied or was an empty string.

Action: Re-try the command by specifying a valid JAZN configuration filename.

CRS-04735: Expected OCR key does not exist

Cause: An infrastructure error occured because a required OCR key was missing.

Action: Call Oracle Support Services.

CRS-04736: Operation on OCR key failed

Cause: Operation on OCR key failed due to an OCR error.

Action: Re-issue the command as oracle owner of clusterware home.

CRS-04737: Failed to allocate number bytes of memory

Cause: Could not allocate memory for internal buffers due to insufficient system memory resources

Action: Correct the system memory resources problem and retry the command

CRS-04738: Size of file string is too large

Cause: Specified file size exceeds 65536 bytes.

Action: Re-issue the command after reducing the size of the file.

CRS-04739: Could not close file string

Cause: Due to an internal error the specified file could not be closed

Action: Re-issue the command after verifying disk space, permissions and path.

CRS-04740: I/O operation on file string failed.

Cause: Due to an internal error an I/O operation on the specified file failed.

Action: Call Oracle Support if the problem persists.

CRS-04741: Insufficient permissions on OCR key

Cause: Operation on OCR key failed due to insufficient permissions.

Action: Re-issue the command as oracle owner of clusterware home.

CRS-04742: OCR updated with contents of string (New = number, Old = number bytes)

Cause: set jazn command was issued and OCR key was updated.

Action: None Required.

CRS-04743: File string was updated from OCR(Size: number(New), number(Old) bytes)

Cause: get jazn command was issued and specified file was updated with the contents from OCR key.

Action: None Required.

CRS-04922: string module: string ignored; module level out of bounds (range 0 - 65535)

Cause: Module log/trace level was out of bounds (range 0 - 65535).

Action: Specify a log/trace level within the valid range (0 - 65535).

CRS-04923: string module: string ignored; module level is invalid (range 0 - 65535)

Cause: Module log/trace level was invalid (range 0 - 65535).

Action: Specify a log/trace level within the valid range (0 - 65535).

CRS-04925: 'all' module keyword was specified with other module names

Cause: The module keyword 'all' already refers to all module names.

Action: When referring to all modules, use 'all' without duplicate references to other module names.

CRS-04980: Duplicate value string specified for resource attribute string

Cause: A duplicate value was specified for a resource attribute.

Action: Specify only one value for a resource attribute.

CRS-04981: Duplicate value string specified for type attribute keyword string

Cause: A duplicate value was specified for a type attribute keyword.

Action: Specify only one value for DEFAULT\_VALUE, FLAGS and TYPE per type attribute.

CRS-04982: Valid type attribute keyword string specified outside a type attribute

Cause: A valid type attribute keyword was specified outside a type attribute.

Action: Specify the ATTRIBUTE type attribute keyword before specifying the DEFAULT\_VALUE, FLAGS or TYPE type attribute keywords.

CRS-04983: Invalid type attribute keyword string specified

Cause: An invalid type attribute keyword was specified.

Action: Specify only the valid type attribute keywords ATTRIBUTE, DEFAULT\_VALUE, FLAGS and TYPE.

CRS-04984: Duplicate definition for type attribute string

Cause: The same type attribute was named on more than one ATTRIBUTE keyword.

Action: Define a type attribute only once.

CRS-05000: Expected resource string does not exist in agent process

Cause: The expected resource must have been created by Oracle Configuration tools.

Action: Check that the resource was not manually deleted. If not the case call Oracle Support.

CRS-05001: Expected dependency in resource string on a resource of type string does not exist

Cause: The expected resource dependency must have been created by Oracle Configuration tools.

Action: Check that the resource dependency was not manually removed.

CRS-05002: Agent action was aborted

Cause: Agent action was aborted either due to action timeout expiry or the user canceled the action.

Action: Retry the operation.

CRS-05003: Invalid attribute value: 'string' for attribute string

Cause: An attribute value passed to the Agent was NULL or invalid.

Action: Give the correct value to the attribute and retry.

CRS-05004: Cannot find listener endpoint for listener string

Cause: listener endpoint not found.

Action: Check listener.ora for that listener.

CRS-05005: IP Address: string is already in use in the network

Cause: The VIP resource attempted to use an IP address already in use in the network.

Action: Use srvctl to re-create vip or scanvip specifying an IP address which is not being used in the network and retry the operation.

CRS-05006: Unable to automatically select a network interface which has subnet mask string and subnet number string

Cause: The subnet mask and subnet number configured for the resource did not match the subnet mask and subnet number of any network interface on this node.

Action: Provide a subnet mask and subnet number which matches at least one network interface's subnet mask and subnet number using srvctl remove and add vip and retry the operation.

CRS-05007: Cannot remove the primary IP string from the network interface

Cause: The primary IP of the network interface was incorrectly configured as the VIP.

Action: Use 'srvctl remove' and 'srvctl add vip' or 'srvctl remove' and 'srvctl add scan' to provide the correct IP address for the VIP and retry the operation.

CRS-05008: Invalid attribute value: string for the network interface

Cause: The network interface value did not match the subnet mask and subnet number of any network interface on the node.

Action: Modify the network interface's value such that the subnet mask and subnet number matches the subnet mask and subnet number of at least one network interface on the node using 'srvctl remove' and 'srvctl add vip' and retry the operation.

CRS-05009: The VIP address string does not belong to the subnet string

Cause: The VIP's subnet number and the network interface's subnet number did not match.

Action: Make the VIP's subnet number match the network interface's subnet number using 'srvctl remove' and 'srvctl add vip' or 'srvctl remove' and 'srvctl add scan' and retry the operation.

CRS-05010: Update of configuration file "string" failed: details at "string" in "string"

Cause: An attempt to open the specified file failed. Common causes are that the file does not exist, or the file permissions prohibit access.

Action: Check that the file exists and has the proper permissions.

CRS-05011: Check of resource "string" failed: details at "string" in "string"

Cause: The check of the database or Automatic Storage Management instance failed.

Action: Check the database or ASM instance alert log and the referenced Oracle Clusterware trace file for additional information. Recover the instance if necessary.

CRS-05012: Check of service resource "string" failed: details at "string" in "string"

Cause: The check of the preconnect service failed because it could not run on the same node as the main service.

Action: Check the referenced Oracle Clusterware trace file for additional information. Start the preconnect service on a different node.

CRS-05013: Agent "string" failed to start process "string" for action "string": details at "string" in "string"

Cause: The named agent failed to start the named process for the named action.

Action: Check the referenced Oracle Clusterware trace file for additional operating system specific information. Refer to operating system documentation to correct the error.

CRS-05014: Agent "string" timed out starting process "string" for action "string": details at "string" in "string"

Cause: The named agent aborted the named process because the process failed to respond within the timeout period.

Action: Check the agent log files for further information

CRS-05015: Agent timed out waiting for a response from the DHCP server

Cause: Agent and the DHCP server were not able to communicate with each other. Common causes of this failure are due to the DHCP server not running, or improper DHCP server configuration, or the DHCP server running out of DHCP leases.

Action: Identify the cause of the problem from the DHCP server log files. If the problem is due to the DHCP server running out of leases, increase the number of addresses which can be served by the DHCP server.

CRS-05016: Process "string" spawned by agent "string" for action "string" failed: details at "string" in "string"

Cause: The named process failed to complete succesfully.

Action: Check details in the agent log for error information from the spawned process.

CRS-05017: The resource action "string string" encountered the following error: string. For details refer to "string" in "string".

Cause: The following error occured during the resouce action.

Action: Examine the accompanying error messages and respond accordingly.

CRS-05018: string Removed unused HAIP route: string / string / string / string

Cause: A potentially conflicting route in the same subnet as the HAIP addresses was found and removed to prevent routing conflicts.

Action: Validate that the route described was not actually in use.

CRS-05019: All OCR locations are on ASM disk groups \[string\], and none of these disk groups are mounted. Details are at "string" in "string".

Cause: OCR was configured on ASM disk groups, and all of the listed disk groups failed to mount. The possible causes are:

1\. A disk was not accessible.

2\. A disk in a normal or high redundancy disk group failed after the most recent dismount.

3\. The ASM\_DISKSTRING in the SPFILE or the GPnP profile was incorrect.

Action: Check the ASM alert logs for more information. To correct disk access or failure issues either: a) restore access to the disks in the disk group and mount the disk group (via ASMCMD or SQL). or b) Issue a force mount to the disk group to offline missing disks and mount a normal or high redundancy disk group. To correct the ASM\_DISKSTRING in the SPFILE and propagate the change to the GPnP profile, in sqlplus, issue the SQL command "ALTER SYSTEM SET ASM\_DISKSTRING <discovery\_string> SCOPE=BOTH"

CRS-05020: Not all endpoints are registered for listener string

Cause: Listener agent failed to register all endpoints to listener.

Action: Check listener log file for that listener.

CRS-05021: Check of storage failed: details at "string" in "string"

Cause: The check of ASM storage failed because the storage was not accessible.

Action: Check the Oracle Clusterware alert log and the referenced Oracle Clusterware trace file for additional information.

CRS-05022: Stop of resource "string" failed: current state is "string"

Cause: The named resource failed to stop.

Action: Ensure no one is using the resource and reissue the stop.

CRS-05023: Failed to unmount file system "string"; details at "string" in "string"

Cause: The named file system resource failed to unmount.

Action: Determine which operating system processes are accessing the mount point using an operating system command such as 'fuser' or 'lsof' for UNIX-based platforms or 'handle' for Windows. Close, shut down, or terminate applications and processes accessing the mount point, then retry.

CRS-05024: Unmounting file system "string"

Cause: A 'stop' of the file system resource mounted on the indicated path started.

Action: This is an informational message only.

CRS-05025: File system "string" unmounted

Cause: A 'stop' of the file system resource mounted on the indicated path completed normally.

Action: This is an informational message only.

CRS-05026: Failed to clean mount point "string"; details at "string" in "string"

Cause: The clean of the volume failed because one or more processes on the system were accessing the mount point.

Action: Determine which operating system processes are accessing the mount point using an operating system command such as 'fuser' or 'lsof' for UNIX-based platforms or 'handle' for Windows. Close, shut down, or terminate applications and processes accessing the mount point, then retry.

CRS-05027: Agent failed to initialize ARP devices required for starting the HAIP resource

Cause: The resource could not be started because the ARP devices failed to start on the same node.

Action: Manually check the ARP devices on the same node and then start the resource.

CRS-05501: Unable to connect to eONS server on port number

Cause: The eONS server may not be active or listening on a different port.

Action: Ensure that the eONS resource is ONLINE and listening on the above port.

CRS-05502: Invalid event template string

Cause: The event template specified is invalid.

Action: The event template format must be <PROPERTY|ELEMENT>(\<attribute name>=<literal|%resource attribute name%>)...

CRS-05503: Error creating the eONS subscriber

Cause: The eONS server may not be active.

Action: Ensure that the CRS eONS resource is in ONLINE state.

CRS-05504: Node down event reported for node 'string'.

Cause: The specified node was not responsive.

Action: Restart the specified node.

CRS-05601: MDNS: string

Cause: None, generic bypass mdns message.

Action: None

CRS-05602: mDNS service stopping by request.

Cause: MDNSD stopping by OHASD request.

Action: None

CRS-05705: Failed to get required resources

Cause: There was an internal error while evaluating the required resources for the subject resource.

Action: Contact Oracle Support Services.

CRS-05706: No more members to consider

Cause: There was no host found on which to start the resource based on the placement policy.

Action: Check the placement policy and the required resources for the subject resource.

CRS-05707: Failed after successful dependency consideration

Cause: There was no host found on which to start the resource based on the placement policy.

Action: Check the placement policy and the required resources for the subject resource.

CRS-05709: Resource 'string' is already running on member 'string'

Cause: An attempt was made to start a resource on a host while it is already running on that host.

Action: This is an insignificant error. Check the operation being performed.

CRS-05801: Agent path is null or does not resemble a filesystem path

Cause: Unable to spawn the agent program because of incorrect agent path.

Action: Fix the agent path using 'crsctl modify type'.

CRS-05802: Unable to start the agent process

Cause: An attempt to start the agent process failed.

Action: Ensure that the agent path is correct and has the proper permissions, and retry the command.

CRS-05805: Missing the required action callback in agent

Cause: Unable to execute resource's command.

Action: Ensure that agent executable or action script contains the missing function.

CRS-05809: Failed to execute 'string' value of 'string' for 'string'. Error information 'string', Category: number, OS error: number

Cause: Unable to spawn the resource action script due to incorrect path value or incorrect permissions or other OS error.

Action: Correct the action script path and permissions or check and fix the reported OS error.

CRS-05810: Attempt to add a duplicate resource 'string'. Details at string in string.

Cause: An identical resource was already being monitored.

Action: Rename the resource and retry the operation.

CRS-05811: Failed to read ORA\_CRS\_HOME from environment. Details at string in string.

Cause: The ORA\_CRS\_HOME environment variable was not set correctly.

Action: This variable is set during CRS installation. If necessary, reinstall CRS.

CRS-05812: Could not get local hostname. Details at string in string.

Cause: The hostname could not be read.

Action: Check that the hostname for the local machine is valid. If the problem persists, contact Oracle Support Services.

CRS-05813: Could not change directory to 'string'. Details at string in string.

Cause: The specified path is inaccessible to the agent process.

Action: Check that the specified path exists.

CRS-05814: Agent 'string' started with invalid arguments. Details at string in string.

Cause: An invalid parameter was supplied to the agent.

Action: Contact Oracle Support Services.

CRS-05815: Agent 'string' could not find any base type entry points for type 'string'. Details at string in string.

Cause: Action entry points were not defined for this agent.

Action: No action necessary if this is a script agent. If this is not a script agent, define action points in your agent code.

CRS-05816: Agent 'string' could not start implicit monitoring for resource 'string'. Details at string in string.

Cause: The resource was currently disabled and hence could not be monitored.

Action: Enable the resource.

CRS-05817: Caught exception from user code for command 'string'. Details at string in string.

Cause: An exception was thrown from the user code when an action entry point was called.

Action: This is due to an error in the agent user code. Modify the agent's code to resolve this.

CRS-05818: Aborted command 'string' for resource 'string'. Details at string in string.

Cause: Execution of the specified command was aborted due to a timeout.

Action: Restart the resource manually. If the problem persists, contact Oracle Support Services.

CRS-05819: Could not abort command 'string' for resource 'string'. Details at string in string.

Cause: Attempt to abort the specified command failed.

Action: Define an abort action entry point for the agent.

CRS-05820: Agent 'string' failed to initialize server process address. Details at string in string.

Cause: Agent could not connect to the server process.

Action: Contact Oracle Support Services.

CRS-05821: Agent 'string' is started with wrong user 'string'. Details at string in string.

Cause: An incorrect owner was specified for the agent.

Action: Make sure CRSD has enough privileges to spawn programs as the value specified as the 'owner' in the ACL attribute.

CRS-05822: Agent 'string' disconnected from server. Details at string in string.

Cause: Agent could not connect to server process.

Action: Contact Oracle Support Services.

CRS-05823: Could not initialize agent framework. Details at string in string.

Cause: Initialization of the agent failed.

Action: Contact Oracle Support Services.

CRS-05824: Could not initialize server connect string 'string'. Details at string in string.

Cause: Incorrect server connect string was specified in the environment.

Action: Contact Oracle Support Services.

CRS-05825: Agent 'string' is unresponsive and will be restarted. Details at string in string.

Cause: The specified agent did not respond and will be restarted automatically.

Action: None

CRS-05826: Agent 'string' could not read environment variable 'string'. Details at string in string.

Cause: The agent could not read a required environment variable.

Action: Contact Oracle Support Services.

CRS-05827: Could not find information for resource 'string'. Details at string in string.

Cause: The specified resource was not found in the internal list of resources.

Action: Check the agent parameters and restart the resource manually.

CRS-05828: Could not start agent 'string'. Details at string in string.

Cause: Creation of the agent process failed.

Action: Contact Oracle Support Services.

CRS-05829: Failed to get definition for resource 'string'. Details at string in string.

Cause: The definition of the resource could not be determined.

Action: Delete the resource and add it again using the crsctl command.

CRS-05830: Invalid path 'string' found for agent filename. Details at string in string.

Cause: The path that was specified for the agent was incorrect.

Action: Check that the path exists and is readable.

CRS-05831: Agent 'string' has exceeded maximum failures and has been disabled. Details at string in string.

Cause: The specified agent has failed too many times.

Action: Contact Oracle Support Services.

CRS-05832: Agent 'string' was unable to process commands. Details at string in string.

Cause: Agent was unable to process commands.

Action: Contact Oracle Support Services.

CRS-05833: Cleaning resource 'string' failed as part of reboot-less node fencing

Cause: A resource 'clean' action associated with reboot-less node eviction encountered an error. This is an expected occurence in most cases.

Action: None

CRS-05837: Unable to open environment file 'string'.

Cause: The environment file specified could not be opened.

Action: Verify that the filename, its location and its permissions are correct.

CRS-05838: Syntax error in environment file 'string'.

Cause: The environment file specified did not have key value pairs in the correct format.

Action: Correct the key value format and retry. Consult the Clusterware Administration manual for the correct format.

CRS-06001: User does not have permission to start CRSD.

Cause: Unable to start CRSD due to insufficient permissions.

Action: Start CRSD as a privileged user.

CRS-06007: Could not communicate with Event Manager.

Cause: Unable to communicate with Event Manager daemon.

Action: Run the 'crsctl check evmd' command to determine whether Event Manager daemon is properly configured and is running.

CRS-06015: Oracle Clusterware has experienced an internal error. Details at string in string.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CRS-06021: Could not set system resource limits for Clusterware: "ulimit -string string".

Cause: A ulimit command issued internally to set system resource limits failed.

Action: Ensure that the correct resource limit values are set in the user profile and limits.conf.

CRS-08000: unable to obtain local host name for reboot advisory log file scan

Cause: An attempt to retrieve the local host name failed. The scan for reboot advisory files will not use host name criteria and so may report occurrences for other nodes as well as this one.

Action: Report this error to Oracle Support Services.

CRS-08001: an error occurred accessing reboot advisory log file location: string

Cause: The scan for reboot advisory log files was unable to access the indicated file system location. The location was skipped, so any reboot advisory files that it contains will not be reported. This message is accompanied by CLSU- messages containing details of the access error.

Action: Respond based on the error described by the accompanying CLSU- messages. This may involve re-creating the directory or changing its permissions.

CRS-08002: an error occurred searching reboot advisory log file location: string

Cause: The scan for reboot advisory log files was unable to read the next file name from the indicated file system location. No further processing of reboot advisory files from that location occurs. This message is accompanied by CLSU- messages containing details of the access error.

Action: Respond based on the error described by the accompanying CLSU- messages.

CRS-08003: reboot advisory log file: string is unexpectedly empty

Cause: The scan for reboot advisory log files encountered a file that was empty. This might happen (rarely) if a component is initializing its use of reboot advisory at the same time the scan is running. Processing of other files in the location continues.

Action: Frequent occurrence of this message should be reported to Oracle Support Services.

CRS-08004: an error occurred reading reboot advisory log file: string

Cause: The scan for reboot advisory log files experienced a read error on a reboot advisory file. No further processing is done for that file, but the scan continues with other files. This message is accompanied by CLSU- messages containing details of the read error.

Action: Respond based on the accompanying CLSU- messages.

CRS-08005: an error occurred closing reboot advisory log file: string

Cause: The scan for reboot advisory log files experienced a close error on a reboot advisory file. The scan continues with other files. This message is accompanied by CLSU- messages containing details of the close error.

Action: Report this error to Oracle Support Services.

CRS-08006: an error occurred opening reboot advisory log file: string

Cause: The scan for reboot advisory log files experienced an error when it opened a reboot advisory file. The scan continues with other files. This message is accompanied by CLSU- messages containing details of the open error.

Action: If the error indicated in the accompanying CLSU- messages is one that can be corrected, do so. Otherwise, report this error to Oracle Support Services.

CRS-08007: an error occurred closing reboot advisory log file location: string

Cause: The scan for reboot advisory log files experienced an error when it closed the indicated file system location. Processing of other reboot advisory locations (if any) continues normally. This message is accompanied by CLSU- messages containing details of the close error.

Action: Report this error to Oracle Support Services.

CRS-08008: string

Cause: Operating system error data related to reboot advisory file processing was returned. The error data is packaged in a CLSU- message that follows "CRS-08008:". One or more of these messages appears after a message announcing the error condition.

Action: Look up the embedded CLSU- message for an explanation of the operating system error data. If there is no CLSU- message ID present, contact Oracle Support Services.

CRS-08009: reboot advisory log file: string contains invalid data (length number, error code number)

Cause: A reboot advisory log record read from the indicated file contained incorrect data.

Action: Report this error to Oracle Support Services.

CRS-08010: invalid network reboot advisory message detected (length number, error code number)

Cause: A reboot advisory record received over the network was improperly formed or contained incorrect data.

Action: Report this error to Oracle Support Services.

CRS-08011: reboot advisory message from host: string, component: string, with time stamp: string

Cause: d a reset or reboot of the affected host, and respond accordingly. Refer to the discussion of reboot advisories in the Oracle Clusterware administration documentation for additional guidance.

Action: Use the reboot advisory message(s) to determine why Oracle Clusterware

CRS-08012: reboot advisory message from a higher Oracle Clusterware version detected

Cause: A reboot advisory message from a higher version installation of Oracle Clusterware was detected. This is an expected occurrence with network reboot advisories when there are nodes with a higher Oracle Clusterware version than this node (such as during an upgrade). It is an unexpected condition with file reboot advisories.

Action: The reboot advisory message is displayed in a following CRS-08013 message in a "raw" text form. In the case of network reboot advisories, the explanatory message text should be readable and useful to determine the cause of the node reboot. If the reboot advisory message is from a file, report this message to Oracle Support Services.

CRS-08013: reboot advisory message text: string

Cause: An explanatory text message associated with a reboot advisory announced in a preceding CRS-08011 or CRS-08012 message was displayed. These text messages are always written in US English locale.

Action: Refer to the descriptions of messages CRS-08011 and -08012, and to the Oracle Clusterware documentation on reboot advisories.

CRS-08014: reboot advisory binary data (number bytesstring) follows:

Cause: Binary data associated with a reboot advisory message was displayed. It is followed by one or more lines of CRS-08015 message containing the binary data formatted in hexadecimal. If an asterisk appears inside the parentheses, an invalid data length was detected.

Action: Refer to the description of message CRS-08011 and -08012, and to the Oracle Clusterware documentation on reboot advisories.

CRS-08015: number string

Cause: Hexadecimal display of binary data included in a reboot advisory log message was displayed. The first number is an offset and is followed by up to 16 bytes of data.

Action: Refer to the description of message CRS-08011 and -08012, and to the Oracle Clusterware documentation on reboot advisories.

CRS-08016: an error occurred determining the location for reboot advisory log files

Cause: The search for reboot advisory log files was unable to determine the file system location used for those files. Processing of reboot advisory files is skipped. This message is accompanied by CLSU- messages containing failure details. This is an internal error.

Action: Report this error to Oracle Support Services.

CRS-08017: location: string has number reboot advisory log files, number were announced and number errors occurred

Cause: This summary message is written during Oracle Clusterware startup if one or more reboot advisory log files was found and examined.

Action: This message is informational, but if the error count is nonzero the associated messages (earlier in the alert log) should be examined.

CRS-08018: warning: missing cluster identity data for reboot advisory message validation

Cause: During Oracle Clusterware start up, an attempt to obtain the identity of the cluster failed. Processing continues normally, but network reboot advisories from nodes in other clusters may be reported in this cluster's alert log.

Action: Report this error to Oracle Support Services.

CRS-08019: warning generated by the initialization of the reboot advisory in the CSS agent, string

Cause: During initialization of the reboot advisory, a warning was generated

Action: Report this warning to Oracle Support Services.

CRS-08020: error generated by the initialization of the reboot advisory in the CSS agent, string

Cause: During initialization of the reboot advisory, an error was generated.

Action: Report this error to Oracle Support Services.

CRS-09000: Failed to allocate memory.

Cause: During intialization, memory could not be allocated.

Action: Report this error to Oracle Support Services.

CRS-09001: Internal Error

Cause: An internal error occurred.

Action: Report this error to Oracle Support Services.

CRS-09004: Error reading from standard input

Cause: Could not read commands from the command line.

Action: Report this error to Oracle Support Services.

CRS-09005: Quoted string not ended

Cause: An unmatched " was found in the command entered.

Action: Put in the corresponding quote or remove the unmatched quote.

CRS-09008: Unknown verb string

Cause: Unknown or invalid verb passed to oclumon.

Action: Use 'oclumon -h' in command line or help command in interactive mode to see the supported verbs.

CRS-09009: Error string: Parsing error. Invalid arguments given.

Cause: Invalid or unknown arguments passed.

Action: Refer to product documentation or to command online help for an explanation of verbs and arguments.

CRS-09010: Error string: mandatory data not supplied

Cause: Mandatory data not supplied to the command.

Action: Refer to product documentation or to command online help for an explanation of verbs and arguments.

CRS-09011: Error string: Failed to initialize connection to the Cluster Logger Service

Cause: Error occurred while connecting to the Cluster Logger Service.

Action: Ensure that Cluster Logger Service is running and reachable from the client node by using the 'ping' command for the given node.

CRS-09012: Error string: Error sending query to the Cluster Logger Service

Cause: Error occurred while sending query to the Cluster Logger Service.

Action: Ensure that the Cluster Logger Service is running and reachable from the client node by using the 'ping' command for the given node.

CRS-09013: Error string: Invalid data received from the Cluster Logger Service

Cause: Invalid or unknown data received from the Cluster Logger Service.

Action: Ensure that the Cluster Logger Service is running and reachable from the client node by using the 'ping' command for the given node.

CRS-09014: Error: Corrupt reply from the Cluster Logger Service

Cause: Invalid or unknown data received from the Cluster Logger Service.

Action: Make sure that the version of both master and client installation is same. Also, check the connectivity between master and client using the 'ping'.

CRS-09017: Error: Invalid or unknown reply received from the Cluster Logger Service

Cause: Error occurred in the data received.

Action: Make sure that the version of both master and client installation is same. Also, check the connectivity between master and client.

CRS-09018: Error string: No arguments supplied

Cause: No argument was supplied with the command.

Action: Some commands need arguments with them. Refer to the product documentation or to the online help display.

CRS-09019: Error string: No parameter string supported

Cause: A wrong parameter was passed with the command.

Action: Refer to the command help and pass the correct parameters.

CRS-09020: Error string: No master node name given

Cause: The master node name was not passed in the command.

Action: Pass the appropriate master node name with the command.

CRS-09021: Error string: Invalid or no start time given

Cause: A start time was not provided or the time was passed in the wrong format.

Action: Pass the correct start time. For correct format, refer to command help.

CRS-09022: Error string: Invalid or no end time given

Cause: A end time was not provided or the time was passed in the wrong format.

Action: Pass the correct end time. For correct format, refer to command help.

CRS-09023: Error string: Time not given or in wrong format or invalid

Cause: Time was not provided or was invalid.

Action: Pass the correct and valid time. For correct format, refer to command help.

CRS-09024: Error string: No node name given

Cause: Node name not provided.

Action: Provide a node name in the command. Refer to the product documentation or to the command online help for information.

CRS-09025: Error string: No disk ID name given

Cause: Disk ID was not given in the command with -diskid.

Action: Pass a valid disk ID with -diskid option.

CRS-09026: Error string: No parameter given

Cause: The parameter was not passed in the query.

Action: Pass appropriate parameter for query. Refer to the product documentation or to the command online help for information.

CRS-09027: Error string: Parameter string is not supported with this verb

Cause: Invalid or unknown parameter passed.

Action: Pass the correct parameter. Refer to the product documentation or to the command online help for information.

CRS-09028: Error string: No NIC ID given

Cause: NIC ID was not given in the command with -nicid.

Action: Pass a valid NIC ID with -nic option.

CRS-09029: Error string: No PID given

Cause: PID was not given in the command with -pid.

Action: Pass a valid PID with -pid option.

CRS-09030: Error string: No region given

Cause: Incorrect or no region given with -c option.

Action: Pass a valid region with -c option. Refer to the product documentation or to the command online help for information.

CRS-09031: Argument string not supported with this verb string. -h for help.

Cause: Unknown or invalid argument passed with the command.

Action: Refer to the product documentation or to the command online help for information on supported arguments.

CRS-09032: Invalid hour given in the time argument

Cause: Invalid hour in the time string was passed.

Action: Pass a valid time string in accordance with the format. Refer to the product documentation or to the command online help for information on supported arguments.

CRS-09033: Invalid minutes given in the time argument

Cause: Invalid minutes in the time string was passed.

Action: Pass a valid time string in accordance with the format. Refer to the product documentation or to the command online help for information on supported arguments.

CRS-09034: Invalid seconds given in the time argument

Cause: Invalid seconds in the time string was passed.

Action: Pass a valid time string in accordance with the format. Refer to the product documentation or to the command online help for information on supported arguments.

CRS-09035: Arguments not in proper format, or invalid arguments

Cause: Invalid arguments given.

Action: Pass a valid verb and correct arguments for it. Refer to the product documentation or to the command online help for information on supported arguments.

CRS-09036: Invalid Cluster Health Monitor repository size given

Cause: Non-numeric value or value out of range given for Cluster Health Monitor repository size.

Action: Specify Cluster Health Monitor repository size in the valid range. Refer to the product documentation or to the command online help for information on supported arguments.

CRS-09037: string Error: Node name not given. -disk, -nic and -proc need node name

Cause: The required node name was not provided for -disk, -nic, or -proc.

Action: Provide a node name with -n option. Refer to the product documentation or to the command online help for information on supported arguments.

CRS-09038: Error: -s and -e need to be specified together

Cause: Either -s or -e is missing.

Action: Start and end time need to be given together for range queries, which cannot be unbounded. Refer to the product documentation or to the command online help for information on supported arguments.

CRS-09039: Error string: -i is not allowed with the range query

Cause: The -i option was specified on an oclumon range query.

Action: Use -i only in continuous mode. Refer to the command inline help or product documentation for more information.

CRS-09040: Error string: Band value not given or incorrect

Cause: The band value was not passed with -t option or was invalid.

Action: Provide a valid band value. Refer command help.

CRS-09041: Error string: The -repos argument was specified without an option.

Cause: -repos was not provided with the option, generating a parsing error.

Action: Provide a valid option to -repos. Refer to the product documentation or to the command online help for information on supported arguments.

CRS-09042: Error string: No size given with resize

Cause: A valid value was not provided with resize.

Action: Provide a valid numerical value with 'resize'. Refer to the product documentation or to the command online help for information on supported arguments.

CRS-09043: Error string: Non-numeric or invalid value for size: string

Cause: An invalid or non-numeric value was provided for size.

Action: Provide a valid numeric size. Refer to the product documentation or to the command online help for information on supported arguments.

CRS-09044: No key specified with -getkey

Cause: An option was not given with -getkey.

Action: Provide a valid key as an option with -getkey.

CRS-09045: No key given for -get

Cause: An option was not provided with -get.

Action: Provide a valid option with -get. Refer to the product documentation or to the command online help for information on supported arguments.

CRS-09046: Invalid key given

Cause: An unknown key was provided with -get.

Action: Provide a supported key with -get. Refer to the product documentation or to the command online help for information on supported arguments.

CRS-09047: Error string: Error Dumping Log (return code:number ) for node string

Cause: An error occurred while dumping local log.

Action: Report this error to Oracle Support Services. Cluster Health Monitor repository directory may be unreachable, unreadable or incorrect.

CRS-09048: Error string: No data received from the Cluster Logger Service after number attempts

Cause: Data was not received from the Cluster Logger Service after the given number of attempts or data was not available.

Action: None

CRS-09049: Error string: Cannot get environment variable CRFHOME

Cause: An internal error occurred.

Action: Report this error to Oracle Support Services.

CRS-09050: Error string: Too many host names

Cause: Too many host names were provided.

Action: Provide valid number of host names. Refer to the product documentation or to the command online help for information.

CRS-09051: Error string: Invalid interval size given

Cause: Non-numeric or invalid interval provided.

Action: Provide a valid numerical value for interval size. Refer to the product documentation or to the command online help for information

CRS-09052: Error string: string control not supported

Cause: The given debug control was not supported.

Action: Provide a supported control. Refer to the product documentation or to the command online help for information.

CRS-09053: Key:value pair missing

Cause: A required key:value pair was missing.

Action: Provide a valid key:value pair. Refer to the product documentation or to the command online help for information

CRS-09054: Incomplete or invalid parameters string

Cause: Incomplete or invalid parameters supplied.

Action: Provide the complete and correct parameters. Refer to the product documentation or to the command online help for information

CRS-09055: module:level given in invalid format or invalid value

Cause: Invalid format or value specified for module:level.

Action: Provide correct module:level. Refer to the product documentation or to the command online help for information

CRS-09056: Error string: Invalid Cluster Health Monitor repository location given

Cause: Invalid Cluster Health Monitor repository location provided.

Action: Provide a directory with read and write permissions for Cluster Health Monitor repository location. Refer to the product documentation or to the command online help for information.

CRS-09057: Error string: No response received from the Cluster Logger Service

Cause: No data received from the Cluster Logger Service for the query.

Action: Ensure that the Cluster Logger Service is running and reachable from the client node by using the 'ping' command for the given node.

CRS-09058: Error string: Changing log level failed due to authentication failure

Cause: Log level could not be changed due to authentication failure.

Action: Ensure that this command is run as root.

CRS-09059: Error string: Changing log level failed due to connection failure

Cause: A connection failure occurred while changing the log.

Action: Ensure that the daemons are running and are reachable from the client node by using the 'ping' command for the given node.

CRS-09060: Error string: Unable to send message due to memory allocation failure

Cause: Memory could not be allocated for debug message.

Action: Report this error to Oracle Support Services.

CRS-09061: Error string: Changing log level failed due to response time-out

Cause: A time out happened while waiting for response.

Action: Report this error to Oracle Support Services.

CRS-09062: Error string: Error in changing log level

Cause: An error occured while changing log level.

Action: Report this error to Oracle Support Services.

CRS-09065: Disk ID not found

Cause: Given disk ID was not found or not present in the interesting list.

Action: Provide a disk ID which is available at the start of the query range.

CRS-09066: Process ID not found

Cause: Given process ID was not found.

Action: Provide a process ID which is available at the start of the query range.

CRS-09067: NIC ID not found

Cause: Given NIC ID was not found.

Action: Provide a correct NIC ID.

CRS-09068: Error string: -allnodes and -n must not be used together

Cause: Both -allnodes and -n were supplied on a dumpnodeview command.

Action: Specify either -allnodes or -n with specific nodes.

CRS-09069: The new Cluster Health Monitor repository location is string.

Cause: The Cluster Health Monitor repository location was successfully replaced.

Action: None

CRS-09070: The new Cluster Health Monitor repository retention time is number seconds.

Cause: The Cluster Health Monitor repository retention time was successfully modified.

Action: None

CRS-09100: Error setting Cluster Health Monitor repository size

Cause: An error occurred while setting Cluster Health Monitor repository size on the Cluster Logger Service.

Action: Report this error to Oracle Support Services.

CRS-09101: Error updating Cluster Health Monitor repository size in configuration file.

Cause: An error occurred while writing the Cluster Health Monitor repository size to configuration files.

Action: Report this error to Oracle Support Services.

CRS-09102: No data for the node at the given time

Cause: Data was not found for the given node.

Action: This is an informational message only.

CRS-09103: No data available

Cause: Data was not available for the query.

Action: Make sure the System Monitor Service is running on the given node.

CRS-09104: No data available for the given nodes

Cause: Data was not available for given nodes.

Action: Make sure the System Monitor Service is running on the given nodes.

CRS-09105: Internal Error on master

Cause: An internal error on master caused this error.

Action: Report this error to Oracle Support Services.

CRS-09106: Data requested was outside Cluster Health Monitor retention time limits.

Cause: A request for data outside Cluster Health Monitor repository limit caused this error.

Action: Data needs to be requested in the proper Cluster Health Monitor repository limits. Refer to the product documentation for more information.

CRS-09107: Start time greater than end time

Cause: A start time greater \[or later\] than end time caused an error.

Action: Make sure the start time is less than the end time for the given range query.

CRS-09108: Threshold out of acceptable range

Cause: A threshold was specified that is outside the allowed range.

Action: Make sure threshold is within the acceptable range. Refer documentation or online help for more information

CRS-09109: New Cluster Health Monitor repository location same as the old location on node string

Cause: The new location specified for Cluster Health Monitor repository is same as the old location.

Action: Provide a different location for Cluster Health Monitor repository. Refer documentation or online help for more information.

CRS-09110: Cluster Health Monitor repository location not changed as the location provided does not exist on node string.

Cause: The new location specified for Cluster Health Monitor repository does not exist.

Action: Provide a different location for Cluster Health Monitor repository. Refer documentation or online help for more information.

CRS-09111: Error updating Cluster Health Monitor repository location string in configuration file.

Cause: An error occurred while writing the Cluster Health Monitor repository location to configuration files.

Action: Report this error to Oracle Support Services.

CRS-09114: Cluster Health Monitor repository location change failed on one or more nodes. Aborting location change.

Cause: An error occurred while setting Cluster Health Monitor repository location on the Cluster Logger Service.

Action: Retry specifying a valid location.

CRS-09116: Cluster Health Monitor repository retention change failed on one or more nodes. Aborting retention change.

Cause: An error occurred while setting Cluster Health Monitor repository size on the Cluster Logger Service.

Action: Retry specifying a valid location.

CRS-09500: The system monitor service aborted on host string. Details at string in string.

Cause: The system monitor service aborted due to an internal error.

Action: If the problem persists, contact Oracle Support Services.

CRS-09501: The Cluster Logger Service aborted on host string. Details at string in string.

Cause: The Cluster Logger Service aborted due to an internal error.

Action: If the problem persists, contact Oracle Support Services.

CRS-09502: The Cluster Health Monitor repository location string is inaccessible. Details at string in string.

Cause: An error occurred while accessing the Cluster Health repository.

Action: Check that the Cluster Health Monitor repository location in question has the correct permissions. Determine whether this behavior is limited to one node or whether it occurs across all of the nodes in the cluster. Use the 'oclumon manage -repos reploc \<location>' command to replace the Cluster Health Monitor repository location.

CRS-09503: The system monitor service on this host is unable to communicate with the Cluster Logger Service on host string, and will log data to the local repository.

Cause: Communication was lost with the Cluster Logger Service node.

Action: Verify all network connections between cluster nodes and repair any problematic connections. If no network problems are found,

1\. Run diagcollection.pl.

2\. Contact Oracle Support Services.

CRS-09504: The Cluster Logger Service on host string is dropping the Cluster Health Monitor node view. Details at string in string.

Cause: The Cluster Logger Service was unable to insert Cluster Health Monitor node view into Cluster Health Monitor repository.

Action: Contact Oracle Support Services.

CRS-09505: The Cluster Health Monitor repository is deleted due to corruption and the Cluster Logger Service is disabled on string. Details at string in string.

Cause: A critical error occurred while operating on Cluster Health Monitor repository.

Action: Contact Oracle Support Services.

CRS-09506: The system monitor service local repository is disabled on the host string. Details at string in string.

Cause: An internal error occurred while writing to the system monitor service local repository.

Action: Contact Oracle Support Services.

CRS-09507: The maximum Cluster Health Monitor repository retention time is reached. Deleting the oldest Cluster Health Monitor node views in age order.

Cause: The maximum time for which the oldest Cluster Health Monitor node view will be available on Cluster Health Monitor repository was reached.

Action: If necessary, use 'oclumon manage -repos resize \<size>' command to change the retention time.

CRS-09508: The Cluster Health Monitor repository retention time cannot be changed due to lack of disk space on node string.

Cause: The Cluster Health Monitor retention time condition could not be fulfilled because the Cluster Health Monitor repository ran out of disk space at run time at the repository location.

Action: Use the 'oclumon manage -repos reploc \<location>' command to replace the Cluster Health Monitor repository with a disk location that has at least 1GB of available space per cluster node.

CRS-09509: The new Cluster Logger Service master is string.

Cause: A new Cluster Logger Service master node was elected.

Action: None

CRS-09510: The new Cluster Logger Service replica is string.

Cause: A new Cluster Logger Service replica node was elected.

Action: None

CRS-09520: The storage of Grid Infrastructure Management Repository is number% full. The storage location is 'string'.

Cause: The storage of Grid Infrastructure Management Repository was close to full. This storage can be a shared file system or an Oracle ASM disk group.

Action: Make sure there is sufficient free space in repository location.

CRS-09600: Failed to initialize string daemon

Cause: An error occurred during initialization.

Action: Report this error to Oracle Support Services.

CRS-09603: Failed to read configuration files

Cause: An error encountered while retrieving information from configuration files.

Action: Report this error to Oracle Support Services.

CRS-09607: Cannot spawn thread for string

Cause: An error encountered while spawning thread.

Action: Report this error to Oracle Support Services.

CRS-09608: ASM disk method failed

Cause: An error encountered with ASM disks configuration.

Action: Report this error to Oracle Support Services.

CRS-09609: Encountered cssd failure. Reinitializing CSSD layer.

Cause: An error was encountered with CSSD layer while retrieving information.

Action: Report this error to Oracle Support Services.

CRS-09610: Encountered a fatal internal error. Daemon string exiting.

Cause: A fatal error occurred with CSSD layer.

Action: Report this error to Oracle Support Services.

CRS-09611: Mark string disks encountered errors

Cause: An error occurred while accessing disk.

Action: Report this error to Oracle Support Services.

CRS-09612: Mark string disks failed

Cause: A fatal error occurred while accessing disk.

Action: Report this error to Oracle Support Services.

CRS-09615: Disk method Failure: string

Cause: Internal error occurred.

Action: Report this error to Oracle Support Services.

CRS-09616: Daemon started: string

Cause: A daemon process started successfully.

Action: None

CRS-09617: Invalid message type encountered

Cause: An invalid or corrupted message was received.

Action: Report this error to Oracle Support Services.

CRS-09618: Daemon stopped: string

Cause: A daemon process stopped successfully.

Action: None

CRS-10002: failed to allocate memory

Cause: Memory allocation failed.

Action: Correct the system memory problem and retry.

CRS-10004: unable to reach string address from local node

Cause: An attempt to reach the IP address specified failed.

Action: Make sure that the specified IP address is a valid IP address and is assigned to an interface. Make sure that there are no firewalls between local node and node on which specified IP address is hosted.

CRS-10005: unable to determine local hostname

Cause: The hostname could not be read.

Action: Check that the hostname for the local machine is valid. Look at the accompanying messages. If the problem persists, contact Oracle Support Services.

CRS-10006: APPVIP type needs a VIP name. Specify a VIP name using -vip commandline option

Cause: VIP resource name was missing in the command line for APPVIP type.

Action: Specify a VIP name using -vip option.

CRS-10008: unable to generate client ID for VIP type string, cluster name string, VIP resource name string

Cause: An attempt to generate client ID for specified cluster name, VIP type and resource name failed.

Action: Make sure that cluster name and VIP resource name do not exceed 252 characters. Make sure that VIP type is a valid VIP type. Refer to 'crsctl get clientid -help' for more information.

CRS-10010: unable to discover DHCP server in the network listening on port number for client ID string

Cause: An attempt to discover DHCP server listening on port specified failed.

Action: Make sure that DHCP servers exist on the network and are listening on port specified. If they are listening on a different port specify then specify that port using the -port option. For more information refer to help for 'crsctl discover dhcp' command.

CRS-10011: unable to request DHCP lease for client ID string on port number

Cause: An attempt to request DHCP lease for the specified client ID on specified port failed.

Action: Make sure that there are DHCP servers with IP addresses available on the network. If other DHCP servers are available which are listening on a different port specify an alternative port using the -port option. For more information refer to help for 'crsctl request dhcp' command.

CRS-10013: unable to release DHCP lease for client ID string, on port number

Cause: An attempt to release DHCP lease for the specified client ID on specified port failed.

Action: Make sure that there are DHCP servers listening on port specified. If the DHCP server is listening on a different port specify an alternative port using -port option. For more information refer to help for 'crsctl release dhcp' command.

CRS-10014: HOSTVIP type needs a node name. Specify a node name using -n option

Cause: Node name was missing in the command line for HOSTVIP type.

Action: For HOSTVIP type node name needs to be specified via -n option.

CRS-10015: VIP type string is invalid

Cause: An invalid VIP type was specified for DHCP client ID generation.

Action: Make sure that VIP type is a valid VIP type. Refer to 'crsctl get clientid -help' for more information.

CRS-10016: error obtaining local host DNS resolver configuration

Cause: An attempt to obtain local host DNS configuration failed.

Action: Make sure that the user executing the command has sufficient permission to read local system configuration.

CRS-10017: the number name servers configured on this system exceeds the number maximum allowed

Cause: An attempt to obtain local host DNS configuration failed because more name servers were found then allowed on this operating system.

Action: Reduce the number of name servers configured to the maximum allowed.

CRS-10023: Domain name look up for name string failed. Operating system error: string

Cause: An attempt to query DNS servers for name specified failed.

Action: Look at accompanying messages for more information on the failure.

CRS-10029: could not verify if port number at address string is in use

Cause: An attempt to verify if port at address specified is in use failed.

Action: Make sure that the user has permission to create socket at port specified. For ports < 1024 user should be root. Also look at the accompanying messages for more information.

CRS-10030: could not verify if port number on local node is in use

Cause: An attempt to verify if port specified on local node is in use failed.

Action: Make sure that the user has permission to create socket at port specified. For ports < 1024 the user should be root. Also look at the accompanying messages for more information.

CRS-10033: could not stop the DNS listening daemon running on port number at address string

Cause: An attempt to stop the DNS listening daemon running on port and address specified failed.

Action: Make sure that the user has permission to send packets at the port specified. For ports < 1024 the user should be root. Also look at the accompanying messages for more information.

CRS-10034: could not stop the DNS listening daemon running on port number on local node

Cause: An attempt to stop the DNS listening daemon on local node running on port specified failed.

Action: Make sure that the user has permission to send packets at the port specified. For ports < 1024 the user should be root. Also look at the accompanying messages for more information.

CRS-10035: invalid name server 'string' specified in command line

Cause: An invalid IPv4 address was specified on the command line for -dnsserver option.

Action: Specify a valid IPv4 address on the command line.

CRS-10036: value for command line parameter 'string' is not an integer

Cause: An invalid value was specified for the specified command line parameter.

Action: Re-submit the request with an integer value.

CRS-10038: invalid IP address 'string' specified

Cause: An invalid IP address was supplied on command line.

Action: Supply an IP address that conforms to IETF RFC-791.

CRS-10039: invalid subnet 'string' specified

Cause: An invalid subnet was supplied to crsctl.

Action: Supply a subnet address that conforms to IETF RFC-950.

CRS-10040: unable to get list of network interfaces

Cause: An attempt to get the list of network interfaces failed.

Action: Look at the accompanying messages for more information.

CRS-10041: subnet 'string' is not configured on the node

Cause: The subnet specified did not match subnet of any network interface on this node.

Action: Specify a subnet that matches at least one network interface's subnet on this node.

CRS-10043: DNS daemon is not listening on port number at address string

Cause: An attempt to check if the DNS daemon is listening on port and address specified failed.

Action: Make sure that the address specified is reachable. Make sure that there is no firewall between the node on which this command was run and the address specified. Also look at the accompanying messages for more information.

CRS-10051: CVU found following errors with Clusterware setup: string

Cause: A resource-specific error was detected by the Clusterware Verification Utility (CVU). This message is accompanied by others providing details of the error condition.

Action: Respond based on the accompanying messages.

CRS-10100: Execution of crswrapexece.pl script with arguments 'string' fails.

Cause: crswrapexece.pl script failed when executed with the specific arguments.

Action: Check system log and crswrapexece.log for more details. Contact Oracle Support Services.

CRS-10101: Internal Error

Cause: Execution of crswrapexece.pl script failed due to missing argument.

Action: Contact Oracle Support Services.

CRS-10102: Failure to open environment file string.

Cause: The crswrapexece.pl script failed to open the environment file, which might be caused by hostname change or user edits.

Action: Check for the existence and permission of the environment file.

CRS-10103: Found string syntax errors in environment file string.

Cause: crswrapexece.pl found syntax errors in the provided environment file.

Action: Check and fix syntax error in the indicated environment file. If the problem persists, contact Oracle Support Services.

CRS-10131: Failure to create named pipe string. Details \[string\].

Cause: The specified named pipe could not be created. Oracle High Availability Service would not be able to restart if crashes.

Action: Check for the existence and permission of the parent directory, where the named pipe was created.

CRS-10132: Oracle High Availability Service was restarted at least string times within the last string seconds. Stop auto-restarting Oracle High Availability Service.

Cause: Oracle High Availability Service was restarted too rapidly within a short period of time.

Action: Check the Oracle High Availability Service log file to determine the cause. If the problem persists, contact Oracle Support Services.

CRS-10250: Database name is required to access database wallets. Use -name option to supply a database name.

Cause: The option -name was missing on the command line.

Action: For APPQOSDB wallet types -name is a mandatory parameter. Retry the command with -name option.