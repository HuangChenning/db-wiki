---
title: "7.6.8 The Keyring Proxy Bridge Plugin"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/daemon-keyring-proxy-plugin.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 7.6.8 The Keyring Proxy Bridge Plugin

MySQL Keyring originally implemented keystore capabilities using server plugins, but began transitioning to use the component infrastructure in MySQL 8.0. The transition includes revising the underlying implementation of keyring plugins to use the component infrastructure. This is facilitated using the plugin named `daemon_keyring_proxy_plugin` that acts as a bridge between the plugin and component service APIs, and enables keyring plugins to continue to be used with no change to user-visible characteristics.

`daemon_keyring_proxy_plugin` is built in and nothing need be done to install or enable it.