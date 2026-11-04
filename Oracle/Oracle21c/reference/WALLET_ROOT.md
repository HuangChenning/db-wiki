---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/WALLET_ROOT.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.380 WALLET\_ROOT

`WALLET_ROOT` specifies the path to the root of a directory tree containing a subdirectory for each pluggable database (PDB).

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `WALLET_ROOT = wallet-root-directory-path` |
| Default value | There is no default value. |
| Modifiable | No |
| Modifiable in a PDB | No |
| Basic | No |
| Oracle RAC | Multiple instances must have the same value. |

The name of the various wallet files is always the same, regardless of the component they are associated with. The wallets for each component are stored under each PDB GUID directory within the `WALLET_ROOT` directory structure in a directory whose name is based on the component name. For example, for the TDE component, the subdirectory name is `tde`.

If the `WALLET_ROOT` parameter is not set, the `SQLNET.ENCRYPTION_WALLET_LOCATION` parameter is used (as in Oracle Database releases prior to Oracle Database 18c), but no isolated keystore can be used unless the `WALLET_ROOT` parameter is set. The `TDE_CONFIGURATION` initialization parameter cannot be used to configure any PDB to run in isolated mode unless the `WALLET_ROOT` parameter is also set.

Note:

The `SQLNET.ENCRYPTION_WALLET_LOCATION` parameter is deprecated in Oracle Database 18c.

For example, the contents of the directory at the location specified by the `WALLET_ROOT` initialization parameter could look as follows, where wallet-root is the directory specified by the `WALLET_ROOT` parameter:

```
wallet-root/eus/ewallet.p12
wallet-root/tde/ewallet.p12
wallet-root/tde/ewallet_2016120918333644.p12
wallet-root/tde_seps/cwallet.sso
wallet-root/tls/ewallet.p12
wallet-root/xdb_wallet/ewallet.p12
wallet-root/3FD1C95B48205D0FE053C5A0E40AEF8C/tde/ewallet.p12
wallet-root/3FD1C95B48205D0FE053C5A0E40AEF8C/tde/ewallet_2016110918331622.p12
wallet-root/3FD1C95B48205D0FE053C5A0E40AEF8C/tde/ewallet_2016110918332363.p12
wallet-root/3FD1C95B48205D0FE053C5A0E40AEF8C/tde_seps/cwallet.sso
wallet-root/3FD1C95B48205D0FE053C5A0E40AEF8C/tls/cwallet.sso
wallet-root/3FD1C95B48205D0FE053C5A0E40AEF8C/tls/ewallet.p12
```

When the `WALLET_ROOT` parameter is set, you can omit the path from some `ADMINISTER KEY MANAGEMENT` commands.

The `WALLET_ROOT` value can include references to environment variables. The following example shows how to use `WALLET_ROOT` when multiple TDE-enabled databases are installed into the same `ORACLE_HOME`:

```
WALLET_ROOT=/etc/ORACLE/KEYSTORES/$ORACLE_SID
```

The `ORACLE_SID` environment variable (or the `DB_UNIQUE_NAME` environment variable for Oracle RAC) makes sure that each database that is installed into the same `ORACLE_HOME` has its own set of wallets and TDE keys. This sets the root of the wallet directory hierarchy to the directory specified by `wallet-root-directory-path`.

Note:

The normalized length of the `wallet-root-directory-name` that is specified with the `WALLET_ROOT` parameter cannot exceed 255 characters, otherwise one of the following sets of error messages is displayed:

```
ORA-46693: The WALLET_ROOT location is missing or invalid.
ORA-32021: parameter value longer than 255 characters
ORA-01078: failure in processing system parameters
```

```
ORA-46693: The WALLET_ROOT location is missing or invalid.
ORA-07204: sltln: name translation failed due to lack of output buffer space.
ORA-01078: failure in processing system parameters
```

The normalized length includes the length of expanded environment variables specified with the `WALLET_ROOT` parameter. The values of the environment variables of the user who starts the instance are used in the normalization of the `WALLET_ROOT` parameter.

The `SHOW PARAMETER WALLET_ROOT` command always displays the normalized value (with all the environment variables expanded).

For non-ASM file systems, the PDB GUID-extended paths for the TDE component are created automatically under the directory specified by the `WALLET_ROOT` parameter when any Transparent Data Encryption (TDE) wallet is created for a PDB.

Enabling Automatic Creation of Directories Under WALLET\_ROOT

By using the specific configuration of `WALLET_ROOT` described in each of the following sub-sections, Oracle Database can be configured to automatically create the necessary pdb-guid and component name directories under the `WALLET_ROOT` directory path. Other settings of `WALLET_ROOT` are allowed, but would not result in the automatic creation of the necessary sub-directories by the ASM OMF layer.

Required setting to enable auto-directory creation for a database not using Oracle ASM

For a database not using Oracle ASM filesystems, the `WALLET_ROOT` parameter needs to be set as follows:

```
WALLET_ROOT=wallet-root-directory-path
```

This sets the root of the wallet directory hierarchy to the directory specified by `wallet-root-directory-path`. For example:

```
/etc/ORACLE/KEYSTORES/FINANCE
```

When this is done, Oracle Database automatically creates the directory for the TDE wallet of a CDB$ROOT at the following location:

```
/etc/ORACLE/KEYSTORES/FINANCE/tde
```

The directories, that Oracle Database automatically creates for holding the TDE wallets of isolated PDBs, will include the pdb-guid. For example:

```
/etc/ORACLE/KEYSTORES/FINANCE/3FD1C95B48205D0FE053C5A0E40AEF8C/tde
```

Required setting to enable auto-directory creation for a database using Oracle ASM with Oracle Managed Files

For a database using ASM with OMF, the `WALLET_ROOT` parameter needs to begin with a plus sign followed by a disk group name and the value of the `DB_UNIQUE_NAME` initialization parameter. In the example below, `DATA` is the name of a disk group and `FINRAC` is the value of the `DB_UNIQUE_NAME` initialization parameter:

```
WALLET_ROOT=+DATA/FINRAC
```

When this is done, Oracle Database automatically creates the necessary directory within the ASM filesystem at the following location when the `ADMINISTER` `KEY` `MANAGEMENT` `CREATE` `KEYSTORE` command is run:

```
+DATA/FINRAC/tde
```

For isolated PDBs, the directories that Oracle Database automatically creates for holding the TDE wallets of PDBs will include the pdb-guid. For example:

```
+DATA/FINRAC/3FD1C95B48205D0FE053C5A0E40AEF8C/tde
```

Required setting to enable auto-directory creation for RAC-enabled databases

For a RAC-enabled database, only shared TDE wallets are supported (as opposed to individual TDE-wallets per RAC instance). `WALLET_ROOT` can either point to an ASM disk group, or a directory in ACFS. If the `WALLET_ROOT` parameter points to `+` `diskgroup` `/` `dbname`, then the `/tde` sub-directory is automatically created when issuing an `ADMINISTER` `KEY` `MANAGEMENT` `CREATE` `KEYSTORE` command. For example, when `WALLET_ROOT` is set to `+DATA/FINANCE`, the directory `+DATA/FINANCE/tde` is automatically created. This guarantees that when multiple databases are installed, their TDE-wallets are kept separate.

See Also:

" [TDE\_CONFIGURATION](TDE_CONFIGURATION.md) "