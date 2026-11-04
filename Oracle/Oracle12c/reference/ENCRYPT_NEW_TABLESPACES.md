---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ENCRYPT_NEW_TABLESPACES.html
tags:
  - oracle
  - 12c
  - reference
---

`ENCRYPT_NEW_TABLESPACES` specifies whether to encrypt newly created user tablespaces.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `ENCRYPT_NEW_TABLESPACES = { CLOUD_ONLY \| ALWAYS \| DDL }` |
| Default value | `CLOUD_ONLY` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | The same value should be specified for all instances. |

The values that can be specified for the `ENCRYPT_NEW_TABLESPACES` parameter have the following meanings:

- `CLOUD_ONLY`:
	When a user tablespace is created in the Oracle Cloud, it is transparently encrypted with Advanced Encryption Standard 128 (AES 128) if the `ENCRYPTION` … `ENCRYPT` clause for the SQL `CREATE` `TABLESPACE` statement is not specified. When a user tablespace is created in an on-premises database, the `ENCRYPTION` clause of the `CREATE` `TABLESPACE` statement determines if the tablespace is encrypted.
	`CLOUD_ONLY` is the default value.
- `ALWAYS`:
	Whether the user tablespace is created in the Oracle Cloud or in an on-premises database, the tablespace will be transparently encrypted with AES128 if the `ENCRYPTION` … `ENCRYPT` clause is not specified in the `CREATE` `TABLESPACE` statement.
- `DDL`:
	Whether the user tablespace is created in the Oracle Cloud or in an on-premises database, the `CREATE` `TABLESPACE` statement will follow the specified DDL. If no `ENCRYPTION` clause is specified, then the tablespace will not be encrypted. If the `ENCRYPTION` `USING` … `ENCRYPT` clause is specified, then the specified algorithm will be used to encrypt the tablespace. If `ENCRYPTION` `ENCRYPT` is specified, but no algorithm is specified, then the tablespace will be encrypted with the default AES128 algorithm.

Note:

This initialization parameter is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

- [Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ASOAG-GUID-9D9BDB52-CA0F-4275-B16E-B71173C76D56) for more information about tablespace encryption
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=SQLRF01403) for more information about the `CREATE` `TABLESPACE` statement