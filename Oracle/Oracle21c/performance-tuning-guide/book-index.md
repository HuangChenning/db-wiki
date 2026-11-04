---
title: Database Performance Tuning Guide
book: Database Performance Tuning Guide
doc_id: F32091-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/tgdba/book-index.html
tags:
  - oracle
  - 21c
  - performance-tuning-guide
---

A B C D E F H I L M N O P Q R S T U V W

---

## A

- Active Session History
	- report
		- activity over time [9.3.8](analyzing-sampled-data.md)
				- load profile [9.3.2](analyzing-sampled-data.md)
				- top events [9.3.1](analyzing-sampled-data.md)
				- top files [9.3.7](analyzing-sampled-data.md)
				- top Java [9.3.5](analyzing-sampled-data.md)
				- top latches [9.3.7](analyzing-sampled-data.md)
				- top objects [9.3.7](analyzing-sampled-data.md)
				- top PL/SQL [9.3.4](analyzing-sampled-data.md)
				- top sessions [9.3.6](analyzing-sampled-data.md)
				- Top SQL [9.3.3](analyzing-sampled-data.md)
				- using [9.3](analyzing-sampled-data.md)
		- reports [9.2](analyzing-sampled-data.md)
- ADDM
	- enabling in a PDB [7.1.3.1](automatic-performance-diagnostics.md)
- allocation of memory [11.1](database-memory-allocation.md)
- applications
	- deploying [2.7](designing-and-developing-for-performance.md)
		- design principles [2.5](designing-and-developing-for-performance.md)
		- development trends [2.5.7](designing-and-developing-for-performance.md)
		- implementing [2.5.6](designing-and-developing-for-performance.md)
- Automatic Database Diagnostic Monitor
	- actions and rationales of recommendations [7.1.5](automatic-performance-diagnostics.md)
		- analysis results example [7.1.6](automatic-performance-diagnostics.md)
		- and DB time [7.1.1](automatic-performance-diagnostics.md)
		- example report [7.1.6](automatic-performance-diagnostics.md)
		- findings [7.1.5](automatic-performance-diagnostics.md)
		- results [7.1.5](automatic-performance-diagnostics.md)
		- setups [7.2](automatic-performance-diagnostics.md)
		- types of problems considered [7.1.1](automatic-performance-diagnostics.md)
		- types of recommendations [7.1.5](automatic-performance-diagnostics.md)
- automatic database diagnostic monitoring [1.2.1](performance-tuning-overview.md)
- automatic memory management [11.2.2](database-memory-allocation.md)
- automatic segment-space management [4.1.4](configuring-database-for-performance.md), [10.3.2](instance-tuning-using-performance-views.md), [17.2.6.2](IO-configuration-and-design.md)
- Automatic shared memory management [12.1](tuning-system-global-area.md)
- automatic SQL tuning [1.2.1](performance-tuning-overview.md)
- automatic undo management [4.1.2](configuring-database-for-performance.md)
- Automatic Workload Repository [1.2.1](performance-tuning-overview.md)
	- Active Data Guard support [6.2.8](gathering-database-statistics.md)
		- AWR data storage and retrieval in a multitenant environment [6.2.7.2](gathering-database-statistics.md)
		- categorization of AWR statistics in a multitenant environment [6.2.7.1](gathering-database-statistics.md)
		- compare periods report
		- about [8.1](comparing-database-performance-over-time.md)
				- advisory statistics [8.3.2.8](comparing-database-performance-over-time.md), [8.3.2.16](comparing-database-performance-over-time.md)
				- details [8.3.2](comparing-database-performance-over-time.md)
				- dictionary cache statistics [8.3.2.14](comparing-database-performance-over-time.md)
				- I/O statistics [8.3.2.7](comparing-database-performance-over-time.md)
				- instance activity statistics [8.3.2.6](comparing-database-performance-over-time.md)
				- latch statistics [8.3.2.11](comparing-database-performance-over-time.md)
				- library cache statistics [8.3.2.15](comparing-database-performance-over-time.md)
				- operating system statistics [8.3.2.2](comparing-database-performance-over-time.md)
				- segment statistics [8.3.2.12](comparing-database-performance-over-time.md), [8.3.2.13](comparing-database-performance-over-time.md)
				- service statistics [8.3.2.4](comparing-database-performance-over-time.md)
				- SQL statistics [8.3.2.5](comparing-database-performance-over-time.md)
				- summary [8.3.1](comparing-database-performance-over-time.md)
				- supplemental information [8.3.3](comparing-database-performance-over-time.md)
				- time model statistics [8.3.2.1](comparing-database-performance-over-time.md)
				- undo statistics [8.3.2.10](comparing-database-performance-over-time.md)
				- using [8.3](comparing-database-performance-over-time.md)
				- wait events [8.3.2.3](comparing-database-performance-over-time.md)
				- wait statistics [8.3.2.9](comparing-database-performance-over-time.md)
		- configuring [6.2.1](gathering-database-statistics.md)
		- default settings [6.1.4](gathering-database-statistics.md)
		- factors affecting space usage [6.1.4](gathering-database-statistics.md)
		- managing snapshots in ADG standby databases [6.2.8.2](gathering-database-statistics.md)
		- minimizing space usage [6.1.4](gathering-database-statistics.md)
		- modifying snapshot settings [6.2.2.4](gathering-database-statistics.md)
		- multitenant environment support [6.2.7](gathering-database-statistics.md)
		- overview [6.1.1](gathering-database-statistics.md)
		- recommendations for retention period [6.1.4](gathering-database-statistics.md)
		- reports [6.3.2.1](gathering-database-statistics.md)
		- retention period [6.1.4](gathering-database-statistics.md)
		- space usage [6.1.4](gathering-database-statistics.md)
		- statistics collected [6.1.1](gathering-database-statistics.md)
		- turning off automatic snapshot collection [6.1.4](gathering-database-statistics.md)
		- unusual percentages in reports [6.3](gathering-database-statistics.md)
		- Viewing AWR data in a multitenant environment [6.2.7.3](gathering-database-statistics.md)
		- viewing remote snapshots for ADG standby databases [6.2.8.3](gathering-database-statistics.md)
		- views for accessing data [6.2.6](gathering-database-statistics.md)
- Autonomous Data Warehouse
	- ADW [12.2](tuning-system-global-area.md)
- Autonomous Transaction Processing
	- ATP [12.2](tuning-system-global-area.md)
- awrrpt.sql
	- Automatic Workload Repository report [6.3.2.1](gathering-database-statistics.md)

---

## B

- baselines [1.1.2.2](performance-tuning-overview.md), [6.1.3](gathering-database-statistics.md)
	- performance [6.1](gathering-database-statistics.md)
- benchmarking workloads [2.6.2](designing-and-developing-for-performance.md)
- big bang rollout strategy [2.7.1](designing-and-developing-for-performance.md)
- bitmap indexes [2.5.3.2](designing-and-developing-for-performance.md)
- block cleanout [10.2.4](instance-tuning-using-performance-views.md)
- block size
	- choosing [17.2.6](IO-configuration-and-design.md)
		- optimal [17.2.6](IO-configuration-and-design.md)
- bottlenecks
	- elimination [1.1.2.4.2](performance-tuning-overview.md)
		- fixing [3.1](performance-improvement-methods.md)
		- identifying [3.1](performance-improvement-methods.md)
		- memory [11.1](database-memory-allocation.md)
		- resource [10.3.19](instance-tuning-using-performance-views.md)
- B-tree indexes [2.5.3.2](designing-and-developing-for-performance.md)
- buffer busy wait events [10.3.2](instance-tuning-using-performance-views.md)
	- actions [10.3.2](instance-tuning-using-performance-views.md)
- buffer cache
	- contention [10.3.3](instance-tuning-using-performance-views.md), [10.3.4](instance-tuning-using-performance-views.md), [10.3.11](instance-tuning-using-performance-views.md)
		- hit ratio [13.2.2](tuning-database-buffer-cache.md)
- buffer pools
	- multiple [13.3](tuning-database-buffer-cache.md)
- buffer waits
	- about [8.3.2.9.1](comparing-database-performance-over-time.md)
- business logic [2.4.1.2](designing-and-developing-for-performance.md), [2.5.6](designing-and-developing-for-performance.md)

---

## C

- chained rows [10.2.4](instance-tuning-using-performance-views.md)
- classes
	- wait events [5.1.3](measuring-database-performance.md), [10.1.3.2](instance-tuning-using-performance-views.md)
- client/server applications [18.4.1.2](managing-operating-system-resources.md)
- Cloud Control [1.2](performance-tuning-overview.md)
- column order
	- indexes [2.5.3.5](designing-and-developing-for-performance.md)
- components
	- hardware [2.4.1.1](designing-and-developing-for-performance.md)
		- software [2.4.1.2](designing-and-developing-for-performance.md)
- conceptual modeling [3.1.2](performance-improvement-methods.md)
- consistency
	- read [10.2.4](instance-tuning-using-performance-views.md)
- consistent gets from cache statistic [13.2.2](tuning-database-buffer-cache.md)
- contention
	- library cache latch [10.3.11](instance-tuning-using-performance-views.md)
		- memory [10](instance-tuning-using-performance-views.md), [11.1](database-memory-allocation.md)
		- shared pool [10.3.11](instance-tuning-using-performance-views.md)
		- tuning [10](instance-tuning-using-performance-views.md)
		- wait events [10.3.11](instance-tuning-using-performance-views.md)
- context switches [18.4.1.4.2](managing-operating-system-resources.md)
- CONTROL\_FILES initialization parameter [4.1.1](configuring-database-for-performance.md)
- CPUs [2.4.1.1](designing-and-developing-for-performance.md)
	- statistics [10.1.2.1.3](instance-tuning-using-performance-views.md)
		- utilization [18.4.1](managing-operating-system-resources.md)
- CREATE INDEX statement
	- PARALLEL clause [4.2.3](configuring-database-for-performance.md)
- CURSOR\_SHARING initialization parameter [14.2.1](tuning-shared-pool-and-large-pool.md)
- CURSOR\_SPACE\_FOR\_TIME initialization parameter [14.3.2](tuning-shared-pool-and-large-pool.md)
- cursors
	- accessing [14.2.6](tuning-shared-pool-and-large-pool.md)
		- sharing [14.2.6](tuning-shared-pool-and-large-pool.md)

---

## D

- data
	- and transactions [2.4.1.2](designing-and-developing-for-performance.md)
		- cache [18.1.1](managing-operating-system-resources.md)
		- gathering [5.1](measuring-database-performance.md)
		- modeling [2.5.2](designing-and-developing-for-performance.md)
		- queries [2.4.2](designing-and-developing-for-performance.md)
		- searches [2.4.2](designing-and-developing-for-performance.md)
- database caching modes
	- configuring [13.5](tuning-database-buffer-cache.md)
		- default database caching mode [13.5.1](tuning-database-buffer-cache.md)
		- determining which mode to use [13.5.3](tuning-database-buffer-cache.md)
		- force full database caching mode
		- about [13.5.2](tuning-database-buffer-cache.md)
		- verifying [13.5.4](tuning-database-buffer-cache.md)
- database monitoring [1.2.1](performance-tuning-overview.md)
	- diagnostic [7.1](automatic-performance-diagnostics.md)
- database performance
	- comparing [8.1](comparing-database-performance-over-time.md)
		- degradation over time [8.1](comparing-database-performance-over-time.md)
- Database Resource Manager [10.1.2.1.3](instance-tuning-using-performance-views.md), [18.1.3](managing-operating-system-resources.md), [18.4.2](managing-operating-system-resources.md)
- databases
	- diagnosing and monitoring [7.1](automatic-performance-diagnostics.md)
		- size [2.4.2](designing-and-developing-for-performance.md)
		- statistics [5.1](measuring-database-performance.md)
- database tuning
	- performance degradation over time [8.1](comparing-database-performance-over-time.md)
		- transient performance problems [9.1](analyzing-sampled-data.md)
- DB\_BLOCK\_SIZE initialization parameter [17.2.1.2](IO-configuration-and-design.md)
- DB\_DOMAIN initialization parameter [4.1.1](configuring-database-for-performance.md)
- DB\_NAME initialization parameter [4.1.1](configuring-database-for-performance.md)
- DBA\_OBJECTS view [13.3.5.2](tuning-database-buffer-cache.md)
- db block gets from cache statistic [13.2.2](tuning-database-buffer-cache.md)
- db file scattered read wait events [10.3.3](instance-tuning-using-performance-views.md)
	- actions [10.3.3](instance-tuning-using-performance-views.md), [10.3.4](instance-tuning-using-performance-views.md)
- db file sequential read wait events [10.3.3](instance-tuning-using-performance-views.md), [10.3.4](instance-tuning-using-performance-views.md)
	- actions [10.3.4](instance-tuning-using-performance-views.md)
- DBMS\_ADVISOR package
	- setting DBIO\_EXPECTED [7.2](automatic-performance-diagnostics.md)
		- setups for ADDM [7.2](automatic-performance-diagnostics.md)
- DBMS\_SHARED\_POOL package
	- managing the shared pool [14.3.5](tuning-shared-pool-and-large-pool.md)
- DB time
	- metric [7.1.1](automatic-performance-diagnostics.md)
		- statistic [5.1.1](measuring-database-performance.md)
- debugging designs [2.6.4](designing-and-developing-for-performance.md)
- deploying applications [2.7](designing-and-developing-for-performance.md)
- design principles [2.5](designing-and-developing-for-performance.md)
- designs
	- debugging [2.6.4](designing-and-developing-for-performance.md)
		- testing [2.6.4](designing-and-developing-for-performance.md)
		- validating [2.6.4](designing-and-developing-for-performance.md)
- development environments [2.5.6](designing-and-developing-for-performance.md)
- diagnostic monitoring [1.2.1](performance-tuning-overview.md), [7.1](automatic-performance-diagnostics.md)
- dictionary cache [8.3.2.14](comparing-database-performance-over-time.md)
- direct path
	- read events [10.3.5](instance-tuning-using-performance-views.md)
		- read events actions [10.3.5](instance-tuning-using-performance-views.md)
		- read events causes [10.3.5](instance-tuning-using-performance-views.md)
		- wait events [10.3.6](instance-tuning-using-performance-views.md)
		- write events actions [10.3.6](instance-tuning-using-performance-views.md)
		- write events causes [10.3.6](instance-tuning-using-performance-views.md)
- disks
	- monitoring operating system file activity [10.1.2.2](instance-tuning-using-performance-views.md)

---

## E

- emergencies
	- performance [3.2](performance-improvement-methods.md)
- Emergency Performance Method [3.2.1](performance-improvement-methods.md)
- End to End Application Tracing
	- action and module names [2.5.6](designing-and-developing-for-performance.md)
- enqueue
	- about [8.3.2.9.2](comparing-database-performance-over-time.md)
- enqueue wait events [10.3.7](instance-tuning-using-performance-views.md)
	- actions [10.3.7](instance-tuning-using-performance-views.md)
		- statistics [10.1.3.4](instance-tuning-using-performance-views.md)
- estimating workloads [2.6.2](designing-and-developing-for-performance.md)
	- benchmarking [2.6.2](designing-and-developing-for-performance.md)
		- extrapolating [2.6.2](designing-and-developing-for-performance.md)
- extrapolating workloads [2.6.2](designing-and-developing-for-performance.md)

---

## F

- FAST\_START\_MTTR\_TARGET
	- and tuning instance recovery [10.4.3](instance-tuning-using-performance-views.md)
- fast lookup
	- disabling for a table [12.6.3.3](tuning-system-global-area.md)
- Fast-Start checkpointing architecture [10.4.2](instance-tuning-using-performance-views.md)
- Fast-Start Fault Recovery [10.4](instance-tuning-using-performance-views.md), [10.4.2](instance-tuning-using-performance-views.md)
- free buffer wait events [10.3.9](instance-tuning-using-performance-views.md)
- free lists [10.3.2](instance-tuning-using-performance-views.md)
- function-based indexes [2.5.3.2](designing-and-developing-for-performance.md)

---

## I

- I/O
	- and SQL statements [10.3.3](instance-tuning-using-performance-views.md)
		- contention [10.1.2.2.1](instance-tuning-using-performance-views.md), [10.1.3.2](instance-tuning-using-performance-views.md), [10.3.3](instance-tuning-using-performance-views.md), [10.3.15](instance-tuning-using-performance-views.md)
		- excessive I/O waits [10.3.3](instance-tuning-using-performance-views.md)
		- monitoring [10.1.2.2](instance-tuning-using-performance-views.md)
		- objects causing I/O waits [10.3.3](instance-tuning-using-performance-views.md)
- idle wait events [10.3.10](instance-tuning-using-performance-views.md)
	- SQL\*Net message from client [10.3.19](instance-tuning-using-performance-views.md)
- indexes
	- adding columns [2.5.3.1](designing-and-developing-for-performance.md)
		- appending columns [2.5.3.1](designing-and-developing-for-performance.md)
		- bitmap [2.5.3.2](designing-and-developing-for-performance.md)
		- B-tree [2.5.3.2](designing-and-developing-for-performance.md)
		- column order [2.5.3.5](designing-and-developing-for-performance.md)
		- costs [2.5.3.3](designing-and-developing-for-performance.md)
		- creating [4.2.3](configuring-database-for-performance.md)
		- design [2.5.3](designing-and-developing-for-performance.md)
		- function-based [2.5.3.2](designing-and-developing-for-performance.md)
		- partitioned [2.5.3.2](designing-and-developing-for-performance.md)
		- placement on disk [17.2.2](IO-configuration-and-design.md)
		- reducing I/O [2.5.3.5](designing-and-developing-for-performance.md)
		- reverse key [2.5.3.2](designing-and-developing-for-performance.md)
		- selectivity [2.5.3.5](designing-and-developing-for-performance.md)
		- sequences in [2.5.3.4](designing-and-developing-for-performance.md)
		- serializing in [2.5.3.4](designing-and-developing-for-performance.md)
- initialization parameters
	- CONTROL\_FILES [4.1.1](configuring-database-for-performance.md)
		- DB\_DOMAIN [4.1.1](configuring-database-for-performance.md)
		- DB\_NAME [4.1.1](configuring-database-for-performance.md)
		- OPEN\_CURSORS [4.1.1](configuring-database-for-performance.md)
		- STREAMS\_POOL\_SIZE [12.3](tuning-system-global-area.md)
- instance activity
	- comparing [8.3.2.6](comparing-database-performance-over-time.md)
- instance caging [18.4](managing-operating-system-resources.md)
- instance configuration
	- initialization files [4.1.1](configuring-database-for-performance.md)
		- performance considerations [4.1](configuring-database-for-performance.md)
- instance recovery
	- Fast-Start Fault Recovery [10.4.2](instance-tuning-using-performance-views.md)
		- performance tuning [10.4](instance-tuning-using-performance-views.md)
- Internet scalability [2.3.2](designing-and-developing-for-performance.md)

---

## L

- LARGE\_POOL\_SIZE initialization parameter [14.4.3](tuning-shared-pool-and-large-pool.md)
- latch contention
	- library cache latches [10.2.1](instance-tuning-using-performance-views.md)
		- shared pool latches [10.2.1](instance-tuning-using-performance-views.md)
- latches [9.3.7.3](analyzing-sampled-data.md)
	- tuning [1.1.2.3](performance-tuning-overview.md), [10.3.11](instance-tuning-using-performance-views.md)
- latch free wait events
	- actions [10.3.11](instance-tuning-using-performance-views.md)
- latch wait events [10.3.11](instance-tuning-using-performance-views.md)
- library cache [8.3.2.15](comparing-database-performance-over-time.md)
	- latch contention [10.3.11](instance-tuning-using-performance-views.md)
		- latch wait events [10.3.11](instance-tuning-using-performance-views.md)
		- lock [10.3.14](instance-tuning-using-performance-views.md)
		- pin [10.3.13](instance-tuning-using-performance-views.md)
- linear scalability [2.3.3](designing-and-developing-for-performance.md)
- locks and lock holders
	- finding [10.3.7](instance-tuning-using-performance-views.md)
- log buffer
	- space wait events [10.3.15](instance-tuning-using-performance-views.md)
- log file
	- parallel write wait events [10.3.12](instance-tuning-using-performance-views.md)
		- switch wait events [10.3.16](instance-tuning-using-performance-views.md)
		- sync wait events [10.3.17](instance-tuning-using-performance-views.md)
- log writer processes
	- tuning [17.2.3.2](IO-configuration-and-design.md)
- LRU
	- aging policy [13.3](tuning-database-buffer-cache.md)
		- latch contention [10.3.11](instance-tuning-using-performance-views.md)

---

## M

- MAXOPENCURSORS clause [14.2.6.2](tuning-shared-pool-and-large-pool.md)
- max session memory statistic [14.4.3](tuning-shared-pool-and-large-pool.md)
- MEMOPTIMIZE\_POOL\_SIZE initialization parameter [12.6.3.1](tuning-system-global-area.md)
- MEMOPTIMIZE\_WRITE hint [12.6.2.2](tuning-system-global-area.md)
- Memoptimized Rowstore
	- about [12.6.1](tuning-system-global-area.md)
		- fast ingest
		- about [12.6.2](tuning-system-global-area.md)
				- disabling [12.6.2.3](tuning-system-global-area.md)
				- enabling [12.6.2.1](tuning-system-global-area.md)
				- using [12.6.2.2](tuning-system-global-area.md)
		- fast lookup
		- about [12.6.3](tuning-system-global-area.md)
				- enabling for a table [12.6.3.2](tuning-system-global-area.md)
		- memoptimize pool [12.6.3.1](tuning-system-global-area.md)
- MEMOPTIMIZE FOR WRITE clause [12.6.2.1](tuning-system-global-area.md)
- memoptimize pool [12.6.3.1](tuning-system-global-area.md)
- memory
	- hardware component [2.4.1.1](designing-and-developing-for-performance.md)
		- PGA statistics [8.3.2.8](comparing-database-performance-over-time.md)
		- statistics [8.3.2.16](comparing-database-performance-over-time.md)
- memory allocation
	- importance [11.1](database-memory-allocation.md)
		- tuning [12.3.5](tuning-system-global-area.md)
- memory management
	- automatic shared [11.2.2](database-memory-allocation.md)
- metrics [6.1](gathering-database-statistics.md)
- migrated rows [10.2.4](instance-tuning-using-performance-views.md)
- mirroring
	- redo logs [17.2.3.3](IO-configuration-and-design.md)
- modeling
	- conceptual [3.1.2](performance-improvement-methods.md)
		- data [2.5.2](designing-and-developing-for-performance.md)
		- workloads [2.6.3](designing-and-developing-for-performance.md)
- monitoring
	- diagnostic [1.2.1](performance-tuning-overview.md)
- multiple buffer pools [13.3](tuning-database-buffer-cache.md)

---

## N

- NAMESPACE column
	- V$LIBRARYCACHE view [14.3.1.1.1](tuning-shared-pool-and-large-pool.md)
- network
	- hardware component [2.4.1.1](designing-and-developing-for-performance.md)
		- speed [2.4.2](designing-and-developing-for-performance.md)
- network communication wait events [10.3.19](instance-tuning-using-performance-views.md)
	- db file scattered read wait events [10.3.3](instance-tuning-using-performance-views.md)
		- db file sequential read wait events [10.3.3](instance-tuning-using-performance-views.md), [10.3.4](instance-tuning-using-performance-views.md)
		- SQL\*Net message from Dblink [10.3.19](instance-tuning-using-performance-views.md)
		- SQL\*Net more data to client [10.3.19](instance-tuning-using-performance-views.md)

---

## O

- object-orientation [2.5.7](designing-and-developing-for-performance.md)
- OPEN\_CURSORS initialization parameter [4.1.1](configuring-database-for-performance.md)
- operating system
	- data cache [18.1.1](managing-operating-system-resources.md)
		- monitoring disk I/O [10.1.2.2](instance-tuning-using-performance-views.md)
- optimization
	- described [1.1.3.1](performance-tuning-overview.md)
- optimizer
	- introduction [1.1.3.1](performance-tuning-overview.md)
		- query [1.1.3.1](performance-tuning-overview.md)
- Oracle CPU statistics [10.1.2.1.3](instance-tuning-using-performance-views.md)
- Oracle Enterprise Manager Cloud Control [1.2](performance-tuning-overview.md)
	- advisors [1.2.1](performance-tuning-overview.md)
		- Performance page [1.2.1](performance-tuning-overview.md)
- Oracle Forms
	- control of parsing and private SQL areas [14.2.6.5](tuning-shared-pool-and-large-pool.md)
- Oracle Managed Files [17.2.5](IO-configuration-and-design.md)
- Oracle Orion
	- calibration tool parameters [17.4.4](IO-configuration-and-design.md)
		- command-line options [17.4.4](IO-configuration-and-design.md)
- Oracle performance improvement method [3.1](performance-improvement-methods.md)
	- steps [3.1.1](performance-improvement-methods.md)

---

## P

- page table [18.4.1.1.2](managing-operating-system-resources.md)
- paging [18.4.1.2](managing-operating-system-resources.md)
	- reducing [12.3.4.1](tuning-system-global-area.md)
- PARALLEL clause
	- CREATE INDEX statement [4.2.3](configuring-database-for-performance.md)
- parameter
	- RESULT\_CACHE\_MAX\_TEMP\_RESULT [15.2.3](tuning-result-cache.md)
		- RESULT\_CACHE\_MAX\_TEMP\_SIZE [15.2.3](tuning-result-cache.md)
		- RESULT\_CACHE\_MODE [15.2.3](tuning-result-cache.md)
- parameters
	- initialization [8.3.3.1](comparing-database-performance-over-time.md)
- parsing
	- hard [2.5.5](designing-and-developing-for-performance.md)
		- Oracle Forms [14.2.6.5](tuning-shared-pool-and-large-pool.md)
		- Oracle precompilers [14.2.6.2](tuning-shared-pool-and-large-pool.md)
		- reducing unnecessary calls [14.2.6](tuning-shared-pool-and-large-pool.md)
		- soft [2.5.5](designing-and-developing-for-performance.md)
- partitioned indexes [2.5.3.2](designing-and-developing-for-performance.md)
- performance
	- emergencies [3.2](performance-improvement-methods.md)
		- improvement method [3.1](performance-improvement-methods.md)
		- improvement method steps [3.1.1](performance-improvement-methods.md)
		- mainframe [18.2.3](managing-operating-system-resources.md)
		- monitoring memory on Windows [18.4.1.1.1](managing-operating-system-resources.md)
		- tools for diagnosing and tuning [1.2](performance-tuning-overview.md)
		- tools for performance tuning [1.2](performance-tuning-overview.md)
		- UNIX-based systems [18.2.1](managing-operating-system-resources.md)
		- Windows [18.2.2](managing-operating-system-resources.md)
- Performance Hub active reports
	- about [6.4.1](gathering-database-statistics.md)
		- generating [6.4](gathering-database-statistics.md), [6.4.3](gathering-database-statistics.md)
- performance problems
	- transient [9.1](analyzing-sampled-data.md)
- performance tuning
	- Fast-Start Fault Recovery [10.4](instance-tuning-using-performance-views.md)
		- instance recovery [10.4](instance-tuning-using-performance-views.md)
		- FAST\_START\_MTTR\_TARGET [10.4.2](instance-tuning-using-performance-views.md)
				- setting FAST\_START\_MTTR\_TARGET [10.4.3](instance-tuning-using-performance-views.md)
				- using V$INSTANCE\_RECOVERY [10.4.2.3](instance-tuning-using-performance-views.md)
- per-session PGA memory limit
	- PGA [16.3.2](tuning-program-global-area.md)
- PGA\_AGGREGATE\_TARGET initialization parameter [4.1.1](configuring-database-for-performance.md)
- physical reads from cache statistic [13.2.2](tuning-database-buffer-cache.md)
- proactive monitoring [1.1.2.4.1](performance-tuning-overview.md)
- processes
	- scheduling [18.4.1.4.1](managing-operating-system-resources.md)
- Program Global Area
	- PGA [12.2](tuning-system-global-area.md)
- program global area (PGA)
	- direct path read [10.3.5](instance-tuning-using-performance-views.md)
		- direct path write [10.3.6](instance-tuning-using-performance-views.md)
		- shared servers [14.4.1](tuning-shared-pool-and-large-pool.md)
- programming languages [2.5.6](designing-and-developing-for-performance.md)

---

## Q

- queries
	- data [2.4.2](designing-and-developing-for-performance.md)
- query optimizer [1.1.3.1](performance-tuning-overview.md)
	- See: optimizer

---

## R

- rdbms ipc reply wait events [10.3.18](instance-tuning-using-performance-views.md)
- read consistency [10.2.4](instance-tuning-using-performance-views.md)
- read wait events
	- direct path [10.3.5](instance-tuning-using-performance-views.md)
		- scattered [10.3.3](instance-tuning-using-performance-views.md)
- redo logs [4.1.3](configuring-database-for-performance.md)
	- buffer size [10.3.15](instance-tuning-using-performance-views.md)
		- mirroring [17.2.3.3](IO-configuration-and-design.md)
		- placement on disk [17.2.3.2](IO-configuration-and-design.md)
		- sizing [4.1.3](configuring-database-for-performance.md)
- reducing
	- contention with dispatchers [4.3.1](configuring-database-for-performance.md)
		- paging and swapping [12.3.4.1](tuning-system-global-area.md)
- RELEASE\_CURSOR clause [14.2.6.2](tuning-shared-pool-and-large-pool.md)
- Remote Management Framework (RMF) [6.2.8.1](gathering-database-statistics.md)
- resources
	- allocation [2.4.1.2](designing-and-developing-for-performance.md), [2.5.6](designing-and-developing-for-performance.md)
		- bottlenecks [10.3.19](instance-tuning-using-performance-views.md)
		- wait events [10.3.4](instance-tuning-using-performance-views.md)
- response time [2.4.2](designing-and-developing-for-performance.md)
- reverse key indexes [2.5.3.2](designing-and-developing-for-performance.md)
- RMF [6.2.8.1](gathering-database-statistics.md)
- rollout strategies
	- big bang approach [2.7.1](designing-and-developing-for-performance.md)
		- trickle approach [2.7.1](designing-and-developing-for-performance.md)

---

## S

- scalability [2.3.1](designing-and-developing-for-performance.md)
	- factors preventing [2.3.3](designing-and-developing-for-performance.md)
		- Internet [2.3.2](designing-and-developing-for-performance.md)
		- linear [2.3.3](designing-and-developing-for-performance.md)
- scattered read wait events [10.3.3](instance-tuning-using-performance-views.md)
	- actions [10.3.3](instance-tuning-using-performance-views.md)
- segment-level statistics [10.1.3.5](instance-tuning-using-performance-views.md)
- selectivity
	- ordering columns in an index [2.5.3.5](designing-and-developing-for-performance.md)
- sequential read wait events
	- actions [10.3.4](instance-tuning-using-performance-views.md)
- service hours [2.4.2](designing-and-developing-for-performance.md)
- session memory statistic [14.4.3](tuning-shared-pool-and-large-pool.md)
- SGA\_TARGET initialization parameter
	- automatic memory management [12.1](tuning-system-global-area.md)
- SHARED\_POOL\_SIZE initialization parameter [14.3.1.4](tuning-shared-pool-and-large-pool.md), [14.3.1.5](tuning-shared-pool-and-large-pool.md)
- shared pool contention [10.3.11](instance-tuning-using-performance-views.md)
- shared server
	- performance issues [4.3](configuring-database-for-performance.md)
		- reducing contention [4.3](configuring-database-for-performance.md)
		- tuning [4.3](configuring-database-for-performance.md)
		- tuning memory [14.4.1](tuning-shared-pool-and-large-pool.md)
- SHOW SGA statement [12.3.4.2.1](tuning-system-global-area.md)
- sizing redo logs [4.1.3](configuring-database-for-performance.md)
- snapshots
	- about [6.1.2](gathering-database-statistics.md)
- soft parsing [2.5.5](designing-and-developing-for-performance.md)
- software
	- components [2.4.1.2](designing-and-developing-for-performance.md)
- sort areas
	- tuning [16.1.1](tuning-program-global-area.md)
- SQL\*Net
	- message from client idle events [10.3.19](instance-tuning-using-performance-views.md)
		- message from dblink wait events [10.3.19](instance-tuning-using-performance-views.md)
		- more data to client wait events [10.3.19](instance-tuning-using-performance-views.md)
- SQL statements
	- waiting for I/O [10.3.3](instance-tuning-using-performance-views.md)
- SQL Tuning Advisor [1.2.1](performance-tuning-overview.md)
- statistics
	- baselines [6.1](gathering-database-statistics.md)
		- consistent gets from cache [13.2.2](tuning-database-buffer-cache.md)
		- databases [5.1](measuring-database-performance.md)
		- db block gets from cache [13.2.2](tuning-database-buffer-cache.md)
		- dictionary cache [8.3.2.14](comparing-database-performance-over-time.md)
		- gathering [5.1](measuring-database-performance.md)
		- I/O [8.3.2.7](comparing-database-performance-over-time.md)
		- instance activity [8.3.2.6](comparing-database-performance-over-time.md)
		- latch [8.3.2.11](comparing-database-performance-over-time.md)
		- library cache [8.3.2.15](comparing-database-performance-over-time.md)
		- max session memory [14.4.3](tuning-shared-pool-and-large-pool.md)
		- memory [8.3.2.16](comparing-database-performance-over-time.md)
		- operating system
		- comparing [8.3.2.2](comparing-database-performance-over-time.md)
		- PGA memory [8.3.2.8](comparing-database-performance-over-time.md)
		- physical reads from cache [13.2.2](tuning-database-buffer-cache.md)
		- segment [8.3.2.12](comparing-database-performance-over-time.md), [8.3.2.13](comparing-database-performance-over-time.md)
		- segment-level [10.1.3.5](instance-tuning-using-performance-views.md)
		- service [8.3.2.4](comparing-database-performance-over-time.md)
		- session memory [14.4.3](tuning-shared-pool-and-large-pool.md)
		- shared server processes [4.3.2](configuring-database-for-performance.md)
		- SQL [8.3.2.5](comparing-database-performance-over-time.md)
		- time model [5.1.1](measuring-database-performance.md), [8.3.2.1](comparing-database-performance-over-time.md)
		- undo [8.3.2.10](comparing-database-performance-over-time.md)
		- waits [8.3.2.9](comparing-database-performance-over-time.md)
- STREAMS\_POOL\_SIZE initialization parameter [12.3](tuning-system-global-area.md)
- striping
	- manual [17.2.2](IO-configuration-and-design.md)
- swapping [18.4.1.1.1](managing-operating-system-resources.md), [18.4.1.2](managing-operating-system-resources.md)
	- reducing [12.3.4.1](tuning-system-global-area.md)
- switching processes [18.4.1.4.1](managing-operating-system-resources.md)
- system architecture [2.4](designing-and-developing-for-performance.md)
	- configuration [2.4.2](designing-and-developing-for-performance.md)
		- hardware components [2.4.1.1](designing-and-developing-for-performance.md)
		- CPUs [2.4.1.1](designing-and-developing-for-performance.md)
				- I/O subsystems [2.4.1.1](designing-and-developing-for-performance.md)
				- memory [2.4.1.1](designing-and-developing-for-performance.md)
				- networks [2.4.1.1](designing-and-developing-for-performance.md)
		- software components [2.4.1.2](designing-and-developing-for-performance.md)
		- business logic [2.4.1.2](designing-and-developing-for-performance.md)
				- data and transactions [2.4.1.2](designing-and-developing-for-performance.md)
				- resources for managing user requests [2.4.1.2](designing-and-developing-for-performance.md)
				- user interface [2.4.1.2](designing-and-developing-for-performance.md)
- System Global Area tuning [12.3.4.2](tuning-system-global-area.md)

---

## T

- tables
	- creating [4.2](configuring-database-for-performance.md)
		- design [2.5.3](designing-and-developing-for-performance.md)
		- placement on disk [17.2.2](IO-configuration-and-design.md)
		- setting storage options [4.2](configuring-database-for-performance.md)
- tablespaces [4.1.4](configuring-database-for-performance.md)
	- creating [4.1.4](configuring-database-for-performance.md)
		- temporary [4.1.4](configuring-database-for-performance.md)
- temporary tablespaces [4.1.4](configuring-database-for-performance.md)
	- creating [4.1.4](configuring-database-for-performance.md)
- testing designs [2.6.4](designing-and-developing-for-performance.md)
- thrashing [18.4.1.2](managing-operating-system-resources.md)
- time model statistics [5.1.1](measuring-database-performance.md)
	- comparing [8.3.2.1](comparing-database-performance-over-time.md)
- Top Java
	- Active Session History report [9.3.5](analyzing-sampled-data.md)
- top PL/SQL
	- Active Session History report [9.3.4](analyzing-sampled-data.md)
- Top Sessions
	- Active Session History report [9.3.6](analyzing-sampled-data.md)
- Top SQL
	- Active Session History report [9.3.3](analyzing-sampled-data.md)
- transactions and data [2.4.1.2](designing-and-developing-for-performance.md)
- trickle rollout strategy [2.7.1](designing-and-developing-for-performance.md)
- tuning
	- and bottleneck elimination [1.1.2.4.2](performance-tuning-overview.md)
		- and proactive monitoring [1.1.2.4.1](performance-tuning-overview.md)
		- latches [1.1.2.3](performance-tuning-overview.md), [10.3.11](instance-tuning-using-performance-views.md)
		- resource contention [10](instance-tuning-using-performance-views.md)
		- shared server [4.3](configuring-database-for-performance.md)
		- sorts [16.1.1](tuning-program-global-area.md)
		- System Global Area (SGA) [12.3.4.2](tuning-system-global-area.md)

---

## U

- undo management, automatic mode [4.1.2](configuring-database-for-performance.md)
- UNIX system performance [18.2.1](managing-operating-system-resources.md)
- user global area (UGA)
	- shared servers [4.3](configuring-database-for-performance.md), [14.4.1](tuning-shared-pool-and-large-pool.md)
- user interface [2.4.1.2](designing-and-developing-for-performance.md)
- users
	- interaction method [2.4.2](designing-and-developing-for-performance.md)
		- interfaces [2.5.6](designing-and-developing-for-performance.md)
		- location [2.4.2](designing-and-developing-for-performance.md)
		- network speed [2.4.2](designing-and-developing-for-performance.md)
		- number of [2.4.2](designing-and-developing-for-performance.md)
		- requests [2.5.6](designing-and-developing-for-performance.md)
		- response time [2.4.2](designing-and-developing-for-performance.md)

---

## V

- V$ACTIVE\_SESSION\_HISTORY view [10.1.3.3](instance-tuning-using-performance-views.md)
- V$BUFFER\_POOL\_STATISTICS view [13.3.4](tuning-database-buffer-cache.md)
- V$DB\_CACHE\_ADVICE view [13.2.1](tuning-database-buffer-cache.md)
- V$EVENT\_HISTOGRAM view [10.1.3.3](instance-tuning-using-performance-views.md)
- V$FILE\_HISTOGRAM view [10.1.3.3](instance-tuning-using-performance-views.md)
- V$JAVA\_LIBRARY\_CACHE\_MEMORY view [14.3.1.2.3](tuning-shared-pool-and-large-pool.md)
- V$JAVA\_POOL\_ADVICE view [14.3.1.2.3](tuning-shared-pool-and-large-pool.md)
- V$LIBRARY\_CACHE\_MEMORY view [14.3.1.2.2](tuning-shared-pool-and-large-pool.md)
- V$LIBRARYCACHE view
	- NAMESPACE column [14.3.1.1.1](tuning-shared-pool-and-large-pool.md)
- V$QUEUE view [4.3.2](configuring-database-for-performance.md)
- V$ROWCACHE view
	- performance statistics [14.3.1.3](tuning-shared-pool-and-large-pool.md)
- V$SESSION\_EVENT view [10.1.3.3](instance-tuning-using-performance-views.md)
- V$SESSION\_WAIT\_CLASS view [10.1.3.3](instance-tuning-using-performance-views.md)
- V$SESSION\_WAIT\_HISTORY view [10.1.3.3](instance-tuning-using-performance-views.md)
- V$SESSION\_WAIT view [10.1.3.3](instance-tuning-using-performance-views.md)
- V$SESSION view [10.1.3.3](instance-tuning-using-performance-views.md), [10.1.3.4](instance-tuning-using-performance-views.md)
- V$SESSTAT view [14.4.3](tuning-shared-pool-and-large-pool.md)
- V$SHARED\_POOL\_ADVICE view [14.3.1.2.1](tuning-shared-pool-and-large-pool.md)
- V$SHARED\_POOL\_RESERVED view [14.3.6.1](tuning-shared-pool-and-large-pool.md)
- V$SYSSTAT view
	- redo buffer allocation [13.4.2](tuning-database-buffer-cache.md)
		- using [13.2.2](tuning-database-buffer-cache.md)
- V$SYSTEM\_EVENT view [10.1.3.3](instance-tuning-using-performance-views.md)
- V$SYSTEM\_WAIT\_CLASS view [10.1.3.3](instance-tuning-using-performance-views.md)
- V$TEMP\_HISTOGRAM view [10.1.3.3](instance-tuning-using-performance-views.md)
- V$WAITSTAT view [10.1.3.4](instance-tuning-using-performance-views.md)
- validating designs [2.6.4](designing-and-developing-for-performance.md)
- views [2.5.4](designing-and-developing-for-performance.md)
- vmstat UNIX command [18.4.1.1.1](managing-operating-system-resources.md)

---

## W

- wait events [5.1.3](measuring-database-performance.md)
	- buffer busy waits [10.3.2](instance-tuning-using-performance-views.md)
		- classes [5.1.3](measuring-database-performance.md), [10.1.3.2](instance-tuning-using-performance-views.md)
		- comparing [8.3.2.3](comparing-database-performance-over-time.md)
		- direct path [10.3.6](instance-tuning-using-performance-views.md)
		- enqueue [10.3.7](instance-tuning-using-performance-views.md)
		- free buffer waits [10.3.9](instance-tuning-using-performance-views.md)
		- idle wait events [10.3.10](instance-tuning-using-performance-views.md)
		- latch [10.3.11](instance-tuning-using-performance-views.md)
		- library cache latch [10.3.11](instance-tuning-using-performance-views.md)
		- log buffer space [10.3.15](instance-tuning-using-performance-views.md)
		- log file parallel write [10.3.12](instance-tuning-using-performance-views.md)
		- log file switch [10.3.16](instance-tuning-using-performance-views.md)
		- log file sync [10.3.17](instance-tuning-using-performance-views.md)
		- network communication wait events [10.3.19](instance-tuning-using-performance-views.md)
		- rdbms ipc reply [10.3.18](instance-tuning-using-performance-views.md)
		- resource wait events [10.3.4](instance-tuning-using-performance-views.md)
- Windows performance [18.2.2](managing-operating-system-resources.md)
- workloads [2.6.2](designing-and-developing-for-performance.md), [2.6.3](designing-and-developing-for-performance.md), [2.6.4](designing-and-developing-for-performance.md)