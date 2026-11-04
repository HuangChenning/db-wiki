---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/COMPATIBLE.html
tags:
  - oracle
  - 12c
  - reference
---

`COMPATIBLE` enables you to use a new release of Oracle while ensuring the ability to downgrade the database to an earlier release.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `COMPATIBLE = ` `release_number` |
| Default value | `12.2.0` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | `11.2.0` to default release  Values must be specified as at least three decimal numbers with each pair separated by a dot, such as `12.2.0` or `12.2.0.0.0` |
| Basic | Yes |
| Oracle RAC | Multiple instances must have the same value. |

The `COMPATIBLE` parameter specifies the Oracle version number that the database disk format must be compatible with. The database can be downgraded to the version specified in the `COMPATIBLE` parameter or any later version.

Setting `COMPATIBLE` ensures that new features do not write data formats or structures to disk that are not compatible with the earlier release, preventing a future downgrade. Features that require a higher value of `COMPATIBLE` to work correctly may be restricted or disabled to ensure downgrades are possible.

Typically, users keep `COMPATIBLE` unchanged when upgrading their Oracle software. After upgrade, users will run the new release of the Oracle software for a few weeks to ensure that the new release is working correctly. Afterwards, users can choose to update `COMPATIBLE` to the latest version to take advantage of the new features.

Notes:

- The value of the `COMPATIBLE` parameter can be increased to a higher version, but it can never be decreased to a lower version.
- When using a standby database, this parameter must have the same value on both the primary and standby databases.
- When you set the value of the `COMPATIBLE` parameter to `12.2.0`, the maximum size of SQL identifiers is increased from 30 bytes to 128 bytes.

See Also:

[Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=UPGRD-GUID-7FCE8614-8163-4393-AE66-2ADD1F73934F) for more information on setting this parameter