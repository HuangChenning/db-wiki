---
title: ALTER OUTLINE
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_2005.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Purpose

Note:

Oracle strongly recommends that you use SQL plan management for new applications. SQL plan management creates SQL plan baselines, which offer superior SQL performance stability compared with stored outlines.

You can migrate existing stored outlines to SQL plan baselines by using the `MIGRATE_STORED_OUTLINE` function of the `DBMS_SPM` package or Enterprise Manager DB Control. When the migration is complete, the stored outlines are marked as migrated and can be removed. You can drop all migrated stored outlines on your system by using the `DROP_MIGRATED_STORED_OUTLINE` function of the `DBMS_SPM` package.

See Also: [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/optplanmgmt.htm#PFGRF007) for more information about SQL plan management and [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_spm.htm#ARPLS150) for information about the `DBMS_SPM` package

Use the `ALTER` `OUTLINE` statement to rename a stored outline, reassign it to a different category, or regenerate it by compiling the outline's SQL statement and replacing the old outline data with the outline created under current conditions.

See Also:

[CREATE OUTLINE](statements_6005.md) and [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/optplanmgmt.htm#PFGRF007) for more information on outlines

Prerequisites

To modify an outline, you must have the `ALTER` `ANY` `OUTLINE` system privilege.

Syntax

alter\_outline::=

![alter_outline](img/alter_outline.gif)

> ```
> ALTER OUTLINE [ PUBLIC | PRIVATE ] outline
>   { REBUILD
>   | RENAME TO new_outline_name
>   | CHANGE CATEGORY TO new_category_name
>   | { ENABLE | DISABLE }
>   } ...
>   ;
> ```
  

Semantics

PUBLIC | PRIVATE

Specify `PUBLIC` if you want to modify the public version of this outline. This is the default.

Specify `PRIVATE` if you want to modify an outline that is private to the current session and whose data is stored in the current parsing schema.

outline

Specify the name of the outline to be modified.

REBUILD

Specify `REBUILD` to regenerate the execution plan for `outline` using current conditions.

See Also:

"Rebuilding an Outline: Example"

RENAME TO Clause

Use the `RENAME` `TO` clause to specify an outline name to replace `outline`.

CHANGE CATEGORY TO Clause

Use the `CHANGE` `CATEGORY` `TO` clause to specify the name of the category into which the `outline` will be moved.

ENABLE | DISABLE

Use this clause to selectively enable or disable this outline. Outlines are enabled by default. The `DISABLE` keyword lets you disable one outline without affecting the use of other outlines.

Examples

Rebuilding an Outline: Example The following statement regenerates a stored outline called `salaries` by compiling the text of the outline and replacing the old outline data with the outline created under current conditions.

```
ALTER OUTLINE salaries REBUILD;
```