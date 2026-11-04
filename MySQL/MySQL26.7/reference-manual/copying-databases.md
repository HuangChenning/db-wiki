---
title: "MySQL :: MySQL 26.7 Reference Manual :: 3.15 Copying MySQL Databases to Another Machine"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/copying-databases.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

## 3.15 Copying MySQL Databases to Another Machine

In cases where you need to transfer databases between different architectures, you can use [**mysqldump**](mysqldump.md) to create a file containing SQL statements. You can then transfer the file to the other machine and feed it as input to the [**mysql**](mysql.md) client.

Use [**mysqldump --help**](mysqldump.md) to see what options are available.

Note

If GTIDs are in use on the server where you create the dump ([`gtid_mode=ON`](replication-options-gtids.md)), by default, [**mysqldump**](mysqldump.md) includes the contents of the [`gtid_executed`](replication-options-gtids.md) set in the dump to transfer these to the new machine. The results of this can vary depending on the MySQL Server versions involved. Check the description for **mysqldump's** `--set-gtid-purged` option to find what happens with the versions you are using, and how to change the behavior if the outcome of the default behavior is not suitable for your situation.

The easiest (although not the fastest) way to move a database between two machines is to run the following commands on the machine on which the database is located:

```svg
mysqladmin -h 'other_hostname' create db_name
mysqldump db_name | mysql -h 'other_hostname' db_name
```

If you want to copy a database from a remote machine over a slow network, you can use these commands:

```svg
mysqladmin create db_name
mysqldump -h 'other_hostname' --compress db_name | mysql db_name
```

You can also store the dump in a file, transfer the file to the target machine, and then load the file into the database there. For example, you can dump a database to a compressed file on the source machine like this:

```svg
mysqldump --quick db_name | gzip > db_name.gz
```

Transfer the file containing the database contents to the target machine and run these commands there:

```svg
mysqladmin create db_name
gunzip < db_name.gz | mysql db_name
```

You can also use [**mysqldump**](mysqldump.md) and [**mysqlimport**](mysqlimport.md) to transfer the database. For large tables, this is much faster than simply using [**mysqldump**](mysqldump.md). In the following commands, *`DUMPDIR`* represents the full path name of the directory you use to store the output from [**mysqldump**](mysqldump.md).

First, create the directory for the output files and dump the database:

```svg
mkdir DUMPDIR
mysqldump --tab=DUMPDIR
   db_name
```

Then transfer the files in the *`DUMPDIR`* directory to some corresponding directory on the target machine and load the files into MySQL there:

```svg
mysqladmin create db_name           # create database
cat DUMPDIR/*.sql | mysql db_name   # create tables in database
mysqlimport db_name
   DUMPDIR/*.txt   # load data into tables
```

Do not forget to copy the `mysql` database because that is where the grant tables are stored. You might have to run commands as the MySQL `root` user on the new machine until you have the `mysql` database in place.

After you import the `mysql` database on the new machine, execute [**mysqladmin flush-privileges**](mysqladmin.md) so that the server reloads the grant table information.