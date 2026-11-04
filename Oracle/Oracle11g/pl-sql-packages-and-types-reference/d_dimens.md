---
title: DBMS_DIMENSION
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_dimens.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 59 DBMS\_DIMENSION

`DBMS_DIMENSION` enables you to verify dimension relationships and provides an alternative to the Enterprise Manager Dimension Wizard for displaying a dimension definition.

See Also:

[Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/dimen.htm#DWHSG010) for detailed conceptual and usage information about the `DBMS_DIMENSION` package

This chapter contains the following topics:

- Using DBMS\_DIMENSION
	- Security Model
- Summary of DBMS\_DIMENSION Subprograms

---

## Using DBMS\_DIMENSION

This section contains topics which relate to using the `DBMS_DIMENSION` package.

- Security Model

---

### Security Model

Security on this package can be controlled by granting `EXECUTE` to selected users or roles.

A user can validate or describe all the dimensions in his own schema. To validate or describe a dimension in another schema, you must have either an object privilege on the dimension or one of the following system privileges: `CREATE ANY DIMENSION`, `ALTER ANY DIMENSION`, and `DROP ANY DIMENSION`.

---

## Summary of DBMS\_DIMENSION Subprograms

Table 59-1 DBMS\_DIMENSION Package Subprograms

| Subprogram | Description |
| --- | --- |
| DESCRIBE\_DIMENSION Procedure | Prints out the definition of the input dimension, including dimension owner and name, levels, hierarchies, and attributes |
| VALIDATE\_DIMENSION Procedure | Verifies that the relationships specified in a dimension are correct |

---

### DESCRIBE\_DIMENSION Procedure

This procedure displays the definition of the dimension, including dimension name, levels, hierarchies, and attributes. It displays the output using the `DBMS_OUTPUT` package.

Syntax

```
DBMS_DIMENSION.DESCRIBE_DIMENSION (
   dimension  IN VARCHAR2);
```

Parameters

Table 59-2 DESCRIBE\_DIMENSION Procedure Parameter

| Parameter | Description |
| --- | --- |
| `dimension` | The owner and name of the dimension in the format of `owner.name`. |

---

### VALIDATE\_DIMENSION Procedure

This procedure verifies that the relationships specified in a dimension are valid. The rowid for any row that is found to be invalid will be stored in the table `DIMENSION_EXCEPTIONS` in the user's schema.

Syntax

```
DBMS_DIMENSION.VALIDATE_DIMENSION (
   dimension               IN VARCHAR2,
   incremental             IN BOOLEAN := TRUE,
   check_nulls             IN BOOLEAN := FALSE,
   statement_id            IN VARCHAR2 := NULL );
```

Parameters

Table 59-3 VALIDATE\_DIMENSION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `dimension` | The owner and name of the dimension in the format of `owner.name`. |
| `incremental` | If `TRUE`, check only the new rows for tables of this dimension. If `FALSE`, check all the rows. |
| `check_nulls` | If `TRUE`, then all level columns are verified to be non-null.  If `FALSE`, this check is omitted. Specify `FALSE` when non- `NULL` ness is guaranteed by other means, such as `NOT` `NULL` constraints. |
| `statement_id` | A client-supplied unique identifier to associate output rows with specific invocations of the procedure. |