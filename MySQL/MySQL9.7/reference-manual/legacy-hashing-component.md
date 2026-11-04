---
title: "7.5.8 Legacy Hashing Component"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/legacy-hashing-component.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 7.5.8 Legacy Hashing Component

Note

Exploits for the MD5 and SHA-1 algorithms have become known. You may wish to consider using another one-way encryption algorithm instead, such as the [`SHA2()`](encryption-functions.md) function. See [Section 14.13, “Encryption and Compression Functions”](encryption-functions.md).

The legacy hashing component calclulates an MD5 and SHA-1 checksum for the string.

- Purpose: Provides a migration path for users and applications so that you can move to a more secure hashing algorithm.
- URN: `file://component_classic_hashing`

For installation instructions, see [Section 7.5.1, “Installing and Uninstalling Components”](component-loading.md).

The component performs the following for the MD5 encryption algorithm:

- Calculates an MD5 128-bit checksum for the string.
- The value is returned as a string of 32 hexadecimal digits.
- The value returned is `NULL` if the argument was `NULL`.

The component performs the following for the SHA-1 encryption algorithm:

- Calculates an SHA-1 160-bit checksum for the string, as described in RFC 3174 (Secure Hash Algorithm).
- The value is returned as a string of 40 hexadecimal digits.
- The value returned is `NULL` if the argument is `NULL`.
- SHA(in string) returns a string the same as SHA1().

Keep in mind the following for the legacy hashing component:

- The component only works on string arguments. Applications that needs to calculate checksums over other argument types need to add a `CAST`.
- The component reads the FIPs mode at its initialization time. MD5 always returns `NULL` if the FIPs mode is read to be on.
- If a generated column within any table table uses the `MD5()` and `SHA1` functions that are removed as of MySQL 9.6.0, and MySQL server is upgraded to MySQL 9.6.0 or later, the table stops working. To resolve this, you must dispose of the generated column and have triggers on the table to generate the column value.