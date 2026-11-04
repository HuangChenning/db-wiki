---
title: COMMENT
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_4009.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Purpose

Use the `COMMENT` statement to add to the data dictionary a comment about a table or table column, view, materialized view, operator, indextype, mining model, or edition.

To drop a comment from the database, set it to the empty string ' '.

Prerequisites

The object about which you are adding a comment must be in your own schema or:

- To add a comment to a table, view, or materialized view, you must have `COMMENT` `ANY` `TABLE` system privilege.
- To add a comment to an indextype, you must have the `CREATE` `ANY` `INDEXTYPE` system privilege.
- To add a comment to an operator, you must have the `CREATE` `ANY` `OPERATOR` system privilege.
- To add a comment to an edition, you must have the `CREATE` `ANY` `EDITION` system privilege, granted either directly or through a role.

Syntax