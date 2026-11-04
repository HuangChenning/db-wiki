---
title: "30.1 Prerequisites for Using the sys Schema"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/sys-schema-prerequisites.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

Before using the [`sys`](sys-schema.md) schema, the prerequisites described in this section must be satisfied.

Because the [`sys`](sys-schema.md) schema provides an alternative means of accessing the Performance Schema, the Performance Schema must be enabled for the [`sys`](sys-schema.md) schema to work. See [Section 29.3, “Performance Schema Startup Configuration”](performance-schema-startup-configuration.md).

For full access to the [`sys`](sys-schema.md) schema, a user must have these privileges:

- [`SELECT`](privileges-provided.md) on all [`sys`](sys-schema.md) tables and views
- [`EXECUTE`](privileges-provided.md) on all [`sys`](sys-schema.md) stored procedures and functions
- [`INSERT`](privileges-provided.md) and [`UPDATE`](privileges-provided.md) for the [`sys_config`](sys-sys-config.md) table, if changes are to be made to it
- Additional privileges for certain [`sys`](sys-schema.md) schema stored procedures and functions, as noted in their descriptions (for example, the [`ps_setup_save()`](sys-ps-setup-save.md) procedure)

It is also necessary to have privileges for the objects underlying the [`sys`](sys-schema.md) schema objects:

Certain Performance Schema instruments and consumers must be enabled and (for instruments) timed to take full advantage of [`sys`](sys-schema.md) schema capabilities:

- All `wait` instruments
- All `stage` instruments
- All `statement` instruments
- ``*`xxx`*_current`` and ``*`xxx`*_history_long`` consumers for all events

You can use the [`sys`](sys-schema.md) schema itself to enable all of the additional instruments and consumers:

```
CALL sys.ps_setup_enable_instrument('wait');
CALL sys.ps_setup_enable_instrument('stage');
CALL sys.ps_setup_enable_instrument('statement');
CALL sys.ps_setup_enable_consumer('current');
CALL sys.ps_setup_enable_consumer('history_long');
```

For many uses of the `sys` schema, the default Performance Schema is sufficient for data collection. Enabling all the instruments and consumers just mentioned has a performance impact, so it is preferable to enable only the additional configuration you need. Also, remember that if you enable additional configuration, you can easily restore the default configuration like this:

```
CALL sys.ps_setup_reset_to_default(TRUE);
```