---
title: "MySQL :: MySQL 26.10 Reference Manual :: 15.1.35 DROP MASKING POLICY Statement"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/drop-masking-policy.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 15.1.35 DROP MASKING POLICY Statement

```sql
DROP MASKING POLICY [IF EXISTS] mask_ssn;
```

`DROP MASKING POLICY` deletes the named masking policy from the `mysql.column_masking_policies` table. To use this statement, you must have the `MANAGE_DATA_MASKING_POLICY` privilege, and the `object_policy` component must be loaded. If the component is not loaded, an error occurs.

DROP MASKING POLICY accepts one policy name. If the named policy does not exist, an error occurs unless `IF       EXISTS` is provided. With `IF EXISTS`, the statement succeeds with no effect.

Dropping a masking policy does not check if a table column currently refers to the policy, and does not affect statements that are already running. If a masking policy is deleted, it is not possible to access the data in a column masked by it. The masking policy must be restored to access the data. Unmasked columns in the same table are unaffected.

```sql
DROP MASKING POLICY IF EXISTS mask_password;
```