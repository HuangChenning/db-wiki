---
title: "4.8.1 lz4_decompress — Decompress mysqlpump LZ4-Compressed Output"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/lz4-decompress.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 4.8.1 lz4\_decompress — Decompress mysqlpump LZ4-Compressed Output

The **lz4\_decompress** utility decompresses [**mysqlpump**](mysqlpump.md) output that was created using LZ4 compression. **lz4\_decompress** was added in MySQL 5.7.10.

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

To decompress [**mysqlpump**](mysqlpump.md) ZLIB-compressed output, use [**zlib\_decompress**](zlib-decompress.md). See [Section 4.8.5, “zlib\_decompress — Decompress mysqlpump ZLIB-Compressed Output”](zlib-decompress.md).