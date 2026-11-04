---
title: "14.2 Loadable Function Reference"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/loadable-function-reference.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

The following table lists each function that is loadable at runtime and provides a short description of each one. For a table listing built-in functions and operators, see [Section 14.1, “Built-In Function and Operator Reference”](built-in-function-reference.md)

For general information about loadable functions, see [Section 7.7, “MySQL Server Loadable Functions”](server-loadable-functions.md).

**Table 14.2 Loadable Functions**

| Name | Description | Deprecated |
| --- | --- | --- |
| [`asymmetric_decrypt()`](enterprise-encryption-functions.md) | Decrypt ciphertext using private or public key |  |
| `asymmetric_derive()` | Derive symmetric key from asymmetric keys |  |
| [`asymmetric_encrypt()`](enterprise-encryption-functions.md) | Encrypt cleartext using private or public key |  |
| [`asymmetric_sign()`](enterprise-encryption-functions.md) | Generate signature from digest |  |
| [`asymmetric_verify()`](enterprise-encryption-functions.md) | Verify that signature matches digest |  |
| [`asynchronous_connection_failover_add_managed()`](replication-functions-async-failover.md) | Add a replication source server in a managed group to the source list |  |
| [`asynchronous_connection_failover_add_source()`](replication-functions-async-failover.md) | Add a replication source server to the source list |  |
| [`asynchronous_connection_failover_delete_managed()`](replication-functions-async-failover.md) | Remove managed group of replication source servers from the source list |  |
| [`asynchronous_connection_failover_delete_source()`](replication-functions-async-failover.md) | Remove a replication source server from the source list |  |
| [`audit_api_message_emit_udf()`](audit-api-message-emit.md) | Add message event to audit log |  |
| [`audit_log_encryption_password_get()`](audit-log-reference.md) | Fetch audit log encryption password |  |
| [`audit_log_encryption_password_set()`](audit-log-reference.md) | Set audit log encryption password |  |
| [`audit_log_filter_flush()`](audit-log-reference.md) | Flush audit log filter tables |  |
| [`audit_log_filter_remove_filter()`](audit-log-reference.md) | Remove audit log filter |  |
| [`audit_log_filter_remove_user()`](audit-log-reference.md) | Unassign audit log filter from user |  |
| [`audit_log_filter_set_filter()`](audit-log-reference.md) | Define audit log filter |  |
| [`audit_log_filter_set_user()`](audit-log-reference.md) | Assign audit log filter to user |  |
| [`audit_log_read()`](audit-log-reference.md) | Return audit log records |  |
| [`audit_log_read_bookmark()`](audit-log-reference.md) | Bookmark for most recent audit log event |  |
| [`audit_log_rotate()`](audit-log-reference.md) | Rotate audit log file |  |
| [`create_asymmetric_priv_key()`](enterprise-encryption-functions.md) | Create private key |  |
| [`create_asymmetric_pub_key()`](enterprise-encryption-functions.md) | Create public key |  |
| `create_dh_parameters()` | Generate shared DH secret |  |
| [`create_digest()`](enterprise-encryption-functions.md) | Generate digest from string |  |
| [`firewall_group_delist()`](firewall-reference.md) | Remove account from firewall group profile |  |
| [`firewall_group_enlist()`](firewall-reference.md) | Add account to firewall group profile |  |
| [`flush_rewrite_rules()`](rewriter-query-rewrite-plugin-reference.md) | Load rewrite\_rules table into Rewriter cache |  |
| [`gen_blacklist()`](data-masking-plugin-functions.md) | Perform dictionary term replacement | Yes |
| [`gen_blocklist()`](data-masking-component-functions.md) | Perform dictionary term replacement |  |
| [`gen_blocklist()`](data-masking-plugin-functions.md) | Perform dictionary term replacement |  |
| [`gen_dictionary()`](data-masking-component-functions.md) | Return random term from dictionary |  |
| [`gen_dictionary_drop()`](data-masking-plugin-functions.md) | Remove dictionary from registry |  |
| [`gen_dictionary_load()`](data-masking-plugin-functions.md) | Load dictionary into registry |  |
| [`gen_dictionary()`](data-masking-plugin-functions.md) | Return random term from dictionary |  |
| [`gen_range()`](data-masking-component-functions.md) | Generate random number within range |  |
| [`gen_range()`](data-masking-plugin-functions.md) | Generate random number within range |  |
| [`gen_rnd_canada_sin()`](data-masking-component-functions.md) | Generate random Canada Social Insurance Number |  |
| [`gen_rnd_email()`](data-masking-component-functions.md) | Generate random email address |  |
| [`gen_rnd_email()`](data-masking-plugin-functions.md) | Generate random email address |  |
| [`gen_rnd_iban()`](data-masking-component-functions.md) | Generate random International Bank Account Number |  |
| [`gen_rnd_pan()`](data-masking-component-functions.md) | Generate random payment card Primary Account Number |  |
| [`gen_rnd_pan()`](data-masking-plugin-functions.md) | Generate random payment card Primary Account Number |  |
| [`gen_rnd_ssn()`](data-masking-component-functions.md) | Generate random US Social Security Number |  |
| [`gen_rnd_ssn()`](data-masking-plugin-functions.md) | Generate random US Social Security Number |  |
| [`gen_rnd_uk_nin()`](data-masking-component-functions.md) | Generate random United Kingdom National Insurance Number |  |
| [`gen_rnd_us_phone()`](data-masking-component-functions.md) | Generate random US phone number |  |
| [`gen_rnd_us_phone()`](data-masking-plugin-functions.md) | Generate random US phone number |  |
| [`gen_rnd_uuid()`](data-masking-component-functions.md) | Generate random Universally Unique Identifier |  |
| [`group_replication_disable_member_action()`](group-replication-functions-for-member-actions.md) | Enable a member action so that the member does not take it in the specified situation |  |
| [`group_replication_enable_member_action()`](group-replication-functions-for-member-actions.md) | Enable a member action for the member to take in the specified situation |  |
| [`group_replication_get_communication_protocol()`](group-replication-functions-for-communication-protocol.md) | Return Group Replication protocol version |  |
| [`group_replication_get_write_concurrency()`](group-replication-functions-for-maximum-consensus.md) | Return maximum number of consensus instances executable in parallel |  |
| [`group_replication_reset_member_actions()`](group-replication-functions-for-member-actions.md) | Reset the member actions configuration to the default settings |  |
| [`group_replication_set_as_primary()`](group-replication-functions-for-new-primary.md) | Assign group member as new primary |  |
| [`group_replication_set_communication_protocol()`](group-replication-functions-for-communication-protocol.md) | Set Group Replication protocol version |  |
| [`group_replication_set_write_concurrency()`](group-replication-functions-for-maximum-consensus.md) | Set maximum number of consensus instances executable in parallel |  |
| [`group_replication_switch_to_multi_primary_mode()`](group-replication-functions-for-mode.md) | Change group from single-primary to multi-primary mode |  |
| [`group_replication_switch_to_single_primary_mode()`](group-replication-functions-for-mode.md) | Change group from multi-primary to single-primary mode |  |
| [`keyring_aws_rotate_cmk()`](keyring-functions-plugin-specific.md) | Rotate AWS customer master key |  |
| [`keyring_aws_rotate_keys()`](keyring-functions-plugin-specific.md) | Rotate keys in keyring\_aws storage file |  |
| [`keyring_hashicorp_update_config()`](keyring-functions-plugin-specific.md) | Cause runtime keyring\_hashicorp reconfiguration |  |
| [`keyring_key_fetch()`](keyring-functions-general-purpose.md) | Fetch keyring key value |  |
| [`keyring_key_generate()`](keyring-functions-general-purpose.md) | Generate random keyring key |  |
| [`keyring_key_length_fetch()`](keyring-functions-general-purpose.md) | Return keyring key length |  |
| [`keyring_key_remove()`](keyring-functions-general-purpose.md) | Remove keyring key |  |
| [`keyring_key_store()`](keyring-functions-general-purpose.md) | Store key in keyring |  |
| [`keyring_key_type_fetch()`](keyring-functions-general-purpose.md) | Return keyring key type |  |
| [`load_rewrite_rules()`](rewriter-query-rewrite-plugin-reference.md) | Rewriter plugin helper routine |  |
| [`mask_canada_sin()`](data-masking-component-functions.md) | Mask Canada Social Insurance Number |  |
| [`mask_iban()`](data-masking-component-functions.md) | Mask International Bank Account Number |  |
| [`mask_inner()`](data-masking-component-functions.md) | Mask interior part of string |  |
| [`mask_inner()`](data-masking-plugin-functions.md) | Mask interior part of string |  |
| [`mask_outer()`](data-masking-component-functions.md) | Mask left and right parts of string |  |
| [`mask_outer()`](data-masking-plugin-functions.md) | Mask left and right parts of string |  |
| [`mask_pan()`](data-masking-component-functions.md) | Mask payment card Primary Account Number part of string |  |
| [`mask_pan()`](data-masking-plugin-functions.md) | Mask payment card Primary Account Number part of string |  |
| [`mask_pan_relaxed()`](data-masking-component-functions.md) | Mask payment card Primary Account Number part of string |  |
| [`mask_pan_relaxed()`](data-masking-plugin-functions.md) | Mask payment card Primary Account Number part of string |  |
| [`mask_ssn()`](data-masking-component-functions.md) | Mask US Social Security Number |  |
| [`mask_ssn()`](data-masking-plugin-functions.md) | Mask US Social Security Number |  |
| [`mask_uk_nin()`](data-masking-component-functions.md) | Mask United Kingdom National Insurance Number |  |
| [`mask_uuid()`](data-masking-component-functions.md) | Mask Universally Unique Identifier part of string |  |
| [`masking_dictionaries_flush()`](data-masking-component-functions.md) | Cause masking\_dictionaries cache to be reloaded from table |  |
| [`masking_dictionary_remove()`](data-masking-component-functions.md) | Remove dictionary from the database table |  |
| [`masking_dictionary_term_add()`](data-masking-component-functions.md) | Add new term to the dictionary |  |
| [`masking_dictionary_term_remove()`](data-masking-component-functions.md) | Remove existing term from the dictionary |  |
| [`mysql_firewall_flush_status()`](firewall-reference.md) | Reset firewall status variables |  |
| [`mysql_query_attribute_string()`](query-attributes.md) | Fetch query attribute value |  |
| [`normalize_statement()`](firewall-reference.md) | Normalize SQL statement to digest form |  |
| [`read_firewall_group_allowlist()`](firewall-reference.md) | Update firewall group profile recorded-statement cache |  |
| [`read_firewall_groups()`](firewall-reference.md) | Update firewall group profile cache |  |
| [`read_firewall_users()`](firewall-reference.md) | Update firewall account profile cache | Yes |
| [`read_firewall_whitelist()`](firewall-reference.md) | Update firewall account profile recorded-statement cache | Yes |
| [`service_get_read_locks()`](locking-service.md) | Acquire locking service shared locks |  |
| [`service_get_write_locks()`](locking-service.md) | Acquire locking service exclusive locks |  |
| [`service_release_locks()`](locking-service.md) | Release locking service locks |  |
| [`set_firewall_group_mode()`](firewall-reference.md) | Establish firewall group profile operational mode |  |
| [`set_firewall_mode()`](firewall-reference.md) | Establish firewall account profile operational mode | Yes |
| [`version_tokens_delete()`](version-tokens-reference.md) | Delete tokens from version tokens list |  |
| [`version_tokens_edit()`](version-tokens-reference.md) | Modify version tokens list |  |
| [`version_tokens_lock_exclusive()`](version-tokens-reference.md) | Acquire exclusive locks on version tokens |  |
| [`version_tokens_lock_shared()`](version-tokens-reference.md) | Acquire shared locks on version tokens |  |
| [`version_tokens_set()`](version-tokens-reference.md) | Set version tokens list |  |
| [`version_tokens_show()`](version-tokens-reference.md) | Return version tokens list |  |
| [`version_tokens_unlock()`](version-tokens-reference.md) | Release version tokens locks |  |