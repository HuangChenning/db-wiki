---
title: "V$ENCRYPTED_TABLESPACES"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1124.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ENCRYPTED_TABLESPACES` displays information about the tablespaces that are encrypted.

| Column | Datatype | Description |
| --- | --- | --- |
| `TS#` | `NUMBER` | Tablespace number |
| `ENCRYPTIONALG` | `VARCHAR2(7)` | Encryption algorithm: |
| `ENCRYPTEDTS` | `VARCHAR2(3)` | Indicates whether the tablespace is encrypted (`YES`) or not (`NO`) |
| `ENCRYTPEDKEY` <sup>Foot 1</sup> | `RAW(32)` | Encrypted version of the tablespace key for the encrypted tablespace |
| `MASTERKEYID` <sup>Footref 1</sup> | `RAW(16)` | ID of the master key that was used to encrypt the tablespace key |
| `BLOCKS_ENCRYPTED` <sup>Footref 1</sup> | `NUMBER` | Number of tablespace blocks that have been encrypted during the lifetime of this instance |
| `BLOCKS_DECRYPTED` <sup>Footref 1</sup> | `NUMBER` | Number of tablespace blocks that have been decrypted during the lifetime of this instance |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).