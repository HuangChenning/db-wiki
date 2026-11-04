---
title: "8.5.3 MySQL Enterprise Data Masking Plugin"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/data-masking-plugin.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 8.5.3 MySQL Enterprise Data Masking Plugin

MySQL Enterprise Data Masking is based on a plugin library that implements these elements:

- A server-side plugin named `data_masking`.
- A set of loadable functions provides an SQL-level API for performing masking and de-identification operations. Some of these functions require the [`SUPER`](privileges-provided.md) privilege.