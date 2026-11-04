---
title: SQL Language Quick Reference
book: SQL Language Quick Reference
doc_id: F31302-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlqr/SQL-Statements.html
tags:
  - oracle
  - 21c
  - sql-language-quick-reference
---

This chapter presents the syntax for Oracle SQL statements.

This chapter includes the following section:

- Syntax for SQL Statements

### Syntax for SQL Statements

SQL statements are the means by which programs and users access data in an Oracle database.

The sections that follow show each SQL statement and its related syntax. Refer to [Subclauses](Subclauses.md) for the syntax of the subclauses listed in the syntax for the statements.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF008) for detailed information about SQL statements

[ADMINISTER KEY MANAGEMENT](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF55976)

```
ADMINISTER KEY MANAGEMENT
  { keystore_management_clauses
  | key_management_clauses
  | secret_management_clauses
  | zero_downtime_software_patching_clauses
  } ;
```

[ALTER ANALYTIC VIEW](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-5256BE3A-F134-40D4-8E70-684E073574C8)

```
ALTER ANALYTIC VIEW [ schema. ] analytic_view_name 
  { RENAME TO new_av_name | COMPILE | alter_add_cache_clause | alter_drop_cache_clause };
```

[ALTER ATTRIBUTE DIMENSION](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-F345D0F9-8133-4257-9A07-EDCE558A1332)

```
ALTER ATTRIBUTE DIMENSION [ schema. ]
  attr_dim_name { RENAME TO new_attr_dim_name | COMPILE };
```

[ALTER AUDIT POLICY](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF56045)

```
ALTER AUDIT POLICY policy
  [ ADD [ privilege_audit_clause ] [ action_audit_clause ] [ role_audit_clause ] ]
  [ DROP [ privilege_audit_clause ] [ action_audit_clause ] [ role_audit_clause ] ]
  [ CONDITION { DROP | 'audit_condition' 
    EVALUATE PER { STATEMENT | SESSION | INSTANCE }   } ]
  [ ONLY TOPLEVEL ]
;
```

[ALTER CLUSTER](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00801)

```
ALTER CLUSTER [ schema. ] cluster
  { physical_attributes_clause
  | SIZE size_clause
  | [ MODIFY PARTITION partition ] allocate_extent_clause
  | deallocate_unused_clause
  | { CACHE | NOCACHE }
  } ...
  [ parallel_clause ] ;
```

[ALTER DATABASE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00802)

```
ALTER DATABASE [ database ]
  { startup_clauses
  | recovery_clauses
  | database_file_clauses
  | logfile_clauses
  | controlfile_clauses
  | standby_database_clauses
  | default_settings_clauses
  | instance_clauses
  | security_clause
  | prepare_clause
  | drop_mirror_copy
  | lost_write_protection
  | cdb_fleet_clauses
  | property_clause
  | replay_upgrade_clause
  } ;
```

[ALTER DATABASE DICTIONARY](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-27DDB403-7E7F-40EC-9B48-5E3B475E27AE)

```
ALTER DATABASE DICTIONARY 
{   ENCRYPT CREDENTIALS
  | REKEY CREDENTIALS
  | DELETE CREDENTIALS KEY 
};
```

[ALTER DATABASE LINK](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF30050)

```
ALTER [ SHARED ] [ PUBLIC ] DATABASE LINK dblink
  { CONNECT { ( TO user IDENTIFIED BY password [ dblink_authentication ] )
  | WITH credential }
  | dblink_authentication
  };
```

[ALTER DIMENSION](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00803)

```
ALTER DIMENSION [ schema. ] dimension
  { ADD { level_clause
        | hierarchy_clause
        | attribute_clause
        | extended_attribute_clause
        }
  } ...
  |
  { DROP { LEVEL level [ RESTRICT | CASCADE ]
         | HIERARCHY hierarchy
         | ATTRIBUTE attribute [ LEVEL level [ COLUMN column ] ]...
         }
  } ...
  |
  COMPILE
  ;
```

[ALTER DISKGROUP](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF01113)

```
ALTER DISKGROUP
  { diskgroup_name
      { { { add_disk_clause | drop_disk_clause }
          [, { add_disk_clause | drop_disk_clause } ]...
        | resize_disk_clause
        } [ rebalance_diskgroup_clause ]
      | replace_disk_clause
      | rename_disk_clause
      | disk_online_clause
      | disk_offline_clause
      | rebalance_diskgroup_clause
      | check_diskgroup_clause
      | diskgroup_template_clauses
      | diskgroup_directory_clauses
      | diskgroup_alias_clauses
      | diskgroup_volume_clauses
      | diskgroup_attributes
      | drop_diskgroup_file_clause
      | convert_redundancy_clause
      | usergroup_clauses
      | user_clauses
      | file_permissions_clause
      | file_owner_clause
      | scrub_clause
      | quotagroup_clauses
      | filegroup_clauses
      }
    | { diskgroup_name [, diskgroup_name ]...
      | ALL
      } { undrop_disk_clause
        | diskgroup_availability
        | enable_disable_volume
        }
  } ;
```

[ALTER FLASHBACK ARCHIVE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF20009)

```
ALTER FLASHBACK ARCHIVE flashback_archive
  { SET DEFAULT
  | { ADD | MODIFY } TABLESPACE tablespace [flashback_archive_quota]
  | REMOVE TABLESPACE tablespace_name
  | MODIFY RETENTION flashback_archive_retention
  | PURGE { ALL | BEFORE { SCN expr | TIMESTAMP expr } }
  | [NO] OPTIMIZE DATA
  };
```

[ALTER FUNCTION](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00804)

```
ALTER FUNCTION [ schema. ] function_name
{ function_compile_clause | { EDITIONABLE | NONEDITIONABLE } }
```

[ALTER HIERARCHY](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-37A4E442-EE3A-4239-8228-F08A2F666D91)

```
ALTER HIERARCHY [ schema. ] hierarchy_name 
  { RENAME TO new_hier_name | COMPILE };
```

[ALTER INDEX](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00805)

```
ALTER INDEX [ schema. ]index_name [ index_ilm_clause ]
  { { deallocate_unused_clause
    | allocate_extent_clause
    | shrink_clause
    | parallel_clause
    | physical_attributes_clause
    | logging_clause
    | partial_index_clause
    } ...
  | rebuild_clause [ { DEFERRED | IMMEDIATE } INVALIDATION ]
  | PARAMETERS ( 'ODCI_parameters' )
  | COMPILE
  | { ENABLE | DISABLE }
  | UNUSABLE [ ONLINE ] [ { DEFERRED | IMMEDIATE } INVALIDATION ]
  | VISIBLE | INVISIBLE
  | RENAME TO new_name
  | COALESCE [ CLEANUP ] [ ONLY ] [ parallel_clause ]
  | { MONITORING | NOMONITORING } USAGE
  | UPDATE BLOCK REFERENCES
  | alter_index_partitioning
  }
  ;
```

[ALTER INDEXTYPE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00806)

```
ALTER INDEXTYPE [ schema. ] indextype
  { { ADD | DROP } [ schema. ] operator ( parameter_types ) 
      [ , { ADD | DROP } [schema. ] operator ( parameter_types ) ]... [ using_type_clause ]
  | COMPILE
  }
  [ WITH LOCAL [ RANGE ] PARTITION ] [ storage_table_clause ]
  ;
```

[ALTER INMEMORY JOIN GROUP](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF57214)

```
ALTER INMEMORY JOIN GROUP [ schema. ] join_group
  { ADD | REMOVE } ( [ schema. ] table ( column ) ) ;
```

[ALTER JAVA](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00807)

```
ALTER JAVA
  { SOURCE | CLASS } [ schema. ]object_name 
  [ RESOLVER 
      ( ( match_string [, ] { schema_name | - } )... )
  ]
  { { COMPILE | RESOLVE }
  | invoker_rights_clause
  } ;
```

[ALTER LIBRARY](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00818)

```
ALTER LIBRARY [ schema. ] library_name
{ library_compile_clause | { EDITIONABLE | NONEDITIONABLE } }
```

[ALTER LOCKDOWN PROFILE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-B4029154-54A8-4B78-97C3-9CED416F1C34)

```
ALTER LOCKDOWN PROFILE
  { lockdown_features
  | lockdown_options
  | lockdown_statements
  [ USERS = { ALL | COMMON | LOCAL } ];
  } ;
```

[ALTER MATERIALIZED VIEW](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00808)

```
ALTER MATERIALIZED VIEW
  [ schema. ] materialized_view
  [ physical_attributes_clause
  | modify_mv_column_clause
  | table_compression
  | inmemory_table_clause
  | LOB_storage_clause [, LOB_storage_clause ]...
  | modify_LOB_storage_clause [, modify_LOB_storage_clause ]...
  | alter_table_partitioning
  | parallel_clause
  | logging_clause
  | allocate_extent_clause
  | deallocate_unused_clause
  | shrink_clause
  | { CACHE | NOCACHE }
  ]
  [ alter_iot_clauses ]
  [ USING INDEX physical_attributes_clause ]
  [ MODIFY scoped_table_ref_constraint
  | alter_mv_refresh
  ]
  [ evaluation_edition_clause ]
  [ { ENABLE | DISABLE } ON QUERY COMPUTATION ]
  [ alter_query_rewrite_clause
  | COMPILE
  | CONSIDER FRESH
  ] ;
```

[ALTER MATERIALIZED VIEW LOG](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00809)

```
ALTER MATERIALIZED VIEW LOG [ FORCE ]
  ON [ schema. ]table
  [ physical_attributes_clause
  | add_mv_log_column_clause
  | alter_table_partitioning
  | parallel_clause
  | logging_clause
  | allocate_extent_clause
  | shrink_clause
  | move_mv_log_clause
  | { CACHE | NOCACHE }
  ] [ mv_log_augmentation ] [  mv_log_purge_clause ] [ for_refresh_clause ]
  ;
```

[ALTER MATERIALIZED ZONEMAP](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF56854)

```
ALTER MATERIALIZED ZONEMAP [ schema. ] zonemap_name
  { alter_zonemap_attributes
  | zonemap_refresh_clause
  | { ENABLE | DISABLE } PRUNING
  | COMPILE
  | REBUILD
  | UNUSABLE
  } ;
```

[ALTER OPERATOR](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF01112)

```
ALTER OPERATOR [ schema. ] operator
  { add_binding_clause
  | drop_binding_clause
  | COMPILE
  } ;
```

[ALTER OUTLINE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00810)

```
ALTER OUTLINE [ PUBLIC | PRIVATE ] outline
  { REBUILD
  | RENAME TO new_outline_name
  | CHANGE CATEGORY TO new_category_name
  | { ENABLE | DISABLE }
  } ...
  ;
```

[ALTER PACKAGE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00811)

```
ALTER PACKAGE [ schema. ] package_name
{ package_compile_clause | { EDITIONABLE | NONEDITIONABLE } }
```

[ALTER PLUGGABLE DATABASE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF55667)

```
ALTER PLUGGABLE DATABASE
  { pdb_unplug_clause
  | pdb_settings_clauses
  | pdb_datafile_clause
  | pdb_recovery_clauses
  | pdb_change_state
  | pdb_change_state_from_root
  | application_clauses
  | snapshot_clauses
  | prepare_clause
  | drop_mirror_copy
  | lost_write_protection
  | pdb_managed_recovery
  } ;
```

[ALTER PMEM FILESTORE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-330BB1D5-5194-4B09-93AF-B80DBD36774A)

```
ALTER PMEM FILESTORE  filestore_name
 (
  ( [ RESIZE size_clause ]  |  autoextend_clause )
 | ( MOUNT [ (MOUNTPOINT file_path | BACKINGFILE file_name) ] [ FORCE ] )
 | DISMOUNT
 )
```

[ALTER PROCEDURE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00812)

```
ALTER PROCEDURE [ schema. ] procedure_name
{ procedure_compile_clause | { EDITIONABLE | NONEDITIONABLE } }
```

[ALTER PROFILE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00813)

```
ALTER PROFILE profile LIMIT
  { resource_parameters | password_parameters } ...
  [ CONTAINER = { CURRENT | ALL } ] ;
```

[ALTER RESOURCE COST](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00814)

```
ALTER RESOURCE COST
  { { CPU_PER_SESSION
    | CONNECT_TIME
    | LOGICAL_READS_PER_SESSION
    | PRIVATE_SGA
    } integer
  } ...
  ;
```

[ALTER ROLE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00815)

```
ALTER ROLE role
  { NOT IDENTIFIED
  | IDENTIFIED
      { BY password
      | USING [ schema. ] package
      | EXTERNALLY
      | GLOBALLY AS domain_name_of_directory_group
      }
  }
  [ CONTAINER = { CURRENT | ALL } ] ;
```

[ALTER ROLLBACK SEGMENT](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00816)

```
ALTER ROLLBACK SEGMENT rollback_segment
  { ONLINE
  | OFFLINE
  | storage_clause
  | SHRINK [ TO size_clause ]
  };
```

[ALTER SEQUENCE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00817)

```
ALTER SEQUENCE [ schema. ] sequence
  { 
    { INCREMENT BY | START WITH } integer
  | { MAXVALUE integer | NOMAXVALUE }
  | { MINVALUE integer | NOMINVALUE }
  |   RESTART
  | { CYCLE | NOCYCLE }
  | { CACHE integer | NOCACHE }
  | { ORDER | NOORDER }
  | { KEEP | NOKEEP }
  | { SCALE {EXTEND | NOEXTEND} | NOSCALE }
  | { SHARD {EXTEND | NOEXTEND} | NOSHARD }
  | { SESSION | GLOBAL }
  } ...
;
```

[ALTER SESSION](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00901)

```
ALTER SESSION
 { ADVISE { COMMIT | ROLLBACK | NOTHING }
 | CLOSE DATABASE LINK dblink
 | { ENABLE | DISABLE } COMMIT IN PROCEDURE
 | { ENABLE | DISABLE } GUARD
 | { ENABLE | DISABLE | FORCE } PARALLEL
   { DML | DDL | QUERY } [ PARALLEL integer ]
 | { ENABLE RESUMABLE [ TIMEOUT integer ] [ NAME string ]
   | DISABLE RESUMABLE
   }
 | { ENABLE | DISABLE } SHARD DDL
 | SYNC WITH PRIMARY  
 | alter_session_set_clause
 } ;
```

[ALTER SYNONYM](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF56347)

```
ALTER [ PUBLIC ] SYNONYM [ schema. ] synonym
  { EDITIONABLE | NONEDITIONABLE | COMPILE } ;
```

[ALTER SYSTEM](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00902)

```
ALTER SYSTEM
  { archive_log_clause
  | checkpoint_clause
  | check_datafiles_clause
  | distributed_recov_clauses
  | FLUSH { SHARED_POOL | GLOBAL CONTEXT | BUFFER_CACHE | FLASH_CACHE
          | REDO TO target_db_name [ [ NO ] CONFIRM APPLY ] }
  | end_session_clauses
  | SWITCH LOGFILE
  | { SUSPEND | RESUME }
  | quiesce_clauses
  | rolling_migration_clauses
  | rolling_patch_clauses
  | security_clauses
  | affinity_clauses
  | shutdown_dispatcher_clause
  | REGISTER
  | SET alter_system_set_clause
        [ alter_system_set_clause ]...
  | RESET alter_system_reset_clause
          [ alter_system_reset_clause ]...
  | RELOCATE CLIENT client_id
  | cancel_sql_clause
  | FLUSH PASSWORDFILE_METADATA_CACHE
  } ;
```

[ALTER TABLE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF01001)

```
ALTER TABLE [ schema. ] table
  [ memoptimize_read_clause ] [ memoptimize_write_clause ]
  [ alter_table_properties
  | column_clauses
  | constraint_clauses
  | alter_table_partitioning [ { DEFERRED | IMMEDIATE } INVALIDATION ]
  | alter_external_table
  | move_table_clause
  | modify_to_partitioned
  | modify_opaque_type   
  | immutable_table_clauses
  | blockchain_table_clauses
  ]
  [ enable_disable_clause
  | { ENABLE | DISABLE }
    { TABLE LOCK | ALL TRIGGERS | CONTAINER_MAP | CONTAINERS_DEFAULT }
  ] ...
  ;
```

[ALTER TABLESPACE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF01002)

```
ALTER TABLESPACE tablespace alter_tablespace_attrs ;
```

[ALTER TABLESPACE SET](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-63FEDE73-C1F1-4B7A-98ED-8C34C4073549)

```
ALTER TABLESPACE SET tablespace_set alter_tablespace_attrs ;
```

[ALTER TRIGGER](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF01101)

```
ALTER TRIGGER [ schema. ] trigger_name
  { trigger_compile_clause
  | { ENABLE| DISABLE }
  | RENAME TO new_name
  | { EDITIONABLE | NONEDITIONABLE }
  } ;
```

[ALTER TYPE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF01102)

```
ALTER TYPE [ schema. ] type_name
{ alter_type_clause | { EDITIONABLE | NONEDITIONABLE } }
```

[ALTER USER](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF01103)

```
ALTER USER
  { user
    { IDENTIFIED
      { BY password [ REPLACE old_password ]
      | EXTERNALLY [ AS 'certificate_DN' | AS 'kerberos_principal_name' ]
      | GLOBALLY [ AS '[directory_DN]' ]
      }
    | NO AUTHENTICATION
    | DEFAULT COLLATION collation_name
    | DEFAULT TABLESPACE tablespace
    | [ LOCAL ] TEMPORARY TABLESPACE { tablespace | tablespace_group_name }
    | { QUOTA { size_clause
              | UNLIMITED
              } ON tablespace
      } ...
    | PROFILE profile
    | DEFAULT ROLE { role [, role ]...
                   | ALL [ EXCEPT role [, role ]... ]
                   | NONE
                   }
    | PASSWORD EXPIRE
    | EXPIRE PASSWORD ROLLOVER PERIOD 
    | ACCOUNT { LOCK | UNLOCK }
    | ENABLE EDITIONS [ FOR object_type [, object_type ]... ] [ FORCE ]
    | [HTTP] DIGEST { ENABLE | DISABLE }
    | CONTAINER = { CURRENT | ALL }
    | container_data_clause
    } ...
  | user [, user ]... proxy_clause
  } ;
```

[ALTER VIEW](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF01104)

```
ALTER VIEW [ schema. ] view
  { ADD out_of_line_constraint
  | MODIFY CONSTRAINT constraint
      { RELY | NORELY }
  | DROP { CONSTRAINT constraint
         | PRIMARY KEY
         | UNIQUE (column [, column ]...)
         }
  | COMPILE
  | { READ ONLY | READ WRITE }
  | { EDITIONABLE | NONEDITIONABLE }
  } ;
```

[ANALYZE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF01105)

```
ANALYZE
  { { TABLE [ schema. ] table
    | INDEX [ schema. ] index
    } [ partition_extension_clause ]
  | CLUSTER [ schema. ] cluster
  }
  { validation_clauses
  | LIST CHAINED ROWS [ into_clause ]
  | DELETE [ SYSTEM ] STATISTICS
  } ;
```

[ASSOCIATE STATISTICS](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF01106)

```
ASSOCIATE STATISTICS WITH
  { column_association | function_association }
  [ storage_table_clause ] ;
```

[AUDIT (Traditional Auditing)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF01107)

```
AUDIT
  { audit_operation_clause [ auditing_by_clause | IN SESSION CURRENT ]
  | audit_schema_object_clause
  | NETWORK
  | DIRECT_PATH LOAD [ auditing_by_clause ]
  } [ BY { SESSION | ACCESS } ]
    [ WHENEVER [ NOT ] SUCCESSFUL ]
    [ CONTAINER = { CURRENT | ALL } ]
;
```

[AUDIT (Unified Auditing)](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF56110)

```
AUDIT
  { POLICY policy
    [ { BY user [, user]... }
    | { EXCEPT user [, user]... }
    | by_users_with_roles ]
    [ WHENEVER [ NOT ] SUCCESSFUL ]
  }
  |
  { CONTEXT NAMESPACE namespace ATTRIBUTES attribute [, attribute ]...
      [, CONTEXT NAMESPACE namespace ATTRIBUTES attribute [, attribute ]... ]...
    [ BY user [, user]... ]
  } ;
```

[CALL](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF01108)

```
CALL
  { routine_clause
  | object_access_expression
  }
  [ INTO :host_variable
    [ [ INDICATOR ] :indicator_variable ] ] ;
```