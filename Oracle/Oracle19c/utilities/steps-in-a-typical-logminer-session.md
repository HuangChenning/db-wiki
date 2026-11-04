---
title: Utilities
book: Oracle AI Database Utilities Guide
doc_id: E96081-35
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/steps-in-a-typical-logminer-session.html
tags:
  - oracle
  - 19c
  - utilities
---

## 24.12 Steps in a Typical LogMiner Session

- Understanding How to Run LogMiner Sessions  
	On Premises and Oracle Autonomous Cloud Platform Services LogMiner Sessions are similar, but require different users.
- Typical LogMiner Session Task 1: Enable Supplemental Logging  
	To be able to use LogMiner with redo log files, you must enable supplemental logging.
- Typical LogMiner Session Task 2: Extract a LogMiner Dictionary  
	To use LogMiner, you must select an option to supply LogMiner with a database dictionary.
- Typical LogMiner Session Task 3: Specify Redo Log Files for Analysis  
	You must specify the redo log files that you want to analyze with `DBMS_LOGMNR_ADD_LOGFILE` before starting LogMiner.
- Start LogMiner  
	See how to start LogMiner, and what options you can use to analyze redo log files, filter criteria, and other session characteristics.
- Query V$LOGMNR\_CONTENTS  
	After you start LogMiner, you can query the Oracle Database `V$LOGMNR_CONTENTS` view.
- Typical LogMiner Session Task 6: End the LogMiner Session  
	Ending the LogMiner session.

**Parent topic:** [Using LogMiner to Analyze Redo Log Files](oracle-logminer-utility.md)

### 24.12.1 Understanding How to Run LogMiner Sessions

On Premises and Oracle Autonomous Cloud Platform Services LogMiner Sessions are similar, but require different users.

In a traditional LogMiner session, and when you run LogMiner on `CDB$ROOT`, you run LogMiner by using a PL/SQL package that is owned by `SYS`. To use LogMiner, there are requirements for the user account that you use with LogMiner.

When you run LogMiner in an On-Premise Oracle Database, you can create one `CDB$ROOT` capture extract to capture data from multiple PDBs at the same time, or mine multiple individual PDB logs using Oracle GoldenGate, each capturing data from just one PDB. However for Oracle Autonomous Database Cloud Platform Services, where you do not have access to `CDB$ROOT`, you must use the per-PDB capture method. In this mode, you provision a local user with a predefined set of privileges to the source PDB whose logs you want to review. All LogMiner processing is restricted to this PDB only.

With On-Premise PDBs, you can start as many sessions as resources allow. But for Cloud configurations, while you can still start many concurrent sessions in `CDB$ROOT`, you can start only one session for each PDB using the LogMiner PL/SQL package.

To run LogMiner on `CDB$ROOT`, you use the PL/SQL package `DBMS_LOGMNR.ADD_LOGFILE` and add log files explicitly. Additionally, if you choose to extract a LogMiner dictionary rather than use the online catalog, then you can also use the `DBMS_LOGMNR_D` package.

To run LogMiner on individual PDBs, the procedures are slightly different. instead of using `DBMS_LOGMNR.ADD_LOGFILE`. you specify a period in which you want to review log files for the PDB. Specify the SCN value of the log that you want to query, with either `startScn` and, if you choose, `endScn`, or `startTime`, and if you choose, `endTime`. You then start LogMiner with `DBMS_LOGMNR.START_LOGMNR`. `DBMS_LOGMNR.START_LOGMNR` automatically adds the redo logs for you to analyze.

The `DBMS_LOGMNR` package contains the procedures used to initialize and run LogMiner, including interfaces to specify names of redo log files, filter criteria, and session characteristics. The `DBMS_LOGMNR_D` package queries the database dictionary tables of the current database to create a LogMiner dictionary file.

Requirements for Running LogMiner for Individual PDB

To run LogMiner to query individual PDBs, you must provision a local user with the necessary privilege, using the procedure call `DBMS_GOLDENGATE_AUTH.GRANT_ADMIN_PRIVILEGE`. Also, users with the `GGADMIN` privilege can run Per-PDB capture Extracts.

Again, with individual PDBs, you do not specify the archive logs that you want to mine. Instead, connect to the PDB that you want to mine, and then run `dbms_logmnr_d.STORE_IN_REDO_LOGS`. For example:

```
SQL> execute dbms_logmnr_d.build(option=>dbms_logmnr_d.STORE_IN_REDO_LOGS);
```

You can then connect to the PDB, identify SCNs, then run `dbms_logmnr.start_logmnr` to query the log files for the starting point system change number (SCN) for the PDB log history that you want to view, and if you choose, an end point SCN. Mining proceeds at that point just as with traditional LogMiner queries to the V$LOGMNR\_CONTENTS view. However, only redo generated for the PDB to which you are connected is available

Note:

If you shut down a PDB while Extract and any LogMiner processes are running, then these processes are terminated, as with other active sessions. When the PDB is reopened, restart of Extract mining should continue as normal. When you unplug the PDB, there are no special actions required. However, when you plug in a PDB after unplugging it, all LogMiner and Capture sessions that previously existed in the PDB are removed.

Requirements for Running Traditional LogMiner Sessions When Not Connected As SYS

With On Premises log mining, the LogMiner PL/SQL packages are owned by the `SYS` schema. Therefore, if you are not connected as user `SYS`, then:

- You must include `SYS` in your call. For example:
	```
	EXECUTE SYS.DBMS_LOGMNR.END_LOGMNR;
	```
- You must have been granted the `EXECUTE_CATALOG_ROLE` role.

### 24.12.2 Typical LogMiner Session Task 1: Enable Supplemental Logging

To be able to use LogMiner with redo log files, you must enable supplemental logging.

Redo-based applications can require that additional columns are logged in the redo log files. The process of logging these additional columns is called **supplemental logging**. By default, Oracle Database does not have supplemental logging enabled. At the very least, to use LogMiner, you must enable minimal supplemental logging.

Example 24-2 Enabling Minimal Supplemental Logging

To enable supplemental logging, enter the following statement:

```
ALTER DATABASE ADD SUPPLEMENTAL LOG DATA;
```

### 24.12.3 Typical LogMiner Session Task 2: Extract a LogMiner Dictionary

To use LogMiner, you must select an option to supply LogMiner with a database dictionary.

Choose one of the following options:

- Specify use of the online catalog by using the `DICT_FROM_ONLINE_CATALOG` option when you start LogMiner.
- Extract the database dictionary information to the redo log files.
- Extract database dictionary information to a flat file.

**Parent topic:** Steps in a Typical LogMiner Session

### 24.12.4 Typical LogMiner Session Task 3: Specify Redo Log Files for Analysis

You must specify the redo log files that you want to analyze with `DBMS_LOGMNR_ADD_LOGFILE` before starting LogMiner.

To query logs on `CDB$ROOT` for On Premises, before you can start LogMiner, you must specify the redo log files that you want to analyze. To specify log files, run the `DBMS_LOGMNR.ADD_LOGFILE` procedure, as demonstrated in the following steps. You can add and remove redo log files in any order.

Note:

To query logs for an individual PDB, you use a slightly different procedure. After you connect to the PDB, you query `DBA_LOGMNR_DICTIONARY_BUILDLOG`, identify a `START_SCN` value, and then start LogMiner with `DBMS_LOGMNR.START_LOGMNR`, specifying the SCN value of the log that you want to review. `DBMS_LOGMNR.START_LOGMNR` automatically adds the redo logs for you to analyze. Refer to "Querying Individual PDBs Using LogMiner" for an example.

1. Use SQL\*Plus to start an Oracle Database instance, with the database either mounted or unmounted. For example, enter the `STARTUP` statement at the SQL prompt:
	```
	STARTUP
	```
2. Create a list of redo log files. Specify the `NEW` option of the `DBMS_LOGMNR.ADD_LOGFILE` PL/SQL procedure to signal that this is the beginning of a new list. For example, enter the following to specify the `/oracle/logs/log1.f` redo log file:
	```
	EXECUTE DBMS_LOGMNR.ADD_LOGFILE( -
	   LOGFILENAME => '/oracle/logs/log1.f', -
	   OPTIONS => DBMS_LOGMNR.NEW);
	```
3. If desired, add more redo log files by specifying the `ADDFILE` option of the `DBMS_LOGMNR.ADD_LOGFILE` PL/SQL procedure. For example, enter the following to add the `/oracle/logs/log2.f` redo log file:
	```
	EXECUTE DBMS_LOGMNR.ADD_LOGFILE( -
	   LOGFILENAME => '/oracle/logs/log2.f', -
	   OPTIONS => DBMS_LOGMNR.ADDFILE);
	```
	The `OPTIONS` parameter is optional when you are adding additional redo log files. For example, you can simply enter the following:
	```
	EXECUTE DBMS_LOGMNR.ADD_LOGFILE( -
	   LOGFILENAME=>'/oracle/logs/log2.f');
	```
4. If desired, remove redo log files by using the `DBMS_LOGMNR.REMOVE_LOGFILE` PL/SQL procedure. For example, enter the following to remove the `/oracle/logs/log2.f` redo log file:
	```
	EXECUTE DBMS_LOGMNR.REMOVE_LOGFILE( -
	   LOGFILENAME => '/oracle/logs/log2.f');
	```

### 24.12.5 Start LogMiner

See how to start LogMiner, and what options you can use to analyze redo log files, filter criteria, and other session characteristics.

After you have created a LogMiner dictionary file and specified which redo log files to analyze, you can start LogMiner and analyze your Oracle Database transactions.

1. To start LogMiner, execute the `DBMS_LOGMNR.START_LOGMNR` procedure.
	Oracle recommends that you specify a LogMiner dictionary option. If you do not specify a dictionary option, then LogMiner cannot translate internal object identifiers and data types to object names and external data formats. As a result, LogMiner returns internal object IDs and present data as binary data. Additionally, you cannot use the `MINE_VALUE` and `COLUMN_PRESENT` functions without a dictionary.
	If you are specifying the name of a flat file LogMiner dictionary, then you must supply a fully qualified file name for the dictionary file. For example, to start LogMiner using `/oracle/database/dictionary.ora`, issue the following statement:
	```
	EXECUTE DBMS_LOGMNR.START_LOGMNR( -
	   DICTFILENAME =>'/oracle/database/dictionary.ora');
	```
	If you are not specifying a flat file dictionary name, then use the `OPTIONS` parameter to specify either the `DICT_FROM_REDO_LOGS` or `DICT_FROM_ONLINE_CATALOG` option.
	If you specify `DICT_FROM_REDO_LOGS`, then LogMiner expects to find a dictionary in the redo log files that you specified with the `DBMS_LOGMNR.ADD_LOGFILE` procedure. To determine which redo log files contain a dictionary, look at the `V$ARCHIVED_LOG` view. To see an example of this task, refer to "Extracting a LogMiner Dictionary to the Redo Log Files."
	Note:
	If you add additional redo log files after LogMiner has been started, then you must restart LogMiner. LogMiner does not retain options included in the previous call to `DBMS_LOGMNR.START_LOGMNR`; you must respecify the options that you want to use. However, if you do not specify a dictionary in the current call to `DBMS_LOGMNR.START_LOGMNR`, then LogMiner does retain the dictionary specification from the previous call.
2. Optionally, you can filter or format your query, or use the `OPTIONS` parameter to specify additional characteristics of your LogMiner session. For example, you might decide to use the online catalog as your LogMiner dictionary and to have only committed transactions shown in the `V$LOGMNR_CONTENTS` view, as follows:
	```
	EXECUTE DBMS_LOGMNR.START_LOGMNR(OPTIONS => -
	   DBMS_LOGMNR.DICT_FROM_ONLINE_CATALOG + -
	   DBMS_LOGMNR.COMMITTED_DATA_ONLY);
	```
	You can execute the `DBMS_LOGMNR.START_LOGMNR` procedure multiple times, specifying different options each time. For example, if you did not obtain the desired results from a query of `V$LOGMNR_CONTENTS`, you can restart LogMiner with different options. Unless you need to respecify the LogMiner dictionary, you do not need to add redo log files if they were already added with a previous call to `DBMS_LOGMNR.START_LOGMNR`.

### 24.12.6 Query V$LOGMNR\_CONTENTS

After you start LogMiner, you can query the Oracle Database `V$LOGMNR_CONTENTS` view.

For example:

```
SELECT (XIDUSN || '.' || XIDSLT || '.' || XIDSQN) AS XID, 
   USERNAME, SQL_REDO FROM V$LOGMNR_CONTENTS WHERE USERNAME != 'SYS' 
   AND SEG_OWNER IS NULL OR SEG_OWNER NOT IN ('SYS', 'SYSTEM');

XID         USERNAME  SQL_REDO

1.15.3045   RON       set transaction read write;
1.15.3045   RON       insert into "HR"."JOBS"("JOB_ID","JOB_TITLE",
                      "MIN_SALARY","MAX_SALARY") values ('9782',
                      'HR_ENTRY',NULL,NULL);
1.18.3046   JANE      set transaction read write;
1.18.3046   JANE      insert into "OE"."CUSTOMERS"("CUSTOMER_ID",
                      "CUST_FIRST_NAME","CUST_LAST_NAME",
                      "CUST_ADDRESS","PHONE_NUMBERS","NLS_LANGUAGE",
                      "NLS_TERRITORY","CREDIT_LIMIT","CUST_EMAIL",
                      "ACCOUNT_MGR_ID") values ('9839','Edgar',
                      'Cummings',NULL,NULL,NULL,NULL,
                       NULL,NULL,NULL);
1.9.3041    RAJIV      set transaction read write;
1.9.3041    RAJIV      insert into "OE"."CUSTOMERS"("CUSTOMER_ID",
                       "CUST_FIRST_NAME","CUST_LAST_NAME","CUST_ADDRESS",
                       "PHONE_NUMBERS","NLS_LANGUAGE","NLS_TERRITORY",
                       "CREDIT_LIMIT","CUST_EMAIL","ACCOUNT_MGR_ID") 
                       values ('9499','Rodney','Emerson',NULL,NULL,NULL,NULL,
                       NULL,NULL,NULL);
1.15.3045    RON       commit;
1.8.3054     RON       set transaction read write;
1.8.3054     RON       insert into "HR"."JOBS"("JOB_ID","JOB_TITLE",
                       "MIN_SALARY","MAX_SALARY") values ('9566',
                       'FI_ENTRY',NULL,NULL);
1.18.3046    JANE      commit;
1.11.3047    JANE      set transaction read write;
1.11.3047    JANE      insert into "OE"."CUSTOMERS"("CUSTOMER_ID",
                       "CUST_FIRST_NAME","CUST_LAST_NAME",
                       "CUST_ADDRESS","PHONE_NUMBERS","NLS_LANGUAGE",
                       "NLS_TERRITORY","CREDIT_LIMIT","CUST_EMAIL",
                       "ACCOUNT_MGR_ID") values ('8933','Ronald',
                       'Frost',NULL,NULL,NULL,NULL,NULL,NULL,NULL);
1.11.3047    JANE      commit;
1.8.3054     RON       commit;
```

To see more examples, refer to "Filtering an Formatting Data Returned to `V$LOGMNR_CONTENTS`.

### 24.12.7 Typical LogMiner Session Task 6: End the LogMiner Session

Ending the LogMiner session.

To properly end a LogMiner session, use the `DBMS_LOGMNR.END_LOGMNR` PL/SQL procedure, as follows:

```
EXECUTE DBMS_LOGMNR.END_LOGMNR;
```

This procedure closes all the redo log files and allows all the database and system resources allocated by LogMiner to be released.

If this procedure is not executed, then LogMiner retains all its allocated resources until the end of the Oracle session in which it was called. It is particularly important to use this procedure to end the LogMiner session if either the `DDL_DICT_TRACKING` option or the `DICT_FROM_REDO_LOGS` option was used.

**Parent topic:** Steps in a Typical LogMiner Session