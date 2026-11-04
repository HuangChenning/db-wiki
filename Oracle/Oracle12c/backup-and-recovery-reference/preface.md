---
title: Database Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: E85640-04
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/rcmrf/preface.html
tags:
  - oracle
  - 12c
  - backup-and-recovery-reference
---

### Audience

Backup and Recovery Reference is intended for database administrators who perform the following tasks:

- Use Recovery Manager (RMAN) to back up, restore, and recover Oracle databases
- Perform maintenance on RMAN backups of database files

To use this document, you must know the following:

- Relational database concepts and basic database administration as described in [Oracle Database Concepts](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=CNCPT) and the [Oracle Database Administrator's Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=ADMIN)
- RMAN concepts and tasks as described in [Oracle Database Backup and Recovery User's Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=BRADV)
- The operating system environment under which you run Oracle Database

### Documentation Accessibility

For information about Oracle's commitment to accessibility, visit the Oracle Accessibility Program website at [http://www.oracle.com/pls/topic/lookup?ctx=acc&id=docacc](http://www.oracle.com/pls/topic/lookup?ctx=acc&id=docacc).

Access to Oracle Support

Oracle customers that have purchased support have access to electronic support through My Oracle Support. For information, visit [http://www.oracle.com/pls/topic/lookup?ctx=acc&id=info](http://www.oracle.com/pls/topic/lookup?ctx=acc&id=info) or visit [http://www.oracle.com/pls/topic/lookup?ctx=acc&id=trs](http://www.oracle.com/pls/topic/lookup?ctx=acc&id=trs) if you are hearing impaired.

### Conventions

The text in this reference adheres to the following conventions:

- `UPPERCASE` `monospace`
	RMAN keywords, SQL keywords, column headings in tables and views, and initialization parameters.
- `lowercase` `monospace`
	Variable text in RMAN examples.
- `italics`
	RMAN or SQL placeholders, that is, text that should not be entered as is, but represents a value to be entered by the user.

See Also:

[About RMAN Commands](about-rman-commands.md) for more information about RMAN conventions