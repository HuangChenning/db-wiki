---
title: "4.6.3 myisamchk — MyISAM Table-Maintenance Utility"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/myisamchk.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 4.6.3 myisamchk — MyISAM Table-Maintenance Utility

The **myisamchk** utility gets information about your database tables or checks, repairs, or optimizes them. **myisamchk** works with `MyISAM` tables (tables that have `.MYD` and `.MYI` files for storing data and indexes).

You can also use the [`CHECK TABLE`](check-table.md) and [`REPAIR TABLE`](repair-table.md) statements to check and repair `MyISAM` tables. See [Section 13.7.2.2, “CHECK TABLE Statement”](check-table.md), and [Section 13.7.2.5, “REPAIR TABLE Statement”](repair-table.md).

The use of **myisamchk** with partitioned tables is not supported.

Caution

It is best to make a backup of a table before performing a table repair operation; under some circumstances the operation might cause data loss. Possible causes include but are not limited to file system errors.

Invoke **myisamchk** like this:

```
myisamchk [options] tbl_name ...
```

The *`options`* specify what you want **myisamchk** to do. They are described in the following sections. You can also get a list of options by invoking **myisamchk --help**.

With no options, **myisamchk** simply checks your table as the default operation. To get more information or to tell **myisamchk** to take corrective action, specify options as described in the following discussion.

*`tbl_name`* is the database table you want to check or repair. If you run **myisamchk** somewhere other than in the database directory, you must specify the path to the database directory, because **myisamchk** has no idea where the database is located. In fact, **myisamchk** does not actually care whether the files you are working on are located in a database directory. You can copy the files that correspond to a database table into some other location and perform recovery operations on them there.

You can name several tables on the **myisamchk** command line if you wish. You can also specify a table by naming its index file (the file with the `.MYI` suffix). This enables you to specify all tables in a directory by using the pattern `*.MYI`. For example, if you are in a database directory, you can check all the `MyISAM` tables in that directory like this:

```
myisamchk *.MYI
```

If you are not in the database directory, you can check all the tables there by specifying the path to the directory:

```
myisamchk /path/to/database_dir/*.MYI
```

You can even check all tables in all databases by specifying a wildcard with the path to the MySQL data directory:

```
myisamchk /path/to/datadir/*/*.MYI
```

The recommended way to quickly check all `MyISAM` tables is:

```
myisamchk --silent --fast /path/to/datadir/*/*.MYI
```

If you want to check all `MyISAM` tables and repair any that are corrupted, you can use the following command:

```
myisamchk --silent --force --fast --update-state \
          --key_buffer_size=64M --myisam_sort_buffer_size=64M \
          --read_buffer_size=1M --write_buffer_size=1M \
          /path/to/datadir/*/*.MYI
```

This command assumes that you have more than 64MB free. For more information about memory allocation with **myisamchk**, see [Section 4.6.3.6, “myisamchk Memory Usage”](myisamchk-memory.md).

For additional information about using **myisamchk**, see [Section 7.6, “MyISAM Table Maintenance and Crash Recovery”](myisam-table-maintenance.md).

Important

*You must ensure that no other program is using the tables while you are running **myisamchk***. The most effective means of doing so is to shut down the MySQL server while running **myisamchk**, or to lock all tables that **myisamchk** is being used on.

Otherwise, when you run **myisamchk**, it may display the following error message:

```
warning: clients are using or haven't closed the table properly
```

This means that you are trying to check a table that has been updated by another program (such as the [**mysqld**](mysqld.md) server) that hasn't yet closed the file or that has died without closing the file properly, which can sometimes lead to the corruption of one or more `MyISAM` tables.

If [**mysqld**](mysqld.md) is running, you must force it to flush any table modifications that are still buffered in memory by using [`FLUSH TABLES`](flush.md). You should then ensure that no one is using the tables while you are running **myisamchk**

However, the easiest way to avoid this problem is to use [`CHECK TABLE`](check-table.md) instead of **myisamchk** to check tables. See [Section 13.7.2.2, “CHECK TABLE Statement”](check-table.md).

**myisamchk** supports the following options, which can be specified on the command line or in the `[myisamchk]` group of an option file. For information about option files used by MySQL programs, see [Section 4.2.2.2, “Using Option Files”](option-files.md).

**Table 4.21 myisamchk Options**

| Option Name | Description |
| --- | --- |
| [\--analyze](myisamchk-other-options.md) | Analyze the distribution of key values |
| [\--backup](myisamchk-repair-options.md) | Make a backup of the.MYD file as file\_name-time.BAK |
| [\--block-search](myisamchk-other-options.md) | Find the record that a block at the given offset belongs to |
| [\--character-sets-dir](myisamchk-repair-options.md) | Directory where character sets can be found |
| [\--check](myisamchk-check-options.md) | Check the table for errors |
| [\--check-only-changed](myisamchk-check-options.md) | Check only tables that have changed since the last check |
| [\--correct-checksum](myisamchk-repair-options.md) | Correct the checksum information for the table |
| [\--data-file-length](myisamchk-repair-options.md) | Maximum length of the data file (when re-creating data file when it is full) |
| [\--debug](myisamchk-general-options.md) | Write debugging log |
| \--decode\_bits | Decode\_bits |
| [\--defaults-extra-file](myisamchk-general-options.md) | Read named option file in addition to usual option files |
| [\--defaults-file](myisamchk-general-options.md) | Read only named option file |
| [\--defaults-group-suffix](myisamchk-general-options.md) | Option group suffix value |
| [\--description](myisamchk-other-options.md) | Print some descriptive information about the table |
| [\--extend-check](myisamchk-check-options.md) | Do very thorough table check or repair that tries to recover every possible row from the data file |
| [\--fast](myisamchk-check-options.md) | Check only tables that haven't been closed properly |
| [\--force](myisamchk-check-options.md) | Do a repair operation automatically if myisamchk finds any errors in the table |
| \--force | Overwrite old temporary files. For use with the -r or -o option |
| \--ft\_max\_word\_len | Maximum word length for FULLTEXT indexes |
| \--ft\_min\_word\_len | Minimum word length for FULLTEXT indexes |
| \--ft\_stopword\_file | Use stopwords from this file instead of built-in list |
| [\--HELP](myisamchk-general-options.md) | Display help message and exit |
| [\--help](myisamchk-general-options.md) | Display help message and exit |
| [\--information](myisamchk-check-options.md) | Print informational statistics about the table that is checked |
| \--key\_buffer\_size | Size of buffer used for index blocks for MyISAM tables |
| [\--keys-used](myisamchk-repair-options.md) | A bit-value that indicates which indexes to update |
| [\--max-record-length](myisamchk-repair-options.md) | Skip rows larger than the given length if myisamchk cannot allocate memory to hold them |
| [\--medium-check](myisamchk-check-options.md) | Do a check that is faster than an --extend-check operation |
| \--myisam\_block\_size | Block size to be used for MyISAM index pages |
| \--myisam\_sort\_buffer\_size | The buffer that is allocated when sorting the index when doing a REPAIR or when creating indexes with CREATE INDEX or ALTER TABLE |
| [\--no-defaults](myisamchk-general-options.md) | Read no option files |
| [\--parallel-recover](myisamchk-repair-options.md) | Uses the same technique as -r and -n, but creates all the keys in parallel, using different threads (beta) |
| [\--print-defaults](myisamchk-general-options.md) | Print default options |
| [\--quick](myisamchk-repair-options.md) | Achieve a faster repair by not modifying the data file |
| \--read\_buffer\_size | Each thread that does a sequential scan allocates a buffer of this size for each table it scans |
| [\--read-only](myisamchk-check-options.md) | Do not mark the table as checked |
| [\--recover](myisamchk-repair-options.md) | Do a repair that can fix almost any problem except unique keys that aren't unique |
| [\--safe-recover](myisamchk-repair-options.md) | Do a repair using an old recovery method that reads through all rows in order and updates all index trees based on the rows found |
| [\--set-auto-increment](myisamchk-other-options.md) | Force AUTO\_INCREMENT numbering for new records to start at the given value |
| [\--set-collation](myisamchk-repair-options.md) | Specify the collation to use for sorting table indexes |
| [\--silent](myisamchk-general-options.md) | Silent mode |
| \--sort\_buffer\_size | The buffer that is allocated when sorting the index when doing a REPAIR or when creating indexes with CREATE INDEX or ALTER TABLE |
| [\--sort-index](myisamchk-other-options.md) | Sort the index tree blocks in high-low order |
| \--sort\_key\_blocks | sort\_key\_blocks |
| [\--sort-records](myisamchk-other-options.md) | Sort records according to a particular index |
| [\--sort-recover](myisamchk-repair-options.md) | Force myisamchk to use sorting to resolve the keys even if the temporary files would be very large |
| \--stats\_method | Specifies how MyISAM index statistics collection code should treat NULLs |
| [\--tmpdir](myisamchk-repair-options.md) | Directory to be used for storing temporary files |
| [\--unpack](myisamchk-repair-options.md) | Unpack a table that was packed with myisampack |
| [\--update-state](myisamchk-check-options.md) | Store information in the.MYI file to indicate when the table was checked and whether the table crashed |
| [\--verbose](myisamchk-general-options.md) | Verbose mode |
| [\--version](myisamchk-general-options.md) | Display version information and exit |
| [\--wait](myisamchk-general-options.md) | Wait for locked table to be unlocked, instead of terminating |
| \--write\_buffer\_size | Write buffer size |