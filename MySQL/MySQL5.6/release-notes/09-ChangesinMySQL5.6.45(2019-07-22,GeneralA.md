---
title: "Changes in MySQL 5.6.45 (2019-07-22, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=8"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

- Functionality Added or Changed
- Bugs Fixed

> Functionality Added or Changed

- Microsoft Windows: A new warning message now reminds DBAs that connections made using the

MySQL named pipe on Windows has limited the permissions a connector can request on the named pipe.

Previously, the `named_pipe_full_access_group` system variable was set to a value that maps to the built-in Windows `Everyone` group (SID S-1-1-0) by default. However, this group is not ideal and

## MySQL 5.6 Release Notes

should be replaced with a group that restricts its membership for connectors that are unable to request fewer permissions on the MySQL named pipe.

The new warning is written to the error log at startup if the string value assigned to`named_pipe_full_access_group` is `'*everyone*'` (or the Windows System Language equivalent)and named pipes are enabled. In addition, the warning is written to the error log and raised to the client if the system variable is reset to the `Everyone` group at runtime. (WL #12670)

> Bugs Fixed

- InnoDB: A query that scanned the primary key of a table did not return the expected result. (Bug

#28104394, Bug #91032)

- InnoDB: A full-text cache lock taken when data is synchronized was not released if the full-text cache

size exceeded the full-text cache size limit. (Bug #25289359)

- InnoDB: Client sessions using different `auto_increment_increment` values while performing

concurrent insert operations could cause a duplicate key error. (Bug #15851528, Bug #67526)References: Reverted patches: Bug #14049391, Bug #65225.

- Replication: In query log events in the binary log, the thread ID used for the execution of `DROP TABLE`

and `DELETE` statements was identified incorrectly or not at all. On a multi-threaded replication slave,where temporary tables were involved (which require the correct thread ID as they are session specific),this omission resulted in errors when using `mysqlbinlog` to replay the binary log for point-in-time recovery. The thread ID is now set correctly. (Bug #28642318, Bug #92398)

- Installing from RPM packages could result in an error log with incorrect permissions. (Bug #29702462)
- Enabling audit log encryption could cause a server exit. (Bug #29549327)
- MySQL Installer did not install OpenSSL DLL dependencies if the Development component was not

selected. (Bug #29423421, Bug #94168, Bug #30199579, Bug #96573)

- The parser could leak memory for certain multiple-statement queries. (Bug #29419820)
- MySQL does not support OpenSSL session tickets, but did not set the `SSL_OP_NO_TICKET` flag to

inform OpenSSL of that. The flag is now set. (Bug #27655493)

- `UpdateXML()` did not always free memory properly in certain cases. (Bug #27312862)
- Empty values in the `name` column of the `mysql.plugin` system table caused the server to exit during

startup. (Bug #27302459)

- Some `PROXY` grants were not replicated to slaves, causing incorrect replication. (Bug #23289541, Bug

#81424, Bug #23623115)

- If an `INSTALL PLUGIN` statement contained invalid UTF-8 characters in the shared library name, it

caused the server to hang (or to raise an assertion in debug builds). (Bug #14653594, Bug #23080148,Bug #27167197)
