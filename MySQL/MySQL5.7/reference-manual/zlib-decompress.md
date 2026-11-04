---
title: "4.8.5 zlib_decompress — Decompress mysqlpump ZLIB-Compressed Output"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/zlib-decompress.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 4.8.5 zlib\_decompress — Decompress mysqlpump ZLIB-Compressed Output

The **zlib\_decompress** utility decompresses [**mysqlpump**](mysqlpump.md) output that was created using ZLIB compression. **zlib\_decompress** was added in MySQL 5.7.10.

Invoke **zlib\_decompress** like this:

```
zlib_decompress input_file output_file
```

Example:

```
mysqlpump --compress-output=ZLIB > dump.zlib
zlib_decompress dump.zlib dump.txt
```

To see a help message, invoke **zlib\_decompress** with no arguments.

To decompress [**mysqlpump**](mysqlpump.md) LZ4-compressed output, use [**lz4\_decompress**](lz4-decompress.md). See [Section 4.8.1, “lz4\_decompress — Decompress mysqlpump LZ4-Compressed Output”](lz4-decompress.md).