---
title: "9.6.4 MyISAM Table Optimization"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/myisam-optimization.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 9.6.4 MyISAM Table Optimization

To coalesce fragmented rows and eliminate wasted space that results from deleting or updating rows, run [**myisamchk**](myisamchk.md) in recovery mode:

```
$> myisamchk -r tbl_name
```

You can optimize a table in the same way by using the [`OPTIMIZE TABLE`](optimize-table.md) SQL statement. [`OPTIMIZE TABLE`](optimize-table.md) does a table repair and a key analysis, and also sorts the index tree so that key lookups are faster. There is also no possibility of unwanted interaction between a utility and the server, because the server does all the work when you use [`OPTIMIZE         TABLE`](optimize-table.md). See [Section 15.7.3.4, “OPTIMIZE TABLE Statement”](optimize-table.md).

[**myisamchk**](myisamchk.md) has a number of other options that you can use to improve the performance of a table:

- [`--analyze`](myisamchk-other-options.md) or `-a`: Perform key distribution analysis. This improves join performance by enabling the join optimizer to better choose the order in which to join the tables and which indexes it should use.
- [`--sort-index`](myisamchk-other-options.md) or `-S`: Sort the index blocks. This optimizes seeks and makes table scans that use indexes faster.
- [``--sort-records=*`index_num`*``](myisamchk-other-options.md) or ``-R *`index_num`*``: Sort data rows according to a given index. This makes your data much more localized and may speed up range-based [`SELECT`](select.md) and `ORDER             BY` operations that use this index.

For a full description of all available options, see [Section 6.6.4, “myisamchk — MyISAM Table-Maintenance Utility”](myisamchk.md).