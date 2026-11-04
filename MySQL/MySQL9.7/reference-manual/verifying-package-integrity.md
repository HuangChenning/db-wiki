---
title: "2.1.4 Verifying Package Integrity Using MD5 Checksums or GnuPG"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/verifying-package-integrity.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 2.1.4 Verifying Package Integrity Using MD5 Checksums or GnuPG

After downloading the MySQL package that suits your needs and before attempting to install it, make sure that it is intact and has not been tampered with. There are three means of integrity checking:

The following sections describe how to use these methods.

If you notice that the MD5 checksum or GPG signatures do not match, first try to download the respective package one more time, perhaps from another mirror site.