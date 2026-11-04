---
title: "5.1.12 IPv6 Support"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/ipv6-support.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 5.1.12 IPv6 Support

Support for IPv6 in MySQL includes these capabilities:

- MySQL Server can accept TCP/IP connections from clients connecting over IPv6. For example, this command connects over IPv6 to the MySQL server on the local host:
	```
	$> mysql -h ::1
	```
	To use this capability, two things must be true:
	- Your system must be configured to support IPv6. See [Section 5.1.12.1, “Verifying System Support for IPv6”](ipv6-system-support.md).
	- The default MySQL server configuration permits IPv6 connections in addition to IPv4 connections. To change the default configuration, start the server with the [`bind_address`](server-system-variables.md) system variable set to an appropriate value. See [Section 5.1.7, “Server System Variables”](server-system-variables.md).
- MySQL account names permit IPv6 addresses to enable DBAs to specify privileges for clients that connect to the server over IPv6. See [Section 6.2.4, “Specifying Account Names”](account-names.md). IPv6 addresses can be specified in account names in statements such as [`CREATE USER`](create-user.md), [`GRANT`](grant.md), and [`REVOKE`](revoke.md). For example:
	```
	mysql> CREATE USER 'bill'@'::1' IDENTIFIED BY 'secret';
	mysql> GRANT SELECT ON mydb.* TO 'bill'@'::1';
	```
- IPv6 functions enable conversion between string and internal format IPv6 address formats, and checking whether values represent valid IPv6 addresses. For example, [`INET6_ATON()`](miscellaneous-functions.md) and [`INET6_NTOA()`](miscellaneous-functions.md) are similar to [`INET_ATON()`](miscellaneous-functions.md) and [`INET_NTOA()`](miscellaneous-functions.md), but handle IPv6 addresses in addition to IPv4 addresses. See [Section 12.20, “Miscellaneous Functions”](miscellaneous-functions.md).

The following sections describe how to set up MySQL so that clients can connect to the server over IPv6.