---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/PRIVATE_TEMP_TABLE_PREFIX.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.293 PRIVATE\_TEMP\_TABLE\_PREFIX

`PRIVATE_TEMP_TABLE_PREFIX` specifies the prefix that the database uses for private temporary tables.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `PRIVATE_TEMP_TABLE_PREFIX =` `string` |
| Default value | `ORA$PTT_` |
| Modifiable | `ALTER SYSTEM ... DEFERRED` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | The same value must be specified on each instance. |

The default value used for the `PRIVATE_TEMP_TABLE_PREFIX` parameter is `ORA$PTT_`.

If you choose to specify a different prefix value, it must begin with the string `ORA$` and must be unique across the database. Use the following SQL query to determine if the prefix value is unique (in the query, replace prefix-value with your actual prefix value):

```
select count(*) from obj$ where name like '<prefix-value>%';
```

If the above query returns 0, then the prefix you specified is an appropriate value to set.

Note:

After setting the prefix, regular table, view, and object names cannot use the same prefix.

See Also:

- " [DBA\_PRIVATE\_TEMP\_TABLES](DBA_PRIVATE_TEMP_TABLES.md) "
- " [USER\_PRIVATE\_TEMP\_TABLES](USER_PRIVATE_TEMP_TABLES.md) "
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN-GUID-6EB347F0-64BA-4B15-8182-41BA7D5A876F) for an introduction to private temporary tables