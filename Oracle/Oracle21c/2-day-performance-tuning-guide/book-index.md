---
title: "2 Day + Performance Tuning Guide"
book: "2 Day + Performance Tuning Guide"
doc_id: F32092-02
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/tdppt/book-index.html
tags:
  - oracle
  - 21c
  - 2-day-performance-tuning-guide
---

A B C D E H I J L M N O P R S T U W

---

## A

- about [13](optimizing-data-access-paths.md)
- Active Session History
	- about [8.1](resolving-transient-performance-problems.md)
		- ASH Analytics page [4.4](monitoring-real-time-database-performance.md)
		- report
		- sampled data [8.1](resolving-transient-performance-problems.md)
		- statistics [2.1.4](oracle-database-performance-method.md)
- active sessions [2.1.1](oracle-database-performance-method.md)
	- captured in Active Session History [2.1.4](oracle-database-performance-method.md)
- ADDM
	- See: Automatic Database Diagnostic Monitor
- Agent-to-Agent file transfer [10.3.2.4](using-automatic-workload-repository-warehouse.md)
- alerts
	- clearing [6.3](monitoring-performance-alerts.md)
		- default [6](monitoring-performance-alerts.md)
		- performance [6.1](monitoring-performance-alerts.md)
		- responding to [6.2](monitoring-performance-alerts.md)
- ASH
	- See: Active Session History
- ASH Analytics [4.4](monitoring-real-time-database-performance.md)
- Automatic Database Diagnostic Monitor
	- about [3.1](automatic-database-performance-monitoring.md)
		- accessing results [7.3](manual-database-performance-monitoring.md)
		- analysis [3.1.1](automatic-database-performance-monitoring.md)
		- configuring [3.2](automatic-database-performance-monitoring.md)
		- findings
		- about [3.4](automatic-database-performance-monitoring.md)
				- viewing [3.3](automatic-database-performance-monitoring.md)
		- for a multitenant environment [3.1.4](automatic-database-performance-monitoring.md)
		- for Oracle RAC [3.1.3](automatic-database-performance-monitoring.md)
		- identifying high-load SQL [11.1](identifying-high-load-sql-statements.md)
		- recommendations
		- actions [3.4](automatic-database-performance-monitoring.md)
				- implementing [3.5](automatic-database-performance-monitoring.md)
				- interpreting [3.4](automatic-database-performance-monitoring.md)
				- rationales [3.4](automatic-database-performance-monitoring.md)
				- types [3.1.2](automatic-database-performance-monitoring.md)
		- report [3.3](automatic-database-performance-monitoring.md)
		- reviewing results [3.3](automatic-database-performance-monitoring.md)
		- running manually
		- analyzing current database performance [7.1](manual-database-performance-monitoring.md)
				- analyzing historical database performance [7.2](manual-database-performance-monitoring.md)
- Automatic Memory Management [10.3.1.1](using-automatic-workload-repository-warehouse.md)
- Automatic SQL Tuning
	- modifying task attributes [12.1.2](tuning-sql-statements.md)
		- viewing recommendations [12.1.2](tuning-sql-statements.md)
		- viewing results [12.1.2](tuning-sql-statements.md)
- Automatic Storage Management [10.3.1.2](using-automatic-workload-repository-warehouse.md)
- Automatic Workload Repository
	- about [2.1](oracle-database-performance-method.md)
		- baselines [9.1](resolving-performance-degradation-over-time.md)
		- compare periods report
		- about [9](resolving-performance-degradation-over-time.md)
				- details [9.3.2](resolving-performance-degradation-over-time.md)
				- saving [9.2.1](resolving-performance-degradation-over-time.md), [9.2.3](resolving-performance-degradation-over-time.md)
				- summary [9.3.1](resolving-performance-degradation-over-time.md)
				- supplemental information [9.3.3](resolving-performance-degradation-over-time.md)
				- using [9.3](resolving-performance-degradation-over-time.md)
				- using another baseline [9.2.1](resolving-performance-degradation-over-time.md)
		- snapshots [2.1](oracle-database-performance-method.md)
		- statistics collected by [2.1](oracle-database-performance-method.md)
		- using [3.2.3](automatic-database-performance-monitoring.md)
- Automatic Workload Repository (AWR)
	- Autonomous Data Warehouse (ADW) [10.5](using-automatic-workload-repository-warehouse.md)
- Autonomous Data Warehouse (ADW)
	- Automatic Workload Repository (AWR) [10.5](using-automatic-workload-repository-warehouse.md)
- average active sessions
	- about [4.1](monitoring-real-time-database-performance.md)
- AWR
	- See: Automatic Workload Repository
- awrinfo.sql script [10.3.1.2](using-automatic-workload-repository-warehouse.md)
- AWR Warehouse
	- about [10](using-automatic-workload-repository-warehouse.md)
		- ASH Analytics page [10.2](using-automatic-workload-repository-warehouse.md)
		- AWR Report page [10.2](using-automatic-workload-repository-warehouse.md)
		- Compare Period ADDM page [10.2](using-automatic-workload-repository-warehouse.md)
		- Compare Periods Report page [10.2](using-automatic-workload-repository-warehouse.md)
		- credentials [10.3.2.1](using-automatic-workload-repository-warehouse.md)
		- ETL [10.1.2](using-automatic-workload-repository-warehouse.md)
		- extract errors [10.4](using-automatic-workload-repository-warehouse.md)
		- load errors [10.4](using-automatic-workload-repository-warehouse.md)
		- memory management [10.3.1.1](using-automatic-workload-repository-warehouse.md)
		- Performance Home page [10.2](using-automatic-workload-repository-warehouse.md)
		- set up [10.1](using-automatic-workload-repository-warehouse.md)
		- snapshot view access [10.1.1](using-automatic-workload-repository-warehouse.md)
		- source database [10.1.1](using-automatic-workload-repository-warehouse.md)
		- staging location [10.3.2.3](using-automatic-workload-repository-warehouse.md)
		- storage requirements [10.3.1.2](using-automatic-workload-repository-warehouse.md)
		- SYSAUX tablespace [10.3.1.2](using-automatic-workload-repository-warehouse.md), [10.4](using-automatic-workload-repository-warehouse.md)
		- transfer errors [10.4](using-automatic-workload-repository-warehouse.md)
		- troubleshooting [10.4](using-automatic-workload-repository-warehouse.md)

---

## C

- CONTROL\_MANAGEMENT\_PACK\_ASSESS parameter [2.2.1](oracle-database-performance-method.md)
	- and ADDM [3.2.1](automatic-database-performance-monitoring.md)
		- and database operations [5.1.3](monitoring-real-time-database-operations.md)
- CPU
	- I/O wait [4.3.1](monitoring-real-time-database-performance.md)
		- load [4.3.1](monitoring-real-time-database-performance.md)
		- performance problems [4.3.1](monitoring-real-time-database-performance.md)
		- time [2.1.1](oracle-database-performance-method.md)
		- utilization, monitoring [4.3.1](monitoring-real-time-database-performance.md)

---

## D

- data access paths, optimizing [13](optimizing-data-access-paths.md)
- Database Home page
	- accessing [1.4](introduction.md)
- database operations
	- composite operations, defined [5.1.1](monitoring-real-time-database-operations.md)
		- creating [5.2](monitoring-real-time-database-operations.md)
		- enabling monitoring with initialization parameters [5.1.3](monitoring-real-time-database-operations.md)
		- identifying an operation [5.1.4](monitoring-real-time-database-operations.md)
		- monitoring [5.1](monitoring-real-time-database-operations.md)
		- simple operations, defined [5.1.1](monitoring-real-time-database-operations.md)
		- viewing on Monitored SQL Executions page [5.3](monitoring-real-time-database-operations.md)
- database operations, monitoring
	- purpose [5.1.2](monitoring-real-time-database-operations.md)
- database performance
	- alerts [6.1](monitoring-performance-alerts.md)
		- automatic monitoring [3](automatic-database-performance-monitoring.md)
		- comparing [9](resolving-performance-degradation-over-time.md)
		- current analysis [7.1](manual-database-performance-monitoring.md)
		- degradation over time [9](resolving-performance-degradation-over-time.md)
		- historical analysis [7.2](manual-database-performance-monitoring.md)
		- manual monitoring [7](manual-database-performance-monitoring.md)
		- overview [2](oracle-database-performance-method.md)
- Database Resource Manager
	- using [4.3.1](monitoring-real-time-database-performance.md)
- database statistics
	- about [2.1](oracle-database-performance-method.md)
- database time
	- about [2.1.1](oracle-database-performance-method.md)
		- and ADDM findings [3.4](automatic-database-performance-monitoring.md)
		- in calculating average active sessions [4.1](monitoring-real-time-database-performance.md)
- database tuning
	- performance degradation over time [9](resolving-performance-degradation-over-time.md)
		- preparing the database [2.2.1](oracle-database-performance-method.md)
		- proactive tuning [2.2.2](oracle-database-performance-method.md)
		- reactive tuning [2.2.3](oracle-database-performance-method.md)
		- real-time performance problems [4](monitoring-real-time-database-performance.md)
		- SQL tuning [2.2.4](oracle-database-performance-method.md)
		- tools [1.3](introduction.md)
		- transient performance problems [8](resolving-transient-performance-problems.md)
		- using the Performance page [4](monitoring-real-time-database-performance.md)
- Data Guard [10.3.1.3](using-automatic-workload-repository-warehouse.md)
- DBIO\_EXPECTED parameter
	- setting [3.2.1](automatic-database-performance-monitoring.md), [3.2.2](automatic-database-performance-monitoring.md)
- DBMS\_ADVISOR package
	- configuring ADDM [3.2.2](automatic-database-performance-monitoring.md)
		- setting DBIO\_EXPECTED [3.2.2](automatic-database-performance-monitoring.md)
- DBMS\_SQL\_MONITOR package [5.2](monitoring-real-time-database-operations.md)
- DB time
	- See: database time
- disk
	- performance problems [4.3.3](monitoring-real-time-database-performance.md)
		- utilization, monitoring [4.3.3](monitoring-real-time-database-performance.md)

---

## E

- ETL [10.1.2](using-automatic-workload-repository-warehouse.md)
- events [6](monitoring-performance-alerts.md)
- execution plans
	- about [12](tuning-sql-statements.md)
		- evolving [12.4.3](tuning-sql-statements.md)
- extract errors, AWR Warehouse [10.4](using-automatic-workload-repository-warehouse.md)

---

## H

- high-load SQL
	- about [11](identifying-high-load-sql-statements.md)
		- identifying using ADDM [11.1](identifying-high-load-sql-statements.md)
		- identifying using top SQL [11.2](identifying-high-load-sql-statements.md)
		- statistics [2.1.5](oracle-database-performance-method.md)
		- tuning [12.1.1](tuning-sql-statements.md), [12.1.2](tuning-sql-statements.md)
- host activity, monitoring [4.3](monitoring-real-time-database-performance.md)
	- CPU [4.3.2](monitoring-real-time-database-performance.md)
		- CPU utilization [4.3.1](monitoring-real-time-database-performance.md)
		- disk utilization [4.3.3](monitoring-real-time-database-performance.md)

---

## I

- I/O wait times, monitoring [4.2.2](monitoring-real-time-database-performance.md)
- incidents [6](monitoring-performance-alerts.md)
- index
	- about [13](optimizing-data-access-paths.md)
		- bitmap [13](optimizing-data-access-paths.md)
		- B-tree [13](optimizing-data-access-paths.md)
		- creating [13.1](optimizing-data-access-paths.md)
		- functional [13](optimizing-data-access-paths.md)
- indexes
	- creating [2.2.4](oracle-database-performance-method.md)
- initialization parameter [10.3.1.1](using-automatic-workload-repository-warehouse.md)
- In-Memory Column Store (IM column store)
- instance activity, monitoring [4.2](monitoring-real-time-database-performance.md)
	- I/O wait times [4.2.2](monitoring-real-time-database-performance.md)
		- parallel execution [4.2.3](monitoring-real-time-database-performance.md)
		- services [4.2.4](monitoring-real-time-database-performance.md)
		- throughput [4.2.1](monitoring-real-time-database-performance.md)

---

## J

- job\_queue\_processes parameter [10.3.1.6](using-automatic-workload-repository-warehouse.md)

---

## L

- load errors, AWR Warehouse [10.4](using-automatic-workload-repository-warehouse.md)

---

## M

- materialized view logs [13](optimizing-data-access-paths.md)
	- creating [2.2.4](oracle-database-performance-method.md), [13.1](optimizing-data-access-paths.md)
- materialized views
	- creating [2.2.4](oracle-database-performance-method.md), [13.1](optimizing-data-access-paths.md)
- memory
	- performance problems [4.3.2](monitoring-real-time-database-performance.md)
		- swap utilization [4.3.2](monitoring-real-time-database-performance.md)
		- utilization, monitoring [4.3.2](monitoring-real-time-database-performance.md)
- memory management, AWR Warehouse [10.3.1.1](using-automatic-workload-repository-warehouse.md)
- metrics [6.1](monitoring-performance-alerts.md), [9.1.4](resolving-performance-degradation-over-time.md)
- Monitored SQL Executions page [5.3](monitoring-real-time-database-operations.md)
- monitoring
	- PL/SQL [4.1.3](monitoring-real-time-database-performance.md)
		- resource consumption [4.1.4](monitoring-real-time-database-performance.md)
		- session attributes [4.1.6](monitoring-real-time-database-performance.md)
		- session identifiers [4.1.5](monitoring-real-time-database-performance.md)
		- SQL [4.1.2](monitoring-real-time-database-performance.md)

---

## N

- Network Latency [10.3.2.4](using-automatic-workload-repository-warehouse.md)

---

## O

- Oracle Diagnostics Pack [1.3](introduction.md)
- Oracle performance method
	- about [2](oracle-database-performance-method.md)
		- pretuning tasks [2.2.1](oracle-database-performance-method.md)
		- proactive database tuning tasks [2.2.2](oracle-database-performance-method.md)
		- reactive database tuning tasks [2.2.3](oracle-database-performance-method.md)
		- SQL tuning tasks [2.2.4](oracle-database-performance-method.md)
		- using [2.2](oracle-database-performance-method.md)
- Oracle Tuning Pack [1.3](introduction.md)

---

## P

- parallel execution, monitoring [4.2.3](monitoring-real-time-database-performance.md)
- parameters
	- CONTROL\_MANAGEMENT\_PACK\_ASSESS [2.2.1](oracle-database-performance-method.md), [3.2.1](automatic-database-performance-monitoring.md), [5.1.3](monitoring-real-time-database-operations.md)
		- initialization [9.3.3](resolving-performance-degradation-over-time.md)
		- STATISTICS\_LEVEL [3.2.1](automatic-database-performance-monitoring.md), [5.1.3](monitoring-real-time-database-operations.md)
- Performance page
	- about [4](monitoring-real-time-database-performance.md)
- performance problems
	- common [2.3](oracle-database-performance-method.md)
		- CPU [4.3.1](monitoring-real-time-database-performance.md)
		- diagnosing [3.1](automatic-database-performance-monitoring.md)
		- disk [4.3.3](monitoring-real-time-database-performance.md)
		- memory [4.3.2](monitoring-real-time-database-performance.md)
		- real-time [4](monitoring-real-time-database-performance.md)
		- transient [8](resolving-transient-performance-problems.md)
- PL/SQL
	- monitoring [4.1.3](monitoring-real-time-database-performance.md)
- problems, as a type of incident [6](monitoring-performance-alerts.md)

---

## S

- services
	- about [4.2.4](monitoring-real-time-database-performance.md)
		- monitoring [4.2.4](monitoring-real-time-database-performance.md)
- session attributes [4.1.6](monitoring-real-time-database-performance.md)
- session identifiers [4.1.5](monitoring-real-time-database-performance.md)
- sessions
	- about [2.1.1](oracle-database-performance-method.md)
		- active [2.1.1](oracle-database-performance-method.md), [2.1.4](oracle-database-performance-method.md)
		- average active [4.1](monitoring-real-time-database-performance.md)
- snapshots
	- about [2.1](oracle-database-performance-method.md)
		- creating [3.2.3.1](automatic-database-performance-monitoring.md)
		- default interval [3.2.3](automatic-database-performance-monitoring.md)
		- modifying settings [3.2.3.2](automatic-database-performance-monitoring.md)
		- viewing statistics [3.6](automatic-database-performance-monitoring.md)
- snapshot upload, AWR Warehouse [10.1.2](using-automatic-workload-repository-warehouse.md)
- source ADW, AWR Warehouse [10.1.1](using-automatic-workload-repository-warehouse.md)
- source database, AWR Warehouse [10.1.1](using-automatic-workload-repository-warehouse.md)
- spikes
	- determining cause of [4.4](monitoring-real-time-database-performance.md)
- SQL
	- monitoring [4.1.2](monitoring-real-time-database-performance.md)
- SQL Access Advisor
	- about [12](tuning-sql-statements.md), [13](optimizing-data-access-paths.md)
		- filters [13.1.3](optimizing-data-access-paths.md)
		- initial options [13.1.1](optimizing-data-access-paths.md), [13.2](optimizing-data-access-paths.md)
		- recommendations
		- about [13](optimizing-data-access-paths.md)
				- details [13.2.2](optimizing-data-access-paths.md)
				- implementing [13.3](optimizing-data-access-paths.md)
				- options [13.1.4](optimizing-data-access-paths.md)
				- reviewing [13.2](optimizing-data-access-paths.md)
				- SQL [13.2.3](optimizing-data-access-paths.md)
				- summary [13.2.1](optimizing-data-access-paths.md)
		- running [13.1](optimizing-data-access-paths.md)
		- scheduling [13.1.5](optimizing-data-access-paths.md)
		- task options [13.2.4](optimizing-data-access-paths.md)
		- workload options [13.2.4](optimizing-data-access-paths.md)
		- workload source [13.1.2](optimizing-data-access-paths.md)
- SQL Performance Analyzer
	- about [2.3](oracle-database-performance-method.md)
- SQL plan baselines
	- about [12.4](tuning-sql-statements.md)
		- capturing automatically [12.4.1](tuning-sql-statements.md)
		- evolving [12.4.3](tuning-sql-statements.md)
		- loading manually [12.4.2](tuning-sql-statements.md)
- SQL plan management [12.4](tuning-sql-statements.md)
- SQL Plan Management Evolve Advisor [12.4.3](tuning-sql-statements.md)
- SQL profiles
	- deleting [12.3](tuning-sql-statements.md)
		- disabling [12.3](tuning-sql-statements.md)
		- enabling [12.3](tuning-sql-statements.md)
- SQL Tuning Advisor
	- about [12](tuning-sql-statements.md)
		- automated maintenance tasks [12.1.2](tuning-sql-statements.md)
		- implementing recommendations [12.1.1](tuning-sql-statements.md)
		- limited scope [12.1.1](tuning-sql-statements.md)
		- using [12.1.1](tuning-sql-statements.md), [12.1.2](tuning-sql-statements.md)
- SQL tuning sets
	- about [12.2](tuning-sql-statements.md)
		- creating [12.2.1](tuning-sql-statements.md)
		- load method [12.2.1.2](tuning-sql-statements.md)
- stacked area charts
	- described [4.1](monitoring-real-time-database-performance.md)
- statistics
	- Active Session History [2.1.4](oracle-database-performance-method.md)
		- baselines [9.1](resolving-performance-degradation-over-time.md)
		- database [2.1](oracle-database-performance-method.md)
		- database time [2.1.1](oracle-database-performance-method.md), [3.4](automatic-database-performance-monitoring.md)
		- default retention [3.2.3](automatic-database-performance-monitoring.md)
		- gathering [2.1](oracle-database-performance-method.md)
		- high-load SQL [2.1.5](oracle-database-performance-method.md)
		- sampled data [8.1](resolving-transient-performance-problems.md)
		- session [2.1.3](oracle-database-performance-method.md)
		- system [2.1.3](oracle-database-performance-method.md)
		- wait events [2.1.2](oracle-database-performance-method.md)
- STATISTICS\_LEVEL parameter
	- and ADDM [3.2.1](automatic-database-performance-monitoring.md)
		- and database operations [5.1.3](monitoring-real-time-database-operations.md)
- stats collection [10.3.1.5](using-automatic-workload-repository-warehouse.md)
- storage requirements, AWR Warehouse [10.3.1.2](using-automatic-workload-repository-warehouse.md)
- SYSAUX tablespace [10.3.1.2](using-automatic-workload-repository-warehouse.md), [10.4](using-automatic-workload-repository-warehouse.md)

---

## T

- throughput, monitoring [4.2.1](monitoring-real-time-database-performance.md)
- Top Activity page
	- about [11.2](identifying-high-load-sql-statements.md)
- top dimensions
	- monitoring [4.1.1](monitoring-real-time-database-performance.md)
- top SQL
	- identifying high-load SQL [11.2](identifying-high-load-sql-statements.md)
		- in Active Session History report [8.3.3](resolving-transient-performance-problems.md)
- transfer errors, AWR Warehouse [10.4](using-automatic-workload-repository-warehouse.md)
- troubleshooting, AWR Warehouse [10.4](using-automatic-workload-repository-warehouse.md)

---

## U

- user activity, monitoring

---

## W

- wait classes
	- grouped wait events [2.1.2](oracle-database-performance-method.md)
- wait events
	- statistics [2.1.2](oracle-database-performance-method.md)
- wait time [2.1.1](oracle-database-performance-method.md)