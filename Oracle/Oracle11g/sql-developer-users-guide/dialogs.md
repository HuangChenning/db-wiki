---
title: Dialog Boxes for Creating/Editing Objects
book: "SQL Developer User's Guide"
doc_id: E12152-08
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/doc.112/e12152/dialogs.htm
tags:
  - oracle
  - 11g
  - sql-developer-users-guide
---

## 4 Dialog Boxes for Creating/Editing Objects

SQL Developer uses dialog boxes for creating and editing database connections and objects in the database (tables, views, procedures, and so on). The dialog boxes sometimes have multiple tabs, each reflecting a logical grouping of properties for that type of object.

For an explanation of any dialog box or tab, click the Help button or press the F1 key.

The dialog boxes are not presented here in any rigorous order, because the help for each box is an independent piece of information and is normally seen when you click Help or press F1 in that box.

Note:

For all Name fields, any name that you type is automatically converted to and stored in the database metadata in uppercase, unless you enclose the name in quotation marks (" "). (Names of database objects in SQL and PL/SQL statements are not case-sensitive.)

To include lowercase characters, special characters, or spaces in object names, enclose the name in quotation marks (" ") when you type it. Example: `"My table"`

## Add Extension

This dialog box is displayed when you click Add in the [File Types](intro.md) pane of [SQL Developer Preferences](intro.md).

Extension: Specify the file extension, including the period (for example,.xyz).

After you click OK, you can select that extension and modify its details, including the file type, content type, and whether to have files with the extension automatically opened by SQL Developer.

## Branch/Tag

This dialog box is displayed when you right-click a remote directory in the Subversion repository and select Branch/Tag. Create a branch by copying the current working copy or a revision from the repository to a selected location in the repository.

From: Location of the working copy or revision.

Working Copy: Causes the current working copy to be copied.

HEAD Revision: Causes the HEAD revision (the latest revision in the repository) to be copied.

Use Revision: Causes the revision specified in the text box to be copied. To see a list of revisions from which you can choose, click List Revisions.

To: Destination location.