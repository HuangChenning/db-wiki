---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-EMX_USAGE_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.195 V$EMX\_USAGE\_STATS

`V$EMX_USAGE_STATS` is used to track how often each report in Oracle Enterprise Manager Database Express (EM Express) is used and how long the EM Express servlet takes to serve these reports to the client.

This view contains statistics such as the number of requests captured in the EM Express servlet for each report, total elapsed time for the EM Express servlet to render each report, as well as a detailed time breakdown including database login time, request initialization time, time to run the SQL query, and time to stream and send the query result back to the client.

All statistics are accumulated over all requests for each EM Express report since the last time the database instance was restarted.

It also includes the timestamp of the last request for each report.

| Column | Datatype | Description |
| --- | --- | --- |
| `REPORT` | `VARCHAR2(400)` | Name of the EM Express report. All EM Express reports are XML reports with this format: %/orarep/component/report |
| `COUNT` | `NUMBER` | Number of requests captured by the EM Express servlet for this report since the last time the database instance was restarted |
| `LOGIN_ELAPSED_TIME` | `NUMBER` | Accumulated elapsed time for logging into the database across all requests for this report since the last time the database instance was restarted |
| `INITREQ_ELAPSED_TIME` | `NUMBER` | Accumulated elapsed time for initializing and preparing requests across all requests for this report since the last time the database instance was restarted |
| `SQL_ELAPSED_TIME` | `NUMBER` | Accumulated elapsed time for all requests that ran SQL queries for this report since the last time the database instance was restarted |
| `SEND_ELAPSED_TIME` | `NUMBER` | Accumulated elapsed time for streaming and sending the query result back to the client browser across all requests for this report since the last time the database instance was restarted |
| `TOTAL_ELAPSED_TIME` | `NUMBER` | Accumulated total elapsed time across all requests for this report since the last time the database instance was restarted |
| `LAST_REQ_TIME` | `DATE` | Timestamp of the last request for this report since the last time the database instance was restarted |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |