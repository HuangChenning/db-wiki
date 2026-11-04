---
title: Defining Operators
book: "Data Cartridge Developer's Guide"
doc_id: E10765-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/operators.htm
tags:
  - oracle
  - 11g
  - data-cartridge-developers-guide
---

## 9 Defining Operators

This chapter introduces user-defined operators and then demonstrates how to use them, both with and without indextypes.

This chapter contains these topics:

- User-Defined Operators
- Operators and Indextypes

## User-Defined Operators

A user-defined operator is a top-level schema object. In many ways, user-defined operators act like the built-in operators such as <, >, and =; for instance, they can be invoked in all the same situations. They contribute to ease of use by simplifying SQL statements, making them shorter and more readable.

User-defined operators are:

- Identified by names, which are in the same namespace as tables, views, types, and standalone functions
- Bound to functions, which define operator behavior in specified contexts
- Controlled by privileges, which indicate the circumstances in which each operator can be used
- Often associated with indextypes, which can be used to define indexes that are not built into the database

See Also:

Oracle Database SQL Language Reference for detailed information on syntax and privileges

### Operator Bindings

An operator binding associates the operator with the signature of a function that implements the operator. A signature consists of a list of the data types of the arguments of the function, in order of occurrence, and the function's return type. Operator bindings tell Oracle which function to execute when the operator is invoked. An operator can be bound to several functions if each function has a different signature. To be considered different, functions must have different argument lists. Functions whose argument lists match, but whose return data types do not match, are not considered different and cannot be bound to the same operator.

Operators can be bound to:

- Standalone functions
- Package functions
- User-defined type member methods

Operators can be bound to functions and methods in any accessible schema. Each operator must have at least one binding when you create it. If you attempt to specify non-unique operator bindings, the Oracle server raises an error.

### Operator Privileges

To create an operator and its bindings, you must have:

- `CREATE` `OPERATOR` or `CREATE` `ANY` `OPERATOR` privilege
- `EXECUTE` privilege on the function, operator, package, or type referenced

To drop a user-defined operator, you must own the operator or have the `DROP` `ANY` `OPERATOR` privilege.

To invoke a user-defined operator in an expression, you must own the operator or have `EXECUTE` privilege on it.

### Creating Operators

To create an operator, specify its name and its bindings with the `CREATE OPERATOR` statement. Example 9-1 creates the operator `Contains()`, binding it to functions that provide implementations in the Text and Spatial domains.

Example 9-1 Creating an Operator

```
CREATE OPERATOR Contains
BINDING
(VARCHAR2, VARCHAR2) RETURN NUMBER USING text.contains,
(Spatial.Geo, Spatial.Geo) RETURN NUMBER USING Spatial.contains;
```

### Dropping Operators

To drop an operator and all its bindings, specify its name with the `DROP` `OPERATOR` statement. Example 9-2 drops the operator `Contains()`.

Example 9-2 Dropping an Operator; RESTRICT Option

```
DROP OPERATOR Contains;
```

The default `DROP` behavior is `DROP` `RESTRICT`: if there are dependent indextypes or ancillary operators for any of the operator bindings, then the `DROP` operation is disallowed.

To override the default behavior, use the `FORCE` option. Example 9-3 drops the operator and all its bindings and marks any dependent indextype objects and dependent ancillary operators invalid.

Example 9-3 Dropping an Operator; FORCE Option

```
DROP OPERATOR Contains FORCE;
```

### Altering Operators

You can add bindings to or drop bindings from an existing operator with the `ALTER OPERATOR` statement. Example 9-4 adds a binding to the operator `Contains().`

Example 9-4 Adding a Binding to an Operator

```
ALTER OPERATOR Contains
  ADD BINDING (music.artist, music.artist) RETURN NUMBER
  USING music.contains;
```

You need certain privileges to perform alteration operations:

- To alter an operator, the operator must be in your own schema, or you must have the `ALTER ANY OPERATOR` privilege.
- You must have `EXECUTE` privileges on the operators and functions referenced.

The following restrictions apply to the `ALTER OPERATOR` statement:

- You can only issue `ALTER OPERATOR` statements that relate to existing operators.
- You can only add or drop one binding in each `ALTER OPERATOR` statement.
- You cannot drop an operator's only binding with `ALTER OPERATOR`; use the `DROP OPERATOR` statement to drop the operator. An operator cannot exist without any bindings.
- If you add a binding to an operator associated with an indextype, the binding is not associated to the indextype unless you also issue the `ALTER INDEXTYPE ADD OPERATOR` statement

### Commenting Operators

To add comment text to an operator, specify the name and text with the `COMMENT` statement. Example 9-5 supplies information about the `Contains()` operator:

Example 9-5 Adding COMMENTs to an Operator

```
COMMENT ON OPERATOR
Contains IS 'a number that indicates if the text contains the key';
```

Comments on operators are available in the data dictionary through these views:

- `USER_OPERATOR_COMMENTS`
- `ALL_OPERATOR_COMMENTS`
- `DBA_OPERATOR_COMMENTS`

You can only comment operators in your own schema unless you have the `COMMENT ANY OPERATOR` privilege.

### Invoking Operators

Like built-in operators, user-defined operators can be invoked wherever expressions can occur. For example, user-defined operators can be used in:

- The select list of a `SELECT` command.
- The condition of a `WHERE` clause.
- The `ORDER` `BY` and `GROUP` `BY` clauses.

When an operator is invoked, Oracle evaluates the operator by executing a function bound to it. When several functions are bound to the operator, Oracle executes the function whose argument data types match those of the invocation (after any implicit type conversions). Invoking an operator with an argument list that does not match the signature of any function bound to that operator causes an error to be raised. Because user-defined operators can have multiple bindings, they can be used as overloaded functions.

Assume that Example 9-6 creates the operator `Contains()`.

Example 9-6 Creating the Contains() Operator

```
CREATE OPERATOR Contains
BINDING 
(VARCHAR2, VARCHAR2) RETURN NUMBER 
USING text.contains, 
(spatial.geo, spatial.geo) RETURN NUMBER 
USING spatial.contains;
```

If `Contains()` is used in Example 9-7, the operator invocation `Contains(resume,` `'Oracle')` causes Oracle to execute the function `text.contains(resume,` `'Oracle')` because the signature of the function matches the data types of the operator arguments. Similarly, the operator invocation `Contains(location`, `:bay_area)` executes the function `spatial.contains(location`, `:bay_area)`.

Example 9-7 Using the Operator Contains() in a Query

```
SELECT * FROM MyEmployees
WHERE Contains(resume, 'Oracle')=1 AND Contains(location, :bay_area)=1;
```

Executing the statement in Example 9-8 raises an error because none of the operator bindings satisfy the argument data types.

Example 9-8 An Incorrect Use of the Operator Contains()

```
SELECT * FROM MyEmployees
WHERE Contains(address, employee_addr_type('123 Main Street', 'Anytown', 'CA',
  '90001'))=1;
```

## Operators and Indextypes

Operators are often defined in connection with indextypes. After creating the operators with their functional implementations, you can create an indextype that supports evaluations of these operators using an index scan.

Operators that occur outside `WHERE` clauses are essentially stand-ins for the functions that implement them; the meaning of such an operator is determined by its functional implementation. Operators that occur in `WHERE` clauses are sometimes evaluated using functional implementations; at other times they are evaluated by index scans. This section describes the various situations and the methods of evaluation.

### Operators in the WHERE Clause

Operators appearing in the `WHERE` clause can be evaluated efficiently by an index scan using the scan methods provided by the indextype. This process involves:

1. Creating an indextype that supports the evaluation of the operator
2. Recognizing operator predicates of a certain form
3. Selecting a domain index
4. Setting up an appropriate index scan
5. Executing the index scan methods

The following sections describe each of these steps in detail.

#### Operator Predicates

An indextype supports efficient evaluation of operator predicates that can be represented by a range of lower and upper bounds on the operator return values. Specifically, predicates of the forms listed in Example 9-9 are candidates for index scan-based evaluation.

Example 9-9 Operator Predicates

```
op(...) LIKE value_expression
op(...) relop value_expression
```

where `value_expression` must evaluated to a constant (not a column) that can be used as a domain index key, and `relop` is one of `<`, `<=`, `=`, `>=`, or `>`

Operator predicates that Oracle can convert internally into one of the forms in Example 9-9 can also make use of the index scan-based evaluation.

Using the operators in expressions, such as `op(...) + 2 = 3`, precludes index scan-based evaluation.

Predicates of the form `op() is NULL` are evaluated using the functional implementation.

#### Operator Resolution

An index scan-based evaluation of an operator is only possible if the operator operates on a column or object attribute indexed by an indextype. The optimizer makes the final decision between the indexed implementation and the functional implementation, taking into account the selectivity and cost while generating the query execution plan.

Consider the query in Example 9-10.

Example 9-10 Using the Contains() Operator in a Simple Query

```
SELECT * FROM MyEmployees WHERE Contains(resume, 'Oracle') = 1;
```

The optimizer can choose to use a domain index in evaluating the `Contains()` operator if

- The `resume` column has a defined index.
- The index is of type `TextIndexType`.
- `TextIndexType` supports the appropriate `Contains()` operator.

If any of these conditions do not hold, Oracle performs a complete scan of the `MyEmployees` table and applies the functional implementation of `Contains()` as a post-filter. However, if all these conditions are met, the optimizer uses selectivity and cost functions to compare the cost of index-based evaluation with the full table scan and generates the appropriate execution plan.

Consider a slightly different query in Example 9-11.

Example 9-11 Using the Contains() Operator in a Complex Query

```
SELECT * FROM MyEmployees WHERE Contains(resume, 'Oracle') =1 AND id =100;
```

Here, you can access the `MyEmployees` table through an index on the `id` column, one on the `resume` column, or a bitmap merge of the two. The optimizer estimates the costs of the three plans and picks the least expensive variant one, which could be to use the index on `id` and apply the `Contains()` operator on the resulting rows. In that case, Oracle would use the functional implementation of `Contains()` rather than the domain index.

#### Index Scan Setup

If a domain index is selected for the evaluation of an operator predicate, an index scan is set up. The index scan is performed by the scan methods [ODCIIndexStart()](ext_idx_ref.md), [ODCIIndexFetch()](ext_idx_ref.md), and [ODCIIndexClose()](ext_idx_ref.md), specified as part of the corresponding indextype implementation. The [ODCIIndexStart()](ext_idx_ref.md) method is invoked with the operator-related information, including name and arguments and the lower and upper bounds describing the predicate. After the [ODCIIndexStart()](ext_idx_ref.md) call, a series of fetches are performed to obtain row identifiers of rows satisfying the predicate, and finally the [ODCIIndexClose()](ext_idx_ref.md) is called when the SQL cursor is destroyed.

#### Execution Model for Index Scan Methods

To implement the index scan routines, you must understand how they are invoked and how multiple sets of invocations can be combined.

As an example, consider the query in Example 9-12.

Example 9-12 Using the Contains() Operator in a Multiple Table Query

```
SELECT * FROM MyEmployees1, MyEmployees2 
WHERE 
  Contains(MyEmployees1.resume, 'Oracle') =1 AND 
  Contains(MyEmployees2.resume, 'UNIX') =1 AND 
  MyEmployees1.employee_id = MyEmployees2.employee_id;
```

If the optimizer choses to use the domain indexes on the `resume` columns of both tables, the indextype routines might be invoked in the sequence demonstrated in Example 9-13.

Example 9-13 Invoking Indextype Routines for the Contains() Operator Query

```
start(ctx1, ...); /* corr. to Contains(MyEmployees1.resume, 'Oracle') */
start(ctx2, ...); /* corr. to Contains(MyEmployees2.resume, 'UNIX');
fetch(ctx1, ...);
fetch(ctx2, ...);
fetch(ctx1, ...);
...
close(ctx1);
close(ctx2);
```

In this example, a single indextype routine is invoked several times for different instances of the `Contains()` operator. It is possible that many operators are being evaluated concurrently through the same indextype routines. A routine that gets all the information it needs through its parameters, such as the `CREATE` routine, does not maintain any state across calls, so evaluating multiple operators concurrently is not a problem. Other routines that must maintain state across calls, like the `FETCH` routine, must know which row to return next. These routines should maintain state information in the `SELF` parameter that is passed in to each call. The `SELF` parameter, an instance of the implementation type, can be used to store either the entire state or a handle to the cursor-duration memory that stores the state (if the state information is large).

### Using Operators Outside the WHERE Clause

Operators that are used outside the `WHERE` clause are evaluated using the functional implementation. To execute the statement in Example 9-14, Oracle scans the `MyEmployees` table and invokes the functional implementation for `Contains()` on each instance of `resume`, passing it the actual value of the `resume`, the text data, in the current row. Note that this function would not make use of any domain indexes built on the `resume` column.

Example 9-14 Using Operators Outside the WHERE Clause

```
SELECT Contains(resume, 'Oracle') FROM MyEmployees;
```

Because functional implementations can make use of domain indexes, the following sections discuss how to write functions that use domain indexes and how they are invoked by the system.

#### Creating Index-based Functional Implementations

For many domain-specific operators, such as `Contains()`, the functional implementation has two options:

- If the operator is operating on a column or `OBJECT` attribute that has a domain index, the function can evaluate the operator by looking at the index data rather than the actual argument value.
	For example, when `Contains(resume`, `'Oracle')` is invoked on a particular row of the `MyEmployees` table, it is easier for the function to look up the text domain index defined on the `resume` column and evaluate the operator based on the row identifier for the row containing the `resume` than to work on the `resume` text data argument.
- If the operator is operating on a column that does not have an appropriate domain index defined on it or if the operator is invoked with literal values (non-columns), the functional implementation evaluates the operator based on the argument values. This is the default behavior for all operator bindings.

To make your operator handle both options, provide a functional implementation that has three arguments in addition to the original arguments to the operator:

- Index context: domain index information and the row identifier of the row on which the operator is being evaluated
- Scan context: a context value to share state with subsequent invocations of the same operator operating on other rows of the table
- Scan flag: indicates whether the current call is the last invocation during which all cleanup operations should be performed

The function `TextContains()` in Example 9-15 provides the index-based functional implementation for the `Contains()` operator.

Example 9-15 Implementing the Contains() Operator in Index-Based Functions

```
CREATE FUNCTION TextContains (Text IN VARCHAR2, Key IN VARCHAR2,
indexctx IN ODCIIndexCtx, scanctx IN OUT TextIndexMethods, scanflg IN NUMBER)
RETURN NUMBER AS
BEGIN
.......
END TextContains;
```

The `Contains()` operator is bound to the functional implementation, as demonstrated in Example 9-16.

Example 9-16 Binding the Contains() Operator to the Functional Implementation

```
CREATE OPERATOR Contains
BINDING (VARCHAR2, VARCHAR2) RETURN NUMBER 
WITH INDEX CONTEXT, SCAN CONTEXT TextIndexMethods
USING TextContains;
```

The `WITH INDEX CONTEXT` clause specifies that the functional implementation can make use of any applicable domain indexes. The `SCAN CONTEXT` specifies the data type of the scan context argument, which must be identical to the implementation type of the indextype that supports this operator.

#### Operator Resolution

Oracle invokes the functional implementation for the operator if the operator appears outside the `WHERE` clause. If the functional implementation is index-based, or defined to use an indextype, the additional index information is passed in as arguments, but only if the operator's first argument is a column or object attribute with a domain index of the appropriate indextype.

For example, in the query `SELECT Contains(resume, 'Oracle & Unix') FROM MyEmployees`, Oracle evaluates the operator `Contains()` using the index-based functional implementation, passing it the index information about the domain index on the `resume` column instead of the `resume` data.

#### Operator Execution

To execute the index-based functional implementation, Oracle sets up the arguments in the following manner:

- The initial set of arguments is identical to those specified by the user for the operator.
- If the first argument is not a column, the `ODCIIndexCtx` attributes are set to `NULL`.
- If the first argument is a column, the `ODCIIndexCtx` attributes are set up as follows.
	- If there is an applicable domain index, the `ODCIIndexInfo` attribute contains information about it; otherwise the attribute is set to `NULL`.
		- The `rowid` attribute holds the row identifier of the row being operated on.
- The scan context is set to `NULL` on the first invocation of the operator. Because it is an `IN` / `OUT` parameter, the return value from the first invocation is passed in to the second invocation and so on.
- The scan flag is set to `RegularCall` for all normal invocations of the operator. After the last invocation, the functional implementation is invoked one more time, at which time any cleanup actions can be performed. During this call, the scan flag is set to `CleanupCall` and all other arguments except the scan context are set to `NULL`.

When index information is passed in, the implementation can compute the operator value with a domain index lookup using the row identifier as key. The index metadata is used to identify the index structures associated with the domain index. The scan context is typically used to share state with the subsequent invocations of the same operator.

If there is no indextype that supports the operator, or if there is no domain index on the column passed to the operator as its first argument, then the index context argument is null. However, the scan context argument is still available and can be used as described in this section. Thus, the operator can maintain state between invocations even if no index is used by the query.

### Operators that Return Ancillary Data

In addition to filtering rows, operators in `WHERE` clauses sometimes must return ancillary data. Ancillary data is modeled as one or more operators, each of which has

- A single literal number argument, which ties it to the corresponding primary operator
- A functional implementation with access to state generated by the index scan-based implementation of the primary operator

In the query in Example 9-17, the primary operator, `Contains()`, can be evaluated using an index scan that determines which rows satisfy the predicate, and computes a score value for each row. The functional implementation for the `Score` operator accesses the state generated by the index scan to obtain the score for a given row identified by its row identifier. The literal argument `1` associates the ancillary operator `Score` to the primary operator `Contains()`, which generates the ancillary data.

Example 9-17 Accessing Ancillary Data with the Contains() Operator

```
SELECT Score(1) FROM MyEmployees 
WHERE Contains(resume, 'OCI & UNIX', 1) =1;
```

The functional implementation of an ancillary operator can use either the domain index or the state generated by the primary operator. When invoked, the functional implementation is passed three extra arguments:

- The index context, which contains the domain index information
- The scan context, which provides access to the state generated by the primary operator
- A scan flag to indicate whether the functional implementation is being invoked for the last time

The following sections discuss how operators modeling ancillary data are defined and invoked.

#### Operator Bindings that Compute Ancillary Data

An operator binding that computes ancillary data is called a primary binding. Example 9-18 defines a primary binding for the operator `Contains()`.

Example 9-18 Comparing Ancillary Data with the Contains() Operator

```
CREATE OPERATOR Contains
BINDING (VARCHAR2, VARCHAR2) RETURN NUMBER
WITH INDEX CONTEXT, SCAN CONTEXT TextIndexMethods COMPUTE ANCILLARY DATA
USING TextContains;
```

This definition registers two bindings for `Contains()`:

- `CONTAINS(VARCHAR2`, `VARCHAR2)`, used when ancillary data is not required
- `CONTAINS(VARCHAR2`, `VARCHAR2`, `NUMBER)`, used when ancillary data is required (the `NUMBER` argument associates this binding with the ancillary operator binding)

The two bindings have a single functional implementation, as shown in Example 9-19:

Example 9-19 Implementing Bindings for Computations

```
TextContains(VARCHAR2, VARCHAR2, ODCIIndexCtx, TextIndexMethods, NUMBER).
```

#### Operator Bindings That Model Ancillary Data

An operator binding that models ancillary data is called an ancillary binding. Functional implementations for ancillary data operators are similar to index-based functional implementations. When you have defined the function, you bind it to the operator with an additional `ANCILLARY` `TO` attribute, indicating that the functional implementation must share its state with the primary operator binding.

Note that the functional implementation for the ancillary operator binding must have the same signature as the functional implementation for the primary operator binding.

Example 9-20 demonstrates how to evaluate the ancillary operator inside a `TextScore` () function.

Example 9-20 Evaluating an Ancillary Operator

```
CREATE FUNCTION TextScore (Text IN VARCHAR2, Key IN VARCHAR2,
  indexctx IN ODCIIndexCtx, scanctx IN OUT TextIndexMethods, scanflg IN NUMBER)
RETURN NUMBER AS
BEGIN
.......
END TextScore;
```

Using the `TextScore()` definition, you could create an ancillary binding, as in Example 9-21.

Example 9-21 Creating an Ancillary Operator Binding

```
CREATE OPERATOR Score
BINDING (NUMBER) RETURN NUMBER
ANCILLARY TO Contains(VARCHAR2, VARCHAR2) 
USING TextScore;
```

The `ANCILLARY` `TO` clause specifies that `Score` shares state with the primary operator binding `CONTAINS(VARCHAR2`, `VARCHAR2)`.

The ancillary operator binding is invoked with a single literal number argument, such as `Score` (1), `Score` (2), and so on.

#### Operator Resolution

The operators corresponding to ancillary data are invoked by the user with a single number argument. This number argument must be a literal in both the ancillary operation, and in the primary operator invocation, so that the operator association can be done at query compilation time.

To determine the corresponding primary operator, Oracle matches the number passed to the ancillary operator with the number passed as the last argument to the primary operator. It is an error to find zero or more than one matching primary operator invocation. After the matching primary operator invocation is found,

- The arguments to the primary operator become operands of the ancillary operator.
- The ancillary and primary operator executions are passed the same scan context.

For example, in the Example 9-17 query, the invocation of `Score` is determined to be ancillary to `Contains()` based on the number argument `1`, and the functional implementation for `Score` gets the operands `(resume`, `'Oracle&Unix'`, `indexctx`, `scanctx, scanflg)`, where `scanctx` is shared with the invocation of `Contains()`.

#### Operator Execution

Operator execution uses an index scan to process the `Contains()` operator. For each of the rows returned by the `fetch()` call of the index scan, the functional implementation of `Score` is invoked by passing to it the `ODCIIndexCtx` argument, which contains the index information, row identifier, and a handle to the index scan state. The functional implementation can use the handle to the index scan state to compute the score.