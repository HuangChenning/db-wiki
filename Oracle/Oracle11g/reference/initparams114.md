---
title: LDAP_DIRECTORY_ACCESS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams114.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `LDAP_DIRECTORY_ACCESS = { NONE \| PASSWORD \| SSL }` |
| Default value | `NONE` |
| Modifiable | `ALTER SYSTEM` |
| Basic | No |

`LDAP_DIRECTORY_ACCESS` specifies whether Oracle refers to Oracle Internet Directory for user authentication information. If directory access is turned on, then this parameter also specifies how users are authenticated.

Values:

- `NONE`
	Oracle does not refer to Oracle Internet Directory for Enterprise User Security information.
- `PASSWORD`
	Oracle tries to connect to the enterprise directory service using the database password stored in the database wallet. If that fails, then the Oracle Internet Directory connection fails and the database will not be able to retrieve enterprise roles and schema mappings upon enterprise user login.
- `SSL`
	Oracle tries to connect to Oracle Internet Directory using SSL.

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm) for more information on Enterprise User Security