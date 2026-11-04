---
title: PRKC-01000 to PRKC-01168
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/prkcmsg.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 71 PRKC-01000 to PRKC-01168

PRKC-01000: No active nodes detected in the cluster

Cause: The active node list of the cluster could not be retrieved. This could occur if the operating system dependent clusterware was not functioning properly in one or more nodes in the cluster, or because there was no clusterware installed on the system.

Action: Check the state of the cluster by running 'lsnodes' binary from your ORACLE\_HOME/bin and see if it prints the node list correctly.

PRKC-01001: Error submitting commands in the buffer

Cause: This is an internal error.

Action: Contact Oracle Support Services.

PRKC-01002: All the submitted commands did not execute successfully

Cause: Either a node failed in the middle of a manageability operation, or the communication between nodes was disrupted.

Action: Check the state of your cluster by running 'lsnodes' binary from your ORACLE\_HOME/bin and see if it prints the node list correctly.

PRKC-01004: Problem in copying file to nodes

Cause: Attempted file copy operation(s) from the local node to one or more nodes in the cluster and one or multiple of those copy file operations failed. Possible causes: 1) One or more file copy operations to nodes in the cluster failed. 2) The destination directory did not have write permission for the user on one or more of the nodes.the source file did not exist. 3) The 'rcp' command to one or more nodes failed on UNIX platforms.

Action: 1) Check that the source file exists. 2) Check that all nodes in the cluster are up. 3) Check that destination directory has write permission for the user. 4) On UNIX based platforms check that user can do 'rcp' to all the nodes.

PRKC-01005: Problem in removing file from nodes

Cause: Attempted file remove operation(s) from the local node to one or more nodes in the cluster and one or multiple of those file remove operations failed. Possible causes: 1) One or more nodes failed during the operation. 2) The destination directory did not have write permission for the user on one or more of the nodes. 3) The source file did not exist. 4) The 'rcp' command to one or more nodes failed on UNIX platforms.

Action: Check the accompanying error messages for details.

PRKC-01006: Problem in moving file to nodes

Cause: Attempted file move operation(s) from the local node to one or more nodes in the cluster and one or multiple of those move file operations failed. Possible causes: 1) One or more nodes failed during the operation. 2) The destination directory did not have write permission for the user on one or more of the nodes. 3) The source file did not exist. 4) The 'rcp' command to one or more nodes failed on UNIX platforms.

Action: Check the accompanying error messages for details.

PRKC-01007: Problem in creating directories on the nodes

Cause: Attempted directory create operation(s) from the local node to one or more nodes in the cluster and one or multiple of those directory create operations failed. Possible causes: 1) One or more nodes failed during the operation. 2) The destination directory did not have write permission for the user on one or more of the nodes. 3) The 'rcp' command to one or more nodes failed on UNIX platforms.

Action: Check the accompanying error messages for details.

PRKC-01009: Failed to start the service on all nodes

Cause: The service failed to start on one or more nodes of the cluster.

Action: Check if all the nodes in cluster are up and look in the clusterware alert log.

PRKC-01010: Failed to stop the service on all nodes

Cause: The service failed to stop on one or more nodes of the cluster.

Action: Check if all the nodes in cluster are up and service is still up on failed nodes. Look in the clusterware alert log.

PRKC-01011: Failed to delete the service from all nodes

Cause: The service failed to be deleted on one or more nodes of the cluster.

Action: Check if all the nodes in cluster are up and service is still registered. Look in the clusterware alert log.

PRKC-01012: Failed to create the service on all nodes

Cause: The service failed to be created on one or more nodes of the cluster.

Action: Check if all the nodes in cluster are up. Look in the clusterware alert log.

PRKC-01016: Failed to retrieve value of the enviornment variable "{0}", {1}

Cause: Attempted to retrieve value of an environment variable which was not defined.

Action: Define the environment variable.

PRKC-01017: Problem restarting GSD

Cause: GSD (Global Services Daemon) could not be started on the local node. This could occur if the operating system dependent clusterware was not functioning properly or there is already a running GSD.

Action: Check the state of your clusterware by running 'lsnodes' from ORACLE\_HOME/bin. It should list the nodes in the cluster. Try 'gsdctl stop' and then 'gsdctl start' again.

PRKC-01018: Error getting coordinator node

Cause: This could occur if the operating system dependent clusterware was not functioning properly.

Action: Use 'gsdctl stop' on each node to stop the GSDs. Use 'gsdctl start' on each node in the cluster.

PRKC-01019: Error creating handle to GSD daemon on the node {0}

Cause: Global Services Daemon was not running on the node.

Action: Use 'gsdctl stat' to check the status of the daemon. Use 'gsdctl start' to start it.

PRKC-01020: Exception while executing the operation on the remote node {0}

Cause: Attempted to execute an operation on the remote node when the Global Services Daemon was not up on the remote node {0}.

Action: Start the Global Services Daemon on the remote node using 'gsdctl start'.

PRKC-01021: Problem in the clusterware

Cause: The operating system dependent clusterware could not be contacted. This could occur because the operating system dependent clusterware was not functioning properly.

Action: Check the state of the operating system dependent clusterware.

PRKC-01022: Could not get node name for node {0} in {1}

Cause: The operating system dependent clusterware could not be contacted. This could occur because the operating system dependent clusterware was not functioning properly.

Action: Check the state of the operating system dependent clusterware using 'lsnodes -n'.

PRKC-01025: Failed to create a file under the filepath {0} because the filepath is not executable or writable

Cause: The directory of the specified filepath did not have execute or write permission. So the temporary file could not be created to test whether the filepath was shared among nodes.

Action: Make the directory of the specified filepath executable and writable.

PRKC-01141: Oracle Restart is not supported in version {0}. It is supported from version {1} onwards

Cause: This is an internal error.

Action: Contact Oracle Support Services.

PRKC-01144: File "{0}" not found.

Cause: The file was not found in the file system.

Action: Make sure that the file exists in the file system.

PRKC-01148: Failed to get host name for the local computer

Cause: An error occurred while attempting to retrieve the TCP/IP host name

Action: Correct the problem indicated by the accompanying error messages.

PRKC-01149: Failed to get OCR locations

Cause: An error occurred while attempting to retrieve the OCR locations, possibly due to missing or incorrrect OCR locations file, or incomplete OCR configuration, or due to missing or incorrect SRVM shared libraries.

Action: Verify that the Clusterware has been correctly installed and configured. Verify that the ocr.loc file is present and readable in the appropriate location for your platform.

PRKC-01150: Failed to get drive letters used on following nodes: "{0}"

Cause: An error occurred while attempting to retrieve used drive letters on one or more nodes.

Action: Look at the accompanying messages and fix the error(s). The messages typically relate to a node not being reachable, or the remote execution service not running on the node, or some permissions issue when attempting to use the remote execution service on the remote node.

PRKC-01151: The given path "{0}" does not exist

Cause: The specified path may not have been created or an incorrect path has been specified.

Action: Make sure that the given path exists by specifying a correct existing path.

PRKC-01152: The specified path "{0}" is not a directory

Cause: The specified path may be a file, not a directory, or an incorrect path may have been specified.

Action: Make sure to specify a path that is a valid directory path.

PRKC-01153: No directory is available on the remote node "{0}" to copy the binary RemoteExecService.exe

Cause: Either the path defined by value of registry key HKEY\_LOCAL\_MACHINE/System/CurrentControlSet/Services/OracleRemExecService is not available on the remote node, or the c:/temp/ directory is not available or not accessible on the specified remote node.

Action: Make sure that the required path is available on the remote node.

PRKC-01155: The node list provided had only one entry or had multiple entries that were duplicates of a single nodename entry

Cause: The list of nodes provided for the shared path check was either only one node, or the list included entries that were duplicates of the same single node.

Action: Please provide the correct nodelist for the cluster on which the check is being called, making sure that there are at least two distinct entries.

PRKC-01156: Failed to validate raw device "{0}" -- Details: {1}

Cause: The raw device was not an existing device that could be opened and recognized by the OS as a "raw/character" device type.

Action: Make sure the supplied value identifies a valid raw device that can be opened as a "raw/character" device type.

PRKC-01157: Failed to validate raw device "{0}"

Cause: The raw device was not an existing device that could be opened and recognized by the OS as a "raw/character" device type.

Action: Make sure the supplied value identifies a valid raw device that can be opened as a "raw/character" device type.

PRKC-01158: Failed to validate raw device "{0}" -- Details: {1}

Cause: The device was not an existing device that could be opened and recognized by the OS as either "raw/character" or a "block" device type.

Action: Make sure the supplied value identifies a valid device that can be opened as a "raw/character" or "block" device type.

PRKC-01159: Failed to validate device "{0}"

Cause: The device was not an existing device that could be opened and recognized by the OS as either "raw/character" or a "block" device type.

Action: Make sure the supplied value identifies a valid device that can be opened as a "raw/character" or "block" device type.

PRKC-01160: Failed to retrieve the value of environment variable "{0}" on following nodes: "{1}", \[{2}\]

Cause: An error occurred while attempting to retrieve value of environment variable on one or more nodes due to the node not being reachable, or the remote execution service not running on the node, or some permissions issue when attempting to use the remote execution service on the remote node.

Action: Look at the accompanying messages and respond accordingly.

PRKC-01161: Failed to retrieve the Windows domain on following nodes: "{0}"

Cause: An error occurred while attempting to retrieve the Windows domain on one or more nodes. The possible causes include:"

\- A node is not reachable.

\- Remote execution service is not running on the node.

\- Permissions problems prevented use of remote execution service on a node.

Action: Look at the accompanying messages and respond accordingly.

PRKC-01162: "{0}" is not a file

Cause: The indicated object was expected to be a file, but it was not.

Action: Make sure that the indicated object is a file and not a directory.

PRKC-01163: {0} Exception occurred while determining validity of storage type.

Cause: An error occurred while getting storage type of the given path. Null arguments might have been passed.

Action: Make sure that the native api is passing non null arguments.

PRKC-01164: invalid command or arguments

Cause: This is an internal error.

Action: Contact Oracle Support Services.

PRKC-01165: Failed to set up Windows service OracleRemoteExecService on node '{0}'

Cause: An error occurred while setting up OracleRemoteExecService on the specified nodes."

Action: Look at the accompanying messages and respond accordingly.

PRKC-01166: Storage is partially shared. Details: {0}

Cause: A subset of the nodes provided shared the given filesystem path with the local node.

Action: Mount the NFS filesystem on the node(s) that do not share the filesystem path.

PRKC-01167: Failed to resolve the specified path "{0}" to its physical path on following nodes: "{1}", \[{2}\]

Cause: An error occurred while attempting to resolve the path on one or more nodes due to the node not being reachable, the remote execution service not running on the node, or some permissions issue when attempting to use the remote execution service on the remote node.

Action: Look at the accompanying messages and respond accordingly.

PRKC-01168: Failed to get sub-keys of registry key {0}

Cause: Could not find any sub-keys for the given registry key.

Action: Check manually via 'regedit' that the registry key exists and has sub keys under it. If so, retry. Otherwise, contact Oracle Support Services.