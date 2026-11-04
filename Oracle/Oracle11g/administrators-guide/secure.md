---
title: Managing Users and Securing the Database
book: "Administrator's Guide"
doc_id: E25494-07
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e25494/secure.htm
tags:
  - oracle
  - 11g
  - administrators-guide
---

## 7 Managing Users and Securing the Database

In this chapter:

## The Importance of Establishing a Security Policy for Your Database

It is important to develop a security policy for every database. The security policy establishes methods for protecting your database from accidental or malicious destruction of data or damage to the database infrastructure.

Each database can have an administrator, referred to as the security administrator, who is responsible for implementing and maintaining the database security policy If the database system is small, the database administrator can have the responsibilities of the security administrator. However, if the database system is large, a designated person or group of people may have sole responsibility as security administrator.

For information about establishing security policies for your database, see [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/guidelines.htm#DBSEG009).

## Managing Users and Resources

To connect to the database, each user must specify a valid user name that has been previously defined to the database. An account must have been established for the user, with information about the user being stored in the data dictionary.

When you create a database user (account), you specify the following attributes of the user:

- User name
- Authentication method
- Default tablespace
- Temporary tablespace
- Other tablespaces and quotas
- User profile

To learn how to create and manage users, see [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/users.htm#DBSEG002).

## Managing User Privileges and Roles

Privileges and roles are used to control user access to data and the types of SQL statements that can be executed. The table that follows describes the three types of privileges and roles:

| Type | Description |
| --- | --- |
| System privilege | A system-defined privilege usually granted only by administrators. These privileges allow users to perform specific database operations. |
| Object privilege | A system-defined privilege that controls access to a specific object. |
| Role | A collection of privileges and other roles. Some system-defined roles exist, but most are created by administrators. Roles group together privileges and other roles, which facilitates the granting of multiple privileges and roles to users. |

Privileges and roles can be granted to other users by users who have been granted the privilege to do so. The granting of roles and privileges starts at the administrator level. At database creation, the administrative user `SYS` is created and granted all system privileges and predefined Oracle Database roles. User `SYS` can then grant privileges and roles to other users, and also grant those users the right to grant specific privileges to others.

To learn how to administer privileges and roles for users, see [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authorization.htm#DBSEG004).

## Auditing Database Activity

You can monitor and record selected user database actions, including those performed by administrators. There are several reasons why you might want to implement database auditing. Complete background information and instructions for database auditing are found in [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/auditing.htm#DBSEG006).

## Predefined User Accounts

Oracle Database includes several predefined user accounts. The three types of predefined accounts are:

- Administrative accounts (`SYS`, `SYSTEM`, `SYSMAN`, and `DBSNMP`)
	`SYS` and `SYSTEM` are described in ["About Database Administrator Security and Privileges"](dba.md). `SYSMAN` is used to perform Oracle Enterprise Manager administration tasks. The management agent of Enterprise Manager uses the `DBSNMP` account to monitor and manage the database. You must not delete these accounts.
- Sample schema accounts
	These accounts are used for examples in Oracle Database documentation and instructional materials. Examples are `HR`, `SH`, and `OE`. You must unlock these accounts and reset their passwords before using them.
- Internal accounts.
	These accounts are created so that individual Oracle Database features or components can have their own schemas. You must not delete internal accounts, and you must not attempt to log in with them.

See Also:

[Oracle Database 2 Day + Security Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10575/tdpsg_user_accounts.htm#TDPSG20030) for a table of predefined accounts.