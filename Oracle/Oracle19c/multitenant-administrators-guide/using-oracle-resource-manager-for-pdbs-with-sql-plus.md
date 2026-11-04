---
title: "Administrator’s Guide"
book: "Multitenant Administrator's Guide"
doc_id: E96136-19
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/multi/using-oracle-resource-manager-for-pdbs-with-sql-plus.html
tags:
  - oracle
  - 19c
  - multitenant-administrators-guide
---

## 22 Using Oracle Resource Manager for PDBs

Use PL/SQL package procedures to administer Oracle Resource Manager (Resource Manager) to allocate resources to pluggable databases (PDBs) in a multitenant container database (CDB).

This chapter assumes that you meet the following prerequisites:

- You understand how to configure and manage a CDB.
- You understand how to use Resource Manager to allocate resources in a non-CDB.

Note:

- You can complete the tasks in this chapter using SQL\*Plus or Oracle SQL Developer.
- You can also administer the Resource Manager with the graphical user interface of Oracle Enterprise Manager Cloud Control (Cloud Control).
- For simplicity, this chapter refers to PDBs, application roots, and application PDBs as “PDBs.”

See Also:

- " [Administering a Multitenant Environment](managing-a-multitenant-environment.md) "
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-2BEF5482-CF97-4A85-BD90-9195E41E74EF) to learn more about Resource Manager

**Parent topic:** [Using Oracle Features in a Multitenant Environment](using-oracle-features-in-a-multitenant-environment.md)

### Overview of Oracle Resource Manager in a Multitenant Environment

In a CDB, workloads within multiple PDBs can compete for system and CDB resources. Resource plans solve this problem.

In a multitenant environment, Resource Manager operates on two levels:

- CDB level
	Resource Manager can manage the workloads for multiple PDBs that are contending for system and CDB resources. You can specify how resources are allocated to PDBs, and you can limit the resource utilization of specific PDBs. The principal tool is a CDB resource plan.
- PDB level
	Resource Manager can manage the workloads within each PDB. The principal tool is a PDB resource plan.

Resource Manager allocates the resources in two steps:

1. It allocates a portion of the system's resources to each PDB.
2. In a specific PDB, it allocates a portion of system resources obtained in the preceding step to each session connected to the PDB.

Note:

Resource Manager manages activity in the root automatically.

To use Resource Manager in a multitenant environment, you must meet the following prerequisites:

- The CDB must exist and must contain PDBs.
- To complete a task that uses the `DBMS_RESOURCE_MANAGER` package, you must have `ADMINISTER_RESOURCE_MANAGER` system privilege.

- Purpose of Resource Management in a Multitenant Environment  
	Resource Manager can provide more efficient use of resources for a CDB.
- Overview of Resource Plan Directives  
	A **CDB resource plan** allocates resources to its PDBs according to its set of resource plan directives (directives).
- Background and Administrative Tasks and Consumer Groups  
	In a CDB, background and administrative tasks map to the Resource Manager consumer groups that run them optimally.
- Initialization Parameters for PDB-Level Resources  
	Use initialization parameters to control CPU, memory, sessions, and I/O in a PDB.

See Also:

- " [Creating and Configuring a CDB](creating-and-configuring-a-cdb.md) " and " [Creating and Removing PDBs and Application Containers](creating-pdbs.md) "
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-1A627E9A-0138-4DA8-B2E3-E98D3C4AA65D) to learn more about the `DBMS_RESOURCE_MANAGER` package

**Parent topic:** Using Oracle Resource Manager for PDBs

#### Purpose of Resource Management in a Multitenant Environment

Resource Manager can provide more efficient use of resources for a CDB.

When resource allocation decisions for a CDB are left to the operating system, you may encounter the following problems with workload management:

- Inappropriate allocation of resources among PDBs
	The operating system distributes resources equally among all active processes and cannot prioritize one task over another. Therefore, one or more PDBs might use an inordinate amount of the system resources, leaving the other PDBs starved for resources.
- Inappropriate allocation of resources within a single PDB
	One or more sessions connected to a single PDB might use an inordinate amount of the system resources, leaving other sessions connected to the same PDB starved for resources.
- Inconsistent performance of PDBs
	A single PDB might perform inconsistently when other PDBs are competing for more system resources or less system resources at various times.
- Lack of resource usage data for PDBs
	Resource usage data is critical for monitoring and tuning PDBs. It might be possible to use operating system monitoring tools to gather the resource usage data for a non-CDB if it is the only database running on the system. However, in a CDB, operating system monitoring tools are no longer as useful because there are multiple PDBs running on the system.

Resource Manager helps to overcome these problems by allowing the CDB more control over how hardware resources are allocated among the PDBs and within PDBs.

In a CDB with multiple PDBs, some PDBs typically are more important than others. The Resource Manager enables you to prioritize and limit the resource usage of specific PDBs. With the Resource Manager, you can:

- Specify that different PDBs should receive different shares of the system resources so that more resources are allocated to the more important PDBs
- Limit the CPU usage of a particular PDB
- Limit the number of parallel execution servers that a particular PDB can use
- Limit the memory usage of a particular PDB
- Specify the amount of memory guaranteed for a particular PDB
- Specify the maximum amount of memory a particular PDB can use
- Use PDB performance profiles for different sets of PDB
	A performance profile for a set of PDBs can specify shares of system resources, CPU usage, and number of parallel execution servers. PDB performance profiles enable you to manage resources for large numbers of PDBs by specifying Resource Manager directives for profiles instead of individual PDBs.
- Limit the resource usage of different sessions connected to a single PDB
- Limit the I/O generated by specific PDBs
- Monitor the resource usage of PDBs

**Parent topic:** Overview of Oracle Resource Manager in a Multitenant Environment

#### Overview of Resource Plan Directives

A **CDB resource plan** allocates resources to its PDBs according to its set of resource plan directives (directives).

A parent-child relationship exists between a CDB resource plan and its resource plan directives. Each directive references either a set of PDBs in a performance profile, or a single PDB.

You can specify directives for both individual PDBs and for PDB performance profiles in the same CDB. No two directives for the currently active plan can reference the same PDB or the same PDB performance profile.

- PDB Performance Profiles  
	A **PDB performance profile** configures resource plan directives for a set of PDBs that have the same priorities and resource controls.
- Resource Plan Directives  
	Directives control allocation of CPU and parallel execution servers.

**Parent topic:** Overview of Oracle Resource Manager in a Multitenant Environment

##### PDB Performance Profiles

A **PDB performance profile** configures resource plan directives for a set of PDBs that have the same priorities and resource controls.

For example, you might create a performance profiles called Gold, Silver, and Bronze. Each profile specifies a different set of directives depending on the importance of the type of PDB. Gold PDBs are more mission critical than Silver PDBs, which are more mission critical than Bronze PDBs. A PDB specifies its performance profile with the `DB_PERFORMANCE_PROFILE` initialization parameter.

You can use PDB lockdown profiles to specify PDB initialization parameters that control resources, such as `SGA_TARGET` and `PGA_AGGREGATE_LIMIT`. A lockdown profile prevents the PDB administrator from modifying the settings.

Oracle recommends using matching names for performance profiles and lockdown profiles. To prevent PDB owners from switching profiles, Oracle recommends putting the PDB performance profile in the PDB lockdown profile.

**Parent topic:** Overview of Resource Plan Directives

##### Resource Plan Directives

Directives control allocation of CPU and parallel execution servers.

A directive can control the allocation of resources to PDBs based on the share value that you specify for each PDB or PDB performance profile. A higher share value results in more resources. For example, you can specify that one PDB is allocated double the resources allocated to a second PDB by setting the share value for the first PDB twice as high as the share value for the second PDB. Similarly, you can specify that one PDB performance profile is allocated double the resources allocated to a second PDB performance profile by setting the share value for the first PDB performance profile twice as high as the share value for the second PDB performance profile. The settings apply to the set of PDBs that use each profile.

You can also specify utilization limits for PDBs and PDB performance profiles. The limit controls allocation to the PDB or performance profile. For example, the limit can control how much CPU a PDB gets as a percentage of the total CPU available to the CDB.

You can use both shares and utilization limits together for precise control over the resources allocated to each PDB and PDB performance profile in a CDB.

See Also:

" [About Restricting PDB Users for Enhanced Security](administering-a-cdb-with-sql-plus.md) " for more information about PDB lockdown profiles

**Parent topic:** Overview of Resource Plan Directives

#### Background and Administrative Tasks and Consumer Groups

In a CDB, background and administrative tasks map to the Resource Manager consumer groups that run them optimally.

Resource Manager uses the following rules to map a task to a consumer group:

- A task is mapped to a consumer group in the container that starts the task.
	If a task starts in the CDB root, then the task maps to a consumer group in the CDB root. If the task starts in a PDB, then the task maps to a consumer group in the PDB.
- Many maintenance and administrative tasks automatically map to a consumer group.
	For example, automated maintenance tasks map to `ORA$AUTOTASK`. In certain cases, the tasks map to a consumer group, but the mapping is modifiable. Such tasks include RMAN backup, RMAN image copy, Oracle Data Pump, and In-Memory population.

Note:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-AC101C05-DD43-445C-85F7-0A04DCBC2EE0) to learn more about the mapping rules for predefined consumer groups

**Parent topic:** Overview of Oracle Resource Manager in a Multitenant Environment

#### Initialization Parameters for PDB-Level Resources

Use initialization parameters to control CPU, memory, sessions, and I/O in a PDB.

- CPU-Related Initialization Parameters for PDBs  
	The `CPU_COUNT` initialization parameter specifies the number of CPUs available for Oracle Database to use.
- Memory-Related Initialization Parameters for PDBs  
	Several initialization parameters control the memory usage of a PDB.
- Session-Related Initialization Parameters for PDBs  
	Several initialization parameters control how sessions consume resources in a PDB.
- I/O-Related Initialization Parameters for PDBs  
	The `MAX_IOPS` and `MAX_MBPS` initialization parameters limit the disk I/O generated by a PDB.

**Parent topic:** Overview of Oracle Resource Manager in a Multitenant Environment

##### Memory-Related Initialization Parameters for PDBs

Several initialization parameters control the memory usage of a PDB.

When the PDB is the current container, the initialization parameters in the following table control the memory usage of the current PDB. When one or more of these parameters is set for a PDB, ensure that the CDB and the other PDBs have sufficient memory for their operations. The initialization parameters control the memory usage of PDBs only if the following conditions are met:

- The `NONCDB_COMPATIBLE` initialization parameter is set to `false` in the CDB root.
- The `MEMORY_TARGET` initialization parameter is not set or is set to `0` (zero) in the CDB root.

Note:

Oracle recommends against setting the `DB_CACHE_SIZE` and `SHARED_POOL_SIZE` parameters in a PDB. The only shared memory sizing parameter that should be set in a PDB is `SGA_TARGET`, which specifies the maximum SGA that the PDB can use at any time.

Table 22-1 Initialization Parameters That Control the Memory Usage of PDBs

| Initialization Parameter | Description |
| --- | --- |
| `DB_CACHE_SIZE` | Sets the minimum, guaranteed buffer cache space for the PDB.  The following requirements must be met:  - It must be less than or equal to 50% of the setting for the `DB_CACHE_SIZE` in the CDB root. - The sum of the `DB_CACHE_SIZE` settings for all PDBs must be less than or equal to 50% of the setting for the `DB_CACHE_SIZE` in the CDB root.  These requirements do not apply if the `SGA_TARGET` initialization parameter is set to a nonzero value in the CDB root.  When the `SGA_TARGET` initialization parameter is set to a nonzero, the following requirements must be met:  - The values of `DB_CACHE_SIZE` plus `SHARED_POOL_SIZE` in a PDB must be less than or equal to 50% of the PDB’s `SGA_TARGET` value. - The values of `DB_CACHE_SIZE` plus `SHARED_POOL_SIZE` in a PDB must be less than or equal to 50% of the `SGA_TARGET` value at the CDB level. - The sum of `DB_CACHE_SIZE` plus `SHARED_POOL_SIZE` across all the PDBs in a CDB must be less than or equal to 50% of the `SGA_TARGET` value at the CDB level. |
| `SHARED_POOL_SIZE` | Sets the minimum, guaranteed shared pool space for the PDB.  The following requirements must be met:  - It must be less than or equal to 50% of the setting for the `SHARED_POOL_SIZE` in the CDB root. - The sum of the `SHARED_POOL_SIZE` settings for all PDBs must be less than or equal to 50% of the setting for the `SHARED_POOL_SIZE` in the CDB root.  These requirements do not apply if the `SGA_TARGET` initialization parameter is set to a nonzero value in the CDB root.  When the `SGA_TARGET` initialization parameter is set to a nonzero, the following requirements must be met:  - The values of `DB_CACHE_SIZE` plus `SHARED_POOL_SIZE` in a PDB must be less than or equal to 50% of the PDB’s `SGA_TARGET` value. - The values of `DB_CACHE_SIZE` plus `SHARED_POOL_SIZE` in a PDB must be less than or equal to 50% of the `SGA_TARGET` value at the CDB level. - The sum of `DB_CACHE_SIZE` plus `SHARED_POOL_SIZE` across all the PDBs in a CDB must be less than or equal to 50% of the `SGA_TARGET` value at the CDB level. |
| `SGA_MIN_SIZE` | Sets the minimum SGA size for the PDB.  The following requirements must be met:  - It must be less than or equal to 50% of the setting for the `SGA_TARGET` in the CDB root. - It must be less than or equal to 50% of the setting for the `SGA_TARGET` in the PDB. - The sum of the `SGA_MIN_SIZE` settings for all PDBs must be less than or equal to 50% of the setting for the `SGA_TARGET` in the CDB root.  These requirements do not apply if the `SGA_TARGET` initialization parameter is not set or is set to `0` (zero) in the CDB root. |
| `SGA_TARGET` | Sets the maximum SGA size for the PDB.  The `SGA_TARGET` setting in the PDB is enforced only if the `SGA_TARGET` initialization parameter is set to a nonzero value in the CDB root. The `SGA_TARGET` setting in the PDB must be less than or equal to the `SGA_TARGET` setting in the CDB root. |
| `PGA_AGGREGATE_LIMIT` | Sets the maximum PGA size for the PDB.  The following requirements must be met:  - It must be less than or equal to the setting for the `PGA_AGGREGATE_LIMIT` in the CDB root. - It must be greater than or equal to two times the setting for the `PGA_AGGREGATE_TARGET` in the PDB. |
| `PGA_AGGREGATE_TARGET` | Sets the target aggregate PGA size for the PDB.  The following requirements must be met:  - It must be less than or equal to the `PGA_AGGREGATE_TARGET` value set at the CDB level. - It must be less than or equal to 50% of the `PGA_AGGREGATE_LIMIT` initialization parameter value set at the CDB level. - It must be less than or equal to 50% of the `PGA_AGGREGATE_LIMIT` value set in the PDB. |

Example 22-1 Setting the Maximum Aggregate PGA Memory Available for a PDB

With the PDB as the current container, run the following SQL statement to set the `PGA_AGGREGATE_LIMIT` initialization parameter both in memory and in the SPFILE to 90 MB:

```
ALTER SYSTEM SET PGA_AGGREGATE_LIMIT = 90M SCOPE = BOTH;
```

Example 22-2 Setting the Minimum SGA Size for a PDB

i

With the PDB as the current container, run the following SQL statement to set the `SGA_MIN_SIZE` initialization parameter both in memory and in the SPFILE to 500 MB:

```
ALTER SYSTEM SET SGA_MIN_SIZE = 500M SCOPE = BOTH;
```

**Parent topic:** Initialization Parameters for PDB-Level Resources

##### Session-Related Initialization Parameters for PDBs

Several initialization parameters control how sessions consume resources in a PDB.

Table 22-2 Initialization Parameters That Control the Session Usage of PDBs

| Initialization Parameter | Description (When Set at PDB Level) | Default at PDB Level |
| --- | --- | --- |
| `SESSIONS` | Sets the maximum of number of sessions that a PDB can use.  If the PDB tries to use more sessions than configured by its `SESSIONS` parameter, then an `ORA-00018` error message is generated. For PDBs, the `SESSIONS` parameter does not count recursive sessions and therefore does not require the 10% adjustment.  The `SESSIONS` parameter for a PDB can only be modified by the PDB. It cannot be set higher than the `SESSIONS` value set at the CDB level. | `SESSIONS` at the CDB level multiplied by ratio of PDB-level `CPU_COUNT` / CDB-level `CPU_COUNT` |
| `MAX_IDLE_TIME` | Specifies the maximum number of minutes that a session can be idle. After the maximum is reached, Oracle Database automatically terminates the session. | `0` (not set) |
| `MAX_IDLE_BLOCKER_TIME` | Sets the number of minutes that a session can be idle before it is a candidate for termination.  With this parameter, an idle session is terminated if it is blocking another session. Oracle Database considers a session blocked in any of the following situations:  - The session is holding a lock needed by another session. - The session is a parallel operation and its consumer group, PDB, or CDB has either reached its maximum parallel server limit or has queued parallel operations. - The PDB or database instance for the session is about to hit its sessions or processes limit.  Unlike `MAX_IDLE_TIME`, `MAX_IDLE_BLOCKER_TIME` terminates resources only when they are needed. | `0` (not set) |

**Parent topic:** Initialization Parameters for PDB-Level Resources

##### I/O-Related Initialization Parameters for PDBs

The `MAX_IOPS` and `MAX_MBPS` initialization parameters limit the disk I/O generated by a PDB.

A large amount of disk I/O can cause poor performance. Several factors can result in excess disk I/O, such as poorly designed SQL or index and table scans in high-volume transactions. If one PDB is generating a large amount of disk I/O, then it can degrade the performance of other PDBs in the same CDB.

Use one or both of the following initialization parameters to limit the I/O generated by a specific PDB:

- The `MAX_IOPS` initialization parameter limits the number of I/O operations for each second.
- The `MAX_MBPS` initialization parameter limits the megabytes for I/O operations for each second.

If you set both preceding initialization parameters for a single PDB, then Oracle Database enforces both limits. Note that these limits are not enforced for Oracle Exadata, which uses I/O Resource Management (IORM) to manage I/Os between PDBs.

If these initialization parameters are set with the CDB root as the current container, then the values become the default values for all containers in the CDB. If they are set with an application root as the current container, then the values become the default values for all application PDBs in the application container. When they are set with a PDB or application PDB as the current container, then the settings take precedence over the default settings in the CDB root or the application root. These parameters cannot be set in a non-CDB.

The default for both initialization parameters is 0 (zero). If these initialization parameters are set to 0 (zero) in a PDB, and the CDB root is set to 0, then there is no I/O limit for the PDB. If these initialization parameters are set to 0 (zero) in an application PDB, and its application root is set to 0, then there is no I/O limit for the application PDB.

Critical I/O operations, such as ones for the control file and password file, are exempted from the limit and continue to run even if the limit is reached. However, all I/O operations, including critical I/O operations, are counted when the number of I/O operations and the megabytes for I/O operations are calculated.

You can use the `DBA_HIST_RSRC_PDB_METRIC` view to calculate a reasonable I/O limit for a PDB. Consider the values in the following columns when calculating a limit: `IOPS`, `IOMBPS`, `IOPS_THROTTLE_EXEMPT`, and `IOMBPS_THROTTLE_EXEMPT`. The `rsmgr:io rate limit` wait event indicates that a limit was reached.

Example 22-3 Limiting the I/O Generated by a PDB

With the PDB as the current container, run the following SQL statement to set the `MAX_IOPS` initialization parameter both in memory and in the SPFILE to a limit of 1,000 I/O operations for each second:

```
ALTER SYSTEM SET MAX_IOPS = 1000 SCOPE = BOTH;
```

Example 22-4 Limiting the Megabytes of I/O Generated by a PDB

With the PDB as the current container, run the following SQL statement to set the `MAX_MBPS` initialization parameter both in memory and in the SPFILE to a limit of 200 MB of I/O for each second:

```
ALTER SYSTEM SET MAX_MBPS = 200 SCOPE = BOTH;
```

See Also:

- " [Modifying a PDB at the System Level](administering-pdbs-with-sql-plus.md) "
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=REFRN-GUID-7D89F457-0CE6-4152-98EA-7F1BE4E0ADC7) for more information about the `MAX_IOPS` initialization parameter
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=REFRN-GUID-9F7E0143-76FB-488A-9A04-2D85F1417CB6) for more information about the `MAX_MBPS` initialization parameter

**Parent topic:** Initialization Parameters for PDB-Level Resources

### Managing CDB Resource Plans

In a CDB, PDBs might have different levels of priority. You can create CDB resource plans to distribute resources to different PDBs based on these priorities.

- About CDB Resource Plans  
	Create CDB resource plans that allocate shares and resource limits for PDBs.
- Creating a CDB Resource Plan for Managing PDBs  
	To create a CDB resource plan for individual PDBs and define the directives for the plan, use the `DBMS_RESOURCE_MANAGER` package.
- Creating a CDB Resource Plan for Managing PDBs: Scenario  
	This scenario illustrates each of the steps involved in creating a CDB resource plan for individual PDBs.
- Creating a CDB Resource Plan with PDB Performance Profiles  
	Use the `DBMS_RESOURCE_MANAGER` package to create a CDB resource plan for PDB performance profiles and define the directives for the plan. Each PDB that uses a profile adopts the CDB resource plan directive.
- Creating a CDB Resource Plan for PDB Performance Profiles: Scenario  
	This scenario illustrates the steps involved in creating a CDB resource plan for PDB performance profiles.
- Enabling a CDB Resource Plan  
	You enable the Resource Manager for a CDB by setting the `RESOURCE_MANAGER_PLAN` initialization parameter in the root.
- Modifying a CDB Resource Plan  
	Modifying a CDB resource plan includes tasks such as updating the plan, creating, updating, or deleting plan directives for PDBs, and updating default directives.
- Disabling a CDB Resource Plan  
	Disable the Resource Manager for a CDB by unsetting the `RESOURCE_MANAGER_PLAN` initialization parameter in the CDB root.
- Viewing Information About Plans and Directives in a CDB  
	You can view information about CDB resource plans, CDB resource plan directives, and predefined resource plans in a CDB.

**Parent topic:** Using Oracle Resource Manager for PDBs

#### About CDB Resource Plans

Create CDB resource plans that allocate shares and resource limits for PDBs.

- Shares for Allocating Resources to PDBs  
	To allocate resources among PDBs, assign a share value to each PDB or performance profile. A higher share value results in more guaranteed resources for a PDB or the PDBs that use the performance profile.
- Utilization Limits for PDBs  
	A utilization limit restrains the system resource usage of a specific PDB or a specific PDB performance profile.
- The Default Directive for PDBs  
	When you do not explicitly define directives for a PDB, the PDB uses the default directive for PDBs.

**Parent topic:** Managing CDB Resource Plans

##### Shares for Allocating Resources to PDBs

To allocate resources among PDBs, assign a share value to each PDB or performance profile. A higher share value results in more guaranteed resources for a PDB or the PDBs that use the performance profile.

Specify a share value for a PDB using the `DBMS_RESOURCE_MANAGER.CREATE_CDB_PLAN_DIRECTIVE` procedure and for a PDB performance profile using the `DBMS_RESOURCE_MANAGER.CREATE_CDB_PROFILE_DIRECTIVE` procedure. In both cases, the `shares` parameter specifies the share value for the PDB. Multiple PDBs can use the same PDB performance profile.

The following figure shows an example of three PDBs with share values specified for them in a CDB resource plan.

Figure 22-1 Shares in a CDB Resource Plan

![Figure 22-1 Shares in a CDB Resource Plan](img/admin_vm_101.png)

> This illustration shows a CDB resource plan in root. The plan includes three directives, and each directive specifies a share for a PDB. One directive specifies three shares for the salespdb PDB, a second share specifies three shares for the servicespdb PDB, and a third directive specifies one share for the hrpdb PDB.


The preceding figure shows that the total number of shares is seven (3 plus 3 plus 1). The `salespdb` and the `servicespdb` PDB are each guaranteed 3/7 of the resources, while the `hrpdb` PDB is guaranteed 1/7 of the resources. However, any PDB can use more than the guaranteed amount of a resource when no resource contention exists.

The following table shows the resource allocation to the PDBs in the preceding figure based on the share values. The table assumes that loads of the PDBs consume all system resources allocated.

Table 22-3 Resource Allocation for Sample PDBs

| Resource | Resource Allocation | See Also |
| --- | --- | --- |
| CPU | The `salespdb` and `servicespdb` PDBs can consume the same amount of CPU resources. The `salespdb` and `servicespdb` PDBs are each guaranteed three times more CPU resource than the `hrpdb` PDB. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-514BDECF-BE80-4CCA-A00D-EF37C2CFC435) for more information about this resource |
| Parallel execution servers | Queued parallel queries from the `salespdb` and `servicespdb` PDBs are selected equally. Queued parallel queries from the `salespdb` and `servicespdb` PDBs are selected three times as often as queued parallel queries from the `hrpdb` PDB. | [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-15685C9E-AD79-4342-BFA9-18D478915267) for more information about this resource |

**Parent topic:** About CDB Resource Plans

##### Utilization Limits for PDBs

A utilization limit restrains the system resource usage of a specific PDB or a specific PDB performance profile.

You can specify utilization limits for CPU and parallel execution servers. Utilization limits for a PDB are set by the CDB resource plan.

The following table describes utilization limits for PDBs and the Resource Manager action taken when a PDB reaches a utilization limit. For limits specified with a PDB performance profile, the limit applies to every PDB that uses the PDB performance profile. For example, if `pdb1` and `pdb20` have a performance profile `BRONZE`, and if `BRONZE` has a limit set to 10%, then `pdb1` has a 10% limit and `pdb20` has a 10% limit.

Table 22-4 Utilization Limits for PDBs

| Resource | Resource Utilization Limit | Resource Manager Action When Limit Is Reached |
| --- | --- | --- |
| CPU | The CPU utilization limit for sessions connected to a PDB is set by the `utilization_limit` parameter in subprograms of the `DBMS_RESOURCE_MANAGER` package. The `utilization_limit` parameter specifies the percentage of the system resources that a PDB can use. The value ranges from 0 to 100.  You can also limit CPU for a PDB by setting the initialization parameter `CPU_COUNT`. For example, if you set the `CPU_COUNT` to `8`, then the PDB cannot use more than 8 CPUs at any time. If both `utilization_limit` and `CPU_COUNT` are specified, then the more restrictive (lower) value is enforced. | Resource Manager throttles the PDB sessions so that the CPU utilization for the PDB does not exceed the utilization limit. |
| Parallel execution servers | You can limit the number of parallel execution servers in a PDB by means of parallel statement queuing. The limit is a “queuing point” because the database queues parallel queries when the limit is reached.  You can set the limit (queuing point) in either of the following ways:  - The value of the `PARALLEL_SERVERS_TARGET` initialization parameter setting in the PDB - The value of the `PARALLEL_SERVERS_TARGET` initialization parameter setting in the CDB root multiplied by the value of the `parallel_server_limit` directive set for the PDB in the CDB resource manager plan 	For example, if the `PARALLEL_SERVERS_TARGET` initialization parameter is set to 200 in the CDB root, and if the `parallel_server_limit` directive for a PDB is set to 10%, then utilization limit for the PDB is 20 parallel execution servers (200 \*.10).  If the limit is set in both preceding ways, then the lower limit of the two is used. See [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=REFRN-GUID-B6CE9EA3-B846-4AA7-B668-FD3BEE433A24) for the default value for `PARALLEL_SERVERS_TARGET`.  Note: Oracle recommends using the `PARALLEL_SERVERS_TARGET` initialization parameter instead of the `parallel_server_limit` directive in a CDB plan. | Resource Manager queues parallel queries when the number of parallel execution servers used by the PDB would exceed the limit.  Note: In a CDB, parallel statements are queued based on the `PARALLEL_SERVERS_TARGET` settings at both the PDB and CDB level. A statement is queued when the number of parallel servers used by the PDB exceeds the target for the PDB or when the number of parallel servers used by all PDBs exceeds the target for the CDB. |

The following figure shows an example of three PDBs with shares and utilization limits specified for them in a CDB resource plan.

Figure 22-2 Shares and Utilization Limits in a CDB Resource Plan

![Figure 22-2 Shares and Utilization Limits in a CDB Resource Plan](img/admin_vm_104.png)

> This illustration shows a CDB resource plan in root. The plan includes three directives, and each directive specifies a share, a utilization\_limit, and a parallel\_server\_limit for a PDB. One directive specifies the following for the salespdb PDB:
>
> - share = 3
> - utilization\_limit = 100
> - parallel\_server\_limit = 100
> - memory\_limit = 100
>
> A second directive specifies the following for the servicespdb PDB:
>
> - share = 3
> - utilization\_limit = 100
> - parallel\_server\_limit = 100
> - memory\_limit = 100
>
> A third directive specifies the following for the hrpdb PDB:
>
> - share = 1
> - utilization\_limit = 70
> - parallel\_server\_limit = 70
> - memory\_limit = 70


The preceding figure shows that there are no utilization limits on the `salespdb` and `servicespdb` PDBs because `utilization_limit` and `parallel_server_limit` are both set to 100% for them. However, the `hrpdb` PDB is limited to 70% of the applicable system resources because `utilization_limit` and `parallel_server_limit` are both set to 70%.

Note:

This scenario assumes that the `PARALLEL_SERVERS_TARGET` initialization parameter does not specify a lower limit in a PDB. When the `PARALLEL_SERVERS_TARGET` initialization parameter specifies a lower limit for parallel execution servers in a PDB, the lower limit is used.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-B1E0B0A8-2709-4A1C-821D-9CEC35B03603)
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=REFRN-GUID-78CDCDE7-5A1D-4AC1-B5BD-B185CB296416) to learn about `CPU_COUNT`

**Parent topic:** About CDB Resource Plans

##### The Default Directive for PDBs

When you do not explicitly define directives for a PDB, the PDB uses the default directive for PDBs.

The following table shows the attributes of the initial default directive for PDBs.

Table 22-5 Initial Default Directive Attributes for PDBs

| Directive Attribute | Value |
| --- | --- |
| `shares` | 1 |
| `utilization_limit` | 100 |
| `parallel_server_limit` | 100 |

When a PDB is plugged into a CDB and no directive is defined for it, the PDB uses the default directive for PDBs.

You can create new directives for the new PDB. You can also change the default directive attribute values for PDBs by using the `UPDATE_CDB_DEFAULT_DIRECTIVE` procedure in the `DBMS_RESOURCE_MANAGER` package.

When a PDB is unplugged from a CDB, the directive for the PDB is retained. If the same PDB is plugged back into the CDB, then it uses the directive defined for it if the directive was not deleted manually.

Figure 22-3 shows an example of the default directive in a CDB resource plan.

Figure 22-3 Default Directive in a CDB Resource Plan

![Figure 22-3 Default Directive in a CDB Resource Plan](img/admin_vm_103.png)

> This illustration shows a CDB resource plan in root. The plan includes three directives and one default directive, and each directive specifies a share, a utilization\_limit, and a parallel\_server\_limit for a PDB. One directive specifies the following for the salespdb PDB:
>
> - share = 3
> - utilization\_limit = 100
> - parallel\_server\_limit = 100
> - memory\_limit = 100
>
> A second directive specifies the following for the servicespdb PDB:
>
> - share = 3
> - utilization\_limit = 100
> - parallel\_server\_limit = 100
> - memory\_limit = 100
>
> A third directive specifies the following for the hrpdb PDB:
>
> - share = 1
> - utilization\_limit = 70
> - parallel\_server\_limit = 70
> - memory\_limit = 70
>
> The default directive specifies the following for any PDB with no directive:
>
> - share = 1
> - utilization\_limit = 50
> - parallel\_server\_limit = 50
> - memory\_limit = 50
>
> The illustration shows the default directive applied to two PDBs with no directive, `marketingpdb` and `testingpdb`, and three dots indicate that the default directive applies to any number of PDBs with no directive.


Figure 22-3 shows that the default PDB directive specifies that the `share` is 1, the `utilization_limit` is 50%, and the `parallel_server_limit` is 50%. Any PDB that is part of the CDB and does not have directives defined for it uses the default PDB directive. Figure 22-3 shows the PDBs `marketingpdb` and `testingpdb` using the default PDB directive. Therefore, `marketingpdb` and `testingpdb` each get 1 share and utilization limits of 50.

See Also:

- " Creating New CDB Resource Plan Directives for a PDB "
- " Updating the Default Directive for PDBs in a CDB Resource Plan "
- " [Creating and Removing PDBs and Application Containers](creating-pdbs.md) "
- " [Unplugging a PDB from a CDB](removing-a-pdb.md) "
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-CDF30CA7-5A14-4C17-8C32-746F0763A7C9) for information about the parallel server limit

**Parent topic:** About CDB Resource Plans

#### Creating a CDB Resource Plan for Managing PDBs

To create a CDB resource plan for individual PDBs and define the directives for the plan, use the `DBMS_RESOURCE_MANAGER` package.

The general steps for creating a CDB resource plan for individual PDBs are the following:

1. Create the pending area using the `CREATE_PENDING_AREA` procedure.
2. Create the CDB resource plan using the `CREATE_CDB_PLAN` procedure.
3. Create directives for the PDBs using the `CREATE_CDB_PLAN_DIRECTIVE` procedure.
4. (Optional) Update the default PDB directive using the `UPDATE_CDB_DEFAULT_DIRECTIVE` procedure.
5. Validate the pending area using the `VALIDATE_PENDING_AREA` procedure.
6. Submit the pending area using the `SUBMIT_PENDING_AREA` procedure.

**Parent topic:** Managing CDB Resource Plans

#### Creating a CDB Resource Plan for Managing PDBs: Scenario

This scenario illustrates each of the steps involved in creating a CDB resource plan for individual PDBs.

The scenario assumes that you want to create a CDB resource plan for a CDB named `newcdb`. The plan includes a directive for each PDB. In this scenario, you also update the default directive and the AutoTask directive.

The directives are defined using various procedures in the `DBMS_RESOURCE_MANAGER` package. The attributes of each directive are defined using parameters in these procedures. Table 22-6 describes the types of directives in the plan.

Table 22-6 Attributes for PDB Directives in a CDB Resource Plan

| Directive Attribute | Description | See Also |
| --- | --- | --- |
| `shares` | Resource allocation share for CPU and parallel execution server resources. | " Shares for Allocating Resources to PDBs " |
| `utilization_limit` | Resource utilization limit for CPU. | " Utilization Limits for PDBs " |
| `parallel_server_limit` | Maximum percentage of parallel execution servers that a PDB can use before queuing parallel statements.  When the `parallel_server_limit` directive is specified for a PDB, the limit is the `PARALLEL_SERVERS_TARGET` value of the CDB root multiplied by the value of the `parallel_server_limit` parameter in the `CREATE_CDB_PLAN_DIRECTIVE` procedure.  Note: Oracle recommends using the `PARALLEL_SERVERS_TARGET` initialization parameter instead of the `parallel_server_limit` directive in a CDB plan. | " Utilization Limits for PDBs " |

Table 22-7 describes how the CDB resource plan allocates resources to its PDBs using the directive attributes described in Table 22-6.

Table 22-7 Sample Directives for PDBs in a CDB Resource Plan

| PDB | shares Directive | utilization\_limit Directive | parallel\_server\_limit Directive |
| --- | --- | --- | --- |
| `salespdb` | 3 | Unlimited | Unlimited |
| `servicespdb` | 3 | Unlimited | Unlimited |
| `hrpdb` | 1 | 70 | 70 |
| Default | 1 | 50 | 50 |
| AutoTask | 1 | 75 | 75 |

The `salespdb` and `servicespdb` PDBs are more important than the other PDBs in the CDB. Therefore, they get a higher share (3), unlimited CPU utilization resource, and unlimited parallel execution server resource.

The default directive applies to PDBs for which specific directives have not been defined. For this scenario, assume that the CDB has several PDBs that use the default directive. This scenario updates the default directive.

In addition, this scenario updates the AutoTask directive. The AutoTask directive applies to automatic maintenance tasks that are run in the root maintenance window.

To create a CDB resource plan:

1. Create a pending area using the `CREATE_PENDING_AREA` procedure:
	```
	exec DBMS_RESOURCE_MANAGER.CREATE_PENDING_AREA();
	```
2. Create a CDB resource plan named `newcdb_plan` using the `CREATE_CDB_PLAN` procedure:
	```
	BEGIN
	  DBMS_RESOURCE_MANAGER.CREATE_CDB_PLAN(
	    plan    => 'newcdb_plan',
	    comment => 'CDB resource plan for newcdb');
	END;
	/
	```
3. Create the CDB resource plan directives for the PDBs using the `CREATE_CDB_PLAN_DIRECTIVE` procedure. Each directive specifies how resources are allocated to a specific PDB.
	Table 22-7 describes the directives for the `salespdb`, `servicespdb`, and `hrpdb` PDBs in this scenario. Run the following procedures to create these directives:
	```
	BEGIN
	  DBMS_RESOURCE_MANAGER.CREATE_CDB_PLAN_DIRECTIVE(
	    plan                  => 'newcdb_plan', 
	    pluggable_database    => 'salespdb', 
	    shares                => 3, 
	    utilization_limit     => 100,
	    parallel_server_limit => 100);
	END;
	/
	BEGIN
	  DBMS_RESOURCE_MANAGER.CREATE_CDB_PLAN_DIRECTIVE(
	    plan                  => 'newcdb_plan', 
	    pluggable_database    => 'servicespdb', 
	    shares                => 3, 
	    utilization_limit     => 100,
	    parallel_server_limit => 100);
	END;
	/
	BEGIN
	  DBMS_RESOURCE_MANAGER.CREATE_CDB_PLAN_DIRECTIVE(
	    plan                  => 'newcdb_plan', 
	    pluggable_database    => 'hrpdb', 
	    shares                => 1, 
	    utilization_limit     => 70,
	    parallel_server_limit => 70);
	END;
	/
	```
	All other PDBs in this CDB use the default PDB directive.
4. If the current default CDB resource plan directive for PDBs does not meet your requirements, then update the directive using the `UPDATE_CDB_DEFAULT_DIRECTIVE` procedure.
	The default directive applies to PDBs for which specific directives have not been defined. See " The Default Directive for PDBs " for more information.
	Table 22-7 describes the default directive that PDBs use in this scenario. Run the following procedure to update the default directive:
	```
	BEGIN
	  DBMS_RESOURCE_MANAGER.UPDATE_CDB_DEFAULT_DIRECTIVE(
	    plan                      => 'newcdb_plan', 
	    new_shares                => 1, 
	    new_utilization_limit     => 50,
	    new_parallel_server_limit => 50);
	END;
	/
	```
5. Validate the pending area using the `VALIDATE_PENDING_AREA` procedure:
	```
	exec DBMS_RESOURCE_MANAGER.VALIDATE_PENDING_AREA();
	```
6. Submit the pending area using the `SUBMIT_PENDING_AREA` procedure:
	```
	exec DBMS_RESOURCE_MANAGER.SUBMIT_PENDING_AREA();
	```

**Parent topic:** Managing CDB Resource Plans

#### Creating a CDB Resource Plan with PDB Performance Profiles

Use the `DBMS_RESOURCE_MANAGER` package to create a CDB resource plan for PDB performance profiles and define the directives for the plan. Each PDB that uses a profile adopts the CDB resource plan directive.

The general steps for creating a CDB resource plan with PDB performance profiles are the following:

1. Create the pending area using the `CREATE_PENDING_AREA` procedure.
2. Create the CDB resource plan using the `CREATE_CDB_PLAN` procedure.
3. Create directives for the PDB performance profiles using the `CREATE_CDB_PROFILE_DIRECTIVE` procedure.
4. (Optional) Update the default PDB directive using the `UPDATE_CDB_DEFAULT_DIRECTIVE` procedure.
5. Validate the pending area using the `VALIDATE_PENDING_AREA` procedure.
6. Submit the pending area using the `SUBMIT_PENDING_AREA` procedure.
7. For each PDB that will use a profile, set the `DB_PERFORMANCE_PROFILE` initialization parameter and specify the profile name.

**Parent topic:** Managing CDB Resource Plans

#### Creating a CDB Resource Plan for PDB Performance Profiles: Scenario

This scenario illustrates the steps involved in creating a CDB resource plan for PDB performance profiles.

The scenario assumes that you want to create a CDB resource plan for a CDB named `newcdb`. The plan includes a directive for each PDB performance profile. In this scenario, you also update the default directive and the AutoTask directive.

In the CDB resource plan, you give each profile a name. In each PDB, you set the `DB_PERFORMANCE_PROFILE` initialization parameter to specify which PDB performance profile the PDB uses.

The directives are defined using various procedures in the `DBMS_RESOURCE_MANAGER` package. The attributes of each directive are defined using parameters in these procedures. The following table describes the types of directives in the plan.

Table 22-8 Attributes for PDB Performance Profile Directives in a CDB Resource Plan

| Directive Attribute | Description | See Also |
| --- | --- | --- |
| `shares` | Resource allocation share for CPU and parallel execution server resources. | " Shares for Allocating Resources to PDBs " |
| `utilization_limit` | Resource utilization limit for CPU. | " Utilization Limits for PDBs " |
| `parallel_server_limit` | Maximum percentage of parallel execution servers that a PDB can use.  When the `parallel_server_limit` directive is specified for a PDB performance profile, the limit is the value of the `PARALLEL_SERVERS_TARGET` initialization parameter setting in the CDB root multiplied by the value of the `parallel_server_limit` parameter in the `CREATE_CDB_PROFILE_DIRECTIVE` procedure. | " Utilization Limits for PDBs " |

The following table describes how the CDB resource plan allocates resources to its PDB performance profiles using the directive attributes described in Table 22-8.

Table 22-9 Sample Directives for PDB Performance Profiles in a CDB Resource Plan

| PDB | shares Directive | utilization\_limit Directive | parallel\_server\_limit Directive |
| --- | --- | --- | --- |
| `gold` | 3 | Unlimited | Unlimited |
| `silver` | 2 | 40 | 40 |
| `bronze` | 1 | 20 | 20 |
| Default | 1 | 10 | 10 |
| AutoTask | 2 | 60 | 60 |

The default directive applies to PDBs for which specific directives have not been defined. For this scenario, assume that the CDB has several PDBs that use the default directive. This scenario updates the default directive.

In addition, this scenario updates the AutoTask directive. The AutoTask directive applies to automatic maintenance tasks that are run in the root maintenance window.

To create a CDB resource plan for PDB performance profiles:

1. For each PDB that will use a profile, set the `DB_PERFORMANCE_PROFILE` initialization parameter to the name of the profile that the PDB will use.
	1. Run an `ALTER SYSTEM` statement to set the parameter.
		For example, with the PDB as the current container, run the following SQL statement:
		```
		ALTER SYSTEM SET DB_PERFORMANCE_PROFILE=gold SCOPE=spfile;
		```
		2. Close the PDB:
		```
		ALTER PLUGGABLE DATABASE CLOSE IMMEDIATE;
		```
		3. Open the PDB:
		```
		ALTER PLUGGABLE DATABASE OPEN;
		```
2. Create a pending area using the `CREATE_PENDING_AREA` procedure:
	```
	exec DBMS_RESOURCE_MANAGER.CREATE_PENDING_AREA();
	```
3. Create a CDB resource plan named `newcdb_plan` using the `CREATE_CDB_PLAN` procedure:
	```
	BEGIN
	  DBMS_RESOURCE_MANAGER.CREATE_CDB_PLAN(
	    plan    => 'newcdb_plan',
	    comment => 'CDB resource plan for newcdb');
	END;
	/
	```
4. Create the CDB resource plan directives for the PDBs using the `CREATE_CDB_PLAN_DIRECTIVE` procedure. Each directive specifies how resources are allocated to a specific PDB.
	Table 22-7 describes the directives for the `gold`, `silver`, and `bronze` profiles in this scenario. Run the following procedures to create these directives:
	```
	BEGIN
	  DBMS_RESOURCE_MANAGER.CREATE_CDB_PROFILE_DIRECTIVE(
	    plan                  => 'newcdb_plan', 
	    profile               => 'gold', 
	    shares                => 3, 
	    utilization_limit     => 100,
	    parallel_server_limit => 100);
	END;
	/
	BEGIN
	  DBMS_RESOURCE_MANAGER.CREATE_CDB_PROFILE_DIRECTIVE(
	    plan                  => 'newcdb_plan', 
	    profile               => 'silver', 
	    shares                => 2, 
	    utilization_limit     => 40,
	    parallel_server_limit => 40);
	END;
	/
	BEGIN
	  DBMS_RESOURCE_MANAGER.CREATE_CDB_PROFILE_DIRECTIVE(
	    plan                  => 'newcdb_plan', 
	    profile               => 'bronze', 
	    shares                => 1, 
	    utilization_limit     => 20,
	    parallel_server_limit => 20);
	END;
	/
	```
	All other PDBs in this CDB use the default PDB directive.
5. If the current default CDB resource plan directive for PDBs does not meet your requirements, then update the directive using the `UPDATE_CDB_DEFAULT_DIRECTIVE` procedure.
	The default directive applies to PDBs for which specific directives have not been defined.
	Table 22-7 describes the default directive that PDBs use in this scenario. Run the following procedure to update the default directive:
	```
	BEGIN
	  DBMS_RESOURCE_MANAGER.UPDATE_CDB_DEFAULT_DIRECTIVE(
	    plan                      => 'newcdb_plan', 
	    new_shares                => 1, 
	    new_utilization_limit     => 10,
	    new_parallel_server_limit => 10);
	END;
	/
	```
6. Validate the pending area using the `VALIDATE_PENDING_AREA` procedure:
	```
	exec DBMS_RESOURCE_MANAGER.VALIDATE_PENDING_AREA();
	```
7. Submit the pending area using the `SUBMIT_PENDING_AREA` procedure:
	```
	exec DBMS_RESOURCE_MANAGER.SUBMIT_PENDING_AREA();
	```

See Also:

" The Default Directive for PDBs "

**Parent topic:** Managing CDB Resource Plans

#### Enabling a CDB Resource Plan

You enable the Resource Manager for a CDB by setting the `RESOURCE_MANAGER_PLAN` initialization parameter in the root.

This parameter specifies the top plan, which is the plan to be used for the current CDB instance. If no plan is specified with this parameter, then the Resource Manager is not enabled.

Prerequisites

Before enabling a CDB resource plan, complete the prerequisites described in " Overview of Oracle Resource Manager in a Multitenant Environment ".

To enable a CDB resource plan:

1. In SQL\*Plus, ensure that the current container is the root.
2. Perform one of the following actions:
	- Use an `ALTER SYSTEM` statement to set the `RESOURCE_MANAGER_PLAN` initialization parameter to the CDB resource plan.
		The following example sets the CDB resource plan to `newcdb_plan` using an `ALTER SYSTEM` statement:
		```
		ALTER SYSTEM SET RESOURCE_MANAGER_PLAN = 'newcdb_plan';
		```
		- In a text initialization parameter file, set the `RESOURCE_MANAGER_PLAN` initialization parameter to the CDB resource plan, and restart the CDB.
		The following example sets the CDB resource plan to `newcdb_plan` in an initialization parameter file:
		```
		RESOURCE_MANAGER_PLAN = 'newcdb_plan'
		```

See Also:

- " [About Container Access in a CDB](administering-a-cdb-with-sql-plus.md) "
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-6B8C0335-D36B-44D3-95BC-82FA2141D967) to learn how to schedule a CDB resource plan change with Oracle Scheduler

**Parent topic:** Managing CDB Resource Plans

#### Modifying a CDB Resource Plan

Modifying a CDB resource plan includes tasks such as updating the plan, creating, updating, or deleting plan directives for PDBs, and updating default directives.

- Updating a CDB Resource Plan  
	You can update a CDB resource plan to change its comment using the `UPDATE_CDB_PLAN` procedure.
- Managing CDB Resource Plan Directives for a PDB  
	You can create, update, and delete CDB resource plan directives for a PDB.
- Managing CDB Resource Plan Directives for a PDB Performance Profile  
	You can create, update, and delete CDB resource plan directives for a PDB performance profile.
- Updating the Default Directive for PDBs in a CDB Resource Plan  
	You can update the default directive for PDBs in a CDB resource plan using the `UPDATE_CDB_DEFAULT_DIRECTIVE` procedure. The default directive applies to PDBs for which specific directives have not been defined.
- Updating the Default Directive for Maintenance Tasks in a CDB Resource Plan  
	You can update the AutoTask directive in a CDB resource plan using the `UPDATE_CDB_AUTOTASK_DIRECTIVE` procedure. The AutoTask directive applies to automatic maintenance tasks that are run in the root maintenance window.
- Deleting a CDB Resource Plan  
	You can delete a CDB resource plan using the `DELETE_CDB_PLAN` procedure.

**Parent topic:** Managing CDB Resource Plans

##### Updating a CDB Resource Plan

You can update a CDB resource plan to change its comment using the `UPDATE_CDB_PLAN` procedure.

Prerequisites

Before updating a CDB resource plan, complete the prerequisites described in " Overview of Oracle Resource Manager in a Multitenant Environment ".

To update a CDB resource plan:

1. In SQL\*Plus, ensure that the current container is the root.
2. Create a pending area:
	```
	exec DBMS_RESOURCE_MANAGER.CREATE_PENDING_AREA();
	```
3. Run the `UPDATE_CDB_PLAN` procedure, and enter a new comment in the `new_comment` parameter.
	For example, the following procedure changes the comment for the `newcdb_plan` CDB resource plan:
	```
	BEGIN
	  DBMS_RESOURCE_MANAGER.UPDATE_CDB_PLAN(
	    plan        => 'newcdb_plan',
	    new_comment => 'CDB plan for PDBs in newcdb');
	END;
	/
	```
4. Validate the pending area:
	```
	exec DBMS_RESOURCE_MANAGER.VALIDATE_PENDING_AREA();
	```
5. Submit the pending area:
	```
	exec DBMS_RESOURCE_MANAGER.SUBMIT_PENDING_AREA();
	```

See Also:

- " About CDB Resource Plans "
- " [About Container Access in a CDB](administering-a-cdb-with-sql-plus.md) "

**Parent topic:** Modifying a CDB Resource Plan

##### Managing CDB Resource Plan Directives for a PDB

You can create, update, and delete CDB resource plan directives for a PDB.

- Creating New CDB Resource Plan Directives for a PDB  
	When you create a PDB in a CDB, you can create a CDB resource plan directive for the PDB using the `CREATE_CDB_PLAN_DIRECTIVE` procedure. The directive specifies how resources are allocated to the new PDB.
- Updating CDB Resource Plan Directives for a PDB  
	You can update the CDB resource plan directive for a PDB using the `UPDATE_CDB_PLAN_DIRECTIVE` procedure. The directive specifies how resources are allocated to the PDB.
- Deleting CDB Resource Plan Directives for a PDB  
	You can delete the CDB resource plan directive for a PDB using the `DELETE_CDB_PLAN_DIRECTIVE` procedure.

**Parent topic:** Modifying a CDB Resource Plan

###### Creating New CDB Resource Plan Directives for a PDB

When you create a PDB in a CDB, you can create a CDB resource plan directive for the PDB using the `CREATE_CDB_PLAN_DIRECTIVE` procedure. The directive specifies how resources are allocated to the new PDB.

Prerequisites

Before creating a new CDB resource plan directive for a PDB, complete the prerequisites described in " Overview of Oracle Resource Manager in a Multitenant Environment ".

To create a new CDB resource plan directive for a PDB:

1. In SQL\*Plus, ensure that the current container is the root.
2. Create a pending area:
	```
	exec DBMS_RESOURCE_MANAGER.CREATE_PENDING_AREA();
	```
3. Run the `CREATE_CDB_PLAN_DIRECTIVE` procedure, and specify the appropriate values for the new PDB.
	For example, the following procedure allocates resources to a PDB named `operpdb` in the `newcdb_plan` CDB resource plan:
	```
	BEGIN
	  DBMS_RESOURCE_MANAGER.CREATE_CDB_PLAN_DIRECTIVE(
	    plan                  => 'newcdb_plan', 
	    pluggable_database    => 'operpdb', 
	    shares                => 1, 
	    utilization_limit     => 20,
	    parallel_server_limit => 30);
	END;
	/
	```
4. Validate the pending area:
	```
	exec DBMS_RESOURCE_MANAGER.VALIDATE_PENDING_AREA();
	```
5. Submit the pending area:
	```
	exec DBMS_RESOURCE_MANAGER.SUBMIT_PENDING_AREA();
	```

See Also:

- " About CDB Resource Plans "
- " [About Container Access in a CDB](administering-a-cdb-with-sql-plus.md) "

**Parent topic:** Managing CDB Resource Plan Directives for a PDB

###### Updating CDB Resource Plan Directives for a PDB

You can update the CDB resource plan directive for a PDB using the `UPDATE_CDB_PLAN_DIRECTIVE` procedure. The directive specifies how resources are allocated to the PDB.

Prerequisites

Before updating a CDB resource plan directive for a PDB, ensure that you meet the prerequisites described in " Overview of Oracle Resource Manager in a Multitenant Environment ".

To update a CDB resource plan directive for a PDB:

1. In SQL\*Plus, ensure that the current container is the root.
2. Create a pending area:
	```
	exec DBMS_RESOURCE_MANAGER.CREATE_PENDING_AREA();
	```
3. Run the `UPDATE_CDB_PLAN_DIRECTIVE` procedure, and specify the new resource allocation values for the PDB.
	For example, the following procedure updates the resource allocation to a PDB named `operpdb` in the `newcdb_plan` CDB resource plan:
	```
	BEGIN
	  DBMS_RESOURCE_MANAGER.UPDATE_CDB_PLAN_DIRECTIVE(
	    plan                      => 'newcdb_plan', 
	    pluggable_database        => 'operpdb', 
	    new_shares                => 1, 
	    new_utilization_limit     => 10,
	    new_parallel_server_limit => 20);
	END;
	/
	```
4. Validate the pending area:
	```
	exec DBMS_RESOURCE_MANAGER.VALIDATE_PENDING_AREA();
	```
5. Submit the pending area:
	```
	exec DBMS_RESOURCE_MANAGER.SUBMIT_PENDING_AREA();
	```

See Also:

- " [About Container Access in a CDB](administering-a-cdb-with-sql-plus.md) "
- " About CDB Resource Plans "

**Parent topic:** Managing CDB Resource Plan Directives for a PDB

###### Deleting CDB Resource Plan Directives for a PDB

You can delete the CDB resource plan directive for a PDB using the `DELETE_CDB_PLAN_DIRECTIVE` procedure.

You might delete the directive for a PDB if you unplug or drop the PDB. However, you can retain the directive, and if the PDB is plugged into the CDB in the future, the existing directive applies to the PDB.

Prerequisites

Before deleting a CDB resource plan directive for a PDB, complete the prerequisites described in " Overview of Oracle Resource Manager in a Multitenant Environment ".

To delete a CDB resource plan directive for a PDB:

1. In SQL\*Plus, ensure that the current container is the root.
2. Create a pending area:
	```
	exec DBMS_RESOURCE_MANAGER.CREATE_PENDING_AREA();
	```
3. Run the `DELETE_CDB_PLAN_DIRECTIVE` procedure, and specify the CDB resource plan and the PDB.
	For example, the following procedure deletes the directive for a PDB named `operpdb` in the `newcdb_plan` CDB resource plan:
	```
	BEGIN
	  DBMS_RESOURCE_MANAGER.DELETE_CDB_PLAN_DIRECTIVE(
	    plan               => 'newcdb_plan', 
	    pluggable_database => 'operpdb');
	END;
	/
	```
4. Validate the pending area:
	```
	exec DBMS_RESOURCE_MANAGER.VALIDATE_PENDING_AREA();
	```
5. Submit the pending area:
	```
	exec DBMS_RESOURCE_MANAGER.SUBMIT_PENDING_AREA();
	```

See Also:

- " [About Container Access in a CDB](administering-a-cdb-with-sql-plus.md) "
- " About CDB Resource Plans "

**Parent topic:** Managing CDB Resource Plan Directives for a PDB

##### Managing CDB Resource Plan Directives for a PDB Performance Profile

You can create, update, and delete CDB resource plan directives for a PDB performance profile.

- Creating New CDB Resource Plan Directives for a PDB Performance Profile  
	You can create a CDB resource plan directive for the a new PDB performance profile using the `CREATE_CDB_PROFILE_DIRECTIVE` procedure. The directive specifies how resources are allocated to the all PDBs that use the new profile.
- Updating CDB Resource Plan Directives for a PDB Performance Profile  
	Update the CDB resource plan directive for a PDB performance profile using the `UPDATE_CDB_PROFILE_DIRECTIVE` procedure. The directive specifies how resources are allocated to the PDBs that use the PDB performance profile.
- Deleting CDB Resource Plan Directives for a PDB Performance Profile  
	You can delete the CDB resource plan directive for a PDB performance profile using the `DELETE_CDB_PROFILE_DIRECTIVE` procedure.

**Parent topic:** Modifying a CDB Resource Plan

###### Creating New CDB Resource Plan Directives for a PDB Performance Profile

You can create a CDB resource plan directive for the a new PDB performance profile using the `CREATE_CDB_PROFILE_DIRECTIVE` procedure. The directive specifies how resources are allocated to the all PDBs that use the new profile.

Prerequisites

Before creating a new CDB resource plan directive for a PDB performance profile, complete the prerequisites described in " Overview of Oracle Resource Manager in a Multitenant Environment ".

To create a new CDB resource plan directive for a PDB performance profile:

1. In SQL\*Plus, ensure that the current container is the root.
2. Create a pending area:
	```
	exec DBMS_RESOURCE_MANAGER.CREATE_PENDING_AREA();
	```
3. Run the `CREATE_CDB_PROFILE_DIRECTIVE` procedure, and specify the appropriate values for the new PDB performance profile.
	For example, the following procedure allocates resources to a PDB performance profile named `copper` in the `newcdb_plan` CDB resource plan:
	```
	BEGIN
	  DBMS_RESOURCE_MANAGER.CREATE_CDB_PROFILE_DIRECTIVE(
	    plan                  => 'newcdb_plan', 
	    profile               => 'copper', 
	    shares                => 1, 
	    utilization_limit     => 20,
	    parallel_server_limit => 30);
	END;
	/
	```
4. Validate the pending area:
	```
	exec DBMS_RESOURCE_MANAGER.VALIDATE_PENDING_AREA();
	```
5. Submit the pending area:
	```
	exec DBMS_RESOURCE_MANAGER.SUBMIT_PENDING_AREA();
	```

Note:

For a PDB to use the new profile, the PDB must have the `DB_PERFORMANCE_PROFILE` initialization parameter set to the profile name.

See Also:

- " About CDB Resource Plans "
- " [About Container Access in a CDB](administering-a-cdb-with-sql-plus.md) "

**Parent topic:** Managing CDB Resource Plan Directives for a PDB Performance Profile

###### Updating CDB Resource Plan Directives for a PDB Performance Profile

Update the CDB resource plan directive for a PDB performance profile using the `UPDATE_CDB_PROFILE_DIRECTIVE` procedure. The directive specifies how resources are allocated to the PDBs that use the PDB performance profile.

Before updating a CDB resource plan directive for a PDB performance profile, complete the prerequisites described in " Overview of Oracle Resource Manager in a Multitenant Environment ".

To update a CDB resource plan directive for a PDB performance profile:

1. In SQL\*Plus, ensure that the current container is the root.
2. Create a pending area:
	```
	exec DBMS_RESOURCE_MANAGER.CREATE_PENDING_AREA();
	```
3. Run the `UPDATE_CDB_PROFILE_DIRECTIVE` procedure, and specify the new resource allocation values for the PDB performance profile.
	For example, the following procedure updates the resource allocation for a PDB performance profile named `copper` in the `newcdb_plan` CDB resource plan:
	```
	BEGIN
	  DBMS_RESOURCE_MANAGER.UPDATE_CDB_PROFILE_DIRECTIVE(
	    plan                      => 'newcdb_plan', 
	    profile                   => 'copper', 
	    new_shares                => 1, 
	    new_utilization_limit     => 10,
	    new_parallel_server_limit => 20);
	END;
	/
	```
4. Validate the pending area:
	```
	exec DBMS_RESOURCE_MANAGER.VALIDATE_PENDING_AREA();
	```
5. Submit the pending area:
	```
	exec DBMS_RESOURCE_MANAGER.SUBMIT_PENDING_AREA();
	```

See Also:

- " About CDB Resource Plans "
- " [About Container Access in a CDB](administering-a-cdb-with-sql-plus.md) "

**Parent topic:** Managing CDB Resource Plan Directives for a PDB Performance Profile

###### Deleting CDB Resource Plan Directives for a PDB Performance Profile

You can delete the CDB resource plan directive for a PDB performance profile using the `DELETE_CDB_PROFILE_DIRECTIVE` procedure.

If no PDBs use a performance profile, then you might delete the directive for the profile.

Prerequisites

Before deleting a CDB resource plan directive for a PDB performance profile, complete the prerequisites described in " Overview of Oracle Resource Manager in a Multitenant Environment ".

To delete a CDB resource plan directive for a PDB performance profile:

1. In SQL\*Plus, ensure that the current container is the root.
2. Create a pending area:
	```
	exec DBMS_RESOURCE_MANAGER.CREATE_PENDING_AREA();
	```
3. Run the `DELETE_CDB_PROFILE_DIRECTIVE` procedure, and specify the CDB resource plan and the PDB performance profile.
	For example, the following procedure deletes the directive for a PDB named `operpdb` in the `newcdb_plan` CDB resource plan:
	```
	BEGIN
	  DBMS_RESOURCE_MANAGER.DELETE_CDB_PLAN_DIRECTIVE(
	    plan    => 'newcdb_plan', 
	    profile => 'operpdb');
	END;
	/
	```
4. Validate the pending area:
	```
	exec DBMS_RESOURCE_MANAGER.VALIDATE_PENDING_AREA();
	```
5. Submit the pending area:
	```
	exec DBMS_RESOURCE_MANAGER.SUBMIT_PENDING_AREA();
	```

See Also:

- " [About Container Access in a CDB](administering-a-cdb-with-sql-plus.md) ".
- " About CDB Resource Plans "

**Parent topic:** Managing CDB Resource Plan Directives for a PDB Performance Profile

##### Updating the Default Directive for PDBs in a CDB Resource Plan

You can update the default directive for PDBs in a CDB resource plan using the `UPDATE_CDB_DEFAULT_DIRECTIVE` procedure. The default directive applies to PDBs for which specific directives have not been defined.

Prerequisites

Before updating the default directive for PDBs in a CDB resource plan, complete the prerequisites described in " Overview of Oracle Resource Manager in a Multitenant Environment ".

To update the default directive for PDBs in a CDB resource plan:

1. In SQL\*Plus, ensure that the current container is the root.
2. Create a pending area:
	```
	exec DBMS_RESOURCE_MANAGER.CREATE_PENDING_AREA();
	```
3. Run the `UPDATE_CDB_DEFAULT_DIRECTIVE` procedure, and specify the appropriate default resource allocation values.
	For example, the following procedure updates the default directive for PDBs in the `newcdb_plan` CDB resource plan:
	```
	BEGIN
	  DBMS_RESOURCE_MANAGER.UPDATE_CDB_DEFAULT_DIRECTIVE(
	    plan                  => 'newcdb_plan', 
	    new_shares            => 2, 
	    new_utilization_limit => 40);
	END;
	/
	```
4. Validate the pending area:
	```
	exec DBMS_RESOURCE_MANAGER.VALIDATE_PENDING_AREA();
	```
5. Submit the pending area:
	```
	exec DBMS_RESOURCE_MANAGER.SUBMIT_PENDING_AREA();
	```

##### Updating the Default Directive for Maintenance Tasks in a CDB Resource Plan

You can update the AutoTask directive in a CDB resource plan using the `UPDATE_CDB_AUTOTASK_DIRECTIVE` procedure. The AutoTask directive applies to automatic maintenance tasks that are run in the root maintenance window.

Prerequisites

Before updating the default directive for maintenance tasks in a CDB resource plan, complete the prerequisites described in " Overview of Oracle Resource Manager in a Multitenant Environment ".

To update the AutoTask directive for maintenance tasks in a CDB resource plan:

1. In SQL\*Plus, ensure that the current container is the root.
2. Create a pending area:
	```
	exec DBMS_RESOURCE_MANAGER.CREATE_PENDING_AREA();
	```
3. Run the `UPDATE_CDB_AUTOTASK_DIRECTIVE` procedure, and specify the appropriate AutoTask resource allocation values.
	For example, the following procedure updates the AutoTask directive for maintenance tasks in the `newcdb_plan` CDB resource plan:
	```
	BEGIN
	  DBMS_RESOURCE_MANAGER.UPDATE_CDB_AUTOTASK_DIRECTIVE(
	    plan                  => 'newcdb_plan', 
	    new_shares            => 2, 
	    new_utilization_limit => 60);
	END;
	/
	```
4. Validate the pending area:
	```
	exec DBMS_RESOURCE_MANAGER.VALIDATE_PENDING_AREA();
	```
5. Submit the pending area:
	```
	exec DBMS_RESOURCE_MANAGER.SUBMIT_PENDING_AREA();
	```

See Also:

- " [About Container Access in a CDB](administering-a-cdb-with-sql-plus.md) "
- " About CDB Resource Plans "

**Parent topic:** Modifying a CDB Resource Plan

##### Deleting a CDB Resource Plan

You can delete a CDB resource plan using the `DELETE_CDB_PLAN` procedure.

The resource plan must be disabled. You might delete a CDB resource plan if the plan is no longer needed. You can enable a different CDB resource plan, or you can disable Resource Manager for the CDB.

Prerequisites

Before deleting a CDB resource plan, complete the prerequisites described in " Overview of Oracle Resource Manager in a Multitenant Environment ".

To delete a CDB resource plan:

1. In SQL\*Plus, ensure that the current container is the root.
2. Create a pending area:
	```
	exec DBMS_RESOURCE_MANAGER.CREATE_PENDING_AREA();
	```
3. Run the `DELETE_CDB_PLAN` procedure, and specify the CDB resource plan.
	For example, the following procedure deletes the `newcdb_plan` CDB resource plan:
	```
	BEGIN
	  DBMS_RESOURCE_MANAGER.DELETE_CDB_PLAN(
	    plan => 'newcdb_plan');
	END;
	/
	```
4. Validate the pending area:
	```
	exec DBMS_RESOURCE_MANAGER.VALIDATE_PENDING_AREA();
	```
5. Submit the pending area:
	```
	exec DBMS_RESOURCE_MANAGER.SUBMIT_PENDING_AREA();
	```

#### Disabling a CDB Resource Plan

Disable the Resource Manager for a CDB by unsetting the `RESOURCE_MANAGER_PLAN` initialization parameter in the CDB root.

A CDB resource plan that specifies shares or utilization limits for PDBs is required to enable CPU management, both between PDBs and within a PDB. If a resource plan with shares or utilization limits is enabled for a PDB, and if the CDB resource plan is not specified, then the CDB resource plan is set to `DEFAULT_CDB_PLAN`. This setting gives equal shares to all PDBs and specifies no utilization limits. To disable CPU resource management throughout the CDB, set `RESOURCE_MANAGER_PLAN` to `ORA$INTERNAL_CDB_PLAN`.

Prerequisites

Before disabling a CDB resource plan, complete the prerequisites described in " Overview of Oracle Resource Manager in a Multitenant Environment ".

To disable a CDB resource plan:

1. In SQL\*Plus, ensure that the current container is the root.
2. Perform one of the following actions:
	- Use an `ALTER SYSTEM` statement to unset the `RESOURCE_MANAGER_PLAN` initialization parameter for the CDB.
		The following example unsets the `RESOURCE_MANAGER_PLAN` initialization parameter using an `ALTER SYSTEM` statement:
		```
		ALTER SYSTEM SET RESOURCE_MANAGER_PLAN = '';
		```
		- In an initialization parameter file, unset the `RESOURCE_MANAGER_PLAN` initialization parameter, and restart the CDB.
		The following example unsets the `RESOURCE_MANAGER_PLAN` initialization parameter in an initialization parameter file:
		```
		RESOURCE_MANAGER_PLAN =
		```

#### Viewing Information About Plans and Directives in a CDB

You can view information about CDB resource plans, CDB resource plan directives, and predefined resource plans in a CDB.

- Viewing CDB Resource Plans  
	An example illustrates using the `DBA_CDB_RSRC_PLANS` view to display all CDB resource plans defined in the CDB.
- Viewing CDB Resource Plan Directives  
	An example illustrates using the `DBA_CDB_RSRC_PLAN_DIRECTIVES` view to display all directives defined in all CDB resource plans in the CDB.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-9CF57A7E-CCE3-4F80-9E21-29AF9B2283F0) for information about monitoring Oracle Database Resource Manager

**Parent topic:** Managing CDB Resource Plans

##### Viewing CDB Resource Plans

An example illustrates using the `DBA_CDB_RSRC_PLANS` view to display all CDB resource plans defined in the CDB.

The `DEFAULT_CDB_PLAN` is supplied with Oracle Database. You can use this default plan if it meets your requirements.

To view CDB resource plans:

1. Start SQL\*Plus or SQL Developer, and log in to the CDB root.
2. Run the following query:
	```
	COLUMN PLAN FORMAT A30
	COLUMN STATUS FORMAT A10
	COLUMN COMMENTS FORMAT A35
	 
	SELECT PLAN, STATUS, COMMENTS 
	FROM   DBA_CDB_RSRC_PLANS 
	ORDER BY PLAN;
	```
	Your output looks similar to the following:
	```
	PLAN                     STATUS      COMMENTS
	------------------------ ----------- ----------------------------
	DEFAULT_CDB_PLAN                     Default CDB plan
	DEFAULT_MAINTENANCE_PLAN             Default CDB maintenance plan
	NEWCDB_PLAN                          CDB plan for PDBs in newcdb
	ORA$INTERNAL_CDB_PLAN                Internal CDB plan
	```

Note:

Plans in the pending area have a status of `PENDING`. Plans in the pending area are being edited. Any plan that is not in the pending area has a `NULL` status.

See Also:

" About CDB Resource Plans "

**Parent topic:** Viewing Information About Plans and Directives in a CDB

##### Viewing CDB Resource Plan Directives

An example illustrates using the `DBA_CDB_RSRC_PLAN_DIRECTIVES` view to display all directives defined in all CDB resource plans in the CDB.

The `DEFAULT_CDB_PLAN` is a default CDB plan that is supplied with Oracle Database. With `DEFAULT_CDB_PLAN`, every PDB has 1 share and a utilization limit of 100. If the CDB resource plan has no CPU directives configured, that is, the `shares` and `utilization_limits` directives are unset, then CPU Resource Manager uses the PDB-level `CPU_MIN_COUNT` and `CPU_COUNT` parameters to manage CPU. Note that `ORA$DEFAULT_PDB_DIRECTIVE` is the default directive for PDBs.

To view CDB resource plan directives:

1. Start SQL\*Plus or SQL Developer, and log in to the CDB root.
2. Run the following query:
	```
	COLUMN PLAN HEADING 'Plan' FORMAT A24
	COLUMN PLUGGABLE_DATABASE HEADING 'Pluggable Database' FORMAT A25
	COLUMN SHARES HEADING 'Shares' FORMAT 999
	COLUMN UTILIZATION_LIMIT HEADING 'Utilization|Limit' FORMAT 999
	COLUMN PARALLEL_SERVER_LIMIT HEADING 'Parallel|Server|Limit' FORMAT 999
	 
	SELECT PLAN, 
	       PLUGGABLE_DATABASE, 
	       SHARES, 
	       UTILIZATION_LIMIT,
	       PARALLEL_SERVER_LIMIT
	  FROM DBA_CDB_RSRC_PLAN_DIRECTIVES
	  ORDER BY PLAN;
	```
	Your output looks similar to the following:
	```
	Parallel
	                                                          Utilization   Server
	Plan                     Pluggable Database        Shares       Limit    Limit
	------------------------ ------------------------- ------ ----------- --------
	DEFAULT_CDB_PLAN         ORA$DEFAULT_PDB_DIRECTIVE      1         100      100
	DEFAULT_CDB_PLAN         ORA$AUTOTASK                              90      100
	DEFAULT_MAINTENANCE_PLAN ORA$AUTOTASK                              90      100
	DEFAULT_MAINTENANCE_PLAN ORA$DEFAULT_PDB_DIRECTIVE      1         100      100
	NEWCDB_PLAN              HRPDB                          1          70       70
	NEWCDB_PLAN              SALESPDB                       3         100      100
	NEWCDB_PLAN              ORA$DEFAULT_PDB_DIRECTIVE      1          50       50
	NEWCDB_PLAN              ORA$AUTOTASK                   1          75       75 
	NEWCDB_PLAN              SERVICESPDB                    3         100      100
	```
	The preceding output shows the directives for the `newcdb_plan` created in " Creating a CDB Resource Plan for Managing PDBs: Scenario " and modified in " Modifying a CDB Resource Plan ".

See Also:

- " About CDB Resource Plans "
- " The Default Directive for PDBs "

**Parent topic:** Viewing Information About Plans and Directives in a CDB

### Managing PDB Resource Plans

You can create, enable, and modify resource plans for individual PDBs.

- About PDB Resource Plans  
	A PDB resource plan determines how the resources for a specific PDB are allocated to consumer groups within this PDB.
- Creating a PDB Resource Plan  
	You create a PDB resource plan in the same way that you create a resource plan for a non-CDB. You use procedures in the `DBMS_RESOURCE_MANAGER` PL/SQL package to create the plan.
- Enabling a PDB Resource Plan  
	Enable a PDB resource plan by setting the `RESOURCE_MANAGER_PLAN` initialization parameter to the plan with an `ALTER SYSTEM` statement when the current container is the PDB.
- Modifying a PDB Resource Plan  
	You can use the `DBMS_RESOURCE_MANAGER` package to modify a PDB resource plan in the same way you would modify the resource plan for a non-CDB.
- Disabling a PDB Resource Plan  
	You disable a PDB resource plan by unsetting the `RESOURCE_MANAGER_PLAN` initialization parameter in the PDB.

**Parent topic:** Using Oracle Resource Manager for PDBs

#### About PDB Resource Plans

A PDB resource plan determines how the resources for a specific PDB are allocated to consumer groups within this PDB.

A PDB resource plan is similar to a resource plan for a non-CDB. A PDB resource plan differs from a CDB resource plan, which determines the amount of resources allocated to each PDB.

The following restrictions apply to PDB resource plans:

- A PDB resource plan cannot have subplans.
- A PDB resource plan cannot have a multiple-level scheduling policy.

If you create a PDB using a non-CDB, and the non-CDB contains resource plans, then these resource plans might not conform to the preceding restrictions. In this case, Oracle Database automatically transforms these resource plans into equivalent PDB resource plans that meet these requirements. The original resource plans and directives are recorded in the `DBA_RSRC_PLANS` and `DBA_RSRC_PLAN_DIRECTIVES` views with the `LEGACY` status.

- CDB Resource Plan Requirements When Creating PDB Resource Plans  
	When you create PDB resource plans, the CDB resource plan must meet certain requirements.
- PDB Resource Plan: Example  
	A one-to-many relationship exists between CDB resource plans and PDB resource plans.

See Also:

- " About CDB Resource Plans "
- " [Options for Creating a PDB from a Non-CDB](overview-of-pdb-creation.md) "
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-4BBE0B17-3B05-49FA-979A-C649A9EE6DD9) to learn more about resource plans

**Parent topic:** Managing PDB Resource Plans

##### CDB Resource Plan Requirements When Creating PDB Resource Plans

When you create PDB resource plans, the CDB resource plan must meet certain requirements.

Create directives for a CDB resource plan by using the `DBMS_RESOURCE_MANAGER.CREATE_CDB_PLAN_DIRECTIVE` procedure. Create directives for a PDB resource plan using the `CREATE_PLAN_DIRECTIVE` procedure in the same package. When you create one or more PDB resource plans and there is no CDB resource plan, the CDB uses the `DEFAULT_CDB_PLAN` that is supplied with Oracle Database.

The following table describes the requirements for the CDB resource plan and the results when the requirements are not met. The parameter values described in the "CDB Resource Plan Requirements" column are for the `CREATE_CDB_PLAN_DIRECTIVE` procedure. The parameter values described in the "Results When Requirements Are Not Met" column are for the `CREATE_PLAN_DIRECTIVE` procedure.

Table 22-10 CDB Resource Plan Requirements for PDB Resource Plans

| Resource | CDB Resource Plan Requirements | Results When Requirements Are Not Met |
| --- | --- | --- |
| CPU | One of the following requirements must be met:  - A share value must be specified for the PDB using the `shares` parameter. - A utilization limit for CPU below 100 must be specified for the PDB using the `utilization_limit` parameter.  These values can be set in a directive for the specific PDB or in a default directive. | The CPU allocation policy of the PDB resource plan is not enforced.  The CPU limit specified by the `utilization_limit` parameter in the PDB resource plan is not enforced. |
| Parallel execution servers | One of the following requirements must be met:  - A share value must be specified for the PDB using the `shares` parameter. - A parallel server limit below 100 must be specified for the PDB using the `parallel_server_limit` parameter.  These values can be set in a directive for the specific PDB or in a default directive. | The parallel execution server allocation policy of the PDB resource plan is not enforced.  The parallel server limit specified by `parallel_server_limit` in the PDB resource plan is not enforced. However, you can set the `PARALLEL_SERVERS_TARGET` initialization parameter in a PDB to enforce the parallel limit. |

**Parent topic:** About PDB Resource Plans

##### PDB Resource Plan: Example

A one-to-many relationship exists between CDB resource plans and PDB resource plans.

The following figure shows an example of a CDB resource plan and a PDB resource plan.

Figure 22-4 A CDB Resource Plan and a PDB Resource Plan

![Figure 22-4 A CDB Resource Plan and a PDB Resource Plan](img/admin_vm_102.png)

> This illustration shows a CDB resource plan in root and a PDB resource plan in the servicespdb PDB.
>
> The CDB resource plan includes three directives, and each directive specifies a share, a utilization\_limit, and a parallel\_server\_limit for a PDB. One directive specifies the following for the salespdb PDB:
>
> - share = 3
> - utilization\_limit = 100
> - parallel\_server\_limit = 100
> - memory\_limit = 100
>
> A second directive specifies the following for the servicespdb PDB:
>
> - share = 3
> - utilization\_limit = 100
> - parallel\_server\_limit = 100
> - memory\_limit = 100
>
> A third directive specifies the following for the hrpdb PDB:
>
> - share = 1
> - utilization\_limit = 70
> - parallel\_server\_limit = 70
> - memory\_limit = 70
>
> The illustration shows the salespdb PDB, the servicespdb PDB, and the hrpdb PDB. It shows the PDB resource plan for the servicespdb PDB. This PDB resource plan includes three directives, and each directive specifies a CPU percentage for a consumer group. One directive specifies 75% of CPU for the "OLTP" consumer group, a second directive specifies 15% of CPU for the "REPORTING" consumer group, and a third directive specifies 10% of CPU for the "OTHER\_GROUPS" consumer group.


The preceding figure shows some of the directives in a PDB resource plan for the `servicespdb` PDB. Other PDBs in the CDB can also have PDB resource plans.

**Parent topic:** About PDB Resource Plans

#### Creating a PDB Resource Plan

You create a PDB resource plan in the same way that you create a resource plan for a non-CDB. You use procedures in the `DBMS_RESOURCE_MANAGER` PL/SQL package to create the plan.

A CDB resource plan allocates a portion of the system's resources to a PDB. A PDB resource plan determines how this portion is allocated within the PDB.

The following is a summary of the steps required to create a PDB resource plan:

1. In SQL\*Plus, ensure that the current container is a PDB.
2. Create a pending area using the `CREATE_PENDING_AREA` procedure.
3. Create, modify, or delete consumer groups using the `CREATE_CONSUMER_GROUP` procedure.
4. Map sessions to consumer groups using the `SET_CONSUMER_GROUP_MAPPING` procedure.
5. Create the PDB resource plan using the `CREATE_PLAN` procedure.
6. Create PDB resource plan directives using the `CREATE_PLAN_DIRECTIVE` procedure.
7. Validate the pending area using the `VALIDATE_PENDING_AREA` procedure.
8. Submit the pending area using the `SUBMIT_PENDING_AREA` procedure.

Ensure that the current container is a PDB and that the user has the required privileges when you complete these steps. See [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-4816CA07-1376-45FD-82D4-F9E332936683) for detailed information about completing these steps.

You also have the option of creating a simple resource plan that is adequate for many situations using the `CREATE_SIMPLE_PLAN` procedure. See [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-EFC4517C-6C4D-44F8-A652-2266D6FB49EB) for information about creating a simple resource plan.

Note:

Some restrictions apply to PDB resource plans. See " About PDB Resource Plans " for information.

**Parent topic:** Managing PDB Resource Plans

#### Enabling a PDB Resource Plan

Enable a PDB resource plan by setting the `RESOURCE_MANAGER_PLAN` initialization parameter to the plan with an `ALTER SYSTEM` statement when the current container is the PDB.

If no plan is specified with this parameter, then no PDB resource plan is enabled for the PDB.

Prerequisites

Before enabling a PDB resource plan, complete the prerequisites described in " Overview of Oracle Resource Manager in a Multitenant Environment ".

To enable a PDB resource plan:

1. In SQL\*Plus, ensure that the current container is a PDB.
2. Use an `ALTER SYSTEM` statement to set the `RESOURCE_MANAGER_PLAN` initialization parameter to the PDB resource plan.

You can also schedule a PDB resource plan change with Oracle Scheduler.

Example 22-5 Enabling a PDB Resource Plan

The following example sets the PDB resource plan to `salespdb_plan`.

```
ALTER SYSTEM SET RESOURCE_MANAGER_PLAN = 'salespdb_plan';
```

See Also:

- " [About Container Access in a CDB](administering-a-cdb-with-sql-plus.md) "
- " [Modifying a PDB at the System Level](administering-pdbs-with-sql-plus.md) "
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ADMIN-GUID-6B8C0335-D36B-44D3-95BC-82FA2141D967) to learn how to schedule a PDB resource plan change with Oracle Scheduler

**Parent topic:** Managing PDB Resource Plans

#### Modifying a PDB Resource Plan

You can use the `DBMS_RESOURCE_MANAGER` package to modify a PDB resource plan in the same way you would modify the resource plan for a non-CDB.

Prerequisites

Before modifying a PDB resource plan, complete the prerequisites described in " Overview of Oracle Resource Manager in a Multitenant Environment ".

To modify a PDB resource plan:

1. In SQL\*Plus, ensure that the current container is a PDB.
2. Create a pending area:
	```
	exec DBMS_RESOURCE_MANAGER.CREATE_PENDING_AREA();
	```
3. Modify the PDB resource plan by completing one or more of the following tasks:
	- Update a consumer group using the `UPDATE_CONSUMER_GROUP` procedure.
		- Delete a consumer group using the `DELETE_CONSUMER_GROUP` procedure.
		- Update a resource plan using the `UPDATE_PLAN` procedure.
		- Delete a resource plan using the `DELETE_PLAN` procedure.
		- Update a resource plan directive using the `UPDATE_PLAN_DIRECTIVE` procedure.
		- Delete a resource plan directive using the `DELETE_PLAN_DIRECTIVE` procedure.
4. Validate the pending area:
	```
	exec DBMS_RESOURCE_MANAGER.VALIDATE_PENDING_AREA();
	```
5. Submit the pending area:
	```
	exec DBMS_RESOURCE_MANAGER.SUBMIT_PENDING_AREA();
	```

#### Disabling a PDB Resource Plan

You disable a PDB resource plan by unsetting the `RESOURCE_MANAGER_PLAN` initialization parameter in the PDB.

Prerequisites

Before disabling a PDB resource plan, complete the prerequisites described in " Overview of Oracle Resource Manager in a Multitenant Environment ".

To disable a PDB resource plan:

1. In SQL\*Plus, ensure that the current container is a PDB.
2. Use an `ALTER SYSTEM` statement to unset the `RESOURCE_MANAGER_PLAN` initialization parameter for the PDB.

Example 22-6 Disabling a PDB Resource Plan

The following example disables the PDB resource plan.

```
ALTER SYSTEM SET RESOURCE_MANAGER_PLAN = '';
```

See Also:

- " [Modifying a PDB at the System Level](administering-pdbs-with-sql-plus.md) "
- See " [About Container Access in a CDB](administering-a-cdb-with-sql-plus.md) ".

**Parent topic:** Managing PDB Resource Plans

### Monitoring PDBs Managed by Oracle Database Resource Manager

A set of dynamic performance views enables you to monitor the results of your Oracle Database Resource Manager settings for PDBs.

- About Resource Manager Views for PDBs  
	You can monitor the results of your Oracle Database Resource Manager settings for PDBs using views.
- Monitoring CPU Usage for PDBs  
	The `V$RSRCPDBMETRIC` view enables you to track CPU metrics in milliseconds, in terms of number of sessions, or in terms of utilization for the past one minute.
- Monitoring Parallel Execution for PDBs  
	The `V$RSRCPDBMETRIC` view enables you to track parallel statements and parallel server use for PDBs.
- Monitoring the I/O Generated by PDBs  
	The `V$RSRCPDBMETRIC` view enables you to track the amount of I/O generated by PDBs.
- Monitoring Memory Usage for PDBs  
	The `V$RSRCPDBMETRIC` view enables you to track the amount memory used by PDBs.

**Parent topic:** Using Oracle Resource Manager for PDBs

#### About Resource Manager Views for PDBs

You can monitor the results of your Oracle Database Resource Manager settings for PDBs using views.

The following views are available:

- `V$RSRCPDBMETRIC`
	The `V$RSRCPDBMETRIC` view provides current statistics on resource consumption for PDBs, including CPU usage, parallel execution, I/O generated, and memory usage.
- `V$RSRCPDBMETRIC_HISTORY`
	The columns in the `V$RSRCPDBMETRIC_HISTORY` view are the same as the columns in the `V$RSRCPDBMETRIC` view. The only difference between these views is that the `V$RSRCPDBMETRIC` view contains metrics for the past one minute only, whereas the `V$RSRCPDBMETRIC_HISTORY` view contains metrics for the last 60 minutes.
- `V$RSRC_PDB`
	The `V$RSRC_PDB` view provides cumulative statistics. The statistics are accumulated since the time that the CDB resource plan was set.
- `DBA_HIST_RSRC_PDB_METRIC`
	This view contains the historical statistics of `V$RSRCPDBMETRIC_HISTORY`, taken using Automatic Workload Repository (AWR) snapshots.

Note:

The `V$RSRCPDBMETRIC` and `V$RSRCPDBMETRIC_HISTORY` views record statistics for resources that are not currently being managed by Resource Manager when the `STATISTICS_LEVEL` initialization parameter is set to `ALL` or `TYPICAL`.

See Also:

- [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=TGSQL789) for more information about real-time SQL monitoring
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=REFRN-GUID-35F9BE03-3DCB-46FC-8D00-4BC5BCBBC443) to learn about `V$RSRCPDBMETRIC`, `V$RSRCPDBMETRIC_HISTORY`, `V$RSRC_PDB`, and `DBA_HIST_RSRC_PDB_METRIC`

**Parent topic:** Monitoring PDBs Managed by Oracle Database Resource Manager

#### Monitoring CPU Usage for PDBs

The `V$RSRCPDBMETRIC` view enables you to track CPU metrics in milliseconds, in terms of number of sessions, or in terms of utilization for the past one minute.

The view provides real-time metrics for each PDB and is very useful in scenarios where you are running workloads and want to continuously monitor CPU resource utilization.

The active CDB resource plan manages CPU usage for a PDB. Use this view to compare the maximum and average CPU utilization for PDBs with other PDB settings such as the following:

- CPU time used
- Time waiting for CPU
- Average number of sessions that are consuming CPU
- Number of sessions that are waiting for CPU allocation

For example, you can view the amount of CPU resources a PDB used and how long it waited for resource allocation. Alternatively, you can view how many sessions from each PDB are executed against the total number of active sessions.

Tracking CPU Consumption in Terms of CPU Utilization for PDBs

To track CPU consumption in terms of CPU utilization, query the `CPU_UTILIZATION_LIMIT` and `AVG_CPU_UTILIZATION` columns. `AVG_CPU_UTILIZATION` lists the average percentage of the server's CPU that is consumed by a PDB. `CPU_UTILIZATION_LIMIT` represents the maximum percentage of the server's CPU that a PDB can use. This limit is set using the `UTILIZATION_LIMIT` directive attribute.

The following query displays this information by showing the container ID (`CON_ID`) and name of each PDB:

```
COLUMN PDB_NAME FORMAT A10

SELECT r.CON_ID, 
       p.PDB_NAME, 
       r.CPU_UTILIZATION_LIMIT, 
       r.AVG_CPU_UTILIZATION 
FROM   V$RSRCPDBMETRIC r, 
       CDB_PDBS p
WHERE r.CON_ID = p.CON_ID;
```

Tracking CPU Consumption and Throttling for PDBs

Use the `CPU_CONSUMED_TIME` and `CPU_TIME_WAIT` columns to track CPU consumption and throttling in milliseconds for each PDB. The column `NUM_CPUS` represents the number of CPUs that Resource Manager is managing.

The following query displays this information by showing the container ID (`CON_ID`) and name of each PDB:

```
COLUMN PDB_NAME FORMAT A10

SELECT r.CON_ID, 
       p.PDB_NAME, 
       r.CPU_CONSUMED_TIME, 
       r.CPU_WAIT_TIME, 
       r.NUM_CPUS 
FROM   V$RSRCPDBMETRIC r, 
       CDB_PDBS p
WHERE r.CON_ID = p.CON_ID;
```

Tracking CPU Consumption and Throttling in Terms of Number of Sessions for PDBs

To track the CPU consumption and throttling in terms of number of sessions, use the `RUNNING_SESSIONS_LIMIT`, `AVG_RUNNING_SESSIONS`, and `AVG_WAITING_SESSIONS` columns. `RUNNING_SESSIONS_LIMIT` lists the maximum number of sessions from a particular PDB that can be running at any time. This limit is defined by the `UTILIZATION_LIMIT` directive attribute that you set for the PDB. `AVG_RUNNING_SESSIONS` lists the average number of sessions that are consuming CPU, and `AVG_WAITING_SESSIONS` lists the average number of sessions that are waiting for CPU.

The following query displays this information by showing the container ID (`CON_ID`) and name of each PDB:

```
COLUMN PDB_NAME FORMAT A10

SELECT r.CON_ID, 
       p.PDB_NAME, 
       r.RUNNING_SESSIONS_LIMIT, 
       r.AVG_RUNNING_SESSIONS, 
       r.AVG_WAITING_SESSIONS 
FROM   V$RSRCPDBMETRIC r, 
       CDB_PDBS p
WHERE r.CON_ID = p.CON_ID;
```

**Parent topic:** Monitoring PDBs Managed by Oracle Database Resource Manager

#### Monitoring Parallel Execution for PDBs

The `V$RSRCPDBMETRIC` view enables you to track parallel statements and parallel server use for PDBs.

Parallel execution servers for a PDB are managed with the active CDB resource plan of the PDB's CDB. To track parallel statements and parallel server use for PDBs, use the `AVG_ACTIVE_PARALLEL_STMTS`, `AVG_QUEUED_PARALLEL_STMTS`, `AVG_ACTIVE_PARALLEL_SERVERS`, `AVG_QUEUED_PARALLEL_SERVERS`, and `PARALLEL_SERVERS_LIMIT` columns.

`AVG_ACTIVE_PARALLEL_STMTS` and `AVG_ACTIVE_PARALLEL_SERVERS` list the average number of parallel statements running and the average number of parallel servers used by the parallel statements. `AVG_QUEUED_PARALLEL_STMTS` and `AVG_QUEUED_PARALLEL_SERVERS` list the average number of parallel statements queued and average number of parallel servers that were requested by queued parallel statements. `PARALLEL_SERVERS_LIMIT` lists the number of parallel servers allowed to be used by the PDB.

The following query displays this information by showing the container ID (`CON_ID`) and name of each PDB:

```
COLUMN PDB_NAME FORMAT A10

SELECT r.CON_ID, p.PDB_NAME, r.AVG_ACTIVE_PARALLEL_STMTS, r.AVG_QUEUED_PARALLEL_STMTS, 
   r.AVG_ACTIVE_PARALLEL_SERVERS, r.AVG_QUEUED_PARALLEL_SERVERS, r.PARALLEL_SERVERS_LIMIT
   FROM V$RSRCPDBMETRIC r, CDB_PDBS p
   WHERE r.CON_ID = p.CON_ID;
```

**Parent topic:** Monitoring PDBs Managed by Oracle Database Resource Manager

#### Monitoring the I/O Generated by PDBs

The `V$RSRCPDBMETRIC` view enables you to track the amount of I/O generated by PDBs.

I/O is limited for a PDB by setting the `MAX_IOPS` initialization parameter or the `MAX_MBPS` initialization parameter in the PDB. Use this view to compare the I/O generated by PDBs in terms of the number of operations each second and the number of megabytes each second.

Tracking the Number of I/O Operations Generated Each Second by PDBs

To track the I/O operations generated each second by PDBs during the previous minute, use the `IOPS` column.

The following query displays this information by showing the container ID (`CON_ID`) and name of each PDB:

```
COLUMN PDB_NAME FORMAT A10

SELECT r.CON_ID, p.PDB_NAME, r.IOPS 
   FROM V$RSRCPDBMETRIC r, CDB_PDBS p
   WHERE r.CON_ID = p.CON_ID;
```

Tracking the Number Megabytes Generated for I/O Operations Each Second by PDBs

To track number of megabytes generated for I/O operations each second by PDBs during the previous minute, use the `IOMBPS` column.

The following query displays this information by showing the container ID (`CON_ID`) and name of each PDB:

```
COLUMN PDB_NAME FORMAT A10

SELECT r.CON_ID, p.PDB_NAME, r.IOMBPS 
   FROM V$RSRCPDBMETRIC r, CDB_PDBS p
   WHERE r.CON_ID = p.CON_ID;
```

**Parent topic:** Monitoring PDBs Managed by Oracle Database Resource Manager

#### Monitoring Memory Usage for PDBs

The `V$RSRCPDBMETRIC` view enables you to track the amount memory used by PDBs.

Use this view to track the amount of SGA, PGA, buffer cache, and shared pool memory currently used by PDBs.

To track the current memory usage, in bytes, for specific PDBs, use the `SGA_BYTES`, `PGA_BYTES`, `BUFFER_CACHE_BYTES`, and `SHARED_POOL_BYTES` columns.

The following query displays this information by showing the container ID (`CON_ID`) and name of each PDB:

```
COLUMN PDB_NAME FORMAT A10

SELECT r.CON_ID, p.PDB_NAME, r.SGA_BYTES, r.PGA_BYTES, r.BUFFER_CACHE_BYTES, r.SHARED_POOL_BYTES
   FROM V$RSRCPDBMETRIC r, CDB_PDBS p
   WHERE r.CON_ID = p.CON_ID;
```

**Parent topic:** Monitoring PDBs Managed by Oracle Database Resource Manager