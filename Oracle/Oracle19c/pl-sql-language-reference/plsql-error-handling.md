---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/plsql-error-handling.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## 11 PL/SQL Error Handling

This chapter explains how to handle PL/SQL compile-time warnings and PL/SQL runtime errors. The latter are called exceptions.

Note:

The language of warning and error messages depends on the `NLS_LANGUAGE` parameter. For information about this parameter, see [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=NLSPG199).

Topics

- [Compile-Time Warnings](compile-time-warnings.md)
- [Overview of Exception Handling](overview-exception-handling.md)
- [Internally Defined Exceptions](internally-defined-exceptions.md)
- [Predefined Exceptions](predefined-exceptions.md)
- [User-Defined Exceptions](user-defined-exceptions.md)
- [Redeclared Predefined Exceptions](redeclared-predefined-exceptions.md)
- [Raising Exceptions Explicitly](raising-exceptions-explicitly.md)
- [Exception Propagation](exception-propagation.md)
- [Unhandled Exceptions](unhandled-exceptions.md)
- [Retrieving Error Code and Error Message](retrieving-error-code-and-error-message.md)
- [Continuing Execution After Handling Exceptions](continuing-execution-handling-exceptions.md)
- [Retrying Transactions After Handling Exceptions](retrying-transactions-handling-exceptions.md)
- [Handling Errors in Distributed Queries](handling-errors-distributed-queries.md)

See Also:

- " [Exception Handling in Triggers](exception-handling-triggers.md) "
- " [Handling FORALL Exceptions After FORALL Statement Completes](bulk-sql-and-bulk-binding.md) "

Tip:

If you have problems creating or running PL/SQL code, check the Oracle Database trace files. The `DIAGNOSTIC_DEST` initialization parameter specifies the current location of the trace files. You can find the value of this parameter by issuing `SHOW` `PARAMETER` `DIAGNOSTIC_DEST` or query the `V$DIAG_INFO` view. For more information about diagnostic data, see [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ADMIN11007).