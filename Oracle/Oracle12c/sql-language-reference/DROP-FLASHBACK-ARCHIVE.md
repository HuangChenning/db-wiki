---
title: SQL Language Reference
book: SQL Language Reference
doc_id: E83703-08
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/DROP-FLASHBACK-ARCHIVE.html
tags:
  - oracle
  - 12c
  - sql-language-reference
---

Purpose

Use the `DROP` `FLASHBACK` `ARCHIVE` clause to remove a flashback data archive from the system. This statement removes the flashback data archive and all the historical data in it, but does not drop the tablespaces that were used by the flashback data archive.

Prerequisites

You must have the `FLASHBACK` `ARCHIVE` `ADMINISTER` system privilege to drop a flashback data archive.

Syntax

drop\_flashback\_archive::=

![drop_flashback_archive](img/drop_flashback_archive.gif)

> ```
> DROP FLASHBACK ARCHIVE flashback_archive;
> ```


Semantics

flashback\_archive

Specify the name of the flashback data archive you want to drop.

See Also:

[CREATE FLASHBACK ARCHIVE](CREATE-FLASHBACK-ARCHIVE.md) for information on creating flashback data archives and for some simple examples of using flashback data archives