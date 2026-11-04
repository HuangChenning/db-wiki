---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ENCRYPTION_WALLET.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.199 V$ENCRYPTION\_WALLET

`V$ENCRYPTION_WALLET` displays information on the status of the wallet and the wallet location for Transparent Data Encryption (TDE).

In a multitenant container database (CDB), this view displays information on the wallets for all pluggable database (PDBs) when queried from `CDB$ROOT`. When queried from a PDB, this view only displays wallet details of that PDB.

Note that, even if TDE is not configured in the database, a query of `V$ENCRYPTION_WALLET` checks for TDE configuration validity and may print warnings in alert log.

| Column | Datatype | Description |
| --- | --- | --- |
| `WRL_TYPE` | `VARCHAR2(20)` | Type of the wallet resource locator (for example, `FILE`) |
| `WRL_PARAMETER` | `VARCHAR2(4000)` | Parameter of the wallet resource locator (for example, absolute directory location of the wallet or keystore, if `WRL_TYPE` = `FILE`) |
| `STATUS` | `VARCHAR2(30)` | Status of the wallet. Possible values:  - `CLOSED`: The wallet is closed - `NOT_AVAILABLE`: The wallet is not available in the location specified by the `WALLET_ROOT` initialization parameter - `OPEN`: The wallet is open - `OPEN_NO_MASTER_KEY`: The wallet is open, but no master key is set - `OPEN_UNKNOWN_MASTER_KEY_STATUS`: The wallet is open, but the database could not determine whether the master key is set. This situation can occur when the database is in the mounted state and cannot check if the master key for a hardware keystore is set because the data dictionary is not available. - `UNDEFINED`: The database could not determine the status of the wallet |
| `WALLET_TYPE` | `VARCHAR2(20)` | Displays the type of keystore being used, `FILE` or `OKV`  If the keystore was created with the `mkstore` utility, then the `WALLET_TYPE` is `UNKNOWN`. Oracle recommends that you create keystores with the `ADMINISTER` `KEY` `MANAGEMENT` statement. |
| `WALLET_ORDER` | `VARCHAR2(9)` | Possible values:  - `SINGLE` - This value is displayed: 	- When only a single wallet is configured 		- In an auto-login OKV configuration. In this case, `TDE_CONFIGURATION` = `OKV\|FILE`, and the `SINGLE` value is displayed for both the `OKV` and `FILE` keystores. - `PRIMARY` - When more than one wallet is configured, this value indicates that the wallet is primary (holds the current master key). - `SECONDARY` - When more than one wallet is configured, this value indicates that the wallet is secondary (holds old keys).  The lookup of master keys happens in the primary keystore first, and then in the secondary keystore, if required.  If there is only one type of keystore (Hardware Security Module or Software Keystore) being used, then `SINGLE` will appear.  If both types are used, then the value in this column shows the order in which each keystore will be looked up. |
| `KEYSTORE_MODE` | `VARCHAR2(8)` | Displays the keystore mode:  - `NONE`: This value is seen when this column is queried from the `CDB$ROOT`, or when the database is a non-CDB. The keystore mode does not apply in these cases. - `UNITED`: The PDB is configured to use the wallet of the `CDB$ROOT`. To open the wallet in this configuration, the password of the wallet of the `CDB$ROOT` must be used. - `ISOLATED`: The PDB is configured to use its own wallet. To open the wallet in this configuration, the password of the isolated wallet must be used. |
| `FULLY_BACKED_UP` | `VARCHAR2(9)` | Indicates whether all the keys in the keystore have been backed up |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |