---
title: "6.8.1 lz4_decompress — Decompress mysqlpump LZ4-Compressed Output"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/lz4-decompress.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 6.8.1 lz4\_decompress — Decompress mysqlpump LZ4-Compressed Output

The **lz4\_decompress** utility decompresses [**mysqlpump**](mysqlpump.md) output that was created using LZ4 compression.

Note

**lz4\_decompress** is deprecated as of MySQL 8.0.34; expect it to be removed in a future version of MySQL. This is because the associated [**mysqlpump**](mysqlpump.md) utility is deprecated as of MySQL 8.0.34.

Note

If MySQL was configured with the [`-DWITH_LZ4=system`](source-configuration-options.md) option, **lz4\_decompress** is not built. In this case, the system **lz4** command can be used instead.

Invoke **lz4\_decompress** like this:

```
lz4_decompress input_file output_file
```

Example:

```
mysqlpump --compress-output=LZ4 > dump.lz4
lz4_decompress dump.lz4 dump.txt
```

To see a help message, invoke **lz4\_decompress** with no arguments.

To decompress [**mysqlpump**](mysqlpump.md) ZLIB-compressed output, use [**zlib\_decompress**](zlib-decompress.md). See [Section 6.8.3, “zlib\_decompress — Decompress mysqlpump ZLIB-Compressed Output”](zlib-decompress.md).