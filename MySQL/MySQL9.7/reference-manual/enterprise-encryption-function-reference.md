---
title: "8.6.4 MySQL Enterprise Encryption Function Reference"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/enterprise-encryption-function-reference.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 8.6.4 MySQL Enterprise Encryption Function Reference

MySQL Enterprise Encryption functions are provided by the MySQL `component_enterprise_encryption` component. See [Section 8.6.5, “MySQL Enterprise Encryption Component Function Descriptions”](enterprise-encryption-functions.md).

**Table 8.58 MySQL Enterprise Encryption Functions**

| Name | Description |
| --- | --- |
| [`asymmetric_decrypt()`](enterprise-encryption-functions.md) | Decrypt ciphertext using private or public key |
| `asymmetric_derive()` | Derive symmetric key from asymmetric keys |
| [`asymmetric_encrypt()`](enterprise-encryption-functions.md) | Encrypt cleartext using private or public key |
| [`asymmetric_sign()`](enterprise-encryption-functions.md) | Generate signature from digest |
| [`asymmetric_verify()`](enterprise-encryption-functions.md) | Verify that signature matches digest |
| [`create_asymmetric_priv_key()`](enterprise-encryption-functions.md) | Create private key |
| [`create_asymmetric_pub_key()`](enterprise-encryption-functions.md) | Create public key |
| `create_dh_parameters()` | Generate shared DH secret |
| [`create_digest()`](enterprise-encryption-functions.md) | Generate digest from string |