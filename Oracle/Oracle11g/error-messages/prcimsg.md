---
title: PRCI-01000 to PRCI-01145
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/prcimsg.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 84 PRCI-01000 to PRCI-01145

PRCI-01000: Failed to retrieve install information on local node using OUI location {0}

Cause: An attempt to retrieve install information on the local node from the specified location failed.

Action: Examine the accompanying error messages for details.

PRCI-01001: Failed to retrieve install information on remote node {0} using OUI location {1}

Cause: An attempt to retrieve install information on a remote node from the specified location failed.

Action: Examine the accompanying error messages for details.

PRCI-01100: Failed to get Vendor Cluster for CRS home {0}

Cause: Unable to locate vendor cluster library or execute lsnodes.

Action: Install Vendor Clusterware. Then try to run lsnodes again.

PRCI-01101: Failed to get Vendor Cluster for CRS home {0} on node {1}

Cause: Unable to locate vendor cluster library or execute lsnodes on the specified node.

Action: Install Vendor Clusterware on the specified node. Then try to run lsnodes again.

PRCI-01102: Failed to get OracleCM Cluster for CRS home {0}

Cause: Failed to get OracleCM Cluster for the local node using CRS home provided.

Action: Install Oracle 9i and make sure that /etc/ORCLcluster exists.

PRCI-01103: Failed to get OracleCM Cluster for CRS home {0} on node {1}

Cause: Failed to get OracleCM Cluster for the specified node using CRS home provided.

Action: Examine the accompanying error messages for details.

PRCI-01104: Failed to check Oracle Restart running state for Oracle Restart home {0}

Cause: Failed to check whether Oracle Restart is running from the specified home on the local node.

Action: Examine the accompanying error messages for details.

PRCI-01105: Failed to check Oracle Restart running state for Oracle Restart home {0} on node {1}

Cause: Failed to check whether Oracle Restart is running from the specified home on the specified node.

Action: Examine the accompanying error messages for details.

PRCI-01106: Failed to check Oracle Restart configuration state for Oracle Restart home {0} on node {1}

Cause: Failed to check whether Oracle Restart is configured for the specified home on the specified node.

Action: Examine the accompanying error messages for details.

PRCI-01107: Failed to check CRS running state for CRS home {0}

Cause: Failed to check whether Oracle Clusterware is running from the specified home on the local node.

Action: Examine the accompanying error messages for details.

PRCI-01108: Failed to check CRS running state for CRS home {0} on node {1}

Cause: Failed to check whether Oracle Clusterware is running from the specified home on the specified node.

Action: Examine the accompanying error messages for details.

PRCI-01109: Failed to check CRS configuration state for CRS home {0}

Cause: Failed to check whether Oracle Clusterware is configured for the specified home on the specified node.

Action: Examine the accompanying error messages for details.

PRCI-01110: Failed to check CRS configuration state for CRS home {0} on node {1}

Cause: Failed to check whether Oracle Clusterware is configured for the specified home on the local node.

Action: Examine the accompanying error messages for details.

PRCI-01111: File path is null

Cause: The specified file is null or an empty string.

Action: Provide a valid file path that is not null.

PRCI-01112: Directory name passed was null

Cause: The specified directory name is null or an empty string.

Action: Provide a valid directory name that is not null.

PRCI-01113: Directory {0} does not exist

Cause: Could not find the specified directory or it was a file instead of a directory.

Action: Provide an existing directory name.

PRCI-01114: Node name is null

Cause: The specified node name is null or an empty string.

Action: This is an internal error. Contact Oracle Support Services.

PRCI-01115: argument passed is null

Cause: The specified database name is null or an empty string.

Action: This is an internal error. Contact Oracle Support Services.

PRCI-01116: Failed to check if a database named {0} exists

Cause: Failed to execute the command 'crsctl stat resource <database\_resource\_name>' to decide whether the specified database exists or not.

Action: Examine the accompanying error messages for details.

PRCI-01117: Failed to retrieve list of databases under high availability management

Cause: Failed to execute the command 'crsctl stat resource -w TYPE=ora.database.type \<filter>' in order to get the list of databases managed by Oracle Restart.

Action: Examine the accompanying error messages for details.

PRCI-01118: Failed to determine if database {0} depends on Automatic Storage Management

Cause: Failed to execute crsctl command to decide whether the specified database depended on Automatic Storage Management (ASM).

Action: Examine the accompanying error messages for details.

PRCI-01119: Failed to check if a database named {0} exists on node {1}

Cause: Failed to decide whether the specified database exists or not on the specified node because the specified node is null or an invalid node or crsctl command execution failed.

Action: Examine the accompanying error messages for details.

PRCI-01120: Failed to retrieve list of databases under high availability management for node {0}

Cause: Failed to get the list of database managed by Oracle Restart on the specified node because the specified node is null or an invalid node or crsctl command execution failed.

Action: Examine the accompanying error messages for details.

PRCI-01121: Failed to determine if database {0} depends on Automatic Storage Management on node {1}

Cause: Failed to execute crsctl command to decide whether the specified database depended on Automatic Storage Management (ASM) on the specified node because the specified node is null or an invalid node or crsctl command execution failed.

Action: Examine the accompanying error messages for details.

PRCI-01122: Failed to determine if the public network is using dynamic address assignment (DHCP)

Cause: An attempt to determine whether the public network is using dynamic address assignment (DHCP) failed.

Action: Examine the accompanying error messages for details.

PRCI-01123: CRS home does not exist on the local node

Cause: CRS home is not installed on the local node.

Action: Install a CRS home using the Oracle Universal Installer.

PRCI-01124: Oracle Restart home does not exist on the local node

Cause: Oracle Restart home is not installed.

Action: Install an Oracle Restart home using the Oracle Universal Installer.

PRCI-01125: CRS home does not exist on node {0}

Cause: CRS home is not installed on the specified node.

Action: Install a CRS home using the Oracle Universal Installer.

PRCI-01126: Oracle Restart home does not exist on node {0}

Cause: Oracle Restart home is not installed on the specified node.

Action: Install an Oracle Restart home using the Oracle Universal Installer.

PRCI-01127: CRS active version cannot be queried in a non-cluster environment

Cause: Clusterware is not configured.

Action: Ensure that Clusterware is configured.

PRCI-01128: Failed to check Oracle Restart configuration state

Cause: Oracle Restart may not be configured

Action: Ensure that Oracle Restart is installed and configured

PRCI-01129: Failed to check Oracle Restart configuration state on node {1}

Cause: Oracle Restart may not be configured

Action: Ensure that Oracle Restart is installed and configured

PRCI-01130: Failed to check CRS configuration state

Cause: Clusterware CRS may not be configured

Action: Ensure that Clusterware CRS is installed and configured

PRCI-01131: Failed to check CRS configuration state on node {1}

Cause: Clusterware CRS may not be configured

Action: Ensure that Clusterware CRS is installed and configured

PRCI-01132: Failed to get clustername for CRS home {0} and version {1}

Cause: Clusterware is not configured and CRS stack is not up

Action: Ensure that Clusterware CRS is installed and configured and the stack is up.

PRCI-01133: The IP address {0} does not have the same number of fields with the subnet mask {1}

Cause: IP address is in IPv4 address format while the subnet mask is in IPv6 address format or the other way around.

Action: Ensure that both the IP address and the subnet mask use the same representation (the longer required among IPv4 and IPv6).

PRCI-01134: Applying subnet mask {0} to IP address {1} resulted in an invalid IP address format

Cause: This won't ever happen. Message added just in case.

Action: None

PRCI-01135: Failed to check if path {0} on node {1} is on ACFS

Cause: An attempt to determine if the specified path is on ACFS failed. This can occur because:

1\. The Clusterware stack is down on the specified node.

2\. ASM is down on the specified node.

3\. A diskgroup associated with the path is not online.

4\. The path is not mounted.

Action: Perform checks corresponding to the above causes:

1\. Ensure the Clusterware stack is running on the specified node.

2\. Ensure that ASM is running on the specified node.

3\. Ensure that the diskgroup associated with the path is online.

4\. Ensure that the file system is mounted on the node.

PRCI-01136: The specified path {0} is not on Oracle Automatic Storage Manager Cluster File System (ACFS)

Cause: The specified path is not on ACFS.

Action: Specify a path that is on ACFS. This check will only accept paths on ACFS.

PRCI-01137: Failed to check if path {0} is on ACFS

Cause: An attempt to determine if the specified path is on ACFS failed. This can occur because:

1\. The Clusterware stack is down on the specified node.

2\. ASM is down on the specified node.

3\. A diskgroup associated with the path is not online.

4\. The path is not mounted.

Action: Perform checks corresponding to the above causes:

1\. Ensure the Clusterware stack is running on the specified node.

2\. Ensure that ASM is running on the specified node.

3\. Ensure that the diskgroup associated with the path is online.

4\. Ensure that the file system is mounted on the node.

PRCI-01140: Error occurred while reading input from console

Cause: An attempt to read input from console failed

Action: Make sure that the process running this program has a valid standard input (stdin).

PRCI-01141: Failed to get volume device for path {0}

Cause: An attempt to retrieve the volume device for the given ACFS path failed. This can occur because:

1\. The Clusterware stack is down on the node.

2\. ASM is down on the node.

3\. A diskgroup associated with the path is not online.

4\. The path is not mounted.

Action: Perform checks corresponding to the above causes:

1\. Ensure the Clusterware stack is running on the node.

2\. Ensure that ASM is running on the node.

3\. Ensure that the diskgroup associated with the path is mounted.

4\. Ensure that the file system is mounted on the node.

PRCI-01142: Failed to get volume device for path {0} on node {1}

Cause: An attempt to retrieve the volume device for the given ACFS path failed. This can occur because:

1\. The Clusterware stack is down on the specified node.

2\. ASM is down on the specified node.

3\. A diskgroup associated with the path is not online.

4\. The path is not mounted.

Action: Perform checks corresponding to the above causes:

1\. Ensure the Clusterware stack is running on the specified node.

2\. Ensure that ASM is running on the specified node.

3\. Ensure that the diskgroup associated with the path is mounted.

4\. Ensure that the file system is mounted on the specified node.

PRCI-01143: Error executing the script {0} on nodes {1}

Cause: An error occurred in executing the script on the list of nodes mentioned. This message is accompanied by others providing details of the error.

Action: Correct the problem indicated by the accompanying messages and retry.

PRCI-01144: Failed to retrieve Oracle Grid Infrastructure home path

Cause: An attempt to read Grid Infrastructure home path from OLR configuration file or registry entry failed.

Action: Examine the accompanying error messages for details.

1\. Make sure Grid Infrastructure is configured as either Oracle Clusterware or Oracle Restart,and that the invoking user is able to read the configuration.

2\. Issue the command '\<GI home>/srvm/admin/getcrshome' and examine the resulting output.

PRCI-01145: Failed to retrieve Oracle Grid Infrastructure home path on node {0}

Cause: An attempt to read Grid Infrastructure home path from OLR configuration file or registry entry on specified node failed.

Action: Examine the accompanying error messages for details.

1\. Make sure Grid Infrastructure is configured as either Oracle Clusterware or Oracle Restart,and that the invoking user is able to read the configuration.

2\. Issue the command '\<GI home>/srvm/admin/getcrshome' and examine the resulting output.