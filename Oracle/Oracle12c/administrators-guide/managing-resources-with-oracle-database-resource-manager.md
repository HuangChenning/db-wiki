---
title: "Database Administrator’s Guide"
book: "Database Administrator's Guide"
doc_id: E85760-09
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/admin/managing-resources-with-oracle-database-resource-manager.html
tags:
  - oracle
  - 12c
  - administrators-guide
---

Oracle Database Resource Manager (Resource Manager) enables you to manage resource allocation for a database.

Note:

This chapter discusses using PL/SQL package procedures to administer the Resource Manager. An easier way to administer the Resource Manager is with the graphical user interface of Oracle Enterprise Manager Cloud Control (Cloud Control). For instructions about administering Resource Manager with Cloud Control, see the Cloud Control online help.

To use Resource Manager with Cloud Control:

1. Access the Database Home Page.
2. From the Administration menu, select Resource Manager.

- About Oracle Database Resource Manager  
	Oracle Database Resource Manager (the Resource Manager) enables you to manage multiple workloads within a database that are contending for system and database resources.
- Assigning Sessions to Resource Consumer Groups  
	There are automatic and manual methods that database administrators, users, and applications can use to assign sessions to resource consumer groups. When a session is assigned to a resource consumer group, Oracle Database Resource Manager (the Resource Manager) can manage resource allocation for it.
- The Types of Resources Managed by the Resource Manager  
	Resource plan directives specify how resources are allocated to resource consumer groups or subplans. Each directive can specify several different methods for allocating resources to its consumer group or subplan.
- Creating a Simple Resource Plan  
	You can quickly create a simple resource plan that is adequate for many situations using the `CREATE_SIMPLE_PLAN` procedure.
- Creating a Complex Resource Plan  
	When your situation calls for a more complex resource plan, you must create the plan, with its directives and consumer groups, in a staging area called the pending area, and then validate the plan before storing it in the data dictionary.
- Enabling Oracle Database Resource Manager and Switching Plans  
	You enable Oracle Database Resource Manager (the Resource Manager) by setting the `RESOURCE_MANAGER_PLAN` initialization parameter. This parameter specifies the top plan, identifying the plan to be used for the current instance. If no plan is specified with this parameter, the Resource Manager is not enabled.
- Putting It All Together: Oracle Database Resource Manager Examples  
	Examples illustrate how to allocate resources with Resource Manager.
- Managing Multiple Database Instances on a Single Server  
	Oracle Database provides a method for managing CPU allocations on a multi-CPU server running multiple database instances. This method is called instance caging. Instance caging and Oracle Database Resource Manager (the Resource Manager) work together to support desired levels of service across multiple instances.
- Maintaining Consumer Groups, Plans, and Directives  
	You can maintain consumer groups, resource plans, and resource plan directives for Oracle Database Resource Manager (the Resource Manager). You perform maintenance tasks using the `DBMS_RESOURCE_MANAGER` PL/SQL package.
- Viewing Database Resource Manager Configuration and Status  
	You can use several static data dictionary views and dynamic performance views to view the current configuration and status of Oracle Database Resource Manager (the Resource Manager).
- Monitoring Oracle Database Resource Manager  
	A set of dynamic performance views enable you to monitor the results of your Oracle Database Resource Manager settings.
- Interacting with Operating-System Resource Control  
	Many operating systems provide tools for resource management. These tools often contain "workload manager" or "resource manager" in their names, and are intended to allow multiple applications to share the resources of a single server, using an administrator-defined policy. Examples are Hewlett Packard's Process Resource Manager or Solaris Containers, Zones, and Resource Pools.
- Oracle Database Resource Manager Reference  
	Resource Manager includes predefined resource plans, consumer groups, and consumer groups mapping rules. You can query data dictionary views for information about your Resource Manager configuration.

**Parent topic:** [Database Resource Management and Task Scheduling](database-resource-management-and-task-scheduling.md)

### 27.1 About Oracle Database Resource Manager

Oracle Database Resource Manager (the Resource Manager) enables you to manage multiple workloads within a database that are contending for system and database resources.

**Parent topic:** Managing Resources with Oracle Database Resource Manager

#### 27.1.1 What Solutions Does the Resource Manager Provide for Workload Management?

Resource Manager allows the database to have more control over how hardware resources are allocated.

When database resource allocation decisions are left to the operating system, you may encounter the following problems with workload management:

- Excessive overhead
	Excessive overhead results from operating system context switching between Oracle Database server processes when the number of server processes is high.
- Inefficient scheduling
	The operating system deschedules database servers while they hold latches, which is inefficient.
- Inappropriate allocation of resources
	The operating system distributes resources equally among all active processes and cannot prioritize one task over another.
- Inability to manage database-specific resources, such as parallel execution servers and active sessions

The Resource Manager helps to overcome these problems by allowing the database more control over how hardware resources are allocated. In an environment with multiple concurrent user sessions that run jobs with differing priorities, all sessions should not be treated equally. The Resource Manager enables you to classify sessions into groups based on session attributes, and to then allocate resources to those groups in a way that optimizes hardware utilization for your application environment.

With the Resource Manager, you can:

- Guarantee certain sessions a minimum amount of CPU regardless of the load on the system and the number of users.
- Distribute available CPU by allocating percentages of CPU time to different users and applications. In a data warehouse, a higher percentage can be given to ROLAP (relational online analytical processing) applications than to batch jobs.
- Limit the degree of parallelism of any operation performed by members of a group of users.
- Manage the order of parallel statements in the parallel statement queue. Parallel statements from a critical application can be enqueued ahead of parallel statements from a low priority group of users.
- Limit the number of parallel execution servers that a group of users can use. This ensures that all the available parallel execution servers are not allocated to only one group of users.
- Create an active session pool. An active session pool consists of a specified maximum number of user sessions allowed to be concurrently active within a group of users. Additional sessions beyond the maximum are queued for execution, but you can specify a timeout period, after which queued jobs will terminate. The active session pool limits the total number of sessions actively competing for resources, thereby enabling active sessions to make faster progress.
- Monitor resources
	When Resource Manager is enabled, Resource Manager automatically records statistics about resource usage, and you can examine these statistics using real-time SQL monitoring and the Resource Manager dynamic performance views (the `V$RSRC_*` views). See " Monitoring Oracle Database Resource Manager " for information about using real-time SQL monitoring and the Resource Manager dynamic performance views.
- Limit the amount of PGA memory used by each session that belongs to a group of users.
- Manage runaway sessions or calls in the following ways:
	- By detecting when a session or call consumes more than a specified amount of CPU, physical I/O, logical I/O, or elapsed time, and then automatically either terminating the session or call, or switching to a consumer group with a lower resource allocation or a limit on the percentage of CPU that the group can use
		A logical I/O, also known as a buffer I/O, refers to reads and writes of buffers in the buffer cache. When a requested buffer is not found in memory, the database performs a physical I/O to copy the buffer from either disk or the flash cache into memory, and then a logical I/O to read the cached buffer.
		- By recording detailed information about SQL statements that consume more than a specified amount of CPU, physical I/O, logical I/O, or elapsed time with real-time SQL monitoring
		- By using the Automatic Workload Repository (AWR) to analyze a persistent record of SQL statements that consume more than a specified amount of CPU, physical I/O, logical I/O, or elapsed time
		- By logging information about a runaway session without taking any other action related to the session
- Prevent the execution of operations that the optimizer estimates will run for a longer time than a specified limit.
- Limit the amount of time that a session can be idle. This can be further defined to mean only sessions that are blocking other sessions.
- Allow a database to use different resource plans, based on changing workload requirements. You can dynamically change the resource plan, for example, from a daytime resource plan to a nighttime resource plan, without having to shut down and restart the instance. You can also schedule a resource plan change with Oracle Scheduler. See [Oracle Scheduler Concepts](oracle-scheduler-concepts.md) for more information.

**Parent topic:** About Oracle Database Resource Manager

#### 27.1.2 The Elements of Resource Manager

Resource Manager includes several elements that you can manage.

- About the Elements of Resource Manager  
	The elements of the Resource Manager include resource consumer groups, resource plans, and resource plan directives.
- About Resource Consumer Groups  
	A resource consumer group (consumer group) is a collection of user sessions that are grouped together based on their processing needs.
- About Resource Plan Directives  
	The Resource Manager allocates resources to consumer groups according to the set of resource plan directives (directives) that belong to the currently active resource plan.
- About Resource Plans  
	A resource plan is a container for directives that specify how resources are allocated to resource consumer groups.
- Example: A Simple Resource Plan  
	An example illustrates a simple resource plan.
- About Subplans  
	Instead of referencing a consumer group, a resource plan directive (directive) can reference another resource plan. In this case, the plan is referred to as a subplan.
- Example: A Resource Plan with Subplans  
	An example illustrates a resource plan with subplans.

**Parent topic:** About Oracle Database Resource Manager

##### 27.1.2.1 About the Elements of Resource Manager

The elements of the Resource Manager include resource consumer groups, resource plans, and resource plan directives.

| Element | Description |
| --- | --- |
| Resource consumer group | A group of sessions that are grouped together based on resource requirements. The Resource Manager allocates resources to resource consumer groups, not to individual sessions. |
| Resource plan | A container for directives that specify how resources are allocated to resource consumer groups. You specify how the database allocates resources by activating a specific resource plan. |
| Resource plan directive | Associates a resource consumer group with a particular plan and specifies how resources are to be allocated to that resource consumer group. |

You use the `DBMS_RESOURCE_MANAGER` PL/SQL package to create and maintain these elements. The elements are stored in tables in the data dictionary. You can view information about them with data dictionary views.

See Also:

" Resource Manager Data Dictionary Views "

**Parent topic:** The Elements of Resource Manager

##### 27.1.2.2 About Resource Consumer Groups

A resource consumer group (consumer group) is a collection of user sessions that are grouped together based on their processing needs.

When a session is created, it is automatically mapped to a consumer group based on mapping rules that you set up. As a database administrator (DBA), you can manually switch a session to a different consumer group. Similarly, an application can run a PL/SQL package procedure that switches its session to a particular consumer group.

Because the Resource Manager allocates resources (such as CPU) only to consumer groups, when a session becomes a member of a consumer group, its resource allocation is determined by the allocation for the consumer group.

There are special consumer groups that are always present in the data dictionary. They cannot be modified or deleted. They are:

- `SYS_GROUP`
	This is the initial consumer group for all sessions created by user accounts `SYS` or `SYSTEM`. This initial consumer group can be overridden by session-to–consumer group mapping rules.
- `OTHER_GROUPS`
	This consumer group contains all sessions that have not been assigned to a consumer group. Every resource plan must contain a directive to `OTHER_GROUPS`.

There can be no more than 28 resource consumer groups in any active plan.

See Also:

- Table 27-6
- " Specifying Session-to–Consumer Group Mapping Rules "

**Parent topic:** The Elements of Resource Manager

##### 27.1.2.3 About Resource Plan Directives

The Resource Manager allocates resources to consumer groups according to the set of resource plan directives (directives) that belong to the currently active resource plan.

There is a parent-child relationship between a resource plan and its resource plan directives. Each directive references one consumer group, and no two directives for the currently active plan can reference the same consumer group.

A directive has several ways in which it can limit resource allocation for a consumer group. For example, it can control how much CPU the consumer group gets as a percentage of total CPU, and it can limit the total number of sessions that can be active in the consumer group. See " The Types of Resources Managed by the Resource Manager " for more information.

**Parent topic:** The Elements of Resource Manager

##### 27.1.2.4 About Resource Plans

A resource plan is a container for directives that specify how resources are allocated to resource consumer groups.

In addition to the resource plans that are predefined for each Oracle database, you can create any number of resource plans. However, only one resource plan is active at a time. When a resource plan is active, each of its child resource plan directives controls resource allocation for a different consumer group. Each plan must include a directive that allocates resources to the consumer group named `OTHER_GROUPS`. `OTHER_GROUPS` applies to all sessions that belong to a consumer group that is not part of the currently active plan.

Note:

Although the term "resource plan" (or just "plan") denotes one element of the Resource Manager, in this chapter it is also used to refer to a complete resource plan schema, which includes the resource plan element itself, its resource plan directives, and the consumer groups that the directives reference. For example, when this chapter refers to the `DAYTIME` resource plan, it could mean either the resource plan element named `DAYTIME`, or the particular resource allocation schema that the `DAYTIME` resource plan and its directives define. Thus, for brevity, it is acceptable to say, "the `DAYTIME` plan favors interactive applications over batch applications."

**Parent topic:** The Elements of Resource Manager

##### 27.1.2.5 Example: A Simple Resource Plan

An example illustrates a simple resource plan.

Figure 27-1 shows a simple resource plan for an organization that runs online transaction processing (OLTP) applications and reporting applications simultaneously during the daytime. The currently active plan, `DAYTIME`, allocates CPU resources among three resource consumer groups. Specifically, `OLTP` is allotted 75% of the CPU time, `REPORTS` is allotted 15%, and `OTHER_GROUPS` receives the remaining 10%. Any group can use more resources than it is guaranteed if there is no resource contention. For example, `OLTP` is guaranteed 75% of the CPU, but if there is no resource contention, it can use up to 100% of the CPU.

Figure 27-1 A Simple Resource Plan

![Figure 27-1 A Simple Resource Plan](img/admin078.gif)

> This is a text description of Figure 27-1. It illustrates the simple resource plan that is described in the preceding text.


Oracle Database provides a procedure (`CREATE_SIMPLE_PLAN`) that enables you to quickly create a simple resource plan. This procedure is discussed in " Creating a Simple Resource Plan ".

Note:

The currently active resource plan does not enforce allocations until CPU usage is at 100%. If the CPU usage is below 100%, the database is not CPU-bound and hence there is no need to enforce allocations to ensure that all sessions get their designated resource allocation.

In addition, when allocations are enforced, unused allocation by any consumer group can be used by other consumer groups. In the previous example, if the `OLTP` group does not use all of its allocation, the Resource Manager permits the `REPORTS` group or `OTHER_GROUPS` group to use the unused allocation.

**Parent topic:** The Elements of Resource Manager

##### 27.1.2.6 About Subplans

Instead of referencing a consumer group, a resource plan directive (directive) can reference another resource plan. In this case, the plan is referred to as a subplan.

The subplan itself has directives that allocate resources to consumer groups and other subplans. The resource allocation scheme then works like this: The top resource plan (the currently active plan) divides resources among consumer groups and subplans. Each subplan allocates its portion of the total resource allocation among its consumer groups and subplans. You can create hierarchical plans with any number of subplans.

You create a resource subplan in the same way that you create a resource plan. To create a plan that is to be used only as a subplan, you use the `SUB_PLAN` argument in the package procedure `DBMS_RESOURCE_MANAGER.CREATE_PLAN`.

In any top level plan, you can reference a subplan only once. A subplan is not required to have a directive to `OTHER_GROUPS` and cannot be set as a resource plan.

**Parent topic:** The Elements of Resource Manager

##### 27.1.2.7 Example: A Resource Plan with Subplans

An example illustrates a resource plan with subplans.

In this example, the Great Bread Company allocates the CPU resource as shown in Figure 27-2. The figure illustrates a top plan (`GREAT_BREAD`) and all of its descendents. For simplicity, the requirement to include the `OTHER_GROUPS` consumer group is ignored, and resource plan directives are not shown, even though they are part of the plan. Rather, the CPU percentages that the directives allocate are shown along the connecting lines between plans, subplans, and consumer groups.

Figure 27-2 A Resource Plan With Subplans

![Figure 27-2 A Resource Plan With Subplans](img/admin027.gif)

> This is a text description of admin027.gif. It illustrates the Database Resource Manager plan with subplans that is described in the text following the image.
>
> End of image description.


The `GREAT_BREAD` plan allocates resources as follows:

- 20% of CPU resources to the consumer group `MARKET`
- 60% of CPU resources to subplan `SALES_TEAM`, which in turn divides its share equally between the `WHOLESALE` and `RETAIL` consumer groups
- 20% of CPU resources to subplan `DEVELOP_TEAM`, which in turn divides its resources equally between the `BREAD` and `MUFFIN` consumer groups

It is possible for a subplan or consumer group to have multiple parents. An example would be if the `MARKET` group were included in the `SALES_TEAM` subplan. However, a plan cannot contain any loops. For example, the `SALES_TEAM` subplan cannot have a directive that references the `GREAT_BREAD` plan.

See Also:

" Putting It All Together: Oracle Database Resource Manager Examples " for an example of a more complex resource plan.

**Parent topic:** The Elements of Resource Manager

#### 27.1.3 About Resource Manager Administration Privileges

You must have the required privileges to administer the Resource Manager.

You must have the system privilege `ADMINISTER_RESOURCE_MANAGER` to administer the Resource Manager. This privilege (with the `ADMIN` option) is granted to database administrators through the `DBA` role.

Being an administrator for the Resource Manager enables you to execute all of the procedures in the `DBMS_RESOURCE_MANAGER` PL/SQL package.

You may, as an administrator with the `ADMIN` option, choose to grant the administrative privilege to other users or roles. To do so, use the `DBMS_RESOURCE_MANAGER_PRIVS` PL/SQL package. The relevant package procedures are listed in the following table.

| Procedure | Description |
| --- | --- |
| `GRANT_SYSTEM_PRIVILEGE` | Grants the `ADMINISTER_RESOURCE_MANAGER` system privilege to a user or role. |
| `REVOKE_SYSTEM_PRIVILEGE` | Revokes the `ADMINISTER_RESOURCE_MANAGER` system privilege from a user or role. |

The following PL/SQL block grants the administrative privilege to user `HR`, but does not grant `HR` the `ADMIN` option. Therefore, `HR` can execute all of the procedures in the `DBMS_RESOURCE_MANAGER` package, but `HR` cannot use the `GRANT_SYSTEM_PRIVILEGE` procedure to grant the administrative privilege to others.

```
BEGIN
  DBMS_RESOURCE_MANAGER_PRIVS.GRANT_SYSTEM_PRIVILEGE(
   GRANTEE_NAME   => 'HR',
   PRIVILEGE_NAME => 'ADMINISTER_RESOURCE_MANAGER',
   ADMIN_OPTION   => FALSE);
END;
/
```

You can revoke this privilege using the `REVOKE_SYSTEM_PRVILEGE` procedure.

Note:

The `ADMINISTER_RESOURCE_MANAGER` system privilege can only be granted or revoked using the `DBMS_RESOURCE_MANAGER_PRIVS` package. It cannot be granted or revoked through the SQL `GRANT` or `REVOKE` statements.

See Also:

- [Oracle Database PL/SQL Packages and Types Reference.](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=ARPLS050) for information about the `DBMS_RESOURCE_MANAGER` package
- [Oracle Database PL/SQL Packages and Types Reference.](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=ARPLS051) for information about the `DBMS_RESOURCE_MANAGER_PRIVS` package
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=DBSEG99948) for information about the `ADMIN` option

**Parent topic:** About Oracle Database Resource Manager

### 27.2 Assigning Sessions to Resource Consumer Groups

There are automatic and manual methods that database administrators, users, and applications can use to assign sessions to resource consumer groups. When a session is assigned to a resource consumer group, Oracle Database Resource Manager (the Resource Manager) can manage resource allocation for it.

Note:

Sessions that are not assigned to a consumer group are placed in the consumer group `OTHER_GROUPS`.

- Overview of Assigning Sessions to Resource Consumer Groups  
	Before you enable the Resource Manager, you must specify how user sessions are assigned to resource consumer groups.
- Assigning an Initial Resource Consumer Group  
	The initial consumer group of a session is determined by the mapping rules that you configure.
- Specifying Session-to–Consumer Group Mapping Rules  
	You can create and prioritize session-to–consumer group mapping rules.
- Switching Resource Consumer Groups  
	You can switch the resource consumer group of a session.
- Specifying Automatic Consumer Group Switching  
	You can configure the Resource Manager to automatically switch a session to another consumer group when a certain condition is met.
- Granting and Revoking the Switch Privilege  
	A user or application must have the switch privilege to switch a session to a specified resource consumer group.

**Parent topic:** Managing Resources with Oracle Database Resource Manager

#### 27.2.1 Overview of Assigning Sessions to Resource Consumer Groups

Before you enable the Resource Manager, you must specify how user sessions are assigned to resource consumer groups.

You do this by creating mapping rules that enable the Resource Manager to automatically assign each session to a consumer group upon session startup, based upon session attributes. After a session is assigned to its initial consumer group and is running, you can call a procedure to manually switch the session to a different consumer group. You would typically do this if the session is using excessive resources and must be moved to a consumer group that is more limited in its resource allocation. You can also grant the switch privilege to users and to applications so that they can switch their sessions from one consumer group to another.

The database can also automatically switch a session from one consumer group to another (typically lower priority) consumer group when there are changes in session attributes or when a session exceeds designated resource consumption limits.

**Parent topic:** Assigning Sessions to Resource Consumer Groups

#### 27.2.2 Assigning an Initial Resource Consumer Group

The initial consumer group of a session is determined by the mapping rules that you configure.

For information on how to configure mapping rules, see " Specifying Session-to–Consumer Group Mapping Rules ".

**Parent topic:** Assigning Sessions to Resource Consumer Groups

#### 27.2.3 Specifying Session-to–Consumer Group Mapping Rules

You can create and prioritize session-to–consumer group mapping rules.

- About Session-to–Consumer Group Mapping Rules  
	You can specify the initial consumer group for a session and dynamically switch the session to a different consumer group if the session attributes change.
- Creating Consumer Group Mapping Rules  
	You use the `SET_CONSUMER_GROUP_MAPPING` procedure to map a session attribute/value pair to a consumer group.
- Modifying and Deleting Consumer Group Mapping Rules  
	To modify a consumer group mapping rule, run the `SET_CONSUMER_GROUP_MAPPING` procedure against the desired attribute/value pair, specifying a new consumer group.
- Creating Mapping Rule Priorities  
	To resolve conflicting mapping rules, you can establish a priority ordering of the session attributes from most important to least important.

**Parent topic:** Assigning Sessions to Resource Consumer Groups

##### 27.2.3.1 About Session-to–Consumer Group Mapping Rules

You can specify the initial consumer group for a session and dynamically switch the session to a different consumer group if the session attributes change.

By creating session-to–consumer group mapping rules, you can:

- Specify the initial consumer group for a session based on session attributes.
- Enable the Resource Manager to dynamically switch a running session to another consumer group based on changing session attributes.

The mapping rules are based on session attributes such as the user name, the service that the session used to connect to the database, or the name of the client program.

To resolve conflicts among mapping rules, the Resource Manager orders the rules by priority. For example, suppose user `SCOTT` connects to the database with the `SALES` service. If one mapping rule states that user `SCOTT` starts in the `MED_PRIORITY` consumer group, and another states that sessions that connect with the `SALES` service start in the `HIGH_PRIORITY` consumer group, mapping rule priorities resolve this conflict.

There are two types of session attributes upon which mapping rules are based: login attributes and run-time attributes. The login attributes are meaningful only at session login time, when the Resource Manager determines the initial consumer group of the session. Run-time attributes apply any time during and after session login. You can reassign a logged in session to another consumer group by changing any of its run-time attributes.

You use the `SET_CONSUMER_GROUP_MAPPING` and `SET_CONSUMER_GROUP_MAPPING_PRI` procedures to configure the automatic assignment of sessions to consumer groups. You must use a pending area for these procedures. (You must create the pending area, run the procedures, optionally validate the pending area, and then submit the pending area. For examples of using the pending area, see " Creating a Complex Resource Plan ".)

A session is automatically switched to a consumer group through mapping rules at distinct points in time:

- When the session first logs in, the mapping rules are evaluated to determine the initial group of the session.
- If a session attribute is dynamically changed to a new value (which is only possible for run-time attributes), then the mapping rules are reevaluated, and the session might be switched to another consumer group.

Predefined Consumer Group Mapping Rules

Each Oracle database comes with a set of predefined consumer group mapping rules:

- As described in " About Resource Consumer Groups ", all sessions created by user accounts `SYS` or `SYSTEM` are initially mapped to the `SYS_GROUP` consumer group.
- Sessions performing a data load with Data Pump or performing backup or copy operations with RMAN are automatically mapped to the predefined consumer groups designated in Table 27-7.

You can use the `DBMS_RESOURCE_MANAGER`.`SET_CONSUMER_GROUP_MAPPING` procedure to modify or delete any of these predefined mapping rules.

See Also:

- " Assigning an Initial Resource Consumer Group "
- " Specifying Automatic Switching with Mapping Rules "

**Parent topic:** Specifying Session-to–Consumer Group Mapping Rules

##### 27.2.3.2 Creating Consumer Group Mapping Rules

You use the `SET_CONSUMER_GROUP_MAPPING` procedure to map a session attribute/value pair to a consumer group.

The parameters for this procedure are the following:

| Parameter | Description |
| --- | --- |
| `ATTRIBUTE` | The session attribute type, specified as a package constant |
| `VALUE` | The value of the attribute |
| `CONSUMER_GROUP` | The consumer group to map to for this attribute/value pair |

`ATTRIBUTE` can be one of the following:

| Attribute | Type | Description |
| --- | --- | --- |
| `ORACLE_USER` | Login | The Oracle Database user name |
| `SERVICE_NAME` | Login | The database service name used by the client to establish a connection |
| `CLIENT_OS_USER` | Login | The operating system user name of the client that is logging in |
| `CLIENT_PROGRAM` | Login | The name of the client program used to log in to the server |
| `CLIENT_MACHINE` | Login | The name of the computer from which the client is making the connection |
| `CLIENT_ID` | Login | The client identifier for the session  The client identifier session attribute is set by the `DBMS_SESSION.SET_IDENTIFIER` procedure. |
| `MODULE_NAME` | Run-time | The module name in the currently running application as set by the `DBMS_APPLICATION_INFO.SET_MODULE` procedure or the equivalent OCI attribute setting |
| `MODULE_NAME_ACTION` | Run-time | A combination of the current module and the action being performed as set by either of the following procedures or their equivalent OCI attribute setting:  - `DBMS_APPLICATION_INFO.SET_MODULE` - `DBMS_APPLICATION_INFO.SET_ACTION`  The attribute is specified as the module name followed by a period (.), followed by the action name (`module_name.action_name`). |
| `SERVICE_MODULE` | Run-time | A combination of service and module names in this form: `service_name.module_name` |
| `SERVICE_MODULE_ACTION` | Run-time | A combination of service name, module name, and action name, in this form: `service_name.module_name.action_name` |
| `ORACLE_FUNCTION` | Run-time | An RMAN or Data Pump operation. Valid values are `DATALOAD`, `BACKUP`, and `COPY`. There are predefined mappings for each of these values. If your session is performing any of these functions, it is automatically mapped to a predefined consumer group. See Table 27-7 for details. |

For example, the following PL/SQL block causes user `SCOTT` to map to the `DEV_GROUP` consumer group every time that he logs in:

```
BEGIN
  DBMS_RESOURCE_MANAGER.SET_CONSUMER_GROUP_MAPPING  
     (DBMS_RESOURCE_MANAGER.ORACLE_USER, 'SCOTT', 'DEV_GROUP');
END;
/
```

Again, you must create a pending area before running the `SET_CONSUMER_GROUP_MAPPING` procedure.

You can use wildcards for the value of most attributes in the `value` parameter in the `SET_CONSUMER_GROUP_MAPPING` procedure. To specify values with wildcards, use the same semantics as the SQL `LIKE` operator. Specifically, wildcards use the following semantics:

- `%` for a multicharacter wildcard
- `_` for a single character wildcard
- `\` to escape the wildcards

Wildcards can only be used if the attribute is one of the following:

- `CLIENT_OS_USER`
- `CLIENT_PROGRAM`
- `CLIENT_MACHINE`
- `MODULE_NAME`
- `MODULE_NAME_ACTION`
- `SERVICE_MODULE`
- `SERVICE_MODULE_ACTION`

**Parent topic:** Specifying Session-to–Consumer Group Mapping Rules

##### 27.2.3.3 Modifying and Deleting Consumer Group Mapping Rules

To modify a consumer group mapping rule, run the `SET_CONSUMER_GROUP_MAPPING` procedure against the desired attribute/value pair, specifying a new consumer group.

To delete a rule, run the `SET_CONSUMER_GROUP_MAPPING` procedure against the desired attribute/value pair and specify a `NULL` consumer group.

**Parent topic:** Specifying Session-to–Consumer Group Mapping Rules

##### 27.2.3.4 Creating Mapping Rule Priorities

To resolve conflicting mapping rules, you can establish a priority ordering of the session attributes from most important to least important.

You use the `SET_CONSUMER_GROUP_MAPPING_PRI` procedure to set the priority of each attribute to a unique integer from 1 (most important) to 12 (least important). The following example illustrates this setting of priorities:

```
BEGIN
  DBMS_RESOURCE_MANAGER.SET_CONSUMER_GROUP_MAPPING_PRI(
    EXPLICIT => 1,
    SERVICE_MODULE_ACTION => 2,
    SERVICE_MODULE => 3,
    MODULE_NAME_ACTION => 4,
    MODULE_NAME => 5,
    SERVICE_NAME => 6,
    ORACLE_USER => 7,
    CLIENT_PROGRAM => 8,
    CLIENT_OS_USER => 9,
    CLIENT_MACHINE => 10,
    CLIENT_ID => 11);
END;
/
```

In this example, the priority of the database user name is set to 7 (less important), while the priority of the module name is set to 5 (more important).

Note:

`SET_CONSUMER_GROUP_MAPPING_PRI` requires that you include the pseudo-attribute `EXPLICIT` as an argument. It must be set to 1. It indicates that explicit consumer group switches have the highest priority. You explicitly switch consumer groups with these package procedures, which are described in detail in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=ARPLS050):

- `DBMS_SESSION.SWITCH_CURRENT_CONSUMER_GROUP`
- `DBMS_RESOURCE_MANAGER.SWITCH_CONSUMER_GROUP_FOR_SESS`
- `DBMS_RESOURCE_MANAGER.SWITCH_CONSUMER_GROUP_FOR_USER`

To illustrate how mapping rule priorities work, continuing with the previous example, assume that in addition to the mapping of user `SCOTT` to the `DEV_GROUP` consumer group, there is also a module name mapping rule as follows:

```
BEGIN
  DBMS_RESOURCE_MANAGER.SET_CONSUMER_GROUP_MAPPING
     (DBMS_RESOURCE_MANAGER.MODULE_NAME, 'EOD_REPORTS', 'LOW_PRIORITY');
END;
/
```

Now if the application in user `SCOTT` 's session sets its module name to `EOD_REPORTS`, the session is reassigned to the `LOW_PRIORITY` consumer group, because module name mapping has a higher priority than database user mapping.

You can query the view `DBA_RSRC_MAPPING_PRIORITY` to see the current priority ordering of session attributes.

See Also:

- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=ARPLS003) for information about setting the module name with the `DBMS_APPLICATION_INFO.SET_MODULE` procedure
- " Granting and Revoking the Switch Privilege "

**Parent topic:** Specifying Session-to–Consumer Group Mapping Rules

#### 27.2.4 Switching Resource Consumer Groups

You can switch the resource consumer group of a session.

- Manually Switching Resource Consumer Groups  
	You can change the resource consumer group of running sessions.
- Enabling Users or Applications to Manually Switch Consumer Groups  
	You can grant a user the switch privilege so that he can switch his current consumer group using the `SWITCH_CURRENT_CONSUMER_GROUP` procedure in the `DBMS_SESSION` package.

**Parent topic:** Assigning Sessions to Resource Consumer Groups

##### 27.2.4.1 Manually Switching Resource Consumer Groups

You can change the resource consumer group of running sessions.

- About Manually Switching Resource Consumer Groups  
	The `DBMS_RESOURCE_MANAGER` PL/SQL package provides two procedures that enable you to change the resource consumer group of running sessions.
- Switching a Single Session  
	The `SWITCH_CONSUMER_GROUP_FOR_SESS` procedure causes the specified session to immediately be moved into the specified resource consumer group. In effect, this procedure can raise or lower priority of the session.
- Switching All Sessions for a User  
	The `SWITCH_CONSUMER_GROUP_FOR_USER` procedure changes the resource consumer group for all sessions pertaining to the specified user name.

**Parent topic:** Switching Resource Consumer Groups

###### 27.2.4.1.1 About Manually Switching Resource Consumer Groups

The `DBMS_RESOURCE_MANAGER` PL/SQL package provides two procedures that enable you to change the resource consumer group of running sessions.

Both of these procedures can also change the consumer group of any parallel execution server sessions associated with the coordinator session. The changes made by these procedures pertain to current sessions only; they are not persistent. They also do not change the initial consumer groups for users.

Instead of killing (terminating) a session of a user who is using excessive CPU, you can change that user's consumer group to one that is allocated fewer resources.

**Parent topic:** Manually Switching Resource Consumer Groups

###### 27.2.4.1.2 Switching a Single Session

The `SWITCH_CONSUMER_GROUP_FOR_SESS` procedure causes the specified session to immediately be moved into the specified resource consumer group. In effect, this procedure can raise or lower priority of the session.

The following PL/SQL block switches a specific session to a new consumer group. The session identifier (`SID`) is 17, the session serial number (`SERIAL#`) is 12345, and the new consumer group is the `HIGH_PRIORITY` consumer group.

```
BEGIN
  DBMS_RESOURCE_MANAGER.SWITCH_CONSUMER_GROUP_FOR_SESS ('17', '12345',
   'HIGH_PRIORITY');
END;
/
```

The `SID`, session serial number, and current resource consumer group for a session are viewable using the `V$SESSION` view.

See Also:

[Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=REFRN30223) for details about the `V$SESSION` view.

**Parent topic:** Manually Switching Resource Consumer Groups

###### 27.2.4.1.3 Switching All Sessions for a User

The `SWITCH_CONSUMER_GROUP_FOR_USER` procedure changes the resource consumer group for all sessions pertaining to the specified user name.

The following PL/SQL block switches all sessions that belong to user `HR` to the `LOW_GROUP` consumer group:

```
BEGIN
  DBMS_RESOURCE_MANAGER.SWITCH_CONSUMER_GROUP_FOR_USER ('HR',
    'LOW_GROUP'); 
END;
/
```

**Parent topic:** Manually Switching Resource Consumer Groups

##### 27.2.4.2 Enabling Users or Applications to Manually Switch Consumer Groups

You can grant a user the switch privilege so that he can switch his current consumer group using the `SWITCH_CURRENT_CONSUMER_GROUP` procedure in the `DBMS_SESSION` package.

A user can run this procedure from an interactive session, for example from SQL\*Plus, or an application can call this procedure to switch its session, effectively dynamically changing its priority.

The `SWITCH_CURRENT_CONSUMER_GROUP` procedure enables users to switch to only those consumer groups for which they have the switch privilege. If the caller is another procedure, then this procedure enables users to switch to a consumer group for which the owner of that procedure has switch privileges.

The parameters for this procedure are the following:

| Parameter | Description |
| --- | --- |
| `NEW_CONSUMER_GROUP` | The consumer group to which the user is switching. |
| `OLD_CONSUMER_GROUP` | Returns the name of the consumer group from which the user switched. Can be used to switch back later. |
| `INITIAL_GROUP_ON_ERROR` | Controls behavior if a switching error occurs.  If `TRUE`, in the event of an error, the user is switched to the initial consumer group.  If `FALSE`, raises an error. |

The following SQL\*Plus session illustrates switching to a new consumer group. By printing the value of the output parameter `old_group`, the example illustrates how the old consumer group name is saved.

```
SET serveroutput on
DECLARE
    old_group varchar2(30);
BEGIN
  DBMS_SESSION.SWITCH_CURRENT_CONSUMER_GROUP('BATCH_GROUP', old_group, FALSE);
  DBMS_OUTPUT.PUT_LINE('OLD GROUP = ' || old_group);
END;
/
```

The following line is output:

```
OLD GROUP = OLTP_GROUP
```

Note that the Resource Manager considers a switch to have taken place even if the `SWITCH_CURRENT_CONSUMER_GROUP` procedure is called to switch the session to the consumer group that it is already in.

Note:

The Resource Manager also works in environments where a generic database user name is used to log on to an application. The `DBMS_SESSION` package can be called to switch the consumer group assignment of a session at session startup, or as particular modules are called.

See Also:

- " Granting and Revoking the Switch Privilege "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=ARPLS054) for additional examples and more information about the `DBMS_SESSION` package

**Parent topic:** Switching Resource Consumer Groups

#### 27.2.5 Specifying Automatic Consumer Group Switching

You can configure the Resource Manager to automatically switch a session to another consumer group when a certain condition is met.

Automatic switching can occur when: a session attribute changes, causing a new mapping rule to take effect, or a session exceeds the CPU, physical I/O, or logical I/O resource consumption limits set by its consumer group, or it exceeds the elapsed time limit set by its consumer group.

- Specifying Automatic Switching with Mapping Rules  
	If a session attribute changes while the session is running, then the session-to–consumer group mapping rules are reevaluated. If a new rule takes effect, then the session might be moved to a different consumer group.
- Specifying Automatic Switching by Setting Resource Limits  
	You can manage runaway sessions or calls that use CPU, physical I/O, or logical I/O resources beyond a specified limit. A runaway session is a SQL query, while a runaway call is a PL/SQL call.

**Parent topic:** Assigning Sessions to Resource Consumer Groups

##### 27.2.5.1 Specifying Automatic Switching with Mapping Rules

If a session attribute changes while the session is running, then the session-to–consumer group mapping rules are reevaluated. If a new rule takes effect, then the session might be moved to a different consumer group.

See " Specifying Session-to–Consumer Group Mapping Rules " for more information.

**Parent topic:** Specifying Automatic Consumer Group Switching

##### 27.2.5.2 Specifying Automatic Switching by Setting Resource Limits

You can manage runaway sessions or calls that use CPU, physical I/O, or logical I/O resources beyond a specified limit. A runaway session is a SQL query, while a runaway call is a PL/SQL call.

When you create a resource plan directive for a consumer group, you can specify limits for CPU, physical I/O, or logical I/O resource consumption for sessions in that group. You can specify limits for physical I/O and logical I/O separately. You can also specify a limit for elapsed time. If the `SWITCH_FOR_CALL` resource plan directive is set to `FALSE`, then Resource Manager enforces these limits from the start of the session. If the `SWITCH_FOR_CALL` resource plan directive is set to `TRUE`, then Resource Manager enforces these limits from the start of the SQL operation or PL/SQL block.

You can then specify the action that is to be taken if any single session or call exceeds one of these limits. The possible actions are the following:

- The session is dynamically switched to a designated consumer group.
	The target consumer group is typically one that has lower resource allocations.
- The session is killed (terminated).
- The session's current SQL statement is aborted.
- Information about the session is logged, but no other action is taken for the session.

The following are the resource plan directive attributes that are involved in this type of automatic session switching.

- `SWITCH_GROUP`
- `SWITCH_TIME`
- `SWITCH_ESTIMATE`
- `SWITCH_IO_MEGABYTES`
- `SWITCH_IO_REQS`
- `SWITCH_FOR_CALL`
- `SWITCH_IO_LOGICAL`
- `SWITCH_ELAPSED_TIME`

See " Creating Resource Plan Directives " for descriptions of these attributes.

Switches occur for sessions that are running and consuming resources, not waiting for user input or waiting for CPU cycles. After a session is switched, it continues in the target consumer group until it becomes idle, at which point it is switched back to its original consumer group. However, if `SWITCH_FOR_CALL` is set to `TRUE`, then the Resource Manager does not wait until the session is idle to return it to its original resource consumer group. Instead, the session is returned when the current top-level call completes. A top-level call in PL/SQL is an entire PL/SQL block treated as one call. A top-level call in SQL is an individual SQL statement.

`SWITCH_FOR_CALL` is useful for three-tier applications where the middle tier server is using session pooling.

A switched session is allowed to continue running even if the active session pool for the new group is full. Under these conditions, a consumer group can have more sessions running than specified by its active session pool.

When `SWITCH_FOR_CALL` is `FALSE`, the Resource Manager views a session as idle if a certain amount of time passes between calls. This time interval is a few seconds and is not configurable.

The following are examples of automatic switching based on resource limits. You must create a pending area before running these examples.

Example 1

The following PL/SQL block creates a resource plan directive for the `OLTP` group that switches any session in that group to the `LOW_GROUP` consumer group if a call in the sessions exceeds 5 seconds of CPU time. This example prevents unexpectedly long queries from consuming too many resources. The switched-to consumer group is typically one with lower resource allocations.

```
BEGIN
  DBMS_RESOURCE_MANAGER.CREATE_PLAN_DIRECTIVE (
   PLAN             => 'DAYTIME',
   GROUP_OR_SUBPLAN => 'OLTP',
   COMMENT          => 'OLTP group',
   MGMT_P1          => 75,
   SWITCH_GROUP     => 'LOW_GROUP',
   SWITCH_TIME      => 5);
END;
/
```

Example 2

The following PL/SQL block creates a resource plan directive for the `OLTP` group that temporarily switches any session in that group to the `LOW_GROUP` consumer group if the session exceeds 10,000 physical I/O requests or exceeds 2,500 Megabytes of data transferred. The session is returned to its original group after the offending top call is complete.

```
BEGIN
  DBMS_RESOURCE_MANAGER.CREATE_PLAN_DIRECTIVE (
   PLAN                => 'DAYTIME',
   GROUP_OR_SUBPLAN    => 'OLTP',
   COMMENT             => 'OLTP group',
   MGMT_P1             => 75,
   SWITCH_GROUP        => 'LOW_GROUP',
   SWITCH_IO_REQS      => 10000,
   SWITCH_IO_MEGABYTES => 2500,
   SWITCH_FOR_CALL     => TRUE);
END;
/
```

Example 3

The following PL/SQL block creates a resource plan directive for the `REPORTING` group that kills (terminates) any session that exceeds 60 seconds of CPU time. This example prevents runaway queries from consuming too many resources.

```
BEGIN
  DBMS_RESOURCE_MANAGER.CREATE_PLAN_DIRECTIVE (
   PLAN             => 'DAYTIME',
   GROUP_OR_SUBPLAN => 'REPORTING',
   COMMENT          => 'Reporting group',
   MGMT_P1          => 75,
   SWITCH_GROUP     => 'KILL_SESSION',
   SWITCH_TIME      => 60);
END;
/
```

In this example, the reserved consumer group name `KILL_SESSION` is specified for `SWITCH_GROUP`. Therefore, the session is terminated when the switch criteria is met. Other reserved consumer group names are `CANCEL_SQL` and `LOG_ONLY`. When `CANCEL_SQL` is specified, the current call is canceled when switch criteria are met, but the session is not terminated. When `LOG_ONLY` is specified, information about the session is recorded in real-time SQL monitoring, but no specific action is taken for the session.

Example 4

The following PL/SQL block creates a resource plan directive for the `OLTP` group that temporarily switches any session in that group to the `LOW_GROUP` consumer group if the session exceeds 100 logical I/O requests. The session is returned to its original group after the offending top call is complete.

```
BEGIN
  DBMS_RESOURCE_MANAGER.CREATE_PLAN_DIRECTIVE (
   PLAN                => 'DAYTIME',
   GROUP_OR_SUBPLAN    => 'OLTP',
   COMMENT             => 'OLTP group',
   MGMT_P1             => 75,
   SWITCH_GROUP        => 'LOW_GROUP',
   SWITCH_IO_LOGICAL   => 100,
   SWITCH_FOR_CALL     => TRUE);
END;
/
```

Example 5

The following PL/SQL block creates a resource plan directive for the `OLTP` group that temporarily switches any session in that group to the `LOW_GROUP` consumer group if a call in a session exceeds five minutes (300 seconds). The session is returned to its original group after the offending top call is complete.

```
BEGIN
  DBMS_RESOURCE_MANAGER.CREATE_PLAN_DIRECTIVE (
   PLAN                => 'DAYTIME',
   GROUP_OR_SUBPLAN    => 'OLTP',
   COMMENT             => 'OLTP group',
   MGMT_P1             => 75,
   SWITCH_GROUP        => 'LOW_GROUP',
   SWITCH_FOR_CALL     => TRUE,
   SWITCH_ELAPSED_TIME => 300);
END;
/
```

See Also:

- " Creating Resource Plan Directives "
- " What Solutions Does the Resource Manager Provide for Workload Management?" for information about logical I/O

**Parent topic:** Specifying Automatic Consumer Group Switching

#### 27.2.6 Granting and Revoking the Switch Privilege

A user or application must have the switch privilege to switch a session to a specified resource consumer group.

- About Granting and Revoking the Switch Privilege  
	Using the `DBMS_RESOURCE_MANAGER_PRIVS` PL/SQL package, you can grant or revoke the switch privilege to a user, role, or `PUBLIC`. The switch privilege enables a user or application to switch a session to a specified resource consumer group.
- Granting the Switch Privilege  
	You can grant a user the privilege to switch to a specific consumer group using the `GRANT_SWITCH_CONSUMER_GROUP` procedure.
- Revoking Switch Privileges  
	You can revoke a user’s privilege to switch to a specific consumer group using the `REVOKE_SWITCH_CONSUMER_GROUP` procedure.

**Parent topic:** Assigning Sessions to Resource Consumer Groups

##### 27.2.6.1 About Granting and Revoking the Switch Privilege

Using the `DBMS_RESOURCE_MANAGER_PRIVS` PL/SQL package, you can grant or revoke the switch privilege to a user, role, or `PUBLIC`. The switch privilege enables a user or application to switch a session to a specified resource consumer group.

The package also enables you to revoke the switch privilege. The relevant package procedures are listed in the following table.

| Procedure | Description |
| --- | --- |
| `GRANT_SWITCH_CONSUMER_GROUP` | Grants permission to a user, role, or `PUBLIC` to switch to a specified resource consumer group. |
| `REVOKE_SWITCH_CONSUMER_GROUP` | Revokes permission for a user, role, or `PUBLIC` to switch to a specified resource consumer group. |

`OTHER_GROUPS` has switch privileges granted to `PUBLIC`. Therefore, all users are automatically granted the switch privilege for this consumer group.

The following switches do not require explicit switch privilege:

- There is a consumer group mapping specified by the `SET_CONSUMER_GROUP_MAPPING` procedure in the `DBMS_RESOURCE_MANAGER` package, and a session is switching to a different consumer group due to the mapping. See " Creating Consumer Group Mapping Rules ".
- There is an automatic consumer group switch when a switch condition is met based on the setting of the `switch_group` parameter of a resource plan directive.

Explicit switch privilege is required for a user to switch a session to a consumer group in all other cases.

See Also:

- " Enabling Users or Applications to Manually Switch Consumer Groups "
- " Specifying Automatic Consumer Group Switching "

**Parent topic:** Granting and Revoking the Switch Privilege

##### 27.2.6.2 Granting the Switch Privilege

You can grant a user the privilege to switch to a specific consumer group using the `GRANT_SWITCH_CONSUMER_GROUP` procedure.

The following example grants user `SCOTT` the privilege to switch to consumer group `OLTP`.

```
BEGIN
  DBMS_RESOURCE_MANAGER_PRIVS.GRANT_SWITCH_CONSUMER_GROUP (
   GRANTEE_NAME   => 'SCOTT',
   CONSUMER_GROUP => 'OLTP',
   GRANT_OPTION   =>  TRUE);
END;
/
```

User `SCOTT` is also granted permission to grant switch privileges for `OLTP` to others.

If you grant permission to a role to switch to a particular resource consumer group, then any user who is granted that role and has enabled that role can switch his session to that consumer group.

If you grant `PUBLIC` the permission to switch to a particular consumer group, then any user can switch to that group.

If the `GRANT_OPTION` argument is `TRUE`, then users granted switch privilege for the consumer group can also grant switch privileges for that consumer group to others.

**Parent topic:** Granting and Revoking the Switch Privilege

##### 27.2.6.3 Revoking Switch Privileges

You can revoke a user’s privilege to switch to a specific consumer group using the `REVOKE_SWITCH_CONSUMER_GROUP` procedure.

The following example revokes user `SCOTT` 's privilege to switch to consumer group `OLTP`.

```
BEGIN
  DBMS_RESOURCE_MANAGER_PRIVS.REVOKE_SWITCH_CONSUMER_GROUP (
   REVOKEE_NAME   => 'SCOTT', 
   CONSUMER_GROUP => 'OLTP');
END;
/
```

If you revoke a user's switch privileges for a particular consumer group, any subsequent attempts by that user to switch to that consumer group manually will fail. The user's session will then be automatically assigned to `OTHER_GROUPS`.

If you revoke from a role the switch privileges to a consumer group, any users who had switch privileges for the consumer group only through that role are no longer able to switch to that consumer group.

If you revoke switch privileges to a consumer group from `PUBLIC`, any users other than those who are explicitly assigned switch privileges either directly or through a role are no longer able to switch to that consumer group.

**Parent topic:** Granting and Revoking the Switch Privilege

### 27.3 The Types of Resources Managed by the Resource Manager

Resource plan directives specify how resources are allocated to resource consumer groups or subplans. Each directive can specify several different methods for allocating resources to its consumer group or subplan.

- CPU  
	To manage CPU resources, Resource Manager allocates resources among consumer groups and redistributes CPU resources that were allocated but were not used. You can also set a limit on the amount of CPU resources that can be allocated to a particular consumer group.
- Exadata I/O  
	Management attributes enable you to specify CPU resource allocation for Exadata I/O.
- Parallel Execution Servers  
	Resource Manager can manage usage of the available parallel execution servers for a database.
- Program Global Area (PGA)  
	To manage PGA resources, Resource Manager can limit the amount of PGA memory that can be allocated to each session in a particular consumer group.
- Runaway Queries  
	Runaway sessions and calls can adversely impact overall performance if they are not managed properly. Resource Manager can take action when a session or call consumes more than a specified amount of CPU, physical I/O, logical I/O, or elapsed time. Resource Manager can either switch the session or call to a consumer group that is allocated a small amount of CPU or terminate the session or call.
- Active Session Pool with Queuing  
	You can control the maximum number of concurrently active sessions allowed within a consumer group. This maximum defines the active session pool.
- Undo Pool  
	You can specify an undo pool for each consumer group. An undo pool controls the total amount of undo for uncommitted transactions that can be generated by a consumer group.
- Idle Time Limit  
	You can specify an amount of time that a session can be idle, after which it is terminated.

**Parent topic:** Managing Resources with Oracle Database Resource Manager

#### 27.3.1 CPU

To manage CPU resources, Resource Manager allocates resources among consumer groups and redistributes CPU resources that were allocated but were not used. You can also set a limit on the amount of CPU resources that can be allocated to a particular consumer group.

- Management Attributes  
	Management attributes enable you to specify how CPU resources are to be allocated among consumer groups and subplans.
- Utilization Limit  
	Use the `UTILIZATION_LIMIT` attribute to impose an absolute upper limit on CPU utilization for a resource consumer group. This absolute limit overrides any redistribution of CPU within a plan.

**Parent topic:** The Types of Resources Managed by the Resource Manager

##### 27.3.1.1 Management Attributes

Management attributes enable you to specify how CPU resources are to be allocated among consumer groups and subplans.

Multiple levels of CPU resource allocation (up to eight levels) provide a means of prioritizing CPU usage within a plan. Consumer groups and subplans at level 2 get resources that were not allocated at level 1 or that were allocated at level 1 but were not completely consumed by a consumer group or subplan at level 1. Similarly, resource consumers at level 3 are allocated resources only when some allocation remains from levels 1 and 2. The same rules apply to levels 4 through 8. Multiple levels not only provide a way of prioritizing, but they provide a way of explicitly specifying how all primary and leftover resources are to be used.

Use the management attributes `MGMT_P` `n`, where n is an integer between 1 and 8, to specify multiple levels of CPU resource allocation. For example, use the `MGMT_P1` directive attribute to specify CPU resource allocation at level 1 and `MGMT_P2` directive attribute to specify resource allocation at level 2.

Use management attributes with parallel statement directive attributes, such as Degree of Parallelism Limit and Parallel Server Limit, to control parallel statement queuing. When parallel statement queuing is used, management attributes are used to determine which consumer group is allowed to issue the next parallel statement. For example, if you set the `MGMT_P1` directive attribute for a consumer group to 80, that group has an 80% chance of issuing the next parallel statement.

See Also:

[Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=VLDBG1396) for information about parallel statement queuing

Table 27-1 illustrates a simple resource plan with three levels.

Table 27-1 A Simple Three-Level Resource Plan

| Consumer Group | Level 1 CPU Allocation | Level 2 CPU Allocation | Level 3 CPU Allocation |
| --- | --- | --- | --- |
| `HIGH_GROUP` | 80% |  |  |
| `LOW_GROUP` |  | 50% |  |
| `MAINT_SUBPLAN` |  | 50% |  |
| `OTHER_GROUPS` |  |  | 100% |

High priority applications run within `HIGH_GROUP`, which is allocated 80% of CPU. Because `HIGH_GROUP` is at level one, it gets priority for CPU utilization, but only up to 80% of CPU. This leaves a remaining 20% of CPU to be shared 50-50 by `LOW_GROUP` and the `MAINT_SUPLAN` at level 2. Any unused allocation from levels 1 and 2 are then available to `OTHER_GROUPS` at level 3. Because `OTHER_GROUPS` has no sibling consumer groups or subplans at its level, 100% is specified.

Within a particular level, CPU allocations are not fixed. If there is not sufficient load in a particular consumer group or subplan, residual CPU can be allocated to remaining consumer groups or subplans. Thus, when there is only one level, unused allocation by any consumer group or subplan can be redistributed to other "sibling" consumer groups or subplans. If there are multiple levels, then the unused allocation is distributed to the consumer groups or subplans at the next level. If the last level has unused allocations, these allocations can be redistributed to all other levels in proportion to their designated allocations.

As an example of redistribution of unused allocations from one level to another, if during a particular period, `HIGH_GROUP` consumes only 25% of CPU, then 75% is available to be shared by `LOW_GROUP` and `MAINT_SUBPLAN`. Any unused portion of the 75% at level 2 is then made available to `OTHER_GROUPS` at level 3. However, if `OTHER_GROUPS` has no session activity at level 3, then the 75% at level 2 can be redistributed to all other consumer groups and subplans in the plan proportionally.

**Parent topic:** CPU

##### 27.3.1.2 Utilization Limit

Use the `UTILIZATION_LIMIT` attribute to impose an absolute upper limit on CPU utilization for a resource consumer group. This absolute limit overrides any redistribution of CPU within a plan.

In the previous scenario, suppose that due to inactivity elsewhere, `LOW_GROUP` acquires 90% of CPU. Suppose that you do not want to allow `LOW_GROUP` to use 90% of the server because you do not want non-critical sessions to inundate the CPUs. The `UTILIZATION_LIMIT` attribute of resource plan directives can prevent this situation.

Setting the `UTILIZATION_LIMIT` attribute is optional. If you omit this attribute for a consumer group, there is no limit on the amount of CPU that the consumer group can use. Therefore, if all the other applications are idle, a consumer group that does not have `UTILIZATION_LIMIT` set can be allocated 100% of the CPU resources.

You can also use the `UTILIZATION_LIMIT` attribute as the sole means of limiting CPU utilization for consumer groups, without specifying level limits.

Table 27-2 shows a variation of the previous plan. In this plan, using `UTILIZATION_LIMIT`, CPU utilization is capped at 75% for `LOW_GROUP`, 50% for `MAINT_SUBPLAN`, and 75% for `OTHER_GROUPS`. (Note that the sum of all utilization limits can exceed 100%. Each limit is applied independently.)

Table 27-2 A Three-Level Resource Plan with Utilization Limits

| Consumer Group | Level 1 CPU Allocation | Level 2 CPU Allocation | Level 3 CPU Allocation | Utilization Limit |
| --- | --- | --- | --- | --- |
| `HIGH_GROUP` | 80% |  |  |  |
| `LOW_GROUP` |  | 50% |  | 75% |
| `MAINT_SUBPLAN` |  | 50% |  | 50% |
| `OTHER_GROUPS` |  |  | 100% | 75% |

In the example described in Table 27-2, if `HIGH_GROUP` is using only 10% of the CPU at a given time, then the remaining 90% is available to `LOW_GROUP` and the consumer groups in `MAINT_SUBPLAN` at level 2. If `LOW_GROUP` uses only 20% of the CPU, then 70% can be allocated to `MAINT_SUBPLAN`. However, `MAINT_SUBPLAN` has a `UTILIZATION_LIMIT` of 50%. Therefore, even though more CPU resources are available, the server cannot allocate more than 50% of the CPU to the consumer groups that belong to the subplan `MAINT_SUBPLAN`.

You can set `UTILIZATION_LIMIT` for both a subplan and the consumer groups that the subplan contains. In such cases, the limit for a consumer group is computed using the limits specified for the subplan and that consumer group. For example, the `MAINT_SUBPLAN` contains the consumer groups `MAINT_GROUP1` and `MAINT_GROUP2`. `MAINT_GROUP1` has `UTILIZATION_LIMIT` set to 40%. However, the limit for `MAINT_SUBPLAN` is set to 50%. Therefore, the limit for consumer group `MAINT_GROUP1` is computed as 40% of 50%, or 20%. For an example of how to compute `UTILIZATION_LIMIT` for a consumer group when limits are specified for both the consumer group and the subplan to which the group belongs, see " Example 4 - Specifying a Utilization Limit for Consumer Groups and Subplans ".

See Also:

- " Creating Resource Plan Directives "
- " Putting It All Together: Oracle Database Resource Manager Examples "

**Parent topic:** CPU

#### 27.3.2 Exadata I/O

Management attributes enable you to specify CPU resource allocation for Exadata I/O.

See Also:

The Exadata documentation for information about using management attributes for Exadata I/O

**Parent topic:** The Types of Resources Managed by the Resource Manager

#### 27.3.3 Parallel Execution Servers

Resource Manager can manage usage of the available parallel execution servers for a database.

- Degree of Parallelism Limit  
	You can limit the maximum degree of parallelism for any operation within a consumer group. Use the `PARALLEL_DEGREE_LIMIT_P1` directive attribute to specify the degree of parallelism for a consumer group.
- Parallel Server Limit  
	Use the `PARALLEL_SERVER_LIMIT` directive attribute to specify the maximum percentage of the parallel execution server pool that a particular consumer group can use. The number of parallel execution servers used by a particular consumer group is counted as the sum of the parallel execution servers used by all sessions in that consumer group.
- Parallel Queue Timeout  
	The `PARALLEL_QUEUE_TIMEOUT` directive attribute enables you to specify the maximum time, in seconds, that a parallel statement can wait in the parallel statement queue before it is timed out.

**Parent topic:** The Types of Resources Managed by the Resource Manager

##### 27.3.3.1 Degree of Parallelism Limit

You can limit the maximum degree of parallelism for any operation within a consumer group. Use the `PARALLEL_DEGREE_LIMIT_P1` directive attribute to specify the degree of parallelism for a consumer group.

The degree of parallelism limit applies to one operation within a consumer group; it does not limit the total degree of parallelism across all operations within the consumer group. However, you can combine both the `PARALLEL_DEGREE_LIMIT_P1` and the `PARALLEL_SERVER_LIMIT` directive attributes to achieve the desired control. For more information about the `PARALLEL_SERVER_LIMIT` attribute, see " Parallel Server Limit ".

See Also:

[Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=VLDBG14020) for more information about degree of parallelism in producer/consumer operations

**Parent topic:** Parallel Execution Servers

##### 27.3.3.2 Parallel Server Limit

Use the `PARALLEL_SERVER_LIMIT` directive attribute to specify the maximum percentage of the parallel execution server pool that a particular consumer group can use. The number of parallel execution servers used by a particular consumer group is counted as the sum of the parallel execution servers used by all sessions in that consumer group.

It is possible for a single consumer group to launch enough parallel statements to use all of the available parallel execution servers. If this happens when a high-priority parallel statement from a different consumer group is run, then no parallel execution servers are available to allocate to this group. You can avoid such a scenario by limiting the number of parallel execution servers that can be used by a particular consumer group. You can also set the directive `PARALLEL_STMT_CRITICAL` to `BYPASS_QUEUE` for the high-priority consumer group so that parallel statements from the consumer group bypass the parallel statement queue.

For example, assume that the total number of parallel execution servers is 32, as set by the `PARALLEL_SERVERS_TARGET` initialization parameter, and the `PARALLEL_SERVER_LIMIT` directive attribute for the consumer group `MY_GROUP` is set to 50%. This consumer group can use a maximum of 50% of 32, or 16 parallel execution servers.

If your resource plan has management attributes (`MGMT_P1`, `MGMT_P2`, and so on), then a separate parallel statement queue is managed as a First In First Out (FIFO) queue for each management attribute.

If your resource plan does not have any management attributes, then a single parallel statement queue is managed as a FIFO queue.

In the case of an Oracle Real Application Clusters (Oracle RAC) environment, the target number of parallel execution servers is the sum of (`PARALLEL_SERVER_LIMIT` \* `PARALLEL_SERVERS_TARGET` / 100) across all Oracle RAC instances. If a consumer group is using the number of parallel execution servers computed above or more, then it has exceeded its limit, and its parallel statements will be queued.

If a consumer group does not have any parallel statements running within an Oracle RAC database, then the first parallel statement is allowed to exceed the limit specified by `PARALLEL_SERVER_LIMIT`.

Note:

In an Oracle Real Application Clusters (Oracle RAC) environment, the `PARALLEL_SERVER_LIMIT` attribute applies to the entire cluster and not to a single instance.

- Managing Parallel Statement Queuing Using Parallel Server Limit  
	The `PARALLEL_SERVER_LIMIT` attribute enables you to specify when parallel statements from a consumer group can be queued. Oracle Database maintains a separate parallel statement queue for each consumer group.

See Also:

- " Creating Resource Plan Directives "
- " Managing Parallel Statement Queuing Using Parallel Server Limit "
- [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=VLDBG1396) for information about parallel statement queuing

**Parent topic:** Parallel Execution Servers

###### 27.3.3.2.1 Managing Parallel Statement Queuing Using Parallel Server Limit

The `PARALLEL_SERVER_LIMIT` attribute enables you to specify when parallel statements from a consumer group can be queued. Oracle Database maintains a separate parallel statement queue for each consumer group.

A parallel statement from a consumer group is not run and instead is added to the parallel statement queue of that consumer group if the following conditions are met:

- `PARALLEL_DEGREE_POLICY` is set to `AUTO`.
	Setting this initialization parameter to `AUTO` enables automatic degree of parallelism (Auto DOP), parallel statement queuing, and in-memory parallel execution.
	Note that parallel statements which have `PARALLEL_DEGREE_POLICY` set to `MANUAL` or `LIMITED` are executed immediately and are not added to the parallel statement queue.
- The number of active parallel execution servers across all consumer groups exceeds the `PARALLEL_SERVERS_TARGET` initialization parameter setting. This condition applies regardless of whether you specify `PARALLEL_SERVER_LIMIT`. If `PARALLEL_SERVER_LIMIT` is not specified, then it defaults to 100%.
- The sum of the number of active parallel execution servers for the consumer group and the degree of parallelism of the parallel statement exceeds the target number of active parallel execution servers.
	The target number of active parallel execution servers is computed as follows:
	`PARALLEL_SERVER_LIMIT` /100 \* `PARALLEL_SERVERS_TARGET`

See Also:

" Parallel Server Limit "

**Parent topic:** Parallel Server Limit

##### 27.3.3.3 Parallel Queue Timeout

The `PARALLEL_QUEUE_TIMEOUT` directive attribute enables you to specify the maximum time, in seconds, that a parallel statement can wait in the parallel statement queue before it is timed out.

When you use parallel statement queuing, if the database does not have sufficient resources to execute a parallel statement, the statement is queued until the required resources become available. However, there is a chance that a parallel statement may be waiting in the parallel statement queue for longer than is desired. You can prevent such scenarios by specifying the maximum time a parallel statement can wait in the parallel statement queue.

The `PARALLEL_QUEUE_TIMEOUT` attribute can be set for each consumer group. This attribute is applicable even if you do not specify other management attributes (`MGMT_P1`, `MGMT_P2`, and so on) in your resource plan.

See Also:

[Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=VLDBG1396) for more information about parallel statement queuing

Note:

Because the parallel statement queue is clusterwide, all directives related to the parallel statement queue are also clusterwide.

When a parallel statement is timed out, the statement execution ends with the following error message:

```
ORA-07454: queue timeout, n second(s), exceeded
```

If you want more per-workload management, then you must use the following directive attributes:

- `MGMT_P` `n`
	Management attributes control how a parallel statement is selected from the parallel statement queue for execution. You can prioritize the parallel statements of one consumer group over another by setting a higher value for the management attributes of that group.
- `PARALLEL_SERVER_LIMIT`
- `PARALLEL_QUEUE_TIMEOUT`
- `PARALLEL_DEGREE_LIMIT_P1`

See Also:

" Example of Managing Parallel Statements Using Directive Attributes " for more information about the combined use of all the parallel execution server directive attributes

Although parallel execution server usage is monitored for all sessions, the parallel execution server directive attributes you set affect only sessions for which parallel statement queuing is enabled (`PARALLEL_DEGREE_POLICY` is set to `AUTO`). If a session has the `PARALLEL_DEGREE_POLICY` set to `MANUAL`, parallel statements from this session are not queued. However, any parallel execution servers used by such sessions are included in the count that is used to determine the limit for `PARALLEL_SERVER_LIMIT`. Even if this limit is exceeded, parallel statements from this session are not queued.

**Parent topic:** Parallel Execution Servers

#### 27.3.4 Program Global Area (PGA)

To manage PGA resources, Resource Manager can limit the amount of PGA memory that can be allocated to each session in a particular consumer group.

To limit the PGA resources for each session in a consumer group, set the `session_pga_limit` parameter in the package procedure `DBMS_RESOURCE_MANAGER.CREATE_PLAN_DIRECTIVE`. The value of this parameter is the maximum amount of PGA memory, in megabytes, allowed for each session in the consumer group. If a session exceeds the limit set for its consumer group, then error ORA-10260 is raised. This limit includes parallel query slaves and job queue processes.

For example, poorly written PL/SQL code can consume an unbounded amount of PGA. You can use the `session_pga_limit` parameter to limit sessions that run PL/SQL code to ensure that those sessions do not use an inordinate amount of PGA resource.

The following table illustrates a simple resource plan with PGA limits.

Table 27-3 A Simple Resource Plan with PGA Limits

| Consumer Group | session\_pga\_limit Value |
| --- | --- |
| `HIGH_GROUP` | 20 |
| `LOW_GROUP` | 10 |
| `MAINT_SUBPLAN` | Null (unlimited) |
| `OTHER_GROUPS` | Null (unlimited) |

In this resource plan, high priority applications run within `HIGH_GROUP`, and each session in that group is limited to 20 MB of PGA resource. The sessions used by the lower priority applications within `LOW_GROUP` are limited to 10 MB of PGA resource. The sessions used for maintenance jobs within `MAINT_SUPLAN` and other sessions within `OTHER_GROUPS` can use unlimited PGA resource.

Note:

You can limit the PGA usage of a whole instance with the `PGA_AGGREGATE_LIMIT` initialization parameter.

**Parent topic:** The Types of Resources Managed by the Resource Manager

#### 27.3.5 Runaway Queries

Runaway sessions and calls can adversely impact overall performance if they are not managed properly. Resource Manager can take action when a session or call consumes more than a specified amount of CPU, physical I/O, logical I/O, or elapsed time. Resource Manager can either switch the session or call to a consumer group that is allocated a small amount of CPU or terminate the session or call.

Note:

Starting with Oracle Database 12c Release 2 (12.2.0.1), Resource Manager can also limit the amount of PGA memory that can be allocated to each session in a particular consumer group.

- Automatic Consumer Group Switching  
	You can control resource allocation by specifying criteria that, if met, causes the automatic switching of a session to a specified consumer group.
- Canceling SQL and Terminating Sessions  
	You can also specify directives to cancel long-running SQL queries or to terminate long-running sessions based on the amount of system resources consumed.
- Execution Time Limit  
	You can specify a maximum execution time allowed for an operation.

See Also:

" Program Global Area (PGA) "

**Parent topic:** The Types of Resources Managed by the Resource Manager

##### 27.3.5.1 Automatic Consumer Group Switching

You can control resource allocation by specifying criteria that, if met, causes the automatic switching of a session to a specified consumer group.

Typically, this method is used to switch a session from a high-priority consumer group—one that receives a high proportion of system resources—to a lower priority consumer group because that session exceeded the expected resource consumption for a typical session in the group.

See " Specifying Automatic Switching by Setting Resource Limits " for more information.

**Parent topic:** Runaway Queries

##### 27.3.5.2 Canceling SQL and Terminating Sessions

You can also specify directives to cancel long-running SQL queries or to terminate long-running sessions based on the amount of system resources consumed.

See " Specifying Automatic Switching by Setting Resource Limits " for more information.

**Parent topic:** Runaway Queries

##### 27.3.5.3 Execution Time Limit

You can specify a maximum execution time allowed for an operation.

If the database estimates that an operation will run longer than the specified maximum execution time, then the operation is terminated with an error. This error can be trapped and the operation rescheduled.

**Parent topic:** Runaway Queries

#### 27.3.6 Active Session Pool with Queuing

You can control the maximum number of concurrently active sessions allowed within a consumer group. This maximum defines the active session pool.

An active session is a session that is actively processing a transaction or SQL statement. Specifically, an active session is either in a transaction, holding a user enqueue, or has an open cursor and has not been idle for over 5 seconds. An active session is considered active even if it is blocked, for example waiting for an I/O request to complete. When the active session pool is full, a session that is trying to process a call is placed into a queue. When an active session completes, the first session in the queue can then be removed from the queue and scheduled for execution. You can also specify a period after which a session in the execution queue times out, causing the call to terminate with an error.

Active session limits should not be used for OLTP workloads. In addition, active session limits should not be used to implement connection pooling or parallel statement queuing.

To manage parallel statements, you must use parallel statement queuing with the `PARALLEL_SERVER_LIMIT` attribute and management attributes (`MGMT_P1`, `MGMT_P2`, and so on).

**Parent topic:** The Types of Resources Managed by the Resource Manager

#### 27.3.7 Undo Pool

You can specify an undo pool for each consumer group. An undo pool controls the total amount of undo for uncommitted transactions that can be generated by a consumer group.

When the total undo generated by a consumer group exceeds its undo limit, the current DML statement generating the undo is terminated. No other members of the consumer group can perform further data manipulation until undo space is freed from the pool.

**Parent topic:** The Types of Resources Managed by the Resource Manager

#### 27.3.8 Idle Time Limit

You can specify an amount of time that a session can be idle, after which it is terminated.

You can also specify a more stringent idle time limit that applies to sessions that are idle and blocking other sessions.

**Parent topic:** The Types of Resources Managed by the Resource Manager

### 27.4 Creating a Simple Resource Plan

You can quickly create a simple resource plan that is adequate for many situations using the `CREATE_SIMPLE_PLAN` procedure.

This procedure enables you to both create consumer groups and allocate resources to them by executing a single procedure call. Using this procedure, you are not required to invoke the procedures that are described in succeeding sections for creating a pending area, creating each consumer group individually, specifying resource plan directives, and so on.

You specify the following arguments for the `CREATE_SIMPLE_PLAN` procedure:

| Parameter | Description |
| --- | --- |
| `SIMPLE_PLAN` | Name of the plan |
| `CONSUMER_GROUP1` | Consumer group name for first group |
| `GROUP1_PERCENT` | CPU resource allocated to this group |
| `CONSUMER_GROUP2` | Consumer group name for second group |
| `GROUP2_PERCENT` | CPU resource allocated to this group |
| `CONSUMER_GROUP3` | Consumer group name for third group |
| `GROUP3_PERCENT` | CPU resource allocated to this group |
| `CONSUMER_GROUP4` | Consumer group name for fourth group |
| `GROUP4_PERCENT` | CPU resource allocated to this group |
| `CONSUMER_GROUP5` | Consumer group name for fifth group |
| `GROUP5_PERCENT` | CPU resource allocated to this group |
| `CONSUMER_GROUP6` | Consumer group name for sixth group |
| `GROUP6_PERCENT` | CPU resource allocated to this group |
| `CONSUMER_GROUP7` | Consumer group name for seventh group |
| `GROUP7_PERCENT` | CPU resource allocated to this group |
| `CONSUMER_GROUP8` | Consumer group name for eighth group |
| `GROUP8_PERCENT` | CPU resource allocated to this group |

You can specify up to eight consumer groups with this procedure. The only resource allocation method supported is CPU. The plan uses the `EMPHASIS` CPU allocation policy (the default) and each consumer group uses the `ROUND_ROBIN` scheduling policy (also the default). Each consumer group specified in the plan is allocated its CPU percentage at level 2. Also implicitly included in the plan are `SYS_GROUP` (a system-defined group that is the initial consumer group for the users `SYS` and `SYSTEM`) and `OTHER_GROUPS`. The `SYS_GROUP` consumer group is allocated 100% of the CPU at level 1, and `OTHER_GROUPS` is allocated 100% of the CPU at level 3.

Example: Creating a Simple Plan with the CREATE\_SIMPLE\_PLAN Procedure

The following PL/SQL block creates a simple resource plan with two user-specified consumer groups:

```
BEGIN
  DBMS_RESOURCE_MANAGER.CREATE_SIMPLE_PLAN(SIMPLE_PLAN => 'SIMPLE_PLAN1',
   CONSUMER_GROUP1 => 'MYGROUP1', GROUP1_PERCENT => 80,
   CONSUMER_GROUP2 => 'MYGROUP2', GROUP2_PERCENT => 20);
END;
/
```

Executing the preceding statements creates the following plan:

| Consumer Group | Level 1 | Level 2 | Level 3 |
| --- | --- | --- | --- |
| `SYS_GROUP` | 100% | \- | \- |
| `MYGROUP1` | \- | 80% | \- |
| `MYGROUP2` | \- | 20% | \- |
| `OTHER_GROUPS` | \- | \- | 100% |

See Also:

- " Creating a Resource Plan " for more information on the `EMPHASIS` CPU allocation policy
- " Creating Resource Consumer Groups " for more information on the `ROUND_ROBIN` scheduling policy
- " Elements of the Resource Manager "

**Parent topic:** Managing Resources with Oracle Database Resource Manager

### 27.5 Creating a Complex Resource Plan

When your situation calls for a more complex resource plan, you must create the plan, with its directives and consumer groups, in a staging area called the pending area, and then validate the plan before storing it in the data dictionary.

The following is a summary of the steps required to create a complex resource plan.

Note:

A complex resource plan is any resource plan that is not created with the `DBMS_RESOURCE_MANAGER.CREATE_SIMPLE_PLAN` procedure.

Step 1: Create a pending area.

Step 2: Create, modify, or delete consumer groups.

Step 3: Map sessions to consumer groups.

Step 4: Create the resource plan.

Step 5: Create resource plan directives.

Step 6: Validate the pending area.

Step 7: Submit the pending area.

You use procedures in the `DBMS_RESOURCE_MANAGER` PL/SQL package to complete these steps.

- About the Pending Area  
	The pending area is a staging area where you can create a new resource plan, update an existing plan, or delete a plan without affecting currently running applications.
- Creating a Pending Area  
	You create a pending area with the `CREATE_PENDING_AREA` procedure.
- Creating Resource Consumer Groups  
	You create a resource consumer group using the `CREATE_CONSUMER_GROUP` procedure.
- Mapping Sessions to Consumer Groups  
	You can map sessions to consumer groups using the `SET_CONSUMER_GROUP_MAPPING` procedure.
- Creating a Resource Plan  
	You create a resource plan with the `CREATE_PLAN` procedure.
- Creating Resource Plan Directives  
	You use the `CREATE_PLAN_DIRECTIVE` procedure to create resource plan directives. Each directive belongs to a plan or subplan and allocates resources to either a consumer group or subplan.
- Validating the Pending Area  
	At any time when you are making changes in the pending area, you can call `VALIDATE_PENDING_AREA` to ensure that the pending area is valid so far.
- Submitting the Pending Area  
	After you have validated your changes, call the `SUBMIT_PENDING_AREA` procedure to make your changes active.
- Clearing the Pending Area  
	You can clear the pending area at any time using the `CLEAR_PENDING_AREA` procedure.

See Also:

- Predefined Consumer Group Mapping Rules
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=ARPLS050) for details on the `DBMS_RESOURCE_MANAGER` PL/SQL package.
- " Elements of the Resource Manager "

**Parent topic:** Managing Resources with Oracle Database Resource Manager

#### 27.5.1 About the Pending Area

The pending area is a staging area where you can create a new resource plan, update an existing plan, or delete a plan without affecting currently running applications.

When you create a pending area, the database initializes it and then copies existing plans into the pending area so that they can be updated.

Tip:

After you create the pending area, if you list all plans by querying the `DBA_RSRC_PLANS` data dictionary view, you see two copies of each plan: one with the `PENDING` status, and one without. The plans with the `PENDING` status reflect any changes you made to the plans since creating the pending area. Pending changes can also be viewed for consumer groups using `DBA_RSRC_CONSUMER_GROUPS` and for resource plan directives using `DBA_RSRC_PLAN_DIRECTIVES`. See Resource Manager Data Dictionary Views for more information.

After you make changes in the pending area, you validate the pending area and then submit it. Upon submission, all pending changes are applied to the data dictionary, and the pending area is cleared and deactivated.

If you attempt to create, update, or delete a plan (or create, update, or delete consumer groups or resource plan directives) without first creating the pending area, you receive an error message.

Submitting the pending area does not activate any new plan that you create; it just stores new or updated plan information in the data dictionary. However, if you modify a plan that is currently active, the plan is reactivated with the new plan definition. See " Enabling Oracle Database Resource Manager and Switching Plans " for information about activating a resource plan.

When you create a pending area, no other users can create one until you submit or clear the pending area or log out.

**Parent topic:** Creating a Complex Resource Plan

#### 27.5.2 Creating a Pending Area

You create a pending area with the `CREATE_PENDING_AREA` procedure.

Example: Creating a pending area:

The following PL/SQL block creates and initializes a pending area:

```
BEGIN
  DBMS_RESOURCE_MANAGER.CREATE_PENDING_AREA();
END;
/
```

**Parent topic:** Creating a Complex Resource Plan

#### 27.5.3 Creating Resource Consumer Groups

You create a resource consumer group using the `CREATE_CONSUMER_GROUP` procedure.

You can specify the following parameters:

| Parameter | Description |
| --- | --- |
| `CONSUMER_GROUP` | Name to assign to the consumer group. |