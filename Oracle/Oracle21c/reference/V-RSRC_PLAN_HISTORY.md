---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RSRC_PLAN_HISTORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.196 V$RSRC\_PLAN\_HISTORY

`V$RSRC_PLAN_HISTORY` displays a history of when a resource plan was enabled, disabled, or modified on the instance. Up to 15 of the most recent entries are shown. Once the database is opened, this view shows at least one row. The row with the most recent `START_TIME` and with `END_TIME` equal to NULL gives information about the current resource plan.

| Column | Datatype | Description |
| --- | --- | --- |
| `SEQUENCE#` | `NUMBER` | A sequential counter that uniquely describes a row. When the instance is restarted, this value is reset to zero. |
| `ID` | `NUMBER` | Resource plan ID; NULL if the Resource Manager was disabled |
| `NAME` | `VARCHAR2(30)` | Resource plan name; NULL if the Resource Manager was disabled |
| `START_TIME` | `DATE` | Time that the resource plan was enabled |
| `END_TIME` | `DATE` | Time that the resource plan was disabled; NULL if the row contains the current resource plan information |
| `ENABLED_BY_SCHEDULER` | `VARCHAR2(5)` | Indicates whether the plan was enabled by a Job Scheduler window (`TRUE`) or not (`FALSE`) |
| `WINDOW_NAME` | `VARCHAR2(128)` | Job Scheduler window that triggered the resource plan event; NULL if a user triggered the resource plan event |
| `ALLOWED_AUTOMATED_SWITCHES` | `VARCHAR2(5)` | Indicates whether automated plan switches were allowed after this resource plan event (`TRUE`) or whether automated plan switches were disabled after this resource plan event (`FALSE`)  See Also: the `SWITCH_PLAN` procedure |
| `CPU_MANAGED` | `VARCHAR2(3)` | Indicates whether the resource plan has parameters that specify a policy for how the Resource Manager should schedule sessions to manage CPU usage (`ON`) or whether Resource Manager is not managing CPU usage (`OFF`) |
| `CPU_SCOPE` | `VARCHAR2(13)` | Reserved for future use |
| `INSTANCE_CAGING` | `VARCHAR2(3)` | Indicates whether instance caging is enabled (`ON`) or disabled (`OFF`). Instance caging is enabled if the `CPU_COUNT` initialization parameter is explicitly modified to a value other than `0` and Resource Manager is enabled. |
| `PARALLEL_EXECUTION_MANAGED` | `VARCHAR2(32)` | State of parallel statement queuing:  - `OFF` - Parallel statement queuing is disabled - `STARTUP` - Parallel statement queuing is enabled. This is a temporary state that can occur when an Oracle RAC database is undergoing configuration changes - `FIFO` - Parallel statement queuing is enabled. All parallel statements are managed in a single Oracle RAC FIFO queue - `FULL` - Parallel statement queuing is enabled. All parallel statements are managed in per-consumer group queues according to the current resource plan. This state is used when a resource plan that contains resource allocation directives (`MGMT_P*`) is enabled. - `DISABLED` - Parallel statement queuing is disabled. This state can occur when memory is unavailable for use by parallel statement queuing in the System Global Area (SGA). Restart the Oracle instance to re-enable parallel statement queuing.  For an Oracle RAC database, only the instance running as primary Database Resource Manager (DBRM) shows the correct state of parallel statement queuing. All other instances default to the value `FULL`. A single instance database always shows the correct value for this field. |
| `CPU_COUNT` | `NUMBER` | Value of the `CPU_COUNT` initialization parameter in the container to which the data pertains |
| `CPU_MIN_COUNT` | `NUMBER` | Value of the `CPU_MIN_COUNT` initialization parameter in the container to which the data pertains |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |