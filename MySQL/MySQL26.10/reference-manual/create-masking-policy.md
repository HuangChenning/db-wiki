---
title: "MySQL :: MySQL 26.10 Reference Manual :: 15.1.21 CREATE MASKING POLICY Statement"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/create-masking-policy.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 15.1.21 CREATE MASKING POLICY Statement

```sql
CREATE MASKING POLICY
   [IF NOT EXISTS] policy_name (policy_argument)
   CASE WHEN current_role_or_user_in
     THEN policy_argument
       ELSE masking_expr(policy_argument)
         END;
         
policy_param:
  param_name
         
current_role_or_user_in:
  CURRENT_ROLE_IN (role_list) 
 |CURRENT_USER_IN (user_list)
```

CREATE MASKING POLICY creates a masking policy with the given name and parameter.

An error occurs if the policy exists and you did not specify `IF NOT EXISTS`.

Note

Masking policy definitions are stored by the `object_policy` component. If the component is not installed, this statement returns an error.

Only users with the `MANAGE_DATA_MASKING_POLICY` privilege can create a masking policy.

A masking policy is a rule, or set of rules, which determines how a column's data is transformed for access control. A masking policy consists of the following:

- A policy name:
	- Policy name must be unique.
	- Policy name cannot be empty.
	- Policy name cannot end in a space.
	- Policy name cannot exceed 64 characters.
- A policy argument:
	- Policy argument cannot be empty.
	- Policy argument cannot end in a space.
	- Policy argument cannot exceed 64 characters.
- A gatekeeper function: criteria which determine whether data is masked.
	The following gatekeeper functions are supported:
	- [``CURRENT_ROLE_IN(*`role1`*,*`role2`*,...)``](gatekeeper-functions.md): supports a comma-separated list of roles.
	- [``CURRENT_USER_IN(*`user1`*,*`user2`*,...)``](gatekeeper-functions.md): supports a comma-separated list of usernames.
- A masking function: logic which transforms the data.
	- This must be a CASE expression over the policy argument.
	- The masking function cannot reference any column other than that defined in the policy argument and must not contain subqueries, window functions, table references, user-defined variables, or non-deterministic constructs.

The following masking policy, when applied to a column, permits anyone in the `admin` role to view the contents of the column. Otherwise, the data is SHA2-encoded.

```sql
CREATE MASKING POLICY mask_password1(pass_column)
CASE WHEN CURRENT_ROLE_IN('admin')
     THEN pass_column
     ELSE sha2(pass_column, 256)
END;
```

The following masking policy, when applied to a column, returns only SHA2-encrypted data for users in the `webapp` role.

```sql
CREATE MASKING POLICY mask_password2(pass_column)
CASE WHEN CURRENT_ROLE_IN('webapp')
     THEN sha2(pass_column, 256)
     ELSE pass_column
END;
```