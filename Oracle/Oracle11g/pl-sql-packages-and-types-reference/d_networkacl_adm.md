---
title: DBMS_NETWORK_ACL_ADMIN
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_networkacl_adm.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 94 DBMS\_NETWORK\_ACL\_ADMIN

The `DBMS_NETWORK_ACL_ADMIN` package provides the interface to administer the network Access Control List (ACL).

See Also:

For more information, see ["Managing Fine-grained Access to External Network Services"](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authorization.htm#DBSEG40012) in Oracle Database Security Guide

The chapter contains the following topics:

- Using DBMS\_NETWORK\_ACL\_ADMIN
	- Examples
- Summary of DBMS\_NETWORK\_ACL\_ADMIN Subprograms

---

## Using DBMS\_NETWORK\_ACL\_ADMIN

- Examples

---

### Examples

Example1

Grant the connect and resolve privileges for host www.us.oracle.com to SCOTT.

```
BEGIN
  DBMS_NETWORK_ACL_ADMIN.CREATE_ACL(acl         => 'www.xml',
                                    description => 'WWW ACL',
                                    principal   => 'SCOTT',
                                    is_grant    => true,
                                    privilege   => 'connect');
 
  DBMS_NETWORK_ACL_ADMIN.ADD_PRIVILEGE(acl       => 'www.xml',
                                       principal => 'SCOTT',
                                       is_grant  => true,
                                       privilege => 'resolve');
 
  DBMS_NETWORK_ACL_ADMIN.ASSIGN_ACL(acl  => 'www.xml',
                                    host => 'www.us.oracle.com');
END;
/
COMMIT;
```

Example 2

Grant the resolve privilege for www.us.oracle.com to ADAMS. Since an ACL for www.us.oracle.com exists already, just add the privilege for ADAMS.

```
BEGIN
  DBMS_NETWORK_ACL_ADMIN.ADD_PRIVILEGE(acl       => 'www.xml',
                                       principal => 'ADAMS',
                                       is_grant  => true,
                                       privilege => 'resolve');
END;
/
COMMIT;
```

Example 3

Assign the ACL www.xml to www-proxy.us.oracle.com so that SCOTT and ADAMS can access www-proxy.us.oracle.com also.

```
BEGIN
  DBMS_NETWORK_ACL_ADMIN.ASSIGN_ACL(acl  => 'www.xml',
                                    host => 'www-proxy.us.oracle.com');
END;
/
COMMIT;
```

Example 4

Unassign the ACL from www.us.oracle.com so that no access to www.us.oracle.com is allowed.

```
BEGIN
  DBMS_NETWORK_ACL_ADMIN.UNASSIGN_ACL(host => 'www.us.oracle.com');
END;
/
COMMIT;
```

Example 5

The [DOMAINS Function](d_networkacl_utl.md) in the DBMS\_NETWORK\_ACL\_UTLILITY package returns all the domains to which a host belongs. It can be used in conjunction with the CHECK\_PRIVILEGE\_ACLID Function in this package to determine the privilege assignments affecting a user's permission to access a network host. The function [DOMAIN\_LEVEL Function](d_networkacl_utl.md) in the DBMS\_NETWORK\_ACL\_UTILITY package returns the level of each domain and can be used to order the ACL assignments by their precedence.

For example, for SCOTT's permission to connect to www.us.oracle.com:

```
SELECT host, lower_port, upper_port, acl,
   DECODE(
       DBMS_NETWORK_ACL_ADMIN.CHECK_PRIVILEGE_ACLID(aclid, 'SCOTT', 'connect'),
          1, 'GRANTED', 0, 'DENIED', NULL) privilege
   FROM dba_network_acls
  WHERE host IN
    (SELECT * FROM
       TABLE(DBMS_NETWORK_ACL_UTILITY.DOMAINS('www.us.oracle.com')))
 ORDER BY DBMS_NETWORK_ACL_UTILITY.DOMAIN_LEVEL(host) desc, lower_port, 
                                             upper_port;

 HOST                 LOWER_PORT UPPER_PORT         ACL          PRIVILEGE
 -------------------- ---------- ---------- -------------------- ---------
 www.us.oracle.com            80         80 /sys/acls/www.xml    GRANTED
 www.us.oracle.com          3000       3999 /sys/acls/www.xml    GRANTED
 www.us.oracle.com                          /sys/acls/www.xml    GRANTED
 *.oracle.com                               /sys/acls/all.xml
 *                                          /sys/acls/all.xml
```

Example 6

For example, for SCOTT's permission to do domain name resolution for www.us.oracle.com:

```
SELECT host, acl,
  DECODE(
       DBMS_NETWORK_ACL_ADMIN.CHECK_PRIVILEGE_ACLID(aclid, 'SCOTT', 'resolve'),
         1, 'GRANTED', 0, 'DENIED', NULL) privilege
  FROM dba_network_acls
 WHERE host IN
   (SELECT * FROM
      TABLE(DBMS_NETWORK_ACL_UTILITY.DOMAINS('www.us.oracle.com'))) and
   lower_port IS NULL AND upper_port IS NULL
ORDER BY DBMS_NETWORK_ACL_UTILITY.DOMAIN_LEVEL(host) desc;

HOST                         ACL          PRIVILEGE
-------------------- -------------------- ---------
www.us.oracle.com    /sys/acls/www.xml    GRANTED
*.oracle.com         /sys/acls/all.xml
*                    /sys/acls/all.xml
```

Note that the ' `resolve` ' privilege takes effect only in ACLs assigned without any port range (when `lower_port` and `upper_port` are `NULL`). For this reason, the example does not include `lower_port` and `upper_port` columns in the query.

---

## Summary of DBMS\_NETWORK\_ACL\_ADMIN Subprograms

Table 94-1 DBMS\_NETWORK\_ACL\_ADMIN Package Subprograms

| Subprogram | Description |
| --- | --- |
| ADD\_PRIVILEGE Procedure | Adds a privilege to grant or deny the network access to the user in an access control list (ACL) |
| ASSIGN\_ACL Procedure | Assigns an access control list (ACL) to a network host, and optionally specific to a TCP port range |
| ASSIGN\_WALLET\_ACL Procedure | Assigns an access control list (ACL) to a wallet |
| CHECK\_PRIVILEGE Function | Checks if a privilege is granted to or denied from the user in an access control list (ACL) |
| CHECK\_PRIVILEGE\_ACLID Function | Checks if a privilege is granted to or denied from the user in an ACL by specifying the object ID of the access control list |
| CREATE\_ACL Procedure | Creates an access control list (ACL) with an initial privilege setting |
| DELETE\_PRIVILEGE Procedure | Deletes a privilege in an access control list (ACL) |
| DROP\_ACL Procedure | Drops an access control list (ACL) |
| UNASSIGN\_ACL Procedure | Unassigns the access control list (ACL) currently assigned to a network host |
| UNASSIGN\_WALLET\_ACL Procedure | Unassigns the access control list (ACL) currently assigned to a wallet |

---

### ADD\_PRIVILEGE Procedure

This procedure adds a privilege to grant or deny the network access to the user. The access control entry (ACE) is created if it does not exist.

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

Table 94-2 ADD\_PRIVILEGE Function Parameters

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
        acl         => 'us-oracle-com-permissions.xml',
        principal   => 'ST_USERS',
        is_grant    =>  TRUE,
        privilege   => 'connect')
END;
```

---

### ASSIGN\_ACL Procedure

This procedure assigns an access control list (ACL) to a host computer, domain, or IP subnet, and if specified, the TCP port range.

Syntax

```
DBMS_NETWORK_ACL_ADMIN.ASSIGN_ACL (
   acl         IN VARCHAR2,
   host        IN VARCHAR2,
   lower_port  IN PLS_INTEGER DEFAULT NULL,
   upper_port  IN PLS_INTEGER DEFAULT NULL);
```

Parameters

Table 94-3 ASSIGN\_ACL Function Parameters

| Parameter | Description |
| --- | --- |
| `acl` | Name of the ACL. Relative path will be relative to " `/sys/acls` ". |
| `host` | Host to which the ACL is to be assigned. The host can be the name or the IP address of the host. A wildcard can be used to specify a domain or a IP subnet. The host or domain name is case-insensitive. |
| `lower_port` | Lower bound of a TCP port range if not `NULL` |
| `upper_port` | Upper bound of a TCP port range. If `NULL`, lower\_port is assumed. |

Usage Notes

- Only one ACL can be assigned to any host computer, domain, or IP subnet, and if specified, the TCP port range. When you assign a new access control list to a network target, Oracle Database unassigns the previous access control list that was assigned to the same target. However, Oracle Database does not drop the access control list. You can drop the access control list by using the DROP\_ACL Procedure. To remove an access control list assignment, use the UNASSIGN\_ACL Procedure.
- The ACL assigned to a domain takes a lower precedence than the other ACLs assigned sub-domains, which take a lower precedence than the ACLs assigned to the individual hosts. So for a given host, for example, "www.us.oracle.com", the following domains are listed in decreasing precedences:
	\- www.us.oracle.com
	\- \*.us.oracle.com
	\- \*.oracle.com
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
     acl         => 'us-oracle-com-permissions.xml',
     host        => '*.us.oracle.com',
     lower_port  => 80);
END;
```

---

### ASSIGN\_WALLET\_ACL Procedure

This procedure assigns an access control list (ACL) to a wallet.

Syntax

```
UTL_HTTP.ASSIGN_WALLET_ACL (
   acl          IN  VARCHAR2,
   wallet_path  IN  VARCHAR2);
```

Parameters

Table 94-4 ASSIGN\_WALLET\_ACL Procedure Parameters

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
    wallet_path => 'file:/oracle/wallets/test_wallet');
END;
```

---

### CHECK\_PRIVILEGE Function

This function checks if a privilege is granted to or denied from the user in an ACL.

Syntax

```
DBMS_NETWORK_ACL_ADMIN.CHECK_PRIVILEGE (
   acl             IN VARCHAR2,
   user            IN VARCHAR2,
   privilege       IN VARCHAR2)
  RETURN NUMBER;
```

Parameters

Table 94-5 CHECK\_PRIVILEGE Function Parameters

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
       'us-oracle-com-permissions.xml', 'SCOTT', 'resolve'),
  1, 'GRANTED', 0, 'DENIED', NULL) PRIVILEGE 
FROM DUAL;
```

---

### CHECK\_PRIVILEGE\_ACLID Function

This function checks if a privilege is granted to or denied from the user in an ACL by specifying the object ID of the access control list.

Syntax

```
DBMS_NETWORK_ACL_ADMIN.CHECK_PRIVILEGE_ACLID (
   aclid           IN RAW,
   user            IN VARCHAR2 DEFAULT NULL)
   privilege       IN VARCHAR2,
 RETURN NUMBER;
```

Parameters

Table 94-6 CHECK\_PRIVILEGE\_ACLID Function Parameters

| Parameter | Description |
| --- | --- |
| `aclid` | Object ID of the ACL |
| `user` | User to check against. If the user is `NULL`, the invoker is assumed. The username is case-sensitive as in the `USERNAME` column of the `ALL_USERS` view. |
| `privilege` | Network privilege to check |

Return Values

Returns 1 when the privilege is granted; 0 when the privilege is denied; `NULL` when the privilege is neither granted or denied.

---

### CREATE\_ACL Procedure

This procedure creates an access control list (ACL) with an initial privilege setting. An ACL must have at least one privilege setting. The ACL has no access control effect unless it is assigned to the network target.

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

Table 94-7 CREATE\_ACL Procedure Parameters

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
     acl          => 'us-oracle-com-permissions.xml',
     description  => 'Network permissions for *.us.oracle.com',
     principal    => 'SCOTT',
     is_grant     => TRUE,
     privilege    => 'connect');
END;
```

---

### DELETE\_PRIVILEGE Procedure

This procedure deletes a privilege in an access control list.

Syntax

```
DBMS_NETWORK_ACL_ADMIN.DELETE_PRIVILEGE (
   acl           IN VARCHAR2,
   principal     IN VARCHAR2,
   is_grant      IN BOOLEAN DEFAULT NULL,
   privilege     IN VARCHAR2 DEFAULT NULL);
```

Parameters

Table 94-8 DELETE\_PRIVILEGE Function Parameters

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
        acl         => 'us-oracle-com-permissions.xml',
        principal   => 'ST_USERS')
END;
```

---

### DROP\_ACL Procedure

This procedure drops an access control list (ACL).

Syntax

```
DBMS_NETWORK_ACL_ADMIN.DROP_ACL (
   acl           IN VARCHAR2);
```

Parameters

Table 94-9 DROP\_ACL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `acl` | Name of the ACL. Relative path will be relative to "/sys/acls". |

Examples

```
BEGIN
   DBMS_NETWORK_ACL_ADMIN.DROP_ACL(
      acl => 'us-oracle-com-permissions.xml');
END;
```

---

### UNASSIGN\_ACL Procedure

This procedure unassigns the access control list (ACL) currently assigned to a network host.

Syntax

```
DBMS_NETWORK_ACL_ADMIN.UNASSIGN_ACL (
   acl         IN VARCHAR2 DEFAULT NULL,
   host        IN VARCHAR2 DEFAULT NULL,
   lower_port  IN PLS_INTEGER DEFAULT NULL,
   upper_port  IN PLS_INTEGER DEFAULT NULL);
```

Parameters

Table 94-10 UNASSIGN\_ACL Function Parameters

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
     host        => '*.us.oracle.com',
     lower_port  => 80);
END;
```

---

### UNASSIGN\_WALLET\_ACL Procedure

This procedure unassigns the access control list (ACL) currently assigned to a wallet.

Syntax

```
UTL_HTTP.UNASSIGN_WALLET_ACL (
   acl          IN  VARCHAR2 DEFAULT NULL,
   wallet_path  IN  VARCHAR2 DEFAULT NULL);
```

Parameters

Table 94-11 UNASSIGN\_WALLET\_ACL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `acl` | Name of the ACL. Relative path will be relative to `"/sys/acls"`. If `acl` is `NULL`, any ACL assigned to the wallet is unassigned |
| `wallet_path` | Directory path of the wallet to which the ACL is assigned. The path is case-sensitive and of the format `file`:`directory-path`. If both `acl` and `wallet_path` are `NULL`, all ACLs assigned to any wallets are unassigned. |

Examples

```
BEGIN
  DBMS_NETWORK_ACL_ADMIN.UNASSIGN_WALLET_ACL(
    acl         => 'wallet-acl.xml', 
    wallet_path => 'file:/oracle/wallets/test_wallet');
END;
```