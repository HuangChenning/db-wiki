---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/UTL_INADDR.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 271 UTL\_INADDR

The `UTL_INADDR ` package provides a PL/SQL procedures to support internet addressing. It provides an API to retrieve host names and IP addresses of local and remote hosts.

This chapter contains the following topics:

### 271.1 UTL\_INADDR Security Model

This package is an invoker's rights package, which means that the invoking user must be granted the `connect` privilege in the access control list assigned to the remote network host to which he or she wishes to connect.

Note:

For more information about managing fine-grained access, see [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=DBSEG40012).

### 271.2 UTL\_INADDR Exceptions

This table describes cxceptions raised by `UTL_INADDR` subprograms.

Table 271-1 Exception - Internet Address Package

| Number | Exception | Description |
| --- | --- | --- |
| `ORA-24247` | `NETWORK_ACCESS_DENIED` | Access to network is denied. |
| `ORA-29257` | `UNKNOWN_HOST` | The host is unknown. |

### 271.3 UTL\_INADDR Examples

This UTL\_INADDR example retrieves the local host name and IP address.

```
SET serveroutput on
BEGIN
  DBMS_OUTPUT.PUT_LINE(UTL_INADDR.GET_HOST_NAME);  -- get local host name
  DBMS_OUTPUT.PUT_LINE(UTL_INADDR.GET_HOST_ADDRESS);  -- get local IP addr
END;
/
```

### 271.4 Summary of UTL\_INADDR Subprograms

This table lists the `UTL_INADDR` subprograms and briefly describes them.

Table 271-2 UTL\_INADDR Package Subprograms

| Subprogram | Description |
| --- | --- |
| GET\_HOST\_ADDRESS Function | Retrieves the IP address of the local or remote host given its name |
| GET\_HOST\_NAME Function | Retrieves the name of the local or remote host given its IP address |

#### 271.4.1 GET\_HOST\_ADDRESS Function

This function retrieves the IP address of the specified host.

Syntax

```
UTL_INADDR.GET_HOST_ADDRESS (
   host  IN VARCHAR2 DEFAULT NULL) 
RETURN host_address VARCHAR2;
```

Parameters

Table 271-3 GET\_HOST\_ADDRESS Function Parameters

| Parameter | Description |
| --- | --- |
| `host` | The name of the host to retrieve the IP address. |

Return Values

Table 271-4 GET\_HOST\_ADDRESS Function Return Values

| Parameter | Description |
| --- | --- |
| `host_address` | The IP address of the specified host, or that of the local host if host is `NULL`. |

Exceptions

`UNKNOWN_HOST:` The specified IP address is unknown

Usage Notes

The permission to obtain the host name or IP address of the current host is controlled by the `resolve` privilege on `LOCALHOST`.

#### 271.4.2 GET\_HOST\_NAME Function

This function retrieves the name of the local or remote host given its IP address.

Syntax

```
UTL_INADDR.GET_HOST_NAME (
   ip  IN VARCHAR2 DEFAULT NULL)
RETURN host_name VARCHAR2;
```

Parameters

Table 271-5 GET\_HOST\_NAME Function Parameters

| Parameter | Description |
| --- | --- |
| `ip` | The IP address of the host used to determine its host name. If ip is not `NULL,` the official name of the host with its domain name is returned. If this is `NULL,` the name of the local host is returned and the name does not contain the domain to which the local host belongs. |

Return Values

Table 271-6 GET\_HOST\_NAME Function Return Values

| Parameter | Description |
| --- | --- |
| `host_name` | The name of the local or remote host of the specified IP address. |

Exceptions

`UNKNOWN_HOST:` The specified IP address is unknown

Usage Notes

The permission to obtain the host name or IP address of the current host is controlled by the `resolve` privilege granted through `DBMS_NETWORK_ACL_ADMIN` on `LOCALHOST`.