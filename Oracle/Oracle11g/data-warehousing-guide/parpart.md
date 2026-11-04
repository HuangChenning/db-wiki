---
title: Partitioning in Data Warehouses
book: Data Warehousing Guide
doc_id: E25554-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e25554/parpart.htm
tags:
  - oracle
  - 11g
  - data-warehousing-guide
---

## 5 Partitioning in Data Warehouses

This chapter provides an introduction to the topic of partitioning in a data warehousing environment, and includes:

- Overview of Partitioning in Data Warehouses

## Overview of Partitioning in Data Warehouses

Data warehouses often contain very large tables and require techniques both for managing these large tables and for providing good query performance across them. An important tool for achieving this, as well as enhancing data access and improving overall application performance is partitioning.

Partitioning offers support for very large tables and indexes by letting you decompose them into smaller and more manageable pieces called partitions. This support is especially important for applications that access tables and indexes with millions of rows and many gigabytes of data. Partitioned tables and indexes facilitate administrative operations by enabling these operations to work on subsets of data. For example, you can add a new partition, organize an existing partition, or drop a partition with minimal to zero interruption to a read-only application.

Partitioning can help you tune SQL statements to avoid unnecessary index and table scans (using partition pruning). It also enables you to improve the performance of massive join operations when large amounts of data (for example, several million rows) are joined together by using partition-wise joins. Finally, partitioning data greatly improves manageability of very large databases and dramatically reduces the time required for administrative tasks such as backup and restore.

When adding or creating a partition, you have the option of deferring the segment creation until the data is first inserted, which is particularly valuable when installing applications that have a large footprint.

Granularity in a partitioning scheme can be easily changed by splitting or merging partitions. Thus, if a table's data is skewed to fill some partitions more than others, the ones that contain more data can be split to achieve a more even distribution. Partitioning also enables you to swap partitions with a table. By being able to easily add, remove, or swap a large amount of data quickly, swapping can be used to keep a large amount of data that is being loaded inaccessible until loading is completed, or can be used as a way to stage data between different phases of use. Some examples are current day's transactions or online archives.

A good starting point for considering partitioning strategies is to use the partitioning advice within the SQL Access Advisor, part of the Tuning Pack. The SQL Access Advisor offers both graphical and command-line interfaces.

A complementary approach that is commonly used with partitioning is parallel execution, which speeds up long-running queries, ETL, and some other operations. For data warehouses with very high loads of parallel statements, parallel statement queuing can be used to automatically manage the parallel statements.

See Also:

- [Chapter 6, "Parallel Execution in Data Warehouses"](px.md)
- [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25523/toc.htm) for a detailed examination of how and when to use partitioning as well as parallel execution and parallel statement queuing
- [Oracle Database 2 Day + Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10822/tdppt_sqlopt.htm#TDPPT171) for details regarding the SQL Access Advisor