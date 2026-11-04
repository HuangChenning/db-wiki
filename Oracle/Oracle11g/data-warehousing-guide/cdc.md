---
title: Change Data Capture
book: Data Warehousing Guide
doc_id: E25554-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e25554/cdc.htm
tags:
  - oracle
  - 11g
  - data-warehousing-guide
---

## 17 Change Data Capture

Change Data Capture efficiently identifies and captures data that has been added to, updated in, or removed from, Oracle relational tables and makes this change data available for use by applications or individuals.

Note:

Oracle Change Data Capture will be de-supported in a future release of Oracle Database and will be replaced with Oracle GoldenGate. Therefore, Oracle strongly recommends that you use Oracle GoldenGate for new applications.

For Oracle Database 11g Release 2 (11.2), Change Data Capture continues to function as in earlier releases. If you are currently using Change Data Capture, then you will be able to continue to do so for the foreseeable future. However, Change Data Capture will not be further enhanced, and will only be supported based on the current, documented functionality.

This chapter describes Change Data Capture in the following sections:

See [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for reference information about the Change Data Capture publish and subscribe PL/SQL packages.

## Overview of Change Data Capture

Often, data warehousing involves the extraction and transportation of relational data from one or more production databases into a data warehouse for analysis. Change Data Capture quickly identifies and processes only the data that has changed and makes the change data available for further use.

### Capturing Change Data Without Change Data Capture

Prior to the introduction of Change Data Capture, there were a number of ways that users could capture change data, including table differencing and change-value selection.

Table differencing involves transporting a copy of an entire table from the source (production) database to the staging database (where the change data is captured), where an older version of the table already exists. Using the SQL `MINUS` operator, you can obtain the inserted and new versions of updated rows with the following query:

```
SELECT * FROM new_version 
MINUS SELECT * FROM old_version;
```

Moreover, you can obtain the deleted rows and old versions of updated rows with the following query:

```
SELECT * FROM old_version 
MINUS SELECT * FROM new_version;
```

However, there are several problems with this method:

- It requires that the new version of the entire table be transported to the staging database, not just the change data, thereby greatly increasing transport costs.
- The computational cost of performing the two `MINUS` operations on the staging database can be very high.
- Table differencing cannot capture data that have reverted to their old values. For example, suppose the price of a product changes several times between the old version and the new version of the product's table. If the price in the new version ends up being the same as the old, table differencing cannot detect that the price has fluctuated. Moreover, any intermediate price values between the old and new versions of the product's table cannot be captured using table differencing.
- There is no way to determine which changes were made as part of the same transaction. For example, suppose a sales manager creates a special discount to close a deal. The fact that the creation of the discount and the creation of the sale occurred as part of the same transaction cannot be captured, unless the source database is specifically designed to do so.

Change-value selection involves capturing the data on the source database by selecting the new and changed data from the source tables based on the value of a specific column. For example, suppose the source table has a `LAST_UPDATE_DATE` column. To capture changes, you base your selection from the source table on the `LAST_UPDATE_DATE` column value.

However, there are also several limitations with this method:

- The overhead of capturing the change data must be borne on the source database, and you must run potentially expensive queries against the source table on the source database. The need for these queries may force you to add indexes that would otherwise be unneeded. There is no way to offload this overhead to the staging database.
- This method is no better at capturing intermediate values than the table differencing method. If the price in the product's table fluctuates, you will not be able to capture all the intermediate values, or even tell if the price had changed, if the ending value is the same as it was the last time that you captured change data.
- This method is also no better than the table differencing method at capturing which data changes were made together in the same transaction. If you need to capture information concerning which changes occurred together in the same transaction, you must include specific designs for this purpose in your source database.
- The granularity of the change-value column may not be fine enough to uniquely identify the new and changed rows. For example, suppose the following:
	- You capture data changes using change-value selection on a date column such as `LAST_UPDATE_DATE`.
		- The capture happens at a particular instant in time, 14-FEB-2003 17:10:00.
		- Additional updates occur to the table during the same second that you performed your capture.
	When you next capture data changes, you will select rows with a `LAST_UPDATE_DATE` strictly after 14-FEB-2003 17:10:00, and thereby miss the changes that occurred during the remainder of that second.
	To use change-value selection, you either have to accept that anomaly, add an artificial change-value column with the granularity you need, or lock out changes to the source table during the capture process, thereby further burdening the performance of the source database.
- You have to design your source database in advance with this capture mechanism in mind – all tables from which you wish to capture change data must have a change-value column. If you want to build a data warehouse with data sources from legacy systems, those legacy systems may not supply the necessary change-value columns you need.

Change Data Capture does not depend on expensive and cumbersome table differencing or change-value selection mechanisms. Instead, it captures the change data resulting from `INSERT`, `UPDATE`, and `DELETE` operations made to user tables. The change data is then stored in a relational table called a change table, and the change data is made available to applications or individuals in a controlled way.

### Capturing Change Data with Change Data Capture

Change Data Capture can capture and publish committed change data in either of the following modes:

- Synchronous
	Triggers on the source database allow change data to be captured immediately, as each SQL statement that performs a data manipulation language (DML) operation (`INSERT`, `UPDATE`, or `DELETE`) is made. In this mode, change data is captured as part of the transaction modifying the source table. Synchronous Change Data Capture is available with Oracle Standard Edition and Enterprise Edition. This mode is described in detail in "Synchronous Change Data Capture".
- Asynchronous
	By taking advantage of the data sent to the redo log files, change data is captured after a SQL statement that performs a DML operation is committed. In this mode, change data is not captured as part of the transaction that is modifying the source table, and therefore has no effect on that transaction.
	There are three modes of asynchronous Change Data Capture: HotLog, Distributed HotLog, and AutoLog. These modes are described in detail in "Asynchronous Change Data Capture".
	Asynchronous Change Data Capture is built on, and provides a relational interface to, Oracle Streams. See [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/toc.htm) for information on Oracle Streams.

The following list describes the advantages of capturing change data with Change Data Capture:

- Completeness
	Change Data Capture can capture all effects of `INSERT`, `UPDATE`, and `DELETE` operations, including data values before and after `UPDATE` operations.
- Performance
	Asynchronous Change Data Capture can be configured to have minimal performance impact on the source database.
- Interface
	Change Data Capture includes the `DBMS_CDC_PUBLISH` and `DBMS_CDC_SUBSCRIBE` packages, which provide easy-to-use publish and subscribe interfaces.
- Cost
	Change Data Capture reduces overhead cost because it simplifies the extraction of change data from the database and is part of the Oracle Database.

Note that you cannot use any table that uses transparent data encryption as a source table for synchronous Change Data Capture. Asynchronous Change Data Capture supports transparent data encryption if both the source and staging databases have `COMPATIBLE` set to 11 or higher. Change Data Capture does not encrypt the data in the change table. A user who wants to encrypt a column in the change table can manually use an `ALTER` `TABLE` statement to encrypt the column in the change table. See [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/toc.htm) for information on Oracle Streams.

A Change Data Capture system is based on the interaction of publishers and subscribers to capture and distribute change data, as described in the next section.

### Publish and Subscribe Model

Most Change Data Capture systems have one person who captures and publishes change data; this person is the [publisher](glossary.md). There can be multiple applications or individuals that access the change data; these applications and individuals are the [subscribers](glossary.md). Change Data Capture provides PL/SQL packages to accomplish the publish and subscribe tasks.

The following sections describe the roles of the publisher and subscriber in detail. Subsequent sections describe change sources, more about modes of Change Data Capture, and change tables.

#### Publisher

The publisher is usually a database administrator (DBA) who creates and maintains the schema objects that make up the Change Data Capture system. For all modes of Change Data Capture, except Distributed HotLog, there is typically one publisher on the staging database. For the Distributed HotLog mode of Change Data Capture there needs to be a publisher defined on the source and staging databases. The following list describes the source and staging databases and the objects of interest to Change Data Capture on each:

- Source database
	This is the production database that contains the data of interest. The following objects of interest to Change Data Capture reside on the source database:
	- The source tables
		The [source tables](glossary.md) are the production database tables that contain the data of interest. They may be all or a subset of the source database tables.
		- Redo log files
		For asynchronous modes of change data capture, the change data is collected from either the online or archived redo log files (or both). For asynchronous AutoLog mode, archived redo log files are copied from the source database to the staging database.
		- Change source
		The change source is a logical representation of the source database. The method for representing the source varies, depending on the mode of Change Data Capture.
		For the asynchronous Distributed HotLog mode of Change Database capture only, the change source resides on the source database. For the other modes of Change Data Capture, the change source resides on the staging database.
		See "Asynchronous Distributed HotLog Mode" for details about the Distributed HotLog change source.
- Staging database
	This is the database to which the captured change data is applied. Depending on the capture mode that the publisher uses, the staging database can be the same as, or different from, the source database. The following Change Data Capture objects reside on the staging database:
	- Change table
		A [change table](glossary.md) is a relational table into which change data for a single source table is loaded. To subscribers, a change table is known as a [publication](glossary.md).
		- Change set
		A [change set](glossary.md) is a set of change data that is guaranteed to be transactionally consistent. It contains one or more change tables.
		- Change source
		The change source for the following modes of Change Data Capture reside on the staging database:
		- Synchronous - See "Synchronous Change Data Capture" for details.
				- Asynchronous HotLog - See "Asynchronous HotLog Mode" for details.
				- Asynchronous AutoLog - See "Asynchronous AutoLog Mode" for details.

These are the main tasks performed by the publisher:

- Determines the source databases and tables from which the subscribers are interested in viewing change data, and the mode (synchronous or one of the asynchronous modes) in which to capture the change data.
- Uses the Oracle-supplied package, `DBMS_CDC_PUBLISH`, to set up the system to capture change data from the source tables of interest.
- Allows subscribers to have controlled access to the change data in the change tables by using the SQL `GRANT` and `REVOKE` statements to grant and revoke the `SELECT` privilege on change tables for users and roles. (Keep in mind, however, that subscribers use views, not change tables directly, to access change data.)

In Figure 17-1, the publisher determines that subscribers are interested in viewing change data from the `HQ` source database. In particular, subscribers are interested in change data from the `sh.sales` and `sh.promotions` source tables.

The publisher decides to use the asynchronous AutoLog mode of capturing change data. On the `DW` staging database, he creates a change source `HQ_SRC`, a change set, `SH_SET`, and two change tables: `sales_ct` and `promo_ct`. The `sales_ct` change table contains all the columns from the source table, `sh.sales`. For the `promo_ct` change table, however, the publisher has decided to exclude the `PROMO_COST` column.

Figure 17-1 Publisher Components in a Change Data Capture System

![Description of Figure 17-1 follows](https://docs.oracle.com/cd/E11882_01/server.112/e25554/dwhsg127.gif)  
[Description of "Figure 17-1 Publisher Components in a Change Data Capture System"](https://docs.oracle.com/cd/E11882_01/server.112/e25554/img_text/dwhsg127.htm)  

#### Subscribers

The subscribers are consumers of the published change data. A subscriber performs the following tasks:

- Uses the Oracle supplied package, `DBMS_CDC_SUBSCRIBE`, to:
	- Create subscriptions
		A [subscription](glossary.md) controls access to the change data from one or more source tables of interest within a single change set. A subscription contains one or more subscriber views.
		A subscriber view is a view that specifies the change data from a specific publication in a subscription. The subscriber is restricted to seeing change data that the publisher has published and has granted the subscriber access to use. See "Subscribing to Change Data" for more information on choosing a method for specifying a subscriber view.
		- Notify Change Data Capture when ready to receive a set of change data
		A [subscription window](glossary.md) defines the time range of rows in a publication that the subscriber can currently see in subscriber views. The oldest row in the window is called the [low boundary](glossary.md); the newest row in the window is called the [high boundary](glossary.md). Each subscription has its own subscription window that applies to all of its subscriber views.
		- Notify Change Data Capture when finished with a set of change data
- Uses `SELECT` statements to retrieve change data from the subscriber views.

A subscriber has the privileges of the user account under which the subscriber is running, plus any additional privileges that have been granted to the subscriber.

In Figure 17-2, the subscriber is interested in a subset of columns that the publisher (in Figure 17-1) has published. Note that the publications shown in Figure 17-2, are represented as change tables in Figure 17-1; this reflects the different terminology used by subscribers and publishers, respectively.

The subscriber creates a subscription, `sales_promos_list` and two subscriber views (`spl_sales` and `spl_promos`) on the `SH_SET` change set on the DW staging database. Within each subscriber view, the subscriber includes a subset of the columns that were made available by the publisher. Note that because the publisher did not create a change table that includes the `PROMO_COST` column, there is no way for the subscriber to view change data for that column. The subscriber need not be aware of the mode of change data capture employed by the publisher.

Figure 17-2 Subscriber Components in a Change Data Capture System

![Description of Figure 17-2 follows](https://docs.oracle.com/cd/E11882_01/server.112/e25554/dwhsg128.gif)  
[Description of "Figure 17-2 Subscriber Components in a Change Data Capture System"](https://docs.oracle.com/cd/E11882_01/server.112/e25554/img_text/dwhsg128.htm)  

Change Data Capture provides the following benefits for subscribers:

- Guarantees that each subscriber sees all the changes
- Keeps track of multiple subscribers and gives each subscriber shared access to change data
- Handles all the storage management by automatically removing data from change tables when it is no longer required by any of the subscribers. Keep in mind that Change Data Capture starts a job in the job queue that runs once every 24 hours for handling purging. Many things can go wrong with this job (such as if it is deleted or the schedule is changed), so this automatic processing depends on the job queue process being up and running and the Change Data Capture job being there. Also, in logical standby environments, the purge job is not submitted.
	Note:
	Oracle provides the previously listed benefits only when the subscriber accesses change data through a subscriber view.

## Change Sources and Modes of Change Data Capture

Change Data Capture provides synchronous and asynchronous modes for capturing change data. The following sections summarize how each mode of Change Data Capture is performed, and the change source associated with each mode of Change Data Capture.

### Synchronous Change Data Capture

The synchronous mode uses triggers on the source database to capture change data. It has no latency because the change data is captured continuously and in real time on the source database. The change tables are populated when DML operations on the source table are committed.

There is a single, predefined synchronous change source, `SYNC_SOURCE`, that represents the source database. This is the only synchronous change source. It cannot be altered or dropped.

While the synchronous mode of Change Data Capture adds overhead to the source database at capture time, this mode can reduce costs (as compared to attempting to extract change data using table differencing or change-value section) by simplifying the extraction of change data.

Change tables for this mode of Change Data Capture must reside locally in the source database.

Figure 17-3 illustrates the synchronous configuration. Triggers executed after DML operations occur on the source tables populate the change tables in the change sets within the `SYNC_SOURCE` change source.

Figure 17-3 Synchronous Change Data Capture Configuration

![Description of Figure 17-3 follows](https://docs.oracle.com/cd/E11882_01/server.112/e25554/dwhsg124.gif)  
[Description of "Figure 17-3 Synchronous Change Data Capture Configuration"](https://docs.oracle.com/cd/E11882_01/server.112/e25554/img_text/dwhsg124.htm)  

### Asynchronous Change Data Capture

The asynchronous modes capture change data from the database redo log files after changes have been committed to the source database.

The asynchronous modes of Change Data Capture are dependent on the level of supplemental logging enabled at the source database. Supplemental logging adds redo logging overhead at the source database, so it must be carefully balanced with the needs of the applications or individuals using Change Data Capture. See "Asynchronous Change Data Capture and Supplemental Logging" for information on supplemental logging.

The three modes of capturing change data are described in the following sections:

- Asynchronous HotLog Mode
- Asynchronous Distributed HotLog Mode
- Asynchronous AutoLog Mode

#### Asynchronous HotLog Mode

In the asynchronous HotLog mode, change data is captured from the online redo log file on the source database. There is a brief latency between the act of committing source table transactions and the arrival of change data.

There is a single, predefined HotLog change source, `HOTLOG_SOURCE`, that represents the current online redo log files of the source database. This is the only HotLog change source. It cannot be altered or dropped.

Change tables for this mode of Change Data Capture must reside locally in the source database.

Figure 17-4 illustrates the asynchronous HotLog configuration. The Logwriter Process (`LGWR`) records committed transactions in the online redo log files on the source database. Change Data Capture uses Oracle Streams processes to automatically populate the change tables in the change sets within the `HOTLOG_SOURCE` change source as newly committed transactions arrive.

Figure 17-4 Asynchronous HotLog Configuration

![Description of Figure 17-4 follows](https://docs.oracle.com/cd/E11882_01/server.112/e25554/dwhsg123.gif)  
[Description of "Figure 17-4 Asynchronous HotLog Configuration"](https://docs.oracle.com/cd/E11882_01/server.112/e25554/img_text/dwhsg123.htm)  

#### Asynchronous Distributed HotLog Mode

In the asynchronous Distributed HotLog mode, change data is captured from the online redo log file on the source database.

There is no predefined Distributed HotLog change source. Unlike other modes of Change Data Capture, the Distributed HotLog mode splits change data capture activities and objects across the source and staging database. Change sources are defined on the source database by the staging database publisher.

A Distributed HotLog change source represents the current online redo log files of the source database. However, staging database publishers can define multiple Distributed HotLog change sources, each of which contains change sets on a different staging database. The source and staging database can be on different hardware platforms and be running different operating systems, however some restrictions apply. See "Summary of Supported Distributed HotLog Configurations and Restrictions" for information on these restrictions.

Figure 17-5 illustrates the asynchronous Distributed HotLog configuration. The change source on the source database captures change data from the online redo log files and uses Streams to propagate it to the change set on the staging database. The change set on the staging database populates the change tables within the change set.

There are two publishers required for this mode of Change Data Capture, one on the source database and one on the staging database. The source database publisher defines a database link on the source database to connect to the staging database as the staging database publisher. The staging database publisher defines a database link on the staging database to connect to the source database on the source database publisher. All publishing operations are performed by the staging database publisher. See "Performing Asynchronous Distributed HotLog Publishing" for details.

Figure 17-5 Asynchronous Distributed HotLog Configuration

![Description of Figure 17-5 follows](https://docs.oracle.com/cd/E11882_01/server.112/e25554/dwhsg126.gif)  
[Description of "Figure 17-5 Asynchronous Distributed HotLog Configuration"](https://docs.oracle.com/cd/E11882_01/server.112/e25554/img_text/dwhsg126.htm)  

#### Asynchronous AutoLog Mode

In the asynchronous AutoLog mode, change data is captured from a set of redo log files managed by redo transport services. Redo transport services control the automated transfer of redo log files from the source database to the staging database. Using database initialization parameters (described in "Initialization Parameters for Asynchronous AutoLog Publishing"), the publisher configures redo transport services to copy the redo log files from the source database system to the staging database system and to automatically register the redo log files. Asynchronous AutoLog mode can obtain change data from either the source database online redo log or from source database archived redo logs. These options are known as asynchronous AutoLog online and asynchronous AutoLog archive.With the AutoLog online option, redo transport services is set up to copy redo data from the online redo log at the source database to the standby redo log at the staging database. Change sets are populated after individual source database transactions commit. There can only be one AutoLog online change source on a given staging database and it can contain only one change set.With the AutoLog archive option, redo transport services is set up to copy archived redo logs from the source database to the staging database. Change sets are populated as new archived redo log files arrive on the staging database. The degree of latency depends on the frequency of redo log file switches on the source database. The AutoLog archive option has a higher degree of latency than the AutoLog online option, but there can be as many AutoLog archive change sources as desired on a given staging database.

There is no predefined AutoLog change source. The publisher provides information about the source database to create an AutoLog change source. See "Performing Asynchronous AutoLog Publishing" for details.

Figure 17-6 shows a Change Data Capture asynchronous AutoLog online configuration in which the LGWR process on the source database copies redo data to both the online redo log file on the source database and to the standby redo log files on the staging database as specified by the `LOG_ARCHIVE_DEST_2` parameter. (Although the image presents this parameter as `LOG_ARCHIVE_DEST_2`, the integer value can be any value between 1 and 10.)

Note that the LGWR process uses Oracle Net to send redo data over the network to the remote file server (RFS) process. Transmitting redo data to a remote destination requires uninterrupted connectivity through Oracle Net.

On the staging database, the RFS process writes the redo data to the standby redo log files. Then, Change Data Capture uses Oracle Streams downstream capture to populate the change tables in the change sets within the AutoLog change source.

The source database and the staging database must be running on the same hardware, operating system, and Oracle version.

Figure 17-6 Asynchronous Autolog Online Change Data Capture Configuration

![Description of Figure 17-6 follows](https://docs.oracle.com/cd/E11882_01/server.112/e25554/dwhsg122.gif)  
[Description of "Figure 17-6 Asynchronous Autolog Online Change Data Capture Configuration"](https://docs.oracle.com/cd/E11882_01/server.112/e25554/img_text/dwhsg122.htm)  

Figure 17-7 shows a typical Change Data Capture asynchronous AutoLog archive configuration in which, when the redo log file switches on the source database, archiver processes archive the redo log file on the source database to the destination specified by the `LOG_ARCHIVE_DEST_1` parameter and copy the redo log file to the staging database as specified by the `LOG_ARCHIVE_DEST_2` parameter. (Although the image presents these parameters as `LOG_ARCHIVE_DEST_1` and `LOG_ARCHIVE_DEST_2`, the integer value in these parameter strings can be any value between 1 and 10.)

Note that the archiver processes use Oracle Net to send redo data over the network to the remote file server (RFS) process. Transmitting redo log files to a remote destination requires uninterrupted connectivity through Oracle Net.

On the staging database, the RFS process writes the redo data to the copied log files. Then, Change Data Capture uses Oracle Streams downstream capture to populate the change tables in the change sets within the AutoLog change source.

See [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/toc.htm) for more information regarding Redo Transport Services.

Figure 17-7 Asynchronous AutoLog Archive Change Data Capture Configuration

![Description of Figure 17-7 follows](https://docs.oracle.com/cd/E11882_01/server.112/e25554/dwhsg125.gif)  
[Description of "Figure 17-7 Asynchronous AutoLog Archive Change Data Capture Configuration"](https://docs.oracle.com/cd/E11882_01/server.112/e25554/img_text/dwhsg125.htm)  

## Change Sets

A change set is a logical grouping of change data that is guaranteed to be transactionally consistent and that can be managed as a unit. A change set is a member of one (and only one) change source.

Note:

Change Data Capture change sources can contain one or more change sets with the following restrictions:
1. All of the change sets for a Distributed HotLog change source must be on the same staging database
2. An AutoLog online change source can only contain one change set

When a publisher includes two or more change tables in the same change set, subscribers can perform join operations across the tables represented within the change set and be assured of transactional consistency.

Conceptually, a change set shares the same mode as its change source. For example, an AutoLog change set is a change set contained in an AutoLog change source. Publishers define change sets using the `DBMS_CDC_PUBLISH.CREATE_CHANGE_SET` package. In the case of synchronous Change Data Capture, the publisher can also use a predefined change set, `SYNC_SET`. The `SYNC_SET` change set, however, cannot be altered or dropped.

To keep the change tables in the change set from growing larger indefinitely, publishers can purge unneeded change data from change tables at the change set level. See "Purging Change Tables of Unneeded Data" for more information on purging change data.

### Valid Combinations of Change Sources and Change Sets

Table 17-1 summarizes the valid combinations of change sources and change sets and indicates whether each is predefined or publisher-defined. In addition, it indicates whether the source database represented by the change source is local to or remote from the staging database, and whether the change source is used for synchronous or asynchronous Change Data Capture.

Table 17-1 Summary of Change Sources and Change Sets

| Mode | Change Source | Source Database Represented | Associated Change Sets |
| --- | --- | --- | --- |
| Synchronous | Predefined `SYNC_SOURCE` | Local | Predefined `SYNC_SET` and publisher-defined |
| Asynchronous HotLog | Predefined `HOTLOG_SOURCE` | Local | Publisher-defined |
| Asynchronous Distributed HotLog | Publisher-defined | Remote | Publisher-defined. Change sets must all be on the same staging database |
| Asynchronous AutoLog online | Publisher-defined | Remote | Publisher-defined. There can only be one change set in an AutoLog online change source |
| Asynchronous AutoLog archive | Publisher-defined | Remote | Publisher-defined |

## Change Tables

A given change table contains the change data resulting from DML operations performed on a given source table. A change table consists of two things: the change data itself, which is stored in a database table; and the system metadata necessary to maintain the change table, which includes control columns.

The publisher specifies the source columns that are to be included in the change table. Typically, for a change table to contain useful data, the publisher needs to include the primary key column in the change table along with any other columns of interest to subscribers. For example, suppose subscribers are interested in changes that occur to the `UNIT_COST` and the `UNIT_PRICE` columns in the `sh.costs` table. If the publisher does not include the `PROD_ID` column in the change table, subscribers will know only that the unit cost and unit price of some products have changed, but will be unable to determine for which products these changes have occurred.

There are optional and required control columns. The required control columns are always included in a change table; the optional ones are included if specified by the publisher when creating the change table. Control columns are managed by Change Data Capture. See "Understanding Change Table Control Columns" and "Understanding TARGET\_COLMAP$ and SOURCE\_COLMAP$ Values" for detailed information on control columns.

## Getting Information About the Change Data Capture Environment

Information about the Change Data Capture environment is provided in the static data dictionary views described in Table 17-2 and Table 17-3. Table 17-2 lists the views that are intended for use by publishers; the user must have the `SELECT_CATALOG_ROLE` privilege to access the views listed in this table. Table 17-3 lists the views that are intended for use by subscribers. Table 17-3 includes views with the prefixes `ALL` and `USER`. These prefixes have the following general meanings:

- A view with the `ALL` prefix allows the user to display all the information accessible to the user, including information from the current user's schema as well as information from objects in other schemas, if the current user has access to those objects by way of grants of privileges or roles.
- A view with the `USER` prefix allows the user to display all the information from the schema of the user issuing the query without the use of additional special privileges or roles.
	Note:
	To look at all the views (those intended for both the publisher and the subscriber), a user must have the `SELECT_CATALOG_ROLE` privilege.

Table 17-2 Views Intended for Use by Change Data Capture Publishers

| View Name | Description |
| --- | --- |
| `ALL_CHANGE_SOURCES` | Describes existing change sources. |
| `ALL_CHANGE_PROPAGATIONS` | Describes the Oracle Streams propagation associated with a given Distributed HotLog change source on the source database. This view is populated on the source database for 11.1 or 11.2 change sources or on the staging database for 9.2, 10.1 or 10.2 change sources. |
| `ALL_CHANGE_PROPAGATION_SETS` | Describes the Oracle Streams propagation associated with a given Distributed HotLog change set on the staging database. This view is populated on the source database for 11.1 or 11.2 change sources or on the staging database for 9.2, 10.1 or 10.2 change sources. |
| `ALL_CHANGE_SETS` | Describes existing change sets. |
| `ALL_CHANGE_TABLES` | Describes existing change tables. |
| `DBA_SOURCE_TABLES` | Describes all published source tables in the database. |
| `DBA_PUBLISHED_COLUMNS` | Describes all published columns of source tables in the database. |
| `DBA_SUBSCRIPTIONS` | Describes all subscriptions. |
| `DBA_SUBSCRIBED_TABLES` | Describes all source tables to which any subscriber has subscribed. |
| `DBA_SUBSCRIBED_COLUMNS` | Describes the columns of source tables to which any subscriber has subscribed. |

Table 17-3 Views Intended for Use by Change Data Capture Subscribers

| View Name | Description |
| --- | --- |
| `ALL_SOURCE_TABLES` | Describes all public source tables for change tables that are owned by the current user. |
| `USER_SOURCE_TABLES` | Describes all public source tables for change tables that are owned by the current user. |
| `ALL_PUBLISHED_COLUMNS` | Describes all published columns of source tables for change tables that are owned by the current user.<sup>Foot 1</sup> |
| `USER_PUBLISHED_COLUMNS` | Describes all published columns of source tables for change tables that are owned by the current user. |
| `ALL_SUBSCRIPTIONS` | Describes all of the subscriptions created by the current user. |
| `USER_SUBSCRIPTIONS` | Describes all of the subscriptions created by the current user. |
| `ALL_SUBSCRIBED_TABLES` | Describes the source tables to which the current user has subscribed. |
| `USER_SUBSCRIBED_TABLES` | Describes the source tables to which the current user has subscribed. |
| `ALL_SUBSCRIBED_COLUMNS` | Describes the columns of source tables to which the current user has subscribed. |
| `USER_SUBSCRIBED_COLUMNS` | Describes the columns of source tables to which the current user has subscribed. |

<sup>Footnote 1</sup> `ALL_PUBLISHED_COLUMNS`, `USER_PUBLISHED_COLUMNS`, and the view for `*_SOURCE_TABLES` are synonyms, so the user must have ownership to view the table or column information.

See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_part.htm#REFRN002) for complete information about these views.

## Preparing to Publish Change Data

This section describes the tasks the publisher should perform before starting to publish change data, information on creating publishers, information on selecting a mode in which to capture change data, instructions on setting up database links required for the asynchronous Distributed HotLog mode of Change Data Capture, and instructions on setting database initialization parameters required by Change Data Capture.

A publisher should do the following before performing the actual steps for publishing:

- Gather requirements from the subscribers.
- Determine which source database contains the relevant source tables.
- Choose the capture mode: synchronous, asynchronous HotLog, asynchronous Distributed HotLog, or asynchronous AutoLog, as described in "Determining the Mode in Which to Capture Data".
- Ensure that the source and staging database DBAs have set database initialization parameters, as described in "Setting Initialization Parameters for Change Data Capture Publishing" and "Publishing Change Data".
- Sets up database links from the source database to the staging database and from the staging database to the source database, as shown in "Performing Asynchronous Distributed HotLog Publishing". Be aware that this requires the source database publisher to know the username and password of the staging database publisher and the staging database publisher to know the username and password of the source database publisher.

### Creating a User to Serve As a Publisher

For all modes of Change Database Capture, the staging database DBA creates a user to serve as a publisher for Change Data Capture. In addition, for the asynchronous Distributed HotLog mode of Change Data Capture, the source database DBA also creates a user to serve as a publisher. On the source database, this publisher's only task is to create a database link from the source database to the staging database.

The `SYS` and `SYSTEM` users cannot be used as a Change Data Capture publisher, and a Change Data Capture publisher should not use the `SYSTEM` tablespace as its default tablespace.

The following sections describe how to set up a publisher as required for each mode of Change Data Capture.

Note:

If a publisher is dropped with a SQL `DROP USER CASCADE` statement, then all Change Data Capture objects owned by that publisher are dropped, except those that contain Change Data Capture objects owned by other publishers.For example, suppose publisher `CDCPUB1` owns the change set `CDCPUB1_SET` that contains the change table `CDCPUB2.SALES_CT`. Issuing a `DROP USER CASCADE` statement to drop `CDCPUB1` does not result in the `CDCPUB1_SET` change set being dropped. However, after all of the change tables contained within the change set have been dropped, any publisher can drop the `CDCPUB1_SET` change set with the `DBMS_CDC_PUBLISH.DROP_CHANGE_SET` subprogram.

#### Granting Privileges and Roles to the Publisher

Regardless of change data capture mode to be used, the staging database publisher must be granted the privileges and roles in the following list:

- `EXECUTE_CATALOG_ROLE` privilege
- `SELECT_CATALOG_ROLE` privilege
- `CREATE TABLE` and `CREATE SESSION` privileges
- `EXECUTE` on the `DBMS_CDC_PUBLISH` package

For asynchronous HotLog, Distributed HotLog, and AutoLog publishing, the staging database publisher must be configured as an Oracle Streams administrator and also be granted the `CREATE` `SEQUENCE` privilege, as follows. (See [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/toc.htm) for information on configuring an Oracle Streams administrator.)

- Be granted the `CREATE SEQUENCE` privilege
- Be granted the `DBA` role
- Be the `GRANTEE` specified in a `DBMS_STREAMS_AUTH.GRANT_ADMIN_PRIVILEGE` subprogram issued by the staging database DBA

For asynchronous Distributed HotLog publishing, the source database publisher must be granted the `DBA` role and must be the grantee specified in a `DBMS_STREAMS_AUTH.GRANT_ADMIN_PRIVILEGE` subprogram.

#### Creating a Default Tablespace for the Publisher

Oracle recommends that when creating the publisher account on a staging database, the DBA specify a default tablespace for the publisher; the publisher should use this tablespace for any change tables he or she creates.

#### Password Files and Setting the REMOTE\_LOGIN\_PASSWORDFILE Parameter

You must ensure that a password file has been generated. This occurs automatically when using the Database Configuration Assistant.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm)
- "Database Configuration Assistant Considerations" for more information on setting passwords

### Determining the Mode in Which to Capture Data

These factors influence the decision on the mode in which to capture change data:

- Whether or not the staging database is remote from the source database
- Tolerance for latency between changes made on the source database and changes captured by Change Data Capture. Note that latency generally increases from Synchronous to Asynchronous AutoLog Archive in Table 17-4
- Performance impact on the source database transactions and overall database performance
- Whether the source and staging databases will be running on the same hardware, using the same operating systems, or using the same Oracle database release

Table 17-4 summarizes these factors that influence the mode decision.

Table 17-4 Factors Influencing Choice of Change Data Capture Mode

| Mode | Location of, Hardware, and Software on Staging Database | Capture Mechanism | Source Database Performance Impact |
| --- | --- | --- | --- |
| Synchronous | Location must be the same as the source database and therefore hardware, operating system, and Oracle database release are the same as source system. | Change data is automatically committed as part of the same transaction it reflects. | Adds overhead to source database transactions to perform change data capture. |
| Asynchronous HotLog | Location must be the same as the source database and therefore hardware, operating system, and Oracle database release are the same as source system. | Change data is captured from the current online redo log file. Change sets are populated automatically as new transactions are committed. | Minimal impact on source database transactions to perform supplemental logging. Additional source database overhead to perform change data capture. |
| Asynchronous Distributed HotLog | Location is remote from the source database. Hardware, operating system, and Oracle database release can be different from the source system. | Change data is captured from the current online redo log file. The change set is populated automatically as new committed transactions arrive on the staging database. | Minimal impact on source database transactions to perform supplemental logging.  Some overhead on the source database is incurred when mining the online redo log files. |
| Asynchronous AutoLog Online | Location is remote from the source database. Hardware, operating system, and Oracle database release are the same as source system. | Change data is captured from the standby redo log files. The change set is populated automatically as new committed transactions arrive on the staging database. | Minimal impact on source database transactions to perform supplemental logging.  Minimal source database overhead for redo transport services. |
| Asynchronous AutoLog Archive | Location is remote from the source database. Hardware, operating system, and Oracle database release are the same as source system. | Change data is captured from archived redo log files. Change sets are populated automatically as archived redo log files arrive on the staging database. | Minimal impact on source database transactions to perform supplemental logging.  Minimal source database overhead for redo transport services. |

### Setting Initialization Parameters for Change Data Capture Publishing

Initialization parameters must be set on the source or staging database, or both, for Change Data Capture to succeed. Which parameters to set depend on the mode in which Change Data Capture is publishing change data, and on whether the parameters are being set on the source or staging database.

The following sections describe the database initialization parameter settings for each mode of Change Data Capture. Sometimes the DBA is directed to add a value to a current setting. (The DBA can use the SQL `SHOW` `PARAMETERS` statement to see the current value of a setting.)

See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for general information about these database initialization parameters and [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/toc.htm) for more information about the database initialization parameters set for asynchronous publishing.

#### Initialization Parameters for Synchronous Publishing

Set the `JAVA_POOL_SIZE` parameter as follows:

```
JAVA_POOL_SIZE = 50000000
```

#### Initialization Parameters for Asynchronous HotLog Publishing

Table 17-5 lists the source database initialization parameters and their recommended settings for asynchronous HotLog publishing.

Table 17-5 Source Database Initialization Parameters for Asynchronous HotLog Publishing

| Parameter | Recommended Value |
| --- | --- |
| `COMPATIBLE` | 11.0 |
| `JAVA_POOL_SIZE` | 50000000 |
| `JOB_QUEUE_PROCESSES` | (current value) + 2 |
| `PARALLEL_MAX_SERVERS` | (current value) + (5 \* (the number of change sets planned)) |
| `PROCESSES` | (current value) + (7 \* (the number of change sets planned)) |
| `SESSIONS` | (current value) + (2 \* (the number of change sets planned)) |
| `STREAMS_POOL_SIZE` | - If the current value of the `STREAMS_POOL_SIZE` parameter is 50 MB or greater, then set this parameter to: 	(current value) + ((the number of change sets planned) \* (21 MB)) - If the current value of the `STREAMS_POOL_SIZE` parameter is less than 50 MB, then set the value of this parameter to: 	50 MB + ((the number of change sets planned) \* (21 MB))  See [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/toc.htm) for information on how the `STREAMS_POOL_SIZE` parameter is applied when changed dynamically. |
| `UNDO_RETENTION` | 3600 |

#### Initialization Parameters for Asynchronous Distributed HotLog Publishing

Table 17-6 lists the source database initialization parameters and their recommended settings for asynchronous Distributed HotLog publishing when the source database is Oracle Database release 10.1.0, 10.2.0, 11.1.0, or 11.2.0.

Table 17-7 lists the source database initialization parameters and their recommended settings for asynchronous Distributed HotLog publishing when the source database is Oracle Database release 9.2.

Table 17-8 lists the staging database initialization parameters and their recommended settings for asynchronous Distributed HotLog publishing. These are the same regardless of which Oracle database release is being used for the source database.

Table 17-6 Source Database (10.1.0, 10.2.0, 11.1.0, 11.2.0) Initialization Parameters for Asynchronous Distributed HotLog Publishing

| Parameter | Recommended Value |
| --- | --- |
| `COMPATIBLE` | 11.0, depending on the source Oracle database release |
| `GLOBAL_NAMES` | `TRUE` |
| `JOB_QUEUE_PROCESSES` | (current value) + 2 |
| `OPEN_LINKS` | 4, or the number of Distributed HotLog change sources planned, whichever is greater. |
| `PARALLEL_MAX_SERVERS` | (current value) + (3 \* (the number of change sources planned)) |
| `PROCESSES` | (current value) + (4 \* (the number of change sources planned)) |
| `SESSIONS` | (current value) + (the number of change sources planned) |
| `STREAMS_POOL_SIZE` | - If the current value of the `STREAMS_POOL_SIZE` parameter is 50 MB or greater, then set this parameter to: 	(current value) + ((the number of change sources planned) \* (20 MB)) - If the current value of the `STREAMS_POOL_SIZE` parameter is less than 50 MB, then set the value of this parameter to: 	50 MB + ((the number of change sets planned) \* (20 MB))  See [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/toc.htm) for information on how the `STREAMS_POOL_SIZE` parameter is applied when changed dynamically. |
| `UNDO_RETENTION` | 3600 |

Table 17-7 Source Database (9.2) Initialization Parameters for Asynchronous Distributed HotLog Publishing

| Parameter | Recommended Value |
| --- | --- |
| `COMPATIBLE` | 9.2.0 |
| `GLOBAL_NAMES` | `TRUE` |
| `JOB_QUEUE_PROCESSES` | (current value) + 2 |
| `LOG_PARALLELISM` | 1 |
| `LOGMNR_MAX_PERSISTENT_SESSIONS` | Value equal to the number of change sources planned |
| `OPEN_LINKS` | 4, or the number of Distributed HotLog change sources planned, whichever is greater |
| `PARALLEL_MAX_SERVERS` | (current value) + (3 \* (the number of change sources planned)) |
| `PROCESSES` | (current value) + (4 \* (the number of change sources planned)) |
| `SESSIONS` | (current value) + (the number of change sources planned) |
| `SHARED_POOL_SIZE` | - If the current value of the `SHARED_POOL_SIZE` parameter is 50 MB or greater, then set this parameter to: 	(current value) + ((the number of change sources planned) \* (20 MB)) - If the current value of the `SHARED_POOL_SIZE` parameter is less than 50 MB, then set the value of this parameter to: 	50 MB + ((the number of change sources planned) \* (20 MB)) |
| `UNDO_RETENTION` | 3600 |

Table 17-8 Staging Database (11.2.0) Initialization Parameters for Asynchronous Distributed HotLog Publishing

| Parameter | Recommended Value |
| --- | --- |
| `COMPATIBLE` | 11.0 |
| `GLOBAL_NAMES` | `TRUE` |
| `JAVA_POOL_SIZE` | 50000000 |
| `OPEN_LINKS` | 4, or the number of Distributed HotLog change sets planned, whichever is greater. |
| `PARALLEL_MAX_SERVERS` | (current value) + (2 \* (the number of change sets planned)) |
| `PROCESSES` | (current value) + (3 \* (the number of change sets planned)) |
| `SESSIONS` | (current value) + (the number of change sets planned) |
| `STREAMS_POOL_SIZE` | - If the current value of the `STREAMS_POOL_SIZE` parameter is 50 MB or greater, then set this parameter to: 	(current value) + ((the number of change sets planned) \* (11 MB)) - If the current value of the `STREAMS_POOL_SIZE` parameter is less than 50 MB, then set the value of this parameter to: 	50 MB + ((the number of change sets planned) \* (11 MB))  See [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/toc.htm) for information on how the `STREAMS_POOL_SIZE` parameter is applied when changed dynamically. |

#### Initialization Parameters for Asynchronous AutoLog Publishing

Table 17-9 lists the database initialization parameters and their recommended settings for the asynchronous AutoLog publishing source database and Table 17-10 lists the database initialization parameters and their recommended settings for the asynchronous AutoLog publishing staging database.

Table 17-9 Source Database Initialization Parameters for Asynchronous AutoLog Publishing

| Parameter | Recommended Value |
| --- | --- |
| `COMPATIBLE` | 11.0 |
| `LOG_ARCHIVE_DEST_1` <sup>Foot 1</sup> | The directory specification on the source database where its own archived redo log files are to be kept. |
| `LOG_ARCHIVE_DEST_2` <sup>Footref 1</sup> | This parameter must include the `SERVICE`, `ARCH` or `LGWR ASYNC`, `OPTIONAL`, `NOREGISTER`, and `REOPEN` attributes so that redo transport services are configured to copy the redo log files from the source database to the staging database. This parameter must also include either the `VALID_FOR` or the `TEMPLATE` attribute depending on the AutoLog option. These attributes are set as follows:  - `SERVICE` specifies the network name of the staging database. - `ARCH` or `LGWR ASYNC` 	To use the AutoLog online option, specify `LGWR` `ASYNC`. `LGWR` `ASYNC` specifies that the log writer process (`LGWR`) copy redo data asynchronously to the staging database as the redo is generated on the source database. The copied redo data becomes available to Change Data Capture after its source database transaction commits.To use the AutoLog archive option, specify either `ARCH` or `LGWR` `ASYNC`. `ARCH` specifies that the archiver process (`ARCn`) copy the redo log files to the staging database after a source database log switch occurs. `LGWR` `ASYNC` specifies that the log writer process (`LGWR`) copy redo data asynchronously to the staging database as the redo is generated on the source database. For both `ARCH` and `LGWR` `ASYNC`, the copied redo data becomes available to Change Data Capture only after a source database log switch occurs when using the AutoLog archive option. - `OPTIONAL` specifies that the copying of a redo log file to the staging database need not succeed before the corresponding online redo log at the source database can be overwritten. This is needed to avoid stalling operations on the source database due to a transmission failure to the staging database. The original redo log file remains available to the source database in either archived or backed up form, if it is needed. - `NOREGISTER` specifies that the staging database location is not recorded in the staging database control file. - `REOPEN` specifies the minimum number of seconds the log writer process (`LGWR`) or the archive process (`ARCn`) should wait before trying to access the staging database if a previous attempt to access this location failed. - `VALID_FOR` When using the AutoLog online option, set `VALID_FOR` either to (`ONLINE_LOGFILE`, `PRIMARY_ROLE`) or (`ONLINE_LOGFILE`, `ALL_ROLES`) to enable redo data to be copied from the online redo log on the source database to the standby redo log at the staging database. - `TEMPLATE` When using the AutoLog archive option, specify `TEMPLATE` to define a directory specification and a format template for the file name used for the archived redo log files that are copied to the staging database.<sup>Foot 2</sup> |
| `LOG_ARCHIVE_DEST_STATE_1` <sup>Footref 1</sup> | `ENABLE`  Indicates that redo transport services can transmit archived redo log files to this destination. |
| `LOG_ARCHIVE_DEST_STATE_2` <sup>Footref 1</sup> | `ENABLE`  Indicates that redo transport services can transmit redo log files to this destination. |
| `LOG_ARCHIVE_FORMAT` <sup>Footref 2</sup> | `"arch_%s_%t_%r.dbf"`  Specifies a format template for the default file name when archiving redo log files.<sup>Footref 2</sup> The string value (`arch`) and the file name extension (.`dbf`) do not have to be exactly as specified here. |
| `REMOTE_ARCHIVE_ENABLE` | `TRUE`  Indicates that this source database can send redo log files to remote destinations. |

<sup>Footnote 1</sup> The integer value in this parameter can be any value between 1 and 10. In this manual, the values 1 and 2 are used. For each `LOG_ARCHIVE_DEST_` `n` parameter, there must be a corresponding `LOG_ARCHIVE_DEST_STATE_` `n` parameter that specifies the same value for `n`.

<sup>Footnote 2</sup> In the format template, %t corresponds to the thread number, %s corresponds to the sequence number, and %r corresponds to the resetlogs ID. Together, these ensure that unique names are constructed for the copied redo log files. Each of these items must be present, but their ordering and format are flexible.

Table 17-10 Staging Database Initialization Parameters for Asynchronous AutoLog Publishing

| Parameter | Recommended Value |
| --- | --- |
| `COMPATIBLE` | 11.2.0 |
| `GLOBAL_NAMES` | `TRUE` |
| `JAVA_POOL_SIZE` | 50000000 |
| `LOG_ARCHIVE_DEST_1` <sup>Foot 1</sup> | The directory specification on the staging database where its own archived redo log files are to be kept. If the staging database has an AutoLog online change source, the following attributes should be specified:  - `LOCATION` specifies a unique directory path name for the staging database's own archived redo log files. - Set `VALID_FOR` either to (`ONLINE_LOGFILE`, `PRIMARY_ROLE`) or (`ONLINE_LOGFILE`, `ALL_ROLES`) to enable the online redo log file to be archived locally. |
| `LOG_ARCHIVE_DEST_2` <sup>Footref 1</sup> | If the staging database has an AutoLog online change source, this specifies the standby redo log files on the staging database that receive change data from the source database. It is very important to specify a unique location for these standby redo log files so that they do not overwrite the staging database's own archived log files.  - `LOCATION` specifies a unique directory path name for the staging database's standby redo log files. - `MANDATORY` specifies that a standby redo log file must be successfully archived before it can be overwritten. - Set `VALID_FOR` either to (`STANDBY_LOGFILE`, `PRIMARY_ROLE`) or (`STANDBY_LOGFILE`, `ALL_ROLES`) to enable the staging database to receive change data from the source database and write it to the staging database standby log files. |
| `LOG_ARCHIVE_DEST_STATE_1` <sup>Footref 1</sup> | `ENABLE`  Indicates that redo transport services can transmit archived redo log files to this destination. |
| `LOG_ARCHIVE_DEST_STATE_2` <sup>Footref 1</sup> | `ENABLE`  Indicates that redo transport services can transmit redo log files to this destination. |
| `LOG_ARCHIVE_FORMAT` <sup>Footref 2</sup> | `"arch_%s_%t_%r.dbf"`  Specifies a format template for the default file name when archiving redo log files <sup>Foot 2</sup> . The string value (`arch`) and the file name extension (`.dbf`) do not have to be exactly as specified here. |
| `JOB_QUEUE_PROCESSES` | 2 |
| `PARALLEL_MAX_SERVERS` | (current value) + (5 \* (the number of change sets planned)) |
| `PROCESSES` | (current value) + (7 \* (the number of change sets planned)) |
| `REMOTE_ARCHIVE_ENABLE` | `TRUE`  Indicates that this staging database can receive remotely archived redo log files. |
| `SESSIONS` | (current value)+ (2 \* (the number of change sets planned)) |
| `STREAMS_POOL_SIZE` | - If the current value of the `STREAMS_POOL_SIZE` parameter is 50 MB or greater, then set this parameter to: 	(current value) + ((the number of change sets planned) \* (21 MB)) - If the current value of the `STREAMS_POOL_SIZE` parameter is less than 50 MB, then set the value of this parameter to: 	50 MB + ((the number of change sets planned) \* (21 MB))  See [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/toc.htm) for information on how the `STREAMS_POOL_SIZE` parameter is applied when changed dynamically. |
| `UNDO_RETENTION` | 3600 |

<sup>Footnote 1</sup> The integer value in this parameter can be any value between 1 and 10. In this manual, the values 1 and 2 are used. For each `LOG_ARCHIVE_DEST_` `n` parameter, there must be a corresponding `LOG_ARCHIVE_DEST_STATE_` `n` parameter that specifies the same value for `n`.

<sup>Footnote 2</sup> In the format template, %t corresponds to the thread number, %s corresponds to the sequence number, and %r corresponds to the resetlogs ID. Together, these ensure that unique names are constructed for the copied redo log files. Each of these items must be present, but their ordering and format are flexible.

### Adjusting Initialization Parameter Values When Oracle Streams Values Change

Asynchronous Change Data Capture uses an Oracle Streams configuration for each change set. This Streams configuration consists of a Streams capture process and a Streams apply process, with an accompanying queue and queue table. Each Streams configuration uses additional processes, parallel execution servers, and memory. For details about the Streams architecture, see [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/toc.htm).

If anything in your configuration changes, initialization parameters may need to be adjusted. See Table 17-10, "Staging Database Initialization Parameters for Asynchronous AutoLog Publishing" for more information.

### Tracking Changes to the CDC Environment

You can track when partition maintenance operations, direct-path loads, and DDL operations occur in a change table. To do this, set the `ddl_markers` flag in the `DBMS_CDC_PUBLISH.CREATE_CHANGE_TABLE` procedure.

## Publishing Change Data

The following sections provide step-by-step instructions on performing the various types of publishing:

- Performing Synchronous Publishing
- Performing Asynchronous HotLog Publishing
- Performing Asynchronous Distributed HotLog Publishing
- Performing Asynchronous AutoLog Publishing

### Performing Synchronous Publishing

For synchronous Change Data Capture, the publisher must use the predefined change source, `SYNC_SOURCE`. The publisher can define new change sets or can use the predefined change set, `SYNC_SET`. The publisher must not create change tables on source tables owned by `SYS` or `SYSTEM` because triggers do not fire and therefore changes are not captured.

This example shows how to create a change set. If the publisher wants to use the predefined `SYNC_SET`, he or she should skip Step 3 and specify `SYNC_SET` as the change set name in the remaining steps.

This example assumes that the publisher and the source database DBA are two different people.

Note that for synchronous Change Data Capture, the source database and the staging database are the same.

Step 1 Source Database DBA: Set the JAVA\_POOL\_SIZE parameter.

The source database DBA sets the database initialization parameters, as described in "Setting Initialization Parameters for Change Data Capture Publishing".

```
java_pool_size = 50000000
```

Step 2 Source Database DBA: Create and grant privileges to the publisher.

The source database DBA creates a user (for example, `cdcpub`), to serve as the Change Data Capture publisher and grants the necessary privileges to the publisher so that he or she can perform the operations needed to create Change Data Capture change sets and change tables on the source database, as described in "Creating a User to Serve As a Publisher". This example assumes that the tablespace `ts_cdcpub` has already been created.

```
CREATE USER cdcpub IDENTIFIED EXTERNALLY DEFAULT TABLESPACE ts_cdcpub
QUOTA UNLIMITED ON SYSTEM
QUOTA UNLIMITED ON SYSAUX;
GRANT CREATE SESSION TO cdcpub;
GRANT CREATE TABLE TO cdcpub;
GRANT CREATE TABLESPACE TO cdcpub;
GRANT CREATE JOB TO cdcpub;
GRANT UNLIMITED TABLESPACE TO cdcpub;
GRANT SELECT_CATALOG_ROLE TO cdcpub;
GRANT EXECUTE_CATALOG_ROLE TO cdcpub;
GRANT ALL ON sh.sales TO cdcpub;
GRANT ALL ON sh.products TO cdcpub;
GRANT EXECUTE ON DBMS_CDC_PUBLISH TO cdcpub;
```

Step 3 Staging Database Publisher: Create a change set.

The publisher uses the `DBMS_CDC_PUBLISH.CREATE_CHANGE_SET` procedure on the staging database to create change sets.

The following example shows how to create a change set called `CHICAGO_DAILY`:

```
BEGIN
    DBMS_CDC_PUBLISH.CREATE_CHANGE_SET( 
    change_set_name    => 'CHICAGO_DAILY', 
    description        => 'Change set for sales history info', 
    change_source_name => 'SYNC_SOURCE');
END;
/
```

The change set captures changes from the predefined change source `SYNC_SOURCE`. Because `begin_date` and `end_date` parameters cannot be specified for synchronous change sets, capture begins at the earliest available change data and continues capturing change data indefinitely.

Step 4 Staging Database Publisher: Create a change table.

The publisher uses the `DBMS_CDC_PUBLISH.CREATE_CHANGE_TABLE` procedure to create change tables.

The publisher can set the `options_string` field of the `DBMS_CDC_PUBLISH.CREATE_CHANGE_TABLE` procedure to have more control over the physical properties and tablespace properties of the change table. The `options_string` field can contain any option, except partitioning, that is available in the `CREATE TABLE` statement.

The following example creates a change table that captures changes that occur on a source table. The example uses the sample schema table `sh.products` as the source table. It assumes that the publisher has already created the `TS_CHICAGO_DAILY` tablespace.

```
BEGIN
   DBMS_CDC_PUBLISH.CREATE_CHANGE_TABLE(
```
```
owner             => 'cdcpub',
   change_table_name => 'products_ct', 
   change_set_name   => 'CHICAGO_DAILY',
   source_schema     => 'SH',
   source_table      => 'PRODUCTS',
   column_type_list  => 'PROD_ID NUMBER(6), 
                         PROD_NAME VARCHAR2(50),
                         PROD_LIST_PRICE NUMBER(8,2)', 
   capture_values    => 'both',
   rs_id             => 'y', 
   row_id            => 'n',
   user_id           => 'n',
   timestamp         => 'n',
   object_id         => 'n',
   source_colmap     => 'y',
   target_colmap     => 'y',
   options_string    => 'TABLESPACE TS_CHICAGO_DAILY');
END;
 /
```

This statement creates a change table named `products_ct` within the change set `CHICAGO_DAILY`. The `column_type_list` parameter identifies the columns captured by the change table. The `source_schema` and `source_table` parameters identify the schema and source table that reside in the source database.

The `capture_values` setting in the example indicates that for update operations, the change data contains two separate rows for each row that changed: one row contains the row values before the update occurred, and the other row contains the row values after the update occurred.

See "Managing Change Tables" for more information.

Step 5 Staging Database Publisher: Grant access to subscribers.

The publisher controls subscriber access to change data by granting and revoking the `SELECT` privilege on change tables for users and roles. The publisher grants access to specific change tables. Without this step, a subscriber cannot access any change data. This example assumes that user `subscriber1` already exists.

```
GRANT SELECT ON cdcpub.products_ct TO subscriber1;
```

The Change Data Capture synchronous system is now ready for `subscriber1` to create subscriptions.

### Performing Asynchronous HotLog Publishing

Change Data Capture uses Oracle Streams local capture to perform asynchronous HotLog publishing. See [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/toc.htm) for information on Streams local capture.

For HotLog Change Data Capture, the publisher must use the predefined change source, `HOTLOG_SOURCE`, and must create the change sets and the change tables that contain the changes. The staging database is always the source database. This example assumes that the publisher and the source database DBA are two different people.

Note that for asynchronous HotLog Change Data Capture, the source database and the staging database are the same.

The following steps set up redo logging, Oracle Streams, and Change Data Capture for asynchronous HotLog publishing:

Step 1 Source Database DBA: Set the database initialization parameters.

The source database DBA sets the database initialization parameters, as described in "Setting Initialization Parameters for Change Data Capture Publishing". In this example, one change set is defined and the current value of the `STREAMS_POOL_SIZE` parameter is 50 MB.

```
compatible = 11.0
java_pool_size = 50000000
job_queue_processes = 2
```
```
parallel_max_servers = <current value> + 5
processes = <current value> + 7
sessions = <current value> + 2
streams_pool_size = <current value> + 21 MB
undo_retention = 3600
```

Step 2 Source Database DBA: Alter the source database.

The source database DBA performs the following three tasks. The second is required. The first and third are optional, but recommended. It is assumed that the database is currently running in `ARCHIVELOG` mode.

1. Place the database into `FORCE` `LOGGING` logging mode to protect against unlogged direct write operations in the source database that cannot be captured by asynchronous Change Data Capture:
	```
	ALTER DATABASE FORCE LOGGING;
	```
	Note that logging can also be enforced at the tablespace or at the table level.
2. Enable supplemental logging. Supplemental logging places additional column data into a redo log file whenever an `UPDATE` operation is performed. Minimally, database-level minimal supplemental logging must be enabled for any Change Data Capture source database:
	```
	ALTER DATABASE ADD SUPPLEMENTAL LOG DATA;
	```
3. Create an unconditional log group on all columns to be captured in the source table. Source table columns that are unchanged and are not in an unconditional log group, will be null in the change table, instead of reflecting their actual source table values. (This example captures rows in the `sh.products` table only. The source database DBA would repeat this step for each source table for which change tables will be created.)
	```
	ALTER TABLE sh.products
	ADD SUPPLEMENTAL LOG GROUP log_group_products
	  (PROD_ID, PROD_NAME, PROD_LIST_PRICE) ALWAYS;
	```
	If you intend to capture all the column values in a row whenever a column in that row is updated, you can use the following statement instead of listing each column one-by-one in the `ALTER` `TABLE` statement. However, do not use this form of the `ALTER` `TABLE` statement if all columns are not needed. Logging all columns incurs more overhead than logging selected columns.
	```
	ALTER TABLE sh.products ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS;
	```
	See [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/archredo.htm#ADMIN11332) for information about running a database in `ARCHIVELOG` mode and for information on `FORCE` `LOGGING` mode; see "Asynchronous Change Data Capture and Supplemental Logging" and [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/toc.htm) for more information about supplemental logging.

Step 3 Source Database DBA: Create and grant privileges to the publisher.

The source database DBA creates a user, (for example, `cdcpub`), to serve as the Change Data Capture publisher and grants the necessary privileges to the publisher so that he or she can perform the underlying Oracle Streams operations needed to create Change Data Capture change sets and change tables on the source database, as described in "Creating a User to Serve As a Publisher". This example assumes that the `ts_cdcpub` tablespace has already been created.

```
CREATE USER cdcpub IDENTIFIED EXTERNALLY DEFAULT TABLESPACE ts_cdcpub
QUOTA UNLIMITED ON SYSTEM 
QUOTA UNLIMITED ON SYSAUX;
GRANT CREATE SESSION TO cdcpub;
GRANT CREATE TABLE TO cdcpub;
GRANT CREATE TABLESPACE TO cdcpub;
GRANT UNLIMITED TABLESPACE TO cdcpub;
GRANT SELECT_CATALOG_ROLE TO cdcpub;
GRANT EXECUTE_CATALOG_ROLE TO cdcpub;
GRANT CREATE SEQUENCE TO cdcpub;
GRANT DBA TO cdcpub;
GRANT EXECUTE on DBMS_CDC_PUBLISH TO cdcpub;

EXECUTE DBMS_STREAMS_AUTH.GRANT_ADMIN_PRIVILEGE(GRANTEE => 'cdcpub');
```

Note that for HotLog Change Data Capture, the source database and the staging database are the same database.

Step 4 Source Database DBA: Prepare the source tables.

The source database DBA must prepare the source tables on the source database for asynchronous Change Data Capture by instantiating each source table. Instantiating each source table causes the underlying Oracle Streams environment to record the information it needs to capture each source table's changes. The source table structure and the column datatypes must be supported by Change Data Capture. See "Datatypes and Table Structures Supported for Asynchronous Change Data Capture" for more information.

```
BEGIN
DBMS_CAPTURE_ADM.PREPARE_TABLE_INSTANTIATION(TABLE_NAME => 'sh.products');
END;
/
```

Step 5 Staging Database Publisher: Create change sets.

The publisher uses the `DBMS_CDC_PUBLISH.CREATE_CHANGE_SET` procedure on the staging database to create change sets. Note that when Change Data Capture creates a change set, its associated Oracle Streams capture and apply processes are also created (but not started).

The following example creates a change set called `CHICAGO_DAILY` that captures changes starting today, and stops capturing change data 5 days from now.

```
BEGIN
       DBMS_CDC_PUBLISH.CREATE_CHANGE_SET(
       change_set_name => 'CHICAGO_DAILY',
       description => 'Change set for product info',
       change_source_name => 'HOTLOG_SOURCE',
       stop_on_ddl => 'y',
       begin_date => sysdate,
       end_date => sysdate+5);
END;
/
```

The change set captures changes from the predefined `HOTLOG_SOURCE` change source.

Step 6 Staging Database Publisher: Create the change tables that will contain the changes to the source tables.

The publisher uses the `DBMS_CDC_PUBLISH.CREATE_CHANGE_TABLE` procedure on the staging database to create change tables.

The publisher creates one or more change tables for each source table to be published, specifies which columns should be included, and specifies the combination of before and after images of the change data to capture.

The following example creates a change table on the staging database that captures changes made to a source table on the source database. The example uses the sample table `sh.products` as the source table.

```
BEGIN
   DBMS_CDC_PUBLISH.CREATE_CHANGE_TABLE(
   owner              => 'cdcpub',
   change_table_name  => 'products_ct', 
   change_set_name    => 'CHICAGO_DAILY',
   source_schema      => 'SH',
   source_table       => 'PRODUCTS',
   column_type_list   => 'PROD_ID NUMBER(6), PROD_NAME VARCHAR2(50),
      PROD_LIST_PRICE NUMBER(8,2)',
   capture_values     => 'both',
   rs_id              => 'y',
   row_id             => 'n',
   user_id            => 'n',
   timestamp          => 'n',
   object_id          => 'n',
   source_colmap      => 'n',
   target_colmap      => 'y',
   options_string     => 'TABLESPACE TS_CHICAGO_DAILY');
END;
/
```

This statement creates a change table named `products_ct` within change set `CHICAGO_DAILY`. The `column_type_list` parameter identifies the columns to be captured by the change table. The `source_schema` and `source_table` parameters identify the schema and source table that reside on the source database.

The `capture_values` setting in this statement indicates that for update operations, the change data will contain two separate rows for each row that changed: one row will contain the row values before the update occurred and the other row will contain the row values after the update occurred.

The `options_string` parameter in this statement specifies a tablespace for the change table. (This example assumes that the publisher previously created the `TS_CHICAGO_DAILY` tablespace.)

See "Managing Change Tables" for more information.

Step 7 Staging Database Publisher: Enable the change set.

Because asynchronous change sets are always disabled when they are created, the publisher must alter the change set to enable it. The Oracle Streams capture and apply processes are started when the change set is enabled.

```
BEGIN
   DBMS_CDC_PUBLISH.ALTER_CHANGE_SET(
      change_set_name => 'CHICAGO_DAILY',
      enable_capture => 'y');
END;
/
```

Step 8 Staging Database Publisher: Grant access to subscribers.

The publisher controls subscriber access to change data by granting and revoking the `SELECT` privilege on change tables for users and roles. The publisher grants access to specific change tables. Without this step, a subscriber cannot access change data. This example assumes that user `subscriber1` already exists.

```
GRANT SELECT ON cdcpub.products_ct TO subscriber1;
```

The Change Data Capture asynchronous HotLog system is now ready for `subscriber1` to create subscriptions.

### Performing Asynchronous Distributed HotLog Publishing

For Distributed HotLog Change Data Capture, the staging database is remote from the source database. However, steps must be performed on both the source database and the staging database to set up database links, Oracle Streams, and Change Data Capture. Tasks must be performed by a source database DBA, a staging database DBA, and a publisher on each database, as follows:

- The source database DBA sets up Oracle Net, database initialization parameters, alters the source database to enable force logging and supplemental logging, and creates the source database publisher.
- The staging database DBA sets database initialization parameters and creates a staging database publisher.
- The source database publisher sets up a database link from the source database to the staging database.
- The staging database publisher sets up a database link from the staging database to the source database, creates new change sources, change sets, and the change tables that will contain the changes that are made to individual source tables, and grants necessary privileges to subscribers.

This example assumes that the source database DBA, the staging database DBA, and the publishers are four different people.

Step 1 Source Database DBA: Prepare the source database.

The source database DBA performs the following tasks:

1. Configures Oracle Net so that the source database can communicate with the staging database. See [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for information about Oracle Net.
2. Sets the database initialization parameters on the source database as described in "Setting Initialization Parameters for Change Data Capture Publishing". In the following code example, the source database is Oracle Database release 11.2, the number of planned change sources is 1, and the current value of the `STREAMS_POOL_SIZE` parameter is 50 MB:
	```
	compatible = 11.0
	global_names = true
	job_queue_processes = <current value> + 2
	open_links = 4
	```
	```
	parallel_max_servers = <current value> + 3
	processes = <current value> + 4
	sessions = <current value> + 1
	streams_pool_size = <current value> + 20 MB
	undo_retention = 3600
	```

Step 2 Staging Database DBA: Set the database initialization parameters.

The staging database DBA performs the following tasks:

1. Sets the database initialization parameters on the staging database, as described in "Setting Initialization Parameters for Change Data Capture Publishing". In this example, one change set will be defined and the current value for the `STREAMS_POOL_SIZE` parameter is 50 MB or greater:
	```
	compatible = 11.0
	global_names = true
	java_pool_size = 50000000
	open_links = 4
	job_queue_processes = 2
	parallel_max_servers = <current_value> + 2
	processes = <current_value> + 3
	sessions = <current value> + 1
	streams_pool_size = <current_value> + 11 MB
	undo_retention = 3600
	```

Step 3 Source Database DBA: Alter the source database.

The source database DBA performs the following three tasks. The second is required. The first and third are optional, but recommended. It is assumed that the database is currently running in `ARCHIVELOG` mode.

1. Place the database into `FORCE` `LOGGING` logging mode to protect against unlogged direct writes in the source database that cannot be captured by asynchronous Change Data Capture:
	```
	ALTER DATABASE FORCE LOGGING;
	```
2. Enable supplemental logging. Supplemental logging places additional column data into a redo log file whenever an update operation is performed.
	```
	ALTER DATABASE ADD SUPPLEMENTAL LOG DATA;
	```
3. Create an unconditional log group on all columns to be captured in the source table. Source table columns that are unchanged and are not in an unconditional log group, will be null in the change table, instead of reflecting their actual source table values. (This example captures rows in the `sh.products` table only. The source database DBA would repeat this step for each source table for which change tables will be created).
	```
	ALTER TABLE sh.products
	ADD SUPPLEMENTAL LOG GROUP log_group_products
	    (PROD_ID, PROD_NAME, PROD_LIST_PRICE) ALWAYS;
	```
	If you intend to capture all the column values in a row whenever a column in that row is updated, you can use the following statement instead of listing each column one-by-one in the `ALTER` `TABLE` statement. However, do not use this form of the `ALTER` `TABLE` statement if all columns are not needed. Logging all columns incurs more overhead than logging selected columns.
	```
	ALTER TABLE sh.products ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS;
	```
	See Also:
	- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/archredo.htm#ADMIN11332) for information about running a database in `ARCHIVELOG` mode
	- "Asynchronous Change Data Capture and Supplemental Logging" for more information on supplemental logging
	- [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/toc.htm) for more information on supplemental logging

Step 4 Source Database DBA: Create and grant privileges to the publisher.

The source database DBA creates a user, (for example, `source_cdcpub`), to serve as the source database publisher and grants the necessary privileges to the publisher so that he or she can set up a database link from the source database to connect to the staging database publisher, as described in "Creating a User to Serve As a Publisher". For example:

```
CREATE USER source_cdcpub IDENTIFIED EXTERNALLY
   QUOTA UNLIMITED ON SYSTEM
   QUOTA UNLIMITED ON SYSAUX;
GRANT CREATE SESSION TO source_cdcpub;
GRANT DBA TO source_cdcpub;
GRANT CREATE DATABASE LINK TO source_cdcpub;
GRANT EXECUTE on DBMS_CDC_PUBLISH TO source_cdcpub;
GRANT EXECUTE_CATALOG_ROLE TO source_cdcpub;
GRANT SELECT_CATALOG_ROLE TO source_cdcpub;
EXECUTE DBMS_STREAMS_AUTH.GRANT_ADMIN_PRIVILEGE(
      GRANTEE=> 'source_cdcpub');
```

Step 5 Staging Database DBA: Create and grant privileges to the publisher.

The staging database DBA creates a user, (for example, `staging_cdcpub`), to serve as the Change Data Capture publisher and grants the necessary privileges to the publisher so that he or she can perform underlying Oracle Streams operations, create a database link from the staging database to connect to the source database publisher, create the change sources on the source database, and the change sets and change tables on the staging database, as described in "Creating a User to Serve As a Publisher". For example:

```
CREATE USER staging_cdcpub IDENTIFIED EXTERNALLY
   DEFAULT TABLESPACE ts_cdcpub
   QUOTA UNLIMITED ON SYSTEM;
GRANT CREATE SESSION TO staging_cdcpub;
GRANT CREATE TABLE TO staging_cdcpub;
GRANT CREATE TABLESPACE TO staging_cdcpub;
GRANT UNLIMITED TABLESPACE TO staging_cdcpub;
GRANT SELECT_CATALOG_ROLE TO staging_cdcpub;
GRANT EXECUTE_CATALOG_ROLE TO staging_cdcpub;
GRANT CONNECT, RESOURCE, DBA TO staging_cdcpub;
GRANT CREATE SEQUENCE TO staging_cdcpub;
EXECUTE DBMS_STREAMS_AUTH.GRANT_ADMIN_PRIVILEGE(grantee => 'staging_cdcpub');
GRANT CREATE DATABASE LINK TO staging_cdcpub;
```

Step 6 Source Database Publisher: Create Database Link

The source database publisher creates a link from the source database to the staging database. Because the `GLOBAL_NAMES` initialization parameter is set to `TRUE`, the database link name will be same as that of the staging database. It connects to the staging database using the username and password of the staging database publisher. In this example, the name of the staging database is `staging_db`:

```
CREATE DATABASE LINK staging_db
CONNECT TO staging_cdcpub IDENTIFIED BY Stg395V3
USING 'staging_db';
```

For detailed information on database links, see [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/ds_concepts.htm#ADMIN02801).

Step 7 Staging Database Publisher: Create Database Link

The staging database publisher creates a link from the staging database to the source database. Again, because the `GLOBAL_NAMES` initialization parameter is set to `TRUE`, the database link name will be the same as that of the source database. It connects to the source database using the username and password of the source database publisher. In this example, the name of the source database is `source_db`:

```
CREATE DATABASE LINK source_db
CONNECT TO source_cdcpub IDENTIFIED BY Lvh412A7
USING 'source_db';
```

Note that this database link must exist when creating, altering or dropping Distributed HotLog change sources, change sets and change tables. However, this database link is not required for change capture to occur. Once the required Distributed HotLog change sources, change sets and change tables are in place and enabled, this database link can be dropped without interrupting change capture. This database link would need to be re-created to create, alter or drop Distributed HotLog change sources, change sets and change tables.

Step 8 Staging Database Publisher: Identify the change source database and create the change sources.

The staging database publisher uses the `DBMS_CDC_PUBLISH.CREATE_HOTLOG_CHANGE_SOURCE` procedure on the staging database to create the Distributed HotLog change sources on the source database.

Note that when Change Data Capture creates a change source, its associated Oracle Streams capture process is also created (but not started).

The publisher creates the Distributed HotLog change source and specifies the database link defined from the staging database to the source database. The name of the database link is the same as the name of the source database:

```
BEGIN
   DBMS_CDC_PUBLISH.CREATE_HOTLOG_CHANGE_SOURCE(
       change_source_name => 'CHICAGO',
       description => 'test source',
       source_database => 'source_db');
END;
/
```

Step 9 Staging Database Publisher: Create change sets.

The publisher uses the `DBMS_CDC_PUBLISH.CREATE_CHANGE_SET` procedure on the staging database to create a change set. A Distributed HotLog change source can contain one or more change sets on the same staging database. The publisher cannot provide beginning and ending dates.

Note that when Change Data Capture creates a change set, its associated Oracle Streams apply process is also created (but not started).

The following example shows how to create a change set called `CHICAGO_DAILY` that captures changes starting today, and continues capturing change data indefinitely. (If, at some time in the future, the publisher decides that he or she wants to stop capturing change data for this change set, he or she should disable the change set and then drop it.)

```
BEGIN
   DBMS_CDC_PUBLISH.CREATE_CHANGE_SET(
       change_set_name => 'CHICAGO_DAILY',
       description => 'change set for product info',
       change_source_name => 'CHICAGO',
       stop_on_ddl => 'y');
END;
/
```

Step 10 Staging Database Publisher: Create the change tables.

The publisher uses the `DBMS_CDC_PUBLISH.CREATE_CHANGE_TABLE` procedure on the staging database to create change tables.

The publisher creates one or more change tables for each source table to be published, specifies which columns should be included, and specifies the combination of before and after images of the change data to capture.

The publisher can set the `options_string` field of the `DBMS_CDC_PUBLISH.CREATE_CHANGE_TABLE` procedure to have more control over the physical properties and tablespace properties of the change tables. The `options_string` field can contain any option available (except partitioning) on the `CREATE` `TABLE` statement. In this example, it specifies a tablespace for the change set. (This example assumes that the publisher previously created the `TS_CHICAGO_DAILY` tablespace.)

The following example creates a change table on the staging database that captures changes made to a source table in the source database. The example uses the sample table `sh.products`.

```
BEGIN
   DBMS_CDC_PUBLISH.CREATE_CHANGE_TABLE(
       owner             => 'staging_cdcpub',
       change_table_name => 'products_ct',
       change_set_name   => 'CHICAGO_DAILY',
       source_schema     => 'SH',
       source_table      => 'PRODUCTS',
       column_type_list  => 'PROD_ID NUMBER(6), PROD_NAME VARCHAR2(50),
          PROD_LIST_PRICE NUMBER(8,2),
          JOB_ID VARCHAR2(10), DEPARTMENT_ID NUMBER(4)',
       capture_values    => 'both',
       rs_id             => 'y',
       row_id            => 'n',
       user_id           => 'n',
       timestamp         => 'n',
       object_id         => 'n',
       source_colmap     => 'n',
       target_colmap     => 'y',
       options_string    => 'TABLESPACE TS_CHICAGO_DAILY');
END;
/
```

This example creates a change table named `products_ct` within change set `CHICAGO_DAILY`. The `column_type_list` parameter identifies the columns captured by the change table. The `source_schema` and `source_table` parameters identify the schema and source table that reside in the source database, not the staging database.

The `capture_values` setting in the example indicates that for update operations, the change data will contain two separate rows for each row that changed: one row will contain the row values before the update occurred and the other row will contain the row values after the update occurred. Note that for Distributed HotLog change sets, the `object_id` and `source_colmap` capture values must be set to `'n'`. If the change source is 9.2 or 10.1, `row_id` and `user_id` must also be `'n'`.

See "Managing Change Tables" for more information.

Step 11 Staging Database Publisher: Enable the change source.

Because Distributed HotLog change sources are always disabled when they are created, the publisher must alter the change source to enable it. The Oracle Streams capture process is started when the change source is enabled.

```
BEGIN
  DBMS_CDC_PUBLISH.ALTER_HOTLOG_CHANGE_SOURCE(
    change_source_name => 'CHICAGO',
    enable_source      => 'Y');
END;
/
```

Step 12 Staging Database Publisher: Enable the change set.

Because asynchronous change sets are always disabled when they are created, the publisher must alter the change set to enable it. The Oracle Streams apply processes is started when the change set is enabled.

```
BEGIN
   DBMS_CDC_PUBLISH.ALTER_CHANGE_SET(
       change_set_name => 'CHICAGO_DAILY',
       enable_capture  => 'y');
END;
/
```

Step 13 Staging Database Publisher: Grant access to subscribers.

The publisher controls subscriber access to change data by granting and revoking the `SELECT` privilege on change tables for users and roles on the staging database. The publisher grants access to specific change tables. Without this step, a subscriber cannot access any change data. This example assumes that user `subscriber1` already exists.

```
GRANT SELECT ON staging_cdcpub.products_ct TO subscriber1;
```

The Change Data Capture Distributed HotLog system is now ready for `subscriber1` to create subscriptions.

### Performing Asynchronous AutoLog Publishing

Change Data Capture uses Oracle Streams downstream capture to perform asynchronous AutoLog publishing. The Change Data Capture staging database is considered a downstream database in the Streams environment. The asynchronous AutoLog online option uses Streams real-time downstream capture. The asynchronous AutoLog archive option uses Streams archived-log downstreams capture. See [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/toc.htm) for information on Streams downstream capture.

For asynchronous AutoLog Change Data Capture, the publisher creates new change sources, as well as the change sets and the change tables that will contain the changes that are made to individual source tables.

Steps must be performed on both the source database and the staging database to set up redo transport services, Streams, and Change Data Capture for asynchronous AutoLog publishing. Because the source database and staging database are usually on separate systems, this example assumes that the source database DBA, the staging database DBA, and the publisher are different people.

Step 1 Source Database DBA: Prepare to copy redo log files from the source database.

The source database DBA and the staging database DBA must set up redo transport services to copy redo log files from the source database to the staging database and to prepare the staging database to receive these redo log files, as follows:

1. The source database DBA configures Oracle Net so that the source database can communicate with the staging database. See [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for information about Oracle Net.
2. The source database DBA sets the database initialization parameters on the source database as described in "Setting Initialization Parameters for Change Data Capture Publishing". In the following code examples, `STAGINGDB` is the network name of the staging database.
	The following is an example for the AutoLog online option:
	```
	compatible = 11.0
	log_archive_dest_1 ="location=/oracle/dbs mandatory reopen=5"
	log_archive_dest_2 ="service=stagingdb lgwr async optional noregister reopen=5
	                     valid_for=(online_logfile,primary_role)" 
	log_archive_dest_state_1 = enable
	log_archive_dest_state_2 = enable
	log_archive_format="arch_%s_%t_%r.dbf"
	```
	The following is an example for the AutoLog archive option:
	```
	compatible = 11.0
	log_archive_dest_1="location=/oracle/dbs mandatory reopen=5"
	log_archive_dest_2 = "service=stagingdb arch optional noregister reopen=5
	                      template=/usr/oracle/dbs/arch_%s_%t_%r.dbf" 
	log_archive_dest_state_1 = enable
	log_archive_dest_state_2 = enable
	log_archive_format="arch_%s_%t_%r.dbf"
	```
	See [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/toc.htm) for information on redo transport services.

Step 2 Staging Database DBA: Set the database initialization parameters.

The staging database must be run in `ARCHIVELOG` mode for Asynchronous Autolog CDC. The staging database DBA sets the database initialization parameters on the staging database, as described in "Setting Initialization Parameters for Change Data Capture Publishing". In these examples, one change set will be defined and the current value for the `STREAMS_POOL_SIZE` is 50 MB or greater.

The following is an example for the AutoLog online option:

```
compatible = 11.0
global_names = true
java_pool_size = 50000000
log_archive_dest_1="location=/oracle/dbs mandatory reopen=5
                    valid_for=(online_logfile,primary_role)"
log_archive_dest_2="location=/usr/oracle/dbs mandatory
                    valid_for=(standby_logfile,primary_role)"
log_archive_dest_state_1=enable
log_archive_dest_state_2=enable
log_archive_format="arch_%s_%t_%r.dbf"
job_queue_processes = 2
parallel_max_servers = <current_value> + 5
processes = <current_value> + 7
sessions = <current value> + 2
streams_pool_size = <current_value> + 21 MB
undo_retention = 3600
```

The following is an example for the AutoLog archive option:

```
compatible = 11.0
global_names = true
java_pool_size = 50000000
log_archive_dest_1="location=/oracle/dbs mandatory reopen=5
                    valid_for=(online_logfile,primary_role)"
log_archive_dest_2="location=/oracle/stdby mandatory
                    valid_for=(standby_logfile,primary_role)"
log_archive_dest_state_1=enable
log_archive_dest_state_2=enable
log_archive_format="arch_%s_%t_%r.dbf"
job_queue_processes = 2
parallel_max_servers = <current_value> + 5
processes = <current_value> + 7
sessions = <current value> + 2
streams_pool_size = <current_value> + 21 MB
undo_retention = 3600
```

Step 3 Source Database DBA: Alter the source database.

The source database DBA performs the following three tasks. The second is required. The first and third are optional, but recommended. It is assumed that the database is currently running in `ARCHIVELOG` mode.

1. Place the database into `FORCE` `LOGGING` logging mode to protect against unlogged direct writes in the source database that cannot be captured by asynchronous Change Data Capture:
	```
	ALTER DATABASE FORCE LOGGING;
	```
2. Enable supplemental logging. Supplemental logging places additional column data into a redo log file whenever an update operation is performed.
	```
	ALTER DATABASE ADD SUPPLEMENTAL LOG DATA;
	```
3. Create an unconditional log group on all columns to be captured in the source table. Source table columns that are unchanged and are not in an unconditional log group, will be null in the change table, instead of reflecting their actual source table values. (This example captures rows in the `sh.products` table only. The source database DBA would repeat this step for each source table for which change tables will be created).
	```
	ALTER TABLE sh.products
	ADD SUPPLEMENTAL LOG GROUP log_group_products
	    (PROD_ID, PROD_NAME, PROD_LIST_PRICE) ALWAYS;
	```
	If you intend to capture all the column values in a row whenever a column in that row is updated, you can use the following statement instead of listing each column one-by-one in the `ALTER` `TABLE` statement. However, do not use this form of the `ALTER` `TABLE` statement if all columns are not needed. Logging all columns incurs more overhead than logging selected columns.
	```
	ALTER TABLE sh.products ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS;
	```
	See [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for information about running a database in `ARCHIVELOG` mode. See "Asynchronous Change Data Capture and Supplemental Logging" and [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/toc.htm) for more information on supplemental logging.

Step 4 Staging Database DBA: Create Standby Redo Log Files

This step is only needed for the AutoLog online option.

The staging database DBA must create the actual standby redo log files on the staging database:

1. Determine the log file size used on the source database because the standby redo log files must be the same size or larger. You can query `V$LOG` on the source database to determine the source database log file size.
2. Determine the number of standby log file groups required on the staging database. This must be at least one more than the number of online log file groups on the source database. You can query `V$LOG` on the source database to determine the number of online log file groups on the source database.
3. Use the SQL statement `ALTER` `DATABASE` `ADD` `STANDBY` `LOGFILE` to add the standby log file groups to the staging database:
	```
	ALTER DATABASE ADD STANDBY LOGFILE GROUP 3
	    ('/oracle/dbs/slog3a.rdo', '/oracle/dbs/slog3b.rdo') SIZE 500M;
	```
	You can query `V$STANDBY_LOG` on the staging database to ensure that the standby log file groups have been added successfully.

Step 5 Staging Database DBA: Create and grant privileges to the publisher.

The staging database DBA creates a user, (for example, `cdcpub`), to serve as the Change Data Capture publisher and grants the necessary privileges to the publisher so that he or she can perform the underlying Oracle Streams operations needed to create Change Data Capture change sources, change sets, and change tables on the staging database, as described in "Creating a User to Serve As a Publisher". For example:

```
CREATE USER cdcpub IDENTIFIED EXTERNALLY DEFAULT TABLESPACE ts_cdcpub
   QUOTA UNLIMITED ON SYSTEM
   QUOTA UNLIMITED ON SYSAUX;
GRANT CREATE SESSION TO cdcpub;
GRANT CREATE TABLE TO cdcpub;
GRANT CREATE TABLESPACE TO cdcpub;
GRANT UNLIMITED TABLESPACE TO cdcpub;
GRANT SELECT_CATALOG_ROLE TO cdcpub;
GRANT EXECUTE_CATALOG_ROLE TO cdcpub;
GRANT DBA TO cdcpub;
GRANT CREATE SEQUENCE TO cdcpub;
GRANT EXECUTE on DBMS_CDC_PUBLISH TO cdcpub;
EXECUTE DBMS_STREAMS_AUTH.GRANT_ADMIN_PRIVILEGE(grantee => 'cdcpub');
```

Step 6 Source Database DBA: Build the LogMiner data dictionary.

The source database DBA builds a LogMiner data dictionary at the source database so that redo transport services can transport this data dictionary to the staging database. This LogMiner data dictionary build provides the table definitions as they were just prior to beginning to capture change data. Change Data Capture automatically updates the data dictionary with any source table data definition language (DDL) operations that are made during the course of change data capture to ensure that the dictionary is always synchronized with the source database tables.

When building the LogMiner data dictionary, the source database DBA should get the SCN value of the data dictionary build. In Step 8, when the publisher creates a change source, he or she will need to provide this value as the `first_scn` parameter.

```
SET SERVEROUTPUT ON
VARIABLE f_scn NUMBER;
BEGIN
    :f_scn := 0;
    DBMS_CAPTURE_ADM.BUILD(:f_scn);
    DBMS_OUTPUT.PUT_LINE('The first_scn value is ' || :f_scn);
END;
/
The first_scn value is 207722
```

For asynchronous AutoLog publishing to work, it is critical that the source database DBA build the data dictionary (and the build completes) before the source tables are prepared. The source database DBA must be careful to follow Step 6 and Step 7 in the order they are presented here.

See [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/toc.htm) for more information on the LogMiner data dictionary.

Step 7 Source Database DBA: Prepare the source tables.

The source database DBA must prepare the source tables on the source database for asynchronous Change Data Capture by instantiating each source table so that the underlying Oracle Streams environment records the information it needs to capture each source table's changes. The source table structure and the column datatypes must be supported by Change Data Capture. See "Datatypes and Table Structures Supported for Asynchronous Change Data Capture" for more information.

```
BEGIN
   DBMS_CAPTURE_ADM.PREPARE_TABLE_INSTANTIATION(
       TABLE_NAME => 'sh.products');
END;
/
```

Step 8 Source Database DBA: Get the global name of the source database.

In Step 8, the publisher will need to reference the global name of the source database. The global name of the source database will be used on the staging database to create the AutoLog change source. The source database DBA can query the `GLOBAL_NAME` column in the `GLOBAL_NAME` view on the source database to retrieve this information for the publisher:

```
SELECT GLOBAL_NAME FROM GLOBAL_NAME;
GLOBAL_NAME                                                                     
----------------------------------------------------------------------------
HQDB
```

Step 9 Staging Database Publisher: Identify each change source database and create the change sources.

The publisher uses the `DBMS_CDC_PUBLISH.CREATE_AUTOLOG_CHANGE_SOURCE` procedure on the staging database to create change sources.

The process of managing the capture system begins with the creation of a change source. A change source describes the source database from which the data will be captured, and manages the relationship between the source database and the staging database. A change source always specifies the SCN of a data dictionary build from the source database as its `first_scn` parameter.

The publisher gets the SCN of the data dictionary build and the global database name from the source database DBA (as shown in Step 5 and Step 7, respectively). If the publisher cannot get the value to use for the `first_scn` parameter value from the source database DBA, then, with the appropriate privileges, he or she can query the `V$ARCHIVED_LOG` view on the source database to determine the value. This is described in the `DBMS_CDC_PUBLISH` chapter of the [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_cdcpub.htm#ARPLS023).

On the staging database, the publisher creates the AutoLog change source and specifies the global name as the `source_database` parameter value and the SCN of the data dictionary build as the `first_scn` parameter value. To create an AutoLog online change source:

```
BEGIN
   DBMS_CDC_PUBLISH.CREATE_AUTOLOG_CHANGE_SOURCE(
       change_source_name  => 'CHICAGO',
       description         => 'test source',
       source_database     => 'HQDB',
       first_scn           => 207722,
       online_log          => 'y');
END;
/
```

To create an AutoLog archive change source:

```
BEGIN
   DBMS_CDC_PUBLISH.CREATE_AUTOLOG_CHANGE_SOURCE(
       change_source_name   => 'CHICAGO',
       description          => 'test source',
       source_database      => 'HQDB',
       first_scn            => 207722);
END;
/
```

Step 10 Staging Database Publisher: Create change sets.

The publisher uses the `DBMS_CDC_PUBLISH.CREATE_CHANGE_SET` procedure on the staging database to create change sets. The publisher can optionally provide beginning and ending dates to indicate where to begin and end the data capture.

Note that when Change Data Capture creates a change set, its associated Oracle Streams capture and apply processes are also created (but not started).

The following example shows how to create a change set called `CHICAGO_DAILY` that captures changes starting today, and continues capturing change data indefinitely. (If, at some time in the future, the publisher decides that he or she wants to stop capturing change data for this change set, he or she should disable the change set and then drop it.)

```
BEGIN
   DBMS_CDC_PUBLISH.CREATE_CHANGE_SET(
       change_set_name    => 'CHICAGO_DAILY',
       description        => 'change set for product info',
       change_source_name => 'CHICAGO',
       stop_on_ddl        => 'y');
END;
/
```

Step 11 Staging Database Publisher: Create the change tables.

The publisher uses the `DBMS_CDC_PUBLISH.CREATE_CHANGE_TABLE` procedure on the staging database to create change tables.

The publisher creates one or more change tables for each source table to be published, specifies which columns should be included, and specifies the combination of before and after images of the change data to capture.

The publisher can set the `options_string` field of the `DBMS_CDC_PUBLISH.CREATE_CHANGE_TABLE` procedure to have more control over the physical properties and tablespace properties of the change tables. The `options_string` field can contain any option available (except partitioning) on the `CREATE` `TABLE` statement. In this example, it specifies a tablespace for the change set. (This example assumes that the publisher previously created the `TS_CHICAGO_DAILY` tablespace.)

The following example creates a change table on the staging database that captures changes made to a source table in the source database. The example uses the sample table `sh.products`.

```
BEGIN
   DBMS_CDC_PUBLISH.CREATE_CHANGE_TABLE(
       owner             => 'cdcpub',
       change_table_name => 'products_ct',
       change_set_name   => 'CHICAGO_DAILY',
       source_schema     => 'SH',
       source_table      => 'PRODUCTS',
       column_type_list  => 'PROD_ID NUMBER(6), PROD_NAME VARCHAR2(50),
          PROD_LIST_PRICE NUMBER(8,2)',
          JOB_ID VARCHAR2(10), DEPARTMENT_ID NUMBER(4)',
       capture_values    => 'both',
       rs_id             => 'y',
       row_id            => 'n',
       user_id           => 'n',
       timestamp         => 'n',
       object_id         => 'n',
       source_colmap     => 'n',
       target_colmap     => 'y',
       options_string    => 'TABLESPACE TS_CHICAGO_DAILY');
END;
/
```

This example creates a change table named `products_ct` within change set `CHICAGO_DAILY`. The `column_type_list` parameter identifies the columns captured by the change table. The `source_schema` and `source_table` parameters identify the schema and source table that reside in the source database, not the staging database.

The `capture_values` setting in the example indicates that for update operations, the change data will contain two separate rows for each row that changed: one row will contain the row values before the update occurred and the other row will contain the row values after the update occurred.

See "Managing Change Tables" for more information.

Step 12 Staging Database Publisher: Enable the change set.

Because asynchronous change sets are always disabled when they are created, the publisher must alter the change set to enable it. The Oracle Streams capture and apply processes are started when the change set is enabled.

```
BEGIN
   DBMS_CDC_PUBLISH.ALTER_CHANGE_SET(
       change_set_name => 'CHICAGO_DAILY',
       enable_capture  => 'y');
END;
/
```

Step 13 Source Database DBA: Switch the redo log files at the source database.

To begin capturing data, a log file must be archived. The source database DBA can initiate the process by switching the current redo log file:

```
ALTER SYSTEM SWITCH LOGFILE;
```

Step 14 Staging Database Publisher: Grant access to subscribers.

The publisher controls subscriber access to change data by granting and revoking the SQL `SELECT` privilege on change tables for users and roles on the staging database. The publisher grants access to specific change tables. Without this step, a subscriber cannot access any change data. This example assumes that user `subscriber1` already exists.

```
GRANT SELECT ON cdcpub.products_ct TO subscriber1;
```

The Change Data Capture asynchronous AutoLog system is now ready for `subscriber1` to create subscriptions.

## Subscribing to Change Data

When a publisher creates a change table, Change Data Capture assigns it a publication ID and maintains a list of all the publication IDs in the `DBA_PUBLISHED_COLUMNS` view. A publication ID is a numeric value that Change Data Capture assigns to each change table defined by the publisher.

The subscribers register their interest in one or more source tables, and obtain subscriptions to these tables. Assuming sufficient access privileges, the subscribers may subscribe to any source tables for which the publisher has created one or more change tables by doing one of the following:

- Specifying the source tables and columns of interest.
	When there are multiple publications that contain the columns of interest, then Change Data Capture selects one on behalf of the user.
- Specifying the publication IDs and columns of interest.
	When there are multiple publications on a single source table and these publications share some columns, the subscriber should specify publication IDs (rather than source tables) if any of the shared columns will be used in a single subscription.

The following steps provide an example to demonstrate both scenarios:

Step 1 Find the source tables for which the subscriber has access privileges.

The subscriber queries the `DBA_SOURCE_TABLES` view to see all the published source tables for which the subscriber has access privileges:

```
SELECT * FROM DBA_SOURCE_TABLES;

SOURCE_SCHEMA_NAME             SOURCE_TABLE_NAME
------------------------------ ------------------------------
SH                             PRODUCTS
```

Step 2 Find the change set names and columns for which the subscriber has access privileges.

The subscriber queries the `DBA_PUBLISHED_COLUMNS` view to see all the change sets, columns, and publication IDs for the `sh.products` table for which the subscriber has access privileges:

```
SELECT UNIQUE CHANGE_SET_NAME, COLUMN_NAME, PUB_ID 
FROM DBA_PUBLISHED_COLUMNS
WHERE SOURCE_SCHEMA_NAME ='SH' AND SOURCE_TABLE_NAME = 'PRODUCTS';

CHANGE_SET_NAME     COLUMN_NAME        PUB_ID
----------------    ------------------ ------------ 
CHICAGO_DAILY       PROD_ID            41494
CHICAGO_DAILY       PROD_LIST_PRICE    41494
CHICAGO_DAILY       PROD_NAME          41494
```

Step 3 Create a subscription.

The subscriber calls the `DBMS_CDC_SUBSCRIBE`.`CREATE_SUBSCRIPTION` procedure to create a subscription.

The following example shows how the subscriber identifies the change set of interest (`CHICAGO_DAILY`), and then specifies a unique subscription name that will be used throughout the life of the subscription:

```
BEGIN
       DBMS_CDC_SUBSCRIBE.CREATE_SUBSCRIPTION(
       change_set_name   => 'CHICAGO_DAILY',
       description       => 'Change data for PRODUCTS',
       subscription_name => 'SALES_SUB');
END;
/
```

Step 4 Subscribe to a source table and the columns in the source table.

The subscriber calls the `DBMS_CDC_SUBSCRIBE`.`SUBSCRIBE` procedure to specify which columns of the source tables are of interest to the subscriber.

A subscription can contain one or more source tables referenced by the same change set.

In the following example, the subscriber wants to see the `PROD_ID`, `PROD_NAME`, and `PROD_LIST_PRICE` columns from the `PRODUCTS` table. Because all these columns are contained in the same publication (and the subscriber has privileges to access that publication) as shown in the query in Step 2, the following call can be used:

```
BEGIN
       DBMS_CDC_SUBSCRIBE.SUBSCRIBE(
       subscription_name => 'SALES_SUB',
       source_schema     => 'SH',
       source_table      => 'PRODUCTS',
       column_list       => 'PROD_ID, PROD_NAME, PROD_LIST_PRICE',
       subscriber_view   => 'SALES_VIEW');
END;
/
```

However, assume that for security reasons the publisher has not created a single change table that includes all these columns. Suppose that instead of the results shown in Step 2, the query of the `DBA_PUBLISHED_COLUMNS` view shows that the columns of interest are included in multiple publications as shown in the following example:

```
SELECT UNIQUE CHANGE_SET_NAME, COLUMN_NAME, PUB_ID 
FROM DBA_PUBLISHED_COLUMNS
WHERE SOURCE_SCHEMA_NAME ='SH' AND SOURCE_TABLE_NAME = 'PRODUCTS';

CHANGE_SET_NAME     COLUMN_NAME        PUB_ID
----------------    ------------------ ------------ 
CHICAGO_DAILY       PROD_ID            34883
CHICAGO_DAILY       PROD_NAME          34885
CHICAGO_DAILY       PROD_LIST_PRICE    34883
CHICAGO_DAILY       PROD_ID            34885
```

This returned data shows that the `PROD_ID` column is included in both publication 34883 and publication 34885. A single subscribe call must specify columns available in a single publication. Therefore, if the subscriber wants to subscribe to columns in both publications, using `PROD_ID` to join across the subscriber views, then the subscriber must use two calls, each specifying a different publication ID:

```
BEGIN
       DBMS_CDC_SUBSCRIBE.SUBSCRIBE(
       subscription_name => 'MULTI_PUB',
       publication_id    => 34885,
       column_list       => 'PROD_ID, PROD_NAME',
       subscriber_view   => 'prod_idname');

       DBMS_CDC_SUBSCRIBE.SUBSCRIBE(
       subscription_name => 'MULTI_PUB',
       publication_id    => 34883, 
       column_list       => 'PROD_ID, PROD_LIST_PRICE',
       subscriber_view   => 'prod_price'); 
END; 
/
```

Note that each `DBMS_CDC_SUBSCRIBE.SUBSCRIBE` call specifies a unique subscriber view.

Step 5 Activate the subscription.

The subscriber calls the `DBMS_CDC_SUBSCRIBE``.ACTIVATE_SUBSCRIPTION` procedure to activate the subscription.

A subscriber calls this procedure when finished subscribing to source tables (or publications), and ready to receive change data. Whether subscribing to one or multiple source tables, the subscriber needs to call the `ACTIVATE_SUBSCRIPTION` procedure only once.

The `ACTIVATE_SUBSCRIPTION` procedure creates empty subscriber views. At this point, `DBMS_CDC_SUBSCRIBE.SUBSCRIBE` calls can be made.

```
BEGIN
   DBMS_CDC_SUBSCRIBE.ACTIVATE_SUBSCRIPTION(
       subscription_name => 'SALES_SUB');
END;
/
```

Step 6 Get the next set of change data.

The subscriber calls the `DBMS_CDC_SUBSCRIBE.EXTEND_WINDOW` procedure to get the next available set of change data. This sets the high boundary of the subscription window. For example:

```
BEGIN
   DBMS_CDC_SUBSCRIBE.EXTEND_WINDOW(
       subscription_name => 'SALES_SUB');
END;
/
```

If this is the subscriber's first call to the `EXTEND_WINDOW` procedure, then the subscription window contains all the change data in the publication. Otherwise, all the new change data that was created since the last call to the `EXTEND_WINDOW` procedure is added to the subscription window.

If no new change data has been added, then the subscription window remains unchanged.

Step 7 Read and query the contents of the subscriber views.

The subscriber uses the SQL `SELECT` statement on the subscriber view to query the change data (within the current boundaries of the subscription window). The subscriber can do this for each subscriber view in the subscription. For example:

```
SELECT PROD_ID, PROD_NAME, PROD_LIST_PRICE FROM SALES_VIEW;

PROD_ID    PROD_NAME                                          PROD_LIST_PRICE
---------- -------------------------------------------------- ---------------
30         And 2 Crosscourt Tee Kids                          14.99
30         And 2 Crosscourt Tee Kids                          17.66
10         Gurfield& Murks Pleated Trousers                   17.99
10         Gurfield& Murks Pleated Trousers                   21.99
```

The subscriber view name, `SALES_VIEW`, was specified when the subscriber called the `DBMS_CDC_SUBSCRIBE.SUBSCRIBE` procedure in Step 4.

Step 8 Indicate that the current set of change data is no longer needed.

The subscriber uses the `DBMS_CDC_SUBSCRIBE`.`PURGE_WINDOW` procedure to let Change Data Capture know that the subscriber no longer needs the current set of change data. This helps Change Data Capture to manage the amount of data in the change table and sets the low boundary of the subscription window. Calling the `DBMS_CDC_SUBSCRIBE`.`PURGE_WINDOW` procedure causes the subscription window to be empty. See "Purging Change Tables of Unneeded Data" for details on how the `DBMS_CDC_SUBSCRIBE`.`PURGE_WINDOW` works.

For example:

```
BEGIN
   DBMS_CDC_SUBSCRIBE.PURGE_WINDOW(
       subscription_name => 'SALES_SUB');
END;
/
```

Note:

Before using `DBMS_CDC_PUBLISH.PURGE`, call `DBMS_CDC_SUBSCRIBE.EXTEND_WINDOW`, which protects the data that is still needed by the subscriber and makes the publisher aware that there is some important data that should not be purged.

Step 9 Repeat Steps 6 through 8.

The subscriber repeats Steps 6 through 8 as long as the subscriber is interested in additional change data.

Step 10 End the subscription.

The subscriber uses the `DBMS_CDC_SUBSCRIBE`.`DROP_SUBSCRIPTION` procedure to end the subscription. This is necessary to prevent the publications that underlie the subscription from holding change data indefinitely.

```
BEGIN
   DBMS_CDC_SUBSCRIBE.DROP_SUBSCRIPTION(
       subscription_name => 'SALES_SUB');
END;
/
```

## Managing Published Data

This section provides information about the management tasks involved in managing change sets and change tables. For the most part, these tasks are the responsibility of the publisher. However, to purge unneeded data from the change tables, both the publisher and the subscribers have responsibilities as described in "Purging Change Tables of Unneeded Data"

The following topics are covered in this section:

- Managing Asynchronous Change Sources
- Managing Asynchronous Change Sets
- Managing Change Tables
- Exporting and Importing Change Data Capture Objects Using Oracle Data Pump
- Impact on Subscriptions When the Publisher Makes Changes

### Managing Asynchronous Change Sources

This section provides information about tasks that the publisher can perform to manage asynchronous change sources. The following topic is covered:

- Enabling And Disabling Asynchronous Distributed HotLog Change Sources

#### Enabling And Disabling Asynchronous Distributed HotLog Change Sources

The publisher can enable and disable asynchronous Distributed HotLog change sources. When a change source is disabled, it cannot process new change data until the change source is enabled.

Asynchronous Distributed HotLog change sources are always created disabled.

The publisher can enable the `PRODUCTS_SOURCE` asynchronous Distributed HotLog change source with the following call:

```
BEGIN
DBMS_CDC_PUBLISH.ALTER_HOTLOG_CHANGE_SOURCE(
change_source_name => 'PRODUCTS_SOURCE',
enable_source      => 'y');
END;
/
```

The Oracle Streams capture process for the change source is started when the change source is enabled.The publisher can disable the `PRODUCTS_SOURCE` asynchronous Distributed HotLog change source using the same call, but with enable\_source set to `'n'`. The Oracle Streams capture process for the change source is stopped when the change source is disabled.

An asynchronous Distributed HotLog change source and its change sets must be enabled separately in order to process change data and populate change tables. See "Enabling and Disabling Asynchronous Change Sets" for more information.

Although a disabled change source cannot process new change data, it does not lose any change data, provided the necessary archived redo log files remain available until the change source and its changes sets are enabled and can process them. Oracle recommends that change sources and change sets be enabled as much as possible to avoid accumulating archived redo log files. See "Asynchronous Change Data Capture and Redo Log Files" for more information.

### Managing Asynchronous Change Sets

This section provides information about tasks that the publisher can perform to manage asynchronous change sets. The following topics are covered:

- Creating Asynchronous Change Sets with Starting and Ending Dates
- Enabling and Disabling Asynchronous Change Sets
- Stopping Capture on DDL for Asynchronous Change Sets
- Recovering from Errors Returned on Asynchronous Change Sets

#### Creating Asynchronous Change Sets with Starting and Ending Dates

Change sets associated with asynchronous HotLog and AutoLog change sources can optionally specify starting and ending dates to limit the change data they capture. (Change sets associated with Distributed HotLog change sources cannot specify starting and ending dates). A change set with no starting date begins capture with the earliest available change data. A change set with no ending date continues capturing change data indefinitely.

The following example creates a change set, `PRODUCTS_SET`, in the AutoLog change source, `HQ_SOURCE,` that starts capture two days from now and continues indefinitely:

```
BEGIN
DBMS_CDC_PUBLISH.CREATE_CHANGE_SET(
```
```
change_set_name    => 'PRODUCTS_SET',
description        => 'Products Application Change Set',
change_source_name => 'HQ_SOURCE',
stop_on_ddl        => 'Y',
begin_date         => sysdate+2);
```
```
END;
/
```

#### Enabling and Disabling Asynchronous Change Sets

The publisher can enable and disable asynchronous change sets. When a change set is disabled, it cannot process new change data until the change set is enabled.

Synchronous change sets are always created enabled. Asynchronous change sets are always created disabled.

The publisher can enable the `PRODUCTS_SET` asynchronous change set with the following call:

```
BEGIN
DBMS_CDC_PUBLISH.ALTER_CHANGE_SET(
```
```
change_set_name => 'PRODUCTS_SET',
enable_capture  => 'y');
```
```
END;
/
```

For asynchronous HotLog and AutoLog change sets, the Oracle Streams capture and apply processes are started when the change set is enabled. For asynchronous Distributed HotLog change sets, the Oracle Streams apply process is started when the change set is enabled.

The publisher can disable the `PRODUCTS_SET` asynchronous change set using the same call, but with `enable_capture` set to `'n'`. For asynchronous HotLog and AutoLog change sets, the Oracle Streams capture and apply processes are stopped when the change set is disabled. For asynchronous Distributed HotLog change sets, the Oracle Streams apply process is stopped when the change set is disabled.

An asynchronous Distributed HotLog change source and its change sets must be enabled separately in order to process change data and populate change tables. See "Enabling And Disabling Asynchronous Distributed HotLog Change Sources" for more information.

Although a disabled change set cannot process new change data, it does not lose any change data if the necessary archived redo log files remain available until the change set is enabled and processes them. Oracle recommends that change sets be enabled as much as possible to avoid accumulating archived redo log files. See "Asynchronous Change Data Capture and Redo Log Files" for more information.

Change Data Capture can automatically disable an asynchronous change set if there is an internal capture error. The publisher must check the alert log for more information, take any necessary actions to adjust to the DDL or recover from the internal error, and explicitly enable the change set. See "Recovering from Errors Returned on Asynchronous Change Sets" for more information.

#### Stopping Capture on DDL for Asynchronous Change Sets

The publisher can specify that a change set be automatically disabled by Change Data Capture if DDL is encountered. Some DDL commands can adversely affect capture, such as dropping a source table column that is being captured. If the change set stops on DDL, the publisher has a chance to analyze and fix the problem before capture proceeds. If the change set does not stop on DDL, internal capture errors are possible after DDL occurs.

The publisher can specify whether a change set stops on DDL when creating or altering the change set. The publisher can alter the `PRODUCTS_SET` change set to stop on DDL with the following call:

```
BEGIN
DBMS_CDC_PUBLISH.ALTER_CHANGE_SET(
```
```
change_set_name  => 'PRODUCTS_SET',
stop_on_ddl      => 'y');
```
```
END;
/
```

The publisher can alter the `PRODUCTS_SET` change set so that it does not stop on DDL by setting `stop_on_ddl` to `'n'`.

If a DDL statement causes processing to stop, a message is written to the alert log indicating the DDL statement and change set involved. For example, if a `TRUNCATE TABLE` DDL statement causes the `PRODUCTS_SET` change set to stop processing, the alert log contains lines such as the following:

```
Change Data Capture received DDL for change set PRODUCTS_SET
Change Data Capture received DDL and stopping: truncate table products
```

Because they do not affect the column data itself, the following DDL statements do not cause Change Data Capture to stop capturing change data when the `stop_on_ddl` parameter is set to `'Y'`:

- `ANALYZE TABLE`
- `LOCK TABLE`
- `GRANT` privileges to access a table
- `REVOKE` privileges to access a table
- `COMMENT` on a table
- `COMMENT` on a column

These statements can be issued on the source database without concern for their impact on Change Data Capture processing. For example, when an `ANALYZE` `TABLE` command is issued on the `PRODUCTS` source table, the alert log on the staging database will contain a line similar to the following when the `stop_on_ddl` parameter is set to `'Y'`:

```
Change Data Capture received DDL and ignoring: analyze table products compute statistics
```

#### Recovering from Errors Returned on Asynchronous Change Sets

Errors during asynchronous Change Data Capture are possible due to a variety of circumstances. If a change set stops on DDL, that DDL must be removed before capture can continue. If a change set does not stop on DDL, but a DDL change occurs that affects capture, it can result in an Oracle error. There are also system conditions that can cause Oracle errors, such as being out of disk space.

In all these cases, the change set is disabled and marked as having an error. Subscriber procedures detect when a change set has an error and return the following message:

```
ORA-31514: change set disabled due to capture error
```

The publisher must check the alert log for more information and attempt to fix the underlying problem. The publisher can then attempt to recover from the error by calling `ALTER_CHANGE_SET` with the `recover_after_error` and `remove_ddl` parameters set to ' `y` '.

The publisher can repeat this procedure as many times as necessary to resolve the problem. When recovery succeeds, the error is removed from the change set and the publisher can enable the asynchronous change set (as described in "Enabling and Disabling Asynchronous Change Sets").

The publisher should be aware that if there are multiple consecutive DDLs, the change set stops for each one separately. For example, suppose there are two consecutive DDLs. When the change set stops for the first DDL, the publisher must remove that DDL and then re-enable capture for the change set. The change set will then stop for the second DDL. The publisher must remove the second DDL and re-enable capture for the change set again.

If more information is needed to resolve capture errors, the publisher can query the `DBA_APPLY_ERROR` view to see information about Streams apply errors; capture errors correspond to Streams apply errors. The publisher must always use the `DBMS_CDC_PUBLISH.ALTER_CHANGE_SET` procedure to recover from capture errors because both Streams and Change Data Capture actions are needed for recovery and only the `DBMS_CDC_PUBLISH.ALTER_CHANGE_SET` procedure performs both sets of actions. See [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/toc.htm) for information about the error queue and apply errors.

The following two scenarios demonstrate how a publisher might investigate and then recover from two different types of errors returned to Change Data Capture:

##### An Error Due to Running Out of Disk Space

The publisher can view the contents of the alert log to determine which error is being returned for a given change set and which SCN is not being processed. For example, the alert log may contain lines such as the following (where LCR refers to a logical change record):

```
Change Data Capture has encountered error number: 1688 for change set: 
   CHICAGO_DAILY
Change Data Capture did not process LCR with scn 219337
```

The publisher can determine the message associated with the error number specified in the alert log by querying the `DBA_APPLY_ERROR` view for the error message text, where the `APPLY_NAME` in the `DBA_APPLY_ERROR` view equals the `APPLY_NAME` of the change set specified in the alert log. For example:

```
SQL> SELECT ERROR_MESSAGE FROM DBA_APPLY_ERROR
       WHERE APPLY_NAME =
      (SELECT APPLY_NAME FROM ALL_CHANGE_SETS WHERE SET_NAME ='CHICAGO_DAILY');

ERROR_MESSAGE 
-------------------------------------------------------------------------------- 
ORA-01688: unable to extend table LOGADMIN.CT1 partition P1 by 32 in tablespace 
    TS_CHICAGO_DAILY
```

After taking action to fix the problem that is causing the error, the publisher can attempt to recover from the error. For example, the publisher can attempt to recover the `CHICAGO_DAILY` change set after an error with the following call:

```
BEGIN
DBMS_CDC_PUBLISH.ALTER_CHANGE_SET(
  change_set_name     => 'CHICAGO_DAILY',
  recover_after_error => 'y');
END;
/
```

If the recovery does not succeed, then an error is returned and the publisher can take further action to attempt to resolve the problem. The publisher can retry the recovery procedure as many times as necessary to resolve the problem.

Note:

When recovery succeeds, the publisher must remember to enable the change set. After being enabled, the change data capture operation will proceed with the logical change record (LCR) where the error occurred. No change data will be lost.

##### An Error Due to Stopping on DDL

Suppose a SQL `TRUNCATE` `TABLE` statement is issued against the `PRODUCTS` source table and the `stop_on_ddl` parameter is set to `'Y'`, then an error such as the following is returned from an attempt to enable the change set:

```
ERROR at line 1:
ORA-31468: cannot process DDL change record
ORA-06512: at "SYS.DBMS_CDC_PUBLISH", line 79
ORA-06512: at line 2
```

The alert log will contain lines similar to the following:

```
Mon Jun  9 16:13:44 2003
Change Data Capture received DDL for change set PRODUCTS_SET
Change Data Capture received DDL and stopping: truncate table products
Mon Jun  9 16:13:50 2003
Change Data Capture did not process LCR with scn 219777
Streams Apply Server P001 pid=19 OS id=11730 stopped
Streams Apply Reader P000 pid=17 OS id=11726 stopped
Streams Apply Server P000 pid=17 OS id=11726 stopped
Streams Apply Server P001 pid=19 OS id=11730 stopped
Streams AP01 with pid=15, OS id=11722 stopped
```

Because the `TRUNCATE` `TABLE` statement removes all rows from a table, the publisher will want to notify subscribers before taking action to re-enable Change Data Capture processing. He or she might suggest to subscribers that they purge and extend their subscription windows. The publisher can then attempt to restore Change Data Capture processing by altering the change set and specifying the `remove_ddl` `=>` `'Y'` parameter along with the `recover_after_error` `=>` `'Y'` parameter, as follows:

```
BEGIN
DBMS_CDC_PUBLISH.ALTER_CHANGE_SET(
```
```
change_set_name     => 'PRODUCTS_SET',
recover_after_error => 'y',
remove_ddl          => 'y');
```
```
END;
/
```

After this procedure completes, the alert log will contain lines similar to the following:

```
Mon Jun  9 16:20:17 2003
Change Data Capture received DDL and ignoring: truncate table products
The scn for the truncate statement is 202998
```

Now, the publisher must enable the change set. All change data that occurred after the `TRUNCATE TABLE` statement will be reflected in the change table. No change data will be lost.

### Managing Synchronous Change Sets

The publisher can enable and disable synchronous change sets. When a change set is disabled, it cannot process new change data until the change set is enabled.

#### Enabling and Disabling Synchronous Change Sets

Synchronous change sets are always created enabled. Asynchronous change sets are always created disabled.

The publisher can enable the `PRODUCTS_SET` synchronous change set with the following call:

```
BEGIN
DBMS_CDC_PUBLISH.ALTER_CHANGE_SET(
```
```
change_set_name => 'PRODUCTS_SET',
enable_capture  => 'y');
```
```
END;
/
```

The publisher can disable the `PRODUCTS_SET` synchronous change set using the same call, but with `enable_capture` set to `'n'`.

### Managing Change Tables

All change table management tasks are the responsibility of the publisher with one exception: purging change tables of unneeded data. This task requires action from both the publisher and the subscriber to work most effectively.

The following topics are discussed in this section:

- Creating Change Tables
- Understanding Change Table Control Columns
- Understanding TARGET\_COLMAP$ and SOURCE\_COLMAP$ Values
- Using Change Markers
- Controlling Subscriber Access to Change Tables
- Purging Change Tables of Unneeded Data
- Dropping Change Tables

#### Creating Change Tables

When creating change tables, the publisher should be aware that Oracle recommends the following:

- For all modes of Change Data Capture, publishers should not create change tables in system tablespaces.
	Either of the following methods can be used to ensure that change tables are created in tablespaces managed by the publisher. The first method creates all the change tables created by the publisher in a single tablespace, while the second method allows the publisher to specify a different tablespace for each change table.
	- When the database administrator creates the account for the publisher, he or she can specify a default tablespace. For example:
		```
		CREATE USER cdcpub DEFAULT TABLESPACE ts_cdcpub;
		```
		- When the publisher creates a change table, he or she can use the `options_string` parameter to specify a tablespace for the change table being created. See Step 4 in "Performing Synchronous Publishing" for an example.
	If both methods are used, the tablespace specified by the publisher in the `options_string` parameter takes precedence over the default tablespace specified in the SQL `CREATE` `USER` statement.
- For asynchronous Change Data Capture, the publisher should be certain that the source table that will be referenced in a `DBMS_CDC_PUBLISH.CREATE_CHANGE_TABLE` procedure has been created prior to calling this procedure, particularly if the change set that will be specified in the procedure has the `stop_on_ddl` parameter set to `'Y'`.
	Suppose the publisher created a change set with the `stop_on_ddl` parameter set to `'Y'`, then created the change table, and then the source table was created. In this scenario, the DDL that creates the source table would trigger the `stop_on_ddl` condition and cause Change Data Capture processing to stop.
	Note:
	The publisher must not attempt to control a change table's partitioning properties. Change Data Capture automatically manages the change table partitioning as part of its change table management.
- For asynchronous Change Data Capture, the source database DBA should create an unconditional log group for all source table columns that will be captured in a change table. This should be done before any change tables are created on a source table. If an unconditional log group is not created for source table columns to be captured, then when an update DML operation occurs, some unchanged user column values in change tables will be null instead of reflecting the actual source table value. This will require the publisher to evaluate the `TARGET_COLMAP$` control column to distinguish unchanged column values from column values that are actually null. See "Asynchronous Change Data Capture and Supplemental Logging" for information on creating unconditional log groups and see "Understanding Change Table Control Columns" for information on control columns.

#### Understanding Change Table Control Columns

A change table consists of two things: the change data itself, which is stored in a database table, and the system metadata necessary to maintain the change table, which includes control columns.

Table 17-11 describes the control columns for a change table, including the column name, datatype, mode, whether the column is optional or not, and a description.

The mode indicates the type of Change Data Capture associated with the column. A value of `ALL` indicates that the column is associated with the synchronous mode and all modes of asynchronous Change Data Capture. Note that for both synchronous and asynchronous Change Data Capture, if the subscriber wants a query of a subscriber view to return DML changes in the order in which they occurred, the query should order data by `CSCN$` and then `RSID$`.

A control column is considered optional if the publisher can choose to exclude it from a change table. Table 17-11 identifies which control columns are optional under what modes. All optional control columns are specified with a parameter in the `DBMS_CDC_PUBLISH.CREATE_CHANGE_TABLE` procedure. The syntax for the `DBMS_CDC_PUBLISH.CREATE_CHANGE_TABLE` procedure is documented in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_cdcpub.htm#ARPLS023).

Table 17-11 Control Columns for a Change Table

| Column | Datatype | Mode | Optional Column | Description |
| --- | --- | --- | --- | --- |
| `OPERATION$` | `CHAR(2)` | All | No | The value in this column can be any one of the following <sup>Foot 1</sup> :  `I`: Indicates this row represents an insert operation  `UO`: Indicates this row represents the before-image of an updated source table row for the following cases:  - Asynchronous Change Data Capture - Synchronous Change Data Capture when the change table includes a primary key-based object ID and a captured column that is not a primary key has changed.  `UU`: Indicates this row represents the before-image of an updated source table row for synchronous Change Data Capture, in cases other than those represented by `UO`.  `UN`: Indicates this row represents the after-image of an updated source table row.  `D`: Indicates this row represents a delete operation. |
| `CSCN$` | `NUMBER` | All | No | For synchronous CDC, the value for the `EXTEND_WINDOW` operation. For asynchronous CDC, the value for the DML operation. |
| `DDLDESC$` | `CLOB` | Asynchronous | Yes | A clob containing the actual DDL statement executed. |
| `DDLPDOBJN$` | `NUMBER` | Asynchronous | Yes | This is not used in this release. |
| `DDLOPER$` | `NUMBER` | Asynchronous | Yes | A bit vector that indicates what kind of DDL operation happened. |
| `RSID$` | `NUMBER` | All | Yes | Unique row sequence ID within this transaction.<sup>Foot 2</sup> The `RSID$` column reflects an operation's capture order within a transaction, but not across transactions. The publisher cannot use the `RSID$` column value by itself to order committed operations across transactions; it must be used in conjunction with the `CSCN$` column value. |
| `SOURCE_COLMAP$` | `RAW(128)` | Synchronous | Yes | Bit mask <sup>Foot 3</sup> of updated columns in the source table. |
| `TARGET_COLMAP$` | `RAW(128)` | All | Yes | Bit mask <sup>Footref 3</sup> of updated columns in the change table. |
| `COMMIT_TIMESTAMP$` | `DATE` | All | No | Commit time of this transaction. |
| `TIMESTAMP$` | `DATE` | All | Yes | Time when the operation occurred in the source table. |
| `USERNAME$` | `VARCHAR2(30)` | All | Yes | Name of the user who caused the operation. Value is always `NULL` for change sources created on Oracle Databases prior to release 10.2. |
| `ROW_ID$` | `ROW_ID` | All | Yes | Row ID of affected row in source table. Value is always NULL for change sources created on Oracle Databases prior to release 10.2. |
| `XIDUSN$` | `NUMBER` | Asynchronous | No | Transaction ID undo segment number. |
| `XIDSLT$` | `NUMBER` | Asynchronous | No | Transaction ID slot number. |
| `XIDSEQ$` | `NUMBER` | Asynchronous | No | Transaction ID sequence number. |
| `SYS_NC_OID$` | `RAW(16)` | Synchronous | Yes | Object ID. |

<sup>Footnote 1</sup> If you specify a query based on this column, specify the `I` or `D` column values as "I " or "D ", respectively. The `OPERATION$` column is a 2-character column; values are left-justified and space-filled. A query that specifies a value of "I" or "D" will return no values.

<sup>Footnote 2</sup> You can use the `RSID$` column to associate the after-image with the before-image of a given operation. The value of the after-image `RSID$` column always matches the value of the before-image `RSID$` column value for a given update operation.

<sup>Footnote 3</sup> A bit mask is an array of binary values that indicate which columns in a row have been updated.

#### Understanding TARGET\_COLMAP$ and SOURCE\_COLMAP$ Values

The `TARGET_COLMAP$` and `SOURCE_COLMAP$` columns are used to indicate which columns in a row have changed. The `TARGET_COLMAP$` column indicates which columns in the change table row have changed. The `SOURCE_COLMAP$` column (which is included for synchronous change tables only) indicates which columns in a source table row have changed.

Because the datatype of the `TARGET_COLMAP$` and the `SOURCE_COLMAP$` columns is `RAW(128)`, each column can hold 128 bytes of binary information. This binary information consists of words strung together with the low order byte on the left and the high order byte on the right. By default, when the field is displayed, the system interprets each byte and displays a value for each. Example 17-1 provides a sample `TARGET_COLMAP$` value. The text following the example explains how to interpret this data.

Example 17-1 Sample TARGET\_COLMAP$ VALUE

```
FE110000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
000000000000
```

In Example 17-1, the first 'FE' is the low order byte and the last '00' is the high order byte. To correctly interpret the meaning of the values, you must consider which bits are set in each byte. The bits in the bitmap are counted starting at zero. The first bit is bit 0, the second bit is bit 1, and so on. Bit 0 is always ignored. For the other bits, if a particular bit is set to 1, it means that the value for that column has been changed.

To interpret the string of bytes as presented in the Example 17-1, you read from left to right. The first byte is the string 'FE'. Broken down into bits (again from left to right) this string is "1111 1110", which maps to columns " 7,6,5,4 3,2,1,-" in the change table (where the hyphen represents the ignored bit). The first bit tells you if column 7 in the change table has changed. The right-most bit is ignored. The values in Example 17-1 indicate that the first 7 columns have a value present. This is typical - the first several columns in a change table are control columns.

The next byte in Example 17-1 is the string '11'. Broken down into bits, this string is "0001 0001", which maps to columns "15,14,13,12 11,10,9,8" in the change table. These bits indicate that columns 8 and 12 are changed. Columns 9, 10, 11, 13, 14, 15, are not changed. The rest of the string is all '00', indicating that none of the other columns has been changed.

A publisher can issue the following query to determine the mapping of column numbers to column names:

```
SELECT COLUMN_NAME, COLUMN_ID FROM ALL_TAB_COLUMNS 
WHERE OWNER='PUBLISHER_STEWART' AND TABLE_NAME='MY_CT';

COLUMN_NAME                    COLUMN_ID
------------------------------ ----------
OPERATION$                           1
CSCN$                                2
COMMIT_TIMESTAMP$                    3
XIDUSN$                              4
XIDSLT$                              5
XIDSEQ$                              6
RSID$                                7
TARGET_COLMAP$                       8
C_ID                                 9
C_KEY                                10
C_ZIP                                11

COLUMN_NAME                     COLUMN_ID
------------------------------ ----------
C_DATE                               12
C_1                                  13
C_3                                  14
C_5                                  15
C_7                                  16
C_9                                  17
```

Using Example 17-1, the publisher can conclude that following columns were changed in the particular change row in the change table represented by this `TARGET_COLMAP$` value: `OPERATION$`, `CSCN$`, `COMMIT_TIMESTAMP$`, `XIDUSN$`, `XIDSLT$`, `XIDSEQ$`, `RSID$`, `TARGET_COLMAP$`, and `C_DATE`.

Note that Change Data Capture generates values for all control columns in all change rows, so the bits corresponding to control columns are always set to 1 in every `TARGET_COLMAP$` column. Bits that correspond to user columns that have changed are set to 1 for the `OPERATION$` column values `UN` and `I`, as appropriate. (See Table 17-11 for information about the `OPERATION$` column values.) Also note that if you use asynchronous CDC, you will always see a 1 for the columns that were included in the `UPDATE` `SET` clause, irrespective of whether the value was actually changed from its original value. For synchronous CDC, you will only see a 1 if the value was changed from its original value.

A common use for the values in the `TARGET_COLMAP$` column is for determining the meaning of a null value in a change table. A column value in a change table can be null for two reasons: the value was changed to null by a user or application, or Change Data Capture inserted a null value into the column because a value was not present in the redo data from the source table. If a user changed the value to null, the bit for that column will be set to 1; if Change Data Capture set the value to null, then the column will be set to 0.

Values in the `SOURCE_COLMAP$` column are interpreted in a similar manner, with the following exceptions:

- The `SOURCE_COLMAP$` column refers to columns of source tables, not columns of change tables.
- The `SOURCE_COLMAP$` column does not reference control columns because these columns are not present in the source table.
- Changed source columns are set to 1 in the `SOURCE_COLMAP$` column for `OPERATION$` column values `UO`, `UU`, `UN`, and `I`, as appropriate. (See Table 17-11 for information about the `OPERATION$` column values.)
- The `SOURCE_COLMAP$` column is valid only for synchronous change tables.

#### Using Change Markers

The following example illustrates how to use change markers. First, create the change set:

```
BEGIN
   DBMS_CDC_PUBLISH.CREATE_CHANGE_SET (
      CHANGE_SET_NAME     => 'async_set1',
      CHANGE_SOURCE_NAME  => 'HOTLOG_SOURCE',
      STOP_ON_DDL         => 'N',
      BEGIN_DATE          => SYSDATE,
      END_DATE            => SYSDATE+5);

PL/SQL procedure successfully completed
```

Next, create the change table. Note that this should have the three DDL markers `ddloper$`, `ddldesc$`, and `ddlpdobjn$`.

```
BEGIN
   DBMS_CDC_PUBLISH.CREATE_CHANGE_TABLE (
      OWNER             => 'tcdcpub',
      CHANGE_TABLE_NAME => 'cdc_psales_act',
      CHANGE_SET_NAME   => 'async_set1',
      SOURCE_SCHEMA     => 'tcdcpub',
      SOURCE_TABLE      => 'cdc_psales',
      COLUMN_TYPE_LIST  => 'PROD_IC NUMBER(6)
         NUMBER, TIME_ID DATE',
      CAPTURE_VALUES    => 'both',
      RS_ID             => 'N',
      ROW_ID            => 'N',
      USER_ID           => 'N',
      TIMESTAMP         => 'N',
      OBJECT_ID         => 'N',
      SOURCE_COLMAP     => 'N',
      TARGET_COLMAP     => 'Y',
      OPTIONS_STRING    => NULL,
      DDL_MARKERS       => 'Y');
END;
/

PL/SQL procedure successfully completed.
describe cdc_psales_act;

Name                    Null?     Type
---------------------------------------
OPERATION$                        CHAR(2)
CSCN$                             NUMBER
COMMIT_TIMESTAMP                  DATE
XIDUSN$                           NUMBER
XIDSLT$                           NUMBER
XIDSEQ$                           NUMBER
TARGET_COLMAP$                    RAW(128)
DDLOPER$                          NUMBER
DDLDESC$                          CLOB
DDLPDOBJN$                        NUMBER
PROD_D                            NUMBER(6)
CUST_ID                           NUMBER
TIME_ID                           DATE
```

Then, enable capture for the change set:

```
BEGIN
   DBMS_CDC_PUBLISH.ALTER_CHANGE_SET (
      CHANGE_SET_NAME  => 'asynch_set1',
      ENABLE_CAPTURE   => 'Y');
END;
.
PL/SQL procedure successfully completed
```

Finally, issue a DDL statement and see if it is captured:

```
ALTER TABLE cdc_psales DROP PARTITION Dec_06;

SELECT ddloper$, DECODE(ddloper$, NULL, 'NULL',
       DBMS_CDC_PUBLISH.GET_DDLOPER(ddloper$)) 
          AS DDL_OPER
FROM cdc_psales_act
WHERE DDLOPER$ IS NOT NULL
ORDER BY cscn$;

ddloper$            DDL_OPER
---------------------------------
512                 Drop Partition
1 row selected.

SELECT ddldesc$
FROM cdc_psales_act
WHERE ddloper$
IS NOT NULL 
ORDER BY cscn;

DDLDESC$
------------------------
alter table cdc_psales drop partition Dec_06
1 row selected.
```

#### Purging Change Tables of Unneeded Data

This section describes purge operations. For optimum results, purge operations require action from the subscribers. Each subscriber indicates when he or she is done using change data, and then Change Data Capture or the publisher actually removes (purges) data that is no longer being used by any subscriber from the change table, as follows:

- Subscriber
	When finished using change data, a subscriber must call the `DBMS_CDC_SUBSCRIBE.PURGE_WINDOW` procedure. This indicates to Change Data Capture and the publisher that the change data is no longer needed by this subscriber. The `DBMS_CDC_SUBSCRIBE.PURGE_WINDOW` procedure does not physically remove rows from the change tables; however, the data is removed logically from the subscriber view and can no longer be selected.
	In addition, as shown in "Subscribing to Change Data" beginning, the subscriber should call the `DBMS_CDC_SUBSCRIBE.DROP_SUBSCRIPTION` procedure to drop unneeded subscriptions.
	See [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_cdcsub.htm#ARPLS65553) for information about the `DBMS_CDC_SUBSCRIBE.DROP_SUBSCRIPTION` and the `DBMS_CDC_SUBSCRIBE.PURGE_WINDOW` procedures.
- Change Data Capture
	Change Data Capture creates a purge job using the `DBMS_SCHEDULER` package (which runs under the account of the publisher who created the first change table). This purge job calls the `DBMS_CDC_PUBLISH.PURGE` procedure to remove data that subscribers are no longer using from the change tables. This job has the name `cdc$_default_purge_job`. By default, this job runs every 24 hours. You can change the schedule of this job using `DBMS_SCHEDULER.SET_ATTRIBUTE` and set the `repeat_interval` attribute. You can verify or modify any other attributes with the `DBMS_SCHEDULER` package.
	This ensures that the size of the change tables does not grow without limit. The call to the `DBMS_CDC_PUBLISH.PURGE` procedure evaluates all active subscription windows to determine which change data is still needed. It will not purge any data that could be referenced by one or more subscribers with active subscription windows.
	See [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_sched.htm#ARPLS72235) for information about the `DBMS_SCHEDULER` package.
- Publisher
	The publisher can manually execute a purge operation at any time. The publisher has the ability to perform purge operations at a finer granularity than the automatic purge operation performed by Change Data Capture. There are three purge operations available to the publisher:
	- `DBMS_CDC_PUBLISH.PURGE`
		Purges all change tables on the staging database. This is the same `PURGE` operation as is performed automatically by Change Data Capture.
		- `DBMS_CDC_PUBLISH.PURGE_CHANGE_SET`
		Purges all the change tables in a named change set.
		- `DBMS_CDC_PUBLISH.PURGE_CHANGE_TABLE`
		Purges a named changed table.

Thus, calls to the `DBMS_CDC_SUBSCRIBE.PURGE_WINDOW` procedure by subscribers and calls to the `PURGE` procedure by Change Data Capture (or one of the `PURGE` procedures by the publisher) work together: when each subscriber purges a subscription window, it indicates change data that is no longer needed; the `PURGE` procedure evaluates the sum of the input from all the subscribers before actually purging data. You can purge a table by using the `PURGE_CHANGE_TABLE` procedure, and you can purge all the change tables in a change set with the `PURGE_CHANGE_SET` procedure.

If `force` is set to `N`, Oracle Database tries to purge with the most efficient means (using a table lock), but does not guarantee it. Setting `force` to `Y` guarantees this purge.

Note that it is possible that a subscriber could fail to call `PURGE_WINDOW`, with the result being that unneeded rows would not be deleted by the purge job. The publisher can query the `DBA_SUBSCRIPTIONS` view to determine if this is happening, however, the publisher should first consider that subscribers may still be using the change data. In extreme circumstances, a publisher may decide to manually drop an active subscription so that space can be reclaimed. One such circumstance is a subscriber that is an applications program that fails to call the `PURGE_WINDOW` procedure when appropriate. The `DBMS_CDC_PUBLISH.DROP_SUBSCRIPTION` procedure lets the publisher drop active subscriptions if circumstances require it; however, the publisher should first consider that subscribers may still be using the change data.

Before using `DBMS_CDC_PUBLISH.PURGE`, it is important to execute `DBMS_CDC_SUBSCRIBE.EXTEND_WINDOW`, which protects the data and ensures that the publisher is aware of the required data that is needed by the subscriber. Without running the `EXTEND_WINDOW` procedure, the purge job will work as expected and it will purge all the data irrespective of whether data has been consumed or not by the subscriber.

#### Dropping Change Tables

To drop a change table, the publisher must call the `DBMS_CDC_PUBLISH.DROP_CHANGE_TABLE` procedure. This procedure ensures that both the change table itself and the Change Data Capture metadata for the table are dropped. If the publisher tries to use a SQL `DROP` `TABLE` statement on a change table, it will fail with the following error:

```
ORA-31496 must use DBMS_CDC_PUBLISH.DROP_CHANGE_TABLE to drop change tables
```

The `DBMS_CDC_PUBLISH.DROP_CHANGE_TABLE` procedure also safeguards the publisher from inadvertently dropping a change table while there are active subscribers using the change table. If `DBMS_CDC_PUBLISH.DROP_CHANGE_TABLE` is called while subscriptions are active, the procedure will fail with the following error:

```
ORA-31424 change table has active subscriptions
```

If the publisher still wants to drop the change table, in spite of active subscriptions, he or she must call the `DROP_CHANGE_TABLE` procedure using the `force_flag => 'Y'` parameter. This tells Change Data Capture to override its normal safeguards and allow the change table to be dropped despite active subscriptions. The subscriptions will no longer be valid, and subscribers will lose access to the change data.

Note:

The `DROP` `USER` `CASCADE` statement will drop all the publisher's change tables, and if any other users have active subscriptions to the (dropped) change table, these will no longer be valid. In addition to dropping the change tables, the `DROP` `USER` `CASCADE` statement drops any change sources, change sets, and subscriptions that are owned by the user specified in the `DROP` `USER` `CASCADE` statement.

### Exporting and Importing Change Data Capture Objects Using Oracle Data Pump

Oracle Data Pump is the supported export and import utility for Change Data Capture.

The following sections describe restrictions, provide examples, and describe publisher considerations for using Oracle Data Pump with Change Data Capture:

- Restrictions on Using Oracle Data Pump with Change Data Capture
- Examples of Oracle Data Pump Export and Import Commands
- Publisher Considerations for Exporting and Importing Change Tables
- Re-Creating AutoLog Change Data Capture Objects After an Import Operation

#### Restrictions on Using Oracle Data Pump with Change Data Capture

Change Data Capture change sources, change sets, change tables, and subscriptions are exported and imported by the Oracle Data Pump `expdp` and `impdp` commands with the following restrictions.

- Change Data Capture objects are exported and imported only as part of full database export and import operations (those in which the `expdp` and `impdb` commands specify the `FULL=y` parameter). Schema-level import and export operations include some underlying objects (for example, the table underlying a change table), but not the Change Data Capture metadata needed for change data capture to occur.
- A user doing an import of Change Data Capture objects needs the following privileges:
	- either `CREATE` `SEQUENCE` or `CREATE` `ANY` `SEQUENCE`
		If the user doing the import is the original publisher, then `CREATE` `SEQUENCE` will suffice.
		- `ALTER` `DATABASE`
		- either `EXP_FULL_DATABASE` or `IMP_FULL_DATABASE`
		Access to the import package by `PUBLIC` has been removed and access is only to those that have either `EXP_FULL_DATABASE` or `IMP_FULL_DATABASE`.
- AutoLog change sources, change sets, and change tables are not supported. See "Re-Creating AutoLog Change Data Capture Objects After an Import Operation".
- You should export asynchronous change sets and change tables at a time when users are not making DDL and DML changes to the database being exported.
- When importing asynchronous change sets and change tables, you must also import the underlying Oracle Streams configuration; set the Oracle Data Pump import parameter `STREAMS_CONFIGURATION` to `y` explicitly (or implicitly by accepting the default), so that the necessary Streams objects are imported. If you perform an import operation and specify `STREAMS_CONFIGURATION` `=` `n`, then imported asynchronous change sets and change tables will not be able to continue capturing change data.
- Change Data Capture objects never overwrite existing objects when they are imported (similar to the effect of the import command `TABLE_EXISTS_ACTION = skip` parameter for tables). Change Data Capture generates warnings in the import log for these cases.
- Change Data Capture objects are validated at the end of an import operation to determine if all expected underlying objects are present in the correct form. Change Data Capture generates validation warnings in the import log if it detects validation problems. Imported Change Data Capture objects with validation warnings usually cannot continue capturing change data.

#### Examples of Oracle Data Pump Export and Import Commands

The following are examples of Data Pump export and import commands that support Change Data Capture objects:

```
> expdp DIRECTORY=dpump_dir FULL=y
> impdp DIRECTORY=dpump_dir FULL=y STREAMS_CONFIGURATION=y
```

See [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/toc.htm) for information on Oracle Data Pump.

#### Publisher Considerations for Exporting and Importing Change Tables

The following are publisher considerations for exporting and importing change tables:

- When change tables are imported, the job queue is checked for a Change Data Capture purge job. If no purge job is found, then one is submitted automatically (using the `DBMS_CDC_PUBLISH.PURGE` procedure). If a change table is imported, but no subscriptions are taken out before the purge job runs (24 hours later, by default), then all rows in the table will be purged.
	The publisher can use one of the following methods to prevent the purging of data from a change table:
	- Suspend the purge job using the `DBMS_SCHEDULER` package to either disable the job (using the `STOP_JOB` procedure) or execute the job sometime in the future when there are subscriptions (using the `SET_ATTRIBUTE` procedure).
		Note:
		If you disable the purge job, you must remember to reset it once subscriptions have been activated. This prevents the change table from growing indefinitely.
		- Create a temporary subscription to preserve the change table data until real subscriptions appear. Then, drop the temporary subscription.
- When importing data into a source table for which a change table already exists, the imported data is also recorded in any associated change tables.
	Assume that the publisher has a source table `SALES` that has an associated change table `ct_sales.` When the publisher imports data into `SALES`, that data is also recorded in `ct_sales`.
- When importing a change table having the optional control `ROW_ID` column, the `ROW_ID` columns stored in the change table have meaning only if the associated source table has not been imported. If a source table is re-created or imported, each row will have a new `ROW_ID` that is unrelated to the `ROW_ID` that was previously recorded in a change table.

The original level of export and import support available in Oracle9i Database is retained for backward compatibility. Synchronous change tables that reside in the `SYNC_SET` change set can be exported as part of a full database, schema, or individual table export operation and can be imported as needed. The following Change Data Capture objects are not included in the original export and import support: change sources, change sets, change tables that do not reside in the `SYNC_SET` change set, and subscriptions.

#### Re-Creating AutoLog Change Data Capture Objects After an Import Operation

After a Data Pump full database import operation completes for a database containing AutoLog Change Data Capture objects, the following steps must be performed to restore these objects:

1. The publisher must manually drop the database objects underlying AutoLog Change Data Capture objects.
2. The publisher must re-create the AutoLog change sources, change sets, and change tables using the appropriate `DBMS_CDC_PUBLISH` procedures.
3. Subscribers must re-create their subscriptions to the AutoLog change sets.

Change data may be lost in the interval between a Data Pump full database export operation involving AutoLog Change Data Capture objects and their re-creation after a Data Pump full database import operation in the preceding step. This can be minimized by preventing changes to the source tables during this interval, if possible.

Before re-creating an AutoLog Change Data Capture configuration after a Data Pump import operation, you must first drop the underlying objects: the table underlying a change table, subscriber views, a sequence used by the change set, and a Streams apply process, queue and queue table. Table 17-12 presents each underlying object and the method you use to drop it up after a Data Pump import operation.

Table 17-12 Methods to Drop Objects After a Data Pump Import Operation

| Object | SQL Statement or PL/SQL Package to Drop Object |
| --- | --- |
| Table | SQL `DROP TABLE` statement |
| Subscriber View | SQL `DROP VIEW` statement |
| Sequence Used by Change Set | SQL `DROP SEQUENCE` statement |
| Streams Apply Process | PL/SQL `DBMS_APPLY_ADM.DROP_APPLY()` package |
| Streams Queue | PL/SQL `DBMS_AQADM.DROP_QUEUE()` package |
| Streams Queue Table | PL/SQL `DBMS_AQADM.DROP_QUEUE_TABLE()` package |

You can obtain the name of the sequence used by a change set by querying the `ALL_SEQUENCES` view for a sequence name that begins with `CDC$` and contains at least the initial characters of the change set name.

You can obtain the names of the Streams objects by querying the `DBA_APPLY`, `DBA_QUEUES`, and `DBA_QUEUE_TABLES` views for names that begin with `CDC$` and contain at least the initial characters of the change set name.

### Impact on Subscriptions When the Publisher Makes Changes

The Change Data Capture environment is dynamic. The publisher can add and drop change tables at any time. The publisher can also add columns to and drop columns from existing change tables at any time. The following list describes how changes to the Change Data Capture environment affect subscriptions:

- Subscribers do not get explicit notification if the publisher adds a new change table or adds columns to an existing change table. A subscriber can check the `ALL_PUBLISHED_COLUMNS` view to see if new columns have been added, and whether or not the subscriber has access to them.
- Table 17-13 describes what happens when the publisher adds a column to a change table.

Table 17-13 Effects of Publisher Adding a Column to a Change Table

| If the publisher adds | And... | Then... |
| --- | --- | --- |
| A user column | A new subscription includes this column | The subscription window for this subscription starts at the point the column was added. |
| A user column | A new subscription does not include this newly added column | The subscription window for this subscription starts at the earliest available change data. The new column will not be seen. |
| A user column | A subscription exists | The subscription window for this subscription remains unchanged. |
| A control column | A new subscription is created | The subscription window for this subscription starts at the earliest available change data. The subscription can see the control column immediately. All change table rows that existed prior to adding the control column will have the null value for the newly added control column. |
| A control column | A subscription exists | This subscription can see the new control columns after the subscription window is purged (`DBMS_CDC_PUBLISH.PURGE_WINDOW` procedure) such that the low boundary for the window crosses over the point when the control column was added. |

## Considerations for Synchronous Change Data Capture

The following sections provide information that the publisher should be aware of when using the synchronous mode of Change Data Capture:

- Restriction on Direct-Path INSERT
- Datatypes and Table Structures Supported for Synchronous Change Data Capture
- Limitation on Restoring Source Tables from the Recycle Bin

### Restriction on Direct-Path INSERT

Synchronous Change Data Capture does not support the direct-path `INSERT` statement (and, by association, the `MERGE` statement and the `multi_table_insert` clause of the `INSERT` statement).

When the publisher creates a change table in synchronous mode, Change Data Capture creates triggers on the source table. Because a direct-path `INSERT` statement disables all database triggers, any rows inserted into the source table using the SQL statement for direct-path `INSERT` in parallel DML mode will not be captured in the change table.

Similarly, Change Data Capture cannot capture the inserted rows from multitable insert and merge operations because these statements use a direct-path `INSERT` statement. The direct-path `INSERT` statement does not return an error message to indicate that the triggers used by Change Data Capture did not fire.

See [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for more information regarding the direct-path `INSERT` statement and triggers.

### Datatypes and Table Structures Supported for Synchronous Change Data Capture

Synchronous Change Data Capture supports columns of all built-in Oracle datatypes except the following:

- `BFILE`
- `BLOB`
- `CLOB`
- `LONG`
- `NCLOB`
- `ROWID`
- `UROWID`
- object types (for example, XMLType)

In addition, virtual columns are not supported. Furthermore, Change Data Capture does not support the usage of quoted identifiers; as a consequence, the usage of reserved keywords with Change Data Capture is not supported. See Oracle Database SQL Language Reference for a list of reserved keywords.

Synchronous Change Data Capture does not support the following table structures:

- Source tables that are temporary tables
- Source tables that are object tables
- Index-organized tables with columns of unsupported datatypes (including `LOB` columns) or with overflow segments

### Limitation on Restoring Source Tables from the Recycle Bin

If the source table for a synchronous change table is dropped and then restored from the recycle bin, changes are no longer captured in that change table. The publisher must create a new synchronous change table to capture future changes to the restored source table.

## Considerations for Asynchronous Change Data Capture

The following sections provide information that the publisher and the source and staging database DBAs should be aware of when using the asynchronous mode of Change Data Capture:

- Asynchronous Change Data Capture and Redo Log Files
- Asynchronous Change Data Capture and Supplemental Logging
- Asynchronous Change Data Capture and Oracle Streams Components
- Datatypes and Table Structures Supported for Asynchronous Change Data Capture
- Restrictions for NOLOGGING and UNRECOVERABLE Operations

### Asynchronous Change Data Capture and Redo Log Files

The asynchronous mode of Change Data Capture uses redo log files, as follows:

- HotLog
	Asynchronous HotLog and Distributed HotLog read the source database online redo log files whenever possible and the archived redo log files otherwise.
- AutoLog
	Asynchronous AutoLog Change Data Capture reads redo log files that have been copied from the source database to the staging database by redo transport services.
	When using the AutoLog online option, the destination attribute must be `LGWR` `ASYNC`. Redo transport services copies redo data from the online redo log at the source database to the standby redo log at the staging database. Change Data Capture obtains the change data after the source database transaction commits.
	When using the AutoLog archive option, the destination attribute can be `ARCH` or `LGWR` `ASYNC`. In `ARCH` mode, redo transport services copies archived redo log files to the staging database after a log switch occurs on the source database. In `LGWR` mode, redo transport services copies redo data to the staging database while it is being written to the online redo log file on the source database.

For log files to be archived, the source databases for asynchronous Change Data Capture must run in `ARCHIVELOG` mode, as specified with the following SQL statement:

```
ALTER DATABASE ARCHIVELOG;
```

See [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/archredo.htm#ADMIN11332) for information about running a database in `ARCHIVELOG` mode.

A redo log file used by Change Data Capture must remain available on the staging database until Change Data Capture has captured it. However, it is not necessary that the redo log file remain available until the Change Data Capture subscriber is done with the change data.

To determine which redo log files are no longer needed by Change Data Capture for a given change set, the publisher alters the change set's Streams capture process, which causes Streams to perform some internal cleanup and populates the `DBA_LOGMNR_PURGED_LOG` view. The publisher follows these steps:

1. Uses the following query on the staging database to get the three SCN values needed to determine an appropriate new `first_scn` value for the change set, `CHICAGO_DAILY:`
	```
	SELECT cap.CAPTURE_NAME, cap.FIRST_SCN, cap.APPLIED_SCN, 
	        cap.REQUIRED_CHECKPOINT_SCN
	FROM DBA_CAPTURE cap, ALL_CHANGE_SETS cset
	WHERE cset.SET_NAME = 'CHICAGO_DAILY' AND
	      cap.CAPTURE_NAME = cset.CAPTURE_NAME;
	CAPTURE_NAME                    FIRST_SCN APPLIED_SCN REQUIRED_CHECKPOINT_SCN
	------------------------------ ---------- ----------- -----------------------
	CDC$C_CHICAGO_DAILY                778059      778293                  778293
	```
2. Determines a new `first_scn` value that is greater than or equal to the original `first_scn` value and less than or equal to the `applied_scn` and `required_checkpoint_scn` values returned by the query in step 1. In this example, this value is 778293, and the capture process name is `CDC$C_CHICAGO_DAILY`, therefore the publisher can alter the `first_scn` value for the capture process as follows:
	```
	BEGIN
	DBMS_CAPTURE_ADM.ALTER_CAPTURE(
	  capture_name => 'CDC$C_CHICAGO_DAILY',
	  first_scn    => 778293);
	END;
	/
	```
	If there is not an SCN value that meets these criteria, then the change set needs all of its redo log files.
3. Queries the `DBA_LOGMNR_PURGED_LOG` view to see any log files that are no longer needed by Change Data Capture:
	```
	SELECT FILE_NAME
	FROM DBA_LOGMNR_PURGED_LOG;
	```
	Note:
	Redo log files may be required on the staging database for purposes other than Change Data Capture. Before deleting a redo log file, the publisher should be sure that no other users need it.

See the information on setting the first SCN for an existing capture process and on capture process checkpoints in [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/toc.htm) for more information.

The `first_scn` value can be updated for all change sets in an AutoLog change source by using the `DBMS_CDC_PUBLISH.ALTER_AUTOLOG_CHANGE_SOURCE` `first_scn` parameter. Note that the new `first_scn` value must meet the criteria stated in Step 2 of the preceding list for all change sets in the AutoLog change source.

Both the size of the redo log files and the frequency with which a log switch occurs can affect the generation of the archived log files at the source database. For Change Data Capture, the most important factor in deciding what size to make a redo log file is the tolerance for latency between when a change is made and when that change data is available to subscribers. However, because the Oracle Database software attempts a check point at each log switch, if the redo log file is too small, frequent log switches will lead to frequent checkpointing and negatively impact the performance of the source database.

See [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/toc.htm) for step-by-step instructions on monitoring log file archival information. Substitute the terms source and staging database for the Oracle Data Guard terms primary database and archiving destinations, respectively.

When using redo transport services to supply redo log files to an AutoLog change source, gaps in the sequence of redo log files are automatically detected and resolved. If a situation arises where it is necessary to manually add a log file to an AutoLog change set, the publisher can use instructions on explicitly assigning log files to a downstream capture process described in [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/toc.htm). These instructions require the name of the capture process for the AutoLog change set. The publisher can obtain the name of the capture process for an AutoLog change set from the `ALL_CHANGE_SETS` data dictionary view.

### Asynchronous Change Data Capture and Supplemental Logging

The asynchronous modes of Change Data Capture work best with appropriate supplemental logging on the source database. (Supplemental logging is not used by synchronous Change Data Capture.)

The source database DBA must enable some form of database-level supplemental logging. The following example enables minimal database-level supplemental logging:

```
ALTER DATABASE ADD SUPPLEMENTAL LOG DATA;
```

In addition, Oracle recommends that the source database DBA:

- Supplementally log all source table columns that are part of a primary key or function to uniquely identify a row. This can be done using database-level or table-level identification key logging, or through a table-level unconditional log group.
- Create an unconditional log group for all source table columns that are captured by any asynchronous change table. This should be done before any change tables are created on a source table.
	```
	ALTER TABLE sh.promotions
	ADD SUPPLEMENTAL LOG GROUP log_group_cust
	(PROMO_NAME, PROMO_SUBCATEGORY, PROMO_CATEGORY) ALWAYS;
	```
	If an unconditional log group is not created for all source table columns to be captured, then when an update DML operation occurs, some unchanged user column values in change tables will be null instead of reflecting the actual source table value.
	For example, suppose a source table contains two columns, `X` and `Y`, and that the source database DBA has defined an unconditional log group for that table that includes only column `Y`. Furthermore, assume that a user updates only column `Y` in that table row. When the subscriber views the change data for that row, the value of the unchanged column `X` will be null. However, because the actual column value for `X` is excluded from the redo log file and therefore cannot be included in the change table, the subscriber cannot assume that the actual source table value for column `X` is null. The subscriber must rely on the contents of the `TARGET_COLMAP$` control column to determine whether the actual source table value for column `X` is null or it is unchanged.

See [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/toc.htm) for more information on the various types of supplemental logging.

### Asynchronous Change Data Capture and Oracle Streams Components

Asynchronous Change Data Capture generates components of Oracle Streams to capture change data and to populate change sets. These components must not be reused or shared for any other purposes. For example, the capture queue that Change Data Capture generates for a Distributed HotLog change source should not be used as the source queue for new user-created Streams propagations.

For HotLog and AutoLog modes, each change set contains a Streams capture process, queue, queue table and apply process. The staging database publisher owns all of these objects.For Distributed HotLog mode, each change source resides on the source database and contains a Streams capture process, queue and queue table. Each change set resides on the staging database and contains a Streams apply process. When the first change set in a change source is created, Change Data Capture generates a queue and queue table on the staging database to be shared among all change sets in the change source. Change Data Capture also generates a Streams Propagation on the source database from the change source queue to the change set queue on the staging database. The source database publisher owns the source database objects and the staging database publisher owns the staging database objects.

Figure 17-8 illustrates an example of how Streams components are used in an asynchronous Distributed HotLog Change Data Capture environment. In this example, there is a Distributed HotLog change source `disthot_change_src` on the source database and two change sets, `Change_Set_1` and `Change_Set_2`, on the staging database.

Figure 17-8 Streams Components in an Asynchronous Distributed HotLog Change Data Capture System

![Description of Figure 17-8 follows](https://docs.oracle.com/cd/E11882_01/server.112/e25554/dwhsg129.gif)  
[Description of "Figure 17-8 Streams Components in an Asynchronous Distributed HotLog Change Data Capture System"](https://docs.oracle.com/cd/E11882_01/server.112/e25554/img_text/dwhsg129.htm)  

### Datatypes and Table Structures Supported for Asynchronous Change Data Capture

Asynchronous Change Data Capture supports columns of all built-in Oracle datatypes except the following:

- `BFILE`
- `LONG`
- `ROWID`
- `UROWID`
- object types (for example, XMLType)

In addition, virtual columns are not supported. Furthermore, Change Data Capture does not support the usage of quoted identifiers; as a consequence, the usage of reserved keywords with Change Data Capture is not supported. See Oracle Database SQL Language Reference for a list of reserved keywords.

Asynchronous Change Data Capture does not support the following table structures:

- Source tables that are temporary tables
- Source tables that are object tables
- Index-organized tables with columns of unsupported datatypes (including `LOB` columns) or with overflow segments

### Restrictions for NOLOGGING and UNRECOVERABLE Operations

If you use the `NOLOGGING` or `UNRECOVERABLE` keyword for a SQL operation, asynchronous Change Data Capture cannot capture the changes from that operation. Similarly, if you use the `UNRECOVERABLE` clause in the control file for a SQL\*Loader direct path load, then the changes from that direct load cannot be captured by asynchronous Change Data Capture.

See [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for information about the `NOLOGGING` and `UNRECOVERABLE` keywords and [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/toc.htm) for information about direct path loads and SQL\*Loader.

## Implementation and System Configuration

Change Data Capture comes packaged with the appropriate Oracle drivers already installed with which you can implement either asynchronous or synchronous data capture. The synchronous mode of Change Data Capture is included with the Standard Edition, but the asynchronous mode requires you have the Enterprise Edition.

In addition, note that Change Data Capture uses Java. Therefore, when you install Oracle Database, ensure that Java is enabled.

Change Data Capture places system triggers on the SQL `CREATE` `TABLE`, `ALTER` `TABLE`, and `DROP` `TABLE` statements. If system triggers are disabled on the source database, Change Data Capture will not function correctly. Therefore, you should never disable system triggers.

To remove Change Data Capture from the database, the SQL script `rmcdc.sql` is provided in the `admin` directory. This will remove the system triggers that Change Data Capture places on the SQL `CREATE` `TABLE`, `ALTER` `TABLE`, and `DROP` `TABLE` statements. In addition, `rmcdc.sql` removes all Java classes used by Change Data Capture. Note that after `rmcdc.sql` is called, Change Data Capture will no longer operate on the system. If the system administrator decides to remove the Java Virtual Machine from a database, `rmcdc.sql` must be called before `rmjvm` is called.

To reinstall Change Data Capture, the SQL script `initcdc.sql` is provided in the `admin` directory. It creates the Change Data Capture system triggers and Java classes that are required by Change Data Capture. Note that the Java Virtual Machine must be available to reinstall Change Data Capture.

### Database Configuration Assistant Considerations

All of the predefined templates provided with the Database Configuration Assistant support the Oracle Change Data Capture feature. The predefined templates are:

- General Purpose
- Data Warehouse
- Transaction Processing
- New Database

If you choose the New Database option to build a custom database, note that Oracle JVM is selected by default in the Additional database configurations dialog box. Do not change this setting; Oracle Change Data Capture requires the Oracle JVM feature.

### Summary of Supported Distributed HotLog Configurations and Restrictions

The following sections describe the supported configurations for the Distributed HotLog mode of Change Data Capture as well as the restrictions.

#### Oracle Database Releases for Source and Staging Databases

The Distributed HotLog mode of Change Data Capture allows the following combinations of Oracle Database releases for the source and staging databases:

- The source database can be Oracle Database release 9.2 (9.2.0.6 or higher patch set), 10.1, 10.2, 11.1, or 11.2.
- The staging database can be Oracle Database release 11.1 or 11.2.

Note:

When a release 9.2 or 10.1 Oracle Database serves as the source database for the Distributed HotLog mode of Change Data Capture, metadata for the source database is stored on the staging database, whereas metadata for an Oracle Database release 11.1 or 11.2 source database is stored on the source database. Therefore, to view the metadata for an Oracle Database release 9.2 or 10.1 source database, the publisher must query the `CHANGE_SOURCES` data dictionary view on the staging database, and to view the metadata for an Oracle Database release 11.1 or 11.2 source database, the publisher must query the `CHANGE_SOURCES` data dictionary view on the source database.

#### Upgrading a Distributed HotLog Change Source to Oracle Release 11 (11.1 or 11.2)

As mentioned in the previous topic, the metadata for an Oracle Database release 11 Distributed HotLog change source is stored on the source database, but the metadata for a release 9.2 or 10.1 change source is stored on the staging database.

When you upgrade a release 10.2 Oracle Database to release 11, then there is additional metadata movement required.

When you upgrade a release 9.2 or 10.1 Oracle Database to release 11, Change Data Capture does not move the source database metadata from the staging database to the source database as part of the upgrade operation. However, the first time the change source is enabled after the upgrade (using the `DBMS_CDC_PUBLISH.ALTER_HOTLOG_CHANGE_SOURCE` procedure), Change Data Capture detects that the metadata needs to be upgraded and moved to the source database and does so automatically.

If the publisher prefers to not alter the change source immediately after an upgrade, the change source metadata can remain on the staging database until a more appropriate time. Oracle recommends that the source database metadata not be left on the staging database indefinitely after an upgrade to Oracle Database release 11 so that information about the Distributed HotLog change source becomes available in the data dictionary views on the source database.

#### Hardware Platforms and Operating Systems

The Distributed HotLog mode of Change Data Capture supports the use of different hardware platforms or operating systems (or both) for the source and staging databases.

#### Requirements for Multiple Publishers on the Staging Database

If there are multiple publishers on the staging database for the Distributed HotLog mode of Change Data capture, and one publisher defines a change table in another publisher's Distributed HotLog change set, then Change Data Capture uses the database link established by publisher who created the change set to access the source database. Therefore, the database link to the source database established by the publisher who created the change set must be intact for the change table to be successfully created. If the change set publisher's database link is not present when creating a change table, an error is returned indicating that the connection description for the remote database was not found.

#### Requirements for Database Links

The database link from the source database to the staging database must exist for the life of a Distributed HotLog change source.

The database link from the staging database to the source database must exist when creating, altering or dropping Distributed HotLog change sources, change sets and change tables. However, this database link is not required for change capture to occur. Once the required Distributed HotLog change sources, change sets and change tables are in place and enabled, this database link can be dropped without interrupting change capture. This database link would need to be re-created to create, alter or drop Distributed HotLog change sources, change sets and change tables.