---
title: "5.1.4 Server System Variable Reference"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/server-system-variable-reference.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 5.1.4 Server System Variable Reference

The following table lists all system variables applicable within `mysqld`.

The table lists command-line options (Cmd-line), options valid in configuration files (Option file), server system variables (System Var), and status variables (Status var) in one unified list, with an indication of where each option or variable is valid. If a server option set on the command line or in an option file differs from the name of the corresponding system variable, the variable name is noted immediately below the corresponding option. The scope of the variable (Var Scope) is Global, Session, or both. Please see the corresponding item descriptions for details on setting and using the variables. Where appropriate, direct links to further information about the items are provided.

**Table 5.2 System Variable Summary**

| Name | Cmd-Line | Option File | System Var | Var Scope | Dynamic |
| --- | --- | --- | --- | --- | --- |
| [audit\_log\_buffer\_size](audit-log-reference.md) | Yes | Yes | Yes | Global | No |
| [audit\_log\_compression](audit-log-reference.md) | Yes | Yes | Yes | Global | No |
| [audit\_log\_connection\_policy](audit-log-reference.md) | Yes | Yes | Yes | Global | Yes |
| [audit\_log\_current\_session](audit-log-reference.md) |  |  | Yes | Both | No |
| [audit\_log\_disable](audit-log-reference.md) | Yes | Yes | Yes | Global | Yes |
| [audit\_log\_encryption](audit-log-reference.md) | Yes | Yes | Yes | Global | No |
| [audit\_log\_exclude\_accounts](audit-log-reference.md) | Yes | Yes | Yes | Global | Yes |
| [audit\_log\_file](audit-log-reference.md) | Yes | Yes | Yes | Global | No |
| [audit\_log\_filter\_id](audit-log-reference.md) |  |  | Yes | Both | No |
| [audit\_log\_flush](audit-log-reference.md) |  |  | Yes | Global | Yes |
| [audit\_log\_format](audit-log-reference.md) | Yes | Yes | Yes | Global | No |
| [audit\_log\_format\_unix\_timestamp](audit-log-reference.md) | Yes | Yes | Yes | Global | Yes |
| [audit\_log\_include\_accounts](audit-log-reference.md) | Yes | Yes | Yes | Global | Yes |
| [audit\_log\_policy](audit-log-reference.md) | Yes | Yes | Yes | Global | No |
| [audit\_log\_read\_buffer\_size](audit-log-reference.md) | Yes | Yes | Yes | Varies | Varies |
| [audit\_log\_rotate\_on\_size](audit-log-reference.md) | Yes | Yes | Yes | Global | Yes |
| [audit\_log\_statement\_policy](audit-log-reference.md) | Yes | Yes | Yes | Global | Yes |
| [audit\_log\_strategy](audit-log-reference.md) | Yes | Yes | Yes | Global | No |
| [authentication\_ldap\_sasl\_auth\_method\_name](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_ldap\_sasl\_bind\_base\_dn](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_ldap\_sasl\_bind\_root\_dn](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_ldap\_sasl\_bind\_root\_pwd](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_ldap\_sasl\_ca\_path](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_ldap\_sasl\_group\_search\_attr](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_ldap\_sasl\_group\_search\_filter](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_ldap\_sasl\_init\_pool\_size](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_ldap\_sasl\_log\_status](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_ldap\_sasl\_max\_pool\_size](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_ldap\_sasl\_server\_host](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_ldap\_sasl\_server\_port](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_ldap\_sasl\_tls](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_ldap\_sasl\_user\_search\_attr](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_ldap\_simple\_auth\_method\_name](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_ldap\_simple\_bind\_base\_dn](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_ldap\_simple\_bind\_root\_dn](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_ldap\_simple\_bind\_root\_pwd](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_ldap\_simple\_ca\_path](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_ldap\_simple\_group\_search\_attr](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_ldap\_simple\_group\_search\_filter](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_ldap\_simple\_init\_pool\_size](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_ldap\_simple\_log\_status](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_ldap\_simple\_max\_pool\_size](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_ldap\_simple\_server\_host](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_ldap\_simple\_server\_port](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_ldap\_simple\_tls](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_ldap\_simple\_user\_search\_attr](pluggable-authentication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [authentication\_windows\_log\_level](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [authentication\_windows\_use\_principal\_name](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [auto\_generate\_certs](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [auto\_increment\_increment](replication-options-source.md) | Yes | Yes | Yes | Both | Yes |
| [auto\_increment\_offset](replication-options-source.md) | Yes | Yes | Yes | Both | Yes |
| [autocommit](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [automatic\_sp\_privileges](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [avoid\_temporal\_upgrade](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [back\_log](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [basedir](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [big\_tables](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [bind\_address](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [binlog\_cache\_size](replication-options-binary-log.md) | Yes | Yes | Yes | Global | Yes |
| [binlog\_checksum](replication-options-binary-log.md) | Yes | Yes | Yes | Global | Yes |
| [binlog\_direct\_non\_transactional\_updates](replication-options-binary-log.md) | Yes | Yes | Yes | Both | Yes |
| [binlog\_error\_action](replication-options-binary-log.md) | Yes | Yes | Yes | Global | Yes |
| [binlog\_format](replication-options-binary-log.md) | Yes | Yes | Yes | Both | Yes |
| [binlog\_group\_commit\_sync\_delay](replication-options-binary-log.md) | Yes | Yes | Yes | Global | Yes |
| [binlog\_group\_commit\_sync\_no\_delay\_count](replication-options-binary-log.md) | Yes | Yes | Yes | Global | Yes |
| [binlog\_gtid\_simple\_recovery](replication-options-gtids.md) | Yes | Yes | Yes | Global | No |
| [binlog\_max\_flush\_queue\_time](replication-options-binary-log.md) | Yes | Yes | Yes | Global | Yes |
| [binlog\_order\_commits](replication-options-binary-log.md) | Yes | Yes | Yes | Global | Yes |
| [binlog\_row\_image](replication-options-binary-log.md) | Yes | Yes | Yes | Both | Yes |
| [binlog\_rows\_query\_log\_events](replication-options-binary-log.md) | Yes | Yes | Yes | Both | Yes |
| [binlog\_stmt\_cache\_size](replication-options-binary-log.md) | Yes | Yes | Yes | Global | Yes |
| [binlog\_transaction\_dependency\_history\_size](replication-options-binary-log.md) | Yes | Yes | Yes | Global | Yes |
| [binlog\_transaction\_dependency\_tracking](replication-options-binary-log.md) | Yes | Yes | Yes | Global | Yes |
| [block\_encryption\_mode](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [bulk\_insert\_buffer\_size](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [character\_set\_client](server-system-variables.md) |  |  | Yes | Both | Yes |
| [character\_set\_connection](server-system-variables.md) |  |  | Yes | Both | Yes |
| [character\_set\_database](server-system-variables.md) (note 1) |  |  | Yes | Both | Yes |
| [character\_set\_filesystem](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [character\_set\_results](server-system-variables.md) |  |  | Yes | Both | Yes |
| [character\_set\_server](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [character\_set\_system](server-system-variables.md) |  |  | Yes | Global | No |
| [character\_sets\_dir](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [check\_proxy\_users](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [collation\_connection](server-system-variables.md) |  |  | Yes | Both | Yes |
| [collation\_database](server-system-variables.md) (note 1) |  |  | Yes | Both | Yes |
| [collation\_server](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [completion\_type](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [concurrent\_insert](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [connect\_timeout](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [connection\_control\_failed\_connections\_threshold](connection-control-plugin-variables.md) | Yes | Yes | Yes | Global | Yes |
| [connection\_control\_max\_connection\_delay](connection-control-plugin-variables.md) | Yes | Yes | Yes | Global | Yes |
| [connection\_control\_min\_connection\_delay](connection-control-plugin-variables.md) | Yes | Yes | Yes | Global | Yes |
| [core\_file](server-system-variables.md) |  |  | Yes | Global | No |
| [daemon\_memcached\_enable\_binlog](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [daemon\_memcached\_engine\_lib\_name](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [daemon\_memcached\_engine\_lib\_path](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [daemon\_memcached\_option](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [daemon\_memcached\_r\_batch\_size](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [daemon\_memcached\_w\_batch\_size](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [datadir](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [date\_format](server-system-variables.md) |  |  | Yes | Global | No |
| [datetime\_format](server-system-variables.md) |  |  | Yes | Global | No |
| [debug](server-options.md) | Yes | Yes | Yes | Both | Yes |
| [debug\_sync](server-system-variables.md) |  |  | Yes | Session | Yes |
| [default\_authentication\_plugin](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [default\_password\_lifetime](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [default\_storage\_engine](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [default\_tmp\_storage\_engine](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [default\_week\_format](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [delay\_key\_write](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [delayed\_insert\_limit](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [delayed\_insert\_timeout](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [delayed\_queue\_size](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [disabled\_storage\_engines](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [disconnect\_on\_expired\_password](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [div\_precision\_increment](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [end\_markers\_in\_json](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [enforce\_gtid\_consistency](replication-options-gtids.md) | Yes | Yes | Yes | Global | Varies |
| [eq\_range\_index\_dive\_limit](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [error\_count](server-system-variables.md) |  |  | Yes | Session | No |
| [event\_scheduler](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [expire\_logs\_days](replication-options-binary-log.md) | Yes | Yes | Yes | Global | Yes |
| [explicit\_defaults\_for\_timestamp](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [external\_user](server-system-variables.md) |  |  | Yes | Session | No |
| [flush](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [flush\_time](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [foreign\_key\_checks](server-system-variables.md) |  |  | Yes | Both | Yes |
| [ft\_boolean\_syntax](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [ft\_max\_word\_len](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [ft\_min\_word\_len](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [ft\_query\_expansion\_limit](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [ft\_stopword\_file](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [general\_log](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [general\_log\_file](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_concat\_max\_len](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [group\_replication\_allow\_local\_disjoint\_gtids\_join](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_allow\_local\_lower\_version\_join](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_auto\_increment\_increment](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_bootstrap\_group](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_components\_stop\_timeout](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_compression\_threshold](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_enforce\_update\_everywhere\_checks](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_exit\_state\_action](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_flow\_control\_applier\_threshold](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_flow\_control\_certifier\_threshold](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_flow\_control\_mode](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_force\_members](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_group\_name](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_group\_seeds](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_gtid\_assignment\_block\_size](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_ip\_whitelist](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_local\_address](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_member\_weight](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_poll\_spin\_loops](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_recovery\_complete\_at](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_recovery\_reconnect\_interval](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_recovery\_retry\_count](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_recovery\_ssl\_ca](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_recovery\_ssl\_capath](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_recovery\_ssl\_cert](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_recovery\_ssl\_cipher](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_recovery\_ssl\_crl](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_recovery\_ssl\_crlpath](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_recovery\_ssl\_key](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_recovery\_ssl\_verify\_server\_cert](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_recovery\_use\_ssl](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_single\_primary\_mode](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_ssl\_mode](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_start\_on\_boot](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_transaction\_size\_limit](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [group\_replication\_unreachable\_majority\_timeout](group-replication-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [gtid\_executed](replication-options-gtids.md) |  |  | Yes | Varies | No |
| [gtid\_executed\_compression\_period](replication-options-gtids.md) | Yes | Yes | Yes | Global | Yes |
| [gtid\_mode](replication-options-gtids.md) | Yes | Yes | Yes | Global | Varies |
| [gtid\_next](replication-options-gtids.md) |  |  | Yes | Session | Yes |
| [gtid\_owned](replication-options-gtids.md) |  |  | Yes | Both | No |
| [gtid\_purged](replication-options-gtids.md) |  |  | Yes | Global | Yes |
| [have\_compress](server-system-variables.md) |  |  | Yes | Global | No |
| [have\_crypt](server-system-variables.md) |  |  | Yes | Global | No |
| [have\_dynamic\_loading](server-system-variables.md) |  |  | Yes | Global | No |
| [have\_geometry](server-system-variables.md) |  |  | Yes | Global | No |
| [have\_openssl](server-system-variables.md) |  |  | Yes | Global | No |
| [have\_profiling](server-system-variables.md) |  |  | Yes | Global | No |
| [have\_query\_cache](server-system-variables.md) |  |  | Yes | Global | No |
| [have\_rtree\_keys](server-system-variables.md) |  |  | Yes | Global | No |
| [have\_ssl](server-system-variables.md) |  |  | Yes | Global | No |
| [have\_statement\_timeout](server-system-variables.md) |  |  | Yes | Global | No |
| [have\_symlink](server-system-variables.md) |  |  | Yes | Global | No |
| [host\_cache\_size](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [hostname](server-system-variables.md) |  |  | Yes | Global | No |
| [identity](server-system-variables.md) |  |  | Yes | Session | Yes |
| [ignore\_builtin\_innodb](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [ignore\_db\_dirs](server-system-variables.md) |  |  | Yes | Global | No |
| [init\_connect](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [init\_file](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [init\_slave](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_adaptive\_flushing](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_adaptive\_flushing\_lwm](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_adaptive\_hash\_index](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_adaptive\_hash\_index\_parts](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_adaptive\_max\_sleep\_delay](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_api\_bk\_commit\_interval](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_api\_disable\_rowlock](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_api\_enable\_binlog](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_api\_enable\_mdl](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_api\_trx\_level](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_autoextend\_increment](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_autoinc\_lock\_mode](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_background\_drop\_list\_empty](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_buffer\_pool\_chunk\_size](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_buffer\_pool\_dump\_at\_shutdown](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_buffer\_pool\_dump\_now](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_buffer\_pool\_dump\_pct](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_buffer\_pool\_filename](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_buffer\_pool\_instances](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_buffer\_pool\_load\_abort](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_buffer\_pool\_load\_at\_startup](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_buffer\_pool\_load\_now](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_buffer\_pool\_size](innodb-parameters.md) | Yes | Yes | Yes | Global | Varies |
| [innodb\_change\_buffer\_max\_size](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_change\_buffering](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_change\_buffering\_debug](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_checksum\_algorithm](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_checksums](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_cmp\_per\_index\_enabled](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_commit\_concurrency](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_compress\_debug](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_compression\_failure\_threshold\_pct](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_compression\_level](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_compression\_pad\_pct\_max](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_concurrency\_tickets](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_data\_file\_path](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_data\_home\_dir](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_deadlock\_detect](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_default\_row\_format](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_disable\_resize\_buffer\_pool\_debug](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_disable\_sort\_file\_cache](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_doublewrite](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_fast\_shutdown](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_fil\_make\_page\_dirty\_debug](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_file\_format](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_file\_format\_check](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_file\_format\_max](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_file\_per\_table](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_fill\_factor](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_flush\_log\_at\_timeout](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_flush\_log\_at\_trx\_commit](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_flush\_method](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_flush\_neighbors](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_flush\_sync](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_flushing\_avg\_loops](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_force\_load\_corrupted](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_force\_recovery](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_ft\_aux\_table](innodb-parameters.md) |  |  | Yes | Global | Yes |
| [innodb\_ft\_cache\_size](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_ft\_enable\_diag\_print](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_ft\_enable\_stopword](innodb-parameters.md) | Yes | Yes | Yes | Both | Yes |
| [innodb\_ft\_max\_token\_size](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_ft\_min\_token\_size](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_ft\_num\_word\_optimize](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_ft\_result\_cache\_limit](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_ft\_server\_stopword\_table](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_ft\_sort\_pll\_degree](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_ft\_total\_cache\_size](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_ft\_user\_stopword\_table](innodb-parameters.md) | Yes | Yes | Yes | Both | Yes |
| [innodb\_io\_capacity](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_io\_capacity\_max](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_large\_prefix](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_limit\_optimistic\_insert\_debug](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_lock\_wait\_timeout](innodb-parameters.md) | Yes | Yes | Yes | Both | Yes |
| [innodb\_locks\_unsafe\_for\_binlog](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_log\_buffer\_size](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_log\_checkpoint\_now](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_log\_checksums](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_log\_compressed\_pages](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_log\_file\_size](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_log\_files\_in\_group](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_log\_group\_home\_dir](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_log\_write\_ahead\_size](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_lru\_scan\_depth](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_max\_dirty\_pages\_pct](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_max\_dirty\_pages\_pct\_lwm](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_max\_purge\_lag](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_max\_purge\_lag\_delay](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_max\_undo\_log\_size](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_merge\_threshold\_set\_all\_debug](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_monitor\_disable](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_monitor\_enable](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_monitor\_reset](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_monitor\_reset\_all](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_numa\_interleave](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_old\_blocks\_pct](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_old\_blocks\_time](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_online\_alter\_log\_max\_size](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_open\_files](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_optimize\_fulltext\_only](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_page\_cleaners](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_page\_size](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_print\_all\_deadlocks](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_purge\_batch\_size](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_purge\_rseg\_truncate\_frequency](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_purge\_threads](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_random\_read\_ahead](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_read\_ahead\_threshold](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_read\_io\_threads](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_read\_only](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_replication\_delay](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_rollback\_on\_timeout](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_rollback\_segments](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_saved\_page\_number\_debug](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_sort\_buffer\_size](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_spin\_wait\_delay](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_stats\_auto\_recalc](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_stats\_include\_delete\_marked](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_stats\_method](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_stats\_on\_metadata](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_stats\_persistent](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_stats\_persistent\_sample\_pages](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_stats\_sample\_pages](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_stats\_transient\_sample\_pages](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_status\_output](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_status\_output\_locks](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_strict\_mode](innodb-parameters.md) | Yes | Yes | Yes | Both | Yes |
| [innodb\_support\_xa](innodb-parameters.md) | Yes | Yes | Yes | Both | Yes |
| [innodb\_sync\_array\_size](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_sync\_debug](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_sync\_spin\_loops](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_table\_locks](innodb-parameters.md) | Yes | Yes | Yes | Both | Yes |
| [innodb\_temp\_data\_file\_path](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_thread\_concurrency](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_thread\_sleep\_delay](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_tmpdir](innodb-parameters.md) | Yes | Yes | Yes | Both | Yes |
| [innodb\_trx\_purge\_view\_update\_only\_debug](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_trx\_rseg\_n\_slots\_debug](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_undo\_directory](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_undo\_log\_truncate](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_undo\_logs](innodb-parameters.md) | Yes | Yes | Yes | Global | Yes |
| [innodb\_undo\_tablespaces](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_use\_native\_aio](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [innodb\_version](innodb-parameters.md) |  |  | Yes | Global | No |
| [innodb\_write\_io\_threads](innodb-parameters.md) | Yes | Yes | Yes | Global | No |
| [insert\_id](server-system-variables.md) |  |  | Yes | Session | Yes |
| [interactive\_timeout](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [internal\_tmp\_disk\_storage\_engine](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [join\_buffer\_size](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [keep\_files\_on\_create](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [key\_buffer\_size](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [key\_cache\_age\_threshold](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [key\_cache\_block\_size](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [key\_cache\_division\_limit](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [keyring\_aws\_cmk\_id](keyring-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [keyring\_aws\_conf\_file](keyring-system-variables.md) | Yes | Yes | Yes | Global | No |
| [keyring\_aws\_data\_file](keyring-system-variables.md) | Yes | Yes | Yes | Global | No |
| [keyring\_aws\_region](keyring-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [keyring\_encrypted\_file\_data](keyring-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [keyring\_encrypted\_file\_password](keyring-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [keyring\_file\_data](keyring-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [keyring\_okv\_conf\_dir](keyring-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [keyring\_operations](keyring-system-variables.md) |  |  | Yes | Global | Yes |
| [language](server-options.md) | Yes | Yes | Yes | Global | No |
| [large\_files\_support](server-system-variables.md) |  |  | Yes | Global | No |
| [large\_page\_size](server-system-variables.md) |  |  | Yes | Global | No |
| [large\_pages](server-options.md) | Yes | Yes | Yes | Global | No |
| [last\_insert\_id](server-system-variables.md) |  |  | Yes | Session | Yes |
| [lc\_messages](server-options.md) | Yes | Yes | Yes | Both | Yes |
| [lc\_messages\_dir](server-options.md) | Yes | Yes | Yes | Global | No |
| [lc\_time\_names](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [license](server-system-variables.md) |  |  | Yes | Global | No |
| [local\_infile](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [lock\_wait\_timeout](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [locked\_in\_memory](server-system-variables.md) |  |  | Yes | Global | No |
| [log\_bin](replication-options-binary-log.md) |  |  | Yes | Global | No |
| [log\_bin\_basename](replication-options-binary-log.md) |  |  | Yes | Global | No |
| [log\_bin\_index](replication-options-binary-log.md) | Yes | Yes | Yes | Global | No |
| [log\_bin\_trust\_function\_creators](replication-options-binary-log.md) | Yes | Yes | Yes | Global | Yes |
| [log\_bin\_use\_v1\_row\_events](replication-options-binary-log.md) | Yes | Yes | Yes | Global | Yes |
| [log\_builtin\_as\_identified\_by\_password](replication-options-binary-log.md) | Yes | Yes | Yes | Global | Yes |
| [log\_error](server-options.md) | Yes | Yes | Yes | Global | No |
| [log\_error\_verbosity](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [log\_output](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [log\_queries\_not\_using\_indexes](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [log\_slave\_updates](replication-options-binary-log.md) | Yes | Yes | Yes | Global | No |
| [log\_slow\_admin\_statements](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [log\_slow\_slave\_statements](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [log\_statements\_unsafe\_for\_binlog](replication-options-binary-log.md) | Yes | Yes | Yes | Global | Yes |
| [log\_syslog](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [log\_syslog\_facility](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [log\_syslog\_include\_pid](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [log\_syslog\_tag](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [log\_throttle\_queries\_not\_using\_indexes](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [log\_timestamps](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [log\_warnings](server-options.md) | Yes | Yes | Yes | Global | Yes |
| [long\_query\_time](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [low\_priority\_updates](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [lower\_case\_file\_system](server-system-variables.md) |  |  | Yes | Global | No |
| [lower\_case\_table\_names](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [master\_info\_repository](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [master\_verify\_checksum](replication-options-binary-log.md) | Yes | Yes | Yes | Global | Yes |
| [max\_allowed\_packet](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [max\_binlog\_cache\_size](replication-options-binary-log.md) | Yes | Yes | Yes | Global | Yes |
| [max\_binlog\_size](replication-options-binary-log.md) | Yes | Yes | Yes | Global | Yes |
| [max\_binlog\_stmt\_cache\_size](replication-options-binary-log.md) | Yes | Yes | Yes | Global | Yes |
| [max\_connect\_errors](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [max\_connections](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [max\_delayed\_threads](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [max\_digest\_length](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [max\_error\_count](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [max\_execution\_time](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [max\_heap\_table\_size](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [max\_insert\_delayed\_threads](server-system-variables.md) |  |  | Yes | Both | Yes |
| [max\_join\_size](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [max\_length\_for\_sort\_data](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [max\_points\_in\_geometry](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [max\_prepared\_stmt\_count](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [max\_relay\_log\_size](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [max\_seeks\_for\_key](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [max\_sort\_length](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [max\_sp\_recursion\_depth](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [max\_tmp\_tables](server-system-variables.md) |  |  | Yes | Both | Yes |
| [max\_user\_connections](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [max\_write\_lock\_count](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [mecab\_rc\_file](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [metadata\_locks\_cache\_size](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [metadata\_locks\_hash\_instances](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [min\_examined\_row\_limit](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [multi\_range\_count](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [myisam\_data\_pointer\_size](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [myisam\_max\_sort\_file\_size](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [myisam\_mmap\_size](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [myisam\_recover\_options](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [myisam\_sort\_buffer\_size](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [myisam\_stats\_method](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [myisam\_use\_mmap](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [mysql\_firewall\_mode](firewall-reference.md) | Yes | Yes | Yes | Global | Yes |
| [mysql\_firewall\_trace](firewall-reference.md) | Yes | Yes | Yes | Global | Yes |
| [mysql\_native\_password\_proxy\_users](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [mysqlx\_bind\_address](x-plugin-options-system-variables.md) | Yes | Yes | Yes | Global | No |
| [mysqlx\_connect\_timeout](x-plugin-options-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [mysqlx\_idle\_worker\_thread\_timeout](x-plugin-options-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [mysqlx\_max\_allowed\_packet](x-plugin-options-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [mysqlx\_max\_connections](x-plugin-options-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [mysqlx\_min\_worker\_threads](x-plugin-options-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [mysqlx\_port](x-plugin-options-system-variables.md) | Yes | Yes | Yes | Global | No |
| [mysqlx\_port\_open\_timeout](x-plugin-options-system-variables.md) | Yes | Yes | Yes | Global | No |
| [mysqlx\_socket](x-plugin-options-system-variables.md) | Yes | Yes | Yes | Global | No |
| [mysqlx\_ssl\_ca](x-plugin-options-system-variables.md) | Yes | Yes | Yes | Global | No |
| [mysqlx\_ssl\_capath](x-plugin-options-system-variables.md) | Yes | Yes | Yes | Global | No |
| [mysqlx\_ssl\_cert](x-plugin-options-system-variables.md) | Yes | Yes | Yes | Global | No |
| [mysqlx\_ssl\_cipher](x-plugin-options-system-variables.md) | Yes | Yes | Yes | Global | No |
| [mysqlx\_ssl\_crl](x-plugin-options-system-variables.md) | Yes | Yes | Yes | Global | No |
| [mysqlx\_ssl\_crlpath](x-plugin-options-system-variables.md) | Yes | Yes | Yes | Global | No |
| [mysqlx\_ssl\_key](x-plugin-options-system-variables.md) | Yes | Yes | Yes | Global | No |
| [named\_pipe](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [named\_pipe\_full\_access\_group](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [ndb\_allow\_copying\_alter\_table](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Both | Yes |
| [ndb\_autoincrement\_prefetch\_sz](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Both | Yes |
| [ndb\_batch\_size](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Both | Yes |
| [ndb\_blob\_read\_batch\_bytes](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Both | Yes |
| [ndb\_blob\_write\_batch\_bytes](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Both | Yes |
| [ndb\_cache\_check\_time](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [ndb\_clear\_apply\_status](mysql-cluster-options-variables.md) | Yes |  | Yes | Global | Yes |
| [ndb\_cluster\_connection\_pool](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | No |
| [ndb\_cluster\_connection\_pool\_nodeids](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | No |
| [ndb\_data\_node\_neighbour](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [ndb\_default\_column\_format](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [ndb\_default\_column\_format](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [ndb\_deferred\_constraints](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Both | Yes |
| [ndb\_deferred\_constraints](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Both | Yes |
| [ndb\_distribution](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [ndb\_distribution](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [ndb\_eventbuffer\_free\_percent](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [ndb\_eventbuffer\_max\_alloc](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [ndb\_extra\_logging](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [ndb\_force\_send](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Both | Yes |
| [ndb\_fully\_replicated](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Both | Yes |
| [ndb\_index\_stat\_enable](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Both | Yes |
| [ndb\_index\_stat\_option](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Both | Yes |
| [ndb\_join\_pushdown](mysql-cluster-options-variables.md) |  |  | Yes | Both | Yes |
| [ndb\_log\_apply\_status](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | No |
| [ndb\_log\_apply\_status](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | No |
| [ndb\_log\_bin](mysql-cluster-options-variables.md) | Yes |  | Yes | Both | No |
| [ndb\_log\_binlog\_index](mysql-cluster-options-variables.md) | Yes |  | Yes | Global | Yes |
| [ndb\_log\_empty\_epochs](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [ndb\_log\_empty\_epochs](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [ndb\_log\_empty\_update](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [ndb\_log\_empty\_update](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [ndb\_log\_exclusive\_reads](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Both | Yes |
| [ndb\_log\_exclusive\_reads](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Both | Yes |
| [ndb\_log\_fail\_terminate](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | No |
| [ndb\_log\_orig](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | No |
| [ndb\_log\_orig](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | No |
| [ndb\_log\_transaction\_id](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | No |
| [ndb\_log\_transaction\_id](mysql-cluster-options-variables.md) |  |  | Yes | Global | No |
| [ndb\_log\_update\_as\_write](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [ndb\_log\_update\_minimal](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [ndb\_log\_updated\_only](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [ndb\_optimization\_delay](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [ndb\_optimized\_node\_selection](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [ndb\_optimized\_node\_selection](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | No |
| [ndb\_read\_backup](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [ndb\_recv\_thread\_activation\_threshold](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [ndb\_recv\_thread\_cpu\_mask](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [ndb\_report\_thresh\_binlog\_epoch\_slip](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [ndb\_report\_thresh\_binlog\_mem\_usage](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [ndb\_row\_checksum](mysql-cluster-options-variables.md) |  |  | Yes | Both | Yes |
| [ndb\_show\_foreign\_key\_mock\_tables](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [ndb\_slave\_conflict\_role](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [Ndb\_system\_name](mysql-cluster-options-variables.md) |  |  | Yes | Global | No |
| [ndb\_table\_no\_logging](mysql-cluster-options-variables.md) |  |  | Yes | Session | Yes |
| [ndb\_table\_temporary](mysql-cluster-options-variables.md) |  |  | Yes | Session | Yes |
| [ndb\_use\_copying\_alter\_table](mysql-cluster-options-variables.md) |  |  | Yes | Both | No |
| [ndb\_use\_exact\_count](mysql-cluster-options-variables.md) |  |  | Yes | Both | Yes |
| [ndb\_use\_transactions](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Both | Yes |
| [ndb\_version](mysql-cluster-options-variables.md) |  |  | Yes | Global | No |
| [ndb\_version\_string](mysql-cluster-options-variables.md) |  |  | Yes | Global | No |
| [ndb\_wait\_connected](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | No |
| [ndb\_wait\_setup](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | No |
| [ndbinfo\_database](mysql-cluster-options-variables.md) |  |  | Yes | Global | No |
| [ndbinfo\_max\_bytes](mysql-cluster-options-variables.md) | Yes |  | Yes | Both | Yes |
| [ndbinfo\_max\_rows](mysql-cluster-options-variables.md) | Yes |  | Yes | Both | Yes |
| [ndbinfo\_offline](mysql-cluster-options-variables.md) |  |  | Yes | Global | Yes |
| [ndbinfo\_show\_hidden](mysql-cluster-options-variables.md) | Yes |  | Yes | Both | Yes |
| [ndbinfo\_table\_prefix](mysql-cluster-options-variables.md) |  |  | Yes | Global | No |
| [ndbinfo\_version](mysql-cluster-options-variables.md) |  |  | Yes | Global | No |
| [net\_buffer\_length](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [net\_read\_timeout](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [net\_retry\_count](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [net\_write\_timeout](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [new](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [ngram\_token\_size](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [offline\_mode](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [old](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [old\_alter\_table](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [old\_passwords](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [open\_files\_limit](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [optimizer\_prune\_level](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [optimizer\_search\_depth](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [optimizer\_switch](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [optimizer\_trace](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [optimizer\_trace\_features](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [optimizer\_trace\_limit](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [optimizer\_trace\_max\_mem\_size](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [optimizer\_trace\_offset](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [parser\_max\_mem\_size](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [performance\_schema](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_accounts\_size](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_digests\_size](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_events\_stages\_history\_long\_size](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_events\_stages\_history\_size](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_events\_statements\_history\_long\_size](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_events\_statements\_history\_size](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_events\_transactions\_history\_long\_size](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_events\_transactions\_history\_size](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_events\_waits\_history\_long\_size](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_events\_waits\_history\_size](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_hosts\_size](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_max\_cond\_classes](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_max\_cond\_instances](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_max\_digest\_length](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_max\_file\_classes](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_max\_file\_handles](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_max\_file\_instances](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_max\_index\_stat](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_max\_memory\_classes](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_max\_metadata\_locks](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_max\_mutex\_classes](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_max\_mutex\_instances](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_max\_prepared\_statements\_instances](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_max\_program\_instances](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_max\_rwlock\_classes](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_max\_rwlock\_instances](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_max\_socket\_classes](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_max\_socket\_instances](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_max\_sql\_text\_length](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_max\_stage\_classes](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_max\_statement\_classes](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_max\_statement\_stack](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_max\_table\_handles](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_max\_table\_instances](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_max\_table\_lock\_stat](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_max\_thread\_classes](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_max\_thread\_instances](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_session\_connect\_attrs\_size](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_setup\_actors\_size](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_setup\_objects\_size](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [performance\_schema\_show\_processlist](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [performance\_schema\_users\_size](performance-schema-system-variables.md) | Yes | Yes | Yes | Global | No |
| [pid\_file](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [plugin\_dir](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [port](server-options.md) | Yes | Yes | Yes | Global | No |
| [preload\_buffer\_size](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [profiling](server-system-variables.md) |  |  | Yes | Both | Yes |
| [profiling\_history\_size](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [protocol\_version](server-system-variables.md) |  |  | Yes | Global | No |
| [proxy\_user](server-system-variables.md) |  |  | Yes | Session | No |
| [pseudo\_slave\_mode](server-system-variables.md) |  |  | Yes | Session | Yes |
| [pseudo\_thread\_id](server-system-variables.md) |  |  | Yes | Session | Yes |
| [query\_alloc\_block\_size](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [query\_cache\_limit](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [query\_cache\_min\_res\_unit](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [query\_cache\_size](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [query\_cache\_type](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [query\_cache\_wlock\_invalidate](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [query\_prealloc\_size](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [rand\_seed1](server-system-variables.md) |  |  | Yes | Session | Yes |
| [rand\_seed2](server-system-variables.md) |  |  | Yes | Session | Yes |
| [range\_alloc\_block\_size](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [range\_optimizer\_max\_mem\_size](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [rbr\_exec\_mode](server-system-variables.md) |  |  | Yes | Session | Yes |
| [read\_buffer\_size](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [read\_only](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [read\_rnd\_buffer\_size](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [relay\_log](replication-options-replica.md) | Yes | Yes | Yes | Global | No |
| [relay\_log\_basename](replication-options-replica.md) |  |  | Yes | Global | No |
| [relay\_log\_index](replication-options-replica.md) | Yes | Yes | Yes | Global | No |
| [relay\_log\_info\_file](replication-options-replica.md) | Yes | Yes | Yes | Global | No |
| [relay\_log\_info\_repository](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [relay\_log\_purge](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [relay\_log\_recovery](replication-options-replica.md) | Yes | Yes | Yes | Global | No |
| [relay\_log\_space\_limit](replication-options-replica.md) | Yes | Yes | Yes | Global | No |
| [replication\_optimize\_for\_static\_plugin\_config](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [replication\_sender\_observe\_commit\_only](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [report\_host](replication-options-replica.md) | Yes | Yes | Yes | Global | No |
| [report\_password](replication-options-replica.md) | Yes | Yes | Yes | Global | No |
| [report\_port](replication-options-replica.md) | Yes | Yes | Yes | Global | No |
| [report\_user](replication-options-replica.md) | Yes | Yes | Yes | Global | No |
| [require\_secure\_transport](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [rewriter\_enabled](rewriter-query-rewrite-plugin-reference.md) |  |  | Yes | Global | Yes |
| [rewriter\_verbose](rewriter-query-rewrite-plugin-reference.md) |  |  | Yes | Global | Yes |
| [rpl\_semi\_sync\_master\_enabled](replication-options-source.md) | Yes | Yes | Yes | Global | Yes |
| [rpl\_semi\_sync\_master\_timeout](replication-options-source.md) | Yes | Yes | Yes | Global | Yes |
| [rpl\_semi\_sync\_master\_trace\_level](replication-options-source.md) | Yes | Yes | Yes | Global | Yes |
| [rpl\_semi\_sync\_master\_wait\_for\_slave\_count](replication-options-source.md) | Yes | Yes | Yes | Global | Yes |
| [rpl\_semi\_sync\_master\_wait\_no\_slave](replication-options-source.md) | Yes | Yes | Yes | Global | Yes |
| [rpl\_semi\_sync\_master\_wait\_point](replication-options-source.md) | Yes | Yes | Yes | Global | Yes |
| [rpl\_semi\_sync\_slave\_enabled](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [rpl\_semi\_sync\_slave\_trace\_level](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [rpl\_stop\_slave\_timeout](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [secure\_auth](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [secure\_file\_priv](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [server\_id](replication-options.md) | Yes | Yes | Yes | Global | Yes |
| [server\_id\_bits](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | No |
| [server\_uuid](replication-options.md) |  |  | Yes | Global | No |
| [session\_track\_gtids](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [session\_track\_schema](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [session\_track\_state\_change](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [session\_track\_system\_variables](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [session\_track\_transaction\_info](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [sha256\_password\_auto\_generate\_rsa\_keys](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [sha256\_password\_private\_key\_path](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [sha256\_password\_proxy\_users](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [sha256\_password\_public\_key\_path](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [shared\_memory](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [shared\_memory\_base\_name](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [show\_compatibility\_56](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [show\_create\_table\_verbosity](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [show\_old\_temporals](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [skip\_external\_locking](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [skip\_name\_resolve](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [skip\_networking](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [skip\_show\_database](server-options.md) | Yes | Yes | Yes | Global | No |
| [skip\_slave\_start](replication-options-replica.md) | Yes | Yes | Yes | Global | No |
| [slave\_allow\_batching](mysql-cluster-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [slave\_checkpoint\_group](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [slave\_checkpoint\_period](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [slave\_compressed\_protocol](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [slave\_exec\_mode](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [slave\_load\_tmpdir](replication-options-replica.md) | Yes | Yes | Yes | Global | No |
| [slave\_max\_allowed\_packet](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [slave\_net\_timeout](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [slave\_parallel\_type](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [slave\_parallel\_workers](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [slave\_pending\_jobs\_size\_max](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [slave\_preserve\_commit\_order](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [slave\_rows\_search\_algorithms](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [slave\_skip\_errors](replication-options-replica.md) | Yes | Yes | Yes | Global | No |
| [slave\_sql\_verify\_checksum](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [slave\_transaction\_retries](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [slave\_type\_conversions](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [slow\_launch\_time](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [slow\_query\_log](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [slow\_query\_log\_file](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [socket](server-options.md) | Yes | Yes | Yes | Global | No |
| [sort\_buffer\_size](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [sql\_auto\_is\_null](server-system-variables.md) |  |  | Yes | Both | Yes |
| [sql\_big\_selects](server-system-variables.md) |  |  | Yes | Both | Yes |
| [sql\_buffer\_result](server-system-variables.md) |  |  | Yes | Both | Yes |
| [sql\_log\_bin](replication-options-binary-log.md) |  |  | Yes | Session | Yes |
| [sql\_log\_off](server-system-variables.md) |  |  | Yes | Both | Yes |
| [sql\_mode](server-options.md) | Yes | Yes | Yes | Both | Yes |
| [sql\_notes](server-system-variables.md) |  |  | Yes | Both | Yes |
| [sql\_quote\_show\_create](server-system-variables.md) |  |  | Yes | Both | Yes |
| [sql\_safe\_updates](server-system-variables.md) |  |  | Yes | Both | Yes |
| [sql\_select\_limit](server-system-variables.md) |  |  | Yes | Both | Yes |
| [sql\_slave\_skip\_counter](replication-options-replica.md) |  |  | Yes | Global | Yes |
| [sql\_warnings](server-system-variables.md) |  |  | Yes | Both | Yes |
| [ssl\_ca](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [ssl\_capath](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [ssl\_cert](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [ssl\_cipher](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [ssl\_crl](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [ssl\_crlpath](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [ssl\_key](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [stored\_program\_cache](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [super\_read\_only](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [sync\_binlog](replication-options-binary-log.md) | Yes | Yes | Yes | Global | Yes |
| [sync\_frm](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [sync\_master\_info](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [sync\_relay\_log](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [sync\_relay\_log\_info](replication-options-replica.md) | Yes | Yes | Yes | Global | Yes |
| [system\_time\_zone](server-system-variables.md) |  |  | Yes | Global | No |
| [table\_definition\_cache](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [table\_open\_cache](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [table\_open\_cache\_instances](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [thread\_cache\_size](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [thread\_handling](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [thread\_pool\_algorithm](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [thread\_pool\_high\_priority\_connection](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [thread\_pool\_max\_unused\_threads](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [thread\_pool\_prio\_kickup\_timer](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [thread\_pool\_size](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [thread\_pool\_stall\_limit](server-system-variables.md) | Yes | Yes | Yes | Global | Yes |
| [thread\_stack](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [time\_format](server-system-variables.md) |  |  | Yes | Global | No |
| [time\_zone](server-system-variables.md) |  |  | Yes | Both | Yes |
| [timestamp](server-system-variables.md) |  |  | Yes | Session | Yes |
| [tls\_version](server-system-variables.md) | Yes | Yes | Yes | Global | No |
| [tmp\_table\_size](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [tmpdir](server-options.md) | Yes | Yes | Yes | Global | No |
| [transaction\_alloc\_block\_size](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [transaction\_allow\_batching](mysql-cluster-options-variables.md) |  |  | Yes | Session | Yes |
| [transaction\_isolation](server-options.md) | Yes | Yes |  |  | Yes |
| \- *Variable*: [tx\_isolation](server-system-variables.md) |  |  | Yes | Both | Yes |
| [transaction\_prealloc\_size](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [transaction\_read\_only](server-options.md) | Yes | Yes |  |  | Yes |
| \- *Variable*: [tx\_read\_only](server-system-variables.md) |  |  | Yes | Both | Yes |
| [transaction\_write\_set\_extraction](replication-options-binary-log.md) | Yes | Yes | Yes | Both | Yes |
| [tx\_isolation](server-system-variables.md) |  |  | Yes | Both | Yes |
| [tx\_read\_only](server-system-variables.md) |  |  | Yes | Both | Yes |
| [unique\_checks](server-system-variables.md) |  |  | Yes | Both | Yes |
| [updatable\_views\_with\_limit](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [validate\_password\_check\_user\_name](validate-password-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [validate\_password\_dictionary\_file](validate-password-options-variables.md) | Yes | Yes | Yes | Global | Varies |
| [validate\_password\_length](validate-password-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [validate\_password\_mixed\_case\_count](validate-password-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [validate\_password\_number\_count](validate-password-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [validate\_password\_policy](validate-password-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [validate\_password\_special\_char\_count](validate-password-options-variables.md) | Yes | Yes | Yes | Global | Yes |
| [version](server-system-variables.md) |  |  | Yes | Global | No |
| [version\_comment](server-system-variables.md) |  |  | Yes | Global | No |
| [version\_compile\_machine](server-system-variables.md) |  |  | Yes | Global | No |
| [version\_compile\_os](server-system-variables.md) |  |  | Yes | Global | No |
| [version\_tokens\_session](version-tokens-reference.md) | Yes | Yes | Yes | Both | Yes |
| [version\_tokens\_session\_number](version-tokens-reference.md) | Yes | Yes | Yes | Both | No |
| [wait\_timeout](server-system-variables.md) | Yes | Yes | Yes | Both | Yes |
| [warning\_count](server-system-variables.md) |  |  | Yes | Session | No |

**Notes:**

1\. This option is dynamic, but should be set only by server. You should not set this variable manually.