---
title: "Chapter 5 Tutorial"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/tutorial.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

This chapter provides a tutorial introduction to MySQL by showing how to use the [**mysql**](mysql.md) client program to create and use a simple database. [**mysql**](mysql.md) (sometimes referred to as the “terminal monitor” or just “monitor”) is an interactive program that enables you to connect to a MySQL server, run queries, and view the results. [**mysql**](mysql.md) may also be used in batch mode: you place your queries in a file beforehand, then tell [**mysql**](mysql.md) to execute the contents of the file. Both ways of using [**mysql**](mysql.md) are covered here.

To see a list of options provided by [**mysql**](mysql.md), invoke it with the [`--help`](mysql-command-options.md) option:

```
$> mysql --help
```

This chapter assumes that [**mysql**](mysql.md) is installed on your machine and that a MySQL server is available to which you can connect. If this is not true, contact your MySQL administrator. (If *you* are the administrator, you need to consult the relevant portions of this manual, such as [Chapter 7, *MySQL Server Administration*](server-administration.md).)

This chapter describes the entire process of setting up and using a database. If you are interested only in accessing an existing database, you may want to skip the sections that describe how to create the database and the tables it contains.

Because this chapter is tutorial in nature, many details are necessarily omitted. Consult the relevant sections of the manual for more information on the topics covered here.