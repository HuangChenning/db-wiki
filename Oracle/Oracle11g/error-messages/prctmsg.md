---
title: PRCT-01000 to PRCT-01415
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/prctmsg.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 88 PRCT-01000 to PRCT-01415

PRCT-01000: File path is null

Cause: The supplied path is set to null.

Action: Oracle internal error. Contact Oracle Support Services..

PRCT-01001: Node name is null

Cause: The supplied node name is set to null.

Action: Oracle internal error. Contact Oracle Support Services.

PRCT-01003: Failed to run "{0}" on node "{1}"

Cause: Failed to execute the specified command on the specifed node.

Action: Oracle internal error. Contact Oracle Support Services.

PRCT-01004: Directory name passed was null

Cause: The supplied directory name is set to null.

Action: Oracle internal error. Contact Oracle Support Services.

PRCT-01005: Directory {0} does not exist

Cause: The supplied directory path does not exist.

Action: Oracle internal error. Contact Oracle Support Services.

PRCT-01006: Failed to retrieve cluster name from node "{0}"

Cause: Failed to get the cluster name using 'olsnodes -c' from the specified node.

Action: Execute 'olsnodes -c' from the specified node and check the output of the command. Fix the problem according to the error message given in the command output.

PRCT-01007: Failed to retrieve local node name

Cause: Underlying call failed to get the local hostname.

Action: Please check the underlying error message.

PRCT-01008: Failed to retrieve node names

Cause: Failed to get the node names using 'olsnodes' command.

Action: Execute command 'olsnodes' and check the output of the command. Fix the problem according to the error message given in the command output.

PRCT-01009: crsctl execution failed. Detailed error: {0}

Cause: Failed to execute crsctl command.

Action: Examine the accompanying error message for details.

PRCT-01010: crsctl execution failed on node {0}. Detailed error: {1}

Cause: Failed to execute crsctl command on the specifed node.

Action: Examine the accompanying error message for details.

PRCT-01011: Failed to run "{0}". Detailed error: {1}

Cause: Failed to execute the specified command on the local node.

Action: Execute the specified command from the console and check the result. Fix the problem according to the error message given in the command output.

PRCT-01012: Invalid file path {0}

Cause: The supplied path does not exist.

Action: Oracle internal error. Contact Oracle Support Services.

PRCT-01013: Failed to start remote execution server on local node.

Cause: A remote execution server is required on this platform, but an attempt to start one on this node failed. This message is accompanied by other(s) providing details on the failure.

Action: Correct the problem indicated by the accompanying error messages. On Windows systems, make sure that the current user has authority to remove and create directories and files in the Temp directory and to create and delete registry entries.

PRCT-01014: Internal error: {0}

Cause: An internal error occurred. The included value is an internal identifier.

Action: Oracle internal error. Contact Oracle Support Services.

PRCT-01015: Version supplied is null

Cause: The supplied version was set to null.

Action: Oracle internal error. Contact Oracle Support Services.

PRCT-01050: Failed to parse output returned by kfod when executing kfod at location {0}

Cause: Failed to parse the output returned by executing kfod because the output string is null or has fewer rows than expected

Action: This is an internal error. Contact Oracle Support Services.

PRCT-01051: Failed to parse the output returned by kfod for node {0} when executing kfod at location {1}

Cause: Failed to parse the output returned by executing kfod on the specified node because the output string is null or has fewer rows than expected.

Action: This is an internal error. Contact Oracle Support Services.

PRCT-01052: Failed to parse output {0} returned by kfod when executing kfod at location {1}

Cause: Failed to parse the output returned by executing kfod because the output has fewer columns than expected.

Action: This is an internal error. Contact Oracle Support Services.

PRCT-01053: Failed to parse output {0} returned by kfod for node {1} when executing kfod at location {2}

Cause: Failed to parse the output returned by executing kfod on the specified node because the output has fewer columns than expected.

Action: This is an internal error. Contact Oracle Support Services.

PRCT-01054: Fail to retrieve ASM active version for local node

Cause: Failed to get the active version of ASM by executing 'kfod nohdr=true op=version hostlist=\<hostlist>'.

Action: This is an internal error. Contact Oracle Support Services.

PRCT-01055: Fail to retrieve ASM active version for node {0}. kfod execution failed at location {1}. Detailed error: {2}

Cause: Failed to get the active version of ASM by executing 'kfod nohdr=true op=version hostlist=\<hostlist>' on the specified node.

Action: Examine the accompanying error messages for details.

PRCT-01056: Fail to retrieve ASM instance type. kfod execution failed at location {0}. Detailed error: {1}

Cause: Failed to get the instance type for ASM instance by executing 'kfod nohdr=true op=version'.

Action: Examine the accompanying error messages for details.

PRCT-01057: The value of ASM instance type {0} is not correct

Cause: The value of ASM instance type is invalid.

Action: The instance type of ASM can only be YES or NO.

PRCT-01058: Fail to check if ASM is running on node {0}. kfod execution failed at location {1}. Detailed error: {2}

Cause: Failed to check whether ASM is running by executing 'kfod nohdr=true op=insts hostlist=\<hostlist>'.

Action: Examine the accompanying error messages for details.

PRCT-01059: Fail to retrieve list of disk group names for node {0}. kfod execution failed at location {1}. Detailed error: {2}

Cause: Failed to get the diskgroup names by executing 'kfod nohdr=true op=groups hostlist=\<hostlist>'.

Action: Examine the accompanying error messages for details.

PRCT-01060: Fail to check if ASM is in rolling migration. kfod execution failed at location {1}. Detailed error: {2}

Cause: Failed to check whether ASM is in rolling migration by executing 'kfod nohdr=true op=rm'.

Action: Examine the accompanying error messages for details.

PRCT-01100: Failed to retrieve ACFS active version for local node

Cause: Failed to execute acfsutil to retrieve the ACFS active version on the local node.

Action: Review the underlying error messages that provides the details of why acfsutil execution failed. Resolve the reported problem and retry.

PRCT-01101: Failed to retrieve ACFS active version for node {0}. acfsutil execution failed at file location {1}. Detailed error: {2}

Cause: Failed to execute acfsutil to retrieve the ACFS active version on the supplied node.

Action: Review the underlying error messages that provides the details of why acfsutil execution failed. Resolve the reported problem and retry.

PRCT-01102: Failed to parse output when executing acfsutil at file location {0}

Cause: Unable to parse output returned by acfsutil.

Action: Oracle internal error. Contact Oracle Support Services.

PRCT-01103: Failed to parse the output for node {0} when executing acfsutil at file location {1}

Cause: Unable to parse output returned by acfsutil on the supplied node.

Action: Oracle internal error. Contact Oracle Support Services.

PRCT-01104: Failed to parse output {0} when executing acfsutil at file location {1}

Cause: Unable to parse output returned by acfsutil at specified location.

Action: Oracle internal error. Contact Oracle Support Services.

PRCT-01105: Failed to parse output {0} for node {1} when executing acfsutil at file location {2}

Cause: Unable to parse output returned by acfsutil at specified location on the supplied node.

Action: Oracle internal error. Contact Oracle Support Services.

PRCT-01109: Failed to get diskgroup names for node {0}

Cause: Unable to parse disgkroup names returned by acfsutil on the supplied node.

Action: Oracle internal error. Contact Oracle Support Services.

PRCT-01111: Received empty result while getting ACFS Mount Points on node {1}

Cause: The output returned by acfsutil is empty.

Action: Oracle internal error. Contact Oracle Support Services.

PRCT-01114: Execution of acfsutil command failed on node {0} for location {1}

Cause: Failed to execute acfsutil on the supplied node at the specified location.

Action: Review the underlying error messages that provides the details of why acfsutil execution failed. Resolve the reported problem and retry.

PRCT-01115: Execution of acfsutil failed on node {0} with result {1}

Cause: Failed to execute acfsutil on the supplied node.

Action: Review the underlying error messages that provides the details of why acfsutil execution failed. Resolve the reported problem and retry.

PRCT-01116: Invalid partition path {0} specified to acfsutil on node {1}

Cause: The supplied path path does not exist.

Action: Supply a valid partition path and retry.

PRCT-01117: Received empty result while getting ACFS Disk Groups on node {1}

Cause: The output returned by acfsutil is empty.

Action: Oracle internal error. Contact Oracle Support Services.

PRCT-01118: Received empty result while getting total space at file location {0} on node {1}

Cause: The output returned by acfsutil is empty.

Action: Oracle internal error. Contact Oracle Support Services.

PRCT-01119: Received empty result while getting free space at file location {0} on node {1}

Cause: The output returned by acfsutil is empty.

Action: Oracle internal error. Contact Oracle Support Services.

PRCT-01120: A NULL path has been specified for the location on node {0}

Cause: A null path was provided for the location.

Action: Oracle internal error. Contact Oracle Support Services.

PRCT-01121: Execution of acfsutil failed on local node with result {0}

Cause: Execution of acfsutil failed on the local node.

Action: Review the underlying error messages that provides the details of why acfsutil execution failed. Resolve the reported problem and retry.

PRCT-01122: Received empty result while getting mountpoint for path {0} on the local node

Cause: acfsutil returned an empty value when querying for the mountpoint of a specified path.

Action: Oracle internal error. Contact Oracle Support Services.

PRCT-01123: The mountpoint is either set to null or empty

Cause: The supplied mountpoint is either an empty string or is set to null.

Action: Oracle internal error. Contact Oracle Support Services.

PRCT-01124: Received empty result while getting volume device for mountpoint {0} on the local node

Cause: acfsutil returned an empty value when querying for the volume device of a specified mountpoint.

Action: Oracle internal error. Contact Oracle Support Services.

PRCT-01125: The volume device is either set to null or empty

Cause: The supplied volume device is either an empty string or is set to null.

Action: Oracle internal error. Contact Oracle Support Services.

PRCT-01126: Received empty result while getting mountpoint for volume device {0} on the local node

Cause: acfsutil returned an empty value when querying for the volume device of a specified mountpoint.

Action: Oracle internal error. Contact Oracle Support Services.

PRCT-01127: Received empty result while getting all volume devices on the local node

Cause: No ACFS volume devices has been created.

Action: Use usmca to create ACFS volume devices.

PRCT-01128: ACFS is not supported on this operating system

Cause: ACFS is not supported on the underlying operating system.

Action: Run srvctl filesystem command on a supported operating system.

PRCT-01129: Execution of ACFS driver state check failed on local node with result {0}

Cause: Execution of ACFS driver state check failed on the local node

Action: Review the underlying error messages that provides the details of why ACFS driver state check execution failed. Resolve the reported problem and retry.

PRCT-01130: Execution of advmutil failed on local node with result {0}

Cause: Execution of advmutil failed on the local node

Action: Review the underlying error messages that provides the details of why advmutil execution failed. Resolve the reported problem and retry.

PRCT-01131: Failed to retrieve mount point for volume device {0}

Cause: No ACFS filesystem was mounted for the specified volume device.

Action: Mount the filesystem and retry.

PRCT-01132: ACFS driver state check with "{0}" option on local node failed to display any output

Cause: No output was captured when executing ACFS driver state check with the specified option on the local node.

Action: Internal error. Contact Oracle Support Services.

PRCT-01133: ACFS driver state check with "{0}" option on node {1} failed to display any output

Cause: No output was captured when executing ACFS driver state check with the specified option on the specified node.

Action: Internal error. Contact Oracle Support Services.

PRCT-01134: Execution of ACFS driver state check failed on node {0} with result {1}

Cause: Execution of ACFS driver state check failed on the specified node.

Action: Review the underlying error messages that provides the details of why ACFS driver state check execution failed. Resolve the reported problem and retry.

PRCT-01135: This platform does not support a default location for "{0}"

Cause: An attempt to run the 'acfsutil' command did not provide a location of this binary

Action: Internal error. Contact Oracle Support Services.

PRCT-01149: Failed to retrieve cluster name

Cause: The olsnodes command executed successfully, but there was no output.

Action: This is an internal error. Contact Oracle Support Services.

PRCT-01150: Failed to retrieve cluster name

Cause: Clusterware is not running.

Action: Make sure the clusterware is running.

PRCT-01151: Failed to retrieve cluster nodes status

Cause: Clusterware is not running.

Action: Make sure the clusterware is running.

PRCT-01152: Received empty result while getting cluster nodes Status Map

Cause: The olsnodes command executed successfully, but there was no output.

Action: This is an internal error. Contact Oracle Support Services.

PRCT-01153: Received empty result while getting a list of pinned and unpinned nodes in the cluster

Cause: The olsnodes command executed successfully, but there was no output.

Action: This is an internal error. Contact Oracle Support Services.

PRCT-01154: Failed to retrieve private host name for all cluster nodes. Detailed error: {0}

Cause: Clusterware is not running.

Action: Make sure the clusterware is running.

PRCT-01155: Received empty result while getting the private interconnect for nodes in the cluster

Cause: The olsnodes command executed successfully, but there was no output.

Action: This is an internal error. Contact Oracle Support Services.

PRCT-01200: Failed to retrieve disk group name for volume device {0}. asmcmd execution failed at location {1}. Detailed error: {2}

Cause: Unable to retrieve the disk group name for the specified volume device

Action: Check that ASM instance is running on the local node.

PRCT-01201: Failed to retrieve volume name for volume device {0}. asmcmd execution failed at location {1}. Detailed error: {2}

Cause: Unable to retrieve the volume name for the specified volume device

Action: Check that ASM instance is running on the local node.

PRCT-01202: Failed to parse output returned by asmcmd when executing asmcmd at location {0}

Cause: Unable to parse output returned by asmcmd.

Action: Oracle internal error. Contact Oracle Support Services.

PRCT-01203: Failed to parse the output returned by asmcmd for node {0} when executing asmcmd at location {1}

Cause: This is an internal error.

Action: Contact Oracle Support Services.

PRCT-01204: Failed to find volume device {0}. asmcmd execution failed at location {1}. Detailed error: {2}

Cause: Volume device does not exist.

Action: Create the volume device using asm tools.

PRCT-01205: Failed to parse output {0} returned by asmcmd when executing asmcmd at location {1}

Cause: Unable to parse the specified output returned by asmcmd.

Action: Oracle internal error. Contact Oracle Support Services.

PRCT-01206: Failed to parse output {0} returned by asmcmd for node {1} when executing asmcmd at location {2}

Cause: Unable to parse the specified output returned by asmcmd on specified node.

Action: Oracle internal error. Contact Oracle Support Services.

PRCT-01207: Failed to set the ORACLE\_SID for running asmcmd from CRS home location {0}

Cause: Unable to retrieve the ASM instance name on the local node to generate the ORACLE\_SID value.

Action: Use crsctl to make sure that the CRS stack is up; use 'srvctl status asm' to make sure that the ASM resource is running on the local node.

PRCT-01300: oifcfg execution failed. Detailed error: {0}

Cause: Failed to execute the oifcfg command for the local node. See the underlying error message for further details.

Action: Try to execute the oifcfg command manually.

PRCT-01301: oifcfg execution failed on node {0}. Detailed error: {1}

Cause: Failed to execute the oifcfg command for the remote node. See the underlying error message for further details.

Action: Try to execute the oifcfg command manually.

PRCT-01302: The "{0}" has an invalid IP address format

Cause: The format of the subnet number and/or the subnet mask is an invalid IP address format.

Action: Make sure that both the subnet number and the subnet mask have a valid IP address format.

PRCT-01303: The oifcfg command returned as result the line "{0}" that has less than 4 fields

Cause: This is an internal error.

Action: Contact Oracle Support Services.

PRCT-01400: getcrshome execution failed. Detailed error: {0}

Cause: Failed to execute the getcrshome command. See the underlying error message for further details.

Action: Try to execute the getcrshome command manually.

PRCT-01401: getcrshome execution failed on node {0}. Detailed error: {1}

Cause: Failed to execute the getcrshome command. See the underlying error message for further details.

Action: Try to execute the getcrshome command manually.

PRCT-01402: Attempt to retrieve version of SRVCTL from Oracle Home {0} failed. Detailed error: {1}

Cause: Failed to execute the 'srvctl -V' command. See the underlying error message for further details.

Action: Verify that the 'bin' directory under the indicated oracle home contains the 'srvctl' binary, and verify execution of 'srvctl -V' manually on that oracle home.

PRCT-01403: Failed to parse output returned by srvctl -V when executing command at Oracle home {0}

Cause: Failed to parse the output returned by executing 'srvctl -V' because the output string is null or has unexpected result

Action: Verify execution of 'srvctl -V' manually at oracle home or Contact Oracle Support Services.

PRCT-01404: Attempt to retrieve version of SRVCTL on node {0} from Oracle Home {1} failed. Detailed error: {2}

Cause: Failed to execute the 'srvctl -V' command. See the underlying error message for further details.

Action: Verify that the 'bin' directory in specified node under the indicated oracle home contains the 'srvctl' binary, and verify execution of 'srvctl -V' manually on that oracle home.

PRCT-01405: Failed to parse output returned by srvctl -V when executing command at node {0} and Oracle home {1}

Cause: Failed to parse the output returned by executing 'srvctl -V' at specified node and because the output string is null or has unexpected result

Action: Verify execution of 'srvctl -V' manually at given node and oracle home or Contact Oracle Support Services.

PRCT-01406: Oracle Home location: {0} does not contain {1}

Cause: The current Oracle Home directory does not contain the specified utility.

Action: Provide the correct Oracle Home directory.

PRCT-01415: More than one ACFS resource was found for the mount point path {0}

Cause: When looking up the ACFS resource for a mount point, more than one resource was found.

Action: Remove all but one of the ACFS resources that contains the duplicate mount point path.