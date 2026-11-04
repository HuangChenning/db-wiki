# db-wiki

[中文](README.zh-CN.md) · **English**

A Markdown reading library for Oracle, MySQL, Dameng, and HighGo database documentation, organized by version and manual for browsing, full-text search, and offline reading.

Start with [Oracle 19c](Oracle/Oracle19c/catalog.md), [MySQL 8.4](MySQL/MySQL8.4/catalog.md), [Dameng DM8](dameng/dm8/catalog.md), or [HighGo V9](highgo/highgov9/catalog.md), or choose a manual by task below.

## Overview

For database administrators and developers, this collection covers database concepts, SQL, administration, performance tuning, backup and recovery, and high availability. Chapters retain source metadata for checking the original documentation. Oracle and MySQL chapters are mainly in English; Dameng and HighGo chapters are mainly in Chinese.

## Examples and version entry points

| Database version | Manual directories | Reading entry points |
| --- | ---: | --- |
| Oracle 11g | 45 | [Version catalog](Oracle/Oracle11g/catalog.md) · [Database Concepts](Oracle/Oracle11g/concepts/contents.md) |
| Oracle 12c | 12 | [Version catalog](Oracle/Oracle12c/catalog.md) · [Database Concepts](Oracle/Oracle12c/concepts/contents.md) |
| Oracle 19c | 17 | [Version catalog](Oracle/Oracle19c/catalog.md) · [Database Concepts](Oracle/Oracle19c/concepts/contents.md) |
| Oracle 21c | 23 | [Version catalog](Oracle/Oracle21c/catalog.md) · [Database Concepts](Oracle/Oracle21c/concepts/contents.md) |
| MySQL 5.6 | 2 | [Version catalog](MySQL/MySQL5.6/catalog.md) · [Reference Manual](MySQL/MySQL5.6/reference-manual/contents.md) |
| MySQL 5.7 | 2 | [Version catalog](MySQL/MySQL5.7/catalog.md) · [Reference Manual](MySQL/MySQL5.7/reference-manual/contents.md) |
| MySQL 8.0 | 2 | [Version catalog](MySQL/MySQL8.0/catalog.md) · [Reference Manual](MySQL/MySQL8.0/reference-manual/contents.md) |
| MySQL 8.4 | 1 | [Version catalog](MySQL/MySQL8.4/catalog.md) · [Reference Manual](MySQL/MySQL8.4/reference-manual/contents.md) |
| MySQL 9.7 | 2 | [Version catalog](MySQL/MySQL9.7/catalog.md) · [Reference Manual](MySQL/MySQL9.7/reference-manual/contents.md) |
| MySQL 26.7 | 1 | [Version catalog](MySQL/MySQL26.7/catalog.md) · [Reference Manual](MySQL/MySQL26.7/reference-manual/contents.md) |
| MySQL 26.10 | 1 | [Version catalog](MySQL/MySQL26.10/catalog.md) · [Reference Manual](MySQL/MySQL26.10/reference-manual/contents.md) |
| Dameng DM7 | 21 | [Version catalog](dameng/dm7/catalog.md) · [System Administrator's Manual](dameng/dm7/administrator/contents.md) |
| Dameng DM8 | 56 | [Version catalog](dameng/dm8/catalog.md) · [System Administration](dameng/dm8/administrator/contents.md) |
| HighGo V4.5 | 23 | [Version catalog](highgo/highgov45/catalog.md) · [Installation Manual](highgo/highgov45/develop-installation-manual/contents.md) |
| HighGo V9 | 24 | [Version catalog](highgo/highgov9/catalog.md) · [Administrator's Guide](highgo/highgov9/safety-administrator-guide/contents.md) |

For example, open the [Oracle 19c Database Concepts contents](Oracle/Oracle19c/concepts/contents.md), then [Introduction to Oracle Database](Oracle/Oracle19c/concepts/introduction-to-oracle-database.md) to read a full chapter. Its opening `source` field records the official page URL.

### Browse by task

The Oracle links below use **19c**. For other versions, start with the corresponding version catalog.

| Task | Oracle 19c | Dameng DM8 |
| --- | --- | --- |
| Manage instances and database objects | [Administrator's Guide](Oracle/Oracle19c/administrators-guide/contents.md) | [System Administrator's Manual](dameng/dm8/administrator/contents.md) |
| Look up SQL syntax and functions | [SQL Language Reference](Oracle/Oracle19c/sql-language-reference/contents.md) | [SQL Language Manual](dameng/dm8/sql-language/contents.md) |
| Write stored procedures and program blocks | [PL/SQL Language Reference](Oracle/Oracle19c/pl-sql-language-reference/contents.md) | [SQL Programming](dameng/dm8/sql-programming/contents.md) |
| Analyze performance and tune SQL | [SQL Tuning Guide](Oracle/Oracle19c/sql-tuning-guide/contents.md) | [SQL Tuning](dameng/dm8/administrator/sql-tuning.md) |
| Back up, restore, and recover | [Backup and Recovery User's Guide](Oracle/Oracle19c/backup-and-recovery-users-guide/contents.md) | [Backup and Restore](dameng/dm8/backup-restore/contents.md) |
| Look up parameters and system views | [Database Reference](Oracle/Oracle19c/reference/contents.md) | [Dynamic Views](dameng/dm8/administrator/dynamic-management.md) |

## How it works

1. **Choose a version**: open its `catalog.md` from the table above and select a manual by topic.
2. **Choose a chapter**: open the manual's `contents.md` and browse in book order. Paths shown in backticks in a version catalog are relative to that catalog's directory.
3. **Check the source**: inspect the chapter's opening `version`, `doc_id` (when present), and `source` fields to confirm the applicable version and original page.

## Quick start

Follow the links on GitHub to read without installing a database. For offline reading, clone the repository and open it in an editor that supports Markdown:

```bash
git clone https://github.com/HuangChenning/db-wiki.git
cd db-wiki
```

Open `Oracle/Oracle19c/concepts/contents.md` and follow the first chapter link to start reading.

### Local full-text search

With [ripgrep](https://github.com/BurntSushi/ripgrep) installed, run these commands from the repository root. The `-g '*.md'` filter limits the search to Markdown files:

```bash
# Find transaction-related chapters in Oracle 19c Database Concepts
rg -l -i -g '*.md' 'transaction' Oracle/Oracle19c/concepts

# Find DMRMAN references in the Dameng backup manual, with line numbers
rg -n -g '*.md' 'DMRMAN' dameng/dm8/backup-restore
```

## Limitations and coverage

- **Use the matching version**: parameters, syntax, and features may differ between releases. Check examples against your database version before applying them.
- **Coverage is selective**: this is an entry point to the collected manuals, rather than the vendor's entire documentation library. Updates may lag behind official sources. Some version catalogs note document-number differences between online manuals and local PDFs.
- **Chapter languages are preserved**: the two READMEs provide equivalent navigation; they do not imply that every chapter has a bilingual translation.
- **Conversion can affect formatting**: complex tables, images, and cross-references may contain formatting or parsing errors. Check the chapter's official source before critical operations.
- **Sources and copyright**: original documentation remains the property of its respective rights holders. This repository currently has no `LICENSE` file; inclusion does not constitute an additional license grant.

## Contributing

When reporting a problem, include the database version, manual name, chapter path, and specific issue. For content discrepancies, include the chapter's `source` URL. When adding or revising documentation, preserve the version directories, `catalog.md`, `contents.md`, and source metadata. Store new images in the corresponding manual's `img/` directory.

After adding, removing, or moving manuals, update the version catalog and the links and manual counts in both READMEs.
