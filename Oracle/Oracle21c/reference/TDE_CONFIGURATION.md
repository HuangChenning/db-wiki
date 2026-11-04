---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/TDE_CONFIGURATION.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.359 TDE\_CONFIGURATION

Use `TDE_CONFIGURATION` to set the type of keystore that is used for Transparent Data Encryption (TDE) by the root container; united PDBs inherit the value from the root container, isolated PDBs can be set individually.

Before Oracle Database 18c, each PDB stored its separate encryption keys in the CDB’s keystore (united mode). Starting with Oracle Database 18c Cloud environments, a PDB can optionally store its encryption keys in a separate keystore (isolated mode), thus allowing protection by a separate keystore password. Starting with Oracle Database 19c, Release Update 19.14, isolated mode is available for all Oracle database deployments, including on-premises databases, legacy deployments, and engineered systems.

The `WALLET_ROOT` initialization parameter must be set in order for `TDE_CONFIGURATION` to take effect.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `TDE_CONFIGURATION = "{ KEYSTORE_CONFIGURATION = value [; CONTAINER = pdb-name] }"` |
| Syntax | value::=  `{`  ` FILE \|`  ` OKV \|`  ` HSM \|`  ` FILE\|OKV \|`  ` FILE\|HSM \|`  ` OKV\|FILE \|`  ` HSM\|FILE`  `}`  Notes:  - The `KEYSTORE_CONFIGURATION` value is case-insensitive. For example, you can specify `FILE` or `file`. - `FILE\|OKV`, `FILE\|HSM`, `OKV\|FILE`, and `HSM\|FILE` are values. The vertical bars they contain are not separators in the syntax shown above. |
| Default value | None |
| Modifiable | `ALTER SYSTEM` <sup>Foot 1</sup> |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | The same value must be specified on all instances using the `ALTER SYSTEM SET TDE_CONFIGURATION="KEYSTORE_CONFIGURATION=value" SCOPE=BOTH SID='*';` statement. |

<sup>Footnote 1</sup>

In some cases, when this parameter is set using `ALTER SYSTEM SCOPE=SPFILE`, the `SHOW PARAMETER TDE_CONFIGURATION` statement does not show the correct value. However, the value set for `TDE_CONFIGURATION` can be derived from information shown in the `V$ENCRYPTION_WALLET` view.

The following attributes can be specified:

- `KEYSTORE_CONFIGURATION` attribute. This attribute is required. The value specified with this attribute configures the keystore type for the specified PDB. The following values can be specified for this attribute:
	- `FILE`: This value configures a wallet keystore.
		- `OKV`: This value configures the database to use Oracle Key Vault (OKV) for TDE key management.
		This value is also used to disable an auto-login OKV configuration and cause any existing `cwallet.sso` files, containing the credentials to the OKV server as the `OKV_PASSWORD` client secret, to be ignored.
		- `HSM`: This value configures a hardware security module (HSM).
		Oracle does not support the use of HSMs for TDE key management. For more information, see My Oracle Support note KB593570 "Oracle TDE Support With 3rd Party HSM Vendors" at the following URL: [https://support.oracle.com/support/?documentId=KB593570](https://support.oracle.com/support/?documentId=KB593570)
		- `FILE|OKV`: This value configures a reverse migration from OKV to a wallet keystore.
		- `FILE|HSM`: This value configures a reverse migration from a HSM to a wallet keystore.
		- `OKV|FILE`: This value configures a migration from a wallet to OKV.
		This value is also used in an auto-login OKV configuration, because in this configuration a `cwallet.sso` file, containing the `OKV_PASSWORD` client secret, must be used by the Oracle server to obtain the credentials to log in to the OKV server.
		- `HSM|FILE`: This value configures a migration from a wallet to a HSM.
		Oracle does not support the use of HSMs for TDE key management. For more information, see My Oracle Support note KB593570 "Oracle TDE Support With 3rd Party HSM Vendors" at the following URL: [https://support.oracle.com/support/?documentId=KB593570](https://support.oracle.com/support/?documentId=KB593570)
	Some of the `KEYSTORE_CONFIGURATION` attribute values consist of a single word, for example, the `FILE`, `OKV`, and `HSM` values. The other `KEYSTORE_CONFIGURATION` attribute values consist of two words separated by the "|" character that is a required part of the value’s syntax, for example, the `FILE|OKV`, `FILE|HSM`, `OKV|FILE`, and `HSM|FILE` values.
	In Oracle Database releases prior to Oracle Database 18.1, keystore types were configured in `sqlnet.ora` using the `METHOD` attribute of the `SQLNET.ENCRYPTION_WALLET_LOCATION` parameter.
- `CONTAINER` attribute: This optional attribute can be used only when setting the parameter in the `CDB$ROOT` of a CDB. The `CONTAINER` attribute can be specified only when the `CDB$ROOT` is in `MOUNTED` state. With this attribute, you must specify the name of the PDB for which you are setting the parameter. When you specify the `CONTAINER` attribute, you must use a semicolon ";" as the separation character between the `KEYSTORE_CONFIGURATION` and `CONTAINER` attributes.

Examples

The following statement configures a wallet keystore for the open PDB from which the statement is issued:

```
ALTER SYSTEM SET TDE_CONFIGURATION="KEYSTORE_CONFIGURATION=FILE" SCOPE=BOTH SID='*';
```

The following statement configures an OKV keystore for the PDB in `MOUNTED` state from which the statement is issued:

```
ALTER SYSTEM SET TDE_CONFIGURATION="KEYSTORE_CONFIGURATION=OKV" SCOPE=SPFILE SID='*';
```

The following statement configures an isolated standby PDB for an auto-open Oracle Key Vault setup; standby PDBs are `MOUNTED`, so the command must be executed in the standby root CDB:

```
ALTER SYSTEM SET TDE_CONFIGURATION="KEYSTORE_CONFIGURATION=OKV|FILE; CONTAINER=FINANCIALS" SCOPE=both SID='*';
```

Note:

In an Oracle Data Guard configuration, during keystore migration to OKV or OCI Key Management Service (KMS), or reverse migration to FILE, after the configuration change to `OKV|FILE` or `FILE|OKV` respectively, the wallet must be closed and reopened on the standby.

See Also:

- [WALLET\_ROOT](WALLET_ROOT.md)
- [V$ENCRYPTION\_WALLET](V-ENCRYPTION_WALLET.md)
- [Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ASOAG-GUID-FA569DEC-6FF3-4CA1-86AA-D27F29EDCA3C) for information about managing keystores and encryption keys in united mode
- [Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ASOAG-GUID-ED5C479F-435F-47A5-AD96-8D874BEDA0AA) for information about managing keystores and encryption keys in isolated mode