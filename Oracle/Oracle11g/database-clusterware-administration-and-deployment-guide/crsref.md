---
title: CRSCTL Utility Reference
book: Database Clusterware Administration and Deployment Guide
doc_id: E41959-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/rac.112/e41959/crsref.htm
tags:
  - oracle
  - 11g
  - database-clusterware-administration-and-deployment-guide
---

## E CRSCTL Utility Reference

This appendix describes how to administer Oracle Clusterware using the Oracle Clusterware Control (CRSCTL) utility.

Note:

Do not use CRSCTL commands on Oracle entities (such as resources, resource types, and server pools) that have names beginning with ora unless you are directed to do so by My Oracle Support. The Server Control utility (SRVCTL) is the correct utility to use on Oracle entities.

This appendix includes the following topics:

## CRSCTL Overview

CRSCTL is an interface between you and Oracle Clusterware, parsing and calling Oracle Clusterware APIs for Oracle Clusterware objects.

Oracle Clusterware 11g release 2 (11.2) introduces cluster-aware commands with which you can perform check, start, and stop operations on the cluster. You can run these commands from any node in the cluster on another node in the cluster, or on all nodes in the cluster, depending on the operation.

You can use CRSCTL commands to perform several operations on Oracle Clusterware, such as:

- Starting and stopping Oracle Clusterware resources
- Enabling and disabling Oracle Clusterware daemons
- Checking the health of the cluster
- Managing resources that represent third-party applications
- Integrating Intelligent Platform Management Interface (IPMI) with Oracle Clusterware to provide failure isolation support and to ensure cluster integrity
- Debugging Oracle Clusterware components

### Clusterized (Cluster Aware) Commands

You can run clusterized commands on one node to perform operations on another node in the cluster. These are referred to as remote operations. This simplifies administration because, for example, you no longer have to log in to each node to check the status of the Oracle Clusterware on all of your nodes.

Clusterized commands are completely operating system independent; they rely on the OHASD (Oracle High Availability Services daemon). If this daemon is running, then you can perform remote operations, such as the starting, stopping, and checking the status of remote nodes.

Clusterized commands include the following:

- `crsctl check cluster`
- `crsctl start cluster`
- `crsctl stop cluster`

### Operational Notes

Usage Information

- The CRSCTL utility is located in the `Grid_home/bin` directory. To run CRSCTL commands, type in `crsctl` at the operating system prompt followed by the command and arguments, as shown in the following example:
	```
	crsctl stop crs
	```
- There are three categories of CRSCTL commands:
	- Those that you use in either the Oracle Real Application Clusters (Oracle RAC) environment or in the Oracle Restart environment
		- Those that you use in the Oracle RAC environment, only
		- Those that you use in the Oracle Restart environment, only
- Many CRSCTL commands use the `-f` option to force the command to run and ignore any checks.
	For example, if you specify the force option for the `crsctl stop resource` command on a resource that is running and has dependent resources that are also running, then the force option omits the error message and instead stops or relocates all the dependent resources before stopping the resource you reference in the command.
- Do not use versions of CRSCTL earlier than 11g release 2 (11.2) to manage Oracle Clusterware 11g release 2 (11.2).

Using CRSCTL Help

To print the help information for CRSCTL, use the following command:

```
crsctl -help
```

If you want help for a specific command, such as `start`, then enter the command and append `-help` to the end, as shown in the following example:

```
crsctl start -help
```

You can also use the abbreviations `-h` or `-?` (this option functions in Linux, UNIX, and Windows environments) instead of `-help`.

### Deprecated Subprograms or Commands

Table E-1 lists the commands that are deprecated in Oracle Clusterware 11g release 2 (11.2) and their replacements that you can use to perform the same or similar functionality. These commands are not supported in an Oracle Restart environment:

Table E-1 Deprecated CRSCTL Commands and Replacements

| Deprecated Command | Replacement Commands |
| --- | --- |
| `crs_stat` | `crsctl check cluster -all`  `crsctl stat res -t` |
| `crs_register` | `crsctl add resource`  `crsctl add type`  `crsctl modify resource`  `crsctl modify type` |
| `crs_unregister` | `crsctl stop resource`  `crsctl modify resource` `resource_name` `-attr "AUTO_START=never"` |
| `crs_start` | `crsctl start resource`  `crsctl start crs`  `crsctl start cluster` |
| `crs_stop` | `crsctl stop resource`  `crsctl stop crs`  `crsctl stop cluster` |
| `crs_getperm` | `crsctl getperm resource`  `crsctl getperm type` |
| `crs_profile` | `crsctl add resource`  `crsctl add type`  `crsctl status resource`  `crsctl status type`  `crsctl modify resource`  `crsctl modify type` |
| `crs_relocate` | `crsctl relocate resource` |
| `crs_setperm` | `crsctl setperm resource`  `crsctl setperm type` |
| `crsctl check crsd` | `crsctl check crs` |
| `crsctl check cssd` | `crsctl check css` |
| `crsctl check evmd` | `crsctl check evm` |
| `crsctl debug res log` `resource_name``:``level` | `crsctl set log` |
| `crsctl set css votedisk` | `crsctl add css votedisk`  `crsctl delete css votedisk`  `crsctl query css votedisk`  `crsctl replace votedisk` |
| `crsctl start resources` | `crsctl start resource -all` |
| `crsctl stop resources` | `crsctl stop resource -all` |

## CRSCTL Command Reference

This section is separated into three categories of CRSCTL commands:

- Dual Environment CRSCTL Commands
- Oracle RAC Environment CRSCTL Commands
- Oracle Restart Environment CRSCTL Commands

### Dual Environment CRSCTL Commands

You can use the following commands in either the Oracle RAC or the Oracle Restart environments:

- `crsctl add resource`
- `crsctl add type`
- `crsctl check css`
- `crsctl check evm`
- `crsctl delete resource`
- `crsctl delete type`
- `crsctl get hostname`
- `crsctl getperm resource`
- `crsctl getperm type`
- `crsctl modify resource`
- `crsctl modify type`
- `crsctl setperm resource`
- `crsctl setperm type`
- `crsctl start resource`
- `crsctl status resource`
- `crsctl status type`
- `crsctl stop resource`

#### crsctl add resource

Use the `crsctl add resource` command to register a resource to be managed by Oracle Clusterware. A resource could be an application process, a database, a service, a listener, and so on.

Syntax

```
crsctl add resource resource_name -type resource_type [-file file_path |
-attr "attribute_name=attribute_value,attribute_name=attribute_value,..."]
[-i] [-f]
```

Parameters

Table E-2 crsctl add resource Command Parameters

| Parameter | Description |
| --- | --- |
| ``` resource_name ``` | A short, descriptive name for the resource. |
| ``` -type resource_type ``` | The type of resource that you are adding preceded by the `-type` flag. |
| ``` -file file_path ``` | Path name (either absolute or relative) for a text file containing line-separated attribute name-value pairs that define the resource. |
| ``` -attr "attribute_name= attribute_value ``` | You can specify attributes for a resource you are adding in two different ways:  - Following the `-attr` flag, you can specify one or more comma-delimited attribute name-value pairs enclosed in double quotations marks (`""`). For example: 	``` 	-attr "CHECK_INTERVAL=30,START_TIMEOUT=25" 	``` - Additionally, you can specify attribute values for resource instances with a particular cardinality value, and with a particular degree value. This method can be useful for applications that are tied to a particular server. Following the `-attr` flag, the syntax is as follows: 	``` 	attribute_name{@SERVERNAME(server_name) 	[@DEGREEID(did)] \| @CARDINALITYID(cid) 	[@DEGREEID(did)]}=attribute_value 	``` 	If you specify the `@SERVERNAME(``server_name``)` syntax, then the attribute value you specify for the attribute you specify is limited to resource instances residing on the server you specify. 	Alternatively, if you specify the `@CARDINALITYID(``cid``)` syntax, then the attribute value you specify for the attribute you specify is limited to resource instances with a specific cardinality ID (`cid`). 	Optionally, you can combine the `@DEGREEID(``did``)` syntax with either the `SERVERNAME` or `CARDINALITYID` syntax, or both, to limit the attribute value to resources with the specific `DEGREE`. 	Examples: 	``` 	CHECK_INTERVAL@SERVERNAME(node1)=45 	STOP_TIMEOUT@CARDINALITYID(2)=65 	STOP_TIMEOUT@SERVERNAME(node1)@DEGREEID(2)=65 	STOP_TIMEOUT@CARDINALITYID(3)@DEGREEID(2)=65 	``` |
| ``` -i ``` | If you specify `-i`, then the command returns an error if processing this command requires waiting for Oracle Clusterware to unlock the resource or its dependents. Sometimes, Oracle Clusterware locks resources or other objects to prevent commands from interfering with each other. |
| ``` -f ``` | Use the force option:  - To add a resource that has dependencies on other resources that do not yet exist. The force option overrides checks that would prevent a command from being completed. - To add a resource if the resource has hard dependencies on other resources and the owner of the resources does not execute permissions on one or more of the dependencies. If you do not specify the force option in this case, an error displays. - To add resources of `application` type because you may need to move servers into the Generic server pool. If the servers currently host resources that must be stopped, then the force option is required |

See Also:

[Appendix B, "Oracle Clusterware Resource Reference"](resatt.md) for more information about resources and resource attributes

Usage Notes

- Both the `resource_name` and `-type` `resource_type` parameters are required. You can create an associated resource type using the `crsctl add type` command.
- Any user can create a resource but only clusterware administrators can create resources of type `local_resource` or resources of type `cluster_resource` that have `SERVER_POOLS=*`.
	Once a resource is defined, its ACL controls who can perform particular operations with it. The Oracle Clusterware administrator list is no longer relevant.
	On Windows, a member of the Administrators group has full control over everything.
	See Also:
	"crsctl setperm resource" for more information about setting ACLs
- If an attribute value for an attribute name-value pair contains commas, then the value must be enclosed in single quotation marks (`''`).
- Following is an example of an attribute file:
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
- Do not use this command for any resources with names that begin with ora because these resources are Oracle resources.

Example

Example 1

To register a VIP as a resource with Oracle Clusterware:

```
$ crsctl add resource app.appvip -type app.appvip.type -attr "RESTART_ATTEMPTS=2,
START_TIMEOUT=100,STOP_TIMEOUT=100,CHECK_INTERVAL=10,
USR_ORA_VIP=172.16.0.0,
START_DEPENDENCIES=hard(ora.net1.network)pullup(ora.net1.network),
STOP_DEPENDENCIES=hard(ora.net1.network)"
```

Example 2

To register a resources based on the `test_type1` resource type:

```
$ crsctl add resource r1 -type test_type1 -attr "PATH_NAME=/tmp/r1.txt"
$ crsctl add resource r1 -type test_type1 -attr "PATH_NAME=/tmp/r2.txt"
```

#### crsctl add type

Use the `crsctl add type` command to create a resource type in Oracle Clusterware.

Syntax

```
crsctl add type type_name -basetype base_type_name {-attr
"ATTRIBUTE=attribute_name | -file file_path,TYPE={string | int}
 [,DEFAULT_VALUE=default_value][,FLAGS=[READONLY][|REQUIRED]]"}
```

Parameters

Table E-3 crsctl add type Command Parameters

| Parameter | Description |
| --- | --- |
| ``` type_name ``` | A name for the resource type in the form of `xxx.yyy``.type`. Resource type names must be unique and cannot be changed after the resource type is registered. |
| ``` -basetype base_type_name ``` | The name of an existing base type. Any resource type that you create must either have `local_resource` or `cluster_resource` as its base resource type. |
| ``` -attr ``` | You can specify the resource type attributes using the `-attr` argument. Each type attribute definition can contain up to four type attribute keywords that must be displayed in the order shown. Enter a comma-delimited description of one or more resource type attributes enclosed in double quotation marks (`""`). The keywords for an attribute include:  1. `ATTRIBUTE`: Specify a name for the attribute. The name is case-sensitive and cannot contain spaces. 2. `TYPE`: Specify whether the attribute type is `integer` or `string`. 3. `DEFAULT_VALUE`: (Optional) If the attribute is required, then a default value is not required. For attributes that are not required, you must specify a default value that Oracle Clusterware uses when you create resources based on this resource type. 4. `FLAGS`: (Optional) Specify whether the attribute is `READONLY` or `REQUIRED`. `READONLY` means that after you register a resource with this resource type, you cannot modify this attribute. 	`REQUIRED` means that you must specify the name and value of this attribute when you create a resource that is based on this resource type. If you specify that this attribute is not required, then Oracle Clusterware uses the default value of this attribute that you specify.  You cannot use multiple `-attr` arguments to define multiple arguments for the resource type. Instead, you can specify multiple types within the double quotation marks after the `-attr` flag. For example:  ``` "ATTRIBUTE=FOO,TYPE=integer,DEFAULT_ VALUE=0,FLAGS=REQUIRED,ATTRIBUTE=BAR,TYPE=string" ```  The preceding example defines two type attributes, `FOO` and `BAR`. When you specify the `ATTRIBUTE` keyword, it ends the previous type attribute (if any) and begins a new type attribute. |
| ``` -file file_path ``` | Path name (either absolute or relative) for a text file containing line-separated resource type keyword-value pairs that define the resource type. An example of the contents of the file is:  ``` ATTRIBUTE=FOO TYPE=integer DEFAULT_VALUE=0 FLAGS=REQUIRED ATTRIBUTE=BAR TYPE=string ```  Note: The keywords must be in the following order: `ATTRIBUTE`, `TYPE`, `DEFAULT_VALUE`, and `FLAGS`. When you specify the `ATTRIBUTE` keyword, it ends the previous type attribute (if any) and begins a new type attribute.  The preceding example defines two type attributes, `FOO` and `BAR`. |

See Also:

["Resource Types"](crschp.md) for more information about resource types

Usage Notes

- Both the `type_name` and `base_type_name` parameters are required
- You can either specify a file containing the type information or you can specify the type information on the command line
- Do not use this command for any resource types with names that begin with ora because these resource types are Oracle resource types
- You must have read permissions on the base type

Example

To create a resource type for `demoActionScript`:

```
# crsctl add type test_type1 -basetype cluster_resource 
 -attr "ATTRIBUTE=FOO,TYPE=integer,DEFAULT_VALUE=0"
```

#### crsctl check css

Use the `crsctl check css` command to check the status of Cluster Synchronization Services. This command is most often used when Oracle Automatic Storage Management (Oracle ASM) is installed on the local server.

Syntax

```
crsctl check css
```

Usage Notes

Example

The `crsctl check css` command returns output similar to the following:

```
CRS-4529: Cluster Synchronization Services is online
```

#### crsctl check evm

Starting with Oracle Database 11g release 2 (11.2.0.2), use the `crsctl check evm` command to check the status of the Event Manager.

Syntax

```
crsctl check evm
```

Usage Notes

Example

The `crsctl check evm` command returns output similar to the following:

```
CRS-4533: Event Manager is online
```

#### crsctl delete resource

Use the `crsctl delete resource` command to remove resources from the Oracle Clusterware configuration.

Syntax

```
crsctl delete resource resource_name [-i] [-f]
```

Parameters

Table E-4 crsctl delete resource Command Parameters

| Parameter | Description |
| --- | --- |
| ``` resource_name ``` | Specify the name of the resource you want to remove. |
| ``` -i ``` | If you specify `-i`, then the command returns an error if processing this command requires waiting for Oracle Clusterware to unlock the resource or its dependents. Sometimes, Oracle Clusterware locks resources or other objects to prevent commands from interfering with each other. |
| ``` -f ``` | Use the force option to remove either running resources, or remove this resource even though other resources have a hard dependency on it. |

Usage Notes

- The `resource_name` parameter is required
- You must have read and write permissions to delete the specified resources
- Do not use this command for any resources with names that begin with ora because these resources are Oracle resources

Example

To delete a resource from Oracle Clusterware:

```
# crsctl delete resource myResource
```

#### crsctl delete type

Use the `crsctl delete type` command to remove a resource type from the Oracle Clusterware configuration.

Syntax

```
crsctl delete type type_name [-i]
```

Usage Notes

- The `type_name` parameter is required
- If you specify `-i`, then the command fails if Oracle Clusterware cannot process the request immediately
- Do not use this command for any resource types with names that begin with ora because these resource types are Oracle resource types

Example

To delete a resource type, run the following command as who has write permissions on the resource type:

```
$ crsctl delete type app.appvip.type
```

#### crsctl get hostname

Use the `crsctl get hostname` command to retrieve the host name of the local server.

Syntax

```
crsctl get hostname
```

Example

Oracle Clusterware returns the host name of the local server:

```
$ crsctl get hostname
node2
```

#### crsctl getperm resource

Use the `crsctl getperm resource` command to display the user and group permissions for the specified resource.

Syntax

```
crsctl getperm resource resource_name [ {-u user_name | -g group_name} ]
```

See Also:

[Appendix B, "Oracle Clusterware Resource Reference"](resatt.md) for more information about resources and resource attributes

Parameters

Table E-5 crsctl getperm resource Command Parameters

| Parameter | Description |
| --- | --- |
| ``` resource_name ``` | Specify the name of the resource for which you want to obtain permissions. |
| ``` -u user_name ``` | If you specify `-u`, then Oracle Clusterware obtains permissions for a particular user. |
| ``` -g group_name ``` | If you specify `-g`, then Oracle Clusterware obtains permissions for a particular group. |

Usage Notes

- The `resource_name` parameter is required
- You must have read permission on the specified resources to obtain their permissions
- Do not use this command for any resources with names that begin with ora because these resources are Oracle resources

Example

The `crsctl getperm resource` command returns output similar to the following, depending on the command option you choose:

```
$ crsctl getperm resource app.appvip

Name: app.appvip
owner:root:rwx,pgrp:oinstall:rwx,other::r--
```
```
$ crsctl getperm resource app.appvip -u oracle

Name: app.appvip
rwx
```
```
$ crsctl getperm resource app.appvip -g dba

Name: app.appvip
r--
```

#### crsctl getperm type

Use the `crsctl getperm type` command to obtain permissions for a particular resource type.

Syntax

```
crsctl getperm type resource_type  [-u user_name] | [-g group_name]
```

See Also:

["Resource Types"](crschp.md) for more information about resource types

Parameters

Table E-6 crsctl getperm type Command Parameters

| Parameter | Description |
| --- | --- |
| ``` resource_type ``` | Specify the resource type for which you want to obtain permissions. |
| ``` -u user_name ``` | If you specify `-u`, then Oracle Clusterware obtains permissions for a particular user. |
| ``` -g group_name ``` | If you specify `-g`, then Oracle Clusterware obtains permissions for a particular group. |

Usage Notes

- The `resource_type` parameter is required
- Do not use this command for any resource types with names that begin with ora because these resource types are Oracle resource types

Example

The `crsctl getperm type` command returns output similar to the following:

```
$ crsctl getperm type app.appvip.type

Name: app.appvip.type
owner:root:rwx,pgrp:oinstall:rwx,other::r--
```

#### crsctl modify resource

Use the `crsctl modify resource` command to modify the attributes of a particular resource in Oracle Clusterware.

Syntax

```
crsctl modify resource resource_name -attr "attribute_name=attribute_value"
[-i] [-f] [-delete]
```

Parameters

Table E-7 crsctl modify resource Command Parameters

| Parameter | Description |
| --- | --- |
| ``` resource_name ``` | The name of the resource you want to modify. |
| ``` -attr "attribute_name= attribute_value" ``` | You can specify attributes for a resource you want to modify in two different ways:  - Following the `-attr` flag, you can specify one or more comma-delimited attribute name-value pairs to modify enclosed in double quotations marks (`""`). For example: 	``` 	-attr "CHECK_INTERVAL=30, START_TIMEOUT=25" 	``` - Alternatively, you can specify attribute values for resources on a particular server, with a particular cardinality value, and with a particular degree value. This method can be useful for applications that are somehow tied to a particular server. Following the `-attr` flag, the syntax is as follows: 	``` 	attribute_name{@SERVERNAME(server_name) 	[@DEGREEID(did)] \| @CARDINALITYID(cid) 	[@DEGREEID(did)]}=attribute_value 	``` 	If you specify the `@SERVERNAME(``server_name``)` syntax, then the attribute value you specify for the attribute you specify is limited to resources residing on the server you specify. 	Alternatively, if you specify the `@CARDINALITYID(``cid``)` syntax, then the attribute value you specify for the attribute you specify is limited to resource instances with a specific cardinality ID (`cid`). 	Optionally, you can combine the `@DEGREEID(``did``)` syntax with either the `SERVERNAME` or `CARDINALITYID` syntax, or both, to limit the attribute value to resources with the specific `DEGREE`. 	Examples: 	``` 	CHECK_INTERVAL@SERVERNAME(node1)=45 	STOP_TIMEOUT@CARDINALITYID(2)=65 	STOP_TIMEOUT@SERVERNAME(node1)@DEGREEID(2)=65 	STOP_TIMEOUT@CARDINALITYID(3)@DEGREEID(2)=65 	``` |
| ``` -i ``` | If you specify `-i`, then the command returns an error if processing this command requires waiting for Oracle Clusterware to unlock the resource or its dependents. Sometimes, Oracle Clusterware locks resources or other objects to prevent commands from interfering with each other. |
| ``` -f ``` | Use the `-f` option when:  - The resource has a hard dependency on a non-existing resource - The owner of the resource does not have execute permissions on one or more hard dependencies - The modification results in servers being moved into the Generic pool and resources being stopped or relocated to accomplish the server move |
| ``` -delete ``` | If you specify the `-delete` option, then Oracle Clusterware deletes the named attribute. |

See Also:

[Appendix B, "Oracle Clusterware Resource Reference"](resatt.md) for more information about resources and resource attributes

Usage Notes

- The `resource_name` parameter is required
- If an attribute value for an attribute name-value pair contains commas, then the value must be enclosed in single quotation marks (`''`). For example:
	```
	"START_DEPENDENCIES='hard(res1,res2,res3)'"
	```
- You must have read and write permissions on the specified resources to modify them
- Do not use this command for any resources with names that begin with ora because these resources are Oracle resources

Example

To modify the attributes of the `appsvip` resource:

```
$ crsctl modify resource appsvip -attr USR_ORA_VIP=10.1.220.17 -i
```

#### crsctl modify type

Use the `crsctl modify type` command to modify an existing resource type.

Syntax

```
crsctl modify type type_name -attr "ATTRIBUTE=attribute_name,TYPE={string | int}
[,DEFAULT_VALUE=default_value [,FLAGS=[READONLY][| REQUIRED]]" [-i] [-f]]
```

Parameters

Table E-8 crsctl modify type Command Parameters

| Parameter | Description |
| --- | --- |
| ``` type_name ``` | Specify the name of the resource type you want to modify. You cannot modify resource type names. |
| ``` -attr ``` | You can modify the following resource type keywords:  - `TYPE` - `DEFAULT_VALUE` - `FLAGS`  Note: Although you must specify the `ATTRIBUTE` keyword, you cannot modify it.  See Also: Table E-3, "crsctl add type Command Parameters" for descriptions of these keywords |
| ``` -i ``` | If you specify the `-i` option, then the command fails if Oracle Clusterware cannot process the request immediately. |

See Also:

["Resource Types"](crschp.md) for more information about resource types

Usage Notes

- The `type_name` parameter is required
- Do not use this command for any resource types with names that begin with ora because these resource types are Oracle resource types

Example

The following example modifies the two type attributes `FOO` and `BAR`:

```
$ crsctl modify type myType.type -attr "ATTRIBUTE=FOO,DEFAULT_VALUE=0
ATTRIBUTE=BAR,DEFAULT_VALUE=baz"
```

#### crsctl setperm resource

Use the `crsctl setperm resource` command to set permissions for a particular resource.

Syntax

```
crsctl setperm resource resource_name {-u acl_string | -x acl_string |
-o user_name | -g group_name}
```

Parameters

Table E-9 crsctl setperm resource Command Parameters

| Parameter | Description |
| --- | --- |
| ``` resource_name ``` | Specify the name of the resource for which you want to set permissions. |
| ``` {-u \| -x \| -o \| -g} ``` | You can set only one of the following permissions for a resource:  - `-u` `acl_string`: You can update the access control list (ACL) for a resource - `-x` `acl_string`: You can delete the ACL for a resource - `-o` `user_name`: You can change the owner of a resource by entering a user name - `-g` `group_name`: You can change the primary group of a resource by entering a group name  Specify a user, group, or other ACL string, as follows:  ``` user:user_name[:readPermwritePermexecPerm] \| group:group_name[:readPermwritePermexecPerm] \| other[::readPermwritePermexecPerm] ``` - `user`: User ACL - `group`: Group ACL - `other`: Other ACL - `readPerm`: Read permission for the resource; the letter `r` grants a user, group, or other read permission, the minus sign (`-`) denies read permission - `writePerm`: Write permission for the resource; the letter `w` grants a user, group, or other write permission, the minus sign (`-`) denies write permission - `execPerm`: Execute permission for the resource; the letter `x` grants a user, group, or other execute permission, the minus sign (`-`) denies execute permission |

See Also:

[Appendix B, "Oracle Clusterware Resource Reference"](resatt.md) for more information about resources and resource attributes

Usage Notes

- Do not use this command for any resources with names that begin with ora because these resources are Oracle resources.
- You must have read and write permissions on the specified resources to set their permissions

Example

To grant read, write, and execute permissions on a resource for user Scott:

```
$ crsctl setperm resource myResource -u user:scott:rwx
```

#### crsctl setperm type

Use the `crsctl setperm type` command to set permissions resources of a particular resource type.

Syntax

```
crsctl setperm type resource_type_name {-u acl_string | -x acl_string |
-o user_name | -g group_name}
```

Parameters

Table E-10 crsctl setperm type Command Parameters

| Parameter | Description |
| --- | --- |
| ``` resource_type_name ``` | Specify the name of the resource type for which you want to set permissions. |
| ``` {-u \| -x \| -o \| -g} ``` | You can specify only one of the following parameters for a resource type:  - `-u` `acl_string`: You can update the access control list (ACL) for a resource type - `-x` `acl_string`: You can delete the ACL for a resource type - `-o` `user_name`: You can change the owner of a resource type by entering a user name - `-g` `group_name`: You can change the primary group of a resource type by entering a group name  Specify a user, group, or other ACL string, as follows:  ``` user:user_name[:readPermwritePermexecPerm] \| group:group_name[:readPermwritePermexecPerm] \| other[::readPermwritePermexecPerm] ``` - `user`: User ACL - `group`: Group ACL - `other`: Other ACL - `readPerm`: Read permission for the resource type; the letter `r` grants a user, group, or other read permission, the minus sign (`-`) denies read permission - `writePerm`: Write permission for the resource type; the letter `w` grants a user, group, or other write permission, the minus sign (`-`) denies write permission - `execPerm`: Execute permission for the resource type; the letter `x` grants a user, group, or other execute permission, the minus sign (`-`) denies execute permission |

Usage Notes

- The `resource_type_name` parameter is required
- You must have read and write permissions on the specified resources to set their permissions
- Do not use this command for any resource types with names that begin with ora because these resource types are Oracle resource types

Example

To grant read, write, and execute permissions on a resource type for user Scott:

```
$ crsctl setperm type resType -u user:scott:rwx
```

#### crsctl start resource

Use the `crsctl start resource` command to start many idle resources on a particular server in the cluster.

Syntax

```
crsctl start resource {resource_name [...] | -w filter | -all} [-n server_name]
[-k cid] [-d did] [-env "env1=val1,env2=val2,..."] [-i] [-f]
```

Parameters

Table E-11 crsctl start resource Command Parameters

| Parameter | Description |
| --- | --- |
| ``` resource_name [...] ``` | One or more space-delimited resource names to start. |
| ``` -w filter ``` | Specify a resource filter that Oracle Clusterware uses to match resources. |
| ``` -all ``` | Use this option to start all resources in the cluster. |
| ``` -n server_name ``` | Specify the name of the server on which the resources you want to start reside. If you do not specify a server, then Oracle Clusterware starts the resources on the best server according to the attribute profile of each resource. |
| ``` -k cid ``` | Specify the resource cardinality ID. If you specify this parameter, then Oracle Clusterware starts the resource instances that have the cardinality you specify. |
| ``` -d did ``` | Specify the resource degree ID. If you specify this parameter and the degree ID is greater than 1, then Oracle Clusterware starts all resource instances that meet this criteria.  Note: You cannot use the `-d` option without specifying the `-k` option. |
| ``` -env "env1=val1, env2=val2,..." ``` | You can optionally override one or more resource profile attribute values with the `-env` command option. If you specify multiple environment name-value pairs, then you must separate each pair with a comma and enclose the entire list in double quotation marks (`""`). |
| ``` -i ``` | If you specify `-i`, then the command returns an error if processing this command requires waiting for Oracle Clusterware to unlock the resource or its dependents. Sometimes, Oracle Clusterware locks resources or other objects to prevent commands from interfering with each other. |
| ``` -f ``` | Use the `-f` option to relocate a resource running on another server on which the resource you want to start has a hard start dependency. If you do not specify the force option in this case, then the start command fails. |

Usage Notes

- Any one of the three following options is required to specify which resources you want to start:
	- You can specify one or more resources to start
		- You can specify a resource filter that Oracle Clusterware uses to match resources to start
		- You can specify the `-all` option to start all resources on the specified server
- You must have read and execute permissions on the specified resources to start them
- Do not use this command for any resources with names that begin with ora because these resources are Oracle resources.

Example

To start a resource:

```
# crsctl start resource myResource -n server1
```

#### crsctl status resource

Use the `crsctl status resource` command to obtain the status and configuration information of many particular resources.

Syntax

```
crsctl status resource {resource_name [...] | -w "filter"}  [-p | -v [-e]] |
[-f | -l | -g] [[-k cid | -n server_name] [-d did]] | [-s -k cid [-d did]] [-t]
```

Parameters

Table E-12 crsctl status resource Command Parameters

| Parameter | Description |
| --- | --- |
| ``` resource_name [...] \| -w "filter" ``` | One or more space-delimited resource names of which you want to check the status.  Or you can specify a resource filter that Oracle Clusterware uses to limit the number of resources displayed. The filter must be enclosed in double quotation marks (`""`). Values that contain parentheses or spaces must be enclosed in single quotation marks (`''`). Operators must be surrounded by spaces. Examples of resource filters include:  - `"TYPE == cluster_resource"`: This filter limits the display to only resources of `cluster_resource` type. - `"CHECK_INTERVAL > 10"`: This filter limits the display to resources that have a value greater than 10 for the `CHECK_INTERVAL` resource attribute - `"(CHECK_INTERVAL > 10) AND (NAME co 2)"`: This filter limits the display to resources that have a value greater than 10 for the `CHECK_INTERVAL` resource attribute and the name of the resource contains the number `2`. - `"START_DEPENDENCIES = 'hard(appsvip)'"`: This filter limits the display to resources that have a hard start dependency on the `appsvip` resource.  See Also: ["Filters"](crs_api.md) for more information about filters |
| ``` [-p \| -v [-e]] \| [-f \| -l \| -g] ``` | You can specify one of two options: `[-p \| -v [-e]]` or `[-f \| -l \| -g]`, where:  - Specify the `-p` parameter to display the static configuration of the resource or specify the `-v` parameter to display the run-time configuration of the resource. Use the `-e` parameter with the `-v` parameter to evaluate the special values of the resource instance. - Specify the `-f` parameter to display the full configuration of the resource; or specify the `-l` parameter to display all cardinal and degree values of the resource; or specify the `-g` parameter to check whether the specified resources are registered |
| ``` [-k cid \|  -n server_name] [-d did \| [-s -k cid [-d did]]] ``` | You can specify one of two options: `[-k` `cid` `\| -n` `server_name`\] or `[-s -k` `cid` `[-d` `did`\]\], where:  - Specify the `-k` `cid` parameter to specify a cardinality ID of the resources you want to query. Or you can specify the `-n` parameter to specify a particular server on which to check resources. Optionally, you can specify the `-d` parameter with the `-n` parameter to specify the degree ID of resources you want to check. If you specify a degree ID greater than 1, then Oracle Clusterware checks all resource instances on the server that meet this criteria. - Specify the `-s` parameter with the `-k` parameter to obtain a list of target servers for relocation. You can further limit the output by specifying a degree ID with the `-d` parameter. |
| ``` -t ``` | Specify the `-t` parameter to display the output in tabular form. |

Usage Notes

- Either a space-delimited list of resources or a resource filter is required.
- You must have read permissions on the specified resources to obtain their status.
- Use `crsctl status resource` to query the status information of any resource deployed in the cluster. Oracle recommends, however, that you use the respective SRCVTL command to query the status information of Oracle (`ora.*`) resources.

Example

The `crsctl status resource` command returns output similar to the following:

```
$ crsctl status resource ora.staii14.vip

NAME=ora.staii14.vip
TYPE=ora.cluster_vip_net1.type
TARGET=ONLINE
STATE=ONLINE on staii14
```

#### crsctl status type

Use the `crsctl status type` command to obtain the configuration information of one or more particular resource types.

Syntax

```
crsctl status type resource_type_name [...]] [-g] [-p] [-f]
```

Parameters

Table E-13 crsctl status type Command Parameters

| Parameter | Description |
| --- | --- |
| ``` [resource_type_name [...] ``` | Specify one or more space-delimited resource type names of which you want to check the status. |
| ``` -g] [-p] [-f ``` | You can specify the following parameters as options when Oracle Clusterware checks the status of specific server pools:  - `-g`: Use this parameter to check if the specified resource types are registered - `-p`: Use this parameter to display static configuration of the specified resource types - `-f`: Use this parameter to display the full configuration of the resource types |

Usage Notes

- The `resource_type_name` parameter or a filter is required

Example

The `crsctl status type` command returns output similar to the following:

```
$ crsctl status type ora.network.type

TYPE_NAME=ora.network.type
BASE_TYPE=ora.local_resource.type
```

#### crsctl stop resource

Use the `crsctl stop resource` command to stop running resources.

Syntax

```
crsctl stop resource {resource_name [...] | -w "filter" | -all} [-n server_name]
[-k cid] [-d did] [-env "env1=val1,env2=val2,..."] [-i] [-f]
```

Parameters

Table E-14 crsctl stop resource Command Parameters

| Parameter | Description |
| --- | --- |
| ``` resource_name [...] ``` | One or more space-delimited resource names to stop. |
| ``` -w "filter" ``` | Specify a resource filter that Oracle Clusterware uses to limit the number of resources stopped. The filter must be enclosed in double quotation marks (`""`). Examples of resource filters include:  - `"TYPE == cluster_resource"`: This filter limits Oracle Clusterware to stop only resources of `cluster_resource` type - `"CHECK_INTERVAL > 10"`: This filter limits Oracle Clusterware to stop resources that have a value greater than 10 for the `CHECK_INTERVAL` resource attribute - `"(CHECK_INTERVAL > 10) AND (NAME co 2)"`: This filter limits Oracle Clusterware to stop resources that have a value greater than 10 for the `CHECK_INTERVAL` resource attribute and the name of the resource contains the number `2` |
| ``` -all ``` | Use this option to stop all resources in the cluster. |
| ``` -n server_name ``` | Specify the name of the server on which the resource instances you want to stop reside. If you do not specify a server, then Oracle Clusterware stops all instances of the resource. |
| ``` -k cid ``` | Specify the resource cardinality ID. If you specify this parameter, then Oracle Clusterware stops the resource instances that have the cardinality you specify. |
| ``` -d did ``` | Specify the resource degree ID. If you specify this parameter and the degree ID is greater than 1, then Oracle Clusterware stops all resource instances that meet this criteria. |
| ``` -env "env1=val1, env2=val2,..." ``` | You can optionally override one or more resource profile attribute values with the `-env` command option. If you specify multiple environment name-value pairs, then you must separate each pair with a comma and enclose the entire list in double quotation marks (`""`). |
| ``` -i ``` | If you specify `-i`, then the command returns an error if processing this command requires waiting for Oracle Clusterware to unlock the resource or its dependents. Sometimes, Oracle Clusterware locks resources or other objects to prevent commands from interfering with each other. |
| ``` -f ``` | Specify the `-f` option to force the stopping of the resource when it has other resources running that depend on it. Dependent resources are relocated or stopped when you use this option. |

Usage Notes

- Any one of the three following options is required to specify which resources you want to stop:
	- You can specify one or more resources to stop
		- You can specify a resource filter that Oracle Clusterware uses to match resources to stop
		- You can specify the `-all` option with the `-n` `server_name` option to stop all resources on a particular server
- You must have read and execute permissions on the specified resources to stop them
- Do not use this command for any resources with names that begin with ora because these resources are Oracle resources.

Example

To stop a resource:

```
$ crsctl stop resource -n node1 -k 2
```

### Oracle RAC Environment CRSCTL Commands

The commands listed in this section manage the Oracle Clusterware stack in an Oracle RAC environment, which consists of the following:

- Oracle Clusterware, the member nodes and server pools
- Oracle ASM (if installed)
- Cluster Synchronization Services
- Cluster Time Synchronization Services

You can use the following commands only in an Oracle RAC environment:

- `crsctl add crs administrator`
- `crsctl add css votedisk`
- `crsctl add serverpool`
- `crsctl check cluster`
- `crsctl check crs`
- `crsctl check resource`
- `crsctl check ctss`
- `crsctl config crs`
- `crsctl delete crs administrator`
- `crsctl delete css votedisk`
- `crsctl delete node`
- `crsctl delete serverpool`
- `crsctl disable crs`
- `crsctl discover dhcp`
- `crsctl enable crs`
- `crsctl get clientid dhcp`
- `crsctl get css`
- `crsctl get css ipmiaddr`
- `crsctl get nodename`
- `crsctl getperm serverpool`
- `crsctl lsmodules`
- `crsctl modify serverpool`
- `crsctl pin css`
- `crsctl query crs administrator`
- `crsctl query crs activeversion`
- `crsctl query crs releaseversion`
- `crsctl query crs softwareversion`
- `crsctl query css ipmiconfig`
- `crsctl query css ipmidevice`
- `crsctl query css votedisk`
- `crsctl query dns`
- `crsctl release dhcp`
- `crsctl relocate resource`
- `crsctl relocate server`
- `crsctl replace discoverystring`
- `crsctl replace votedisk`
- `crsctl request dhcp`
- `crsctl set css`
- `crsctl set css ipmiaddr`
- `crsctl set css ipmiadmin`
- `crsctl setperm serverpool`
- `crsctl start cluster`
- `crsctl start crs`
- `crsctl start ip`
- `crsctl start testdns`
- `crsctl status ip`
- `crsctl status server`
- `crsctl status serverpool`
- `crsctl status testdns`
- `crsctl stop cluster`
- `crsctl stop crs`
- `crsctl stop ip`
- `crsctl stop testdns`
- `crsctl unpin css`
- `crsctl unset css`
- `crsctl unset css ipmiconfig`

#### crsctl add crs administrator

Use the `crsctl add crs administrator` command to add a user to the list of cluster administrators.

Syntax

```
crsctl add crs administrator -u user_name [-f]
```

Parameters

Table E-15 crsctl add crs administrator Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -u user_name ``` | The name of the user to whom you want to give Oracle Clusterware administrative privileges. |
| ``` -f ``` | Use this option to override the user name validity check. |

Usage Notes

- You must run this command as `root` or a cluster administrator, or an administrator on Windows systems
- By default, `root`, the user that installed Oracle Clusterware, and the `*` wildcard are members of the list of users who have Oracle Clusterware administrative privileges. Run the `crsctl delete crs administrator` command to remove the wildcard and enable role-separated management of Oracle Clusterware.
	See Also:
	["Role-Separated Management"](admin.md) for more information

Example

To add a user to the list of Oracle Clusterware administrators:

```
# crsctl add crs administrator -u scott
```

#### crsctl add css votedisk

Use the `crsctl add css votedisk` command to add one or more voting disks to the cluster on storage devices other than an Oracle ASM disk group.

Syntax

```
crsctl add css votedisk path_to_voting_disk [path_to_voting_disk ...] [-purge]
```

Parameters

Table E-16 crsctl add css votedisk Command Parameters

| Parameter | Description |
| --- | --- |
| ``` path_to_voting_disk ``` | A fully qualified path to the voting disk you want to add. To add multiple voting disks, separate each path with a space. |
| ``` -purge ``` | Removes all existing voting disks at once. You can replace the existing set of voting files in one operation. |

Usage Notes

- You should have at least three voting disks, unless you have a storage device, such as a disk array, that provides external redundancy. Oracle recommends that you do not use more than 5 voting disks. The maximum number of voting disks that is supported is 15.

See Also:

["Adding, Deleting, or Migrating Voting Disks"](votocr.md) for more information

Example

To add a voting disk to the cluster:

```
$ crsctl add css votedisk /stor/grid/ -purge
```

#### crsctl add serverpool

Caution:

By default, any named user may create a server pool. To restrict the operating system users that have this privilege, Oracle strongly recommends that you add specific users to the CRS Administrators list.

See Also:

["Role-Separated Management"](admin.md) for more information about adding users to the CRS Administrators list

Use the `crsctl add serverpool` command to add a server pool that is for hosting non-database resources (such as application servers) to Oracle Clusterware.

Syntax

```
crsctl add serverpool server_pool_name {-file file_path | 
                  -attr "attr_name=attr_value[,attr_name=attr_value[,...]]"}
                  [-i] [-f]
```

Parameters

Table E-17 crsctl add serverpool Command Parameters

| Parameter | Description |
| --- | --- |
| ``` server_pool_name ``` | A short, descriptive name for the server pool. |
| ``` -file file_path ``` | Fully-qualified path to an attribute file to define the server pool. |
| ``` attribute_name ``` | The name of a server pool attribute Oracle Clusterware uses to manage the server pool preceded by the `-attr` flag. The available attribute names include:  - IMPORTANCE - MIN\_SIZE - MAX\_SIZE - SERVER\_NAMES - PARENT\_POOLS - EXCLUSIVE\_POOLS - ACL - ACTIVE\_SERVERS |
| ``` attribute_value ``` | A value for the server pool attribute.  Note: The `attribute_name` and `attribute_value` parameters must be enclosed in double quotation marks (`""`) and separated by commas. For example:  ``` -attr "MAX_SIZE=30, IMPORTANCE=3" ``` |
| ``` -i ``` | If you specify `-i`, then the command fails if Oracle Clusterware cannot process the request immediately. |
| ``` -f ``` | If you specify the `-f` option, then Oracle Clusterware stops resources running on a server in another server pool and relocates that server into the server pool you are adding. If you do not specify the `-f` option, then Oracle Clusterware checks whether the creation of the server pool results in stopping any resources on a server in another server pool that is going to give up a server to the server pool you are adding. If so, then Oracle Clusterware rejects the `crsctl add serverpool` command. |

Usage Notes

- The `server_pool_name` parameter is required.
- If an attribute value for an attribute name-value pair contains commas, then the value must be enclosed in single quotation marks (`''`).
- Do not use this command for any server pools with names that begin with ora because these server pools are Oracle server pools.
- Running this command may result in Oracle Clusterware relocating other servers between server pools to comply with the new configuration.
- You must run this command as `root` or a cluster administrator.
- Use the `crsctl add serverpool` command to create server pools that host non-database resources. To create server pools that host Oracle databases, use the SRVCTL command utility.
	See Also:
	[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/srvctladmin.htm#RACAD7733) for information about using the SRVCTL command utility to create server pools

Example

Example 1

To add a server pool named `testsp` with a maximum size of 5 servers, run the following command as `root` or the Oracle Clusterware installation owner:

```
# crsctl add serverpool testsp -attr "MAX_SIZE=5"
```

Example 2

Create the `sp1_attr` file with the attribute values for the `sp1` serverpool, each on its own line, as shown in the following example:

```
IMPORTANCE=1
MIN_SIZE=1
MAX_SIZE=2
SERVER_NAMES=node3 node4 node5
PARENT_POOLS=Generic
EXCLUSIVE_POOLS=testsp
ACL=owner:oracle:rwx,pgrp:oinstall:rwx,other::r--
```

Use the following command to create the `sp1` server pool using the `sp1_attr` file as input:

```
$ crsctl add serverpool sp1 -file /tmp/sp1_attr
```

#### crsctl check cluster

Use the `crsctl check cluster` command on any node in the cluster to check the status of the Oracle Clusterware stack.

Syntax

```
crsctl check cluster [-all | [-n server_name [...]]
```

Usage Notes

- You can check the status of the Oracle Clusterware stack on all nodes in the cluster with the `-all` option or you can specify one or more space-delimited nodes. If you do not specify either option, Oracle Clusterware checks the status of the Oracle Clusterware stack on the local server.
- You can use this cluster-aware command on any node in the cluster.

Example

The `crsctl check cluster` command returns output similar to the following:

```
$ crsctl check cluster -all
*****************************************************************
node1:
CRS-4537: Cluster Ready Services is online
CRS-4529: Cluster Synchronization Services is online
CRS-4533: Event Manager is online
*****************************************************************
node2:
CRS-4537: Cluster Ready Services is online
CRS-4529: Cluster Synchronization Services is online
CRS-4533: Event Manager is online
*****************************************************************
```

#### crsctl check crs

Use the `crsctl check crs` command to check the status of Oracle High Availability Services and the Oracle Clusterware stack on the local server.

Syntax

```
crsctl check crs
```

Example

To check the health of Oracle Clusterware on the local server:

```
$ crsctl check crs
CRS-4638: Oracle High Availablity Services is online
CRS-4537: Cluster Ready Services is onlin
CRS-4529: Cluster Synchronization Services is online
CRS-4533: Event Manager is online
```

#### crsctl check resource

Use the `crsctl check resource` command to initiate the check action inside the application-specific agent of a particular resource. Oracle Clusterware only provides output if something prevents the system from issuing the check request, such as a bad resource name.

Syntax

```
crsctl check resource {resource_name [...] | -w "filter" }
      [-n node_name
] [-k cardinality_id] [-d degree_id] }
```

Parameters

Table E-18 crsctl check resource Command Parameters

| Parameter | Description |
| --- | --- |
| ``` resource_name ``` | Specify a particular resource. You can check multiple resources by entering multiple resource names, with each name separated by a space. |
| ``` -w "filter" ``` | Specify a resource filter that Oracle Clusterware uses to limit the number of resources checked. The filter must be enclosed in double quotation marks (`""`). Examples of resource filters include:  - `"TYPE == cluster_resource"`: This filter limits Oracle Clusterware to check only resources of `cluster_resource` type - `"CHECK_INTERVAL > 10"`: This filter limits Oracle Clusterware to check resources that have a value greater than 10 for the `CHECK_INTERVAL` resource attribute - `"(CHECK_INTERVAL > 10) AND (NAME co 2)"`: This filter limits Oracle Clusterware to check resources that have a value greater than 10 for the `CHECK_INTERVAL` resource attribute and the name of the resource contains the number `2` |
| ``` -n node_name ``` | Check the resource instance on a specific node. If you do not specify the `-n` option, then Oracle Clusterware checks the resource instances only on the local server. |
| ``` -k cardinality_id ``` | Specify the resource cardinality ID. |
| ``` -d degree_id ``` | Specify the resource degree ID. |

Usage Notes

- You must have read and execute permissions on the specified resources to check them
- Do not use this command for any resources with names that begin with ora because these resources are Oracle resources
- If this command is successful, it only means that a check was issued; it does not mean the CHECK action has been completed

Example

To initiate the check action inside the application-specific agent of a particular resource:

```
$ crsctl check resource appsvip
```

#### crsctl check ctss

Use the `crsctl check ctss` command to check the status of the Cluster Time Synchronization services.

Syntax

```
crsctl check ctss
```

Example

The `crsctl check ctss` command returns output similar to the following:

```
CRS-4700: The Cluster Time Synchronization Service is in Observer mode.
```

or

```
CRS-4701: The Cluster Time Synchronization Service is in Active mode.
CRS-4702: Offset from the reference node (in msec): 100
```

#### crsctl config crs

Use the `crsctl config crs` command to display Oracle High Availability Services automatic startup configuration.

Syntax

```
crsctl config crs
```

Example

The `crsctl config crs` command returns output similar to the following:

```
CRS-4622: Oracle High Availability Services autostart is enabled.
```

#### crsctl delete crs administrator

Use the `crsctl delete crs administrator` command to remove a user from the Oracle Clusterware administrator list.

Syntax

```
crsctl delete crs administrator -u user_name [-f]
```

Parameters

Table E-19 crsctl delete crs administrator Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -u user_name ``` | The name of the user whose Oracle Clusterware administrative privileges you want to remove.  By default, the list of users with Oracle Clusterware administrative privileges consists of the user who installed Oracle Clusterware, `root`, and `*`. The user who installed Oracle Clusterware and `root` are permanent members this list. The `*` value gives Oracle Clusterware administrative privileges to all users and must be removed to enable role-separated management.  See Also: ["Role-Separated Management"](admin.md) for more information |
| ``` -f ``` | Use this option to override the user name validity check. |

Usage Notes

- The `user_name` parameter is required
- You must run this command as `root` or a cluster administrator, or an administrator on Windows systems
- To enable role-separated management, you must remove the `*` value enclosed in double quotation marks (`""`)

Example

To remove a user from the list of cluster administrators:

```
# crsctl delete crs administrator -u scott
```

#### crsctl delete css votedisk

Use the `crsctl delete css votedisk` to remove a voting disk from the Oracle Clusterware configuration.

Syntax

```
crsctl delete css votedisk voting_disk_GUID [voting_disk_GUID
 [...]]
```

Parameters

Table E-20 crsctl delete css votedisk Command Parameters

| Parameter | Description |
| --- | --- |
| ``` voting_disk_GUID ``` | Enter the file universal identifier (GUID) of the voting disk you want to remove. Specify multiple GUIDs in a space-delimited list. |

Usage Notes

- You can use this command only to remove voting disks from non-Oracle ASM storage devices
- You can obtain the file universal identifiers of each current voting disk by running the `crsctl query css votedisk` command

Example

To remove a voting disk:

```
$ crsctl delete css votedisk 26f7271ca8b34fd0bfcdc2031805581e
```

#### crsctl delete node

Use the `crsctl delete node` to remove a node from the cluster.

Syntax

```
crsctl delete node -n node_name
```

Usage Notes

- You must be `root` to run this command
- The `node_name` parameter is required

Example

To delete the node named `node06` from the cluster, run the following command as `root`:

```
# crsctl delete node -n node06
```

#### crsctl delete serverpool

Use the `crsctl delete serverpool` command to remove a server pool from the Oracle Clusterware configuration.

Syntax

```
crsctl delete serverpool server_pool_name [server_pool_name
 [...]] [-i]
```

See Also:

["Understanding Server Pools"](admin.md) for more information about server pools and server pool attributes

Usage Notes

- The `server_pool_name` parameter is required
- If you specify `-i`, then the command fails if Oracle Clusterware cannot process the request immediately
- Do not use this command for any server pools with names that begin with ora because these server pools are Oracle server pools
- While you can use this command in either environment, it is only useful in the Oracle RAC environment

Example

To delete a server pool, run the following command as `root` or the Oracle Clusterware installation owner:

```
# crsctl delete serverpool sp1
```

#### crsctl disable crs

Use the `crsctl disable crs` command to prevent the automatic startup of Oracle High Availability Services when the server boots.

Syntax

```
crsctl disable crs
```

Usage Notes

- This command only affects the local server
- If you disable Oracle High Availability Services automatic startup, you must use the `crsctl start crs` command to start Oracle High Availability Services

Example

The `crsctl disable crs` command returns output similar to the following:

```
CRS-4621: Oracle High Availability Services autostart is disabled.
```

#### crsctl discover dhcp

Starting with Oracle Database 11g release 2 (11.2.0.2), use the `crsctl discover dhcp` command to send DHCP discover packets on the network at the specified port. If DHCP servers are present on the network, then they respond to the discovery message and the command succeeds.

Syntax

```
crsctl discover dhcp -clientid clientid [-port port]
```

Parameters

Table E-21 crsctl discover dhcp Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -clientid clientid ``` | Specify the client ID for which you want to attempt discovery. Obtain the client ID by running the `crsctl get clientid dhcp` command. |
| ``` -port port ``` | The port to which CRSCTL sends the discovery packets. |

Usage Notes

- You must run this command as `root`

Example

The `crsctl discover dhcp` command returns output similar to the following:

```
# crsctl discover dhcp -clientid stmjk0462clr-stmjk01-vip

CRS-10009: DHCP server returned server: 192.168.53.232,
 loan address : 192.168.29.221/255.255.252.0, lease time: 43200
```

#### crsctl enable crs

Use the `crsctl enable crs` command to enable automatic startup of Oracle High Availability Services when the server boots.

Syntax

```
crsctl enable crs
```

Usage Notes

- This command only affects the local server

Example

The `crsctl enable crs` command returns output similar to the following:

```
CRS-4622: Oracle High Availability Services autostart is enabled.
```

#### crsctl get clientid dhcp

Starting with Oracle Database 11g release 2 (11.2.0.2), use the `crsctl get clientid dhcp` command to display the client ID that the Oracle Clusterware agent uses to obtain the IP addresses from the DHCP server for configured cluster resources. The VIP type is required.

Syntax

```
crsctl get clientid dhcp -cluname cluster_name -viptype vip_type
[-vip vip_res_name] [-n node_name]
```

Parameters

Table E-22 crsctl get clientid dhcp Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -cluname cluster_name ``` | Specify the name of the cluster where the cluster resources are configured. |
| ``` -viptype vip_type ``` | Specify the type of the VIP resource for which you want to display client IDs: `HOSTVIP`, `SCANVIP`, or `APPVIP`. |
| ``` -vip vip_resource_name ``` | Specify the name of the VIP resource. This parameter is required if you specify the `APPVIP` VIP type. |
| ``` -n node_name ``` | Specify the name of the node for which you want to obtain the client ID. This parameter is required if you specify the `HOSTVIP` VIP type. |

Example

The `crsctl get clientid dhcp` command returns output similar to the following:

```
$ crsctl get clientid dhcp -cluname stmjk0462clr -viptype HOSTVIP -n stmjk01

CRS-10007: stmjk0462clr-stmjk01-vip
```

#### crsctl get css

Use the `crsctl get css` command to obtain the value of a specific Cluster Synchronization Services parameter.

Syntax

```
crsctl get css parameter
```

Usage Notes

- Cluster Synchronization Services parameters and their default values include:
	```
	clusterguid
	diagwait
	disktimeout (200 (seconds))
	misscount (30 (seconds))
	reboottime (3 (seconds))
	priority (4 (UNIX), 3 (Windows))
	logfilesize (50 (MB))
	```
- This command does not display default values
- This command only affects the local server

Example

The `crsctl get css disktimeout` command returns output similar to the following:

```
$ crsctl get css disktimeout
CRS-4678: Successful get disktimeout 200 for Cluster Synchronization Services.
```

#### crsctl get css ipmiaddr

Use the `crsctl get css ipmiaddr` command to get the address stored in the Oracle Local Registry of the local Intelligent Platform Management Interface (IPMI) device.

Syntax

```
crsctl get css ipmiaddr
```

Usage Notes

- Run the command under the user account used to install Oracle Clusterware.
- This command only obtains the IP address stored in the Oracle Local Registry. It may not be the IP address actually used by IPMI.
	Use either `ipmiutil` or `ipmitool` as `root` on the local server to obtain the IP address used by the IPMI device.

Example

To obtain the IPMI device IP address:

```
$ crsctl get css ipmiaddr
```

#### crsctl get nodename

Use the `crsctl get nodename` command to obtain the name of the local node.

Syntax

```
crsctl get nodename
```

Example

The `crsctl get nodename` command returns output similar to the following:

```
node2
```

#### crsctl getperm serverpool

Use the `crsctl getperm serverpool` command to obtain permissions for a particular server pool.

Syntax

```
crsctl getperm serverpool server_pool_name  [-u user_name | -g group_name]
```

See Also:

["Understanding Server Pools"](admin.md) for more information about server pools and server pool attributes

Parameters

Table E-23 crsctl getperm serverpool Command Parameters

| Parameter | Description |
| --- | --- |
| ``` server_pool_name ``` | Specify the name of the server pool for which you want to obtain permissions. |
| ``` -u user_name ``` | If you specify `-u`, then Oracle Clusterware obtains permissions for a particular user. |
| ``` -g group_name ``` | If you specify `-g`, then Oracle Clusterware obtains permissions for a particular group. |

Usage Notes

- The `server_pool_name` parameter is required
- Do not use this command for any server pools with names that begin with ora because these server pools are Oracle server pools
- While you can use this command in either environment, it is only useful in the Oracle RAC environment

Example

The `crsctl getperm serverpool` command returns output similar to the following:

```
$ crsctl getperm serverpool sp1
NAME: sp1
owner:root:rwx,pgrp:root:r-x,other::r--
```

#### crsctl lsmodules

Use the `crsctl lsmodules` command to list the components of the modules that you can debug.

See Also:

"Dynamic Debugging" for more information about debugging

Syntax

```
crsctl lsmodules {mdns | gpnp | css | crf | crs | ctss | evm | gipc}
```

Usage Notes

You can specify any of the following components:

  
`mdns`: Multicast domain name server  
`gpnp`: Grid Plug and Play service  
`css`: Cluster Synchronization Services  
`crf`: Cluster Health Monitor  
`crs`: Cluster Ready Services  
`ctss`: Cluster Time Synchronization Service  
`evm`: Event Manager  
`gipc`: Grid Interprocess Communication

Example

The `crsctl lsmodules` command returns output similar to the following:

```
$ crsctl lsmodules evm
List EVMD Debug Module: CLSVER
List EVMD Debug Module: CLUCLS
List EVMD Debug Module: COMMCRS
List EVMD Debug Module: COMMNS
List EVMD Debug Module: CRSOCR
List EVMD Debug Module: CSSCLNT
List EVMD Debug Module: EVMAGENT
List EVMD Debug Module: EVMAPP
...
```

#### crsctl modify serverpool

Use the `crsctl modify serverpool` command to modify an existing server pool.

Syntax

```
crsctl modify serverpool server_pool_name -attr "attr_name=attr_value
                      [,attr_name=attr_value
[, ...]]" [-i] [-f]
```

Parameters

Table E-24 crsctl modify serverpool Command Parameters

| Parameter | Description |
| --- | --- |
| ``` server_pool_name ``` | The name of the server pool you want to modify. |
| ``` attr_name ``` | The name of a server pool attribute you want to modify preceded by the `-attr` flag.  See Also: [Table 2-2, "Server Pool Attributes"](admin.md) for details about server pool attributes |
| ``` attr_value ``` | A value for the server pool attribute.  Note: The `attr_name` and `attr_value` parameters must be enclosed in double quotation marks (`""`) and separated by commas. For example:  ``` -attr "CHECK_INTERVAL=30,START_TIMEOUT=25" ```  See Also: [Table 2-2, "Server Pool Attributes"](admin.md) for details about server pool attributes |
| ``` -i ``` | If you specify `-i`, then the command fails if Oracle Clusterware cannot process the request immediately. |
| ``` -f ``` | If you specify the `-f` option, then Oracle Clusterware stops resources running on a server in another server pool and relocates that server into the server pool you are adding.  If you do not specify the `-f` option, then Oracle Clusterware checks whether the creation of the server pool results in stopping any resources on a server in another server pool that is going to give up a server to the server pool you are adding. If so, then Oracle Clusterware rejects the `crsctl add serverpool` command. |

See Also:

["Understanding Server Pools"](admin.md) for more information about server pools and server pool attributes

Usage Notes

- You must run this command as `root`
- The `server_pool_name` parameter is required
- If an attribute value for an attribute name-value pair contains commas, then the value must be enclosed in single quotation marks (`''`). For example:
	```
	"START_DEPENDENCIES='hard(res1,res2,res3)'"
	```
- Running this command may result in Oracle Clusterware relocating other servers between server pools to comply with the new configuration
- Do not use this command for any server pools with names that begin with ora because these server pools are Oracle server pools
- While you can use this command in either environment, it is only useful in the Oracle RAC environment

Example

To modify an existing server pool, run the following command as `root` or the Oracle Clusterware installation owner:

```
# crsctl modify serverpool sp1 -attr "MAX_SIZE=7"
```

#### crsctl pin css

Use the `crsctl pin css` command to pin many specific nodes. Pinning a node means that the association of a node name with a node number is fixed. If a node is not pinned, its node number may change if the lease expires while it is down. The lease of a pinned node never expires.

Syntax

```
crsctl pin css -n node_name
 [ node_name
 [..]]
```

Usage Notes

- You can specify a space-delimited list of servers
- Any pre-11g release 2 (11.2) Oracle software must reside on a pinned server.
- A node may be unpinned with `crsctl unpin css`.
- Deleting a node with the `crsctl delete node` command implicitly unpins the node.

Example

To pin the node named `node2`:

```
# crsctl pin css -n node2
```

#### crsctl query crs administrator

Use the `crsctl query crs administrator` command to display the list of users with Oracle Clusterware administrative privileges.

Syntax

```
crsctl query crs administrator
```

Example

The `crsctl query crs administrator` command returns output similar to the following:

```
CRS Administrator List: scott
```

#### crsctl query crs activeversion

Use the `crsctl query crs activeversion` command to display the active version of the Oracle Clusterware software running in the cluster. During a rolling upgrade, however, the active version is not advanced until the upgrade is finished across the cluster, until which time the cluster operates at the pre-upgrade version.

Syntax

```
crsctl query crs activeversion
```

Example

The `crsctl query crs activeversion` command returns output similar to the following:

```
Oracle Clusterware active version on the cluster is [11.2.0.2.0]"
```

#### crsctl query crs releaseversion

Use the `crsctl query crs releaseversion` command to display the version of the Oracle Clusterware software stored in the binaries on the local node.

Syntax

```
crsctl query crs releaseversion
```

Example

The `crsctl query crs releaseversion` command returns output similar to the following:

```
Oracle High Availablity Services release version on the local node is [11.2.0.2.0]
```

#### crsctl query crs softwareversion

Use the `crsctl query crs softwareversion` command to display latest version of the software that has been successfully started on the specified node.

Syntax

```
crsctl query crs softwareversion node_name
```

Usage Notes

- If you do not provide a node name, then Oracle Clusterware displays the version of Oracle Clusterware running on the local server.

Example

The `crsctl query crs softwareversion` command returns output similar to the following:

```
Oracle Clusterware version on node [node1] is [11.2.0.2.0]
```

#### crsctl query css ipmiconfig

Starting with Oracle Database 11g release 2 (11.2.0.2), use the `crsctl query css ipmiconfig` command to determine whether Oracle Clusterware on the local server has been configured to use IPMI for failure isolation. Note that this command detects the presence of configuration data, but cannot not validate its correctness.

Syntax

```
crsctl query css ipmiconfig
```

Usage Notes

- This command attempts to locate and access the IPMI configuration stored in the Oracle Cluster Registry (OCR) and should be executed under the account used to install Oracle Clusterware, or an authorization failure may be reported.
- An authorization failure may not result when executed under another account, if the registry contains no IPMI configuration data.

Example

The `crsctl query css ipmiconfig` command returns output similar to the following:

```
CRS-4236: Oracle Clusterware configured to use IPMI
```

Or

```
CRS-4237: Oracle Clusterware is not fully configured to use IPMI
```

#### crsctl query css ipmidevice

Use the `crsctl query css ipmiconfig` command to determine the presence of the Intelligent Platform Management Interface (IPMI) driver on the local system.

Syntax

```
crsctl query css ipmidevice
```

Usage Notes

- This command performs a pre-check during IPMI installation, and is normally issued only by the installer.
- This command performs a perfunctory check and a success return does not guarantee that the IPMI hardware is fully configured for use.
- There are no special privileges required to run this command.

Example

The `crsctl query css ipmidevice` command returns output similar to the following:

```
CRS-4231: IPMI device and/or driver found
```

Or

```
CRS-4218: Unable to access an IPMI device on this system
```

#### crsctl query css votedisk

Use the `crsctl query css votedisk` command to display the voting disks used by Cluster Synchronization Services, the status of the voting disks, and the location of the disks, whether they are stored on Oracle ASM or elsewhere.

Syntax

```
crsctl query css votedisk
```

Usage Notes

Example

The `crsctl query css votedisk` command returns output similar to the following:

```
$ crsctl query css votedisk
##  STATE    File Universal Id                File Name Disk group
--  -----    -----------------                --------- ---------
1. ONLINE   296641fd201f4f3fbf3452156d3b5881 (/ocfs2/host09_vd3) []
2. ONLINE   8c4a552bdd9a4fd9bf93e444223146f2 (/netapp/ocrvf/newvd) []
3. ONLINE   8afeee6ae3ed4fe6bfbb556996ca4da5 (/ocfs2/host09_vd1) []
Located 3 voting disk(s).
```

#### crsctl query dns

Starting with Oracle Database 11g release 2 (11.2.0.2), use the `crsctl query dns` command to obtain a list of addresses returned by DNS lookup of the name with the specified DNS server.

Syntax

```
crsctl query dns {-servers | -name name [-dnsserver DNS_server_address]
[-port port] [-attempts number_of_attempts] [-timeout timeout_in_seconds] [-v]}
```

Parameters

Table E-25 crsctl query dns Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -servers ``` | Use the `-servers` parameter to list the current DNS configuration of the node on which you run the command. Typically, on Linux/UNIX, CRSCTL reads the `/etc/resolv.conf` file at boot time and that is what the system configuration is until you reboot or until the resolver is restarted. CRSCTL gets its information from resolver. You can use this parameter or, optionally, you can specify the other parameters in the command syntax string. |
| ``` -name name ``` | Specify the fully-qualified domain name you want to look up. |
| ``` -dnsserver DNS_server_address ``` | Specify the address of the DNS server on which you want the domain name to be looked up. |
| ``` -port port ``` | The port on which the DNS server listens. If you do not specify a port, then it defaults to port 53. |
| ``` -attempts number_of_attempts ``` | Specify the number of retry attempts. |
| ``` -timeout timeout_in_seconds ``` | Specify the timeout length in seconds. |
| ``` -v ``` | Verbose output. |

Example

The `crsctl query dns` command returns output similar to the following for a DNS server named `stmjk07-vip.stmjk0462.foo.com`:

```
CRS-10024: DNS server returned 192.168.29.250 for name
stmjk07-vip.stmjk0462.foo.com
```

If you choose the `-servers` option, then the command returns output similar to the following:

```
CRS-10018: the following configuration was found on the system:
CRS-10019: There are 3 domains in search order. They are:
us.foo.com
foo.com
foocorp.com
CRS-10022: There are 3 name servers. They are:
192.168.249.41
192.168.249.52
192.168.202.15
CRS-10020: number of retry attempts for name lookup is: 2
CRS-10021: timeout for each name lookup is: 1
```

#### crsctl release dhcp

Starting with Oracle Database 11g release 2 (11.2.0.2), use the `crsctl release dhcp` command to send a DHCP lease release request to a specific client ID and send release packets on the network to a specific port.

Syntax

```
crsctl release dhcp -clientid clientid [-port port]
```

Parameters

Table E-26 crsctl release dhcp Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -clientid clientid ``` | Specify the client ID for which you want to attempt release. Obtain the client ID by running the `crsctl get clientid` command. |
| ``` -port port ``` | The port to which CRSCTL sends the release packets. If you do not specify a port, then CRSCTL uses the default value 67. |

Example

The `crsctl release dhcp` command returns output similar to the following:

```
$ crsctl release dhcp -clientid  stmjk0462clr-stmjk01-vip

CRS-10012: released DHCP server lease for client ID stmjk0462clr-stmjk01-vip
on port 67
```

#### crsctl relocate resource

Use the `crsctl relocate resource` command to relocate resources to another server in the cluster.

Syntax

```
crsctl relocate resource {resource_name | resource_name | -all -s source_server |
-w "filter"} [-n destination_server] [-k cid] [-env "env1=val1,env2=val2,..."]
[-i] [-f]
```

Parameters

Table E-27 crsctl relocate resource Command Parameters

| Parameter | Description |
| --- | --- |
| ``` resource_name ``` | The name of a resource you want to relocate. |
| ``` resource_name \| -all -s source_server ``` | Specify one particular or all resources located on a particular server from which you want to relocate those resources. |
| ``` -w "filter" ``` | Specify a resource filter that Oracle Clusterware uses to limit the number of resources relocated. The filter must be enclosed in double quotation marks (`""`). Examples of resource filters include:  - `"TYPE == cluster_resource"`: This filter limits Oracle Clusterware to relocate only resources of `cluster_resource` type - `"CHECK_INTERVAL > 10"`: This filter limits Oracle Clusterware to relocate resources that have a value greater than 10 for the `CHECK_INTERVAL` resource attribute - `"(CHECK_INTERVAL > 10) AND (NAME co 2)"`: This filter limits Oracle Clusterware to relocate resources that have a value greater than 10 for the `CHECK_INTERVAL` resource attribute and the name of the resource contains the number `2` |
| ``` -n destination_server ``` | Specify the name of the server to which you want relocate resources. If you do not specify a destination server, then Oracle Clusterware relocates the resources to the best server according to the attribute profile of each resource. |
| ``` -k cid ``` | Specify the resource cardinality ID. If you specify this parameter, then Oracle Clusterware relocates the resource instance that have the cardinality you specify. |
| ``` -env "env1=val1, env2=val2,..." ``` | You can optionally override one or more resource profile attribute values for this command. If you specify multiple environment name-value pairs, then you must separate each pair with a comma and enclose the entire list in double quotation marks (`""`). |
| ``` -i ``` | If you specify `-i`, then the command returns an error if processing this command requires waiting for Oracle Clusterware to unlock the resource or its dependents. Sometimes, Oracle Clusterware locks resources or other objects to prevent commands from interfering with each other. |
| ``` -f ``` | Specify the `-f` option to force the relocating of the resource when it has other resources running that depend on it. Dependent resources are relocated or stopped when you use this option.  Note: When you are relocating resources that have cardinality greater than 1, you must use either `-k` or `-s` to narrow down which resource instances are to be relocated. |

Usage Notes

- Any one of the three following options is required to specify which resources you want to relocate:
	- You can specify one particular resource to relocate.
		- Or you can specify one particular or all the resources to relocate from a particular source server.
		- Thirdly, you can specify a resource filter that Oracle Clusterware uses to match resources to relocate.
- If a resource has a degree ID greater than 1, then Oracle Clusterware relocates all instances of the resource.
- You must have read and execute permissions on the specified resources to relocate them
- Do not use this command for any resources with names that begin with ora because these resources are Oracle resources.

Example

To relocate one particular resource from one server to another:

```
# crsctl relocate resource myResource1 -s node1 -n node3
```

#### crsctl relocate server

Use the `crsctl relocate server` command to relocate a server to a different server pool.

Syntax

```
crsctl relocate server server_name [...] -c server_pool_name [-i] [-f]
```

Parameters

Table E-28 crsctl relocate server Command Parameters

| Parameter | Description |
| --- | --- |
| ``` server_name ``` | The name of the server you want to relocate. You can provide a space-delimited list of servers if you want to relocate multiple servers. |
| ``` -c server_pool_name ``` | Specify the name of the server pool to which you want relocate the servers. |
| ``` -i ``` | If you specify `-i`, then the command fails if Oracle Clusterware cannot process the request immediately. |
| ``` -f ``` | If you specify the `-f` option, then Oracle Clusterware stops resources running on the servers in another server pool and relocates that server into the server pool you specified.  If you do not specify the `-f` option, then Oracle Clusterware checks for resources that must be stopped on the servers that are being relocated. If it finds any, then Oracle Clusterware rejects the `crsctl relocate server` command. |

Usage Notes

- The `server_name` and `-c` `server_pool_name` parameters are required

Example

To move the `node6` and `node7` servers into the `sp1` server pool without disrupting any active resources on those nodes, use the following command:

```
$ crsctl relocate server node6 node7 -c sp1
```

#### crsctl replace discoverystring

Use the `crsctl replace discoverystring` command to replace the existing discovery string used to locate voting disk files.

Syntax

```
crsctl replace discoverystring "absolute_path
[,...]"
```

Parameters

Table E-29 crsctl replace discoverystring Command Parameters

| Parameter | Description |
| --- | --- |
| ``` absolute_path ``` | Specify one or more comma-delimited absolute paths that match one or more voting disk file locations. Wildcards may be used.  The list of paths must be enclosed in double quotation marks (`""`). |

Usage Notes

- You must be `root`, the Oracle Clusterware installation owner, or a member of the Administrators group to run this command.
- You can run this command on any node in the cluster.

Example

Assume the current discovery string is `/oracle/css1/*`. To also use voting disk files in the `/oracle/css2/` directory, replace the current discovery string using the following command:

```
# crsctl replace discoverystring "/oracle/css1/*,/oracle/css2/*"
```

#### crsctl replace votedisk

Use the `crsctl replace votedisk` command to move or replace the existing voting disks. This command creates voting disks in the specified locations, either in Oracle ASM or some other storage option. Oracle Clusterware copies existing voting disk information into the new locations and removes the voting disks from the former locations.

Syntax

```
crsctl replace votedisk [+asm_disk_group | path_to_voting_disk [...]]
```

Parameters

Table E-30 crsctl replace votedisk Command Parameters

| Parameter | Description |
| --- | --- |
| \+ `asm_disk_group` | Specify the disk group in Oracle ASM where you want to locate the voting disk. |
| `path_to_voting_disk` \[...\] | A space-delimited list of voting disk file paths for voting disk files that reside outside of Oracle ASM. |

Usage Notes

- You must be `root`, the Oracle Clusterware installation owner, or a member of the Administrators group to run this command.
- Specify to replace a voting disk in either an Oracle ASM disk group or in some other storage device.
- You can run this command on any node in the cluster.

Example

Example 1

To replace a voting disk that is located within Oracle ASM:

```
$ crsctl replace votedisk +diskgroup1
```

Example 2

To replace a voting disk that is located on a shared file system:

```
$ crsctl replace votedisk /mnt/nfs/disk1 /mnt/nfs/disk2
```

#### crsctl request dhcp

Starting with Oracle Database 11g release 2 (11.2.0.2), use the `crsctl request dhcp` command to send DHCP request packets on the network at the specified port. If the DHCP server has an IP address it can provide, then it responds with the IP address for the client ID.

Syntax

```
crsctl request dhcp -clientid clientid [-port port]
```

Parameters

Table E-31 crsctl request dhcp Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -clientid clientid ``` | Specify the client ID for which you want to attempt request. Obtain the client ID by running the `crsctl get clientid` command. |
| ``` -port port ``` | The port to which CRSCTL sends the request packets. If you do not specify a port, then CRSCTL uses the default value 67. |

Example

The `crsctl request dhcp` command returns output similar to the following:

```
$ crsctl request dhcp -clientid stmjk0462clr-stmjk01-vip

CRS-10009: DHCP server returned server: 192.168.53.232,
 loan address : 192.168.29.228/255.255.252.0, lease time: 43200
```

#### crsctl set css

Use the `crsctl set css` command to set the value of a Cluster Synchronization Services parameter.

Syntax

```
crsctl set css parameter value
```

Usage Notes

- Do not use the `crsctl set css` command to set the following parameters unless instructed to do so by My Oracle Support.
- Cluster Synchronization Services parameters include:
	```
	diagwait
	disktimeout
	logfilesize
	misscount
	priority
	reboottime
	```

#### crsctl set css ipmiaddr

Use the `crsctl set css ipmiaddr` command to store the address of the local Intelligent Platform Management Interface (IPMI) device in the Oracle Local Registry.

Syntax

```
crsctl set css ipmiaddr ip_address
```

Usage Notes

- Run the command under the user account used to install Oracle Clusterware
- Obtain the IP address used by the IPMI device using either `ipmiutil` or `ipmitool` as `root` on the local server
- Oracle Clusterware stores the IP address for IPMI in the configuration store, and distributes the address as required
- This command only stores the IPMI IP address on the server from which you run it
- This command fails if another server cannot access IPMI at the supplied address

Example

To store the IPMI IP address on a local server and distribute it to other cluster nodes:

```
$ crsctl set css ipmiaddr 192.0.2.244
```

#### crsctl set css ipmiadmin

Use the `crsctl set css ipmiadmin` command to store the login credentials of an Intelligent Platform Management Interface (IPMI) administrator in the Oracle Local Registry.

Syntax

```
crsctl set css ipmiadmin ipmi_administrator_name
```

Usage Notes

- This command must be run under the user account that installed Oracle Clusterware.
- When prompted, provide the new password to associate with the new administrator account name. Oracle Clusterware stores the name and password for the local IPMI in the configuration store, and distributes the new credentials as required.
- This command only modifies the IPMI administrator on the server from which you run it.
- This command fails if another server cannot access the local IPMI at the supplied address.

Example

To modify the IPMI administrator `scott`:

```
$ crsctl set css ipmiadmin scott
```

#### crsctl setperm serverpool

Use the `crsctl setperm serverpool` command to set permissions for a particular server pool.

Syntax

```
crsctl setperm serverpool server_pool_name {-u acl_string | -x acl_string |
-o user_name | -g group_name}
```

Parameters

Table E-32 crsctl setperm serverpool Command Parameters

| Parameter | Description |
| --- | --- |
| ``` server_pool_name ``` | Specify the name of the server pool for which you want to set permissions. |
| ``` {-u \| -x \| -o \| -g} ``` | You can specify only one of the following parameters for a server pool:  - `-u` `acl_string`: You can update the access control list (ACL) for a server pool - `-x` `acl_string`: You can delete the ACL for a server pool - `-o` `user_name`: You can change the owner of a server pool by entering a user name - `-g` `group_name`: You can change the primary group of a server pool by entering a group name  Specify a user, group, or other ACL string, as follows:  ``` user:user_name[:readPermwritePermexecPerm] \| group:group_name[:readPermwritePermexecPerm] \| other[::readPermwritePermexecPerm] ``` - `user`: User ACL - `group`: Group ACL - `other`: Other ACL - `readPerm`: Read permission for the server pool; the letter `r` grants a user, group, or other read permission, the minus sign (`-`) denies read permission - `writePerm`: Write permission for the server pool; the letter `w` grants a user, group, or other write permission, the minus sign (`-`) denies write permission - `execPerm`: Execute permission for the server pool; the letter `x` grants a user, group, or other execute permission, the minus sign (`-`) denies execute permission |

Usage Notes

- The `server_pool_name` parameter is required
- Do not use this command for any server pools with names that begin with ora because these server pools are Oracle server pools
- While you can use this command in either environment, it is only useful in the Oracle RAC environment

Example

To grant read, write, and execute permissions on a server pool for user Scott Tiger:

```
crsctl setperm serverpool sp3 -u user:scott.tiger:rwx
```

#### crsctl start cluster

Use the `crsctl start cluster` command on any node in the cluster to start the Oracle Clusterware stack.

Syntax

```
crsctl start cluster [-all | -n server_name [...]]
```

Usage Notes

- You can choose to start the Oracle Clusterware stack on all servers in the cluster, on one or more named servers in the cluster (separate multiple server names by a space), or the local server, if you do not specify either `-all` or `-n`.
- You can use this cluster-aware command on any node in the cluster.

Example

To start the Oracle Clusterware stack on two named servers run the following command as `root`:

```
# crsctl start cluster -n node1 node2
```

#### crsctl start crs

Use the `crsctl start crs` command to start Oracle High Availability Services on the local server.

Syntax

```
crsctl start crs
```

Usage Notes

- This command starts Oracle High Availability Services only on the local server

Example

To start Oracle High Availability Services on the local server, run the following command as `root`:

```
# crsctl start crs
```

#### crsctl start ip

Starting with Oracle Database 11g release 2 (11.2.0.2), use the `crsctl start ip` command to start a given IP name or IP address on a specified interface with a specified subnet mask. Run this command on the server on which you want to bring up the IP.

Syntax

```
crsctl start ip -A {IP_name | IP_address}/netmask/interface_name
```

Parameters

Table E-33 crsctl start ip Command Parameters

| Parameter | Description |
| --- | --- |
| ``` {IP_name \| IP_address} ``` | Specify either a domain name or an IP address.  If you do not specify a fully-qualified domain name, then CRSCTL uses a standard name search. |
| ``` netmask ``` | Specify a subnet mask for the IP to start. |
| ``` interface_name ``` | Specify an interface on which to start the IP. |

Example

To start an IP on the local server, run the command similar to the following:

```
$ crsctl start ip -A 192.168.29.220/255.255.252.0/eth0
```

#### crsctl start testdns

Starting with Oracle Database 11g release 2 (11.2.0.2), use the `crsctl start testdns` command to start a test DNS server that will listen on a specified IP address and port. The test DNS server does not respond to incoming packets but does display the packets it receives. Typically, use this command to check if domain forwarding is set up correctly for the GNS domain.

Syntax

```
crsctl start testdns [-address address [-port port]] [-once] [-v]
```

Parameters

Table E-34 crsctl start testdns Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -address address ``` | Specify a server address in the form `IP_address` `/` `netmask` `[/` `interface_name``]`. |
| ``` -port port ``` | The port on which the server listens. If you do not specify a port, then it defaults to port 53. |
| ``` -once ``` | Specify this flag to indicate that the DNS server should exit after it receives one DNS query packet. |
| ``` -v ``` | Verbose output. |

Example

To start a test DNS server on the local server, run the command similar to the following:

```
$ crsctl start testdns -address 192.168.29.218 -port 63 -v
```

#### crsctl status ip

Starting with Oracle Database 11g release 2 (11.2.0.2), use the `crsctl status ip` command to check if a given IP address is up on the network.

Syntax

```
crsctl status ip -A {IP_name | IP_address}
```

Parameters

Table E-35 crsctl status ip Command Parameters

| Parameter | Description |
| --- | --- |
| ``` {IP_name \| IP_address} ``` | Specify either a domain name or an IP address.  If you do not specify a fully-qualified domain name, then CRSCTL uses a standard name search. |

Example

The `crsctl status ip` command returns output similar to the following:

```
CRS-10003: IP address 192.168.29.220 could be reached from current node
```

#### crsctl status server

Use the `crsctl status server` command to obtain the status and configuration information of one or more particular servers.

Syntax

```
crsctl status server [-p | -v | -f]

crsctl status server { server_name [...] | -w "filter"} [-g | -p | -v | -f]
```

Parameters

Table E-36 crsctl status server Command Parameters

| Parameter | Description |
| --- | --- |
| ``` server_name [...] ``` | Specify one or more space-delimited server names. |
| ``` -w "filter" ``` | Specify a filter to determine which servers are displayed. The filter must be enclosed in double quotation marks (`""`). Values that contain parentheses or spaces must be enclosed in single quotation marks (`''`). For example, `"STATE = ONLINE"` limits the display to servers that are online.  See Also: ["Filters"](crs_api.md) for more information about filters |
| ``` -g \| -p \| -v \| -f ``` | You can specify one of the following parameters when Oracle Clusterware checks the status of specific servers:  - `-g`: Use this parameter to check if the specified servers are registered - `-p`: Use this parameter to display static configuration of the specified servers - `-v`: Use this parameter to display the run-time configuration of the specified servers - `-f`: Use this parameter to display the full configuration of the specified servers |

Example

Example 1

The `crsctl status server` command returns output similar to the following:

```
NAME=node1
STATE=ONLINE

NAME=node2
STATE=ONLINE
```

Example 2

To display the full configuration of a specific server, enter a command similar to the following:

```
$ crsctl status server node2 -f
NAME=node2
STATE=ONLINE
ACTIVE_POOLS=Generic ora.orcl
STATE_DETAILS=
```

#### crsctl status serverpool

Use the `crsctl status serverpool` command to obtain the status and configuration information of one or more particular server pools.

Syntax

```
crsctl status serverpool [-p | -v | -f]

crsctl status serverpool [server_pool_name [...]] [-w] [-g | -p | -v | -f]
```

Parameters

Table E-37 crsctl status serverpool Command Parameters

| Parameter | Description |
| --- | --- |
| ``` [server_pool_name [...] ``` | Specify one or more space-delimited server pool names. |
| ``` [-g \| -p \| -v \| -f] ``` | You can optionally specify one of the following parameters:  - `-w`: Use this parameter to specify a filter, such as `MIN_SIZE > 3`, surrounded by double quotation marks (`""`) - `-g`: Use this parameter to check if the specified server pools are registered - `-p`: Use this parameter to display static configuration of the specified server pools - `-v`: Use this parameter to display the run-time configuration of the specified server pools - `-f`: Use this parameter to display the full configuration of the specified server pools |

Usage Notes

- The `server_pool_name` parameter or a filter is required
- Do not use this command for any server pools with names that begin with ora because these server pools are Oracle server pools
- While you can use this command in either environment, it is only useful in the Oracle RAC environment

Examples

Example 1

To display the full configuration of the server pool `sp1`:

```
$ crsctl status serverpool sp1 -f 
NAME=spl
IMPORTANCE=1
MIN_SIZE=0
MAX_SIZE=-1
SERVER_NAMES=node3 node4 node5
PARENT_POOLS=Generic
EXCLUSIVE_POOLS=
ACL=owner:oracle:rwx,pgrp:oinstall:rwx,other::r--
ACTIVE_SERVERS=node3 node4
```

Example 2

To display all the server pools and the servers associated with them, use the following command:

```
$ crsctl status serverpool
NAME=Free
ACTIVE_SERVERS=

NAME=Generic
ACTIVE_SERVERS=node1 node2

NAME=ora.orcl
ACTIVE_SERVERS=node1 node2

NAME=sp1
ACTIVE_SERVERS=node3 node4
```

Example 3

To find a server pool that meets certain criteria, use the following command:

```
$ crsctl status serverpool -w "MAX_SIZE > 1"
NAME=sp2
ACTIVE_SERVERS=node3 node4
```

#### crsctl status testdns

Starting with Oracle Database 11g release 2 (11.2.0.2), use the `crsctl status testdns` command to query the test DNS server running on a specified address and local host name.

Syntax

```
crsctl status testdns [-server DNS_server_address] [-port port] [-v]
```

Parameters

Table E-38 crsctl status testdns Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -server DNS_server_address ``` | Specify the DNS server address for which you want to check the status. |
| ``` -port port ``` | The port on which the DNS server listens. If you do not specify a port, then it defaults to port 53. |
| ``` -v ``` | Verbose output. |

Example

The `crsctl status testdns` command returns output similar to the following:

```
CRS-10024: DNS server returned 192.168.28.74 for name
stmjk07-vip.stmjk0462.foo.com
```

#### crsctl stop cluster

Use the `crsctl stop cluster` command on any node in the cluster to stop the Oracle Clusterware stack on all servers in the cluster or specific servers.

Syntax

```
crsctl stop cluster [-all | -n server_name [...]] [-f]
```

Usage Notes

- If you do not specify `-all` or one or more space-delimited server names, then Oracle Clusterware stops the Oracle Clusterware stack on the local server.
- You can use this cluster-aware command on any node in the cluster.
- This command attempts to gracefully stop resources managed by Oracle Clusterware while attempting to stop the Oracle Clusterware stack.
	If any resources that Oracle Clusterware manages are still running after you run the `crsctl stop cluster` command, then the command fails. Use the `-f` option to unconditionally stop all resources and stop the Oracle Clusterware stack.
- If you intend to stop Oracle Clusterware on all or a list of nodes, then use the `crsctl stop cluster` command, because it prevents certain resources from being relocated to other servers in the cluster before the Oracle Clusterware stack is stopped on a particular server. If you must stop the Oracle High Availability Services on one or more nodes, then wait until the `crsctl stop cluster` command completes and then run the `crsctl stop crs` command on any particular nodes, as necessary.

Example

To stop the Oracle Clusterware stack on a particular server:

```
# crsctl stop cluster -n node1
```

#### crsctl stop crs

Use the `crsctl stop crs` command to stop Oracle High Availability Services on the local server.

Syntax

```
crsctl stop crs [-f]
```

Usage Notes

- This command attempts to gracefully stop resources managed by Oracle Clusterware while attempting to stop Oracle High Availability Services on the local server.
	If any resources that Oracle Clusterware manages are still running after you run the `crsctl stop crs` command, then the command fails. Use the `-f` option to unconditionally stop all resources and stop Oracle High Availability Services on the local server.
- If you intend to stop Oracle Clusterware on all or a list of nodes, then use the `crsctl stop cluster` command, because it prevents certain resources from being relocated to other servers in the cluster before the Oracle Clusterware stack is stopped on a particular server. If you must stop the Oracle High Availability Services on one or more nodes, then wait until the `crsctl stop cluster` command completes and then run the `crsctl stop crs` command on any particular nodes, as necessary.
- In Oracle Clusterware 11g release 2 (11.2.0.3), when you run this command in Solaris Sparc and Solaris X64 environments, drivers remain loaded on shutdown and subsequent startup. This does not happen in Linux environments.

Example

To stop Oracle High Availability Services on the local server:

```
# crsctl stop crs
```

#### crsctl stop ip

Starting with Oracle Database 11g release 2 (11.2.0.2), use the `crsctl stop ip` command to stop a given IP name or IP address on a specified interface with a specified subnet mask. Run this command on the server on which you want to stop the IP.

Syntax

```
crsctl stop ip -A {IP_name | IP_address}/interface_name
```

Parameters

Table E-39 crsctl stop ip Command Parameters

| Parameter | Description |
| --- | --- |
| ``` {IP_name \| IP_address} ``` | Specify either a domain name or an IP address.  If you do not specify a fully-qualified domain name, then CRSCTL uses a standard name search. |
| ``` interface_name ``` | Specify an interface on which to start the IP. |

Example

To stop an IP on the local server, run the command similar to the following:

```
$ crsctl stop ip -A MyIP.domain.com/eth0
```

#### crsctl stop testdns

Starting with Oracle Database 11g release 2 (11.2.0.2), use the `crsctl stop testdns` command to stop a test DNS server.

Syntax

```
crsctl stop testdns [-address address [-port port]] [-domain GNS_domain] [-v]
```

Parameters

Table E-40 crsctl stop testdns Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -address address ``` | Specify the server address for which you started the test DNS server in the form `IP_address` `/` `netmask` `[/` `interface_name``]`. |
| ``` -port port ``` | The port on which the DNS server listens. If you do not specify a port, then it defaults to port 53. |
| ``` [-domain GNS_domain] ``` | Domain for which the server should stop listening. |
| ``` -v ``` | Verbose output. |

Example

The `crsctl stop testdns` command returns output similar to the following:

```
CRS-10032: successfully stopped the DNS listening daemon running on port 53 on
local node
```

#### crsctl unpin css

Use the `crsctl unpin css` command to unpin many servers. If a node is not pinned, its node number may change if the lease expires while it is down.

Syntax

```
crsctl unpin css -n node_name
 [node_name
 [...exit]]
```

Usage Notes

- You can specify a space-delimited list of nodes.
- Unpinned servers that stop for longer than a week are no longer reported by `olsnodes`. These servers are dynamic when they leave the cluster, so you do not need to explicitly remove them from the cluster.
- Deleting a node with the `crsctl delete node` command implicitly unpins the node.
- During upgrade of Oracle Clusterware, all servers are pinned, whereas after a fresh installation of Oracle Clusterware 11g release 2 (11.2), all servers you add to the cluster are unpinned.
- You cannot unpin a server that has an instance of Oracle RAC that is older than 11g release 2 (11.2) if you installed Oracle Clusterware 11g release 2 (11.2) on that server.

Example

To unpin two nodes:

```
$ crsctl unpin css -n node1 node4
```

#### crsctl unset css

Use the `crsctl unset css` command to unset the value of a Cluster Synchronization Services parameter and restore it to its default value.

Syntax

```
crsctl unset css parameter
```

Usage Notes

- You can specify the following Cluster Synchronization Services parameters:
	- `diagwait`
		- `disktimeout`
		- `misscount`
		- `reboottime`
		- `priority`
		- `logfilesize`

Example

To restore the `reboottime` Cluster Synchronization Services parameter to its default value:

```
$ crsctl unset css reboottime
```

#### crsctl unset css ipmiconfig

Starting with Oracle Database 11g release 2 (11.2.0.2), use the `crsctl unset css ipmiconfig` command to clear all previously stored IPMI configuration (login credentials and IP address) from the Oracle Local Registry. This is appropriate when deconfiguring IPMI in your cluster or if IPMI configuration was previously stored by the wrong user.

Syntax

```
crsctl unset css ipmiconfig
```

Usage Notes

- This command must be run under the user account originally used to configure IPMI or by a privileged user.
- This command only clears the IPMI configuration on the server on which you run it.
- If Oracle Clusterware was able to access and use the configuration data to be deleted by this command, then it will continue to do so until you restart Oracle Clusterware.

Example

To clear the IPMI configuration data from the Oracle Local Registry and restart Oracle Clusterware to prevent further use of IPMI, log in as `root` or a member of the Administrator's group on Windows and run the following commands:

```
crsctl unset css ipmiconfig
crsctl stop crs
crsctl start crs
```

### Oracle Restart Environment CRSCTL Commands

The commands listed in this section control Oracle High Availability Services. These commands manage the Oracle High Availability Services stack in the Oracle Restart environment, which consists of the Oracle High Availability Services daemon (`ohasd`), Oracle ASM (if installed), and Cluster Synchronization Services (if Oracle ASM is installed). These commands only affect the local server on which you run them.

Note:

Oracle does not support using `crs_*` commands in an Oracle Restart environment.

Each server in the cluster is in one of two possible states:

- The whole stack is up, which means that Oracle High Availability Services is active
- The whole stack is down, which means that Oracle High Availability Services is inactive

You can use the following commands in the Oracle Restart environment, only:

- `crsctl check has`
- `crsctl config has`
- `crsctl disable has`
- `crsctl enable has`
- `crsctl query has releaseversion`
- `crsctl query has softwareversion`
- `crsctl start has`
- `crsctl stop has`

#### crsctl check has

Use the `crsctl check has` command to check the status of `ohasd`.

Syntax

```
crsctl check has
```

Usage Notes

Example

The `crsctl check has` command returns output similar to the following:

```
CRS-4638: Oracle High Availability Services is online
```

#### crsctl config has

Use the `crsctl check has` command to display the automatic startup configuration of the Oracle High Availability Services stack on the server.

Syntax

```
crsctl config has
```

Usage Notes

Example

The `crsctl config has` command returns output similar to the following:

```
CRS-4622 Oracle High Availability Services autostart is enabled.
```

#### crsctl disable has

Use the `crsctl disable has` command to disable automatic startup of the Oracle High Availability Services stack when the server boots up.

Syntax

```
crsctl disable has
```

Usage Notes

Example

The `crsctl disable has` command returns output similar to the following:

```
CRS-4621 Oracle High Availability Services autostart is disabled.
```

#### crsctl enable has

Use the `crsctl enable has` command to enable automatic startup of the Oracle High Availability Services stack when the server boots up.

Syntax

```
crsctl enable has
```

Usage Notes

Example

The `crsctl enable has` command returns output similar to the following:

```
CRS-4622 Oracle High Availability Services autostart is enabled.
```

#### crsctl query has releaseversion

Use the `crsctl query crs releaseversion` command to display the release version of the Oracle Clusterware software that is stored in the binaries on the local node.

Syntax

```
crsctl query has releaseversion
```

Usage Notes

Example

The `crsctl query has releaseversion` command returns output similar to the following:

```
Oracle High Availability Services release version on the local node is [11.2.0.0.2]
```

#### crsctl query has softwareversion

Use the `crsctl query has softwareversion` command to display the software version on the local node.

Syntax

```
crsctl query has softwareversion
```

Usage Notes

- If you do not provide a server name, then Oracle Clusterware displays the version of Oracle Clusterware running on the local server.

Example

The `crsctl query has softwareversion` command returns output similar to the following:

```
Oracle High Availability Services version on the local node is [11.2.0.2.0]
```

#### crsctl start has

Use the `crsctl start has` command to start Oracle High Availability Services on the local server.

Syntax

```
crsctl start has
```

Usage Notes

Example

To start Oracle High Availability Services on the local server:

```
# crsctl start has
```

#### crsctl stop has

Use the `crsctl stop has` command to stop Oracle High Availability Services on the local server.

Syntax

```
crsctl stop has [-f]
```

Usage Notes

- This command attempts to gracefully stop resources managed by Oracle Clusterware while attempting to stop Oracle High Availability Services.
	If any resources that Oracle Clusterware manages are still running after you run the `crsctl stop has` command, then the command fails. Use the `-f` option to unconditionally stop all resources and stop Oracle High Availability Services.

Example

To stop Oracle High Availability Services on the local server:

```
# crsctl stop has
```

## Troubleshooting and Diagnostic Output

You can use `crsctl set log` commands as the `root` user to enable dynamic debugging for Cluster Ready Services (CRS), Cluster Synchronization Services (CSS), and the Event Manager (EVM), and the clusterware subcomponents. You can dynamically change debugging levels using `crsctl debug` commands. Debugging information remains in the Oracle Cluster Registry (OCR) for use during the next startup. You can also enable debugging for resources.

This section covers the following topics:

- Dynamic Debugging
- Component Level Debugging
- Enabling Debugging for Oracle Clusterware Resources
- Enabling Additional Tracing for Oracle Clusterware Components

### Dynamic Debugging

This section includes the following CRSCTL commands that aid in debugging:

- `crsctl set log`

#### crsctl set log

Use the `crsctl set log` command to set log levels for Oracle Clusterware.

Syntax

```
crsctl set log {[crs | css | evm "component_name=log_level, [...]"] | 
[all=log_level]}
```

You can also set log levels for the agents of specific resources, as follows:

```
crsctl set log res "resource_name=log_level, [...]"
```

Usage Notes

- You can set log levels for various components of the three modules, CRS, CSS, and EVM. If you choose the `all` option, then you can set log levels for all components of one module with one command. Use the `crsctl lsmodules` command to obtain a list of components for each module.
- Enter a comma-delimited list of component name-log level pairs enclosed in double quotation marks (`""`).
	Note:
	Separate component name-log level pairs with an equals sign (`=`) in Oracle Clusterware 11g release 2 (11.2). Previous Oracle Clusterware versions used a colon (`:`).
- The `log_level` is a number from `1` to `5` that sets the log level for the component or resource, where 1 is the least amount of log output and 5 provides the most detailed log output. The default log level is 2.
- To set log levels for resources, specify the name of a particular resource, or a comma-delimited list of resource name-log level pairs enclosed in double quotation marks (`""`).

Examples

To set log levels for the CRSRTI and CRSCOMM components of the CRS module:

```
$ crsctl set log crs "CRSRTI=1,CRSCOMM=2"
```

To set log levels for all components of the EVM module:

```
$ crsctl set log evm all=2
```

To set a log level for a resource:

```
$ crsctl set log res "myResource1=3"
```

### Component Level Debugging

You can use `crsctl set log` and `crsctl set trace` commands as the `root` user to enable dynamic debugging for the various Oracle Clusterware modules.

This section includes the following topics:

- Enabling Debugging for Oracle Clusterware Modules
- Creating an Initialization File to Contain the Debugging Level

#### Enabling Debugging for Oracle Clusterware Modules

You can enable debugging for Oracle Clusterware modules and their components, and for resources, by setting environment variables or by running `crsctl set log` commands, using the following syntax:

```
crsctl set {log | trace} module_name "component:debugging_level
[,component:debugging_level][,...]"
```

Run the `crsctl set` command as the `root` user, and supply the following information:

- `module_name`: The name of one of the following modules:
	  
	`mdns`: Multicast domain name server  
	`gpnp`: Grid Plug and Play service  
	`css`: Cluster Synchronization Services  
	`crf`: Cluster Health Monitor  
	`crs`: Cluster Ready Services  
	`ctss`: Cluster Time Synchronization Service  
	`evm`: Event Manager  
	`gipc`: Grid Interprocess Communication
- `component`: The name of a component for one of the modules. See Table E-41 for a list of all of the components.
- `debugging_level`: A number from `1` to `5` to indicate the level of detail you want the debug command to return, where 1 is the least amount of debugging output and 5 provides the most detailed debugging output. The default debugging level is 2.
	You can dynamically change the debugging level in the `crsctl` command or you can configure an initialization file for changing the debugging level, as described in "Creating an Initialization File to Contain the Debugging Level".

The following commands show examples of how to enable debugging for the various modules:

- To enable debugging for Oracle Clusterware:
	```
	crsctl set log crs "CRSRTI:1,CRSCOMM:2"
	```
- To enable debugging for OCR:
	```
	crsctl set log crs "CRSRTI:1,CRSCOMM:2,OCRSRV:4"
	```
- To enable debugging for EVM:
	```
	crsctl set log evm "EVMCOMM:1"
	```
- To enable debugging for resources
	```
	crsctl set log res "resname:1"
	```

To obtain a list of components that can be used for debugging, run the `crsctl lsmodules` command, as follows:

```
crsctl lsmodules {mdns | gpnp | css | crf | crs | ctss | evm | gipc}
```

Note:

You do not have to be the `root` user to run the `crsctl lsmodulues` command.

Table E-41 shows the components for the CRS, CSS, and EVM modules, respectively. Note that some component names are common between the CRS, EVM, and CSS daemons and may be enabled on that specific daemon. For example, `COMMNS` is the NS layer and, because each daemon uses the NS layer, you can enable this specific module component on any of the daemons to get specific debugging information.

Table E-41 Components for the CRS, CSS, and EVM Modules

| CRS Components <sup>Foot 1</sup> | CSS Components <sup>Foot 2</sup> | EVM Components <sup>Foot 3</sup> |
| --- | --- | --- |
| ``` CRSUI CRSCOMM CRSRTI CRSMAIN CRSPLACE CRSAPP CRSRES CRSCOMM CRSOCR CRSTIMER CRSEVT CRSD CLUCLS CSSCLNT COMMCRS COMMNS ``` | ``` CLSF CSSD GIPCCM GIPCGM GIPCNM GPNP OLR SKGFD ``` | ``` EVMD EVMDMAIN EVMCOMM EVMEVT EVMAPP EVMAGENT CRSOCR CLUCLS CSSCLNT COMMCRS COMMNS ``` |

<sup>Footnote 1</sup> Obtain the list of CRS components using the `crsctl lsmodules crs` command.

<sup>Footnote 2</sup> Obtain the list of CSS components using the `crsctl lsmodules css` command.

<sup>Footnote 3</sup> Obtain the list of EVM components using the `crsctl lsmodules evm` command.

Example 1

To set debugging levels on specific cluster nodes, include the `-nodelist` keyword and the names of the nodes, as follows:

```
crsctl set log crs "CRSRTI:1,CRSCOMM:2" -nodelist node1,node2
```

Table E-42 describes the Cluster Synchronization Services modules.

Table E-42 Cluster Synchronization Services (CSS) Modules and Functions

| Module | Description |
| --- | --- |
| CSS | CSS client component |
| CSSD | CSS daemon component |

Table E-43 describes the function of each communication (COMM) module.

Table E-43 Communication (COMM) Modules and Functions

| Module | Description |
| --- | --- |
| COMMCRS | Clusterware communication layer |
| COMMNS | NS communication layer |

Table E-44 describes the functions performed by each CRS module.

Table E-44 Oracle Clusterware (CRS) Modules and Functions

| Module | Descriptions |
| --- | --- |
| CRSUI | User interface module |
| CRSCOMM | Communication module |
| CRSRTI | Resource management module |
| CRSMAIN | Main module/driver |
| CRSPLACE | CRS placement module |
| CRSAPP | CRS application |
| CRSRES | CRS resources |
| CRSOCR | Oracle Cluster Registry interface |
| CRSTIMER | Various timers related to CRS |
| CRSEVT | CRS EVM/event interface module |
| CRSD | CRS daemon |

Using the `crsctl set log crs` command, you can debug the OCR components listed in Table E-45. The components listed in Table E-45 can also be used for the Oracle Local Registry (OLR) except for OCRMAS and OCRASM. You can also use them for OCR and OLR clients, except for OCRMAS and OCRSRV. Some OCR and OLR clients are OCRCONFIG, OCRDUMP, and so on.

Table E-45 Oracle Cluster Registry (OCR) Component Names

| Module | Description |
| --- | --- |
| OCRAPI | OCR abstraction component |
| OCRCLI | OCR client component |
| OCRSRV | OCR server component |
| OCRMAS | OCR master thread component |
| OCRMSG | OCR message component |
| OCRCAC | OCR cache component |
| OCRRAW | OCR raw device component |
| OCRUTL | OCR util component |
| OCROSD | OCR operating system dependent (OSD) layer |
| OCRASM | OCR ASM component |

Table E-46 describes the OCR tool modules.

Table E-46 OCRCONFIG Modules and Functions

| Module | Description |
| --- | --- |
| OCRCONFIG | OCRCONFIG component for configuring OCR |
| OCRDUMP | OCRDUMP component that lists the Oracle Cluster Registry contents |
| OCRCHECK | OCRCHECK component that verifies all of the configured OCRs |

#### Creating an Initialization File to Contain the Debugging Level

This section describes how to specify the debugging level in an initialization file. This debugging information is stored for use during the next startup.

For each process to debug, you can create an initialization file that contains the debugging level.

The initialization file name includes the name of the process that you are debugging (`process_name``.ini`). The file is located in the `Grid_home` `/log/` `host_name` / `admin/` directory. For example, the name for the CLSCFG debugging initialization file on `node1` would be:

```
Grid_home
/log/node1/admin/clscfg.ini
```

You can also use an initialization file when using OCR utilities. The initialization file for `ocrconfig`, `ocrdump`, and `ocrcheck` is:

```
Grid_home
/srvm/admin/ocrlog.ini
```

The format of the initialization file is as follows:

```
mesg_logging_level=2
comploglvl="OCRAPI:0;OCRSRV:0"
comptrclvl="OCRAPI:0;OCRSRV:0"
```

You can specify component names, logging, and tracing levels.

See Also:

"Enabling Debugging for Oracle Clusterware Modules" for information about dynamically changing debugging levels by specifying the level number (from 1 to 5) on the `crsctl` command

### Enabling Debugging for Oracle Clusterware Resources

You can enable debugging for Oracle Clusterware resources by running the `crsctl set log` command, using the following syntax:

```
crsctl set log res "resource_name=debugging_level
"
```

Run the `crsctl set log` command as the `root` user, and supply the following information:

- `resource_name`: The name of the resource to debug.
- `debugging_level`: A number from `1` to `5` to indicate the level of detail you want the debug command to return, where 1 is the least amount of debugging output and 5 provides the most detailed debugging output. The default debugging level is 2.
	You can dynamically change the debugging level in the `crsctl` command or you can configure an initialization file for changing the debugging level, as described in "Creating an Initialization File to Contain the Debugging Level".

To obtain a list of resources that can be used for debugging, run the `crsctl status resource` command.

Example 1

To generate a debugging log for the VIP resource on `node1`, issue the following command:

```
crsctl set log res "ora.node1.vip:1"
```

### Enabling Additional Tracing for Oracle Clusterware Components

My Oracle Support may ask you to enable tracing to capture additional information. Because the procedures described in this section may affect performance, only perform these activities with the assistance of My Oracle Support.

You can enable tracing for Oracle Clusterware resources by running the `crsctl set trace` command, using the following syntax:

```
crsctl set trace module_name "component_name=tracing_level
,..."
```

Run the `crsctl set trace` command as the `root` user, and supply the following information:

- `module_name`: The name of one of the following modules:
	  
	`mdns`: Multicast domain name server  
	`gpnp`: Grid Plug and Play service  
	`css`: Cluster Synchronization Services  
	`crf`: Cluster Health Monitor  
	`crs`: Cluster Ready Services  
	`ctss`: Cluster Time Synchronization Service  
	`evm`: Event Manager  
	`gipc`: Grid Interprocess Communication
- `component_name`: The name of the component for one of the modules. See Table E-41 for a list of components.
- `tracing_level`: A number from `1` to `5` to indicate the level of detail you want the trace command to return, where 1 is the least amount of tracing output and 5 provides the most detailed tracing output.

Example 1

To generate a trace file for Cluster Synchronization Services, use the following command:

```
crsctl set trace "css=3"
```