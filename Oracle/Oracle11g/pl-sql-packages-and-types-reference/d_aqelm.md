---
title: DBMS_AQELM
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_aqelm.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 24 DBMS\_AQELM

The `DBMS_AQELM` package provides subprograms to manage the configuration of Oracle Streams Advanced Queuing (AQ) asynchronous notification by e-mail and HTTP.

See Also:

[Oracle Streams Advanced Queuing User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e11013/toc.htm) for detailed information about `DBMS_AQELM`

This chapter contains the following topic:

- Summary of DBMS\_AQELM Subprograms

---

## Summary of DBMS\_AQELM Subprograms

Table 24-1 DBMS\_ALERT Package Subprograms

| Subprogram | Description |
| --- | --- |
| SET\_MAILHOST Procedure | Sets the host name for the SMTP server that the database will uses send out e-mail notifications |
| SET\_MAILPORT Procedure | Sets the port number for the SMTP server |
| SET\_SENDFROM Procedure | Sets the sent-from e-mail address |

---

### SET\_MAILHOST Procedure

This procedure sets the host name for the SMTP server. The database uses this SMTP server host name to send out e-mail notifications.

Syntax

```
DBMS_AQELM.SET_MAILHOST (
   mailhost  IN  VARCHAR2);
```

Parameters

Table 24-2 SET\_MAILHOST Procedure Parameters

| Parameter | Description |
| --- | --- |
| `mailhost` | SMTP server host name. |

Usage Notes

As part of the configuration for e-mail notifications, a user with `AQ_ADMINISTRATOR_ROLE` or with `EXECUTE` permissions on the `DBMS_AQELM` package needs to set the host name before registering for e-mail notifications.

---

### SET\_MAILPORT Procedure

This procedure sets the port number for the SMTP server.

Syntax

```
DBMS_AQELM.SET_MAILPORT (
   mailport  IN NUMBER);
```

Parameters

Table 24-3 SET\_MAILPORT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `mailport` | SMTP server port number. |

Usage Notes

As part of the configuration for e-mail notifications, a user with `AQ_ADMINISTRATOR_ROLE` or with `EXECUTE` permissions on `DBMS_AQELM` package needs to set the port number before registering for e-mail notifications. The database uses this SMTP server port number to send out e-mail notifications. If not set, the SMTP mailport defaults to 25

---

### SET\_SENDFROM Procedure

This procedure sets the sent-from e-mail address. This e-mail address is used in the sent-from field in all the e-mail notifications sent out by the database to the registered e-mail addresses.

Syntax

```
DBMS_AQELM.SET_SENDFROM (
   sendfrom  IN  VARCHAR2);
```

Parameters

Table 24-4 SET\_SENDFROM Procedure Parameters

| Parameter | Description |
| --- | --- |
| `sendfrom` | The sent-from e-mail address. |

Usage Notes

As part of the configuration for e-mail notifications, a user with `AQ_ADMINISTRATOR_ROLE` or with `EXECUTE` permissions on the `DBMS_AQELM` package should set the sent-from address before registering for e-mail notifications