---
title: Making Applications Highly Available Using Oracle Clusterware
book: Database Clusterware Administration and Deployment Guide
doc_id: E41959-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/rac.112/e41959/crschp.htm
tags:
  - oracle
  - 11g
  - database-clusterware-administration-and-deployment-guide
---

## 6 Making Applications Highly Available Using Oracle Clusterware

When an application, process, or server fails in a cluster, you want the disruption to be as short as possible, if not completely unknown to users. For example, when an application fails on a server, that application can be restarted on another server in the cluster, minimizing or negating any disruption in the use of that application. Similarly, if a server in a cluster fails, then all of the applications and processes running on that server must be able to fail over to another server to continue providing service to the users. Using customizable [action script](glossary.md) s and application agent programs, as well as resource attributes that you assign to applications and processes, Oracle Clusterware can manage all these entities to ensure high availability.

This chapter explains how to use Oracle Clusterware to start, stop, monitor, restart, and relocate applications. Oracle Clusterware is the underlying cluster solution for Oracle Real Application Clusters (Oracle RAC). The same functionality and principles you use to manage Oracle RAC databases are applied to the management of applications.

This chapter includes the following topics:

## Oracle Clusterware Resources and Agents

This section discusses the framework that Oracle Clusterware uses to monitor and manage [resource](glossary.md) s, in order to ensure high application availability.

This section includes the following topics:

- Resources
- Resource Types
- Agents
- Action Scripts
- Building an Agent
- Registering a Resource in Oracle Clusterware

### Resources

Oracle Clusterware manages applications and processes as resources that you register with Oracle Clusterware. The number of resources you register with Oracle Clusterware to manage an application depends on the application. Applications that consist of only one process are usually represented by only one resource. More complex applications, built on multiple processes or components, may require multiple resources.

When you register an application as a resource in Oracle Clusterware, you define how Oracle Clusterware manages the application using resource attributes you ascribe to the resource. The frequency with which the resource is checked and the number of attempts to restart a resource on the same server after a failure before attempting to start it on another server (failover) are examples of resource attributes. The registration information also includes a path to an action script or application-specific action program that Oracle Clusterware calls to start, stop, check, and clean up the application.

An action script is a shell script (a batch script in Windows) that a generic script agent provided by Oracle Clusterware calls. An application-specific agent is usually a C or C++ program that calls Oracle Clusterware-provided APIs directly.

See Also:

[Appendix B, "Oracle Clusterware Resource Reference"](resatt.md) for an example of an action script

Oracle Clusterware 11g release 2 (11.2) uses agent programs (agents) to manage resources and includes the following built-in agents so that you can use scripts to protect an application:

- `scriptagent`: Use this agent (`scriptagent.exe` in Windows) to use shell or batch scripts to protect an application. Both the `cluster_resource` and `local_resource` resource types are configured to use this agent, and any resources of these types automatically take advantage of this agent.
- `appagent`: This agent (`appagent.exe` in Windows) automatically protects any resources of the `application` resource type used in previous versions of Oracle Clusterware. You are not required to configure anything to take advantage of the agent. It invokes action scripts in the manner done with previous versions of Oracle Clusterware and should only be used for the `application` resource type.
	Note:
	Oracle recommends that you use `scriptagent` for all resources of types other than `application`. Oracle provides the application agent for backward compatibility with the deprecated `application` resource type.

By default, all resources not of the `application` resource type, use the script agent, unless you override this behavior by creating a new resource type and specifying a different agent as part of the resource type specification (using the `AGENT_FILENAME` attribute).

Additionally, you can create your own agents to manage your resources in any manner you want.

See Also:

"Resource Types" for more information about resource types and "Building an Agent" for more information about building custom agents

### Resource Types

Generally, all resources are unique but some resources may have common attributes. Oracle Clusterware uses resource types to organize these similar resources. Benefits that resource types provide are:

- Manage only necessary resource attributes
- Manage all resources based on the resource type

Every resource that you register in Oracle Clusterware must have a certain resource type. In addition to the resource types included in Oracle Clusterware, you can define custom resource types using the Oracle Clusterware Control (CRSCTL) utility. The included resource types are:

- Local resource: Instances of local resources—type name is `local_resource` —run on each server of the cluster. When a server joins the cluster, Oracle Clusterware automatically extends local resources to have instances tied to the new server. When a server leaves the cluster, Oracle Clusterware automatically sheds the instances of local resources that ran on the departing server. Instances of local resources are pinned to their servers; they do not fail over from one server to another.
- Cluster resource: Cluster-aware resource types—type name is `cluster_resource` —are aware of the cluster environment and are subject to [cardinality](glossary.md) and cross-server switchover and failover.

See Also:

- [Appendix E, "CRSCTL Utility Reference"](crsref.md) for more information about using CRSCTL to add resource types
- "Resource States" for more information about resource state

Note:

Previous versions of Oracle Clusterware only supported the application resource type. This resource type still exists, but only for backward compatibility. Oracle recommends that you register application-type resources using the `cluster_resource` resource type in Oracle Clusterware 11g release 2 (11.2). If you decide not to register your application-type resources using the `cluster_resource` resource type, then consult the documentation that corresponds to those applications for administration information.

### Agents

Oracle Clusterware manages applications when they are registered as resources with Oracle Clusterware. Oracle Clusterware has access to application-specific primitives that have the ability to start, stop, and monitor a specific resource. Oracle Clusterware runs all resource-specific commands through an entity called an agent.

An agent is a process that contains the agent framework and user code to manage resources. The agent framework is a library that enables you to plug in your application-specific code to manage customized applications. You program all of the actual application management functions, such as starting, stopping and checking the health of an application, into the agent. These functions are referred to as entry points.

The agent framework is responsible for invoking these entry point functions on behalf of Oracle Clusterware. Agent developers can use these entry points to plug in the required functionality for a specific resource regarding how to start, stop, and monitor a resource. Agents are capable of managing multiple resources.

Agent developers can set the following entry points as callbacks to their code:

- START: The START entry point acts to bring a resource online. The agent framework calls this entry point whenever it receives the start command from Oracle Clusterware.
- STOP: The STOP entry points acts to gracefully bring down a resource. The agent framework calls this entry point whenever it receives the stop command from Oracle Clusterware.
- CHECK: The CHECK (monitor) entry point acts to monitor the health of a resource. The agent framework periodically calls this entry point. If it notices any state change during this action, then the agent framework notifies Oracle Clusterware about the change in the state of the specific resource.
- CLEAN: The CLEAN entry point acts whenever there is a need to clean up a resource. It is a non-graceful operation that is invoked when users must forcefully terminate a resource. This command cleans up the resource-specific environment so that the resource can be restarted.
- ABORT: If any of the other entry points hang, the agent framework calls the ABORT entry point to abort the ongoing action. If the agent developer does not supply an abort function, then the agent framework exits the agent program.

START, STOP, CHECK, and CLEAN are mandatory entry points and the agent developer must provide these entry points when building an agent. Agent developers have several options to implement these entry points, including using C, C++, or scripts. It is also possible to develop agents that use both C or C++ and script-type entry points. When initializing the agent framework, if any of the mandatory entry points are not provided, then the agent framework invokes a script pointed to by the `ACTION_SCRIPT` resource attribute.

See Also:

["ACTION\_SCRIPT"](resatt.md) for information about this resource attribute

At any given time, the agent framework invokes only one entry point per application. If that entry point hangs, then the agent framework calls the ABORT entry point to abort the current operation. The agent framework periodically invokes the CHECK entry point to determine the state of the resource. This entry point must return one of the following states as the resource state:

- CLSAGFW\_ONLINE: The CHECK entry point returns ONLINE if the resource was brought up successfully and is currently in a functioning state. The agent framework continues to monitor the resource when it is in this state. This state has a numeric value of 0 for the `scriptagent`.
- CLSAGFW\_UNPLANNED\_OFFLINE/CLSAGFW\_PLANNED\_OFFLINE: The OFFLINE state indicates that the resource is not currently running. These two states have numeric values of 1 and 2, respectively, for the `scriptagent`.
	Two distinct categories exist to describe an resource's offline state: planned and unplanned.
	When the state of the resource transitions to OFFLINE through Oracle Clusterware, then it is assumed that the intent for this resource is to be offline (`TARGET=OFFLINE`), regardless of which value is returned from the CHECK entry point. However, when an agent detects that the state of a resource has changed independent of Oracle Clusterware (such as somebody stopping the resource through a non-Oracle interface), then the intent must be carried over from the agent to the Cluster Ready Services daemon (`crsd`). The intent then becomes the determining factor for the following:
	- Whether to keep or to change the value of the resource's `TARGET` resource attribute. PLANNED\_OFFLINE indicates that the `TARGET` resource attribute must be changed to OFFLINE only if the resource was running before. If the resource was not running (`STATE=OFFLINE`, `TARGET=OFFLINE`) and a request comes in to start it, then the value of the `TARGET` resource attribute changes to ONLINE. The start request then goes to the agent and the agent reports back to Oracle Clusterware a PLANNED\_OFFLINE resource state, and the value of the `TARGET` resource attribute remains ONLINE. UNPLANNED\_OFFLINE does not change the `TARGET` attribute.
		- Whether to leave the resource's state as UNPLANNED\_OFFLINE or attempt to recover the resource by restarting it locally or failing it over to a another server in the cluster. The PLANNED\_OFFLINE state makes `crsd` leave the resource as is, whereas the UNPLANNED\_OFFLINE state prompts resource recovery.
- CLSAGFW\_UNKNOWN: The CHECK entry point returns UNKNOWN if the current state of the resource cannot be determined. In response to this state, Oracle Clusterware does not attempt to failover or to restart the resource. The agent framework continues to monitor the resource if the previous state of the resource was either ONLINE or PARTIAL. This state has a numeric value of 3 for the `scriptagent`.
- CLSAGFW\_PARTIAL: The CHECK entry point returns PARTIAL when it knows that a resource is partially ONLINE and some of its services are available. Oracle Clusterware considers this state as partially ONLINE and does not attempt to failover or to restart the resource. The agent framework continues to monitor the resource in this state. This state has a numeric value of 4 for the `scriptagent`.
- CLSAGFW\_FAILED: The CHECK entry point returns FAILED whenever it detects that a resource is not in a functioning state and some of its components have failed and some clean up is required to restart the resource. In response to this state, Oracle Clusterware calls the CLEAN action to clean up the resource. After the CLEAN action finishes, the state of the resource is expected to be OFFLINE. Next, depending on the policy of the resource, Oracle Clusterware may attempt to failover or restart the resource. Under no circumstances does the agent framework monitor failed resources. This state has a numeric value of 5 for the `scriptagent`.

The agent framework implicitly monitors resources in the states listed in Table 6-1 at regular intervals, as specified by the `CHECK_INTERVAL` or `OFFLINE_CHECK_INTERVAL` resource attributes.

See Also:

["CHECK\_INTERVAL"](resatt.md) and ["OFFLINE\_CHECK\_INTERVAL"](resatt.md) for more information about these resource attributes

Table 6-1 Agent Framework Monitoring Characteristics

| State | Condition | Frequency |
| --- | --- | --- |
| ONLINE | Always | `CHECK_INTERVAL` |
| PARTIAL | Always | `CHECK_INTERVAL` |
| OFFLINE | Only if the value of the `OFFLINE_CHECK_INTERVAL` resource attribute is greater than 0. | `OFFLINE_CHECK_INTERVAL` |
| UNKNOWN | Only monitored if the resource was previously being monitored as a result of any one of the previously mentioned conditions. | Whatever the value of either the `CHECK_INTERVAL` or `OFFLINE_CHECK_INTERVAL` attributes. |

Whenever an agent starts, the state of all the resources it monitors is set to UNKNOWN. After receiving an initial probe request from Oracle Clusterware, the agent framework executes the CHECK entry point for all of the resources to determine their current states.

Once the CHECK action successfully completes for a resource, the state of the resource transitions to one of the previously mentioned states. The agent framework then starts resources based on commands issued from Oracle Clusterware. After the completion of every action, the agent framework invokes the CHECK action to determine the current resource state. If the resource is in one of the monitored states listed in Table 6-1, then the agent framework periodically executes the CHECK entry point to check for changes in resource state.

By default, the agent framework does not monitor resources that are offline. However, if the value of the `OFFLINE_CHECK_INTERVAL` attribute is greater than 0, then the agent framework monitors offline resources.

### Action Scripts

An action script defines one or more actions to start, stop, check, or clean resources. The agent framework invokes these actions in the absence of the C/C++ actions. Using action scripts, you can build an agent that contains the C/C++ entry points, as well as the script entry points. If all of the actions are defined in the action script, then you can use the script agent to invoke the actions defined in any action scripts.

Before invoking the action defined in the action script, the agent framework exports all the necessary attributes from the resource profile to the environment. Action scripts can log messages to the `stdout/stderr`, and the agent framework prints those messages in the agent logs. However, action scripts can use special tags to send the progress, warning, or error messages to the `crs*` client tools by prefixing one of the following tags to the messages printed to `stdout/stderr`:

```
CRS_WARNING
CRS_ERROR
CRS_PROGRESS
```

The agent framework strips out the prefixed tag when it sends the final message to the `crs*` clients.

Resource attributes can be accessed from within an action script as environment variables prefixed with `_CRS_`. For example, the `START_TIMEOUT` attribute becomes an environment variable named `_CRS_START_TIMEOUT`.

See Also:

- `"crsctl start resource"` and `"crsctl stop resource"` for more information about using the `-env` option as a way to override attribute values for a single start or stop action, respectively
- [Example B-3](resatt.md) for an example of an action script for an agent

### Building an Agent

Building an agent for a specific application involves the following steps:

1. Implement the agent framework entry points either in scripts, C, or C++.
2. Build the agent executable (for C and C++ agents).
3. Collect all the parameters needed by the entry points and define a new resource type. Set the `AGENT_FILENAME` attribute to the absolute path of the newly built executable.

### Registering a Resource in Oracle Clusterware

Register resources in Oracle Clusterware 11g release 2 (11.2) using the `crsctl add resource` command.

Note:

The `CRS_REGISTER` and `CRS_PROFILE` commands are still available in the Oracle Clusterware home but are deprecated for this release.

To register an application as a resource:

```
$ crsctl add resource resource_name -type resource_type [-file file_path] | [-attr "attribute_name='attribute_value', attribute_name='attribute_value', ..."]
```

Choose a name for the resource based on the application for which it is being created. For example, if you create a resource for an Apache Web server, then you might name the resource `myApache`.

The name of the resource type follows the `-type` option. You can specify resource attributes in either a text file specified with the `-file` option or in a comma-delimited list of resource attribute-value pairs enclosed in double quotation marks (`""`) following the `-attr` option. You must enclose space- or comma-delimited attribute names and values enclosed in parentheses in single quotation marks (`''`).

The following is an example of an attribute file:

```
PLACEMENT=favored
HOSTING_MEMBERS=node1 node2 node3
RESTART_ATTEMPTS@CARDINALITYID(1)=0
RESTART_ATTEMPTS@CARDINALITYID(2)=0
FAILURE_THRESHOLD@CARDINALITYID(1)=2
FAILURE_THRESHOLD@CARDINALITYID(2)=4
FAILURE_INTERVAL@CARDINALITYID(1)=300
FAILURE_INTERVAL@CARDINALITYID(2)=500
CHECK_INTERVAL=2
CARDINALITY=2
```

The following is an example of using the `-attr` option:

```
$ crsctl add resource resource_name -type resource_type] [-attr "PLACEMENT='favored', HOSTING_MEMBERS='node1 node2 node3', ..."]
```

See Also:

- "Adding User-defined Resources" for examples of using the `crsctl add resource` command
- `"crsctl add resource"` for more information about using the `crsctl add resource` command
- ["Resource Attributes"](resatt.md) for more information about resource attributes

## Overview of Using Oracle Clusterware to Enable High Availability

Oracle Clusterware manages resources based on how you configure them to increase their availability. You can configure your resources so that Oracle Clusterware:

- Starts resources during cluster or server start
- Restarts resources when failures occur
- Relocates resources to other servers, if the servers are available

To manage your applications with Oracle Clusterware:

1. Create an action script or use an existing agent.
2. Register your applications as resources with Oracle Clusterware.
	If a single application requires that you register multiple resources, you may be required to define relevant dependencies between the resources.
3. Assign the appropriate privileges to the resource.
4. Start or stop your resources.

When a resource fails, Oracle Clusterware attempts to restart the resource based on attribute values that you provide when you register an application or process as a resource. If a server in a cluster fails, then you can configure your resources so that processes that were assigned to run on the failed server restart on another server. Based on various resource attributes, Oracle Clusterware supports a variety of configurable scenarios.

When you register a resource in Oracle Clusterware, the relevant information about the application and the resource-relevant information, is stored in the Oracle Cluster Registry (OCR). This information includes:

- Path to the action script or application-specific agent: This is the absolute path to the script or application-specific agent that defines the start, stop, check, and clean actions that Oracle Clusterware performs on the application.
	See Also:
	"Agents" for more information about these actions
- Privileges: Oracle Clusterware has the necessary privileges to control all of the components of your application for high availability operations, including the right to start processes that are owned by other user identities. Oracle Clusterware must run as a privileged user to control applications with the correct start and stop processes.
- Resource Dependencies: You can create relationships among resources that imply an operational ordering or that affect the placement of resources on servers in the cluster. For example, Oracle Clusterware can only start a resource that has a hard start dependency on another resource if the other resource is running. Oracle Clusterware prevents stopping a resource if other resources that depend on it are running. However, you can force a resource to stop using the `crsctl stop resource -f` command, which first stops all resources that depend on the resource being stopped.

This section includes the following topics:

- Resource Attributes
- Resource States
- Resource Dependencies
- Resource Placement

### Resource Attributes

Resource attributes define how Oracle Clusterware manages resources of a specific resource type. Each resource type has a unique set of attributes. Some resource attributes are specified when you register resources, while others are internally managed by Oracle Clusterware.

Note:

Where you can define new resource attributes, you can only use US-7 ASCII characters.

See Also:

[Appendix B, "Oracle Clusterware Resource Reference"](resatt.md) for complete details of resource attributes

### Resource States

Every resource in a cluster is in a particular state at any time. Certain actions or events can cause that state to change.

Table 6-2 lists and describes the possible [resource state](glossary.md) s.

Table 6-2 Possible Resource States

| State | Description |
| --- | --- |
| ONLINE | The resource is running. |
| OFFLINE | The resource is not running. |
| UNKNOWN | An attempt to stop the resource has failed. Oracle Clusterware does not actively monitor resources that are in this state. You must perform an application-specific action to ensure that the resource is offline, such as stop a process, and then run the `crsctl stop resource` command to reset the state of the resource to OFFLINE. |
| INTERMEDIATE | A resource can be in the INTERMEDIATE state because of one of two events:  1. Oracle Clusterware cannot determine the state of the resource but the resource was either attempting to go online or was online the last time its state was precisely known. Usually, the resource transitions out of this state on its own over time, as the conditions that impeded the check action no longer apply. 2. A resource is partially online. For example, the Oracle Database VIP resource fails over to another server when its home server leaves the cluster. However, applications cannot use this VIP to access the database while it is on a non-home server. Similarly, when an Oracle Database instance is started and not open, the resource is partially online: it is running but is not available to provide services.  Oracle Clusterware actively monitors resources that are in the INTERMEDIATE state and, typically, you are not required to intervene. If the resource is in the INTERMEDIATE state due to the preceding reason 1, then as soon as the state of the resource is established, Oracle Clusterware transitions the resource out of the INTERMEDIATE state.  If the resource is in the INTERMEDIATE state due to the preceding reason 2, then it stays in this state if it remains partially online. For example, the home server of the VIP must rejoin the cluster so the VIP can switch over to it. A database administrator must issue a command to open the database instance.  In either case, however, Oracle Clusterware transitions the resource out of the INTERMEDIATE state automatically as soon as it is appropriate.Use the `STATE_DETAILS` resource attribute to explain the reason for a resource being in the INTERMEDIATE state and provide a solution to transition the resource out of this state. |

### Resource Dependencies

You can configure resources to be dependent on other resources, so that the dependent resources can only start or stop when certain conditions of the resources on which they depend are met. For example, when Oracle Clusterware attempts to start a resource, it is necessary for any resources on which the initial resource depends to be running and in the same location. If Oracle Clusterware cannot bring the resources online, then the initial (dependent) resource cannot be brought online, either. If Oracle Clusterware stops a resource or a resource fails, then any dependent resource is also stopped.

Some resources require more time to start than others. Some resources must start whenever a server starts, while other resources require a manual start action. These and many other examples of resource-specific behavior imply that each resource must be described in terms of how it is expected to behave and how it relates to other resources (resource dependencies).

You can configure resources so that they depend on Oracle resources. When creating resources, however, do not use an ora prefix in the resource name. This prefix is reserved for Oracle use only.

Previous versions of Oracle Clusterware included only two dependency specifications: the `REQUIRED_RESOURCES` resource attribute and the `OPTIONAL_RESOURCES` resource attribute. The `REQUIRED_RESOURCES` resource attribute applied to both start and stop resource dependencies.

Note:

The `REQUIRED_RESOURCES` and `OPTIONAL_RESOURCES` resource attributes are still available only for resources of `application` type. Their use to define resource dependencies in Oracle Clusterware 11g release 2 (11.2) is deprecated.

In Oracle Clusterware 11g release 2 (11.2) resource dependencies are separated into start and stop categories. This separation improves and expands the start and stop dependencies between resources and resource types.

This section includes the following topics:

- Start Dependencies
- Stop Dependencies

#### Start Dependencies

Oracle Clusterware considers start dependencies contained in the profile of a resource when the [start effort evaluation](glossary.md) for that resource begins. You specify start dependencies for resources using the `START_DEPENDENCIES` resource attribute. You can use modifiers on each dependency to further configure the dependency.

See Also:

["START\_DEPENDENCIES"](resatt.md) for more information about the resource attribute, modifiers, and usage

This section includes descriptions of the following START dependencies:

- `hard`
- `weak`
- `attraction`
- `pullup`
- `dispersion`

hard

Define a `hard` start dependency for a resource if another resource must be running before the dependent resource can start. For example, if resource A has a `hard` start dependency on resource B, then resource B must be running before resource A can start.

Note:

Oracle recommends that resources with `hard` start dependencies also have `pullup` start dependencies.

You can configure the `hard` start dependency with the following constraints:

- `START_DEPENDENCIES=hard(global:resourceB)`
	By default, resources A and B must be located on the same server (co-located). Use the `global` modifier to specify that resources need not be co-located. For example, if resource A has a `hard(global:resourceB)` start dependency on resource B, then, if resource B is running on any node in the cluster, resource A can start.
- `START_DEPENDENCIES=hard(intermediate:resourceB)`
	Use the `intermediate` modifier to specify that the dependent resource can start if a resource on which it depends is in either the `ONLINE` or `INTERMEDIATE` state.
- `START_DEPENDENCIES=hard(type:resourceB.type)`
	Use the `type` modifier to specify whether the `hard` start dependency acts on a particular resource or a resource type. For example, if you specify that resource A has a `hard` start dependency on the `resourceB.type` type, then if any resource of the `resourceB.type` type is running, resource A can start.
- `START_DEPENDENCIES=hard(resourceB, intermediate:resourceC, intermediate:global:type:resourceC.type)`
	You can combine modifiers and specify multiple resources in the `START_DEPENDENCIES` resource attribute.
	Note:
	Separate modifier clauses with commas. The `type` modifier clause must always be the last modifier clause in the list and the `type` modifier must always directly precede the type.

weak

If resource A has a `weak` start dependency on resource B, then an attempt to start resource A attempts to start resource B, if resource B is not running. The result of the attempt to start resource B is, however, of no consequence to the result of starting resource A.

You can configure the `weak` start dependency with the following constraints:

- `START_DEPENDENCIES=weak(global:resourceB)`
	By default, resources A and B must be co-located. Use the `global` modifier to specify that resources need not be co-located. For example, if resource A has a `weak(global:resourceB)` start dependency on resource B, then, if resource B is running on any node in the cluster, resource A can start.
- `START_DEPENDENCIES=weak(concurrent:resourceB)`
	Use the `concurrent` modifier to specify that resource A and resource B can start concurrently, instead of waiting for resource B to start, first.
- `START_DEPENDENCIES=weak(type:resourceB.type)`
	Use the `type` modifier to specify that the dependency acts on a resource of a particular resource type, such as `resourceB.type`.

attraction

If resource A has an `attraction` dependency on resource B, then Oracle Clusterware prefers to place resource A on servers hosting resource B. Dependent resources, such as resource A in this case, are more likely to run on servers on which resources to which they have `attraction` dependencies are running. Oracle Clusterware places dependent resources on servers with resources to which they are attracted.

You can configure the `attraction` start dependency with the following constraints:

- `START_DEPENDENCIES=attraction(intermediate:resourceB)`
	Use the `intermediate` modifier to specify whether the resource is attracted to resources that are in the `INTERMEDIATE` state.
- `START_DEPENDENCIES=attraction(type:resourceB.type)`
	Use the `type` modifier to specify whether the dependency acts on a particular resource type. The dependent resource is attracted to the server hosting the greatest number of resources of a particular type.

Note:

Previous versions of Oracle Clusterware used the now deprecated `OPTIONAL_RESOURCES` attribute to express attraction dependency.

pullup

Use the `pullup` start dependency if resource A must automatically start whenever resource B starts. This dependency only affects resource A if it is not running. As is the case for other dependencies, `pullup` may cause the dependent resource to start on any server. Use the `pullup` dependency whenever there is a hard stop dependency, so that if resource A depends on resource B and resource B fails and then recovers, then resource A is restarted.

Note:

Oracle recommends that resources with `hard` start dependencies also have `pullup` start dependencies.

You can configure the `pullup` start dependency with the following constraints:

- `START_DEPENDENCIES=pullup(intermediate:resourceB)`
	Use the `intermediate` modifier to specify whether resource B can be either in the `ONLINE` or `INTERMEDIATE` state to start resource A.
	If resource A has a `pullup` dependency on multiple resources, then resource A starts only when all resources upon which it depends, start.
- `START_DEPENDENCIES=pullup:always(resourceB)`
	Use the `always` modifier to specify whether Oracle Clusterware starts resource A despite the value of its `TARGET` attribute, whether it is `ONLINE` or `OFFLINE`. By default, without using the `always` modifier, `pullup` only starts resources if the value of the `TARGET` attribute of the dependent resource is `ONLINE`.
- `START_DEPENDENCIES=pullup(type:resourceB.type)`
	Use the `type` modifier to specify that the dependency acts on a particular resource type.

dispersion

If you specify the `dispersion` start dependency for a resource, then Oracle Clusterware starts this resource on a server that has the fewest number of resources to which this resource has dispersion. Resources with dispersion may still end up running on the same server if there are not enough servers to disperse them to.

You can configure the `dispersion` start dependency with the following modifiers:

- `START_DEPENDENCIES=dispersion(intermedite:resourceB)`
	Use the `intermediate` modifier to specify that Oracle Clusterware disperses resource A whether resource B is either in the `ONLINE` or `INTERMEDIATE` state.
- `START_DEPENDENCIES=dispersion:active(resourceB)`
	Typically, dispersion is only applied when starting resources. If at the time of starting, resources that disperse each other start on the same server (because there are not enough servers at the time the resources start), then Oracle Clusterware leaves the resources alone once they are running, even when more servers join the cluster. If you specify the `active` modifier, then Oracle Clusterware reapplies dispersion on resources later when new servers join the cluster.

#### Stop Dependencies

Oracle Clusterware considers stop dependencies between resources whenever a resource is stopped (the resource state changes from `ONLINE` to any other state).

hard

If resource A has a `hard` stop dependency on resource B, then resource A must be stopped when B stops running. The two resources may attempt to start or relocate to another server, depending upon how they are configured. Oracle recommends that resources with `hard` stop dependencies also have `hard` start dependencies.

You can configure the `hard` stop dependency with the following modifiers:

- `STOP_DEPENDENCIES=hard(intermedite:resourceB)`
	Use the `intermediate` modifier to specify whether resource B must be in either the `ONLINE` or `INTERMEDIATE` state for resource A to stay online.
- `STOP_DEPENDENCIES=hard(global:resourceB)`
	Use the `global` modifier to specify whether resource A requires that resource B be present on the same server or on any server in the cluster to remain online. If this constraint is not specified, then resources A and B must be running on the same server. Oracle Clusterware stops resource A when that condition is no longer met.
- `STOP_DEPENDENCIES=hard(shutdown:resourceB)`
	Use the `shutdown` modifier to stop the resource only when you shut down the Oracle Clusterware stack using either the `crsctl stop crs` or `crsctl stop cluster` commands.

See Also:

["STOP\_DEPENDENCIES"](resatt.md) for more information about modifiers

Affect of Resource Dependencies on Resource State Recovery

When a resource goes from a running to a non-running state, while the intent to have it running remains unchanged, this transition is called a resource failure. At this point, Oracle Clusterware applies a resource state recovery procedure that may try to restart the resource locally, relocate it to another server, or just stop the dependent resources, depending on the high availability policy for resources and the state of entities at the time.

When two or more resources depend on each other, a failure of one of them may end up causing the other to fail, as well. In most cases, it is difficult to control or even predict the order in which these failures are detected. For example, even if resource A depends on resource B, Oracle Clusterware may detect the failure of resource B after the failure of resource A.

This lack of failure order predictability can cause Oracle Clusterware to attempt to restart dependent resources in parallel, which, ultimately, leads to the failure to restart some resources, because the resources upon which they depend are being restarted out of order.

In this case, Oracle Clusterware reattempts to restart the dependent resources locally if either or both the `hard` stop and `pullup` dependencies are used. For example, if resource A has either a `hard` stop dependency or `pullup` dependency, or both, on resource B, and resource A fails because resource B failed, then Oracle Clusterware may end up trying to restart both resources at the same time. If the attempt to restart resource A fails, then as soon as resource B successfully restarts, Oracle Clusterware reattempts to restart resource A.

### Resource Placement

As part of the start effort evaluation, the first decision that Oracle Clusterware must make is where to start (or place) the resource. Making such a decision is easy when the caller specifies the target server by name. If a target server is not specified, however, then Oracle Clusterware attempts to locate the best possible server for placement given the resource's configuration and the current state of the cluster.

Oracle Clusterware considers a resource's placement policy first and filters out servers that do not fit with that policy. Oracle Clusterware sorts the remaining servers in a particular order depending on the value of the `PLACEMENT` resource attribute of the resource.

See Also:

"Application Placement Policies" for more information about the `PLACEMENT` resource attribute

The result of this consideration is a maximum of two lists of candidate servers on which Oracle Clusterware can start the resource. One list contains preferred servers and the other contains possible servers. The list of preferred servers will be empty if the value of the `PLACEMENT` resource attribute for the resource is set to `balanced` or `restricted`. The placement policy of the resource determines on which server the resource wants to run. Oracle Clusterware considers preferred servers over possible servers, if there are servers in the preferred list.

Oracle Clusterware then considers the resource's dependencies to determine where to place the resource, if any exist. The `attraction` and `dispersion` start dependencies affect the resource placement decision, as do some of the dependency modifiers. Oracle Clusterware applies these placement hints to further order the servers in the two previously mentioned lists. Note that Oracle Clusterware processes each list of servers independently, so that the effect of the resource's placement policy is not confused by that of dependencies.

Finally, Oracle Clusterware chooses the first server from the list of preferred servers, if any servers are listed. If there are no servers on the list of preferred servers, then Oracle Clusterware chooses the first server from the list of possible servers, if any servers are listed. When no servers exist in either list, Oracle Clusterware generates a resource placement error.

Note:

Neither the placement policies nor the dependencies of the resources related to the resource Oracle Clusterware is attempting to start affect the placement decision.

## Registering an Application as a Resource

This section presents examples of the procedures for registering an application as a resource in Oracle Clusterware. The procedures instruct you how to add an Apache Web server as a resource to Oracle Clusterware.

The examples in this section assume that the Oracle Clusterware administrator has full administrative privileges over Oracle Clusterware and the user or group that owns the application that Oracle Clusterware is going to manage. Once the registration process is complete, Oracle Clusterware can start any application on behalf of any operating system user.

Oracle Clusterware distinguishes between an owner of a registered resource and a user. The owner of a resource is the operating system user under which the agent runs. The `ACL` resource attribute of the resource defines permissions for the users and the owner. Only `root` can modify any resource.

See Also:

["Role-Separated Management"](admin.md)

Notes:

- Oracle Clusterware commands prefixed with `crs_` are deprecated with this release. CRSCTL commands replace those commands. See [Appendix E, "CRSCTL Utility Reference"](crsref.md) for a list of CRSCTL commands and their corresponding `crs_` commands.
- Do not use CRSCTL commands on any resources that have names prefixed with `ora` (because these are Oracle resources), unless My Oracle Support directs you to do so.
	To configure Oracle resources, use the server control utility, SRVCTL, which provides you with all configurable options.

This section includes the following topics:

- Creating an Application VIP Managed by Oracle Clusterware
- Adding User-defined Resources
- Adding Resources Using Oracle Enterprise Manager
- Changing Resource Permissions
- Application Placement Policies
- Unregistering Applications and Application Resources

### Creating an Application VIP Managed by Oracle Clusterware

If clients of an application access the application through a network, and the placement policy for the application allows it to fail over to another node, then you must register a virtual internet protocol address (VIP) on which the application depends. An application VIP is a cluster resource that Oracle Clusterware manages (Oracle Clusterware provides a standard VIP agent for application VIPs). You should base any new application VIPs on this VIP type to ensure that your system experiences consistent behavior among all of the VIPs that you deploy in your cluster.

While you can add a VIP in the same way that you can add any other resource that Oracle Clusterware manages, Oracle recommends using the script `Grid_home` `/bin/appvipcfg` to create or delete an application VIP.

To create an application VIP, use the following syntax:

```
appvipcfg create -network=network_number -ip=ip_address -vipname=vip_name
-user=user_name [-group=group_name] [-failback=0 | 1]
```

To delete an application VIP, use the following syntax:

```
appvipcfg delete -vipname=vip_name
```

Where `network_number` is the number of the network, `ip_address` is the IP address, `vip_name` is the name of the VIP, `user_name` is the name of the user who installed Oracle Database, and `group_name` is the name of the group. The default value of the `-failback` option is 0. If you set the option to 1, then the VIP (and therefore any resources that depend on VIP) fails back to the original node when it becomes available again.

For example, as `root`, run the following command:

```
# Grid_home/bin/appvipcfg create -network=1 -ip=148.87.58.196 -vipname=appsVIP -user=root
```

The script only requires a network number (default is 1), the IP address, and a name for the VIP resource, as well as the user that owns the application VIP resource. A VIP resource is typically owned by `root` because VIP related operations require root privileges.

To delete an application VIP, use the same script with the `delete` option. This option accepts the VIP name as a parameter. For example:

```
# Grid_home/bin/appvipcfg delete -vipname=appsVIP
```

After you have created the application VIP using this configuration script, you can view the VIP profile using the following command:

```
Grid_home/bin/crsctl status res appsVIP -p
```

Verify and, if required, modify the following parameters using the `Grid_home` `/bin/crsctl modify res` command.

See Also:

[Appendix B, "Oracle Clusterware Resource Reference"](resatt.md) for detailed information about using CRSCTL commands

The `appvipcfg` script assumes that the default `ora.vip` network resource (`ora.net1.network`) is used as the default. In addition, it is also assumes that a default `app.appvip_net1.type` is used for those purposes.

As the Oracle Database installation owner, start the VIP resource:

```
$ crsctl start resource appsVIP
```

Adding an Application VIP with Oracle Enterprise Manager

To add an application VIP with Oracle Enterprise Manager:

1. Log into Oracle Enterprise Manager Database Control.
2. Click the Cluster tab.
3. Click Administration.
4. Click Manage Resources.
5. Enter a cluster administrator user name and password to display the Manage Resources page.
6. Click Add Application VIP.
7. Enter a name for the VIP in the Name field.
8. Enter a network number in the Network Number field.
9. Enter an IP address for the VIP in the Internet Protocol Address field.
10. Enter root in the Primary User field. Oracle Enterprise Manager defaults to whatever user name you are logged in as.
11. Select Start the resource after creation if you want the VIP to start immediately.
12. Click Continue to display the Confirmation: Add VIP Resource page.
13. Enter root and the root password as the cluster credentials.
14. Click Continue to create the application VIP.

### Adding User-defined Resources

You can add resources to Oracle Clusterware at any time. However, if you add a resource that is dependent on another resource, then you must first add the resource upon which it is dependent.

In the examples in this section, assume that an action script, `myApache.scr`, resides in the `/opt/cluster/scripts` directory on each node to facilitate adding the resource to the cluster. It is also assumed that a server pool has been created to host an application. This server pool is not a sub-pool of Generic, but instead it is used to host the application in a top-level server pool.

See Also:

["Examples of Action Scripts for Third-Party Applications"](resatt.md) to see an example of an action script

Note:

Oracle recommends that you use shared storage, such as Oracle Automatic Storage Management Cluster File System (Oracle ACFS), to store action scripts to decrease script maintenance.

This section includes the following topics:

- Deciding on a Deployment Scheme
- Adding a Resource to a Specified Server Pool
- Adding a Resource Using a Server-Specific Deployment

#### Deciding on a Deployment Scheme

You must decide whether to use administrator or policy management for the application. Use administrator management for smaller, two-node configurations, where your cluster configuration is not likely to change. Use policy management for more dynamic configurations when your cluster consists of more than two nodes. For example, if a resource only runs on node 1 and node 2 because only those nodes have the necessary files, then administrator management is probably more appropriate.

Oracle Clusterware supports the deployment of applications in access-controlled server pools made up of anonymous servers and strictly based on the desired pool size. Cluster policies defined by the administrator can and must be used in this case to govern the server assignment with desired sizes and levels of importance. Alternatively, a strict or preferred server assignment can be used, in which resources run on specifically named servers. This represents the pre-existing model available in earlier releases of Oracle Clusterware now known as administrator management.

Conceptually, a cluster hosting applications developed and deployed in both of the deployment schemes can be viewed as two logically separated groups of servers. One server group is used for server pools, enabling role separation and server capacity control. The other server group assumes a fixed assignment based on named servers in the cluster.

To manage an application using either deployment scheme, you must create a server pool before adding the resource to the cluster. A built-in server pool named Generic always owns the servers used by applications of administrator-based management. The Generic server pool is a logical division and can be used to separate the two parts of the cluster using different management schemes.

For third party developers to use the model to deploy applications, server pools must be used. To take advantage of the pre-existing application development and deployment model based on named servers, sub-pools of Generic (server pools that have Generic as their parent pool, defined by the server pool attribute `PARENT_POOLS`) must be used. By creating sub-pools that use Generic as their parent and enumerating servers by name in the sub-pool definitions, applications ensure that named servers are in Generic and are used exclusively for applications using the named servers model.

#### Adding a Resource to a Specified Server Pool

To add the Apache Web server to a specific server pool as a resource using the policy-based deployment scheme, run the following command as the user that is supposed to run the Apache Server. For an Apache Server this is typically the `root` user:

```
$ crsctl add resource myApache -type cluster_resource
-attr "ACTION_SCRIPT=/opt/cluster/scripts/myapache.scr, PLACEMENT=restricted,
SERVER_POOLS=server_pool_list,CHECK_INTERVAL=30,RESTART_ATTEMPTS=2,
START_DEPENDENCIES=hard(appsvip),STOP_DEPENDENCIES=hard(appsvip)"
```

See Also:

["Examples of Action Scripts for Third-Party Applications"](resatt.md)

In the preceding example, `myApache` is the name of the resource added to the cluster.

Note:

A resource name cannot begin with a period nor with the character string "ora".

Notice that attribute values are enclosed in single quotation marks (' '). Configure the resource as follows:

- The resource is a `cluster_resource` type.
- `ACTION_SCRIPT=/opt/cluster/scripts/myapache.scr:` The path to the required action script.
- `PLACEMENT=restricted`
	See Also:
	"Application Placement Policies" for more information about the `PLACEMENT` resource attribute
- `SERVER_POOLS=` `server_pool_list`: This resource can only run in the server pools specified in a space-separated list.
- `CHECK_INTERVAL=30`: Oracle Clusterware checks this resource every 30 seconds to determine its status.
- `RESTART_ATTEMPTS=2`: Oracle Clusterware attempts to restart this resource twice before failing it over to another node.
- `START_DEPENDENCIES=hard(appsvip)`: This resource has a hard START dependency on the appsvip resource. The appsvip resource must be online in order for myApache to start.
- `STOP_DEPENDENCIES=hard(appsvip)`: This resource has a hard STOP dependency on the appsvip resource. The myApache resource stops if the appsvip resource goes offline.

#### Adding a Resource Using a Server-Specific Deployment

To add the Apache Web server as a resource that uses a named server deployment, it is assumed that the resource is added to a server pool that is by definition a sub-pool of the Generic server pool. Server pools that represent sub-pools of Generic are created using the `crsctl add serverpool` command. These server pools define the Generic server pool as their parent in the server pool attribute `PARENT_POOLS`. In addition, they include a list of server names in the `SERVER_NAMES` parameter to specify the servers that should be assigned to the respective pool. For example:

```
$ crsctl add serverpool myApache_sp -attr "PARENT_POOLS=Generic, SERVER_NAMES=host36 host37"
```

Once this sub-pool has been created, you can add the resource, as in the previous example:

```
$ crsctl add resource myApache -type cluster_resource
-attr "ACTION_SCRIPT=/opt/cluster/scripts/myapache.scr, PLACEMENT='restricted', 
SERVER_POOLS=myApache_sp, CHECK_INTERVAL='30', RESTART_ATTEMPTS='2', 
START_DEPENDENCIES='hard(appsvip)', STOP_DEPENDENCIES='hard(appsvip)'"
```

Note:

A resource name cannot begin with a period nor with the character string "ora".

In addition, note that when adding a resource using a server-specific deployment, the server pools listed in the `SERVER_POOLS` resource parameter must be sub-pools under Generic.

See Also:

["Policy-Based Cluster and Capacity Management"](admin.md)

### Adding Resources Using Oracle Enterprise Manager

To add resources to Oracle Clusterware using Oracle Enterprise Manager:

1. Log into Oracle Enterprise Manager Database Control.
2. Click the Cluster tab.
3. Click Administration.
4. Click Add Resource.
5. Enter a cluster administrator user name and password to display the Add Resource page.
6. Enter a name for the resource in the Name field.
	Note:
	A resource name cannot begin with a period nor with the character string "ora".
7. Choose either cluster\_resource or local\_resource from the Resource Type drop down.
8. Optionally, enter a description of the resource in the Description field.
9. Select Start the resource after creation if you want the resource to start immediately.
10. The optional parameters in the Placement section define where in a cluster Oracle Clusterware places the resource.
	See Also:
	"Application Placement Policies" for more information about placement
	The attributes in this section correspond to the attributes described in [Appendix B, "Oracle Clusterware Resource Reference"](resatt.md).
11. In the Action Program section, choose from the Action Program drop down whether Oracle Clusterware calls an action script, an agent file, or both to manage the resource.
	You must also specify a path to the script, file, or both, depending on what you select from the drop down.
	If you choose Action Script, then you can click Create New Action Script to use the Oracle Enterprise Manager action script template to create an action script for your resource, if you have not yet done so.
12. To further configure the resource, click Attributes. On this page, you can configure start, stop, and status attributes, and offline monitoring and any attributes that you define.
13. Click Advanced Settings to enable more detailed resource attribute configurations.
14. Click Dependencies to configure start and stop dependencies between resources.
	See Also:
	"Resource Dependencies" for more information about dependencies
15. Click Submit when you finish configuring the resource.

### Changing Resource Permissions

Oracle Clusterware manages resources based on the permissions of the user who added the resource. The user who first added the resource owns the resource and the resource runs as the resource owner. Certain resources must be managed as `root`. If a user other than `root` adds a resource that must be run as `root`, then the permissions must be changed as `root` so that `root` manages the resource, as follows:

1. Change the permission of the named resource to `root` by running the following command as `root`:
	```
	# crsctl setperm resource resource_name –o root
	```
2. As the user who installed Oracle Clusterware, enable the Oracle Database installation owner (`oracle`, in the following example) to run the script, as follows:
	```
	$ crsctl setperm resource resource_name –u user:oracle:r-x
	```
3. Start the resource:
	```
	$ crsctl start resource resource_name
	```

### Application Placement Policies

A resource can be started on any server, subject to the placement policies, the resource start dependencies, and the availability of the action script on that server.

The `PLACEMENT` resource attribute determines how Oracle Clusterware selects a server on which to start a resource and where to relocate the resource after a server failure. The `HOSTING_MEMBERS` and `SERVER_POOLS` attributes determine eligible servers to host a resource and the `PLACEMENT` attribute further refines the placement of resources.

See Also:

[Appendix B, "Oracle Clusterware Resource Reference"](resatt.md) for more information about the `HOSTING_MEMBERS` and `SERVER_POOLS` resource attributes

The value of the `PLACEMENT` resource attribute determines how Oracle Clusterware places resources when they are added to the cluster or when a server fails. Together with either the `HOSTING_MEMBERS` or `SERVER_POOLS` attributes, you can configure how Oracle Clusterware places the resources in a cluster. When the value of the `PLACEMENT` attribute is:

- `balanced`: Oracle Clusterware uses any online server for placement. Less loaded servers are preferred to servers with greater loads. To measure how loaded a server is, Oracle Clusterware uses the `LOAD` resource attribute of the resources that are in an `ONLINE` state on the server. Oracle Clusterware uses the sum total of the `LOAD` values to measure the current server load.
- `favored`: If values are assigned to either the `SERVER_POOLS` or `HOSTING_MEMBERS` resource attribute, then Oracle Clusterware considers servers belonging to the member list in either attribute first. If no servers are available, then Oracle Clusterware places the resource on any other available server. If there are values for both the `SERVER_POOLS` and `HOSTING_MEMBERS` attributes, then the `SERVER_POOLS` attribute restricts the choices to the servers within the preference indicated by the value of `HOSTING_MEMBERS`.
- `restricted`: Oracle Clusterware only considers servers that belong to server pools listed in the `SEVER_POOLS` resource attribute or servers listed in the `HOSTING_MEMBERS` resource attribute for resource placement. Only one of these resource attributes can have a value, otherwise it results in an error.

See Also:

["SERVER\_POOLS"](resatt.md) for more information

### Unregistering Applications and Application Resources

To unregister a resource, use the `crsctl delete resource` command. You cannot unregister an application or resource that is ONLINE or required by another resource, unless you use the `-force` option. The following example unregisters the Apache Web server application:

```
$ crsctl delete resource myApache
```

Run the `crsctl delete resource` command as a clean-up step when a resource is no longer managed by Oracle Clusterware. Oracle recommends that you unregister any unnecessary resources.

## Managing Resources

This section includes the following topics:

- Registering Application Resources
- Starting Application Resources
- Relocating Applications and Application Resources
- Stopping Applications and Application Resources
- Displaying Clusterware Application and Application Resource Status Information

### Registering Application Resources

Each application that you manage with Oracle Clusterware is stored as a resource in OCR. Use the `crsctl add resource` command to register applications in OCR. For example, enter the following command to register the Apache Web server application from the previous example:

```
$ crsctl add resource myApache -type cluster_resource
-attr "ACTION_SCRIPT=/opt/cluster/scripts/myapache.scr, PLACEMENT=restricted,
SERVER_POOLS=server_pool_list,CHECK_INTERVAL=30,RESTART_ATTEMPTS=2,
START_DEPENDENCIES=hard(appsvip),STOP_DEPENDENCIES=hard(appsvip)"
```

If you modify a resource, then update OCR by running the `crsctl modify resource` command.

### Starting Application Resources

Start and stop resources with the `crsctl start resource` and `crsctl stop resource` commands. Manually starting or stopping resources outside of Oracle Clusterware can invalidate the resource status. In addition, Oracle Clusterware may attempt to restart a resource on which you perform a manual stop operation.

To start an application resource that is registered with Oracle Clusterware, use the `crsctl start resource` command. For example:

```
$ crsctl start resource myApache
```

See Also:

[Appendix E, "CRSCTL Utility Reference"](crsref.md) for usage information and examples of CRSCTL command output

The command waits to receive a notification of success or failure from the action program each time the action program is called. Oracle Clusterware can start application resources if they have stopped due to exceeding their failure threshold values. You must register a resource using `crsctl add resource` before you can start it.

Running the `crsctl start resource` command on a resource sets the resource `TARGET` value to `ONLINE`. Oracle Clusterware attempts to change the state to match the `TARGET` by running the action program with the `start` action.

If a cluster server fails while you are starting a resource on that server, then check the state of the resource on the cluster by using the `crsctl status resource` command.

### Relocating Applications and Application Resources

Use the `crsctl relocate resource` command to relocate applications and application resources. For example, to relocate the Apache Web server application to a server named `rac2`, run the following command:

```
# crsctl relocate resource myApache -n rac2
```

Each time that the action program is called, the `crsctl relocate resource` command waits for the duration specified by the value of the `SCRIPT_TIMEOUT` resource attribute to receive notification of success or failure from the action program. A relocation attempt fails if:

- The application has required resources that run on the initial server
- Applications that require the specified resource run on the initial server

To relocate an application and its required resources, use the `-f` option with the `crsctl relocate resource` command. Oracle Clusterware relocates or starts all resources that are required by the application regardless of their state.

### Stopping Applications and Application Resources

Stop application resources with the `crsctl stop resource` command. The command sets the resource `TARGET` value to `OFFLINE`. Because Oracle Clusterware always attempts to match the state of a resource to its target, the Oracle Clusterware subsystem stops the application. The following example stops the Apache Web server:

```
# crsctl stop resource myApache
```

You cannot stop a resource if another resource has a hard stop dependency on it, unless you use the force (`-f`) option. If you use the `crsctl stop resource` `resource_name` `-f` command on a resource upon which other resources depend, and if those resources are running, then Oracle Clusterware stops the resource and all of the resources that depend on the resource that you are stopping.

### Displaying Clusterware Application and Application Resource Status Information

To display status information about applications and resources that are on cluster servers, use the `crsctl status resource` command. The following example displays the status information for the Apache Web server application:

```
# crsctl status resource myApache

NAME=myApache
TYPE=cluster_resource
TARGET=ONLINE
STATE=ONLINE on server010
```

Other information this command returns includes the following:

- How many times the resource has been restarted
- How many times the resource has failed within the failure interval
- The maximum number of times that a resource can restart or fail
- The target state of the resource and the normal status information

Use the `-f` option with the `crsctl status resource` `resource_name` command to view full information of a specific resource.

Enter the following command to view information about all applications and resources in tabular format:

```
# crsctl status resource
```

See Also:

[Appendix E, "CRSCTL Utility Reference"](crsref.md) for detailed information about CRSCTL commands

## Managing Automatic Restart of Oracle Clusterware Resources

You can prevent Oracle Clusterware from automatically restarting a resource by setting several resource attributes. You can also control how Oracle Clusterware manages the restart counters for your resources. In addition, you can customize the timeout values for the `start`, `stop`, and `check` actions that Oracle Clusterware performs on resources.

This section includes the following topics:

- Preventing Automatic Restarts
- Automatically Manage Restart Attempts Counter for Resources

### Preventing Automatic Restarts

When a server restarts, Oracle Clusterware attempts to start the resources that run on the server as soon as the server starts. Resource startup might fail, however, if system components on which a resource depends, such as a volume manager or a file system, are not running. This is especially true if Oracle Clusterware does not manage the system components on which a resource depends. To manage automatic restarts, use the `AUTO_START` resource attribute to specify whether Oracle Clusterware should automatically start a resource when a server restarts.

Note:

Regardless of the value of the `AUTO_START` resource attribute for a resource, the resource can start if another resource has a hard or weak start dependency on it or if the resource has a pullup start dependency on another resource.

See Also:

- "Start Dependencies" for more information
- [Appendix B, "Oracle Clusterware Resource Reference"](resatt.md) for more information about the `AUTO_START` resource attribute

### Automatically Manage Restart Attempts Counter for Resources

When a resource fails, Oracle Clusterware attempts to restart the resource the number of times specified in the `RESTART_ATTEMPTS` resource attribute, regardless of how often the resource fails. The `crsd` process maintains an internal counter to track how often Oracle Clusterware restarts a resource. The number of times Oracle Clusterware has attempted to restart a resource is reflected in the `RESTART_COUNT` resource attribute. Oracle Clusterware can automatically manage the restart attempts counter based on the stability of a resource. The `UPTIME_THRESHOLD` resource attribute determines the time period that a resource must remain online, after which the `RESTART_COUNT` attribute gets reset to 0. In addition, the `RESTART_COUNT` resource attribute gets reset to 0 if the resource is relocated or restarted by the user, or the resource fails over to another server.