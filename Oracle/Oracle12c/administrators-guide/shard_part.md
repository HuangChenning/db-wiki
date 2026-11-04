---
title: "Database Administrator’s Guide"
book: "Database Administrator's Guide"
doc_id: E85760-09
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/admin/shard_part.html
tags:
  - oracle
  - 12c
  - administrators-guide
---

Sharding is a data tier architecture in which data is horizontally partitioned across independent databases.

The following topics discuss sharded database design, deployment, schema creation, and management with Oracle Sharding:

- [Overview of Oracle Sharding](sharding-overview.md)  
	Become familiar with the concepts related to managing a sharded database with Oracle Sharding.
- [Sharded Database Schema Design](sharding-schema-design.md)  
	To obtain the benefits of sharding, the schema of a sharded database (SDB) should be designed in a way that maximizes the number of database requests executed on a single shard.
- [Physical Organization of a Sharded Database](sharding-physical-organization.md)  
	Learn about the physical organization of a sharded database.
- [Sharding Methods](sharding-methods.md)  
	This chapter discusses the sharding methods supported by Oracle Sharding, how to choose a method, and how to use subpartitioning.
- [Design Considerations for Sharded Database Applications](sharding-application-development.md)  
	To obtain the benefits of sharding, a schema of an SDB should be designed in a way that maximizes the number of database requests executed on a single shard.
- [Routing in an SDB Environment](sharding-data-routing.md)  
	Oracle Sharding supports two types of routing.
- [Shard-Level High Availability](sharding-high-availability.md)  
	Oracle Sharding is integrated with Oracle Database replication technologies for high availability and disaster recovery at the shard level.
- [Sharded Database Deployment](sharding-deployment.md)  
	Sharded database deployment includes the prerequisites and instructions for installing the required software components, creating the catalog, roles, and the sharded database, configuring replication for high availability, and creating the schema for the sharded database.
- [Sharded Database Lifecycle Management](sharding-lifecycle-management.md)  
	Oracle Sharding provides tools and some automation for lifecycle management of a sharded database.