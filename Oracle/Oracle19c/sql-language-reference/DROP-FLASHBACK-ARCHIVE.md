---
title: DROP FLASHBACK ARCHIVE
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/DROP-FLASHBACK-ARCHIVE.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Purpose

Use the `DROP` `FLASHBACK` `ARCHIVE` clause to remove a flashback archive from the system. This statement removes the flashback archive and all the historical data in it, but does not drop the tablespaces that were used by the flashback archive.

## Prerequisites

You must have the `FLASHBACK` `ARCHIVE` `ADMINISTER` system privilege to drop a flashback archive.

## Syntax

## drop\_flashback\_archive::=

[Description of the illustration drop\_flashback\_archive.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/drop_flashback_archive.html)

## Semantics

## flashback\_archive

Specify the name of the flashback archive you want to drop.

**See Also:** [CREATE FLASHBACK ARCHIVE](CREATE-FLASHBACK-ARCHIVE.md) for information on creating flashback archives and for some simple examples of using flashback archives