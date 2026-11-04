---
title: SSL External Users Conversion Script
book: "Enterprise User Security Administrator's Guide"
doc_id: E10744-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e10744/appb.htm
tags:
  - oracle
  - 11g
  - enterprise-user-security-administrators-guide
---

## B SSL External Users Conversion Script

You should run the SSL external users conversion script after upgrading to Oracle Database 11g Release 2 (11.2), in case you were using SSL-authenticated external users in a pre-Oracle Database 10g Release 2 (10.2) release. The script converts SSL-authenticated external users in pre-Oracle Database 10g Release 2 (10.2) releases into SSL-authenticated external users in Oracle Database 11g Release 2 (11.2).

Note:

The SSL external users conversion script needs to be run only if you have upgraded from a pre-Oracle Database 10g Release 2 (10.2) release.

This chapter covers the following topics:

- Using the SSL External Users Conversion Script
- Converting Global Users into External Users

## B.1 Using the SSL External Users Conversion Script

The SSL external users conversion script has the following syntax:

```
$ORACLE_HOME/rdbms/bin/extusrupgrade
--dbconnectstring database connect string
--dbuser database user
--dbuserpassword database user password
[-a]
[-l username1,username2,...]
[-f filename]
[-o]
[-h]
```

The `database connect string` should be in the format `hostname`:`port_no`:`sid`, where `hostname` is the name of the host on which the database is running, `port_no` is the listener port number and `sid` is the system identifier for the database instance.

Use the `-a` option to convert all SSL-authenticated external users. Here is an example:

```
extusrupgrade --dbconnectstring mymachine:1521:11gR2 --dbuser system --dbuserpassword manager -a
```

Use the `-l` option to specify a comma-delimited list of users to be converted. For example:

```
extusrupgrade --dbconnectstring mymachine:1521:11gR2 --dbuser system --dbuserpassword manager -l user1,user2,user3
```

Use the `-f` option to specify a file that has the list of users to be converted. For example:

```
extusrupgrade --dbconnectstring mymachine:1521:11gR2 --dbuser system --dbuserpassword manager -f usernames.txt
```

There should be one user name in each line in the specified file. Here is a sample `usernames.txt` file:

```
user#1
user>2
user,3
user4
user5
```

You must use the `-f` option to convert users who have special characters (such as #) in their user names.

Note:

You can combine the `-l` and `-f` options in the same command. The script combines the list of users from both the `-l` and `-f` options. If you use the `-a` option along with the `-l option` and the `-f` option, then the `-a` option is ignored.

You can use the `-o` option to print a list of SSL-authenticated external users to the standard output device. The output lists the users you can convert using the extusrupgrade script. The `-o` option cannot be combined with any other option.

```
extusrupgrade --dbconnectstring mymachine:1521:11gR2 --dbuser system --dbuserpassword manager -o
```

A sample output for this could be:

```
user1
user2
user3
```

Tip:

You can redirect the command output to a file to get a list of users who can be converted. You can then edit the file and use it with the `-f` option.

## B.2 Converting Global Users into External Users

Oracle Database 10g and later allows SSL-authenticated external users and SSL-authenticated global users to coexist in the database. Previous releases had the restriction that all SSL users must be either global users or external users, depending on whether Oracle Internet Directory is being used or not for authenticating the users.

If you want a user to be able to connect to the database even when Oracle Internet Directory is not available, then the user should be configured as an external user. You can convert SSL-authenticated global users into SSL-authenticated external users by using the SSL external users conversion script.

For example:

```
extusrupgrade --dbconnectstring mymachine:1521:11gR2 --dbuser system --dbuserpassword manager -l user1,user2
```

The preceding example converts two global users into external users.