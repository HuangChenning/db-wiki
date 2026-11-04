---
title: Database Development Guide
book: Database Development Guide
doc_id: E96334-10
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/adfns/registering-application-data-usage-database.html
tags:
  - oracle
  - 19c
  - development-guide
---

## 10 Registering Application Data Usage with the Database

This chapter details how you can use a centralized database-centric entity called schema annotations to register information about the intended application data usage.

Oracle Database 19c introduces a centralized, database-centric approach to handling intended data usage information using schema annotations. You can add schema annotations centrally in the database to register data usage intent, which is then accessible to various applications and tools.

See Also:

- Oracle Database Concepts for information about [Schema Annotations](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=CNCPT-GUID-D5D5615C-BB2C-4833-A9AF-6BAF0BF9CEC0)
- Oracle Database SQL Language Reference for the syntactic and semantic information about schema annotations

- [Schema Annotations](https://docs.oracle.com/en/database/oracle/oracle-database/19/adfns/registering-application-data-usage-database.html#GUID-2DAF069E-0938-40AF-B05B-75AFE71D666C "This section explains how you can use schema annotations (hereinafter \"annotations\") for database objects.")

### 10.1 Schema Annotations

This section explains how you can use schema annotations (hereinafter "annotations") for database objects.

For many applications, it is important to maintain additional property metadata for database objects such as tables, views, table columns, and indexes. Annotations enable your applications to store and retrieve additional user-specific metadata about database objects and table columns. Applications can use such metadata to help render effective user interfaces and customize application logic.

#### 10.1.1 Overview of Annotations

What are annotations and where can you use them?

Annotations are a lightweight declarative facility for developers to centrally register usage properties for database schema objects. Annotations are stored in dictionary tables and are available to any application looking to standardize behavior across common data in related applications. Annotations are not interpreted by the database in any way. They are custom data properties for database metadata - included for table columns, tables, and indexes, that applications can use as additional property metadata to render user interfaces or customize application logic.

Being a mechanism to define and store application metadata centrally in the database, annotations enable you to share the metadata information across applications, modules and microservices. You can add annotations to schema objects when you create new objects (using the `CREATE` statements) or modify existing objects (using the `ALTER` statements).

Annotating the data model with metadata provides additional data integrity, consistency and data model documentation benefits. Your applications can store user-defined metadata for database objects and table columns that other applications or users can retrieve and use. Storing the metadata along with the data guarantees consistency and universal accessibility to any user or application that uses the data.

An individual annotation has a name and an optional value. The name and the optional value are freeform text fields. For example, you can have an annotation with a name and value pair, such as `Display_Label ‘Employee Salary’`, or you can have a standalone annotation with only a name, such as `UI_Hidden`, which does not need a value because the name is self-explanatory.

The following are further details about annotations.

- When an annotation name is specified for a schema object using the `CREATE` DDL statement, an annotation is automatically created.
- Annotations are additive, meaning that you can specify multiple annotations for the same schema object.
- You can add multiple annotations at once to a schema object using a single DDL statement. Similarly, a single DDL statement can drop multiple annotations from a schema object.
- An annotation is represented as a subordinate element to the database object to which the annotation is added. Annotations do not create a new object type inside the database.
- You can add annotations to any schema object that supports annotations provided you own or have alter privileges on the schema object. You do not need to schema qualify the annotation name.
- You can issue SQL queries on dictionary views to obtain all annotations, including their names and values, and their usage with schema objects.

#### 10.1.2 Annotations and Comments

You can also annotate database objects such as tables and table columns using the `COMMENT` command. Comments that are associated with schema objects are stored in data dictionaries along with the metadata of the objects.

Annotations are simpler to use and have a broader scope than comments. Following are the major differences between comments and annotations:

- Comments are a commenting mechanism used to add metadata to only certain schema objects, such as tables and columns. Comments are not available for other schema objects, such as indexes, procedures, and triggers.
- Comments do not have a name, they have only a freeform value.
- Comments are not additive meaning that you cannot add multiple comments for the same object. Specifying a new comment overwrites the prior comment for the corresponding table or column.
- You need separate DDL statements for comments whereas you can combine multiple annotations into one DDL statement.
- A separate set of dictionary views exists for different entities. For instance, there is a view for table comments and another view for column comments. Annotations, on the other hand, are unified across all object types, which makes them simpler to query and use.

#### 10.1.3 Supported Database Objects

Annotations are supported for the following database objects.

- Tables and table columns
- Views and view columns
- Materialized views and materialized view columns
- Indexes

#### 10.1.4 Privileges Required for Using Annotations

To add or drop annotations, you require the `CREATE` or `ALTER` privilege on the schema object for which the annotation is specified in the `CREATE` or `ALTER` DDL statements.

You cannot create or remove annotations explicitly. Annotations are automatically created when they are used for the first time. Since annotations are stored as subordinate elements within the database object on which they are defined, adding annotations does not create a new object type inside the database.

#### 10.1.5 DDL Statements for Annotations

This section explains the annotation syntax and provides the DDL statements to define or alter annotations for tables, table columns, views, materialized views, and indexes.

Topics:

- Annotation Syntax
- DDL Statements to Annotate a Table
- DDL Statements to Annotate a Table Column
- DDL Statements to Annotate Views and Materialized Views
- DDL Statements to Annotate Indexes

##### 10.1.5.1 Annotation Syntax

The following snippet illustrates the annotation syntax that is used in DDL statements to define annotations for tables, table columns, views, materialized views, and indexes.

```
annotations
         ::= 'ANNOTATIONS' '(' annotations_list ')'

annotations_list
         ::= ( 'ADD' ('IF NOT EXISTS' | 'OR REPLACE' )? | 'DROP' 'IF EXISTS'? | REPLACE)?
 annotation ( ',' ( 'ADD' ('IF NOT EXISTS' | 'OR REPLACE' )? | 'DROP' 'IF EXISTS'? | REPLACE)?
 annotation )*

annotation
         ::= annotation_name annotation_value?

annotation_name
         ::= identifier

annotation_value
         ::= character_string_literal
```

< `annotation_value` > is a character string literal that can hold up to 4000 characters.

< `annotation_name` > is an identifier and has the following requirements:

- An identifier can have up to 1024 characters.
- If an identifier is a reserved word, you must provide the annotation name in double quotes.
- An identifier with double quotes can contain white characters.
- An identifier that contains only white characters is not allowed.

##### 10.1.5.2 DDL Statements to Annotate a Table

You can use the following DDL statements to annotate a table when creating or altering the table.

Using the `CREATE TABLE                 ` Statement

The following are examples of the `CREATE TABLE` statement with annotations.

The following example adds an annotation: `Operation` with a JSON value, and another annotation: `Hidden`, which is standalone and has no value.

```
CREATE TABLE Table1 (
  T NUMBER)
  ANNOTATIONS(Operations '["Sort", "Group"]', Hidden);
```

Adding an annotation can be preceded by the `ADD` keyword. The `ADD` keyword is considered to be the default operation, if nothing is specified.

The following example uses the optional `ADD` keyword to add the `Hidden` annotation (which is also standalone) to `Table2`.

```
CREATE TABLE Table2 (
  T NUMBER)
  ANNOTATIONS (ADD Hidden);
```

The `ADD` keyword is an implicit operation when annotations are defined, and can be omitted.

Using the `ALTER TABLE                 ` Statement

In the following example, the `ALTER TABLE` command drops all annotation values for the following annotation names: `Operations` and `Hidden`.

```
ALTER TABLE Table1
  ANNOTATIONS(DROP Operations, DROP Hidden);
```

The following example has the `ALTER TABLE` command to add `JoinOperations` annotation with `Join` value, and to drop the annotation name: `Hidden`. When dropping an annotation, you need to only include the annotation name with the `DROP` command.

```
ALTER TABLE Table1
  ANNOTATIONS(ADD JoinOperations 'Join', DROP Hidden);
```

Due to the Hidden annotation being dropped in the earlier statement, the output is: `ORA-11553: Annotation name 'HIDDEN' does not exist for the object                     'Table1'`. To avoid this error: when the annotation does not exist, you can use the IF EXISTS clause.

```
ALTER TABLE Table1 ANNOTATIONS(ADD JoinOperations 'Join', DROP IF EXISTS Hidden);
```

Multiple `ADD` and `DROP` keywords can be specified in one DDL statement.

Trying to re-add an annotation with a different value for the same object (for object-level annotations) or for the same column (for column-level annotations) raises an error. For instance, the following statement fails:
```
ALTER TABLE Table1
  ANNOTATIONS(ADD JoinOperations 'Join Ops');
```

The output is:

```
ORA-11552: Annotation name 'JOINOPERATIONS' already exists for the object 'TABLE1'.
```

As an alternative, the annotation syntax allows you to replace an annotation value using the `REPLACE` keyword. The following statement replaces the value of `JoinOperations` with ' `Join                     Ops` ':
```
ALTER TABLE Table1
  ANNOTATIONS(REPLACE JoinOperations 'Join Ops');
```

The output is

```
Table altered.
```

Alternatively, to avoid an error when an annotation already exists, you can use the `IF NOT EXISTS` clause. The following statement adds the `JoinOperations` annotation only if it does not exist. If the annotation exists, the annotation value is unchanged and no error is raised.
```
ALTER TABLE Table1
  ANNOTATIONS(ADD IF NOT EXISTS JoinOperations 'Join Ops');
```

Similarly, dropping a non-existent annotation raises an error:
```
ALTER TABLE Table1 ANNOTATIONS(DROP Title);
```

The output is:

```
ORA-11553: Annotation name 'TITLE' does not exist.
```

To avoid the error, the `IF EXISTS` clause can be used, as follows:
```
ALTER TABLE Table1
  ANNOTATIONS(DROP IF EXISTS Title);
```

The output is:

```
Table altered.
```

See Also:

[CREATE TABLE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=SQLRF-GUID-F9CE0CC3-13AE-4744-A43C-EAC7A71AAAB6) and [ALTER TABLE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=SQLRF-GUID-552E7373-BF93-477D-9DA3-B2C9386F2877) in SQL Language Reference for complete clause changes and definitions.

##### 10.1.5.3 DDL Statements to Annotate a Table Column

You can use the following DDL statements to annotate a table column when creating or altering the table.

Using the `CREATE TABLE ` Statement

To add column-level annotations using a `CREATE TABLE` statement, specify the annotations as a part of the `column_definition` clause. Annotations are specified at the end, after inline constraints.

The following examples specify annotations for columns at table creation.

```
CREATE TABLE Table1
  (T NUMBER ANNOTATIONS(Operations 'Sort', Hidden));

CREATE TABLE Table2
  (T NUMBER ANNOTATIONS (Hidden));
```

The following example specifies table-level and column-level annotations for the `Employee` table.

```
CREATE TABLE Employee (
  Id NUMBER(5) ANNOTATIONS(Identity, Display 'Employee ID', "Group" 'Emp_Info'),
  Ename VARCHAR2(50) ANNOTATIONS(Display 'Employee Name', "Group" 'Emp_Info'),
  Sal NUMBER ANNOTATIONS(Display 'Employee Salary', UI_Hidden)
)
 ANNOTATIONS (Display 'Employee Table');
```

The `Employee` table in the previous example has column-level and object-level annotations with `Display` annotations defined at the column level and object level. You can define a new annotation with the same name as long as it corresponds to a different object, column pair. For instance, you cannot define another annotation with the `Display` name for the `Employee` table but you can define new annotations with `Display` name for every column of the `Employee` table. You can also define other annotations such as " `Group` " for the `Sal` column. The annotation " `Group` " needs to be double quoted because it is a reserved word.

Using the `ALTER TABLE ` Statement

To add column-level annotations using an `ALTER TABLE` statement, specify the annotations as a part of the `modify_col_properties` clause. Annotations are specified at the end, after inline constraints.

The following example adds a new `Identity` annotation for the column T of `Table1` table.

```
ALTER TABLE Table1
  MODIFY T ANNOTATIONS(Identity 'ID');
```

The following example adds a `Label` annotation and drops the `Identity` annotation.

```
ALTER TABLE Table1
  MODIFY T ANNOTATIONS(ADD Label, DROP Identity);
```

See Also:

[CREATE TABLE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=SQLRF-GUID-F9CE0CC3-13AE-4744-A43C-EAC7A71AAAB6) and [ALTER TABLE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=SQLRF-GUID-552E7373-BF93-477D-9DA3-B2C9386F2877) in SQL Language Reference for complete clause changes and definitions.

##### 10.1.5.4 DDL Statements to Annotate Views and Materialized Views

You can use the following DDL statements to annotate a view and a materialized view.

Views and materialized views support annotations at the view level and column level. Column-level annotations are only supported for table views as a part of the column alias definition clause.

Using the `CREATE                     VIEW` Statement

The following example shows the view-level and column-level annotations:

```
CREATE OR REPLACE VIEW HighWageEmp  
(
  Id ANNOTATIONS(Identity, Display 'Employee ID', "Group" 'Emp_Info'),
  Ename ANNOTATIONS (Display 'Employee Name',  "Group" 'Emp_Info'),
  Sal  ANNOTATIONS (Display 'Emp Salary')  
)
ANNOTATIONS (Title 'High Wage Employee View')
AS SELECT * FROM EMPLOYEE WHERE Sal > 100000;
```

Using the `CREATE                     MATERIALIZED VIEW` Statement

The following example adds annotation at the view level in the `Materialized View` statement:

```
CREATE MATERIALIZED VIEW MView1
  ANNOTATIONS (Title 'Tab1 MV1', ADD Snapshot)
  AS SELECT * FROM Table1;
```

The following example adds annotation at the view level and column level in the `Materialized View` statement:

```
CREATE MATERIALIZED VIEW MView1(
  T ANNOTATIONS (Hidden)) 
 ANNOTATIONS (Title 'Tab1 MV1', ADD Snapshot)
 AS SELECT * FROM Table1;
```

Using the `ALTER                     VIEW` Statement

To provide support for annotations, the `ALTER VIEW` statement has a new sub-clause added to it that allows altering annotations at the view level. Other sub-clauses that are supported in the `ALTER VIEW` statement are: modifying view constraints, enabling recompilation, and changing `EDITIONABLE` property.

Column-level annotations for views cannot be altered. Previously added column-level annotations can be dropped only by dropping the view and recreating a new one.

The following example is an `ALTER VIEW` statement that drops the `Title` annotation and adds the `Identity` annotation at the view level.

```
ALTER VIEW HighWageEmp
  ANNOTATIONS(DROP Title, ADD Identity);
```

Using the `ALTER                     MATERIALIZED VIEW` Statement

The `ALTER MATERIALIZED VIEW` statement has a new sub-clause that is added to alter annotations globally at the materialized view level. Column-level annotations can be dropped only by dropping and recreating the materialized view.

The following `ALTER MATERIALIZED VIEW` statement drops `Snapshot` annotation from `MView1`.

```
ALTER MATERIALIZED VIEW MView1
  ANNOTATIONS(DROP Snapshot);
```

See Also:

[CREATE VIEW](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=SQLRF-GUID-61D2D2B4-DACC-4C7C-89EB-7E50D9594D30), [ALTER VIEW](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=SQLRF-GUID-0DEDE960-B481-4B55-8027-EA9E4C863625), [CREATE MATERIALIZED VIEW](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=SQLRF-GUID-EE262CA4-01E5-4618-B659-6165D993CA1B), and [ALTER MATERIALIZED VIEW](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=SQLRF-GUID-29EE5682-AE42-4879-ABAD-E34E66ADD233) in SQL Language Reference for complete clause changes and definitions.

##### 10.1.5.5 DDL Statements to Annotate Indexes

You can use the following DDL statements to annotate an index.

Using the `CREATE INDEX` Statement

The following are examples of creating index-level annotations.

```
CREATE TABLE DEPARTMENT(
  DEPT_ID NUMBER,
  UNIT NUMBER);

CREATE INDEX I_DEPT_ID ON DEPARTMENT(DEPT_ID)
  ANNOTATIONS(Display 'Department Index');

CREATE UNIQUE INDEX UI_UNIT ON DEPARTMENT(UNIT)
  ANNOTATIONS(Display 'Department Unique Index');
```

Using the `ALTER INDEX` Statement

The following is an example of altering an index-level annotation.

```
ALTER INDEX I_DEPT_ID
  ANNOTATIONS(DROP Display, ADD ColumnGroup 'Group1');
```

See Also:

[CREATE INDEX](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=SQLRF-GUID-1F89BBC0-825F-4215-AF71-7588E31D8BFE) and [ALTER INDEX](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=SQLRF-GUID-D8F648E7-8C07-4C89-BB71-862512536558) in SQL Language Reference for complete clause changes and definitions.

#### 10.1.6 Dictionary Table and Views

A dictionary table called `ANNOTATIONS_USAGE$` includes all the usage of annotations with schema objects, such as tables and views. When a new annotation name, value, or both are specified to a schema object, a new entry in `ANNOTATIONS_USAGE$` table is created. Similarly, when a schema object drops an annotation, the corresponding entry is dropped from the `ANNOTATIONS_USAGE$` table.

The following dictionary views track the list of annotations and their usage across all schema objects:

- `{DBA|USER|ALL|CDB}_ANNOTATIONS`
- `{DBA|USER|ALL|CDB}_ANNOTATIONS_USAGE`
- `{DBA|USER|ALL|CDB}_ANNOTATIONS_VALUES`

##### 10.1.6.1 Querying Dictionary Views

You can run queries on dictionary views to obtain the list of annotations that are used for specific schema objects.

Here are examples of query statements issued on an 'EMP' table:

To obtain table-level annotations for the ‘EMP’ table:
```
SELECT * FROM USER_ANNOTATIONS_USAGE
  WHERE Object_Name = 'EMPLOYEE'
   AND Object_Type = 'TABLE'
   AND Column_Name IS NULL;
```

To obtain column-level annotations for the ‘EMP’ table:
```
SELECT * FROM USER_ANNOTATIONS_USAGE
  WHERE Object_Name = 'EMPLOYEE'
   AND Object_Type = 'TABLE'
   AND Column_Name IS NOT NULL;
```

To obtain column-level annotations for the ‘EMP’ table as a single JSON collection per column:
```
SELECT  U.Column_Name, JSON_ARRAYAGG(JSON_OBJECT(U.Annotation_Name, U.Annotation_Value))
  FROM USER_ANNOTATIONS_USAGE U
  WHERE Object_Name = 'EMPLOYEE' AND Object_Type = 'TABLE' AND Column_Name IS NOT NULL
  GROUP BY Column_Name;
```