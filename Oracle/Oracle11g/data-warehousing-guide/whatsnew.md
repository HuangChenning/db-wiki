---
title: "What's New in Oracle Database?"
book: Data Warehousing Guide
doc_id: E25554-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e25554/whatsnew.htm
tags:
  - oracle
  - 11g
  - data-warehousing-guide
---

This section describes the new features of Oracle Database 11g Release 2 (11.2) and provides pointers to additional information. New features information from previous releases is also retained to help those users migrating to the current release.

The following section describes new features in Oracle Database:

- Oracle Database 11g Release 2 (11.2) New Features in Data Warehousing
- Oracle Database 11g Release 1 (11.1) New Features in Data Warehousing

## Oracle Database 11g Release 2 (11.2) New Features in Data Warehousing

- Analytic Functions
	New SQL analytic functions have been introduced that enable you to list (or concatenate) measure values within a group (`LISTAGG`). Another new function (`NTH_VALUE`) enables you to retrieve an arbitrary (in other words, nth) record in a window. Finally, the existing functions `LAG` and `LEAD` now have been improved with the addition of the `IGNORE` `NULLS` option.
	See Also:
	[Chapter 22, "SQL for Analysis and Reporting"](analysis.md) for more information
- Preprocessing of Files from External Tables
	You can now specify a program to be executed that will process files and enable Oracle Database to use the output. This preprocessing of files enables you to load large amounts of compressed data without first uncompressing it on a disk.
	See Also:
	[Chapter 15, "Loading and Transformation"](transform.md) for more information
- Materialized View Refresh Enhancements
	Materialized view logs can now be purged outside the refresh process, thus improving performance. An additional performance improvement is with materialized views that contain aggregates, joins, or both. If you use a `WITH` `COMMIT` `SCN` clause, materialized view log processing can be optimized, thus speeding up the refresh process.
	See Also:
	[Chapter 9, "Basic Materialized Views"](basicmv.md) and [Chapter 16, "Maintaining the Data Warehouse"](refresh.md) for more information

## Oracle Database 11g Release 1 (11.1) New Features in Data Warehousing

- Pivot and Unpivot Operators
	The `PIVOT` operator makes it easy to create aggregated cross-tabular output that condenses many rows into a compact result set useful for reports. For instance, input data holding sales of one month in each row can be pivoted into output holding twelve months in each row, with each month in its own column. By combining multiple input rows into each output row, `PIVOT` also enables inter-row comparison without a table self-join. The `UNPIVOT` operator reshapes data into a format useful for further relational operations. For example, if a source data set presents twelve months of sales values in each row, `UNPIVOT` can reshape each source row into twelve output rows, each holding one month of sales data. The unpivoted results are in a more normalized relational form than the source data, and they can be manipulated with simpler and more efficient SQL.
	See Also:
	[Chapter 21, "SQL for Aggregation in Data Warehouses"](aggreg.md) for more information
- Partition Advisor
	The SQL Access Advisor has been enhanced to include partition advice. It recommends the right strategy to partition tables, indexes, and materialized views to get best performance from an application.
	See Also:
	[Chapter 5, "Partitioning in Data Warehouses"](parpart.md) for more information
- Change Data Capture (CDC) Enhancements
	CDC is now aware of direct-path load operations and implicit data changes as the result of partition-maintenance operations. Users can now turn synchronous CDC on and off as needed. Also, the flexibility of purging change data from change tables has been improved, so you can specify a date range for which data should be purged.
	Another improvement is that it is easier to maintain a subscription window to change data. You now have control over the definition of the change subscription, so the window can be moved forward and backward.
	See Also:
	[Chapter 17, "Change Data Capture"](cdc.md) for more information
- Query Rewrite Enhancements
	Query rewrite has been enhanced to support queries containing inline views. Prior to this release, queries containing inline views could rewrite only if there was an exact text match with the inline views in the materialized views. Because inline views no longer need to textually match between the query and the materialized view, a larger number of queries with inline views can be rewritten. Another significant query rewrite improvement is the ability to rewrite queries that reference remote tables.
	See Also:
	[Chapter 18, "Basic Query Rewrite"](qrbasic.md) for more information
- Refresh Enhancements
	Refresh has been enhanced to support automatic index creation for `UNION` `ALL` materialized views, the use of query rewrite during a materialized view's atomic refresh, and materialized view refresh with set operators. Also, partition change tracking refresh of `UNION` `ALL` materialized views is now possible. Finally, catalog views have been enhanced to contain information on the staleness of partitioned materialized views. These improvements will lead to faster refresh performance.
	See Also:
	[Chapter 16, "Maintaining the Data Warehouse"](refresh.md) for more information
- Oracle OLAP Option Data Warehousing Features
	The OLAP Option of the Oracle Database has been enhanced with several features designed to make OLAP cubes attractive alternatives to tables for managing and querying aggregate data in the data warehouse. These include:
	- Further integration of cubes into the SQL query engine. Advancements include integration of cubes with the Oracle query optimizer and a cube row source. These features dramatically increase the efficiency of SQL queries that select from OLAP cubes and dimensions by pushing joins directly into the Oracle Database's multidimensional engine, allowing efficient joins between tables and cubes and by improving overall row/second throughput when selecting from cubes.
		- Automatic query rewrite to cube organized materialized views. Cube-organized materialized views access data from OLAP cubes rather than tables. Like table-based materialized views, application can write queries to detail tables or views and let the database automatically rewrite the query to pre-aggregated data in the cube.
		- Database-managed automatic refresh of cubes. In this release, cubes can be refreshed using the `DBMS_MVIEW.REFRESH` program, just like table-based materialized views. Cubes provide excellent support for `FAST` (incremental) refresh.
		- Cost-based aggregation. In many situations, cubes are much more efficient at managing aggregate data as compared to tables. Cost-based aggregation improves upon these advantages by improving the efficiency of pre-aggregating and querying aggregate data, and by simplifying the process of managing aggregate data.
	Database administrators who support dimensionally modeled data sets (for example, star/snowflake schema) for query by business intelligence tools and applications should consider using OLAP cubes as a summary management solution because they may offer significant performance advantages.