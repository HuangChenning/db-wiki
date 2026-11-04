---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_AQELM.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 26 DBMS\_AQELM

The package provides subprograms to manage the configuration of Oracle Advanced Queuing (AQ) asynchronous notification by e-mail and HTTP.

See Also:

[Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADQUE0400) for detailed information about `DBMS_AQELM`

This chapter contains the following topics:`DBMS_AQELM`

- Security Model
- Summary of DBMS\_AQELM Subprograms

### 26.1 DBMS\_AQELM Security Model

You need the administrator role `AQ_ADMINISTRATOR_ROLE` to run all procedures in `DBMS_AQELM`.

### 26.2 Summary of DBMS\_AQELM Subprograms

This section lists and briefly describes the DBMS\_AQELM subprograms.

Table 26-1 DBMS\_AQELM Package Subprograms

| Subprogram | Description |
| --- | --- |
| SET\_MAILHOST Procedure | Sets the host name for the SMTP server that the database will uses send out e-mail notifications |
| SET\_MAILPORT Procedure | Sets the port number for the SMTP server |
| SET\_SENDFROM Procedure | Sets the sent-from e-mail address |

#### 26.2.1 SET\_MAILHOST Procedure

This procedure sets the host name for the SMTP server. The database uses this SMTP server host name to send out e-mail notifications.

Syntax

```
DBMS_AQELM.SET_MAILHOST (
   mailhost  IN  VARCHAR2);
```

Parameters

Table 26-2 SET\_MAILHOST Procedure Parameters

| Parameter | Description |
| --- | --- |
| `mailhost ` | SMTP server host name. |

Usage Notes

As part of the configuration for e-mail notifications, a user with `AQ_ADMINISTRATOR_ROLE` or with `EXECUTE` permissions on the `DBMS_AQELM` package needs to set the host name before registering for e-mail notifications.

#### 26.2.2 SET\_MAILPORT Procedure

This procedure sets the port number for the SMTP server.

Syntax

```
DBMS_AQELM.SET_MAILPORT (
   mailport  IN NUMBER);
```

Parameters

Table 26-3 SET\_MAILPORT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `mailport ` | SMTP server port number. |

Usage Notes

As part of the configuration for e-mail notifications, a user with `AQ_ADMINISTRATOR_ROLE` or with `EXECUTE` permissions on `DBMS_AQELM` package needs to set the port number before registering for e-mail notifications. The database uses this SMTP server port number to send out e-mail notifications. If not set, the SMTP mailport defaults to 25

#### 26.2.3 SET\_SENDFROM Procedure

This procedure sets the sent-from e-mail address. This e-mail address is used in the sent-from field in all the e-mail notifications sent out by the database to the registered e-mail addresses.

Syntax

```
DBMS_AQELM.SET_SENDFROM (
   sendfrom  IN  VARCHAR2);
```

Parameters

Table 26-4 SET\_SENDFROM Procedure Parameters

| Parameter | Description |
| --- | --- |
| `sendfrom ` | The sent-from e-mail address. |

Usage Notes

As part of the configuration for e-mail notifications, a user with `AQ_ADMINISTRATOR_ROLE` or with `EXECUTE` permissions on the `DBMS_AQELM` package should set the sent-from address before registering for e-mail notifications