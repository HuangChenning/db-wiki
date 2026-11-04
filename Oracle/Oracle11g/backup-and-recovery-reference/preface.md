---
title: Preface
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/preface.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

This preface contains these topics:

## Audience

Backup and Recovery Reference is intended for database administrators who perform the following tasks:

- Use Recovery Manager (RMAN) to back up, restore, and recover Oracle databases
- Perform maintenance on RMAN backups of database files

To use this document, you must know the following:

- Relational database concepts and basic database administration as described in [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm) and the [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm)
- RMAN concepts and tasks as described in [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm)
- The operating system environment under which you run Oracle Database

## Documentation Accessibility

For information about Oracle's commitment to accessibility, visit the Oracle Accessibility Program website at `http://www.oracle.com/pls/topic/lookup?ctx=acc&id=docacc`.

Access to Oracle Support

Oracle customers that have purchased support have access to electronic support through My Oracle Support. For information, visit `http://www.oracle.com/pls/topic/lookup?ctx=acc&id=info` or visit `http://www.oracle.com/pls/topic/lookup?ctx=acc&id=trs` if you are hearing impaired.

## Related Documentation

For more information, see these Oracle resources:

- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm)
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm)
- [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/toc.htm)

Many of the examples in this book use the sample schemas of the seed database, which is installed by default when you install Oracle. Refer to [Oracle Database Sample Schemas](https://docs.oracle.com/cd/E11882_01/server.112/e10831/toc.htm) for information on how these schemas were created and how you can use them yourself.

## Conventions

The text in this reference adheres to the following conventions:

- `UPPERCASE` `monospace`
	Calls attention to RMAN keywords, SQL keywords, column headings in tables and views, and initialization parameters.
- `lowercase` `monospace`
	Calls attention to variable text in RMAN examples.
- `italics`
	Calls attention to RMAN or SQL placeholders, that is, text that should not be entered as-is but represents a value to be entered by the user.

See Also:

[Chapter 1, "About RMAN Commands"](rcmcomma.md) for more information about RMAN conventions