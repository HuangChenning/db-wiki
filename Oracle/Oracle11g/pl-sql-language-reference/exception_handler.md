---
title: Exception Handler
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/exception_handler.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

An exception handler processes a raised exception. Exception handlers appear in the exception-handling parts of anonymous blocks, subprograms, triggers, and packages.

Topics

Semantics

exception

Name of either a predefined exception (see [Table 11-3](errors.md)) or a user-defined exception (see ["Exception Declaration"](exception_declaration.md)).

If PL/SQL raises a specified exception, then the associated statements run.

OTHERS

Specifies all exceptions not explicitly specified in the exception-handling part of the block. If PL/SQL raises such an exception, then the associated statements run.

Note:

Oracle recommends that the last statement in the `OTHERS` exception handler be either `RAISE` or an invocation of the `RAISE_APPLICATION_ERROR` procedure.

If you do not follow this practice, and PL/SQL warnings are enabled, you get PLW-06009.

In the exception-handling part of a block, the `WHEN` `OTHERS` exception handler is optional. It can appear only once, as the last exception handler in the exception-handling part of the block.

Examples

- [Example 11-3, "Single Exception Handler for Multiple Exceptions"](errors.md)
- [Example 11-4, "Locator Variables for Statements that Share Exception Handler"](errors.md)
- [Example 11-6, "Anonymous Block Handles ZERO\_DIVIDE"](errors.md)
- [Example 11-9, "Declaring, Raising, and Handling User-Defined Exception"](errors.md)
- [Example 11-13, "Exception that Propagates Beyond Scope is Handled"](errors.md)
- [Example 11-23, "Exception Handler Runs and Execution Ends"](errors.md)
- [Example 11-24, "Exception Handler Runs and Execution Continues"](errors.md)
- [Example 12-12, "Handling FORALL Exceptions Immediately"](tuning.md)
- [Example 12-13, "Handling FORALL Exceptions After FORALL Statement Completes"](tuning.md)

Related Topics

In this chapter:

- ["Block"](block.md)
- ["EXCEPTION\_INIT Pragma"](exceptioninit_pragma.md)
- ["Exception Declaration"](exception_declaration.md)
- ["Function Declaration and Definition"](function.md)
- ["Procedure Declaration and Definition"](procedure.md)
- ["RAISE Statement"](raise_statement.md)
- ["SQLCODE Function"](sqlcode_function.md)
- ["SQLERRM Function"](sqlerrm_function.md)

In other chapters:

- ["Overview of Exception Handling"](errors.md)
- ["Continuing Execution After Handling Exceptions"](errors.md)
- ["Retrying Transactions After Handling Exceptions"](errors.md)
- ["CREATE PACKAGE BODY Statement"](create_package_body.md)
- ["CREATE TRIGGER Statement"](create_trigger.md)