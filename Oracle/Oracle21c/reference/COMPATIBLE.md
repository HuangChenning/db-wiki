---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/COMPATIBLE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.50 COMPATIBLE

`COMPATIBLE` enables you to use a new release of Oracle while ensuring the ability to downgrade the database to an earlier release.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `COMPATIBLE = ` `release_number` |
| Default value | `21.0.0` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | `12.2.0` to default release  Values must be specified as at least three decimal numbers with each pair separated by a dot, such as `21.0.0` or `21.0.0.0.0` |
| Basic | Yes |
| Oracle RAC | Multiple instances must have the same value. |

The `COMPATIBLE` parameter specifies the Oracle version number that the database disk format must be compatible with. The database can be downgraded to the version specified in the `COMPATIBLE` parameter or any later version.

Setting `COMPATIBLE` ensures that new features do not write data formats or structures to disk that are not compatible with the earlier release, preventing a future downgrade. Features that require a higher value of `COMPATIBLE` to work correctly may be restricted or disabled to ensure downgrades are possible.

Typically, users keep `COMPATIBLE` unchanged when upgrading their Oracle software. After upgrade, users will run the new release of the Oracle software for a few weeks to ensure that the new release is working correctly. Afterwards, users can choose to update `COMPATIBLE` to the latest version to take advantage of the new features.

Notes:

- The value of the `COMPATIBLE` parameter can be increased to a higher version, but it can never be decreased to a lower version.
- The value of the `COMPATIBLE` parameter should not be changed for a Release Update (RU) or Release Update Revision (RUR). For example, assume you are running Oracle Database 21c and the value of `COMPATIBLE` is `21.0.0`. You then apply Oracle Database Release Update 21.4.0.0.0. Do not set the value of `COMPATIBLE` to `21.4.0`; leave it set to `21.0.0`.
- When using a standby database, this parameter must have the same value on both the primary and standby databases.

See Also:

[Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=UPGRD-GUID-7FCE8614-8163-4393-AE66-2ADD1F73934F) for more information on setting this parameter