---
title: Managing Automated Database Maintenance Tasks
book: "Administrator's Guide"
doc_id: E25494-07
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e25494/tasks.htm
tags:
  - oracle
  - 11g
  - administrators-guide
---

## 26 Managing Automated Database Maintenance Tasks

Oracle Database has automated several common maintenance tasks typically performed by database administrators. These automated maintenance tasks are performed when the system load is expected to be light. You can enable and disable individual maintenance tasks, and can configure when these tasks run and what resource allocations they are allotted.

In this chapter:

Note:

This chapter explains how to administer automated maintenance tasks using PL/SQL packages. An easier way is to use the graphical interface of Enterprise Manager.

To manage automatic maintenance tasks with Enterprise Manager:

1. Access the Database Home Page.
	See [Oracle Database 2 Day DBA](https://docs.oracle.com/cd/E11882_01/server.112/e10897/em_manage.htm#ADMQS033) or the Oracle Enterprise Manager Grid Control online help for instructions.
2. On the Database Home Page, click Server to display the Server page.
3. Under the Oracle Scheduler section, click Automated Maintenance Tasks to configure maintenance tasks, or Windows to configure maintenance windows.

## About Automated Maintenance Tasks

Automated maintenance tasks are tasks that are started automatically at regular intervals to perform maintenance operations on the database. An example is a task that gathers statistics on schema objects for the query optimizer. Automated maintenance tasks run in maintenance windows, which are predefined time intervals that are intended to occur during a period of low system load. You can customize maintenance windows based on the resource usage patterns of your database, or disable certain default windows from running. You can also create your own maintenance windows.

Oracle Database has three predefined automated maintenance tasks:

- Automatic Optimizer Statistics Collection—Collects optimizer statistics for all schema objects in the database for which there are no statistics or only stale statistics. The statistics gathered by this task are used by the SQL query optimizer to improve the performance of SQL execution.
	See Also:
	[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/autostat.htm#PFGRF027) for more information on automatic statistics collection
- Automatic Segment Advisor—Identifies segments that have space available for reclamation, and makes recommendations on how to defragment those segments.
	You can also run the Segment Advisor manually to obtain more up-to-the-minute recommendations or to obtain recommendations on segments that the Automatic Segment Advisor did not examine for possible space reclamation.
	See Also:
	["Using the Segment Advisor"](schema.md) for more information.
- Automatic SQL Tuning Advisor—Examines the performance of high-load SQL statements, and makes recommendations on how to tune those statements. You can configure this advisor to automatically implement SQL profile recommendations.
	See Also:
	[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/sql_tune.htm#PFGRF028) for more information on SQL Tuning Advisor

By default, all three automated maintenance tasks are configured to run in all maintenance windows.

## About Maintenance Windows

A maintenance window is a contiguous time interval during which automated maintenance tasks are run. Maintenance windows are Oracle Scheduler windows that belong to the window group named `MAINTENANCE_WINDOW_GROUP`. A Scheduler window can be a simple repeating interval (such as "between midnight and 6 a.m., every Saturday"), or a more complex interval (such as "between midnight and 6 a.m., on the last workday of every month, excluding company holidays").

When a maintenance window opens, Oracle Database creates an Oracle Scheduler job for each maintenance task that is scheduled to run in that window. Each job is assigned a job name that is generated at run time. All automated maintenance task job names begin with `ORA$AT`. For example, the job for the Automatic Segment Advisor might be called `ORA$AT_SA_SPC_SY_26`. When an automated maintenance task job finishes, it is deleted from the Oracle Scheduler job system. However, the job can still be found in the Scheduler job history.

Note:

To view job history, you must log in as the `SYS` user.

In the case of a very long maintenance window, all automated maintenance tasks except Automatic SQL Tuning Advisor are restarted every four hours. This feature ensures that maintenance tasks are run regularly, regardless of window size.

The framework of automated maintenance tasks relies on maintenance windows being defined in the database. Table 26-1 lists the maintenance windows that are automatically defined with each new Oracle Database installation.

See Also:

- ["About Jobs and Supporting Scheduler Objects"](schedover.md) for more information on windows and groups.

## Configuring Automated Maintenance Tasks

To enable or disable specific maintenance tasks in any subset of maintenance windows, you can use the `DBMS_AUTO_TASK_ADMIN` PL/SQL package.

This section contains the following topics:

- Enabling and Disabling Maintenance Tasks for all Maintenance Windows
- Enabling and Disabling Maintenance Tasks for Specific Maintenance Windows

### Enabling and Disabling Maintenance Tasks for all Maintenance Windows

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

- "Automated Maintenance Tasks Database Dictionary Views"
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_autotaskadm.htm#ARPLS032) for more information on the `DBMS_AUTO_TASK_ADMIN` PL/SQL package.

### Enabling and Disabling Maintenance Tasks for Specific Maintenance Windows

By default, all maintenance tasks run in all predefined maintenance windows. You can disable a maintenance task for a specific window. The following example disables the Automatic SQL Tuning Advisor from running in the window `MONDAY_WINDOW`:

```
BEGIN
  dbms_auto_task_admin.disable(
    client_name => 'sql tuning advisor', 
    operation   => NULL, 
    window_name => 'MONDAY_WINDOW');
END;
/
```

## Configuring Maintenance Windows

You may want to adjust the predefined maintenance windows to a time suitable to your database environment or create a new maintenance window. You can customize maintenance windows using the `DBMS_SCHEDULER` PL/SQL package.

This section contains the following topics:

- Modifying a Maintenance Window
- Creating a New Maintenance Window
- Removing a Maintenance Window

### Modifying a Maintenance Window

The `DBMS_SCHEDULER` PL/SQL package includes a `SET_ATTRIBUTE` procedure for modifying the attributes of a window. For example, the following script changes the duration of the maintenance window `SATURDAY_WINDOW` to 4 hours:

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

["Managing Job Scheduling and Job Priorities with Windows"](scheduse.md) for more information about modifying windows.

### Creating a New Maintenance Window

To create a new maintenance window, you must create an Oracle Scheduler window object and then add it to the window group `MAINTENANCE_WINDOW_GROUP`. You use the `DBMS_SCHEDULER`.`CREATE_WINDOW` package procedure to create the window, and the `DBMS_SCHEDULER`.`ADD_GROUP_MEMBER` procedure to add the new window to the window group.

The following example creates a maintenance window named `EARLY_MORNING_WINDOW`. This window runs for one hour daily between 5 a.m. and 6 a.m.

```
BEGIN
  dbms_scheduler.create_window(
    window_name     => 'EARLY_MORNING_WINDOW',
    duration        =>  numtodsinterval(1, 'hour'),
    resource_plan   => 'DEFAULT_MAINTENANCE_PLAN',
    repeat_interval => 'FREQ=DAILY;BYHOUR=5;BYMINUTE=0;BYSECOND=0');
  dbms_scheduler.add_group_member(
    group_name  => 'MAINTENANCE_WINDOW_GROUP',
    member      => 'EARLY_MORNING_WINDOW');
END;
/
```

See Also:

- ["Creating Windows"](scheduse.md)
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_sched.htm#ARPLS72235) for information on the `DBMS_SCHEDULER` package

### Removing a Maintenance Window

To remove an existing maintenance window, remove it from the `MAINTENANCE_WINDOW_GROUP` window group. The window continues to exist but no longer runs automated maintenance tasks. Any other Oracle Scheduler jobs assigned to this window continue to run as usual.

The following example removes `EARLY_MORNING_WINDOW` from the window group:

```
BEGIN
  DBMS_SCHEDULER.REMOVE_GROUP_MEMBER(
    group_name  => 'MAINTENANCE_WINDOW_GROUP',
    member      => 'EARLY_MORNING_WINDOW');
END;
/
```

See Also:

- ["Removing a Member from a Window Group"](scheduse.md)
- ["Dropping Windows"](scheduse.md)
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_sched.htm#ARPLS72235) for information on the `DBMS_SCHEDULER` package

## Configuring Resource Allocations for Automated Maintenance Tasks

This section contains the following topics on resource allocation for maintenance windows:

- About Resource Allocations for Automated Maintenance Tasks
- Changing Resource Allocations for Automated Maintenance Tasks

See Also:

[Chapter 27, "Managing Resources with Oracle Database Resource Manager"](dbrm.md)

### About Resource Allocations for Automated Maintenance Tasks

By default, all predefined maintenance windows use the resource plan `DEFAULT_MAINTENANCE_PLAN`. Automated maintenance tasks run under its subplan `ORA$AUTOTASK_SUB_PLAN`. This subplan divides its portion of total resource allocation equally among the maintenance tasks.

`DEFAULT_MAINTENANCE_PLAN` defines the following resource allocations:

| Consumer Group/subplan | Level 1 | Level 2 | Maximum Utilization Limit |
| --- | --- | --- | --- |
| `ORA$AUTOTASK_SUB_PLAN` | \- | 25% | 90 |
| `ORA$DIAGNOSTICS` | \- | 5% | 90 |
| `OTHER_GROUPS` | \- | 70% |  |
| `SYS_GROUP` | 75% | \- |  |

In this plan, any sessions in the `SYS_GROUP` consumer group get priority. (Sessions in this group are sessions created by user accounts `SYS` and `SYSTEM`.) Any resource allocation that is unused by sessions in `SYS_GROUP` is then shared by sessions belonging to the other consumer groups and subplans in the plan. Of that allocation, 25% goes to maintenance tasks, 5% goes to background processes performing diagnostic operations, and 70% goes to user sessions. The maximum utilization limit for `ORA$AUTOTASK_SUB_PLAN` and `ORA$DIAGNOSTICS` is 90. Therefore, even if the CPU is idle, this group/plan cannot be allocated more than 90% of the CPU resources.

To reduce or increase resource allocation to the automated maintenance tasks, you make adjustments to `DEFAULT_MAINTENANCE_PLAN`. See "Changing Resource Allocations for Automated Maintenance Tasks" for more information.

Note that as with any resource plan, the portion of an allocation that is not used by a consumer group or subplan is available for other consumer groups or subplans. Note also that the Database Resource Manager does not begin to limit resource allocations according to resource plans until 100% of CPU is being used.

Note:

Although `DEFAULT_MAINTENANCE_PLAN` is the default, you can assign any resource plan to any maintenance window. If you do change a maintenance window resource plan, ensure that you include the subplan `ORA$AUTOTASK_SUB_PLAN` and the consumer group `ORA$DIAGNOSTICS` in the new plan.

See Also:

[Chapter 27, "Managing Resources with Oracle Database Resource Manager"](dbrm.md) for more information on resource plans.

### Changing Resource Allocations for Automated Maintenance Tasks

To change the resource allocation for automated maintenance tasks within a maintenance window, you must change the percentage of resources allocated to the subplan `ORA$AUTOTASK_SUB_PLAN` in the resource plan for that window. (By default, the resource plan for each predefined maintenance window is `DEFAULT_MAINTENANCE_PLAN`.) You must also adjust the resource allocation for one or more other subplans or consumer groups in the window's resource plan such that the resource allocation at the top level of the plan adds up to 100%. For information on changing resource allocations, see [Chapter 27, "Managing Resources with Oracle Database Resource Manager"](dbrm.md).

## Automated Maintenance Tasks Reference

This section contains the following reference topics for automated maintenance tasks:

- Predefined Maintenance Windows
- Automated Maintenance Tasks Database Dictionary Views

### Predefined Maintenance Windows

By default there are seven predefined maintenance windows, each one representing a day of the week. The weekend maintenance windows, `SATURDAY_WINDOW` and `SUNDAY_WINDOW`, are longer in duration than the weekday maintenance windows. The window group `MAINTENANCE_WINDOW_GROUP` consists of these seven windows. The list of predefined maintenance windows is given in Table 26-1.

Table 26-1 Predefined Maintenance Windows

| Window Name | Description |
| --- | --- |
| `MONDAY_WINDOW` | Starts at 10 p.m. on Monday and ends at 2 a.m. |
| `TUESDAY_WINDOW` | Starts at 10 p.m. on Tuesday and ends at 2 a.m. |
| `WEDNESDAY_WINDOW` | Starts at 10 p.m. on Wednesday and ends at 2 a.m. |
| `THURSDAY_WINDOW` | Starts at 10 p.m. on Thursday and ends at 2 a.m. |
| `FRIDAY_WINDOW` | Starts at 10 p.m. on Friday and ends at 2 a.m. |
| `SATURDAY_WINDOW` | Starts at 6 a.m. on Saturday and is 20 hours long. |
| `SUNDAY_WINDOW` | Starts at 6 a.m. on Sunday and is 20 hours long. |

### Automated Maintenance Tasks Database Dictionary Views

Table 26-2 displays information about database dictionary views for automated maintenance tasks:

Table 26-2 Automated Maintenance Tasks Database Dictionary Views

| View Name | Description |
| --- | --- |
| `DBA_AUTOTASK_CLIENT_JOB` | Contains information about currently running Scheduler jobs created for automated maintenance tasks. It provides information about some objects targeted by those jobs, as well as some additional statistics from previous instantiations of the same task. Some of this additional data is taken from generic Scheduler views. |
| `DBA_AUTOTASK_CLIENT` | Provides statistical data for each automated maintenance task over 7-day and 30-day periods. |
| `DBA_AUTOTASK_JOB_HISTORY` | Lists the history of automated maintenance task job runs. Jobs are added to this view after they finish executing. |
| `DBA_AUTOTASK_WINDOW_CLIENTS` | Lists the windows that belong to `MAINTENANCE_WINDOW_GROUP`, along with the Enabled or Disabled status for the window for each maintenance task. Primarily used by Enterprise Manager. |
| `DBA_AUTOTASK_CLIENT_HISTORY` | Provides per-window history of job execution counts for each automated maintenance task. This information is viewable in the Job History page of Enterprise Manager. |

See Also:

["Resource Manager Data Dictionary Views"](dbrm.md) for column descriptions for views.