---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ONE_STEP_PLUGIN_FOR_PDB_WITH_TDE.html
tags:
  - oracle
  - 12c
  - reference
---

If a pluggable database (PDB) has Transparent Data Encryption-encrypted (TDE-encrypted) tables or tablespaces, you can enable `ONE_STEP_PLUGIN_FOR_PDB_WITH_TDE` on the target CDB to simplify the move of TDE keys in a single step PDB move operation. `ONE_STEP_PLUGIN_FOR_PDB_WITH_TDE` eliminates the need of having to manually provide a keystore password when you import the TDE keys into the PDB after it has moved to the target CDB.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `FALSE` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | A different value can be set for this parameter on different Oracle RAC instances. |

The default for `ONE_STEP_PLUGIN_FOR_PDB_WITH_TDE` is `FALSE`.

When `ONE_STEP_PLUGIN_FOR_PDB_WITH_TDE` is set to `TRUE` on the target CDB, the plug in of the PDB does not require a keystore password.

See Also:

[Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ASOAG-GUID-5B665567-8414-4F8E-A08B-DC624690BCB8) for more information about `ONE_STEP_PLUGIN_FOR_PDB_WITH_TDE` and for an example of using the parameter.