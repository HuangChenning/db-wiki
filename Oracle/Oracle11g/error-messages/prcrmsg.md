---
title: PRCR-01000 to PRCR-01135
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/prcrmsg.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 86 PRCR-01000 to PRCR-01135

PRCR-01000: Resource {0} already exists

Cause: An attempt was made to create a resource that already exists.

Action: Check the resource using 'srvctl config \<object>' command and if the resource should not exist then remove it using 'srvctl remove \<object>' command.

PRCR-01001: Resource {0} does not exist

Cause: An attempt was made to operate on a resource that does not exist.

Action: Check the resource using 'srvctl config \<object>' command and if the resource does not exist then create it using 'srvcl add \<object>' command.

PRCR-01002: Resource {0} is already enabled

Cause: An attempt was made to enable a resource that is already enabled.

Action: If the resource is already enabled then no action is needed. Use 'srvctl status \<object>' command to determine whether it is enabled.

PRCR-01003: Resource {0} is already disabled

Cause: An attempt was made to disable a resource that is already disabled.

Action: If the resource is already disabled then no action is needed. Use 'srvctl status \<object>' command to determine whether it is disabled.

PRCR-01004: Resource {0} is already running

Cause: An attempt was made to start a resource that is already running.

Action: If the resource is already running then no action is needed. Use 'srvctl status \<object>' command to determine whether it is running.

PRCR-01005: Resource {0} is already stopped

Cause: An attempt was made to stop a resource that is already stopped.

Action: If the resource is already stopped then no action is needed. Use 'srvctl status \<object>' command to determine whether it is stopped.

PRCR-01006: Failed to add resource {0} for {1}

Cause: An attempt to add the specified resource has failed.

Action: Check and resolve the underlying exception.

PRCR-01007: Failed to check status of resource {0}

Cause: An attempt to check status of specified resource has failed.

Action: Check the help for the underlying exception.

PRCR-01008: Failed to retrieve version of resource {0}

Cause: An attempt to retrieve version of the specified resource has failed.

Action: Check the help for the underlying exception.

PRCR-01009: Failed to retrieve permissions of resource {0}, ACL {1}

Cause: Internal error.

Action: Contact Oracle Support Services.

PRCR-01010: Failed to update permissions of resource {0}

Cause: An attempt to update permissions of specified resource has failed.

Action: Check the help for the underlying exception.

PRCR-01011: Failed to enable resource {0}

Cause: An attempt to enable specified resource has failed.

Action: Check the help for the underlying exception.

PRCR-01012: Failed to disable resource {0}

Cause: An attempt to disable specified resource has failed.

Action: Check the help for the underlying exception.

PRCR-01013: Failed to start resource {0}

Cause: An attempt to start specified resource on several nodes failed.

Action: Check the help for the underlying exception.

PRCR-01014: Failed to stop resource {0}

Cause: An attempt to stop specified resource on several nodes failed.

Action: Check the help for the underlying exception.

PRCR-01015: Failed to relocate resource {0}

Cause: An attempt to relocate specified resource has failed.

Action: Check the help for the underlying exception.

PRCR-01016: Failed to modify resource {0}

Cause: An attempt to modify specified resource has failed.

Action: Check the help for the underlying exception.

PRCR-01024: Failed to remove resource {0} on nodes {1}

Cause: An attempt to remove the resource on the specified nodes failed.

Action: Check the accompanying error messages for details.

PRCR-01025: Resource {0} is still running

Cause: The specified resource is not stopped.

Action: Check the accompanying error messages to decide whether to stop the specified resource.

PRCR-01026: Resource {0} is not running

Cause: The specified resource is not started.

Action: Check the accompanying error messages to decide whether to start the specified resource.

PRCR-01028: Failed to remove resource {0}

Cause: An attempt to remove specified resource failed.

Action: Check the help for the underlying CRSException.

PRCR-01029: Attribute {0} does not exist in resource {1} definition

Cause: An attempt was made to get an attribute which is not defined for that resource type.

Action: Make sure that the attribute exists in the resource definition.

PRCR-01030: Resource attribute name {0} is not valid

Cause: Internal error.

Action: Contact Oracle Support Services.

PRCR-01031: Resource attribute {0} value {1} is not valid

Cause: Specified resource attribute value is not valid.

Action: Try recreating the resource attribute value using srvm APIs or recreating the resource using srvctl commands.

PRCR-01032: Current state of resource {0} is not valid

Cause: Internal error.

Action: Contact Oracle Support Services.

PRCR-01033: Resource type {0} does not exist

Cause: An attempt to retrieve the type has failed.

Action: Make sure that the type exists.

PRCR-01035: Failed to look up CRS resource {0} for {1}

Cause: An attempt to access the specified resource failed because it did not exist.

Action: Check that the specified name and resource type are correct.

PRCR-01036: Failed to retrieve cardinality of the resource {0}

Cause: An attempt to retrieve cardinality of resource has failed.

Action: Examine the accompanying error messages to determine how to respond.

PRCR-01037: Failed to update cardinality of the resource {0} to {1}

Cause: An attempt to set cardinality of the resource has failed.

Action: Examine the accompanying error messages to determine how to respond.

PRCR-01039: Server pool {0} does not exist

Cause: An attempt was made to retrieve the server pool which does not exists.

Action: Make sure that requested server pool exists.

PRCR-01040: Resource {0} is already enabled on node(s) {1}

Cause: An attempt was made to enable a resource that is already enable on nodes.

Action: The status of a resource can be checked by using the 'srvctl status \<object>' command.

PRCR-01041: Resource {0} is already disabled on node(s) {1}

Cause: An attempt was made to disable a resource that is already disabled on nodes.

Action: The status of a resource can be checked by using the 'srvctl status \<object>' command.

PRCR-01042: Failed to get dependent resources {0} of resource {1}: {2}

Cause: Failed to retrieve dependent resources of the given resource.

Action: Examine the accompanying error messages to determine how to respond.

PRCR-01043: Failed to update dependent resources {0} of resource {1} to resource {2}

Cause: Failed to update dependent resources of the given resource.

Action: Examine the accompanying error messages to determine how to respond.

PRCR-01050: Resource {0} is not configured in Oracle cluster environment

Cause: The environment for the specified resource is not Oracle Clusterware.

Action: The specified commands or APIs can only be used when Oracle Clusterware is running. If the environment is configured as Oracle Restart, use the correspond commands and APIs for Oracle Restart.

PRCR-01051: OracleCM Cluster is not found on node {0}

Cause: The OracleCM Cluster was not found on the specified node because the library for OracleCM Cluster was not found.

Action: Install OracleCM Cluster on the specified node.

PRCR-01052: Failed to find OracleCM Cluster library on node {0}

Cause: Failed to check OracleCM Cluster because of the error in executingthe command to find the file /etc/ORCLcluster/oracm/lib/libskgxn2.so.

Action: Make sure that the caller has the read and execute permission for the library file.

PRCR-01053: Vendor Cluster is not found on node {0}

Cause: The Vendor Cluster was not installed and configured on the specified node.

Action: Install and configure the Vendor Cluster on the specified node.

PRCR-01054: Failed to find Vendor Cluster library on node {0}

Cause: Failed to check OracleCM Cluster because of the error in executingthe command to find the file /etc/ORCLcluster/lib/libskgxn2.so.

Action: Make sure that the caller has the read and execute permission for the library file.

PRCR-01055: Cluster membership check failed for node {0}

Cause: The specified node does not belong to the cluster.

Action: Check whether the node name is correct.

PRCR-01061: User permissions are insufficient

Action: Make sure the user is crs-user or root.

PRCR-01062: Failed to retrieve attributes of resource {0} on node {1}

Cause: An attempt to retrieve attributes of the resource has failed.

Action: Make sure that resource exists.

PRCR-01063: Failed to create context

Cause: Internal error.

Action: Contact Oracle Support Services.

PRCR-01064: Failed to start resource {0} on node {1}

Cause: An attempt to start the resource has failed.

Action: Make sure that resource is ready to start on the node before starting it.

PRCR-01065: Failed to stop resource {0}

Cause: An attempt to stop the resource failed because the resource wasn't running or the running resource had dependent resources also running.

Action: Check the accompanying messages to identify dependent resources and stop them. Make sure that resource is running before stopping it.

PRCR-01067: Failed to create a filter

Cause: An attempt to create a filter has failed.

Action: Check the help for the underlying exception.

PRCR-01068: Failed to query resources

Cause: An attempt to query the resource failed.

Action: Check the help for the underlying exception.

PRCR-01069: Attribute {0} of {1} {2} not found

Cause: Internal error.

Action: Contact Oracle Support Services.

PRCR-01070: Failed to check if {0} {1} is registered

Cause: Failed to check if resource is registered.

Action: Check the help for the underlying exception.

PRCR-01071: Failed to register or update {0} {1}

Cause: An attempt to register or update the resource failed.

Action: Check the help for the underlying exception.

PRCR-01072: Failed to unregister {0} {1}

Cause: An attempt to unregister specified Oracle clusterware entity failed.

Action: Check the help for the underlying exception.

PRCR-01074: Failed to retrieve attributes for {0} {1}

Cause: Failed to retrieve attributes for specified resource.

Action: Check the help for the underlying exception.

PRCR-01075: Failed to retrieve status for resource {0}

Cause: Failed to retrieve status for specified resource.

Action: Check the help for the underlying exception.

PRCR-01076: Failed to retrieve status for resource {0}: {1} is missed

Cause: Internal error.

Action: Contact Oracle Support Services.

PRCR-01077: Failed to calculate status for resource {0}: {1}/{2}

Cause: Internal error.

Action: Contact Oracle Support Services.

PRCR-01078: Failed to retrieve attributes of resource {0}

Cause: An attempt to retrieve attributes of the resource has failed.

Action: Make sure that resource exists.

PRCR-01079: Failed to start resource {0}

Cause: An attempt to start the resource has failed.

Action: Make sure that resource is ready to start before starting it.

PRCR-01085: Unknown typeAsString: {0}

Cause: Internal error.

Action: Contact Oracle Support Services.

PRCR-01086: {0} {1} is already registered

Action: Make sure that a resource is not registered before register it.

PRCR-01087: Failed to retrieve resource {0} instances

Cause: Internal error.

Action: Contact Oracle Support Services.

PRCR-01088: Failed to stop resource {0}: it was not started on node {1}

Cause: The resource was not started on the node..

Action: Make sure that resource was started before stopping it.

PRCR-01089: Failed to relocate resource {0}.

Cause: An attempt to relocate specified resource failed.

Action: Check the help for the underlying exception.

PRCR-01090: Failed to relocate resource {0}. It is not running.

Cause: The resource was not started.

Action: Make sure that resource was started before relocating it.

PRCR-01091: Failed to relocate resource {0}. It is not running on node {1}.

Cause: The resource was not started on the node.

Action: Make sure that resource was started before relocating it.

PRCR-01092: Failed to relocate resource {0}. It is running on more than one node

Cause: The resource was started on more than one node.

Action: Make sure that resource is running on one node only before relocating it.

PRCR-01093: Failed to relocate resource {0}. It is already running on node {1}

Cause: The resource is running that node.

Action: Make sure that resource is not running on a node before relocating it.

PRCR-01094: Failed to start resources on node {0}: {1}

Cause: Resources defined by filter cannot be started on the node.

Action: Make sure that resources are not running and ready to run before starting them. Make sure that the node is online.

PRCR-01095: Failed to start resources using filter {0}

Cause: Resources defined by filter cannot be started.

Action: Make sure that resources are not running and ready to run before starting them.

PRCR-01096: Filter cannot be null

Cause: An attempt to use filter has failed.

Action: Make sure that a filter is provided.

PRCR-01097: Resource attribute not found: {0}

Cause: Requested resource attribute not found.

Action: Make sure that resource has requested attribute.

PRCR-01098: Could not set rolling upgrade mode {0}

Cause: An attempt to start the resource in rolling upgrade mode has failed.

Action: Make sure that the correct LD\_LIBRARY\_PATH is set and all shared libraries are present.

PRCR-01099: Cannot start resource {0} on {1} additional nodes because it would exceed the resource cardinality {2}. Resource is already running on {3} nodes

Cause: Resource cannot be started because of its cardinality restriction.

Action: Make sure that number of additional nodes does not exceed the resource cardinality.

PRCR-01100: Cannot start resource {0} on {1} nodes because it would exceed the resource cardinality {2}

Cause: Resource cannot be started because of its cardinality restriction.

Action: Make sure that number of nodes does not exceed the resource cardinality.

PRCR-01101: Cannot stop resource {0} on {1} nodes, it is running on {2} nodes.

Cause: The resource does not have enough running instances to stop.

Action: Make sure that resource has enough running instances to stop.

PRCR-01102: Failed to verify if user {0} has CRS administrator role

Cause: Failed to verify if the user has CRS administrator role.

Action: Resolve the reported error message and retry.

PRCR-01104: Unsupported relocate option {0}

Cause: Internal error.

Action: Contact Oracle Support Services.

PRCR-01105: Failed to relocate resource {0} to node {1}

Cause: An attempt to relocate the resource to the specified node has failed.

Action: Examine accompanying message(s) that provide details of the error, and respond accordingly.

PRCR-01106: Failed to relocate resource {0} from node {1} to node {2}

Cause: An attempt to relocate the resource from the specified node to another has failed.

Action: Check the help for the underlying exception.

PRCR-01107: Error while trying to set default network as dependent resource for {0}

Cause: An attempt to set default network dependency for the specified resource failed.

Action: Examine the accompanying error message(s) for details.

PRCR-01108: ONS cannot be created because default network is not configured.

Cause: An attempt was made to create ONS resource with out creating the dependent default network resource.

Action: Network resource can be created using 'srvctl add nodeapps' command. Create the network resource and try this command again.

PRCR-01109: Failed to remove attributes "{1}" from resource {0}

Cause: Possible reasons: Oracle Clusterware stack might not be active, CRS resource may not exist, or the CRS resource may not have given attributes set.

Action: Make sure that Oracle Clusterware is active, the CRS resource exists and has given attributes set.

PRCR-01110: Failed to retrieve processed attributes of resource {0} for node {1}

Cause: Oracle Clusterware stack was not active or CRS resource did not not exist.

Action: Make sure that Oracle Clusterware is active, the CRS resource exists.

PRCR-01111: Failed to retrieve processed attributes of resource {0} for node {1}

Cause: requested CRS resource did not exist.

Action: Make sure that the CRS resource exists.

PRCR-01112: Failed to retrieve current event sequence number

Cause: Oracle Clusterware stack was not active.

Action: Make sure that Oracle Clusterware is active.

PRCR-01113: Failed to create detailed error message, rc = {0}

Cause: Internal error

Action: Contact Oracle Support Services.

PRCR-01114: Failed to relocate servers {0} into server pool {1}

Cause: Failed to relocate servers into the given server pool. This message may be accompanied by others providing additional details. A likely cause is violation of defined configuration attributes such as pool MIN\_SIZE, SERVER\_NAMES etc.

Action: If the problem stems from violating configuration attributes, either modify the attributes or reformulate the request. Otherwise, contact Oracle Support Services.

PRCR-01115: Failed to find entities of type {0} that match filters {1} and contain attributes {2}

Cause: Failed to look up entitites of given type that match given filters. This message may be accompanied by others providing additional details. A likely cause is that current user does not have permissions to read attributes of entities of given type.

Action: If lack of permissions is the cause of this failure, then use 'srvctl config \<object> -a' command to find the current owner of the entity and retry the query as that owner user. Otherwise, contact Oracle Support Services.

PRCR-01116: {0} {1} cannot be created and registered now

Cause: Oracle Clusterware stack could not create and register an object.

Action: Check the help for the underlying exception.

PRCR-01117: Failed to stop resources using filter {0}

Cause: An attempt to stop resources using specified filter failed.

Action: Respond based on the accompanying exception message.

PRCR-01118: Failed to generate resource permissions for the resource

Cause: Creation of the Access Control List (permission) structures for the resource failed. This message is accompanied by others providing details of the error.

Action: Respond based on the accompanying exception message(s).

PRCR-01119: Failed to look up CRS resources of {0} type

Cause: An attempt to find the resource for the specified resource type failed because it did not exist.

Action: Create a resource of the type.

PRCR-01120: Resources are already running: {0}

Cause: An attempt to start resources failed because they are already running. For detailed information about resources review the accompanying error messages.

Action: None

PRCR-01121: Value of parameter "{0}" cannot be null or empty

Cause: An attempt to construct ACFS resource name failed due to null or empty value for the indicated parameter.

Action: This is an internal error. Contact Oracle Support Services.

PRCR-01122: Resource type {0} is not registered with Oracle Clusterware

Cause: Given resource type was not registered.

Action: Make sure that required resource type is registered.

PRCR-01123: Failed to rename resource type {0}

Cause: An attempt was made to change name of the given resource type. Resource types cannot be renamed.

Action: None

PRCR-01124: Failed to check resource {0}

Cause: An attempt to check the resource failed.

Action: Correct any problems reported in accompanying messages. Make sure that resource is registered with Oracle Clusterware.

PRCR-01125: Failed to check resource {0} on node {1}

Cause: An attempt to check the resource on specified node failed.

Action: Correct any problems reported in accompanying messages. Make sure that resource is registered with Oracle Clusterware.

PRCR-01126: Failed to relocate resource {0} from node {1}

Cause: An attempt to relocate the resource from the specified node has failed.

Action: Examine the accompanying error messages and respond accordingly.

PRCR-01127: Resource {0} does not have attributes {1} on per node basis

Cause: An attempt to remove given attributes failed because these attributes do not exist on per node basis.

Action: Retry after supplying attributes that exist on per node basis.

PRCR-01128: Resource {0} does not have attributes {1} on node {2}

Cause: An attempt to remove given attributes failed because these attributes do not exist on the given node.

Action: Retry after supplying attributes that exist on the node.

PRCR-01129: Failed to upgrade resource type {0}

Cause: An attempt to upgrade specified resource type failed.

Action: Examine the accompanying error message(s) and respond accordingly.

PRCR-01130: Failed to get the name for resource type {0} from resource type enum class

Cause: An attempt to get the name of the resource type for the given resource type enum class.

Action: Ensure that the resource type enum class contains the proper resource type name.

PRCR-01131: CVU resource cannot be created because default network is not configured.

Cause: An attempt was made to create CVU resource without creating the dependent default network resource.

Action: Network resource can be created using 'srvctl add nodeapps' command. Create the network resource and try this command again.

PRCR-01132: Failed to stop resources using a filter

Cause: An attempt to stop resources failed because resources were not running or running resources had dependent resources also running.

Action: Check the accompanying messages to identify dependent resources and stop them. Make sure that resources are running before stopping them.

PRCR-01133: Failed to stop database {0} and its running services

Cause: An attempt to stop given database and its running services failed.

Action: Correct any problems reported in accompanying messages.

PRCR-01134: Failed to stop database {0} and its running services on nodes {1}

Cause: An attempt to stop the given database and its running services failed on the specified nodes.

Action: Correct any problems reported in accompanying messages.

PRCR-01135: Failed to check if node with node number 0 exists

Cause: An attempt failed to determine whether a node numbered 0 exists.

Action: Follow action specified for accompanying message.