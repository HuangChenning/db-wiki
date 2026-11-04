---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/IGNORE_SESSION_SET_PARAM_ERRORS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.148 IGNORE\_SESSION\_SET\_PARAM\_ERRORS

`IGNORE_SESSION_SET_PARAM_ERRORS` controls whether the database ignores errors when clients attempt to modify session parameter values.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `IGNORE_SESSION_SET_PARAM_ERRORS = parameter_name [, parameter_name ] ...` |
| Default value | None |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | Multiple instances should use the same value. |

The `IGNORE_SESSION_SET_PARAM_ERRORS` parameter allows you to change the outcome of the following scenario:

1. An Oracle database uses PDB lockdown profiles to prevent certain initialization parameters from being modified with the `ALTER` `SESSION` statement.
2. A database client attempts to modify one of those parameters with the `ALTER` `SESSION` statement. The client has no knowledge that the parameter is locked down.
3. The database returns an error to the client.

To prevent the database from returning an error in the preceding scenario, set the value of `IGNORE_SESSION_SET_PARAM_ERRORS` to a comma-separated list of locked down initialization parameters. Thereafter, if a client attempts to modify one of those parameters with the `ALTER` `SESSION` statement, the database will ignore the modification attempt and indicate to the client that the operation was successful.

You can set the `IGNORE_SESSION_SET_PARAM_ERRORS` parameter while connected to a specific PDB, or you can apply it to all PDBs by setting it in the CDB root.

Example

The `CURSOR_INVALIDATION` and `CURSOR_SHARING` parameters are locked down in one of the PDBs in your database. If a client application attempts to modify either of these parameters, you want the database to ignore the request and allow the application to continue running without incurring an error. To achieve this, you can connect to the PDB and set the `IGNORE_SESSION_SET_PARAM_ERRORS` parameter. For example:

```
ALTER SYSTEM SET IGNORE_SESSION_SET_PARAM_ERRORS = CURSOR_INVALIDATION, CURSOR_SHARING;
```