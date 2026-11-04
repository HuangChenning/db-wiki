---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/DROP-FLASHBACK-ARCHIVE.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## DROP FLASHBACK ARCHIVE

Purpose

Use the `DROP` `FLASHBACK` `ARCHIVE` clause to remove a flashback archive from the system. This statement removes the flashback archive and all the historical data in it, but does not drop the tablespaces that were used by the flashback archive.

Prerequisites

You must have the `FLASHBACK` `ARCHIVE` `ADMINISTER` system privilege to drop a flashback archive.

Syntax

drop\_flashback\_archive::=

![drop_flashback_archive](img/drop_flashback_archive.gif)

> ```
> DROP FLASHBACK ARCHIVE flashback_archive;
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

flashback\_archive

Specify the name of the flashback archive you want to drop.

See Also:

[CREATE FLASHBACK ARCHIVE](CREATE-FLASHBACK-ARCHIVE.md) for information on creating flashback archives and for some simple examples of using flashback archives