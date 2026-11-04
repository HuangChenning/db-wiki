---
title: "6.5.4 MySQL Enterprise Data Masking and De-Identification Function Reference"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/data-masking-function-reference.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 6.5.4 MySQL Enterprise Data Masking and De-Identification Function Reference

**Table 6.35 MySQL Enterprise Data Masking and De-Identification Functions**

| Name | Description |
| --- | --- |
| `gen_blacklist()` | Perform dictionary term replacement |
| `gen_dictionary_drop()` | Remove dictionary from registry |
| `gen_dictionary_load()` | Load dictionary into registry |
| `gen_dictionary()` | Return random term from dictionary |
| `gen_range()` | Generate random number within range |
| `gen_rnd_email()` | Generate random email address |
| `gen_rnd_pan()` | Generate random payment card Primary Account Number |
| `gen_rnd_ssn()` | Generate random US Social Security Number |
| `gen_rnd_us_phone()` | Generate random US phone number |
| `mask_inner()` | Mask interior part of string |
| `mask_outer()` | Mask left and right parts of string |
| `mask_pan()` | Mask payment card Primary Account Number part of string |
| `mask_pan_relaxed()` | Mask payment card Primary Account Number part of string |
| `mask_ssn()` | Mask US Social Security Number |