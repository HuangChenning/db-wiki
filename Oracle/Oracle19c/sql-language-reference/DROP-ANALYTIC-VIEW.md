---
title: DROP ANALYTIC VIEW
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/DROP-ANALYTIC-VIEW.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Purpose

Use the `DROP` `ANALYTIC` `VIEW` statement to drop an analytic view. An `ANALYTIC` `VIEW` object is a component of analytic views.

## Prerequisites

To drop an analytic view in your own schema, you must have the `DROP` `ANALYTIC` `VIEW` system privilege. To drop an analytic view in another user’s schema, you must have the `DROP` `ANY` `ANALYTIC` `VIEW` system privilege.

## Syntax

## drop\_analytic\_view::=

[Description of the illustration drop\_analytic\_view.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/drop_analytic_view.html)

## Semantics

## IF EXISTS

Specify `IF EXISTS` to drop an existing analytic view.

**Note:** You can only use `IF EXISTS` from Release 19.28 and up.

## schema

Specify the schema in which the analytic view exists. If you do not specify a schema, then Oracle Database looks for the analytic view in your own schema.

## analytic\_view\_name

Specify the name of the analytic view to drop.

## Example

The following statement drops the specified analytic view object:

```md
DROP ANALYTIC VIEW sales_av;
```