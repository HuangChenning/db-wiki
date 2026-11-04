---
title: DROP MATERIALIZED ZONEMAP
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/DROP-MATERIALIZED-ZONEMAP.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Purpose

Use the `DROP` `MATERIALIZED` `ZONEMAP` statement to remove an existing zone map from the database.

## Prerequisites

The zone map must be in your own schema or you must have the `DROP` `ANY` `MATERIALIZED` `VIEW` system privilege. You must also have the privileges to drop the internal table and indexes that the database uses to maintain the zone map data.

**See Also:** [DROP TABLE](DROP-TABLE.md) and [DROP INDEX](DROP-INDEX.md) for information on privileges required to drop objects that the database uses to maintain the zone map

## Syntax

## drop\_materialized\_zonemap::=

[Description of the illustration drop\_materialized\_zonemap.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/drop_materialized_zonemap.html)

## Semantics

## IF EXISTS

Specify `IF EXISTS` to drop an existing zone map.

## schema

Specify the schema containing the zone map. If you omit *schema*, then Oracle Database assumes the zone map is in your own schema.

## zonemap\_name

Specify the name of the existing zone map to be dropped.

## Example

**Dropping a Zone Map: Examples**

The following statement drops the zone map `sales_zmap`:

```md
DROP MATERIALIZED ZONEMAP sales_zmap;
```