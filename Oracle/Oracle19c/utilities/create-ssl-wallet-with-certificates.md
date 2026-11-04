---
title: Utilities
book: Oracle AI Database Utilities Guide
doc_id: E96081-35
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/create-ssl-wallet-with-certificates.html
tags:
  - oracle
  - 19c
  - utilities
---

## 20.3 Create SSL Wallet with Certificates

To access HTTP URIs and Object Stores safely from within your database, you must create a wallet with the appropriate certificates.

You must manually install the appropriate certificates in a wallet to access the `DBMS_CLOUD` family of packages. The certificates are not part of the Oracle Database distribution. You can download the necessary certificates from the following site:

[https://objectstorage.us-phoenix-1.oraclecloud.com/p/KB63IAuDCGhz\_azOVQ07Qa\_mxL3bGrFh1dtsltreRJPbmb-VwsH2aQ4Pur2ADBMA/n/adwcdemo/b/CERTS/o/dbc\_certs.tar](https://objectstorage.us-phoenix-1.oraclecloud.com/p/KB63IAuDCGhz_azOVQ07Qa_mxL3bGrFh1dtsltreRJPbmb-VwsH2aQ4Pur2ADBMA/n/adwcdemo/b/CERTS/o/dbc_certs.tar)

The security wallet must have the following properties.

- The wallet must be created with auto-login capabilities.
- On Oracle Real Application Clusters (Oracle RAC) installations, the wallet must either be accessible for all nodes centrally, or you must create the wallet on all nodes for local wallet storage.

Oracle recommends that you store the SSL wallet in an equivalent location. In the following SSL wallet creation example, we assume that the SSL wallet is in the location `/u01/app/oracle/dcs/commonstore/wallets/ssl`, and you have unpacked the certificates in the path `/home/oracle/dbc`:

```
cd /u01/app/oracle/dcs/commonstore/wallets/ssl
orapki wallet create -wallet . -pwd your_chosen_wallet_pw -auto_login
 
#! /bin/bash
for i in $(ls /home/oracle/dbc/*cer)
do
orapki wallet add -wallet . -trusted_cert -cert $i -pwd SSL Wallet password
done
```

Note:

If you already have a wallet for SSL certificates, then you do not have to create a new wallet. Instead, you can add the required certificates to the existing wallet.

Oracle recommends that you check the certificate location. For example:

```
cd /u01/app/oracle/dcs/commonstore/wallets/ssl
orapki wallet display -wallet .
```

The following is an excerpt of what you should see in the certificate wallet. Note that this is not the complete list of all certificates:

```
[oracle@mydb ssl]$ orapki wallet display -wallet .

Oracle PKI Tool Release 23.0.0.0.0 - Production
Version 23.0.0.0.0
Copyright (c) 2004, 2026, Oracle and/or its affiliates. All rights reserved.

Requested Certificates:
User Certificates:
Trusted Certificates:
Subject: OU=ePKI Root Certification Authority,O=Chunghwa Telecom Co.\, Ltd.,C=TW
Subject: CN=Certum CA
```

**Parent topic:** [DBMS\_CLOUD Family of Packages](dbms_cloud-family-packages.md)