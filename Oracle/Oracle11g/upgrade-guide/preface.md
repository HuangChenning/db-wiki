---
title: Preface
book: Upgrade Guide
doc_id: E23633-11
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e23633/preface.htm
tags:
  - oracle
  - 11g
  - upgrade-guide
---

This manual guides you through the process of planning and executing Oracle Database upgrades. In addition, this manual provides information about compatibility, upgrading applications, and important changes in the new Oracle Database release, such as initialization parameter changes and data dictionary changes.

Oracle Database Upgrade Guide contains information that describes the features and functions of Oracle Database (also known as the standard edition) and Oracle Database Enterprise Edition products. Oracle Database and Oracle Database Enterprise Edition have the same basic features. However, several advanced features are available only with the Enterprise Edition, and some of these are optional. For example, to use application failover, you must have the Enterprise Edition with the Oracle Real Application Clusters option.

See Also:

[Oracle Database New Features Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41360/toc.htm) for information about the differences between Oracle Database and Oracle Database Enterprise Edition and the features and options that are available to you.

This preface contains these topics:

## Audience

Oracle Database Upgrade Guide is intended for database administrators (DBAs), application developers, security administrators, system operators, and anyone who plans or executes Oracle Database upgrades.

To use this document, you must be familiar with the following:

- Relational database concepts
- Your current release of Oracle Database
- Your operating system environment

## Documentation Accessibility

For information about Oracle's commitment to accessibility, visit the Oracle Accessibility Program website at `http://www.oracle.com/pls/topic/lookup?ctx=acc&id=docacc`.

Access to Oracle Support

Oracle customers have access to electronic support through My Oracle Support. For information, visit `http://www.oracle.com/pls/topic/lookup?ctx=acc&id=info` or visit `http://www.oracle.com/pls/topic/lookup?ctx=acc&id=trs` if you are hearing impaired.

## Related Documentation

For more information, see these Oracle resources:

- "Oracle Upgrade Companion" Note ID 785351.1 on My Oracle Support at `https://support.oracle.com`.
- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm) for a comprehensive introduction to the concepts and terminology used in this manual
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for information about administering Oracle Database
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for information on Oracle Database SQL commands and functions
- [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/toc.htm) for information about utilities bundled with Oracle Database, including Data Pump, Export, Import, and SQL\*Loader
- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for information about Oracle Net Services
- [Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e10744/toc.htm) for information about Oracle Label Security
- [Oracle Database High Availability Best Practices](https://docs.oracle.com/cd/E11882_01/server.112/e10803/schedule_outage.htm#HABPT02323) for Oracle operational best practices and help choosing an upgrade method that minimizes downtime.

Many of the examples in this guide use the sample schemas, which are installed by default when you select the Basic Installation option with an Oracle Database installation. Refer to [Oracle Database Sample Schemas](https://docs.oracle.com/cd/E11882_01/server.112/e10831/toc.htm) for information on how these schemas were created and how you can use them yourself.

## Conventions

The following text conventions are used in this document:

| Convention | Meaning |
| --- | --- |
| boldface | Boldface type indicates graphical user interface elements associated with an action, or terms defined in text or the glossary. |
| italic | Italic type indicates book titles, emphasis, or placeholder variables for which you supply particular values. |
| `monospace` | Monospace type indicates commands within a paragraph, URLs, code in examples, text that appears on the screen, or text that you enter. |