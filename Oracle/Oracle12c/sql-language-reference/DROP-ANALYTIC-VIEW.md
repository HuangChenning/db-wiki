---
title: SQL Language Reference
book: SQL Language Reference
doc_id: E83703-08
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/DROP-ANALYTIC-VIEW.html
tags:
  - oracle
  - 12c
  - sql-language-reference
---

Purpose

Use the `DROP` `ANALYTIC` `VIEW` statement to drop an analytic view. An `ANALYTIC` `VIEW` object is a component of analytic views.

Prerequisites

To drop an analytic view in your own schema, you must have the `DROP` `ANALYTIC` `VIEW` system privilege. To drop an analytic view in another user's schema, you must have the `DROP` `ANY` `ANALYTIC` `VIEW` system privilege.

Syntax

drop\_analytic\_view::=

![drop_analytic_view](img/drop_analytic_view.gif)

> ```
> DROP ANALYTIC VIEW [ schema. ] analytic_view_name;
> ```


Semantics

schema

Specify the schema in which the analytic view exists. If you do not specify a schema, then Oracle Database looks for the analytic view in your own schema.

analytic\_view\_name

Specify the name of the analytic view to drop.

Example

The following statement drops the specified analytic view object:

```
DROP ANALYTIC VIEW sales_av;
```