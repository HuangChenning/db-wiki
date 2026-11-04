---
title: "MySQL :: MySQL 26.10 Reference Manual :: 8.3.6 Post-Quantum Cryptography"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/post-quantum-crytpography-ssl.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 8.3.6 Post-Quantum Cryptography

This section describes how to configure MySQL to use post-quantum cryptography (PQC) algorithms for TLS connections if MySQL is built using OpenSSL 3.5.0 or later.

MySQL supports PQC-capable TLS 1.3 key exchange groups and TLS handshake signature algorithms. PQC key exchange is preferred by default when available, but classical key exchange groups remain available as fallbacks unless PQC key exchange is explicitly required. Advertising PQC-capable TLS handshake signature algorithms is disabled by default and must be enabled explicitly.

PQC is supported for the following encrypted connection types:

- Client/server connections on the main connection channel.
- Client/server connections on the administrative connection channel.
- Asynchronous replication TLS connections.
- Group Replication recovery TLS connections.
- Group Replication inter-group channels using the MySQL communication stack. XCom is not supported.
- X Plugin TLS connections.

#### PQC Requirements

PQC key exchange groups and PQC-capable TLS handshake signature algorithms are available only when MySQL is built with OpenSSL 3.5.0 or later. PQC support applies only to TLS 1.3 connections.

PQC-related system variables are present even if MySQL is linked with an older OpenSSL version. For such installations:

- Boolean PQC system variables are disabled and cannot be enabled.
- ``*`*`*_tls_kex`` variables can be edited, but accept only classical key exchange group names.
- Session status variables that report the negotiated key exchange group or signature algorithm return an empty string.

#### Supported Key Exchange Groups

The following key exchange group names are valid in \`\*\_tls\_kex\` values. Names are case-sensitive and must be specified exactly as shown. MySQL does not accept OpenSSL aliases, NIST names, or OID names for these values.

**Table 8.14 Supported Key Exchange Groups**

| Group Name | Type | Description |
| --- | --- | --- |
| `X25519MLKEM768` | PQC hybrid | (OpenSSL 3.5.0, or higher) X25519 with ML-KEM-768 |
| `secp384r1MLKEM1024` | PQC hybrid | (OpenSSL 3.5.0, or higher) P-384 with ML-KEM-1024 |
| `secp256r1MLKEM768` | PQC hybrid | (OpenSSL 3.5.0, or higher) P-256 with ML-KEM-768 |
| `MLKEM512` | PQC pure | (OpenSSL 3.5.0, or higher) ML-KEM-512 |
| `MLKEM768` | PQC pure | (OpenSSL 3.5.0, or higher) ML-KEM-768 |
| `X25519` | Classical | X25519 ECDH group, if available |
| `secp384r1` | Classical | P-384 ECDHE group |
| `secp256r1` | Classical | P-256 ECDHE group |
| `secp521r1` | Classical | P-521 ECDHE group |

You can restrict a channel to a specific list of key exchange groups by setting the corresponding variable to a colon-separated list of groups. For example:

```sql
SET GLOBAL tls_kex = 'X25519MLKEM768:secp384r1MLKEM1024:secp256r1';
```

Each group name must be valid. If any name is invalid, the entire value is rejected. An empty string selects the default list. If the corresponding ``*`*`*_force_pqc`` variable is enabled, the ``*`*`*_tls_kex`` value can only contain PQC group names. An empty string remains valid and selects the default PQC-capable behavior.

#### Supported TLS Handshake Signature Algorithms

If PQC-capable TLS handshake signature algorithms are enabled, MySQL advertises the following PQC signature algorithms, in order of preference:

- ML-DSA-44
- ML-DSA-65
- ML-DSA-87

Enabling a ``*`*`*_use_pqc_sign`` system variable allows MySQL to advertise PQC-capable TLS handshake signature algorithms. It does not require the negotiated TLS connection to use a PQC signature algorithm.

#### Connection Configuration

The following settings control PQC for each connection type:

#### PQC System Variables

- `force_pqc`
	Whether the server requires a PQC-compatible key-exchange group for new TLS connections on the main connection interface. When force\_pqc is ON, the server accepts only TLS 1.3 connections that negotiate a supported PQC key-exchange group. A connection fails if such a group cannot be negotiated.
	The default is OFF, which permits classical fallback for compatibility. When set to OFF, and the server uses OpenSSL 3.5 or later, the server writes a warning at startup or when TLS is reloaded that PQC key exchange is not required. The warning is not emitted for every connection.
	Setting this variable to ON is rejected if the corresponding TLS version configuration permits TLS 1.2 only. Enabling it also drops the TLS session cache because a resumed session does not perform a handshake from which the key-exchange group can be determined.
- `admin_force_pqc`
	Whether the server requires a PQC-compatible key-exchange group for new TLS connections on the administrative connection interface. Its behavior, compatibility considerations, and TLS 1.2 restriction are the same as for force\_pqc, but apply only to the administrative interface.
- `replication_force_pqc`
	Whether asynchronous replication TLS connections require a PQC-compatible key-exchange group. When enabled, the replication connection fails if a supported PQC group cannot be negotiated.
	The default is OFF, which permits classical fallback for replication sources and replicas that do not support PQC. This variable applies to new asynchronous replication TLS sessions only. With OpenSSL versions earlier than 3.5, it is read only and has the fixed value OFF.
- `group_replication_force_pqc`
	Whether Group Replication recovery TLS connections require a PQC-compatible key-exchange group. This applies to MySQL Group Replication channels, including inter-group channels that use the MySQL communication stack. The XCom stack is not supported.
	When `group_replication_force_pqc=ON`, the connection fails if a supported PQC key-exchange group cannot be negotiated. The default is OFF, which permits classical fallback. This variable applies to new Group Replication TLS sessions only. With OpenSSL versions earlier than 3.5, it is read only and OFF.
- `mysqlx_force_pqc`
	Whether X Plugin requires a PQC-compatible key-exchange group for new TLS connections. When enabled, X Plugin accepts only TLS 1.3 connections that negotiate a supported PQC key-exchange group.
	This variable is not dynamic because X Plugin constructs its TLS state at startup. If all X Plugin PQC variables have their default values, X Plugin can instead inherit the corresponding main-server PQC configuration. Use `Mysqlx_force_pqc` to determine the effective X Plugin setting.
	The default is OFF, which permits classical fallback. This variable applies to new X Plugin TLS sessions only. With OpenSSL versions earlier than 3.5, it is read only and OFF.
- `tls_kex`
	The permitted TLS key-exchange groups for the main connection interface. The value is either an empty string or a colon-separated list of supported group names. An empty string selects the server's default list, which includes PQC-capable groups and classical fallback groups.
	For example:
	```sql
	SET GLOBAL tls_kex = 'X25519MLKEM768:secp384r1MLKEM1024:secp256r1';
	```
	The permitted group names are:
	- PQC-capable: X25519MLKEM768, secp384r1MLKEM1024, secp256r1MLKEM768, MLKEM512, and MLKEM768.
	- Classical fallback: X25519 (when available), secp384r1, secp256r1, and secp521r1.
	Every list element must be valid; otherwise the entire assignment is rejected. If `force_pqc=ON`, the nonempty value may contain only the supported PQC group names. An empty string remains permitted. Group names are case-sensitive. MySQL accepts only the names shown in the preceding list; it does not accept OpenSSL aliases, NIST names, or OID names. With OpenSSL versions earlier than 3.5, this variable accepts only the classical fallback groups. The setting applies to new main-interface TLS sessions only.
- `admin_tls_kex`
	The allowed TLS key-exchange groups for the administrative connection interface are:
	- PQC-capable: X25519MLKEM768, secp384r1MLKEM1024, secp256r1MLKEM768, MLKEM512, and MLKEM768.
	- Classical fallback: X25519 (when available), secp384r1, secp256r1, and secp521r1.
	The value is either an empty string or a colon-separated list of group names. An empty string selects the administrative interface's default group list, which includes PQC-capable groups and classical fallback groups. Every list element must be valid; otherwise the entire assignment is rejected. If \`admin\_force\_pqc\` is \`ON\`, the nonempty value may contain only PQC-capable group names. An empty string remains permitted. Group names are case-sensitive. MySQL accepts only the names shown in the preceding list; it does not accept OpenSSL aliases, NIST names, or OID names. With OpenSSL versions earlier than 3.5, this variable accepts only the classical fallback groups. The setting applies to new administrative TLS sessions only.
- `replication_tls_kex`
	The allowed TLS key-exchange groups for asynchronous replication TLS connections are:
	- PQC-capable: X25519MLKEM768, secp384r1MLKEM1024, secp256r1MLKEM768, MLKEM512, and MLKEM768.
	- Classical fallback: X25519 (when available), secp384r1, secp256r1, and secp521r1.
	The value is either an empty string or a colon-separated list of group names. An empty string selects the asynchronous replication channel's default group list, which includes PQC-capable groups and classical fallback groups. Every list element must be valid; otherwise the entire assignment is rejected. If `replication_force_pqc=ON`, the nonempty value may contain only PQC-capable group names. An empty string remains permitted. Group names are case-sensitive. MySQL accepts only the names shown in the preceding list; it does not accept OpenSSL aliases, NIST names, or OID names. With OpenSSL versions earlier than 3.5, this variable accepts only the classical fallback groups. The setting applies to new asynchronous replication TLS sessions only.
- `group_replication_tls_kex`
	The allowed TLS key-exchange groups for Group Replication recovery TLS connections are:
	- PQC-capable: X25519MLKEM768, secp384r1MLKEM1024, secp256r1MLKEM768, MLKEM512, and MLKEM768.
	- Classical fallback: X25519 (when available), secp384r1, secp256r1, and secp521r1.
	The value is either an empty string or a colon-separated list of group names. An empty string selects the Group Replication recovery channel's default group list, which includes PQC-capable groups and classical fallback groups. Every list element must be valid; otherwise the entire assignment is rejected. If `group_replication_force_pqc=ON`, the nonempty value may contain only PQC-capable group names. An empty string remains permitted. Group names are case-sensitive. MySQL accepts only the names shown in the preceding list; it does not accept OpenSSL aliases, NIST names, or OID names. With OpenSSL versions earlier than 3.5, this variable accepts only the classical fallback groups. The setting applies to new Group Replication recovery TLS sessions only.
- `mysqlx_tls_kex`
	The allowed TLS key-exchange groups for X Plugin TLS connections are:
	- PQC-capable: X25519MLKEM768, secp384r1MLKEM1024, secp256r1MLKEM768, MLKEM512, and MLKEM768.
	- Classical fallback: X25519 (when available), secp384r1, secp256r1, and secp521r1.
	The value is either an empty string or a colon-separated list of group names. An empty string is the default. Every list element must be valid; otherwise the entire assignment is rejected. If `mysqlx_force_pqc=ON`, a nonempty value may contain only PQC-capable group names. An empty string remains permitted. Group names are case-sensitive. MySQL accepts only the names shown in the preceding list; it does not accept OpenSSL aliases, NIST names, or OID names. With OpenSSL versions earlier than 3.5, this variable accepts only the classical fallback groups.
	This variable is read only because X Plugin constructs its TLS state at startup. If all X Plugin PQC variables have their default values, X Plugin can inherit the matching main-server TLS configuration.
- `use_pqc_sign`
	Whether the main connection interface advertises PQC-capable TLS handshake signature algorithms in addition to the classical signature algorithms. When OFF, only the classical signature algorithms are advertised. When ON, the server advertises the PQC-capable and classical fallback signature-algorithm lists. Enabling this variable permits PQC signatures; it does not ensure that a PQC signature is selected. PQC certificate generation is outside the scope of this feature. This variable applies to new main-interface TLS sessions only. With OpenSSL versions earlier than 3.5, it is read only and OFF.
- `admin_use_pqc_sign`
	Whether the administrative connection interface advertises PQC-capable TLS handshake signature algorithms together with the classical fallback signature algorithms. If `admin_use_pqc_sign=OFF`, only classical TLS handshake signature algorithms are advertised for administrative TLS connections. When it is ON, the PQC-capable signature-algorithm list is also advertised. The default is OFF. Enabling the variable permits, but does not guarantee, selection of a PQC-capable handshake signature algorithm. This variable applies to new administrative TLS sessions only. With OpenSSL versions earlier than 3.5, it is read only and OFF.
- `replication_use_pqc_sign`
	Whether asynchronous replication TLS connections advertise PQC-capable TLS handshake signature algorithms together with the classical fallback signature algorithms. When OFF, only classical signature algorithms are advertised for these connections. If `replication_use_pqc_sign=ON`, the PQC-capable signature-algorithm list is also advertised. The default is OFF. Enabling the variable permits, but does not guarantee, selection of a PQC-capable handshake signature algorithm. This variable applies to new asynchronous replication TLS sessions only. With OpenSSL versions earlier than 3.5, it is read only and OFF.
- `group_replication_use_pqc_sign`
	Whether Group Replication recovery TLS connections advertise PQC-capable TLS handshake signature algorithms together with the classical fallback signature algorithms. When OFF, only classical signature algorithms are advertised for these connections. If group\_replication\_use\_pqc\_sign=ON, the PQC-capable signature-algorithm list is also advertised. The default is OFF. Enabling the variable permits, but does not guarantee, selection of a PQC-capable handshake signature algorithm. This variable applies to new Group Replication recovery TLS sessions only. With OpenSSL versions earlier than 3.5, it is read only and OFF.
- `mysqlx_use_pqc_sign`
	Whether X Plugin TLS connections advertise PQC-capable TLS handshake signature algorithms together with the classical fallback signature algorithms. This variable is read only because X Plugin applies its TLS configuration at startup. `Mysqlx_use_pqc_sign` reports the effective X Plugin value. When `mysqlx_use_pqc_sign=OFF`, only classical TLS handshake signature algorithms are advertised for X Plugin TLS connections. When it is ON, the PQC-capable signature-algorithm list is also advertised. The default is OFF. Enabling the variable permits, but does not guarantee, selection of a PQC-capable handshake signature algorithm. This variable applies to new X Plugin TLS sessions only. It is read only because X Plugin constructs its TLS state at startup. When all X Plugin PQC variables have their default values, X Plugin can inherit the matching main-server TLS configuration. Use `Mysqlx_use_pqc_sign` to view the effective X Plugin setting. With OpenSSL versions earlier than 3.5, this variable is OFF.

#### PQC Status Variables

- `Tls_key_exchange_algorithm`
	The TLS key-exchange group negotiated for the current TLS connection. The value is an empty string when the connection does not use TLS, the TLS session is resumed, or the TLS library does not expose the negotiated group. A usable value requires OpenSSL 3.5 or later.
- `Tls_sign_algorithm`
	The TLS handshake signature algorithm negotiated for the current TLS connection. The value is an empty string when the connection does not use TLS, the TLS session is resumed, or the TLS library does not expose the negotiated signature algorithm. A usable value requires OpenSSL 3.5 or later.
- `Mysqlx_force_pqc`
	The effective `mysqlx_force_pqc` configuration for the X Plugin TLS channel. This status variable resolves whether X Plugin is using its own PQC configuration or has inherited the corresponding main-server configuration.
- `Mysqlx_tls_kex`
	The effective `mysqlx_tls_kex` configuration for the X Plugin TLS channel. This status variable resolves whether X Plugin is using its own key-exchange-group list or has inherited the corresponding main-server configuration.
- `Mysqlx_use_pqc_sign`
	The effective `mysqlx_use_pqc_sign` configuration for the X Plugin TLS channel. This status variable resolves whether X Plugin is using its own handshake-signature configuration or has inherited the corresponding main-server configuration.

#### MySQL Client Options

- ``--tls-kex=*`value`*``: Specifies a colon-separated list of key exchange groups for the client connection.
- `--force-pqc=0|1`: Requires the client TLS connection to negotiate a PQC-capable key exchange group.
- `--use-pqc-sign=0|1`: Allows the client to advertise PQC-capable TLS handshake signature algorithms.