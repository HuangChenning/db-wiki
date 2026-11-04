---
title: "Database Administrator’s Guide"
book: "Database Administrator's Guide"
doc_id: F31835-17
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/admin/managing-automated-database-maintenance-tasks.html
tags:
  - oracle
  - 21c
  - administrators-guide
---

## 25 Managing Automated Database Maintenance Tasks

Oracle Database has automated several common maintenance tasks typically performed by database administrators. These automated maintenance tasks are performed when the system load is expected to be light. You can enable and disable individual maintenance tasks, and can configure when these tasks run and what resource allocations they are allotted.

Note:

This chapter explains how to administer automated maintenance tasks using PL/SQL packages. An easier way is to use the graphical interface of Oracle Enterprise Manager Cloud Control (Cloud Control).

To manage automatic maintenance tasks with Cloud Control:

1. Access the Database Home Page.
2. From the Administration menu, select Oracle Scheduler, then Automated Maintenance Tasks.
3. On the Automated Maintenance Tasks page, click Configure.

- About Automated Maintenance Tasks  
	Automated maintenance tasks are tasks that are started automatically at regular intervals to perform maintenance operations on the database. An example is a task that gathers statistics on schema objects for the query optimizer.
- About Maintenance Windows  
	A maintenance window is a contiguous time interval during which automated maintenance tasks are run. Maintenance windows are Oracle Scheduler windows that belong to the window group named `MAINTENANCE_WINDOW_GROUP`.
- Configuring Automated Maintenance Tasks  
	To enable or disable specific maintenance tasks in any subset of maintenance windows, you can use the `DBMS_AUTO_TASK_ADMIN` PL/SQL package.
- Configuring Maintenance Windows  
	You may want to adjust the predefined maintenance windows to a time suitable to your database environment or create a new maintenance window. You can customize maintenance windows using the `DBMS_SCHEDULER` PL/SQL package.
- Configuring Resource Allocations for Automated Maintenance Tasks  
	You can reduce or increase resource allocation to the automated maintenance tasks.
- Automated Maintenance Tasks Reference  
	Oracle Database has predefined maintenance windows. It also has data dictionary views that you can query for information about automated maintenance.

**Parent topic:** [Database Resource Management and Task Scheduling](database-resource-management-and-task-scheduling.md)

### 25.1 About Automated Maintenance Tasks

Automated maintenance tasks are tasks that are started automatically at regular intervals to perform maintenance operations on the database. An example is a task that gathers statistics on schema objects for the query optimizer.

Automated maintenance tasks run in maintenance windows, which are predefined time intervals that are intended to occur during a period of low system load. You can customize maintenance windows based on the resource usage patterns of your database, or disable certain default windows from running. You can also create your own maintenance windows.

Oracle Database has these predefined automated maintenance tasks:

- Automatic Optimizer Statistics Collection—Collects optimizer statistics for all schema objects in the database for which there are no statistics or only stale statistics. The statistics gathered by this task are used by the SQL query optimizer to improve the performance of SQL execution.
	See Also:
	[Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/admin&id=TGSQL389) for more information on automatic statistics collection
- Optimizer Statistics Advisor—Analyzes how statistics are being gathered and suggests changes that can be made to fine tune statistics collection.
	See Also:
	[Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/admin&id=TGSQL-GUID-054F4B76-DD57-46EE-98EA-0FF04F49D1B3)
- Automatic Segment Advisor— Identifies segments that have space available for reclamation, and makes recommendations on how to defragment those segments.
	You can also run the Segment Advisor manually to obtain more up-to-the-minute recommendations or to obtain recommendations on segments that the Automatic Segment Advisor did not examine for possible space reclamation.
	See Also:
	" [Using the Segment Advisor](managing-space-for-schema-objects.md) " for more information.
- Automatic SQL Tuning Advisor—Examines the performance of high-load SQL statements, and makes recommendations on how to tune those statements. You can configure this advisor to automatically implement SQL profile recommendations.
	See Also:
	[Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/admin&id=TGSQL540) for more information on SQL Tuning Advisor
- SQL Plan Management (SPM) Evolve Advisor—Evolves plans that have recently been added to the SQL plan baseline. The advisor simplifies plan evolution by eliminating the requirement to do it manually.
	See Also:
	[Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/admin&id=TGSQL94648) for more information on SPM Evolve Advisor

By default, all of these automated maintenance tasks are configured to run in all maintenance windows.

**Parent topic:** Managing Automated Database Maintenance Tasks

### 25.2 About Maintenance Windows

A maintenance window is a contiguous time interval during which automated maintenance tasks are run. Maintenance windows are Oracle Scheduler windows that belong to the window group named `MAINTENANCE_WINDOW_GROUP`.

A Scheduler window can be a simple repeating interval (such as "between midnight and 6 a.m., every Saturday"), or a more complex interval (such as "between midnight and 6 a.m., on the last workday of every month, excluding company holidays").

When a maintenance window opens, Oracle Database creates an Oracle Scheduler job for each maintenance task that is scheduled to run in that window. Each job is assigned a job name that is generated at run time. All automated maintenance task job names begin with `ORA$AT`. For example, the job for the Automatic Segment Advisor might be called `ORA$AT_SA_SPC_SY_26`. When an automated maintenance task job finishes, it is deleted from the Oracle Scheduler job system. However, the job can still be found in the Scheduler job history.

Note:

To view job history, you must log in as the `SYS` user.

In the case of a very long maintenance window, all automated maintenance tasks except Automatic SQL Tuning Advisor are restarted every four hours. This feature ensures that maintenance tasks are run regularly, regardless of window size.

The framework of automated maintenance tasks relies on maintenance windows being defined in the database. Table 25-1 lists the maintenance windows that are automatically defined with each new Oracle Database installation.

See Also:

- " [About Jobs and Supporting Scheduler Objects](oracle-scheduler-concepts.md) " for more information on windows and groups.

**Parent topic:** Managing Automated Database Maintenance Tasks

### 25.3 Configuring Automated Maintenance Tasks

To enable or disable specific maintenance tasks in any subset of maintenance windows, you can use the `DBMS_AUTO_TASK_ADMIN` PL/SQL package.

- Enabling and Disabling Maintenance Tasks for all Maintenance Windows  
	With a single operation, you can disable or enable a particular automated maintenance task for all maintenance windows.
- Enabling and Disabling Maintenance Tasks for Specific Maintenance Windows  
	By default, all maintenance tasks run in all predefined maintenance windows. You can disable a maintenance task for a specific window.

**Parent topic:** Managing Automated Database Maintenance Tasks

#### 25.3.1 Enabling and Disabling Maintenance Tasks for all Maintenance Windows

With a single operation, you can disable or enable a particular automated maintenance task for all maintenance windows.

You can disable a particular automated maintenance task for all maintenance windows with a single operation. You do so by calling the `DISABLE` procedure of the `DBMS_AUTO_TASK_ADMIN` PL/SQL package without supplying the `window_name` argument. For example, you can completely disable the Automatic SQL Tuning Advisor task as follows:

```
BEGIN
  dbms_auto_task_admin.disable(
    client_name => 'sql tuning advisor',
    operation   => NULL,
    window_name => NULL);
END;
/
```

To enable this maintenance task again, use the `ENABLE` procedure, as follows:

```
BEGIN
  dbms_auto_task_admin.enable(
    client_name => 'sql tuning advisor',
    operation   => NULL,
    window_name => NULL);
END;
/
```

The task names to use for the `client_name` argument are listed in the `DBA_AUTOTASK_CLIENT` database dictionary view.

To enable or disable all automated maintenance tasks for all windows, call the `ENABLE` or `DISABLE` procedure with no arguments.

```
EXECUTE DBMS_AUTO_TASK_ADMIN.DISABLE;
```

See Also:

- " Automated Maintenance Tasks Database Dictionary Views "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/admin&id=ARPLS032) for more information on the `DBMS_AUTO_TASK_ADMIN` PL/SQL package.

**Parent topic:** Configuring Automated Maintenance Tasks

#### 25.3.2 Enabling and Disabling Maintenance Tasks for Specific Maintenance Windows

By default, all maintenance tasks run in all predefined maintenance windows. You can disable a maintenance task for a specific window.

The following example disables the Automatic SQL Tuning Advisor from running in the window `MONDAY_WINDOW`:

```
BEGIN
  dbms_auto_task_admin.disable(
    client_name => 'sql tuning advisor', 
    operation   => NULL, 
    window_name => 'MONDAY_WINDOW');
END;
/
```

**Parent topic:** Configuring Automated Maintenance Tasks

### 25.4 Configuring Maintenance Windows

You may want to adjust the predefined maintenance windows to a time suitable to your database environment or create a new maintenance window. You can customize maintenance windows using the `DBMS_SCHEDULER` PL/SQL package.

- Modifying a Maintenance Window  
	The `DBMS_SCHEDULER` PL/SQL package includes a `SET_ATTRIBUTE` procedure for modifying the attributes of a window.
- Creating a New Maintenance Window  
	To create a new maintenance window, you must create an Oracle Scheduler window object and then add it to the window group `MAINTENANCE_WINDOW_GROUP`.
- Removing a Maintenance Window  
	To remove an existing maintenance window, remove it from the `MAINTENANCE_WINDOW_GROUP` window group.

**Parent topic:** Managing Automated Database Maintenance Tasks

#### 25.4.1 Modifying a Maintenance Window

The `DBMS_SCHEDULER` PL/SQL package includes a `SET_ATTRIBUTE` procedure for modifying the attributes of a window.

For example, the following script changes the duration of the maintenance window `SATURDAY_WINDOW` to 4 hours:

```
BEGIN
  dbms_scheduler.disable(
    name  => 'SATURDAY_WINDOW');
  dbms_scheduler.set_attribute(
    name      => 'SATURDAY_WINDOW',
    attribute => 'DURATION',
    value     => numtodsinterval(4, 'hour'));
  dbms_scheduler.enable(
    name => 'SATURDAY_WINDOW');
END;
/
```

Note that you must use the `DBMS_SCHEDULER.DISABLE` subprogram to disable the window before making changes to it, and then re-enable the window with `DBMS_SCHEDULER.ENABLE` when you are finished. If you change a window when it is currently open, the change does not take effect until the next time the window opens.

See Also:

" [Managing Job Scheduling and Job Priorities with Windows](scheduling-jobs-with-oracle-scheduler.md) " for more information about modifying windows.

**Parent topic:** Configuring Maintenance Windows

#### 25.4.2 Creating a New Maintenance Window

To create a new maintenance window, you must create an Oracle Scheduler window object and then add it to the window group `MAINTENANCE_WINDOW_GROUP`.

You use the `DBMS_SCHEDULER`.`CREATE_WINDOW` package procedure to create the window, and the `DBMS_SCHEDULER`.`ADD_GROUP_MEMBER` procedure to add the new window to the window group.

The following example creates a maintenance window named `EARLY_MORNING_WINDOW`. This window runs for one hour daily between 5 a.m. and 6 a.m.

```
BEGIN
  DBMS_SCHEDULER.CREATE_WINDOW(
    window_name     => 'EARLY_MORNING_WINDOW',
    duration        =>  NUMTODSINTERVAL(1, 'hour'),
    resource_plan   => 'DEFAULT_MAINTENANCE_PLAN',
    repeat_interval => 'FREQ=DAILY;BYHOUR=5;BYMINUTE=0;BYSECOND=0');
  DBMS_SCHEDULER.ADD_GROUP_MEMBER(
    group_name  => 'MAINTENANCE_WINDOW_GROUP',
    member      => 'EARLY_MORNING_WINDOW');
END;
/
```

See Also:

- " [Creating Windows](scheduling-jobs-with-oracle-scheduler.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/admin&id=ARPLS72235) for information on the `DBMS_SCHEDULER` package

**Parent topic:** Configuring Maintenance Windows

#### 25.4.3 Removing a Maintenance Window

To remove an existing maintenance window, remove it from the `MAINTENANCE_WINDOW_GROUP` window group.

The window continues to exist but no longer runs automated maintenance tasks. Any other Oracle Scheduler jobs assigned to this window continue to run as usual.

The following example removes `EARLY_MORNING_WINDOW` from the window group:

```
BEGIN
  DBMS_SCHEDULER.REMOVE_GROUP_MEMBER(
    group_name  => 'MAINTENANCE_WINDOW_GROUP',
    member      => 'EARLY_MORNING_WINDOW');
END;
/
```

### 25.5 Configuring Resource Allocations for Automated Maintenance Tasks

You can reduce or increase resource allocation to the automated maintenance tasks.

- About Resource Allocations for Automated Maintenance Tasks  
	By default, all predefined maintenance windows use the resource plan `DEFAULT_MAINTENANCE_PLAN`. Automated maintenance tasks run under its subplan `ORA$AUTOTASK`. This subplan divides its portion of total resource allocation equally among the maintenance tasks.
- Changing Resource Allocations for Automated Maintenance Tasks  
	To change the resource allocation for automated maintenance tasks within a maintenance window, you must change the percentage of resources allocated to the subplan `ORA$AUTOTASK` in the resource plan for that window.

See Also:

[Managing Resources with Oracle Database Resource Manager](managing-resources-with-oracle-database-resource-manager.md)

**Parent topic:** Managing Automated Database Maintenance Tasks

#### 25.5.1 About Resource Allocations for Automated Maintenance Tasks

By default, all predefined maintenance windows use the resource plan `DEFAULT_MAINTENANCE_PLAN`. Automated maintenance tasks run under its subplan `ORA$AUTOTASK`. This subplan divides its portion of total resource allocation equally among the maintenance tasks.

`DEFAULT_MAINTENANCE_PLAN` defines the following resource allocations:

| Consumer Group/subplan | Level 1 | Maximum Utilization Limit |
| --- | --- | --- |
| `ORA$AUTOTASK` | 5% | 90 |
| `OTHER_GROUPS` | 20% | \- |
| `SYS_GROUP` | 75% | \- |

In this plan, any sessions in the `SYS_GROUP` consumer group get priority. (Sessions in this group are sessions created by user accounts `SYS` and `SYSTEM`.) Any resource allocation that is unused by sessions in `SYS_GROUP` is then shared by sessions belonging to the other consumer groups and subplans in the plan. Of that allocation, 5% goes to maintenance tasks and 20% goes to user sessions. The maximum utilization limit for `ORA$AUTOTASK` is 90. Therefore, even if the CPU is idle, this group/plan cannot be allocated more than 90% of the CPU resources.

To reduce or increase resource allocation to the automated maintenance tasks, you make adjustments to `DEFAULT_MAINTENANCE_PLAN`. See " Changing Resource Allocations for Automated Maintenance Tasks " for more information.

Note that as with any resource plan, the portion of an allocation that is not used by a consumer group or subplan is available for other consumer groups or subplans. Note also that the Database Resource Manager does not begin to limit resource allocations according to resource plans until 100% of CPU is being used.

Note:

Although `DEFAULT_MAINTENANCE_PLAN` is the default, you can assign any resource plan to any maintenance window. If you do change a maintenance window resource plan, ensure that you include the subplan `ORA$AUTOTASK` in the new plan.

See Also:

[Managing Resources with Oracle Database Resource Manager](managing-resources-with-oracle-database-resource-manager.md) for more information on resource plans.

**Parent topic:** Configuring Resource Allocations for Automated Maintenance Tasks

#### 25.5.2 Changing Resource Allocations for Automated Maintenance Tasks

To change the resource allocation for automated maintenance tasks within a maintenance window, you must change the percentage of resources allocated to the subplan `ORA$AUTOTASK` in the resource plan for that window.

(By default, the resource plan for each predefined maintenance window is `DEFAULT_MAINTENANCE_PLAN`.) You must also adjust the resource allocation for one or more other subplans or consumer groups in the window's resource plan such that the resource allocation at the top level of the plan adds up to 100%. For information on changing resource allocations, see [Managing Resources with Oracle Database Resource Manager](managing-resources-with-oracle-database-resource-manager.md).

**Parent topic:** Configuring Resource Allocations for Automated Maintenance Tasks

### 25.6 Automated Maintenance Tasks Reference

Oracle Database has predefined maintenance windows. It also has data dictionary views that you can query for information about automated maintenance.

- Predefined Maintenance Windows  
	By default there are seven predefined maintenance windows, each one representing a day of the week.
- Automated Maintenance Tasks Database Dictionary Views  
	You can query a set of data dictionary views for information about automated maintenance tasks.

**Parent topic:** Managing Automated Database Maintenance Tasks

#### 25.6.1 Predefined Maintenance Windows

By default there are seven predefined maintenance windows, each one representing a day of the week.

The weekend maintenance windows, `SATURDAY_WINDOW` and `SUNDAY_WINDOW`, are longer in duration than the weekday maintenance windows. The window group `MAINTENANCE_WINDOW_GROUP` consists of these seven windows. The list of predefined maintenance windows is given in Table 25-1.

Table 25-1 Predefined Maintenance Windows

| Window Name | Description |
| --- | --- |
| `MONDAY_WINDOW` | Starts at 10 p.m. on Monday and ends at 2 a.m. |
| `TUESDAY_WINDOW` | Starts at 10 p.m. on Tuesday and ends at 2 a.m. |
| `WEDNESDAY_WINDOW` | Starts at 10 p.m. on Wednesday and ends at 2 a.m. |
| `THURSDAY_WINDOW` | Starts at 10 p.m. on Thursday and ends at 2 a.m. |
| `FRIDAY_WINDOW` | Starts at 10 p.m. on Friday and ends at 2 a.m. |
| `SATURDAY_WINDOW` | Starts at 6 a.m. on Saturday and is 20 hours long. |
| `SUNDAY_WINDOW` | Starts at 6 a.m. on Sunday and is 20 hours long. |

**Parent topic:** Automated Maintenance Tasks Reference

#### 25.6.2 Automated Maintenance Tasks Database Dictionary Views

You can query a set of data dictionary views for information about automated maintenance tasks.

Table 25-2 displays information about database dictionary views for automated maintenance tasks:

Table 25-2 Automated Maintenance Tasks Database Dictionary Views

| View Name | Description |
| --- | --- |
| `DBA_AUTOTASK_CLIENT_JOB` | Contains information about currently running Scheduler jobs created for automated maintenance tasks. It provides information about some objects targeted by those jobs, as well as some additional statistics from previous instantiations of the same task. Some of this additional data is taken from generic Scheduler views. |
| `DBA_AUTOTASK_CLIENT` | Provides statistical data for each automated maintenance task over 7-day and 30-day periods. |
| `DBA_AUTOTASK_JOB_HISTORY` | Lists the history of automated maintenance task job runs. Jobs are added to this view after they finish executing. |
| `DBA_AUTOTASK_WINDOW_CLIENTS` | Lists the windows that belong to `MAINTENANCE_WINDOW_GROUP`, along with the Enabled or Disabled status for the window for each maintenance task. Primarily used by Cloud Control. |
| `DBA_AUTOTASK_CLIENT_HISTORY` | Provides per-window history of job execution counts for each automated maintenance task. This information is viewable in the Job History page of Cloud Control. |

See Also:

" [Resource Manager Data Dictionary Views](managing-resources-with-oracle-database-resource-manager.md) " for column descriptions for views.

**Parent topic:** Automated Maintenance Tasks Reference