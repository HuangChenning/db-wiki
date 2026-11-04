---
title: Database Performance Tuning Guide
book: Database Performance Tuning Guide
doc_id: F32091-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/tgdba/glossary.html
tags:
  - oracle
  - 21c
  - performance-tuning-guide
---

### ADO policy

A policy that specifies a rule and condition for Automatic Data Optimization (ADO). For example, an ADO policy may specify that an object is marked `NOINMEMORY` (action) 30 days after creation (condition). Specify ADO policies using the `ILM` clause of `CREATE TABLE` and `ALTER TABLE` statements.

### Automatic Data Optimization (ADO)

A technology that creates policies, and automates actions based on those policies, to implement an Information Lifecycle Management (ILM) strategy.

### Automatic In-Memory

A feature that automatically evicts cold (infrequently accessed) segments from the IM column store to ensure that the working data set is always populated.

### availability

The degree to which an application, service, or function is accessible on demand.

### Bloom filter

A low-memory data structure that tests membership in a set. The database uses Bloom filters to improve the performance of hash joins.

### Column Compression Unit (CU)

Contiguous storage for a column in an In-Memory Compression Unit (IMCU).

### columnar data pool

The subpool in the In-Memory Area that stores columnar data. It is also known as the 1 MB pool.

### columnar format

The column-based format for objects that reside in the In-Memory Column Store. The columnar format contrasts with the row format used in data blocks.

### common dictionary

A segment-level, instance-specific set of master dictionary codes, created from local dictionaries. A local dictionary is a sorted list of dictionary codes specific to a Column Compression Unit (CU). A join group uses a common dictionary to optimize joins.

### compression tiering

The application of different levels of compression to data based on its access pattern. For example, administrators may compress inactive data at a higher rate of compression at the cost of slower access.

### data flow operator (DFO)

The unit of work between data redistribution stages in a parallel query.

### database buffer cache

The portion of the system global area (SGA) that holds copies of data blocks. All client processes concurrently connected to the database instance share access to the buffer cache.

### database instance

The combination of the system global area (SGA) and background processes. An instance is associated with one and only one database. Every database instance is either a read/write database instance or a read-only database instance. In an Oracle Real Application Clusters configuration, multiple instances access a single database.

### dense grouping key

A key that represents all grouping keys whose grouping columns come from a specific fact table or dimension.

### dense join key

A key that represents all join keys whose join columns come from a particular fact table or dimension.

### dense key

A numeric key that is stored as a native integer and has a range of values.

### double buffering

A repopulation mechanism in which background processes create new In-Memory Compression Unit (IMCU) versions by combining the original rows with the latest modified rows. During repopulation, the stale IMCUs remain accessible for queries.

### expression

A combination of one or more values, operators, and SQL functions that resolves to a value.

### expression capture interval

The time interval within which the database considers IM expressions for possible capture.

### expression capture window

An expression capture interval defined by invocation of the `IME_OPEN_CAPTURE_WINDOW` and `IME_OPEN_CAPTURE_WINDOW` procedures in the `DBMS_INMEMORY_ADMIN` package.

### Expression Statistics Store (ESS)

A repository maintained by the optimizer to store statistics about expression evaluation. For each segment, the ESS monitors statistics such as frequency of execution, cost of evaluation, timestamp evaluation, and so on. The ESS is persistent in nature and has an SGA representation for fast lookup of expressions.

### Heat Map

Heat Map shows the popularity of data blocks and rows. Automatic Data Optimization (ADO) to decide which segments are candidates for movement to a different storage tier.

### home location

The database instance in which an IMCU resides. When auto DOP is enabled on Oracle RAC, the parallel query coordinator uses home location to determine where each IMCU is located, how large it is, and so on.

### In-Memory hybrid scan

A query that scans both the IM column store and the row store. The optimizer considers an In-Memory hybrid scan automatically when all predicate columns have the `INMEMORY` attribute, and some columns in the `SELECT` list do not have the `INMEMORY` attribute.

### hybrid partitioned table

A table in which some partitions are stored in data file segments and some are stored in external data source.

### IM aggregation

An optimization that accelerates aggregation for queries that join from a single large table to multiple small tables. The transformation uses `KEY VECTOR` and `VECTOR GROUP BY` operators, which is why it is also known as `VECTOR GROUP BY` aggregation.

### IM column store

An optional SGA area that stores copies of tables and partitions in a columnar format optimized for rapid scans.

### IM dynamic scan

The use of lightweight threads to automatically parallelize In-Memory table scans.

### IM expression

A SQL expression whose results are stored in the In-Memory Column Store. If `last_name` is a column stored in the IM column store, then an IM expression might be `UPPER(last_name)`.

### IMCU mirroring

In Oracle RAC, the duplication of an IMCU in multiple IM column stores. For example, the IM column stores on instance 1 and instance 2 are populated with the same `sales` table.

### IMCU pruning

In a query of the In-Memory Column Store, the elimination of IMCUs based on the high and low values in each IMCU. For example, if a statements filters product IDs greater than 100, then the database avoids scanning IMCUs that contain values less than 100.

### IM storage index

A data structure in an IMCU header that stores the minimum and maximum for all columns within the IMCU.

### In-Memory Advisor

A downloadable PL/SQL package that analyzes the analytical processing workload in your database. This advisor recommends a size for the IM column store and a list of objects that would benefit from In-Memory population.

### In-Memory Aggregation

See IM aggregation.

### In-Memory Area

An optional SGA component that contains the IM column store.

### In-Memory Column Store

See IM column store.

### In-Memory Compression Unit (IMCU)

A storage unit in the In-Memory Column Store that is optimized for faster scans. The In-Memory Column Store stores each column in table separately and compresses it. Each IMCU contains all columns for a subset of rows in a specific table segment.

A one-to-many mapping exists between an IMCU and a set of database blocks. For example, if a table contains columns `c1` and `c2`, and if its rows are stored in 100 database blocks on disk, then IMCU 1 might store the values for both columns for blocks 1-50, and IMCU 2 might store the values for both columns for blocks 51-100.

### In-Memory Coordinator Process (IMCO)

A background process whose primary task is to initiate background population and repopulation of columnar data.

### In-Memory Dynamic Scan

See IM dynamic scan.

### In-Memory Expression

See IM expression.

### In-Memory Expression Unit (IMEU)

A container that stores the computed result of an In-Memory Expression (IM expression). Each IMEU is linked to its own parent In-Memory Compression Unit (IMCU).

### In-Memory FastStart

A feature that significantly reduces the time to populate data into the IM column store when a database instance restarts.

### In-Memory population

See population.

### In-Memory virtual column

A virtual column that is eligible to be populated in the In-Memory Column Store.

### Information Lifecycle Management (ILM)

A set of processes and policies for managing data throughout its useful life.

### join group

A user-defined object that specifies frequently joined columns from the same table or different tables. External tables are not supported.

A typical join group candidate is a set of columns used to join fact and dimension tables. Join groups are only supported when `INMEMORY_SIZE` is a nonzero value.

### key vector

A data structure that maps between dense join keys and dense grouping keys.

### large pool

Optional area in the SGA that provides large memory allocations for backup and restore operations, I/O server processes, and session memory for the [shared server](unresolvable-reference.md) and [Oracle XA](unresolvable-reference.md).

### local dictionary

A sorted list of dictionary codes specific to a Column Compression Unit (CU).

### lightweight thread

An execution entity used in an In-Memory Dynamic Scan. Lightweight threads help to parallelize scans of IMCUs.

### metadata pool

A subpool of the In-Memory Area that stores metadata about the objects that reside in the IM column store. The metadata pool is also known as the 64 KB pool.

### memoptimize pool

An SGA pool that stores buffers and related structures for heap-organized tables specified as `MEMOPTIMIZE FOR READ`.

### on-demand population

When `INMEMORY PRIORITY` is set to `NONE`, the IM column store only populates the object when it is accessed through a full scan. If the object is never accessed, or if it is accessed only through an index scan or fetch by rowid, then it is never populated.

### OSON

Oracle's optimized binary JSON format. OSON enables fast queries and updates of the JSON data model in Oracle database server and Oracle database clients.

### OZIP

A proprietary compression technique that offers extremely fast decompression. OZIP is tuned specifically for Oracle Database.

### partition exchange load

A technique in which you create a table, load data into it, and then exchange an existing table partition with the table. This exchange process is a DDL operation with no actual data movement.

### population

The operation of reading existing data blocks from data files, transforming the rows into columnar format, and then writing the columnar data to the IM column store. In contrast, loading refers to bringing new data into the database using DML or DDL.

### priority-based population

When `PRIORITY` is set to a value other than `NONE`, Oracle Database adds the object to a prioritized population queue. The database populates objects based on their queue position, from `CRITICAL` to `LOW`. It is “priority-based” because the IM column store automatically populates objects using the prioritized list whenever the database re-opens. Unlike in on-demand population, objects do not require a full scan to be populated.

### read-only database instance

A database instance that cannot process DML and does not support client connections.

### read/write database instance

A database instance that can process DML and supports direct client connections. By default, a database instance is read/write.

### repopulation

The automatic refresh of a currently populated In-Memory Compression Unit (IMCU) after its data has been significantly modified. In contrast, population is the initial creation of IMCUs in the IM column store.

### service

The logical representation of an application workload that shares common attributes, performance thresholds, and priorities. A single service can be associated with one or more instances of an Oracle RAC database, and a single instance can support multiple services.

### SGA

System global area. A group of shared memory structures that contain data and control information for one Oracle database instance.

### SIMD

Single Instruction, Multiple Data. An instruction that processes data as a single unit, called a **vector**, rather than as separate instructions. SIMD processing is known as **vectorization**.

### Snapshot Metadata Unit (SMU)

A storage unit in the In-Memory Area that contains metadata and transactional information for an associated In-Memory Compression Unit (IMCU).

### Space Management Worker Process (Wnnn)

A process that populates or repopulates data in the IM column store on behalf of In-Memory Coordinator Process (IMCO).

### staleness threshold

An internally set percentage of entries in the transaction journal for an IMCU that initiates repopulation.

### storage tiering

The deployment of data on different tiers of storage depending on its level of access. For example, administrators migrate inactive data from high-performance, high-cost storage to low-cost storage.

### system global area (SGA)

See SGA.

### table scan process

A foreground or PQ process that coordinates an IM dynamic scan.

### threshold-based repopulation

The automatic repopulation of an IMCU when the number of stale entries in an IMCU reaches an internal staleness threshold.

### transaction journal

Metadata in a Snapshot Metadata Unit (SMU) that keeps the IM column store transactionally consistent.

### trickle repopulation

A supplement to threshold-based repopulation. The In-Memory Coordinator Process (IMCO) may instigate trickle repopulation automatically for any IMCU in the IM column store that has stale entries but does not meet the staleness threshold.

### vector aggregation

See IM aggregation.

### virtual column

A column that is not stored on disk. The database derives the values in virtual columns on demand by computing a set of expressions or functions.

### working data set

The subset of `INMEMORY` objects that is actively queried at a given time. Typically, the work working data set changes over time.