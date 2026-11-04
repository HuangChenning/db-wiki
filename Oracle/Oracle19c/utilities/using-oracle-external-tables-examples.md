---
title: Utilities
book: Oracle AI Database Utilities Guide
doc_id: E96081-35
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/using-oracle-external-tables-examples.html
tags:
  - oracle
  - 19c
  - utilities
---

## 18 External Tables Examples

Learn from these examples how to use the `ORACLE_LOADER`, `ORACLE_DATAPUMP``,ORACLE_HDFS`, and `ORACLE_HIVE` access drivers to query data in Oracle Database and Big Data.

- Using the ORACLE\_LOADER Access Driver to Create Partitioned External Tables  
	This topic describes using the `ORACLE_LOADER` access driver to create partitioned external tables.
- Using the ORACLE\_LOADER Access Driver to Create Partitioned Hybrid Tables  
	This topic describes using the `ORACLE_LOADER` access driver to create partitioned hybrid tables.
- Using the ORACLE\_DATAPUMP Access Driver to Create Partitioned External Tables  
	The example in this section shows how to create a subpartitioned external table.
- Using the ORACLE\_BIGDATA Access Driver to Create Partitioned External Tables  
	The example in this section shows how to create a subpartitioned external table.
- Loading LOBs From External Tables  
	External tables are particularly useful for loading large numbers of records from a single file, so that each record appears in its own row in the table.
- Loading CSV Files From External Tables  
	This topic provides examples of how to load CSV files from external tables under various conditions.

**Parent topic:** [External Tables](oracle-external-tables.md)

### 18.1 Using the ORACLE\_LOADER Access Driver to Create Partitioned External Tables

This topic describes using the `ORACLE_LOADER` access driver to create partitioned external tables.

Example 18-1 Using ORACLE\_LOADER to Create a Partitioned External Table

This example assumes there are four data files with the following content:

```
p1a.dat:
1, AAAAA Plumbing,01372,
28, Sparkly Laundry,78907,
13, Andi's Doughnuts,54570,

p1b.dat:
51, DIY Supplies,61614,
87, Fast Frames,22201,
89, Friendly Pharmacy,89901,

p2.dat:
121, Pleasant Pets,33893,
130, Bailey the Bookmonger,99915,
105, Le Bistrot du Chat Noir,94114,

p3.dat:
210, The Electric Eel Diner,07101,
222, Everyt'ing General Store,80118,
231, Big Rocket Market,01754,
```

There are three fields in the data file: `CUSTOMER_NUMBER`, `CUSTOMER_NAME` and `POSTAL_CODE`. The external table uses range partitioning on `CUSTOMER_NUMBER` to create three partitions.

- Partition 1 is for `customer_number` less than 100
- Partition 2 is for `customer_number` less than 200
- Partition 3 is for `customer_number` less than 300

Note that the first partition has two data files while the other partitions only have one. The following is the output from SQLPlus for creating the file.

```
SQL> create table customer_list_xt
  2    (CUSTOMER_NUMBER number, CUSTOMER_NAME VARCHAR2(50), POSTAL_CODE CHAR(5))
  3  organization external
  4    (type oracle_loader default directory def_dir1)
  5  partition by range(CUSTOMER_NUMBER)
  6  (
  7    partition p1 values less than (100) location('p1a.dat', 'p1b.dat'),
  8    partition p2 values less than (200) location('p2.dat'),
  9    partition p3 values less than (300) location('p3.dat')
 10  );

Table created.
SQL>
```

The following is the output from `SELECT *` for the entire table:

```
SQL> select customer_number, customer_name, postal_code
  2    from customer_list_xt
  3    order by customer_number;

CUSTOMER_NUMBER CUSTOMER_NAME                                      POSTA
--------------- -------------------------------------------------- -----
              1  AAAAA Plumbing                                    01372
             13  Andi's Doughnuts                                  54570
             28  Sparkly Laundry                                   78907
             51  DIY Supplies                                      61614
             87  Fast Frames                                       22201
             89  Friendly Pharmacy                                 89901
            105  Le Bistrot du Chat Noir                           94114
            121  Pleasant Pets                                     33893
            130  Bailey the Bookmonger                             99915
            210  The Electric Eel Diner                            07101
            222  Everyt'ing General Store                          80118
            231  Big Rocket Market                                 01754

12 rows selected.

SQL>
```

The following query should only read records from the first partition:

```
SQL> select customer_number, customer_name, postal_code
  2    from customer_list_xt
  3    where customer_number < 20
  4    order by customer_number;

CUSTOMER_NUMBER CUSTOMER_NAME                                      POSTA
--------------- -------------------------------------------------- -----
              1  AAAAA Plumbing                                    01372
             13  Andi's Doughnuts                                  54570

2 rows selected.

SQL>
```

The following query specifies the partition to read as part of the `SELECT` statement.

```
SQL> select customer_number, customer_name, postal_code
  2    from customer_list_xt partition (p1)
  3    order by customer_number;

CUSTOMER_NUMBER CUSTOMER_NAME                                      POSTA
--------------- -------------------------------------------------- -----
              1  AAAAA Plumbing                                    01372
             13  Andi's Doughnuts                                  54570
             28  Sparkly Laundry                                   78907
             51  DIY Supplies                                      61614
             87  Fast Frames                                       22201
             89  Friendly Pharmacy                                 89901

6 rows selected.

SQL>
```

**Parent topic:** External Tables Examples

### 18.2 Using the ORACLE\_LOADER Access Driver to Create Partitioned Hybrid Tables

This topic describes using the `ORACLE_LOADER` access driver to create partitioned hybrid tables.

Hybrid Partitioned Tables is a feature that extends Oracle Partitioning by allowing some partitions to reside in database segments and some partitions in external files or sources. This significantly enhances functionality of partitioning for Big Data SQL where large portions of a table can reside in external partitions.

Example 18-2 Example

Here is an example of a statement for creating a partitioned hybrid l table:

```
CREATE TABLE hybrid_pt (time_id date, customer number)
  TABLESPACE TS1
  EXTERNAL PARTITION ATTRIBUTES (TYPE ORACLE_LOADER 
                                 DEFAULT DIRECTORY data_dir0
                                 ACCESS PARAMETERS(FIELDS TERMINATED BY ',')
                                 REJECT LIMIT UNLIMITED) 
PARTITION by range (time_id)
(
 PARTITION century_18 VALUES LESS THAN ('01-01-1800')
    EXTERNAL,                                                 <-- empty external partition
  PARTITION century_19 VALUES LESS THAN ('01-01-1900')
    EXTERNAL DEFAULT DIRECTORY data_dir1 LOCATION (‘century19_data.txt'),
  PARTITION century_20 VALUES LESS THAN ('01-01-2000') 
    EXTERNAL LOCATION (‘century20_data.txt'),
  PARTITION year_2000 VALUES LESS THAN ('01-01-2001') TABLESPACE TS2,
  PARTITION pmax VALUES LESS THAN (MAXVALUE)
);
```

In this example, the table contains both internal and external partitions. The default tablespace for internal partitions in the table is `TS1`. An `EXTERNAL PARTITION ATTRIBUTES` clause is added for specifying parameters that apply, at the table level, to the external partitions in the table. The clause is mandatory for hybrid partitioned tables. In this case, external partitions are accessed through the `ORACLE_LOADER` access driver, and the parameters required by the access driver are specified in the clause. At the partition level, an `EXTERNAL` clause is specified in each external partition, along with any external parameters applied to the partition.

In this example, `century_18`, `century_19`, and `century_20` are external partitions. `century_18` is an empty partition since it does not contain a location. The default directory for partition `century_19` is `data_dir1`, overriding the table level default directory. The partition has a location `data_dir1:century19_data.txt`. Partition `century_20` has location `data_dir0:century20_data.txt`, since the table level default directory is applied to a location when a default directory is not specified in a partition. Partitions `year_2000` and `pmax` are internal partitions. Partition `year_2000` has a `tablespace TS2`. When a partition has no `EXTERNAL` clause or external parameters specified in it, it is assumed to be an internal partition by default.

**Parent topic:** External Tables Examples

### 18.3 Using the ORACLE\_DATAPUMP Access Driver to Create Partitioned External Tables

The example in this section shows how to create a subpartitioned external table.

It also shows how to use a virtual column to partition the table.

Example 18-3 Using the ORACLE\_DATAPUMP Access Driver to Create Partitioned External Tables

In this example, the dump files used are the same as those created in the previous example using the `ORACLE_LOADER` access driver. However, in this example, in addition to partitioning the data using `customer_number`, the data is subpartitioned using `postal_code`. For every partition, there is a subpartition where the ` postal_code` is less than 50000 and another subpartition for all other values of `postal_code`. With three partitions, each containing two subpartitions, a total of six files is required. To create the files, use the SQL `CREATE TABLE AS SELECT` statement to select the correct rows for the partition and then write those rows into the file for the `ORACLE_DATAPUMP` driver.

The following statement creates a file with data for the first subpartition (`postal_code` less than 50000) of partition `p1` (`customer_number` less than 100).

```
SQL> create table customer_list_dp_p1_sp1_xt
  2  organization external
  3    (type oracle_datapump default directory def_dir1 location('p1_sp1.dmp'))
  4  as
  5    select customer_number, customer_name, postal_code
  6      from customer_list_xt partition (p1)
  7      where to_number(postal_code) < 50000;

Table created.

SQL>
```

This statement creates a file with data for the second subpartition (all other values for postal\_code) of partition `p1` (customer\_number less than 100).

```
SQL> create table customer_list_dp_p1_sp2_xt
  2  organization external
  3    (type oracle_datapump default directory def_dir1 location('p1_sp2.dmp'))
  4  as
  5    select customer_number, customer_name, postal_code
  6      from customer_list_xt partition (p1)
  7      where to_number(postal_code) >= 50000;

Table created.
```

The files for other partitions are created in a similar fashion, as follows:

```
SQL> create table customer_list_dp_p2_sp1_xt
  2  organization external
  3    (type oracle_datapump default directory def_dir1 location('p2_sp1.dmp'))
  4  as
  5    select customer_number, customer_name, postal_code
  6      from customer_list_xt partition (p2)
  7      where to_number(postal_code) < 50000;

Table created.

SQL>
SQL> create table customer_list_dp_p2_sp2_xt
  2  organization external
  3    (type oracle_datapump default directory def_dir1 location('p2_sp2.dmp'))
  4  as
  5    select customer_number, customer_name, postal_code
  6      from customer_list_xt partition (p2)
  7      where to_number(postal_code) >= 50000;

Table created.

SQL>
SQL> create table customer_list_dp_p3_sp1_xt
  2  organization external
  3    (type oracle_datapump default directory def_dir1 location('p3_sp1.dmp'))
  4  as
  5    select customer_number, customer_name, postal_code
  6      from customer_list_xt partition (p3)
  7      where to_number(postal_code) < 50000;

Table created.

SQL>
SQL> create table customer_list_dp_p3_sp2_xt
  2  organization external
  3    (type oracle_datapump default directory def_dir1 location('p3_sp2.dmp'))
  4  as
  5    select customer_number, customer_name, postal_code
  6      from customer_list_xt partition (p3)
  7      where to_number(postal_code) >= 50000;

Table created.

SQL>
```

You can select from each of these external tables to verify that it has the data you intended to write out. After you have executed the SQL ` CREATE TABLE AS SELECT` statement, you can drop these external tables.

To use a virtual column to partition the table, create the partitioned `ORACLE_DATAPUMP` table. Again, the table is partitioned on the `customer_number` column and subpartitioned on the `postal_code` column. The `postal_code` column is a character field that contains numbers, but this example partitions it based on the numeric value, not a character string. In order to do this, create a virtual column, `postal_code_num,` whose value is the `postal_code` field converted to a `NUMBER` data type. The `SUBPARTITION` clause uses the virtual column to determine the subpartition for the row.

```
SQL> create table customer_list_dp_xt
  2  (customer_number    number,
  3   CUSTOMER_NAME      VARCHAR2(50),
  4   postal_code        CHAR(5),
  5   postal_code_NUM    as (to_number(postal_code)))
  6  organization external
  7    (type oracle_datapump default directory def_dir1)
  8  partition by range(customer_number)
  9  subpartition by range(postal_code_NUM)
 10  (
 11    partition p1 values less than (100)
 12     (subpartition p1_sp1 values less than (50000) location('p1_sp1.dmp'),
 13      subpartition p1_sp2 values less than (MAXVALUE) location('p1_sp2.dmp')),
 14    partition p2 values less than (200)
 15     (subpartition p2_sp1 values less than (50000) location('p2_sp1.dmp'),
 16      subpartition p2_sp2 values less than (MAXVALUE) location('p2_sp2.dmp')),
 17    partition p3 values less than (300)
 18     (subpartition p3_sp1 values less than (50000) location('p3_sp1.dmp'),
 19      subpartition p3_sp2 values less than (MAXVALUE) location('p3_sp2.dmp'))
 20  );

Table created.

SQL>
```

If you select all rows, then the data returned is the same as was returned in the previous example using the `ORACLE_LOADER` access driver.

```
SQL> select customer_number, customer_name, postal_code
  2    from customer_list_dp_xt
  3    order by customer_number;

customer_number CUSTOMER_NAME                                      POSTA
--------------- -------------------------------------------------- -----
              1  AAAAA Plumbing                                    01372
             13  Andi's Doughnuts                                  54570
             28  Sparkly Laundry                                   78907
             51  DIY Supplies                                      61614
             87  Fast Frames                                       22201
             89  Friendly Pharmacy                                 89901
            105  Le Bistrot du Chat Noir                           94114
            121  Pleasant Pets                                     33893
            130  Bailey the Bookmonger                             99915
            210  The Electric Eel Diner                            07101
            222  Everyt'ing General Store                          80118
            231  Big Rocket Market                                 01754

12 rows selected.

SQL>
```

The `WHERE` clause can limit the rows read to a subpartition. The following query should only read the first subpartition of the first partition.

```
SQL> select customer_number, customer_name, postal_code
  2    from customer_list_dp_xt
  3    where customer_number < 20 and postal_code_NUM < 39998
  4    order by customer_number;

customer_number CUSTOMER_NAME                                      POSTA
--------------- -------------------------------------------------- -----
              1  AAAAA Plumbing                                    01372

1 row selected.

SQL>
```

You could also specify a specific subpartition in the query, as follows:

```
SQL> select customer_number, customer_name, postal_code
  2    from customer_list_dp_xt subpartition (p2_sp2) order by customer_number;

customer_number CUSTOMER_NAME                                      POSTA
--------------- -------------------------------------------------- -----
            105  Le Bistrot du Chat Noir                           94114
            130  Bailey the Bookmonger                             99915

2 rows selected.

SQL>
```

**Parent topic:** External Tables Examples

### 18.4 Using the ORACLE\_BIGDATA Access Driver to Create Partitioned External Tables

The example in this section shows how to create a subpartitioned external table.

In the following example, we create a table called `SALES_EXTENDED_EXT` that has access to the table `sales_extended.parquet`, and the table `t.dat` that has access to the object store `tab_from_csv_oss`.

Example 18-4 Using the ORACLE\_BIGDATA Access Driver to create

```
CREATE TABLE "SALES_EXTENDED_EXT"
        ("PROD_ID" NUMBER(10,0),
     "CUST_ID" NUMBER(10,0),
     "TIME_ID" VARCHAR2(4000 BYTE),
     "CHANNEL_ID" NUMBER(10,0),
     "PROMO_ID" NUMBER(10,0),
     "QUANTITY_SOLD" NUMBER(10,0),
     "AMOUNT_SOLD" NUMBER(10,2),
     "GENDER" VARCHAR2(4000 BYTE),
     "CITY" VARCHAR2(4000 BYTE),
     "STATE_PROVINCE" VARCHAR2(4000 BYTE),
     "INCOME_LEVEL" VARCHAR2(4000 BYTE)
        )
        ORGANIZATION EXTERNAL
         ( TYPE ORACLE_BIGDATA
           DEFAULT DIRECTORY "DATA_PUMP_DIR"
           ACCESS PARAMETERS
           ( com.oracle.bigdata.credential.name=oss
             com.oracle.bigdata.fileformat=PARQUET
       )
           LOCATION
            ( 'https://objectstorage.eu-frankfurt-1.oraclecloud.com/n/adwc4pm/b/parquetfiles/o//sales_extended.parquet'
            )
         )
        REJECT LIMIT UNLIMITED
       PARALLEL ;

CREATE TABLE tab_from_csv_oss
     (
      c0 number,
      c1 varchar2(20)
     )
     ORGANIZATION external
     (
      TYPE oracle_bigdata
      DEFAULT DIRECTORY data_pump_dir
      ACCESS PARAMETERS
      (
       com.oracle.bigdata.fileformat=csv
       com.oracle.bigdata.credential.name=oci_swift
      )
      location
      (
       'https://objectstorage.us-sanjose-1.oraclecloud.com/n/axffbtla8jep/b/misc/o/t.dat'
      )
     )REJECT LIMIT 1
     ;
```

**Parent topic:** External Tables Examples

### 18.5 Loading LOBs From External Tables

External tables are particularly useful for loading large numbers of records from a single file, so that each record appears in its own row in the table.

The following example shows how to perform such a load.

Example 18-5 Loading LOBs From External Tables

Suppose you define an external table, `my_ext_table`, as follows:

```
CREATE TABLE my_ext_table ( id NUMBER, author VARCHAR2(30), created DATE, text CLOB )
ORGANIZATION EXTERNAL (
  TYPE ORACLE_LOADER
  DEFAULT DIRECTORY MY_DIRECTORY
  ACCESS PARAMETERS (
    RECORDS DELIMITED BY 0x'0A'
    FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
      ( id         CHAR(10),
        author     CHAR(30),
        created    DATE "YYYY-MM-DD",
        text       CHAR(131071)
      )
    )
    LOCATION (
      MY_DIRECTORY:'external.dmp'
    )
);
```

The contents of the `external.dmp` file are as follows:

```
1,Roger,2015-08-08,The quick brown fox jumps over the lazy dog
2,John,2012-01-01,"The angry aligator, acting alone, ate the antelope"
```

The second line in the dump file requires quotation marks around the full text string; otherwise the field would be terminated at the comma.

Note:

Although not a problem in the dump file being used in this example, if something in the full text string contained quotation marks, then you would enclose it in another set of quotation marks, as follows for the word `alone`:
```
2,John,2012-01-01,"The angry aligator, acting ""alone"", ate the antelope"
```

If the full text might contain the record delimiter character (0x'0A', or newline), you can specify a separate file for each document. External tables do not support filler fields, so instead you must use a ` COLUMN TRANSFORMS` clause to specify that the `fname` field contains the name of the external file:

```
DROP TABLE my_ext_table2;

CREATE TABLE my_ext_table2 ( id NUMBER, author VARCHAR2(30), created DATE, text CLOB )
ORGANIZATION EXTERNAL (
  TYPE ORACLE_LOADER
  DEFAULT DIRECTORY MY_DIRECTORY
  ACCESS PARAMETERS (
    RECORDS DELIMITED BY 0x'0A'
    FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
      ( id         CHAR(10),
        author     CHAR(30),
        created    DATE "YYYY-MM-DD",
        fname      char(100)
      )
    COLUMN TRANSFORMS (text FROM LOBFILE(fname) FROM (MY_DIRECTORY) )
    )
    LOCATION (
      'loader.txt'
    )
);
```

Note:

The `FROM (MY_DIRECTORY)` clause is not actually necessary since it has already been specified as the default directory. However it is being shown here for example purposes because if the `loader.txt` file and the individual CLOB files were in different locations, it would be needed.

Once the data is in an external table, you can either leave it there and perform normal table operations (DML and most DDL) on the external table, or you can use the external table as a staging table to get the data into a normal table. To create a new normal (non-external) table, you could use the following SQL statement:

```
CREATE TABLE normaltable AS SELECT * FROM externaltable;
```

You can similarly use the following SQL statement to insert data into the new normal table:

```
INSERT INTO normaltable AS SELECT * FROM externaltable;
```

**Parent topic:** External Tables Examples

### 18.6 Loading CSV Files From External Tables

This topic provides examples of how to load CSV files from external tables under various conditions.

Some of the examples build on previous examples.

Example 18-6 Loading Data From CSV Files With No Access Parameters

This example requires the following conditions:

- The order of the columns in the table must match the order of fields in the data file.
- The records in the data file must be terminated by newline.
- The field in the records in the data file must be separated by commas (if field values are enclosed in quotation marks, then the quotation marks are not removed from the field).
- There cannot be any newline characters in the middle of a field.

The data for the external table is as follows:

```
events_all.csv
Winter Games,10-JAN-2010,10,
Hockey Tournament,18-MAR-2009,3,
Baseball Expo,28-APR-2009,2,
International Football Meeting,2-MAY-2009,14,
Track and Field Finale,12-MAY-2010,3,
Mid-summer Swim Meet,5-JUL-2010,4,
Rugby Kickoff,28-SEP-2009,6,
```

The definition of the external table is as follows:

```
SQL> CREATE TABLE EVENTS_XT_1
  2  (EVENT       varchar2(30),
  3   START_DATE  date,
  4   LENGTH      number)
  5  ORGANIZATION EXTERNAL
  6  (default directory def_dir1 location ('events_all.csv'));

Table created.
```

The following shows a `SELECT` operation on the external table `EVENTS_XT_1`:

```
SQL> select START_DATE, EVENT, LENGTH
  2    from EVENTS_XT_1
  3    order by START_DATE;

START_DAT EVENT                              LENGTH
--------- ------------------------------ ----------
18-MAR-09 Hockey Tournament                       3
28-APR-09 Baseball Expo                           2
02-MAY-09 International Football Meeting         14
28-SEP-09 Rugby Kickoff                           6
10-JAN-10 Winter Games                           10
12-MAY-10 Track and Field Finale                  3
05-JUL-10 Mid-summer Swim Meet                    4

7 rows selected.

SQL>
```

Example 18-7 Default Date Mask For the Session Does Not Match the Format of Data Fields in the Data File

This example is the same as the previous example, except that the default date mask for the session does not match the format of date fields in the data file. In the example below, the session format for dates is ` DD-Mon-YYYY` whereas the format of dates in the data file is `MM/DD/YYYY`. If the external table definition does not have a date mask, then the `ORACLE_LOADER` access driver uses the session date mask to attempt to convert the character data in the data file to a date data type. ou specify an access parameter for the date mask to use for all fields in the data file that are used to load date columns in the external table.

The following is the contents of the data file for the external table:

```
events_all_date_fmt.csv
Winter Games,1/10/2010,10
Hockey Tournament,3/18/2009,3
Baseball Expo,4/28/2009,2
International Football Meeting,5/2/2009,14
Track and Field Finale,5/12/2009,3
Mid-summer Swim Meet,7/5/2010,4
Rugby Kickoff,9/28/2009,6
```

The definition of the external table is as follows:

```
SQL> CREATE TABLE EVENTS_XT_2
  2  (EVENT       varchar2(30),
  3   START_DATE  date,
  4   LENGTH      number)
  5  ORGANIZATION EXTERNAL
  6  (default directory def_dir1
  7   access parameters (fields date_format date mask "mm/dd/yyyy")
  8   location ('events_all_date_fmt.csv'));

Table created.

SQL>
```

The following shows a `SELECT` operation on the external table `EVENTS_XT_2:`

```
SQL> select START_DATE, EVENT, LENGTH
  2    from EVENTS_XT_2
  3    order by START_DATE;

START_DAT EVENT                              LENGTH
--------- ------------------------------ ----------
18-MAR-09 Hockey Tournament                       3
28-APR-09 Baseball Expo                           2
02-MAY-09 International Football Meeting         14
12-MAY-09 Track and Field Finale                  3
28-SEP-09 Rugby Kickoff                           6
10-JAN-10 Winter Games                           10
05-JUL-10 Mid-summer Swim Meet                    4

7 rows selected.
```

Example 18-8 Data is Split Across Two Data Files

This example is that same as the first example in this section except for the following:

- The data is split across two data files.
- Each data file has a row containing the names of the fields.
- Some fields in the data file are enclosed by quotation marks.

The `FIELD NAMES ALL FILES` tells the access driver that the first row in each file contains a row with names of the fields in the file. The access driver matches the names of the fields to the names of the columns in the table. This means the order of the fields in the file can be different than the order of the columns in the table. If a field name in the first row is not enclosed in quotation marks, then the access driver uppercases the name before trying to find the matching column name in the table. If the field name is enclosed in quotation marks, then it does not change the case of the names before looking for a matching name.

Because the fields are enclosed in quotation marks, the access parameter requires the `CSV WITHOUT EMBEDDED RECORD TERMINATORS` clause. This clause states the following:

- Fields in the data file are separated by commas.
- If the fields are enclosed in double quotation marks, then the access driver removes them from the field value.
- There are no new lines embedded in the field values (this option allows the access driver to skip some checks that can slow the performance of `SELECT` operations on the external table).

The two data files are as follows:

```
events_1.csv

"EVENT","START DATE","LENGTH",
"Winter Games", "10-JAN-2010", "10"
"Hockey Tournament", "18-MAR-2009", "3"
"Baseball Expo", "28-APR-2009", "2"
"International Football Meeting", "2-MAY-2009", "14"
```
```
events_2.csv

Event,Start date,Length,
Track and Field Finale, 12-MAY-2009, 3
Mid-summer Swim Meet, 5-JUL-2010, 4
Rugby Kickoff, 28-SEP-2009, 6
```

The external table definition is as follows:

```
SQL> CREATE TABLE EVENTS_XT_3
  2  ("START DATE"  date,
  3   EVENT         varchar2(30),
  4   LENGTH        number)
  5  ORGANIZATION EXTERNAL
  6  (default directory def_dir1
  7   access parameters (records field names all files
  8                      fields csv without embedded record terminators)
  9   location ('events_1.csv', 'events_2.csv'));

Table created.
```

The following shows the result of a `SELECT` operation on the `EVENTS_XT_3` external table:

```
SQL> select "START DATE", EVENT, LENGTH
  2    from EVENTS_XT_3
  3    order by "START DATE";

START DAT EVENT                              LENGTH
--------- ------------------------------ ----------
18-MAR-09 Hockey Tournament                       3
28-APR-09 Baseball Expo                           2
02-MAY-09 International Football Meeting         14
12-MAY-09 Track and Field Finale                  3
28-SEP-09 Rugby Kickoff                           6
10-JAN-10 Winter Games                           10
05-JUL-10 Mid-summer Swim Meet                    4

7 rows selected.
```

Example 18-9 Data Is Split Across Two Files and Only the First File Has a Row of Field Names

This example is the same as example 3 except that only the 1st file has a row of field names. The first row of the second file has real data. The RECORDS clause changes to "field names first file".

The two data files are as follows:

```
events_1.csv (same as for example 3)

"EVENT","START DATE","LENGTH",
"Winter Games", "10-JAN-2010", "10"
"Hockey Tournament", "18-MAR-2009", "3"
"Baseball Expo", "28-APR-2009", "2"
"International Football Meeting", "2-MAY-2009", "14"
```
```
events_2_no_header_row.csv

Track and Field Finale, 12-MAY-2009, 3
Mid-summer Swim Meet, 5-JUL-2010, 4
Rugby Kickoff, 28-SEP-2009, 6
```

The external table definition is as follows:

```
SQL> CREATE TABLE EVENTS_XT_4
  2  ("START DATE"  date,
  3   EVENT         varchar2(30),
  4   LENGTH        number)
  5  ORGANIZATION EXTERNAL
  6  (default directory def_dir1
  7   access parameters (records field names first file
  8                      fields csv without embedded record terminators)
  9   location ('events_1.csv', 'events_2_no_header_row.csv'));

Table created.
```

The following shows a `SELECT` operation on the `EVENTS_XT_4` external table:

```
SQL> select "START DATE", EVENT, LENGTH
  2    from EVENTS_XT_4
  3    order by "START DATE";

START DAT EVENT                              LENGTH
--------- ------------------------------ ----------
18-MAR-09 Hockey Tournament                       3
28-APR-09 Baseball Expo                           2
02-MAY-09 International Football Meeting         14
12-MAY-09 Track and Field Finale                  3
28-SEP-09 Rugby Kickoff                           6
10-JAN-10 Winter Games                           10
05-JUL-10 Mid-summer Swim Meet                    4

7 rows selected.
```

Example 18-10 The Order of the Fields in the File Match the Order of the Columns in the Table

This example has the following conditions:

- The order of the fields in the file match the order of the columns in the table.
- Fields are separated by newlines and are optionally enclosed in double quotation marks.
- There are fields that have embedded newlines in their value and those fields are enclosed in double quotation marks.

The contents of the data files are as follows:

```
event_contacts_1.csv

Winter Games, 10-JAN-2010, Ana Davis,
Hockey Tournament, 18-MAR-2009, "Daniel Dube
Michel Gagnon",
Baseball Expo, 28-APR-2009, "Robert Brown"
Internation Football Meeting, 2-MAY-2009,"Pete Perez
Randall Barnes
Melissa Gray",
```
```
event_contacts_2.csv

Track and Field Finale, 12-MAY-2009, John Taylor,
Mid-summer Swim Meet, 5-JUL-2010, "Louise Stewart
Cindy Sanders"
Rugby Kickoff, 28-SEP-2009, "Don Nguyen
Ray Lavoie"
```

The table definition is as follows. The `CSV WITH EMBEDDED RECORD TERMINATORS` clause tells the access driver how to handle fields enclosed by double quotation marks that also have embedded new lines.

```
SQL> CREATE TABLE EVENTS_CONTACTS_1
  2  (EVENT       varchar2(30),
  3   START_DATE  date,
  4   CONTACT     varchar2(120))
  5  ORGANIZATION EXTERNAL
  6  (default directory def_dir1
  7   access parameters (fields CSV with embedded record terminators)
  8   location ('event_contacts_1.csv', 'event_contacts_2.csv'));

Table created.
```

The following shows the result of a `SELECT` operation on the `EVENT_CONTACTS_1` external table:

```
SQL> column contact format a30 
SQL> select START_DATE, EVENT, CONTACT
  2    from EVENTS_CONTACTS_1
  3    order by START_DATE;

START_DAT EVENT                          CONTACT
--------- ------------------------------ ------------------------------
18-MAR-09 Hockey Tournament              Daniel Dube
                                         Michel Gagnon

28-APR-09 Baseball Expo                  Robert Brown
02-MAY-09 Internation Football Meeting   Pete Perez
                                         Randall Barnes
                                         Melissa Gray

12-MAY-09 Track and Field Finale         John Taylor
28-SEP-09 Rugby Kickoff                  Don Nguyen
                                         Ray Lavoie

10-JAN-10 Winter Games                   Ana Davis
05-JUL-10 Mid-summer Swim Meet           Louise Stewart
                                         Cindy Sanders

7 rows selected.
```

Example 18-11 Not All Fields in the Data File Use Default Settings for the Access Parameters

This example shows what to do when most field in the data file use default settings for the access parameters but a few do not. Instead of listing the setting for all fields, this example shows how you can set attributes for just the fields that are different from the default. The differences are as follows:

- there are two date fields, one of which uses the session format, but `registration_deadline` uses a different format
- `registration_deadline` also uses a value of `NONE` to indicate a null value.

The content of the data file is as follows:

```
events_reg.csv

Winter Games,10-JAN-2010,10,12/1/2009,
Hockey Tournament,18-MAR-2009,3,3/11/2009,
Baseball Expo,28-APR-2009,2,NONE
International Football Meeting,2-MAY-2009,14,3/1/2009
Track and Field Finale,12-MAY-2010,3,5/10/010
Mid-summer Swim Meet,5-JUL-2010,4,6/20/2010
Rugby Kickoff,28-SEP-2009,6,NONE
```

The table definition is as follows. The `ALL FIELDS OVERRIDE` clause allows you to specify information for that field while using defaults for the remaining fields. The remaining fields have a data type of `CHAR(255)` and the field data is terminated by a comma with a trimming option of `LDRTRIM`.

```
SQL> CREATE TABLE EVENT_REGISTRATION_1
  2  (EVENT                 varchar2(30),
  3   START_DATE            date,
  4   LENGTH                number,
  5   REGISTRATION_DEADLINE date)
  6  ORGANIZATION EXTERNAL
  7  (default directory def_dir1
  8   access parameters
  9  (fields all fields override
 10     (REGISTRATION_DEADLINE CHAR (10) DATE_FORMAT DATE MASK "mm/dd/yyyy"
 11                           NULLIF REGISTRATION_DEADLINE = 'NONE'))
 12   location ('events_reg.csv'));

Table created.
```

The following shows the result of a `SELECT` operation on the `EVENT_REGISTRATION_1` external table:

```
SQL> select START_DATE, EVENT, LENGTH, REGISTRATION_DEADLINE
  2    from EVENT_REGISTRATION_1
  3    order by START_DATE;

START_DAT EVENT                              LENGTH REGISTRAT
--------- ------------------------------ ---------- ---------
18-MAR-09 Hockey Tournament                       3 11-MAR-09
28-APR-09 Baseball Expo                           2
02-MAY-09 International Football Meeting         14 01-MAR-09
28-SEP-09 Rugby Kickoff                           6
10-JAN-10 Winter Games                           10 01-DEC-09
12-MAY-10 Track and Field Finale                  3 10-MAY-10
05-JUL-10 Mid-summer Swim Meet                    4 20-JUN-10

7 rows selected.
```

**Parent topic:** External Tables Examples