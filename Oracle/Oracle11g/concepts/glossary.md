---
title: Glossary
book: Concepts
doc_id: E40540-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40540/glossary.htm
tags:
  - oracle
  - 11g
  - concepts
---

access driver

In the external table infrastructure, the API that interprets the external data for the database. The access driver runs inside the database, which uses the driver to read the data in the external table.

access path

The means by which data is retrieved from a database. For example, a query using an index and a query using a full table scan use different access paths.

active transaction

A transaction that has started but not yet committed or rolled back.

ADDM

Automatic Database Diagnostic Monitor. An Oracle Database infrastructure that enables a database to diagnose its own performance and determine how identified problems could be resolved.

ADR

Automatic Diagnostic Repository. A a file-based hierarchical data store for managing diagnostic information, including network tracing and logging.

alert log

A file that provides a chronological log of database messages and errors. The alert log is stored in the ADR.

antijoin

A join that returns rows from the left side of the predicate for which there are no corresponding rows on the right side of the predicate.

application architecture

The computing environment in which a database application connects to an Oracle database. The two most common database architectures are client/server and multitier.

application domain index

A customized index specific to an application.

archived redo log file

A member of the online redo log that has been archived by Oracle Database. The archived redo log files can be applied to a database backup in media recovery.

ARCHIVELOG mode

A mode of the database that enables the archiving of the online redo log.

ascending index

An index in which data is stored in ascending order. By default, character data is ordered by the binary values contained in each byte of the value, numeric data from smallest to largest number, and date from earliest to latest value.

Automatic Database Diagnostic Monitor (ADDM)

See ADDM.

Automatic Diagnostic Repository (ADR)

See ADR.

automatic undo management mode

A mode of the database in which it automatically manages undo space in a dedicated undo tablespace.

See also manual undo management mode.

Automatic Workload Repository (AWR)

See AWR.

AWR

Automatic Workload Repository (AWR). A built-in repository in every Oracle database. Oracle Database periodically makes a snapshot of its vital statistics and workload information and stores them in AWR.

B-tree index

An index organized like an upside-down tree. A B-tree index has two types of blocks: branch blocks for searching and leaf blocks that store values. The leaf blocks contain every indexed data value and a corresponding rowid used to locate the actual row. The "B" stands for "balanced" because all leaf blocks automatically stay at the same depth.

background process

A process that consolidates functions that would otherwise be handled by multiple Oracle programs running for each client process. The background processes asynchronously perform I/O and monitor other Oracle processes.

See also instance; Oracle process.

bind variable

A placeholder in a SQL statement that must be replaced with a valid value or value address for the statement to execute successfully. By using bind variables, you can write a SQL statement that accepts inputs or parameters at run time. The following example shows a query that uses `v_empid` as a bind variable:

```
SELECT * FROM employees WHERE employee_id = :v_empid;
```

bitmap index

A database index in which the database stores a bitmap for each index key instead of a list of rowids.

bitmap join index

A bitmap index for the join of two or more tables.

bitmap merge

An operation that merges bitmaps retrieved from bitmap index scans. For example, if the `gender` and `DOB` columns have bitmap indexes, then the database may use a bitmap merge if the query predicate is `WHERE gender='F' AND DOB > 1966`.

block corruption

A data block that is not in a recognized Oracle format, or whose contents are not internally consistent.

block header

A part of a data block that includes information about the type of block, the address of the block, and sometimes transaction information.

block overhead

Space in a data block that stores metadata required for managing the block. The overhead includes the block header, table directory, and row directory.

branch block

In a B-tree index, a block that the database uses for searching. The leaf blocks store the index entries. The upper-level branch blocks of a B-tree index contain index data that points to lower-level index blocks.

buffer

A main memory address in the database buffer cache. A buffer caches currently and recently used data blocks read from disk. When a new block is needed, the database can replace an old data block with a new one.

byte semantics

Treatment of strings as a sequence of bytes. Offsets into strings and string lengths are expressed in bytes.

cache recovery

The phase of instance recovery where Oracle Database applies all committed and uncommitted changes in the online redo log files to the affected data blocks.

cardinality

The ratio of distinct values to the number of table rows. A column with only two distinct values in a million-row table would have low cardinality.

character encoding

A code that pairs each character from a given repertoire with a code unit to facilitate data storage.

character semantics

Treatment of strings as a sequence of characters. Offsets into strings and string lengths are expressed in characters (character codes).

character set

An encoding scheme used to display characters on your computer screen.

checkpoint

1\. A data structure that marks the checkpoint position, which is the SCN in the redo thread where database instance recovery must begin. Checkpoints are recorded in the control file and each data file header, and are a crucial element of recovery.

2\. The writing of dirty data blocks in the database buffer cache to disk. The database writer (DBW) process writes blocks to disk to synchronize the buffer cache with the data files.

client

In client/server architecture, the front-end database application that interacts with a user. The client portion has no data access responsibilities.

client process

A process that executes the application or Oracle tool code. When users run client applications such as SQL\*Plus, the operating system creates client processes to run the applications.

See also Oracle process.

client/server architecture

Software architecture based on a separation of processing between two CPUs, one acting as the client in the transaction, requesting and receiving services, and the other as the server that provides services in a transaction.

cluster file system

A distributed file system that is a cluster of servers that collaborate to provide high performance service to their clients.

cluster index

A B-tree index on the cluster key.

cluster key

In a table cluster, the column or columns that the clustered tables have in common. For example, the `employees` and `departments` tables share the `department_id` column. You specify the cluster key when creating the table cluster and when creating every table added to the table cluster.

column

Vertical space in a table that represents a domain of data. A table definition includes a table name and set of columns. Each column has a name and data type.

commit

Action that ends a database transaction and makes permanent all changes performed in the transaction.

composite index

An index on multiple columns in a table.

composite partitioning

In partitioning strategy in which a table is partitioned by one data distribution method and then each partition is further divided into subpartitions using a second data distribution method.

compression unit

In Hybrid Columnar Compression, a logical construct that stores a set of rows. When you load data into a table, the database stores groups of rows in columnar format, with the values for each column stored and compressed together. After the database has compressed the column data for a set of rows, the database fits the data into the compression unit.

concurrency

Simultaneous access of the same data by many users. A multiuser database management system must provide adequate concurrency controls so that data cannot be updated or changed improperly, compromising data integrity.

See also data consistency.

condition

The combination of one or more expressions and logical operators in a SQL statement that returns a value of `TRUE`, `FALSE`, or `UNKNOWN`. For example, the condition `1=1` always evaluates to `TRUE`.

connection

Communication pathway between a client process and an Oracle database instance.

See also session.

connection pooling

A resource utilization and user scalability feature that maximizes the number of sessions over a limited number of protocol connections to a shared server.

consistent backup

A whole database backup that you can open with the `RESETLOGS` option without performing media recovery. In other words, the backup does not require the application of redo to be made consistent.

See also inconsistent backup.

context

A set of application-defined attributes that validates and secures an application. The SQL statement `CREATE CONTEXT` creates namespaces for contexts.

control file

A binary file that records the physical structure of a database and contains the names and locations of redo log files, the time stamp of the database creation, the current log sequence number, checkpoint information, and so on.

cube

An organization of measures with identical dimensions and other shared characteristics. The edges of the cube contain the dimension members, whereas the body of the cube contains the data values.

cursor

A handle or name for a private SQL area in the PGA. Because cursors are closely associated with private SQL areas, the terms are sometimes used interchangeably.

database

Organized collection of data treated as a unit. The purpose of a database is to store and retrieve related information. Every Oracle database instance accesses only one database in its lifetime.

database access control

The restriction of data access and database activities. For example, a database administrator can restrict users from querying specified tables or executing specified database commands.

database application

A software program that interacts with a database to access and manipulate data.

database authentication

The process by which a user presents credentials to the database, which verifies the credentials and allows access to the database.

database buffer cache

The portion of the system global area (SGA) that holds copies of data blocks. All client processes concurrently connected to the instance share access to the buffer cache.

database instance

The combination of the system global area (SGA) and background processes. An instance is associated with one and only one database. In an Oracle Real Application Clusters configuration, multiple instances access a single database simultaneously.

database link

In a schema object, a schema object in one database that enables users to access objects on a different database.

database management system (DBMS)

Software that controls the storage, organization, and retrieval of data.

database object

An object in the database that can be manipulated with SQL. Schema objects such as tables and indexes reside in schemas. Nonschema objects such as directories and roles do not reside in schemas.

database security

The aspect of database administration that involves user authentication, encryption, access control, and monitoring.

database server

A server that reliably manages a large amount of data in a multiuser environment so that users can concurrently access the same data. A database server also prevents unauthorized access and provides efficient solutions for failure recovery.

database service

A named representation of one or more database instances. The service name for an Oracle database is normally its global database name. Clients use the service name to connect to one or more database instances.

database user

An account through which you can log in to an Oracle database.

database writer (DBW)

A background process that writes buffers in the database buffer cache to data files.

data block

Smallest logical unit of data storage in Oracle Database. Other names for data blocks include Oracle blocks or pages. One data block corresponds to a specific number of bytes of physical space on disk.

See also extent; segment.

data consistency

A consistent view of the data by each user in a multiuser database.

See also concurrency.

data corruption

An error that occurs when a hardware, software, or network component causes corrupt data to be read or written.

data dictionary

A read-only collection of database tables and views containing reference information about the database, its structures, and its users.

data dictionary cache

A memory area in the shared pool that holds data dictionary information. The data dictionary cache is also known as the row cache because it holds data as rows instead of buffers, which hold entire data blocks.

data dictionary view

A predefined view of tables or other views in the data dictionary. Data dictionary views begin with the prefix `DBA_`, `ALL_`, or `USER_`.

data file

A physical file on disk that was created by Oracle Database and contains the data for a database. The data files can be located either in an operating system file system or Oracle ASM disk group.

data integrity

Business rules that dictate the standards for acceptable data. These rules are applied to a database by using integrity constraints and triggers to prevent invalid data entry.

data mining

The automated search of large stores of data for patterns and trends that transcend simple analysis.

Data Recovery Advisor

An Oracle Database infrastructure that automatically diagnoses persistent data failures, presents repair options to the user, and executes repairs at the user's request.

data segment

The segment containing the data for a nonclustered table, table partition, or table cluster.

See also extent.

data type

In SQL, a fixed set of properties associated with a column value or constant. Examples include `VARCHAR2` and `NUMBER`. Oracle Database treats values of different data types differently.

data warehouse

A relational database designed for query and analysis rather than for OLTP.

DDL

Data definition language. Includes statements such as `CREATE TABLE` or `ALTER INDEX` that define or change a data structure.

deadlock

A situation in which two or more users are waiting for data locked by each other. Such deadlocks are rare in Oracle Database.

dedicated server

A database configuration in which a server process handles requests for a single client process.

See also shared server.

deferrable constraint

A constraint that permits a `SET CONSTRAINT` statement to defer constraint checking until after the transaction is committed. A deferrable constraint enables you to disable the constraint temporarily while making changes that might violate the constraint.

degree of parallelism

The number of parallel execution servers associated with a single operation. Parallel execution is designed to effectively use multiple CPUs. Oracle Database parallel execution framework enables you to either explicitly choose a specific degree of parallelism or to rely on Oracle Database to automatically control it.

dependent object

In a schema object dependency, the object whose definition references another object. For example, if the definition of object A references object B, then A is a dependent object on B.

descending index

An index in which data is stored on a specified column or columns in descending order.

dimension

A structure that categorizes data to enable users to answer business questions. Commonly used dimensions are customers, products, and time.

dimension table

A relational table that stores all or part of the values for a dimension in a star or snowflake schema. Dimension tables typically contain columns for the dimension keys, levels, and attributes.

direct-path INSERT

An `INSERT` in which the database writes data directly to the data files, bypassing the database buffer cache. The database appends the inserted data to the existing data in the table.

directory object

A database object that specifies an alias for a directory on the server file system where external binary file LOBs (BFILEs) and external table data are located. All directory objects are created in a single namespace and are not owned by an individual schema.

dirty read

A transaction reads data that has been written by another transaction that has not been committed yet. Oracle Database never permits dirty reads.

dispatcher

See dispatcher process (Dnnn).

dispatcher process (Dnnn)

Optional background process present only when a shared server configuration is used. Each dispatcher process is responsible for routing requests from connected client processes to available shared server processes and returning the responses.

distributed database

A set of databases in a distributed system that can appear to applications as a single data source.

distributed processing

The operations that occurs when an application distributes its tasks among different computers in a network.

distributed transaction

A transaction that includes statements that, individually or as a group, update data on nodes of a distributed database. Oracle Database ensures the integrity of data in distributed transactions using the two-phase commit mechanism.

DML

Data manipulation language. Includes statements such as `SELECT`, `INSERT`, `UPDATE`, and `DELETE`.

edition

A private environment in which you can redefine database objects. Edition-based redefinition enables you to upgrade an application's database objects while the application is in use, thus minimizing or eliminating down time.

encryption

The process of transforming data into an unreadable format using a secret key and an encryption algorithm.

equijoin

A join with a join condition containing an equality operator.

ETL

Extraction, transformation, and loading (ETL). The process of extracting data from source systems and bringing it into a data warehouse.

execution plan

The combination of steps used by the database to execute a SQL statement. Each step either retrieves rows of data physically from the database or prepares them for the user issuing the statement. You can override execution plans by using hints.

expression

A combination of one or more values, operators, and SQL functions that evaluates to a value. For example, the expression `2*2` evaluates to `4`. In general, expressions assume the data type of their components.

extent

Multiple contiguous data blocks allocated for storing a specific type of information. A segment is made up of one or more extents.

See also data block.

external table

A read-only table whose metadata is stored in the database but whose data in stored in files outside the database. The database uses the metadata describing external tables to expose their data as if they were relational tables.

extraction, transformation, and loading (ETL)

See ETL.

fact

Data that represents a business measure, such as sales or cost data.

fact table

A table in a star schema of a data warehouse that contains factual data. A fact table typically has two types of columns: those that contain facts and those that are foreign keys to dimension tables.

fast full index scan

A full index scan in which the database reads the index blocks in no particular order. The database accesses the data in the index itself, without accessing the table.

fast recovery area

An optional disk location that stores recovery-related files such as control file and online redo log copies, archived redo log files, flashback logs, and RMAN backups.

field

In a table, the intersection of a row and column.

file system

A data structure built inside a contiguous disk address space.

foreign key

An integrity constraint that requires each value in a column or set of columns to match a value in the unique or primary key for a related table. Integrity constraints for foreign keys define actions dictating database behavior if referenced data is altered.

format model

A character literal that describes the format of a datetime in a character string.

full index scan

A scan of an index in which the database reads the entire index in order.

full table scan

A scan of table data in which the database sequentially reads all rows from a table and filters out those that do not meet the selection criteria. All data blocks under the high water mark are scanned.

function

A schema object, similar to a PL/SQL procedure, that always returns a single value.

function-based index

An index that computes the value of a function or expression involving one or more columns and stores it in the index.

granule

The basic unit of work in parallelism. Oracle Database divides the operation executed in parallel (for example, a table scan, table update, or index creation) into granules. Parallel execution processes execute the operation one granule at a time.

grid computing

A computing architecture that coordinates large numbers of servers and storage to act as a single large computer.

grid infrastructure

The software that provides the infrastructure for an enterprise grid architecture. In a cluster, this software includes Oracle Clusterware and Oracle ASM. For a standalone server, this software includes Oracle Restart and Oracle ASM. Oracle Database 11g Release 2 (11.2) combines these infrastructure products into one software installation called the grid infrastructure home.

hard parse

The steps performed by the database to build a new executable version of application code. The database must perform a hard parse instead of a soft parse if the parsed representation of a submitted statement does not exist in the shared pool.

hash cluster

A type of table cluster that is similar to an indexed cluster, except the index key is replaced with a hash function. No separate cluster index exists. In a hash cluster, the data is the index.

hash collision

Hashing multiple input values to the same output value.

hash function

A function that operates on an arbitrary-length input value and returns a fixed-length hash value.

hash join

A join in which the database uses the smaller of two tables or data sources to build a hash table in memory. The database scans the larger table, probing the hash table for the addresses of the matching rows in the smaller table.

hash key value

In a hash cluster, an actual or possible value inserted into the cluster key column. For example, if the cluster key is `department_id`, then hash key values could be 10, 20, 30, and so on.

hash table

An in-memory data structure that associates join keys with rows in a hash join. For example, in a join of the `employees` and `departments` tables, the join key might be the department ID. A hash function uses the join key to generate a hash value. This hash value is an index in an array, which is the hash table.

hash value

In a hash cluster, a unique numeric ID that identifies a bucket. Oracle Database uses a hash function that accepts an infinite number of hash key values as input and sorts them into a finite number of buckets. Each hash value maps to the database block address for the block that stores the rows corresponding to the hash key value (department 10, 20, 30, and so on).

hashing

A mathematical technique in which an infinite set of input values is mapped to a finite set of output values, called hash values. Hashing is useful for rapid lookups of data in a hash table.

heap-organized table

A table in which the data rows are stored in no particular order on disk. By default, `CREATE TABLE` creates a heap-organized table.

hierarchical database

A database that organizes data in a tree structure. Each parent record has one or more child records, similar to the structure of a file system.

high water mark

The boundary between used and unused space in a segment.

hint

An instruction passed to the optimizer through comments in a SQL statement. The optimizer uses hints to choose an execution plan for the statement.

human error outage

An outage that occurs when unintentional or malicious actions are committed that cause data in the database to become logically corrupt or unusable.

implicit query

A component of a DML statement that retrieves data without a subquery. An `UPDATE`, `DELETE`, or `MERGE` statement that does not explicitly include a `SELECT` statement uses an implicit query to retrieve the rows to be modified.

inconsistent backup

A backup in which some files in the backup contain changes made after the checkpoint. Unlike a consistent backup, an inconsistent backup requires media recovery to be made consistent.

index

Optional schema object associated with a nonclustered table, table partition, or table cluster. In some cases indexes speed data access.

index block

A special type of data block that manages space differently from table blocks.

index cluster

An table cluster that uses an index to locate data. The cluster index is a B-tree index on the cluster key.

index clustering factor

A measure of the row order in relation to an indexed value such as last name. The more order that exists in row storage for this value, the lower the clustering factor.

index-organized table

A table whose storage organization is a variant of a primary B-tree index. Unlike a heap-organized table, data is stored in primary key order.

index range scan

An ordered scan of an index that has the following characteristics:

- One or more leading columns of an index are specified in conditions. A condition specifies a combination of one or more expressions and logical (Boolean) operators and returns a value of `TRUE`, `FALSE`, or `UNKNOWN`.
- 0, 1, or more values are possible for an index key.

index scan

The retrieval of a row by traversing an index, using the indexed column values specified by the statement.

index segment

A segment that stores data for a nonpartitioned index or index partition.

index skip scan

An index scan that uses logical subindexes of a composite index. The database "skips" through a single index as if it were searching separate indexes.

index unique scan

An index scan that must have either 0 or 1 rowid associated with an index key. The database performs a unique scan when a predicate references all of the columns in the key of a `UNIQUE` index using an equality operator.

in-flight transaction

A transaction that is running when an outage breaks the connection between a client application and the database.

information system

A formal system for storing and processing information.

initialization parameter

A configuration parameter such as `DB_NAME` or `SGA_TARGET` that affects the operation of a database instance. Settings for initialization parameters are stored in a text-based initialization parameter file or binary server parameter file.

initialization parameter file

A text file that contains initialization parameter settings for a database instance.

inner join

A join of two or more tables that returns only those rows that satisfy the join condition.

instance

The combination of the system global area (SGA) and background processes. An instance is associated with one and only one database. In an Oracle Real Application Clusters configuration, multiple instances access a single database simultaneously.

instance failure

The termination of a database instance because of a hardware failure, Oracle internal error, or `SHUTDOWN ABORT` statement.

instance recovery

The automatic application of redo log records to uncommitted data blocks when an instance is restarted after a failure.

integrity

See data integrity.

integrity constraint

Declarative method of defining a rule for a column. The integrity constraints enforce business rules and prevent the entry of invalid information into tables.

interested transaction list (ITL)

Information in the block header of every segment that determines whether a transaction was uncommitted when the database began modifying the block. Entries in the ITL describe which transactions have rows locked and which rows in the block contain committed and uncommitted changes.

invisible index

An index that is maintained by DML operations, but is not used by default by the optimizer. Making an index invisible is an alternative to making it unusable or dropping it.

join

A statement that retrieves data from multiple tables specified in the `FROM` clause. Join types include inner joins, outer joins, and Cartesian joins.

join condition

A condition that compares two columns, each from a different table, in a join. The database combines pairs of rows, each containing one row from each table, for which the join condition evaluates to `TRUE`.

key

Column or set of columns included in the definition of certain types of integrity constraints.

key compression

The elimination of repeated occurrence of primary key column values in an index-organized table.

key values

Individual values in a key.

large object (LOB)

See LOB.

large pool

Optional area in the SGA that provides large memory allocations for backup and restore operations, I/O server processes, and session memory for the shared server and Oracle XA.

latch

A low-level serialization control mechanism used to protect shared data structures in the SGA from simultaneous access.

leaf block

In a B-tree index, a lower-level block that stores index entries. The upper-level branch blocks of a B-tree index contain index data that points to lower-level index blocks.

library cache

An area of memory in the shared pool. This cache includes the shared SQL areas, private SQL areas (in a shared server configuration), PL/SQL procedures and packages, and control structures such as locks and library cache handles.

listener

A process that listens for incoming client connection requests and manages network traffic to the database.

literal

A fixed data value.

LOB

Large object. An Oracle data type designed to hold large amounts of data.

locally managed tablespace

A tablespace that uses a bitmap stored in each data file to manage the extents. In contrast, a dictionary-managed tablespace uses the data dictionary to manage space.

lock

A database mechanism that prevents destructive interaction between transactions accessing a shared resource such as a table, row, or system object not visible to users. The main categories of locks are DML locks, DDL locks, and latches and internal locks.

logical transaction ID

A globally unique identifier that defines a transaction from the application perspective. The logical transaction ID is bound to the database transaction ID.

logical volume

A virtual disk partition.

logical volume manager (LVM)

A software package, available with most operating systems, that enables pieces of multiple physical disks to be combined into a single contiguous address space that appears as one disk to higher layers of software.

log sequence number

A number that uniquely identifies a set of redo records in a redo log file. When the database fills one online redo log file and switches to a different one, the database automatically assigns the new file a log sequence number.

log switch

The point at which the log writer (LGWR) stops writing to the active redo log file and switches to the next available redo log file. LGWR switches when either the active redo log file is filled with redo records or a switch is manually initiated.

log writer (LGWR)

The background process responsible for redo log buffer management—writing the redo log buffer to the online redo log. LGWR writes all redo entries that have been copied into the buffer since the last time it wrote.

lookup table

A table containing a code column and an associated value column. For example, a job code corresponds to a job name. In contrast to a master table in a pair of master-detail tables, a lookup table is not the means to obtain a detailed result set, such as a list of employees. Rather, a user queries a table such as `employees` for an employee list and then joins the result set to the lookup table.

lost update

A data integrity problem in which one writer of data overwrites the changes of a different writer modifying the same data.

mantissa

The part of a floating-point number that contains its significant digits.

manual undo management mode

A mode of the database in which undo blocks are stored in user-managed undo segments. In automatic undo management mode, undo blocks are stored in a system-managed, dedicated undo tablespaces.

master-detail tables

A detail table has a foreign key relationship with a master table. For example, the `employees` detail table has a foreign key to the `departments` master table. Unlike a lookup table, a master table is typically queried and then joined to the detail table. For example, a user may query a department in the `departments` table and then use this result to find the employees in this department.

master site

In a replication environment, a different database with which a materialized view shares data.

master table

The table associated with a materialized view at a master site.

materialized view

A schema object that stores the result of a query. Oracle materialized views can be read-only or updatable.

See also view.

media recovery

The application of redo or incremental backups to a data block or backup data file.

mounted database

An instance that is started and has the database control file open.

multitier architecture

An architecture in which one or more application servers provide data for clients and serves as an interface between clients and database servers.

network database

A type of database, similar to a hierarchical database, in which records have a many-to-many rather than a one-to-many relationship.

network encryption

Encrypting data as it travels across the network between a client and server.

null

Absence of a value in a column of a row. Nulls indicate missing, unknown, or inapplicable data.

object-relational database management system (ORDBMS)

An RDBMS that implements object-oriented features such as user-defined types, inheritance, and polymorphism.

object table

An special kind of table in which each row represents an object.

object type

A schema object that abstracts a real-world entity such as a purchase order. Attributes model the structure of the entity, whereas methods implement operations an application can perform on the entity.

OLAP

Online Analytical Processing. OLAP is characterized by dynamic, dimensional analysis of historical data.

OLTP

Online Transaction Processing. OLTP systems are optimized for fast and reliable transaction handling. Compared to data warehouse systems, most OLTP interactions involve a relatively small number of rows, but a larger group of tables.

online redo log

The set of two or more online redo log files that record all changes made to Oracle Database data files and control file. When a change is made to the database, Oracle Database generates a redo record in the redo buffer. log writer (LGWR) writes the contents of the redo buffer to the online redo log.

operator

1\. In memory management, operators control the flow of data. Examples include sort, hash join, and bitmap merge operators.

2\. In SQL, an operator manipulates data items called operands or arguments and returns a result. The SQL operators are represented by special characters or by keywords. For example, the multiplication operator is represented by an asterisk (`*`).

optimizer

Built-in database software that determines the most efficient way to execute a SQL statement by considering factors related to the objects referenced and the conditions specified in the statement.

Oracle architecture

Memory and process structures used by Oracle Database to manage a database.

Oracle Automatic Storage Management (Oracle ASM)

See Oracle ASM.

Oracle ASM

Oracle Automatic Storage Management (Oracle ASM). A volume manager and a file system for database files. Oracle ASM is Oracle's recommended storage management solution, providing an alternative to conventional volume managers, file systems, and raw devices.

Oracle ASM disk group

One or more Oracle ASM disks managed as a logical unit. I/O to a disk group is automatically spread across all the disks in the group.

Oracle Clusterware

A set of components that enables servers to operate together as if they were one server. Oracle Clusterware is a requirement for using Oracle RAC and it is the only clusterware that you need for platforms on which Oracle RAC operates.

Oracle Database Vault

A database security feature that controls when, where, and how databases, data, and applications are accessed.

Oracle Data Redaction

A security feature that enables you to mask (redact) data that is returned from queries issued by low-privileged users or applications.

Oracle Enterprise Manager

A system management tool that provides centralized management of an Oracle database environment.

Oracle home

The operating system location of an Oracle Database installation.

Oracle Net

Communication software that enables a network session between a client application and an Oracle database. After a network session is established, Oracle Net acts as a data courier for the client application and the database.

Oracle Net Listener

A process that resides on the server whose responsibility is to listen for incoming client connection requests and manage the traffic to the server. When a client requests a network session with a database, Oracle Net Listener (typically called the listener) receives the request. If the client information matches the listener information, then the listener grants a connection to the database server.

Oracle Net Services

A suite of networking components that provide enterprise-wide connectivity solutions in distributed, heterogeneous computing environments. Oracle Net Services includes Oracle Net, listener, Oracle Connection Manager, Oracle Net Configuration Assistant, and Oracle Net Manager.

Oracle process

A process that runs Oracle Database code. Oracle processes include server processes and background processes.

Oracle RAC

Oracle Real Application Clusters. Option that allows multiple concurrent database instances to share a single physical database.

Oracle Real Application Clusters

See Oracle RAC.

Oracle SQL

An implementation of the ANSI standard for SQL. Oracle SQL supports numerous features that extend beyond standard SQL.

Oracle Virtual Private Database (VPD)

A security feature that enables you to create security policies to control database access at the row and column level. Essentially, VPD adds a dynamic `WHERE` clause to a SQL statement that is issued against the table, view, or synonym to which a VPD security policy was applied.

Oracle XA

An external interface that allows global transactions to be coordinated by a transaction manager other than Oracle Database.

outer join

A join that returns all rows that satisfy the join condition and also returns some or all of those rows from one table for which no rows from the other satisfy the join condition.

parallel execution

The application of multiple CPU and I/O resources to the execution of a single database operation.

partial index

An index that is correlated with the indexing properties of an associated partitioned table.

partition

A piece of a table or index that shares the same logical attributes as the other partitions. For example, all partitions in a table share the same column and constraint definitions.

partition key

A set of one or more columns that determines the partition in which each row in a partitioned table should go. Each row is unambiguously assigned to a single partition.

partitioning

The ability to decompose very large tables and indexes into smaller and more manageable pieces called partitions.

PGA

Program global area. A memory buffer that contains data and control information for a server process.

See also SGA.

physical guess

The physical rowid of an index entry when it was first made. Oracle Database can use physical guesses to probe directly into the leaf block of any index-organized table, bypassing the primary key search.

plan generator

The part of the optimizer that tries different access paths, join methods, and join orders for a given query block to find the plan with the lowest cost.

PL/SQL

Procedural Language/SQL. The Oracle Database procedural language extension to SQL. PL/SQL enables you to mix SQL statements with programmatic constructs such as procedures, functions, and packages.

PL/SQL package

A logical grouping of related PL/SQL types, variables, and subprograms.

PL/SQL procedure

A schema object that consists of a set of SQL statements and other PL/SQL constructs, grouped together, stored in the database, and run as a unit to solve a specific problem or perform a set of related tasks.

PL/SQL subprogram

A named PL/SQL block that can be invoked with a set of parameters

precision

The total number of digits in a floating-point number. You specify a fixed-point number in the form `NUMBER` `(``p``,``s``)`, where `p` represents the precision.

precompiler

A programming tool that enables you to embed SQL statements in a high-level source program written in a language such as C, C++, or COBOL.

predicate

The `WHERE` condition in a SQL statement.

primary key

The column or set of columns that uniquely identifies a row in a table. Only one primary key can be defined for each table.

primary key constraint

An integrity constraint that disallows duplicate values and nulls in a column or set of columns.

private SQL area

An area in memory that holds a parsed statement and other information for processing. The private SQL area contains data such as bind variable values, query execution state information, and query execution work areas.

privilege

The right to run a particular type of SQL statement, or the right to access an object that belongs to another user, run a PL/SQL package, and so on. The types of privileges are defined by Oracle Database.

privilege analysis

A security mechanism that captures privilege usage for a database according to a specified condition. For example, you can find the privileges that a user exercised during a specific database session.

process

A mechanism in an operating system that can run a series of steps. By dividing the work of Oracle Database and database applications into several processes, multiple users and applications can connect to a single database instance simultaneously.

See also background process; Oracle process; client process.

program global area (PGA)

See PGA.

pseudocolumn

A column that is not stored in a table, yet behaves like a table column.

query

An operation that retrieves data from tables or views. For example, `SELECT * FROM employees` is a query.

See also implicit query; subquery.

query block

A top-level `SELECT` statement, subquery, or unmerged view.

query coordinator

In parallel execution, the user session or shadow process that coordinates the parallel execution servers. The parallel execution servers performs each operation in parallel if possible. When the parallel servers are finished executing the statement, the query coordinator performs any portion of the work that cannot be executed in parallel. Finally, the query coordinator returns any results to the user.

query plan

The execution plan used to execute a query.

R

A language and environment for statistical computing and graphics.

read consistency

A consistent view of data seen by a user. For example, in statement-level read consistency the set of data seen by a SQL statement remains constant throughout statement execution.

See also concurrency; data consistency.

read-only database

A database that is available for queries only and cannot be modified.

recoverable error

A class of errors that arise because of an external system failure, independently of the application session logic that is executing. Recoverable errors occur following planned and unplanned outages of networks, nodes, storage, and databases. An example of a nonrecoverable error is submission of invalid data values.

Recovery Manager (RMAN)

See RMAN.

recursive SQL

SQL that the database executes in the background to obtain space for database objects. You can think of recursive SQL as "side effect" SQL.

redo log

A set of files that protect altered database data in memory that has not been written to the data files. The redo log can consist of two parts: the online redo log and the archived redo log.

redo log buffer

Memory structure in the SGA that stores redo entries—a log of changes made to the database. The database writes the redo entries stored in the redo log buffers to an online redo log file, which is used if instance recovery is necessary.

redo record

A record in the online redo log that holds a group of change vectors, each of which describes a change made to a data block. Each redo log file consists of redo records.

redo thread

The redo generated by a database instance.

referenced object

In a schema object dependency, the object that is referenced by another object's definition. For example, if the definition of object A references object B, then B is a referenced object for A.

referential integrity

A rule defined on a key in one table that guarantees that the values in that key match the values in a key in a related table (the referenced value).

relation

A set of tuples.

relational database

A database that conforms to the relational model, storing data in a set of simple relations.

relational database management system (RDBMS)

A management system that moves data into a relational database, stores the data, and retrieves it so that applications can manipulate it.

replication

The process of sharing database objects and data at multiple databases.

reserved pool

A memory area in the shared pool that Oracle Database can use to allocate large contiguous chunks of memory.

reverse key index

A type of B-tree index that physically reverses the bytes of each index key while keeping the column order. For example, if the index key is `20`, and if the two bytes stored for this key in hexadecimal are `C1,15` in a standard B-tree index, then a reverse key index stores the bytes as `15,C1`.

RMAN

Recovery Manager. An Oracle Database utility that backs up, restores, and recovers Oracle databases.

role

A set of privileges that can be granted to database users or to other roles.

row

A set of column information corresponding to a single record in a table. The database stores rows in data blocks.

row chaining

A situation in which Oracle Database must store a row in a series or chain of blocks because it is too large to fit into a single block.

rowid

A globally unique address for a row in a database.

row major format

A type of table storage in which all columns of one row are stored together, followed by all columns of the next row, and so on.

row migration

A situation in which Oracle Database moves a row from one data block to another data block because the row grows too large to fit in the original block.

row piece

A row is stored in a variable-length record. This record is divided into one or more row pieces. Each row piece has a row header and column data.

sample schemas

A set of interlinked schemas that enable Oracle documentation and Oracle instructional materials to illustrate common database tasks.

savepoint

A named SCN in a transaction to which the transaction can be rolled back.

scale

In a floating-point number, the number of digits from the decimal point to the least significant digit. You specify a fixed-point number in the form `NUMBER` `(``p``,``s``)`, where `s` represents the scale.

schema

A named collection of database objects, including logical structures such as tables and indexes. A schema has the name of the database user who owns it.

schema object

A logical structure of data stored in a schema. Examples of schema objects are tables, indexes, sequences, and database links.

schema object dependency

The referencing of one object by another object. For example, a view contains a query that references tables or views, or a PL/SQL subprogram invokes other subprograms.

SCN

System Change Number. A database ordering primitive. The value of an SCN is the logical point in time at which changes are made to a database.

secondary index

An index on an index-organized table. In a sense, it is an index on an index.

security policy

A set of methods for protecting a database from accidental or malicious destruction of data or damage to the database infrastructure.

segment

A set of extents allocated for a specific database object such as a table, index, or table cluster. User segments, undo segments, and temporary segments are all types of segments.

selectivity

In a query, the measure of how many rows from a row set pass a predicate test, for example, `WHERE last_name = 'Smith'`. A selectivity of 0.0 means no rows, whereas a value of 1.0 means all rows. A predicate becomes more selective as the value approaches 0.0 and less selective (or more unselective) as the value approaches 1.0.

self join

A join of a table to itself.

sequence

A schema object that generates a serial list of unique numbers for table columns.

server

In a client/server architecture, the computer that runs Oracle software and handles the functions required for concurrent, shared data access. The server receives and processes the SQL and PL/SQL statements that originate from client applications.

server parameter file

A server-side binary file containing initialization parameter settings that is read and written to by the database.

server process

An Oracle process that communicates with a client process and Oracle Database to fulfill user requests. The server processes are associated with a database instance, but are not part of the instance.

service-oriented architecture (SOA)

A multitier architecture relying on services that support computer-to-computer interaction over a network.

session

A logical entity in the database instance memory that represents the state of a current user login to a database. A single connection can have 0, 1, or more sessions established on it.

SGA

System global area. A group of shared memory structures that contain data and control information for one Oracle database instance.

shared pool

Portion of the SGA that contains shared memory constructs such as shared SQL areas.

shared server

A database configuration that enables multiple client processes to share a small number of server processes.

See also dedicated server.

shared SQL area

An area in the shared pool that contains the parse tree and execution plan for a SQL statement. Only one shared SQL area exists for a unique statement.

single-level partitioning

A partitioning strategy that uses only one method of data distribution, for example, only list partitioning or only range partitioning.

soft parse

The reuse of existing code when the parsed representation of a submitted SQL statement exists in the shared pool and can be shared.

See also hard parse.

sorted hash cluster

A hash cluster that stores the rows corresponding to each value of the hash function in such a way that the database can efficiently return them in sorted order. The database performs the optimized sort internally.

SQL

Structured Query Language. A nonprocedural language to access a relational database. Users describe in SQL what they want done, and the SQL language compiler automatically generates a procedure to navigate the database and perform the task. Oracle SQL includes many extensions to the ANSI/ISO standard SQL language.

See also SQL\*Plus; PL/SQL.

SQL\*Plus

Oracle tool used to run SQL statements against Oracle Database.

standby database

An independent copy of a production database that you can use for disaster protection in a high availability environment.

star schema

A relational schema whose design represents a dimensional data model. The star schema consists of one or more fact tables and one or more dimension tables that are related through foreign keys.

See also dimension table; fact table.

statement-level rollback

A database operation in which the effects of an unsuccessful SQL statement are rolled back because the statement caused an error during execution.

stored procedure

A named PL/SQL block or Java program that Oracle Database stores in the database. Applications can call stored procedures by name.

Structured Query Language (SQL)

See SQL.

subquery

A query nested within another SQL statement. Unlike implicit queries, subqueries use a `SELECT` statement to retrieve data.

summary

In a data warehouse, an aggregate view that reduces query time by precalculating joins and aggregation operations and storing the results in a table.

synonym

An alias for a schema object. You can use synonyms to provide data independence and location transparency.

system change number (SCN)

See SCN.

system global area (SGA)

See SGA.

table

Basic unit of data storage in Oracle Database. Data in tables is stored in rows and columns.

table cluster

A schema object that contains data from one or more tables, all of which have one or more columns in common. In table clusters, the database stores together all the rows from all tables that share the same cluster key.

table compression

The compression of data segments to reduce disk space in a heap-organized table or table partition.

table function

A user-defined PL/SQL function that returns a collection of rows (a nested table or varray). You can select from this collection as if it were a database table by invoking the table function inside the `TABLE` clause in a `SELECT` statement.

tablespace

A database storage unit that groups related logical structures together. The database data files are stored in tablespaces.

temp file

A file that belongs to a temporary tablespace. The temp files in temporary tablespaces cannot contain permanent database objects.

temporary segment

A segment created by Oracle Database when a SQL statement needs a temporary database area to complete execution.

temporary table

A table that holds an intermediate result set for the duration of a transaction or a session. Only the current session can see the data in temporary tables.

trace file

An administrative file that contain diagnostic data used to investigate problems. Oracle Database writes trace files to ADR.

transaction

Logical unit of work that contains one or more SQL statements. All statements in a transaction commit or roll back together. The use of transactions is one of the most important ways that a database management system differs from a file system.

transaction ID

An identifier is unique to a transaction and represents the undo segment number, slot, and sequence number.

transaction recovery

A phase of instance recovery in which uncommitted transactions are rolled back.

transaction table

The data structure within an undo segment that holds the transaction identifiers of the transactions using the undo segment.

Transparent Data Encryption

A database feature that encrypts individual table columns or a tablespace. When a user inserts data into an encrypted column, the database automatically encrypts the data. When users select the column, the data is decrypted. This form of encryption is transparent, provides high performance, and is easy to implement.

transportable tablespace

A tablespace that you can copy or move between databases. Oracle Data Pump provides the infrastructure for transportable tablespaces.

trigger

A PL/SQL or Java procedure that fires when a table or view is modified or when specific user or database actions occur. Procedures are explicitly run, whereas triggers are implicitly run.

tuple

An unordered set of attribute values.

UGA

User global area. Session memory that stores session variables, such as logon information, and can also contain the OLAP pool.

undo data

Records of the actions of transactions, primarily before they are committed. The database can use undo data to logically reverse the effect of SQL statements. Undo data is stored in undo segments.

undo segment

A segment in an undo tablespace.

undo tablespace

A tablespace containing undo segments when automatic undo management mode is enabled.

Unicode

A universal encoded character set that can store information in any language using a single character set.

universal rowid

A data type that can store all types of rowids. Oracle uses universal rowids to store the addresses of index-organized and non-Oracle tables.

unusable index

An index that is not maintained by DML operations and is ignored by the optimizer. All indexes are usable (default) or unusable.

user global area (UGA)

See UGA.

user name

The name by which a user is known to Oracle Database and to other users. Every user name is associated with a password, and both must be entered to connect to Oracle Database.

user process

See client process.

user profile

A named set of resource limits and password parameters that restrict database usage and database instance resources for a user.

view

A custom-tailored presentation of the data in one or more tables. The views do not actually contain or store data, but derive it from the tables on which they are based.

virtual column

A column that is not stored on disk. The database derives the values in virtual columns on demand by computing a set of expressions or functions.

whole database backup

A backup of the control file and all data files that belong to a database.

work area

A private allocation of PGA memory used for memory-intensive operations.