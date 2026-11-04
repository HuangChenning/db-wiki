---
title: "Database Administrator’s Guide"
book: "Database Administrator's Guide"
doc_id: F31835-17
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/admin/managing-read-only-materialized-views.html
tags:
  - oracle
  - 21c
  - administrators-guide
---

## Part VI Managing Read-Only Materialized Views

Read-only materialized views can provide read-only access to the master table's data. You can create and manage read-only materialized views.

- [Read-Only Materialized View Concepts](read-only-materialized-view-concepts.md)  
	Understand the concepts related to read-only materialized views.
- [Read-Only Materialized View Architecture](read-only-materialized-view-architecture.md)  
	Several objects are used in materialized view replication. Some of these objects are optional and are used only as needed to support the created materialized view environment. For example, if you have a complex materialized view that cannot be fast refreshed, then you might not have a materialized view log at the master database.
- [Planning for Read-Only Materialized Views](planning-for-read-only-materialized-views.md)  
	Before you begin to plan your read-only materialized view environment, it is important to understand the concepts and architecture related to materialized views. After you understand concepts and architecture of read-only materialized views, there are important considerations for planning a read-only materialized view environment.
- [Creating and Managing Read-Only Materialized Views](creating-and-managing-read-only-materialized-views.md)  
	You can create and manage read-only materialized views and refresh groups. You can also refresh materialized views.
- [Troubleshooting Problems with Read-Only Materialized Views](troubleshooting-problems-with-read-only-materialized-views.md)  
	You can diagnose and solve problems with database links, materialized view creation, and materialized view refresh.