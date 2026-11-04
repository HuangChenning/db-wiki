---
title: PRKN-01031 to PRKN-01040
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/prknmsg.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 73 PRKN-01031 to PRKN-01040

PRKN-01031: Failed to retrieve local host name

Cause: An attempt to retrieve the local host name using Java network functions failed.

Action: Ensure that the 'localhost' entry exists in the hosts configuration file.

PRKN-01032: Error occured while reading input from Console

Cause: An attempt to read input from console failed

Action: Use terminal windows like xterm or Windows console to run the command.

PRKN-01033: The following nodes do not share the filesystem path "{0}" with node {1}: {2}

Cause: A subset of the nodes provided shared the given filesystem path with the local node.

Action: Mount the NFS filesystem on the node(s) that do not share the filesystem path.

PRKN-01034: Failed to retrieve IP address of host "{0}"

Cause: An attempt to retrieve IP address for the host specified failed.

Action: Run 'nslookup' on the host name and make sure the name is resolved or add the host name to OS hosts file.

PRKN-01035: Host "{0}" is unreachable

Cause: An attempt to reach the specified host via IP failed.

Action: Make sure that the host is up and there are no firewalls blocking connectivity between local node and remote host.

PRKN-01036: Windows registry key "{0}" not found on node "{1}"

Cause: Could not find the specified Windows registry key on the identified node.

Action: Contact Oracle Support Services.

PRKN-01037: Unexpected command output on node {0}: "{1}"

Cause: A remotely-executed command produced output when none was expected.

Action: Ensure that ssh or rsh is configured properly on the target node. If it is, contact Oracle Support Services for assistance.

PRKN-01038: The command "{0}" run on node "{1}" gave an unexpected output: "{2}"

Cause: A remote-shell command produced an output when none was expected.

Action: Ensure that ssh or rsh is configured properly on the specified nodes. If it is, contact Oracle Support Services for assistance.

PRKN-01039: Failed to create directory "{0}" on node "{1}"

Cause: The specified directory could not be created on the specified node.

Action: Ensure that the user is an administrator on the specified node, that the specified drive has default share configured on it, and that there is enough space in the specified location. Look at accompanying error messages and respond accordingly.

PRKN-01040: Failed to remove directory "{0}" on node "{1}"

Cause: The specified directory could not be removed on the specified node.

Action: Ensure that the user is an administrator on the specified node, that the specified drive has default share configured on it. Look at accompanying error messages and respond accordingly.