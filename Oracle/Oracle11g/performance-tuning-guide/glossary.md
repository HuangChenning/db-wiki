---
title: Glossary
book: Performance Tuning Guide
doc_id: E41573-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41573/glossary.htm
tags:
  - oracle
  - 11g
  - performance-tuning-guide
---

access path

The means by which data is retrieved from a database. For example, a query using an index and a query using a full table scan use different access paths.

asynchronous I/O

Independent I/O, in which there is no timing requirement for transmission, and other processes can start before the transmission has finished.

Automatic Workload Repository

Collects, processes, and maintains performance statistics for problem detection and self-tuning purposes.

Autotrace

Generates a report on the execution path used by the SQL optimizer and the statement execution statistics. The report is useful to monitor and tune the performance of DML statements.

bind variable

A variable in a SQL statement that must be replaced with a valid value, or the address of a value, in order for the statement to successfully execute.

block

A unit of data transfer between main memory and disk. Many blocks from one section of memory address space form a segment.

bottleneck

The delay in transmission of data, typically when a system's bandwidth cannot support the amount of information being relayed at the speed it is being processed. However, many factors can create a bottleneck in a system.

buffer

A main memory address where the buffer manager caches currently and recently used data read from disk. Over time, a buffer can hold different blocks. When a new block is needed, the buffer manager can discard an old block and replace it with a new one.

buffer pool

A collection of buffers.

cache

Also known as buffer cache. All buffers and buffer pools.

cache recovery

The part of instance recovery where Oracle Database applies all committed and uncommitted changes in the redo log files to the affected data blocks. Also known as the rolling forward phase of instance recovery.

Cartesian product

A join with no join condition results in a Cartesian product, or a cross product. A Cartesian product is the set of all possible combinations of rows drawn one from each table. Thus, for a join of two tables, each row in one table is matched in turn with every row in the other. A Cartesian product for more than two tables is the result of pairing each row of one table with every row of the Cartesian product of the remaining tables. All other types of joins are subsets of Cartesian products effectively created by deriving the product and then excluding rows that fail the join condition.

compound query

A query that uses set operators (`UNION`, `UNION` `ALL`, `INTERSECT`, or `MINUS`) to combine two or more simple or complex statements. Each simple or complex statement in a compound query is called a component query.

contention

When some process has to wait for a resource that another process is using.

dictionary cache

A collection of database tables and views containing reference information about the database, its structures, and its users. Oracle Database accesses the data dictionary frequently during the parsing of SQL statements. Two special locations in memory are designated to hold dictionary data. One area is called the data dictionary cache, also known as the row cache because it holds data as rows instead of buffers (which hold entire blocks of data). The other area is the library cache. All Oracle processes share these two caches for access to data dictionary information.

direct I/O

I/O which bypasses the buffer cache. See "PIO".

distributed statement

A statement that accesses data on two or more distinct nodes/instances of a distributed database. A remote statement accesses data on one remote node of a distributed database.

dynamic performance views

The views database administrators create on dynamic performance tables (virtual tables that record current database activity). Dynamic performance views are called fixed views because they cannot be altered or removed by the database administrator.

dynamic statistics

An optimization technique in which the database executes a recursive SQL statement to scan a small random sample of a table's blocks to estimate predicate selectivities.

enqueue

This is another term for a lock.

equijoin

A join condition containing an equality operator.

estimator

Uses statistics to estimate the selectivity, cardinality, and cost of execution plans. The main goal of the estimator is to estimate the overall cost of an execution plan.

execution plan

The combination of steps used by the database to execute a SQL statement. Each step either retrieves rows of data physically from the database or prepares them for the user issuing the statement. You can override execution plans by using hints.

EXPLAIN PLAN

A SQL statement that enables examination of the execution plan chosen by the optimizer for DML statements. `EXPLAIN` `PLAN` causes the optimizer to choose an execution plan and then to put data describing the plan into a database table.

fast full index scan

A full index scan in which the database reads the index blocks in no particular order. The database accesses the data in the index itself, without accessing the table.

full index scan

A scan of an index in which the database reads the entire index in order.

full table scan

A scan of table data in which the database sequentially reads all rows from a table and filters out those that do not meet the selection criteria. During full table scans the database scans all data blocks under the high water mark.

hash join

A join in which the database uses the smaller of two tables or data sources to build a hash table in memory. In hash joins, the database scans the larger table, probing the hash table for the addresses of the matching rows in the smaller table.

hint

An instruction passed to the optimizer through comments in a SQL statement. The optimizer uses hints to choose an execution plan for the statement.

index clustering factor

A measure of the row order in relation to an indexed value such as last name. The more order that exists in row storage for this value, the lower the clustering factor.

instance recovery

The automatic application of redo log records to data blocks after a database failure.

join

A query that selects data from multiple tables. A join is characterized by multiple tables in the `FROM` clause. Oracle Database pairs the rows from these tables using the condition specified in the `WHERE` clause and returns the resulting rows. This condition is called the join condition and usually compares columns of all the joined tables.

latch

A simple, low-level serialization mechanism to protect shared data structures in the System Global Area.

library cache

A memory structure containing shared SQL and PL/SQL areas. The library cache is one of three parts of the shared pool.

LIO

Logical I/O. A block read which may or may not be satisfied from the buffer cache.

literal

A constant value, written at compile-time and read-only at run-time. The database can access literals quickly and uses them when modification is not necessary.

mirroring

Maintaining identical copies of data on one or more disks. Typically, mirroring occurs on duplicate hard disks at the operating system level, so that if one disk becomes unavailable, the other disk can service requests without interruptions.

MTBF

Mean time between failures. A common database statistic important to tuning I/O.

nonequijoin

A join condition containing something other than an equality operator.

optimizer

Built-in database software that determines the most efficient way to execute a SQL statement. The query optimizer is made up of the query transformer, the estimator, and the plan generator.

The optimizer generates a set of potential execution plans for SQL statements, estimates the cost of each plan, calls the plan generator to generate the plan, compares the costs, and chooses the plan with the lowest cost. The database uses this approach when the data dictionary has statistics for at least one of the tables accessed by the SQL statements.

optimizer mode

The optimizer operates in either normal mode or tuning mode. In normal mode, the optimizer compiles the SQL and generates an execution plan. In tuning mode, the optimizer performs additional analysis and generates a series of actions, along with their rationale and expected benefit for producing a significantly better plan. When running in tuning mode, the optimizer is known as the Automatic Tuning Optimizer.

outer join

A join condition using the outer join operator (`+`) with one or more columns of one of the tables. Oracle Database returns all rows that meet the join condition. Oracle Database also returns all rows from the table without the outer join operator for which there are no matching rows in the table with the outer join operator.

paging

A technique for increasing the memory space available by moving infrequently-used parts of a program's working memory from main memory to a secondary storage medium, usually a disk. The unit of transfer is called a page.

parse

A hard parse occurs when a SQL statement is executed, and the SQL statement is either not in the shared pool, or it is in the shared pool but it cannot be shared. A SQL statement is not shared if the metadata for the two SQL statements is different. This can happen if a SQL statement is textually identical as a preexisting SQL statement, but the tables referred to in the two statements resolve to physically different tables, or if the optimizer environment is different.

A soft parse occurs when a session attempts to execute a SQL statement, and the statement is in the shared pool, and it can be used (that is, shared). For a statement to be shared, all data, (including metadata, such as the optimizer execution plan) pertaining to the existing SQL statement must be equally applicable to the current statement being issued.

parse call

A call to Oracle Database to prepare a SQL statement for execution. This includes syntactically checking the SQL statement, optimizing it, and building (or locating) an executable form of that statement.

parser

Performs syntax analysis and semantic analysis of SQL statements, and expands views (referenced in a query) into separate query blocks.

PGA

Program Global Area. A nonshared memory region that contains data and control information for a server process, created when the server process is started.

PIO

Physical I/O. A block read which could not be satisfied from the buffer cache, either because the block was not present or because the I/O is a direct I/O which bypasses the buffer cache.

plan generator

Tries out different possible plans for a given query so that the query optimizer can choose the plan with the lowest cost. It explores different plans for a query block by trying out different access paths, join methods, and join orders.

predicate

A `WHERE` condition in SQL.

query optimizer

See optimizer.

query transformer

Decides whether to rewrite a user query to generate a better query plan, merges views, and performs subquery unnesting.

RAID

Redundant arrays of inexpensive disks. RAID configurations provide improved data reliability with the option of striping (manually distributing data). Different RAID configurations (levels) are chosen based on performance and cost, and are suited to different types of applications, depending on their I/O characteristics.

row source generator

Receives the optimal plan from the optimizer and outputs the execution plan for the SQL statement. A row source is an iterative control structure that processes a set of rows in an iterated manner and produces a row set.

segment

A set of extents allocated for a specific type of database object, such as a table, index, or cluster.

selectivity

In a query, the measure of how many rows from a row set pass a predicate test, for example, `WHERE last_name = 'Smith'`.

simple query

A `SELECT` statement that references only one table and does not make reference to `GROUP` `BY` functions.

simple statement

An `INSERT`, `UPDATE`, `DELETE`, or `SELECT` statement that involves only a single table.

SGA

System Global Area. A memory region within main memory used to store data for fast access. Oracle database uses the shared pool to allocate SGA memory for shared SQL and PL/SQL procedures.

skewed data

Values with large variations in the number of duplicates.

SQL Compiler

Compiles SQL statements into a shared cursor. The SQL Compiler is made up of the parser, the optimizer, and the row source generator.

SQL profile

A collection of information that enables the query optimizer to create an optimal execution plan for a SQL statement.

SQL statements (identical)

Textually identical SQL statements do not differ in any way.

SQL statements (similar)

Similar SQL statements differ only due to changing literal values. If literal values were replaced with bind variables, then the SQL statements would be textually identical.

SQL Trace

A basic performance diagnostic tool to help monitor and tune applications running against the Oracle database. SQL Trace lets you assess the efficiency of the SQL statements an application runs and generates statistics for each statement. The trace files produced by this tool serve as input for `TKPROF`.

SQL tuning set (STS)

A database object that includes one or more SQL statements along with their execution statistics and execution context.

SQL\*Loader

Reads and interprets input files. Use this tool to load large amounts of data.

Statspack

A set of SQL, PL/SQL, and SQL\*Plus scripts that allow the collection, automation, storage, and viewing of performance data. This feature has been replaced by the Automatic Workload Repository.

striping

The interleaving of a related block of data across disks. Proper striping reduces I/O and improves performance.

- Stripe depth is the size of the stripe, sometimes called stripe unit.
- Stripe width is the product of the stripe depth and the number of drives in the striped set.

TKPROF

A diagnostic tool to help monitor and tune applications running against the Oracle database. `TKPROF` primarily processes SQL trace output files and translates them into readable output files, providing a summary of user-level statements and recursive SQL calls for the trace files. It can also assess the efficiency of SQL statements, generate execution plans, and create SQL scripts to store statistics in the database.

transaction recovery

The part of instance recovery where Oracle Database applies the rollback segments to undo the uncommitted changes. Also known as the rolling back phase of instance recovery.

UGA

User Global Area. A memory region in the large pool used for user sessions.

wait events

Statistics that are incremented by a server process/thread to indicate that it had to wait for an event to complete before being able to continue processing. Wait events are one of the first places for investigation when performing reactive performance tuning.

wait events (idle)

These events indicate that the server process is idle and waiting for work. Ignore these events when tuning because they do not indicate the nature of the performance bottleneck.

work area

A private allocation of memory used for sorts, hash joins, and other operations that are memory-intensive. A sort operator uses a work area (the sort area) to perform the in-memory sort of a set of rows. Similarly, a hash-join operator uses a work area (the hash area) to build a hash table from its left input.