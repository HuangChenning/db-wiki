---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/TABLESPACE_ENCRYPTION_DEFAULT_ALGORITHM.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.357 TABLESPACE\_ENCRYPTION\_DEFAULT\_ALGORITHM

`TABLESPACE_ENCRYPTION_DEFAULT_ALGORITHM` specifies the default algorithm the database uses when encrypting a tablespace.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `TABLESPACE_ENCRYPTION_DEFAULT_ALGORITHM = { AES128 \| AES192 \| AES256 \| ARIA128 \| ARIA192 \| ARIA256 \| GOST256 \| SEED128 \| 3DES168 }`  Note: `3DES168` must be enclosed in single quotation marks when specified in the `ALTER` `SYSTEM` command. |
| Default value | `AES128` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | The same value should be specified for all instances. |

The value of this initialization parameter determines the algorithm the database uses if an encryption algorithm is not specified when creating an encrypted tablespace or when encrypting an existing tablespace. For example, the value of this parameter takes effect when:

- You create a tablespace with the `CREATE` `TABLESPACE` statement and you specify the `ENCRYPTION` … `ENCRYPT` clause, but you do not specify the `USING` keyword and an algorithm.
- You create a tablespace with the `CREATE` `TABLESPACE` statement and you do not specify the `ENCRYPTION` … `ENCRYPT` clause. However, the value of the `ENCRYPT_NEW_TABLESPACES` initialization parameter instructs the database to encrypt the tablespace.
- You encrypt an existing tablespace with the `ALTER` `TABLESPACE` statement, either by specifying the `ENCRYPTION` `OFFLINE` `ENCRYPT` clause or the `ENCRYPTION` `ONLINE` … `ENCRYPT` clause, and you do not specify the `USING` keyword and an algorithm.

Note:

This parameter is available starting with Oracle Database 21c.

See Also:

- " [ENCRYPT\_NEW\_TABLESPACES](ENCRYPT_NEW_TABLESPACES.md) "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF-GUID-1CDEC3A3-F3F1-4279-9370-36AACF416E0A) for more information about the `CREATE TABLESPACE` statement
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF-GUID-CA074861-55D3-4768-8995-43D4DA26365D) for more information about the `ALTER TABLESPACE` statement