---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/LDAP_DIRECTORY_ACCESS.html
tags:
  - oracle
  - 12c
  - reference
---

`LDAP_DIRECTORY_ACCESS` specifies whether Oracle refers to Oracle Internet Directory for user authentication information.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `LDAP_DIRECTORY_ACCESS = { NONE \| PASSWORD \| SSL }` |
| Default value | `NONE` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
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

[Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=DBIMI152) for more information on Enterprise User Security

Using LDAP\_DIRECTORY\_ACCESS with PDBs

PDBs can use password and SSL authentication with Oracle Internet Directory when the default database wallet location is used.

Since there is only one `LDAP_DIRECTORY_ACCESS` initialization parameter per CDB, all the PDBs in a CDB will use the Oracle Internet Directory authentication specified by the parameter.

For a CDB, the default database wallet path is:

`ORACLE_BASE/admin/` db-unique-name/pdb-GUID `/wallet` (if `ORACLE_BASE` is set)

or:

`ORACLE_HOME/admin/` db-unique-name/pdb-GUID `/wallet` (if `ORACLE_BASE` is not set)

The exception is for the root database, which will a default wallet path of:

`ORACLE_BASE/admin/` db-unique-name `/wallet` (if `ORACLE_BASE` is set)

or:

`ORACLE_HOME/admin/` db-unique-name `/wallet` (if `ORACLE_BASE` is not set)

All the PDBs in a CDB have the same database unique name. By placing wallets in the default location, each PDB can have its own identity. Note that since there is only one `sqlnet.ora` file for a CDB, the wallet location in `sqlnet.ora` is not supported for CDBs, because each PDB must have its own wallet.

Note:

Oracle databases are registered with Oracle Internet Directory using Database Configuration Assistant (DBCA). For registration with Oracle Internet Directory to work, all the PDBs for a CDB must be registered using DBCA.

Using LDAP\_DIRECTORY\_ACCESS with Non-CDBs

For non-CDBs, the default database wallet path is:

`ORACLE_BASE/admin/` db-unique-name `/wallet` (if `ORACLE_BASE` is set)

or:

`ORACLE_HOME/admin/` db-unique-name `/wallet` (if `ORACLE_BASE` is not set)