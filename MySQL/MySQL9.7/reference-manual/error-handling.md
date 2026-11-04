---
title: "Appendix B Error Messages and Common Problems"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/error-handling.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

This appendix describes the types of error information MySQL provides and how to obtain information about them. The final section is for troubleshooting. It describes common problems and errors that may occur and potential resolutions.

## Additional Resources

Other error-related documentation includes:

- Information about configuring where and how the server writes the error log: [Section 7.4.2, “The Error Log”](error-log.md)
- Information about the character set used for error messages: [Section 12.6, “Error Message Character Set”](charset-errors.md)
- Information about the language used for error messages: [Section 12.12, “Setting the Error Message Language”](error-message-language.md)
- Information about errors related to [`InnoDB`](innodb-storage-engine.md): [Section 17.20.5, “InnoDB Error Handling”](innodb-error-handling.md)
- Information about errors specific to NDB Cluster: [NDB Cluster API Errors](https://dev.mysql.com/doc/ndb-internals/en/ndb-errors.html); see also [NDB API Errors and Error Handling](https://docs.oracle.com/cd/E17952_01/ndbapi-en/ndb-api-errors.html), and [MGM API Errors](https://docs.oracle.com/cd/E17952_01/ndbapi-en/mgm-errors.html)
- Descriptions of the error messages that the MySQL server and client programs generate: [MySQL 9.7 Error Message Reference](https://docs.oracle.com/cd/E17952_01/mysql-errors-9.7-en/)