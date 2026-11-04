---
title: "8.3.3 Creating SSL and RSA Certificates and Keys"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/creating-ssl-rsa-files.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 8.3.3 Creating SSL and RSA Certificates and Keys

The following discussion describes how to create the files required for SSL and RSA support in MySQL. File creation can be performed using facilities provided by MySQL itself, or by invoking the **openssl** command directly.

SSL certificate and key files enable MySQL to support encrypted connections using SSL. See [Section 8.3.1, “Configuring MySQL to Use Encrypted Connections”](using-encrypted-connections.md).

RSA key files enable MySQL to support secure password exchange over unencrypted connections for accounts authenticated by the `sha256_password` (deprecated) or `caching_sha2_password` plugin. See [Section 8.4.1.3, “SHA-256 Pluggable Authentication”](sha256-pluggable-authentication.md), and [Section 8.4.1.2, “Caching SHA-2 Pluggable Authentication”](caching-sha2-pluggable-authentication.md).