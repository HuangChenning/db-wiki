---
title: SQL Language Reference
book: SQL Language Reference
doc_id: E83703-08
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/COMMENT.html
tags:
  - oracle
  - 12c
  - sql-language-reference
---

Purpose

Use the `COMMENT` statement to add to the data dictionary a comment about a table or table column, unified audit policy, edition, indextype, materialized view, mining model, operator, or view.

To drop a comment from the database, set it to the empty string ' '.

Prerequisites

The object about which you are adding a comment must be in your own schema or:

- To add a comment to a table, view, or materialized view, you must have `COMMENT` `ANY` `TABLE` system privilege.
- To add a comment to a unified audit policy, you must have the `AUDIT` `SYSTEM` system privilege or the `AUDIT_ADMIN` role.
- To add a comment to an edition, you must have the `CREATE` `ANY` `EDITION` system privilege, granted either directly or through a role.
- To add a comment to an indextype, you must have the `CREATE` `ANY` `INDEXTYPE` system privilege.
- To add a comment to a mining model, you must have the `COMMENT` `ANY` `MINING` `MODEL` system privilege.
- To add a comment to an operator, you must have the `CREATE` `ANY` `OPERATOR` system privilege.

Syntax