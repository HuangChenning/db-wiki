---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-ENCRYPTION_WALLET.html
tags:
  - oracle
  - 12c
  - reference
---

`V$ENCRYPTION_WALLET` displays information on the status of the wallet and the wallet location for Transparent Data Encryption.

| Column | Datatype | Description |
| --- | --- | --- |
| `WRL_TYPE` | `VARCHAR2(20)` | Type of the wallet resource locator (for example, `FILE`) |
| `WRL_PARAMETER` | `VARCHAR2(4000)` | Parameter of the wallet resource locator (for example, absolute directory location of the wallet or keystore, if `WRL_TYPE` = `FILE`) |
| `STATUS` | `VARCHAR2(30)` | Status of the wallet. Possible values:  - `CLOSED`: The wallet is closed - `NOT_AVAILABLE`: The wallet is not available in the location specified by the `WALLET_ROOT` initialization parameter - `OPEN`: The wallet is open - `OPEN_NO_MASTER_KEY`: The wallet is open, but no master key is set - `OPEN_UNKNOWN_MASTER_KEY_STATUS`: The wallet is open, but the database could not determine whether the master key is set. This situation can occur when the database is in the mounted state and cannot check if the master key for a hardware keystore is set because the data dictionary is not available. - `UNDEFINED`: The database could not determine the status of the wallet |
| `WALLET_TYPE` | `VARCHAR2(20)` | Displays the type of keystore being used, `HSM` or `SOFTWARE_KEYSTORE`.  If the keystore was created with the `mkstore` utility, then the `WALLET_TYPE` is `UNKNOWN`. Oracle recommends that you create keystores with the `ADMINISTER` `KEY` `MANAGEMENT` statement. |
| `WALLET_ORDER` | `VARCHAR2(9)` | If only a single wallet is configured, the value in this column is `SINGLE`.  When more than one wallet is configured, the value in this column shows whether the wallet is primary (holds the current master key) or secondary (holds old keys). The lookup of the master key will happen in the primary keystore first, and then in the secondary keystore, if required.  Possible values:  - `PRIMARY` - `SECONDARY`  If there is only one type of keystore (Hardware Security Module or Software Keystore) being used, then `PRIMARY` will appear.  If both types are used, then the value in this column shows the order in which each keystore will be looked up. |
| `FULLY_BACKED_UP` | `VARCHAR2(9)` | Indicates whether all the keys in the keystore have been backed up |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |