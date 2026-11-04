---
title: "14.9 InnoDB Table and Page Compression"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/innodb-compression.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

This section provides information about the `InnoDB` table compression and `InnoDB` page compression features. The page compression feature is referred to as [transparent page compression](glossary.md).

Using the compression features of `InnoDB`, you can create tables where the data is stored in compressed form. Compression can help to improve both raw performance and scalability. The compression means less data is transferred between disk and memory, and takes up less space on disk and in memory. The benefits are amplified for tables with [secondary indexes](glossary.md), because index data is compressed also. Compression can be especially important for [SSD](glossary.md) storage devices, because they tend to have lower capacity than [HDD](glossary.md) devices.