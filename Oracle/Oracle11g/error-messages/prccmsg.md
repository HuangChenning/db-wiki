---
title: PRCC-01000 to PRCC-01020
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/prccmsg.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 81 PRCC-01000 to PRCC-01020

PRCC-01000: Parameter {0} value is not valid

Cause: This is an internal error. The value for the specified parameter is null or empty string.

Action: Contact Oracle Support Services.

PRCC-01001: Failed to retrieve install group: {0}

Cause: An attempt to retrieve the install group failed.

Action: Examine the accompanying error messages for details.

PRCC-01002: Failed to update install group: {0}

Cause: An attempt to set the install group failed.

Action: Examine the accompanying error messages for details.

PRCC-01003: Version for module {0} is not available

Cause: An attempt to retrieve the version information for specified module failed.

Action: Examine the accompanying error messages for details.

PRCC-01004: Unknown identifier {0} specified for checking result of operation

Cause: Failed to retrieve the result from the exception data using the specified identifier because the exception did not have the specified identifier.

Action: This is an internal error. Contact Oracle Support Services.

PRCC-01005: Parameter {0} is not an absolute path

Cause: The specified parameter is not an absolute directory path.

Action: Provide an absolute directory path.

PRCC-01006: Path {0} is not a directory

Cause: The specified path is not a directory.

Action: Provide a directory path.

PRCC-01007: Path {0} does not exist

Cause: The specified path did not exist.

Action: Provide an existing directory path.

PRCC-01008: Enumerated type {0} does not have a member with corresponding value of {1}

Cause: This is an internal error.

Action: Contact Oracle Support Services.

PRCC-01009: Parameter {0} cannot have null as a value

Cause: This is an internal error.

Action: Contact Oracle Support Services.

PRCC-01010: {0} was already enabled

Cause: Given entity was already enabled.

Action: No action needed. To re-enable the entity, first disable it and then retry.

PRCC-01011: {0} was already enabled on {1}

Cause: Given entity was already enabled on given nodes.

Action: No action needed. To re-enable the entity on given nodes, first disable it on these nodes and then retry.

PRCC-01012: {0} was already disabled

Cause: Given entity was already disabled.

Action: No action needed. To re-disable the entity, first enable it and then retry.

PRCC-01013: {0} was already disabled on {1}

Cause: Given entity was already disabled on given nodes.

Action: No action needed.

PRCC-01014: {0} was already running

Cause: Given entity is already running.

Action: No action needed. To re-start the entity, first stop it and then retry.

PRCC-01015: {0} was already running on {1}

Cause: Given entity was already running on given nodes.

Action: No action needed. To re-start the entity on given nodes, first stop it on these nodes and then retry.

PRCC-01016: {0} was already stopped

Cause: Given entity was already stopped.

Action: No action needed. To re-stop the entity, first start it and then retry.

PRCC-01017: {0} was already stopped on {1}

Cause: Given entity was already stopped on given nodes.

Action: No action needed. To re-stop the entity on given nodes, first start it on these nodes and then retry.

PRCC-01018: A request to retrieve private network addresses for node {0} found no addresses

Cause: A request to retrieve private network addresses by executing 'olsnodes -p' returned no private IP addresses.

Action: Check 'oifcfg getif' for cluster\_interconnect networks and ensure this node has an IP address on the cluster\_interconnect networks.

PRCC-01019: Parameter "{0}" value is not valid

Cause: This is an internal error.

Action: Contact Oracle Support Services.

PRCC-01020: Version {0} cannot be used to administer resource configuration of version {1} or later

Cause: This is an internal error.

Action: Contact Oracle Support Services.