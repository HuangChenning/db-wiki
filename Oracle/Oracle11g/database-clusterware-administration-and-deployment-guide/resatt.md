---
title: Oracle Clusterware Resource Reference
book: Database Clusterware Administration and Deployment Guide
doc_id: E41959-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/rac.112/e41959/resatt.htm
tags:
  - oracle
  - 11g
  - database-clusterware-administration-and-deployment-guide
---

## B Oracle Clusterware Resource Reference

This appendix is a reference for Oracle Clusterware resources. It includes descriptions and usage examples of all resource attributes and a detailed description and examples of action scripts.

This appendix includes the following topics:

- Resource Attributes
- Examples of Action Scripts for Third-Party Applications

## Resource Attributes

This section lists and describes attributes used when you register applications as resources in Oracle Clusterware. Use these attributes with the `crsctl add resource` command, as follows:

```
$ crsctl add resource resource_name -type resource_type
{[-attr "attribute_name='attribute_value', attribute_name='attribute_value'
, ..."] | [-file file_name]}
```

List attribute-value pairs in a comma-delimited list after the `-attr` flag and enclose the value of each attribute in single quotation marks (`''`). Some resource attributes you cannot configure and are read only.

Alternatively, you can create a text file that contains the attribute-value pairs. For example:

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

This section includes the following topics:

- Configurable Resource Attributes
- Read-Only Resource Attributes

### Configurable Resource Attributes

This section describes the following resource attributes that you can configure when registering an application as a resource in Oracle Clusterware:

Note:

Values for all attributes must be in lowercase. Attribute names must be in all uppercase letters.

#### ACL

Defines the owner of a resource and the access privileges granted to various operating system users and groups. The resource owner defines the operating system user of the owner and its privileges. You configure this optional attribute when you create a resource. If you do not configure this attribute, then the value is based on the identity of the process creating the resource. You can change the value of the attribute if such a change is allowed based on the existing privileges of the resource.

Note:

All operating system user names and user groups, including `owner`, `pgrp`, `user`, and `group`, must be registered on all servers in the cluster.

In the string:

- `owner`: The operating system user that owns a resource and the user under which the action script or application-specific agent runs, followed by the privileges of the owner.
- `pgrp`: The operating system group that is the primary group of the owner of a resource, followed by the privileges of members of the primary group.
- `other`: Operating system users that are neither the owner nor member of the primary group
- `r`: The read option, which gives the ability to only see a resource, its state, and configuration
- `w`: The write option, which gives the ability to modify a resource's attributes and to delete the resource
- `x`: The execute option, which gives the ability to start, stop, and relocate a resource

By default, the identity of the client that creates a resource is the `owner`. Also by default, `root`, and the user specified in `owner` have full privileges. You can grant required operating system users and operating system groups their privileges by adding the following lines to the `ACL` attribute:

```
user:user_name:rwx
group:group_name:rwx
```

Usage Example

```
ACL=owner:user_1:rwx,pgrp:osdba:rwx,other::r-
```

In the preceding example, the owner of the resource is `user_1`, whose primary group is `osdba`. The user, `user_1`, has all privileges, as does the `osdba` group, while other users can only view the resource.

#### ACTION\_SCRIPT

An absolute file name that includes the path and file name of an action script. The agent specified in the `AGENT_FILENAME` attribute calls the script specified in the `ACTION_SCRIPT` attribute.

Usage Example

```
ACTION_SCRIPT=fully_qualified_path_to_action_script
```

#### ACTIVE\_PLACEMENT

When set to `1`, Oracle Clusterware uses this attribute to reevaluate the placement of a resource during addition or restart of a cluster server. For resources where `PLACEMENT=favored`, Oracle Clusterware may relocate running resources if the resources run on a non-favored server when a favored one joins the cluster.

Usage Example

```
ACTIVE_PLACEMENT=1
```

#### AGENT\_FILENAME

A fully qualified file name of an agent program that a resource type uses to manage its resources. Every resource type must have an agent program to manage its resources. Resource types use agent programs by either specifying a value for this attribute or inheriting it from their base resource type. There are two script agents included with Oracle Clusterware 11g release 2 (11.2): `application` and `scriptagent`. Oracle Clusterware uses the `application` script agent for resources of the deprecated `application` resource type. The default value for this attribute is `scriptagent`.

Usage Example

```
AGENT_FILENAME=%Grid_home%/bin/application
```

#### AUTO\_START

Indicates whether Oracle Clusterware automatically starts a resource after a cluster server restart. Valid `AUTO_START` values are:

- `always`: Restarts the resource when the server restarts regardless of the state of the resource when the server stopped.
- `restore`: Restores the resource to the same state that it was in when the server stopped. Oracle Clusterware attempts to restart the resource if the value of `TARGET` was `ONLINE` before the server stopped.
- `never`: Oracle Clusterware never restarts the resource regardless of the state of the resource when the server stopped.

#### CARDINALITY

The number of servers on which a resource can run, simultaneously. This is the upper limit for resource cardinality.

Usage Example

```
CARDINALITY=1
```

#### CHECK\_INTERVAL

The time interval, in seconds, between repeated executions of the `check` action. Shorter intervals enable more frequent checks but also increase resource consumption if you use the script agent. Use an application-specific agent to reduce resource consumption.

Usage Example

```
CHECK_INTERVAL=60
```

#### DEGREE

The number of instances of a cluster resource that can run on a single server.

Usage Example

```
DEGREE=1
```

#### DESCRIPTION

Enter a description of the resource you are adding.

Usage Example

```
DESCRIPTION=Apache Web server
```

#### ENABLED

Oracle Clusterware uses this attribute to manage the state of the resource. Oracle Clusterware does not attempt to manage a disabled (`ENABLED=0`) resource either directly or because of a dependency to another resource. A disabled resource cannot be started but it can be stopped.

Oracle Clusterware does not actively monitor disabled resources, meaning that Oracle Clusterware does not check their state. However, when Oracle Clusterware starts, it does query the state of disabled resources.

Usage Example

```
ENABLED=1
```

#### FAILURE\_INTERVAL

The interval, in seconds, before which Oracle Clusterware stops a resource if the resource has exceeded the number of failures specified by the `FAILURE_THRESHOLD` attribute. If the value is zero (`0`), then tracking of failures is disabled.

Usage Example

```
FAILURE_INTERVAL=30
```

#### FAILURE\_THRESHOLD

The number of failures of a resource detected within a specified `FAILURE_INTERVAL` for the resource before Oracle Clusterware marks the resource as unavailable and no longer monitors it. If a resource fails the specified number of times, then Oracle Clusterware stops the resource. If the value is zero (`0`), then tracking of failures is disabled. The maximum value is `20`.

Usage Example

```
FAILURE_THRESHOLD=3
```

#### HOSTING\_MEMBERS

A space-separated, ordered list of cluster server names that can host a resource. This attribute is required only when using administrator management, and when the value of the `PLACEMENT` attribute is set to `favored` or `restricted`. When registering applications as Oracle Clusterware resources, use the `SERVER_POOLS` attribute, instead.

Note:

For resources of `application` type, Oracle Clusterware places servers listed in the `HOSTING_MEMBERS` attribute in the Generic server pool.

See Also:

- ["Understanding Server Pools"](admin.md) for more information about the Generic server pool
- "LOAD" for more information about this attribute
- "PLACEMENT" for more information about this attribute

To obtain a list of candidate node names, run the `olsnodes` command to display a list of your server names.

Usage Example

```
HOSTING_MEMBERS=server1 server2 server3
```

#### LOAD

Oracle Clusterware interprets the value of this attribute along with that of the `PLACEMENT` attribute. When the value of `PLACEMENT` is `balanced`, the value of `LOAD` determines where best to place a resource. A nonnegative, numeric value that quantitatively represents how much server capacity an instance of a resource consumes relative to other resources. Oracle Clusterware attempts to place resources on servers with the least total load of running resources.

Usage Example

```
LOAD=1
```

#### NAME

A case-sensitive alphanumeric string that names the resource. Oracle recommends a naming convention that starts with an alphanumeric prefix, such as `myApache`, and complete the name with an identifier to describe it. A resource name can contain any platform-supported characters except the exclamation point (!) and the tilde (~). A resource name cannot begin with a period (.) nor with the string ora.

Usage Example

```
NAME=myApache
```

#### OFFLINE\_CHECK\_INTERVAL

Controls offline monitoring of a resource. The value represents the interval (in seconds) that Oracle Clusterware monitors a resource when its state is `OFFLINE`. Monitoring is disabled if the value is `0`.

Usage Example

```
OFFLINE_CHECK_INTERVAL=30
```

#### PLACEMENT

Specifies how Oracle Clusterware selects a cluster server on which to start a resource. Valid values are `balanced`, `favored`, or `restricted`.

If you set the `PLACEMENT` attribute to `favored` or `restricted`, then you must also assign values to the `SERVER_POOLS` and `HOSTING_MEMBERS` attributes. If you set the value of the `PLACEMENT` attribute to `balanced`, then the `HOSTING_MEMBERS` attribute is not required.

See Also:

- ["Application Placement Policies"](crschp.md) for more information about the `PLACEMENT` attribute
- "HOSTING\_MEMBERS" for more information about this attribute
- "SERVER\_POOLS" for more information about this attribute

Usage Example

```
PLACEMENT=favored
```

#### RESTART\_ATTEMPTS

The number of times that Oracle Clusterware attempts to restart a resource on the resource's current server before attempting to relocate it. A value of `1` indicates that Oracle Clusterware only attempts to restart the resource once on a server. A second failure causes Oracle Clusterware to attempt to relocate the resource. A value of `0` indicates that there is no attempt to restart but Oracle Clusterware always tries to fail the resource over to another server.

Usage Example

```
RESTART_ATTEMPTS=2
```

#### SCRIPT\_TIMEOUT

The maximum time (in seconds) for an action to run. Oracle Clusterware returns an error message if the action script does not complete within the time specified. The timeout applies to all actions (`start`, `stop`, `check`, and `clean`).

Usage Example

```
SCRIPT_TIMEOUT=45
```

#### SERVER\_POOLS

A space-separated list of the server pools to which a particular resource can belong. If a resource can run on any server in a cluster, then use the default value, `*`, unless the resource is a `cluster_resource` type, in which case, the default value for the `SERVER_POOLS` attribute is empty. Only cluster administrators can specify `*` as the value for this attribute.

- Use the `PLACEMENT` attribute with the `SERVER_POOLS` attribute, as follows: If you set the value of the `PLACEMENT` attribute to either `restricted` or `favored`, then you must also provide a value for the `SERVER_POOLS` attribute when using policy management for the resource.
- If the value for `PLACEMENT` is set to `balanced`, then the resource only runs in the Generic and Free pools, unless `SERVER_POOLS=*`.

This attribute creates an affinity between a resource and one or more server pools regarding placement, and is dependent on the value of the `PLACEMENT` attribute.

See Also:

- ["Understanding Server Pools"](admin.md) for more information about server pools and ["Role-Separated Management"](admin.md) for more information about cluster administrators
- "HOSTING\_MEMBERS" for more information about this attribute
- "PLACEMENT" for more information about this attribute

Usage Example

```
SERVER_POOLS=pool1 pool2 pool3
```

#### START\_DEPENDENCIES

Specifies a set of relationships that Oracle Clusterware considers when starting a resource. You can specify a space-separated list of dependencies on several resources and resource types on which a particular resource can depend.

Syntax

```
START_DEPENDENCIES=dependency(resource_set) [dependency(resource_set)] [...]
```

In the preceding syntax example the variables are defined, as follows:

- `dependency`: Possible values are `hard`, `weak`, `attraction`, `pullup`, and `dispersion`. You can specify each dependency only once, except for `pullup`, which you can specify multiple times.
- `resource_set`: A comma-delimited list of resource entities—either individual resources or resource types—enclosed in parentheses `()`, in the form of `res1[, res2[, ...]]`, upon which the resource you are configuring depends.
	Each resource entity is defined, as follows:
	```
	[modifier1:[modifier2:]] {resource_name | type:resource_type}
	```
	In the preceding syntax example, `resource_name` is the name of a specific resource and `type:``resource_type` is the name of a specific resource type. The resource type must be preceded by `type` and the `type` modifier must be the last resource entity in the list.
	Optionally, you can specify modifiers to further configure resource entity dependencies. You can modify each dependency by prefixing the following modifiers to the resource entity:
	- `hard([intermediate:][global:]{` `resource_name` `|` `type:``resource_type` `})` —Specify a `hard` start dependency for a resource when you want the resource to start only when a particular resource or resource of a particular type starts.
		Use `intermediate` to specify that Oracle Clusterware can start this resource if a resource on which it depends is in either the `ONLINE` or `INTERMEDIATE` state. If not specified, then resources must be in the `ONLINE` state for Oracle Clusterware to start this resource.
		Use `global` to specify that resources are not required to reside on the same server as a condition to Oracle Clusterware starting this resource. If not specified, then resources must reside on the same server for Oracle Clusterware to start this resource.
		If you specify the `hard` dependency on a resource type for a resource, then the resource can start if any resource of that particular type is running.
		Note:
		Oracle recommends that resources with `hard` start dependencies also have `pullup` start dependencies.
		- `weak([concurrent:][global:][uniform:]{` `resource_name` `|` `type:``resource_type` `})` —Specify a `weak` start dependency for a resource when you want that resource to start despite whether named resources are running, or not. An attempt to start this resource also attempts to start any resources on which this resource depends if they are not running.
		Use `concurrent` to specify that Oracle Clusterware can start a dependent resource while a resource on which it depends is in the process of starting. If `concurrent` is not specified, then resources must complete startup before Oracle Clusterware can start the dependent resource.
		Use `global` to specify that resources are not required to reside on the same server as a condition to Oracle Clusterware starting the dependent resource.
		Use `uniform` to start all instances of the resource everywhere the resource can run. If you do not specify a modifier (the default), then the resource starts on the same server as the resource on which it depends.
		If you specify the `weak` start dependency on a resource type for a resource, then the resource can start if any resource of that particular type is running.
		- `attraction([intermediate:]{` `resource_name` `|` `type:``resource_type` `})` —Use the `attraction` start dependency when you want this resource to run on the same server with a particular named resource or any resource of a particular type.
		Use `intermediate` to specify that this resource is attracted to resource entities on which it depends that are in the `INTERMEDIATE` state. If not specified, then resources must be in the `ONLINE` state to attract the dependent resource.
		If you specify the `attraction` dependency on a resource type for a resource, then any resource of that particular type attracts the dependent resource.
		- `pullup[:always]([intermediate:][global:]{` `resource_name` `|` `type:``resource_type` `})` —When you specify the `pullup` start dependency for a resource, then this resource starts as a result of named resources starting.
		Use the `always` modifier for `pullup` so that Oracle Clusterware starts this resource despite the value of its `TARGET` attribute, whether that value is `ONLINE` or `OFFLINE`. Otherwise, if you do not specify the `always` modifier, then Oracle Clusterware starts this resource only if the value of the `TARGET` attribute is `ONLINE` for this resource.
		Use `intermediate` to specify that Oracle Clusterware can start this resource if a resource on which it depends is in either the `ONLINE` or `INTERMEDIATE` state. If not specified, then resources must be in the `ONLINE` state for Oracle Clusterware to start this resource.
		Use `global` to specify that resources on which this resource depends are not required to reside on the same server as a condition to Oracle Clusterware starting this resource. If not specified, then resources on which this resource depends must reside on the same server for Oracle Clusterware to start this resource.
		If you specify the `pullup` dependency on a resource type for a resource, then, when any resource of that particular type starts, Oracle Clusterware can start this resource.
		Note:
		Oracle recommends that resources with `hard` start dependencies also have `pullup` start dependencies.
		- `dispersion[:active]([intermediate:]{` `resource_name` `|` `type:``resource_type` `})` —Specify the `dispersion` start dependency for a resource that you want to run on a server that is different from the named resources or resources of a particular type. Resources may still end up running on the same server, depending on availability of servers.
		Use the `active` modifier to configure the `dispersion` dependency so that Oracle Clusterware attempts to relocate the dependent resource to another server if it is co-located with another resource and another server comes online. Oracle Clusterware does not relocate resources to newly available servers unless you specify the `active` modifier.
		Use `intermediate` to specify that Oracle Clusterware can relocate the dependent resource if a resource is in either the `ONLINE` or `INTERMEDIATE` state. If not specified, then resources must be in the `ONLINE` state for dispersion of the dependent resource to occur.

See Also:

["Start Dependencies"](crschp.md) for more details about start dependencies

#### START\_TIMEOUT

The maximum time (in seconds) in which a start action can run. Oracle Clusterware returns an error message if the action does not complete within the time specified. If you do not specify a value for this attribute or you specify `0` seconds, then Oracle Clusterware uses the value of the `SCRIPT_TIMEOUT` attribute.

Usage Example

```
START_TIMEOUT=30
```

See Also:

"SCRIPT\_TIMEOUT" for more information about this attribute

#### STOP\_DEPENDENCIES

Specifies a set of relationships that Oracle Clusterware considers when stopping a resource.

Syntax

```
STOP_DEPENDENCIES=dependency(resource_set) [dependency(resource_set)] ...
```

In the preceding syntax example the variables are defined, as follows:

- `dependency`: The only possible value is `hard`.
- `resource_set`: A comma-delimited list, in the form of `res1[, res2 [,...]]`, of resource entities—either individual resources or resource types—upon which the resource you are configuring depends.
	Each resource entity is defined, as follows:
	```
	[modifier1:[modifier2:][modifier3:]] resource_name | type:resource_type
	```
	In the preceding syntax example, `resource_name` is the name of a specific resource and `type:``resource_type` is the name of a specific resource type. The resource type must be preceded by `type:`.
	Optionally, you can specify modifiers to further configure resource entity dependencies. You can modify each dependency by prefixing the following modifiers to the resource entity:
	`hard([intermediate:][global:][shutdown:]{` `resource_name` `|` `type:``resource_type` `})` —Specify a `hard` stop dependency for a resource that you want to stop when named resources or resources of a particular resource type stop.
	Use `intermediate` to specify that the dependent resource can remain in an `ONLINE` state if a resource is in either the `ONLINE` or `INTERMEDIATE` state. If not specified, then Oracle Clusterware stops the dependent resource unless resources are in the `ONLINE` state.
	Use `global` to specify that the dependent resource remains in an `ONLINE` state if a resource is in an `ONLINE` state on any node in the cluster. If not specified, then when resources residing on the same server go offline, Oracle Clusterware stops the dependent resource.
	Use `shutdown` to apply this dependency when the Oracle Clusterware stack is shut down. This is a convenient way to affect the order of stopping resources when stopping the stack, without having any affect on planned or unplanned events on the individual resources. This dependency, when used with the `shutdown` modifier, does not go into effect if somebody stops the resource directly, but only when the stack is shut down.

See Also:

["Stop Dependencies"](crschp.md) for more details about stop dependencies

#### STOP\_TIMEOUT

The maximum time (in seconds) in which a `stop` or `clean` action can run. Oracle Clusterware returns an error message if the action does not complete within the time specified. If you do not specify this attribute or if you specify `0` seconds, then Oracle Clusterware uses the value of the `SCRIPT_TIMEOUT` attribute.

Usage Example

```
STOP_TIMEOUT=30
```

See Also:

- "SCRIPT\_TIMEOUT" for more information about this attribute
- "START\_TIMEOUT" for more information about this attribute

#### TYPE

The type of resource indicated when you create a resource. This attribute is required when creating a resource.

Usage Example

See Also:

["Resource Types"](crschp.md) for details of resource types

#### UPTIME\_THRESHOLD

The value for `UPTIME_THRESHOLD` represents the length of time that a resource must be up before Oracle Clusterware considers the resource to be stable. By setting a value for the `UPTIME_THRESHOLD` attribute, you can indicate the stability of a resource.

Enter values for this attribute as a number followed by a letter that represents seconds (s), minutes (m), hours (h), days (d), or weeks (w). For example, a value of `7h` represents an uptime threshold of seven hours.

After the time period you specify for `UPTIME_THRESHOLD` elapses, Oracle Clusterware resets the value for `RESTART_COUNT` to `0` at the next resource state change event, such as stop, start, relocate, or failure. Oracle Clusterware can alert you when the value for `RESTART_COUNT` reaches the value that you set for `RESTART_ATTEMPTS`. The counter is effectively reset the next time the resource fails or restarts. The threshold represents the amount of time that restarts are to be counted and discarded. If the resource fails after the threshold, it will still restart.

Note:

Oracle Clusterware writes an alert to the clusterware alert log file when the value for `RESTART_COUNT` reaches the value that you set for `RESTART_ATTEMPTS`.

See Also:

- "RESTART\_ATTEMPTS" for more information about this attribute
- "RESTART\_COUNT" for more information about this attribute

### Read-Only Resource Attributes

You can view these attributes when you run the `crsctl status resource` command on a particular resource. Oracle Clusterware sets these attributes when you register resources.

- ACTION\_FAILURE\_EVENT\_TEMPLATE
- INTERNAL\_STATE
- LAST\_SERVER
- LAST\_STATE\_CHANGE
- PROFILE\_CHANGE\_EVENT\_TEMPLATE
- RESTART\_COUNT
- STATE
- STATE\_CHANGE\_EVENT\_TEMPLATE
- STATE\_DETAILS
- TARGET

#### ACTION\_FAILURE\_EVENT\_TEMPLATE

This is an internally-managed attribute for an `ora.*` resource. You cannot edit this attribute.

#### INTERNAL\_STATE

An internally managed, read-only attribute that describes what, if any, action the policy engine is currently executing on the resource. Possible values and their meanings are as follows:

- `STARTING`: The policy engine is currently starting the resource
- `STOPPING`: The policy engine is currently stopping the resource
- `CLEANING`: The policy engine is currently cleaning the resource
- `STABLE`: The policy engine is not currently executing any action on the resource
	Note, however, that the resource can still be locked as part of some other command.

#### LAST\_SERVER

For `cluster_resource` -type resources, this is an internally managed, read-only attribute that contains the name of the server on which the last `start` action for the resource succeeded.

For `local_resource` -type resources, this is the name of the server to which the resource instance is pinned.

#### LAST\_STATE\_CHANGE

An internally managed, read-only attribute that describes when the policy engine registers the current state of the resource. Note that this may either be the timestamp of when state of the resource changed or when the policy engine discovered the state, as occurs when `crsd` restarts.

#### PROFILE\_CHANGE\_EVENT\_TEMPLATE

This is an internally-managed attribute for an `ora.*` resource. You cannot edit this attribute.

#### RESTART\_COUNT

An internally-managed attribute used by the Oracle Clusterware daemon to count the number of attempts to restart a resource, starting from zero up to the value specified in the `RESTART_ATTEMPTS` attribute. You cannot edit this attribute.

#### STATE

An internally-managed attribute that reflects the current state of the resource as reported by Oracle Clusterware. The state of a resource can be one of the following:

- `ONLINE`: The resource is online and resource monitoring is enabled (see `CHECK_INTERVAL`).
- `OFFLINE`: The resource is offline and only offline resource monitoring is enabled, if configured (see `OFFLINE_CHECK_INTERVAL`).
- `INTERMEDIATE`: The resource is either partially online or was known to be online before and subsequent attempts to determine its state have failed; resource monitoring is enabled (see `CHECK_INTERVAL`).
- `UNKNOWN`: The resource is unmanageable and its current state is unknown; manual intervention is required to resume its operation. A resource in this state is not monitored.

#### STATE\_CHANGE\_EVENT\_TEMPLATE

This is an internally-managed attribute for an `ora.*` resource. You cannot edit this attribute.

#### STATE\_DETAILS

An internally managed, read-only attribute that contains details about the state of a resource.

The four resource states— `ONLINE`, `OFFLINE`, `UNKNOWN`, and `INTERMEDIATE` —may map to different resource-specific values, such as mounted, unmounted, and open. Resource agent developers can use the `STATE_DETAILS` attribute to provide a more detailed description of this mapping, resource to the resource state.

Providing details is optional. If details are not provided, then Oracle Clusterware uses only the four possible resource states. Additionally, if the agent cannot provide these details (as may also happen to the value of the resource state), then Oracle Clusterware sets the value of this attribute to provide minimal details about why the resource is in its current state.

#### TARGET

An internal, read-only attribute that describes the desired state of a resource. Using the `crsctl start` `resource_name` or `crsctl stop` `resource_name` commands, however, can affect the value of this attribute.

## Examples of Action Scripts for Third-Party Applications

This section includes examples of third-party applications using script agents.

Example B-1 shows an action script that fails over the Apache Web server.

Example B-1 Apache Action Script

```
#!/bin/sh

HTTPDCONFLOCATION=/etc/httpd/conf/httpd.conf
WEBPAGECHECK=http://<MyVIP>:80/icons/apache_pb.gif

case $1 in
'start')
    /usr/sbin/apachectl -k start -f $HTTPDCONFLOCATION
   RET=$?
    ;;
sleep(10)
    ;;
'stop')
    /usr/sbin/apachectl -k stop
   RET=$?
    ;;
'clean')
    /usr/sbin/apachectl -k stop
   RET=$?
    ;;
'check')
    /usr/bin/wget -q --delete-after $WEBPAGECHECK
   RET=$?
    ;;
*)
   RET=0
    ;;
esac
# 0: success; 1 : error
if [ $RET -eq 0 ]; then
exit 0
else
exit 1
fi
```

Example B-2 shows the xclock script, which is a simple action script using `xclock` available as a default binary on all Linux and UNIX platforms.

Example B-2 xclock Action Script

```
#!/bin/bash
# start/stop/check script for xclock example
# To test this change BIN_DIR to the directory where xclock is based
# and set the DISPLAY variable to a server within your network.

BIN_DIR=/usr/X11R6/bin
LOG_DIR=/tmp
BIN_NAME=xclock
DISPLAY=yourhost.domain.com:0.0
export DISPLAY
exit_code=0

if [ ! -d $BIN_DIR ]
then
        echo "start failed"
        exit 2
fi

PID1=\`ps -ef | grep $BIN_NAME | grep -v grep | grep -v xclock_app | awk '{ print $2 }'\`
case $1 in
'start')
        if [ "$PID1" != "" ]
        then
           status_p1="running"
        else
           if [ -x $BIN_DIR/$BIN_NAME ]
           then
             umask 002
             ${BIN_DIR}/${BIN_NAME} & 2>${LOG_DIR}/${BIN_NAME}.log
             status_p1="started"
           else
             echo \`basename $0\`": $BIN_NAME: Executable not found"
             exit_code=1
           fi
        fi

         echo "$BIN_NAME: $status_p1"
         exit $exit_code
        ;;

'stop')
        if [ "${PID1}" != "" ]
        then
           kill -9 ${PID1} && echo "$BIN_NAME daemon killed"
        else
           echo "$BIN_NAME: no running Process!"
        fi
        exit $exit_code
        ;;
'check')
        if [ "$PID1" != "" ]
        then
           echo "running"
           exit 0
        else
           echo "not running"
           exit 1
        fi
        ;;*)
        echo "Usage: "\`basename $0\`" {start|stop|check}"
        ;;
esac
```

Example B-3 shows an example of a shell script for an agent to monitor a file. When the agent is started, it creates the file (which is specified through an attribute) and when it is stopped, it deletes the file. The CHECK action consists of merely checking if the file exists or not. The variables with the `_CRS_` prefix are attribute values that are provided to the script in its environment.

Example B-3 Action Script Example

```
#!/bin/sh
TOUCH=/bin/touch
RM=/bin/rm
PATH_NAME=/tmp/$_CRS_NAME

#
# These messages go into the CRSD agent log file.
echo " *******   \`date\` ********** "
echo "Action script '$_CRS_ACTION_SCRIPT' for resource[$_CRS_NAME] called for action $1"
#

case "$1" in
  'start')
     echo "START entry point has been called.."
     echo "Creating the file: $PATH_NAME"
     $TOUCH $PATH_NAME
     exit 0
     ;;

  'stop')
     echo "STOP entry point has been called.." 
     echo "Deleting the file: $PATH_NAME"
     $RM $PATH_NAME
     exit 0
     ;;

  'check')
    echo "CHECK entry point has been called.."
    if [ -e $PATH_NAME ]; then
        echo "Check -- SUCCESS"
        exit 0
    else
        echo "Check -- FAILED"
        exit 1
    fi
    ;;

  'clean')
     echo "CLEAN entry point has been called.."
     echo "Deleting the file: $PATH_NAME"
     $RM -f $PATH_NAME
     exit 0
     ;;

esac
```