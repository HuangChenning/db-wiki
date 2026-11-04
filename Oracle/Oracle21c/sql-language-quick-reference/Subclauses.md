---
title: SQL Language Quick Reference
book: SQL Language Quick Reference
doc_id: F31302-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlqr/Subclauses.html
tags:
  - oracle
  - 21c
  - sql-language-quick-reference
---

This chapter presents the syntax for the subclauses found in the syntax for SQL statements, functions, expressions and conditions.

This chapter includes the following section:

- Syntax for Subclauses

### Syntax for Subclauses

The sections that follow show the syntax for each subclause found in:

- [SQL Statements](SQL-Statements.md)
- [SQL Functions](SQL-Functions.md)
- [SQL Expressions](SQL-Expressions.md)
- [SQL Conditions](SQL-Conditions.md)
	See Also:
	[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF008) for detailed information about SQL subclauses

action\_audit\_clause

```
{ standard_actions | component_actions }...
```

activate\_standby\_db\_clause

```
ACTIVATE
     [ PHYSICAL | LOGICAL ]
     STANDBY DATABASE
     [ FINISH APPLY ]
```

add\_binding\_clause

```
ADD BINDING
  (parameter_type [, parameter_type ]...)
  RETURN (return_type)
  [ implementation_clause ]
  using_function_clause
```

add\_column\_clause

```
ADD
    { column_definition | virtual_column_definition } 
     | ( { column_definition | virtual_column_definition } 
         [, { column_definition | virtual_column_definition } ]...
       )
   [ column_properties ]
   [ ( out_of_line_part_storage [, out_of_line_part_storage]... ) ]
```

add\_disk\_clause

```
ADD
  { SITE sitename [ QUORUM | REGULAR ] [ FAILGROUP failgroup_name ]
    DISK qualified_disk_clause [, qualified_disk_clause ]...
  }...
```

add\_external\_partition\_attrs

```
ADD EXTERNAL PARTITION ATTRIBUTES external_table_clause 
 [ REJECT LIMIT ]
```

add\_filegroup\_clause

```
ADD FILEGROUP filegroup_name
  { DATABASE database_name
  | CLUSTER cluster_name
  | VOLUME asm_volume
  | TEMPLATE               }
  [ FROM TEMPLATE <template_name> ]
  }
[ SET '[ file_type. ] property_name' = 'property_value' ]
```

add\_hash\_index\_partition

```
ADD PARTITION
   [ partition_name ]
   [ TABLESPACE tablespace_name ]
   [ index_compression ]
   [ parallel_clause ]
```

add\_hash\_partition\_clause

```
partitioning_storage_clause
[ update_index_clauses ]
[ parallel_clause ]
[ read_only_clause ]
[ indexing_clause ]
```

add\_hash\_subpartition

```
ADD individual_hash_subparts
   [ dependent_tables_clause ]
   [ update_index_clauses ]
   [ parallel_clause ]
```

add\_list\_partition\_clause

```
list_values_clause
[ table_partition_description ]
[ external_part_subpart_data_props ]
[ ( { range_subpartition_desc [, range_subpartition_desc] ...
    | list_subpartition_desc [, list_subpartition_desc] ...
    | individual_hash_subparts [, individual_hash_subparts] ...
    }
  ) | hash_subparts_by_quantity ]
[ update_index_clauses ]
```

add\_list\_subpartition

```
ADD list_subpartition_desc [, list_subpartition_desc ]...
[ dependent_tables_clause ] [ update_index_clauses ]
```

add\_logfile\_clauses

```
ADD [ STANDBY ] LOGFILE
   { 
     { [ INSTANCE 'instance_name' ] | [ THREAD 'integer' ] }
     [ GROUP integer ] redo_log_file_spec
       [, [ GROUP integer ] redo_log_file_spec ]...
   | MEMBER 'filename' [ REUSE ] [, 'filename' [ REUSE ] ]...
        TO logfile_descriptor [, logfile_descriptor ]...
   }
```

add\_meas\_clause

```
ADD MEASURES  ( (cube_meas)...)
```

add\_mv\_log\_column\_clause

```
ADD (column)
```

add\_overflow\_clause

```
ADD OVERFLOW [ segment_attributes_clause ]
  [ ( PARTITION [ segment_attributes_clause ]
    [, PARTITION [ segment_attributes_clause ] ]...
    )
  ]
```

add\_period\_clause

```
ADD ( period_definition )
```

add\_range\_partition\_clause

```
range_values_clause
[ table_partition_description ]
[ external_part_subpart_data_props ]
[ ( { range_subpartition_desc [, range_subpartition_desc] ...
    | list_subpartition_desc [, list_subpartition_desc] ...
    | individual_hash_subparts [, individual_hash_subparts] ...
    }
  ) | hash_subparts_by_quantity ]
[ update_index_clauses ]
```

add\_range\_subpartition

```
ADD range_subpartition_desc [, range_subpartition_desc ]...
[ dependent_tables_clause ] [ update_index_clauses ]
```

add\_system\_partition\_clause

```
[table_partition_description]
[update_index_clauses]
```

add\_table\_partition

```
ADD {
PARTITION [ partition ] add_range_partition_clause
  [, PARTITION [ partition ] add_range_partition_clause ]...
| PARTITION [ partition ] add_list_partition_clause
  [, PARTITION [ partition ] add_list_partition_clause ]...
| PARTITION [ partition ] add_system_partition_clause
  [, PARTITION [ partition ] add_system_partition_clause ]...
  [ BEFORE { partition_name | partition_number } ]
| PARTITION [ partition ] add_hash_partition_clause
} [ dependent_tables_clause ]
```

add\_update\_secret

```
{ ADD | UPDATE } SECRET 'secret' FOR CLIENT 'client_identifier'
  [ USING TAG 'tag' ]
  [ FORCE KEYSTORE ]
  IDENTIFIED BY { EXTERNAL STORE | keystore_password }
   WITH BACKUP [ USING 'backup_identifier' ]
```

add\_update\_secret\_seps

```
{ ADD | UPDATE } SECRET 'secret' FOR CLIENT 'client_identifier'
  [ USING TAG 'tag' ]
  TO  [ LOCAL ] AUTO_LOGIN KEYSTORE 'directory'
```

add\_volume\_clause

```
ADD VOLUME asm_volume SIZE size_clause [redundancy_clause]
  [ STRIPE_WIDTH integer {K | M} ]
  [ STRIPE_COLUMNS integer ]
```

advanced\_index\_compression

```
{ COMPRESS ADVANCED [ LOW | HIGH ] } | NOCOMPRESS
```

affinity\_clauses

```
{ ENABLE AFFINITY [ schema.]table [SERVICE service_name ]
| 
DISABLE AFFINITY [ schema.]table   
}
```

alias\_file\_name

```
+diskgroup_name [ (template_name) ] /alias_name
```

all\_clause

```
ALL  MEMBER { NAME expression [ MEMBER CAPTION expression ]
            | CAPTION expression [ MEMBER DESCRIPTION expression ]
            | DESCRIPTION expression 
            }
```

allocate\_extent\_clause

```
ALLOCATE EXTENT
  [ ( { SIZE size_clause
      | DATAFILE 'filename'
      | INSTANCE integer
      } ...
    )
  ]
```

allow\_disallow\_clustering

```
{ ALLOW | DISALLOW } CLUSTERING
```

alter\_add\_cache\_clause

```
ADD CACHE
  MEASURE GROUP [ ALL | ( meas_name )... ]
  LEVELS ( [ [ dim_alias "." ] hier_alias "." ] level )...
```

alter\_automatic\_partitioning

```
{ SET PARTITIONING { AUTOMATIC | MANUAL }
| SET STORE IN ( tablespace [, tablespace ]... )
}
```

alter\_datafile\_clause

```
DATAFILE
   { 'filename' | filenumber }
     [, 'filename' | filenumber ]...
   }
   { ONLINE
   | OFFLINE [ FOR DROP ]
   | RESIZE size_clause
   | autoextend_clause
   | END BACKUP
   | ENCRYPT
   | DECRYPT
   }
```

alter\_drop\_cache\_clause

```
DROP CACHE
  MEASURE GROUP [ ALL | ( meas_name )... ]
  LEVELS ( [ [ dim_alias "." ] hier_alias "." ] level )...
```

alter\_external\_table

```
{ add_column_clause
| modify_column_clauses
| drop_column_clause
| parallel_clause
| external_table_data_props
| REJECT LIMIT { integer | UNLIMITED }
| PROJECT COLUMN { ALL | REFERENCED }
}
  [ add_column_clause
  | modify_column_clauses
  | drop_column_clause
  | parallel_clause
  | external_table_data_props
  | REJECT LIMIT { integer | UNLIMITED }
  | PROJECT COLUMN { ALL | REFERENCED }
  ]...
```

alter\_index\_partitioning

```
{ modify_index_default_attrs
| add_hash_index_partition
| modify_index_partition
| rename_index_partition
| drop_index_partition
| split_index_partition
| coalesce_index_partition
| modify_index_subpartition
}
```

alter\_interval\_partitioning

```
{ SET INTERVAL ( [ expr ] )
| SET STORE IN ( tablespace [, tablespace]... )
}
```

alter\_iot\_clauses

```
{ index_org_table_clause
| alter_overflow_clause
| alter_mapping_table_clauses
| COALESCE
}
```

alter\_keystore\_password

```
ALTER KEYSTORE PASSWORD
  [ FORCE KEYSTORE ]
  IDENTIFIED BY old_keystore_password
  SET new_keystore_password
  WITH BACKUP [ USING 'backup_identifier' ]
```

alter\_mapping\_table\_clauses

```
MAPPING TABLE
  { allocate_extent_clause
  | deallocate_unused_clause
  }
```

alter\_mv\_refresh

```
REFRESH
   { { FAST | COMPLETE | FORCE }
   | ON { DEMAND | COMMIT }
   | { START WITH | NEXT } date
   | WITH PRIMARY KEY
   | USING
        { DEFAULT MASTER ROLLBACK SEGMENT
        | MASTER ROLLBACK SEGMENT rollback_segment
        }
   | USING { ENFORCED | TRUSTED } CONSTRAINTS
   }
```

alter\_overflow\_clause

```
{ add_overflow_clause
| OVERFLOW
     { segment_attributes_clause
     | allocate_extent_clause
     | shrink_clause
     | deallocate_unused_clause
     }...
}
```

alter\_query\_rewrite\_clause

```
[ ENABLE | DISABLE ] QUERY REWRITE [ unusable_editions_clause ]
```

alter\_session\_set\_clause

```
SET { { parameter_name = parameter_value }...
    | EDITION = edition_name
    | CONTAINER = container_name [ SERVICE = service_name ]
    | ROW ARCHIVAL VISIBILITY = { ACTIVE | ALL }
    | DEFAULT_COLLATION = { collation_name | NONE }
    }
```

alter\_system\_reset\_clause

```
parameter_name
   [ { SCOPE = { MEMORY | SPFILE | BOTH }
     | SID = { 'sid' | '*' }
     }...
   ]
```

alter\_system\_set\_clause

```
{ set_parameter_clause
| USE_STORED_OUTLINES = (TRUE | FALSE | category_name)
| GLOBAL_TOPIC_ENABLED = (TRUE | FALSE)
}
```

alter\_table\_partitioning

```
{ modify_table_default_attrs
| alter_automatic_partitioning
| alter_interval_partitioning
| set_subpartition_template
| modify_table_partition
| modify_table_subpartition
| move_table_partition
| move_table_subpartition
| add_external_partition_attrs
| add_table_partition
| coalesce_table_partition
| drop_external_partition_attrs
| drop_table_partition
| drop_table_subpartition
| rename_partition_subpart
| truncate_partition_subpart
| split_table_partition
| split_table_subpartition
| merge_table_partitions
| merge_table_subpartitions
| exchange_partition_subpart
}
```

alter\_table\_properties

```
{ { { physical_attributes_clause
    | logging_clause
    | table_compression
    | inmemory_table_clause
    | ilm_clause
    | supplemental_table_logging
    | allocate_extent_clause
    | deallocate_unused_clause
    | { CACHE | NOCACHE }
    | result_cache_clause
    | upgrade_table_clause
    | records_per_block_clause
    | parallel_clause
    | row_movement_clause
    | logical_replication_clause
    | flashback_archive_clause
    }...
  | RENAME TO new_table_name
  } [ alter_iot_clauses ] [ alter_XMLSchema_clause ]
| { shrink_clause
  | READ ONLY
  | READ WRITE
  | REKEY encryption_spec
  | DEFAULT COLLATION collation_name
  | [NO] ROW ARCHIVAL
  | ADD attribute_clustering_clause
  | MODIFY CLUSTERING [ clustering_when ] [ zonemap_clause ]
  | DROP CLUSTERING
  }
}
```

alter\_tablespace\_attrs

```
{ default_tablespace_params
| MINIMUM EXTENT size_clause
| RESIZE size_clause
| COALESCE
| SHRINK SPACE [ KEEP size_clause ]
| RENAME TO new_tablespace_name
| { BEGIN | END } BACKUP
| datafile_tempfile_clauses
| tablespace_logging_clauses
| tablespace_group_clause
| tablespace_state_clauses
| autoextend_clause
| flashback_mode_clause
| tablespace_retention_clause
| alter_tablespace_encryption
}
```

alter\_tablespace\_encryption

```
ENCRYPTION
  { { OFFLINE [ tablespace_encryption_spec ] { ENCRYPT | DECRYPT } }
  | { ONLINE { { [ tablespace_encryption_spec ] { ENCRYPT | REKEY } }
               | DECRYPT }
             [ ts_file_name_convert ] }
  | { FINISH { ENCRYPT | REKEY | DECRYPT } [ ts_file_name_convert ] }
  }
```

alter\_tempfile\_clause

```
TEMPFILE
   { 'filename' [, 'filename' ]...
   | filenumber [, filenumber ]...
   }
   { RESIZE size_clause
   | autoextend_clause
   | DROP [ INCLUDING DATAFILES ]
   | ONLINE
   | OFFLINE
   }
```

alter\_varray\_col\_properties

```
MODIFY VARRAY varray_item
   ( modify_LOB_parameters )
```

alter\_XMLSchema\_clause

```
{ ALLOW ANYSCHEMA
| ALLOW NONSCHEMA
| DISALLOW NONSCHEMA
}
```

alter\_zonemap\_attributes

```
{ PCTFREE integer
| PCTUSED integer
| { CACHE | NOCACHE }
}...
```

alternate\_key\_clause

```
ALTERNATE KEY { [ ( ] attribute [ ) ]
                |  
                ( attribute [, attribute ]... )
              }
```

analytic\_clause

```
[ { query_partition_clause | window_name } ] [ order_by_clause [ windowing_clause ] ]
```

append\_op

```
APPEND pathExpr "=" rhsExpr [ { CREATE | IGNORE | ERROR  } ON MISSING ]
            [ ( NULL | IGNORE | ERROR) ON NULL ]
```

application\_clauses

```
APPLICATION
{ { app_name
    { BEGIN INSTALL 'app_version' [ COMMENT 'comment' ]
    | END INSTALL [ 'app_version' ]
    | BEGIN PATCH number [ MINIMUM VERSION 'app_version' ] [ COMMENT 'comment' ]
    | END PATCH [ number ]
    | BEGIN UPGRADE ['start_app_version'] TO 'end_app_version' [ COMMENT 'comment' ]
    | END UPGRADE [ TO 'end_app_version' ]
    | BEGIN UNINSTALL
    | END UNINSTALL
    | SET PATCH number
    | SET VERSION 'app_version'
    | SET COMPATIBILITY VERSION { 'app_version' | CURRENT }
    | SYNC TO  { 'app_version' | PATCH patch_number } 
    | [( app_name )...] SYNC
    }
  }
  |
  { ALL [ EXCEPT (app_name)... ] SYNC }
}
```

archive\_log\_clause

```
ARCHIVE LOG
   [  INSTANCE 'instance_name' ]
   { { SEQUENCE integer
     | CHANGE integer
     | CURRENT [ NOSWITCH ]
     | GROUP integer
     | LOGFILE 'filename'
          [ USING BACKUP CONTROLFILE ]
     | NEXT
     | ALL
     }
     [ TO 'location' ]
   }
```

array\_DML\_clause

```
[ WITH | WITHOUT ]
ARRAY DML
[ ([ schema. ]type
   [, [ schema. ]varray_type ])
    [, ([ schema. ]type
        [, [ schema. ]varray_type ])...
]
```

array\_step

```
[ { integer | integer TO integer [, integer | integer TO integer ]... } | * ]

Note: The outside square brackets shown in boldface type are part of
      the syntax. In this case, they do not represent optionality.
```

ASM\_filename

```
{ fully_qualified_file_name
| numeric_file_name
| incomplete_file_name
| alias_file_name
}
```

attr\_dim\_attributes\_clause

```
[ alias. ] column [ [ AS ] attribute_name ] [ classification_clause ]...
```

attr\_dim\_level\_clause

```
LEVEL level [ { NOT NULL  |  SKIP WHEN NULL } ]
  [ classification_clause [ classification_clause ]...
  [ LEVEL TYPE 
      {   STANDARD 
        | YEARS 
        | HALF_YEARS
        | QUARTERS
        | MONTHS
        | WEEKS
        | DAYS
        | HOURS
        | MINUTES
        | SECONDS
      }
  ]
  key_clause [ alternate_key_clause ]
  [ MEMBER NAME expression ]
  [ MEMBER CAPTION expression ] 
  [ MEMBER DESCRIPTION expression ]
  [ ORDER BY  [ MIN | MAX ] dim_order_clause 
                    [, [ MIN | MAX ] dim_order_clause ]... ]
  ]
  [ DETERMINES ( attribute [, attribute]... ) ]
```

attr\_dim\_using\_clause

```
USING (source_clause)... [ (join_path_clause)...
```

attribute\_clause

```
ATTRIBUTE level DETERMINES
   { dependent_column
   | ( dependent_column
       [, dependent_column ]... )
   }
```

attribute\_clustering\_clause

```
CLUSTERING [ clustering_join ] cluster_clause
           [ clustering_when ] [ zonemap_clause ]
```

attributes\_clause

```
ATTRIBUTES ( attr_dim_attribute_clause [, attr_dim_attribute_clause ]... )
```

audit\_operation\_clause

```
{ { sql_statement_shortcut
  | ALL
  | ALL STATEMENTS
  } [, { sql_statement_shortcut
       | ALL
       }
    ]
| { system_privilege
  | ALL PRIVILEGES
  } [, { system_privilege
       | ALL PRIVILEGES
       }
    ]
}
```

audit\_schema\_object\_clause

```
{ sql_operation [, sql_operation ]
| ALL
} auditing_on_clause
```

auditing\_by\_clause

```
BY user [, user ]...
```

auditing\_on\_clause

```
ON { [ schema. ] object
   | DIRECTORY directory_name
   | MINING MODEL [ schema. ] model
   | SQL TRANSLATION PROFILE [ schema. ] profile
   | DEFAULT
   }
```

autoextend\_clause

```
AUTOEXTEND
   { OFF
   | ON [ NEXT size_clause ]
        [ maxsize_clause ]
   }
```

av\_meas\_expression

```
{  lead_lag_expression
 | window_expression 
 | share_of_expression
 | qdr_expression
}
```

av\_measure

```
meas_name  [{ base_measure_clause | calc_measure_clause }]
  [ classification_clause ]...
```

av\_simple\_expression

```
{ string | number | NULL | measure_ref }
```

av\_window\_clause

```
HIERARCHY hierarchy_ref
  BETWEEN { preceding_boundary | following_boundary }
[ WITHIN {   LEVEL 
           | PARENT
           | ANCESTOR AT LEVEL level_ref 
         }
```

backup\_keystore

```
BACKUP KEYSTORE [ USING 'backup_identifier' ]
  [ FORCE KEYSTORE ]
  IDENTIFIED BY { EXTERNAL STORE | keystore_password }
  [ TO 'keystore_location' ]
```

base\_meas\_clause

```
FACT FOR MEASURE base_meas meas_aggregate_clause
```

binding\_clause

```
BINDING
   (parameter_type [, parameter_type ]...)
   RETURN return_type
   [ implementation_clause ]
   using_function_clause
    [, (parameter_type [, parameter_type ]...)
       RETURN return_type
       [ implementation_clause ]
       using_function_clause
    ]...
```

bitmap\_join\_index\_clause

```
[ schema.]table
   ( [ [ schema. ]table. | t_alias. ]column
     [ ASC | DESC  ]
       [, [ [ schema. ]table. | t_alias. ]column
          [ ASC | DESC ]
       ]...
   )
   FROM [ schema. ]table [ t_alias ]
          [, [ schema. ]table [ t_alias ]
        ]...
   WHERE condition
      [ local_partitioned_index ] index_attributes
```

blockchain\_table\_clauses

```
blockchain_drop_table_clause blockchain_row_retention_clause 
blockchain_hash_and_data_format_clause
```

blockchain\_drop\_table\_clause

```
NO DROP [ UNTIL number DAYS IDLE ]
```

blockchain\_row\_retention\_clause

```
NO DELETE ( ( [LOCKED] ) | (UNTIL number DAYS AFTER INSERT [LOCKED]) )
```

blockchain\_hash\_and\_data\_format\_clause

```
HASHING USING sha2_512 VERSION v1
```

build\_clause

```
BUILD { IMMEDIATE | DEFERRED }
```

by\_users\_with\_roles

```
BY USERS WITH GRANTED ROLES role [, role]...
```

cache\_clause

```
CACHE cache_specification [, cache_specification]...
```

cache\_specification

```
MEASURE GROUP
 {    ALL 
   | ( measure_name [, measure_name ]... ) [ levels_clause ]...
 }
```

calc\_meas\_order\_by\_clause

```
calc_meas_expression [ { ASC | DESC } ]  [ NULLS { FIRST | LAST } ]
```

calc\_meas\_clause

```
AS ( expression )
```

cancel\_sql\_clause

```
CANCEL SQL ' session_id , serial_number [ , @ instance_id ] [ , sql_id ] '
```

cell\_assignment

```
measure_column [ { { condition
                   | expr
                   | single_column_for_loop
                   }
                     [, { condition
                        | expr
                        | single_column_for_loop
                        }
                     ]...
                 | multi_column_for_loop
                 }
               ]

Note: The outer square brackets are part of the syntax.
      In this case, they do not indicate optionality.
```

cell\_reference\_options

```
[ { IGNORE | KEEP } NAV ]
[ UNIQUE { DIMENSION | SINGLE REFERENCE } ]
```

character\_set\_clause

```
CHARACTER SET character_set
```

check\_datafiles\_clause

```
CHECK DATAFILES [ GLOBAL | LOCAL ]
```

check\_diskgroup\_clause

```
CHECK [ REPAIR | NOREPAIR ]
```

checkpoint\_clause

```
CHECKPOINT [ GLOBAL | LOCAL ]
```

classification\_clause

```
[ CAPTION caption ]
[ DESCRIPTION description ]
[ CLASSIFICATION classification_name
  [ VALUE classification_value ] 
  [ LANGUAGE language ]
]...
```

clause\_options

```
OPTION
{ { = ( 'clause_option' | 'clause_option_pattern'
        [, 'clause_option' | 'clause_option_pattern' ]... ) }
| { = ( 'clause_option' ) option_values }
| { ALL [ EXCEPT = ( 'clause_option' | 'clause_option_pattern'
                     [, 'clause_option' | 'clause_option_pattern' ]... ) ] }
}
```

clear\_free\_space\_clause

```
CLEAR FREE SPACE
```

close\_keystore

```
SET KEYSTORE CLOSE
  [ IDENTIFIED BY { EXTERNAL STORE | keystore_password } ]
  [ CONTAINER = { ALL | CURRENT } ]
```

cluster\_clause

```
BY [ LINEAR | INTERLEAVED ] ORDER clustering_columns
```

cluster\_index\_clause

```
CLUSTER [ schema. ] cluster index_attributes
```

cluster\_range\_partitions

```
PARTITION BY RANGE (column[, column ]...)
( PARTITION [ partition ]
    range_values_clause table_partition_description
      [, PARTITION [ partition ]
        range_values_clause table_partition_description
      ]...
)
```

clustering\_column\_group

```
( column [, column ]... )
```

clustering\_columns

```
clustering_column_group
| ( clustering_column_group [, clustering_column_group ]... )
```

clustering\_join

```
[ schema. ] table JOIN [ schema. ] table ON ( equijoin_condition )
                    [, JOIN [ schema. ] table ON ( equijoin_condition ) ]...
```

clustering\_when

```
[ { YES | NO } ON LOAD ] [ { YES | NO } ON DATA MOVEMENT ]
```

coalesce\_index\_partition

```
COALESCE PARTITION [ parallel_clause ]
```

coalesce\_table\_partition

```
COALESCE PARTITION
  [ update_index_clauses ]
  [ parallel_clause ]
  [ allow_disallow_clustering ]
```

coalesce\_table\_subpartition

```
COALESCE SUBPARTITION subpartition
  [update_index_clauses]
  [parallel_clause]
  [allow_disallow_clustering]
```

column\_association

```
COLUMNS [ schema. ]table.column
          [, [ schema. ]table.column ]...
   using_statistics_type
```

column\_clauses

```
{ { add_column_clause
  | modify_column_clauses
  | drop_column_clause
  | add_period_clause
  | drop_period_clause
  }...
| rename_column_clause
| { modify_collection_retrieval }...
| { modify_LOB_storage_clause }...
| { alter_varray_col_properties }...
}
```

column\_definition

```
column [ datatype [ COLLATE column_collation_name ] ]
  [ SORT ] [ VISIBLE | INVISIBLE ]
  [ DEFAULT [ ON NULL ] expr | identity_clause ]
  [ ENCRYPT encryption_spec ]
  [ { inline_constraint }...
  | inline_ref_constraint
  ]
```

column\_properties

```
{ object_type_col_properties
| nested_table_col_properties
| { varray_col_properties | LOB_storage_clause }
    [ (LOB_partition_storage [, LOB_partition_storage ]...) ]
| XMLType_column_properties
| json_storage_clause
}...
```

commit\_switchover\_clause

```
{ PREPARE | COMMIT } TO SWITCHOVER
[ TO { { [ PHYSICAL | LOGICAL ] PRIMARY
     | [ PHYSICAL ] STANDBY
     } [ { WITH | WITHOUT } SESSION SHUTDOWN
         { WAIT | NOWAIT }
       ]
     | LOGICAL STANDBY
     }
| CANCEL
]
```

component\_actions

```
ACTIONS COMPONENT =
  { DATAPUMP | DIRECT_LOAD | OLS | XS } component_action [, component_action ]...
  |
  DV component_action ON object_name [, component_action ON object_name ]...
  | PROTOCOL { HTTP | FTP | AUTHENTICATION }
```

composite\_hash\_partitions

```
PARTITION BY HASH (column [, column ] ...)
  { subpartition_by_range
  | subpartition_by_list
  | subpartition_by_hash
  }
  { individual_hash_partitions
  | hash_partitions_by_quantity
  }
```

composite\_list\_partitions

```
PARTITION BY LIST ( column [, column]... )
[ AUTOMATIC [ STORE IN ( tablespace [, tablespace ]... ) ] ]
  { subpartition_by_range
  | subpartition_by_list
  | subpartition_by_hash
  }
( list_partition_desc [, list_partition_desc]... )
```

composite\_range\_partitions

```
PARTITION BY RANGE ( column [, column]... )
  [ INTERVAL ( expr ) [ STORE IN ( tablespace [, tablespace]... ) ]]
  { subpartition_by_range
  | subpartition_by_list
  | subpartition_by_hash
  }
( range_partition_desc [, range_partition_desc]... )
```

condition\_clause

```
{ tracking_statistics_clause |  ( ON PLSQL_function_name ) }
```

conditional\_insert\_clause

```
[ ALL | FIRST ]
WHEN condition
THEN insert_into_clause
  [ values_clause ]
  [ error_logging_clause ]
  [ insert_into_clause [ values_clause ] [ error_logging_clause ] ]...
[ WHEN condition
  THEN insert_into_clause
    [ values_clause ]
    [ error_logging_clause ]
    [ insert_into_clause [ values_clause ] [ error_logging_clause ] ]...
]...
[ ELSE insert_into_clause
  [ values_clause ]
  [ error_logging_clause ]
   [ insert_into_clause [ values_clause ] [ error_logging_clause ] ]...
]
```

consistent\_hash\_partitions

```
PARTITION BY CONSISTENT HASH (column [, column ]...)
  [ PARTITIONS AUTO ] TABLESPACE SET tablespace_set
```

consistent\_hash\_with\_subpartitions

```
PARTITION BY CONSISTENT HASH (column [, column ]...)
  { subpartition_by_range
  | subpartition_by_list
  | subpartition_by_hash
  }
  [ PARTITIONS AUTO ]
```

constraint

```
{ inline_constraint
| out_of_line_constraint
| inline_ref_constraint
| out_of_line_ref_constraint
}
```

constraint\_clauses

```
{ ADD { { out_of_line_constraint }...
      | out_of_line_REF_constraint
      }
| MODIFY { CONSTRAINT constraint_name
         | PRIMARY KEY
         | UNIQUE (column [, column ]...)
         } constraint_state [ CASCADE ]
| RENAME CONSTRAINT old_name TO new_name
| { drop_constraint_clause }...
}
```

constraint\_state

```
[ [NOT] DEFERRABLE [INITIALLY {IMMEDIATE | DEFERRED}] ]
 |  INITIALLY { IMMEDIATE | DEFERRED } [ NOT ] [ DEFERRABLE ]
]
[  RELY | NORELY  ]
[ using_index_clause ]
[ ENABLE | DISABLE ]
[ VALIDATE | NOVALIDATE ]
[ exceptions_clause
```

container\_data\_clause

```
{
SET CONTAINER_DATA = { ALL | DEFAULT | ( container_name [, container_name ]... ) }
|
ADD CONTAINER_DATA = ( container_name [, container_name ]... )
|
REMOVE CONTAINER_DATA = ( container_name [, container_name ]... )
}
[ FOR [ schema. ] container_data_object ]
```

container\_map\_clause

```
CONTAINER_MAP UPDATE { add_table_partition | split_table_partition }
```

containers\_clause

```
CONTAINERS( [schema.] { table | view } )
```

context\_clause

```
[ WITH INDEX CONTEXT,
  SCAN CONTEXT implementation_type
  [ COMPUTE ANCILLARY DATA ]
]
[ WITH COLUMN CONTEXT ]
```

controlfile\_clauses

```
CREATE { [ LOGICAL | PHYSICAL ] STANDBY | FAR SYNC INSTANCE }
  CONTROLFILE AS
  'filename' [ REUSE ]
| BACKUP CONTROLFILE TO
  { 'filename' [ REUSE ]
  | trace_file_clause
  }
```

convert\_database\_clause

```
CONVERT TO ( PHYSICAL | SNAPSHOT ) STANDBY
```

convert\_redundancy\_clause

```
CONVERT TO FLEX REDUNDANCY
```

cost\_matrix\_clause

```
COST
  { MODEL [AUTO]
  | ( class_value [, class_value]... )
        VALUES ( ( cost_value [, cost_value]...) 
                 [ , (cost_value [, cost_value]... ) ]...
               )
  }
```

create\_datafile\_clause

```
CREATE DATAFILE
   { 'filename' | filenumber }
     [, 'filename' | filenumber ]...
   }
   [ AS { file_specification
          [, file_specification ]...
        | NEW
        }
   ]
```

create\_file\_dest\_clause

```
CREATE_FILE_DEST = { NONE | 'directory_path_name' | diskgroup_name }
```

create\_key

```
CREATE [ ENCRYPTION ] KEY
  [ USING TAG 'tag' ]
  [ USING ALGORITHM 'encrypt_algorithm' ]
  [ FORCE KEYSTORE ]
  IDENTIFIED BY { EXTERNAL STORE | keystore_password }
  WITH BACKUP [ USING 'backup_identifier' ] 
  [ CONTAINER = { ALL | CURRENT } ]
```

create\_keystore

```
CREATE
  { KEYSTORE ['keystore_location']
  | [ LOCAL ] AUTO_LOGIN KEYSTORE FROM KEYSTORE ['keystore_location']
  }
  IDENTIFIED BY keystore_password
```

create\_mv\_refresh

```
{ REFRESH
  { { FAST | COMPLETE | FORCE }
  | { ON DEMAND 
    | ON COMMIT 
    | ON STATEMENT
    }
  | { START WITH date |
      NEXT date 
    }...
  | WITH { PRIMARY KEY | ROWID }
  | USING
     { DEFAULT [ MASTER | LOCAL ] ROLLBACK SEGMENT
     | [ MASTER | LOCAL ] ROLLBACK SEGMENT rollback_segment
     }...
  | USING
     { ENFORCED | TRUSTED } CONSTRAINTS
  }...
| NEVER REFRESH
}
```

create\_pdb\_clone

```
{ { FROM { src_pdb_name [ @ dblink ] } | { NON$CDB @ dblink } }
|
  { AS PROXY FROM src_pdb_name @ dblink }
}
  [ parallel_pdb_creation_clause ]
  [ default_tablespaces ]
  [ pdb_storage_clause ]
  [ file_name_convert ]
  [ service_name_convert ]
  [ path_prefix_clause ]
  [ tempfile_reuse_clause ]
  [ SNAPSHOT COPY ]
  [ user_tablespaces_clause ]
  [ standbys_clause ]
  [ logging_clause ]
  [ create_file_dest_clause ]
  [ keystore_clause ]
  [ pdb_refresh_mode_clause ]
  [ RELOCATE ]
  [ NO DATA ] 
  [ HOST = 'hostname' ]
  [ PORT = number ]
```

create\_pdb\_from\_mirror\_copy

```
new_pdb_name FROM base_pdb_name @dblinkname 
USING MIRROR COPY mirror_name
```

create\_pdb\_from\_seed

```
ADMIN USER admin_user_name IDENTIFIED BY password
  [ pdb_dba_roles ]
  [ parallel_pdb_creation_clause ]
  [ default_tablespace ]
  [ pdb_storage_clause ]
  [ file_name_convert ]
  [ service_name_convert ]
  [ path_prefix_clause ]
  [ tempfile_reuse_clause ]
  [ user_tablespaces_clause ]
  [ standbys_clause ]
  [ logging_clause ]
  [ create_file_dest_clause ]
  [ HOST = 'hostname' ]
  [ PORT = number ]
```

create\_pdb\_from\_xml

```
[ AS CLONE ] USING filename
  [ source_file_name_convert | source_file_directory ]
  [ { [ COPY | MOVE ] file_name_convert } | NOCOPY ]
  [ service_name_convert ]
  [ default_tablespace ]
  [ pdb_storage_clause ]
  [ path_prefix_clause ]
  [ tempfile_reuse_clause ]
  [ user_tablespaces_clause ]
  [ standbys_clause ]
  [ logging_clause ]
  [ create_file_dest_clause ]
  [ HOST = 'hostname' ]
  [ PORT = number ]
```

create\_zonemap\_as\_subquery

```
CREATE MATERIALIZED ZONEMAP
  [ schema. ] zonemap_name
  [ zonemap_attributes ]
  [ zonemap_refresh_clause ]
  [ { ENABLE | DISABLE } PRUNING ]
  AS query_block
```

create\_zonemap\_on\_table

```
CREATE MATERIALIZED ZONEMAP
  [ schema. ] zonemap_name
  [ zonemap_attributes ]
  [ zonemap_refresh_clause ]
  [ { ENABLE | DISABLE } PRUNING ]
  ON [ schema. ] { table | materialized_view } ( column [, column]... )
```

cross\_outer\_apply\_clause

```
{ CROSS | OUTER } APPLY { table_reference | collection_expression }
```

cube\_meas

```
meas_name( base_meas_clause | calc_meas_clause )
```

cycle\_clause

```
{CYCLE c_alias [, c_alias]...
    SET cycle_mark_c_alias TO cycle_value
    DEFAULT no_cycle_value
}
```

database\_file\_clauses

```
{ RENAME FILE  'filename' [, 'filename' ]...
   TO 'filename'
| create_datafile_clause
| alter_datafile_clause
| alter_tempfile_clause
| move_datafile_clause
}
```

database\_logging\_clauses

```
{ LOGFILE
    [ GROUP integer ] file_specification
      [, [ GROUP integer ] file_specification ]...
| MAXLOGFILES integer
| MAXLOGMEMBERS integer
| MAXLOGHISTORY integer
| { ARCHIVELOG | NOARCHIVELOG }
| FORCE LOGGING
| SET STANDBY NOLOGGING FOR {DATA AVAILABILITY | LOAD PERFORMANCE}
}
```

datafile\_tempfile\_clauses

```
{ ADD { DATAFILE | TEMPFILE }
   [ file_specification [, file_specification ]... ]
| DROP {DATAFILE | TEMPFILE } { 'filename' | file_number }
| SHRINK TEMPFILE { 'filename' | file_number } [KEEP size_clause]
| RENAME DATAFILE 'filename' [, 'filename' ]...
    TO 'filename' [, 'filename' ]...
| { DATAFILE | TEMPFILE } { ONLINE | OFFLINE }
}
```

datafile\_tempfile\_spec

```
[ 'filename' | 'ASM_filename' ]
[ SIZE size_clause ]
[ REUSE ]
[ autoextend_clause ]
```

db\_user\_proxy\_clauses

```
[ WITH
  { ROLE { role_name [, role_name]...
         | ALL EXCEPT role_name [, role_name]...
         }
  | NO ROLES
  }
]
[ AUTHENTICATION REQUIRED ]
```

dblink

```
database[.domain [.domain ]... ] [ @ connection_qualifier ]
```

dblink\_authentication

```
AUTHENTICATED BY user IDENTIFIED BY password
```

deallocate\_unused\_clause

```
DEALLOCATE UNUSED [ KEEP size_clause ]
```

default\_aggregate\_clause

```
DEFAULT AGGREGATE BY aggr_function
```

default\_cost\_clause

```
DEFAULT COST (cpu_cost, io_cost, network_cost)
```

default\_index\_compression

```
INDEX { COMPRESS ADVANCED { LOW | HIGH }
      | NOCOMPRESS
      }
```

default\_measure\_clause

```
DEFAULT MEASURE measure
```

default\_selectivity\_clause

```
DEFAULT SELECTIVITY default_selectivity
```

default\_settings\_clauses

```
{ DEFAULT EDITION = edition_name
| SET DEFAULT { BIGFILE | SMALLFILE } TABLESPACE
| DEFAULT TABLESPACE tablespace
| DEFAULT [ LOCAL ] TEMPORARY TABLESPACE { tablespace | tablespace_group_name }
| RENAME GLOBAL_NAME TO database.domain [.domain ]...
| ENABLE BLOCK CHANGE TRACKING [ USING FILE 'filename' [ REUSE ] ]
| DISABLE BLOCK CHANGE TRACKING
| [NO] FORCE FULL DATABASE CACHING
| CONTAINERS DEFAULT TARGET = { (container_name) | NONE }
| flashback_mode_clause
| undo_mode_clause
| set_time_zone_clause
}
```

default\_table\_compression

```
TABLE { COMPRESS FOR OLTP
      | COMPRESS FOR QUERY { LOW | HIGH }
      | COMPRESS FOR ARCHIVE { LOW | HIGH }
      | NOCOMPRESS
      }
```

default\_tablespace

```
DEFAULT TABLESPACE tablespace
[ DATAFILE datafile_tempfile_spec ]
[ extent_management_clause ]
```

default\_tablespace\_params

```
DEFAULT [ default_table_compression ] [ default_index_compression ]
        [ inmemory_clause ] [ ilm_clause ] [ storage_clause ]
```

default\_temp\_tablespace

```
[ BIGFILE | SMALLFILE ] DEFAULT
{ { TEMPORARY TABLESPACE }
| { LOCAL TEMPORARY TABLESPACE FOR { ALL | LEAF } }
} tablespace
[ TEMPFILE file_specification [, file_specification ]...]
[ extent_management_clause ]
```

deferred\_segment\_creation

```
SEGMENT CREATION { IMMEDIATE | DEFERRED }
```

delete\_secret

```
DELETE SECRET FOR CLIENT 'client_identifier'
  [ FORCE KEYSTORE ]
  IDENTIFIED BY { EXTERNAL STORE | keystore_password }
   WITH BACKUP [ USING 'backup_identifier' ]
```

delete\_secret\_seps

```
DELETE SECRET FOR CLIENT 'client_identifier'
  FROM [ LOCAL ] AUTO_LOGIN KEYSTORE 'directory'
```

dependent\_tables\_clause

```
DEPENDENT TABLES
( table ( partition_spec [, partition_spec]... 
          [, table ( partition_spec [, partition_spec]... ]
        )
)
```

dim\_by\_clause

```
DIMENSION BY ( dim_key [, dim_key ]... )
```

dim\_key

```
dim_ref 
  [classification_clause]...
  KEY  
    {[(] [alias.] fact_column  [)] 
     |
     (  [alias.] fact_column [, [alias.] fact_column]... )
    }
  REFERENCES 
     {[(]  attribute  [)] 
      | 
      ( attribute [, attribute]... )
     }   
  HIERARCHIES ( hier_ref [, hier_ref]... )
```

dim\_order\_clause

```
attribute [ ASC | DESC ] [ NULLS { FIRST | LAST } ]
```

dim\_ref

```
[ schema. ] attr_dim_name [ [AS] dim__alias ]
```

dimension\_join\_clause

```
{ JOIN KEY
   { child_key_column
   | (child_key_column [, child_key_column ]...)
   }
  REFERENCES parent_level
}...
```

disk\_offline\_clause

```
OFFLINE
  { [ QUORUM | REGULAR ] DISK disk_name [, disk_name ]...
  | DISKS IN [ QUORUM | REGULAR ] FAILGROUP failgroup_name [, failgroup_name ]...
  }... [ timeout_clause ]
```

disk\_online\_clause

```
ONLINE
  { { [ QUORUM | REGULAR ] DISK disk_name [, disk_name ]...
    | DISKS IN [ QUORUM | REGULAR ] FAILGROUP failgroup_name [, failgroup_name ]...
    }...
  | ALL
  } [ POWER integer ] [ WAIT | NOWAIT ]
```

diskgroup\_alias\_clauses

```
{ ADD ALIAS
    'alias_name' FOR 'filename'
    [, 'alias_name' FOR 'filename' ]...
| DROP ALIAS 'alias_name' [, 'alias_name' ]...
| RENAME ALIAS
    'old_alias_name' TO 'new_alias_name'
    [, 'old_alias_name' TO 'new_alias_name' ]...
}
```

diskgroup\_attributes

```
SET ATTRIBUTE 'attribute_name' = 'attribute_value'
```

diskgroup\_availability

```
{ MOUNT [ RESTRICTED | NORMAL ] 
           [ FORCE | NOFORCE ]
| DISMOUNT [ FORCE | NOFORCE ]
}
```

diskgroup\_directory\_clauses

```
{ ADD DIRECTORY 'filename' [, 'filename' ]...
| DROP DIRECTORY
    'filename' [ FORCE | NOFORCE ]
    [, 'filename' [ FORCE | NOFORCE ] ]...
| RENAME DIRECTORY
    'old_dir_name' TO 'new_dir_name'
    [, 'old_dir_name' TO 'new_dir_name' ]...
}
```

diskgroup\_template\_clauses

```
{ { ADD | MODIFY } TEMPLATE template_name qualified_template_clause
      [, template_name qualified_template_clause ]...
| DROP TEMPLATE template_name [, template_name ]...
}
```

diskgroup\_volume\_clauses

```
{ add_volume_clause
| modify_volume_clause
| RESIZE VOLUME asm_volume SIZE size_clause
| DROP VOLUME asm_volume
}
```

distributed\_recov\_clauses

```
{ ENABLE | DISABLE } DISTRIBUTED RECOVERY
```

dml\_table\_expression\_clause

```
{ [ schema. ]
  { table
    [ partition_extension_clause
    | @ dblink
    ]
  | { view | materialized view } [ @ dblink ]
  }
| ( subquery [ subquery_restriction_clause ] )
| table_collection_expression
}
```

domain\_index\_clause

```
indextype
   [ local_domain_index_clause ]
   [ parallel_clause ]
   [ PARAMETERS ('ODCI_parameters') ]
```

drop\_binding\_clause

```
DROP BINDING (parameter_type [, parameter_type ]...)
  [ FORCE ]
```

drop\_column\_clause

```
{ SET UNUSED { COLUMN column
             | (column [, column ]...)
             }
  [ { CASCADE CONSTRAINTS | INVALIDATE }... ]
  [ ONLINE ]
| DROP { COLUMN column
       | (column [, column ]...)
       }
  [ { CASCADE CONSTRAINTS | INVALIDATE }... ]
  [ CHECKPOINT [ integer ] ]
| DROP { UNUSED COLUMNS
       | COLUMNS CONTINUE
       }
  [ CHECKPOINT [ integer ] ]
}
```

drop\_constraint\_clause

```
DROP
   { { PRIMARY KEY
     | UNIQUE (column [, column ]...)
     }
     [ CASCADE ]
     [ { KEEP | DROP } INDEX ]
   | CONSTRAINT constraint_name
     [ CASCADE ]
   } [ ONLINE ]
```

drop\_disk\_clause

```
DROP
{ [ QUORUM | REGULAR ] DISK
    disk_name [ FORCE | NOFORCE ]
    [, disk_name [ FORCE | NOFORCE ] ]...
| DISKS IN [ QUORUM | REGULAR ] FAILGROUP
    failgroup_name [ FORCE | NOFORCE ]
    [, failgroup_name [ FORCE | NOFORCE ] ]...
}
```

drop\_diskgroup\_file\_clause

```
DROP FILE 'filename' [, 'filename' ]...
```

drop\_external\_partition\_attrs

```
DROP EXTERNAL PARTITION ATTRIBUTES
```

drop\_filegroup\_clause

```
DROP FILEGROUP filegroup_name [ CASCADE ]
```

drop\_index\_partition

```
DROP PARTITION partition_name
```

drop\_logfile\_clauses

```
DROP [ STANDBY ] LOGFILE
   { logfile_descriptor
     [, logfile_descriptor ]...
   | MEMBER 'filename'
            [, 'filename' ]...
   }
```

drop\_mirror\_copy

```
DROP MIRROR COPY mirror_name
```

drop\_period\_clause

```
DROP ( PERIOD FOR valid_time_column )
```

drop\_table\_partition

```
DROP partition_extended_names
  [ update_index_clauses [ parallel_clause ] ]
```

drop\_table\_subpartition

```
DROP subpartition_extended_names
  [ update_index_clauses [ parallel_clause ] ]
```

ds\_iso\_format

```
[-] P [days D]
  [T [hours H] [minutes M] [seconds [. frac_secs] S ] ]
```

dynamic\_base\_profile

```
INCLUDING base_profile
```

else\_clause

```
ELSE else_expr
```

enable\_disable\_clause

```
{ ENABLE | DISABLE }
[ VALIDATE | NOVALIDATE ]
{ UNIQUE (column [, column ]...)
| PRIMARY KEY
| CONSTRAINT constraint_name
}
[ using_index_clause ]
[ exceptions_clause ]
[ CASCADE ]
[ { KEEP | DROP } INDEX ]
```

enable\_disable\_volume

```
{ ENABLE | DISABLE } VOLUME
  { asm_volume [, asm_volume]...
  | ALL
  }
```

enable\_pluggable\_database

```
ENABLE PLUGGABLE DATABASE
  [ SEED
    [ file_name_convert ]
    [ SYSTEM tablespace_datafile_clauses ]
    [ SYSAUX tablespace_datafile_clauses ]
  ]
  [ undo_mode_clause ]
```

encryption\_spec

```
[ USING 'encrypt_algorithm' ]
[ IDENTIFIED BY password ]
[ 'integrity_algorithm' ]
[ [ NO ] SALT ]
```

end\_session\_clauses

```
{ DISCONNECT SESSION 'integer1, integer2'
     [ POST_TRANSACTION ]
| KILL SESSION 'integer1, integer2 [, @integer3]'
}
[ IMMEDIATE | NOREPLAY ]
```

entry

```
( regular_entry [ format_clause ] ) | wildcard
```

error\_logging\_clause

```
LOG ERRORS 
  [ INTO [schema.] table ]
  [ (simple_expression) ]
  [ REJECT LIMIT { integer | UNLIMITED } ]
```

evaluation\_edition\_clause

```
EVALUATE USING { CURRENT EDITION | EDITION edition | NULL EDITION }
```

exceptions\_clause

```
EXCEPTIONS INTO [ schema. ] table
```

exchange\_partition\_subpart

```
EXCHANGE { partition_extended_name
         | subpartition_extended_name
         }
   WITH TABLE [ schema. ] table
   [ { INCLUDING | EXCLUDING } INDEXES ]
   [ { WITH | WITHOUT } VALIDATION ]
   [ exceptions_clause ]
   [ update_index_clauses [ parallel_clause ] ]
   [ CASCADE ]
```

export\_keys

```
EXPORT [ ENCRYPTION ] KEYS WITH SECRET secret
  TO 'filename'
  [ FORCE KEYSTORE ]
  IDENTIFIED BY keystore_password
  [ WITH IDENTIFIER IN { 'key_id' [, 'key_id' ]... | ( subquery ) } ]
```

expr

```
{ simple_expression
| compound_expression
| calc_meas_expression
| case_expression
| cursor_expression
| datetime_expression
| function_expression
| interval_expression
| JSON_object_access_expr
| model_expression
| object_access_expression
| scalar_subquery_expression
| type_constructor_expression
| variable_expression
}
```

expression\_list

```
{ expr [, expr ]...
| ( [expr [, expr ]] ...)
}
```

extended\_attribute\_clause

```
ATTRIBUTE attribute
  { LEVEL level
    DETERMINES { dependent_column
               | (dependent_column [, dependent_column ]... )
               }
  }...
```

extent\_management\_clause

```
EXTENT MANAGEMENT LOCAL
  [ AUTOALLOCATE
  | UNIFORM [ SIZE size_clause ]
  ]
```

external\_part\_subpart\_data\_props

```
[ DEFAULT DIRECTORY directory ]
[ LOCATION
   ([ directory: ] 'location_specifier'
      [, [ directory: ] 'location_specifier' ]...
   )
]
```

external\_table\_clause

```
([ TYPE access_driver_type ]
 [ external_table_data_props ]
)
[ REJECT LIMIT { integer | UNLIMITED } ]
[ inmemory_table_clause ]
```

external\_table\_data\_props

```
[ DEFAULT DIRECTORY directory ]
[ ACCESS PARAMETERS
  { ('opaque_format_spec')
  | ( opaque_format_spec )
  | USING CLOB subquery
  }
]
[ LOCATION
   ([ directory: ] 'location_specifier'
      [, [ directory: ] 'location_specifier' ]...
   )
]
```

fact\_columns\_clause

```
FACT COLUMNS ( fact_column [ ( [ AS ] fact_alias )... ] )
```

failover\_clause

```
FAILOVER TO target_db_name [ FORCE ]
```

file\_name\_convert

```
FILE_NAME_CONVERT =
  { ( 'filename_pattern', 'replacement_filename_pattern'
      [, 'filename_pattern', 'replacement_filename_pattern' ]... )
    |
    NONE
  }
```

file\_owner\_clause

```
SET OWNERSHIP { OWNER = 'user' | GROUP = 'usergroup' 
                  [, OWNER = 'user' | GROUP = 'usergroup' ]...
              } FOR FILE 'filename' [, 'filename']...
```

file\_permissions\_clause

```
SET PERMISSION { OWNER | GROUP | OTHER }
  = { NONE | READ ONLY | READ WRITE }
  [, { OWNER | GROUP | OTHER | ALL }
    = { NONE | READ ONLY | READ WRITE } ]...
    FOR FILE 'filename' [, 'filename']...
```

file\_specification

```
{ datafile_tempfile_spec
| redo_log_file_spec
}
```

filegroup\_clauses

```
{ add_filegroup_clause
| modify_filegroup_clause
| move_to_filegroup_clause
| drop_filegroup_clause
}
```

filter\_clause

```
hier_ids TO predicate
```

filter\_clauses

```
FILTER FACT ( filter_clause ...)
```

filter\_condition

```
INCLUDING ROWS where_clause
```

flashback\_archive\_clause

```
FLASHBACK ARCHIVE [flashback_archive] | NO FLASHBACK ARCHIVE
```

flashback\_archive\_quota

```
QUOTA integer { M | G | T | P | E }
```

flashback\_archive\_retention

```
RETENTION integer {YEAR | MONTH | DAY}
```

flashback\_mode\_clause

```
FLASHBACK { ON | OFF }
```

flashback\_query\_clause

```
{ VERSIONS BETWEEN { SCN | TIMESTAMP }
    { expr | MINVALUE } AND { expr | MAXVALUE }
| VERSIONS PERIOD FOR valid_time_column BETWEEN
    { expr | MINVALUE } AND { expr | MAXVALUE }
| AS OF { SCN | TIMESTAMP } expr
| AS OF PERIOD FOR valid_time_column expr
}
```

following\_boundary

```
{ CURRENT MEMBER | offset_expr FOLLOWING }
AND
{ offset_expr FOLLOWING | UNBOUNDED FOLLOWING }
```

for\_refresh\_clause

```
{ FOR SYNCHRONOUS REFRESH USING staging_log_name
| FOR FAST REFRESH
}
```

for\_update\_clause

```
FOR UPDATE
  [ OF [ [ schema. ] { table | view } . ] column
         [, [ [ schema. ] { table | view } . ] column
         ]...
  ]
  [ { NOWAIT | WAIT integer 
    |  SKIP LOCKED
    }
  ]
```

format\_clause

```
FORMAT JSON
```

full\_database\_recovery

```
[ STANDBY ] DATABASE
[ { UNTIL { CANCEL
          | TIME date
          | CHANGE integer
          | CONSISTENT
          }
  | USING BACKUP CONTROLFILE
  | SNAPSHOT TIME date
  }...
]
```

fully\_qualified\_file\_name

```
+diskgroup_name/db_name/file_type/
   file_type_tag.filenumber.incarnation_number
```

function\_association

```
{ FUNCTIONS
     [ schema. ]function [, [ schema. ]function ]...
| PACKAGES
     [ schema. ]package [, [ schema. ]package ]...
| TYPES
     [ schema. ]type [, [ schema. ]type ]...
| INDEXES
     [ schema. ]index [, [ schema. ]index ]...
| INDEXTYPES
     [ schema. ]indextype [, [ schema. ]indextype ]...
}
{ using_statistics_type
| { default_cost_clause [, default_selectivity_clause ]
  | default_selectivity_clause [, default_cost_clause ]
  }
}
```

general\_recovery

```
RECOVER
[ AUTOMATIC ]
[ FROM 'location' ]
{ { full_database_recovery
  | partial_database_recovery
  | LOGFILE 'filename'
  }
  [ { TEST
    | ALLOW integer CORRUPTION
    | parallel_clause
    }...
  ]
| CONTINUE [ DEFAULT ]
| CANCEL
}
```

global\_partitioned\_index

```
GLOBAL PARTITION BY
   { RANGE (column_list)
        (index_partitioning_clause)
   | HASH (column_list)
        { individual_hash_partitions
        | hash_partitions_by_quantity
        }
   }
```

grant\_object\_privileges

```
{ object_privilege | ALL [ PRIVILEGES ] }
  [ (column [, column ]...) ]
    [, { object_privilege | ALL [ PRIVILEGES ] }
       [ (column [, column ]...) ]
    ]...
on_object_clause
TO grantee_clause
  [ WITH HIERARCHY OPTION ]
  [ WITH GRANT OPTION ]
```

grant\_roles\_to\_programs

```
role [, role ]... TO program_unit [, program_unit ]...
```

grant\_system\_privileges

```
{ system_privilege | role | ALL PRIVILEGES }
  [, { system_privilege | role | ALL PRIVILEGES } ]...
TO { grantee_clause | grantee_identified_by } [ WITH { ADMIN | DELEGATE } OPTION ]
```

grantee\_clause

```
{ user | role | PUBLIC }
  [, { user | role | PUBLIC } ]...
```

grantee\_identified\_by

```
user [, user ]... IDENTIFIED BY password [, password ]...
```

group\_by\_clause

```
GROUP BY
   { expr
   | rollup_cube_clause
   | grouping_sets_clause
   }
     [, { expr
        | rollup_cube_clause
        | grouping_sets_clause
        }
     ]...
   [ HAVING condition ]
```

grouping\_expression\_list

```
expression_list [, expression_list ]...
```

grouping\_sets\_clause

```
GROUPING SETS
({ rollup_cube_clause | grouping_expression_list })
```

hash\_partitions

```
PARTITION BY HASH (column [, column ] ...)
{ individual_hash_partitions
| hash_partitions_by_quantity
}
```

hash\_partitions\_by\_quantity

```
PARTITIONS hash_partition_quantity
[ STORE IN (tablespace [, tablespace ]...) ]
[ table_compression | index_compression ]
[ OVERFLOW STORE IN (tablespace [, tablespace ]...) ]
```

hash\_subparts\_by\_quantity

```
SUBPARTITIONS integer [STORE IN ( tablespace [, tablespace]... )]
```

heap\_org\_table\_clause

```
[ table_compression ] [ inmemory_table_clause ] [ ilm_clause ]
```

hier\_ancestor\_expression

```
HIER_ANCESTOR ( member_expression AT 
                       {   LEVEL level_ref
                         | DEPTH depth_expression
                       }
                     )
```

hier\_attr\_clause

```
hier_attr_name [ classification_clause ]...
```

hier\_attr\_name

```
{   MEMBER_NAME
  | MEMBER_UNIQUE_NAME
  | MEMBER_CAPTION
  | MEMBER_DESCRIPTION
  | LEVEL_NAME
  | HIER_ORDER
  | DEPTH
  | IS_LEAF
  | PARENT_LEVEL_NAME
  | PARENT_UNIQUE_NAME
}
```

hier\_attrs\_clause

```
HIERARCHICAL ATTRIBUTES ( hier_attr_clause [, hier_attr_clause ]... )
```

hier\_id

```
MEASURES | ( ( dim_alias.) hier_alias )
```

hier\_ids

```
hier_id [ hier_id ]...
```

hier\_lead\_lag\_clause

```
member_expression  OFFSET offset_expr
  [ WITHIN 
    {  { LEVEL | PARENT }
    | ACROSS ANCESTOR AT LEVEL level_ref [ POSITION FROM { BEGINNING | END } ]
    }
  ]
```

hier\_lead\_lag\_expression

```
{ HIER_LEAD | HIER_LAG } ( hier_lead_lag_clause )
```

hier\_navigation\_expression

```
{
    hier_ancestor_expression
  | hier_parent_expression
  | hier_lead_lag_expression
}
```

hier\_parent\_expression

```
HIER_PARENT ( member_expression )
```

hier\_ref

```
[ schema. ] hier_name [ [ AS ] hier_alias ] [ DEFAULT ]
```

hier\_using\_clause

```
USING [ schema. ] attribute_dimension level_hier_clause
```

hierarchical\_query\_clause

```
{ CONNECT BY [ NOCYCLE ] condition [ START WITH condition ]
| START WITH condition CONNECT BY [ NOCYCLE ] condition
}
```

hierarchy\_clause

```
HIERARCHY hierarchy
(child_level { CHILD OF parent_level }...
  [ dimension_join_clause ]
)
```

hierarchy\_ref

```
[ attr_dim_alias. ] hier_alias
```

identity\_clause

```
GENERATED
[ ALWAYS | BY DEFAULT [ ON NULL ] ]
AS IDENTITY [ ( identity_options ) ]
```

identity\_options

```
{ START WITH ( integer | LIMIT VALUE )
| INCREMENT BY integer
| ( MAXVALUE integer | NOMAXVALUE )
| ( MINVALUE integer | NOMINVALUE )
| ( CYCLE | NOCYCLE )
| ( CACHE integer | NOCACHE )
| ( ORDER | NOORDER ) }...
```

ilm\_clause

```
ILM
{ ADD POLICY ilm_policy_clause
| { DELETE | ENABLE | DISABLE } POLICY ilm_policy_name
| DELETE_ALL | ENABLE_ALL | DISABLE_ALL
}
```

ilm\_compression\_policy

```
{ table_compression { SEGMENT | GROUP } 
  { { AFTER ilm_time_period OF { { NO ACCESS } | { NO MODIFICATION } | CREATION } }
  | { ON function_name } }
}
|
{ { ROW STORE COMPRESS ADVANCED
  | COLUMN STORE COMPRESS FOR QUERY
  }
  ROW AFTER ilm_time_period OF NO MODIFICATION
}
```

ilm\_inmemory\_policy

```
{ SET INMEMORY [ inmemory_attributes ]
| MODIFY INMEMORY inmemory_memcompress
| NO INMEMORY
}
[ SEGMENT ]
{ AFTER ilm_time_period OF { NO ACCESS | NO MODIFICATION | CREATION }
        | ON function_name
        }
```

ilm\_policy\_clause

```
{ ilm_compression_policy | ilm_tiering_policy | ilm_inmemory_policy }
```

ilm\_tiering\_policy

```
{ TIER TO tablespace [ SEGMENT | GROUP ] [ ON function_name ] }
|
{ TIER TO tablespace READ ONLY [ SEGMENT | GROUP ]
  { { AFTER ilm_time_period OF { { NO ACCESS } | { NO MODIFICATION } | CREATION } }
  | { ON function_name } } }
```

ilm\_time\_period

```
integer { { DAY | DAYS } | { MONTH | MONTHS } | { YEAR | YEARS } }
```

implementation\_clause

```
{ ANCILLARY TO primary_operator
    ( parameter_type [, parameter_type ]...)
      [, primary_operator
         ( parameter_type [, parameter_type ]...)
      ]...
| context_clause
}
```

immutable\_table\_clauses

```
immutable_table_no_drop_clause immutable_table_no_delete_clause
```

immutable\_table\_no\_delete\_clause

```
NO DELETE ( [ LOCKED ] | ( UNTIL integer DAYS AFTER INSERT [LOCKED] ) )
```

immutable\_table\_no\_drop\_clause

```
NO DROP ( [ LOCKED ] | ( UNTIL integer DAYS AFTER INSERT [LOCKED] ) )
```

import\_keys

```
IMPORT [ ENCRYPTION ] KEYS WITH SECRET secret
  FROM 'filename'
  [ FORCE KEYSTORE ]
  IDENTIFIED BY keystore_password
  WITH BACKUP [ USING 'backup_identifier' ]
```

incomplete\_file\_name

```
+diskgroup_name [ (template_name) ]
```

index\_attributes

```
[ { physical_attributes_clause
  | logging_clause
  | ONLINE
  | TABLESPACE { tablespace | DEFAULT }
  | index_compression
  | { SORT | NOSORT }
  | REVERSE
  | VISIBLE | INVISIBLE
  | partial_index_clause
  | parallel_clause
  }...
]
```

index\_compression

```
{ prefix_compression
| advanced_index_compression
}
```

index\_expr

```
{ column | column_expression }
```

index\_ilm\_clause

```
ILM  
    (
      [  ADD  POLICY | ( DELETE POLICY  policy_name ) ]
         policy_clause  
    )
```

index\_org\_overflow\_clause

```
[ INCLUDING column_name ]
OVERFLOW [ segment_attributes_clause ]
```

index\_org\_table\_clause

```
[ { mapping_table_clause
  | PCTTHRESHOLD integer
  | prefix_compression
  }...
]
[ index_org_overflow_clause ]
```

index\_partition\_description

```
PARTITION
[ partition
   [ { segment_attributes_clause
     | index_compression
     }...
   | PARAMETERS ( 'ODCI_parameters' )
   ]
   [ USABLE | UNUSABLE ]
]
```

index\_partitioning\_clause

```
PARTITION [ partition ]
   VALUES LESS THAN (literal[, literal]... )
   [ segment_attributes_clause ]
```

index\_properties

```
[ { { global_partitioned_index
    | local_partitioned_index
    }
  | index_attributes
  }...
| INDEXTYPE IS { domain_index_clause
               | XMLIndex_clause
               }
]
```

index\_subpartition\_clause

```
{ STORE IN (tablespace[, tablespace ]...)
| (SUBPARTITION
      [ subpartition ][ TABLESPACE tablespace ] [ index_compression ] [ USABLE | UNUSABLE ]
   [, SUBPARTITION
         [ subpartition ][ TABLESPACE tablespace ] [ index_compression ] [ USABLE | UNUSABLE ]
   ]...
  )
}
```

indexing\_clause

```
INDEXING { ON | OFF }
```

individual\_hash\_partitions

```
( PARTITION [partition] [read_only_clause] [indexing_clause] [partitioning_storage_clause]
  [, PARTITION [partition] [read_only_clause] [indexing_clause] [partitioning_storage_clause]]... )
```

individual\_hash\_subparts

```
SUBPARTITION [subpartition] [read_only_clause] [indexing_clause] [partitioning_storage_clause]
```

inline\_constraint

```
[ CONSTRAINT constraint_name ]
{ [ NOT ] NULL
| UNIQUE
| PRIMARY KEY
| references_clause
| CHECK (condition)
}
[ constraint_state ]
```

inline\_external\_table

```
EXTERNAL '(' '(' column_definition ',' ')' inline_external_table_properties ')'
```

inline\_external\_table\_properties

```
TYPE [ access_driver_type ] external_table_data_props 
 [ REJECT LIMIT { integer | UNLIMITED }
```

inline\_ref\_constraint

```
{ SCOPE  IS [ schema. ] scope_table
| WITH ROWID
| [ CONSTRAINT constraint_name ]
  references_clause
  [ constraint_state ]
}
```

inmemory\_attributes

```
[ inmemory_memcompress ] [ inmemory_priority ] [ inmemory_distribute ] [ inmemory_duplicate ]
```

inmemory\_clause

```
( INMEMORY [ inmemory_attributes ] [TEXT ( ( "column_name")/"," 
           | ("column_name" USING "policy_name")/"," ) ] )
| NO INMEMORY
```

inmemory\_column\_clause

```
{ INMEMORY [ inmemory_memcompress ] | NO INMEMORY } ( column [, column ]... )
 [ { INMEMORY [ inmemory_memcompress ] | NO INMEMORY } ( column [, column ]... ) ]...
```

inmemory\_distribute

```
DISTRIBUTE [ AUTO | BY { ROWID RANGE | PARTITION | SUBPARTITION } ]
           [ FOR SERVICE { DEFAULT | ALL | service_name | NONE } ]
```

inmemory\_duplicate

```
DUPLICATE | DUPLICATE ALL | NO DUPLICATE
```

inmemory\_memcompress

```
MEMCOMPRESS FOR { DML | QUERY [ LOW | HIGH ] | CAPACITY [ LOW | HIGH ] }
| NO MEMCOMPRESS
| MEMCOMPRESS AUTO
```

inmemory\_priority

```
PRIORITY { NONE | LOW | MEDIUM | HIGH | CRITICAL }
```

inmemory\_table\_clause

```
[ { INMEMORY [ inmemory_attributes ] } | { NO INMEMORY } ]
[ inmemory_column_clause ]
```

inner\_cross\_join\_clause

```
{ [ INNER ] JOIN table_reference
    { ON condition
    | USING (column [, column ]...)
    }
| { CROSS
  | NATURAL [ INNER ]
  }
  JOIN table_reference
}
```

insert\_into\_clause

```
INTO dml_table_expression_clause [ t_alias ]
[ (column [, column ]...) ]
```

insert\_op

```
INSERT pathExpr "=" rhsExpr [ { REPLACE | IGNORE | ERROR } ON EXISTING ] 
            [ { NULL | IGNORE | ERROR | REMOVE } ON NULL ]
```

instance\_clauses

```
{ ENABLE | DISABLE } INSTANCE 'instance_name'
```

instances\_clause

```
INSTANCES = { ( 'instance_name' [, 'instance_name' ]... )
            | ALL [ EXCEPT ( 'instance_name' [, 'instance_name' ]... ) ] }
```

integer

```
[ + | - ] digit [ digit ]...
```

interval\_day\_to\_second

```
INTERVAL '{ integer | integer time_expr | time_expr }'
{ { DAY | HOUR | MINUTE } [ (leading_precision) ]
| SECOND [ (leading_precision [, fractional_seconds_precision ]) ]
}
[ TO { DAY | HOUR | MINUTE | SECOND [ (fractional_seconds_precision) ] } ]
```

interval\_year\_to\_month

```
INTERVAL 'integer [- integer ]'
{ YEAR | MONTH } [ (precision) ] [ TO { YEAR | MONTH } ]
```

into\_clause

```
INTO [ schema. ] table
```

invoker\_rights\_clause

```
AUTHID { CURRENT_USER | DEFINER }
```

isolate\_keystore

```
[ FORCE ]ISOLATE KEYSTORE INDENTIFIED BY isolated_keystore_password
FROM ROOT KEYSTORE 
[ FORCE KEYSTORE ] IDENTIFIED BY { EXTERNAL STORE | united_keystore_password }
WITH BACKUP [ USING 'backup_identifier' ]
```

join\_clause

```
table_reference
  { inner_cross_join_clause | outer_join_clause | cross_outer_apply_clause }...
```

join\_path\_clause

```
JOIN PATH join_path_name ON join_condition
```

JSON\_ARRAY\_content

```
( , [ JSON_ARRAY_element ] ... )
[ JSON_on_null_clause ] [ JSON_returning_clause ]
[ STRICT ]
```

JSON\_ARRAY\_element

```
expr [ format_clause ]
```

JSON\_column\_definition

```
JSON_exists_column
| JSON_query_column
| JSON_value_column
| JSON_nested_path
| ordinality_column
```

JSON\_columns\_clause

```
COLUMNS ( JSON_column_definition TRUNCATE [ , JSON_column_definition ]... )
```

JSON\_exists\_column

```
column_name [ JSON_value_return_type ]  
EXISTS [ PATH ] [ JSON_path ] [ JSON_exists_on_error_clause ]
[ JSON_exists_on_empty_clause ]
```

JSON\_exists\_on\_empty\_clause

```
{ ERROR | TRUE | FALSE } ON EMPTY
```

JSON\_exists\_on\_error\_clause

```
{ ERROR | TRUE | FALSE } ON ERROR
```

JSON\_nested\_path

```
NESTED [ PATH ] JSON_path  JSON_columns_clause
```

JSON\_object\_content

```
( "*" | [ entry ] ... )
    [ JSON_on_null_clause ] [ JSON_returning_clause ]
    [ STRICT ]
    [ WITH UNIQUE KEYS ]
```

JSON\_on\_null\_clause

```
{ NULL | ABSENT } ON NULL
```

JSON\_parameters

```
( TABLESPACE tablespace 
| storage_clause 
| ( (CHUNK | PCTVERSION | FREEPOOLS) integer )
| RETENTION 
) ...
```

JSON\_passing\_clause

```
PASSING expr AS identifier [, expr AS identifier ]...
```

JSON\_path

```
JSON_basic_path_expression | JSON_relative_object_access
```

JSON\_query\_column

```
column_name JSON_query_return_type FORMAT JSON 
  [ (ALLOW | DISALLOW) SCALARS ] [ JSON_query_wrapper_clause ]
  PATH JSON_path [ JSON_query_on_error_clause ]
```

JSON\_query\_on\_empty\_clause

```
{ ERROR
| NULL
| EMPTY
| EMPTY ARRAY
| EMPTY OBJECT
} ON EMPTY
```

JSON\_query\_on\_error\_clause

```
{ ERROR
| NULL
| EMPTY
| EMPTY ARRAY
| EMPTY OBJECT
} ON ERROR
```

JSON\_query\_on\_mismatch\_clause

```
( ERROR | NULL ) ON MISMATCH
```

JSON\_query\_return\_type

```
VARCHAR2 [ ( size [BYTE | CHAR] ) ]
| CLOB
| BLOB
| JSON
```

JSON\_query\_returning\_clause

```
[ RETURNING JSON_query_return_type ][ (ALLOW | DISALLOW) SCALARS ] 
[ PRETTY ] [ ASCII ]
```

JSON\_query\_wrapper\_clause

```
WITHOUT [ ARRAY ] WRAPPER
| WITH [ UNCONDITIONAL | CONDITIONAL ] [ ARRAY ] WRAPPER
```

JSON\_relative\_object\_access

```
JSON_object_key [ array_step ] 
 ( "." JSON_object_key [ array_step ] )...
```

JSON\_returning\_clause

```
RETURNING VARCHAR2 [ ( size [BYTE | CHAR] ) ] 
[ WITH TYPENAME ] | CLOB | BLOB | JSON
```

JSON\_storage\_clause

```
JSON ( json_column … ) STORE AS 
( ( ( json_parameters )
   | [ LOB_segname ] [ ( json_parameters )]
  ) )
```

JSON\_table\_on\_empty\_clause

```
{ ERROR | NULL | DEFAULT literal } ON EMPTY
```

JSON\_table\_on\_error\_clause

```
{ ERROR | NULL | DEFAULT literal } ON ERROR
```

JSON\_transform\_returning\_clause

```
RETURNING VARCHAR2 [ ( size [BYTE | CHAR] ) ] 
[ WITH TYPENAME ] | CLOB | BLOB | JSON 
[ ALLOW | DISALLOW ]
```

JSON\_value\_column

```
column_name [ JSON_value_return_type ] [ TRUNCATE ] 
  [ PATH ] [ JSON_path ] [ JSON_value_on_error_clause ]
  [ JSON_value_on_empty_clause ]
  [ JSON_value_on_mismatch_clause ]
```

JSON\_value\_mapper\_clause

```
USING CASE-SENSITIVE MAPPING
```

JSON\_value\_on\_empty\_clause

```
{ ERROR | NULL | DEFAULT literal } ON EMPTY
```

JSON\_value\_on\_error\_clause

```
{ ERROR | NULL | DEFAULT literal } ON ERROR
```

JSON\_value\_on\_mismatch\_clause

```
JSON_value_on_mismatch ( 
   ( IGNORE | ERROR | NULL ) 
    ON MISMATCH 
   [ (  (MISSING DATA) | (EXTRA DATA) | (TYPE ERROR)  ) ]
  ) ...
```

JSON\_value\_return\_object\_instance

```
object_type_name [ JSON_value_mapper_clause ]
```

JSON\_value\_return\_type

```
{ VARCHAR2 [ ( size [BYTE | CHAR] ) TRUNCATE ]
| CLOB
| NUMBER [ ( precision [, scale] ) ]
| DATE
| TIMESTAMP
| TIMESTAMP WITH TIME ZONE
| SDO_GEOMETRY
| JSON_value_return_object_instance
 }
```

JSON\_value\_returning\_clause

```
RETURNING JSON_value_return_type  [ ASCII ]
```

key\_clause

```
KEY { [(] attribute [)] | ( attribute [, attribute]... ) }
```

keep\_op

```
KEEP ( pathExpr [ { IGNORE | ERROR } ON MISSING ] )...
```

key\_management\_clauses

```
{ set_key
| create_key
| use_key
| set_key_tag
| export_keys
| import_keys
| migrate_key
| reverse_migrate_key
| move_keys
}
```

keystore\_clause

```
KEYSTORE IDENTIFIED BY 
   { EXTERNAL STORE | keystore_password } 
   [ NO REKEY ]
```

keystore\_management\_clauses

```
{ create_keystore
| open_keystore
| close_keystore
| backup_keystore
| alter_keystore_password
| merge_into_new_keystore
| merge_into_existing_keystore
| isolate_keystore
| unite_keystore
}
```

lead\_lag\_clause

```
HIERARCHY hierarchy_ref OFFSET offset_expr
  [ { 
      WITHIN { LEVEL | PARENT }
    | ACROSS ANCESTOR AT LEVEL level_ref [ POSITION FROM { BEGINNING | END }
    }  
  ]
```

lead\_lag\_expression

```
lead_lag_function_name ( calc_meas_expression ) OVER ( lead_lag_clause )
```

lead\_lag\_function\_name

```
{ LAG | LAG_DIFF | LAG_DIFF_PERCENT | LEAD | LEAD_DIFF | LEAD_DIFF_PERCENT }
```

level\_clause

```
LEVEL level IS
   { level_table.level_column
   | (level_table.level_column
      [, level_table.level_column ]...
     )
   } [ SKIP WHEN NULL ]
```

level\_group\_type

```
DYNAMIC | MATERIALIZED [ USING [ schema.] table ]
```

level\_hier\_clause

```
( level [ CHILD  OF level ]... )
```

level\_member\_literal

```
level_ref { pos_member_keys | named_member_keys }
```

level\_specification

```
( [ [ dim_name. ] hier_name. ] level_name )
```

levels\_clause

```
LEVELS ([ level_specification ]...) level_group_type
```

list\_partition\_desc

```
PARTITION [partition]
list_values_clause
table_partition_description
  [ ( range_subpartition_desc [, range_subpartition_desc]...
      | list_subpartition_desc, [, list_subpartition_desc]...
      | individual_hash_subparts [, individual_hash_subparts]...
    )
    | hash_subparts_by_quantity
  ]
```

list\_partitions

```
PARTITION BY LIST ( column [, column]... )
[ AUTOMATIC [ STORE IN ( tablespace [, tablespace ]... ) ] ]
(PARTITION [ partition ]
    list_values_clause table_partition_description
  [, PARTITION [ partition ]
        list_values_clause table_partition_description
        [ external_part_subpart_data_props ]
  ]...
)
```

list\_partitionset\_clause

```
PARTITIONSET BY LIST (column)
  PARTITION BY CONSISTENT HASH (column [, column]...)
  [ SUBPARTITION BY { { RANGE | HASH } (column [, column]...)
                    | LIST (column)
                    }
  [ subpartition_template ]
  ]
  PARTITIONS AUTO ( list_partitionset_desc [, list_partitionset_desc]... )
```

list\_partitionset\_desc

```
PARTITIONSET partition_set list_values_clause
  [ TABLESPACE SET tablespace_set ]
  [ LOB_storage_clause ]
  [ SUBPARTITIONS STORE IN ( tablespace_set … ) ]
```

list\_subpartition\_desc

```
SUBPARTITION [subpartition] list_values_clause
  [read_only_clause] [indexing_clause] [partitioning_storage_clause]
  [external_part_subpart_data_props]
```

list\_values

```
list_values
{ { literal | NULL } [, { literal | NULL } ]... }
| { ( { literal | NULL } [, { literal | NULL } ]... )
        [, ( { literal | NULL } [, { literal | NULL } ]... ) ] }
```

list\_values\_clause

```
VALUES ( list_values | DEFAULT )
```

listagg\_overflow\_clause

```
{ ON OVERFLOW ERROR }
|
{ ON OVERFLOW TRUNCATE 'truncation-indicator' [ { WITH | WITHOUT } COUNT ] }
```

LOB\_compression\_clause

```
{ COMPRESS [HIGH | MEDIUM | LOW ]
| NOCOMPRESS
}
```

LOB\_deduplicate\_clause

```
{ DEDUPLICATE   
| KEEP_DUPLICATES
}
```

LOB\_parameters

```
{ { ENABLE | DISABLE } STORAGE IN ROW
  | CHUNK integer
  | PCTVERSION integer
  | FREEPOOLS integer
  | LOB_retention_clause
  | LOB_deduplicate_clause
  | LOB_compression_clause
  | { ENCRYPT encryption_spec | DECRYPT }
  | { CACHE | NOCACHE | CACHE READS } [ logging_clause ] 
}...
```

LOB\_partition\_storage

```
PARTITION partition
{ LOB_storage_clause | varray_col_properties }...
  [ (SUBPARTITION subpartition
     { LOB_partitioning_storage | varray_col_properties }...
    )
]
```

LOB\_partitioning\_storage

```
LOB (LOB_item) STORE AS [BASICFILE | SECUREFILE]
  [ LOB_segname [ ( TABLESPACE tablespace | TABLESPACE SET tablespace_set ) ]
  | ( TABLESPACE tablespace | TABLESPACE SET tablespace_set )
  ]
```

LOB\_retention\_storage

```
RETENTION [ MAX | MIN integer | AUTO | NONE ]
```

LOB\_storage\_clause

```
LOB
{ (LOB_item [, LOB_item ]...)
     STORE AS { {SECUREFILE | BASICFILE}
              | (LOB_storage_parameters)
              }...
| (LOB_item)
     STORE AS { {SECUREFILE | BASICFILE}
              | LOB_segname 
              | (LOB_storage_parameters)
              }...
}
```

LOB\_storage\_parameters

```
{ { { TABLESPACE tablespace | TABLESPACE SET tablespace_set }
  | LOB_parameters [storage_clause]
  }...
| storage_clause
```

local\_domain\_index\_clause

```
LOCAL
  [ ( PARTITION partition [ PARAMETERS ( 'ODCI_parameters' ) ]
      [,  PARTITION partition [ PARAMETERS ('ODCI_parameters') ]]...
    )
  ]
```

local\_partitioned\_index

```
LOCAL
[ on_range_partitioned_table
| on_list_partitioned_table
| on_hash_partitioned_table
| on_comp_partitioned_table
]
```

local\_XMLIndex\_clause

```
LOCAL
  [ ( PARTITION partition [ XMLIndex_parameters_clause ]
      [, PARTITION partition [ XMLIndex_parameters_clause ] ]...
    )
  ]
```

lockdown\_features

```
{ DISABLE | ENABLE } FEATURE
{ { = ( 'feature' [, 'feature' ]... ) }
| { ALL [ EXCEPT = ( 'feature' [, 'feature' ]... ) ] }
}
```

lockdown\_options

```
{ DISABLE | ENABLE } OPTION
{ { = ( 'option' [, 'option' ]... ) }
| { ALL [ EXCEPT = ( 'option' [, 'option' ]... ) ] }
}
```

lockdown\_statements

```
{ DISABLE | ENABLE } STATEMENT
{ { = ( 'SQL_statement' [, 'SQL_statement' ]... ) }
| { = ( 'SQL_statement' ) statement_clauses }
| { ALL [ EXCEPT = ( 'SQL_statement' [, 'SQL_statement' ]... ) ] }
}
```

logfile\_clause

```
LOGFILE
[ GROUP integer ] file_specification
  [, [ GROUP integer ] file_specification ]...
```

logfile\_clauses

```
{ { ARCHIVELOG [ MANUAL ]
  | NOARCHIVELOG
  }
| [ NO ] FORCE LOGGING
| SET STANDBY NOLOGGING FOR {DATA AVAILABILITY | LOAD PERFORMANCE}
| RENAME FILE 'filename' [, 'filename' ]...
    TO 'filename'
| CLEAR [ UNARCHIVED ]
    LOGFILE logfile_descriptor [, logfile_descriptor ]...
    [ UNRECOVERABLE DATAFILE ]
| add_logfile_clauses
| drop_logfile_clauses
| switch_logfile_clause
| supplemental_db_logging
}
```

logfile\_descriptor

```
{ GROUP integer
| ('filename' [, 'filename' ]...)
| 'filename'
}
```

logical\_replication\_clause

```
(
             DISABLE LOGICAL REPLICATION 
             | ENABLE LOGICAL REPLICATION [ ALL KEYS | ALLOW NOVALIDATE KEYS ] 
            ) 
}
```

logging\_clause

```
{ LOGGING | NOLOGGING |  FILESYSTEM_LIKE_LOGGING }
```

main\_model

```
[ MAIN main_model_name ]
model_column_clauses
[ cell_reference_options ]
model_rules_clause
```

managed\_standby\_recovery

```
RECOVER
{ MANAGED STANDBY DATABASE
    [ { USING ARCHIVED LOGFILE
      | DISCONNECT [FROM SESSION]
      | NODELAY
      | UNTIL CHANGE integer
      | UNTIL CONSISTENT
      | USING INSTANCES { ALL | integer }
      | parallel_clause
      }...
    | FINISH
    | CANCEL
    ]
| TO LOGICAL STANDBY { db_name | KEEP IDENTITY }
}
```

mapping\_table\_clauses

```
{ MAPPING TABLE | NOMAPPING }
```

materialized\_view\_props

```
[ column_properties ]
[ table_partitioning_clauses ]
[ CACHE | NOCACHE ]
[ parallel_clause ]
[ build_clause ]
```

maximize\_standby\_db\_clause

```
SET STANDBY DATABASE TO MAXIMIZE
{ PROTECTION | AVAILABILITY | PERFORMANCE }
```

maxsize\_clause

```
MAXSIZE { UNLIMITED | size_clause }
```

meas\_aggregate\_clause

```
AGGREGATE BY aggr_function
```

measure\_ref

```
[ MEASURES. ] meas_name
```

measures\_clause

```
MEASURES  ( av_measure [, av_measure]... )
```

member\_expression

```
{ level_member_literal
  | hier_navigation_expression
  | CURRENT MEMBER
  | NULL
  | ALL
}
```

memoptimize\_read\_clause

```
[ { (MEMOPTIMIZE FOR READ) | (NO MEMOPTIMIZE FOR READ) } ]
```

memoptimize\_write\_clause

```
[ { (MEMOPTIMIZE FOR WRITE) | (NO MEMOPTIMIZE FOR WRITE) } ]
```

merge\_insert\_clause

```
WHEN NOT MATCHED THEN
INSERT [ (column [, column ]...) ]
VALUES ({ expr | DEFAULT }
           [, { expr | DEFAULT } ]...
       )
[ where_clause ]
```

merge\_into\_existing\_keystore

```
MERGE KEYSTORE 'keystore1_location' [ IDENTIFIED BY keystore1_password ]
  INTO EXISTING KEYSTORE 'keystore2_location' IDENTIFIED BY keystore2_password
  WITH BACKUP [ USING 'backup_identifier' ]
```

merge\_into\_new\_keystore

```
MERGE KEYSTORE 'keystore1_location' [ IDENTIFIED BY keystore1_password ]
  AND KEYSTORE 'keystore2_location' [ IDENTIFIED BY keystore2_password ]
  INTO NEW KEYSTORE 'keystore3_location' IDENTIFIED BY keystore3_password
```

merge\_table\_partitions

```
MERGE PARTITIONS partition_or_key_value
   { , partition_or_key_value [, partition_or_key_value ]...
   | TO partition_or_key_value }
   [ INTO partition_spec ]
   [ filter_condition ]
   [ dependent_tables_clause ]
   [ update_index_clauses ]
   [ parallel_clause ]
   [ ONLINE ]
   [ allow_disallow_clustering ]
```

merge\_table\_subpartitions

```
MERGE SUBPARTITIONS subpartition_or_key_value
   { , subpartition_or_key_value [, subpartition_or_key_value ]...
   | TO subpartition_or_key_value }
   [ INTO { range_subpartition_desc
          | list_subpartition_desc
          }
   ]
   [ filter_condition ]
   [ dependent_tables_clause ]
   [ update_index_clauses ]
   [ parallel_clause ]
   [ ONLINE ]
   [ allow_disallow_clustering ]
```

merge\_update\_clause

```
WHEN MATCHED THEN
UPDATE SET column = { expr | DEFAULT }
           [, column = { expr | DEFAULT } ]...
[ where_clause ]
[ DELETE where_clause ]
```

migrate\_key

```
{ USE | SET } [ ENCRYPTION ] KEY [ 'key_id' ]
  IDENTIFIED BY OKV_password
  [ FORCE KEYSTORE ]
   MIGRATE USING software_keystore_password
```

mining\_analytic\_clause

```
[ query_partition_clause ] [ order_by_clause ]
```

mining\_attribute\_clause

```
USING
{ * 
| { [ schema . ] table . * 
  | expr [ AS alias ]
  }
    [, { [ schema . ] table . * 
       | expr [ AS alias ]
       }
    ]...
}
```

model\_clause

```
MODEL
   [ cell_reference_options ]
   [ return_rows_clause ]
   [ reference_model ]...
main_model
```

model\_column\_clauses

```
[ PARTITION BY (expr [ c_alias ] [, expr [c_alias] ]...) ]
DIMENSION BY (expr [c_alias] [, expr [c_alias] ]...)
MEASURES (expr [c_alias] [, expr [c_alias] ]...)
```

model\_iterate\_clause

```
ITERATE ( number ) [ UNTIL ( condition ) ]
```

model\_rules\_clause

```
[ RULES
  [ { UPDATE | UPSERT [ ALL ] } ]
  [ { AUTOMATIC | SEQUENTIAL } ORDER ]
  [ model_iterate_clause ]
]
( [ { UPDATE | UPSERT [ ALL ] } ]
cell_assignment [ order_by_clause ] = expr
  [,  [ { UPDATE | UPSERT [ ALL ] } ]
    cell_assignment [ order_by_clause ] = expr
  ]...
)
```

modified\_external\_table

```
EXTERNAL MODIFY modify_external_table_properties
```

modify\_col\_properties

```
column [ datatype ]
       [ COLLATE column_collation_name ]
       [ DEFAULT [ ON NULL ] expr | identity_clause | DROP IDENTITY ]
       [ { ENCRYPT encryption_spec } | DECRYPT ]
       [ inline_constraint ... ]
       [ LOB_storage_clause ]
       [ alter_XMLSchema_clause ]
```

modify\_col\_substitutable

```
COLUMN column
[ NOT ] SUBSTITUTABLE AT ALL LEVELS
[ FORCE ]
```

modify\_col\_visibility

```
column { VISIBLE | INVISIBLE }
```

modify\_collection\_retrieval

```
MODIFY NESTED TABLE collection_item
RETURN AS { LOCATOR | VALUE }
```

modify\_column\_clauses

```
MODIFY
{ ( modify_col_properties | modify_virtcol_properties
    [, modify_col_properties | modify_virtcol_properties ]... )
| ( modify_col_visibility [, modify_col_visibility ]... )
| modify_col_substitutable
}
```

modify\_external\_table\_properties

```
DEFAULT DIRECTORY directory 
 [ LOCATION '(' directory ':' ''' location_specifier ''' ')' ]
 [ ACCESS PARAMETERS 
   [ BADFILE filename ]
   [ LOGFILE filename ]
   [ DISCARDFILE filename ] ]
 [ REJECT LIMIT { integer | UNLIMITED ]
```

modify\_filegroup\_clause

```
MODIFY FILEGROUP filegroup_name
  SET '[ file_type. ] property_name' = 'property_value'
```

modify\_hash\_partition

```
MODIFY partition_extended_name
  { partition_attributes
  | coalesce_table_subpartition
  | alter_mapping_table_clause
  | [ REBUILD ] UNUSABLE LOCAL INDEXES
  | read_only_clause
  | indexing_clause
  }
```

modify\_index\_default\_attrs

```
MODIFY DEFAULT ATTRIBUTES
   [ FOR PARTITION partition ]
   { physical_attributes_clause
   | TABLESPACE { tablespace | DEFAULT }
   | logging_clause
   }...
```

modify\_index\_partition

```
MODIFY PARTITION partition
{ { deallocate_unused_clause
  | allocate_extent_clause
  | physical_attributes_clause
  | logging_clause
  | index_compression
  }...
| PARAMETERS ('ODCI_parameters')
| COALESCE [ CLEANUP ] [ parallel_clause ]
| UPDATE BLOCK REFERENCES
| UNUSABLE
}
```

modify\_index\_subpartition

```
MODIFY SUBPARTITION subpartition
{ UNUSABLE
| allocate_extent_clause
| deallocate_unused_clause
}
```

modify\_list\_partition

```
MODIFY partition_extended_name
  { partition_attributes
  | { ADD | DROP } VALUES ( list_values )
  | { add_range_subpartition
    | add_list_subpartition
    | add_hash_subpartition
    }
  | coalesce_table_subpartition
  | [ REBUILD ] UNUSABLE LOCAL INDEXES
  | read_only_clause
  | indexing_clause
  }
```

modify\_LOB\_parameters

```
{ storage_clause
| PCTVERSION integer
| FREEPOOLS integer
| REBUILD FREEPOOLS
| LOB_retention_clause
| LOB_deduplicate_clause
| LOB_compression_clause
| { ENCRYPT encryption_spec | DECRYPT }
| { CACHE 
  | { NOCACHE | CACHE READS } [ logging_clause ]
  }
| allocate_extent_clause
| shrink_clause
| deallocate_unused_clause
} ...
```

modify\_LOB\_storage\_clause

```
MODIFY LOB (LOB_item)
   (modify_LOB_parameters)
```

modify\_mv\_column\_clause

```
MODIFY ( column [ ENCRYPT encryption_spec
       | DECRYPT ] 
       )
```

modify\_opaque\_type

```
MODIFY OPAQUE TYPE anydata_column
STORE ( type_name [, type_name ]... ) UNPACKED
```

modify\_range\_partition

```
MODIFY partition_extended_name
   { partition_attributes
   | { add_range_subpartition
     | add_hash_subpartition
     | add_list_subpartition
     }
   | coalesce_table_subpartition
   | alter_mapping_table_clause
   | [ REBUILD ] UNUSABLE LOCAL INDEXES
   | read_only_clause
   | indexing_clause
   }
```

modify\_table\_default\_attrs

```
MODIFY DEFAULT ATTRIBUTES
   [ FOR partition_extended_name ]
   [ deferred_segment_creation ]
   [ read_only_clause ]
   [ indexing_clause ]
   [ segment_attributes_clause ]
   [ table_compression ]
   [ inmemory_clause ]
   [ PCTTHRESHOLD integer ]
   [ prefix_compression ]
   [ alter_overflow_clause ]
   [ { LOB (LOB_item) | VARRAY varray } (LOB_parameters) ]...
```

modify\_table\_partition

```
{ modify_range_partition
| modify_hash_partition
| modify_list_partition
}
```

modify\_table\_subpartition

```
MODIFY subpartition_extended_name
{ allocate_extent_clause
| deallocate_unused_cluse
| shrink_clause
| { { LOB LOB_item | VARRAY varray } (modify_LOB_parameters) }...
| [ REBUILD ] UNUSABLE LOCAL INDEXES
| { ADD | DROP } VALUES ( list_values )
| read_only_clause
| indexing_clause
}
```

modify\_to\_partitioned

```
MODIFY table_partitioning_clauses
  [ filter_condition ]
  [ ONLINE ]
  [ UPDATE INDEXES
    [ ( index { local_partitioned_index | global_partitioned_index | GLOBAL }
        [, index { local_partitioned_index | global_partitioned_index | GLOBAL } ]... )
    ]
  ]
```

modify\_virtcol\_properties

```
column [ datatype ]
[ COLLATE column_collation_name ]
[ GENERATED ALWAYS ] AS (column_expression) [ VIRTUAL ]
evaluation_edition_clause [ unusable_editions_clause ]
```

modify\_volume\_clause

```
MODIFY VOLUME asm_volume
   [ MOUNTPATH 'mountpath_name' ]
  [ USAGE 'usage_name' ]
```

modify\_table\_default\_attrs

```
MODIFY DEFAULT ATTRIBUTES
   [ FOR partition_extended_name ]
   [ DEFAULT DIRECTORY directory ]
   [ deferred_segment_creation ]
   [ read_only_clause ]
   [ indexing_clause ]
   [ segment_attributes_clause ]
   [ table_compression ]
   [ inmemory_clause ]
   [ PCTTHRESHOLD integer ]
   [ prefix_compression ]
   [ alter_overflow_clause ]
   [ { LOB (LOB_item) | VARRAY varray } (LOB_parameters) ]...
```

move\_datafile\_clause

```
MOVE DATAFILE ( 'filename' | 'ASM_filename' | file_number )
 [ TO ( 'filename' | 'ASM_filename' ) ]
 [ REUSE ] [ KEEP ]
```

move\_mv\_log\_clause

```
MOVE segment_attributes_clause [parallel_clause]
```

move\_table\_clause

```
MOVE
   [ filter_condition ]
   [ ONLINE ]
   [ segment_attributes_clause ]
   [ table_compression ]
   [ index_org_table_clause ]
   [ { LOB_storage_clause | varray_col_properties }... ]
   [ parallel_clause ]
   [ allow_disallow_clustering ]
   [ UPDATE INDEXES
     [ ( index { segment_attributes_clause
               | update_index_partition }
         [, index { segment_attributes_clause
                  | update_index_partition } ]...
       )
     ]
   ]
```

move\_table\_partition

```
MOVE partition_extended_name
   [ MAPPING TABLE ]
   [ table_partition_description ]
   [ filter_condition ]
   [ update_index_clauses ]
   [ parallel_clause ]
   [ allow_disallow_clustering ]
   [ ONLINE ]
```

move\_table\_subpartition

```
MOVE subpartition_extended_name [ indexing_clause ]
     [ partitioning_storage_clause ]
     [ update_index_clauses ]
     [ filter_condition ]
     [ parallel_clause ]
     [ allow_disallow_clustering ]
     [ ONLINE ]
```

move\_to\_filegroup\_clause

```
MOVE FILE 'ASM_filename' TO FILEGROUP filegroup_name
```

move\_keys

```
MOVE [ENCRYPTION] KEYS  
    TO NEW KEYSTORE keystore_location1
    IDENTIFIED BY keystore1_password
    FROM [FORCE] KEYSTORE
    IDENTIFIED BY keystore_password
    [WITH IDENTIFIER IN
      { 'key_identifier' [, 'key_identifier']... | ( subquery ) } ]
    WITH BACKUP [USING 'backup_identifier']
```

multi\_column\_for\_loop

```
FOR (dimension_column
      [, dimension_column ]...)
IN ( { (literal [, literal ]...)
       [ (literal [, literal ]...) ]...
     | subquery
     }
   )
```

multi\_table\_insert

```
{ ALL
  { insert_into_clause [ values_clause ] [error_logging_clause] }...
| conditional_insert_clause
} subquery
```

multiset\_except

```
nested_table1
MULTISET EXCEPT [ ALL | DISTINCT ]
nested_table2
```

multiset\_intersect

```
nested_table1
MULTISET INTERSECT [ ALL | DISTINCT ]
nested_table2
```

multiset\_union

```
nested_table1
MULTISET UNION [ ALL | DISTINCT ]
nested_table2
```

mv\_log\_augmentation

```
ADD { { OBJECT ID
      | PRIMARY KEY
      | ROWID
      | SEQUENCE
      } [ (column [, column ]...) ]
    | (column [, column ]... )
    } [, { { OBJECT ID
           | PRIMARY KEY
           | ROWID
           | SEQUENCE
           }
           [ (column [, column ]...) ]
         | (column [, column ]...)
         }
      ]...
    [ new_values_clause ]
```

mv\_log\_purge\_clause

```
PURGE { IMMEDIATE [ SYNCHRONOUS | ASYNCHRONOUS ]  )
      | START WITH datetime_expr 
          [ NEXT datetime_expr 
          | REPEAT INTERVAL interval_expr 
          ]
      | [ START WITH datetime_expr ] { NEXT datetime_expr
                                     | REPEAT INTERVAL interval_expr
                                     }
      }
```

named\_member\_keys

```
'['  attr_name = [, attr_name = member_key_expr ]... ']'
```

nested\_clause

```
table_reference (NESTED [PATH]) identifier
[
("." [ JSON_object_key array_step ] ) |
("," JSON_basic_path_expression )
]
[ JSON_table_on_error_clause ]
[ JSON_table_on_empty_clause ]
 JSON_columns_clause
```

nested\_table\_col\_properties

```
NESTED TABLE
{ nested_item | COLUMN_VALUE }
[ substitutable_column_clause ]
[ LOCAL | GLOBAL ]
STORE AS storage_table
[ ( { (object_properties)
    | [ physical_properties ]
    | [ column_properties ]
    }...
  )
]
[ RETURN [ AS ] { LOCATOR | VALUE } ]
```

nested\_table\_partition\_spec

```
PARTITION partition [segment_attributes_clause]
```

new\_values\_clause

```
{ INCLUDING | EXCLUDING } NEW VALUES
```

number

```
[ + | - ]
{ digit [ digit ]... [ . ] [ digit [ digit ]... ]
| . digit [ digit ]...
}
[ [ e | E ] [ + | - ] digit [ digit ]... ] [ f | F | d | D ]
```

numeric\_file\_name

```
+diskgroup_name.filenumber.incarnation_number
```

object\_properties

```
{ { column | attribute }
    [ DEFAULT expr ]
    [ { inline_constraint }...  | inline_ref_constraint ]
| { out_of_line_constraint
  | out_of_line_ref_constraint
  | supplemental_logging_props
  }
}
```

object\_step

```
.{ simple_name | "complex_name"  | * }
```

object\_table

```
OF
   [ schema. ] object_type
   [ object_table_substitution ]
   [ (object_properties) ]
   [ ON COMMIT { DELETE | PRESERVE } ROWS ]
   [ OID_clause ]
   [ OID_index_clause ]
   [ physical_properties ]
   [ table_properties ]
```

object\_table\_substitution

```
[ NOT ] SUBSTITUTABLE AT ALL LEVELS
```

object\_type\_col\_properties

```
COLUMN column substitutable_column_clause
```

object\_view\_clause

```
OF [ schema. ] type_name
{ WITH OBJECT { IDENTIFIER | ID }
  { DEFAULT | ( attribute [, attribute ]... ) }
| UNDER [ schema. ] superview
}
[ ( { out_of_line_constraint
    | attribute { inline_constraint }...
    }  [, { out_of_line_constraint
          | attribute { inline_constraint }...
          }
       ]...
  )
]
```

OID\_clause

```
OBJECT IDENTIFIER IS
{ SYSTEM GENERATED | PRIMARY KEY }
```

OID\_index\_clause

```
OIDINDEX [ index ]
({ physical_attributes_clause
 | TABLESPACE tablespace
 }...
)
```

on\_comp\_partitioned\_table

```
[ STORE IN ( tablespace [, tablespace ]... ) ]
( PARTITION
    [ partition ]
    [ { segment_attributes_clause
      | index_compression
      }...
    ] [ USABLE | UNUSABLE ] [ index_subpartition_clause ]
      [, PARTITION
           [ partition ]
           [ { segment_attributes_clause
             | index_compression
             }...
           ] [ USABLE | UNUSABLE ] [ index_subpartition_clause ]
       ]...
)
```

on\_error\_clause

```
( ERROR | NULL ) ON ERROR
```

on\_hash\_partitioned\_table

```
{ STORE IN (tablespace[, tablespace ]...)
| (PARTITION [ partition ] [ TABLESPACE tablespace ]
    [ index_compression ] [ USABLE | UNUSABLE ]
  [, PARTITION [ partition ] [ TABLESPACE tablespace ]
    [ index_compression ] [ USABLE | UNUSABLE ]] ...
  )
}
```

on\_list\_partitioned\_table

```
( PARTITION
    [ partition ]
    [ { segment_attributes_clause
      | index_compression
      }...
    ] [ USABLE | UNUSABLE ]
      [, PARTITION
           [ partition ]
           [ { segment_attributes_clause
             | index_compression
             }...
           ] [ USABLE | UNUSABLE ]
      ]...
)
```

on\_object\_clause

```
ON { [ schema. ] object
   | USER user [, user]...
   | DIRECTORY directory_name
   | EDITION edition_name
   | MINING MODEL [ schema. ] mining_model_name
   | JAVA { SOURCE | RESOURCE } [ schema. ] object
   | SQL TRANSLATION PROFILE [ schema. ] profile
   }
```

on\_range\_partitioned\_table

```
( PARTITION
    [ partition ]
    [ { segment_attributes_clause
      | index_compression
      }...
    ] [ USABLE | UNUSABLE ]
      [, PARTITION
          [ partition ]
          [ { segment_attributes_clause
            | index_compression
            }...
          ] [ USABLE | UNUSABLE ]
     ]...
)
```

open\_keystore

```
SET KEYSTORE OPEN
  [ FORCE KEYSTORE ]
  IDENTIFIED BY { EXTERNAL STORE | keystore_password }
  [ CONTAINER = { ALL | CURRENT } ]
```

operation

```
removeOp
| insertOp
| replaceOp 
| appendOp
| setOp
| renameOp
| keepOp
```

option\_values

```
{ { VALUE = ( 'option_value' [, 'option_value' ]... ) }
  |
  { MINVALUE = 'option_value' }
  |
  { MAXVALUE = 'option_value' }
}...
```

order\_by\_clause

```
ORDER [ SIBLINGS ] BY
{ expr | position | c_alias }
[ ASC | DESC ]
[ NULLS FIRST | NULLS LAST ]
  [, { expr | position | c_alias }
     [ ASC | DESC ]
     [ NULLS FIRST | NULLS LAST ]
  ]...
```

ordinality\_column

```
column_name FOR ORDINALITY
```

out\_of\_line\_constraint

```
[ CONSTRAINT constraint_name ]
{ UNIQUE (column [, column ]...)
| PRIMARY KEY (column [, column ]...)
| FOREIGN KEY (column [, column ]...) references_clause
| CHECK (condition)
} [ constraint_state ]
```

out\_of\_line\_part\_storage

```
PARTITION partition
  { nested_table_col_properties | LOB_storage_clause | varray_col_properties }
    [ nested_table_col_properties | LOB_storage_clause | varray_col_properties ]...
[ ( SUBPARTITION subpartition
   { nested_table_col_properties | LOB_storage_clause | varray_col_properties }
     [ nested_table_col_properties | LOB_storage_clause | varray_col_properties
     ]...
    [, SUBPARTITION subpartition
     { nested_table_col_properties | LOB_storage_clause | varray_col_properties }
       [ nested_table_col_properties | LOB_storage_clause | varray_col_properties
       ]...
    ]...
  )
]
```

out\_of\_line\_ref\_constraint

```
{ SCOPE FOR ({ ref_col | ref_attr })
    IS [ schema. ] scope_table
| REF ({ ref_col | ref_attr }) WITH ROWID
| [ CONSTRAINT constraint_name ] FOREIGN KEY
    ( { ref_col [, ref_col ] | ref_attr [, ref_attr ] } ) references_clause
    [ constraint_state ]
}
```

outer\_join\_clause

```
[ query_partition_clause ] [ NATURAL ]
outer_join_type JOIN table_reference
  [ query_partition_clause ]
  [ ON condition
  | USING ( column [, column ]...)
  ]
```

outer\_join\_type

```
{ FULL | LEFT | RIGHT } [ OUTER ]
```

parallel\_clause

```
{ NOPARALLEL | PARALLEL [ integer ] }
```

parallel\_pdb\_creation\_clause

```
PARALLEL [ integer ]
```

partial\_database\_recovery

```
{ TABLESPACE tablespace [, tablespace ]...
| DATAFILE { 'filename' | filenumber }
             [, 'filename' | filenumber ]...
}
```

partial\_index\_clause

```
INDEXING { PARTIAL | FULL }
```

partition\_attributes

```
[ { physical_attributes_clause
  | logging_clause
  | allocate_extent_clause
  | deallocate_unused_clause
  | shrink_clause
  }...
]
[ OVERFLOW
  { physical_attributes_clause
  | logging_clause
  | allocate_extent_clause
  | deallocate_unused_clause
  }...
]
[ table_compression ]
[ inmemory_clause ]
[ { { LOB LOB_item | VARRAY varray } (modify_LOB_parameters) }...]
```

partition\_extended\_name

```
PARTITION partition
| 
PARTITION FOR ( partition_key_value [, partition_key_value]... )
```

partition\_extended\_names

```
{ PARTITION | PARTITIONS }
partition | { FOR ( partition_key_value [, partition_key_value ]... ) }
  [, partition | { FOR ( partition_key_value [, partition_key_value ]... ) } ]...
```

partition\_extension\_clause

```
{ PARTITION (partition)
| PARTITION FOR (partition_key_value [, partition_key_value]...)
| SUBPARTITION (subpartition)
| SUBPARTITION FOR (subpartition_key_value [, subpartition_key_value]...)
}
```

partition\_or\_key\_value

```
partition
|
FOR ( partition_key_value [, partition_key_value ]... )
```

partition\_spec

```
PARTITION [ partition ] [ table_partition_description ]
```

partitioning\_storage\_clause

```
[ { { TABLESPACE tablespace | TABLESPACE SET tablespace_set }
  | OVERFLOW [ TABLESPACE tablespace] | TABLESPACE SET tablespace_set ]
  | table_compression
  | index_compression
  | inmemory_clause
  | ilm_clause
  | LOB_partitioning_storage
  | VARRAY varray_item STORE AS [SECUREFILE | BASICFILE] LOB LOB_segname
  | json_storage_clause
  }...
]
```

partitionset\_clauses

```
{ range_partitionset_clause | list_partitionset_clause }
```

password\_parameters

```
{ { FAILED_LOGIN_ATTEMPTS
  | PASSWORD_LIFE_TIME
  | PASSWORD_REUSE_TIME
  | PASSWORD_REUSE_MAX
  | PASSWORD_LOCK_TIME
  | PASSWORD_GRACE_TIME
  | INACTIVE_ACCOUNT_TIME
  }
  { expr | UNLIMITED | DEFAULT }
  | PASSWORD_VERIFY_FUNCTION { function | NULL | DEFAULT }  
  | PASSWORD_ROLLOVER_TIME { expr | DEFAULT } 
}
```

patch\_common

```
target_expr [ json_query_returning_clause ] [ pretty ]
 [ ASCII ] [ TRUNCATE ] [ json_query_on_error_clause ]
```

path\_prefix\_clause

```
PATH_PREFIX = { 'path_name' | directory_object_name | NONE }
```

pdb\_change\_state

```
[ pdb_name ] { pdb_open | pdb_close | pdb_save_or_discard_state }
```

pdb\_change\_state\_from\_root

```
{ pdb_name [, pdb_name ]... | ALL [ EXCEPT pdb_name [, pdb_name ]... ] }
{ pdb_open | pdb_close | pdb_save_or_discard_state }
```

pdb\_close

```
CLOSE [ IMMEDIATE ] [ instances_clause | relocate_clause ]
```

pdb\_datafile\_clause

```
[ pdb_name ] DATAFILE
  { { { 'filename' | filenumber } [, 'filename' | filenumber ]... } | ALL }
  { ONLINE | OFFLINE }
```

pdb\_dba\_roles

```
ROLES = ( role [, role ]... )
```

pdb\_force\_logging\_clause

```
{ ENABLE | DISABLE } FORCE { LOGGING | NOLOGGING }
| SET STANDBY NOLOGGING FOR {DATA AVAILABILITY | LOAD PERFORMANCE}
```

pdb\_general\_recovery

```
RECOVER [ AUTOMATIC ]  [ FROM 'location' ]
  [ DATABASE
  |
  TABLESPACE tablespace [, tablespace ]...
  |
  DATAFILE { 'filename' | filenumber }
             [, 'filename' | filenumber ]...
  |
  LOGFILE 'filename'
  |
  CONTINUE [ DEFAULT ]
  ]
```

pdb\_logging\_clauses

```
{ logging_clause
| pdb_force_logging_clause
}
```

pdb\_managed\_recovery

```
RECOVER MANAGED STANDBY DATABASE [ CANCEL ]
```

pdb\_open

```
OPEN
  { [ READ WRITE | READ ONLY ] [ RESTRICTED ] [ FORCE ]
  | [ READ WRITE ] UPGRADE [ RESTRICTED ]
  | RESETLOGS
  }
  [ instances_clause ] [ services_clause ]
```

pdb\_recovery\_clauses

```
[ pdb_name ] { pdb_general_recovery
             | { BEGIN | END } BACKUP
             | { ENABLE | DISABLE } RECOVERY
             }
```

pdb\_refresh\_mode\_clause

```
REFRESH MODE { MANUAL | EVERY refresh_interval { MINUTES | HOURS} | NONE }
```

pdb\_save\_or\_discard\_state

```
{ SAVE | DISCARD } STATE [ instances_clause ]
```

pdb\_settings\_clauses

```
{ [ pdb_name ]
  { DEFAULT EDITION = edition_name
  | SET DEFAULT ( BIGFILE | SMALLFILE ) TABLESPACE
  | DEFAULT TABLESPACE tablespace_name
  | DEFAULT TEMPORARY TABLESPACE { tablespace | tablespace_group_name }
  | RENAME GLOBAL_NAME TO database.domain [. domain ]...
  | set_time_zone_clause
  | database_file_clauses
  | supplemental_db_logging
  | pdb_storage_clause
  | pdb_logging_clauses
  | pdb_refresh_mode_clause
  | REFRESH
  | SET CONTAINER_MAP = 'map_object'
  }
}
| CONTAINERS { DEFAULT TARGET = { (container_name) | NONE 
             |  HOST "=" "'" "hostname" "'"
        |  PORT "=" "number" }
             }
```

pdb\_storage\_clause

```
STORAGE
  { ( { MAXSIZE { UNLIMITED | size_clause }
        |
        MAX_AUDIT_SIZE { UNLIMITED | size_clause }
        |
        MAX_DIAG_SIZE { UNLIMITED | size_clause }
      }...
    )
  |
  UNLIMITED
  }
```

pdb\_snapshot\_clause

```
ENABLE SNAPSHOT { MANUAL | EVERY snapshot_interval { HOURS | MINUTES } | NONE}
```

pdb\_unplug\_clause

```
pdb_name UNPLUG INTO 'filename'
```

period\_definition

```
PERIOD FOR valid_time_column [ ( start_time_column, end_time_column ) ]
```

permanent\_tablespace\_attrs

```
{ MINIMUM EXTENT size_clause
| BLOCKSIZE integer [ K ]
| logging_clause
| FORCE LOGGING
| tablespace_encryption_clause
| default_tablespace_params
| { ONLINE | OFFLINE }
| extent_management_clause
| segment_management_clause
| flashback_mode_clause
| lost_write_protection
}...
```

permanent\_tablespace\_clause

```
TABLESPACE tablespace
  [ DATAFILE file_specification [, file_specification ]... ]
  [ permanent_tablespace_attrs ]
```

physical\_attributes\_clause

```
[ { PCTFREE integer
  | PCTUSED integer
  | INITRANS integer
  | storage_clause
  }...
]
```

physical\_properties

```
{ [ deferred_segment_creation ] segment_attributes_clause [ table_compression ]
    [ inmemory_table_clause ] [ ilm_clause ]
| [ deferred_segment_creation ] ORGANIZATION
  { HEAP [ segment_attributes_clause ] heap_org_table_clause
  | INDEX [ segment_attributes_clause ] index_org_table_clause
  | EXTERNAL PARTITION ATTRIBUTES external_table_clause [ REJECT LIMIT ]
  }
| CLUSTER cluster (column [, column ]...)
}
```

pivot\_clause

```
PIVOT [ XML ]
  ( aggregate_function ( expr ) [[AS] alias ]
      [, aggregate_function ( expr ) [[AS] alias ] ]...
    pivot_for_clause
    pivot_in_clause
  )
```

pivot\_for\_clause

```
FOR { column
    | ( column [, column]... )
    }
```

pivot\_in\_clause

```
IN ( { { { expr
         | ( expr [, expr]... )
         } [ [ AS] alias]
       }...
     | subquery
     | ANY [, ANY]...
     }
   )
```

plsql\_declarations

```
{ function_declaration | procedure_declaration }...
```

policy\_clause

```
( [ OPTIMIZE condition_clause ]  | tiering_clause [ PLSQL_function_name ] )
```

pos\_member\_keys

```
'['  member_key_expr [, member_key_expr]...']'
```

preceding\_boundary

```
{ UNBOUNDED PRECEDING | offset_expr PRECEDING }
AND
{ CURRENT MEMBER 
  | offset_expr  { PRECEDING | FOLLOWING }
  | UNBOUNDED FOLLOWING
}
```

prefix\_compression

```
COMPRESS [ integer ] | NOCOMPRESS
```

prepare\_clause

```
PREPARE MIRROR COPY copy_name 
[ WITH { EXTERNAL | NORMAL | HIGH } REDUNDANCY ]
[ FOR DATABASE target_cdb_name ]
```

privilege\_audit\_clause

```
PRIVILEGES system_privilege [, system_privilege ]...
```

program\_unit

```
{ FUNCTION [ schema. ] function_name
|
PROCEDURE [ schema. ] procedure_name
|
PACKAGE [ schema. ] package_name }
```

property\_clause

```
PROPERTY { SET | REMOVE } DEFAULT_CREDENTIAL = SYSTEM.OPCTEST
```

proxy\_clause

```
{ GRANT CONNECT THROUGH { ENTERPRISE USERS | db_user_proxy db_user_proxy_clauses }
| REVOKE CONNECT THROUGH { ENTERPRISE USERS | db_user_proxy }}
```

qdr\_expression

```
QUALIFY ( calc_meas_expression, qualifier )
```

qualified\_disk\_clause

```
search_string
[ NAME disk_name ]
[ SIZE size_clause ]
[ FORCE | NOFORCE ]
```

qualified\_template\_clause

```
ATTRIBUTE
( redundancy_clause 
  striping_clause 
)
```

qualifier

```
hierarchy_ref = member_expression
```

query\_block

```
[ with_clause ]
SELECT [ hint ] [ { { DISTINCT | UNIQUE } | ALL } ] select_list
  FROM { table_reference | join_clause | ( join_clause ) }
         [ , { table_reference | join_clause | (join_clause) } ] ...
  [ where_clause ]
  [ hierarchical_query_clause ]
  [ group_by_clause ]
  [ model_clause ]
  [ window_clause ]
```

query\_partition\_clause

```
PARTITION BY
  { expr[, expr ]...
  | ( expr[, expr ]... )
  }
```

query\_rewrite\_clause

```
{ ENABLE | DISABLE } QUERY REWRITE [ unusable_editions_clause ]
```

query\_table\_expression

```
{ query_name
| [ schema. ]
  { table [ modified_external_table
          | partition_extension_clause
          | @ dblink
          ]
  | { view | materialized view } [ @ dblink ]
  | hierarchy
  | analytic_view [ HIERARCHIES
    ( [ [ attr_dim. ] hierarchy [, [ attr_dim. ] hierarchy ]... ] ) ]
  | inline_external_table
  } [sample_clause]
| [ LATERAL ] (subquery [ subquery_restriction_clause ])
| table_collection_expression
}
```

qry\_transform\_clause

```
ENABLE QUERY TRANSFORM [ RELY | NORELY ]
```

quiesce\_clauses

```
QUIESCE RESTRICTED | UNQUIESCE
```

quotagroup\_clauses

```
{ ADD QUOTAGROUP quotagroup_name [ SET property_name = property_value ]
| MODIFY QUOTAGROUP quotagroup_name SET property_name = property_value
| MOVE FILEGROUP filegroup_name TO quotagroup_name
| DROP QUOTAGROUP quotagroup_name
}
```

range\_partition\_desc

```
PARTITION [partition]
range_values_clause
table_partition_description
[ ( { range_subpartition_desc [, range_subpartition_desc] ...
    | list_subpartition_desc [, list_subpartition_desc] ...
    | individual_hash_subparts [, individual_hash_subparts] ...
    }
  ) | hash_subparts_by_quantity ]
```

range\_partitions

```
PARTITION BY RANGE (column[, column ]...)
  [ INTERVAL (expr) [ STORE IN ( tablespace [, tablespace]...) ]]
( PARTITION [ partition ]
    range_values_clause table_partition_description
      [, PARTITION [ partition ]
        range_values_clause table_partition_description
        [ external_part_subpart_data_props ]
      ]...
)
```

range\_partitionset\_clause

```
PARTITIONSET BY RANGE (column [, column]...)
  PARTITION BY CONSISTENT HASH (column [, column]...)
  [ SUBPARTITION BY { { RANGE | HASH } (column [, column]...)
                    | LIST (column)
                    }
  [ subpartition_template ]
  ]
  PARTITIONS AUTO ( range_partitionset_desc [, range_partitionset_desc]... )
```

range\_partitionset\_desc

```
PARTITIONSET partition_set range_values_clause
  [ TABLESPACE SET tablespace_set ]
  [ LOB_storage_clause ]
  [ SUBPARTITIONS STORE IN ( tablespace_set … ) ]
```

range\_subpartition\_desc

```
SUBPARTITION [subpartition] range_values_clause
  [read_only_clause] [indexing_clause] [partitioning_storage_clause]
  [external_part_subpart_data_props]
```

range\_values\_clause

```
VALUES LESS THAN
  ({ literal | MAXVALUE }
     [, { literal | MAXVALUE } ]...
  )
```

read\_only\_clause

```
{ READ ONLY } | { READ WRITE }
```

rebalance\_diskgroup\_clause

```
REBALANCE
  [ { [ { WITH | WITHOUT } phase [, phase]... ] [ POWER integer ] [ WAIT | NOWAIT ] }
    |
    { MODIFY POWER [ integer ] }
  ]
```

rebuild\_clause

```
REBUILD
  [ { PARTITION partition
    | SUBPARTITION subpartition
    }
  | { REVERSE | NOREVERSE }
  ]
  [ parallel_clause
  | TABLESPACE tablespace
  | PARAMETERS ( 'ODCI_parameters' )
  | XMLIndex_parameters_clause
  | ONLINE
  | physical_attributes_clause
  | index_compression
  | logging_clause
  | partial_index_clause
  ]...
```

records\_per\_block\_clause

```
{ MINIMIZE | NOMINIMIZE } RECORDS_PER_BLOCK
```

recovery\_clauses

```
{ general_recovery
| managed_standby_recovery
| BEGIN BACKUP
| END BACKUP
}
```

redo\_log\_file\_spec

```
[ 'filename | ASM_filename'
| ('filename | ASM_filename'
   [, 'filename | ASM_filename' ]...)
]
[ SIZE size_clause ]
[ BLOCKSIZE size_clause
[ REUSE ]
```

redundancy\_clause

```
[ MIRROR | HIGH | UNPROTECTED | PARITY | DOUBLE]
```

reference\_model

```
REFERENCE reference_model_name ON (subquery)
  model_column_clauses [ cell_reference_options ]
```

reference\_partition\_desc

```
PARTITION [partition] [table_partition_description] )
```

reference\_partitioning

```
PARTITION BY REFERENCE ( constraint ) 
  [ (reference_partition_desc...) ]
```

references\_clause

```
REFERENCES [ schema. ] object [ (column [, column ]...) ]
  [ON DELETE { CASCADE | SET NULL } ]
```

register\_logfile\_clause

```
REGISTER [ OR REPLACE ]
  [ PHYSICAL | LOGICAL ]
LOGFILE [ file_specification  [, file_specification ]...
  [ FOR logminer_session_name ]
```

regular\_entry

```
[ KEY ] expr VALUE expr 
                       | expr [ ":" expr ]
```

relational\_properties

```
{ column_definition
| virtual_column_definition
| period_definition
| { out_of_line_constraint | out_of_line_ref_constraint }
| supplemental_logging_props
}
  [, { column_definition
     | virtual_column_definition
     | period_definition
     | { out_of_line_constraint | out_of_line_ref_constraint }
     | supplemental_logging_props
     }
  ]...
```

relational\_table

```
[ (relational_properties) ]
[ immutable_table_clauses ]
[ blockchain_table_clauses ]
[ DEFAULT COLLATION collation_name ]
[ ON COMMIT { DROP | PRESERVE } DEFINITION ]
[ ON COMMIT { DELETE | PRESERVE } ROWS ]
[ physical_properties ]
[ table_properties ]
```

relocate\_clause

```
RELOCATE [ TO 'instance_name' ] 
| NORELOCATE
```

remove\_op

```
REMOVE pathExpr [ { IGNORE | ERROR } ON MISSING ]
```

rename\_column\_clause

```
RENAME COLUMN old_name TO new_name
```

rename\_disk\_clause

```
RENAME
  { DISK old_disk_name TO new_disk_name [, old_disk_name TO new_disk_name ]...
  | DISKS ALL }
```

rename\_index\_partition

```
RENAME
  { PARTITION partition | SUBPARTITION subpartition }
TO new_name
```

rename\_op

```
RENAME pathExpr WITH stringLiteral [ { IGNORE | ERROR } ) ON MISSING ]
```

rename\_partition\_subpart

```
RENAME { partition_extended_name
       | subpartition_extended_name
       } TO new_name
```

replace\_disk\_clause

```
REPLACE DISK disk_name WITH 'path_name' [ FORCE | NOFORCE ]
  [, disk_name WITH 'path_name' [ FORCE | NOFORCE ] ]...
[ POWER integer ] [ WAIT | NOWAIT ]
```

replace\_op

```
REPLACE pathExpr "=" rhsExpr [ { CREATE | IGNORE | ERROR } ON MISSING ]
            [ { NULL | IGNORE | ERROR | REMOVE } ON NULL ]
```

resize\_disk\_clause

```
RESIZE ALL [ SIZE size_clause ]
```

resource\_parameters

```
{ { SESSIONS_PER_USER
  | CPU_PER_SESSION
  | CPU_PER_CALL
  | CONNECT_TIME
  | IDLE_TIME
  | LOGICAL_READS_PER_SESSION
  | LOGICAL_READS_PER_CALL
  | COMPOSITE_LIMIT
  }
  { integer | UNLIMITED | DEFAULT }
| PRIVATE_SGA
  { size_clause | UNLIMITED | DEFAULT }
}
```

result\_cache\_clause

```
RESULT_CACHE ( "("( [ MODE {DEFAULT | FORCE} ] [ "," STANDBY {ENABLE | DISABLE} ] )
                 | ( [ STANDBY {ENABLE | DISABLE} ] [ "," MODE {DEFAULT | FORCE} ] ) ")" )
```

return\_rows\_clause

```
RETURN { UPDATED | ALL } ROWS
```

returning\_clause

```
{ RETURN | RETURNING } expr [, expr ]...
INTO data_item [, data_item ]...
```

reverse\_migrate\_key

```
SET [ ENCRYPTION ] KEY
  IDENTIFIED BY software_keystore_password
  [ FORCE KEYSTORE ]
  REVERSE MIGRATE USING { HSM_auth_string | OKV_password }
  WITH BACKUP [ USING 'backup_identifier']
```

revoke\_object\_privileges

```
{ object_privilege | ALL [ PRIVILEGES ] }
  [, { object_privilege | ALL [ PRIVILEGES ] } ]...
on_object_clause
FROM revokee_clause
[ CASCADE CONSTRAINTS | FORCE ]
```

revoke\_roles\_from\_programs

```
{ role [, role ]... | ALL } FROM program_unit [, program_unit ]...
```

revoke\_system\_privileges

```
{ system_privilege | role | ALL PRIVILEGES }
  [, { system_privilege | role | ALL PRIVILEGES } ]...
FROM revokee_clause
```

revokee\_clause

```
{ user | role | PUBLIC }
  [, { user | role | PUBLIC } ]...
```

role\_audit\_clause

```
ROLES role [, role ]...
```

rolling\_migration\_clauses

```
{ START ROLLING MIGRATION TO 'ASM_version'
| STOP ROLLING MIGRATION
}
```

rolling\_patch\_clauses

```
{ START ROLLING PATCH
| STOP ROLLING PATCH
}
```

rollup\_cube\_clause

```
{ ROLLUP | CUBE } (grouping_expression_list)
```

routine\_clause

```
[ schema. ] [ type. | package. ]
{ function | procedure | method }
[ @dblink_name ]
( [ argument [, argument ]... ] )
```

row\_limiting\_clause

```
[ OFFSET offset { ROW | ROWS } ]
[ FETCH { FIRST | NEXT } [ { rowcount | percent PERCENT } ]
    { ROW | ROWS } { ONLY | WITH TIES } ]
```

row\_movement\_clause

```
{ ENABLE | DISABLE } ROW MOVEMENT
```

row\_pattern

```
[ row_pattern | ] row_pattern_term

Note: The vertical bar is part of the syntax rather than BNF notation.
```

row\_pattern\_aggregate\_func

```
[ RUNNING | FINAL ] aggregate_function
```

row\_pattern\_classifier\_func

```
CLASSIFIER()
```

row\_pattern\_clause

```
MATCH_RECOGNIZE (
  [ row_pattern_partition_by ]
  [ row_pattern_order_by ]
  [ row_pattern_measures ]
  [ row_pattern_rows_per_match ]
  [ row_pattern_skip_to ]
  PATTERN (row_pattern)
  [ row_pattern_subset_clause ]
  DEFINE row_pattern_definition_list
  )
```

row\_pattern\_definition

```
variable_name AS condition
```

row\_pattern\_definition\_list

```
row_pattern_definition [, row_pattern_definition ]...
```

row\_pattern\_factor

```
row_pattern_primary [ row_pattern_quantifier ]
```

row\_pattern\_match\_num\_func

```
MATCH_NUMBER()
```

row\_pattern\_measure\_column

```
expr AS c_alias
```

row\_pattern\_measures

```
MEASURES row_pattern_measure_column [, row_pattern_measure_column ]...
```

row\_pattern\_nav\_compound

```
{ PREV | NEXT }
( [ RUNNING | FINAL ] { FIRST | LAST } ( expr [, offset ] ) [, offset] )
```

row\_pattern\_nav\_logical

```
[ RUNNING | FINAL ] { FIRST | LAST } ( expr [, offset ] )
```

row\_pattern\_nav\_physical

```
{ PREV | NEXT } ( expr [, offset ] )
```

row\_pattern\_navigation\_func

```
row_pattern_nav_logical
| row_pattern_nav_physical
| row_pattern_nav_compound
```

row\_pattern\_order\_by

```
ORDER BY column [, column ]...
```

row\_pattern\_partition\_by

```
PARTITION BY column [, column ]...
```

row\_pattern\_permute

```
PERMUTE ( row_pattern [, row_pattern ]...)
```

row\_pattern\_primary

```
variable_name
| $
| ^
| ( [ row_pattern ] )
| {- row_pattern -}
| row_pattern_permute

Note: The curly brackets are part of the syntax rather than BNF notation.
```

row\_pattern\_quantifier

```
* [ ? ]
| + [ ? ]
| ? [ ? ]
| { [ unsigned_integer ] , [ unsigned_integer ] } [ ? ]
| { unsigned_integer }

Note: The curly brackets are part of the syntax rather than BNF notation.
```

row\_pattern\_rec\_func

```
row_pattern_classifier_func
| row_pattern_match_num_func
| row_pattern_navigation_func
| row_pattern_aggregate_func
```

row\_pattern\_rows\_per\_match

```
ONE ROW PER MATCH
| ALL ROWS PER MATCH
```

row\_pattern\_skip\_to

```
AFTER MATCH {
  SKIP TO NEXT ROW
  | SKIP PAST LAST ROW
  | SKIP TO FIRST variable_name
  | SKIP TO LAST variable_name
  | SKIP TO variable_name
  }
```

row\_pattern\_subset\_clause

```
SUBSET row_pattern_subset_item [, row_pattern_subset_item ]...
```

row\_pattern\_subset\_item

```
variable_name = ( variable_name [, variable_name ] )
```

row\_pattern\_term

```
[ row_pattern_term ] row_pattern_factor
```

sample\_clause

```
SAMPLE [ BLOCK ]
       (sample_percent)
       [ SEED (seed_value) ]
```

scoped\_table\_ref\_constraint

```
{ SCOPE FOR ({ ref_column | ref_attribute })
  IS [ schema. ] { scope_table_name | c_alias }
}
```

scrub\_clause

```
SCRUB [ FILE 'ASM_filename' | DISK disk_name ]
  [ REPAIR | NOREPAIR ]
  [ POWER { AUTO | LOW | HIGH | MAX } ]
  [ WAIT | NOWAIT ]
  [ FORCE | NOFORCE ]
  [ STOP ]
```

search\_clause

```
{ SEARCH
        { DEPTH FIRST BY c_alias [, c_alias]...
            [ ASC | DESC ]
            [ NULLS FIRST | NULLS LAST ]
         | BREADTH FIRST BY c_alias [, c_alias]...
            [ ASC | DESC ]
            [ NULLS FIRST | NULLS LAST ]
        }
        SET ordering_column
}
```

searched\_case\_expression

```
{ WHEN condition THEN return_expr }...
```

secret\_management\_clauses

```
{ add_update_secret
| delete_secret
| add_update_secret_seps
| delete_secret_seps
}
```

security\_clause

```
GUARD { ALL | STANDBY | NONE }
```

security\_clauses

```
{ ENABLE | DISABLE } RESTRICTED SESSION
```

segment\_attributes\_clause

```
{ physical_attributes_clause
| { TABLESPACE tablespace | TABLESPACE SET tablespace_set }
| logging_clause
}...
```

segment\_management\_clause

```
SEGMENT SPACE MANAGEMENT { AUTO | MANUAL }
```

select\_list

```
{ *
| { query_name.*
  | [ schema. ] { table | view | materialized view } .*
  | t_alias.*
  | expr [ [ AS ] c_alias ]
  }
    [, { query_name.*
       | [ schema. ] { table | view | materialized view } .*
       | t_alias.*
       | expr [ [ AS ] c_alias ]
       }
    ]...
}
```

service\_name\_convert

```
SERVICE_NAME_CONVERT =
  { ( 'service_name', 'replacement_service_name'
      [, 'service_name', 'replacement_service_name' ]... )
    |
    NONE
  }
```

set\_encryption\_key

```
{ SET ENCRYPTION KEY
  {
    [ "certificate_id" ] IDENTIFIED BY "wallet_password"
    |
    IDENTIFIED BY "HSM_auth_string" [ MIGRATE USING "wallet_password" ]
  }
}
```

set\_key

```
SET [ ENCRYPTION ] KEY { mkid:mk | mk }
  [ USING TAG 'tag' ]
  [ USING ALGORITHM 'encrypt_algorithm' ]
  [ FORCE KEYSTORE ]
  IDENTIFIED BY { EXTERNAL STORE | keystore_password }
  WITH BACKUP [ USING 'backup_identifier' ] 
  [ CONTAINER = { ALL | CURRENT } ]
```

set\_key\_tag

```
SET TAG 'tag' FOR 'key_id'
  [ FORCE KEYSTORE ]
  IDENTIFIED BY { EXTERNAL STORE | keystore_password }
  [ WITH BACKUP [ USING 'backup_identifier' ]]
```

set\_op

```
SET pathExpr "=" rhsExpr [ { IGNORE | ERROR | REPLACE } ON EXISTING ]
            [ { CREATE | IGNORE | ERROR } ON MISSING ] [ { NULL | IGNORE | ERROR } ON NULL ]
```

set\_parameter\_clause

```
parameter_name =
   parameter_value [, parameter_value ]...
   [ COMMENT = string ]
   [ DEFERRED ]
   [ CONTAINER = { CURRENT | ALL } ]
   [ { SCOPE = { MEMORY | SPFILE | BOTH }
     | SID = { 'sid' | '*' }
     }...
   ]
```

set\_subpartition\_template

```
SET SUBPARTITION TEMPLATE
   { ( range_subpartition_desc [, range_subpartition_desc]... )
   | ( list_subpartition_desc [, list_subpartition_desc]... )
   | ( individual_hash_subparts [, individual_hash_subparts]... )
   | ()
   | hash_subpartition_quantity
   }
```

set\_time\_zone\_clause

```
SET TIME_ZONE =
   '{ { + | - } hh : mi | time_zone_region }'
```

shards\_clause

```
SHARDS ( [schema.] { table | view } )
```

share\_clause

```
HIERARCHY hierarchy_ref
  { PARENT 
  | LEVEL level_ref
  | MEMBER member_expression
  }
```

share\_of\_expression

```
SHARE_OF ( calc_meas_expression  share_clause )
```

sharing\_clause

```
SHARING = { METADATA | DATA | NONE }
```

shrink\_clause

```
SHRINK SPACE [ COMPACT ] [ CASCADE ]
```

shutdown\_dispatcher\_clause

```
SHUTDOWN [ IMMEDIATE ] dispatcher_name
```

simple\_case\_expression

```
expr
  { WHEN comparison_expr THEN return_expr }...
```

single\_column\_for\_loop

```
FOR dimension_column
  { IN ( { literal [, literal ]...
         | subquery
         }
       )
  | [ LIKE pattern ] FROM literal TO literal
      { INCREMENT | DECREMENT } literal
  }
```

single\_table\_insert

```
insert_into_clause
{ values_clause [ returning_clause ]
| subquery 
} [ error_logging_clause ]
```

size\_clause

```
integer [ K | M | G | T | P | E ]
```

source\_clause

```
[ schema . ] fact_table_or_view [ REMOTE ] ( [ [ AS ] alias ] )
```

source\_file\_directory

```
SOURCE_FILE_DIRECTORY = { 'directory_path_name' | NONE }
```

source\_file\_name\_convert

```
SOURCE_FILE_NAME_CONVERT =
  { ( 'filename_pattern', 'replacement_filename_pattern'
      [, 'filename_pattern', 'replacement_filename_pattern' ]... )
    |
    NONE
  }
```

split\_index\_partition

```
SPLIT PARTITION partition_name_old
   AT (literal [, literal ]...)
   [ INTO (index_partition_description,
           index_partition_description
          )
   ]
   [ parallel_clause ]
```

split\_nested\_table\_part

```
NESTED TABLE column INTO
  ( nested_table_partition_spec, nested_table_partition_spec
    [split_nested_table_part]
  ) [split_nested_table_part]
```

split\_table\_partition

```
SPLIT partition_extended_name
  { AT (literal [, literal]... )
    [ INTO ( range_partition_desc, range_partition_desc ) ]
  | VALUES ( list_values )
    [ INTO ( list_partition_desc, list_partition_desc ) ]
  | INTO ( { range_partition_desc [, range_partition_desc ]...
           | list_partition_desc [, list_partition_desc ]... }
         , partition_spec )
  } [ split_nested_table_part ]
    [ filter_condition ]
    [ dependent_tables_clause ]
    [ update_index_clauses ]
    [ parallel_clause ]
    [ allow_disallow_clustering ]
    [ ONLINE ]
```

split\_table\_subpartition

```
SPLIT subpartition_extended_name
  { AT ( literal [, literal]... )
    [ INTO ( range_subpartition_desc, range_subpartition_desc ) ]
  | VALUES ( list_values )
    [ INTO ( list_subpartition_desc, list_subpartition_desc ) ]
  | INTO ( { range_subpartition_desc [, range_subpartition_desc ]...
           | list_subpartition_desc [, list_subpartition_desc ]... }
         , subpartition_spec )
  } [ filter_condition ]
    [ dependent_tables_clause ]
    [ update_index_clauses ]
    [ parallel_clause ]
    [ allow_disallow_clustering ]
    [ ONLINE ]
```

sql\_format

```
[+ | -] days hours : minutes : seconds [. frac_secs ]
```

standard\_actions

```
ACTIONS
  { { object_action | ALL }
    ON { DIRECTORY directory_name
       | MINING MODEL [ schema. ] object_name
       | [ schema. ] object_name }
  | { system_action | ALL }
  }
    [ { object_action | ALL }
      ON { DIRECTORY directory_name
         | MINING MODEL [ schema. ] object_name
         | [ schema. ] object_name }
    | { system_action | ALL } ]...
```

standby\_database\_clauses

```
{ { activate_standby_db_clause
| maximize_standby_db_clause
| register_logfile_clause
| commit_switchover_clause
| start_standby_clause
| stop_standby_clause
| convert_database_clause
} [ parallel_clause ] }
|
{ switchover_clause | failover_clause }
```

standbys\_clause

```
STANDBYS = { ( 'cdb_name' [, 'cdb_name' ]... )
           | { ALL [ EXCEPT ( 'cdb_name' [, 'cdb_name' ]... ) ] }
           | NONE
           }
```

start\_standby\_clause

```
START LOGICAL STANDBY APPLY
[ IMMEDIATE ]
[ NODELAY ]
[ NEW PRIMARY dblink
| INITIAL [ scn_value ]
| { SKIP FAILED TRANSACTION | FINISH }
]
```

startup\_clauses

```
{ MOUNT [ { STANDBY | CLONE } DATABASE ]
| OPEN
  { [ READ WRITE ]
      [ RESETLOGS | NORESETLOGS ]
        [ UPGRADE | DOWNGRADE ]
  | READ ONLY
  }
}
```

statement\_clauses

```
CLAUSE
{ { = ( 'clause' [, 'clause' ]... ) }
| { = ( 'clause' ) clause_options }
| { ALL [ EXCEPT = ( 'clause' [, 'clause' ]... ) ] }
}
```

static\_base\_profile

```
FROM base_profile
```

still\_image\_object\_types

```
{ SI_StillImage
| SI_AverageColor
| SI_PositionalColor
| SI_ColorHistogram
| SI_Texture
| SI_FeatureList
| SI_Color
}
```

stop\_standby\_clause

```
{ STOP | ABORT } LOGICAL STANDBY APPLY
```

storage\_clause

```
STORAGE
({ INITIAL size_clause
 | NEXT size_clause
 | MINEXTENTS integer
 | MAXEXTENTS { integer | UNLIMITED }
 | maxsize_clause
 | PCTINCREASE integer
 | FREELISTS integer
 | FREELIST GROUPS integer
 | OPTIMAL [ size_clause | NULL ]
 | BUFFER_POOL { KEEP | RECYCLE | DEFAULT }
 | FLASH_CACHE { KEEP | NONE | DEFAULT }
 | ENCRYPT
 } ...
)
```

storage\_table\_clause

```
WITH {SYSTEM | USER} MANAGED STORAGE TABLES
```

string

```
[ {N | n} ]
{ '[ c ]...'
| { Q | q } 'quote_delimiter c [ c ]... quote_delimiter'
}
```

striping\_clause

```
[ FINE | COARSE ]
```

sub\_av\_clause

```
USING [ schema . ] base_av_name [ hierarchies_clause ]
  [ filter_clauses] [ add_meas_clause ]
```

subpartition\_by\_hash

```
SUBPARTITION BY HASH (column [, column ]...)
   [ SUBPARTITIONS integer
        [ STORE IN (tablespace [, tablespace ]...) ]
   | subpartition_template
   ]
```

subpartition\_by\_list

```
SUBPARTITION BY LIST ( column [, column]... ) [ subpartition_template ]
```

subpartition\_by\_range

```
SUBPARTITION BY RANGE ( column [, column]... ) [subpartition_template]
```

subpartition\_extended\_name

```
SUBPARTITION subpartition
| 
SUBPARTITION FOR ( subpartition_key_value [, subpartition_key_value]... )
```

subpartition\_extended\_names

```
{ SUBPARTITION | SUBPARTITIONS }
subpartition | { FOR ( subpartition_key_value [, subpartition_key_value ]... ) }
  [, subpartition | { FOR ( subpartition_key_value [, subpartition_key_value ]... ) } ]...
```

subpartition\_or\_key\_value

```
subpartition
|
FOR ( subpartition_key_value [, subpartition_key_value ]... )
```

subpartition\_spec

```
SUBPARTITION [ subpartition ] [ partitioning_storage_clause ]
```

subpartition\_template

```
SUBPARTITION TEMPLATE
  ( { range_subpartition_desc [, range_subpartition_desc] ...
    | list_subpartition_desc [, list_subpartition_desc] ...
    | individual_hash_subparts [, individual_hash_subparts] ...
    }
  ) | hash_subpartition_quantity
```

subquery

```
{ query_block
| subquery { UNION [ALL] | INTERSECT | MINUS } subquery
    [ { UNION [ALL] | INTERSECT | MINUS } subquery ]...
| ( subquery )
} [ order_by_clause ] [ row_limiting_clause ]
```

subquery\_factoring\_clause

```
query_name ([c_alias [, c_alias]...]) AS (subquery) [search_clause] [cycle_clause]
[, query_name ([c_alias [, c_alias]...]) AS (subquery) [search_clause] [cycle_clause]]...
```

subquery\_restriction\_clause

```
WITH { READ ONLY
     | CHECK OPTION 
     } [ CONSTRAINT constraint ]
```

substitutable\_column\_clause

```
{ [ ELEMENT ] IS OF [ TYPE ] ( ONLY type )
| [ NOT ] SUBSTITUTABLE AT ALL LEVELS
}
```

supplemental\_db\_logging

```
{ ADD | DROP } SUPPLEMENTAL LOG
{ DATA
| supplemental_id_key_clause
| supplemental_plsql_clause
| supplemental_subset_replication_clause
}
```

supplemental\_id\_key\_clause

```
DATA
( { ALL | PRIMARY KEY | UNIQUE | FOREIGN KEY }
    [, { ALL | PRIMARY KEY | UNIQUE | FOREIGN KEY } ]...
)
COLUMNS
```

supplemental\_log\_grp\_clause

```
GROUP log_group
(column [ NO LOG ]
  [, column [ NO LOG ] ]...)
  [ ALWAYS ]
```

supplemental\_logging\_props

```
SUPPLEMENTAL LOG { supplemental_log_grp_clause
                 | supplemental_id_key_clause
                 }
```

supplemental\_plsql\_clause

```
DATA FOR PROCEDURAL REPLICATION
```

supplemental\_subset\_replication\_clause

```
DATA SUBSET DATABASE REPLICATION
```

supplemental\_table\_logging

```
{ ADD SUPPLEMENTAL LOG
  { supplemental_log_grp_clause | supplemental_id_key_clause }
    [, SUPPLEMENTAL LOG
       { supplemental_log_grp_clause | supplemental_id_key_clause }
    ]...
| DROP SUPPLEMENTAL LOG
  { supplemental_id_key_clause | GROUP log_group }
    [, SUPPLEMENTAL LOG
       { supplemental_id_key_clause | GROUP log_group }
    ]...
}
```

switch\_logfile\_clause

```
SWITCH ALL LOGFILES TO BLOCKSIZE integer
```

switchover\_clause

```
SWITCHOVER TO target_db_name [ VERIFY | FORCE ]
```

system\_partitioning

```
PARTITION BY SYSTEM [ PARTITIONS integer
                    | reference_partition_desc
                       [, reference_partition_desc ...]
                    ]
```

table\_collection\_expression

```
TABLE (collection_expression) [ (+) ]
```

table\_compression

```
COMPRESS
| ROW STORE COMPRESS [ BASIC | ADVANCED ]
| COLUMN STORE COMPRESS [  FOR { QUERY | ARCHIVE } [ LOW | HIGH ] ]
  [ [NO] ROW LEVEL LOCKING ]
| NOCOMPRESS
```

table\_index\_clause

```
[ schema. ] table [ t_alias ]
(index_expr [ ASC | DESC ]
  [, index_expr [ ASC | DESC ] ]...)
  [ index_properties ]
```

table\_partition\_description

```
[ { INTERNAL | EXTERNAL } ]
[ deferred_segment_creation ]
[ read_only_clause ]
[ indexing_clause ]
[ segment_attributes_clause ]
[ table_compression | prefix_compression ]
[ inmemory_clause ]
[ ilm_clause ]
[ OVERFLOW [ segment_attributes_clause ] ]
[ { json_storage_clause
  | LOB_storage_clause
  | varray_col_properties
  | nested_table_col_properties
  }...
]
```

table\_partitioning\_clauses

```
{ range_partitions
| list_partitions
| hash_partitions
| composite_range_partitions
| composite_list_partitions
| composite_hash_partitions
| reference_partitioning
| system_partitioning
| consistent_hash_partitions
| consistent_hash_with_subpartitions
| partitionset_clauses
}
```

table\_properties

```
[ column_properties ]
[ read_only_clause ]
[ indexing_clause ]
[ table_partitioning_clauses ]
[ attribute_clustering_clause ]
[ CACHE | NOCACHE ]
[ result_cache_clause ]
[ parallel_clause ]
[ ROWDEPENDENCIES | NOROWDEPENDENCIES ]
[ enable_disable_clause ]...
[ row_movement_clause ]
[ logical_replication_clause ]
[ flashback_archive_clause ]
[ ROW ARCHIVAL ]
[ { AS subquery } | { FOR EXCHANGE WITH TABLE [ schema .] table } ]
```

table\_reference

```
{ { { ONLY (query_table_expression) | query_table_expression }
  [ flashback_query_clause ]
  [ pivot_clause | unpivot_clause | row_pattern_clause ] }
| containers_clause
| shards_clause
}
[ t_alias ]
```

tablespace\_clauses

```
{ EXTENT MANAGEMENT LOCAL
| DATAFILE file_specification [, file_specification ]...
| SYSAUX DATAFILE file_specification [, file_specification ]...
| default_tablespace
| default_temp_tablespace
| undo_tablespace
}
```

tablespace\_datafile\_clauses

```
DATAFILES { SIZE size_clause | autoextend_clause }...
```

tablespace\_encryption\_clause

```
ENCRYPTION [ { [ tablespace_encryption_spec ] ENCRYPT } | DECRYPT ]
```

tablespace\_encryption\_spec

```
USING 'encrypt_algorithm'
```

tablespace\_group\_clause

```
TABLESPACE GROUP { tablespace_group_name | '' }
```

tablespace\_logging\_clauses

```
{ logging_clause
| [ NO ] FORCE LOGGING
}
```

tablespace\_retention\_clause

```
RETENTION { GUARANTEE | NOGUARANTEE }
```

tablespace\_state\_clauses

```
{ { ONLINE
  | OFFLINE [ NORMAL | TEMPORARY | IMMEDIATE ]
  }
  | READ { ONLY | WRITE }
  | { PERMANENT | TEMPORARY }
}
```

tempfile\_reuse\_clause

```
TEMPFILE REUSE
```

temporary\_tablespace\_clause

```
{ { TEMPORARY TABLESPACE }
| { LOCAL TEMPORARY TABLESPACE FOR { ALL | LEAF } }
} tablespace
[ TEMPFILE file_specification [, file_specification ]... ]
[ tablespace_group_clause ]
[ extent_management_clause ]
[ tablespace_encryption_clause ]
```

tiering\_clause

```
SEGMENT TIER TO LOW_COST_TBS
```

timeout\_clause

```
DROP AFTER integer { M | H }
```

trace\_file\_clause

```
TRACE
  [ AS 'filename' [ REUSE ] ]
  [ RESETLOGS | NORESETLOGS ]
```

tracking\_statistics\_clause

```
AFTER time_interval
  ( DAYS 
  | MONTHS 
  | YEARS )
   OF [ NO ] ( ACCESS | MODIFICATION | CREATION )
```

truncate\_partition\_subpart

```
TRUNCATE { partition_extended_names | subpartition_extended_names }
   [ { DROP [ ALL ] | REUSE } STORAGE ]
   [ update_index_clauses [ parallel_clause ] ] [ CASCADE ]
```

ts\_file\_name\_convert

```
FILE_NAME_CONVERT =
  ( 'filename_pattern', 'replacement_filename_pattern'
      [, 'filename_pattern', 'replacement_filename_pattern' ]... )
  [ KEEP ]
```

undo\_mode\_clause

```
LOCAL UNDO { ON | OFF }
```

undo\_tablespace

```
[ BIGFILE | SMALLFILE ]
UNDO TABLESPACE tablespace
  [ DATAFILE file_specification [, file_specification ]...]
```

undo\_tablespace\_clause

```
UNDO TABLESPACE tablespace
  [ DATAFILE file_specification [, file_specification ]... ]
  [ extent_management_clause ]
  [ tablespace_retention_clause ]
  [ tablespace_encryption_clause ]
```

undrop\_disk\_clause

```
UNDROP DISKS
```

unite\_keystore

```
UNITE KEYSTORE INDENTIFIED BY isolated_keystore_password
WITH ROOT KEYSTORE [ FORCE KEYSTORE ]
IDENTIFIED BY { EXTERNAL STORE | united_keystore_password }
WITH BACKUP [ USING 'backup_identifier' ]
```

unpivot\_clause

```
UNPIVOT [ {INCLUDE | EXCLUDE} NULLS ]
( { column | ( column [, column]... ) }
  pivot_for_clause
  unpivot_in_clause
)
```

unpivot\_in\_clause

```
IN
( { column | ( column [, column]... ) }
      [  AS { literal | ( literal [, literal]... ) } ]
        [, { column | ( column [, column]... ) }
          [  AS {literal | ( literal [, literal]... ) } ]
        ]...
)
```

unusable\_editions\_clause

```
[ UNUSABLE BEFORE { CURRENT EDITION | EDITION edition } ]
[ UNUSABLE BEGINNING WITH { CURRENT EDITION | EDITION edition | NULL EDITION } ]
```

update\_all\_indexes\_clause

```
UPDATE INDEXES
   [ ( index ( update_index_partition
             | update_index_subpartition
             )
        [, index ( update_index_partition
                 | update_index_subpartition
                 )
        ]...
      )
   ]
```

update\_global\_index\_clause

```
{ UPDATE | INVALIDATE } GLOBAL INDEXES
```

update\_index\_clauses

```
{ update_global_index_clause
| update_all_indexes_clause
}
```

update\_index\_partition

```
index_partition_description [ index_subpartition_clause ]
  [, index_partition_description [ index_subpartition_clause ] ]...
```

update\_index\_subpartition

```
SUBPARTITION [ subpartition ]
   [ TABLESPACE tablespace ]
[, SUBPARTITION [ subpartition ]
      [ TABLESPACE tablespace ]
]...
```

update\_set\_clause

```
SET
{ { (column [, column ]...) = (subquery)
  | column = { expr | (subquery) | DEFAULT }
  }
     [, { (column [, column]...) = (subquery)
        | column = { expr | (subquery) | DEFAULT }
        }
     ]...
| VALUE (t_alias) = { expr | (subquery) }
}
```

upgrade\_table\_clause

```
UPGRADE [ [NOT ] INCLUDING DATA ]
   [ column_properties ]
```

use\_key

```
USE [ ENCRYPTION ] KEY 'key_id'
  [ USING TAG 'tag' ]
  [ FORCE KEYSTORE ]
  IDENTIFIED BY { EXTERNAL STORE | keystore_password }
  [ WITH BACKUP [ USING 'backup_identifier' ] ]
```

user\_clauses

```
{ ADD USER user [, 'user']...
| DROP USER user [, 'user']... [CASCADE]
| REPLACE USER 'old_user' WITH 'new_user' [, 'old_user' WITH 'new_user']...
}
```

user\_tablespaces\_clause

```
USER_TABLESPACES =
  { ( 'tablespace' [, 'tablespace' ]... )
  | ALL [ EXCEPT ( 'tablespace' [, 'tablespace' ]... ) ]
  | NONE
  }
  [ SNAPSHOT COPY | NO DATA | COPY | MOVE | NOCOPY ]
```

usergroup\_clauses

```
{ ADD USERGROUP 'usergroup' WITH MEMBER 'user' [, 'user']...
| MODIFY USERGROUP 'usergroup' { ADD | DROP } MEMBER 'user' [, 'user']...
| DROP USERGROUP 'usergroup' 
}
```

using\_clause

```
USING [ schema. ] fact_table_or_view  [ [ AS ] alias ]
```

using\_function\_clause

```
USING [ schema. ] [ package. | type. ] function_name
```

using\_index\_clause

```
USING INDEX
  { [ schema. ] index
  | (create_index_statement)
  | index_properties
  }
```

using\_snapshot\_clause

```
USING SNAPSHOT { snapshot_name | AT SCN snapshot_SCN | AT snapshot_timestamp }
```

using\_statistics\_type

```
USING { [ schema. ] statistics_type | NULL }
```

using\_type\_clause

```
USING [ schema. ] implementation_type [ array_DML_clause ]
```

validation\_clauses

```
{ VALIDATE REF UPDATE [ SET DANGLING TO NULL ]
| VALIDATE STRUCTURE
     [ CASCADE { FAST | COMPLETE { OFFLINE | ONLINE } [ into_clause ] } ]
}
```

values\_clause

```
VALUES ({ expr | DEFAULT }
          [, { expr | DEFAULT } ]...
       )
```

varray\_col\_properties

```
VARRAY varray_item 
{ [ substitutable_column_clause ] varray_storage_clause
| substitutable_column_clause
}
```

varray\_storage\_clause

```
STORE AS [SECUREFILE | BASICFILE] LOB
{ [LOB_segname] ( LOB_storage_parameters )
| LOB_segname
}
```

virtual\_column\_definition

```
column [ datatype [ COLLATE column_collation_name ] ]
  [ VISIBLE | INVISIBLE ]
  [ GENERATED ALWAYS ] AS (column_expression) [ VIRTUAL ]
  [ evaluation_edition_clause ] [ unusable_editions_clause ]
  [ inline_constraint [ inline_constraint ]... ]
```

where\_clause

```
WHERE condition
```

wildcard

```
[ id "." ] id "." "*"
```

window\_clause

```
WINDOW [ window_name AS window_specification ] ...
```

window\_expression

```
aggregate_function OVER ( window_clause )
```

windowing\_clause

```
{ ROWS | RANGE | GROUPS}
{ BETWEEN
  { UNBOUNDED PRECEDING
  | CURRENT ROW
  | value_expr { PRECEDING | FOLLOWING }
  } 
  AND
  { UNBOUNDED FOLLOWING
  | CURRENT ROW
  | value_expr { PRECEDING | FOLLOWING }
  }
| { UNBOUNDED PRECEDING
  | CURRENT ROW
  | value_expr PRECEDING
  }
}
[ EXCLUDE CURRENT ROW
 | EXCLUDE GROUPS
 | EXCLUDE TIES
 | EXCLUDE NO OTHERS ]
```

window\_specification

```
[ existing_window_name ]
  [ query_partition_clause ]
  [ order_by_clause ]
  [ windowing_clause ]
```

with\_clause

```
WITH [ plsql_declarations ] [ subquery_factoring_clause ]
```

XML\_attributes\_clause

```
XMLATTRIBUTES
  ( [ ENTITYESCAPING | NOENTITYESCAPING ]
    [ SCHEMACHECK | NOSCHEMACHECK ]
    value_expr [ { [AS] c_alias } | { AS EVALNAME value_expr } ]
      [, value_expr [ { [AS] c_alias } | { AS EVALNAME value_expr } ] ]...
  )
```

XMLnamespaces\_clause

```
XMLNAMESPACES
  ( { string AS identifier } | { DEFAULT string }
      [, { string AS identifier } | { DEFAULT string } ]...
  )
```

XML\_passing\_clause

```
PASSING [ BY VALUE ] 
    expr [ AS identifier ]
      [, expr [ AS identifier ] 
      ]...
```

XML\_table\_column

```
column
     { FOR ORDINALITY 
     | { datatype | XMLTYPE [ (SEQUENCE) BY REF ] }
     [ PATH string ] [ DEFAULT expr ]
     }
```

XMLIndex\_clause

```
[XDB.] XMLINDEX [ local_XMLIndex_clause ]
                [ parallel_clause ]
  [ XMLIndex_parameters_clause ]
```

XMLSchema\_spec

```
[ XMLSCHEMA XMLSchema_URL ]
ELEMENT { element | XMLSchema_URL # element }
  [ STORE ALL VARRAYS AS { LOBS | TABLES } ]
  [ { ALLOW | DISALLOW } NONSCHEMA ]
  [ { ALLOW | DISALLOW } ANYSCHEMA ]
```

XMLTABLE\_options

```
[ XML_passing_clause ]
[ RETURNING SEQUENCE BY REF ]
[ COLUMNS XML_table_column [, XML_table_column]...]
```

XMLType\_column\_properties

```
XMLTYPE [ COLUMN ] column
   [ XMLType_storage ]
   [ XMLSchema_spec ]
```

XMLType\_storage

```
STORE
{ AS
{ OBJECT RELATIONAL
| [SECUREFILE | BASICFILE]
  { CLOB | BINARY XML }
    [ { LOB_segname [ (LOB_parameters) ]
      | (LOB_parameters)
      }
    ]
}
| { ALL VARRAYS AS { LOBS | TABLES } }
}
```

XMLType\_table

```
OF XMLTYPE
  [ (oject_properties) ]
  [ XMLTYPE XMLType_storage ]
  [ XMLSchema_spec ]
  [ XMLType_virtual_columns ]
  [ ON COMMIT { DELETE | PRESERVE } ROWS ]
  [ OID_clause ]
  [ OID_index_clause ]
  [ physical_properties ]
  [ table_properties ]
```

XMLType\_view\_clause

```
OF XMLTYPE [ XMLSchema_spec ]
WITH OBJECT { IDENTIFIER | ID }
  { DEFAULT | ( expr [, expr ]...) }
```

XMLType\_virtual\_columns

```
VIRTUAL COLUMNS ( column AS (expr) [, column AS (expr) ]... )
```

ym\_iso\_format

```
[-] P [ years Y ] [months M] [days D]
  [T [hours H] [minutes M] [seconds [. frac_secs] S ] ]
```

zero\_downtime\_software\_patching\_clauses

```
SWITCHOVER LIBRARY path FOR ALL CONTAINERS
```

zonemap\_attributes

```
{ TABLESPACE tablespace
| SCALE integer
| { CACHE | NOCACHE }
}...
```

zonemap\_clause

```
{ WITH MATERIALIZED ZONEMAP [ ( zonemap_name ) ] }
|
{ WITHOUT MATERIALIZED ZONEMAP }
```

zonemap\_refresh\_clause

```
REFRESH
[ FAST | COMPLETE | FORCE ]
[ ON { DEMAND | COMMIT | LOAD | DATA MOVEMENT | LOAD DATA MOVEMENT } ]
```