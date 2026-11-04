---
title: "MySQL :: MySQL 26.7 Reference Manual :: 16 MySQL Data Dictionary"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/data-dictionary.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

## Chapter 16 MySQL Data Dictionary

MySQL Server incorporates a transactional data dictionary that stores information about database objects. In previous MySQL releases, dictionary data was stored in metadata files, nontransactional tables, and storage engine-specific data dictionaries.

This chapter describes the main features, benefits, usage differences, and limitations of the data dictionary. For other implications of the data dictionary feature, refer to the “Data Dictionary Notes” section in the [MySQL 26.7 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/26.7/en/).

Benefits of the MySQL data dictionary include:

- Simplicity of a centralized data dictionary schema that uniformly stores dictionary data. See [Section 16.1, “Data Dictionary Schema”](data-dictionary-schema.md).
- Removal of file-based metadata storage. See [Section 16.2, “Removal of File-based Metadata Storage”](data-dictionary-file-removal.md).
- Transactional, crash-safe storage of dictionary data. See [Section 16.3, “Transactional Storage of Dictionary Data”](data-dictionary-transactional-storage.md).
- Uniform and centralized caching for dictionary objects. See [Section 16.4, “Dictionary Object Cache”](data-dictionary-object-cache.md).
- A simpler and improved implementation for some [`INFORMATION_SCHEMA`](information-schema.md) tables. See [Section 16.5, “INFORMATION\_SCHEMA and Data Dictionary Integration”](data-dictionary-information-schema.md).
- Atomic DDL. See [Section 15.1.1, “Atomic Data Definition Statement Support”](atomic-ddl.md).