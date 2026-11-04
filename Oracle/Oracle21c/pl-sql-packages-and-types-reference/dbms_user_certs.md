---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/dbms_user_certs.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 193 DBMS\_USER\_CERTS

The `DBMS_USER_CERTS` package allows you add and delete certificates.

This chapter contains the following topics:

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADMIN-GUID-707B02F5-E589-4C20-8E2E-5ED4F7888702)
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=CNCPT1132)
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=SQLRF54484)
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=REFRN)
- For information on hidden columns in blockchain tables, see [Hidden Columns in Blockchain Tables](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADMIN-GUID-02BD6C35-E1E9-41B7-BD56-68C7A667B51F)

### 193.1 DBMS\_USER\_CERTS Overview

The `DBMS_USER_CERTS` package allows you add and delete certificates.

The `DBMS_USER_CERTS` package allows you to:
- add certificates
- delete certificates

One use case is to attach a digital signature to a row in a blockchain table and be able to verify the digital signature later. A certificate used to sign one or more rows in blockchain tables and which has since expired should remain in the database until all those rows have been deleted from the blockchain tables.

### 193.2 DBMS\_USER\_CERTS Security Model

The `DBMS_USER_CERTS` package is owned by `SYS` and is installed as part of database installation.

- Both `ADD_CERTIFICATE()` and `DROP_CERTIFICATE()` sub-programs can be executed by any database user. The `EXECUTE` privilege on `DBMS_USER_CERTS` package is granted to `PUBLIC` role.
- Using `ADD_CERTIFICATE()`, a database user can add multiple certificates, each one would be identified uniquely using a `GUID`.
- Only `SYSDBA` or the user who owns the certificate, can drop it using `DROP_CERTIFICATE()`.

### 193.3 Summary of DBMS\_USER\_CERTS Subprograms

The `DBMS_USER_CERTS` package uses `ADD_CERTIFICATE` and `DROP_CERTIFICATE` subprograms to add and delete `X.509` certificates which are used for signature verification for blockchain tables by the current user.

Table 193-1 DBMS\_USER\_CERTS Package Subprograms

| Subprogram | Description |
| --- | --- |
| ADD\_CERTIFICATE Procedure | Adds `X.509` certificates which are used for signature verification of blockchain tables. |
| DROP\_CERTIFICATE Procedure | Drops a certificate that is used for signature verification of blockchain tables. |

#### 193.3.1 ADD\_CERTIFICATE Procedure

This procedure can be used by the current user to add an `X.509` certificate that is used for signature verification of blockchain tables.

Syntax

```
DBMS_USER_CERTS.ADD_CERTIFICATE(
   x509_cert                 IN  BLOB,
   cert_id                   OUT RAW);
```

Parameters

Table 193-2 ADD\_CERTIFICATE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `x509_cert` | The `X.509` certificate used for signature verification of blockchain tables. |
| `cert_id` | The Global Unique Identifier (GUID) for the certificate. |

#### 193.3.2 DROP\_CERTIFICATE Procedure

This procedure can be used by the current user to drop a certificate that is used for signature verification of blockchain tables.

Syntax

```
DBMS_USER_CERTS.DROP_CERTIFICATE(
   cert_id                    IN  RAW);
```

Parameters

Table 193-3 DROP\_CERTIFICATE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `cert_id` | The Global Unique Identifier (GUID) of the certificate. |