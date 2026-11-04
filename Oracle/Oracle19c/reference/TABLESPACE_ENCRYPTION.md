---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/TABLESPACE_ENCRYPTION.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.358 TABLESPACE\_ENCRYPTION

`TABLESPACE_ENCRYPTION` specifies the tablespace encryption policy for a database.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `TABLESPACE_ENCRYPTION = { AUTO_ENABLE \| MANUAL_ENABLE \| DECRYPT_ONLY }` |
| Default value | Cloud databases: `AUTO_ENABLE`  On-premises databases: `MANUAL_ENABLE` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Basic | No |
| Oracle RAC | The same value should be specified for all instances. |

This parameter is introduced in Oracle Database 19c, Release Update 19.16, as an alternative to the `ENCRYPT_NEW_TABLESPACES` parameter. Similar to `ENCRYPT_NEW_TABLESPACES`, this parameter allows you to specify whether to encrypt newly created user tablespaces. However, the `TABLESPACE_ENCRYPTION` parameter offers an additional benefit in Data Guard environments. In previous releases, tablespaces in Data Guard environments were required to use the same encryption policy on the primary and standby databases. For example, if all tablespaces were encrypted on the primary database, then all tablespaces were required to be encrypted on the standby database. The `TABLESPACE_ENCRYPTION` parameter eliminates this requirement and allows you to use different tablespace encryption policies on primary and standby databases. See [Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=ASOAG-GUID-6B769BE8-5312-406F-BD28-51C3C0CCC33D) for more information.

If the behavior specified by the `ENCRYPT_NEW_TABLESPACES` setting conflicts with the behavior specified by the `TABLESPACE_ENCRYPTION` setting, then the `TABLESPACE_ENCRYPTION` behavior takes precedence.

Values:

- `AUTO_ENABLE`
	Use this setting if you would like to encrypt all tablespaces in the database.
	All newly created tablespaces will be encrypted. In the `CREATE` `TABLESPACE` statement, if you specify the `DECRYPT` clause, it will be ignored and the tablespace will be encrypted. If you specify the `ENCRYPTION` `USING` `algorithm` `ENCRYPT` clause, the specified algorithm will be used to encrypt the tablespace. If you specify the `ENCRYPTION` `ENCRYPT` clause and do not specify an algorithm, the tablespace will be encrypted with Advanced Encryption Standard 128 (AES128).
	If an existing tablespace is unencrypted, the database writes a warning to the alert log. See [Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=ASOAG-GUID-1CA947A5-164A-4AA9-AD75-F7D9D4F6FFF8) for information about encrypting existing tablespaces.
	If you attempt to decrypt an existing encrypted tablespace, an error will occur.
	This is the default setting for Cloud databases. Moreover, because all tablespaces must be encrypted in the Cloud, setting this parameter to `MANUAL_ENABLE` or `DECRYPT_ONLY` for a Cloud database will be ignored and the Cloud database will behave as if the setting is `AUTO_ENABLE`.
- `MANUAL_ENABLE`
	Use this setting if you would like to manually control which tablespaces are encrypted.
	To encrypt a tablespace, specify the `ENCRYPTION`... `ENCRYPT` clause in the `CREATE` `TABLESPACE` statement. If you specify the `ENCRYPTION` `USING` `algorithm` `ENCRYPT` clause, the specified algorithm will be used to encrypt the tablespace. If you specify the `ENCRYPTION` `ENCRYPT` clause and do not specify an algorithm, the tablespace will be encrypted with AES128.
	This is the default setting for on-premises databases. This setting is ignored for Cloud databases.
- `DECRYPT_ONLY`
	Use this setting if you do not want any encrypted tablespaces in the database.
	All newly created tablespaces must be unencrypted. If you specify the `ENCRYPT` clause in the `CREATE` `TABLESPACE` statement, an error will occur.
	If an existing tablespace is encrypted, the database writes a warning to the alert log. See [Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=ASOAG-GUID-1CA947A5-164A-4AA9-AD75-F7D9D4F6FFF8) for information about decrypting existing tablespaces.
	If you attempt to encrypt an existing unencrypted tablespace, an error will occur.
	This setting is valid only for on-premises databases. This setting is ignored for Cloud databases.

Note:

This parameter is available starting with Oracle Database 19c, Release Update 19.16.

See Also:

" [ENCRYPT\_NEW\_TABLESPACES](ENCRYPT_NEW_TABLESPACES.md) "