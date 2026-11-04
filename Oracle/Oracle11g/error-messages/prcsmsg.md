---
title: PRCS-01000 to PRCS-01077
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/prcsmsg.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 87 PRCS-01000 to PRCS-01077

PRCS-01000: Failed to get enabled status of {0}

Cause: An attempt to check whether a server is enabled failed.

Action: Examine the accompanying error messages for details.

PRCS-01001: Failed to enable {0}

Cause: An attempt to enable the specified server failed.

Action: Examine the accompanying error messages for details.

PRCS-01002: Failed to disable {0}

Cause: An attempt to disable the specified server failed.

Action: Examine the accompanying error messages for details.

PRCS-01005: Failed to create server {0}

Cause: An attempt to create the specified server failed.

Action: Examine the accompanying error messages for details.

PRCS-01006: Failed to get server for node {0}

Cause: An attempt to get server for the specified node failed.

Action: Examine the accompanying error messages for details.

PRCS-01007: Server pool {0} already exists

Cause: The specified server pool already exists.

Action: Examine the accompanying error messages for details.

PRCS-01008: Server pool {0} does not exist

Cause: The specified server pool does not exist.

Action: Use the srvctl command to create server pool.

PRCS-01009: Failed to create server pool {0}

Cause: An attempt to create specified server pool failed.

Action: Examine the accompanying error messages for details.

PRCS-01010: Failed to get {0} of server pool {1}

Cause: An attempt to get the attribute value of the specified server pool failed.

Action: Examine the accompanying error messages for details.

PRCS-01011: Failed to modify server pool {0}

Cause: An attempt to modify the specified server pool failed.

Action: Examine the accompanying error messages for details.

PRCS-01012: Failed to remove server pool {0}

Cause: Failed to unregister server pool. This message is followed by the reason for failure.

Action: Retry after resolving the issue reported in the failure message.

PRCS-01013: Failed to look up server pool {0}

Cause: An attempt to get the specified server pool failed.

Action: Examine the accompanying error messages for details.

PRCS-01014: Server {0} is already part of server pool {1}

Cause: An attempt to add the server as a candidate for the specified server pool failed because the server is already in the pool's SERVER\_NAME attribute.

Action: No action is needed.

PRCS-01015: Server {0} is not part of server pool {1}

Cause: An attempt to remove the server from the SERVER\_NAMES attribute of the server pool failed because the specified server is not in the pool's SERVER\_NAME attribute.

Action: Add the server to the server pool.

PRCS-01016: Failed to resolve Single Client Access Name {0}

Cause: An attempt to resolve specified Single Client Access Name to a list of IP addresses failed because Single Client Access Name could not be resolved in DNS using nslookup or using other lookup methods.

Action: Check whether the specified Single Client Access Name is correct. Review the underlying error messages that provide the details of which resource failed to resolve. Check the cause and action for the individual error. If Single Client Access Name should be resolved in DNS, check the configuration of Single Client Access Name in DNS.

PRCS-01017: Failed to configure Single Client Access Name {0}

Cause: An attempt to add cluster configuration for Single Client Access Name failed.

Action: Review the underlying error messages that provide the details of which resources failed to create. Check the cause and action for the individual resource creation failure.

PRCS-01018: Failed to add cluster configuration for Single Client Access Name listener {0}

Cause: An attempt to configure Single Client Access Name listener failed because endpoints were not specified correctly or other reasons.

Action: Review the underlying error messages that provide the details of which resources failed to create. Check the cause and action for the individual resource creation failure. If the endpoints were not specified correctly, correct endpoints.

PRCS-01019: Failed to remove the configuration for Single Client Access Name listener {0}

Cause: An attempt to remove the configuration of Single Client Access Name listener failed because other resources depended on it or other reasons.

Action: Review the underlying error messages that provide the details of which resources failed to remove. Stop Single Client Access Name listener resource before removing it. Can consider using force flag to remove Single Client Access Name listener resources if no other resources depend on it.

PRCS-01020: Failed to enable Single Client Access Name resources {0}

Cause: An attempt to enable Single Client Access Name resources failed.

Action: Review the underlying error messages that provide the details of which resources failed to enable. Check the cause and action for the individual resource creation failure.

PRCS-01021: Failed to disable Single Client Access Name resources {0}

Cause: An attempt to disable Single Client Access Name resources failed because current user did not have sufficient privileges to perform this operation or other reasons.

Action: Review the underlying error messages that provide the details of which resources failed to disable. Check the cause and action for the individual resource failure. Make sure that the user has root privileges on Linux/Unix's and Administrator on Windows.

PRCS-01022: Failed to start Single Client Access Name resources {0}

Cause: An attempt to start Single Client Access Name resources failed.

Action: Review the underlying error messages that provides the details of which resources failed to start.

PRCS-01023: Failed to stop Single Client Access Name resources {0}

Cause: An attempt to stop Single Client Access Name resources failed because Single Client Access Name listeners were not stopped/relocated or other reasons.

Action: Review the underlying error messages that provides the details of which resources failed to stop. Check the cause and action for the individual resource creation failure. Stop Single Client Access Name listeners first or use force flag to stop Single Client Access Name Virtual Internet Protocol(VIP) resources if no other resources depend on them.

PRCS-01024: Failed to remove Single Client Access Name Virtual Internet Protocol(VIP) resources {0}

Cause: Could not remove Single Client Access Name Virtual Internet Protocol(VIP) resources because the resources are running or Single Client Access Name listeners depend on or other reasons.

Action: Review the underlying error messages that provides the details of which resources failed to remove. Stop the Single Client Access Name VIPs and Single Client Access Name listeners, then remove Single Client Access Name listeners. Or use force flag to remove Single Client Access Name Virtual Internet Protocol(VIP) resources if no other resources depend on them.

PRCS-01025: Could not find Single Client Access Name Virtual Internet Protocol(VIP) resources {0}

Cause: Could not find Single Client Access Name Virtual Internet Protocol(VIP) resources.

Action: Check the resource name and check the underlying error messages that provides the details of which resources failed to be found.

PRCS-01026: Could not find Single Client Access Name listener resources {0}

Cause: An attempt to find Single Client Access Name listener resources failed.

Action: Check the resource name. Review the underlying error messages that provides the details of which resources failed to be found.

PRCS-01027: Could not find any Single Client Access Name listener with ordinal number {0}

Cause: Could not find the Single Client Access Name listener for specified ordinal number.

Action: Use 'srvctl config scan\_listener' to check available ordinal number.

PRCS-01028: Single Client Access Name listeners already exist

Cause: Single Client Access Name listeners were already created.

Action: Use 'srvctl modify scan\_listener' to modify attributes if needed.

PRCS-01031: Failed to modify Single Client Access Name listeners using endpoints {0}

Cause: An attempt to modify Single Client Access Name listeners failed.

Action: Check if the endpoints specified are valid.

PRCS-01032: No server pool was found that matches the query {0}

Cause: An attempt to find server pools that match the given query found no matching server pool.

Action: Either configure a server pool via 'srvctl add srvpool' command or modify existing a server pool via 'srvctl modify srvpool' command to match the query and retry the request.

PRCS-01034: Failed to modify Single Client Access Name {0}

Cause: Failed to modify the configuration of Single Client Access Name because the endpoints were not specified correctly or extra Single Client Access Name VIPs could not be removed or other reasons.

Action: Review the underlying error messages that provides the details of which resources failed to modify. Resolve the reported problem and retry. If to modify the endpoints, specify correct endpoints. If to update the number of Single Client Access Name VIPs, stop the Single Client Access Name listeners that depend on.

PRCS-01035: Invalid number of TCP ports ({0}) for SCAN Listener

Cause: Either no port was specified, or more than one port was specified.

Action: Specify only one port number for TCP protocol for SCAN Listener.

PRCS-01037: Single Client Access Name VIPs already exist

Cause: An attempt was made to add SCAN VIPs when SCAN VIPs are already configured. Only one SCAN per cluster can be configured.

Action: Remove existing SCAN and add new SCAN. Or modify scan to use new SCAN name or have the existing SCAN name to map to different SCAN VIPs.

PRCS-01038: Failed to find Single Client Access Name Virtual Internet Protocol(VIP) associated with listener {0}

Cause: Cannot find Single Client Access Name Virtual Internet Protocol(VIP) associated with the given listener.

Action: Examine the accompanying error messages to determine how to respond.

PRCS-01039: Failed to find Single Client Access Name listener associated with the given Virtual Internet Protocol(VIP) {0}

Cause: Cannot find Single Client Access Name listener associated with the given Virtual Internet Protocol(VIP).

Action: Examine the accompanying error messages to determine how to respond.

PRCS-01040: User {0} does not have CRS administrator role

Cause: Specified user did not have CRS administrator role.

Action: Grant CRS administator role to the user by using 'crsctl add crs administrator -u <user\_name>' command and retry.

PRCS-01041: Invalid builtin server pool name {0}

Cause: The specified builtin server pool name is invalid.

Action: Provide a valid builtin server pool name. It can be Generic or Free.

PRCS-01042: Server pool {0} is not hosting any database currently

Cause: No database could be found referencing the given server pool.

Action: Create database configuration using 'srvctl add database... -g <server\_pool>' command and retry.

PRCS-01043: Server pool {0} is not hosting any database service currently

Cause: No service could be found referencing the given server pool.

Action: Create service configuration using 'srvctl add service... -g <server\_pool>' command and retry.

PRCS-01046: Name {0} is not valid

Cause: Specified name was not valid.

Action: Specify a valid string name, and retry.

PRCS-01047: Minimum size of {0} is not valid

Cause: Specified minimum size was not valid.

Action: Specify minimum size to be an integer equal to or greater than zero and less than the maximum size (other than -1), and retry.

PRCS-01048: Maximum size of {0} is not valid

Cause: Specified maximum size was not valid.

Action: Specify maximum size to be an integer greater than or equal to -1 and retry.

PRCS-01049: Importance of {0} is not valid

Cause: Specified importance was not valid.

Action: Specify importance value to be an integer greater than or equal to 0 and retry.

PRCS-01050: Could not add GNS VIP {0} because another one with name {1} already exists

Cause: The name of the GNS VIP to be added matches one that already existed.

Action: Specify another name.

PRCS-01051: Could not add GNS VIP using network {0} because registered another one using network {1} already exists

Cause: The network specified for the GNS VIP to be added matches one that already existed.

Action: Specify another network.

PRCS-01053: failed to resolve address for Grid Naming Service VIP {0}: {1}

Cause: The address specified for the GNS VIP could not be resolved.

Action: Specify a valid address.

PRCS-01054: Failed to configure VIP for Grid Naming Service VIP {0}

Cause: The creation of the GNS VIP failed.

Action: Examine the accompanying error message for details.

PRCS-01055: Failed to modify Grid Naming Service VIP {0}

Cause: The modification of the GNS VIP failed.

Action: Examine the accompanying error message for details.

PRCS-01056: Could not find resources for Grid Naming Service Virtual Internet Protocol(VIP) {0}

Cause: The specified GNS VIP did not exist.

Action: Specify a valid GNS VIP name.

PRCS-01057: INTERNAL ERROR: no attributes specified.

Cause: No attributes to modify GNS with were passed to a method.

Action: This is an internal error. Please contact Oracle Customer Support.

PRCS-01058: INTERNAL ERROR: unsupported query type: "${0}"

Cause: The type of query to be made to GNS is unrecognized.

Action: This is an internal error and should not be visible. Please contact Oracle Customer Support.

PRCS-01059: Failed to get sub-server pools of server pool {0}

Cause: Failed to look up PARENT\_POOLS attribute of server pools containing the given server pool name. Ensure that current user has read permissions on the given server pool and its sub-server pools.

Action: Grant read permissions on the given server pool and its sub-server pools.

PRCS-01060: Failed to relocate servers {0} into server pool {1}

Cause: Failed to relocate servers into the given server pool. This message may be accompanied by others providing additional details. A likely cause is violation of defined configuration attributes such as pool MIN\_SIZE, SERVER\_NAMES etc.

Action: If the problem stems from violating configuration attributes, either modify the attributes or reformulate the request. Otherwise, contact Oracle Support Services.

PRCS-01061: Failed to find running database instances hosted by server pool {0}

Cause: Failed to find running database instances hosted by the servers in the given server pool. This message is accompanied by others providing additional details. A likely cause is that current user may not have permissions to query profiles of databases hosted by the given server pool.

Action: If lack of permissions is the cause of this failure, then use 'srvctl config \<object> -a' command to find the current owner of entity and retry the query as that owner user. Otherwise, contact Oracle Support Services.

PRCS-01062: Failed to determine whether server pool {0} has any parents or children

Cause: Failed to find parents or children of the given server pool. A likely cause is that current user may not have permissions to query profile of given server pool or profiles of other server pools whose PARENT\_POOLS attribute contains this server pool name.

Action: If lack of permissions is the cause of this failure, then use 'srvctl config serverpool \<serverpool> -a' command to find the current owner of the server pool and retry the query as that owner user. Otherwise, contact Oracle Support Services.

PRCS-01063: Server pool {0} with minimum size {1}, maximum size {2}, importance {3} and server list ({4}) can not be created

Cause: Specified server pool cannot be created because of the reason provided by an accompanying exception message.

Action: Respond based on the accompanying exception message.

PRCS-01064: Server {0} is not assigned to any server pool

Cause: Given server is not yet recognized by Oracle Clusterware and therefore is not active in any server pool.

Action: Check state of the server using 'crsctl stat server \<server> -f' and contact Oracle Support Services.

PRCS-01065: GNS is not configured.

Cause: GNS has not been configured on the cluster.

Action: Configure GNS by executing "srvctl add gns".

PRCS-01066: Server group {0} with server list ({1}) can not be created

Cause: Specified server group cannot be created because of the reason provided by an accompanying exception message.

Action: Respond based on the accompanying exception message.

PRCS-01067: Failed to find online database instances hosted by server pool {0}

Cause: Failed to find online database instances hosted by the servers in the given server pool. This message is accompanied by others providing additional details. A likely cause is that current user may not have permissions to query profiles of databases hosted by the given server pool.

Action: If lack of permissions is the cause of this failure, then use 'srvctl config \<object> -a' command to find the current owner of the entity and retry the query as that owner user. Otherwise, contact Oracle Support Services.

PRCS-01068: Oracle Clusterware server entity for node {0} does not exist

Cause: The server entity for the specified node does not exist.

Action: Start Oracle Clusterware on the given node and retry.

PRCS-01069: Label {0} in GNS domain name {1} does not follow RFC-1035 convention

Cause: The specified portion of the GNS domain name does not follow RFC-1035 label conventions.

Action: Specify a domain name that follows RFC-1035 conventions. According to RFC-1035 conventions, the domain name consists of a set of labels separated by ".". A label must begin with an alphabetic character and can contain only alphanumerics and "-" (dash or minus character), end with an alphanumeric, and be no more than 63 characters long.

PRCS-01070: Label {0} part of GNS domain name {1} is too long

Cause: The specified portion of the GNS domain name does not follow RFC-1035 label conventions, as it is longer than 63 characters.

Action: Specify a domain name that follows RFC-1035 conventions. The domain name consists of a set of labels separated by ".". Label must begin with an alphabetic character and can contain only alphanumeric characters and "-" (dash or minus character), end with an alphanumeric and be no more than 63 characters long.

PRCS-01071: An error occurred while trying to look up IP address for domain name {0}

Cause: An error occurred while trying to translate the indicated fully domain qualified name (FDQN) to IP addresses.

Action: Make sure that name servers on local node are correctly configured. If the domain in the FDQN is GNS domain make sure that DNS has been set up to forward request to GNS and GNS resource is online. Make sure that there are no firewalls between the local node and the name servers.

PRCS-01072: Failed to create server pool with reserved name {0}

Cause: Request to create the specified server pool was rejected because specified server pool name is the name of builtin server pool of Oracle Clusterware.

Action: Supply a server pool name other than the builtin server pool name (Generic or Free) of Oracle Clusterware and retry.

PRCS-01073: The specified GNS logging level {0} was outside the expected range of {1} to {2}

Cause: The log\_level value in the 'srvctl start gns -l <log\_level>' command was less than the minimum limit.

Action: Ensure that the log\_level value is within the valid range.

PRCS-01074: The specified GNS logging level {0} was outside the expected range of {1} to {2}

Cause: The log\_level value in the 'srvctl start gns -l <log\_level>' command was greater than the maximum limit.

Action: Ensure that the log\_level value is within the valid range.

PRCS-01075: GNS Domain name {0} ends with invalid character {1}

Cause: The specified GNS domain name ends with an invalid character and does not follow RFC-1035 label conventions.

Action: Specify a domain name that follows RFC-1035 conventions. According to RFC-1035 conventions, the domain name consists of a set of labels separated by ".". A label must begin with an alphabetic character and can contain only alphanumeric characters or "-" (dash or minus character), end with an alphanumeric, and be no more than 63 characters long.

PRCS-01076: Invalid Single Client Access Name {0}. The subnet {1} of SCAN VIP {2} differs from the subnet {3} of network {4}

Cause: The SCAN VIPs resolved from the specified Single Client Access Name are in a subnet that differs from the network's subnet.

Action: Use the SCAN name that can be resolved to the SCAN VIPs in the same subnet of network resource.

PRCS-01077: The specified trace level {0} was outside the expected range of {1} to {2}

Cause: The trace level value was less than the minimum limit or greater than the maximum limit.

Action: Ensure that the trace level value is within the valid range.