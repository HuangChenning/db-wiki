---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DB_DOMAIN.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.80 DB\_DOMAIN

In a distributed database system, `DB_DOMAIN` specifies the logical location of the database within the network structure.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DB_DOMAIN = ` `domain_name` |
| Default value | There is no default value. |
| Modifiable | No |
| Modifiable in a PDB | Yes |
| Range of values | Any legal string of name components, separated by periods and up to 128 characters long (including the periods). |
| Basic | Yes |
| Oracle RAC | You must set this parameter for every instance, and multiple instances must have the same value. |

You should set this parameter if this database is or ever will be part of a distributed system. The value consists of the extension components of a global database name, consisting of valid identifiers (any alphanumeric ASCII characters), separated by periods.

Note:

Oracle recommends that you specify `DB_DOMAIN` as a unique string for all databases in a domain.

This parameter allows one department to create a database without worrying that it might have the same name as a database created by another department. If one sales department's `DB_DOMAIN` is `JAPAN.EXAMPLE.COM`, then their `SALES` database (`SALES.JAPAN.EXAMPLE.COM`) is uniquely distinguished from another database with `DB_NAME` = `SALES` but with `DB_DOMAIN` = `US.EXAMPLE.COM`.

If you omit the domains from the name of a database link, Oracle expands the name by qualifying the database with the domain of your local database as it currently exists in the data dictionary, and then stores the link name in the data dictionary. `DB_DOMAIN` should start with an alphabetic character and exclude these characters:
```
"!@%^&*()+=\\|\`~[{]};:'\",<>/?"
```

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN11102) for more information on setting this parameter
- The data dictionary view " [GLOBAL\_NAME](GLOBAL_NAME.md) "