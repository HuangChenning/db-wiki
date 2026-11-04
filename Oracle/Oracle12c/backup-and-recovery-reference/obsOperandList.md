---
title: Database Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: E85640-04
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/rcmrf/obsOperandList.html
tags:
  - oracle
  - 12c
  - backup-and-recovery-reference
---

Purpose

Use the `obsOperandList` subclause used to specify which criteria are used to mark backups as obsolete.

Usage Notes

Using both `RECOVERY WINDOW` and `REDUNDANCY` in a single `REPORT OBSOLETE` or `DELETE OBSOLETE` command is not supported.

Syntax

obsOperandList::=

![obsoperandlist](img/obsoperandlist.gif)

> {RECOVERY WINDOW OF integer DAYS | REDUNDANCY integer} \[ {RECOVERY WINDOW OF integer DAYS | REDUNDANCY integer}\]...


Semantics

obsOperandList

| Syntax Element | Description |
| --- | --- |
| `RECOVERY WINDOW OF` `integer` `DAYS` | Reports as obsolete those backup sets and image copies that are not needed to recover the database to any point within the last `integer` days.  See Also: `CONFIGURE` for an explanation of the recovery window |
| `REDUNDANCY` `integer` | Specifies the minimum level of redundancy considered necessary for a backup set or image copy to be obsolete.  A data file copy is obsolete if there are at least `integer` more recent backup sets or image copies of this file; a data file backup set is obsolete if there are at least `integer` more recent backup sets or image copies of each data file contained in the backup set. For example, `REDUNDANCY` `2` means that there must be at least two more recent backup sets or image copies of a data file for any other backup set or image copy to be obsolete. |

Example

Example 4-33 Deleting Obsolete Backups

The following command deletes all backups and copies not needed to recover the database to an SCN within the last 30 days:

```
DELETE OBSOLETE RECOVERY WINDOW OF 30 DAYS;
```