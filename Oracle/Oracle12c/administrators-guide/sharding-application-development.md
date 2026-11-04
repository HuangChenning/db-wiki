---
title: "Database Administrator’s Guide"
book: "Database Administrator's Guide"
doc_id: E85760-09
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/admin/sharding-application-development.html
tags:
  - oracle
  - 12c
  - administrators-guide
---

To obtain the benefits of sharding, a schema of an SDB should be designed in a way that maximizes the number of database requests executed on a single shard.

The following topics describe the terminology and concepts you will need to manage a sharded database schema:

- Considerations for Sharded Database Schema Design  
	Design of the database schema has a big impact on the performance and scalability of a sharded database (SDB). An improperly designed schema can lead to unbalanced distribution of data and workload across shards and large percentage of multi-shard operations.
- Developing Applications for Oracle Sharding  
	Sharding provides linear scalability and complete fault isolation for the most demanding OLTP applications without compromising on the enterprise qualities of Oracle Database: strict consistency, the full power of SQL, developer agility with JSON, security, high availability, backup and recovery, life-cycle management, and more.

**Parent topic:** [Sharded Database Management](shard_part.md)

### 53.1 Considerations for Sharded Database Schema Design

Design of the database schema has a big impact on the performance and scalability of a sharded database (SDB). An improperly designed schema can lead to unbalanced distribution of data and workload across shards and large percentage of multi-shard operations.

Once the SDB is populated with data, it is impossible to change many attributes of the schema, such as whether a table is sharded or duplicated, sharding key, and so on. Therefore, the following points should be carefully considered before deploying an SDB:

- Which tables should be sharded?
- Which tables should be duplicated?
- Which sharded table should be the root table?
- What method should be used to link other tables to the root table?
- Which sharding method should be used?
- Which sharding key should be used?
- Which super sharding key should be used (if the sharding method is composite)?

**Parent topic:** Design Considerations for Sharded Database Applications

### 53.2 Developing Applications for Oracle Sharding

Sharding provides linear scalability and complete fault isolation for the most demanding OLTP applications without compromising on the enterprise qualities of Oracle Database: strict consistency, the full power of SQL, developer agility with JSON, security, high availability, backup and recovery, life-cycle management, and more.

Sharding is a data tier architecture in which data is horizontally partitioned across independent databases. Each database in such a configuration is called a shard. All of the shards together make up a single logical database, which is referred to as a sharded database (SDB).

There are two methods of sharding available to developers.

- System-managed sharding is a sharding method which does not require the user to specify mapping of data to shards. Data is automatically distributed across shards using partitioning by consistent hash. The partitioning algorithm evenly and randomly distributes data across shards for linear scalability.
- Composite sharding is a sharding method that allows the creation of multiple shardspaces for different subsets of data in a table partitioned by consistent hash. Composite sharding is unique to Oracle and offers developers the ability to differentiate subsets of data within an SDB in order to store them in different geographic locations, allocate to them different hardware resources, etc, and then elastically scale performance within each subset.

Oracle Sharding is based on table partitioning; all of the subpartitioning methods provided by Oracle Database are also supported for sharding.

Sharding is intended for OLTP applications that are suitable for a sharded database architecture. Specifically:

- Applications must have a well-defined data model and data distribution strategy, system-managed (consistent hash) or composite, and must primarily accesses data using a sharding key. Examples of sharding keys include customer ID, account number, country\_id, and so on.
- The data model should be a hierarchical tree structure with a single root table. Oracle Sharding supports any number of levels within the hierarchy.
- For the system-managed sharding method, the sharding key must be based on a column that has high cardinality; the number of unique values in this column must be much bigger than the number of shards. Customer ID, for example, is a good candidate for the sharding key, while a United States state name is not.
- The sharding key should be very stable; its value should almost never change.
- The sharding key must be present in all of the sharded tables. This allows the creation of a family of equi-partitioned tables based on the sharding key. The sharding key must be the leading column of the primary key of the root table.
- Joins between tables in a table family should be performed using the sharding key.
- Composite sharding enables two levels of sharding - one by list or range and another by consistent hash. This is accomplished by the application providing two keys: a super sharding key and a sharding key.
- All database requests that require high performance and fault isolation must only access data associated with a single value of the sharding key. The application must provide the sharding key when establishing a database connection. If this is the case, the request is routed directly to the appropriate shard.
	Multiple requests can be executed in the same session as long as they all are related to the same sharding key. Such transactions typically access 10s or 100s of rows. Examples of single-shard transactions include order entry, lookup and update of a customer’s billing record, and lookup and update of a subscriber’s documents.
- Database requests that must access data associated with multiple values of the sharding key, or for which the value of the sharding key is unknown, must be executed from the query coordinator which orchestrates parallel execution of the query across multiple shards.
- Applications use Oracle integrated connection pools (UCP, OCI, ODP.NET, JDBC) to connect to a sharded database.
- Separate connection pools must be used for direct routing and proxy routing. For direct routing, separate global services must be created for read-write and read-only workloads. For proxy routing, use the GDS$CATALOG service on the shard catalog database.

See Also:

- [Direct Routing to a Shard](sharding-data-routing.md)
- [Queries and DMLs via Proxy Routing in an SDB](sharding-data-routing.md)

**Parent topic:** Design Considerations for Sharded Database Applications