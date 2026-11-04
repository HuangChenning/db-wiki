---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/preface.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## Preface

### Audience

Oracle Database PL/SQL Packages and Types Reference is intended for programmers, systems analysts, project managers, and others interested in developing database applications. This manual assumes a working knowledge of application programming and familiarity with SQL to access information in relational database systems. Some sections also assume a knowledge of basic object-oriented programming.

### Documentation Accessibility

For information about Oracle's commitment to accessibility, visit the Oracle Accessibility Program website at [http://www.oracle.com/pls/topic/lookup?ctx=acc&id=docacc](https://docs.oracle.com/pls/topic/lookup?ctx=acc&id=docacc).

Access to Oracle Support

Oracle customers that have purchased support have access to electronic support through My Oracle Support. For information, visit [http://www.oracle.com/pls/topic/lookup?ctx=acc&id=info](https://docs.oracle.com/pls/topic/lookup?ctx=acc&id=info) or visit [http://www.oracle.com/pls/topic/lookup?ctx=acc&id=trs](https://docs.oracle.com/pls/topic/lookup?ctx=acc&id=trs) if you are hearing impaired.

### Related Documents

For more information, see the following documents:

- [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADFNS)
- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=LNPLS)

Many of the examples in this book use the sample schemas, which are installed by default when you select the Basic Installation option with an Oracle Database installation. Refer to [Oracle Database Sample Schemas](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=COMSC) for information on how these schemas were created and how you can use them yourself.

Printed documentation is available for sale in the Oracle Store at

```
http://shop.oracle.com/
```

To download free release notes, installation documentation, white papers, or other collateral, please visit the Oracle Technology Network (OTN).

```
http://docs.oracle.com/
```

### Conventions

This section describes the conventions used in the text and code examples of this documentation set. It describes:

- Conventions in Text
- Conventions in Code Examples

Conventions in Text

We use various conventions in text to help you more quickly identify special terms. The following table describes those conventions and provides examples of their use.

| Convention | Meaning | Example |
| --- | --- | --- |
| Bold | Bold typeface indicates terms that are defined in the text or terms that appear in a glossary, or both. | When you specify this clause, you create an index-organized table. |
| Italics | Italic typeface indicates book titles or emphasis. | Oracle Database Concepts  Ensure that the recovery catalog and target database do not reside on the same disk. |
| `UPPERCASE monospace (fixed-width) font` | Uppercase monospace typeface indicates elements supplied by the system. Such elements include parameters, privileges, datatypes, RMAN keywords, SQL keywords, SQL\*Plus or utility commands, packages and methods, as well as system-supplied column names, database objects and structures, usernames, and roles. | You can specify this clause only for a `NUMBER` column.  You can back up the database by using the `BACKUP` command.  Query the `TABLE_NAME` column in the `USER_TABLES` data dictionary view.  Use the `DBMS_STATS`.`GENERATE_STATS` procedure. |
| `lowercase monospace (fixed-width) font` | Lowercase monospace typeface indicates executable programs, filenames, directory names, and sample user-supplied elements. Such elements include computer and database names, net service names and connect identifiers, user-supplied database objects and structures, column names, packages and classes, usernames and roles, program units, and parameter values.  Note: Some programmatic elements use a mixture of UPPERCASE and lowercase. Enter these elements as shown. | Enter `sqlplus` to start SQL\*Plus.  The password is specified in the `orapwd` file.  Back up the datafiles and control files in the `/disk1/oracle/dbs` directory.  The `department_id`, `department_name`, and `location_id` columns are in the `hr.departments` table.  Set the `QUERY_REWRITE_ENABLED` initialization parameter to `true.`  The `JRepUtil` class implements these methods. |
| `lowercase italic monospace (fixed-width) font` | Lowercase italic monospace font represents placeholders or variables. | You can specify the `parallel_clause`.  Run `old_release``.SQL` where `old_release` refers to the release you installed prior to upgrading. |

Conventions in Code Examples

Code examples illustrate SQL, PL/SQL, SQL\*Plus, or other command-line statements. They are displayed in a monospace (fixed-width) font and separated from normal text as shown in this example:

```
SELECT username FROM dba_users WHERE username = 'MIGRATE';
```

The following table describes typographic conventions used in code examples and provides examples of their use.

| Convention | Meaning | Example |
| --- | --- | --- |
| ``` [ ] ``` | Anything enclosed in brackets is optional. | ``` DECIMAL (digits [ , precision ]) ``` |
| ``` { } ``` | Braces are used for grouping items. | ``` {ENABLE \| DISABLE} ``` |
| ``` \| ``` | A vertical bar represents a choice of two options. | ``` {ENABLE \| DISABLE} [COMPRESS \| NOCOMPRESS] ``` |
| ``` ... ``` | Ellipsis points mean repetition in syntax descriptions.  In addition, ellipsis points can mean an omission in code examples or text. | ``` CREATE TABLE ... AS subquery;  SELECT col1, col2, ... , coln FROM employees; ``` |
| Other symbols | You must use symbols other than brackets (\[ \]), braces ({ }), vertical bars (\|), and ellipsis points (...) exactly as shown. | ``` acctbal NUMBER(11,2); acct    CONSTANT NUMBER(4) := 3; ``` |
| ``` Italics ``` | Italicized text indicates placeholders or variables for which you must supply particular values. | ``` enter password  DB_NAME = database_name ``` |
| ``` UPPERCASE ``` | Uppercase typeface indicates elements supplied by the system. We show these terms in uppercase in order to distinguish them from terms you define. Unless terms appear in brackets, enter them in the order and with the spelling shown. Because these terms are not case sensitive, you can use them in either UPPERCASE or lowercase. | ``` SELECT last_name, employee_id FROM employees; SELECT * FROM USER_TABLES; DROP TABLE hr.employees; ``` |
| ``` lowercase ``` | Lowercase typeface indicates user-defined programmatic elements, such as names of tables, columns, or files.  Note: Some programmatic elements use a mixture of UPPERCASE and lowercase. Enter these elements as shown. | ``` SELECT last_name, employee_id FROM employees; sqlplus user_id/password CREATE USER mjones IDENTIFIED BY ty3MU9; ``` |