---
title: Preface
book: "SQL*Plus User's Guide and Reference"
doc_id: E16604-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e16604/preface.htm
tags:
  - oracle
  - 11g
  - sqlplus-users-guide-and-reference
---

The SQL\*Plus (pronounced "sequel plus") User's Guide and Reference introduces SQL\*Plus and its uses, and provides a description of each SQL\*Plus command.

This preface contains these topics:

## Audience

The SQL\*Plus User's Guide and Reference is intended for business and technical users and system administrators who perform the following tasks:

- Develop and run batch scripts
- Format, calculate on, store, print and create web output from query results
- Examine table and object definitions
- Perform database administration

This document assumes a basic understanding of the SQL language. If you do not have familiarity with SQL, see the [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm). If you plan to use PL/SQL in conjunction with SQL\*Plus, see the [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/toc.htm).

## Documentation Accessibility

For information about Oracle's commitment to accessibility, visit the Oracle Accessibility Program website at `http://www.oracle.com/pls/topic/lookup?ctx=acc&id=docacc`.

Access to Oracle Support

Oracle customers have access to electronic support through My Oracle Support. For information, visit `http://www.oracle.com/pls/topic/lookup?ctx=acc&id=info` or visit `http://www.oracle.com/pls/topic/lookup?ctx=acc&id=trs` if you are hearing impaired.

## Related Documents

For more information, see these Oracle resources:

- [SQL\*Plus Quick Reference](https://docs.oracle.com/cd/E11882_01/server.112/e16605/toc.htm)
- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/toc.htm)
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm)
- [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/toc.htm)
- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm)
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm)
- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm)
- [Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/toc.htm)
- [Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/toc.htm)
- [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm)
- [Oracle Database Heterogeneous Connectivity Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e11050/toc.htm)
- [Oracle Database Error Messages](https://docs.oracle.com/cd/E11882_01/server.112/e17766/toc.htm)
- [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm)
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm)
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm)
- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm)
- [Pro\*COBOL Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10826/toc.htm)
- [Pro\*C/C++ Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10825/toc.htm)
- Oracle Database installation and user's manuals for your operating system

Many of the examples in this book use the sample schemas, which are installed by default when you select the Basic Installation option with an Oracle Database installation. See [Oracle Database Sample Schemas](https://docs.oracle.com/cd/E11882_01/server.112/e10831/toc.htm) for information on how these schemas were created and how you can use them yourself.

SQL\*Plus error message documentation is available in [SQL\*Plus Error Messages](ch_thirteen.md). Oracle Database error message documentation is only available in HTML. If you only have access to the Oracle Database Documentation media, you can browse the Oracle Database error messages by range. Once you find the specific range, use your browser's "find in page" feature to locate the specific message. When connected to the Internet, you can search for a specific error message using the error message search feature of the Oracle Database online documentation.

## Conventions

The following text conventions are used in this document:

| Convention | Meaning |
| --- | --- |
| boldface | Boldface type indicates graphical user interface elements associated with an action, or terms defined in text or the glossary. |
| italic | Italic type indicates book titles, emphasis, or placeholder variables for which you supply particular values. |
| `monospace` | Monospace type indicates commands within a paragraph, URLs, code in examples, text that appears on the screen, or text that you enter. |