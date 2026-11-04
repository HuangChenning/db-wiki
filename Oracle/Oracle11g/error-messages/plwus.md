---
title: PLW-05000 to PLW-07206
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/plwus.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 53 PLW-05000 to PLW-07206

PLW-05000: mismatch in NOCOPY qualification between specification and body

Cause: The indicated parameter was declared with the NOCOPY hint in the subprogram specification but not in the body, or it was declared with the NOCOPY hint in the body but not in the specification.

Action: Ensure that the specification and the body agree in their use of NOCOPY. If this mismatch is not corrected, the program will obey the declaration given in the specification, ignoring that in the body.

PLW-05001: previous use of 'string' (at line string) conflicts with this use

Cause: While looking for prior declarations of a variable, constant, or label, the compiler found another declaration with the same name in the same scope. Or, the headers of subprogram in a package specification and body were not identical.

Action: Check the spelling of the variable, constant, or label name. Also check the names of all parameters and exceptions declared in the same scope. Then, remove or rename the object with the duplicate name. Or, change the headers of the packaged subprogram in the package specification or body so that they are identical.

PLW-05003: same actual parameter(string and string) at IN and NOCOPY may have side effects

Cause: The indicated parameter was declared with the NOCOPY hint in the subprogram specification but not in the body, or it was declared with the NOCOPY hint in the body but not in the specification.

Action: Ensure that the specification and the body agree in their use of NOCOPY. If this mismatch is not corrected, the program will obey the declaration given in the specification, ignoring that in the body.

PLW-05004: identifier string is also declared in STANDARD or is a SQL builtin

Cause: The indicated identifier was also either: o) declared in package STANDARD, or o) a SQL builtin function, or o) a pseudo-column. This situation can result in name resolution issues since the STANDARD/builtin declaration will be chosen over the local declaration in SQL statements; however the local declaration will be chosen over the STANDARD/builtin declaration outside SQL scope. (See the documentation on PL/SQL name resolution.)

Action: Either: o) rename the given identifier, o) qualify any references to the identifier with the containing scope's name, or o) make sure the intended resolution occurs if using the identifier in SQL scope.

PLW-05005: subprogram string returns without value at line string

Cause: A function terminated without a return value. RETURN statements with values are required for all PL/SQL functions.

Action: Inspect function source code to ensure that every RETURN statement returns a value and that a function does not terminate by executing its END statement. Notice that this message may appear at the call site for a function if the function call was inlined and if the called function did not terminate properly.

PLW-05006: shadow type generation resulted in warning: string

Cause: Compilation of a table function causes the creation of internally- generated types. A problem occurred during creation of these types which was not severe enough to prevent the creation of the types, but which may impact the usage of the table function. See the accompanying error message for more information.

Action: Fix the issue reported in the accompanying error message.

PLW-05007: first parameter to pragma INLINE must be an identifier

Cause: The first parameter to the pragma INLINE must be an identifier denoting a procedure or function.

Action: Use a procedure or function name

PLW-05008: illegal number of arguments for pragma string

Cause: The number of arguments (actual parameters) passed to the named pragma (compiler directive) is incorrect. A required argument was omitted from the argument list, or the pragma syntax is faulty (for example, a comma might be missing between two parameters).

Action: Supply the missing argument or correct the faulty syntax.

PLW-05009: pragma INLINE may not appear in a declaration list

Cause: Pragma INLINE applies only to the following statement, and can not appear immediately prior to a declaration

Action: Remove the pragma.

PLW-05010: duplicate pragma INLINE on procedure 'string'

Cause: Pragma INLINE was applied twice to the same procedure in the same statement. The procedure will be inlined only if all duplicates specify a control value of 'YES'

Action: Remove the duplicate pragma.

PLW-05011: pragma INLINE for procedure 'string' does not apply to any calls

Cause: A pragma INLINE was provided, but there was no call to the mentioned procedure in the next statement.

Action: Remove the unnecessary pragma.

PLW-05012: pragma INLINE for procedure 'string' could not be applied

Cause: A pragma INLINE(\<name>, 'yes') was used, but the named procedure could not be inlined.

Action: Eliminate the reasons which are blocking the inlining. See the documentation for possible problems.

PLW-05013: second parameter to pragma INLINE 'string' is not 'YES' or 'NO'

Cause: The second parameter to the pragma INLINE governs whether or not a procedure call can be inlined. The only legal values are 'YES', meaning that the compiler should attempt to inline the call, and 'NO', meaning that the compiler must not inline the call.

Action: Use 'YES' or 'NO' as appropriate.

PLW-05014: Pragma string cannot be specified here

Cause: The pragma was specified in an inappropriate context.

Action: Remove or relocate the misplaced pragma. Check the documentation to determine the correct context for this pragma.

PLW-05015: implementation restriction - too many debug records

Cause: The program is so large that it overflowed a compiler limit on the size of the debug symbol table. The module was compiled with partial debugging information.

Action: Compile the module with PLSQL\_DEBUG=FALSE, or split it into multiple modules

PLW-05016: INTO clause should not be specified here

Cause: The INTO clause was incorrectly specified on a cursor declaration. It should have been specified on the FETCH statement.

Action: Relocate the misplaced clause.

PLW-05017: prefix of the expression will be ignored

Cause: Generalized invocation with explicit SELF and a dotted name was used to call the type method causing the prefix of the dotted name to be ignored.

Action: Do not use a dotted name to invoked type method in this context.

PLW-05018: unit string omitted optional AUTHID clause; default value DEFINER used

Cause: The AUTHID clause is missing. The unit is allowed to have an AUTHID clause. If the clause is missing, DEFINER's rights are used by default. Good practice suggests that an explicit AUTHID clause should always be used.

Action: Write an explicit AUTHID clause for the unit.

PLW-05019: the language element near keyword string is deprecated beginning with version string

Cause: A deprecated language element was used. The particular language element is deprecated in PL/SQL versions greater than or equal to the version number given in the message text.

Action: The deprecated language element should be deleted or rewritten. Deprecated PL/SQL language elements become obsolete one version after they are deprecated. An obsolete language element will no longer be supported and use of the element will result in an error.

PLW-05020: parameter name must be an identifier

Cause: A string literal was used as the parameter name in a call that used named notation.

Action: Change the code to use an identifier for the parameter name.

PLW-05022: argument 'string' is not comparable

Cause: An argument to either IN, BETWEEN or MEMBER OF was not of a comparable type. Or, if the argument was of an object type, no MAP or ORDER method was specified for the type.

Action: Use appropriate arguments, or specify a MAP or ORDER method.

PLW-05023: PL/Scope is disabled because SYSAUX is offline.

Cause: PL/Scope was disabled for the current PL/SQL unit compilation because the SYSAUX tablespace is or was offline at the time of compilation. Note that PL/Scope stores identified metadata in the SYSAUX tablespace, and thus cannot function when SYSAUX is offline.

Action: Verify SYSAUX is online and recompile the PL/SQL unit.

PLW-05024: Do not use BULK COLLECT clause in a cursor declaration

Cause: A BULK COLLECT clause was specified in a cursor declaration.

Action: Remove the BULK COLLECT clause from the cursor declaration, moving it to the FETCH statement or statements, if appropriate.

PLW-06002: Unreachable code

Cause: d by expression evaluation at compile time.

Action: Inspect program logic for possible defects. Disable the warning if much code is made unreachable intentionally and the warning message is more annoying than helpful.

PLW-06003: unknown inquiry directive 'string'

Cause: An unknown inquiry directive was used. The inquiry directive is neither predefined nor user-defined.

Action: Use a predefined inquiry directive or define the inquiry directive.

PLW-06004: inlining of call of procedure 'string' requested

Cause: A pragma INLINE(, 'YES') referring to the named procedure was found. The compiler will, if possible, inline this call.

Action: None

PLW-06005: inlining of call of procedure 'string' was done

Cause: A call to the procedure was inlined.

Action: None

PLW-06006: uncalled procedure "string" is removed.

Cause: Static program analysis determined that the procedure can never be called or executed. Therefore, it has been removed to save time during compilation and space during execution.

Action: Inspect program logic for possible defects. Disable the warning if the procedure is useful but simply not being used right now and the warning message is more annoying than helpful.

PLW-06007: procedure "string" is removed because optimization removed calls

Cause: Static program analysis determined that the procedure can never be called or executed. Therefore, it has been removed to save time during compilation and space during execution.

Action: Inspect program logic for possible defects. Disable the warning if the procedure is useful but simply not being used right now and the warning message is more annoying than helpful.

PLW-06008: call of procedure 'string' will not be inlined

Cause: A pragma INLINE(, 'NO') referring to the named procedure was found. The compiler is prevented from inlining this call.

Action: None

PLW-06009: procedure "string" OTHERS handler does not end in RAISE or RAISE\_APPLICATION\_ERROR

Cause: The OTHERS handler can exit without executing some form of RAISE or or a call to the standard procedure RAISE\_APPLICATION\_ERROR.

Action: Good programming practices suggest that OTHERS handlers must always pass an exception upward. Inspect the program logic to determine if the handler code needs revision.

PLW-06010: keyword "string" used as a defined name

Cause: A PL/SQL or SQL keyword was used as defined name. Although legal, this is not recommended.

Action: Choose another name for the defined item.

PLW-06011: detailed dependency information discarded due to size limitations

Cause: The compiled unit was so large that the compiler could not store detailed dependency information that could be used to quickly recompile the unit if it was invalidated.

Action: Break up the unit into smaller units.

PLW-06012: SQL statement cannot be inlined. string

Cause: The SQL statement could not be inlined.

Action: None

PLW-06013: deprecated parameter PLSQL\_DEBUG forces PLSQL\_OPTIMIZE\_LEVEL <= 1

Cause: The PLSQL\_DEBUG parameter was set to TRUE forcing the optimization level to 1 (or 0 if the user selected 0) regardless of the setting of the PLSQL\_OPTIMIZE\_LEVEL parameter to a higher level

Action: Do not use the PLSQL\_DEBUG parameter; it is deprecated. Instead, set the PLSQL\_OPTIMIZE\_LEVEL parameter to 1.

PLW-06014: PLSQL\_OPTIMIZE\_LEVEL <= 1 turns off native code generation

Cause: Native code generation was not done because the optimization was set to 1 or less.

Action: The goal of native code generation is high performance and a low optimization level defeats that purpose. Either request a higher optimization level or remove the request for native code generation. Note that using the deprecated parameter PLSQL\_DEBUG also forces the optimization level to 1; do not use this parameter when native code generation is desired.

PLW-06015: parameter PLSQL\_DEBUG is deprecated; use PLSQL\_OPTIMIZE\_LEVEL = 1

Cause: The PLSQL\_DEBUG parameter was specified.

Action: The parameter PLSQL\_DEBUG no longer controls the generation of debugging information by the PL/SQL compiler; debugging information is always generated and no special parameter is needed.

PLW-06016: unit string is too large; native code generation turned off

Cause: Because the program was extremely large, analysis took an excessive amount of time or space to complete causing native compilation to be turned off.

Action: The goal of native code generation is high performance and the compiler does extensive analysis of the program. If possible, reduce the size of the largest procedure, or split the program unit into multiple units.

PLW-06017: an operation will raise an exception

Cause: An operation near this location is certain to raise an exception during execution; it may be a programming error because it is not an explicit RAISE.

Action: The compiler has determined that some operation near this location is certain to raise an exception during execution. This may be a programming error; consider rewriting the code. If the intention is to raise an exception, use an explicit RAISE statement.

PLW-06018: an infinity or NaN value is computed or used

Cause: An operation near this location computes or uses an infinite NUMBER, BINARY\_FLOAT, or BINARY\_DOUBLE value or a NaN BINARY\_FLOAT or BINARY\_DOUBLE value.

Action: The compiler has determined that an operation near this location computes or uses either an infinity or a not-a-number (NaN) value. This may indicate a programming error; consider rewriting the code. If the intention is to use a BINARY\_FLOAT or a BINARY\_DOUBLE non-numeric value, use the appropriate constant from STANDARD rather than computing the value. Some valid uses exist for these values; the warning will still appear in those cases. The use of infinite NUMBER values is not well-defined and should be avoided.

PLW-07202: bind type would result in conversion away from column type

Cause: The column type and the bind type do not exactly match. This will result in the column being converted to the type of the bind variable. This type conversion may prevent the SQL optimizer from using any index the column participates in. This may adversely affect the execution performance of this statement.

Action: To make use of any index for this column, make sure the bind type is the same type as the column type.

PLW-07203: parameter 'string' may benefit from use of the NOCOPY compiler hint

Cause: The mode of the specified parameter was IN OUT or OUT. Use of the NOCOPY compiler hint may speed up calls to this subprogram.

Action: Change the mode of the parameter to explicitly use the NOCOPY compiler hint. For example, if your subprogram declaration is: PROCEDURE proc(p1 IN OUT CLOB); you can change it to: PROCEDURE proc(p1 IN OUT NOCOPY clob); to get the benefit of the NOCOPY hint. For member procedures or functions in object types, you may have to explicitly declare the SELF parameter as illustrated in the following: MEMBER PROCEDURE proc(SELF IN OUT NOCOPY MY\_TYPE);

PLW-07204: conversion away from column type may result in sub-optimal query plan

Cause: The column type and the bind type do not exactly match. This may result in the column being converted to the type of the bind variable. This type conversion may prevent the SQL optimizer from using any index the column participates in. This may adversely affect the execution performance of this statement.

Action: To make use of any index for this column, make sure the bind type is the same type as the column type.

PLW-07205: SIMPLE\_INTEGER is mixed with BINARY\_INTEGER or PLS\_INTEGER

Cause: Using SIMPLE\_INTEGER and BINARY\_INTEGER or PLS\_INTEGER arguments in the same arithmetic expression may inhibit certain optimizations.

Action: Try using SIMPLE\_INTEGER values only if the expression is computed on a performance critical path.

PLW-07206: analysis suggests that the assignment to 'string' may be unnecessary

Cause: This assignment may be unnecessary; the PL/SQL optimizer could not find any further use of the variable which was being set. If the assignment was being done for some side-effect such as raising a specific exception, the compiler may not have been able to understand the side-effect and this warning may be inappropriate.

Action: If the assignment sets a variable whose value will not be used again and there are no side-effects (exceptions or calls) to consider, remove the assignment for better performance. If the assignment was in place to raise a specific known exception, replace the assignment with a RAISE statement.