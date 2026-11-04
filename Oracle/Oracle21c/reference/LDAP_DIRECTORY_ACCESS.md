---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/LDAP_DIRECTORY_ACCESS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.173 LDAP\_DIRECTORY\_ACCESS

`LDAP_DIRECTORY_ACCESS` specifies whether Oracle refers to Oracle Internet Directory for user authentication information.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `LDAP_DIRECTORY_ACCESS = { NONE \| PASSWORD \| SSL }` |
| Default value | `NONE` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |

If directory access is turned on, then this parameter also specifies how users are authenticated.

Values

- `NONE`
	Oracle does not refer to Oracle Internet Directory for Enterprise User Security information.
- `PASSWORD`
	Oracle tries to connect to the enterprise directory service using the database password stored in the database wallet. If that fails, then the Oracle Internet Directory connection fails and the database will not be able to retrieve enterprise roles and schema mappings upon enterprise user login.
- `SSL`
	Oracle tries to connect to Oracle Internet Directory using SSL.

See Also:

[Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBIMI152) for more information on Enterprise User Security

Using LDAP\_DIRECTORY\_ACCESS with PDBs

PDBs can use password or SSL authentication with Oracle Internet Directory for EUS, or Microsoft Active Directory for CMU, when the parameter value is set accordingly.

The `LDAP_DIRECTORY_ACCESS` initialization parameter is PDB-specific and can be set as follows:

- When you use the `ALTER` `SYSTEM` command to set the value of ` LDAP_DIRECTORY_ACCESS` while connected to the CDB root:
	- If you specify the `CONTAINER=ALL` clause, then the setting applies to the CDB root and all PDBs.
		- If you omit the `CONTAINER=ALL` clause, or specify the `CONTAINER=CURRENT` clause, then the setting applies only to the CDB root.
- When you use the `ALTER` `SYSTEM` command to set the value of ` LDAP_DIRECTORY_ACCESS` while connected to a PDB, the setting applies only to that PDB.
- When you set the value of `LDAP_DIRECTORY_ACCESS` in an initialization parameter file, the setting applies only to the CDB root; it does not apply to the PDBs.

For a CDB, if the wallet location is not specified in `sqlnet.ora`, then the default database wallet path is:

`ORACLE_BASE/admin/` db-unique-name/pdb-GUID `/wallet` (if `ORACLE_BASE` is set)

or:

`ORACLE_HOME/admin/` db-unique-name/pdb-GUID `/wallet` (if `ORACLE_BASE` is not set)

The exception is for the root database, which has a default wallet path of:

`ORACLE_BASE/admin/` db-unique-name `/wallet` (if `ORACLE_BASE` is set)

or:

`ORACLE_HOME/admin/` db-unique-name `/wallet` (if `ORACLE_BASE` is not set)

All PDBs in a CDB have the same database unique name. By placing wallets in the default location, each PDB can have its own identity.

Note that because there is only one `sqlnet.ora` file for a CDB, the wallet location in `sqlnet.ora` is only used by the CDB root container. Because each PDB must have its own wallet, a PDB wallet will be specified by the pdb-GUID under the wallet location in `sqlnet.ora`.

For the root container of a CDB, the wallet location is:

WALLET\_LOCATION\_specified\_in\_sqlnet.ora

For each PDB of the CDB, the wallet location is:

WALLET\_LOCATION\_specified\_in\_sqlnet.ora `/` pdb-GUID `/`

Note:

Oracle databases are registered with Oracle Internet Directory using Database Configuration Assistant (DBCA). For registration with Oracle Internet Directory to work, all the PDBs for a CDB must be registered using DBCA.

Using LDAP\_DIRECTORY\_ACCESS with Non-CDBs

For non-CDBs, if the wallet location is not specified in `sqlnet.ora`, then the default database wallet path is:

`ORACLE_BASE/admin/` db-unique-name `/wallet` (if `ORACLE_BASE` is set)

or:

`ORACLE_HOME/admin/` db-unique-name `/wallet` (if `ORACLE_BASE` is not set)