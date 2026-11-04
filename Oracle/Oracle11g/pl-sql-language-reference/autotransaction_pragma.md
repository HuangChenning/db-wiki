---
title: AUTONOMOUS_TRANSACTION Pragma
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/autotransaction_pragma.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

The `AUTONOMOUS_TRANSACTION` pragma marks a routine as autonomous; that is, independent of the main transaction.

In this context, a routine is one of these:

- Schema-level (not nested) anonymous PL/SQL block
- Standalone, package, or nested subprogram
- Method of an ADT
- Noncompound trigger

Topics

Syntax

autonomous\_trans\_pragma::=

  
[Description of the illustration autonomous\_trans\_pragma.gif](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/img_text/autonomous_trans_pragma.htm)  

Examples

- [Example 6-44, "Declaring Autonomous Function in Package"](static.md)
- [Example 6-45, "Declaring Autonomous Standalone Procedure"](static.md)
- [Example 6-46, "Declaring Autonomous PL/SQL Block"](static.md)
- [Example 6-47, "Autonomous Trigger Logs INSERT Statements"](static.md)
- [Example 6-48, "Autonomous Trigger Uses Native Dynamic SQL for DDL"](static.md)
- [Example 6-49, "Invoking Autonomous Function"](static.md)