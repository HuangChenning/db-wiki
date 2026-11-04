---
title: "V$WALLET"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3126.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$WALLET` displays metadata of certificates that may be used as a master key for transparent data encryption.

| Column | Datatype | Description |
| --- | --- | --- |
| `CERT_ID` | `VARCHAR2(52)` | A unique certificate identifier value used to specify a particular PKI certificate for use as the master key |
| `DN` | `VARCHAR2(255)` | Distinguished name of a particular PKI certificate |
| `SERIAL_NUM` | `VARCHAR2(40)` | Unique serial number assigned to a certificate by the issuer or signer |
| `ISSUER` | `VARCHAR2(255)` | Distinguished name of the Certificate Authority or issuer that issued and signed the certificate |
| `KEYSIZE` | `NUMBER` | Size of the PKI key associated with the certificate |
| `STATUS` | `VARCHAR2(16)` | Current status of the certificate:  This column allows the user to identify whether a certificate is currently in use or has already been used for transparent database encryption. |