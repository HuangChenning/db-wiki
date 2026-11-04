---
title: "MySQL :: MySQL 26.10 Reference Manual :: 8.5.2 MySQL Enterprise Data Masking Components"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/data-masking-components.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 8.5.2 MySQL Enterprise Data Masking Components

MySQL Enterprise Data Masking implements these elements:

- A table for persistent storage of dictionaries and terms.
- A component named `component_masking` that implements masking functionality and exposes it as service interface for developers.
	Developers who wish to incorporate the same service functions used by `component_masking` should consult the `internal\components\masking\component_masking.h` file in a MySQL source distribution or https://dev.mysql.com/doc/dev/mysql-server/latest.
- A component named `component_masking_functions` that provides loadable functions.
	The set of loadable functions enables an SQL-level API for performing masking and de-identification operations. Some of the functions require the [`MASKING_DICTIONARIES_ADMIN`](privileges-provided.md) dynamic privilege.