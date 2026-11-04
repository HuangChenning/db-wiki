---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_CONSTRAINTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.140 ALL\_CONSTRAINTS

`ALL_CONSTRAINTS` describes constraint definitions on tables accessible to the current user.

Related Views

- `DBA_CONSTRAINTS` describes all constraint definitions in the database.
- `USER_CONSTRAINTS` describes constraint definitions on tables in the current user's schema.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the constraint definition |
| `CONSTRAINT_NAME` | `VARCHAR2(128)` |  | Name of the constraint definition |
| `CONSTRAINT_TYPE` | `VARCHAR2(1)` |  | Type of the constraint definition:  - `C` - Check constraint on a table - `P` - Primary key - `U` - Unique key - `R` - Referential integrity - `V` - With check option, on a view - `O` - With read only, on a view - `H` - Hash expression - `F` - Constraint that involves a REF column - `S` - Supplemental logging |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name associated with the table (or view) with the constraint definition |
| `SEARCH_CONDITION` | `LONG` |  | Text of search condition for a check constraint. This column returns the correct value only when the row originates from the current container. |
| `SEARCH_CONDITION_VC` | `VARCHAR2(4000)` |  | Text of search condition for a check constraint. This column may truncate the search condition. |
| `R_OWNER` | `VARCHAR2(128)` |  | Owner of the table referred to in a referential constraint |
| `R_CONSTRAINT_NAME` | `VARCHAR2(128)` |  | Name of the unique constraint definition for the referenced table |
| `DELETE_RULE` | `VARCHAR2(9)` |  | Delete rule for a referential constraint:  - `CASCADE` - `SET NULL` - `NO ACTION` |
| `STATUS` | `VARCHAR2(8)` |  | Enforcement status of the constraint:  - `ENABLED` - `DISABLED` |
| `DEFERRABLE` | `VARCHAR2(14)` |  | Indicates whether the constraint is deferrable (`DEFERRABLE`) or not (`NOT DEFERRABLE`) |
| `DEFERRED` | `VARCHAR2(9)` |  | Indicates whether the constraint was initially deferred (`DEFERRED`) or not (`IMMEDIATE`) |
| `VALIDATED` | `VARCHAR2(13)` |  | When `STATUS` = `ENABLED`, possible values are:  - `VALIDATED` - All data obeys the constraint (that is, the existing data in the table was validated when the constraint was enabled, as well as any subsequent data entered into the table) - `NOT` `VALIDATED` - All data may not obey the constraint (that is, the existing data in the table was not validated when the constraint was enabled, but subsequent data entered into the table was validated)  When `STATUS` = `DISABLED`, possible values are:  - `VALIDATED` - All data obeys the constraint, but the unique index on the constraint has been dropped. This setting is useful in data warehousing environments, but has some restrictions. Refer to [Oracle Database Data Warehousing Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DWHSG9055) for more information on this setting. - `NOT` `VALIDATED` - All data may not obey the constraint |
| `GENERATED` | `VARCHAR2(14)` |  | Indicates whether the name of the constraint is user-generated (`USER NAME`) or system-generated (`GENERATED NAME`) |
| `BAD` | `VARCHAR2(3)` |  | Indicates whether this constraint specifies a century in an ambiguous manner (`BAD`) or not (NULL). To avoid errors resulting from this ambiguity, rewrite the constraint using the `TO_DATE` function with a four-digit year.  See Also: the `TO_DATE` function in [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF06132) and [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADFNS182) |
| `RELY` | `VARCHAR2(4)` |  | When `VALIDATED` = `NOT` `VALIDATED`, this column indicates whether the constraint is to be taken into account for query rewrite (`RELY`) or not (NULL).  When `VALIDATED` = `VALIDATED`, this column is not meaningful.  See Also: constraints in [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF52180) |
| `LAST_CHANGE` | `DATE` |  | When the constraint was last enabled or disabled |
| `INDEX_OWNER` | `VARCHAR2(128)` |  | Name of the user owning the index |
| `INDEX_NAME` | `VARCHAR2(128)` |  | Name of the index (only shown for unique and primary-key constraints) |
| `INVALID` | `VARCHAR2(7)` |  | Indicates whether the constraint is invalid (`INVALID`) or not (NULL) |
| `VIEW_RELATED` | `VARCHAR2(14)` |  | Indicates whether the constraint depends on a view (`DEPEND ON VIEW`) or not (NULL) |
| `ORIGIN_CON_ID` | `VARCHAR2(256)` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root) |

See Also:

- " [DBA\_CONSTRAINTS](DBA_CONSTRAINTS.md) "
- " [USER\_CONSTRAINTS](USER_CONSTRAINTS.md) "