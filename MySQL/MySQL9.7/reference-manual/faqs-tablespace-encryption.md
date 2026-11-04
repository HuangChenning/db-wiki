---
title: "A.17 MySQL 9.7 FAQ: InnoDB Data-at-Rest Encryption"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/faqs-tablespace-encryption.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

A.17.1. Is data decrypted for users who are authorized to see it?

A.17.2. What is the overhead associated with InnoDB data-at-rest encryption?

A.17.3. What are the encryption algorithms used with InnoDB data-at-rest encryption?

A.17.4. Is it possible to use 3rd party encryption algorithms in place of the one provided by the InnoDB data-at-rest encryption feature?

A.17.5. Can indexed columns be encrypted?

A.17.6. What data types and data lengths does InnoDB data-at-rest encryption support?

A.17.7. Does data remain encrypted on the network?

A.17.8. Does database memory contain cleartext or encrypted data?

A.17.9. How do I know which data to encrypt?

A.17.10. How is InnoDB data-at-rest encryption different from encryption functions MySQL already provides?

A.17.11. Does the transportable tablespaces feature work with InnoDB data-at-rest encryption?

A.17.12. Does compression work with InnoDB data-at-rest encryption?

A.17.13. Can I use mysqldump with encrypted tables?

A.17.14. How do I change (rotate, re-key) the master encryption key?

A.17.15. How do I migrate data from a cleartext InnoDB tablespace to an encrypted InnoDB tablespace?

| **A.17.1.** | Is data decrypted for users who are authorized to see it? |
| --- | --- |
|  | Yes. `InnoDB` data-at-rest encryption is designed to transparently apply encryption within the database without impacting existing applications. Returning data in encrypted format would break most existing applications. `InnoDB` data-at-rest encryption provides the benefit of encryption without the overhead associated with traditional database encryption solutions, which would typically require expensive and substantial changes to applications, database triggers, and views. |
| **A.17.2.** | What is the overhead associated with `InnoDB` data-at-rest encryption? |
|  | There is no additional storage overhead. According to internal benchmarks, performance overhead amounts to a single digit percentage difference. |
| **A.17.3.** | What are the encryption algorithms used with `InnoDB` data-at-rest encryption? |
|  | `InnoDB` data-at-rest encryption supports the Advanced Encryption Standard (AES256) block-based encryption algorithm. It uses Electronic Codebook (ECB) block encryption mode for tablespace key encryption and Cipher Block Chaining (CBC) block encryption mode for data encryption. |
| **A.17.4.** | Is it possible to use 3rd party encryption algorithms in place of the one provided by the `InnoDB` data-at-rest encryption feature? |
|  | No, it is not possible to use other encryption algorithms. The provided encryption algorithm is broadly accepted. |
| **A.17.5.** | Can indexed columns be encrypted? |
|  | `InnoDB` data-at-rest encryption supports all indexes transparently. |
| **A.17.6.** | What data types and data lengths does `InnoDB` data-at-rest encryption support? |
|  | `InnoDB` data-at-rest encryption supports all supported data types. There is no data length limitation. |
| **A.17.7.** | Does data remain encrypted on the network? |
|  | Data encrypted by the `InnoDB` data-at-rest feature is decrypted when it is read from the tablespace file. Thus, if the data is on the network, it is in cleartext form. However, data on the network can be encrypted using MySQL network encryption, which encrypts data traveling to and from a database using SSL/TLS. |
| **A.17.8.** | Does database memory contain cleartext or encrypted data? |
|  | With `InnoDB` data-at-rest encryption, in-memory data is decrypted, which provides complete transparency. |
| **A.17.9.** | How do I know which data to encrypt? |
|  | Compliance with the PCI-DSS standard requires that credit card numbers (Primary Account Number, or 'PAN') be stored in encrypted form. Breach Notification Laws (for example, CA SB 1386, CA AB 1950, and similar laws in 43+ more US states) require encryption of first name, last name, driver license number, and other PII data. In early 2008, CA AB 1298 added medical and health insurance information to PII data. Additionally, industry specific privacy and security standards may require encryption of certain assets. For example, assets such as pharmaceutical research results, oil field exploration results, financial contracts, or personal data of law enforcement informants may require encryption. In the health care industry, the privacy of patient data, health records and X-ray images is of the highest importance. |
| **A.17.10.** | How is `InnoDB` data-at-rest encryption different from encryption functions MySQL already provides? |
|  | There are symmetric and asymmetric encryption APIs in MySQL that can be used to manually encrypt data within the database. However, the application must manage encryption keys and perform required encryption and decryption operations by calling API functions. `InnoDB` data-at-rest encryption requires no application changes, is transparent to end users, and provides automated, built-in key management. |
| **A.17.11.** | Does the transportable tablespaces feature work with `InnoDB` data-at-rest encryption? |
|  | Yes. It is supported for encrypted file-per-table tablespaces. For more information, see [Exporting Encrypted Tablespaces](innodb-data-encryption.md). |
| **A.17.12.** | Does compression work with `InnoDB` data-at-rest encryption? |
|  | Customers using `InnoDB` data-at-rest encryption receive the full benefit of compression because compression is applied before data blocks are encrypted. |
| **A.17.13.** | Can I use `mysqldump` with encrypted tables? |
|  | Yes. Because these utilities create logical backups, the data dumped from encrypted tables is not encrypted. |
| **A.17.14.** | How do I change (rotate, re-key) the master encryption key? |
|  | `InnoDB` data-at-rest encryption uses a two tier key mechanism. When data-at-rest encryption is used, individual tablespace keys are stored in the header of the underlying tablespace data file. Tablespace keys are encrypted using the master encryption key. The master encryption key is generated when tablespace encryption is enabled, and is stored outside the database. The master encryption key is rotated using the [`ALTER         INSTANCE ROTATE INNODB MASTER KEY`](alter-instance.md) statement, which generates a new master encryption key, stores the key, and rotates the key into use. |
| **A.17.15.** | How do I migrate data from a cleartext `InnoDB` tablespace to an encrypted `InnoDB` tablespace? |
|  | Transferring data from one tablespace to another is not required. To encrypt data in an `InnoDB` file-per-table tablespace, run [``ALTER TABLE         *`tbl_name`* ENCRYPTION = 'Y'``](alter-table.md). To encrypt a general tablespace or the `mysql` tablespace, run [``ALTER         TABLESPACE *`tablespace_name`* ENCRYPTION         = 'Y'``](alter-tablespace.md). Encryption support for general tablespaces was introduced in MySQL 8.0.13. Encryption support for the `mysql` system tablespace is available as of MySQL 8.0.16. |