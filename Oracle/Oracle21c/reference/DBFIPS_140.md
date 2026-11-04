---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBFIPS_140.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.100 DBFIPS\_140

`DBFIPS_140` enables Transparent Data Encryption (TDE) and `DBMS_CRYPTO` PL/SQL package program units to run in a mode compliant to the Federal Information Processing Standard (subsequently known as "FIPS mode").

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `FALSE` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | `TRUE \| FALSE` |
| Basic | No |
| Oracle RAC | All instances must use the same value. |

Values:

- `TRUE`
	Set this parameter to `TRUE` to use TDE and `DBMS_CRYPTO` in FIPS mode. This means that only FIPS-compliant algorithms may be used.
	This method of configuring FIPS mode is considered a legacy configuration, but it is still supported. Oracle recommends that you instead use the consolidated `FIPS_140` parameter in the `fips.ora` file. See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG1041) for more information.
- `FALSE`
	When this parameter is set to `FALSE`, all algorithms (FIPS-compliant or not) may be used. This is the default.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG1060) for a table that describes the effect of setting the value of `DBFIPS_140` to `TRUE` or `FALSE` on different platforms