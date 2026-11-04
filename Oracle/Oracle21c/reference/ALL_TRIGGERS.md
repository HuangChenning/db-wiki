---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_TRIGGERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.126 ALL\_TRIGGERS

`ALL_TRIGGERS` describes the triggers on tables accessible to the current user.

If the user has the `CREATE ANY TRIGGER` privilege, then this view describes all triggers in the database.

Related Views

- `DBA_TRIGGERS` describes all triggers in the database.
- `USER_TRIGGERS` describes the triggers owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the trigger |
| `TRIGGER_NAME` | `VARCHAR2(128)` |  | Name of the trigger |
| `TRIGGER_TYPE` | `VARCHAR2(16)` |  | When the trigger fires:  - `BEFORE STATEMENT` - `BEFORE EACH ROW` - `AFTER STATEMENT` - `AFTER EACH ROW` - `INSTEAD OF` - `COMPOUND` |
| `TRIGGERING_EVENT` | `VARCHAR2(246)` |  | DML, DDL, or database event that fires the trigger  See Also: [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=LNPLS020) for additional information about triggers and triggering events. |
| `TABLE_OWNER` | `VARCHAR2(128)` |  | Owner of the table on which the trigger is defined |
| `BASE_OBJECT_TYPE` | `VARCHAR2(18)` |  | Base object on which the trigger is defined:  - `TABLE` - `VIEW` - `SCHEMA` - `DATABASE` |
| `TABLE_NAME` | `VARCHAR2(128)` |  | If the base object type of the trigger is `SCHEMA` or `DATABASE`, then this column is NULL; if the base object type of the trigger is `TABLE` or `VIEW`, then this column indicates the table or view name on which the trigger is defined |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Name of the nested table column (if a nested table trigger), else NULL |
| `REFERENCING_NAMES` | `VARCHAR2(422)` |  | Names used for referencing `OLD` and `NEW` column values from within the trigger |
| `WHEN_CLAUSE` | `VARCHAR2(4000)` |  | Must evaluate to `TRUE` for `TRIGGER_BODY` to execute |
| `STATUS` | `VARCHAR2(8)` |  | Indicates whether the trigger is enabled (`ENABLED`) or disabled (`DISABLED`); a disabled trigger will not fire |
| `DESCRIPTION` | `VARCHAR2(4000)` |  | Trigger description; useful for re-creating a trigger creation statement |
| `ACTION_TYPE` | `VARCHAR2(11)` |  | Action type of the trigger body:  - `CALL` - `PL/SQL` |
| `TRIGGER_BODY` | `LONG` |  | Statements executed by the trigger when it fires |
| `CROSSEDITION` | `VARCHAR2(7)` |  | Type of crossedition trigger:  - `FORWARD` - `REVERSE` - `NO` |
| `BEFORE_STATEMENT` | `VARCHAR2(3)` |  | Indicates whether the trigger has a `BEFORE STATEMENT` section (`YES`) or not (`NO`) |
| `BEFORE_ROW` | `VARCHAR2(3)` |  | Indicates whether the trigger has a `BEFORE EACH ROW` section (`YES`) or not (`NO`) |
| `AFTER_ROW` | `VARCHAR2(3)` |  | Indicates whether the trigger has an `AFTER EACH ROW` section (`YES`) or not (`NO`) |
| `AFTER_STATEMENT` | `VARCHAR2(3)` |  | Indicates whether the trigger has an `AFTER STATEMENT` section (`YES`) or not (`NO`) |
| `INSTEAD_OF_ROW` | `VARCHAR2(3)` |  | Indicates whether the trigger has an `INSTEAD OF` section (`YES`) or not (`NO`) |
| `FIRE_ONCE` | `VARCHAR2(3)` |  | Indicates whether the trigger will fire only for user processes making changes (`YES`) or whether the trigger will also fire for Replication Apply or SQL Apply processes (`NO`) |
| `APPLY_SERVER_ONLY` | `VARCHAR2(3)` |  | Indicates whether the trigger will only fire for a Replication Apply or SQL Apply process (`YES`) or not (`NO`). If set to `YES`, then the setting of `FIRE_ONCE` does not matter.  See Also: the `DBMS_DDL.SET_TRIGGER_FIRING_PROPERTY` procedure |