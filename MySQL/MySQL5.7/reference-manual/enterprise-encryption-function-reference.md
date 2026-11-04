---
title: "6.6.3 MySQL Enterprise Encryption Function Reference"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/enterprise-encryption-function-reference.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 6.6.3 MySQL Enterprise Encryption Function Reference

**Table 6.36 MySQL Enterprise Encryption Functions**

| Name | Description |
| --- | --- |
| [`asymmetric_decrypt()`](enterprise-encryption-functions.md) | Decrypt ciphertext using private or public key |
| [`asymmetric_derive()`](enterprise-encryption-functions.md) | Derive symmetric key from asymmetric keys |
| [`asymmetric_encrypt()`](enterprise-encryption-functions.md) | Encrypt cleartext using private or public key |
| [`asymmetric_sign()`](enterprise-encryption-functions.md) | Generate signature from digest |
| [`asymmetric_verify()`](enterprise-encryption-functions.md) | Verify that signature matches digest |
| [`create_asymmetric_priv_key()`](enterprise-encryption-functions.md) | Create private key |
| [`create_asymmetric_pub_key()`](enterprise-encryption-functions.md) | Create public key |
| [`create_dh_parameters()`](enterprise-encryption-functions.md) | Generate shared DH secret |
| [`create_digest()`](enterprise-encryption-functions.md) | Generate digest from string |