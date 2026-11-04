---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-WALLET.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.134 V$WALLET

`V$WALLET` displays metadata of certificates that may be used as a master key for Transparent Data Encryption.

Note:

The use of PKI encryption with Transparent Data Encryption is deprecated. To configure Transparent Data Encryption, use the `ADMINISTER KEY MANAGEMENT` SQL statement. See [Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ASOAG600) for more information.

| Column | Datatype | Description |
| --- | --- | --- |
| `CERT_ID` | `VARCHAR2(52)` | A unique certificate identifier value used to specify a particular PKI certificate for use as the master key |
| `DN` | `VARCHAR2(255)` | Distinguished name of a particular PKI certificate |
| `SERIAL_NUM` | `VARCHAR2(40)` | Unique serial number assigned to a certificate by the issuer or signer |
| `ISSUER` | `VARCHAR2(255)` | Distinguished name of the Certificate Authority or issuer that issued and signed the certificate |
| `KEYSIZE` | `NUMBER` | Size of the PKI key associated with the certificate |
| `STATUS` | `VARCHAR2(16)` | Current status of the certificate:  - `UNUSED` - `IN USE` - `USED`  This column allows the user to identify whether a certificate is currently in use or has already been used for Transparent Data Encryption. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |