---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SESSION_CONNECT_INFO.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.19 V$SESSION\_CONNECT\_INFO

`V$SESSION_CONNECT_INFO` displays information about network connections for all currently logged in sessions.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session identifier (can be used to join this view with `V$SESSION`) |
| `SERIAL#` | `NUMBER` | Session serial number. Used to uniquely identify a session's objects. Guarantees that session-level commands are applied to the correct session objects if the session ends and another session begins with the same session ID. (Can be used to join this view with `V$SESSION`.) |
| `AUTHENTICATION_TYPE` | `VARCHAR2(26)` | How the user was authenticated:  - `DATABASE` - Username/password authentication - `OS` - Operating system external user authentication - `NETWORK` - Network protocol or ANO authentication - `PROXY` - OCI proxy connection authentication - `SERVER` - `PASSWORD` - `EXTERNAL ADAPTERS` - `INTERNAL` - `GLOBAL` - `EXTERNAL` - `PASSWORD BASED GLOBAL USER` |
| `OSUSER` | `VARCHAR2(128)` | External username for this database user |
| `NETWORK_SERVICE_BANNER` | `VARCHAR2(4000)` | Product banners for each Oracle Net service used for this connection (one row per banner) |
| `CLIENT_CHARSET` | `VARCHAR2(40)` | Client character set as specified in the `NLS_LANG` environment variable or in the `OCIEnvNlsCreate()` call; `Unknown` if the Oracle client is older than release 11.1 or the connection is through the JDBC thin driver |
| `CLIENT_CONNECTION` | `VARCHAR2(13)` | Client server connection flags:  - `Heterogeneous` - `Homogeneous` |
| `CLIENT_OCI_LIBRARY` | `VARCHAR2(27)` | OCI client library:  - `Home-based` - `Full Instant Client` - `Light Weight Instant Client` - `OCI` - `Unknown` |
| `CLIENT_VERSION` | `VARCHAR2(40)` | Client library version number |
| `CLIENT_DRIVER` | `VARCHAR2(30)` | Client driver name  For pooled connections, the value of this column is null. |
| `CLIENT_LOBATTR` | `VARCHAR2(23)` | Client LOB flags:  - `Client Temp Lob Rfc On` - `Client Temp Lob Rfc Off` |
| `CLIENT_REGID` | `NUMBER` | Query cache registration ID sent by the client |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$SESSION](V-SESSION.md) "