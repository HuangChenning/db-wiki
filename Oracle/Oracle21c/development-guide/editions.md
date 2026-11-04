---
title: Database Development Guide
book: Database Development Guide
doc_id: F31304-06
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/adfns/editions.html
tags:
  - oracle
  - 21c
  - development-guide
---

Edition-based redefinition (EBR) lets you upgrade the database component of an application while it is in use, thereby minimizing or eliminating downtime.

Topics:

### 28.1 Overview of Edition-Based Redefinition

To upgrade an application while it is in use, you must copy the database objects that comprise the database component of the application and redefine the copied objects in isolation. Your changes do not affect users of the application—they can continue to run the unchanged application. When you are sure that your changes are correct, you make the upgraded application available to all users.

Using EBR means using one or more of its component features. The features you use, and the downtime, depend on these factors:

- What kind of database objects you redefine
- How available the database objects must be to users while you are redefining them
- Whether you make the upgraded application available to some users while others continue to use the older version of the application

You always use the edition feature to copy the database objects and redefine the copied objects in isolation; that is why the procedure that this chapter describes for upgrading applications online is called edition-based redefinition (EBR).

If every object that you will redefine is editioned (defined in Editioned and Noneditioned Objects), then the edition is the only feature you use.

Tables are not editioned objects. If you change the structure of one or more tables, then you also use the editioning view feature.

If other users must be able to change data in the tables while you are changing their structure, then you also use forward crossedition triggers. If the pre- and post-upgrade applications will be in ordinary use at the same time (hot rollover), then you also use reverse crossedition triggers. Crossedition triggers are not a permanent part of the application—you drop them when all users are using the post-upgrade application.

An EBR operation that you can perform on an application in one edition while the application runs in other editions is a live operation.

### 28.2 Editions

Editions are nonschema objects; as such, they do not have owners. Editions are created in a single namespace, and multiple editions can coexist in the database.

The database must have at least one edition. Every newly created or upgraded Oracle Database starts with one edition named `ora$base`.

Topics:

- Editioned and Noneditioned Objects
- Creating an Edition
- Editioned Objects and Copy-on-Change
- Making an Edition Available to Some Users
- Making an Edition Available to All Users
- Current Edition and Session Edition
- Retiring an Edition
- Dropping an Edition

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ADMIN13506) for information about CDBs and PDBs

#### 28.2.1 Editioned and Noneditioned Objects

Note:

The terms user and schema are synonymous. The owner of a schema object is the user/schema that owns it.

An editioned object has both a schema object type that is editionable in its owner and the `EDITIONABLE` property. An edition has its own copy of an editioned object, and only that copy is visible to the edition.

A noneditioned object has either a schema object type that is noneditionable in its owner or the `NONEDITIONABLE` property. An edition cannot have its own copy of a noneditioned object. A noneditioned object is visible to all editions.

An object is potentially editioned if enabling editions for its type in its owner would make it an editioned object.

An editioned object belongs to both a schema and an edition, and is uniquely identified by its `OBJECT_NAME`, `OWNER`, and `EDITION_NAME`. A noneditioned object belongs only to a schema, and is uniquely identified by its `OBJECT_NAME` and `OWNER` —its `EDITION_NAME` is `NULL`. (Strictly speaking, the `NAMESPACE` of an object is also required to uniquely identify the object, but you can ignore this fact, because any statement that references the object implicitly or explicitly specifies its `NAMESPACE`.)

You can display the `OBJECT_NAME`, `OWNER`, and `EDITION_NAME` of an object with the static data dictionary views `*_OBJECTS` and `*_OBJECTS_AE`.

You need not know the `EDITION_NAME` of an object to refer to that object (and if you do know it, you cannot specify it). The context of the reference implicitly specifies the edition. If the context is a data definition language (DDL) statement, then the edition is the current edition of the session that issued the command. If the context is source code, then the edition is the one in which the object is actual.

Topics:

- Name Resolution for Editioned and Noneditioned Objects
- Noneditioned Objects That Can Depend on Editioned Objects
- Editionable and Noneditionable Schema Object Types
- Enabling Editions for a User
- EDITIONABLE and NONEDITIONABLE Properties
- Rules for Editioned Objects

See Also:

- Enabling Editions for a User
- Current Edition and Session Edition
- Editioned Objects and Copy-on-Change

##### 28.2.1.1 Name Resolution for Editioned and Noneditioned Objects

To try to resolve an object name, Oracle Database uses the procedure described in [Name Resolution in Schema Scope](schema-object-dependency.md). For the procedure to succeed, all pieces of the object name must be visible in the current edition.

During name resolution for an editioned object, both editioned objects in the current edition and noneditioned objects are visible.

During name resolution for a noneditioned object, only noneditioned objects are visible. Therefore, if you try to create a noneditioned object that references an editioned object (except in the cases described in Noneditioned Objects That Can Depend on Editioned Objects), the creation fails with an error.

When you change a referenced editioned object, all of its dependents (direct and indirect) become invalid. When an invalid object is referenced, the database tries to validate that object.

See Also:

- Current Edition and Session Edition
- [Understanding Schema Object Dependency](schema-object-dependency.md), for general information about dependencies among schema objects, including invalidation, revalidation, and name resolution

##### 28.2.1.2 Noneditioned Objects That Can Depend on Editioned Objects

Ordinarily, a noneditioned object cannot depend on an editioned object, because the editioned object is invisible during name resolution. However, if a noneditioned object specifies an edition to search for editioned objects during name resolution—an evaluation edition—then it can depend on editioned objects. To specify an evaluation edition, a noneditioned object must be one of the following:

- Materialized view
- Virtual column

Topics:

- Materialized Views
- Virtual Columns

###### 28.2.1.2.1 Materialized Views

A materialized view is a noneditioned object that can specify an evaluation edition, thereby enabling it to depend on editioned objects. A materialized view that depends on editioned objects may be eligible for query rewrite only in a specific range of editions, which you specify in the `query_rewrite_clause`.

The simplified syntax for creating a materialized view is:

```
CREATE MATERIALIZED VIEW [ schema.] materialized_view other_clauses
[ evaluation_edition_clause ] [ query_rewrite_clause ] AS subquery
```

Where `evaluation_edition_clause` is:

```
EVALUATE USING { CURRENT EDITION | EDITION edition | NULL EDITION }
```

And `query_rewrite_clause` is:

```
{ DISABLE | ENABLE } QUERY REWRITE
[ unusable_before_clause ] [ unusable_beginning_clause ]
```

Where `unusable_before_clause` is:

```
UNUSABLE BEFORE { CURRENT EDITION | EDITION edition }
```

And `unusable_beginning_clause` is:

```
UNUSABLE BEGINNING WITH { CURRENT EDITION | EDITION edition | NULL EDITION }
```

`CURRENT` `EDITION` is the edition in which the DDL statement runs. Specifying `NULL` `EDITION` is equivalent to omitting the clause that includes it. If you omit `evaluation_edition_clause`, then editioned objects are invisible during name resolution.

To disable, enable, or change the evaluation edition or unusable editions, use the `ALTER` `MATERIALIZED` `VIEW` statement.

To display the evaluation editions and unusable editions of materialized views, use the static data dictionary views `*_MVIEWS`.

Dropping the evaluation edition invalidates the materialized view. Dropping an edition where the materialized view is usable does not invalidate the materialized view.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF01302) for more information about `CREATE` `MATERIALIZED` `VIEW` statement

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF00808)

[Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN20139)

###### 28.2.1.2.2 Virtual Columns

A virtual column (also called a "generated column") does not consume disk space. The database generates the values in a virtual column on demand by evaluating an expression. The expression can invoke PL/SQL functions (which can be editioned objects). A virtual column can specify an evaluation edition, thereby enabling it to depend on an expression that invokes editioned PL/SQL functions.

The syntax for creating a virtual column is:

```
column [ datatype ] [ GENERATED ALWAYS ] AS ( column_expression )
[ VIRTUAL ] [ evaluation_edition_clause ]
[ unusable_before_clause ] [ unusable_beginning_clause ]
[ inline_constraint ]...
```

Where `evaluation_edition_clause` is as described in Materialized Views.

The database does not maintain dependencies on the functions that a virtual column invokes. Therefore, if you drop the evaluation edition, or if a virtual column depends on a noneditioned function and the function becomes editioned, then any of the following can raise an exception:

- Trying to query the virtual column
- Trying to update a row that includes the virtual column
- A trigger that tries to access the virtual column

To display the evaluation editions of virtual columns, use the static data dictionary views `*_TAB_COLS`.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF54465) for the complete syntax and semantics of the virtual column definition
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN20276) for more information about `ALL_TAB_COLS`

##### 28.2.1.3 Editionable and Noneditionable Schema Object Types

Before a schema object type can be editionable in a schema, it must be editionable in the database. The schema object types that are editionable in the database are determined by the value of the `COMPATIBLE` initialization parameter and are shown by the dynamic performance view `V$EDITIONABLE_TYPES`.

If the value of `COMPATIBLE` is 12 or greater, then these schema object types are editionable in the database:

- `SYNONYM`
- `VIEW`
- SQL translation profile
- All PL/SQL object types:
	- `FUNCTION`
		- `LIBRARY`
		- `PACKAGE` and `PACKAGE` `BODY`
		- `PROCEDURE`
		- `TRIGGER`
		- `TYPE` and `TYPE` `BODY`

All other schema object types are noneditionable in the database and in every schema, and objects of that type are always noneditioned. `TABLE` is an example of a noneditionable schema object type. Tables are always noneditioned objects.

If a schema object type is editionable in the database, then it can be editionable in schemas.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ADMIN11112) for more information about `COMPATIBLE` initialization parameter
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN30660) for more information about `V$EDITIONABLE_TYPES`
- Enabling Editions for a User

##### 28.2.1.4 Enabling Editions for a User

Note:

- Enabling editions is not a live operation.
- When a database is upgraded from Release 11.2 to Release 12.1, users who were enabled for editions in the pre-upgrade database are enabled for editions in the post-upgrade database and the default schema object types are editionable in their schemas. The default schema object types are displayed by the static data dictionary view `DBA_EDITIONED_TYPES`. Users who were not enabled for editions in the pre-upgrade database are not enabled for editions in the post-upgrade database and no schema object types are editionable in their schemas.
- To see which users already have editions enabled, see the `EDITIONS_ENABLED` column of the static data dictionary view `DBA_USERS` or `USER_USERS`.

To enable editions for a user, use the `ENABLE` `EDITIONS` clause of either the `CREATE` `USER` or `ALTER` `USER` statement.

With the `ALTER` `USER` statement, you can specify the schema object types that become editionable in the schema:

```
ALTER USER user ENABLE EDITIONS [ FOR type [, type ]... ]
```

Any type that you omit from the `FOR` list is noneditionable in the schema, despite being editionable in the database. If a type is noneditionable in the database, then it is always noneditionable in every schema.

If you omit the `FOR` list from the `ALTER USER` statement or use the `CREATE USER` statement to enable editions for a user, then the types that become editionable in the schema are `VIEW`, `SYNONYM`, `PROCEDURE`, `FUNCTION`, `PACKAGE`, `PACKAGE BODY`, `TRIGGER`, `TYPE`, `TYPE BODY`, and `LIBRARY`.

To enable edition for other object types that are not enabled by default, you must explicitly specify the object type in the `FOR` clause. For example, to enable editions for `SQL TRANSLATION PROFILE`, run the following command:

```
ALTER USER user ENABLE EDITIONS [ FOR SQL TRANSLATION PROFILE];
```

The static data dictionary view `DBA_EDITIONED_TYPES` lists all the object types that can appear in the `FOR` type clause. Refer to this view if you need to enable editions for specific object types.

Enabling editions is retroactive and irreversible. When you enable editions for a user, that user is editions-enabled forever. When you enable editions for a schema object type in a schema, that type is editions-enabled forever in that schema. Every object that an editions-enabled user owns or will own becomes an editioned object if its type is editionable in the schema and it has the `EDITIONABLE` property. For information about the `EDITIONABLE` property, see EDITIONABLE and NONEDITIONABLE Properties.

Topics:

- Potentially Editioned Objects with Noneditioned Dependents
- Users Who Cannot Have Editions Enabled

See Also:

Oracle Database SQL Language Reference for the complete syntax and semantics of the [`CREATE` `USER`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF01503) and [`ALTER` `USER`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF01103) statements

[Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN23867) for more information about `DBA_EDITIONED_TYPES`

[Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN23302) for more information about `DBA_USERS`

[Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN26302) for more information about `USER_USERS`

###### 28.2.1.4.1 Potentially Editioned Objects with Noneditioned Dependents

If a potentially editioned object has a noneditioned dependent, then you can enable editions for the owner of the potentially editioned object only if one of the following is true:

- Enabling editions for the owner of the potentially editioned object would cause the noneditioned dependent to become editioned.
- You specify `FORCE`:
	```
	ALTER USER user ENABLE EDITIONS [ FOR type [, type ]... ] FORCE;
	```
	The preceding statement enables editions for the specified user and invalidates noneditioned dependents of editioned objects.

Note:

If the preceding statement invalidates a noneditioned dependent object that contains an Abstract Data Type (ADT), and you drop the edition that contains the editioned object on which the invalidated object depends, then you cannot recompile the invalidated object. Therefore, the object remains invalid.

`FORCE` is useful in the following situation: You must editions-enable users `A` and `B`. User `A` owns potentially editioned objects `a1` and `a2`. User `B` owns potentially editioned objects `b1` and `b2`. Object `a1` depends on object `b1`. Object `b2` depends on object `a2`. Editions-enable users `A` and `B` like this:

1. Using `FORCE`, enable editions for user `A`:
	```
	ALTER USER A ENABLE EDITIONS FORCE;
	```
	Now `a1` and `a2` are editioned objects, and noneditioned object `b2` (which depends on `a2`) is invalid.
2. Enable editions for user `B`:
	```
	ALTER USER B ENABLE EDITIONS;
	```
	Now `b1` and `b2` are editioned objects; however, `b2` is still invalid.
3. Recompile `b2`, using the appropriate `ALTER` statement with `COMPILE`. For a PL/SQL object, also specify `REUSE` `SETTINGS`.
	For example, if `b2` is a procedure, use this statement:
	```
	ALTER PROCEDURE b2 COMPILE REUSE SETTINGS
	```

`FORCE` is unnecessary in the following situation: You must editions-enable user `C`, who owns potentially editioned object `c1`. Object `c1` has dependent `d1`, a potentially editioned object owned by user `D`. User `D` owns no potentially editioned objects that have dependents owned by `C`. If you editions-enable `D` first, making `d1` an editioned object, then you can editions-enable `C` without violating the rule that a noneditioned object cannot depend on an editioned object.

See Also:

- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=LNPLS99974) for information about the `ALTER` statements for PL/SQL objects
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF008) for information about the `ALTER` statements for SQL objects
- [Invalidation of Dependent Objects](schema-object-dependency.md) for information about invalidation of dependent objects

###### 28.2.1.4.2 Users Who Cannot Have Editions Enabled

You cannot enable editions for these users:

- Oracle-maintained users
	For an Oracle-maintained user, the value of the column ORACLE\_MAINTAINED is Y in the \*\_USERS views.
- A user who owns one or more evolved ADTs.
	Trying to do so causes error ORA-38820. If an ADT has no table dependents, you can use the `ALTER` `TYPE` `RESET` statement to reset its version to 1, so that it is no longer considered to be evolved. (Resetting the version of an ADT to 1 invalidates its dependents.)

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ADMIN13508) for information about common users in a CDB
- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=LNPLS99995) for the syntax of the `ALTER` `TYPE` `RESET` statement

##### 28.2.1.5 EDITIONABLE and NONEDITIONABLE Properties

Note:

When a database is upgraded from Release 11.2 to Release 12.1, objects in user-created schemas get the `EDITIONABLE` property and public synonyms get the `NONEDITIONABLE` property.

The `CREATE` and `ALTER` statements for the schema object types that are editionable in the database let you specify that the object you are creating or altering is `EDITIONABLE` or `NONEDITIONABLE`.

The `DBMS_SQL_TRANSLATOR.CREATE_PROFILE` procedure lets you specify that the SQL translation profile that you are creating is `EDITIONABLE` or `NONEDITIONABLE`.

To see which objects are `EDITIONABLE`, see the `EDITIONABLE` column of the static data dictionary view `*_OBJECTS` or `*_OBJECTS_AE`.

Topics:

- Creating New EDITIONABLE and NONEDITIONABLE Objects
- Replacing or Altering EDITIONABLE and NONEDITIONABLE Objects

See Also:

- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=LNPLS99979) for the syntax and semantics of the `CREATE` and `ALTER` statements for PL/SQL schema objects
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF-GUID-049B7AE8-11E1-4110-B3E4-D117907D77AC) for the syntax and semantics of the `CREATE` and `ALTER` statements for SQL schema objects
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ARPLS73547) for information about the `DBMS_SQL_TRANSLATOR.CREATE_PROFILE` procedure
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN20146) for more information about `*_OBJECTS`
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN20578) for more information about `*_OBJECTS_AE`

###### 28.2.1.5.1 Creating New EDITIONABLE and NONEDITIONABLE Objects

When you create a new schema object whose type is editionable in the database, you can specify the property `EDITIONABLE` or `NONEDITIONABLE`. If you omit the property, then the object is `EDITIONABLE` by default unless it is one of the following:

- `PUBLIC` `SYNONYM`, which is `NONEDITIONABLE` by default
- `PACKAGE` `BODY`, which inherits the property of the package specification
- `TYPE` `BODY`, which inherits the property of the type specification

For `PACKAGE` `BODY` or `TYPE` `BODY`, if you specify a property, then it must match the property of the corresponding package or type specification.

When you create an `EDITIONABLE` object of a type that is editionable in its schema, the new object is an editioned object that is visible only in the edition that is current when the object is created. Creating an editioned object is a live operation with respect to the editions in which the new object is invisible.

When you create either an object with the `NONEDITIONABLE` property or an object whose type is noneditionable in its schema, the new object is a noneditioned object, which is visible to all editions.

Suppose that in the current edition, your schema has no schema object named `obj`, but in another edition, your schema has an editioned object named `obj`. You can create an object named `obj` in your schema in the current edition, but it must be an editioned object (that is, uniquely identified by its `OBJECT_NAME`, `OWNER`, and `EDITION_NAME`). The type of the new object (which can be different from the type of the existing editioned object with the same name) must be editionable in your schema and the new object must have the `EDITIONABLE` property.

See Also:

- Current Edition and Session Edition for information about the current edition
- Example: Dropping an Editioned Object
- Example: Creating an Object with the Name of a Dropped Inherited Object

###### 28.2.1.5.2 Replacing or Altering EDITIONABLE and NONEDITIONABLE Objects

When you replace or alter an existing object (with the `CREATE` `OR` `REPLACE` or `ALTER` statement):

- If the schema is not enabled for editions, then you can change the property of the object from `EDITIONABLE` to `NONEDITIONABLE`, or the reverse.
- If the schema is enabled for editions for the type of the object being replaced or altered, then you cannot change the property of the object from `EDITIONABLE` to `NONEDITIONABLE`, or the reverse.

Altering an editioned object is a live operation with respect to the editions in which the altered object is invisible.

##### 28.2.1.6 Rules for Editioned Objects

- A noneditioned object usually cannot depend on an editioned object.
- An Abstract Data Type (ADT) cannot be both editioned and evolved.
- An editioned object cannot be the starting or ending point of a `FOREIGN` `KEY` constraint.
	This rule affects only editioned views. An editioned view can be either an ordinary view or an editioning view.

See Also:

- Name Resolution for Editioned and Noneditioned Objects
- [Oracle Database Object-Relational Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ADOBJ00603) for information about type evolution

#### 28.2.2 Creating an Edition

To create an edition, use the SQL statement `CREATE` `EDITION`.

You must create the edition as the child of an existing edition. The parent of the first edition created with a `CREATE` `EDITION` statement is `ora$base`. This statement creates the edition `e2` as the child of `ora$base`:

```
CREATE EDITION e2
```

(Example: Editioned Objects and Copy-on-Change and others use the preceding statement.)

An edition can have at most one child.

The descendents of an edition are its child, its child's child, and so on. The ancestors of an edition are its parent, its parent's parent, and so on. The root edition has no parent, and a leaf edition has no child.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF20017) for information about the `CREATE` `EDITION` statement, including the privileges required to use it
- [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ADMIN13508) for information about CDBs

#### 28.2.3 Editioned Objects and Copy-on-Change

When you create an edition, all editioned objects in its parent edition are copied to it. Changes to an editioned object in one edition do not affect copies of that editioned object in other editions.

The preceding paragraph describes what happens conceptually. In practice, to optimize performance, Oracle Database copies an editioned object from an ancestor edition to a descendent edition only when the descendent edition changes the object. This strategy is called copy-on-change.

An editioned object that was conceptually (but not actually) copied to a descendent edition is called an inherited object. When a user of the descendent edition references an inherited object in a DDL statement, Oracle Database actually copies the object to the descendent edition. This copying operation is called actualization, and it creates an actual object in the descendent edition.

Note:

There is one exception to the actualization rule in the preceding paragraph: When a `CREATE` `OR` `REPLACE` `object` statement replaces an inherited object with an identical object (that is, an object with the same source code and settings), Oracle Database does not create an actual object in the descendent edition.

##### 28.2.3.1 Example: Editioned Objects and Copy-on-Change

Example 28-1 creates a procedure named `hello` in the edition `ora$base`, and then creates the edition `e2` as a child of `ora$base`. When `e2` invokes `hello`, it invokes the inherited procedure in `ora$base`. Then `e2` changes `hello`, actualizing it. Now when `e2` invokes `hello`, it invokes its own actual procedure. The procedure `hello` in the edition `ora$base` remains unchanged.

Example 28-1 Editioned Objects and Copy-on-Change

1. Assume that this procedure is an editioned object in `ora$base`:
	```
	CREATE OR REPLACE PROCEDURE hello IS
	  BEGIN
	    DBMS_OUTPUT.PUT_LINE('Hello, edition 1.');
	  END hello;
	/
	```
2. In `ora$base`, invoke the procedure:
	```
	BEGIN hello(); END;
	/
	```
	Result:
	```
	Hello, edition 1.
	 
	PL/SQL procedure successfully completed.
	```
3. Create a child edition:
	```
	CREATE EDITION e2;
	```
	Conceptually, the procedure is copied to the child edition, and only the copy is visible in the child edition. The copy is an inherited object, not an actual object.
4. Use the child edition:
	```
	ALTER SESSION SET EDITION = e2;
	```
5. Invoke the procedure:
	```
	BEGIN hello(); END;
	/
	```
	Conceptually, the child edition invokes its own copy of the procedure (which is identical to the procedure in the parent edition, `ora$base`). However, the child edition actually invokes the procedure in the parent edition. Result:
	```
	Hello, edition 1.
	 
	PL/SQL procedure successfully completed.
	```
6. Change the procedure:
	```
	CREATE OR REPLACE PROCEDURE hello IS
	  BEGIN
	    DBMS_OUTPUT.PUT_LINE('Hello, edition 2.');
	  END hello;
	/
	```
	Oracle Database actualizes the procedure in the child edition, and the change affects only the actual object in the child edition, not the procedure in the parent edition.
7. Invoke the procedure:
	```
	BEGIN hello(); END;
	/
	```
	The child edition invokes its own actual procedure:
	```
	Hello, edition 2.
	PL/SQL procedure successfully completed.
	```
8. Return to the parent edition:
	```
	ALTER SESSION SET EDITION = ora$base;
	```
9. Invoke the procedure and see that it has not changed:
	```
	BEGIN hello(); END;
	/
	```
	Result:
	```
	Hello, edition 1.
	 
	PL/SQL procedure successfully completed.
	```

See Also:

Changing Your Session Edition for information about `ALTER SESSION SET EDITION`

##### 28.2.3.2 Example: Dropping an Editioned Object

Example 28-2 creates a procedure named `goodbye` in the edition `ora$base`, and then creates edition `e2` as a child of `ora$base`. After `e2` drops `goodbye`, it can no longer invoke it, but `ora$base` can still invoke it.

Because `e2` dropped the procedure `goodbye`:

- Its descendents do not inherit the procedure `goodbye`.
- No object named `goodbye` is visible in `e2`, so `e2` can create an object named `goodbye`, but it must be an editioned object. If `e2` creates a new editioned object named `goodbye`, then the descendents of `e2` inherit that object.

Example 28-2 Dropping an Editioned Object

1. Assume that this procedure is an editioned object in `ora$base`:
	```
	CREATE OR REPLACE PROCEDURE goodbye IS
	  BEGIN
	    DBMS_OUTPUT.PUT_LINE('Good-bye!');
	  END goodbye;
	/
	```
2. Invoke the procedure:
	```
	BEGIN goodbye; END;
	/
	```
	Result:
	```
	Good-bye!
	 
	PL/SQL procedure successfully completed.
	```
3. Create edition `e2` as a child of `ora$base`:
	```
	CREATE EDITION e2;
	```
	In `e2`, the procedure is an inherited object.
4. Use edition `e2`:
	```
	ALTER SESSION SET EDITION = e2;
	```
	`ALTER` `SESSION` `SET` `EDITION` must be a top-level SQL statement.
5. In `e2`, invoke the procedure:
	```
	BEGIN goodbye; END;
	/
	```
	`e2` invokes the procedure in `ora$base`:
	```
	Good-bye!
	 
	PL/SQL procedure successfully completed.
	```
6. In `e2`, drop the procedure:
	```
	DROP PROCEDURE goodbye;
	```
7. In `e2`, try to invoke the dropped procedure:
	```
	BEGIN goodbye; END;
	/
	```
	Result:
	```
	BEGIN goodbye; END;
	      *
	ERROR at line 1:
	ORA-06550: line 1, column 7:
	PLS-00201: identifier 'GOODBYE' must be declared
	ORA-06550: line 1, column 7:
	PL/SQL: Statement ignored
	```
8. Return to `ora$base`:
	```
	ALTER SESSION SET EDITION = ora$base;
	```
9. In `ora$base`, invoke the procedure:
	```
	BEGIN goodbye; END;
	/
	```
	Result:
	```
	Good-bye!
	 
	PL/SQL procedure successfully completed.
	```

See Also:

- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=LNPLS99991), for more information about the `DROP` `PROCEDURE` statement, including the privileges required to use it
- Creating New EDITIONABLE and NONEDITIONABLE Objects
- Changing Your Session Edition for more information about `ALTER SESSION SET EDITION`

##### 28.2.3.3 Example: Creating an Object with the Name of a Dropped Inherited Object

In Example 28-3, `e2` creates a function named `goodbye` and then an edition named `e3` as a child of `e2`. When `e3` tries to invoke the procedure `goodbye` (which `e2` dropped), an error occurs, but `e3` successfully invokes the function `goodbye` (which `e2` created).

Example 28-3 Creating an Object with the Name of a Dropped Inherited Object

1. Return to `e2`:
	```
	ALTER SESSION SET EDITION = e2;
	```
2. In `e2`, create a function named `goodbye`:
	```
	CREATE OR REPLACE FUNCTION goodbye
	  RETURN BOOLEAN
	IS
	BEGIN
	  RETURN(TRUE);
	END goodbye;
	/
	```
	This function must be an editioned object. It has the `EDITIONABLE` property by default. If the type `FUNCTION` is not editionable in the schema, then you must use the `ALTER` `USER` statement to make it editioned.
3. Create edition `e3`:
	```
	CREATE EDITION e3 AS CHILD OF e2;
	```
	Edition `e3` inherits the function `goodbye`.
4. Use edition `e3`:
	```
	ALTER SESSION SET EDITION = e3;
	```
5. In `e3`, try to invoke the procedure `goodbye`:
	```
	BEGIN
	  goodbye;
	END;
	/
	```
	Result:
	```
	ERROR at line 2:
	ORA-06550: line 2, column 3:
	PLS-00306: wrong number or types of arguments in call to 'GOODBYE'
	ORA-06550: line 2, column 3:
	PL/SQL: Statement ignored
	```
6. In `e3`, invoke function `goodbye`:
	```
	BEGIN
	  IF goodbye THEN
	    DBMS_OUTPUT.PUT_LINE('Good-bye!');
	  END IF;
	END;
	/
	```
	Result:
	```
	Good-bye!
	 
	PL/SQL procedure successfully completed.
	```

See Also:

- Changing Your Session Edition for information about `ALTER` `SESSION` `SET` `EDITION`
- Enabling Editions for a User for instructions to enable editions for a user

#### 28.2.4 Making an Edition Available to Some Users

As the creator of the edition, you automatically have the `USE` privilege `WITH` `GRANT` `OPTION` on it. To grant the `USE` privilege on the edition to other users, use the SQL statement `GRANT` `USE` `ON` `EDITION`.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF01603) for information about the `GRANT` statement

#### 28.2.5 Making an Edition Available to All Users

To make an edition available to all users, either:

- Grant the `USE` privilege on the edition to `PUBLIC`:
	```
	GRANT USE ON EDITION edition_name TO PUBLIC
	```
- Make the edition the database default edition:
	```
	ALTER DATABASE DEFAULT EDITION = edition_name
	```
	This has the side effect of allowing all users to use the edition, because it effectively grants the `USE` privilege on `edition_name` to `PUBLIC`.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF00802) for information about the `ALTER` `DATABASE` statement
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF01603) for information about the `GRANT` statement

#### 28.2.6 Current Edition and Session Edition

Each database session uses exactly one edition at a time. The edition that a database session is using at any one time is called its current edition. When a database session begins, its current edition is its session edition, which is the edition in which it begins. If you change the session edition, the current edition changes to the same thing. However, there are situations in which the current edition and session edition differ.

Topics:

##### 28.2.6.1 Your Initial Session Edition

When you connect to the database, you can specify your initial session edition. Your initial session edition can be the database default edition or any edition on which you have the `USE` privilege. To see the names of the editions that are available to you, use this query:

```
SELECT EDITION_NAME FROM ALL_EDITIONS;
```

How you specify your initial session edition at connection time depends on how you connect to the database—see the documentation for your interface.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ADMIN13170) for information about setting the database default edition
- [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQPUG013) for information about connecting to the database with SQL\*Plus
- [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=LNOCI08100) for information about connecting to the database with Oracle Call Interface (OCI)
- [Oracle Database JDBC Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=JJDBC-GUID-864DB502-5E50-4044-8132-33D6AAF8927A) for information about connecting to the database with JDBC

As of Oracle Database 11g Release 2 (11.2.0.2), if you do not specify your session edition at connection time, then:

- If you use a database service to connect to the database, and an initial session edition was specified for that service, then the initial session edition for the service is your initial session edition.
- Otherwise, your initial session edition is the database default edition.

As of Release 11.2.0.2, when you create or modify a database service, you can specify its initial session edition.

To create or modify a database service, Oracle recommends using the `srvctl` `add` `service` or `srvctl` `modify` `service` command. To specify the default initial session edition of the service, use the `-edition` option.

Alternatively, you can create or modify a database service with the `DBMS_SERVICE`.`CREATE_SERVICE` or `DBMS_SERVICE`.`MODIFY_SERVICE` procedure, and specify the default initial session edition of the service with the `EDITION` attribute.

Note:

As of Oracle Database 11g Release 2 (11.2.0.1), the `DBMS_SERVICE`.`CREATE_SERVICE` and `DBMS_SERVICE`.`MODIFY_SERVICE` procedures are deprecated in databases managed by Oracle Clusterware and Oracle Restart.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ADMIN12956) for information about the `-edition` option of the `srvctl` `add` `service` command
- [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ADMIN12980) for information about the `-edition` option of the `srvctl` `modify` `service` command
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ARPLS68021) for information about the `EDITION` attribute of the `DBMS_SERVICE`.`CREATE_SERVICE` procedure
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ARPLS68027) for information about the `EDITION` attribute of the `DBMS_SERVICE`.`MODIFY_SERVICE` procedure

##### 28.2.6.2 Changing Your Session Edition

After connecting to the database, you can change your session edition with the SQL statement `ALTER` `SESSION` `SET` `EDITION`. You can change your session edition to the database default edition or any edition on which you have the `USE` privilege. When you change your session edition, your current edition changes to that same edition.

These statements from Example: Editioned Objects and Copy-on-Change and Example: Dropping an Editioned Object change the session edition (and current edition) first to `e2` and later to `ora$base`:

```
ALTER SESSION SET EDITION = e2
...
ALTER SESSION SET EDITION = ora$base
```

Note:

`ALTER` `SESSION` `SET` `EDITION` must be a top-level SQL statement. To defer an edition change (in a logon trigger, for example), use the `DBMS_SESSION`.`SET_EDITION_DEFERRED` procedure.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF00901) for more information about the `ALTER` `SESSION` `SET` `EDITION` statement
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ARPLS72968) for more information about the `DBMS_SESSION`.`SET_EDITION_DEFERRED` procedure

##### 28.2.6.3 Displaying the Names of the Current and Session Editions

This statement returns the name of the current edition:

```
SELECT SYS_CONTEXT('USERENV', 'CURRENT_EDITION_NAME') FROM DUAL;
```

This statement returns the name of the session edition:

```
SELECT SYS_CONTEXT('USERENV', 'SESSION_EDITION_NAME') FROM DUAL;
```

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF06117) for more information about the `SYS_CONTEXT` function

##### 28.2.6.4 When the Current Edition Might Differ from the Session Edition

The current edition might differ from the session edition in these situations:

- A crossedition trigger fires.
- You run a statement by calling the `DBMS_SQL`.`PARSE` procedure, specifying the edition in which the statement is to run, as in Example 28-4.
	While the statement is running, the current edition is the specified edition, but the session edition does not change.

Example 28-4 creates a function that returns the names of the session edition and current edition. Then it creates a child edition, which invokes the function twice. The first time, the session edition and current edition are the same. The second time, they are not, because a different edition is passed as a parameter to the `DBMS_SQL`.`PARSE` procedure.

Example 28-4 Current Edition Differs from Session Edition

1. Create function that returns the names of the session edition and current edition:
	```
	CREATE OR REPLACE FUNCTION session_and_current_editions
	  RETURN VARCHAR2
	IS
	BEGIN
	  RETURN
	  'Session: '|| SYS_CONTEXT('USERENV', 'SESSION_EDITION_NAME') ||
	  ' / ' ||
	  'Current: '|| SYS_CONTEXT('USERENV', 'CURRENT_EDITION_NAME');
	END session_and_current_editions;
	/
	```
2. Create child edition:
	```
	CREATE EDITION e2 AS CHILD OF ora$base;
	```
3. Use child edition:
	```
	ALTER SESSION SET EDITION = e2;
	```
4. Invoke function:
	```
	BEGIN
	  DBMS_OUTPUT.PUT_LINE (session_and_current_editions());
	END;
	/
	```
	Result:
	```
	Session: E2 / Current: E2
	 
	PL/SQL procedure successfully completed.
	```
5. Invoke function again:
	```
	DECLARE
	  c     NUMBER := DBMS_SQL.OPEN_CURSOR();
	  v     VARCHAR2(200);
	  dummy NUMBER;
	  stmt  CONSTANT VARCHAR2(32767)
	    := 'SELECT session_and_current_editions() FROM DUAL';
	BEGIN
	  DBMS_SQL.PARSE (c => c,
	                  statement => stmt,
	                  language_flag => DBMS_SQL.NATIVE,
	                  edition => 'ora$base');
	 
	  DBMS_SQL.DEFINE_COLUMN (c, 1, v, 200);
	  dummy := DBMS_SQL.EXECUTE_AND_FETCH (c, true);
	  DBMS_SQL.COLUMN_VALUE (c, 1, v);
	  DBMS_SQL.CLOSE_CURSOR(c);
	  DBMS_OUTPUT.PUT_LINE (v);
	END;
	/
	```
	Result:
	```
	Session: E2 / Current: ORA$BASE
	 
	PL/SQL procedure successfully completed.
	```

See Also:

- Crossedition Trigger Interaction with Editions
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ARPLS68277) for information about the `DBMS_SQL`.`PARSE` procedure

#### 28.2.7 Retiring an Edition

After making a new edition (an upgraded application) available to all users, retire the old edition (the original application), so that no user except `SYS` can use the old edition.

Note:

If the old edition is the database default edition, make another edition the database default edition before you retire the old edition:

```
ALTER DATABASE DEFAULT EDITION = edition_name
```

To retire an edition, you must revoke the `USE` privilege on the edition from every grantee. To list the grantees, use this query, where:`e` is a placeholder for the name of the edition to be dropped:

```
SELECT GRANTEE, PRIVILEGE
FROM DBA_TAB_PRIVS
WHERE TABLE_NAME = :e AND TYPE = 'EDITION'
/
```

When you retire an edition, update the evaluation editions and unusable editions of noneditioned objects accordingly.

See Also:

- Noneditioned Objects That Can Depend on Editioned Objects for information about changing evaluation editions and unused editions
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF01609) for information about the `REVOKE` statement
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF00802) for information about the `ALTER` `DATABASE` statement

#### 28.2.8 Dropping an Edition

Note:

If the edition includes crossedition triggers, see Dropping the Crossedition Triggers, before you drop the edition.

To drop an edition, use the `DROP` `EDITION` statement. If the edition has actual objects, you must specify the `CASCADE` clause, which drops the actual objects.

If a `DROP` `EDITION` `edition` `CASCADE` statement is interrupted before finishing normally (from a power failure, for example), the static data dictionary view `*_EDITIONS` shows that the value of `USABLE` for `edition` is `NO`. The only operation that you can perform on such an unusable `edition` is `DROP` `EDITION` `CASCADE`.

You drop an edition in these situations:

- You want to roll back the application upgrade.
- (Optional) You have retired the edition.

You can drop an edition only if all of these statements are true:

- The edition is either the root edition or a leaf edition.
- The edition is not in use. (That is, it is not the current edition or session edition of a session.)
- The edition is not the database default edition.

If the edition is the root, and the `COMPATIBLE` parameter is set to 12.2.0 or higher, the edition is marked as unusable. A covered object is an editioned object that is no longer inherited in any usable descendent edition. Each covered object in any unusable edition is dropped by an automated scheduled maintenance process. After there is no object left in the root unusable edition, the edition itself is dropped automatically. This cleanup process is repeated for each unusable root edition found. A user can run this process on demand by manually executing the `DBMS_EDITIONS_UTILITIES`.`CLEAN_UNUSABLE_EDITIONS` procedure (see [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ARPLS-GUID-40AD8944-D7E0-4ACA-9A05-3DC502F47D27)).

If the `COMPATIBLE` is set to 12.1.0 or lower, the root edition must have no objects that its descendents inherit. Each object inherited from the root edition must either be actualized or dropped explicitly before the edition can be dropped.

If the edition is the leaf, every editioned object in the leaf is dropped, followed by the edition itself before the statement finishes execution.

Note:

After you have dropped an edition, you cannot recompile a noneditioned object that depends on an editioned object if both of the following are true:

- The noneditioned object contains an ADT.
- The noneditioned object was invalidated when the owner of the editioned object on which it depends was enabled for editions using `FORCE`.

To explicitly actualize an inherited object in the child edition:

1. Make the child edition your session edition.
	For instructions, see Changing Your Session Edition.
2. Recompile the object, using the appropriate `ALTER` statement with `COMPILE`. For a PL/SQL object, also specify `REUSE` `SETTINGS`.
	For example, this statement actualizes the procedure `p1`:
	```
	ALTER PROCEDURE p1 COMPILE REUSE SETTINGS
	```

When you drop an edition, update the evaluation editions and unusable editions of noneditioned objects accordingly.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF00818) for information about the `ALTER` `LIBRARY` statement
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF01104) for information about the `ALTER` `VIEW` statement
- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=LNPLS99999) for information about the `ALTER` `FUNCTION` statement
- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=LNPLS99998) for information about the `ALTER` `PACKAGE` statement
- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=LNPLS99997) for information about the `ALTER` `PROCEDURE` statement
- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=LNPLS99996) for information about the `ALTER` `TRIGGER` statement
- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=LNPLS99995) for information about the `ALTER` `TYPE` statement
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF20019) for more information about the `DROP` `EDITION` statement
- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=LNPLS99974) for information about the `ALTER` statements for PL/SQL objects
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF008) for information about the `ALTER` statements for SQL objects.
- Noneditioned Objects That Can Depend on Editioned Objects for information about changing evaluation editions and unused editions

### 28.3 Editions and Audit Policies

Audit policies configured on an object in an edition is applied across all the editions of the object. Existing audit policies are extended to the objects in newly created editions.

Auditing is the monitoring and recording of configured database actions from both database users and application users, who are recognized in the database using the `CLIENT_IDENTIFIER` attribute. You can audit SQL statements, security-relevant activities and also fine-grained activities.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=DBSEG-GUID-C8DF47D5-4E31-4715-AFBA-EC3BE294EC37#GUID-C8DF47D5-4E31-4715-AFBA-EC3BE294EC37) for information on audit policies.

### 28.4 Editioning Views

On a noneditioning view, the only type of trigger that you can define is an `INSTEAD` `OF` trigger. On an editioning view, you can define every type of trigger that you can define on a table (except crossedition triggers, which are temporary, and `INSTEAD` `OF` triggers). Therefore, and because they can be editioned, editioning views let you treat their base tables as if the base tables were editioned. However, you cannot add indexes or constraints to an editioning view; if your upgraded application requires new indexes or constraints, you must add them to the base table.

Note:

If you will change a base table or an index on a base table, then see " [Nonblocking and Blocking DDL Statements](sql-processing-for-application-developers.md)."

An editioning view selects a subset of the columns from a single base table and, optionally, provides aliases for them. In providing aliases, the editioning view maps physical column names (used by the base table) to logical column names (used by the application). An editioning view is like an API for a table.

There is no performance penalty for accessing a table through an editioning view, rather than directly. That is, if a SQL `SELECT`, `INSERT`, `UPDATE`, `DELETE`, or `MERGE` statement uses one or more editioning views, one or more times, and you replace each editioning view name with the name of its base table and adjust the column names if necessary, performance does not change.

The static data dictionary view `*_EDITIONING_VIEWS` describes every editioning view in the database that is visible in the session edition. `*_EDITIONING_VIEWS_AE` describes every actual object in every editioning view in the database, in every edition.

Topics:

- Creating an Editioning View
- Partition-Extended Editioning View Names
- Changing the Writability of an Editioning View
- Replacing an Editioning View
- Dropped or Renamed Base Tables
- Adding Indexes and Constraints to the Base Table
- SQL Optimizer Index Hints

See Also:

Oracle Database Reference for more information about the static data dictionary views [`*_EDITIONING_VIEWS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN20668) and [`*_EDITIONING_VIEWS_AE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN20683).

#### 28.4.1 Creating an Editioning View

Before an editioning view is created, its owner must be editions-enabled and the schema object type `VIEW` must be editionable in its owner.

To create an editioning view, use the SQL statement `CREATE` `VIEW` with the keyword `EDITIONING`. To make the editioning view read-only, specify `WITH` `READ` `ONLY`; to make it read-write, omit `WITH` `READ` `ONLY`. Do not specify `NONEDITIONABLE`, or an error occurs.

If an editioning view is read-only, users of the unchanged application can see the data in the base table, but cannot change it. The base table has semi-availability. Semi-availability is acceptable for applications such as online dictionaries, which users read but do not change. Make the editioning view read-only if you do not define crossedition triggers on the base table.

If an editioning view is read-write, users of the unchanged application can both see and change the data in the base table. The base table has maximum availability. Maximum availability is required for applications such as online stores, where users submit purchase orders. If you define crossedition triggers on the base table, make the editioning view read-write.

Because an editioning view must do no more than select a subset of the columns from the base table and provide aliases for them, the `CREATE` `VIEW` statement that creates an editioning view has restrictions. Violating the restrictions causes the creation of the view to fail, even if you specify `FORCE`.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF01504) for more information about using the `CREATE` `VIEW` statement to create editioning views, including the restrictions
- Enabling Editions for a User

#### 28.4.2 Partition-Extended Editioning View Names

An editioning view defined on a partitioned table can have a partition-extended name, with partition and subpartition names that refer to the partitions and subpartitions of the base table.

The data manipulation language (DML) statements that support partition-extended table names also support partition-extended editioning view names. These statements are:

- `DELETE`
- `INSERT`
- `SELECT`
- `UPDATE`

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF00223) for information about referring to partitioned tables

#### 28.4.3 Changing the Writability of an Editioning View

To change an existing editioning view from read-only to read-write, use the SQL statement `ALTER` `VIEW` `READ` `WRITE`. To change an existing editioning view from read-write to read-only, use the SQL statement `ALTER` `VIEW` `READ` `ONLY`.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF01104) for more information about the `ALTER` `VIEW` statement

#### 28.4.4 Replacing an Editioning View

To replace an editioning view, use the SQL statement `CREATE` `VIEW` with the `OR` `REPLACE` clause and the keyword `EDITIONING`.

You can replace an editioning view only with another editioning view. Any triggers defined on the replaced editioning view are retained.

#### 28.4.5 Dropped or Renamed Base Tables

If you drop or rename the base table on which an editioning view is defined, the editioning view is not dropped, but the editioning view and its dependents become invalid. However, any triggers defined on the editioning view remain.

#### 28.4.6 Adding Indexes and Constraints to the Base Table

If your upgraded application requires new indexes or constraints, you must add them to the base table. You cannot add them to the editioning view.

If the new indexes might negatively impact the old edition (the original application), make them invisible. In the crossedition triggers that must use the new indexes, specify them in `INDEX` hints.

When all users are using only the upgraded application:

- If the new indexes were used only by the crossedition triggers, drop them.
- If the new indexes are helpful in the upgraded application, make them visible.

See Also:

- [Guidelines for Managing Indexes](indexes.md)
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF50405) for information about `INDEX` hints
- SQL Optimizer Index Hints

#### 28.4.7 SQL Optimizer Index Hints

SQL optimizer index hints are specified in terms of the logical names of the columns participating in the index. Any SQL optimizer index hints specified on an editioning view using logical column names must be mapped to an index on the corresponding physical column in the base table.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF00219) for information about using hints

### 28.5 Crossedition Triggers

The most important difference between crossedition triggers and noncrossedition triggers is how they interact with editions. A crossedition trigger is visible only in the edition in which it is actual, never in a descendent edition. Forward crossedition triggers move data from columns used by the old edition to columns used by the new edition; reverse crossedition triggers do the reverse.

Other important differences are:

- Crossedition triggers can be ordered with triggers defined on other tables, while noncrossedition triggers can be ordered only with other triggers defined on the same table.
- Crossedition triggers are temporary—you drop them after you have made the restructured tables available to all users.

Topics:

- Forward Crossedition Triggers
- Reverse Crossedition Triggers
- Crossedition Trigger Interaction with Editions
- Creating a Crossedition Trigger
- Transforming Data from Pre- to Post-Upgrade Representation
- Dropping the Crossedition Triggers

See Also:

[Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=LNPLS020) for general information about triggers

#### 28.5.1 Forward Crossedition Triggers

The DML changes that you make to the table in the post-upgrade edition are written only to new columns or new tables, never to columns that users of pre-upgrade (ancestor) editions might be reading or writing. However, if the user of an ancestor edition changes the table data, the editioning view that you see must accurately reflect these changes. This is accomplished with forward crossedition triggers.

A forward crossedition trigger defines a transform, which is a rule for transforming an old row to one or more new rows. An old row is a row of data in the pre-upgrade representation. A new row is a row of data in the post-upgrade representation. The name of the trigger refers to the trigger itself and to the transform that the trigger defines.

#### 28.5.2 Reverse Crossedition Triggers

If the pre- and post-upgrade editions will be in ordinary use at the same time (hot rollover), use reverse crossedition triggers to ensure that when users of the post-upgrade edition make changes to the table data, the changes are accurately reflected in the pre-upgrade editions.

#### 28.5.3 Crossedition Trigger Interaction with Editions

The most important difference between crossedition triggers and noncrossedition triggers is how they interact with editions.

In this topic, the current edition is the edition in which the triggering DML statement runs. The current edition might differ from the session edition.

Topics:

##### 28.5.3.1 Which Triggers Are Visible

Editions inherit noncrossedition triggers in the same way that they inherit other editioned objects (see Editioned Objects and Copy-on-Change).

Editions do not inherit crossedition triggers. A crossedition trigger might fire in response to a DML statement that another edition runs, but its name is visible only in the edition in which it was created. Therefore, an edition can reuse the name of a crossedition trigger created in an ancestor edition. Reusing the name of a crossedition trigger does not change the conditions under which the older trigger fires.

Crossedition triggers that appear in static data dictionary views are actual objects in the current edition.

##### 28.5.3.2 What Kind of Triggers Can Fire

What kind of triggers can fire depends on the category of the triggering DML statement.

Categories:

- Forward Crossedition Trigger SQL
- Reverse Crossedition Trigger SQL
- Application SQL

Note:

The `APPEND` hint on a SQL `INSERT` statement does not prevent crossedition triggers from firing.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF50901) for information about the `APPEND` hint

###### 28.5.3.2.1 Forward Crossedition Trigger SQL

Forward crossedition trigger SQL is SQL that is executed in either of these ways:

- Directly from the body of a forward crossedition trigger
	This category includes SQL in an invoked subprogram only if the subprogram is local to the forward crossedition trigger.
- By invoking the `DBMS_SQL`.`PARSE` procedure with a non- `NULL` value for the `apply_crossedition_trigger` parameter
	The only valid non- `NULL` value for the `apply_crossedition_trigger` parameter is the unqualified name of a forward crossedition trigger.

If a forward crossedition trigger invokes a subprogram in another compilation unit, the SQL in the subprogram is forward crossedition trigger SQL only if it is invoked by the `DBMS_SQL`.`PARSE` procedure with a non- `NULL` value for the `apply_crossedition_trigger` parameter.

Forward crossedition trigger SQL can fire only triggers that satisfy all of these conditions:

- They are forward crossedition triggers.
- They were created either in the current edition or in a descendent of the current edition.
- They explicitly follow the running forward crossedition trigger.

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ARPLS058) for more information about the `DBMS_SQL`.`PARSE` procedure

###### 28.5.3.2.2 Reverse Crossedition Trigger SQL

Reverse crossedition trigger SQL is SQL that is executed directly from the body of a reverse crossedition trigger. This category includes SQL in an invoked subprogram only if the subprogram is local to the reverse crossedition trigger.

Reverse crossedition trigger SQL can fire only triggers that satisfy all of these conditions:

- They are reverse crossedition triggers.
- They were created either in the current edition or in an ancestor of the current edition.
- They explicitly precede the running reverse crossedition trigger.

###### 28.5.3.2.3 Application SQL

Application SQL is all SQL except crossedition trigger SQL, including these DML statements:

- Dynamic SQL DML statements coded with the `DBMS_SQL` package.
- DML statements executed by Java stored procedures and external procedures (even when these procedures are invoked by `CALL` triggers)

Application SQL fires both noncrossedition and crossedition triggers, according to these rules:

| Kind of Trigger | Conditions Under Which Trigger Can Fire |
| --- | --- |
| Noncrossedition | Trigger is both visible and enabled in the current edition. |
| Forward crossedition | Trigger was created in a descendent of the current edition. |
| Reverse crossedition | Trigger was created either in the current edition or in an ancestor of the current edition. |

See Also:

[Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=LNPLS01108) for information about `DBMS_SQL` package

##### 28.5.3.3 Firing Order

For a trigger to fire in response to a specific DML statement, the trigger must:

- Be the right kind
- Satisfy the selection criteria (for example, the type of DML statement and the `WHEN` clause)
- Be enabled

For the triggers that meet these requirements, firing order depends on the `FOLLOWS` and `PRECEDES` clauses, the trigger type, and the edition.

Topics:

- FOLLOWS and PRECEDES Clauses
- Trigger Type and Edition

See Also:

- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=LNPLS99985) for general information about trigger firing order
- What Kind of Triggers Can Fire

###### 28.5.3.3.1 FOLLOWS and PRECEDES Clauses

When triggers A and B are to be fired at the same timing point, A fires before B fires if either of these is true:

- A explicitly precedes B.
- B explicitly follows A.

This rule is independent of conditions such as:

- Whether the triggers are enabled or disabled
- Whether the columns specified in the `UPDATE` `OF` clause are modified
- Whether the `WHEN` clauses are satisfied
- Whether the triggers are associated with the same kinds of DML statements (`INSERT`, `UPDATE`, or `DELETE`)
- Whether the triggers have overlapping timing points

The firing order of triggers that do not explicitly follow or precede each other is unpredictable.

###### 28.5.3.3.2 Trigger Type and Edition

For each timing point associated with a triggering DML statement, eligible triggers fire in this order. In categories [^1] through [^2], `FOLLOWS` relationships apply; in categories [^3] and [^4], `PRECEDES` relationships apply.

1. Noncrossedition triggers
2. Forward crossedition triggers created in the current edition
3. Forward crossedition triggers created in descendents of the current edition, in the order that the descendents were created (child, grandchild, and so on)
4. Reverse crossedition triggers created in the current edition
5. Reverse crossedition triggers created in the ancestors of the current edition, in the reverse order that the ancestors were created (parent, grandparent, and so on)

##### 28.5.3.4 Crossedition Trigger Execution

A crossedition trigger runs using the edition in which it was created. Any code that the crossedition trigger calls (including package references, PL/SQL subprogram calls, and SQL statements) also runs in the edition in which the crossedition trigger was created.

If a PL/SQL package is actual in multiple editions, then the package variables and other state are private in each edition, even within a single session. Because each crossedition trigger and the code that it calls run using the edition in which the crossedition trigger was created, the same session can instantiate two or more versions of the package, with the same name.

#### 28.5.4 Creating a Crossedition Trigger

Before a crossedition trigger is created, its owner must be editions-enabled and the schema object type `TRIGGER` must be editionable in its owner. (For instructions, see Enabling Editions for a User.)

Create a crossedition trigger with the SQL statement `CREATE` `TRIGGER`, observing these rules:

- A crossedition trigger must be defined on a table, not a view.
- A crossedition trigger must have the `EDITIONABLE` property.
- A crossedition trigger must be a DML trigger (simple or compound).
	The DML statement in a crossedition trigger body can be either a static SQL statement or a native dynamic SQL statement.
- A crossedition trigger is forward unless you specify `REVERSE`. (Specifying `FORWARD` is optional.)
- The `FOLLOWS` clause is allowed only when creating a forward crossedition trigger or a noncrossedition trigger. (The `FOLLOWS` clause indicates that the trigger being created is to fire after the specified triggers fire.)
- The `PRECEDES` clause is allowed only when creating a reverse crossedition trigger. (The `PRECEDES` clause indicates that the trigger being created is to fire before the specified triggers fire.)
- The triggers specified in the `FOLLOWS` or `PRECEDES` clause must exist, but need not be enabled or successfully compiled.
- Like a noncrossedition trigger, a crossedition trigger is created in the enabled state unless you specify `DISABLE`. (Specifying `ENABLE` is optional.)
	Tip:
	Create crossedition triggers in the disabled state, and enable them after you are sure that they compile successfully. If you create them in the enabled state, and they fail to compile, the failure affects users of the existing application.
- The operation in a crossedition trigger body must be idempotent (that is, performing the operation multiple times is redundant; it does not change the result).

See Also:

- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=LNPLS01374) for more information about using the `CREATE` `TRIGGER` statement to create crossedition triggers
- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=LNPLS00601) for more information about Static SQL
- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=LNPLS01102) for more information about native dynamic SQL

##### 28.5.4.1 Coding the Forward Crossedition Trigger Body

The operation in the body of a forward crossedition trigger must be idempotent, because it is impossible to predict:

- The context in which the body will first run for an old row.
	The possibilities are:
	- When a user of an ancestor edition runs a DML statement that fires the trigger (a serendipitous change)
		- When you apply the transform that the trigger defines (do a bulk upgrade of rows from old format to new format)
- How many times the body will run for each old row.

Topics:

- Handling Data Transformation Collisions
- Handling Changes to Other Tables

See Also:

Transforming Data from Pre- to Post-Upgrade Representation for information about applying transforms

###### 28.5.4.1.1 Handling Data Transformation Collisions

If a forward crossedition trigger populates a new table (rather than new columns of a table), its body must handle data transformation collisions.

For example, suppose that a column of the new table has a `UNIQUE` constraint. A serendipitous change fires the forward crossedition trigger, which inserts a row in the new table. Later, another serendipitous change fires the forward crossedition trigger, or you apply the transform defined by the trigger. The trigger tries to insert a row in the new table, violating the `UNIQUE` constraint.

If your collision-handling strategy depends on why the trigger is running, you can determine the reason with the function `APPLYING_CROSSEDITION_TRIGGER`. When called directly from a trigger body, this function returns the `BOOLEAN` value `TRUE` if the trigger is running because of a serendipitous change and `FALSE` if the trigger is running because you are applying the transform in bulk. (`APPLYING_CROSSEDITION_TRIGGER` is defined in the package `DBMS_STANDARD`. It has no parameters.)

To ignore collisions and insert the rows that do not collide with existing rows, put the `IGNORE_ROW_ON_DUPKEY_INDEX` hint in the `INSERT` statement.

If you do not want to ignore such collisions, but want to know where they occur so that you can handle them, put the `CHANGE_DUPKEY_ERROR_INDEX` hint in the `INSERT` or `UPDATE` statement, specifying either an index or set of columns. Then, when a unique key violation occurs for that index or set of columns, ORA-38911 is reported instead of ORA-00001. You can write an exception handler for ORA-38911.

Note:

Although they have the syntax of hints, `IGNORE_ROW_ON_DUPKEY_INDEX` and `CHANGE_DUPKEY_ERROR_INDEX` are mandates. The optimizer always uses them.

Example 28-5 creates a crossedition trigger that uses the `APPLYING_CROSSEDITION_TRIGGER` function and the `IGNORE_ROW_ON_DUPKEY_INDEX` and `CHANGE_DUPKEY_ERROR_INDEX` hints to handle data transformation collisions. The trigger transforms old rows in `table1` to new rows in `table2`. The tables were created as follows:

```
CREATE TABLE table1 (key NUMBER, value VARCHAR2(20));

CREATE TABLE table2 (key NUMBER, value VARCHAR2(20), last_updated TIMESTAMP);
CREATE UNIQUE INDEX i2 on table2(key);
```

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF30052) for more information about `IGNORE_ROW_ON_DUPKEY_INDEX`
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF30053) for more information about `CHANGE_DUPKEY_ERROR_INDEX`
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF00219) for general information about hints

Example 28-5 Crossedition Trigger that Handles Data Transformation Collisions

```
CREATE OR REPLACE TRIGGER trigger1
  BEFORE INSERT OR UPDATE ON table1
  FOR EACH ROW
  CROSSEDITION
DECLARE
  row_already_present  EXCEPTION;
  PRAGMA EXCEPTION_INIT(row_already_present, -38911);
BEGIN
  IF APPLYING_CROSSEDITION_TRIGGER THEN
    /* The trigger is running because of applying the transform.
       If the old edition of the app has already caused this trigger
          to insert a row, we do not modify the row as part of applying
          the transform. Therefore, insert the new row into table2 only if
          it is not already there. */
    INSERT /*+ IGNORE_ROW_ON_DUPKEY_INDEX(table2(key)) */
    INTO table2
    VALUES(:new.key, :new.value, to_date('1900-01-01', 'YYYY-MM-DD'));
  ELSE
     /* The trigger is running because of a serendipitous change.
          If no previous run of the trigger has already inserted
          the corresponding row into table2, insert the new row;
          otherwise, update the previously inserted row. */
    BEGIN
      INSERT /*+ CHANGE_DUPKEY_ERROR_INDEX(table2(key)) */
      INTO table2
      VALUES(:new.key, :new.value, SYSTIMESTAMP);
    EXCEPTION WHEN row_already_present THEN
      UPDATE table2
      SET value = :new.value, last_updated = SYSTIMESTAMP
      WHERE key = :new.key;
    END;
  END IF;
END;
/
```

###### 28.5.4.1.2 Handling Changes to Other Tables

If the body of a forward crossedition trigger includes explicit SQL statements that change tables other than the one on which the trigger is defined, and if the rows of those tables do not have a one-to-one correspondence with the rows of the table on which the trigger is defined, then the body code must implement a locking mechanism that correctly handles these situations:

- Two or more users of ancestor editions simultaneously issue DML statements for the table on which the trigger is defined.
- At least one user of an ancestor edition issues a DML statement for the table on which the trigger is defined.

#### 28.5.5 Transforming Data from Pre- to Post-Upgrade Representation

After redefining the database objects that comprise the application that you are upgrading (in the new edition), you must transform the application data from its pre-upgrade representation (in the old edition) to its post-upgrade representation (in the new edition). The rules for this transformation are called transforms, and they are defined by forward crossedition triggers.

Some old rows might have been transformed to new rows by serendipitous changes; that is, by changes that users of the pre-upgrade application made, which fired forward crossedition triggers. However, any rows that were not transformed by serendipitous changes are still in their pre-upgrade representation. To ensure that all old rows are transformed to new rows, you must apply the transforms that you defined on the tables that store the application data.

There are three ways to apply a transform:

- Fire the trigger that defines the transform on every row of the table, one row at a time.
- Instead of firing the trigger, run a SQL statement that does what the trigger would do, but faster, and then fire any triggers that follow that trigger.
	This second way is recommended over the first way if you have replaced an entire table or created a new table.
- Invoke the procedure `DBMS_EDITIONS_UTILITIES`.`SET_NULL_COLUMN_VALUES_TO_EXPR` to use a metadata operation to apply the transform to the new column.
	This third way has the fastest installation time, but there are restrictions on the expression that represents the transform, and queries of the new column are slower until the metadata is replaced by actual data.
	Metadata is replaced by actual data:
	- In an individual column element that is updated.
		- In every element of a column whose table is "compacted" using online table redefinition.
	.

For the first two ways of applying the transform, invoke either the `DBMS_SQL`.`PARSE` procedure or the subprograms in the `DBMS_PARALLEL_EXECUTE` package. The latter is recommended if you have a lot of data. The subprograms enable you to incrementally update the data in a large table in parallel, in two high-level steps:

1. Group sets of rows in the table into smaller chunks.
2. Apply the desired `UPDATE` statement to the chunks in parallel, committing each time you have finished processing a chunk.

The advantages are:

- You lock only one set of rows at a time, for a relatively short time, instead of locking the entire table.
- You do not lose work that has been done if something fails before the entire operation finishes.

For both the `DBMS_SQL`.`PARSE` procedure and the `DBMS_PARALLEL_EXECUTE` subprograms, the actual parameter values for `apply_crossedition_trigger`, `fire_apply_trigger`, and `sql_stmt` are the same:

- For `apply_crossedition_trigger`, specify the name of the forward crossedition trigger that defines the transform to be applied.
- To fire the trigger on every row of the table, one row at a time:
	- For the value of `fire_apply_trigger`, specify `TRUE`.
		- For `sql_stmt`, supply a SQL statement whose only significant effect is to select the forward crossedition trigger to be fired; for example, an `UPDATE` statement that sets some column to its own existing value in each row.
- To run a SQL statement that does what the trigger would do, and then fire any triggers that follow that trigger:
	- For the value of `fire_apply_trigger`, specify `FALSE`.
		- For `sql_stmt`, supply a SQL statement that does what the forward crossedition trigger would do, but faster—for example, a PL/SQL anonymous block that calls one or more PL/SQL subprograms.

See Also:

- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ARPLS058) for more information about the `DBMS_SQL`.`PARSE` procedure
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ARPLS233) for more information about the `DBMS_PARALLEL_EXECUTE` package
- Forward Crossedition Triggers for information about forward crossedition triggers
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ARPLS73756) for more information about `DBMS_EDITIONS_UTILITIES`.`SET_NULL_COLUMN_VALUES_TO_EXPR` procedure

##### 28.5.5.1 Preventing Lost Updates

To prevent lost updates when applying a transform, use this procedure:

1. Enable crossedition triggers.
2. Wait until pending changes to the affected tables are either committed or rolled back.
	Use the `DBMS_UTILITY`.`WAIT_ON_PENDING_DML` procedure.
3. Apply the transform.

Note:

This scenario, where the forward crossedition trigger changes only the table on which it is defined, is sufficient to illustrate the risk. Suppose that Session One issues an `UPDATE` statement against the table when the crossedition trigger is not yet enabled; and that Session Two then enables the crossedition trigger and immediately applies the transformation.

A race condition can now occur when both Session One and Session Two will change the same row (row n). Chance determines which session reaches row n first. Both updates succeed, even if the session that reaches row n second must wait until the session that reached it first commits its change and releases its lock.

The problem occurs when Session Two wins the race. Because its SQL statement was compiled after the trigger was enabled, the program that implements the statement also implements the trigger action; therefore, the intended post-upgrade column values are set for row n. Now Session One reaches row n, and because its SQL statement was compiled before the trigger was enabled, the program that implements the statement does not implement the trigger action. Therefore, the values that Session Two set in the post-upgrade columns do not change—they reflect the values that the source columns had before Session One updated row n. That is, the intended side-effect of Session One's update is lost.

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ARPLS73275) for more information about `DBMS_UTILITY`.`WAIT_ON_PENDING_DML` procedure

#### 28.5.6 Dropping the Crossedition Triggers

To drop a crossedition trigger, use the `DROP` `TRIGGER` statement. Alternatively, you can drop crossedition triggers by dropping the edition in which they are actual, by using the `DROP` `EDITION` statement with the `CASCADE` clause.

You drop crossedition triggers in these situations:

- You are rolling back the application upgrade (dropping the post-upgrade edition).
	Before dropping the post-upgrade edition, you must disable or drop any constraints on the new columns.
- You have finished the application upgrade and made the post-upgrade edition available to all users.
	When all sessions are using the post-upgrade edition, you can drop the forward crossedition triggers. However, before dropping the reverse crossedition triggers, you must disable or drop any constraints on the old columns.

To disable or drop constraints, use the `ALTER` `TABLE` statement with the `DISABLE` `CONSTRAINT` or `DROP` `CONSTRAINT` clause..

See Also:

- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=LNPLS99990) for more information about `DROP` `TRIGGER` statement
- Dropping an Edition for more information about dropping editions
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF01001) for more information about `ALTER` `TABLE` statement

### 28.6 Displaying Information About EBR Features

Topics:

- Displaying Information About Editions
- Displaying Information About Editioning Views
- Displaying Information About Crossedition Triggers

#### 28.6.1 Displaying Information About Editions

Table 28-1 briefly describes the static data dictionary views that display information about editions.

Table 28-1 \*\_ Dictionary Views with Edition Information

| View | Description |
| --- | --- |
| [`*_EDITIONS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN20634) | Describes every edition in the database. |
| [`*_EDITION_COMMENTS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN20635) | Shows the comments associated with every edition in the database. |
| [`*_EDITIONED_TYPES`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN23867) | Lists the schema object types that are editioned by default in each schema. |
| [`*_OBJECTS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN20146) | Describes every object in the database that is visible in the current edition. For each object, this view shows whether it is editionable. |
| [`*_OBJECTS_AE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN20578) | Describes every object in the database, in every edition. For each object, this view shows whether it is editionable. |
| [`*_ERRORS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN20065) | Describes every error in the database in the current edition. |
| [`*_ERRORS_AE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN20577) | Describes every error in the database, in every edition. |
| [`*_USERS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN20302) | Describes every user in the database. Useful for showing which users have editions enabled. |
| [`*_SERVICES`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN20465) | Describes every service in the database. The `EDITIONS` column shows the default initial current edition. |
| [`*_MVIEWS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN20139) | Describes every materialized view. If the materialized view refers to editioned objects, then this view shows the evaluation edition and the range of editions where the materialized view is eligible for query rewrite. |
| [`*_TAB_COLS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN20276) | Describes every column of every table, view, and cluster. For each virtual column, this view shows the evaluation edition and the usable range. |

Note:

`*_OBJECTS` and `*_OBJECTS_AE` include dependent objects that are invalidated by operations in [Table 27-2](schema-object-dependency.md) only after one of the following:

- A reference to the object (either during compilation or execution)
- An invocation of `DBMS_UTILITY`.`COMPILE_SCHEMA`
- An invocation of any `UTL_RECOMP` subprogram

See Also:

- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN002) for more information about a specific view
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ARPLS-GUID-A279BC5C-6CF5-4467-931D-0917C984DAB2) for more information about `DBMS_UTILITY`.`COMPILE_SCHEMA` procedure
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ARPLS380) for more information about `UTL_RECOMP` subprogram

#### 28.6.2 Displaying Information About Editioning Views

Table 28-2 briefly describes the static data dictionary views that display information about editioning views.

Table 28-2 \*\_ Dictionary Views with Editioning View Information

| View | Description |
| --- | --- |
| [`*_VIEWS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN20305) | Describes every view in the database that is visible in the current edition, including editioning views. |
| [`*_EDITIONING_VIEWS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN20668) | Describes every editioning view in the database that is visible in the current edition. Useful for showing relationships between editioning views and their base tables. Join with \*\_OBJECTS\_AE for additional information. |
| [`*_EDITIONING_VIEWS_AE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN20681) | Describes every actual object in every editioning view in the database, in every edition. |
| [`*_EDITIONING_VIEW_COLS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN20669) | Describes the columns of every editioning view in the database that is visible in the current edition. Useful for showing relationships between the columns of editioning views and the table columns to which they map. Join with \*\_OBJECTS\_AE, `*_TAB_COL`, or both, for additional information. |
| [`*_EDITIONING_VIEW_COLS_AE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN20683) | Describes the columns of every editioning view in the database, in every edition. |

Each row of `*_EDITIONING_VIEWS` matches exactly one row of `*_VIEWS`, and each row of `*_VIEWS` that has `EDITIONING_VIEW` = `'Y'` matches exactly one row of `*_EDITIONING_VIEWS`. Therefore, in this example, the `WHERE` clause is redundant:

```
SELECT ...
  FROM DBA_EDITIONING_VIEWS INNER JOIN DBA_VIEWS
  USING (OWNER, VIEW_NAME)
  WHERE EDITIONING_VIEW = 'Y'
  AND ...
```

The row of `*_VIEWS` that matches a row of `*_EDITIONING_VIEWS` has `EDITIONING_VIEW` = `'Y` ' by definition. Conversely, no row of `*_VIEWS` that has `EDITIONING_VIEW` = `'N'` has a counterpart in `*_ EDITIONING_VIEWS`.

See Also:

[Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN002) for more information about a specific view

#### 28.6.3 Displaying Information About Crossedition Triggers

The static data dictionary views that display information about triggers are described in [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN002). Crossedition triggers that appear in static data dictionary views are actual objects in the current edition.

Child cursors cannot be shared if the set of crossedition triggers that might run differs. The dynamic performance views `V$SQL_SHARED_CURSOR` and `GV$SQL_SHARED_CURSOR` have a `CROSSEDITION_TRIGGER_MISMATCH` column that tells whether this is true.

See Also:

[Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN30254) for information about `V$SQL_SHARED_CURSOR`

### 28.7 Using EBR to Upgrade an Application

To use EBR to upgrade your application online, you must first ready your application:

1. Editions-enable the appropriate users and the appropriate schema object types in their schemas.
	In schemas where you will create editioning views (in the next step), the type `VIEW` must be editionable.
	For instructions, see Enabling Editions for a User.
2. Prepare your application to use editioning views.
	For instructions, see Preparing Your Application to Use Editioning Views.

With the editioning views in place, you can use EBR to upgrade your application online as often as necessary. For each upgrade:

- If the type of every object that you will redefine is editionable (tables are not editionable), then use the procedure in Procedure for EBR Using Only Editions.
- If you will change the structure of one or more tables, and while you are doing so, other users need not be able to change data in those tables, then use the procedure in Procedure for EBR Using Editioning Views.
- If you will change the structure of one or more tables, and while you are doing so, other users must be able to change data in those tables, then use the procedure in Procedure for EBR Using Crossedition Triggers.

Topics:

- Preparing Your Application to Use Editioning Views
- Procedure for EBR Using Only Editions
- Procedure for EBR Using Editioning Views
- Procedure for EBR Using Crossedition Triggers
- Rolling Back the Application Upgrade
- Reclaiming Space Occupied by Unused Table Columns
- Example: Using EBR to Upgrade an Application

#### 28.7.1 Preparing Your Application to Use Editioning Views

An application that uses one or more tables must cover each table with an editioning view. An editioning view covers a table when all of these statements are true:

- Every ordinary object in the application references the table only through the editioning view. (An ordinary object is any object except an editioning view or crossedition trigger. Editioning views and crossedition triggers must reference tables.)
- Application users are granted object privileges only on the editioning view, not on the table.
- Oracle Virtual Private Database (VPD) policies are attached only to the editioning view, not to the table. (Regular auditing and fine-grained auditing (FGA) policies are attached only to the table.)

When the editioning view is actualized, a copy of the VPD policy is attached to the actualized editioning view. (A policy is uniquely identified by its name and the object to which it is attached.) If the policy function is also actualized, the copy of the policy uses the actualized policy function; otherwise, it uses the original policy function.

The static data dictionary views `*_POLICIES`, which describe the VPD policies, can have different results in different editions.

See Also:

- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=DBSEG007) for information about VPD, including that static data dictionary views that show information about VPD policies
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=REFRN20164) for information about `*_POLICIES`

If an existing application does not use editioning views, prepare it to use them by following this procedure for each table that it uses:

1. Give the table a new name (so that you can give its current name to its editioning view).
	Oracle recommends choosing a new name that is related to the original name and reflects the change history. For example, if the original table name is `Data`, the new table name might be `Data_1`.
2. (Optional) Give each column of the table a new name.
	Again, Oracle recommends choosing new names that are related to the original names and reflect the change history. For example, `Name` and `Number` might be changed to `Name_1` and `Number_1`.
	Any triggers that depend on renamed columns are now invalid. For details, see the entry for `ALTER` `TABLE` `table` `RENAME` `column` in [Table 27-2](schema-object-dependency.md).
3. Create the editioning view, giving it the original name of the table.
	For instructions, see Creating an Editioning View.
	Because the editioning view has the name that the table had, objects that reference that name now reference the editioning view.
4. If triggers are defined on the table, drop them, and rerun the code that created them.
	Now the triggers that were defined on the table are defined on the editioning view.
5. If VPD policies are attached to the table, drop the policies and policy functions and rerun the code that created them.
	Now the VPD policies that were attached to the table are attached to the editioning view.
6. Revoke all object privileges on the table from all application users.
	To see which application users have which object privileges on the table, use this query:
	```
	SELECT GRANTEE, PRIVILEGE
	FROM DBA_TAB_PRIVS
	WHERE TABLE_NAME='table_name';
	```
7. For every privilege revoked in step [^5], grant the same privilege on the editioning view.
8. For each user who owns a private synonym that refers to the table, enable editions, specifying that the type `SYNONYM` is editionable in the schema (for instructions, see Enabling Editions for a User).
9. Notify the owners of private synonyms that refer to the table that they must re-create those synonyms.

#### 28.7.2 Procedure for EBR Using Only Editions

Use this procedure only if every object that you will redefine is editioned (as defined in Editioned and Noneditioned Objects). Tables are never editioned objects.

1. Create a new edition.
	For instructions, see Creating an Edition.
2. Make the new edition your session edition.
	For instructions, see Changing Your Session Edition.
3. Make the necessary changes to the editioned objects of the application.
4. Ensure that all objects are valid.
	Query the static data dictionary `*_OBJECTS_AE`, which describes every actual object in the database, in every edition. If invalid objects remain, recompile them, using any `UTL_RECOMP` subprogram (described in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ARPLS380)).
5. Check that the changes work as intended.
	If so, go to step [^7].
	If not, either make further changes (return to step[^6]) or roll back the application upgrade (for instructions, see Rolling Back the Application Upgrade).
6. Make the new edition (the upgraded application) available to all users.
	For instructions, see Making an Edition Available to All Users.
7. Retire the old edition (the original application), so that all users except `SYS` use only the upgraded application.
	For instructions, see Retiring an Edition.
	Example 28-6 shows how to use the preceding procedure to change a very simple PL/SQL procedure.

Example 28-6 EBR of Very Simple Procedure

1. Create PL/SQL procedure for this example:
	```
	CREATE OR REPLACE PROCEDURE hello IS
	BEGIN
	  DBMS_OUTPUT.PUT_LINE('Hello, edition 1.');
	END hello;
	/
	```
2. Invoke PL/SQL procedure:
	```
	BEGIN hello(); END;
	/
	```
	Result:
	```
	Hello, edition 1.
	 
	PL/SQL procedure successfully completed.
	```
3. Do EBR of procedure:
	1. Create new edition:
		```
		CREATE EDITION e2 AS CHILD OF ora$base;
		```
		Result:
		```
		Edition created.
		```
		2. Make new edition your session edition:
		```
		ALTER SESSION SET EDITION = e2;
		```
		Result:
		```
		Session altered.
		```
		3. Change procedure:
		```
		CREATE OR REPLACE PROCEDURE hello IS
		BEGIN
		  DBMS_OUTPUT.PUT_LINE('Hello, edition 2.');
		END hello;
		/
		```
		Result:
		```
		Procedure created.
		```
		4. Check that change works as intended:
		```
		BEGIN hello(); END;
		/
		```
		Result:
		```
		Hello, edition 2.
		PL/SQL procedure successfully completed.
		```
		5. Make new edition available to all users (requires system privileges):
		```
		ALTER DATABASE DEFAULT EDITION = e2;
		```
		6. Retire old edition (requires system privileges):
		List grantees:
		```
		SELECT GRANTEE, PRIVILEGE
		FROM DBA_TAB_PRIVS
		WHERE TABLE_NAME = UPPER('ora$base')
		/
		```
		Result:
		```
		GRANTEE                        PRIVILEGE
		------------------------------ ---------
		PUBLIC                         USE
		 
		1 row selected.
		```
		Revoke use on old edition from all grantees:
		```
		REVOKE USE ON EDITION ora$base FROM PUBLIC;
		```

#### 28.7.3 Procedure for EBR Using Editioning Views

Use this procedure only if you will change the structure of one or more tables, and while you are doing so, other users need not be able to change data in those tables.

1. Create a new edition.
	For instructions, see Creating an Edition.
2. Make the new edition your session edition.
	For instructions, see Changing Your Session Edition.
3. In the new edition, if the editioning views are read-only, make them read-write.
	For instructions, see Changing the Writability of an Editioning View.
4. In every edition except the new edition, make the editioning views read-only.
5. Make the necessary changes to the objects of the application.
6. Ensure that all objects are valid.
	Query the static data dictionary `*_OBJECTS_AE`, which describes every actual object in the database, in every edition. If invalid objects remain, recompile them, using any `UTL_RECOMP` subprogram (described in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ARPLS380)).
7. Check that the changes work as intended.
	If so, go to step [^9].
	If not, either make further changes (return to step [^8]) or roll back the application upgrade (for instructions, see Rolling Back the Application Upgrade).
8. Make the upgraded application available to all users.
	For instructions, see Making an Edition Available to All Users.
9. Retire the old edition (the original application), so that all users except `SYS` use only the upgraded application.
	For instructions, see Retiring an Edition.

#### 28.7.4 Procedure for EBR Using Crossedition Triggers

Use this procedure only if you will change the structure of one or more tables, and while you are doing so, other users must be able to change data in those tables.

1. Create a new edition.
	For instructions, see Creating an Edition.
2. Make the new edition your session edition.
	For instructions, see Changing Your Session Edition.
3. Make the permanent changes to the objects of the application.
	For example, add new columns to the tables and create any new permanent subprograms.
	Objects that depend on objects that you changed might now be invalid. For more information, see [Table 27-2](schema-object-dependency.md).
4. Ensure that all objects are valid.
	Query the static data dictionary `*_OBJECTS_AE`, which describes every actual object in the database, in every edition. If invalid objects remain, recompile them, using any `UTL_RECOMP` subprogram (described in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ARPLS380)).
5. Create the temporary objects—the crossedition triggers (in the disabled state) and any subprograms that they need.
	For instructions, see Creating a Crossedition Trigger.
	You need reverse crossedition triggers only if you do step [^11], which is optional.
6. When the crossedition triggers compile successfully, enable them.
	Use the `ALTER` `TRIGGER` statement with the `ENABLE` option. For information about this statement, see [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=LNPLS99996).
7. Wait until pending changes are either committed or rolled back.
	Use the procedure `DBMS_UTILITY`.`WAIT_ON_PENDING_DML`, described in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ARPLS73275).
8. Apply the transforms.
	For instructions, see Transforming Data from Pre- to Post-Upgrade Representation.
	Note:
	It is impossible to predict whether this step visits an existing row before a user of an ancestor edition updates, inserts, or deletes data from that row.
9. Check that the changes work as intended.
	If so, go to step [^11].
	If not, either make further changes (return to step [^10]) or roll back the application upgrade (for instructions, see Rolling Back the Application Upgrade).
10. (Optional) Grant the `USE` privilege on your session edition to the early users of the upgraded application.
	For instructions, see Making an Edition Available to Some Users.
11. Make the upgraded application available to all users.
	For instructions, see Making an Edition Available to All Users.
12. Disable or drop the constraints and then drop the crossedition triggers.
	For instructions, see Dropping the Crossedition Triggers.
13. Retire the old edition (the original application), so that all users except `SYS` use only the upgraded application.
	For instructions, see Retiring an Edition.

#### 28.7.5 Rolling Back the Application Upgrade

To roll back the application upgrade:

1. Change your session edition to something other than the new edition that you created for the upgrade.
	For instructions, see Changing Your Session Edition.
2. Drop the new edition that you created for the upgrade.
	For instructions, see Dropping an Edition.
3. If you created new table columns during the upgrade, reclaim the space that they occupy (for instructions, see Reclaiming Space Occupied by Unused Table Columns).

#### 28.7.6 Reclaiming Space Occupied by Unused Table Columns

If you roll back an upgrade for which you created new table columns,

To reclaim the space that unused columns occupy:

1. Set the values of the unused columns to `NULL`.
	To avoid locking out other users while doing this operation, use the `DBMS_PARALLEL_EXECUTE` procedure (described in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ARPLS233)).
2. Set the unused columns to `UNUSED`.
	Use the `ALTER` `TABLE` statement (described in [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF01001)) with the `SET` `UNUSED` clause (described in [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF53205)).
3. Shrink the table.
	Use the `ALTER` `TABLE` statement (described in [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF01001)) with the `SHRINK` `SPACE` clause (described in [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=SQLRF53181)).

#### 28.7.7 Example: Using EBR to Upgrade an Application

This example uses an edition, an editioning view, a forward crossedition trigger, and a reverse crossedition trigger.

Topics:

- Existing Application
- Preparing the Application to Use Editioning Views
- Using EBR to Upgrade the Application

Note:

Before you can use EBR to upgrade an application, you must enable editions for every schema that the application uses. For instructions, see Enabling Editions for a User.

##### 28.7.7.1 Existing Application

The existing application—the application to be upgraded—consists of a single table on which a trigger is defined.

The existing application has a trigger, which you can check. The following examples show the existing application:

- Example: Creating the Existing Application
- Example: Viewing Data in Existing Table

###### 28.7.7.1.1 Example: How the Existing Application Was Created

The application was created as in Example 28-7.

Example 28-7 Creating the Existing Application

1. Create table:
	```
	CREATE TABLE Contacts(
	  ID            NUMBER(6,0) CONSTRAINT Contacts_PK PRIMARY KEY,
	  Name          VARCHAR2(47),
	  Phone_Number  VARCHAR2(20)
	);
	```
2. Populate table (not shown).
3. Prepare to create trigger on table:
	```
	ALTER TABLE Contacts ENABLE VALIDATE CONSTRAINT Contacts_PK;
	 
	DECLARE Max_ID INTEGER;
	BEGIN
	  SELECT MAX(ID) INTO Max_ID FROM Contacts;
	  EXECUTE IMMEDIATE '
	    CREATE SEQUENCE Contacts_Seq
	      START WITH '||To_Char(Max_ID + 1);
	END;
	/
	```
4. Create trigger:
	```
	CREATE TRIGGER Contacts_BI
	  BEFORE INSERT ON Contacts FOR EACH ROW
	BEGIN
	  :NEW.ID := Contacts_Seq.NEXTVAL;
	END;
	/
	```

###### 28.7.7.1.2 Example: Viewing Data in the Existing Table

Example 28-8 shows how the table `Contacts` looks after being populated with data.

Example 28-8 Viewing Data in the Existing Table

Query:

```
SELECT * FROM Contacts
ORDER BY Name;
```

Result:

```
ID NAME                                            PHONE_NUMBER
---------- ----------------------------------------------- --------------------
       174 Abel, Ellen                                     011.44.1644.429267
       166 Ande, Sundar                                    011.44.1346.629268
       130 Atkinson, Mozhe                                 650.124.6234
       105 Austin, David                                   590.423.4569
       204 Baer, Hermann                                   515.123.8888
       116 Baida, Shelli                                   515.127.4563
       167 Banda, Amit                                     011.44.1346.729268
       172 Bates, Elizabeth                                011.44.1343.529268
       192 Bell, Sarah                                     650.501.1876
       151 Bernstein, David                                011.44.1344.345268
       129 Bissot, Laura                                   650.124.5234
       169 Bloom, Harrison                                 011.44.1343.829268
       185 Bull, Alexis                                    650.509.2876
       187 Cabrio, Anthony                                 650.509.4876
       148 Cambrault, Gerald                               011.44.1344.619268
       154 Cambrault, Nanette                              011.44.1344.987668
       110 Chen, John                                      515.124.4269
       ...
       120 Weiss, Matthew                                  650.123.1234
       200 Whalen, Jennifer                                515.123.4444
       149 Zlotkey, Eleni                                  011.44.1344.429018

107 rows selected.
```

Suppose that you must redefine `Contacts`, replacing the `Name` column with the columns `First_Name` and `Last_Name`, and adding the column `Country_Code`. Also suppose that while you are making this structural change, other users must be able to change the data in `Contacts`.

You need all features of EBR: the edition, which is always needed; the editioning view, because you are redefining a table; and crossedition triggers, because other users must be able to change data in the table while you are redefining it.

##### 28.7.7.2 Preparing the Application to Use Editioning Views

Example 28-9 shows how to create the editioning view from which other users will access the table `Contacts` while you are redefining it in the new edition.

Example 28-9 Creating an Editioning View for the Existing Table

1. Give table a new name (so that you can give its current name to editioning view):
	```
	ALTER TABLE Contacts RENAME TO Contacts_Table;
	```
2. (Optional) Give columns of table new names:
	```
	ALTER TABLE Contacts_Table
	  RENAME COLUMN Name TO Name_1;
	ALTER TABLE Contacts_Table
	  RENAME COLUMN Phone_Number TO Phone_Number_1;
	```
3. Create editioning view:
	```
	CREATE OR REPLACE EDITIONING VIEW Contacts AS
	  SELECT
	    ID                 ID,
	    Name_1             Name,
	    Phone_Number_1     Phone_Number
	  FROM Contacts_Table;
	```
4. Move trigger `Contacts_BI` from table to editioning view:
	```
	DROP TRIGGER Contacts_BI;
	 
	CREATE TRIGGER Contacts_BI
	  BEFORE INSERT ON Contacts FOR EACH ROW
	BEGIN
	  :NEW.ID := Contacts_Seq.NEXTVAL;
	END;
	/
	```

##### 28.7.7.3 Using EBR to Upgrade the Example Application

You can use triggers to upgrade an existing application.

The following examples show how to use triggers to updated the example application:

- Example: Creating Edition in Which to Upgrade the Example Application
- Example: Changing the Table and Replacing the Editioning View
- Example: Creating and Enabling the Crossedition Triggers
- Example: Applying the Transforms
- Example: Viewing Data in the Changed Table

###### 28.7.7.3.1 Example: Creating an Edition in Which to Upgrade the Example Application

Example 28-10 shows how to create an edition in which to upgrade the existing application (in Existing Application), make the new edition the session edition, and check that the new edition really is the session edition.

Example 28-10 Creating an Edition in Which to Upgrade the Example Application

1. Create the new edition:
	```
	CREATE EDITION Post_Upgrade AS CHILD OF Ora$Base;
	```
2. Make new edition your session edition:
	```
	ALTER SESSION SET EDITION = Post_Upgrade;
	```
3. Check session edition:
	```
	SELECT
	SYS_CONTEXT('Userenv', 'Current_Edition_Name') "Current_Edition"
	FROM DUAL;
	```
	Result:
	```
	Current_Edition
	-----------------------------------------------------------------------------
	POST_UPGRADE
	 
	1 row selected.
	```

In the `Post_Upgrade` edition, Example: Creating an Edition in Which to Upgrade the Example Application shows how to add the new columns to the physical table and recompile the trigger that was invalidated by adding the columns. Then, it shows how to replace the editioning view `Contacts` so that it selects the columns of the table by their desired logical names.

Note:

Because you will change the base table, see " [Nonblocking and Blocking DDL Statements](sql-processing-for-application-developers.md)."

###### 28.7.7.3.2 Example: Changing the Table and Replacing the Editioning View

In the `Post_Upgrade` edition, Example 28-11 shows how to create two procedures for the forward crossedition trigger to use, create both the forward and reverse crossedition triggers in the disabled state, and enable them.

Example 28-11 Changing the Table and Replacing the Editioning View

1. Add new columns to physical table:
	```
	ALTER TABLE Contacts_Table ADD (
	  First_Name_2     varchar2(20),
	  Last_Name_2      varchar2(25),
	  Country_Code_2   varchar2(20),
	  Phone_Number_2   varchar2(20)
	);
	```
	(This is nonblocking DDL.)
2. Recompile invalidated trigger:
	```
	ALTER TRIGGER Contacts_BI COMPILE REUSE SETTINGS;
	```
3. Replace editioning view so that it selects replacement columns with their desired logical names:
	```
	CREATE OR REPLACE EDITIONING VIEW Contacts AS
	  SELECT
	    ID                 ID,
	    First_Name_2       First_Name,
	    Last_Name_2        Last_Name,
	    Country_Code_2     Country_Code,
	    Phone_Number_2     Phone_Number
	  FROM Contacts_Table;
	```

###### 28.7.7.3.3 Example: Creating and Enabling the Crossedition Triggers

In the `Post_Upgrade` edition, Example 28-12 shows how to apply the transforms.

Example 28-12 Creating and Enabling the Crossedition Triggers

1. Create first procedure that forward crossedition trigger uses:
	```
	CREATE OR REPLACE PROCEDURE Set_First_And_Last_Name (
	  Name        IN  VARCHAR2,
	  First_Name  OUT VARCHAR2,
	  Last_Name   OUT VARCHAR2)
	IS
	  Comma_Pos NUMBER := INSTR(Name, ',');
	BEGIN
	  IF Comma_Pos IS NULL OR Comma_Pos < 2 THEN
	    RAISE Program_Error;
	  END IF;
	 
	  Last_Name := SUBSTR(Name, 1, Comma_Pos-1);
	  Last_Name := RTRIM(Ltrim(Last_Name));
	 
	  First_Name := SUBSTR(Name, Comma_Pos+1);
	  First_Name := RTRIM(LTRIM(First_Name));
	END Set_First_And_Last_Name;
	/
	```
2. Create second procedure that forward crossedition trigger uses:
	```
	CREATE OR REPLACE PROCEDURE Set_Country_Code_And_Phone_No (
	  Phone_Number     IN  VARCHAR2,
	  Country_Code     OUT VARCHAR2,
	  Phone_Number_V2  OUT VARCHAR2)
	IS
	  Char_To_Number_Error EXCEPTION;
	  PRAGMA EXCEPTION_INIT(Char_To_Number_Error, -06502);
	  Bad_Phone_Number EXCEPTION;
	  Nmbr VARCHAR2(30) := REPLACE(Phone_Number, '.', '-');
	 
	  FUNCTION Is_US_Number(Nmbr IN VARCHAR2)
	    RETURN BOOLEAN
	  IS
	    Len NUMBER := LENGTH(Nmbr);
	    Dash_Pos NUMBER := INSTR(Nmbr, '-');
	    n PLS_INTEGER;
	  BEGIN
	    IF Len IS NULL OR Len <> 12 THEN
	      RETURN FALSE;
	    END IF;
	    IF Dash_Pos IS NULL OR Dash_Pos <> 4 THEN
	      RETURN FALSE;
	    END IF;
	    BEGIN
	      n := TO_NUMBER(SUBSTR(Nmbr, 1, 3));
	    EXCEPTION WHEN Char_To_Number_Error THEN
	      RETURN FALSE;
	    END;
	 
	    Dash_Pos := INSTR(Nmbr, '-', 5);
	 
	    IF Dash_Pos IS NULL OR Dash_Pos <> 8 THEN
	      RETURN FALSE;
	    END IF;
	 
	    BEGIN
	      n := TO_NUMBER(SUBSTR(Nmbr, 5, 3));
	    EXCEPTION WHEN Char_To_Number_Error THEN
	      RETURN FALSE;
	    END;
	 
	    BEGIN
	      n := TO_NUMBER(SUBSTR(Nmbr, 9));
	    EXCEPTION WHEN Char_To_Number_Error THEN
	      RETURN FALSE;
	    END;
	 
	    RETURN TRUE;
	  END Is_US_Number;
	 
	BEGIN
	  IF Nmbr LIKE '011-%' THEN
	    DECLARE
	      Dash_Pos NUMBER := INSTR(Nmbr, '-', 5);
	    BEGIN
	      Country_Code := '+'|| TO_NUMBER(SUBSTR(Nmbr, 5, Dash_Pos-5));
	      Phone_Number_V2 := SUBSTR(Nmbr, Dash_Pos+1);
	    EXCEPTION WHEN Char_To_Number_Error THEN
	      raise Bad_Phone_Number;
	    END;
	  ELSIF Is_US_Number(Nmbr) THEN
	    Country_Code := '+1';
	    Phone_Number_V2 := Nmbr;
	  ELSE
	    RAISE Bad_Phone_Number;
	  END IF;
	EXCEPTION WHEN Bad_Phone_Number THEN
	  Country_Code := '+0';
	  Phone_Number_V2 := '000-000-0000';
	END Set_Country_Code_And_Phone_No;
	/
	```
3. Create forward crossedition trigger in disabled state:
	```
	CREATE OR REPLACE TRIGGER Contacts_Fwd_Xed
	  BEFORE INSERT OR UPDATE ON Contacts_Table
	  FOR EACH ROW
	  FORWARD CROSSEDITION
	  DISABLE
	BEGIN
	  Set_First_And_Last_Name(
	    :NEW.Name_1,
	    :NEW.First_Name_2,
	    :NEW.Last_Name_2
	  );
	  Set_Country_Code_And_Phone_No(
	    :NEW.Phone_Number_1,
	    :NEW.Country_Code_2,
	    :NEW.Phone_Number_2
	  );
	END Contacts_Fwd_Xed;
	/
	```
4. Enable forward crossedition trigger:
	```
	ALTER TRIGGER Contacts_Fwd_Xed ENABLE;
	```
5. Create reverse crossedition trigger in disabled state:
	```
	CREATE OR REPLACE TRIGGER Contacts_Rvrs_Xed
	  BEFORE INSERT OR UPDATE ON Contacts_Table
	  FOR EACH ROW
	  REVERSE CROSSEDITION
	  DISABLE
	BEGIN
	  :NEW.Name_1 := :NEW.Last_Name_2||', '||:NEW.First_Name_2;
	  :NEW.Phone_Number_1 :=
	  CASE :New.Country_Code_2
	    WHEN '+1' THEN
	      REPLACE(:NEW.Phone_Number_2, '-', '.')
	    ELSE
	      '011.'||LTRIM(:NEW.Country_Code_2, '+')||'.'||
	      REPLACE(:NEW.Phone_Number_2, '-', '.')
	  END;
	END Contacts_Rvrs_Xed;
	/
	```
6. Enable reverse crossedition trigger:
	```
	ALTER TRIGGER Contacts_Rvrs_Xed ENABLE;
	```
7. Wait until pending changes are either committed or rolled back:
	```
	DECLARE
	  scn              NUMBER  := NULL;
	  timeout CONSTANT INTEGER := NULL;
	BEGIN
	  IF NOT DBMS_UTILITY.WAIT_ON_PENDING_DML(Tables  => 'Contacts_Table',
	                                          timeout => timeout,
	                                          scn     => scn)
	  THEN
	    RAISE_APPLICATION_ERROR(-20000,
	     'Wait_On_Pending_DML() timed out. CETs were enabled before SCN: '||SCN);
	  END IF;
	END;
	/
	```

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ARPLS73275) for information about the `DBMS_UTILITY`.`WAIT_ON_PENDING_DML` procedure

###### 28.7.7.3.4 Example: Applying the Transforms

In the Post\_Upgrade edition, Example 28-13 example shows how to apply the transforms.

Example 28-13 Applying the Transforms

```
DECLARE
  c NUMBER := DBMS_SQL.OPEN_CURSOR();
  x NUMBER;
BEGIN
  DBMS_SQL.PARSE(
    c                          => c,
    Language_Flag              => DBMS_SQL.NATIVE,
    Statement                  => 'UPDATE Contacts_Table SET ID = ID',
    Apply_Crossedition_Trigger => 'Contacts_Fwd_Xed'
  );
  x := DBMS_SQL.EXECUTE(c);
  DBMS_SQL.CLOSE_CURSOR(c);
  COMMIT;
END;
/
```

###### 28.7.7.3.5 Example: Viewing Data in the Changed Table

In the `Post_Upgrade` edition, Example 28-14 shows how to check that the change worked as intended. Compare Example: Viewing Data in the Changed Table to Example: Viewing Data in the Existing Table.

Example 28-14 Viewing Data in the Changed Table

1. Format columns for readability:
	```
	COLUMN ID FORMAT 999
	COLUMN Last_Name FORMAT A15
	COLUMN First_Name FORMAT A15
	COLUMN Country_Code FORMAT A12
	COLUMN Phone_Number FORMAT A12
	```
2. Query:
	```
	SELECT * FROM Contacts
	ORDER BY Last_Name;
	```
	Result:
	```
	ID FIRST_NAME      LAST_NAME       COUNTRY_CODE PHONE_NUMBER
	---- --------------- --------------- ------------ ------------
	 174 Ellen           Abel            +44          1644-429267
	 166 Sundar          Ande            +44          1346-629268
	 130 Mozhe           Atkinson        +1           650-124-6234
	 105 David           Austin          +1           590-423-4569
	 204 Hermann         Baer            +1           515-123-8888
	 116 Shelli          Baida           +1           515-127-4563
	 167 Amit            Banda           +44          1346-729268
	 172 Elizabeth       Bates           +44          1343-529268
	 192 Sarah           Bell            +1           650-501-1876
	 151 David           Bernstein       +44          1344-345268
	 129 Laura           Bissot          +1           650-124-5234
	 169 Harrison        Bloom           +44          1343-829268
	 185 Alexis          Bull            +1           650-509-2876
	 187 Anthony         Cabrio          +1           650-509-4876
	 154 Nanette         Cambrault       +44          1344-987668
	 148 Gerald          Cambrault       +44          1344-619268
	 110 John            Chen            +1           515-124-4269
	       ...
	 120 Matthew         Weiss           +1           650-123-1234
	 200 Jennifer        Whalen          +1           515-123-4444
	 149 Eleni           Zlotkey         +44          1344-429018
	 
	107 rows selected.
	```

If the change worked as intended, you can now follow steps [^11] through [^12] of the procedure in Procedure for EBR Using Crossedition Triggers.

[^1]: Noncrossedition triggers

[^undefined]: Forward crossedition triggers created in the current edition

[^2]: Forward crossedition triggers created in descendents of the current edition, in the order that the descendents were created (child, grandchild, and so on)

[^3]: Reverse crossedition triggers created in the current edition

[^4]: Reverse crossedition triggers created in the ancestors of the current edition, in the reverse order that the ancestors were created (parent, grandparent, and so on)

[^5]: Revoke all object privileges on the table from all application users.

To see which application users have which object privileges on the table, use this query:

```
SELECT GRANTEE, PRIVILEGE
FROM DBA_TAB_PRIVS
WHERE TABLE_NAME='table_name';
```

[^undefined]: For every privilege revoked in step 6, grant the same privilege on the editioning view.

[^6]: Make the necessary changes to the editioned objects of the application.

[^undefined]: Ensure that all objects are valid.

Query the static data dictionary `*_OBJECTS_AE`, which describes every actual object in the database, in every edition. If invalid objects remain, recompile them, using any `UTL_RECOMP` subprogram (described in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ARPLS380)).

[^undefined]: Check that the changes work as intended.

If so, go to step 6.

If not, either make further changes (return to step 3) or roll back the application upgrade (for instructions, see Rolling Back the Application Upgrade).

[^7]: Make the new edition (the upgraded application) available to all users.

For instructions, see Making an Edition Available to All Users.

[^undefined]: Retire the old edition (the original application), so that all users except `SYS` use only the upgraded application.

For instructions, see Retiring an Edition.

Example 28-6 shows how to use the preceding procedure to change a very simple PL/SQL procedure.

[^8]: Make the necessary changes to the objects of the application.

[^undefined]: Ensure that all objects are valid.

Query the static data dictionary `*_OBJECTS_AE`, which describes every actual object in the database, in every edition. If invalid objects remain, recompile them, using any `UTL_RECOMP` subprogram (described in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ARPLS380)).

[^undefined]: Check that the changes work as intended.

If so, go to step 8.

If not, either make further changes (return to step 5) or roll back the application upgrade (for instructions, see Rolling Back the Application Upgrade).

[^9]: Make the upgraded application available to all users.

For instructions, see Making an Edition Available to All Users.

[^undefined]: Retire the old edition (the original application), so that all users except `SYS` use only the upgraded application.

For instructions, see Retiring an Edition.

[^10]: Make the permanent changes to the objects of the application.

For example, add new columns to the tables and create any new permanent subprograms.

Objects that depend on objects that you changed might now be invalid. For more information, see [Table 27-2](schema-object-dependency.md).

[^undefined]: Ensure that all objects are valid.

Query the static data dictionary `*_OBJECTS_AE`, which describes every actual object in the database, in every edition. If invalid objects remain, recompile them, using any `UTL_RECOMP` subprogram (described in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ARPLS380)).

[^undefined]: Create the temporary objects—the crossedition triggers (in the disabled state) and any subprograms that they need.

For instructions, see Creating a Crossedition Trigger.

You need reverse crossedition triggers only if you do step 10, which is optional.

[^undefined]: When the crossedition triggers compile successfully, enable them.

Use the `ALTER` `TRIGGER` statement with the `ENABLE` option. For information about this statement, see [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=LNPLS99996).

[^undefined]: Wait until pending changes are either committed or rolled back.

Use the procedure `DBMS_UTILITY`.`WAIT_ON_PENDING_DML`, described in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=ARPLS73275).

[^undefined]: Apply the transforms.

For instructions, see Transforming Data from Pre- to Post-Upgrade Representation.

Note:

It is impossible to predict whether this step visits an existing row before a user of an ancestor edition updates, inserts, or deletes data from that row.

[^undefined]: Check that the changes work as intended.

If so, go to step 10.

If not, either make further changes (return to step 3) or roll back the application upgrade (for instructions, see Rolling Back the Application Upgrade).

[^11]: (Optional) Grant the `USE` privilege on your session edition to the early users of the upgraded application.

For instructions, see Making an Edition Available to Some Users.

[^undefined]: Make the upgraded application available to all users.

For instructions, see Making an Edition Available to All Users.

[^undefined]: Disable or drop the constraints and then drop the crossedition triggers.

For instructions, see Dropping the Crossedition Triggers.

[^12]: Retire the old edition (the original application), so that all users except `SYS` use only the upgraded application.

For instructions, see Retiring an Edition.