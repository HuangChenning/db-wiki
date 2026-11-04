---
title: "Oracle Data Redaction Use with Oracle Database Features"
book: "Advanced Security Administrator's Guide"
doc_id: E40393-10
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e40393/redaction_other.htm
tags:
  - oracle
  - 11g
  - advanced-security-administrators-guide
---

## 6 Oracle Data Redaction Use with Oracle Database Features

You can use Oracle Data Redaction with other Oracle products, such as Oracle Virtual Private Database or Oracle Enterprise Manager Data Masking and Subsetting Pack.

This chapter contains the following topics:

## 6.1 Oracle Data Redaction and DML and DDL Operations

Although you will use Oracle Data Redaction primarily for redacting the displayed results of application queries, you should understand of how it affects DML and DDL operations, especially if you have users who issue ad-hoc SQL against tables with redacted columns.

Note the following:

- Oracle Data Redaction treats the `RETURNING INTO` clause of a DML statement as a query, even though the result is not displayed. The result that is sent to the buffer is what would have been displayed had the `RETURNING INTO` clause been run as an ordinary SQL query, rather than as part of a DML statement. If your application performs further processing on the buffer that contains the `RETURNING INTO` value, then consider changing the application because it may not expect to find a redacted value in the buffer.
- If a redacted column appears as the source in a DML or DDL operation, then Oracle Data Redaction considers this as an attempt to circumvent the policy and prevents it with an `ORA-28081: Insufficient privileges - the command references a redacted object` error unless you have the `EXEMPT REDACTION POLICY` system privilege. Internally, Oracle Data Pump issues these kinds of operations, so you may also need to grant the `EXEMPT REDACTION POLICY` system privilege to a user if they need to perform schema-level exports of tables that have redacted columns.

## 6.2 Oracle Data Redaction and Nested Functions, Inline Views, and the WHERE Clause

Oracle Data Redaction policies work as follows:

- Nested functions are redacted innermost. For example, in `SELECT SUM(AVG(TO_NUMBER(((X))) FROM HR.EMPLOYEES WHERE ...`, the `TO_NUMBER` function is redacted first, followed by `AVG`, and then last the `SUM` function.
- Inline views are redacted outermost. For example, in `SELECT XYZ … AS SELECT A… AS SELECT B… AS SELECT C…`, `SELECT XYZ` is redacted first, followed by `AS SELECT A`, then `AS SELECT B`, and so on. `AS SELECT C` is redacted last.
- The WHERE clause is never redacted. Data Redaction redacts only data in the column `SELECT` list.

## 6.3 Oracle Data Redaction and Aggregate Functions

Because Oracle Data Redaction dynamically modifies the value of each row in a column, certain SQL queries that use aggregate functions cannot take full advantage of database optimizations that presume the row values to be static. In the case of SQL queries that call aggregate functions, it may be possible to notice performance overhead due to redaction.

## 6.4 Oracle Data Redaction and Object Types

You cannot redact object types. This is because Database Redaction cannot handle all of the possible ways that you can configure object types.

## 6.5 Oracle Data Redaction and Editions

You cannot redact editioned views. You also cannot use a redacted column in the definition of any editioned view.

## 6.6 Oracle Data Redaction and Oracle Virtual Private Database

Oracle Virtual Private Database policies are unaffected by Oracle Data Redaction because the Virtual Private Database inline view, which contains the Virtual Private Database predicate, acts on actual values.

Oracle Data Redaction differs from Oracle Virtual Private Database in the following ways:

- Oracle Data Redaction provides more redacting features than Oracle Virtual Private Database, which only supports `NULL` redacting. Many applications cannot use `NULL` redacting, so Data Redaction is a good solution for these applications.
- Oracle Virtual Private Database policies can be static, dynamic, and context sensitive, whereas Data Redaction policies only allow static and context-sensitive policy expressions.
- Data Redaction permits only one policy to be defined on a table or view, whereas you can define multiple Virtual Private Database policies on an object.
- Data Redaction is when application users try to access an object that is protected by a Data Redaction policy using a synonym, but (unlike Oracle Virtual Private Database) Data Redaction does not support the creation of policies directly on the synonyms themselves.

## 6.7 Oracle Data Redaction and Oracle Database Vault

You can use Oracle Data Redaction in an Oracle Database Vault environment. For example, if there is an Oracle Database Vault realm around an object, a user who does not belong to the authorized list of realm owners or participants cannot see the object data, regardless of whether the user was granted the `EXEMPT REDACTION POLICY` privilege. If the user attempts a DML or DDL statement on the data, error messages result.

## 6.8 Oracle Data Redaction and the EXPDP Utility access\_method Parameter

If you are using Oracle Data Pump to perform full database export operations using the new Data Pump default settings (`direct_path`), and if you receive error messages that you do not understand, then use this section to repeat the operation in such a way as to better understand the error.

If you try to use the Oracle Data Pump Export (`EXPDP`) utility with the `access_method` parameter set to `direct_path` to export data from a schema that contains an object that has a Data Redaction policy defined on it, then the following error message may appear and the export operation fails:

```
ORA-31696: unable to export/import TABLE_DATA:"schema.table" using client specified DIRECT_PATH method
```

This problem only occurs when you perform a schema-level export as a user who was not granted the `EXP_FULL_DATABASE` role. It does not occur during a full database export, which requires the `EXP_FULL_DATABASE` role. The `EXP_FULL_DATABASE` role includes the `EXEMPT REDACTION POLICY` system privilege, which bypasses Data Redaction policies.

To find the underlying problem, try the `EXPDP` invocation again, but do not set the `access_method` parameter to `direct_path`. Instead, use either `automatic` or `external_table`. The underlying problem could be a permissions problem, for example:

```
ORA-28081: Insufficient privileges - the command references a redacted object.
```

See Also:

[Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/dp_export.htm#SUTIL200) for more information about using Data Pump Export.

## 6.9 Oracle Data Redaction and Data Masking and Subsetting Pack

Oracle Enterprise Manager Data Masking and Subsetting Pack enables you to create a development or test copy of the production database, by taking the data in the production database, masking this data in bulk, and then putting the resulting masked data in the development or test copy. You can still apply Data Redaction policies to the non-production database, in order to redact columns that contain data that was already masked by Oracle Enterprise Manager Data Masking and Subsetting Pack.

Remember that Oracle Enterprise Manager Data Masking and Subsetting Pack is used to mask data sets when you want to move the data to development and test environments. Data Redaction is mainly designed for redacting at runtime for production applications in a consistent fashion across multiple applications, without having to make application code changes.

See Also:

[Oracle Database Real Application Testing User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41481/tdm_data_masking.htm#RATUG04000) for more information about data masking