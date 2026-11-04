---
title: "8.5.3 MySQL Enterprise Data Masking and De-Identification Plugin"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/data-masking-plugin.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 8.5.3 MySQL Enterprise Data Masking and De-Identification Plugin

MySQL Enterprise Data Masking and De-Identification is based on a plugin library that implements these elements:

- A server-side plugin named `data_masking`.
- A set of loadable functions provides an SQL-level API for performing masking and de-identification operations. Some of these functions require the [`SUPER`](privileges-provided.md) privilege.