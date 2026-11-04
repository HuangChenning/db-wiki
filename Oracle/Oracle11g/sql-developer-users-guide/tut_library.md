---
title: "Tutorial: Creating Objects for a Small Database"
book: "SQL Developer User's Guide"
doc_id: E12152-08
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/doc.112/e12152/tut_library.htm
tags:
  - oracle
  - 11g
  - sql-developer-users-guide
---

## 3 Tutorial: Creating Objects for a Small Database

In this tutorial, you will use SQL Developer to create objects for a simplified library database, which will include tables for books, patrons (people who have library cards), and transactions (checking a book out, returning a book, and so on).

The tables are deliberately oversimplified for this tutorial. They would not be adequate for any actual public or organizational library. For example, this library contains only books (not magazines, journals, or other document formats), and it can contain no more than one copy of any book.

You will perform the following major steps:

Note:

To delete the objects that you create for this tutorial, you can use the DROP statements at the beginning of the script in Script for Creating and Using the Library Tutorial Objects.

Related Topics

Script for Creating and Using the Library Tutorial Objects

[Chapter 1, "SQL Developer Concepts and Usage"](intro.md)

[SQL Developer User Interface](intro.md)

[Database Objects](intro.md)

## Create a Table (BOOKS)

The BOOKS table contains a row for each book in the library. It includes columns of character and number types, a primary key, a unique constraint, and a check constraint. You will use the Create Table dialog box to create the table declaratively; the table that you create will be essentially the same as if you had entered the following statement using the SQL Worksheet:

```
CREATE TABLE books (
   book_id VARCHAR2(20),
   title VARCHAR2(50)
      CONSTRAINT title_not_null NOT NULL,
   author_last_name VARCHAR2(30)
      CONSTRAINT last_name_not_null NOT NULL,
   author_first_name VARCHAR2(30),
   rating NUMBER,
   CONSTRAINT books_pk PRIMARY KEY (book_id),
   CONSTRAINT rating_1_to_10 CHECK (rating IS NULL OR
      (rating >= 1 and rating <= 10)),
   CONSTRAINT author_title_unique UNIQUE (author_last_name, title));
```

To create the BOOKS table, connect to the database as the user in the schema you want to use for this tutorial. Right-click the Tables node in the schema hierarchy on the left side, select New Table, and enter the following information. (If a tab or field is not mentioned, do not enter anything for it. Be sure that the Advanced box is not checked when you start creating the table.)

For detailed information about the table dialog box and its tabs, see [Create Table (quick creation)](dialogs.md) and [Create/Edit Table (with advanced options)](dialogs.md).

Schema: Specify your current schema as the schema in which to create the table.

Name: BOOKS

Create the table columns using the following information. After creating each column except the last one (rating), click Add Column to add the next column. (If you accidentally click OK instead of Add Column, right-click the BOOKS table in the Connections navigator display, select Edit, and continue to add columns.)

| Column Name | Type | Size | Other Information and Notes |
| --- | --- | --- | --- |
| book\_id | VARCHAR2 | 20 | Primary Key (Automatically checks Not Null; an index is also created on the primary key column. This is the Dewey code or other book identifier.) |
| title | VARCHAR2 | 50 | Not Null |
| author\_last\_name | VARCHAR2 | 30 | Not Null |
| author\_first\_name | VARCHAR2 | 30 |  |
| rating | NUMBER |  | (Librarian's personal rating of the book, from 1 (poor) to 10 (great)) |

After you have entered the last column (rating), check Advanced (next to Schema). This displays a pane for more table options. For this table, you will use the Unique Constraints and Check Constraints panes.

Unique Constraints pane

Click Add to add a unique constraint for the table, namely, that the combination of author\_last\_name and title must be unique within the table. (This is deliberately oversimplified, since most major libraries will have allow more than one copy of a book in their holdings. Also, the combination of last name and title is not always a "foolproof" check for uniqueness, but it is sufficient for this simple scenario.)

Name: author\_title\_unique

In Available Columns, double-click TITLE and then AUTHOR\_LAST\_NAME to move them to Selected Columns.

Check Constraints pane

Click Add to add a check constraint for the table, namely, that the rating column value is optional (it can be null), but if a value is specified, it must be a number from 1 through 10. You must enter the condition using SQL syntax that is valid in a CHECK clause (but do not include the CHECK keyword or enclosing parentheses for the entire CHECK clause text).

Name: rating\_1\_to\_10

Condition: rating is null or (rating >= 1 and rating <= 10)

Click OK to finish creating the table.

Go to Create a Table (PATRONS) to create the next table.

## Create a Table (PATRONS)

The PATRONS table contains a row for each patron who can check books out of the library (that is, each person who has a library card). It includes an object type (MDSYS.SDO\_GEOMETRY) column. You will use the Create Table dialog box to create the table declaratively; the table that you create will be essentially the same as if you had entered the following statement using the SQL Worksheet:

```
CREATE TABLE patrons (
   patron_id NUMBER,
   last_name VARCHAR2(30)
      CONSTRAINT patron_last_not_null NOT NULL,
   first_name VARCHAR2(30),
   street_address VARCHAR2(50),
   city_state_zip VARCHAR2(50),
   location MDSYS.SDO_GEOMETRY,
   CONSTRAINT patrons_pk PRIMARY KEY (patron_id));
```

The use of single city\_state\_zip column for all that information is not good database design; it is done here merely to simplify your work in the tutorial.

The location column (Oracle Spatial geometry representing the patron's geocoded address) is merely to show the use of a complex (object) type.

To create the PATRONS table, if you are not already connected, connect to the database as the user for the schema you are using for this tutorial. Right-click the Tables node in the schema hierarchy on the left side, select New Table, and enter the following information. (If a tab or field is not mentioned, do not enter anything for it. Be sure that the Advanced box is not checked when you start creating the table.)

Schema: Specify your current schema as the schema in which to create the table.

Name: PATRONS

Create most of the table columns using the following information. After creating each column except the city\_state\_zip column, click Add Column to add the next column. (If you accidentally click OK instead of Add Column, right-click the PATRONS table in the Connections navigator display, select Edit, and continue to add columns.)

| Column Name | Type | Size | Other Information and Notes |
| --- | --- | --- | --- |
| patron\_id | NUMBER |  | Primary Key. (Unique patron ID number, with values to be created using a sequence that you will create) |
| last\_name | VARCHAR2 | 30 | Not Null |
| first\_name | VARCHAR2 | 30 |  |
| street\_address | VARCHAR2 | 30 |  |
| city\_state\_zip | VARCHAR2 | 30 |  |

The last column in the table (location) requires a complex data type, for which you must use the Columns tab with advanced options. Check Advanced (next to Schema). This displays a pane for selecting more table options.

In the Columns pane, click the city\_state\_zip column name, and click the Add Column (+) icon to add the following as the last column in the table.

| Column Name | Type | Other Information and Notes |
| --- | --- | --- |
| location | Complex type  Schema: MDSYS  Type: SDO\_GEOMETRY | (Oracle Spatial geometry object representing the patron's geocoded address) |

After you have entered the last column (location), click OK to finish creating the table.

Go to Create a Table (TRANSACTIONS) to create the next table.

## Create a Table (TRANSACTIONS)

The TRANSACTIONS table contains a row for each transaction involving a patron and a book (for example, someone checking a book out or returning a book). It includes two foreign key columns. You will use the Create Table dialog box to create the table declaratively; the table that you create will be essentially the same as if you had entered the following statement using the SQL Worksheet:

```
CREATE TABLE transactions (
   transaction_id NUMBER,
   patron_id CONSTRAINT for_key_patron_id
      REFERENCES patrons(patron_id),
   book_id CONSTRAINT for_key_book_id
      REFERENCES books(book_id),
   transaction_date DATE
      CONSTRAINT tran_date_not_null NOT NULL,
   transaction_type NUMBER
      CONSTRAINT tran_type_not_null NOT NULL,
   CONSTRAINT transactions_pk PRIMARY KEY (transaction_id));
```

To create the TRANSACTIONS table, if you are not already connected, connect to the database as the user for the schema you are using for this tutorial. Right-click the Tables node in the schema hierarchy on the left side, select New Table, and enter the following information. (If a tab or field is not mentioned, do not enter anything for it. Be sure that the Advanced box is not checked when you start creating the table.)

Schema: Specify your current schema as the schema in which to create the table.

Name: TRANSACTIONS

Create the table columns using the following information. After creating each column except the last one (transaction\_type), click Add Column to add the next column. (If you accidentally click OK instead of Add Column, right-click the TRANSACTIONS table in the Connections navigator display, select Edit, and continue to add columns.)

| Column Name | Type | Size | Other Information and Notes |
| --- | --- | --- | --- |
| transaction\_id | NUMBER |  | Primary Key. (Unique transaction ID number, with values to be created using a trigger and sequence that will be created automatically) |
| patron\_id | NUMBER |  | (Foreign key; must match a patron\_id value in the PATRONS table) |
| book\_id | VARCHAR2 | 20 | (Foreign key; must match a book\_id value in the BOOKS table) |
| transaction\_date | DATE |  | (Date and time of the transaction) |
| transaction\_type | NUMBER |  | (Numeric code indicating the type of transaction, such as 1 for checking out a book) |

After you have entered the last column (transaction\_type), check Advanced (next to Schema). This displays a pane for selecting more table options. For this table, you will use the Column Sequences and Foreign Keys panes.

Column Sequences pane

You have already specified TRANSACTION\_ID as the primary key, and you will use this pane only to specify that the primary key column values are to be populated automatically. This convenient approach uses a trigger and a sequence (both created automatically by SQL Developer), and ensures that each transaction ID value is unique.

Column: TRANSACTION\_ID

Sequence: New Sequence

Trigger: TRANSACTIONS\_TRG (The default; a before-insert trigger with this name will be created automatically.)

Foreign Keys tab

1\. Click Add to create the first of the two foreign keys for the TRANSACTIONS table.

Name: for\_key\_patron\_id

Referenced Schema: Name of the schema containing the table with the primary key or unique constraint to which this foreign key refers. Use the schema you have been using for this tutorial.

Referenced Table: PATRONS

Referenced Constraint: PATRONS\_PK (The name of the primary key constraint for the PATRONS table. Be sure that the Referenced Column on PATRONS displayed value is PATRON\_ID.)

Associations: Local Column: PATRON\_ID

Associations: Referenced Column on PATRONS: PATRON\_ID

2\. Click Add to create the second of the two foreign keys for the TRANSACTIONS table.

Name: for\_key\_book\_id

Referenced Schema: Name of the schema containing the table with the primary key or unique constraint to which this foreign key refers. Use the schema you have been using for this tutorial.

Referenced Table: BOOKS

Referenced Constraint: BOOKS\_PK (The name of the primary key constraint for the BOOKS table. Be sure that the Referenced Column on BOOKS displayed value is BOOK\_ID.

Associations: Local Column: BOOK\_ID

Associations: Referenced Column on BOOKS: BOOK\_ID

3\. Click OK to finish creating the table.

You have finished creating all the tables. To create a sequence for use in generating unique primary key values for the PATRONS table, go to Create a Sequence.

## Create a Sequence

Create one sequence object, which will be used in INSERT statements to generate unique primary key values in the PATRONS table. (You do not need to create a sequence for the primary key in the TRANSACTIONS table, because you used the SQL Developer feature that enables automatic population of primary key values for that table.) You will use the Create Sequence dialog box to create the sequence declaratively; the sequence that you create will be essentially the same as if you had entered the following statements using the SQL Worksheet:

```
CREATE SEQUENCE patron_id_seq 
   START WITH 100
   INCREMENT BY 1;
```

After creating the sequence, you can use it in INSERT statements to generate unique numeric values. The following example uses the patron\_id\_seq sequence in creating a row for a new patron (library user), assigning her a patron ID that is the next available value of the patron\_id\_seq sequence:

```
INSERT INTO patrons VALUES  (patron_id_seq.nextval, 
   'Smith', 'Jane', '123 Main Street', 'Mytown, MA 01234', null);
```

To create the sequence, if you are not already connected, connect to the database as the user for the schema you are using for this tutorial. Right-click the Sequences node in the schema hierarchy on the left side, select New Sequence, and enter information using the Create Sequence dialog box.

Schema: Specify your current schema as the schema in which to create the sequence.

Name: patron\_id\_seq

Increment: 1

Start with: 100

Min value: 100

Click OK to finish creating the sequence.

To insert sample data into the tables, go to Insert Data into the Tables.

## Insert Data into the Tables

For your convenience in using the view and the PL/SQL procedure that you will create, add some sample data to the BOOKS, PATRONS, and TRANSACTIONS tables. (If you do not add sample data, you can still create the remaining objects in this tutorial, but the view and the procedure will not return any results.)

Go to the SQL Worksheet window associated with the database connection you have been using. (For information about using the SQL Worksheet, see [Using the SQL Worksheet](intro.md).) Copy and paste the following INSERT statements into the Enter SQL Statement box:

```
INSERT INTO books VALUES ('A1111', 'Moby Dick', 'Melville', 'Herman', 10);
INSERT INTO books VALUES ('A2222', 'Get Rich Really Fast', 'Scammer', 'Ima', 1);
INSERT INTO books VALUES ('A3333', 'Finding Inner Peace', 'Blissford', 'Serenity', null);
INSERT INTO books VALUES ('A4444', 'Great Mystery Stories', 'Whodunit', 'Rodney', 5);
INSERT INTO books VALUES ('A5555', 'Software Wizardry', 'Abugov', 'D.', 10);
 
INSERT INTO patrons VALUES  (patron_id_seq.nextval, 
   'Smith', 'Jane', '123 Main Street', 'Mytown, MA 01234', null);
INSERT INTO patrons VALUES  (patron_id_seq.nextval, 
   'Chen', 'William', '16 S. Maple Road', 'Mytown, MA 01234', null);
INSERT INTO patrons VALUES  (patron_id_seq.nextval, 
   'Fernandez', 'Maria', '502 Harrison Blvd.', 'Sometown, NH 03078', null);
INSERT INTO patrons VALUES  (patron_id_seq.nextval, 
   'Murphy', 'Sam', '57 Main Street', 'Mytown, MA 01234', null);
 
INSERT INTO transactions (patron_id, book_id, 
  transaction_date, transaction_type) 
  VALUES (100, 'A1111', SYSDATE, 1);
INSERT INTO transactions (patron_id, book_id, 
  transaction_date, transaction_type) 
  VALUES (100, 'A2222', SYSDATE, 2);
INSERT INTO transactions (patron_id, book_id, 
  transaction_date, transaction_type) 
  VALUES (101, 'A3333', SYSDATE, 3);
INSERT INTO transactions (patron_id, book_id, 
  transaction_date, transaction_type) 
  VALUES (101, 'A2222', SYSDATE, 1);
INSERT INTO transactions (patron_id, book_id, 
  transaction_date, transaction_type) 
  VALUES (102, 'A3333', SYSDATE, 1);
INSERT INTO transactions (patron_id, book_id, 
  transaction_date, transaction_type) 
  VALUES (103, 'A4444', SYSDATE, 2);
INSERT INTO transactions (patron_id, book_id, 
  transaction_date, transaction_type) 
  VALUES (100, 'A4444', SYSDATE, 1);
INSERT INTO transactions (patron_id, book_id, 
  transaction_date, transaction_type) 
  VALUES (102, 'A2222', SYSDATE, 2);
INSERT INTO transactions (patron_id, book_id, 
  transaction_date, transaction_type) 
  VALUES (102, 'A5555', SYSDATE, 1);
INSERT INTO transactions (patron_id, book_id, 
  transaction_date, transaction_type) 
  VALUES (101, 'A2222', SYSDATE, 1);
```

Click the Run Script icon, or press the F5 key.

To create a view, go to Create a View.

## Create a View

Create a view that returns information about patrons and their transactions. This view queries the PATRONS and TRANSACTIONS tables, and returns rows that contain a patron's ID, last name, and first name, along with a transaction and the transaction type. The rows are ordered by patron ID, and by transaction type within patron IDs.

To create the patrons\_trans\_view view, if you are not already connected, connect to the database as the user for the schema you are using for this tutorial. Right-click the Views node in the schema hierarchy on the left side, select New View, and enter the following information. (If a tab or field is not mentioned, do not enter anything for it.)

Schema: Specify your current schema as the schema in which to create the view.

Name: patrons\_trans\_view

SQL Query tab

In the SQL Query box, enter (or copy and paste) the following statement:

```
SELECT p.patron_id,
       p.last_name,
       p.first_name,
       t.transaction_type,
       t.transaction_date
  FROM patrons p, transactions t
 WHERE p.patron_id = t.patron_id
 ORDER BY p.patron_id, t.transaction_type
```

Then click Test Syntax, and ensure that you have not made any syntax errors. If you made any errors, correct then and click Test Syntax again.

DDL

Review the SQL statement that SQL Developer will use to create the view. If you want to make any changes, go back to the SQL Query tab and make the changes there.

If you want to save the CREATE VIEW statement to a SQL script file, click Save and specify the location and file name.

When you are finished, click OK.

You have finished creating the view. If you inserted data to the underlying tables, as described in Insert Data into the Tables, you can see the data returned by this view as follows: in the Connections navigator, expand Views, and select PATRONS\_TRANS\_VIEW, then click the Data tab.

To create a procedure that lists all books with a specified rating, go to Create a PL/SQL Procedure.

## Create a PL/SQL Procedure

Create a procedure that lists all books with a specified rating. You can then call this procedure with an input parameter (a number from 1 to 10), and the output will be all the titles of all books with that rating.

To create the procedure, if you are not already connected, connect to the database as the user for the schema you are using for this tutorial. Right-click the Procedures node in the schema hierarchy on the left side, select New Procedure, and enter the following information using the Create PL/SQL Procedure dialog box.

Object Name: list\_a\_rating

Click OK. A source window for the new procedure is opened. Enter (or copy and paste) the following procedure text, replacing any existing text:

```
CREATE OR REPLACE
PROCEDURE list_a_rating(in_rating IN NUMBER) AS
  matching_title VARCHAR2(50);
  TYPE my_cursor IS REF CURSOR;
  the_cursor my_cursor;
BEGIN
  OPEN the_cursor
    FOR 'SELECT title 
           FROM books 
          WHERE rating = :in_rating'
    USING in_rating;
  DBMS_OUTPUT.PUT_LINE('All books with a rating of ' || in_rating || ':');
  LOOP
    FETCH the_cursor INTO matching_title;
    EXIT WHEN the_cursor%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE(matching_title);
  END LOOP;
  CLOSE the_cursor;
END list_a_rating;
```

This procedure uses a cursor (named the\_cursor) to return only rows where the book has the specified rating (in\_rating parameter), and uses a loop to output the title of each book with that rating.

Click the Save icon to save the procedure.

As a usage example, after creating the procedure named LIST\_A\_RATING, if you have inserted data into the BOOKS table (for example, using the INSERT statements in Insert Data into the Tables), you could use the following statement to return all books with a rating of 10:

```
CALL list_a_rating(10);
```

To run this procedure within SQL Developer, right-click LIST\_A\_RATING in the Connections navigator hierarchy display and select Run. Under PL/SQL Block in the Run PL/SQL dialog box, change IN\_RATING => IN\_RATING to IN\_RATING => 10, and click OK. The Log window display will now include the following output:

```
All books with a rating of 10:                                                  
Moby Dick                                                                       
Software Wizardry
```

## Debug a PL/SQL Procedure

If you want to practice debugging a PL/SQL procedure with SQL Developer, create a procedure that is like the list\_a\_rating procedure that you created in Create a PL/SQL Procedure, but with a logic error. (The coding is also deliberately inefficient, to allow the display of the rating in a variable.)

Before you can debug the procedure, you must ensure that the user associated with the database connection has the DEBUG CONNECT SESSION and DEBUG ANY PROCEDURE privileges.

To create this procedure, if you are not already connected, connect to the database as the user for the schema you are using for this tutorial. Right-click the Procedures node in the schema hierarchy on the left side, select New Procedure, and enter the following information using the Create PL/SQL Procedure dialog box.

Object Name: list\_a\_rating2

Click OK. A source window for the new procedure is opened. Enter (or copy and paste) the following procedure text, replacing any existing text:

```
CREATE OR REPLACE
PROCEDURE  list_a_rating2(in_rating IN NUMBER) AS
  matching_title VARCHAR2(50);
  matching_rating NUMBER;
  TYPE my_cursor IS REF CURSOR;
  the_cursor my_cursor;
  rating_cursor my_cursor;
BEGIN
  OPEN the_cursor 
    FOR 'SELECT title 
           FROM books 
          WHERE rating <= :in_rating' 
    USING in_rating;
  OPEN rating_cursor FOR 'SELECT rating FROM books WHERE 
    rating <= :in_rating' USING in_rating;
  DBMS_OUTPUT.PUT_LINE('All books with a rating of ' || in_rating || ':');
  LOOP
    FETCH the_cursor INTO matching_title;
    FETCH rating_cursor INTO matching_rating;
    EXIT WHEN the_cursor%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE(matching_title);
  END LOOP;
  CLOSE the_cursor;
  CLOSE rating_cursor;
END list_a_rating2;
```

This procedure contains a logic error in the definition of the\_cursor: it selects titles where the rating is less than or equal to a specified rating, whereas it should select titles only where the rating is equal to the specified rating.

Click the Save icon to save the procedure.

Assume that you wanted to run this procedure and list all books with a rating of 10. Right-click LIST\_A\_RATING2 in the Connections navigator hierarchy display and select Run. Under PL/SQL Block in the Run PL/SQL dialog box, change, change IN\_RATING => IN\_RATING to IN\_RATING => 10, and click OK. In the Log window, however, you see unexpected output: many titles are listed, including some with ratings other than 10. So, you decide to debug the procedure.

To debug the procedure, follow these steps:

1. Click the Compile for Debug icon in the toolbar under the LIST\_A\_RATING2 tab.
2. Set two breakpoints by clicking in the left margin (left of the thin vertical line) beside each of these two lines:
	```
	FETCH the_cursor INTO matching_title;
	FETCH rating_cursor INTO matching_rating;
	```
	Clicking in the left margin toggles the setting and unsetting of breakpoints. Clicking beside these two lines will enable you to see the values of the matching\_title and matching\_rating variables as execution proceeds in debug mode.
3. On the Debug menu, select Debug LIST\_A\_RATING2. Ensure that the line IN\_RATING => IN\_RATING has been changed to IN\_RATING => 10, and click OK.
4. Click View, then Debugger, then Data to display the Data pane. (Tip: Expand the Name column width so that you can see MATCHING\_RATING.)
5. Press the F9 key (or click Debug, then Resume) to have execution proceed, stopping at the next breakpoint.
6. Repeatedly press the F9 key (or click Debug, then Resume), noticing especially the value of MATCHING\_RATING as each row is processed. You will notice the first incorrect result when you see that the title Get Rich Really Fast is included, even though its rating is only 1 (obviously less than 10). (See the screen illustration with debugging information in [Running and Debugging Functions and Procedures](intro.md).)
7. When you have enough information to fix the problem, you can click the Debugging - Log tab, and Terminate icon in the debugging toolbar.

From this debugging session, you know that to fix the logic error, you should change `rating <= :in_rating` to `rating = :in_rating` in the definition of the\_cursor.

## Use the SQL Worksheet for Queries

You can use the SQL Worksheet to test SQL statements using a database connection. To display the worksheet, from the Tools menu, select SQL Worksheet. In the Select Connection dialog box, select the database connection that you used to create the BOOKS, PATRONS, and TRANSACTIONS tables for the tutorial in Chapter 3, "Tutorial: Creating Objects for a Small Database".

The SQL Worksheet has the user interface shown in [Using the SQL Worksheet](intro.md).

In the Enter SQL Statement box, enter the following statement (the semicolon is optional for the SQL Worksheet):

```
SELECT author_last_name, title FROM books;
```

Notice the automatic highlighting of SQL keywords (SELECT and FROM in this example).

Click the Execute SQL Statement icon in the SQL Worksheet toolbar. The results of the query are displayed on the Results tab under the area in which you entered the SQL statement.

In the Enter SQL Statement box, enter (or copy and paste) the following statement, which is the same as the SELECT statement in the view you created in Create a View:

```
SELECT p.patron_id,
       p.last_name,
       p.first_name,
       t.transaction_type,
       t.transaction_date
  FROM patrons p, transactions t
 WHERE p.patron_id = t.patron_id
 ORDER BY p.patron_id, t.transaction_type;
```

Click the Execute SQL Statement icon in the SQL Worksheet toolbar, and view the results of the query.

Click the Execute Explain Plan icon in the SQL Worksheet toolbar to see the execution plan (displayed on the Explain tab) that Oracle Database follows to execute the SQL statement. The information includes the optimizer strategy and the cost of executing the statement. (For information about how to generate and interpret execution plans, see Oracle Database Performance Tuning Guide.)

## Script for Creating and Using the Library Tutorial Objects

The following statements create and use the database objects that you have created (or will create) for the tutorial in Chapter 3, "Tutorial: Creating Objects for a Small Database". You can view these commands to help you understand the library database objects that are covered in the tutorial.

```
-- Clean up from any previous tutorial actions.
DROP TABLE transactions;
DROP TABLE books;
DROP TABLE patrons;
DROP SEQUENCE patron_id_seq;
DROP SEQUENCE transactions_seq;
DROP TRIGGER transactions_trg;
DROP VIEW patrons_trans_view;
DROP PROCEDURE list_a_rating;
DROP PROCEDURE list_a_rating2;
 
set serveroutput on
 
-- Create objects.
 
CREATE TABLE books (
   book_id VARCHAR2(20),
   title VARCHAR2(50)
      CONSTRAINT title_not_null NOT NULL,
   author_last_name VARCHAR2(30)
      CONSTRAINT last_name_not_null NOT NULL,
   author_first_name VARCHAR2(30),
   rating NUMBER,
   CONSTRAINT books_pk PRIMARY KEY (book_id),
   CONSTRAINT rating_1_to_10 CHECK (rating IS NULL OR
      (rating >= 1 and rating <= 10)),
   CONSTRAINT author_title_unique UNIQUE (author_last_name, title));
 
CREATE TABLE patrons (
   patron_id NUMBER,
   last_name VARCHAR2(30)
      CONSTRAINT patron_last_not_null NOT NULL,
   first_name VARCHAR2(30),
   street_address VARCHAR2(50),
   city_state_zip VARCHAR2(50),
   location MDSYS.SDO_GEOMETRY,
   CONSTRAINT patrons_pk PRIMARY KEY (patron_id));
 
CREATE TABLE transactions (
   transaction_id NUMBER,
   patron_id CONSTRAINT for_key_patron_id
      REFERENCES patrons(patron_id),
   book_id CONSTRAINT for_key_book_id
      REFERENCES books(book_id),
   transaction_date DATE
      CONSTRAINT tran_date_not_null NOT NULL,
   transaction_type NUMBER
      CONSTRAINT tran_type_not_null NOT NULL,
   CONSTRAINT transactions_pk PRIMARY KEY (transaction_id));
 
CREATE SEQUENCE patron_id_seq 
   START WITH 100
   INCREMENT BY 1;
 
-- The sequence for the transaction_id 
-- in the tutorial is created automatically,
-- and may have the name TRANSACTIONS_SEQ.
CREATE SEQUENCE transactions_seq 
   START WITH 1
   INCREMENT BY 1;
 
-- The before-insert trigger for transaction ID values
-- in the tutorial is created automatically,
-- and may have the name TRANSACTIONS_TRG.
CREATE OR REPLACE TRIGGER transactions_trg
   BEFORE INSERT ON TRANSACTIONS 
  FOR EACH ROW 
  BEGIN
    SELECT TRANSACTIONS_SEQ.NEXTVAL INTO :NEW.TRANSACTION_ID FROM DUAL;
  END;
/
 
CREATE VIEW patrons_trans_view AS
  SELECT p.patron_id,
         p.last_name,
         p.first_name,
         t.transaction_type,
         t.transaction_date
    FROM patrons p, transactions t
   WHERE p.patron_id = t.patron_id
   ORDER BY p.patron_id, t.transaction_type;
 
-- Procedure: List all books that have a specified rating.
CREATE OR REPLACE PROCEDURE list_a_rating(in_rating IN NUMBER) AS
  matching_title VARCHAR2(50);
  TYPE my_cursor IS REF CURSOR;
  the_cursor my_cursor;
BEGIN
  OPEN the_cursor
    FOR 'SELECT title 
           FROM books 
          WHERE rating = :in_rating'
    USING in_rating;
  DBMS_OUTPUT.PUT_LINE('All books with a rating of ' || in_rating || ':');
  LOOP
    FETCH the_cursor INTO matching_title;
    EXIT WHEN the_cursor%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE(matching_title);
  END LOOP;
  CLOSE the_cursor;
END;
/
show errors;
 
-- Insert and query data.
 
INSERT INTO books VALUES ('A1111', 'Moby Dick', 'Melville', 'Herman', 10);
INSERT INTO books VALUES ('A2222', 'Get Rich Really Fast', 'Scammer', 'Ima', 1);
INSERT INTO books VALUES ('A3333', 'Finding Inner Peace', 'Blissford', 'Serenity', null);
INSERT INTO books VALUES ('A4444', 'Great Mystery Stories', 'Whodunit', 'Rodney', 5);
INSERT INTO books VALUES ('A5555', 'Software Wizardry', 'Abugov', 'D.', 10);
 
INSERT INTO patrons VALUES  (patron_id_seq.nextval, 
   'Smith', 'Jane', '123 Main Street', 'Mytown, MA 01234', null);
INSERT INTO patrons VALUES  (patron_id_seq.nextval, 
   'Chen', 'William', '16 S. Maple Road', 'Mytown, MA 01234', null);
INSERT INTO patrons VALUES  (patron_id_seq.nextval, 
   'Fernandez', 'Maria', '502 Harrison Blvd.', 'Sometown, NH 03078', null);
INSERT INTO patrons VALUES  (patron_id_seq.nextval, 
   'Murphy', 'Sam', '57 Main Street', 'Mytown, MA 01234', null);
 
INSERT INTO transactions (patron_id, book_id, 
  transaction_date, transaction_type) 
  VALUES (100, 'A1111', SYSDATE, 1);
INSERT INTO transactions (patron_id, book_id, 
  transaction_date, transaction_type) 
  VALUES (100, 'A2222', SYSDATE, 2);
INSERT INTO transactions (patron_id, book_id, 
  transaction_date, transaction_type) 
  VALUES (101, 'A3333', SYSDATE, 3);
INSERT INTO transactions (patron_id, book_id, 
  transaction_date, transaction_type) 
  VALUES (101, 'A2222', SYSDATE, 1);
INSERT INTO transactions (patron_id, book_id, 
  transaction_date, transaction_type) 
  VALUES (102, 'A3333', SYSDATE, 1);
INSERT INTO transactions (patron_id, book_id, 
  transaction_date, transaction_type) 
  VALUES (103, 'A4444', SYSDATE, 2);
INSERT INTO transactions (patron_id, book_id, 
  transaction_date, transaction_type) 
  VALUES (100, 'A4444', SYSDATE, 1);
INSERT INTO transactions (patron_id, book_id, 
  transaction_date, transaction_type) 
  VALUES (102, 'A2222', SYSDATE, 2);
INSERT INTO transactions (patron_id, book_id, 
  transaction_date, transaction_type) 
  VALUES (102, 'A5555', SYSDATE, 1);
INSERT INTO transactions (patron_id, book_id, 
  transaction_date, transaction_type) 
  VALUES (101, 'A2222', SYSDATE, 1);
 
-- Test the view and the procedure.
SELECT * FROM patrons_trans_view;
CALL list_a_rating(10);
```