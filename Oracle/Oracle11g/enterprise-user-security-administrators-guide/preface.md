---
title: Preface
book: "Enterprise User Security Administrator's Guide"
doc_id: E10744-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e10744/preface.htm
tags:
  - oracle
  - 11g
  - enterprise-user-security-administrators-guide
---

Welcome to the Oracle Database Enterprise User Security Administrator's Guide for the 11g Release 2 (11.2) Oracle Database.

Oracle Database contains a comprehensive suite of security features that protect your data. These features include database privileges, roles, and integration with the Oracle Identity Management infrastructure for identity management services. Identity management refers to the process by which the complete security lifecycle—account creation, suspension, modification, and deletion—for network entities is managed by an organization.

The Oracle Database Enterprise User Security Administrator's Guide describes how to implement, configure, and administer Oracle Database users in Oracle Internet Directory, the directory service provided by the Oracle Identity Management platform.

This preface contains these topics:

## Intended Audience

The Oracle Database Enterprise User Security Administrator's Guide is intended for security administrators, DBAs, and application developers who perform one or more of the following tasks:

- Manage database users and privileges
- Provision database users
- Develop PL/SQL applications for enterprise users

To use this document, you need a working knowledge of SQL and Oracle fundamentals. You should also be familiar with Oracle security features described in "Related Documents".

## Documentation Accessibility

For information about Oracle's commitment to accessibility, visit the Oracle Accessibility Program website at `http://www.oracle.com/pls/topic/lookup?ctx=acc&id=docacc`.

Access to Oracle Support

Oracle customers have access to electronic support through My Oracle Support. For information, visit `http://www.oracle.com/pls/topic/lookup?ctx=acc&id=info` or visit `http://www.oracle.com/pls/topic/lookup?ctx=acc&id=trs` if you are hearing impaired.

## Related Documents

For more information, see these Oracle resources:

- [Oracle Internet Directory Administrator's Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=OIDAG)
- [Oracle Identity Management User Reference Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=OIMUR)
- [Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)
- [Oracle Database 2 Day DBA](https://docs.oracle.com/cd/E11882_01/server.112/e10897/toc.htm)
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm)
- [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/toc.htm)
- [Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/toc.htm)
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm)
- [Oracle Database SQL Language Quick Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41085/toc.htm)
- [Oracle Database Error Messages](https://docs.oracle.com/cd/E11882_01/server.112/e17766/toc.htm)
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm)
- [Oracle Database Heterogeneous Connectivity User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e11050/toc.htm)
- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm)

Many of the examples in this book use the sample schemas, which are installed by default when you select the Basic Installation option with an Oracle Database installation. Refer to [Oracle Database Sample Schemas](https://docs.oracle.com/cd/E11882_01/server.112/e10831/toc.htm) for information on how these schemas were created and how you can use them yourself.

To download free release notes, installation documentation, white papers, or other collateral, please visit the Oracle Technology Network (OTN). You must register online before using OTN; registration is free and can be done at

```
http://www.oracle.com/technetwork/community/join/overview/
```

If you already have a username and password for OTN, then you can go directly to the documentation section of the OTN Web site at

```
http://www.oracle.com/technetwork/indexes/documentation/
```

For conceptual information about the security technologies supported by Enterprise User Security, you can refer to the following third-party publications:

- Applied Cryptography, Second Edition: Protocols, Algorithms, and Source Code in C by Bruce Schneier. New York: John Wiley & Sons, 1996.
- SSL & TLS Essentials: Securing the Web by Stephen A. Thomas. New York: John Wiley & Sons, 2000.
- Understanding and Deploying LDAP Directory Services by Timothy A. Howes, Ph.D., Mark C. Smith, and Gordon S. Good. Indianapolis: New Riders Publishing, 1999.
- Understanding Public-Key Infrastructure: Concepts, Standards, and Deployment Considerations by Carlisle Adams and Steve Lloyd. Indianapolis: New Riders Publishing, 1999.

## Conventions

This section describes the conventions used in the text and code examples of this documentation set. It describes:

- Conventions in Text
- Conventions in Code Examples
- Conventions for Windows Operating Systems

Conventions in Text

We use various conventions in text to help you more quickly identify special terms. The following table describes those conventions and provides examples of their use.

| Convention | Meaning | Example |
| --- | --- | --- |
| Bold | Bold typeface indicates terms that are defined in the text or terms that appear in a glossary, or both. | When you specify this clause, you create an index-organized table. |
| Italics | Italic typeface indicates book titles or emphasis. | Oracle Database Concepts  Ensure that the recovery catalog and target database do not reside on the same disk. |
| `UPPERCASE monospace (fixed-width) font` | Uppercase monospace typeface indicates elements supplied by the system. Such elements include parameters, privileges, datatypes, RMAN keywords, SQL keywords, SQL\*Plus or utility commands, packages and methods, as well as system-supplied column names, database objects and structures, usernames, and roles. | You can specify this clause only for a `NUMBER` column.  You can back up the database by using the `BACKUP` command.  Query the `TABLE_NAME` column in the `USER_TABLES` data dictionary view.  Use the `DBMS_STATS`.`GENERATE_STATS` procedure. |
| `lowercase monospace (fixed-width) font` | Lowercase monospace typeface indicates executable programs, filenames, directory names, and sample user-supplied elements. Such elements include computer and database names, net service names and connect identifiers, user-supplied database objects and structures, column names, packages and classes, usernames and roles, program units, and parameter values.  Note: Some programmatic elements use a mixture of UPPERCASE and lowercase. Enter these elements as shown. | Enter `sqlplus` to start SQL\*Plus.  The password is specified in the `orapwd` file.  Back up the datafiles and control files in the `/disk1/oracle/dbs` directory.  The `department_id`, `department_name`, and `location_id` columns are in the `hr.departments` table.  Set the `QUERY_REWRITE_ENABLED` initialization parameter to `true.`  Connect as `oe` user.  The `JRepUtil` class implements these methods. |
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
| ``` Italics ``` | Italicized text indicates placeholders or variables for which you must supply particular values. | ``` CONNECT SYSTEM Enter password: password DB_NAME = database_name ``` |
| ``` UPPERCASE ``` | Uppercase typeface indicates elements supplied by the system. We show these terms in uppercase in order to distinguish them from terms you define. Unless terms appear in brackets, enter them in the order and with the spelling shown. Because these terms are not case sensitive, you can use them in either UPPERCASE or lowercase. | ``` SELECT last_name, employee_id FROM employees; SELECT * FROM USER_TABLES; DROP TABLE hr.employees; ``` |
| ``` lowercase ``` | Lowercase typeface indicates user-defined programmatic elements, such as names of tables, columns, or files.  Note: Some programmatic elements use a mixture of UPPERCASE and lowercase. Enter these elements as shown. | ``` SELECT last_name, employee_id FROM employees; sqlplus hr/hr CREATE USER mjones IDENTIFIED BY ty3MU9; ``` |

Conventions for Windows Operating Systems

The following table describes conventions for Windows operating systems and provides examples of their use.

| Convention | Meaning | Example |
| --- | --- | --- |
| Choose Start > menu item | How to start a program. | To start the Database Configuration Assistant, choose Start > Programs > Oracle - HOME\_NAME > Configuration and Migration Tools > Database Configuration Assistant. |
| File and directory names | File and directory names are not case sensitive. The following special characters are not allowed: left angle bracket (<), right angle bracket (>), colon (:), double quotation marks ("), slash (/), pipe (\|), and dash (-). The special character backslash (\\) is treated as an element separator, even when it appears in quotes. If the filename begins with \\\\, then Windows assumes it uses the Universal Naming Convention. | c:\\winnt"\\"system32 is the same as C:\\WINNT\\SYSTEM32 |
| `C:\>` | Represents the Windows command prompt of the current hard disk drive. The escape character in a command prompt is the caret (^). Your prompt reflects the subdirectory in which you are working. Referred to as the command prompt in this manual. | ``` C:\oracle\oradata> ``` |
| Special characters | The backslash (\\) special character is sometimes required as an escape character for the double quotation mark (") special character at the Windows command prompt. Parentheses and the single quotation mark (') do not require an escape character. Refer to your Windows operating system documentation for more information on escape and special characters. | ``` C:\>exp HR/HR TABLES=employees QUERY=\"WHERE job_id='SA_REP' and salary<8000\" ``` |
| ``` HOME_NAME ``` | Represents the Oracle home name. The home name can be up to 16 alphanumeric characters. The only special character allowed in the home name is the underscore. | ``` C:\> net start OracleHOME_NAMETNSListener ``` |
| `ORACLE_HOME` and `ORACLE_BASE` | In releases prior to Oracle8i release 8.1.3, when you installed Oracle components, all subdirectories were located under a top level `ORACLE_HOME` directory. The default for Windows was `C:\orant`.  This release complies with Optimal Flexible Architecture (OFA) guidelines. All subdirectories are not under a top level `ORACLE_HOME` directory. There is a top level directory called `ORACLE_BASE` that by default is `C:\oracle\product\10.1.0`. If you install the latest Oracle release on a computer with no other Oracle software installed, then the default setting for the first Oracle home directory is `C:\oracle\product\10.1.0\db_` `n`, where `n` is the latest Oracle home number. The Oracle home directory is located directly under `ORACLE_BASE`.  All directory path examples in this guide follow OFA conventions.  Refer to [Oracle Database Installation Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/install.112/e47798/toc.htm) for additional information about OFA compliances and for information about installing Oracle products in non-OFA compliant directories. | Go to the `ORACLE_BASE` `\` `ORACLE_HOME` `\rdbms\admin` directory. |