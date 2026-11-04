---
title: PRCN-02018 to PRCN-03018
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/prcnmsg.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 85 PRCN-02018 to PRCN-03018

PRCN-02018: Current user {0} is not a privileged user

Cause: Current user did not have sufficient privileges to perform this operation.

Action: Make sure that the user has root privileges on Linux/Unix's and Administrator on Windows.

PRCN-02030: Subnet does not exist for resource {0}

Cause: An attempt was made to query subnet for a network resource configured with Oracle clusterware and it was not found.

Action: Internal error. Contact Oracle Support.

PRCN-02031: Unknown DHCP server name {0} found for resource {1}

Cause: The DHCP server type obtained for the network resource is not a valid server type.

Action: Internal error. Contact Oracle Support.

PRCN-02032: Failed to retrieve DHCP server type {0}

Cause: An attempt to query the DHCP server type for the network resource failed because its value could not be retrieved from the Oracle clusterware resource attributes.

Action: make sure Oracle clusterware is up and running. and also look at the help for the accompanying CRS error message.

PRCN-02033: Failed to update DHCP server type to {0} {1}

Cause: An attempt to update the DHCP server type for the network resource failed because its value could not be updated in the Oracle Clusterware resource attribute.

Action: Make sure that the Clusterware stack is up. Make sure that the user has enough permission to modify node applications. Examine the accompanying message for additional details.

PRCN-02034: Could not find dependent resource {0} for resource {1}: {2}

Cause: Could not get the resource associated with a given resource. Could not get the ASM resource associated with a given ASM disk group resource.

Action: Make sure that clusterware stack is up. Make sure that the network resource associated with this resource has not been removed. Make sure that the user has permission to perform this operation.

PRCN-02035: Port {0} is not available on node(s) or virtual host(s): {1}

Cause: The port specified is already being used by some other applications on the nodes or virtual hosts given.

Action: Stop the applications that are using these ports or specify a different port and try the command again.

PRCN-02036: Failed to retrieve port number(s) for {0}

Cause: An attempt to retrieve the port number(s) for the cluster resource failed.

Action: Make sure that the clusterware stack is up. Make sure that the resource you are querying has been configured. Also take a look at the help for the accompanying error message(s).

PRCN-02037: Failed to retrieve Oracle home for {0}

Cause: An attempt to retrieve Oracle home value for the listener resource failed.

Action: Make sure that the clusterware stack is up. Make sure that listener is configured. If node name is being specified in the command line make sure that the node name is a valid node name. Also look at help for the accompanying error message(s).

PRCN-02038: Failed to update Oracle home {0} for listener {1}

Cause: An attempt to update the Oracle home value for the listener resource failed.

Action: Make sure that the clusterware stack is up. Make sure that the listener is configured. If node name is being specified in the command line make sure that the node name is a valid node name. Make sure that user is a owner or has write permissions to modify the listener resource. Also look at the help for other errors listed in error stack.

PRCN-02039: Failed to retrieve Oracle home for {0} on node {1}

Cause: An attempt to retrieve Oracle home value for the listener resource on a the specified node failed.

Action: Make sure that the clusterware stack is up. Make sure that the listener is configured on the node. Make sure that the node name being passed in the command line is a valid node name. Also look at the help for the accompanying error message(s).

PRCN-02040: Failed to update Oracle home {0} for {1} on node {2}

Cause: Attempt to update value of attribute Oracle home for listener resource on the specified node failed.

Action: Make sure that the clusterware stack is up. Make sure that the listener is configured on the node. Make sure that the user has enough permission to modify the listener. Make sure that the node name being passed in the command line is a valid node name. Also look at the help for other errors listed in error stack.

PRCN-02041: Failed to retrieve properties of {0}

Cause: Failed to retrieve properties of the given entity.

Action: Make sure that user has permission to read resource attribute.

PRCN-02042: Failed to set properties {0} of {1}

Cause: Failed to update properties of the given entity.

Action: Make sure that user has permission to update resource attribute.

PRCN-02043: Multiple network resources {0} exist on the cluster

Cause: More than one network resource has been configured and the one to be used for creating this resource has not been specified.

Action: Use command line option -k <net\_num> argument to specify the network to be used and retry the command again.

PRCN-02044: No listener exists

Cause: No listener has been configured.

Action: Use netca or srvctl to add/configure a listener.

PRCN-02045: No network exists

Cause: No network has been configured.

Action: Use 'srvctl add nodeapps' to add/configure network resource.

PRCN-02046: Netmask does not exist for resource {0}

Cause: An attempt to retrieve the subnet information for the network resource resulted in not finding subnet mask.

Action: Internal error. Contact Oracle Support.

PRCN-02047: VIP {0} exists

Cause: The VIP with specified name has been registered in CRS.

Action: Remove the existing VIP before registering it again.

PRCN-02048: The network number {0} is already registered for subnet ''{3}'' and adapters ''{4}''. Can not add network number {0} for the specified subnet ''{1}'' and adapters ''{2}''.

Cause: The network number is taken by a registered network resource.

Action: Use a different network number to add a new network resource with the specified subnet and adapters, or modify existing network using 'srvctl modify nodeapps'.

PRCN-02049: The network attributes specified (network number: {0}, subnet: {1}, adapters: {2}) conflict with an already registered network (network number: {3}, subnet: {4}, adapters: {5})

Cause: The network resource is registered with different network number

Action: Use the registered network resource with the registered network number or provide different subnet or adapters.

PRCN-02050: The requested VIP (nodename: {0}, VIP name: {1}, network number: {2}) has the same VIP name but different network number or preferred node than the registered VIP (nodename: {3}, VIP name: {4}, network number: {5}).

Cause: One VIP name (and IP address) can only be used by one VIP with the same network number on the same node.

Action: Use a different VIP name or IP address.

PRCN-02051: The requested VIP (nodename: {0}, VIP name: {1}, network number: {2}) has the same network number and the same preferred node but different VIP name with the registered VIP (nodename: {3}, VIP name: {4}, network number: {5}).

Cause: One network resource on one preferred node can have only one cluster VIP.

Action: Use different network number or preferred node to register different VIP.

PRCN-02052: Failed to modify Network resource (network number: {0}) to use (subnet: {1}, netmask {2} adapters: {3}).

Cause: CRS was unable to modify the network resource to use new subnet/netmask/interface

Action: Make sure that clusterware stack is up. Make sure that the subnet, netmask and adapters value are correct. Make sure that the interface being referred to is running. Make sure that the user who is trying to modify network resource has root privileges. Examine the accompanying message for additional details.

PRCN-02053: Failed to modify ONS listening port for local client connections to {0}

Cause: CRS unable to modify the ONS listening port for local connections

Action: Make sure that clusterware stack is up. If the port is in use by another application, try using a different port.

PRCN-02054: Failed to modify ONS listening port for remote client connections to {0}

Cause: CRS unable to modify the ONS listening port for remote client connections

Action: Make sure that clusterware stack is up. If the port is in use by another application, try using a different port.

PRCN-02055: Failed to update port number(s) to {0} for {1}

Cause: An attempt to update the listener port failed for the nodes of the cluster.

Action: The port could be in use. Try using different port. If node name was specified in the command line make sure that the node name is a valid node name. Also look at the help for the accompanying error message(s).

PRCN-02056: Invalid listener protocol type {0}

Cause: The specified listener protocol type is invalid.

Action: Provide a valid listener protocol type. It can be TCP, TCPS, IPC, NMP, or SDP.

PRCN-02057: Invalid listener protocol value {0}

Cause: The specified listener protocol value is invalid.

Action: Provide a valid listener protocol value. It cannot contain special characters ':,/'

PRCN-02058: Invalid listener protocol ENDPOINTS {0}. Delimiter is "{1}", invalid part is "{2}".

Cause: The specified listener ENDPOINTS are invalid.

Action: Provide valid listener protocol ENDPOINTS. It cannot contain invalid part.

PRCN-02059: Invalid listener port number {0}

Cause: The specified listener port number is invalid.

Action: Provide a valid listener port number.

PRCN-02060: Duplicated listener protocol value {0}

Cause: The specified listener protocol value is a duplication of another one.

Action: Remove duplicated listener protocol value.

PRCN-02061: Failed to add listener {0}

Cause: An attempt to add listener failed because endpoints were not specified correctly or other reasons.

Action: Review the underlying error messages that provide the details of which resources failed to create. Check the cause and action for the individual resource creation failure. If the endpoints were not specified correctly, correct endpoints.

PRCN-02062: The specified hostname or address {0} cannot be resolved.

Cause: An invalid IP address or unresolvable hostname was specified.

Action: If IP address is specified then make sure that it is of legal length. If a host name is specified than make sure that the host name resolves to an IP address.

PRCN-02063: Failed to modify OC4J listening port to {0}

Cause: CRS unable to modify the OC4J instances listening port.

Action: Make sure that clusterware stack is up. If the port is in use by another application, try using a different port.

PRCN-02064: Found {0} VIPs for {1}

Cause: A conflict was found in VIP resource definition: either more than one VIP is using the same name or address, or a VIP is using the same name or address as a real host.

Action: Ensure that each VIP is defined with a distinct name and address relative to other VIPs and hosts in the network.

PRCN-02065: Port(s) {0} are not available on the nodes given

Cause: The ports specified are already being used by some other applications on the nodes given.

Action: Stop the applications that are using these ports or specify different ports and try the command again.

PRCN-02066: Failed to retrieve cluster listener for {0} because it has the type of Single Client Access Name Listener

Cause: Failed to use cluster listener APIs or srvctl commands for specified listener.

Action: Use Single Client Access Name Listener (SCAN listener) APIs or srvctl commands (srvctl \<verb> scan\_listener) for specified listener name.

PRCN-02067: Port {0} is not available across node(s) "{1}"

Cause: The port specified is already being used by some other applications across the nodes given.

Action: Stop the application that is using this port or specify a different port and try the command again.

PRCN-02068: Failed to check the port availability

Cause: This is an internal error.

Action: Contact Oracle Support Services.

PRCN-02069: Unable to retrieve the list of nodes

Cause: This is an internal error.

Action: Contact Oracle Support Services.

PRCN-02070: Failed to validate network. No interface on {0} matches required network (subnet: {1}, netmask: {2} adapters: {3}).

Cause: The nodes don't have the configuration for the required network.

Action: Specify a subnet that exists on all nodes, or reconfigure the nodes to ensure that the specified subnet exists on all nodes.

PRCN-02071: Failed to update attribute USE\_EVM to {0}

Cause: An attempt to update the attribute value of USE\_EVM for ONS failed.

Action: Examine the accompanying error message(s) and respond accordingly.

PRCN-02072: Failed to get multicast port for events from EONS

Cause: An attempt to get multicast port for events from EONS failed.

Action: Examine the accompanying error message(s) and respond accordingly.

PRCN-02073: Failed to remove EONS

Cause: An attempt to remove EONS failed.

Action: Examine the accompanying error message(s) and respond accordingly.

PRCN-02074: Specified check interval of {0} minutes is below the minimum check interval {1} minutes

Cause: The CVU resource check interval specified was less than the minimum check interval.

Action: Retry the operation with a interval greater than or equal to the minimum check interval.

PRCN-02075: Failed to modify the CVU CHECK\_INTERVAL attribute to {0}

Cause: CRS was unable to modify the CVU CHECK\_INTERVAL attribute.

Action: Make sure that Clusterware stack is up. Make sure that user is an owner or has write permissions to modify the CVU resource. Check for and respond to any accompanying error messages.

PRCN-02076: Failed to retrieve the CVU CHECK\_INTERVAL attribute for "{0}"

Cause: An attempt to retrieve the CHECK\_INTERVAL for the CVU cluster resource failed.

Action: Make sure that the Clusterware stack is up. Make sure that the CVU resource has been configured. Check for and respond to any accompanying error messages.

PRCN-02077: Failed to modify the CVU CHECK\_RESULTS attribute to "{0}"

Cause: CRS was unable to modify the CVU CHECK\_RESULTS attribute.

Action: Make sure that Clusterware stack is up. Make sure that the CVU resource has been configured. Check for and respond to any accompanying error messages.

PRCN-02078: Failed to retrieve the CVU CHECK\_RESULTS for "{0}"

Cause: An attempt to retrieve the CHECK\_RESULTS atribute for the CVU cluster resource failed.

Action: Make sure that the Clusterware stack is up. Make sure that the CVU resource has been configured. Check for and respond to any accompanying error messages.

PRCN-02079: Port {0} is out of the valid range, between 1 and 65535 and cannot be used on any of the nodes given

Cause: The port number that was provided was either less than 1 or greater than 65535.

Action: Make sure the port provided has a value between 1 and 65535.

PRCN-03000: The IPMI configuration failed on all nodes

Cause: The node names were invalid or were valid but had no IPMI device present.

Action: Make sure that all nodes are reachable and the IPMI device exists on those nodes.

PRCN-03001: The IPMI configuration failed on one or more nodes

Cause: There was at least one node with invalid name or with no IPMI device.

Action: Make sure that all nodes are reachable and the IPMI device exists on those nodes.

PRCN-03002: There is no network resource configured for the cluster

Cause: A request to add a listener was rejected due to the lack of a network resource.

Action: Use command 'srvctl add network' to configure the network first, then retry the command.

PRCN-03003: Failed to unregister EONS resource type

Cause: A request to unregister the EONS resource type failed because of the reason provided by an accompanying exception message.

Action: Examine the accompanying error message for details.

PRCN-03004: Listener {0} already exists

Cause: The specified listener was already created.

Action: Use 'srvctl modify listener' to modify attributes if needed.

PRCN-03005: Failed to add or use registered network {0} with network interfaces ''{1}'' because the network was already registered for network interfaces ''{2}''

Cause: The network resource was already registered with different interfaces.

Action: Use the same network interfaces as the one registered with network resource.

PRCN-03006: Failed to add or use registered network {0} with network interfaces ''{1}'' because the network was already registered with no interface specified

Cause: The network resource was already registered with no user specified interface.

Action: Do not specify network interface as the system decides the network interface.

PRCN-03007: Failed to add or use registered network {0} with network mask ''{1}'' because the network was already registered for network mask ''{2}''

Cause: The network resource was already registered with a different network mask.

Action: Use the same network mask as the one registered with network resource.

PRCN-03008: Failed to add or use registered network {0} with network subnet ''{1}'' because the network was already registered for network subnet ''{2}''

Cause: The network resource was already registered with a different network subnet.

Action: Use the same network subnet as the one registered with network resource.

PRCN-03009: Failed to retrieve log file attribute for {0} resource

Cause: An attempt to retrieve the log file attribute for the cluster resource failed.

Action: Make sure that the clusterware stack is up. Make sure that the resource you are querying has been configured. Refer also to any accompanying error messages for details.

PRCN-03010: Failed to retrieve log component attribute for {0} resource

Cause: An attempt to retrieve the log component attribute for the cluster resource failed.

Action: Make sure that the clusterware stack is up. Make sure that the resource you are querying has been configured. Refer also to any accompanying error messages for details.

PRCN-03011: Failed to retrieve debug file attribute for {0} resource

Cause: An attempt to retrieve the debug file attribute for the cluster resource failed.

Action: Make sure that the clusterware stack is up. Make sure that the resource you are querying has been configured. Refer also to any accompanying error messages for details.

PRCN-03012: Failed to retrieve debug component attribute for {0} resource

Cause: An attempt to retrieve the debug component attribute for the cluster resource failed.

Action: Make sure that the clusterware stack is up. Make sure that the resource you are querying has been configured. Refer also to any accompanying error messages for details.

PRCN-03013: Failed to update log file attribute of {0} resource

Cause: An attempt to update the attribute value of LOG\_FILE for ONS failed.

Action: Examine the accompanying error message(s) and respond accordingly.

PRCN-03014: Failed to update log component attribute of {0} resource

Cause: An attempt to update the attribute value of LOG\_COMP for ONS failed.

Action: Examine the accompanying error message(s) and respond accordingly.

PRCN-03015: Failed to update debug file attribute of {0} resource

Cause: An attempt to update the attribute value of DEBUG\_FILE for ONS failed.

Action: Examine the accompanying error message(s) and respond accordingly.

PRCN-03016: Failed to update debug component attribute of {0} resource

Cause: An attempt to update the attribute value of DEBUG\_COMP for ONS failed.

Action: Examine the accompanying error message(s) and respond accordingly.

PRCN-03017: Specified check interval of {0} minutes exceeds the maximum check interval {1} minutes

Cause: The CVU resource check interval specified was more than the maximum check interval.

Action: Retry the operation with an interval smaller than or equal to the maximum check interval.

PRCN-03018: Addition of listener version {0} is not allowed using srvctl version {1}

Cause: The versions of srvctl used and listener to be created did not match.

Action: Use the same version of srvctl as listener.