---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-GCR_METRICS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.248 V$GCR\_METRICS

`V$GCR_METRICS` displays information about the current status of the metrics defined to the GCR component that runs under the LMHB background process to detect and mitigate potential issues in the cluster instances.

| Column | Datatype | Description |
| --- | --- | --- |
| `METRIC_ID` | `NUMBER` | Metric identification number as used internally to refer to the metric |
| `METRIC_NAME` | `VARCHAR2(40)` | Name of the metric |
| `ENVIRONMENT` | `NUMBER` | Environment that the metric should run in:  - `0`: Nowhere (do not run) - `1`: Oracle ASM instance only - `2`: Oracle Database instance only - `3`: Oracle ASM and Oracle Database instance - `4`: Standby instance - `5`: Oracle ASM and Standby instance - `6`: Oracle Database and Standby instance - `7`: Oracle Database, Oracle ASM, and Standby instance - `15`: All instance types |
| `FREQUENCY` | `NUMBER` | How often the metric runs, in seconds |
| `SCOPE` | `NUMBER` | The scope of sharing of the metric:  - `0`: The metric does not have associated data - `1`: Global - shared with all other instances in the cluster - `2`: Local - used only locally (not shared) - `4`: Node Global - shared with other instances in the cluster on the same node only - `8`: DB Only - Shared with other instances of the same database only |
| `DATA_TYPE` | `VARCHAR2(7)` | The type of the data associated with this metric:  - `0`: None - `1`: Boolean - `2`: Numeric - `3`: Process |
| `STATUS` | `VARCHAR2(9)` | Indicates the status of the metric: - `ACTIVE`: Indicates that the metric is active. - `INACTIVE`: Indicates that the metric is turned off. |
| `STATUS_CHANGE_TIME` | `TIMESTAMP(6)` | Time of last metric change of status |
| `LAST_RAN_ITERATION` | `NUMBER` | Iteration of the last time the metric ran |
| `LAST_RAN_TIME` | `TIMESTAMP(6)` | Time of last run |
| `LAST_PASS_ITERATION` | `NUMBER` | Iteration of last time the metric passed |
| `LAST_PASS_TIME` | `TIMESTAMP(6)` | Time of last metric pass |
| `TOTAL_PASSES` | `NUMBER` | Total number of times the metric passed since start of LMHB |
| `LAST_FAIL_ITERATION` | `NUMBER` | Iteration of last time the metric failed |
| `LAST_FAIL_TIME` | `TIMESTAMP(6)` | Time of last metric failure |
| `TOTAL_FAILS` | `NUMBER` | Total number of times the metric has failed since start of LMHB |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |