---
title: Preface
book: "JDBC Developer's Guide"
doc_id: E16548-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/java.112/e16548/preface.htm
tags:
  - oracle
  - 11g
  - jdbc-developers-guide
---

This preface introduces you to the Oracle Database JDBC Developer's Guide discussing the intended audience, structure, and conventions of this document. A list of related Oracle documents is also provided.

This preface covers the following topics:

## Audience

The Oracle Database JDBC Developer's Guide is intended for developers of Java Database Connectivity (JDBC)-based applications and applets. This book can be read by anyone with an interest in JDBC programming, but assumes at least some prior knowledge of the following:

- Java
- Oracle PL/SQL
- Oracle databases

## Documentation Accessibility

For information about Oracle's commitment to accessibility, visit the Oracle Accessibility Program website at `http://www.oracle.com/pls/topic/lookup?ctx=acc&id=docacc`.

Access to Oracle Support

Oracle customers have access to electronic support through My Oracle Support. For information, visit `http://www.oracle.com/pls/topic/lookup?ctx=acc&id=info` or visit `http://www.oracle.com/pls/topic/lookup?ctx=acc&id=trs` if you are hearing impaired.

Accessibility of Links to External Web Sites in Documentation

This documentation may contain links to Web sites of other companies or organizations that Oracle does not own or control. Oracle neither evaluates nor makes any representations regarding the accessibility of these Web sites.

Deaf/Hard of Hearing Access to Oracle Support Services

To reach Oracle Support Services, use a telecommunications relay service (TRS) to call Oracle Support at 1.800.223.1711. An Oracle Support Services engineer will handle technical issues and provide customer support according to the Oracle service request process. Information about TRS is available at `http://www.fcc.gov/cgb/consumerfacts/trs.html`, and a list of phone numbers is available at `http://www.fcc.gov/cgb/dro/trsphonebk.html`.

## Related Documents

The following books are also available from the Oracle Java Platform group:

- [Oracle Database Java Developer's Guide](https://docs.oracle.com/cd/E11882_01/java.112/e10588/toc.htm)
	This book introduces the basic concepts of Java and provides general information about server-side configuration and functionality. Information that pertains to the Oracle Java platform as a whole, rather than to a particular product (such as JDBC) is in this book. This book also discusses Java stored procedures, which were formerly discussed in a standalone book.
- [Oracle Database JPublisher User's Guide](https://docs.oracle.com/cd/E11882_01/java.112/e10587/toc.htm)
	This book describes how to use the Oracle JPublisher utility to translate object types and other user-defined types to Java classes. If you are developing JDBC applications that use object types, VARRAY types, nested table types, or object reference types, then JPublisher can generate custom Java classes to map to them.

The following OC4J documents, for Oracle Application Server releases, are also available from the Oracle Java Platform group:

- [Oracle Application Server Containers for J2EE User's Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=JIUSR)
	This book provides some overview and general information for OC4J; primer chapters for servlets, JSP pages, and EJBs; and general configuration and deployment instructions.
- [Oracle Containers for J2EE Support for JavaServer Pages Developer's Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=JIJSP)
	This book provides information for JSP developers who want to run their pages in OC4J. It includes a general overview of JSP standards and programming considerations, as well as discussion of Oracle value-added features and steps for getting started in the OC4J environment.
- [Oracle Containers for J2EE JSP Tag Libraries and Utilities Reference](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=JIJSU)
	This book provides conceptual information and detailed syntax and usage information for tag libraries, JavaBeans, and other Java utilities provided with OC4J.
- [Oracle Containers for J2EE Servlet Developer's Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=JISVL)
	This book provides information for servlet developers regarding use of servlets and the servlet container in OC4J. It also documents relevant OC4J configuration files.
- [Oracle Containers for J2EE Services Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=JISVC)
	This book provides information about basic Java services supplied with OC4J, such as JTA, JNDI, and the Oracle Application Server Java Object Cache.
- [Oracle Containers for J2EE Enterprise JavaBeans Developer's Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=JIEJB)
	This book provides information about the EJB implementation and EJB container in OC4J.

The following documents are from the Oracle Server Technologies group:

- [Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/toc.htm)
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm)
- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/toc.htm)
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm)
- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm)
- [Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm)
- [Oracle Database Error Messages](https://docs.oracle.com/cd/E11882_01/server.112/e17766/toc.htm)

The following documents from the Oracle Application Server group may also be of some interest:

- [Oracle Application Server Administrator's Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=ASADM)
- [Oracle Fusion Middleware Administrator's Guide for Oracle HTTP Server](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=HSADM)
- [Oracle Fusion Middleware Performance Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=ASPER)
- [Oracle Fusion Middleware Application Globalization Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=ASNLS)
- [Oracle Fusion Middleware Administrator's Guide for Oracle Web Cache](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=OWCAG)
- [Oracle Fusion Middleware Upgrade Planning Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=ASMAS)

The following are available from the JDeveloper group:

- Oracle JDeveloper online help
- Oracle JDeveloper documentation on the Oracle Technology Network:
	`http://www.oracle.com/technetwork/developer-tools/jdev/overview/index.html`

Printed documentation is available for sale in the Oracle Store at:

`http://oraclestore.oracle.com/`

To download free release notes, installation documentation, white papers, or other collateral, visit the Oracle Technology Network (OTN). You must register online before using OTN; registration is free and can be done at

`http://www.oracle.com/technetwork/community/join/overview/index.html`

If you already have a user name and password for OTN, then you can go directly to the documentation section of the OTN Web site at

`http://www.oracle.com/technetwork/documentation/index.html`

The following resources are available from Sun Microsystems:

- Web site for JDBC, including the latest specifications:
	`http://www.oracle.com/technetwork/java/javase/jdbc/index.html`

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
| Italics | Italic typeface indicates book titles or emphasis. | Oracle Database  Ensure that the recovery catalog and target database do not reside on the same disk. |
| `UPPERCASE monospace (fixed-width) font` | Uppercase monospace typeface indicates elements supplied by the system. Such elements include parameters, privileges, data types, RMAN keywords, SQL keywords, SQL\*Plus or utility commands, packages and methods, as well as system-supplied column names, database objects and structures, user names, and roles. | You can specify this clause only for a `NUMBER` column.  You can back up the database by using the `BACKUP` command.  Query the `TABLE_NAME` column in the `USER_TABLES` data dictionary view.  Use the `DBMS_STATS`.`GENERATE_STATS` procedure. |
| `lowercase monospace (fixed-width) font` | Lowercase monospace typeface indicates executables, filenames, directory names, and sample user-supplied elements. Such elements include computer and database names, net service names, and connect identifiers, as well as user-supplied database objects and structures, column names, packages and classes, user names and roles, program units, and parameter values.  Note: Some programmatic elements use a mixture of UPPERCASE and lowercase. Enter these elements as shown. | Enter `sqlplus` to start SQL\*Plus.  The password is specified in the `orapwd` file.  Back up the datafiles and control files in the `/disk1/oracle/dbs` directory.  The `department_id`, `department_name`, and `location_id` columns are in the `hr.departments` table.  Set the `QUERY_REWRITE_ENABLED` initialization parameter to `true.`  Connect as `oe` user.  The `JRepUtil` class implements these methods. |
| `lowercase italic monospace (fixed-width) font` | Lowercase italic monospace font represents placeholders or variables. | You can specify the `parallel_clause`.  Run `old_release``.SQL` where `old_release` refers to the release you installed prior to upgrading. |

Conventions in Code Examples

Code examples illustrate Java, SQL, and command-line statements. Examples are displayed in a monospace (fixed-width) font and separated from normal text as shown in this example:

```
SELECT username FROM dba_users WHERE username = 'MIGRATE';
```

The following table describes typographic conventions used in code examples and provides examples of their use.

| Convention | Meaning | Example |
| --- | --- | --- |
| ``` [ ] ``` | Brackets enclose one or more optional items. Do not enter the brackets. | ``` DECIMAL (digits [ , precision ]) ``` |
| ``` { } ``` | Braces enclose two or more items, one of which is required. Do not enter the braces. | ``` {ENABLE \| DISABLE} ``` |
| ``` \| ``` | A vertical bar represents a choice of two or more options within brackets or braces. Enter one of the options. Do not enter the vertical bar. | ``` {ENABLE \| DISABLE} [COMPRESS \| NOCOMPRESS] ``` |
| ``` ... ``` | Horizontal ellipsis points indicate either: - That we have omitted parts of the code that are not directly related to the example - That you can repeat a portion of the code | ``` CREATE TABLE ... AS subquery;  SELECT col1, col2, ... , coln FROM employees; ``` |
| ``` . . . ``` | Vertical ellipsis points indicate that we have omitted several lines of code not directly related to the example. | ``` SQL> SELECT NAME FROM V$DATAFILE; NAME ------------------------------------ /fsl/dbs/tbs_01.dbf /fs1/dbs/tbs_02.dbf . . . /fsl/dbs/tbs_09.dbf 9 rows selected. ``` |
| Other notation | You must enter symbols other than brackets, braces, vertical bars, and ellipsis points as shown. | ``` acctbal NUMBER(11,2); acct    CONSTANT NUMBER(4) := 3; ``` |
| ``` Italics ``` | Italicized text indicates placeholders or variables for which you must supply particular values. | ``` CONNECT SYSTEM/system_password DB_NAME = database_name ``` |
| ``` UPPERCASE ``` | Uppercase typeface indicates elements supplied by the system. We show these terms in uppercase in order to distinguish them from terms you define. Unless terms appear in brackets, enter them in the order and with the spelling shown. However, because these terms are not case sensitive, you can enter them in lowercase. | ``` SELECT last_name, employee_id FROM employees; SELECT * FROM USER_TABLES; DROP TABLE hr.employees; ``` |
| ``` lowercase ``` | Lowercase typeface indicates programmatic elements that you supply. For example, lowercase indicates names of tables, columns, or files.  Note: Some programmatic elements use a mixture of UPPERCASE and lowercase. Enter these elements as shown. | ``` SELECT last_name, employee_id FROM employees; sqlplus hr/hr CREATE USER mjones IDENTIFIED BY ty3MU9; ``` |

Conventions for Windows Operating Systems

The following table describes conventions for Windows operating systems and provides examples of their use.

| Convention | Meaning | Example |
| --- | --- | --- |
| Choose Start > | How to start a program. | To start the Database Configuration Assistant, choose Start > Programs > Oracle - HOME\_NAME > Configuration and Migration Tools > Database Configuration Assistant. |
| File and directory names | File and directory names are not case sensitive. The following special characters are not allowed: left angle bracket (<), right angle bracket (>), colon (:), double quotation marks ("), slash (/), pipe (\|), and dash (-). The special character backslash (\\) is treated as an element separator, even when it appears in quotes. If the file name begins with \\\\, then Windows assumes it uses the Universal Naming Convention. | ``` c:\winnt"\"system32 is the same as C:\WINNT\SYSTEM32 ``` |
| `C:\>` | Represents the Windows command prompt of the current hard disk drive. The escape character in a command prompt is the caret (^). Your prompt reflects the subdirectory in which you are working. Referred to as the command prompt in this manual. | ``` C:\oracle\oradata> ``` |
| Special characters | The backslash (\\) special character is sometimes required as an escape character for the double quotation mark (") special character at the Windows command prompt. Parentheses and the single quotation mark (') do not require an escape character. Refer to your Windows operating system documentation for more information on escape and special characters. | ``` C:\>exp scott/tiger TABLES=emp QUERY=\"WHERE job='SALESMAN' and sal<1600\" C:\>imp SYSTEM/password FROMUSER=scott TABLES=(emp, dept) ``` |
| ``` HOME_NAME ``` | Represents the Oracle home name. The home name can be up to 16 alphanumeric characters. The only special character allowed in the home name is the underscore. | ``` C:\> net start OracleHOME_NAMETNSListener ``` |
| `ORACLE_HOME` and `ORACLE_BASE` | In releases prior to Oracle8i release 8.1.3, when you installed Oracle components, all subdirectories were located under a top level `ORACLE_HOME` directory that by default used one of the following names: - `C:\orant` for Windows NT - `C:\orawin98` for Windows 98  This release complies with Optimal Flexible Architecture (OFA) guidelines. All subdirectories are not under a top level `ORACLE_HOME` directory. There is a top level directory called `ORACLE_BASE` that by default is `C:\oracle`. If you install the latest Oracle release on a computer with no other Oracle software installed, then the default setting for the first Oracle home directory is `C:\oracle\ora` `nn`, where `nn` is the latest release number. The Oracle home directory is located directly under `ORACLE_BASE`.  All directory path examples in this guide follow OFA conventions.  Refer to Oracle Database Platform Guide for Microsoft Windows for additional information about OFA compliances and for information about installing Oracle products in non-OFA compliant directories. | Go to the `ORACLE_BASE` `\` `ORACLE_HOME` `\rdbms\admin` directory. |