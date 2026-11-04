---
title: "MySQL :: MySQL 26.7 Reference Manual :: 10.12.2 Using Symbolic Links"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/symbolic-links.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 10.12.2 Using Symbolic Links

You can move databases or tables from the database directory to other locations and replace them with symbolic links to the new locations. You might want to do this, for example, to move a database to a file system with more free space or increase the speed of your system by spreading your tables to different disks.

For `InnoDB` tables, use the `DATA         DIRECTORY` clause of the [`CREATE         TABLE`](create-table.md) statement instead of symbolic links, as explained in [Section 17.6.1.2, “Creating Tables Externally”](innodb-create-table-external.md). This new feature is a supported, cross-platform technique.

The recommended way to do this is to symlink entire database directories to a different disk. Symlink `MyISAM` tables only as a last resort.

To determine the location of your data directory, use this statement:

```sql
SHOW VARIABLES LIKE 'datadir';
```