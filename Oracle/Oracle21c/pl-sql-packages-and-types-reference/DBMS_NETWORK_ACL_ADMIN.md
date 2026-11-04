---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_NETWORK_ACL_ADMIN.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 121 DBMS\_NETWORK\_ACL\_ADMIN

The `DBMS_NETWORK_ACL_ADMIN` package provides the interface to administer the network Access Control List (ACL).

The chapter contains the following topics:

See Also:

For more information, see ["Managing Fine-grained Access to External Network Services"](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=DBSEG40012) in Oracle Database Security Guide

### 121.1 DBMS\_NETWORK\_ACL\_ADMIN Overview

The `DBMS_NETWORK_ACL_ADMIN` package provides the interface to administer the network access control lists (ACL).

ACLs are used to control access by users to external network services and resources from the database through PL/SQL network utility packages including [UTL\_TCP](UTL_TCP.md) , [UTL\_HTTP](UTL_HTTP.md) , [UTL\_SMTP](UTL_SMTP.md) and [UTL\_INADDR](UTL_INADDR.md) .

### 121.2 DBMS\_NETWORK\_ACL\_ADMIN Deprecated Subprograms

Oracle recommends that you do not use deprecated subprograms in new applications. Support for deprecated features is for backward compatibility only

### 121.3 DBMS\_NETWORK\_ACL\_ADMIN Security Model

The `EXECUTE` privilege on the `DBMS_NETWORK_ACL_ADMIN` package is granted to the `DBA` role and to the `EXECUTE_CATALOG_ROLE` by default.

### 121.4 DBMS\_NETWORK\_ACL\_ADMIN Constants

The `DBMS_NETWORK_ACL_ADMIN` package defines constants to use specifying parameter values.

These are shown in the following table.

Table 121-1 DBMS\_NETWORK\_ACL\_ADMIN Constants

| Constant | Type | Value | Description |
| --- | --- | --- | --- |
| `IP_ADDR_MASK` | `VARCHAR2(80)` | `'([[:digit:]]+\.){3}[[:digit:]]+'` | IP address mask: `xxx.xxx.xxx.xxx` |
| `IP_SUBNET_MASK` | `VARCHAR2(80)` | ' `([[:digit:]]+\.){0,3}\*'` | IP subnet mask: `xxx.xxx...*` |
| `HOSTNAME_MASK` | `VARCHAR2(80)` | '\[` ^\.\:\/\*]+(\.[^\.\:\/\*]+)*'` | Hostname mask: ` ???.???.???...???` |
| `DOMAIN_MASK` | `VARCHAR2(80)` | ''\\\*(\\.\[^\\.\\:\\/\\\*\]+)\*' | Domain mask: `*.???.???...???` |

### 121.5 DBMS\_NETWORK\_ACL\_ADMIN Exceptions

The following table lists the exceptions raised by the ` DBMS_NETWORK_ACL_ADMIN` package.

Table 121-2 DBMS\_NETWORK\_ACL\_ADMIN Exceptions

| Exception | Error Code | Description |
| --- | --- | --- |
| `ACE_ALREADY_EXISTS` | `24243` | ACE already exists |
| `EMPTY_ACL` | `24246` | Empty ACL |
| `ACL_NOT_FOUND` | `46114` | ACL not found |
| `ACL_ALREADY_EXISTS` | `46212` | ACL already exists |
| `INVALID_ACL_PATH` | `46059` | Invalid ACL path |
| `INVALID_HOST` | `24244` | Invalid host |
| `INVALID_PRIVILEGE` | `24245` | Invalid privilege |
| `INVALID_WALLET_PATH` | `29248` | Invalid wallet path |
| `BAD_ARGUMENT` | `29261` | Bad argument |
| `UNRESOLVED_PRINCIPAL` | `46238` | Unresolved principal |
| `PRIVILEGE_NOT_GRANTED          ` | `01927` | Privilege not granted |

### 121.6 DBMS\_NETWORK\_ACL\_ADMIN Examples

Grant the `connect` and `resolve` privileges for host `www.us.example.com` to `SCOTT`.

Example1

```
DBMS_NETWORK_ACL_ADMIN.APPEND_HOST_ACE(
  host => 'www.us.example.com',
  ace  =>  xs$ace_type(privilege_list => xs$name_list('connect', 'resolve'),
                       principal_name => 'scott',
                       principal_type => xs_acl.ptype_db));
```

Example 2

Revoke the `resolve` privilege for host `www.us.example.com` from `SCOTT`.

```
dbms_network_acl_admin.remove_host_ace(
  host => 'www.us.example.com',
  ace  =>  xs$ace_type(privilege_list => xs$name_list('resolve'),
                       principal_name => 'scott',
                       principal_type => xs_acl.ptype_db));
```

Example 3

Grant the `use_client_certificates` and `use_passwords` privileges for wallet `file:/example/wallets/hr_wallet` to `SCOTT`.

```
dbms_network_acl_admin.append_wallet_ace(
  wallet_path => 'file:/example/wallets/hr_wallet',
  ace         =>  xs$ace_type(privilege_list => xs$name_list('use_client_certificates', 'use_passwords'),
                              principal_name => 'scott',
                              principal_type => xs_acl.ptype_db));
```

Example 4

Revoke the `use_passwords` privilege for wallet `file:/example/wallets/hr_wallet` from `SCOTT`.

```
dbms_network_acl_admin.remove_wallet_ace(
  wallet_path => 'file:/example/wallets/hr_wallet',
  ace         =>  xs$ace_type(privilege_list => xs$name_list('use_passwords'),
                              principal_name => 'scott',
                              principal_type => xs_acl.ptype_db));
```

Example 5

The `CONTAINS_HOST` in the `DBMS_NETWORK_ACL_UTLILITY` package determines if a host is contained in a domain. It can be used in conjunction with the `DBA_HOST_ACE` view to determine the users and their privilege assignments to access a network host.For example, for access to `www.us.example.com`:

```
SELECT HOST, LOWER_PORT, UPPER_PORT,
       ACE_ORDER, PRINCIPAL, PRINCIPAL_TYPE,
       GRANT_TYPE, INVERTED_PRINCIPAL, PRIVILEGE,
       START_DATE, END_DATE
  FROM (SELECT ACES.*,
DBMS_NETWORK_ACL_UTILITY.CONTAINS_HOST('www.us.example.com',
                                                      HOST) PRECEDENCE
          FROM DBA_HOST_ACES ACES)
 WHERE PRECEDENCE IS NOT NULL
 ORDER BY PRECEDENCE DESC,
          LOWER_PORT NULLS LAST,
          UPPER_PORT NULLS LAST,
          ACE_ORDER;
 
HOST               LOWER_PORT UPPER_PORT ACE_ORDER PRINCIPAL PRINCIPAL_TYPE   GRANT_TYPE INVERTED_PRINCIPAL PRIVILEGE START_DATE END_DATE
------------------ ---------- ---------- --------- --------- ---------------- ---------- ------------------ ---------- ---------- --------
www.us.example.com         80        80          1 SCOTT     DATABASE USER    GRANT      NO                 HTTP
www.us.example.com         80        80          2 ADAMS     DATABASE USER    GRANT      NO                 HTTP
*                                                1 HQ_DBA    DATABASE USER    GRANT      NO                 CONNECT
*                                                1 HQ_DBA    DATABASE USER    GRANT      NO                 RESOLVE
```

Example 6

For example, for `HQ_DBA` 's own permission to access to `www.us.example.com`:

```
SELECT HOST, LOWER_PORT, UPPER_PORT, PRIVILEGE, STATUS
  FROM (SELECT ACES.*,
DBMS_NETWORK_ACL_UTILITY.CONTAINS_HOST('www.us.example.com',
                                                      HOST) PRECEDENCE
          FROM USER_HOST_ACES ACES)
 WHERE PRECEDENCE IS NOT NULL
 ORDER BY PRECEDENCE DESC,
          LOWER_PORT NULLS LAST,
          UPPER_PORT NULLS LAST;
 
 
HOST               LOWER_PORT UPPER_PORT PRIVILEGE STATUS
------------------ ---------- ---------- --------- -------
*                                        CONNECT   GRANTED
*                                        RESOLVE   GRANTED
```

### 121.7 Summary of DBMS\_NETWORK\_ACL\_ADMIN Subprograms

This table lists and briefly describes the `DBMS_NETWORK_ACL_ADMIN` package subprograms.

Table 121-3 DBMS\_NETWORK\_ACL\_ADMIN Package Subprograms

| Subprogram | Description |
| --- | --- |
| ADD\_PRIVILEGE Procedure | \[DEPRECATED\] Adds a privilege to grant or deny the network access to the user in an access control list (ACL) |
| APPEND\_HOST\_ACE Procedure | Appends an access control entry (ACE) to the access control list (ACL) of a network host. |
| APPEND\_HOST\_ACL Procedure | Appends access control entries (ACE) of an access control list (ACL) to the ACL of a network host |
| APPEND\_WALLET\_ACE Procedure | Appends an access control entry (ACE) to the access control list (ACL) of a wallet |
| APPEND\_WALLET\_ACL Procedure | Appends access control entries (ACE) of an access control list (ACL) to the ACL of a wallet |
| ASSIGN\_ACL Procedure | \[DEPRECATED\] Assigns an access control list (ACL) to a host computer, domain, or IP subnet, and if specified, the TCP port range. |
| ASSIGN\_WALLET\_ACL Procedure | \[DEPRECATED\] Assigns an access control list (ACL) to a wallet |
| CHECK\_PRIVILEGE Function | \[DEPRECATED\] Checks if a privilege is granted or denied the user in an access control list (ACL) |
| CHECK\_PRIVILEGE\_ACLID Function | \[DEPRECATED\] Checks if a privilege is granted to or denied from the user in an ACL by specifying the object ID of the access control list |
| CREATE\_ACL Procedure | \[DEPRECATED\] Creates an access control list (ACL) with an initial privilege setting |
| DELETE\_PRIVILEGE Procedure | \[DEPRECATED\] Deletes a privilege in an access control list (ACL) |
| DROP\_ACL Procedure | \[DEPRECATED\] Drops an access control list (ACL) |
| REMOVE\_HOST\_ACE Procedure | Removes privileges from access control entries (ACE) in the access control list (ACL) of a network host matching the given ACE |
| REMOVE\_WALLET\_ACE Procedure | Removes privileges from access control entries (ACE) in the access control list (ACL) of a wallet matching the given ACE |
| SET\_HOST\_ACL Procedure | Sets the access control list (ACL) of a network host which controls access to the host from the database |
| SET\_WALLET\_ACL Procedure | Sets the access control list (ACL) of a wallet which controls access to the wallet from the database |
| UNASSIGN\_ACL Procedure | \[DEPRECATED\] Unassigns the access control list (ACL) currently assigned to a network host |
| UNASSIGN\_WALLET\_ACL Procedure | \[DEPRECATED\] Unassigns the access control list (ACL) currently assigned to a wallet |

#### 121.7.1 ADD\_PRIVILEGE Procedure

This procedure adds a privilege to grant or deny the network access to the user. The access control entry (ACE) is created if it does not exist.

Note:

This procedure is deprecated in Oracle Database 12c. While the procedure remains available in the package for reasons of backward compatibility, Oracle recommends using the APPEND\_HOST\_ACE Procedure and the APPEND\_WALLET\_ACE Procedure.

Syntax

```
DBMS_NETWORK_ACL_ADMIN.ADD_PRIVILEGE (
   acl             IN VARCHAR2,
   principal       IN VARCHAR2,
   is_grant        IN BOOLEAN,
   privilege       IN VARCHAR2,
   position        IN PLS_INTEGER DEFAULT NULL,
   start_date      IN TIMESTAMP WITH TIMESTAMP DEFAULT NULL,
   end_date        IN TIMESTAMP WITH TIMESTAMP DEFAULT NULL );
```

Parameters

Table 121-4 ADD\_PRIVILEGE Function Parameters

| Parameter | Description |
| --- | --- |
| `acl` | Name of the ACL. Relative path will be relative to "/sys/acls" |
| `principal` | Principal (database user or role) to whom the privilege is granted or denied. Case sensitive. |
| `is_grant` | Privilege is granted or denied. |
| `privilege` | Network privilege to be granted or denied |
| `position` | Position (1-based) of the ACE. If a non- `NULL` value is given, the privilege will be added in a new ACE at the given position and there should not be another ACE for the principal with the same `is_grant` (grant or deny). If a `NULL` value is given, the privilege will be added to the ACE matching the principal and the `is_grant` if one exists, or to the end of the ACL if the matching ACE does not exist. |
| `start_date` | Start date of the access control entry (ACE). When specified, the ACE will be valid only on and after the specified date. The `start_date` will be ignored if the privilege is added to an existing ACE. |
| `end_date` | End date of the access control entry (ACE). When specified, the ACE expires after the specified date. The `end_date` must be greater than or equal to the `start_date`. The `end_date` will be ignored if the privilege is added to an existing ACE. |

Usage Notes

To remove the permission, use the DELETE\_PRIVILEGE Procedure.

Examples

```
BEGIN
  DBMS_NETWORK_ACL_ADMIN.ADD_PRIVILEGE(
        acl         => 'us-example-com-permissions.xml',
        principal   => 'ST_USERS',
        is_grant    =>  TRUE,
        privilege   => 'connect')
END;
```

#### 121.7.2 APPEND\_HOST\_ACE Procedure

This procedure appends an access control entry (ACE) to the access control list (ACL) of a network host. The ACL controls access to the given host from the database and the ACE specifies the privileges granted to or denied from the specified principal.

Syntax

```
DBMS_NETWORK_ACL_ADMIN.APPEND_HOST_ACE (
   host         IN VARCHAR2,
   lower_port   IN PLS_INTEGER DEFAULT NULL,
   upper_port   IN PLS_INTEGER DEFAULT NULL,
   ace          IN XS$ACE_TYPE);
```

Parameters

Table 121-5 APPEND\_HOST\_ACE Function Parameters

| Parameter | Description |
| --- | --- |
| `host` | The host, which can be the name or the IP address of the host. You can use a wildcard to specify a domain or a IP subnet. The host or domain name is case-insensitive. |
| `lower_port` | Lower bound of an optional TCP port range |
| `upper_port` | Upper bound of an optional TCP port range. If `NULL`, `lower_port` is assumed. |
| `ace` | The ACE |

Usage Notes

- Duplicate privileges in the matching ACE in the host ACL will be skipped.
- To remove the ACE, use the REMOVE\_HOST\_ACE Procedure.
- A host's ACL takes precedence over its domains' ACLs. For a given host, say `www.us.example.com`, the following domains are listed in decreasing precedence:
	- `www.us.example.com`
		- `*.us.example.com`
		- `*.example.com`
		- `*.com`
		- `*`
- An IP address' ACL takes precedence over its subnets' ACLs. For a given IP address, say `192.168.0.100`, the following subnets are listed in decreasing precedence:
	- `192.168.0.100`
		- `192.168.0.*`
		- `192.168.*`
		- `192.*`
		- `*`
- An ACE with a "resolve" privilege can be appended only to a host's ACL without a port range.
- When ACEs with "connect" privileges are appended to a host's ACLs with and without a port range, the one appended to the host with a port range takes precedence.
- When specifying a TCP port range of a host, it cannot overlap with other existing port ranges of the host.
- If the ACL is shared with another host or wallet, a copy of the ACL will be made before the ACL is modified.

See Also:

[Oracle Database Real Application Security Administrator's and Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=DBFSG99821) for more information about the `XS$ACE_TYPE` object type

#### 121.7.3 APPEND\_HOST\_ACL Procedure

This procedure appends access control entries (ACE) of an access control list (ACL) to the ACL of a network host.

Syntax

```
DBMS_NETWORK_ACL_ADMIN.APPEND_HOST_ACL (
   host         IN VARCHAR2,
   lower_port   IN PLS_INTEGER DEFAULT NULL,
   upper_port   IN PLS_INTEGER DEFAULT NULL,
   acl          IN VARCHAR2);
```

Parameters

Table 121-6 APPEND\_HOST\_ACL Function Parameters

| Parameter | Description |
| --- | --- |
| `host` | The host, which can be the name or the IP address of the host. You can use a wildcard to specify a domain or a IP subnet. The host or domain name is case-insensitive. |
| `lower_port` | Lower bound of an optional TCP port range |
| `upper_port` | Upper bound of an optional TCP port range. If `NULL`, `lower_port` is assumed. |
| `acl` | The ACL from which to append |

Usage Notes

- Duplicate privileges in the matching ACE in the host ACL will be skipped.
- To remove the ACE, use the REMOVE\_HOST\_ACE Procedure.
- A host's ACL takes precedence over its domains' ACLs. For a given host, say `www.us.example.com`, the following domains are listed in decreasing precedence:
	- `www.us.example.com`
		- `*.us.example.com`
		- `*.example.com`
		- `*.com`
		- `*`
- An IP address' ACL takes precedence over its subnets' ACLs. For a given IP address, say `192.168.0.100`, the following subnets are listed in decreasing precedence:
	- `192.168.0.100`
		- `192.168.0.*`
		- `192.168.*`
		- `192.*`
		- `*`
- An ACE with a "resolve" privilege can be appended only to a host's ACL without a port range.
- When ACEs with "connect" privileges are appended to a host's ACLs with and without a port range, the one appended to the host with a port range takes precedence.
- When specifying a TCP port range of a host, it cannot overlap with other existing port ranges of the host.- If the ACL is shared with another host or wallet, a copy of the ACL will be made before the ACL is modified.

#### 121.7.4 APPEND\_WALLET\_ACE Procedure

This procedure appends an access control entry (ACE) to the access control list (ACL) of a wallet. The ACL controls access to the given wallet from the database and the ACE specifies the privileges granted to or denied from the specified principal.

Syntax

```
DBMS_NETWORK_ACL_ADMIN.APPEND_WALLET_ACE (
   wallet_path    IN VARCHAR2,
   ace            IN XS$ACE_TYPE);
```

Parameters

Table 121-7 APPEND\_WALLET\_ACE Function Parameters

| Parameter | Description |
| --- | --- |
| `wallet_path` | Directory path of the wallet. The path is case-sensitive of the format `file:``directory-path`. |
| `ace` | The ACE |

Usage Notes

- Duplicate privileges in the matching ACE in the host ACL will be skipped.
- To remove the ACE, use the REMOVE\_WALLET\_ACE Procedure.
- If the ACL is shared with another host or wallet, a copy of the ACL is made before the ACL is modified.

#### 121.7.5 APPEND\_WALLET\_ACL Procedure

This procedure appends access control entries (ACE) of an access control list (ACL) to the ACL of a wallet.

Syntax

```
DBMS_NETWORK_ACL_ADMIN.APPEND_WALLET_ACL (
   wallet_path    IN VARCHAR2,
   acl            IN VARCHAR2);
```

Parameters

Table 121-8 APPEND\_WALLET\_ACL Function Parameters

| Parameter | Description |
| --- | --- |
| `wallet_path` | Directory path of the wallet. The path is case-sensitive of the format `file:``directory-path`. |
| `ace` | The ACL from which to append |

Usage Notes

- Duplicate privileges in the matching ACE in the host ACL will be skipped.
- To remove the ACE, use REMOVE\_WALLET\_ACE.
- If the ACL is shared with another host or wallet, a copy of the ACL is made before the ACL is modified.

#### 121.7.6 ASSIGN\_ACL Procedure

This procedure assigns an access control list (ACL) to a host computer, domain, or IP subnet, and if specified, the TCP port range.

Note:

This procedure is deprecated in Oracle Database 12c. While the procedure remains available in the package for reasons of backward compatibility, Oracle recommends using the APPEND\_HOST\_ACE Procedure and the APPEND\_WALLET\_ACE Procedure.

Syntax

```
DBMS_NETWORK_ACL_ADMIN.ASSIGN_ACL (
   acl         IN VARCHAR2,
   host        IN VARCHAR2,
   lower_port  IN PLS_INTEGER DEFAULT NULL,
   upper_port  IN PLS_INTEGER DEFAULT NULL);
```

Parameters

Table 121-9 ASSIGN\_ACL Function Parameters

| Parameter | Description |
| --- | --- |
| `acl` | Name of the ACL. Relative path will be relative to " `/sys/acls` ". |
| `host` | Host to which the ACL is to be assigned. The host can be the name or the IP address of the host. A wildcard can be used to specify a domain or a IP subnet. The host or domain name is case-insensitive. |
| `lower_port` | Lower bound of a TCP port range if not `NULL` |
| `upper_port` | Upper bound of a TCP port range. If `NULL`, `lower_port` is assumed. |

Usage Notes

- Only one ACL can be assigned to any host computer, domain, or IP subnet, and if specified, the TCP port range. When you assign a new access control list to a network target, Oracle Database unassigns the previous access control list that was assigned to the same target. However, Oracle Database does not drop the access control list. You can drop the access control list by using the DROP\_ACL Procedure. To remove an access control list assignment, use the UNASSIGN\_ACL Procedure.
- The ACL assigned to a domain takes a lower precedence than the other ACLs assigned sub-domains, which take a lower precedence than the ACLs assigned to the individual hosts. So for a given host, for example, "www.us.example.com", the following domains are listed in decreasing precedences:
	\- www.us.example.com
	\- \*.us.example.com
	\- \*.example.com
	\- \*.com
	\- \*
	In the same way, the ACL assigned to an subnet takes a lower precedence than the other ACLs assigned smaller subnets, which take a lower precedence than the ACLs assigned to the individual IP addresses. So for a given IP address, for example, "192.168.0.100", the following subnets are listed in decreasing precedences:
	\- 192.168.0.100
	\- 192.168.0.\*
	\- 192.168.\*
	\- 192.\*
	\- \*
- The port range is applicable only to the "connect" privilege assignments in the ACL. The "resolve" privilege assignments in an ACL have effects only when the ACL is assigned to a host without a port range.
	For the "connect" privilege assignments, an ACL assigned to the host without a port range takes a lower precedence than other ACLs assigned to the same host with a port range.
- When specifying a TCP port range, both `lower_port` and `upper_port` must not be `NULL` and `upper_port` must be greater than or equal to `lower_port`. The port range must not overlap with any other port ranges for the same host assigned already.
- To remove the assignment, use UNASSIGN\_ACL Procedure.

Examples

```
BEGIN
   DBMS_NETWORK_ACL_ADMIN.ASSIGN_ACL(
     acl         => 'us-example-com-permissions.xml',
     host        => '*.us.example.com',
     lower_port  => 80);
END;
```

#### 121.7.7 ASSIGN\_WALLET\_ACL Procedure

This procedure assigns an access control list (ACL) to a wallet.

Note:

This procedure is deprecated in Oracle Database 12c. While the procedure remains available in the package for reasons of backward compatibility, Oracle recommends using the APPEND\_HOST\_ACE Procedure and the APPEND\_WALLET\_ACE Procedure.

Syntax

```
UTL_HTTP.ASSIGN_WALLET_ACL (
   acl          IN  VARCHAR2,
   wallet_path  IN  VARCHAR2);
```

Parameters

Table 121-10 ASSIGN\_WALLET\_ACL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `acl` | Name of the ACL. Relative path will be relative to `"/sys/acls` " |
| `wallet_path` | Directory path of the wallet to which the ACL is to be assigned. The path is case-sensitive and of the format `file:``directory-path`. |

Usage Notes

To remove the assignment, use the UNASSIGN\_WALLET\_ACL Procedure.

Examples

```
BEGIN
  DBMS_NETWORK_ACL_ADMIN.CREATE_ACL(
    acl         => 'wallet-acl.xml', 
    description => 'Wallet ACL',
    principal   => 'SCOTT',
    is_grant    => TRUE,
    privilege   => 'use-client-certificates');
 
  DBMS_NETWORK_ACL_ADMIN.ADD_PRIVILEGE(
    acl         => 'wallet-acl.xml', 
    principal   => 'SCOTT',
    is_grant    => TRUE,
    privilege   => 'use-passwords');
 
  DBMS_NETWORK_ACL_ADMIN.ASSIGN_WALLET_ACL(
    acl         => 'wallet-acl.xml', 
    wallet_path => 'file:/example/wallets/test_wallet');
END;
```

#### 121.7.8 CHECK\_PRIVILEGE Function

This function checks if a privilege is granted or denied the user in an ACL.

Note:

This procedure is deprecated in Oracle Database 12c. The procedure remains available in the package only for reasons of backward compatibility.

Syntax

```
DBMS_NETWORK_ACL_ADMIN.CHECK_PRIVILEGE (
   acl             IN VARCHAR2,
   user            IN VARCHAR2,
   privilege       IN VARCHAR2)
  RETURN NUMBER;
```

Parameters

Table 121-11 CHECK\_PRIVILEGE Function Parameters

| Parameter | Description |
| --- | --- |
| `acl` | Name of the ACL. Relative path will be relative to "/sys/acls". |
| `user` | User to check against. If the user is `NULL`, the invoker is assumed. The username is case-sensitive as in the `USERNAME` column of the `ALL_USERS` view. |
| `privilege` | Network privilege to check |

Return Values

Returns 1 when the privilege is granted; 0 when the privilege is denied; `NULL` when the privilege is neither granted or denied.

Examples

```
SELECT DECODE(
  DBMS_NETWORK_ACL_ADMIN.CHECK_PRIVILEGE(
       'us-example-com-permissions.xml', 'SCOTT', 'resolve'),
  1, 'GRANTED', 0, 'DENIED', NULL) PRIVILEGE 
FROM DUAL;
```

#### 121.7.9 CHECK\_PRIVILEGE\_ACLID Function

This function checks if a privilege is granted to or denied from the user in an ACL by specifying the object ID of the access control list.

Note:

This procedure is deprecated in Oracle Database 12c. The procedure remains available in the package only for reasons of backward compatibility.

Syntax

```
DBMS_NETWORK_ACL_ADMIN.CHECK_PRIVILEGE_ACLID (
   aclid           IN RAW,
   user            IN VARCHAR2 DEFAULT NULL)
   privilege       IN VARCHAR2,
 RETURN NUMBER;
```

Parameters

Table 121-12 CHECK\_PRIVILEGE\_ACLID Function Parameters

| Parameter | Description |
| --- | --- |
| `aclid` | Object ID of the ACL |
| `user` | User to check against. If the user is `NULL`, the invoker is assumed. The username is case-sensitive as in the `USERNAME` column of the `ALL_USERS` view. |
| `privilege` | Network privilege to check |

Return Values

Returns 1 when the privilege is granted; 0 when the privilege is denied; `NULL` when the privilege is neither granted or denied.

#### 121.7.10 CREATE\_ACL Procedure

This deprecated procedure creates an access control list (ACL) with an initial privilege setting. An ACL must have at least one privilege setting. The ACL has no access control effect unless it is assigned to the network target.

Note:

This procedure is deprecated in Oracle Database 12c. While the procedure remains available in the package for reasons of backward compatibility, Oracle recommends using the APPEND\_HOST\_ACE Procedure and the APPEND\_WALLET\_ACE Procedure.

Syntax

```
DBMS_NETWORK_ACL_ADMIN.CREATE_ACL (
   acl             IN VARCHAR2,
   description     IN VARCHAR2,
   principal       IN VARCHAR2,
   is_grant        IN BOOLEAN,
   privilege       IN VARCHAR2,
   start_date      IN TIMESTAMP WITH TIMEZONE DEFAULT NULL,
   end_date        IN TIMESTAMP WITH TIMEZONE DEFAULT NULL );
```

Parameters

Table 121-13 CREATE\_ACL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `acl` | Name of the ACL. Relative path will be relative to "/sys/acls". |
| `description` | Description attribute in the ACL |
| `principal` | Principal (database user or role) to whom the privilege is granted or denied. Case sensitive. |
| `is_grant` | Privilege is granted or not (denied) |
| `privilege` | Network privilege to be granted or denied - `'connect` \| `resolve'` (case sensitive). A database user needs the `connect` privilege to an external network host computer if he or she is connecting using the `UTL_TCP`, `UTL_HTTP`, `UTL_SMTP`, and `UTL_MAIL` utility packages. To resolve a host name that was given a host IP address, or the IP address that was given a host name, with the `UTL_INADDR` package, grant the database user the `resolve` privilege. |
| `start_date` | Start date of the access control entry (ACE). When specified, the ACE is valid only on and after the specified date. |
| `end_date` | End date of the access control entry (ACE). When specified, the ACE expires after the specified date. The `end_date` must be greater than or equal to the `start_date`. |

Usage Notes

To drop the access control list, use the DROP\_ACL Procedure.

Examples

```
BEGIN
  DBMS_NETWORK_ACL_ADMIN.CREATE_ACL(
     acl          => 'us-example-com-permissions.xml',
     description  => 'Network permissions for *.us.example.com',
     principal    => 'SCOTT',
     is_grant     => TRUE,
     privilege    => 'connect');
END;
```

#### 121.7.11 DELETE\_PRIVILEGE Procedure

This deprecated procedure deletes a privilege in an access control list.

Note:

This procedure is deprecated in Oracle Database 12c. While the procedure remains available in the package for reasons of backward compatibility, Oracle recommends using the REMOVE\_HOST\_ACE Procedure and the REMOVE\_WALLET\_ACE Procedure.

Syntax

```
DBMS_NETWORK_ACL_ADMIN.DELETE_PRIVILEGE (
   acl           IN VARCHAR2,
   principal     IN VARCHAR2,
   is_grant      IN BOOLEAN DEFAULT NULL,
   privilege     IN VARCHAR2 DEFAULT NULL);
```

Parameters

Table 121-14 DELETE\_PRIVILEGE Function Parameters

| Parameter | Description |
| --- | --- |
| `acl` | Name of the ACL. Relative path will be relative to "/sys/acls". |
| `principal` | Principal (database user or role) for whom all the ACE will be deleted |
| `is_grant` | Privilege is granted or not (denied). If a `NULL` value is given, the deletion is applicable to both granted or denied privileges. |
| `privilege` | Network privilege to be deleted. If a `NULL` value is given, the deletion is applicable to all privileges. |

Examples

```
BEGIN
  DBMS_NETWORK_ACL_ADMIN.DELETE_PRIVILEGE(
        acl         => 'us-example-com-permissions.xml',
        principal   => 'ST_USERS')
END;
```

#### 121.7.12 DROP\_ACL Procedure

This deprecated procedure drops an access control list (ACL).

Note:

This procedure is deprecated in Oracle Database 12c. The procedure remains available in the package only for reasons of backward compatibility.

Syntax

```
DBMS_NETWORK_ACL_ADMIN.DROP_ACL (
   acl           IN VARCHAR2);
```

Parameters

Table 121-15 DROP\_ACL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `acl` | Name of the ACL. Relative path will be relative to "/sys/acls". |

Examples

```
BEGIN
   DBMS_NETWORK_ACL_ADMIN.DROP_ACL(
      acl => 'us-example-com-permissions.xml');
END;
```

#### 121.7.13 REMOVE\_HOST\_ACE Procedure

This procedure removes privileges from access control entries (ACE) in the access control list (ACL) of a network host matching the given ACE.

Syntax

```
DBMS_NETWORK_ACL_ADMIN.REMOVE_HOST_ACE (
   host               IN VARCHAR2,
   lower_port         IN PLS_INTEGER DEFAULT NULL,
   upper_port         IN PLS_INTEGER DEFAULT NULL,
   ace                IN XS$ACE_TYPE,
   remove_empty_acl   IN BOOLEAN DEFAULT FALSE);
```

Parameters

Table 121-16 REMOVE\_HOST\_ACE Function Parameters

| Parameter | Description |
| --- | --- |
| `host` | The host, which can be the name or the IP address of the host. You can use a wildcard to specify a domain or a IP subnet. The host or domain name is case-insensitive. |
| `lower_port` | Lower bound of an optional TCP port range |
| `upper_port` | Upper bound of an optional TCP port range. If `NULL`, `lower_port` is assumed. |
| `ace` | The ACE |
| `remove_empty_acl` | Whether to remove the ACL when it becomes empty when the ACE is removed |

Usage Notes

If the ACL is shared with another host or wallet, a copy of the ACL is made before the ACL is modified.

#### 121.7.14 REMOVE\_WALLET\_ACE Procedure

This procedure removes privileges from access control entries (ACE) in the access control list (ACL) of a wallet matching the given ACE.

Syntax

```
DBMS_NETWORK_ACL_ADMIN.REMOVE_WALLET_ACE (
   wallet_path        IN VARCHAR2,
   ace                IN XS$ACE_TYPE,
   remove_empty_acl   IN BOOLEAN DEFAULT FALSE);
```

Parameters

Table 121-17 REMOVE\_WALLET\_ACE Function Parameters

| Parameter | Description |
| --- | --- |
| `wallet_path` | Directory path of the wallet. The path is case-sensitive of the format `file:``directory-path`. |
| `ace` | The ACE |
| `remove_empty_acl` | Whether to remove the ACL when it becomes empty when the ACE is removed |

Usage Notes

If the ACL is shared with another host or wallet, a copy of the ACL is made before the ACL is modified.

#### 121.7.15 SET\_HOST\_ACL Procedure

This procedure sets the access control list (ACL) of a network host which controls access to the host from the database.

Syntax

```
DBMS_NETWORK_ACL_ADMIN.SET_HOST_ACL (
   host         IN VARCHAR2,
   lower_port   IN PLS_INTEGER DEFAULT NULL,
   upper_port   IN PLS_INTEGER DEFAULT NULL,
   acl          IN VARCHAR2);
```

Parameters

Table 121-18 SET\_HOST\_ACL Function Parameters

| Parameter | Description |
| --- | --- |
| `host` | The host, which can be the name or the IP address of the host. You can use a wildcard to specify a domain or a IP subnet. The host or domain name is case-insensitive. |
| `lower_port` | Lower bound of an optional TCP port range |
| `upper_port` | Upper bound of an optional TCP port range. If `NULL`, `lower_port` is assumed. |
| `acl` | The ACL. `NULL` to unset the host's ACL. |

Usage Notes

A host's ACL is created and set on-demand when an access control entry (ACE) is appended to the host's ACL. Users are discouraged from setting a host's ACL manually.

#### 121.7.16 SET\_WALLET\_ACL Procedure

This procedure sets the access control list (ACL) of a wallet which controls access to the wallet from the database.

Syntax

```
DBMS_NETWORK_ACL_ADMIN.SET_WALLET_ACL (
   wallet_path    IN VARCHAR2,
   acl            IN VARCHAR2);
```

Parameters

Table 121-19 SET\_WALLET\_ACL Function Parameters

| Parameter | Description |
| --- | --- |
| `wallet_path` | Directory path of the wallet. The path is case-sensitive of the format `file:``directory-path`. |
| `acl` | The ACL. `NULL` to unset the host's ACL. |

Usage Notes

A wallet's ACL is created and set on-demand when an access control entry (ACE) is appended to the wallet's ACL. Users are discouraged from setting a wallet's ACL manually.

#### 121.7.17 UNASSIGN\_ACL Procedure

This deprecated procedure unassigns the access control list (ACL) currently assigned to a network host.

Note:

This procedure is deprecated in Oracle Database 12c. While the procedure remains available in the package for reasons of backward compatibility, Oracle recommends using the REMOVE\_HOST\_ACE Procedure and the REMOVE\_WALLET\_ACE Procedure.

Syntax

```
DBMS_NETWORK_ACL_ADMIN.UNASSIGN_ACL (
   acl         IN VARCHAR2 DEFAULT NULL,
   host        IN VARCHAR2 DEFAULT NULL,
   lower_port  IN PLS_INTEGER DEFAULT NULL,
   upper_port  IN PLS_INTEGER DEFAULT NULL);
```

Parameters

Table 121-20 UNASSIGN\_ACL Function Parameters

| Parameter | Description |
| --- | --- |
| `acl` | Name of the ACL. Relative path will be relative to "/sys/acls". If ACL is `NULL`, any ACL assigned to the host is unassigned. |
| `host` | Host from which the ACL is to be removed. The host can be the name or the IP address of the host. A wildcard can be used to specify a domain or a IP subnet. The host or domain name is case-insensitive. If host is `NULL`, the ACL will be unassigned from any host. If both `host` and `acl` are `NULL`, all ACLs assigned to any hosts are unassigned. |
| `lower_port` | Lower bound of a TCP port range if not `NULL` |
| `upper_port` | Upper bound of a TCP port range. If `NULL`, `lower_port` is assumed. |

Examples

```
BEGIN
   DBMS_NETWORK_ACL_ADMIN.UNASSIGN_ACL(
     host        => '*.us.example.com',
     lower_port  => 80);
END;
```

#### 121.7.18 UNASSIGN\_WALLET\_ACL Procedure

This deprecated procedure unassigns the access control list (ACL) currently assigned to a wallet.

Note:

This procedure is deprecated in Oracle Database 12c. While the procedure remains available in the package for reasons of backward compatibility, Oracle recommends using the REMOVE\_HOST\_ACE Procedure and the REMOVE\_WALLET\_ACE Procedure.

Syntax

```
UTL_HTTP.UNASSIGN_WALLET_ACL (
   acl          IN  VARCHAR2 DEFAULT NULL,
   wallet_path  IN  VARCHAR2 DEFAULT NULL);
```

Parameters

Table 121-21 UNASSIGN\_WALLET\_ACL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `acl` | Name of the ACL. Relative path will be relative to `"/sys/acls"`. If `acl` is `NULL`, any ACL assigned to the wallet is unassigned |
| `wallet_path` | Directory path of the wallet to which the ACL is assigned. The path is case-sensitive and of the format `file`:`directory-path`. If both `acl` and `wallet_path` are `NULL`, all ACLs assigned to any wallets are unassigned. |

Examples

```
BEGIN
  DBMS_NETWORK_ACL_ADMIN.UNASSIGN_WALLET_ACL(
    acl         => 'wallet-acl.xml', 
    wallet_path => 'file:/example/wallets/test_wallet');
END;
```