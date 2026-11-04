---
title: Index
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/index.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

A B C D E F G H I J K L M N O P Q R S T U V W Z

---

## Symbols

$$PLSQL\_LINE inquiry directive, [2.10.1.4.1](fundamentals.md)

$$PLSQL\_UNIT inquiry directive, [2.10.1.4.1](fundamentals.md)

% wildcard character, [2.7.5.3](fundamentals.md)

%BULK\_EXCEPTIONS cursor attribute, [12.4.1.4](tuning.md)

%BULK\_ROWCOUNT cursor attribute, [12.4.1.5](tuning.md)

%FOUND cursor attribute

%ISOPEN cursor attribute

%NOTFOUND cursor attribute

for implicit cursor, [6.2.1.3](static.md)

for named cursor, [6.2.2.7.3](static.md)

%ROWCOUNT cursor attribute

for implicit cursor, [6.2.1.4](static.md)

for named cursor, [6.2.2.7.4](static.md)

%ROWTYPE attribute, [5.11.4](composites.md)

column alias and, [6.2.2.5](static.md)

explicit cursor and, [6.2.2.5](static.md)

syntax diagram, [13](rowtype_attribute.md)

virtual columns and, [5.11.4.3](composites.md)

%TYPE attribute, [2.3.5](fundamentals.md)

initial value and, [2.3.5](fundamentals.md)

NOT NULL constraint and, [2.3.5](fundamentals.md)

syntax diagram, [13](type_attribute.md)

\_ wildcard character, [2.7.5.3](fundamentals.md)

---

## A

Abstract Data Type (ADT), [1.2.8.5](overview.md)

creating, [14](create_type.md)

editioned, [14](alter_type.md)

for use in any schema, [8.13.7](subprograms.md)

accent-insensitive comparison, [2.7.5.2.3](fundamentals.md)

ACCESS\_INTO\_NULL exception, [11.4](errors.md)

ADT

See Abstract Data Type (ADT)

aggregate function, [14](create_function.md)

in PL/SQL expression, [2.7.8](fundamentals.md)

pipelined table function as, [12.5.6](tuning.md)

SQL%NOTFOUND attribute and, [6.2.1.3](static.md)

alias

column

in cursor FOR LOOP, [6.3.2](static.md)

in explicit cursor, [6.2.2.5](static.md)

table

for avoiding inner capture, [B.6](nameresolution.md)

for row expression, [B.6.2](nameresolution.md)

for table element attribute or method, [B.6.1](nameresolution.md)

aliasing (problem)

SELECT BULK COLLECT INTO statement and, [12.4.2.1.1](tuning.md)

subprogram parameter, [8.6.4](subprograms.md)

ALTER FUNCTION statement, [14](alter_function.md)

ALTER LIBRARY statement, [14](alter_library.md)

ALTER PACKAGE statement, [14](alter_package.md)

ALTER PROCEDURE statement, [14](alter_procedure.md)

ALTER TRIGGER statement, [14](alter_trigger.md)

ALTER TYPE statement, [14](alter_type.md)

AND operator, [2.7.3](fundamentals.md)

anonymous block, [1.2.2](overview.md)

AUTHID property and, [8.13](subprograms.md)

ANYDATA data type, [12.5.2](tuning.md)

ANYDATASET data type, [12.5.2](tuning.md)

ANYTYPE data type, [12.5.2](tuning.md)

architecture of PL/SQL, [1.3](overview.md)

array

associative

See associative array

non-PL/SQL, [5.1](composites.md)

assignment of value

to composite variable

collection, [5.6](composites.md)

record, [5.12](composites.md)

to scalar variable, [2.6](fundamentals.md)

assignment statement, [2.6.1](fundamentals.md)

syntax diagram, [13](assignment_statement.md)

associative array, [5.2](composites.md)

characteristics of, [5.1](composites.md)

comparisons, [5.8](composites.md)

declaring constant, [5.2.1](composites.md)

FIRST and LAST methods for, [5.9.5.1](composites.md)

in FORALL statement, [13](forall_statement.md)

NLS parameters and, [5.2.2](composites.md)

pipelined table function and, [12.5.2](tuning.md)

See also collection

atomic (lexical) unit, [2.2](fundamentals.md)

atomically null collection

See null collection

attribute

%ROWTYPE

See %ROWTYPE attribute

%TYPE

See %TYPE attribute

cursor

See cursor attribute

AUTHID property, [8.13](subprograms.md)

autonomous transaction, [6.7](static.md)

pipelined table function in, [13](pipe_row_statement.md)

autonomous trigger, [6.7.6](static.md)

AUTONOMOUS\_TRANSACTION pragma, [13](autotransaction_pragma.md)

for pipelined table function, [12.5.2](tuning.md)

---

## B

bag data structure, [5.1](composites.md)

base type, [3](datatypes.md)

basic LOOP statement, [4.2.1](controlstatements.md)

syntax diagram, [13](basic_loop_statement.md)

BETWEEN operator, [2.7.5.4](fundamentals.md)

BINARY\_DOUBLE data type

predefined constants for, [3.1.2](datatypes.md)

subtype of, [3.1.3](datatypes.md)

tuning code and, [12.3.5.1](tuning.md)

BINARY\_FLOAT data type

predefined constants for, [3.1.2](datatypes.md)

subtype of, [3.1.3](datatypes.md)

tuning code and, [12.3.5.1](tuning.md)

BINARY\_INTEGER data type

See PLS\_INTEGER data type

bind variable

avoiding SQL injection with, [7.4.2.1](dynamic.md)

placeholder for

See placeholder for bind variable

blank-padding

in assignment, [3.1.4.3.2](datatypes.md)

in comparison, [3.1.4.3.3](datatypes.md)

block, [1.2.2](overview.md)

syntax diagram, [13](block.md)

BOOLEAN data type, [3.2](datatypes.md)

BOOLEAN expression, [2.7.6](fundamentals.md)

BOOLEAN static expression, [2.10.1.5.2](fundamentals.md)

BOOLEAN variable, [2.6.4](fundamentals.md)

built-in function

See SQL function

bulk binding, [12.4](tuning.md)

BULK COLLECT clause, [12.4.2](tuning.md)

aliasing and, [12.4.2.1.1](tuning.md)

of FETCH statement, [12.4.2.2](tuning.md)

of RETURNING INTO clause, [12.4.2.3](tuning.md)

FORALL statement and, [12.4.3](tuning.md)

of SELECT INTO statement, [12.4.2.1](tuning.md)

query result set processing and, [6.3.1.2](static.md)

that returns no rows, [12.4.2](tuning.md)

bulk SQL, [12.4](tuning.md)

in compound DML trigger, [9.3.5.3](triggers.md)

---

## C

C procedure, invoking, [8.14](subprograms.md)

cache, function result, [8.11](subprograms.md)

calculated column

See virtual column

call specification, [8.14](subprograms.md)

in CREATE FUNCTION statement, [14](create_function.md)

in CREATE PROCEDURE statement, [14](create_procedure.md)

in package, [10.1](packages.md)

call stack, AUTHID property and, [8.13](subprograms.md)

capture, [B.5](nameresolution.md)

cascading triggers, [9.10](triggers.md)

CASE expression

searched, [2.7.7.2](fundamentals.md)

simple, [2.7.7.1](fundamentals.md)

case sensitivity

character comparison and, [2.7.5.2.3](fundamentals.md)

character literal and, [2.2.3](fundamentals.md)

identifier and, [2.2.2](fundamentals.md)

quoted user-defined identifier, [2.2.2.3.2](fundamentals.md)

keyword and, [D](reservewords.md)

LIKE operator and, [2.7.5.3](fundamentals.md)

reserved word and, [D](reservewords.md)

CASE statement, [4.1](controlstatements.md)

searched, [4.1.5](controlstatements.md)

syntax diagram, [13](case_statement.md)

simple, [4.1.4](controlstatements.md)

IF THEN ELSIF statement and, [4.1.3](controlstatements.md)

syntax diagram, [13](case_statement.md)

CASE\_NOT\_FOUND exception, [11.4](errors.md)

case-insensitive comparison, [2.7.5.2.3](fundamentals.md)

CHAR data type, [3.1.4](datatypes.md)

CHAR data type family, [E](predefined.md)

character code, [2.1](fundamentals.md)

character literal, [2.2.3](fundamentals.md)

See also string

character set, [2.1](fundamentals.md)

CLOB data type and comparison operator, [2.7.5](fundamentals.md)

CLOB data type family, [E](predefined.md)

CLOSE statement, [13](close_statement.md)

collating sequence, [2.7.5.2.3](fundamentals.md)

collection, [5](composites.md)

as public package item, [5.10](composites.md)

assigning one to another, [5.6](composites.md)

comparing one to another, [5.8](composites.md)

cursor variable and, [13](cursor_variable.md)

declaration syntax, [13](collection.md)

empty, [5.1](composites.md)

creating with constructor, [5.5](composites.md)

index

See index collection

internal size of

DELETE method and, [5.9.1](composites.md)

EXTEND method and, [5.9.3](composites.md)

TRIM method and, [5.9.2](composites.md)

multidimensional, [5.7](composites.md)

null, [5.1](composites.md)

assigning to collection variable, [5.6.2](composites.md)

pipelined table function and, [12.5.1](tuning.md)

retrieving query results into, [12.4.2](tuning.md)

types of, [5.1](composites.md)

collection constructor, [5.5](composites.md)

collection method, [5.9](composites.md)

as subprogram parameter, [5.9](composites.md)

invocation syntax, [13](collection_method.md)

null collection and, [5.9](composites.md)

COLLECTION\_IS\_NULL exception, [11.4](errors.md)

column alias

in cursor FOR LOOP, [6.3.2](static.md)

in explicit cursor, [6.2.2.5](static.md)

comment, [2.2.4](fundamentals.md)

nested, [2.2.4.2](fundamentals.md)

PL/SQL Wrapper utility and, [A.3](wrap.md)

syntax diagram, [13](comment.md)

COMMIT statement, [6.6.1](static.md)

FOR UPDATE cursor and, [6.6.6.3](static.md)

in autonomous transaction, [6.7.5.2](static.md)

comparison

of collections, [5.8](composites.md)

of records, [5.13](composites.md)

comparison operator, [2.7.5](fundamentals.md)

cursor variable and, [13](cursor_variable.md)

compatible data type

for collection variables, [5.6.1](composites.md)

for scalar variables, [2.6](fundamentals.md)

compilation

conditional, [2.10](fundamentals.md)

for native execution, [12.9](tuning.md)

interpreted, [12.9.5](tuning.md)

compilation parameter, [1.3.2](overview.md)

displaying value of, [2.10.1.4.1](fundamentals.md)

predefined inquiry directive for, [2.10.1.4.1](fundamentals.md)

compiler directive

See pragma

compile-time warning, [11.1](errors.md)

composite data type, [5](composites.md)

composite variable, [5](composites.md)

compound DML trigger, [9.3.5](triggers.md)

computation-intensive code, [12.3.5](tuning.md)

concatenation operator (||), [2.7.1](fundamentals.md)

concurrent transactions, [6.7.5.4](static.md)

condition, SQL multiset, [5.8.3](composites.md)

conditional compilation, [2.10](fundamentals.md)

conditional compilation directive, [2.10.1](fundamentals.md)

error, [2.10.1.3](fundamentals.md)

inquiry, [2.10.1.4](fundamentals.md)

restrictions on, [2.10.4](fundamentals.md)

selection, [2.10.1.2](fundamentals.md)

conditional predicate, [9.3.1](triggers.md)

conditional selection statement, [4.1](controlstatements.md)

conditional trigger, [9.1](triggers.md)

constant

declaring, [2.3.2](fundamentals.md)

associative array, [5.2.1](composites.md)

record, [5.11.2](composites.md)

syntax diagram, [13](constant.md)

initial value of, [2.3.3](fundamentals.md)

predefined, [3.1.2](datatypes.md)

static, [2.10.1.5.4](fundamentals.md)

in DBMS\_DB\_VERSION package, [2.10.1.5.5](fundamentals.md)

constrained subtype, [3.4.2](datatypes.md)

in performance-critical code, [12.3.5.2](tuning.md)

subprogram parameter and, [8.6.1](subprograms.md)

constraint

cursor parameter and, [13](explicit_cursor.md)

NOT NULL

See NOT NULL constraint

trigger compared to, [9.2](triggers.md)

constructor

See collection constructor

context of transaction, [6.7.2](static.md)

CONTINUE statement, [4.2.4](controlstatements.md)

syntax diagram, [13](continue_statement.md)

CONTINUE WHEN statement, [4.2.5](controlstatements.md)

syntax diagram, [13](continue_statement.md)

control statement, [4](controlstatements.md)

control token, [2.10.1.1](fundamentals.md)

correlated subquery, [6.3.4](static.md)

correlation name, [9.3.2](triggers.md)

with LONG or LONG RAW column, [9.9.2](triggers.md)

COUNT collection method, [5.9.6](composites.md)

CREATE FUNCTION statement, [14](create_function.md)

CREATE LIBRARY statement, [14](create_library.md)

CREATE PACKAGE statement, [14](create_package.md)

CREATE TRIGGER statement, [14](create_trigger.md)

CREATE TYPE BODY statement, [14](create_type_body.md)

CREATE TYPE statement, [14](create_type.md)

CREATE\_WRAPPED procedure, [A.4](wrap.md)

crossedition trigger, [9.3](triggers.md)

CURRENT OF clause, [6.6.6.2](static.md)

FOR UPDATE cursor and, [6.6.6.2](static.md)

ROWID pseudocolumn instead of, [6.6.6.3](static.md)

CURRENT\_USER, [8.13.1](subprograms.md)

CURRVAL pseudocolumn, [6.1.2.1](static.md)

cursor, [6.2](static.md)

explicit

See explicit cursor

FOR UPDATE, [6.6.6.2](static.md)

after COMMIT or ROLLBACK, [6.6.6.3](static.md)

implicit

See implicit cursor

in SERIALLY\_REUSABLE package, [10.7.2](packages.md)

named, [6.2.2](static.md)

pipelined table function and, [12.5.5](tuning.md)

See also explicit cursor and cursor variable

nested, [6.5](static.md)

cursor attribute

for cursor variable, [6.4.6](static.md)

for explicit cursor, [6.2.2.7](static.md)

%FOUND, [6.2.2.7.2](static.md)

%ISOPEN, [6.2.2.7.1](static.md)

%NOTFOUND, [6.2.2.7.3](static.md)

%ROWCOUNT, [6.2.2.7.4](static.md)

for implicit cursor, [6.2.1](static.md)

DBMS\_SQL package and, [7.3](dynamic.md)

native dynamic SQL and, [7.2](dynamic.md)

SQL%BULK\_EXCEPTIONS, [12.4.1.4](tuning.md)

SQL%BULK\_ROWCOUNT, [12.4.1.5](tuning.md)

SQL%FOUND, [6.2.1.2](static.md)

SQL%ISOPEN, [6.2.1.1](static.md)

SQL%NOTFOUND, [6.2.1.3](static.md)

SQL%ROWCOUNT, [6.2.1.4](static.md)

where you can use, [6.2](static.md)

CURSOR expression, [6.5](static.md)

passing to pipelined table function, [12.5.6](tuning.md)

cursor FOR LOOP statement

query result set processing with, [6.3.2](static.md)

recursive invocation in, [8.9](subprograms.md)

syntax diagram, [13](cursor_for_loop_statement.md)

cursor parameter, [6.2.2.6](static.md)

cursor specification, [13](explicit_cursor.md)

cursor variable, [6.4](static.md)

declaration syntax diagram, [13](cursor_variable.md)

CURSOR\_ALREADY\_OPEN exception, [11.4](errors.md)

---

## D

data abstraction, [1.2.8](overview.md)

data definition language statement

See DDL statement

Data Pump Import and triggers, [9.13](triggers.md)

data type

collection

See collection

compatible

for collection variables, [5.6.1](composites.md)

for scalar variables, [2.6](fundamentals.md)

composite, [5](composites.md)

object

See Abstract Data Type (ADT)

of expression, [2.7](fundamentals.md)

predefined, [E](predefined.md)

RECORD

See record

scalar, [3](datatypes.md)

SQL, [3.1](datatypes.md)

user-defined

See Abstract Data Type (ADT)

what it determines, [3](datatypes.md)

See also subtype

data type conversion, [3.1](datatypes.md)

implicit

See implicit data type conversion

SQL injection and, [7.4.1.3](dynamic.md)

data type family, [3](datatypes.md)

overloaded subprogram and, [8.8](subprograms.md)

predefined data types grouped by, [E](predefined.md)

subtypes with base types in same, [3.4.3](datatypes.md)

database character set, [2.1.1](fundamentals.md)

database link, IR, [8.13.6](subprograms.md)

DATABASE trigger, [9.4.2](triggers.md)

DATE data type family, [E](predefined.md)

DBMS\_ASSERT package, [7.4.2.2](dynamic.md)

DBMS\_DB\_VERSION package, [2.10.1.5.5](fundamentals.md)

DBMS\_DDL package, [A.4](wrap.md)

DBMS\_PARALLEL\_EXECUTE package, [12.6](tuning.md)

DBMS\_PREPROCESSOR package, [2.10.3](fundamentals.md)

DBMS\_PROFILE package, [12.8.1](tuning.md)

DBMS\_SQL package, [7.3](dynamic.md)

switching to native dynamic SQL from, [7.3](dynamic.md)

DBMS\_SQL.TO\_CURSOR\_NUMBER function, [7.3.2](dynamic.md)

DBMS\_SQL.TO\_REFCURSOR function, [7.3.1](dynamic.md)

DBMS\_STANDARD package, [2.4](fundamentals.md)

DBMS\_TRACE package, [12.8.2](tuning.md)

DBMS\_WARNING package, [11.1.1](errors.md)

dbmsupgin.sql script, [12.9.5](tuning.md)

dbmsupgnv.sql script, [12.9.5](tuning.md)

DDL statement

dynamic SQL for, [7](dynamic.md)

in trigger, [6.7.6](static.md)

subprogram side effects and, [8.12](subprograms.md)

deadlock

autonomous transaction and, [6.7.5.4](static.md)

implicit rollback and, [6.6.4](static.md)

declaration, [2.3](fundamentals.md)

exception raised in, [11.8.1](errors.md)

default value

of cursor parameter, [6.2.2.6.1](static.md)

of subprogram parameter, [8.6.5](subprograms.md)

See also initial value

DEFINE

binding category, [12.4](tuning.md)

PL/SQL Wrapper utility and, [A.3](wrap.md)

DEFINER, [8.13.1](subprograms.md)

definer’s rights unit

See DR unit

DELETE collection method, [5.9.1](composites.md)

COUNT method and, [5.9.6](composites.md)

EXISTS method and, [5.9.4](composites.md)

EXTEND method and, [5.9.3](composites.md)

FIRST method and, [5.9.5](composites.md)

LAST method and, [5.9.5](composites.md)

NEXT method and, [5.9.8](composites.md)

PRIOR method and, [5.9.8](composites.md)

TRIM method and, [5.9.2](composites.md)

DELETE statement

BEFORE statement trigger and, [9.8](triggers.md)

PL/SQL extension to, [13](delete_statement.md)

See also DML statement

DELETING conditional predicate, [9.3.1](triggers.md)

delimiter, [2.2.1](fundamentals.md)

dense collection, [5.1](composites.md)

Descriptive Intermediate Attributed Notation for Ada (DIANA), [C](limits.md)

DETERMINISTIC option, [13](function.md)

for pipelined table function, [12.5.2](tuning.md)

directive

compiler

See pragma

error, [2.10.1.3](fundamentals.md)

inquiry, [2.10.1.4](fundamentals.md)

selection, [2.10.1.2](fundamentals.md)

See also conditional compilation directive

DML statement

in FORALL statement, [12.4.1](tuning.md)

inside pipelined table function, [12.5.2](tuning.md)

on pipelined table function result, [12.5.7](tuning.md)

PL/SQL syntax of, [6.1.1](static.md)

repeating efficiently, [12.4.1](tuning.md)

DML statement statement

avoiding inner capture in, [B.6](nameresolution.md)

DML trigger, [9.3](triggers.md)

dot notation

for collection method, [5.9](composites.md)

for identifier in named PL/SQL unit, [2.4](fundamentals.md)

for pseudocolumn, [6.1.2.1](static.md)

for record field, [5](composites.md)

name resolution and, [B.1](nameresolution.md)

double quotation mark ("), [2.1.1](fundamentals.md)

DR unit

call stack and, [8.13](subprograms.md)

dynamic SQL and, [8.13](subprograms.md)

name resolution and, [8.13](subprograms.md)

privilege checking and, [8.13](subprograms.md)

SCHEMA trigger and, [9.4.1](triggers.md)

SET ROLE command and, [8.13.2](subprograms.md)

static SQL and, [8.13](subprograms.md)

See also AUTHID property

DROP FUNCTION statement, [14](drop_function.md)

DROP LIBRARY statement, [14](drop_library.md)

DROP PACKAGE statement, [14](drop_package.md)

DROP PROCEDURE statement, [14](drop_procedure.md)

DROP TRIGGER statement, [14](drop_trigger.md)

DROP TYPE BODY statement, [14](drop_type_body.md)

DUP\_VAL\_ON\_INDEX exception, [11.4](errors.md)

dynamic SQL, [7](dynamic.md)

AUTHID property and, [8.13](subprograms.md)

native, [7.2](dynamic.md)

switching to DBMS\_SQL package from, [7.3](dynamic.md)

placeholder for bind variable in

EXECUTE IMMEDIATE statement and, [7.2.1](dynamic.md)

repeated, [7.2.3](dynamic.md)

tuning, [12.2](tuning.md)

---

## E

editioned Abstract Data Type (ADT), [14](alter_type.md)

element of collection, [5](composites.md)

embedded SQL

See static SQL

empty collection, [5.1](composites.md)

creating with constructor, [5.5](composites.md)

error directive, [2.10.1.3](fundamentals.md)

error handling, [11](errors.md)

error-reporting function

SQLCODE, [13](sqlcode_function.md)

SQLERRM, [13](sqlerrm_function.md)

SQL%BULK\_EXCEPTIONS and, [12.4.1.4](tuning.md)

escape character, [2.7.5.3](fundamentals.md)

escaped identifier, [B.4](nameresolution.md)

evaluation order, [2.7.2](fundamentals.md)

events publication, [9.14](triggers.md)

evolution of type, [14](alter_type.md)

exception

handling, [11.2](errors.md)

in FORALL statement, [12.4.1.2](tuning.md)

in trigger, [9.7](triggers.md)

See also exception handler

internally defined

See internally defined exception

predefined

See predefined exception

raised in cursor FOR LOOP statement, [6.3.2](static.md)

raised in declaration, [11.8.1](errors.md)

raised in exception handler, [11.8.2](errors.md)

raising explicitly, [11.7](errors.md)

reraising, [11.7.1.3](errors.md)

unhandled, [11.9](errors.md)

in FORALL statement, [12.4.1.2](tuning.md)

user-defined

See user-defined exception

exception handler, [11.2](errors.md)

continuing execution after, [11.11](errors.md)

exception raised in, [11.8.2](errors.md)

for NO\_DATA\_NEEDED, [12.5.8](tuning.md)

GOTO statement and, [13](goto_statement.md)

locator variables for, [11.2.2](errors.md)

retrieving error code and message in, [11.10](errors.md)

retrying transaction after, [11.12](errors.md)

syntax diagram, [13](exception_handler.md)

EXCEPTION\_INIT pragma, [13](exceptioninit_pragma.md)

for giving error code to user-defined exception, [11.7.2](errors.md)

for giving name to internally defined exception, [11.3](errors.md)

EXECUTE IMMEDIATE statement, [7.2.1](dynamic.md)

syntax diagram, [13](executeimmediate_statement.md)

EXISTS collection method, [5.9.4](composites.md)

EXIT statement, [4.2.2](controlstatements.md)

syntax diagram, [13](exit_statement.md)

EXIT WHEN statement, [4.2.3](controlstatements.md)

in basic LOOP statement, [4.2.3](controlstatements.md)

syntax diagram, [13](exit_statement.md)

exiting a loop, [4.2](controlstatements.md)

explicit cursor, [6.2.2](static.md)

declaration syntax diagram, [13](explicit_cursor.md)

in package

declaring, [10.8](packages.md)

opening and closing, [10.7.3](packages.md)

query result processing with

in FOR LOOP statement, [6.3.2](static.md)

with OPEN, FETCH, and CLOSE statements, [6.3.3](static.md)

explicit format model, [7.4.2.3](dynamic.md)

expression, [2.7](fundamentals.md)

CURSOR, [6.5](static.md)

passing to pipelined table function, [12.5.6](tuning.md)

data type of, [2.7](fundamentals.md)

in explicit cursor, [6.2.2.5](static.md)

SQL function in PL/SQL, [2.7.8](fundamentals.md)

static, [2.10.1.5](fundamentals.md), [2.10.1.5](fundamentals.md)

syntax diagram, [13](expression.md)

EXTEND collection method, [5.9.3](composites.md)

external subprogram, [8.14](subprograms.md)

---

## F

FETCH statement

across COMMIT, [6.6.6.3](static.md)

record variable and, [5.12.2.2](composites.md)

syntax diagram, [13](fetch_statement.md)

that returns no row, [6.2.2.3](static.md)

with BULK COLLECT clause, [12.4.2.2](tuning.md)

with cursor variable, [6.4.3](static.md)

with explicit cursor, [6.2.2.3](static.md)

field of record, [5](composites.md)

FIRST collection method, [5.9.5](composites.md)

FOR LOOP statement, [4.2.6](controlstatements.md)

bounds of, [4.2.6.2](controlstatements.md)

FORALL statement and, [12.4.1](tuning.md)

STEP clause and, [4.2.6](controlstatements.md)

syntax diagram, [13](for_loop_statement.md)

See also cursor FOR LOOP statement

FOR UPDATE cursor, [6.6.6.2](static.md)

after COMMIT or ROLLBACK, [6.6.6.3](static.md)

FORALL statement, [12.4.1](tuning.md), [12.4.1](tuning.md)

associative array in, [13](forall_statement.md)

bulk binding and, [12.4](tuning.md)

BULK COLLECT clause and, [12.4.3](tuning.md)

for sparse collection, [12.4.1.1](tuning.md)

SQL%BULK\_EXCEPTIONS and, [12.4.1.4.1](tuning.md)

handling exception raised in

after FORALL completes, [12.4.1.4](tuning.md)

immediately, [12.4.1.3](tuning.md)

number of rows affected by, [12.4.1.5](tuning.md)

syntax diagram, [13](forall_statement.md)

unhandled exception in, [12.4.1.2](tuning.md)

format model, [7.4.2.3](dynamic.md)

forward declaration of subprogram, [8.5](subprograms.md)

function

aggregate

See aggregate function

built-in

See SQL function

declaration syntax diagram, [13](function.md)

error-reporting

SQLCODE, [13](sqlcode_function.md)

SQLERRM, [12.4.1.4](tuning.md)

invoking, [8.3](subprograms.md)

in SQL statement, [8.12](subprograms.md)

options for, [8.4.1](subprograms.md)

SQL

See SQL function

structure of, [8.4.1](subprograms.md)

table

See table function

See also subprogram

function result cache, [8.11](subprograms.md)

function specification, [13](function.md)

---

## G

generated column

See virtual column

global identifier, [2.5](fundamentals.md)

GOTO statement, [4.3.1](controlstatements.md)

restrictions on, [13](goto_statement.md)

syntax diagram, [13](goto_statement.md)

---

## H

hardware arithmetic, [12.3.5.1](tuning.md)

hash table, [5.1](composites.md)

hiding PL/SQL source text

See wrapping PL/SQL source text

host variable

bulk-binding, [12.4.4](tuning.md)

cursor variable as, [6.4.8](static.md)

packages and, [10.2](packages.md)

---

## I

identifier, [2.2.2](fundamentals.md)

ambiguous reference to, [B](nameresolution.md)

escaped, [B.4](nameresolution.md)

global, [2.5](fundamentals.md)

in static SQL, [6.1.1](static.md)

local, [2.5](fundamentals.md)

reference to, [2.4](fundamentals.md)

scope of, [2.5](fundamentals.md)

user-defined, [2.2.2.3](fundamentals.md)

collecting data about, [12.7](tuning.md)

visibility of, [2.5](fundamentals.md)

See also name

IDL, [C](limits.md)

IF statement, [4.1](controlstatements.md)

IF THEN form, [4.1.1](controlstatements.md)

IF THEN ELSE form, [4.1.2](controlstatements.md)

IF THEN ELSIF form, [4.1.3](controlstatements.md)

nested IF THEN ELSE statement and, [4.1.3](controlstatements.md)

simple CASE statement and, [4.1.3](controlstatements.md)

nested, [4.1.2](controlstatements.md)

syntax diagram, [13](if_statement.md)

imp and triggers, [9.13](triggers.md)

implicit cursor, [6.2.1](static.md)

CURSOR expression with, [6.5](static.md)

declaration syntax, [13](sql_cursor.md)

dynamic SQL and, [7.3](dynamic.md)

query result processing with

with cursor FOR LOOP statement, [6.3.2](static.md)

with SELECT INTO statement, [6.3.1](static.md)

implicit data type conversion

minimizing, [12.3.5.3](tuning.md)

of subprogram parameter, [8.6.2](subprograms.md)

causing overload error, [8.8.3](subprograms.md)

of subtypes

constrained, [3.4.2](datatypes.md)

unconstrained, [3.4.1](datatypes.md)

with base types in same family, [3.4.3](datatypes.md)

implicit ROLLBACK statement, [6.6.4](static.md)

Import and triggers, [9.13](triggers.md)

IN operator, [2.7.5.5](fundamentals.md)

IN OUT parameter mode, [8.6.3](subprograms.md)

IN parameter mode, [8.6.3](subprograms.md)

in-bind, [12.4](tuning.md)

independent transaction

See autonomous transaction

index collection, [12.4.1.1](tuning.md)

representing subset with, [12.4.1.1](tuning.md)

index of collection, [5](composites.md)

index-by table

See associative array

infinite loop, [4.2.1](controlstatements.md)

INFORMATIONAL compile-time warning, [11.1](errors.md)

initial value

%TYPE attribute and, [2.3.5](fundamentals.md)

NOT NULL constraint and, [2.3.4](fundamentals.md)

of constant, [2.3.3](fundamentals.md)

of variable

nested table, [5.4](composites.md)

record, [5.11.1](composites.md)

scalar, [2.3.3](fundamentals.md)

varray, [5.3](composites.md)

See also default value

initialization parameter, [1.3.2](overview.md)

INLINE pragma, [12.1.1](tuning.md)

syntax diagram, [13](inline_pragma.md)

inner capture, [B.5.3](nameresolution.md)

avoiding, [B.6](nameresolution.md)

input, [1.2.7](overview.md)

inquiry directive, [2.10.1.4](fundamentals.md)

INSERT statement

inserting record with, [5.14](composites.md)

restrictions on, [5.16](composites.md)

PL/SQL extension to, [13](insert_statement.md)

See also DML statement

INSERTING conditional predicate, [9.3.1](triggers.md)

instance method, IR, [8.13.8](subprograms.md)

INSTEAD OF trigger, [9.1](triggers.md)

for CREATE statement, [9.4.3](triggers.md)

on DML statement, [9.3.4](triggers.md)

compound, [9.3.5.1](triggers.md)

for pipelined table function result, [12.5.7](tuning.md)

on nested table column, [9.3.4](triggers.md)

Interface Definition Language (IDL), [C](limits.md)

internally defined exception, [11.3](errors.md)

giving name to, [11.3](errors.md)

raising explicitly, [11.7.1.2](errors.md)

interpreted compilation, [12.9.5](tuning.md)

INVALID\_CURSOR exception, [11.4](errors.md)

INVALID\_NUMBER exception, [11.4](errors.md)

invoker’s rights unit

See IR unit

IR unit

Abstract Data Type (ADT), [8.13.7](subprograms.md)

call stack and, [8.13](subprograms.md)

database link, [8.13.6](subprograms.md)

dynamic SQL and, [8.13](subprograms.md)

instance method, [8.13.8](subprograms.md)

invoked by trigger, [8.13.5](subprograms.md)

invoked by view, [8.13.5](subprograms.md)

name resolution and, [8.13](subprograms.md)

overriding name resolution in, [8.13.4](subprograms.md)

privilege checking and, [8.13](subprograms.md)

static SQL and, [8.13](subprograms.md)

template objects in, [8.13.3](subprograms.md)

See also AUTHID property

IS \[NOT\] NULL operator, [2.7.5.1](fundamentals.md)

collections and, [5.8.1](composites.md)

isolation level of transaction, [6.7.3](static.md)

---

## J

Java class method invocation, [8.14](subprograms.md)

---

## K

key-value pair

See associative array

keywords, [2.2.2.1](fundamentals.md)

list of, [D](reservewords.md)

---

## L

labeled LOOP statement, [4.2.3](controlstatements.md)

LAST collection method, [5.9.5](composites.md)

LEVEL pseudocolumn, [6.1.2](static.md)

lexical unit, [2.2](fundamentals.md)

library

creating, [14](create_library.md)

dropping, [14](drop_library.md)

explicitly recompiling, [14](alter_library.md)

library arithmetic, [12.3.5.1](tuning.md)

LIKE operator, [2.7.5.3](fundamentals.md)

LIMIT clause, [12.4.2.2.1](tuning.md)

LIMIT collection method, [5.9.7](composites.md)

line-continuation character, [2.2.3](fundamentals.md)

literal, [2.2.3](fundamentals.md)

local identifier, [2.5](fundamentals.md)

locator variable, [11.2.2](errors.md)

lock mode, [6.6.6.1](static.md)

LOCK TABLE statement, [6.6.6.1](static.md)

locking

overriding default, [6.6.6](static.md)

result set row, [6.6.6.2](static.md)

table, [6.6.6.1](static.md)

logical operator, [2.7.3](fundamentals.md)

logical value, [3.2](datatypes.md)

LOGIN\_DENIED exception, [11.4](errors.md)

LONG data type, [3.1.5](datatypes.md)

in trigger, [9.9.2](triggers.md)

LONG RAW data type, [3.1.5](datatypes.md)

in trigger, [9.9.2](triggers.md)

LOOP statement

exiting, [4.2](controlstatements.md)

kinds of, [4.2](controlstatements.md)

labeled, [4.2](controlstatements.md), [4.2.3](controlstatements.md)

nested, [4.2.3](controlstatements.md)

optimizing, [12.3.4](tuning.md)

LOOP UNTIL structure, [4.2.7](controlstatements.md)

---

## M

MALFORMED\_WRAP\_INPUT exception, [A.4](wrap.md)

manageability, [1.1.6](overview.md)

materialized view, trigger and, [14](create_trigger.md)

membership test, [2.7.5.5](fundamentals.md)

Method 4, [7.3](dynamic.md)

method, collection

See collection method

mixed parameter notation, [8.6.6](subprograms.md)

mode

lock, [6.6.6.1](static.md)

subprogram parameter, [8.6.3](subprograms.md)

multibyte character set

as database character set, [2.1.1](fundamentals.md)

variables for values from, [3.1.4.2](datatypes.md)

multidimensional collection, [5.7](composites.md)

multiline comment, [2.2.4.2](fundamentals.md)

multiple data transformations, [12.5](tuning.md)

multiset condition, [5.8.3](composites.md)

mutating table, [9.9.3](triggers.md)

mutating-table error

for function, [8.12](subprograms.md)

for trigger, [9.9.3](triggers.md)

---

## N

name

qualified

See dot notation

qualified remote, [2.4](fundamentals.md)

remote, [2.4](fundamentals.md)

simple, [2.4](fundamentals.md)

See also identifier

name resolution, [B](nameresolution.md)

AUTHID property and, [8.13](subprograms.md)

in static SQL, [B.4](nameresolution.md)

overriding in IR unit, [8.13.4](subprograms.md)

PL/SQL and SQL differences, [B.3](nameresolution.md)

named cursor, [6.2.2](static.md)

pipelined table function and, [12.5.5](tuning.md)

See also explicit cursor and cursor variable

named parameter notation, [8.6.6](subprograms.md)

national character set, [2.1.2](fundamentals.md)

native dynamic SQL, [7.2](dynamic.md)

switching to DBMS\_SQL package from, [7.3](dynamic.md)

native execution, compilation for, [12.9](tuning.md)

NATURAL subtype, [3.3.2](datatypes.md)

NATURALN subtype, [3.3.2](datatypes.md)

nested comment, [2.2.4.2](fundamentals.md)

nested cursor, [6.5](static.md)

nested IF statement, [4.1.2](controlstatements.md)

IF THEN ELSIF form and, [4.1.3](controlstatements.md)

nested LOOP statement, [4.2.3](controlstatements.md)

nested record

assignment example, [5.12.1](composites.md)

declaration example, [5.11.3](composites.md)

nested subprogram, [8.2](subprograms.md)

declaration and definition of, [8.2](subprograms.md)

forward declaration for, [8.5](subprograms.md)

nested table, [5.4](composites.md)

assigning null value to, [5.6.2](composites.md)

assigning set operation result to, [5.6.3](composites.md)

characteristics of, [5.1](composites.md)

column in view, trigger on, [9.3.4](triggers.md)

comparing to NULL, [5.8.1](composites.md)

comparing two, [5.8.2](composites.md)

correlation names and, [9.3.2](triggers.md)

COUNT method for, [5.9.6.2](composites.md)

FIRST and LAST methods for, [5.9.5.3](composites.md)

returned by function, [12.5.1](tuning.md)

SQL multiset conditions and, [5.8.3](composites.md)

See also collection

nested transaction, [6.7](static.md)

NEW correlation name, [9.3.2](triggers.md)

with LONG or LONG RAW column, [9.9.2](triggers.md)

new features, [Preface](whatsnew.md)

NEXT collection method, [5.9.8](composites.md)

NEXTVAL pseudocolumn, [6.1.2.1](static.md)

NLS parameters

associative array and, [5.2.2](composites.md)

character comparison and, [2.7.5.2.3](fundamentals.md)

SQL injection and, [7.4.1.3](dynamic.md)

NO\_DATA\_FOUND exception, [11.4](errors.md)

NO\_DATA\_NEEDED exception, [12.5.8](tuning.md)

SQLCODE for, [11.4](errors.md)

NOCOPY hint, [13](parameter_declaration.md)

subprogram parameter aliasing and, [8.6.4.1](subprograms.md)

tuning subprogram invocation with, [12.3.3](tuning.md)

nonpadded comparison semantics, [3.1.4.3.3](datatypes.md)

no-op (no operation) statement, [4.3.2](controlstatements.md)

NOT NULL constraint, [2.3.4](fundamentals.md)

%TYPE attribute and, [2.3.5](fundamentals.md)

EXTEND method and, [5.9.3](composites.md)

NOT operator, [2.7.3](fundamentals.md)

NOT\_LOGGED\_ON exception, [11.4](errors.md)

null collection, [5.1](composites.md)

assigning to collection variable, [5.6.2](composites.md)

collection method and, [5.9](composites.md)

NULL statement

syntax diagram, [13](null_statement.md)

uses for, [4.3.2](controlstatements.md)

null string, [2.2.3](fundamentals.md)

NULL value

assigning to record variable, [5.12.3](composites.md)

comparing to collection

associative array, [5.8](composites.md)

nested table, [5.8.1](composites.md)

varray, [5.8.1](composites.md)

comparison operator and, [2.7.5](fundamentals.md)

concatenation operator and, [2.7.1](fundamentals.md)

for $$PLSQL\_UNIT inquiry directive, [2.10.1.4.1](fundamentals.md)

for collection variable, [5.6.2](composites.md)

for subprogram parameter, [8.6.5](subprograms.md)

for unresolvable inquiry directive, [2.10.1.4.3](fundamentals.md)

in control statement, [2.7.3](fundamentals.md)

IN operator and, [2.7.5.5](fundamentals.md)

in set, [2.7.5.5](fundamentals.md)

simple CASE expression and, [2.7.7.1](fundamentals.md)

simple CASE statement and, [4.1.4](controlstatements.md)

NUMBER data type family

inefficiency of, [12.3.5.1](tuning.md)

members of, [E](predefined.md)

---

## O

obfuscating PL/SQL source text

See wrapping PL/SQL source text

object type

See Abstract Data Type (ADT)

OBJECT\_VALUE pseudocolumn, [9.3.3](triggers.md)

OCI

associative array and, [5.2.3](composites.md)

cursor variable and, [6.4.8](static.md)

OLD correlation name, [9.3.2](triggers.md)

OPEN FOR statement, [13](openfor_statement.md)

recursive invocation and, [8.9](subprograms.md)

OPEN statement, [13](open_statement.md)

recursive invocation and, [8.9](subprograms.md)

operation, [2.7.2](fundamentals.md)

operator

comparison, [2.7.5](fundamentals.md)

cursor variable and, [13](cursor_variable.md)

logical, [2.7.3](fundamentals.md)

relational, [2.7.5.2](fundamentals.md)

collection and, [5.8](composites.md)

operator precedence, [2.7.2](fundamentals.md)

optimizer

PL/SQL, [12.1](tuning.md)

SQL, [12.5.5](tuning.md)

OR operator, [2.7.3](fundamentals.md)

Oracle Call Interface (OCI)

associative array and, [5.2.3](composites.md)

cursor variable and, [6.4.8](static.md)

Oracle RAC environment, result caches in, [8.11.5.6](subprograms.md)

ORA-n error

See internally defined exception

ordinary user-defined identifier, [2.2.2.3.1](fundamentals.md)

Original Import and triggers, [9.13](triggers.md)

OUT parameter mode, [8.6.3](subprograms.md)

out-bind, [12.4](tuning.md)

outer capture, [B.5.1](nameresolution.md)

output, [1.2.7](overview.md)

overloaded subprogram, [8.8](subprograms.md)

INLINE pragma and, [12.1.1](tuning.md)

---

## P

package, [10.1](packages.md)

as application, [10.1](packages.md)

body of

See package body

DBMS\_STANDARD, [2.4](fundamentals.md)

explicitly recompiling, [14](alter_package.md)

features of, [10.2](packages.md)

guidelines for writing, [10.8](packages.md)

initialization of, [10.5](packages.md)

of static constants, [2.10.1.5.4](fundamentals.md)

private items in, [10.4](packages.md)

product-specific, [10](packages.md)

public items in

See public package item

reasons to use, [10.2](packages.md)

SERIALLY\_REUSABLE, [10.7](packages.md)

specification of

See package specification

STANDARD

See STANDARD package

state of, [10.6](packages.md)

supplied by Oracle, [10](packages.md)

wrapping, [A](wrap.md)

guideline for, [A.2](wrap.md)

package body, [10.1](packages.md)

creating, [14](create_package_body.md)

dropping, [14](drop_package.md)

initialization part of, [10.4](packages.md)

assigning initial values in, [10.8](packages.md)

replacing, [14](create_package_body.md)

package specification, [10.1](packages.md)

creating, [14](create_package.md)

cursor variable in, [13](cursor_variable.md)

dropping, [14](drop_package.md)

replacing, [14](create_package.md)

See also public package item

package subprogram, [8.2](subprograms.md)

parallel DML

bulk binding and, [12.4](tuning.md)

for large table, [12.6](tuning.md)

PARALLEL\_ENABLE option, [13](function.md)

for pipelined table function, [12.5.2](tuning.md)

for table function, [12.5.1](tuning.md)

parameter

compilation

See compilation parameter

explicit cursor, [6.2.2.6](static.md)

initialization, [1.3.2](overview.md)

subprogram

See subprogram parameter

parameter mode, [8.6.3](subprograms.md)

PARENT correlation name, [9.3.2](triggers.md)

with LONG or LONG RAW column, [9.9.2](triggers.md)

parentheses

nested, [2.7.2](fundamentals.md)

to control evaluation order, [2.7.2](fundamentals.md)

to improve readability, [2.7.2](fundamentals.md)

pattern matching, [2.7.5.3](fundamentals.md)

percent sign (%) wildcard character, [2.7.5.3](fundamentals.md)

PERFORMANCE compile-time warning, [11.1](errors.md)

PIPE ROW statement, [12.5.2](tuning.md)

PIPELINED option, [12.5.1](tuning.md)

where to specify, [12.5.2](tuning.md)

pipelined table function, [12.5.1](tuning.md)

as aggregate function, [12.5.6](tuning.md)

in autonomous transaction, [13](pipe_row_statement.md)

See also table function

placeholder for bind variable

in conditional compilation directive, [2.10.4](fundamentals.md)

in dynamic SQL

EXECUTE IMMEDIATE statement and, [7.2.1](dynamic.md)

repeated, [7.2.3](dynamic.md)

in static SQL, [6.1.1](static.md)

OPEN FOR statement and, [6.4.2](static.md)

in trigger body, [9.3.2](triggers.md)

PLS\_INTEGER data type, [3.3](datatypes.md)

tuning code and, [12.3.5.1](tuning.md)

PLS\_INTEGER static expression, [2.10.1.5.1](fundamentals.md)

PL/Scope tool, [12.7](tuning.md)

PL/SQL architecture, [1.3](overview.md)

PL/SQL block

See block

PL/SQL engine, [1.3.1](overview.md), [1.3.1](overview.md)

PL/SQL function result cache, [8.11](subprograms.md)

PL/SQL language

advantages of, [1.1](overview.md)

high performance of, [1.1.2](overview.md)

high productivity with, [1.1.3](overview.md)

lexical units of, [2.2](fundamentals.md)

limits of, [C](limits.md)

main features of, [1.2](overview.md)

manageability and, [1.1.6](overview.md)

new features of, [Preface](whatsnew.md)

portability of, [1.1.4](overview.md)

program limits of, [C](limits.md)

scalability of, [1.1.5](overview.md)

SQL integration in, [1.1.1](overview.md)

syntax and semantics, [13](langelems.md)

PL/SQL optimizer, [12.1](tuning.md)

PL/SQL table

See associative array

PL/SQL unit, [1.3.2](overview.md)

stored

See stored PL/SQL unit

PL/SQL Wrapper utility, [A.3](wrap.md)

PLSQL\_CCFLAGS compilation parameter, [2.10.1.4.2](fundamentals.md)

PLSQL\_OPTIMIZE\_LEVEL compilation parameter, [12.1](tuning.md)

PLSQL\_WARNINGS compilation parameter

displaying value of

with ALL\_PLSQL\_OBJECT\_SETTINGS view, [11.1](errors.md)

with DBMS\_WARNING subprogram, [11.1.1](errors.md)

setting value of

with ALTER statements, [11.1](errors.md)

with PLSQL\_WARNINGS subprogram, [11.1.1](errors.md)

portability, [1.1.4](overview.md)

positional parameter notation, [8.6.6](subprograms.md)

POSITIVE subtype, [3.3.2](datatypes.md)

POSITIVEN subtype, [3.3.2](datatypes.md)

post-processed source text, [2.10.3](fundamentals.md)

pragma, [2.9](fundamentals.md)

AUTONOMOUS\_TRANSACTION, [13](autotransaction_pragma.md)

for pipelined table function, [12.5.2](tuning.md)

EXCEPTION\_INIT, [13](exceptioninit_pragma.md)

INLINE, [12.1.1](tuning.md)

syntax diagram, [13](inline_pragma.md)

RESTRICT\_REFERENCES, [13](restrictreferences_pragma.md)

SERIALLY\_REUSABLE, [13](seriallyreusable_pragma.md)

precedence, operator, [2.7.2](fundamentals.md)

predefined constant, [3.1.2](datatypes.md)

predefined data type, [E](predefined.md)

predefined exception, [11.4](errors.md)

raising explicitly, [11.7.1.2](errors.md)

redeclared, [11.6](errors.md)

predefined inquiry directive, [2.10.1.4.1](fundamentals.md)

predefined subtype, [E](predefined.md)

preprocessor control token, [2.10.1.1](fundamentals.md)

PRIOR collection method, [5.9.8](composites.md)

privilege checking and AUTHID property, [8.13](subprograms.md)

procedure

declaration syntax, [13](procedure.md)

invoking, [8.3](subprograms.md)

structure of, [8.4.1](subprograms.md)

See also subprogram

procedure specification, [13](procedure.md)

product-specific package, [10](packages.md)

Profiler API, [12.8.1](tuning.md)

profiling and tracing programs, [12.8](tuning.md)

program limits, [C](limits.md)

PROGRAM\_ERROR exception, [11.4](errors.md)

pseudocolumn, [6.1.2](static.md)

pseudoinstruction

See pragma

pseudorecord, [9.3.2](triggers.md)

See also correlation name

public package item

appropriate, [10.3.1](packages.md)

collection type as, [5.10](composites.md)

cursor variable as, [13](cursor_variable.md)

declaring, [10.3](packages.md)

RECORD type as, [5.11.3](composites.md), [5.11.3](composites.md)

referencing, [10.3](packages.md)

remote variable, [10.3.1](packages.md)

scope of, [10.3](packages.md)

visibility of, [10.3](packages.md)

publishing events, [9.14](triggers.md)

purity rules for subprograms, [8.12](subprograms.md)

---

## Q

qualified name

See dot notation

qualified remote name, [2.4](fundamentals.md)

query

invoking function in, [12.3.2](tuning.md)

processing result set of, [6.3](static.md)

multiple-row dynamic query, [7.2.2](dynamic.md)

See also SELECT INTO statement

quotation mark, single or double, [2.1.1](fundamentals.md)

quoted user-defined identifier, [2.2.2.3.2](fundamentals.md)

---

## R

RAISE statement, [11.7.1](errors.md)

syntax diagram, [13](raise_statement.md)

RAISE\_APPLICATION\_ERROR procedure, [11.7.2](errors.md)

raising exception explicitly, [11.7](errors.md)

range test, [2.7.5.4](fundamentals.md)

read-only transaction, [6.6.5](static.md)

read-write transaction, [6.6.5](static.md)

recompiling stored PL/SQL unit, [14](sqlstatements.md)

record, [5](composites.md)

as public package item, [5.11.3](composites.md)

assigning value to, [5.12](composites.md)

creating, [5.11](composites.md)

syntax diagram, [13](record_definition.md)

declaring constant, [5.11.2](composites.md)

nested

See nested record

representing row, [5.11.4](composites.md)

types of, [5.11.3](composites.md)

recursive subprogram, [8.9](subprograms.md)

result-cached, [8.11.4.2](subprograms.md)

recursive trigger, [9.8](triggers.md)

REF CURSOR

See cursor variable

REF CURSOR type, [6.4.1](static.md)

relational operator, [2.7.5.2](fundamentals.md)

collection and, [5.8](composites.md)

RELEASE constant, [2.10.1.5.5](fundamentals.md)

remote exception handling

subprograms and, [11.8](errors.md)

triggers and, [9.7](triggers.md)

remote name, [2.4](fundamentals.md)

remote public package variable, [10.3.1](packages.md)

remote subprogram

with composite parameter, [5](composites.md)

REPEAT UNTIL structure, [4.2.7](controlstatements.md)

replacing stored PL/SQL unit, [14](sqlstatements.md)

reraising exception, [11.7.1.3](errors.md)

reserved preprocessor control token, [2.10.1.1](fundamentals.md)

reserved words

information about, [2.2.2.1](fundamentals.md)

list of, [D](reservewords.md)

RESTRICT\_REFERENCES pragma, [13](restrictreferences_pragma.md)

result cache, [8.11](subprograms.md)

RESULT\_CACHE clause, [8.11.1](subprograms.md)

RESULT\_CACHE option for function, [13](function.md)

RETURN clause of function, [8.4.1](subprograms.md)

RETURN INTO clause

See RETURNING INTO clause

RETURN statement, [8.4.2](subprograms.md)

RETURNING INTO clause, [13](returninginto_clause.md)

BULK COLLECT clause of, [12.4.2.3](tuning.md)

FORALL statement and, [12.4.3](tuning.md)

REUSE SETTINGS clause, [1.3.2](overview.md)

ROLLBACK statement, [6.6.2](static.md)

FOR UPDATE cursor and, [6.6.6.3](static.md)

implicit, [6.6.4](static.md)

in autonomous transaction, [6.7.5.2](static.md)

transparent, [9.8](triggers.md)

rowid, [3.1.6](datatypes.md)

ROWID data type, [3.1.6](datatypes.md)

ROWID pseudocolumn, [6.1.2](static.md)

instead of CURRENT OF clause, [6.6.6.3](static.md)

row-level trigger, [9.3](triggers.md)

ROWNUM pseudocolumn

bulk SELECT operation and, [12.4.2.1.2](tuning.md)

single-row result set and, [6.3.1.1](static.md)

ROWTYPE\_MISMATCH exception, [11.4](errors.md)

runtime error

See exception

---

## S

same-scope capture, [B.5.2](nameresolution.md)

SAMPLE clause, [12.4.2.1.2](tuning.md)

SAVEPOINT statement, [6.6.3](static.md)

in autonomous transaction, [6.7.5.3](static.md)

scalability

SERIALLY\_REUSABLE packages and, [10.7](packages.md)

subprograms and, [1.1.5](overview.md)

scalar data type, [3](datatypes.md)

scalar variable

assigning value to, [2.6](fundamentals.md)

declaration, [2.3.1](fundamentals.md)

syntax diagram, [13](variable_declaration.md)

initial value of, [2.3.3](fundamentals.md)

SCHEMA trigger, [9.4.1](triggers.md)

scope of identifier, [2.5](fundamentals.md)

searched CASE expression, [2.7.7.2](fundamentals.md)

searched CASE statement, [4.1.5](controlstatements.md)

syntax diagram, [13](case_statement.md)

security mechanism

against SQL injection, [7.4](dynamic.md)

PL/SQL source text wrapping

benefit of, [A](wrap.md)

limitations of, [A.1](wrap.md)

trigger as, [9.2](triggers.md)

SELECT FOR UPDATE statement, [6.6.6.2](static.md)

SELECT INTO statement

assigning values with

to record variable, [5.12.2.1](composites.md)

to scalar variables, [2.6.2](fundamentals.md)

avoiding inner capture in, [B.6](nameresolution.md)

query result set processing with, [6.3.1](static.md)

SQL%NOTFOUND attribute and, [6.2.1.3](static.md)

SQL%ROWCOUNT attribute and, [6.2.1.4](static.md)

syntax diagram, [13](selectinto_statement.md)

with BULK COLLECT clause, [12.4.2.1](tuning.md)

See also query

selection directive, [2.10.1.2](fundamentals.md)

selector

in simple CASE expression, [2.7.7.1](fundamentals.md)

in simple CASE statement, [4.1.4](controlstatements.md)

SELF\_IS\_NULL exception, [11.4](errors.md)

sequence, [6.1.2.1](static.md)

sequential control statement, [4.3](controlstatements.md)

SERIALLY\_REUSABLE package, [10.7](packages.md)

SERIALLY\_REUSABLE pragma, [13](seriallyreusable_pragma.md)

session cursor, [6.2](static.md)

set data structure, [5.1](composites.md)

set membership test, [2.7.5.5](fundamentals.md)

SET ROLE command and AUTHID property, [8.13.2](subprograms.md)

SET TRANSACTION statement, [6.6.5](static.md)

SEVERE compile-time warning, [11.1](errors.md)

short-circuit evaluation

how it works, [2.7.4](fundamentals.md)

tuning code and, [12.3.7](tuning.md)

side effects of subprogram, [8.10](subprograms.md)

SIGNTYPE subtype, [3.3.2](datatypes.md)

simple CASE expression, [2.7.7.1](fundamentals.md)

simple CASE statement, [4.1.4](controlstatements.md)

IF THEN ELSIF statement and, [4.1.3](controlstatements.md)

syntax diagram, [13](case_statement.md)

simple DML trigger, [9.3](triggers.md)

simple name, [2.4](fundamentals.md)

SIMPLE\_DOUBLE subtype, [3.1.3](datatypes.md)

tuning code and, [12.3.5.1](tuning.md)

SIMPLE\_FLOAT subtype, [3.1.3](datatypes.md)

tuning code and, [12.3.5.1](tuning.md)

SIMPLE\_INTEGER subtype, [3.3.3](datatypes.md)

tuning code and, [12.3.5.1](tuning.md)

single quotation mark (’), [2.1.1](fundamentals.md)

single-line comment, [2.2.4.1](fundamentals.md)

sparse collection, [5.1](composites.md)

FORALL statement for, [12.4.1.1](tuning.md)

SQL%BULK\_EXCEPTIONS and, [12.4.1.4.1](tuning.md)

traversing, [5.9.8](composites.md)

specification

cursor, [13](explicit_cursor.md)

function, [13](function.md)

package

See package specification

procedure, [13](procedure.md)

SQL

bulk, [12.4](tuning.md)

in compound DML trigger, [9.3.5.3](triggers.md)

dynamic

See dynamic SQL

static

See static SQL

SQL cursor

See implicit cursor

SQL data type, [3.1](datatypes.md)

SQL function

in PL/SQL expression, [2.7.8](fundamentals.md)

tuning and, [12.3.6](tuning.md)

SQL injection, [7.4](dynamic.md)

SQL integration in PL/SQL, [1.1.1](overview.md)

SQL multiset condition, [5.8.3](composites.md)

SQL MULTISET operator, [5.6.3](composites.md)

SQL optimizer, [12.5.5](tuning.md)

SQL statement

for stored PL/SQL unit, [14](sqlstatements.md)

in trigger, [9.1](triggers.md)

invoking collection method in, [5.9](composites.md)

invoking PL/SQL function in, [8.12](subprograms.md)

tuning, [12.3.1](tuning.md)

See also anonymous block

SQL%BULK\_EXCEPTIONS cursor attribute, [12.4.1.4](tuning.md)

SQL%BULK\_ROWCOUNT cursor attribute, [12.4.1.5](tuning.md)

SQL%FOUND cursor attribute, [6.2.1.2](static.md)

SQL%NOTFOUND cursor attribute, [6.2.1.3](static.md)

SQL%ROWCOUNT cursor attribute, [6.2.1.4](static.md)

SQL\*Loader and triggers, [9.13](triggers.md)

SQLCODE function, [13](sqlcode_function.md)

SQLERRM function, [13](sqlerrm_function.md)

SQL%BULK\_EXCEPTIONS and, [12.4.1.4](tuning.md)

SQLJ object type, creating, [14](create_type.md)

standalone subprogram, [8.2](subprograms.md)

function

creating, [14](create_function.md)

dropping, [14](drop_function.md)

explicitly recompiling, [14](alter_function.md)

replacing, [14](create_function.md)

procedure

creating, [14](create_procedure.md)

dropping, [14](drop_procedure.md)

explicitly recompiling, [14](alter_procedure.md)

replacing, [14](create_procedure.md)

STANDARD package

data type defined in

See predefined data type

exception defined in

See predefined exception

how it defines PL/SQL environment, [10.10](packages.md)

listing identifiers defined in, [2.2.2.2](fundamentals.md)

referencing item defined in, [2.4](fundamentals.md)

statement injection, [7.4.1.2](dynamic.md)

statement modification, [7.4.1.1](dynamic.md)

statement-level trigger, [9.3](triggers.md)

static constant, [2.10.1.5.4](fundamentals.md)

in DBMS\_DB\_VERSION package, [2.10.1.5.5](fundamentals.md)

static expression, [2.10.1.5](fundamentals.md), [2.10.1.5](fundamentals.md)

static SQL, [6](static.md)

AUTHID property and, [8.13](subprograms.md)

name resolution in, [B.4](nameresolution.md)

placeholder for bind variable in, [6.1.1](static.md)

OPEN FOR statement and, [6.4.2](static.md)

PL/SQL identifier in, [6.1.1](static.md)

STORAGE\_ERROR exception, [11.4](errors.md)

recursive invocation and, [8.9](subprograms.md)

store table, [5.4.2](composites.md)

stored PL/SQL unit, [1.3.2](overview.md)

creating, [14](sqlstatements.md)

recompiling, [14](sqlstatements.md)

replacing, [14](sqlstatements.md)

wrapping, [A](wrap.md)

stored subprogram, [8.2](subprograms.md)

unhandled exception in, [11.9](errors.md)

wrapping, [A](wrap.md)

string

null, [2.2.3](fundamentals.md)

zero-length, [2.2.3](fundamentals.md)

See also character literal

STRING subtype, [3.1.4.3.1](datatypes.md)

strong REF CURSOR type

creating, [6.4.1](static.md)

FETCH statement and, [6.4.3](static.md)

subprogram, [8](subprograms.md)

inlining, [12.1.1](tuning.md)

invoked by trigger, [9.5](triggers.md)

remote

See remote subprogram

unhandled exception in, [11.9](errors.md)

subprogram invocation

optimization of, [12.1.1](tuning.md)

resolution of, [8.7](subprograms.md)

syntax of, [8.3](subprograms.md)

tuning, [12.3.3](tuning.md)

subprogram parameter, [8.6](subprograms.md)

collection as, [5.9](composites.md)

CURSOR expression as actual, [6.5](static.md)

cursor variable as, [6.4.7](static.md)

optional, [8.6.5](subprograms.md)

pseudorecord as, [9.3.2](triggers.md)

query result as, [6.4.7](static.md)

required, [8.6.5](subprograms.md)

subquery

correlated, [6.3.4](static.md)

result set processing with, [6.3.4](static.md)

SUBSCRIPT\_BEYOND\_COUNT exception, [11.4](errors.md)

SUBSCRIPT\_OUTSIDE\_LIMIT exception, [11.4](errors.md)

subtype, [3](datatypes.md)

constrained, [3.4.2](datatypes.md)

subprogram parameter and, [8.6.1](subprograms.md)

of BINARY\_DOUBLE data type, [3.1.3](datatypes.md)

of BINARY\_FLOAT data type, [3.1.3](datatypes.md)

of PLS\_INTEGER data type, [3.3.2](datatypes.md)

predefined, [E](predefined.md)

unconstrained, [3.4.1](datatypes.md)

user-defined, [3.4](datatypes.md)

See also data type

synonym, [2.4](fundamentals.md)

SYS\_INVALID\_ROWID exception, [11.4](errors.md)

SYS\_REFCURSOR type, [6.4.1](static.md)

system trigger, [9.4](triggers.md)

---

## T

table

hash, [5.1](composites.md)

index-by

See associative array

mutating, [9.9.3](triggers.md)

nested, [5.4](composites.md)

characteristics of, [5.1](composites.md)

parallel DML for large, [12.6](tuning.md)

PL/SQL

See associative array

store, [5.4.2](composites.md)

unordered, [5.1](composites.md)

updating large in parallel, [12.6](tuning.md)

table alias

for avoiding inner capture, [B.6](nameresolution.md)

for row expression, [B.6.2](nameresolution.md)

for table element attribute or method, [B.6.1](nameresolution.md)

table function, [12.5.1](tuning.md)

pipelined

See pipelined table function

weak cursor variable argument to, [6.4.1](static.md)

TCL statement, [6.1.1](static.md)

in subprogram invoked by trigger, [9.5](triggers.md)

in trigger, [6.7.6](static.md)

TIMEOUT\_ON\_RESOURCE exception, [11.4](errors.md)

timing point

of compound DML trigger, [9.3.5.1](triggers.md)

of simple DML trigger, [9.3](triggers.md)

of system trigger, [9.4](triggers.md)

trigger firing order and, [9.10](triggers.md)

TO\_CURSOR\_NUMBER function, [7.3.2](dynamic.md)

TO\_REFCURSOR function, [7.3.1](dynamic.md)

TOO\_MANY\_ROWS exception, [11.4](errors.md)

Trace API, [12.8.2](tuning.md)

trace file, [11](errors.md)

tracing and profiling programs, [12.8](tuning.md)

transaction

autonomous, [6.7](static.md)

pipelined table function in, [13](pipe_row_statement.md)

ending

with COMMIT statement, [6.6.1](static.md)

with ROLLBACK statement, [6.6.2](static.md)

nested, [6.7](static.md)

read-only, [6.6.5](static.md)

read-write, [6.6.5](static.md)

retrying after handling exception, [11.12](errors.md)

SQL%ROWCOUNT cusor attribute and, [6.2.1.4](static.md)

Transaction Control Language

See TCL statement

TRANSACTIONS initialization parameter, [6.7.5.4](static.md)

trigger, [9](triggers.md)

as security mechanism, [9.2](triggers.md)

AUTHID property and, [8.13](subprograms.md)

autonomous, [6.7.6](static.md)

cascading, [9.10](triggers.md)

DDL statement in, [6.7.6](static.md)

hiding implementation details of, [A.1](wrap.md)

IR subprogram invoked by, [8.13.5](subprograms.md)

materialized view and, [14](create_trigger.md)

recursive, [9.8](triggers.md)

TCL statement in, [6.7.6](static.md)

TRIM collection method, [5.9.2](composites.md)

tri-state logic, [2.7.3](fundamentals.md)

tuning PL/SQL code, [12](tuning.md)

type

See data type

type-compatible data type

for collection variables, [5.6.1](composites.md)

for scalar variables, [2.6](fundamentals.md)

---

## U

unconstrained subtype, [3.4.1](datatypes.md)

underscore (\_) wildcard character, [2.7.5.3](fundamentals.md)

unhandled exception, [11.9](errors.md)

in FORALL statement, [12.4.1.2](tuning.md)

unordered table, [5.1](composites.md)

UPDATE statement

BEFORE statement trigger and, [9.8](triggers.md)

PL/SQL extensions to, [13](update_statement.md)

with values in record, [5.15](composites.md)

restrictions on, [5.16](composites.md)

See also DML statement

UPDATING conditional predicate, [9.3.1](triggers.md)

UROWID data type, [3.1.6](datatypes.md)

USER\_DUMP\_DEST initialization parameter, [11](errors.md)

user-defined exception, [11.5](errors.md)

giving error code to, [11.7.2](errors.md)

raising

with RAISE statement, [11.7.1.1](errors.md)

with RAISE\_APPLICATION\_ERROR procedure, [11.7.2](errors.md)

user-defined identifier, [2.2.2.3](fundamentals.md)

collecting data about, [12.7](tuning.md)

user-defined subtype, [3.4](datatypes.md)

user-defined type

See Abstract Data Type (ADT)

utlrp.sql script, [12.9.5](tuning.md)

---

## V

V$RESERVED\_WORDS view, [D](reservewords.md)

validation check for avoiding SQL injection, [7.4.2.2](dynamic.md)

VALUE\_ERROR exception, [11.4](errors.md)

VARCHAR subtype, [3.1.4.3.1](datatypes.md)

VARCHAR2 data type, [3.1.4](datatypes.md)

VARCHAR2 static expression, [2.10.1.5.3](fundamentals.md)

variable

binding of, [12.4](tuning.md)

BOOLEAN, [2.6.4](fundamentals.md)

collection

See collection

composite, [5](composites.md)

cursor

See cursor variable

host

cursor variable as, [6.4.8](static.md)

packages and, [10.2](packages.md)

in cursor variable query, [6.4.5](static.md)

in explicit cursor query, [6.2.2.4](static.md)

locator, [11.2.2](errors.md)

record

See record

remote public package, [10.3.1](packages.md)

scalar

See scalar variable

with undefined value, [6.1.1](static.md)

variable-size array

See varray

varray, [5.3](composites.md)

assigning null value to, [5.6.2](composites.md)

characteristics of, [5.1](composites.md)

comparing to NULL, [5.8.1](composites.md)

COUNT method for, [5.9.6.1](composites.md)

FIRST and LAST methods for, [5.9.5.2](composites.md)

returned by function, [12.5.1](tuning.md)

See also collection

VERSION constant, [2.10.1.5.5](fundamentals.md)

view

AUTHID property and, [8.13](subprograms.md)

INSTEAD OF trigger and, [14](create_trigger.md)

IR subprogram invoked by, [8.13.5](subprograms.md)

materialized, trigger and, [14](create_trigger.md)

virtual column

%ROWTYPE attribute and, [5.11.4.3](composites.md)

explicit cursors and, [6.2.2.5](static.md)

visibility

---

## W

warning, compile-time, [11.1](errors.md)

weak REF CURSOR type

creating, [6.4.1](static.md)

FETCH statement and, [6.4.3](static.md)

WHILE LOOP statement, [4.2.7](controlstatements.md)

syntax diagram, [13](while_loop_statement.md)

whitespace character

wildcard character, [2.7.5.3](fundamentals.md)

WRAP function, [A.4](wrap.md)

wrap utility

wrapping PL/SQL source text, [A](wrap.md)

---

## Z

ZERO\_DIVIDE exception, [11.4](errors.md)

zero-length string, [2.2.3](fundamentals.md)