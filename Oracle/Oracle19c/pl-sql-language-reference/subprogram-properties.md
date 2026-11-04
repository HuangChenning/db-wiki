---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/subprogram-properties.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Subprogram Properties

Each subprogram property can appear only once in the subprogram declaration. The properties can appear in any order. Properties appear before the `IS` or `AS` keyword in the subprogram heading. The properties cannot appear in nested subprograms.

Only the `ACCESSIBLE BY` property can appear in package subprograms. Standalone subprograms may have the following properties in their declaration.