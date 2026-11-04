---
title: "17.9 InnoDB Table and Page Compression"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/innodb-compression.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

This section provides information about the `InnoDB` table compression and `InnoDB` page compression features. The page compression feature is also referred to as [transparent page compression](glossary.md).

Using the compression features of `InnoDB`, you can create tables where the data is stored in compressed form. Compression can help to improve both raw performance and scalability. The compression means less data is transferred between disk and memory, and takes up less space on disk and in memory. The benefits are amplified for tables with [secondary indexes](glossary.md), because index data is compressed also. Compression can be especially important for [SSD](glossary.md) storage devices, because they tend to have lower capacity than [HDD](glossary.md) devices.