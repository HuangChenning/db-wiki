---
title: "8.5.1 Data-Masking Components Versus the Data-Masking Plugin"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/data-masking-components-vs-plugin.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 8.5.1 Data-Masking Components Versus the Data-Masking Plugin

Previously, MySQL enabled masking and de-identification capabilities using a server-side plugin, but transitioned to use the component infrastructure as an alternative implementation. The following table briefly compares MySQL Enterprise Data Masking components and the plugin library to provide an overview of their differences. It may assist you in making the transition from the plugin to components.

Note

Only the data-masking components or the plugin should be enabled at a time. Enabling both components and the plugin is unsupported and results may not be as anticipated.

**Table 8.55 Comparison Between Data-Masking Components and Plugin Elements**

| Category | Components | Plugin |
| --- | --- | --- |
| Interface | Service functions, loadable functions | Loadable functions |
| Support for multibyte character sets | Yes, for general-purpose masking functions | No |
| General-purpose masking functions | [`mask_inner()`](data-masking-component-functions.md), [`mask_outer()`](data-masking-component-functions.md) | [`mask_inner()`](data-masking-plugin-functions.md), [`mask_outer()`](data-masking-plugin-functions.md) |
| Masking of specific types | PAN, SSN, IBAN, UUID, Canada SIN, UK NIN | PAN, SSN |
| Random generation, specific types | email, US phone, PAN, SSN, IBAN, UUID, Canada SIN, UK NIN | email, US phone, PAN, SSN |
| Random generation of integer from given range | Yes | Yes |
| Persisting substitution dictionaries | Database | File |
| Privilege to manage dictionaries | Dedicated privilege | FILE |
| Automated loadable-function registration/deregistration during installation/uninstallation | Yes | No |
| Enhancements to existing functions | More arguments added to the [`gen_rnd_email()`](data-masking-component-functions.md) function | N/A |