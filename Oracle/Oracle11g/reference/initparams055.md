---
title: DB_DOMAIN
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams055.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DB_DOMAIN =` `domain_name` |
| Default value | There is no default value. |
| Modifiable | No |
| Range of values | Any legal string of name components, separated by periods and up to 128 characters long (including the periods). |
| Basic | Yes |
| Oracle RAC | You must set this parameter for every instance, and multiple instances must have the same value. |

In a distributed database system, `DB_DOMAIN` specifies the logical location of the database within the network structure. You should set this parameter if this database is or ever will be part of a distributed system. The value consists of the extension components of a global database name, consisting of valid identifiers (any alphanumeric ASCII characters), separated by periods.

Note:

Oracle recommends that you specify `DB_DOMAIN` as a unique string for all databases in a domain.

This parameter allows one department to create a database without worrying that it might have the same name as a database created by another department. If one sales department's `DB_DOMAIN` is `JAPAN.ACME.COM`, then their `SALES` database (`SALES.JAPAN.ACME.COM`) is uniquely distinguished from another database with `DB_NAME` = `SALES` but with `DB_DOMAIN` = `US.ACME.COM`.

If you omit the domains from the name of a database link, Oracle expands the name by qualifying the database with the domain of your local database as it currently exists in the data dictionary, and then stores the link name in the data dictionary. The characters valid in a database domain name are: alphanumeric characters, underscore (\_), and number sign (#).

See Also:

- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for more information on setting this parameter
- The data dictionary view ["GLOBAL\_NAME"](statviews_5127.md)