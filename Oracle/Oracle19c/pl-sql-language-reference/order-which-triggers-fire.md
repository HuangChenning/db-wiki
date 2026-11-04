---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/order-which-triggers-fire.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Order in Which Triggers Fire

If two or more triggers with different timing points are defined for the same statement on the same table, then they fire in this order:

1. All `BEFORE` `STATEMENT` triggers
2. All `BEFORE` `EACH` `ROW` triggers
3. All `AFTER` `EACH` `ROW` triggers
4. All `AFTER` `STATEMENT` triggers

If it is practical, replace the set of individual triggers with different timing points with a single compound trigger that explicitly codes the actions in the order you intend. For information about compound triggers, see " [Compound DML Triggers](dml-triggers.md) ".

If you are creating two or more triggers with the same timing point, and the order in which they fire is important, then you can control their firing order using the `FOLLOWS` and `PRECEDES` clauses (see " [FOLLOWS | PRECEDES](CREATE-TRIGGER-statement.md) ").

If multiple compound triggers are created on a table, then:

- All `BEFORE` `STATEMENT` sections run at the `BEFORE` `STATEMENT` timing point, `BEFORE` `EACH` `ROW` sections run at the `BEFORE` `EACH` `ROW` timing point, and so forth.
	If trigger execution order was specified using the `FOLLOWS` clause, then the `FOLLOWS` clause determines the order of execution of compound trigger sections. If `FOLLOWS` is specified for some but not all triggers, then the order of execution of triggers is guaranteed only for those that are related using the `FOLLOWS` clause.
- All `AFTER` `STATEMENT` sections run at the `AFTER` `STATEMENT` timing point, `AFTER` `EACH` `ROW` sections run at the `AFTER` `EACH` `ROW` timing point, and so forth.
	If trigger execution order was specified using the `PRECEDES` clause, then the `PRECEDES` clause determines the order of execution of compound trigger sections. If `PRECEDES` is specified for some but not all triggers, then the order of execution of triggers is guaranteed only for those that are related using the `PRECEDES` clause.
	Note:
	`PRECEDES` applies only to reverse crossedition triggers, which are described in [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ADFNS99909).

The firing of compound triggers can be interleaved with the firing of simple triggers.

When one trigger causes another trigger to fire, the triggers are said to be cascading. The database allows up to 32 triggers to cascade simultaneously. To limit the number of trigger cascades, use the initialization parameter `OPEN_CURSORS` (described in [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=REFRN10137)), because a cursor opens every time a trigger fires.