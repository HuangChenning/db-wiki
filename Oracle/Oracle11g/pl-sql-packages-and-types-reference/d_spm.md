---
title: DBMS_SPM
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_spm.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 136 DBMS\_SPM

The `DBMS_SPM` package supports the SQL plan management feature by providing an interface for the DBA or other user to perform controlled manipulation of plan history and SQL plan baselines maintained for various SQL statements.

See Also:

For more information about ["Using SQL Plan Management"](https://docs.oracle.com/cd/E11882_01/server.112/e41573/optplanmgmt.htm#PFGRF007) in the Oracle Database Performance Tuning Guide

This chapter contains the following topics:

---

## Using DBMS\_SPM

- Overview
- Security Model
- Constants
- Examples

---

### Overview

The `DBMS_SPM` package allows the user to manage SQL execution plans using SQL plan management. SQL plan management prevents performance regressions resulting from sudden changes to the execution plan of a SQL statement by recording and evaluating the execution plans of SQL statements over time, and builds SQL plan baselines composed of a set of existing plans known to be efficient. The SQL plan baselines are then used to preserve performance of corresponding SQL statements, regardless of changes occurring in the system. Common usage scenarios where SQL plan management can improve or preserve SQL performance include:

- A database upgrade that installs a new optimizer version usually results in plan changes for a small percentage of SQL statements, with most of the plan changes resulting in either no performance change or improvement. However, certain plan changes may cause performance regressions. The use of SQL plan baselines significantly minimizes potential performance regressions resulting from a database upgrade.
- Ongoing system and data changes can impact plans for some SQL statements, potentially causing performance regressions. The use of SQL plan baselines helps to minimize performance regressions and stabilize SQL performance.
- Deployment of new application modules means introducing new SQL statements into the system. The application software may use appropriate SQL execution plans developed under a standard test configuration for the new SQL statements. If the system production configuration differs significantly from the test configuration, SQL plan baselines can be evolved over time to produce better performance.

---

### Security Model

The package is owned by `SYS`. The `EXECUTE` package privilege is required to execute its procedures. Any user granted the `ADMINISTER` `SQL` `MANAGEMENT` `OBJECT` privilege is able to execute the `DBMS_SPM` package.

---

### Constants

The `DBMS_SPM` package uses the constants shown in Table 136-1, "DBMS\_SPM Constants". These constants are defined as standard input for the `time_limit` parameter of the EVOLVE\_SQL\_PLAN\_BASELINE Function.

Table 136-1 DBMS\_SPM Constants

| Constant | Type | Value | Description |
| --- | --- | --- | --- |
| `AUTO_LIMIT` | `INTEGER` | `2147483647` | Oracle determines the appropriate time spent by the EVOLVE\_SQL\_PLAN\_BASELINE Function. |
| `NO_LIMIT` | `INTEGER` | `2147483647 -1` | There is no limit to the time spent by the EVOLVE\_SQL\_PLAN\_BASELINE Function. |

---

### Examples

Detailed examples are located under the following topics:

- [Migrating Stored Outlines to SQL Plan Baselines](https://docs.oracle.com/cd/E11882_01/server.112/e41573/optplanmgmt.htm#PFGRF3616)
- [Migrating Outlines to Utilize SQL Plan Management Features](https://docs.oracle.com/cd/E11882_01/server.112/e41573/optplanmgmt.htm#PFGRF95139)
- [Migrating Outlines to Preserve Stored Outline Behavior](https://docs.oracle.com/cd/E11882_01/server.112/e41573/optplanmgmt.htm#PFGRF95140)
- [Performing Follow-Up Tasks After Stored Outline Migratio](https://docs.oracle.com/cd/E11882_01/server.112/e41573/optplanmgmt.htm#PFGRF95141) n

---

## Data Structures

The `DBMS_SPM` package defines a `TABLE` type.

Table Types

- NAMELIST Table Type

---

### NAMELIST Table Type

This type allows for a list of names as an input parameter.

Syntax

```
TYPE  name_list  IS TABLE OF VARCHAR2(30);
```

---

## Summary of DBMS\_SPM Subprograms

This table list the package subprograms in alphabetical order.

Table 136-2 DBMS\_SPM Package Subprograms

| Subprogram | Description |
| --- | --- |
| ALTER\_SQL\_PLAN\_BASELINE Function | Changes an attribute of a single plan or all plans associated with a SQL statement using the attribute name/value format |
| CONFIGURE Procedure | Sets configuration options for SQL management base, in parameter/value format |
| CREATE\_STGTAB\_BASELINE Procedure | Creates a staging table that used for transporting SQL plan baselines from one system to another |
| DROP\_SQL\_PLAN\_BASELINE Function | drops a single plan, or all plans associated with a SQL statement |
| EVOLVE\_SQL\_PLAN\_BASELINE Function | Evolves SQL plan baselines associated with one or more SQL statements |
| LOAD\_PLANS\_FROM\_CURSOR\_CACHE Functions | Loads one or more plans present in the cursor cache for a SQL statement |
| LOAD\_PLANS\_FROM\_SQLSET Function | Loads plans stored in a SQL tuning set (STS) into SQL plan baselines |
| MIGRATE\_STORED\_OUTLINE Functions | Migrates existing stored outlines to SQL plan baselines |
| PACK\_STGTAB\_BASELINE Function | Packs (exports) SQL plan baselines from SQL management base into a staging table |
| UNPACK\_STGTAB\_BASELINE Function | Unpacks (imports) SQL plan baselines from a staging table into SQL management base |

---

### ALTER\_SQL\_PLAN\_BASELINE Function

This function changes an attribute of a single plan or all plans associated with a SQL statement using the attribute name/value format.

Syntax

```
DBMS_SPM.ALTER_SQL_PLAN_BASELINE (
   sql_handle        IN VARCHAR2 := NULL,
   plan_name         IN VARCHAR2 := NULL,
   attribute_name    IN VARCHAR2,
   attribute_value   IN VARCHAR2)
 RETURN PLS_INTEGER;
```

Parameters

Table 136-3 ALTER\_SQL\_PLAN\_BASELINE Function Parameters

| Parameter | Description |
| --- | --- |
| `sql_handle` | SQL statement handle. It identifies plans associated with a SQL statement for an attribute change. If `NULL` then `plan_name` must be specified. |
| `plan_name` | Plan name. It identifies a specific plan. Default `NULL` means set the attribute for all plans associated with a SQL statement identified by `sql_handle`. If `NULL` then `sql_handle` must be specified. |
| `attribute_name` | Name of plan attribute to set (see table below). |
| `attribute_value` | Value of plan attribute to use (see table below) |

Table 136-4 Names & Values for ALTER\_SQL\_PLAN\_BASELINE Function Parameters

| Name | Description | Possible Values |
| --- | --- | --- |
| `enabled` | ' `YES` ' means the plan is available for use by the optimizer. It may or may not be used depending on `accepted` status. | ' `YES` ' or ' `NO` ' |
| `fixed` | ' `YES` ' means the SQL plan baseline is not evolved over time. A fixed plan takes precedence over a non-fixed plan. | ' `YES` ' or ' `NO` ' |
| `autopurge` | ' `YES` ' means the plan is purged if it is not used for a time period. ' `NO` ' means it is never purged. | ' `YES` ' or ' `NO` ' |
| `plan_name` | Name of the plan | String of up to 30-characters |
| `description` | Plan description. | String of up to 500-characters |

Return Values

The number of plans altered.

Usage Notes

When a single plan is specified, one of various statuses, or plan name, or description can be altered. When all plans for a SQL statement are specified, one of various statuses, or description can be altered. This function can be called numerous times, each time setting a different plan attribute of same plan(s) or different plan(s).

---

### CONFIGURE Procedure

This procedure sets configuration options for SQL management base, in parameter/value format. This function can be called numerous times, each time setting a different configuration option.

Syntax

```
DBMS_SPM.CONFIGURE (
   parameter_name    IN VARCHAR2,
   parameter_value   IN NUMBER);
```

Parameters

Table 136-5 CONFIGURE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `parameter_name` | Name of parameter to set (see table below) |
| `parameter_value` | Value of parameter to use (see table below) |

Table 136-6 Names & Values for CONFIGURE Procedure Parameters

| Name | Description | Possible Values | Default Value |
| --- | --- | --- | --- |
| `space_budget_percent` | Maximum percent of `SYSAUX` space that can be used for SQL management base | 1,2, …, 50 | 10 |
| `plan_retention_weeks` | Number of weeks to retain unused plans before they are purged | 5,6, …, 523 | 53 |

Usage Notes

- The default space budget for SQL management base is no more than ten percent of the size of `SYSAUX` tablespace. The space budget can be set to a maximum of 50%. The default unused plan retention period is one year and one week, which means a plan will be automatically purged if it has not been used for more than a year. The retention period can be set to a maximum of 523 weeks (i.e. a little over 10 years).
- When the space occupied by SQL management base exceeds the defined space budget limit, a weekly database alert is generated.

---

### CREATE\_STGTAB\_BASELINE Procedure

This procedure creates a staging table used for transporting SQL plan baselines from one system to another.

Syntax

```
DBMS_SPM.CREATE_STGTAB_BASELINE (
   table_name        IN VARCHAR2,
   table_owner       IN VARCHAR2 := NULL,
   tablespace_name   IN VARCHAR2 := NULL);
```

Parameters

Table 136-7 CREATE\_STGTAB\_BASELINE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `table_name` | Name of staging table to create for the purpose of packing and unpacking SQL plan baselines |
| `table_owner` | Name of owner of the staging table. Default `NULL` means current schema is the table owner. |
| `tablespace_name` | Name of tablespace. Default NULL means create staging table in the default tablespace. |

Usage Notes

The creation of staging table is the first step. To migrate SQL plan baselines from one system to another, the user/DBA has to perform a series of steps as follows:

1. Create a staging table in the source system
2. Select SQL plan baselines in the source system and pack them into the staging table
3. Export staging table into a flat file using Oracle EXP utility or Data Pump
4. Transfer flat file to the target system
5. Import staging table from the flat file using Oracle IMP utility or Data Pump
6. Select SQL plan baselines from the staging table and unpack them into the target system

---

### DROP\_SQL\_PLAN\_BASELINE Function

This function drops a single plan, or all plans associated with a SQL statement.

Syntax

```
DBMS_SPM.DROP_SQL_PLAN_BASELINE (
   sql_handle     IN VARCHAR2 := NULL,
   plan_name      IN VARCHAR2 := NULL)
RETURN PLS_INTEGER;
```

Parameters

Table 136-8 DROP\_SQL\_PLAN\_BASELINE Function Parameters

| Parameter | Description |
| --- | --- |
| `sql_handle` | SQL statement handle. It identifies plans associated with a SQL statement that are to be dropped. If `NULL` then `plan_name` must be specified. |
| `plan_name` | Plan name. It identifies a specific plan. Default `NULL` means to drop all plans associated with the SQL statement identified by `sql_handle`. |

Return Values

The number of plans dropped

---

### EVOLVE\_SQL\_PLAN\_BASELINE Function

This function evolves SQL plan baselines associated with one or more SQL statements. A SQL plan baseline is evolved when one or more of its non-accepted plans is changed to an accepted plan or plans. If interrogated by the user (parameter `verify` = ' `YES` '), the execution performance of each non-accepted plan is compared against the performance of a plan chosen from the associated SQL plan baseline. If the non-accepted plan performance is found to be better than SQL plan baseline performance, the non-accepted plan is changed to an accepted plan provided such action is permitted by the user (parameter `commit` = 'YES').

The second form of the function employs a plan list format.

Syntax

```
DBMS_SPM.EVOLVE_SQL_PLAN_BASELINE (
   sql_handle   IN VARCHAR2 := NULL,
   plan_name    IN VARCHAR2 := NULL,
   time_limit   IN INTEGER  := DBMS_SPM.AUTO_LIMIT,
   verify       IN VARCHAR2 := 'YES',
   commit       IN VARCHAR2 := 'YES')
  RETURN CLOB;

DBMS_SPM.EVOLVE_SQL_PLAN_BASELINE (
   plan_list    IN DBMS_SPM.NAME_LIST,
   time_limit   IN INTEGER  := DBMS_SPM.AUTO_LIMIT,
   verify       IN VARCHAR2 := 'YES',
   commit       IN VARCHAR2 := 'YES')
  RETURN CLOB;
```

Parameters

Table 136-9 EVOLVE\_SQL\_PLAN\_BASELINE Function Parameters

| Parameter | Description |
| --- | --- |
| `sql_handle` | SQL statement identifier. Unless `plan_name` is specified, `NULL` means to consider all statements with non-accepted plans in their SQL plan baselines. |
| `plan_name` | Plan identifier. Default `NULL` means to consider all non- accepted plans in the SQL plan baseline of either the identified SQL statement or all SQL statements if `sql_handle` is `NULL`. |
| `plan_list` | A list of plan names. Each plan in the list can belong to same or different SQL statement. |
| `time_limit` | Time limit in number of minutes. This applies only if `verify` = ' `YES` '. The time limit is global and it is used as follows: The time limit for first non-accepted plan verification is set equal to the input value; the time limit for second non-accepted plan verification is set equal to (input value - time spent in first plan verification); and so on.  - `DBMS_SPM`.`AUTO_LIMIT` (Default) lets the system choose an appropriate time limit based on the number of plan verifications required to be done. - `DBMS_SPM`.`NO_LIMIT` means there is no time limit. - A positive integer value represents a user specified time limit. |
| `verify` | Specifies whether to execute the plans and compare the performance before changing non-accepted plans into accepted plans. A performance verification involves executing a non-accepted plan and a plan chosen from corresponding SQL plan baseline and comparing their performance statistics. If non-accepted plan shows performance improvement, it is changed to an accepted plan.  - ' `YES` ' (Default) - verifies that a non-accepted plan gives better performance before changing it to an accepted plan - ' `NO` ' - directs not to execute plans but only to change non-accepted plans into accepted plans |
| `commit` | Specifies whether to update the `ACCEPTED` status of non-accepted plans from ' `NO` ' to ' `YES` '.  - ' `YES` ' (Default) - perform updates of qualifying non-accepted plans and generate a report that shows the updates and the result of performance verification when verify = ' `YES` '. - ' `NO` ' - generate a report without any updates. Note that `commit` = ' `NO` ' together with `verify` = ' `NO` ' represents a no-op. |

Return Values

A `CLOB` containing a formatted text report showing non-accepted plans in sequence, each with a possible change of its `ACCEPTED` status, and if verify = ' `YES` ' the result of their performance verification.

Usage Notes

Invoking this subprogram requires the `ADMINISTER` `SQL` `MANAGEMENT` `OBJECT` privilege.

---

### LOAD\_PLANS\_FROM\_CURSOR\_CACHE Functions

This function loads one or more plans present in the cursor cache for a SQL statement, or a set of SQL statements. It has four overloads: using SQL statement text, using SQL handle, using SQL ID, or using attribute\_name and attribute\_value pair.

Syntax

```
DBMS_SPM.LOAD_PLANS_FROM_CURSOR_CACHE (
   sql_id            IN  VARCHAR2,
   plan_hash_value   IN  NUMBER   := NULL,
   sql_text          IN  CLOB,
   fixed             IN  VARCHAR2 := 'NO',
   enabled           IN  VARCHAR2 := 'YES')
 RETURN PLS_INTEGER;

DBMS_SPM.LOAD_PLANS_FROM_CURSOR_CACHE (
   sql_id            IN  VARCHAR2,
   plan_hash_value   IN  NUMBER   := NULL,
   sql_handle        IN  VARCHAR2,
   fixed             IN  VARCHAR2 := 'NO',
   enabled           IN  VARCHAR2 := 'YES')
 RETURN PLS_INTEGER;

DBMS_SPM.LOAD_PLANS_FROM_CURSOR_CACHE (
   sql_id            IN  VARCHAR2,
   plan_hash_value   IN  NUMBER   := NULL,
   fixed             IN  VARCHAR2 := 'NO',
   enabled           IN  VARCHAR2 := 'YES')
 RETURN PLS_INTEGER;

DBMS_SPM.LOAD_PLANS_FROM_CURSOR_CACHE (
   attribute_name   IN VARCHAR2,
   attribute_value  IN VARCHAR2,
   fixed            IN VARCHAR2 := 'NO',
   enabled          IN VARCHAR2 := 'YES')
  RETURN PLS_INTEGER;
```

Parameters

Table 136-10 LOAD\_PLANS\_FROM\_CURSOR\_CACHE Function Parameters

| Parameter | Description |
| --- | --- |
| `sql_id` | SQL statement identifier. Identifies a SQL statement in the cursor cache. Note: In the third overload the text of identified SQL statement is extracted from cursor cache and is used to identify the SQL plan baseline into which the plan(s) are loaded. If the SQL plan baseline doesn't exist it is created. |
| `plan_hash_value` | Plan identifier. Default `NULL` means capture all plans present in the cursor cache for the SQL statement identified by `SQL_ID`. |
| `sql_text` | SQL text to use in identifying the SQL plan baseline into which the plans are loaded. If the SQL plan baseline does not exist, it is created. The use of text is crucial when the user tunes a SQL statement by adding hints to its text and then wants to load the resulting plan(s) into the SQL plan baseline of the original SQL statement. |
| `sql_handle` | SQL handle to use in identifying the SQL plan baseline into which the plans are loaded. The `sql_handle` must denote an existing SQL plan baseline. The use of handle is crucial when the user tunes a SQL statement by adding hints to its text and then wants to load the resulting plan(s) into the SQL plan baseline of the original SQL statement. |
| `fixed` | Default `'NO'` means the loaded plans are used as non-fixed plans. Value `'YES'` means the loaded plans are used as fixed plans and the SQL plan baseline will not be evolved over time. |
| `attribute_name` | One of possible attribute names:  - `SQL_TEXT` '' - ' `PARSING_SCHEMA_NAME` ' - ' `MODULE` ' - ' `ACTION'` |
| `attribute_value` | Attribute value is used as a search pattern of `LIKE` predicate if attribute name is `'SQL_TEXT'`. Otherwise, it is used as an equality search value. (for example, for specifying `attribute_name` => `'SQL_TEXT'`, and `attribute_value` => `'% HR-123 %'` means applying `SQL_TEXT` `LIKE` `'%` `HR` - `123` `%'` as a selection filter. Similarly, specifying `attribute_name` => `'MODULE'`, and `attribute_value` => `'HR'` means applying `'MODULE` = ' `HR'` as a plan selection filter). The attribute value is upper-cased except when it is enclosed in double quotes or attribute name is `'SQL_TEXT'`. |
| `enabled` | Default ' `YES` ' means the loaded plans are enabled for use by the optimizer |

Return Values

Number of plans loaded

Usage Notes

Invoking this subprogram requires the `ADMINISTER` `SQL` `MANAGEMENT` `OBJECT` privilege.

---

### LOAD\_PLANS\_FROM\_SQLSET Function

This function loads plans stored in a SQL tuning set (STS) into SQL plan baselines. The plans loaded from STS are not verified for performance but added as accepted plans to existing or new SQL plan baselines. This function can be used to seed SQL management base with new SQL plan baselines.

Syntax

```
DBMS_SPM.LOAD_PLANS_FROM_SQLSET (
   sqlset_name      IN  VARCHAR2,
   sqlset_owner     IN  VARCHAR2 := NULL,
   basic_filter     IN  VARCHAR2 := NULL,
   fixed            IN  VARCHAR2 := 'NO',
   enabled          IN  VARCHAR2 := 'YES'
   commit_rows      IN  NUMBER   := 1000)
RETURN PLS_INTEGER;
```

Parameters

Table 136-11 LOAD\_PLANS\_FROM\_SQLSET Function Parameters

| Parameter | Description |
| --- | --- |
| `sqlset_name` | Name of the STS from where the plans are loaded into SQL plan baselines |
| `sqlset_owner` | Owner of STS. `NULL` means current schema is the owner. |
| `basic_filter` | A filter applied to the STS to select only qualifying plans to be loaded. The filter can take the form of any `WHERE` clause predicate that can specified against the view `DBA_SQLSET_STATEMENTS`. For example `basic_filter` => ' `sql_text like ''select /*LOAD_STS*/%'''` or `basic_filter => 'sql_id=''b62q7nc33gzwx'''`. |
| `fixed` | Default ' `NO` ' means the loaded plans are used as non-fixed plans. Value ' `YES` ' means the loaded plans are used as fixed plans and the SQL plan baseline will not be evolved over time. |
| `enabled` | Default ' `YES` ' means the loaded plans are enabled for use by the optimizer |
| `commit_rows` | Number of SQL plans to load before doing a periodic commit. This helps to shorten the undo log. |

Return Values

The number of plans loaded

Usage Notes

- To load plans from a remote system, first load the plans into an STS on the remote system, export/import the STS from remote to local system, and then use this function.
- To load plans from Automatic Workload Repository (AWR), first load the plans stored in AWR snapshots into an STS, and then use this procedure.
- The user can also capture plans resident in the cursor cache for one or more SQL statements into an STS, and then use this procedure.

---

### MIGRATE\_STORED\_OUTLINE Functions

This function migrates stored outlines for one or more SQL statements to plan baselines in the SQL management base (SMB). Users can specify which stored outline(s) to be migrated based on outline name, SQL text, or outline category, or migrate all stored outlines in the system to SQL plan baselines.

This second overload of the function migrates stored outlines for one or more SQL statements to plan baselines in the SQL management base (SMB) given one or more outline names.

Syntax

```
DBMS_SPM.MIGRATE_STORED_OUTLINE (
   attribute_name     IN  VARCHAR2,
   attribute_value    IN  CLOB,
   fixed              IN  VARCHAR2 := 'NO')
 RETURN CLOB;

DBMS_SPM.MIGRATE_STORED_OUTLINE (
   outln_list         IN  DBMS_SPM.NAME_LIST,
   fixed              IN  VARCHAR2 := 'NO')
 RETURN CLOB;
```

Parameters

Table 136-12 MIGRATE\_STORED\_OUTLINE Function Parameters

| Parameter | Description |
| --- | --- |
| `attribute_name` | Specifies the type of parameter used in `attribute_value` to identify the migrated stored outlines. It is case insensitive. Possible values:  - `outline_name` - `sql_text` - `category` - `all` |
| `attribute_value` | Based on `attribute_name`, this can be:  - Name of stored outline to be migrated - SQL text of stored outlines to be migrated - Category of stored outlines to be migrated - `NULL` if `attribute_name` is `all` |
| `fixed` | `NO` (default) or `YES`. Specifies the "fixed" status of the plans generated during migration. By default, plans are generated as "non-fixed" plans. |
| `outln_list` | List of outline names to be migrated |

Return Values

A `CLOB` containing a formatted report to describe the statistics during the migration, including:

- Number of stored outlines successfully migrated
- Number of stored outlines (and also the corresponding outline names) failed to be migrated and the reasons for the failure

Usage Note

- When the user specifies an outline name, the function migrates stored outlines to plan baseline based on given outline name, which uniquely identifies a single stored outline to be migrated.
- When the user specifies SQL text, the function migrates all stored outlines created for a given SQL statement. A single SQL statement can have multiple stored outlines created for it under different category names. One plan baseline plan is created for each stored outline. The new plan baselines have category names set to `DEFAULT`. The module name of a plan baseline is set to be the same as the stored outline.
- When the user specifies a category name, the function migrates all stored outlines with the given category name. Only one stored outline exists per category per SQL statement. One plan baseline is created for each stored outline.
- When user specifies to migrate `all`, the function migrates all stored outlines in the system to plan baselines. One plan baseline is created for each stored outline.

---

### PACK\_STGTAB\_BASELINE Function

This function packs (exports) SQL plan baselines from SQL management base into a staging table.

Syntax

```
DBMS_SPM.PACK_STGTAB_BASELINE (
   table_name       IN VARCHAR2,
   table_owner      IN VARCHAR2 := NULL,
   sql_handle       IN VARCHAR2 := NULL,
   plan_name        IN VARCHAR2 := NULL,
   sql_text         IN CLOB     := NULL,
   creator          IN VARCHAR2 := NULL,   origin           IN VARCHAR2 := NULL,
   enabled          IN VARCHAR2 := NULL,
   accepted         IN VARCHAR2 := NULL,
   fixed            IN VARCHAR2 := NULL,
   module           IN VARCHAR2 := NULL,
   action           IN VARCHAR2 := NULL)
RETURN NUMBER;
```

Parameters

Table 136-13 PACK\_STGTAB\_BASELINE Function Parameters

| Parameter | Description |
| --- | --- |
| `table_name` | Name of staging table into which SQL plan baselines are packed (case insensitive unless double quoted) |
| `table_owner` | Name of staging table owner.Default `NULL` means current schema is the table owner |
| `sql_handle` | SQL handle (case sensitive) |
| `plan_name` | Plan name (case sensitive, % wildcards accepted) |
| `sql_text` | SQL text string (case sensitive, % wildcards accepted) |
| `creator` | Creator of SQL plan baseline (case insensitive unless double quoted) |
| `origin` | Origin of SQL plan baseline, should be `'MANUAL-LOAD'`, `'AUTO-CAPTURE'`, `'MANUAL_SQLTUNE'` or `'AUTO-SQLTUNE'` (case insensitive) |
| `enabled` | Must be ' `YES` ' or ' `NO` ' (case insensitive) |
| `accepted` | Must be ' `YES` ' or ' `NO` ' (case insensitive) |
| `fixed` | Must be ' `YES` ' or ' `NO` ' (case insensitive) |
| `module` | Module (case sensitive) |
| `action` | Action (case sensitive) |

Return Values

Number of SQL plan baselines packed

---

### UNPACK\_STGTAB\_BASELINE Function

This function unpacks (imports) SQL plan baselines from a staging table into SQL management base.

Syntax

```
DBMS_SPM.UNPACK_STGTAB_BASELINE (
   table_name       IN VARCHAR2,
   table_owner      IN VARCHAR2 := NULL,
   sql_handle       IN VARCHAR2 := NULL,
   plan_name        IN VARCHAR2 := NULL,
   sql_text         IN CLOB     := NULL,
   creator          IN VARCHAR2 := NULL,   origin           IN VARCHAR2 := NULL,
   enabled          IN VARCHAR2 := NULL,
   accepted         IN VARCHAR2 := NULL,
   fixed            IN VARCHAR2 := NULL,
   module           IN VARCHAR2 := NULL,
   action           IN VARCHAR2 := NULL)
RETURN NUMBER;
```

Parameters

Table 136-14 UNPACK\_STGTAB\_BASELINE Function Parameters

| Parameter | Description |
| --- | --- |
| `table_name` | Name of staging table from which SQL plan baselines are unpacked (case insensitive unless double quoted) |
| `table_owner` | Name of staging table owner.Default NULL means current schema is the table owner |
| `sql_handle` | SQL handle (case sensitive) |
| `plan_name` | Plan name (case sensitive,% wildcards accepted) |
| `sql_text` | SQL text string (case sensitive, % wildcards accepted) |
| `creator` | Creator of SQL plan baseline (case insensitive unless double quoted) |
| `origin` | Origin of SQL plan baseline, should be `'MANUAL-LOAD'`, `'AUTO-CAPTURE'`,`'MANUAL_SQLTUNE'` or `'AUTO-SQLTUNE'` (case insensitive) |
| `enabled` | Must be ' `YES` ' or ' `NO` ' (case insensitive) |
| `accepted` | Must be ' `YES` ' or ' `NO` ' (case insensitive) |
| `fixed` | Must be ' `YES` ' or ' `NO` ' (case insensitive) |
| `module` | Module (case sensitive) |
| `action` | Action (case sensitive) |

Return Values

Number of plans unpacked