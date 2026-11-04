---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_RULE_ADM.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 156 DBMS\_RULE\_ADM

The `DBMS_RULE_ADM` package provides the subprograms for creating and managing rules, rule sets, and rule evaluation contexts.

This chapter contains the following topics:

### 156.1 DBMS\_RULE\_ADM Overview

This package provides the subprograms for creating and managing rules, rule sets, and rule evaluation contexts.

See Also:

- [Rule TYPEs](Rule-TYPEs.md) for more information about the types used with the `DBMS_RULE_ADM` package
- [DBMS\_RULE](DBMS_RULE.md)

### 156.2 DBMS\_RULE\_ADM Security Model

`PUBLIC` is granted `EXECUTE` privilege on this package.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=DBSEG40048) for more information about user group `PUBLIC`

### 156.3 Summary of DBMS\_RULE\_ADM Subprograms

This table lists the `DBMS_RULE_ADM` subprograms and briefly describes them.

Table 156-1 DBMS\_RULE\_ADM Package Subprograms

| Subprogram | Description |
| --- | --- |
| ADD\_RULE Procedure | Adds the specified rule to the specified rule set |
| ALTER\_EVALUATION\_CONTEXT Procedure | Alters a rule evaluation context |
| ALTER\_RULE Procedure | Changes one or more aspects of the specified rule |
| CREATE\_EVALUATION\_CONTEXT Procedure | Creates a rule evaluation context |
| CREATE\_RULE Procedure | Creates a rule with the specified name |
| CREATE\_RULE\_SET Procedure | Creates a rule set with the specified name |
| DROP\_EVALUATION\_CONTEXT Procedure | Drops the rule evaluation context with the specified name |
| DROP\_RULE Procedure | Drops the rule with the specified name |
| DROP\_RULE\_SET Procedure | Drops the rule set with the specified name |
| GRANT\_OBJECT\_PRIVILEGE Procedure | Grants the specified object privilege on the specified object to the specified user or role |
| GRANT\_SYSTEM\_PRIVILEGE Procedure | Grants the specified system privilege to the specified user or role |
| REMOVE\_RULE Procedure | Removes the specified rule from the specified rule set |
| REVOKE\_OBJECT\_PRIVILEGE Procedure | Revokes the specified object privilege on the specified object from the specified user or role |
| REVOKE\_SYSTEM\_PRIVILEGE Procedure | Revokes the specified system privilege from the specified user or role |

Note:

All subprograms commit unless specified otherwise.

#### 156.3.1 ADD\_RULE Procedure

This procedure adds the specified rule to the specified rule set.

Syntax

```
DBMS_RULE_ADM.ADD_RULE(
   rule_name           IN  VARCHAR2,
   rule_set_name       IN  VARCHAR2,
   evaluation_context  IN  VARCHAR2   DEFAULT NULL,
   rule_comment        IN  VARCHAR2   DEFAULT NULL);
```

Parameters

Table 156-2 ADD\_RULE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rule_name` | The name of the rule you are adding to the rule set, specified as `[``schema_name``.]` `rule_name`. For example, to add a rule named `all_a` in the `hr` schema, enter `hr.all_a` for this parameter. If the schema is not specified, then the current user is the default. |
| `rule_set_name` | The name of the rule set to which you are adding the rule, specified as `[``schema_name``.]` `rule_set_name`. For example, to add the rule to a rule set named `apply_rules` in the `hr` schema, enter `hr.apply_rules` for this parameter. If the schema is not specified, then the current user is the default. |
| `evaluation_context` | An evaluation context name in the form `[``schema_name``.]` `evaluation_context_name`. If the schema is not specified, then the current user is the default.  Only specify an evaluation context if the rule itself does not have an evaluation context and you do not want to use the rule set's evaluation context for the rule. |
| `rule_comment` | Optional description, which can contain the reason for adding the rule to the rule set |

Usage Notes

To run this procedure, a user must meet at least one of the following requirements:

- Have `ALTER_ON_RULE_SET` privilege on the rule set
- Have `ALTER` \_ `ANY` \_ `RULE` \_ `SET` system privilege
- Be the owner of the rule set

Also, the rule set owner must meet at least one of the following requirements:

- Have `EXECUTE_ON_RULE` privilege on the rule
- Have `EXECUTE` \_ `ANY` \_ `RULE` system privilege
- Be the rule owner

If the rule has no evaluation context and no evaluation context is specified when you run this procedure, then the rule uses the evaluation context associated with the rule set. In such a case, the rule owner must have the necessary privileges on all the base objects accessed by the rule using the evaluation context.

If an evaluation context is specified, then the rule set owner must meet at least one of the following requirements:

- Have `EXECUTE_ON_EVALUATION_CONTEXT` privilege on the evaluation context
- Have `EXECUTE_ANY_EVALUATION_CONTEXT` system privilege, and the owner of the evaluation context must not be `SYS`
- Be the evaluation context owner

Also, the rule owner must have the necessary privileges on all the base objects accessed by the rule using the evaluation context.

#### 156.3.2 ALTER\_EVALUATION\_CONTEXT Procedure

This procedure alters a rule evaluation context. A rule evaluation context defines external data that can be referenced in rule conditions. The external data can either exist as variables or as table data.

Syntax

```
DBMS_RULE_ADM.ALTER_EVALUATION_CONTEXT(
  evaluation_context_name      IN  VARCHAR2,
  table_aliases                IN  SYS.RE$TABLE_ALIAS_LIST    DEFAULT NULL,
  remove_table_aliases         IN  BOOLEAN                    DEFAULT FALSE,
  variable_types               IN  SYS.RE$VARIABLE_TYPE_LIST  DEFAULT NULL,
  remove_variable_types        IN  BOOLEAN                    DEFAULT FALSE,
  evaluation_function          IN  VARCHAR2                   DEFAULT NULL,
  remove_evaluation_function   IN  BOOLEAN                    DEFAULT FALSE,
  evaluation_context_comment   IN  VARCHAR2                   DEFAULT NULL,
  remove_eval_context_comment  IN  BOOLEAN                    DEFAULT FALSE);
```

Parameters

Table 156-3 ALTER\_EVALUATION\_CONTEXT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `evaluation_context_name` | The name of the evaluation context you are altering, specified as `[``schema_name``.]` `evaluation_context_name`.  For example, to alter an evaluation context named `dept_` `eval_context` in the `hr` schema, enter `hr.dept_eval_context` for this parameter. If the schema is not specified, then the current user is the default. |
| `table_aliases` | If `NULL` and `remove_table_aliases` is `FALSE`, then the procedure retains the existing table aliases. If `NULL` and `remove_table_aliases` is `TRUE`, then the procedure removes the existing table aliases.  If non- `NULL`, then the procedure replaces the existing table aliases for the evaluation context with the specified table aliases.  Table aliases specify the tables in an evaluation context. The table aliases can be used to reference tables in rule conditions. |
| `remove_table_aliases` | If `TRUE` and `table_aliases` is `NULL`, then the procedure removes the existing table aliases for the evaluation context. If `TRUE` and `table_aliases` is non- `NULL`, then the procedure raises an error.  If `FALSE`, then the procedure does not remove table aliases. |
| `variable_types` | If `NULL` and `remove_variable_types` is `FALSE`, then the procedure retains the variable types. If `NULL` and `remove_variable_types` is `TRUE`, then the procedure removes the existing variable types.  If non- `NULL`, then the procedure replaces the existing variable types for the evaluation context with the specified variable types. |
| `remove_variable_types` | If `TRUE` and `variable_types` is `NULL`, then the procedure removes the existing variable types for the evaluation context. If `TRUE` and `variable_types` is non- `NULL`, then the procedure raises an error.  If `FALSE`, then the procedure does not remove the variable types. |
| `evaluation_function` | If `NULL` and `remove_evaluation_function` is `FALSE`, then the procedure retains the existing evaluation function. If `NULL` and `remove_evaluation_function` is `TRUE`, then the procedure removes the existing evaluation function.  If non- `NULL`, then the procedure replaces the existing evaluation function for the evaluation context with the specified evaluation function.  An evaluation function is an optional function that will be called to evaluate rules that use the evaluation context. It must have the same form as the `DBMS_RULE.EVALUATE` procedure. If the schema is not specified, then the current user is the default.  See CREATE\_EVALUATION\_CONTEXT Procedure for more information about evaluation functions. |
| `remove_evaluation_function` | If `TRUE` and `evaluation_function` is `NULL`, then the procedure removes the existing evaluation function for the evaluation context. If `TRUE` and `evaluation_function` is non- `NULL`, then the procedure raises an error.  If `FALSE`, then the procedure does not remove the evaluation function. |
| `evaluation_context_comment` | If `NULL` and `remove_eval_context_comment` is `FALSE`, then the procedure retains the existing evaluation context comment. If `NULL` and `remove_evaluation_function` is `TRUE`, then the procedure removes the existing evaluation context comment.  If non- `NULL`, then the procedure replaces the existing comment for the evaluation context with the specified comment.  An evaluation context comment is an optional description of the rule evaluation context. |
| `remove_eval_context_comment` | If `TRUE` and `evaluation_context_comment` is `NULL`, then the procedure removes the existing comment for the evaluation context. If `TRUE` and `evaluation_context_comment` is non- `NULL`, then the procedure raises an error.  If `FALSE`, then the procedure does not remove the evaluation context comment. |

Usage Notes

To run this procedure, a user must meet at least one of the following requirements:

- Be the owner of the evaluation context being altered
- Have `ALL_ON_EVALUATION_CONTEXT` or `ALTER_ON_EVALUATION_CONTEXT` object privilege on an evaluation context owned by another user
- Have `ALTER_ANY_EVALUATION_CONTEXT` system privilege
	See Also:
	[Rule TYPEs](Rule-TYPEs.md) for more information about the types used with the `DBMS_RULE_ADM` package

#### 156.3.3 ALTER\_RULE Procedure

This procedure changes one or more aspects of the specified rule.

Syntax

```
DBMS_RULE_ADM.ALTER_RULE(
   rule_name                  IN  VARCHAR2,
   condition                  IN  VARCHAR2        DEFAULT NULL,
   evaluation_context         IN  VARCHAR2        DEFAULT NULL,
   remove_evaluation_context  IN  BOOLEAN         DEFAULT FALSE,
   action_context             IN  SYS.RE$NV_LIST  DEFAULT NULL,
   remove_action_context      IN  BOOLEAN         DEFAULT FALSE,
   rule_comment               IN  VARCHAR2        DEFAULT NULL,
   remove_rule_comment        IN  BOOLEAN         DEFAULT FALSE);
```

Parameters

Table 156-4 ALTER\_RULE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rule_name` | The name of the rule you are altering, specified as `[``schema_name``.]` `rule_name`. For example, to alter a rule named `all_a` in the `hr` schema, enter `hr.all_a` for this parameter. If the schema is not specified, then the current user is the default. |
| `condition` | The condition to be associated with the rule.  If non- `NULL`, then the procedure replaces the existing condition of the rule with the specified condition. |
| `evaluation_context` | An evaluation context name in the form `[``schema_name``.]` `evaluation_context_name`. If the schema is not specified, then the current user is the default.  If non- `NULL`, then the procedure replaces the existing evaluation context of the rule with the specified evaluation context. |
| `remove_evaluation_context` | If `TRUE`, then the procedure sets the evaluation context for the rule to `NULL`, which effectively removes the evaluation context from the rule.  If `FALSE`, then the procedure retains any evaluation context for the specified rule.  If the `evaluation_context` parameter is non- `NULL`, then this parameter should be set to `FALSE`. |
| `action_context` | If non- `NULL`, then the procedure changes the action context associated with the rule. A rule action context is information associated with a rule that is interpreted by the client of the rules engine when the rule is evaluated. |
| `remove_action_context` | If `TRUE`, then the procedure sets the action context for the rule to `NULL`, which effectively removes the action context from the rule.  If `FALSE`, then the procedure retains any action context for the specified rule.  If the `action_context` parameter is non- `NULL`, then this parameter should be set to `FALSE`. |
| `rule_comment` | If non- `NULL`, then the existing comment of the rule is replaced by the specified comment. |
| `remove_rule_comment` | If `TRUE`, then the procedure sets the comment for the rule to `NULL`, which effectively removes the comment from the rule.  If `FALSE`, then the procedure retains any comment for the specified rule.  If the `rule_comment` parameter is non- `NULL`, then this parameter should be set to `FALSE`. |

Usage Notes

To run this procedure, a user must meet at least one of the following requirements:

- Have `ALTER_ON_RULE` privilege on the rule
- Have `ALTER` \_ `ANY` \_ `RULE` system privilege
- Be the owner of the rule being altered

If an evaluation context is specified, then the rule owner must meet at least one of the following requirements:

- Have `EXECUTE_ON_EVALUATION_CONTEXT` privilege on the evaluation context
- Have `EXECUTE_ANY_EVALUATION_CONTEXT` system privilege, and the owner of the evaluation context must not be `SYS`
- Be the evaluation context owner

Also, the rule owner must have the necessary privileges on all the base objects accessed by the rule using the evaluation context.

See Also:

[Rule TYPEs](Rule-TYPEs.md) for more information about the types used with the `DBMS_RULE_ADM` package

#### 156.3.4 CREATE\_EVALUATION\_CONTEXT Procedure

This procedure creates a rule evaluation context. A rule evaluation context defines external data that can be referenced in rule conditions. The external data can either exist as variables or as table data.

Syntax

```
DBMS_RULE_ADM.CREATE_EVALUATION_CONTEXT(
  evaluation_context_name      IN  VARCHAR2,
  table_aliases                IN  SYS.RE$TABLE_ALIAS_LIST    DEFAULT NULL,
  variable_types               IN  SYS.RE$VARIABLE_TYPE_LIST  DEFAULT NULL,
  evaluation_function          IN  VARCHAR2                   DEFAULT NULL,
  evaluation_context_comment   IN  VARCHAR2                   DEFAULT NULL);
```

Parameters

Table 156-5 CREATE\_EVALUATION\_CONTEXT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `evaluation_context_name` | The name of the evaluation context you are creating, specified as `[``schema_name``.]` `evaluation_context_name`.  For example, to create an evaluation context named `dept_` `eval_context` in the `hr` schema, enter `hr.dept_eval_context` for this parameter. If the schema is not specified, then the current user is the default. |
| `table_aliases` | Table aliases that specify the tables in an evaluation context. The table aliases can be used to reference tables in rule conditions. |
| `variable_types` | A list of variables for the evaluation context |
| `evaluation_function` | An optional function that will be called to evaluate rules using the evaluation context. It must have the same form as the `DBMS_RULE.EVALUATE` procedure. If the schema is not specified, then the current user is the default.  See " Usage Notes " for more information about the evaluation function. |
| `evaluation_context_comment` | An optional description of the rule evaluation context. |

Usage Notes

To run this procedure, a user must meet at least one of the following requirements:

- Be the owner of the evaluation context being created and have `CREATE_EVALUATION_CONTEXT_OBJ` system privilege
- Have `CREATE` \_ `ANY` \_ `EVALUATION` \_ `CONTEXT` system privilege
	See Also:
	[Rule TYPEs](Rule-TYPEs.md) for more information about the types used with the `DBMS_RULE_ADM` package

The evaluation function must have the following signature:

```
FUNCTION evaluation_function_name(
  rule_set_name       IN   VARCHAR2,
  evaluation_context  IN   VARCHAR2,
  event_context       IN   SYS.RE$NV_LIST               DEFAULT NULL,
  table_values        IN   SYS.RE$TABLE_VALUE_LIST      DEFAULT NULL,
  column_values       IN   SYS.RE$COLUMN_VALUE_LIST     DEFAULT NULL,
  variable_values     IN   SYS.RE$VARIABLE_VALUE_LIST   DEFAULT NULL,
  attribute_values    IN   SYS.RE$ATTRIBUTE_VALUE_LIST  DEFAULT NULL,
  stop_on_first_hit   IN   BOOLEAN                      DEFAULT FALSE,
  simple_rules_only   IN   BOOLEAN                      DEFAULT FALSE,
  true_rules          OUT  SYS.RE$RULE_HIT_LIST,
  maybe_rules         OUT  SYS.RE$RULE_HIT_LIST);
RETURN BINARY_INTEGER;
```

Note:

Each parameter is required and must have the specified datatype. However, you can change the names of the parameters.

The return value of the function must be one of the following:

- `DBMS_RULE_ADM.EVALUATION_SUCCESS`: The user specified evaluation function completed the rule set evaluation successfully. The rules engine returns the results of the evaluation obtained by the evaluation function to the rules engine client using the `DBMS_RULE.EVALUATE` procedure.
- `DBMS_RULE_ADM.EVALUATION_CONTINUE`: The rules engine evaluates the rule set as if there were no evaluation function. The evaluation function is not used, and any results returned by the evaluation function are ignored.
- `DBMS_RULE_ADM.EVALUATION_FAILURE`: The user specified evaluation function failed. Rule set evaluation stops, and an error is raised.

#### 156.3.5 CREATE\_RULE Procedure

This procedure creates a rule.

Syntax

```
DBMS_RULE_ADM.CREATE_RULE(
   rule_name           IN  VARCHAR2,
   condition           IN  VARCHAR2,
   evaluation_context  IN  VARCHAR2        DEFAULT NULL,
   action_context      IN  SYS.RE$NV_LIST  DEFAULT NULL,
   rule_comment        IN  VARCHAR2        DEFAULT NULL);
```

Parameters

Table 156-6 CREATE\_RULE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rule_name` | The name of the rule you are creating, specified as `[``schema_name``.]` `rule_name`. For example, to create a rule named `all_a` in the `hr` schema, enter `hr.all_a` for this parameter. If the schema is not specified, then the current user is the default. |
| `condition` | The condition to be associated with the rule. A condition evaluates to `TRUE` or `FALSE` and can be any condition allowed in the `WHERE` clause of a `SELECT` statement. For example, the following is a valid rule condition:  ``` department_id = 30 ```  Ensure that the proper case is used for text in rule conditions.  Note: Do not include the word `"WHERE"` in the condition. |
| `evaluation_context` | An optional evaluation context name in the form `[``schema_name``.]` `evaluation_context_name`, which is associated with the rule. If the schema is not specified, then the current user is the default.  If `evaluation_context` is not specified, then the rule inherits the evaluation context from its rule set. |
| `action_context` | The action context associated with the rule. A rule action context is information associated with a rule that is interpreted by the client of the rules engine when the rule is evaluated. |
| `rule_comment` | An optional description of the rule |

Usage Notes

To run this procedure, a user must meet at least one of the following requirements:

- Be the owner of the rule being created and have the `CREATE_RULE_OBJ` system privilege
- Have `CREATE` \_ `ANY` \_ `RULE` system privilege

If an evaluation context is specified, then the rule owner must meet at least one of the following requirements:

- Have `EXECUTE_ON_EVALUATION_CONTEXT` privilege on the evaluation context
- Have `EXECUTE_ANY_EVALUATION_CONTEXT` system privilege, and the owner of the evaluation context must not be `SYS`.
- Be the evaluation context owner

Also, the rule owner must have the necessary privileges on all the base objects accessed by the rule using the evaluation context.

See Also:

[Rule TYPEs](Rule-TYPEs.md) for more information about the types used with the `DBMS_RULE_ADM` package

#### 156.3.6 CREATE\_RULE\_SET Procedure

This procedure creates a rule set.

Syntax

```
DBMS_RULE_ADM.CREATE_RULE_SET(
   rule_set_name       IN  VARCHAR2,
   evaluation_context  IN  VARCHAR2  DEFAULT NULL,
   rule_set_comment    IN  VARCHAR2  DEFAULT NULL);
```

Parameters

Table 156-7 CREATE\_RULE\_SET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rule_set_name` | The name of the rule set you are creating, specified as `[``schema_name``.]` `rule_set_name`. For example, to create a rule set named `apply_rules` in the `hr` schema, enter `hr.apply_rules` for this parameter. If the schema is not specified, then the current user is the default. |
| `evaluation_context` | An optional evaluation context name in the form `[``schema_name``.]` `evaluation_context_name`, which applies to all rules in the rule set that are not associated with an evaluation context explicitly. If the schema is not specified, then the current user is the default. |
| `rule_set_comment` | An optional description of the rule set |

Usage Notes

To run this procedure, a user must meet at least one of the following requirements:

- Be the owner of the rule set being created and have `CREATE_RULE_SET_OBJ` system privilege
- Have `CREATE` \_ `ANY` \_ `RULE` \_ `SET` system privilege

If an evaluation context is specified, then the rule set owner must meet at least one of the following requirements:

- Have `EXECUTE_ON_EVALUATION_CONTEXT` privilege on the evaluation context
- Have `EXECUTE_ANY_EVALUATION_CONTEXT` system privilege, and the owner of the evaluation context must not be `SYS`
- Be the evaluation context owner

#### 156.3.7 DROP\_EVALUATION\_CONTEXT Procedure

This procedure drops a rule evaluation context.

Syntax

```
DBMS_RULE_ADM.DROP_EVALUATION_CONTEXT(
   evaluation_context_name  IN  VARCHAR2,
   force                    IN  BOOLEAN   DEFAULT FALSE);
```

Parameters

Table 156-8 DROP\_EVALUATION\_CONTEXT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `evaluation_context_name` | The name of the evaluation context you are dropping, specified as `[``schema_name``.]` `evaluation_context_name`.  For example, to drop an evaluation context named `dept_eval_context` in the `hr` schema, enter `hr.dept_eval_context` for this parameter. If the schema is not specified, then the current user is the default. |
| `force` | If `TRUE`, then the procedure removes the rule evaluation context from all rules and rule sets that use it.  If `FALSE` and no rules or rule sets use the rule evaluation context, then the procedure drops the rule evaluation context.  If `FALSE` and one or more rules or rule sets use the rule evaluation context, then the procedure raises an exception.  Caution: Setting `force` to `TRUE` can result in rules and rule sets that do not have an evaluation context. If neither a rule nor the rule set it is in has an evaluation context, and no evaluation context was specified for the rule by the `ADD_RULE` procedure, then the rule cannot be evaluated. |

Usage Notes

To run this procedure, a user must meet at least one of the following requirements:

- Be the owner of the evaluation context
- Have `DROP` \_ `ANY` \_ `EVALUATION` \_ `CONTEXT` system privilege

#### 156.3.8 DROP\_RULE Procedure

This procedure drops a rule.

Syntax

```
DBMS_RULE_ADM.DROP_RULE(
   rule_name  IN  VARCHAR2,
   force      IN  BOOLEAN   DEFAULT FALSE);
```

Parameters

Table 156-9 DROP\_RULE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rule_name` | The name of the rule you are dropping, specified as `[``schema_name``.]` `rule_name`. For example, to drop a rule named `all_a` in the `hr` schema, enter `hr.all_a` for this parameter. If the schema is not specified, then the current user is the default. |
| `force` | If `TRUE`, then the procedure removes the rule from all rule sets that contain it.  If `FALSE` and no rule sets contain the rule, then the procedure drops the rule.  If `FALSE` and one or more rule sets contain the rule, then the procedure raises an exception. |

Usage Notes

To run this procedure, a user must meet at least one of the following requirements:

- Be the owner of the rule
- Have `DROP` \_ `ANY` \_ `RULE` system privilege
	Note:
	- To remove a rule from a rule set without dropping the rule from the database, use the `REMOVE_RULE` procedure.
	- The rule evaluation context associated with the rule, if any, is not dropped when you run this procedure.

#### 156.3.9 DROP\_RULE\_SET Procedure

This procedure drops a rule set.

Syntax

```
DBMS_RULE_ADM.DROP_RULE_SET(
   rule_set_name  IN  VARCHAR2,
   delete_rules   IN  BOOLEAN   DEFAULT FALSE);
```

Parameters

Table 156-10 DROP\_RULE\_SET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rule_set_name` | The name of the rule set you are dropping, specified as `[``schema_name``.]` `rule_set_name`. For example, to drop a rule set named `apply_rules` in the `hr` schema, enter `hr.apply_rules` for this parameter. If the schema is not specified, then the current user is the default. |
| `delete_rules` | If `TRUE`, then the procedure drops any rules that are in the rule set. If any of the rules in the rule set are also in another rule set, then these rules are not dropped.  If `FALSE`, then the procedure does not drop the rules in the rule set. |

Usage Notes

To run this procedure, a user must meet at least one of the following requirements:

- Have `DROP` \_ `ANY` \_ `RULE` \_ `SET` system privilege
- Be the owner of the rule set
	Note:
	The rule evaluation context associated with the rule set, if any, is not dropped when you run this procedure.

#### 156.3.10 GRANT\_OBJECT\_PRIVILEGE Procedure

This procedure grants the specified object privilege on the specified object to the specified user or role. If a user owns the object, then the user automatically is granted all privileges on the object, with grant option.

Syntax

```
DBMS_RULE_ADM.GRANT_OBJECT_PRIVILEGE(
   privilege     IN  BINARY_INTEGER,
   object_name   IN  VARCHAR2,
   grantee       IN  VARCHAR2,
   grant_option  IN  BOOLEAN   DEFAULT FALSE);
```

Parameters

Table 156-11 GRANT\_OBJECT\_PRIVILEGE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `privilege` | The name of the object privilege to grant to the grantee on the object. See " Usage Notes " for the available object privileges. |
| `object_name` | The name of the object for which you are granting the privilege to the grantee, specified as `[``schema_name``.]` `object_name`. For example, to grant the privilege on a rule set named `apply_rules` in the `hr` schema, enter `hr.apply_rules` for this parameter. If the schema is not specified, then the current user is the default. The object must be an existing rule, rule set, or evaluation context. |
| `grantee` | The name of the user or role for which the privilege is granted. The specified user cannot be the owner of the object. |
| `grant_option` | If `TRUE`, then the specified user or users granted the specified privilege can grant this privilege to others.  If `FALSE`, then the specified user or users granted the specified privilege cannot grant this privilege to others. |

Usage Notes

To run this procedure, a user must meet at least one of the following requirements:

- Be the owner of the object on which the privilege is granted
- Have the same privilege as the privilege being granted with the grant option

In addition, if the object is a rule set, then the user must have `EXECUTE` privilege on all the rules in the rule set with grant option or must own the rules in the rule set.

Table 156-12 lists the object privileges.

Table 156-12 Object Privileges for Evaluation Contexts, Rules, and Rule Sets

| Privilege | Description |
| --- | --- |
| `SYS.DBMS_RULE_ADM.ALL_ON_EVALUATION_CONTEXT` | Alter and execute a particular evaluation context in another user's schema |
| `SYS.DBMS_RULE_ADM.ALL_ON_RULE` | Alter and execute a particular rule in another user's schema |
| `SYS.DBMS_RULE_ADM.ALL_ON_RULE_SET` | Alter and execute a particular rule set in another user's schema |
| `SYS.DBMS_RULE_ADM.ALTER_ON_EVALUATION_CONTEXT` | Alter a particular evaluation context in another user's schema |
| `SYS.DBMS_RULE_ADM.ALTER_ON_RULE` | Alter a particular rule in another user's schema |
| `SYS.DBMS_RULE_ADM.ALTER_ON_RULE_SET` | Alter a particular rule set in another user's schema |
| `SYS.DBMS_RULE_ADM.EXECUTE_ON_EVALUATION_CONTEXT` | Execute a particular evaluation context in another user's schema |
| `SYS.DBMS_RULE_ADM.EXECUTE_ON_RULE` | Execute a particular rule in another user's schema |
| `SYS.DBMS_RULE_ADM.EXECUTE_ON_RULE_SET` | Execute a particular rule set in another user's schema |

Examples

For example, to grant the `HR` user the privilege to alter a rule named `hr_dml` in the `strmadmin` schema, enter the following:

```
BEGIN 
  DBMS_RULE_ADM.GRANT_OBJECT_PRIVILEGE(
    privilege    => SYS.DBMS_RULE_ADM.ALTER_ON_RULE,
    object_name  => 'strmadmin.hr_dml',
    grantee      => 'hr', 
    grant_option => FALSE);
END;
/
```

#### 156.3.11 GRANT\_SYSTEM\_PRIVILEGE Procedure

This procedure grant the specified system privilege to the specified user or role.

Syntax

```
DBMS_RULE_ADM.GRANT_SYSTEM_PRIVILEGE(
   privilege     IN  BINARY_INTEGER,
   grantee       IN  VARCHAR2,
   grant_option  IN  BOOLEAN   DEFAULT FALSE);
```

Parameters

Table 156-13 GRANT\_SYSTEM\_PRIVILEGE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `privilege` | The name of the system privilege to grant to the grantee. |
| `grantee` | The name of the user or role for which the privilege is granted |
| `grant_option` | If `TRUE`, then the specified user or users granted the specified privilege can grant the system privilege to others.  If `FALSE`, then the specified user or users granted the specified privilege cannot grant the system privilege to others. |

Usage Notes

Table 156-14 lists the system privileges.

Table 156-14 System Privileges for Evaluation Contexts, Rules, and Rule Sets

| Privilege | Description |
| --- | --- |
| `SYS.DBMS_RULE_ADM.ALTER_ANY_EVALUATION_CONTEXT` | Alter any evaluation context owned by any user |
| `SYS.DBMS_RULE_ADM.ALTER_ANY_RULE` | Alter any rule owned by any user |
| `SYS.DBMS_RULE_ADM.ALTER_ANY_RULE_SET` | Alter any rule set owned by any user |
| `SYS.DBMS_RULE_ADM.CREATE_ANY_EVALUATION_CONTEXT` | Create a new evaluation context in any schema |
| `SYS.DBMS_RULE_ADM.CREATE_EVALUATION_CONTEXT_OBJ` | Create a new evaluation context in the grantee's schema |
| `SYS.DBMS_RULE_ADM.CREATE_ANY_RULE` | Create a new rule in any schema |
| `SYS.DBMS_RULE_ADM.CREATE_RULE_OBJ` | Create a new rule in the grantee's schema |
| `SYS.DBMS_RULE_ADM.CREATE_ANY_RULE_SET` | Create a new rule set in any schema |
| `SYS.DBMS_RULE_ADM.CREATE_RULE_SET_OBJ` | Create a new rule set in the grantee's schema |
| `SYS.DBMS_RULE_ADM.DROP_ANY_EVALUATION_CONTEXT` | Drop any evaluation context in any schema |
| `SYS.DBMS_RULE_ADM.DROP_ANY_RULE` | Drop any rule in any schema |
| `SYS.DBMS_RULE_ADM.DROP_ANY_RULE_SET` | Drop any rule set in any schema |
| `SYS.DBMS_RULE_ADM.EXECUTE_ANY_EVALUATION_CONTEXT` | Execute any evaluation context owned by any user |
| `SYS.DBMS_RULE_ADM.EXECUTE_ANY_RULE` | Execute any rule owned by any user |
| `SYS.DBMS_RULE_ADM.EXECUTE_ANY_RULE_SET` | Execute any rule set owned by any user |

For example, to grant the `strmadmin` user the privilege to create a rule set in any schema, enter the following:

```
BEGIN 
  DBMS_RULE_ADM.GRANT_SYSTEM_PRIVILEGE(
    privilege    => SYS.DBMS_RULE_ADM.CREATE_ANY_RULE_SET,
    grantee      => 'strmadmin', 
    grant_option => FALSE);
END;
/
```

#### 156.3.12 REMOVE\_RULE Procedure

This procedure removes the specified rule from the specified rule set.

Syntax

```
DBMS_RULE_ADM.REMOVE_RULE(
   rule_name                IN  VARCHAR2,
   rule_set_name            IN  VARCHAR2,
   evaluation_context       IN  VARCHAR2  DEFAULT NULL,
   all_evaluation_contexts  IN  BOOLEAN   DEFAULT FALSE);
```

Parameters

Table 156-15 REMOVE\_RULE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rule_name` | The name of the rule you are removing from the rule set, specified as `[``schema_name``.]` `rule_name`. For example, to remove a rule named `all_a` in the `hr` schema, enter `hr.all_a` for this parameter. If the schema is not specified, then the current user is the default. |
| `rule_set_name` | The name of the rule set from which you are removing the rule, specified as `[``schema_name``.]` `rule_set_name`. For example, to remove the rule from a rule set named `apply_rules` in the `hr` schema, enter `hr.apply_rules` for this parameter. If the schema is not specified, then the current user is the default. |
| `evaluation_context_name` | The name of the evaluation context associated with the rule you are removing, specified as `[``schema_name``.]` `evaluation_context_name`. For example, to specify an evaluation context named `dept_eval_context` in the `hr` schema, enter `hr.dept_eval_context` for this parameter. If the schema is not specified, then the current user is the default.  If an evaluation context was specified for the rule you are removing when you added the rule to the rule set using the `ADD_RULE` procedure, then specify the same evaluation context. If you added the same rule more than once with different evaluation contexts, then specify the rule with the evaluation context you want to remove. If you specify an evaluation context that is not associated with the rule, then the procedure raises an error.  Specify `NULL` if you did not specify an evaluation context when you added the rule to the rule set. If you specify `NULL` and there are one or more evaluation contexts associated with the rule, then the procedure raises an error. |
| `all_evaluation_contexts` | If `TRUE`, then the procedure removes the rule from the rule set with all of its associated evaluation contexts.  If `FALSE`, then the procedure only removes the rule with the specified evaluation context.  This parameter is relevant only if the same rule is added more than once to the rule set with different evaluation contexts. |

Usage Notes

To run this procedure, a user must meet at least one of the following requirements:

- Have `ALTER_ON_RULE_SET` privilege on the rule set
- Have `ALTER` \_ `ANY` \_ `RULE` \_ `SET` system privilege
- Be the owner of the rule set
	Note:
	This procedure does not drop a rule from the database. To drop a rule from the database, use the `DROP_RULE` procedure.

#### 156.3.13 REVOKE\_OBJECT\_PRIVILEGE Procedure

This procedure revokes the specified object privilege on the specified object from the specified user or role.

Syntax

```
DBMS_RULE_ADM.REVOKE_OBJECT_PRIVILEGE(
   privilege    IN  BINARY_INTEGER,
   object_name  IN  VARCHAR2,
   revokee      IN  VARCHAR2);
```

Parameters

Table 156-16 REVOKE\_OBJECT\_PRIVILEGE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `privilege` | The name of the object privilege on the object to revoke from the revokee. See GRANT\_OBJECT\_PRIVILEGE Procedure for a list of the object privileges. |
| `object_name` | The name of the object for which you are revoking the privilege from the revokee, specified as `[``schema_name``.]` `object_name`. For example, to revoke an object privilege on a rule set named `apply_rules` in the `hr` schema, enter `hr.apply_rules` for this parameter. If the schema is not specified, then the current user is the default. The object must be an existing rule, rule set, or evaluation context. |
| `revokee` | The name of the user or role from which the privilege is revoked. The user who owns the object cannot be specified. |

#### 156.3.14 REVOKE\_SYSTEM\_PRIVILEGE Procedure

This procedure revokes the specified system privilege from the specified user or role.

Syntax

```
DBMS_RULE_ADM.REVOKE_SYSTEM_PRIVILEGE(
   privilege  IN  BINARY_INTEGER,
   revokee    IN  VARCHAR2);
```

Parameters

Table 156-17 REVOKE\_SYSTEM\_PRIVILEGE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `privilege` | The name of the system privilege to revoke from the revokee. See GRANT\_SYSTEM\_PRIVILEGE Procedure for a list of the system privileges. |
| `revokee` | The name of the user or role from which the privilege is revoked |