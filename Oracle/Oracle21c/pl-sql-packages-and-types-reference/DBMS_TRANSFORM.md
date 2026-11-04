---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_TRANSFORM.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 186 DBMS\_TRANSFORM

The `DBMS_TRANSFORM` package provides an interface to the message format transformation features of Oracle Advanced Queuing.

This chapter contains the following topic:

- Summary of DBMS\_TRANSFORM Subprograms

See Also:

[Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADQUE-GUID-95868022-ECDA-4685-9D0A-52ED7663C84B) for more on message format transformations.

### 186.1 Summary of DBMS\_TRANSFORM Subprograms

This table lists the `DBMS_TRANSFORM` subprograms and briefly describes them.

Table 186-1 DBMS\_TRANSFORM Package Subprograms

| Subprograms | Description |
| --- | --- |
| CREATE\_TRANSFORMATION Procedure | Creates a transformation that maps an object of the source type to an object of the destination type |
| DROP\_TRANSFORMATION Procedure | Drops the given transformation |
| MODIFY\_TRANSFORMATION Procedure | Modifies an existing transformation |

#### 186.1.1 CREATE\_TRANSFORMATION Procedure

This procedure creates a transformation that maps an object of the source type to an object of the target type. The transformation expression can be a SQL expression or a PL/SQL function. It must return an object of the target type.

Syntax

```
DBMS_TRANSFORM.CREATE_TRANSFORMATION (
    schema               VARCHAR2(30),
    name                 VARCHAR2(30),
    from_schema          VARCHAR2(30),
    from_type            VARCHAR2(30),
    to_schema            VARCHAR2(30),
    to_type              VARCHAR2(30),
    transformation       VARCHAR2(4000));
```

Parameters

Table 186-2 CREATE\_TRANSFORMATION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema` | Specifies the schema of the transformation. |
| `name` | Specifies the name of the transformation. |
| `from_schema` | Specifies the schema of the source type. |
| `from_type` | Specifies the source type. |
| `to_schema` | Specifies the target type schema. |
| `to_type` | Specifies the target type. |
| `transformation` | Specifies the transformation expression, returning an object of the target type. The expression must be a function returning an object of the target type or a constructor expression for the target type. You can choose not to specify a transformation expression and instead specify transformations for attributes of the target type using `MODIFY_TRANSFORMATION`. |

Usage Notes

- The transformation expression must be a SQL expression or a PL/SQL function returning the type of the specified attribute of the target type.
- To create, modify or drop transformations, a user must be granted execute privileges on `DBMS_TRANSFORM`. The user must also have execute privileges on the user defined types that are the source and destination types of the transformation. In addition, the user must also have execute privileges on any PLSQL function being used in the transformation function.
- The transformation cannot write database state (perform DML) or commit or rollback the current transaction.
- The transformation must be a SQL function with source type as input type, returning an object of the target type. It could also be a SQL expression of target type, referring to a source type. All references to the source type must be of the form `source.user_data`.
- Both source and target types must be non-scalar database types. A null transformation expression maps to a null target object.

For using the transformation at enqueue and dequeue time, the login user invoking the operation must have execute privileges on the PLSQL functions used by the transformation. For propagation, the owning schema of the queue must have these privileges.

#### 186.1.2 DROP\_TRANSFORMATION Procedure

This procedure drops the given transformation.

Syntax

```
DBMS_TRANSFORM.DROP_TRANSFORMATION (
```

schema VARCHAR2(30),

```
name        VARCHAR2(30));
```

Parameters

Table 186-3 DROP\_TRANSFORMATION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema` | Specifies the schema of the transformation. |
| `name` | Specifies the name of the transformation. |

#### 186.1.3 MODIFY\_TRANSFORMATION Procedure

This procedure modifies the transformation expression for the given transformation.

Syntax

```
DBMS_TRANSFORM.MODIFY_TRANSFORMATION (
   schema             VARCHAR2(30),
   name               VARCHAR2(30),
   attribute_number   INTEGER,
   transformation     VARCHAR2(4000));
```

Parameters

Table 186-4 MODIFY\_TRANSFORMATION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema` | Specifies the schema of the transformation. |
| `name` | Specifies the name of the transformation. |
| `attribute_number` | The attribute of the target type for which the new transformation expression is being specified. When specifying the new transformation as a single expression of the target type, specify a value of 0. |
| `transformation` | The transformation expression must be a SQL expression or a PL/SQL function returning the type of the specified attribute of the target type. If the attribute\_number is 0, then the expression must be a PL/SQL function returning an object of the target type or a constructor expression for the target type. |

Usage Notes

- If the new transformation is a single expression of the target type, it may be specified with an `attribute_number` of 0. The new transformation may also be specified for each attribute of the target type.
- You can use this procedure to define the transformation as a separate expression for each attribute of the target type. For large transformations, this representation may be more readable and allow the application of fine grain control over the transformation. If the transformation expression was left unspecified for some of the attributes of the target type, they are evaluated to null when the transformation is applied.