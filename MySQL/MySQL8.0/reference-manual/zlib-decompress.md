---
title: "6.8.3 zlib_decompress — Decompress mysqlpump ZLIB-Compressed Output"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/zlib-decompress.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 6.8.3 zlib\_decompress — Decompress mysqlpump ZLIB-Compressed Output

The **zlib\_decompress** utility decompresses [**mysqlpump**](mysqlpump.md) output that was created using ZLIB compression.

Note

**zlib\_decompress** is deprecated as of MySQL 8.0.34; expect it to be removed in a future version of MySQL. This is because the associated [**mysqlpump**](mysqlpump.md) utility is deprecated as of MySQL 8.0.34.

Note

If MySQL was configured with the [`-DWITH_ZLIB=system`](source-configuration-options.md) option, **zlib\_decompress** is not built. In this case, the system **openssl zlib** command can be used instead.

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

To decompress [**mysqlpump**](mysqlpump.md) LZ4-compressed output, use [**lz4\_decompress**](lz4-decompress.md). See [Section 6.8.1, “lz4\_decompress — Decompress mysqlpump LZ4-Compressed Output”](lz4-decompress.md).