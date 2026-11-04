---
title: "What's New in Oracle Net Services?"
book: "Net Services Administrator's Guide"
doc_id: E41945-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e41945/whatsnew.htm
tags:
  - oracle
  - 11g
  - net-services-administrators-guide
---

This preface describes the new networking features of Oracle Database 11g and provides pointers to additional information.

## Oracle Database 11g Release 2 New Features in Oracle Net Services

The new features for Oracle Net Services in Oracle Database 11g Release 2 include:

- Internet Protocol Version 6 (IPv6) Addressing and Connectivity
	This feature includes the following enhancements:
	- IPv6 support for a single-instance database environment
		- Session layer abstraction to support listening across all IPv4 and IPv6 interfaces
	See Also:
	- ["TCP/IP Protocol"](layers.md) to learn about IPv6
	- ["About IPv6 Addresses in Connect Descriptors"](concepts.md)
	- ["Configuring Oracle Connection Manager as a Bridge for IPv4 and IPv6"](cman.md)
- Oracle Restart
	Oracle Restart enhances the availability of Oracle databases in a single-instance environment by restarting the database, the listener, and other Oracle components after a hardware or software failure or whenever your database host computer restarts. The components are started in the proper order, taking into consideration the dependencies among components.
	See Also:
	["About Oracle Restart"](net_arch.md)
- Support for `TRANSPORT_CONNECT_TIMEOUT` and `CONNECT_TIMEOUT` at the description level in the connect string. These timeouts apply to each IP address that resolves to a host name.
	- `TRANSPORT_CONNECT_TIMEOUT` specifies the time, in seconds, for a client to establish a TCP connection to the database server. The default value is 60 seconds.
		- `CONNECT_TIMEOUT` specifies the time, in seconds, for a client to establish an Oracle Net connection to the database instance. This parameter overrides the `SQLNET.OUTBOUND_CONNECT_TIMEOUT` parameter.
- CIDR and wildcard support for valid node checking.
	The valid node checking list can include CIDR notation for IPv4 and IPv6 addresses. Wildcard format (\*) is supported for IPv4 addresses.

## Oracle Database 11g Release 1 New Features in Oracle Net Services

The new features for Oracle Net Services in Oracle Database 11g Release 1 include:

- Enhanced Network Administration Security
	- Non-Anonymous LDAP Access for Net Naming
		Database administrators can now restrict access to a service by associating an access control list (ACL) with it. This feature can be used with installations that require an extremely high level of security.
		See ["Configuring the Directory Naming Method"](naming.md) and ["Configuring Database Access Control"](profile.md).
- Performance Improvements
	- New Oracle Net fastpath for the common usage scenarios significantly improves Oracle Net performance and is enabled by default in Oracle Database 11g. Users do not need to perform any configuration for this feature.
		- Efficient network support for bulk data transfers, such as SecureFiles LOBs. This feature eases the notion of session data unit (SDU) and optimizes large data transfers over an Oracle Net connection by using new paradigms.
		See ["Configuring Session Data Unit"](performance.md).
		- PHP Scalability
		This feature adds Oracle Net support for efficient event-dispatch mechanisms on platforms that support them. This is internally enabled for PHP usage scenarios and users do not need to perform any configuration for enabling this feature.
- Fast Reconnects for High Availability (HA)
	- This feature adds a mechanism for efficient detection of terminated nodes and connect time failover. Configurable timeouts have been implemented at various levels.
- Support for Database Resident Connection Pooling
	- This feature enables you to share connections or sessions between multiple middle-tier processes
		See Also:
		- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/dist_pro.htm#CNCPT1896) for additional information about database resident connection pooling
		- ["About Database Resident Connection Pooling"](concepts.md)
- Enhancements to the Easy Connect Naming Method
	For TCP/IP environments, you can simplify client configuration by using the Easy Connect naming method. The Easy Connect naming method simplifies network management by allowing clients to connect to Oracle Database services without first configuring net service names. Instead, clients make connections with the host name and optional port and service name of the database. See ["Using the Easy Connect Naming Method"](naming.md).