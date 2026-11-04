---
title: "12.2 Loadable Function Reference"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/loadable-function-reference.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

The following table lists each function that is loadable at runtime and provides a short description of each one. For a table listing built-in functions and operators, see [Section 12.1, “Built-In Function and Operator Reference”](built-in-function-reference.md)

For general information about loadable functions, see [Section 5.6, “MySQL Server Loadable Functions”](server-loadable-functions.md).

**Table 12.2 Loadable Functions**

| Name | Description |
| --- | --- |
| [`asymmetric_decrypt()`](enterprise-encryption-functions.md) | Decrypt ciphertext using private or public key |
| [`asymmetric_derive()`](enterprise-encryption-functions.md) | Derive symmetric key from asymmetric keys |
| [`asymmetric_encrypt()`](enterprise-encryption-functions.md) | Encrypt cleartext using private or public key |
| [`asymmetric_sign()`](enterprise-encryption-functions.md) | Generate signature from digest |
| [`asymmetric_verify()`](enterprise-encryption-functions.md) | Verify that signature matches digest |
| [`audit_log_encryption_password_get()`](audit-log-reference.md) | Fetch audit log encryption password |
| [`audit_log_encryption_password_set()`](audit-log-reference.md) | Set audit log encryption password |
| [`audit_log_filter_flush()`](audit-log-reference.md) | Flush audit log filter tables |
| [`audit_log_filter_remove_filter()`](audit-log-reference.md) | Remove audit log filter |
| [`audit_log_filter_remove_user()`](audit-log-reference.md) | Unassign audit log filter from user |
| [`audit_log_filter_set_filter()`](audit-log-reference.md) | Define audit log filter |
| [`audit_log_filter_set_user()`](audit-log-reference.md) | Assign audit log filter to user |
| [`audit_log_read()`](audit-log-reference.md) | Return audit log records |
| [`audit_log_read_bookmark()`](audit-log-reference.md) | Bookmark for most recent audit log event |
| [`create_asymmetric_priv_key()`](enterprise-encryption-functions.md) | Create private key |
| [`create_asymmetric_pub_key()`](enterprise-encryption-functions.md) | Create public key |
| [`create_dh_parameters()`](enterprise-encryption-functions.md) | Generate shared DH secret |
| [`create_digest()`](enterprise-encryption-functions.md) | Generate digest from string |
| [`flush_rewrite_rules()`](rewriter-query-rewrite-plugin-reference.md) | Load rewrite\_rules table into Rewriter cache |
| `gen_blacklist()` | Perform dictionary term replacement |
| `gen_dictionary_drop()` | Remove dictionary from registry |
| `gen_dictionary_load()` | Load dictionary into registry |
| `gen_dictionary()` | Return random term from dictionary |
| `gen_range()` | Generate random number within range |
| `gen_rnd_email()` | Generate random email address |
| `gen_rnd_pan()` | Generate random payment card Primary Account Number |
| `gen_rnd_ssn()` | Generate random US Social Security Number |
| `gen_rnd_us_phone()` | Generate random US phone number |
| [`keyring_aws_rotate_cmk()`](keyring-functions-plugin-specific.md) | Rotate AWS customer master key |
| [`keyring_aws_rotate_keys()`](keyring-functions-plugin-specific.md) | Rotate keys in keyring\_aws storage file |
| [`keyring_key_fetch()`](keyring-functions-general-purpose.md) | Fetch keyring key value |
| [`keyring_key_generate()`](keyring-functions-general-purpose.md) | Generate random keyring key |
| [`keyring_key_length_fetch()`](keyring-functions-general-purpose.md) | Return keyring key length |
| [`keyring_key_remove()`](keyring-functions-general-purpose.md) | Remove keyring key |
| [`keyring_key_store()`](keyring-functions-general-purpose.md) | Store key in keyring |
| [`keyring_key_type_fetch()`](keyring-functions-general-purpose.md) | Return keyring key type |
| [`load_rewrite_rules()`](rewriter-query-rewrite-plugin-reference.md) | Rewriter plugin helper routine |
| `mask_inner()` | Mask interior part of string |
| `mask_outer()` | Mask left and right parts of string |
| `mask_pan()` | Mask payment card Primary Account Number part of string |
| `mask_pan_relaxed()` | Mask payment card Primary Account Number part of string |
| `mask_ssn()` | Mask US Social Security Number |
| [`mysql_firewall_flush_status()`](firewall-reference.md) | Reset firewall status variables |
| [`normalize_statement()`](firewall-reference.md) | Normalize SQL statement to digest form |
| [`read_firewall_users()`](firewall-reference.md) | Update firewall account profile cache |
| [`read_firewall_whitelist()`](firewall-reference.md) | Update firewall account profile recorded-statement cache |
| [`service_get_read_locks()`](locking-service.md) | Acquire locking service shared locks |
| [`service_get_write_locks()`](locking-service.md) | Acquire locking service exclusive locks |
| [`service_release_locks()`](locking-service.md) | Release locking service locks |
| [`set_firewall_mode()`](firewall-reference.md) | Establish firewall account profile operational mode |
| [`version_tokens_delete()`](version-tokens-reference.md) | Delete tokens from version tokens list |
| [`version_tokens_edit()`](version-tokens-reference.md) | Modify version tokens list |
| [`version_tokens_lock_exclusive()`](version-tokens-reference.md) | Acquire exclusive locks on version tokens |
| [`version_tokens_lock_shared()`](version-tokens-reference.md) | Acquire shared locks on version tokens |
| [`version_tokens_set()`](version-tokens-reference.md) | Set version tokens list |
| [`version_tokens_show()`](version-tokens-reference.md) | Return version tokens list |
| [`version_tokens_unlock()`](version-tokens-reference.md) | Release version tokens locks |