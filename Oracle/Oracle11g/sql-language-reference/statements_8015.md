---
title: DROP FLASHBACK ARCHIVE
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_8015.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Purpose

Use the `DROP` `FLASHBACK` `ARCHIVE` clause to remove a flashback data archive from the system. This statement removes the flashback data archive and all the historical data in it, but does not drop the tablespaces that were used by the flashback data archive.

Prerequisites

You must have the `FLASHBACK` `ARCHIVE` `ADMINISTER` system privilege to drop a flashback data archive.

Syntax

drop\_flashback\_archive::=

  
[Description of the illustration ''drop\_flashback\_archive.gif''](https://docs.oracle.com/cd/E11882_01/server.112/e41084/img_text/drop_flashback_archive.htm)  

Semantics

flashback\_archive

Specify the name of the flashback data archive you want to drop.

See Also:

[CREATE FLASHBACK ARCHIVE](statements_5010.md) for information on creating flashback data archives and for some simple examples of using flashback data archives