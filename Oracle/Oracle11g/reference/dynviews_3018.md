---
title: "V$SESSION_CONNECT_INFO"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3018.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SESSION_CONNECT_INFO` displays information about network connections for all currently logged in sessions.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session identifier (can be used to join this view with `V$SESSION`) |
| `SERIAL#` | `NUMBER` | Session serial number. Used to uniquely identify a session's objects. Guarantees that session-level commands are applied to the correct session objects if the session ends and another session begins with the same session ID. (Can be used to join this view with `V$SESSION`.) |
| `AUTHENTICATION_TYPE` | `VARCHAR2(26)` | How the user was authenticated: - `DATABASE` - Username/password authentication - `OS` - Operating system external user authentication - `NETWORK` - Network protocol or ANO authentication - `PROXY` - OCI proxy connection authentication - `SERVER` - `PASSWORD` - `EXTERNAL ADAPTERS` - `INTERNAL` - `GLOBAL` - `EXTERNAL` - `PASSWORD BASED GLOBAL USER` |
| `OSUSER` | `VARCHAR2(30)` | External username for this database user |
| `NETWORK_SERVICE_BANNER` | `VARCHAR2(4000)` | Product banners for each Oracle Net service used for this connection (one row per banner) |
| `CLIENT_CHARSET` | `VARCHAR2(40)` | Client character set as specified in the `NLS_LANG` environment variable or in the `OCIEnvNlsCreate()` call; `Unknown` if the Oracle client is older than release 11.1 or the connection is through the JDBC thin driver |
| `CLIENT_CONNECTION` | `VARCHAR2(13)` | Client server connection flags: |
| `CLIENT_OCI_LIBRARY` | `VARCHAR2(27)` | OCI client library: |
| `CLIENT_VERSION` | `VARCHAR2(40)` | Client library version number |
| `CLIENT_DRIVER` | `VARCHAR2(9)` | Client driver name |
| `CLIENT_LOBATTR` | `VARCHAR2(23)` | Client LOB flags: |
| `CLIENT_REGID` | `NUMBER` | Query cache registration ID sent by the client |