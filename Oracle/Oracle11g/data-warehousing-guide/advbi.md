---
title: Advanced Business Intelligence Queries
book: Data Warehousing Guide
doc_id: E25554-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e25554/advbi.htm
tags:
  - oracle
  - 11g
  - data-warehousing-guide
---

## 24 Advanced Business Intelligence Queries

This chapter illustrates techniques for handling advanced business intelligence queries. We hope to enhance your understanding of how different SQL features can be used together to perform demanding analyses. Although the features shown here have been addressed on an individual basis in [Chapter 21, "SQL for Aggregation in Data Warehouses"](aggreg.md), [Chapter 22, "SQL for Analysis and Reporting"](analysis.md), and [Chapter 23, "SQL for Modeling"](sqlmodel.md), seeing features one at a time gives only a limited sense of how they can work together. Here we show the analytic power available when the features are combined.

What makes a business intelligence query "advanced"? The label is best applied to multistep queries, often involving dimension hierarchies. In such queries, the final result depends on several sets of retrieved data, multiple calculation steps, and the data retrieved may involve multiple levels of a dimension hierarchy. Prime examples of advanced queries are market share calculations based on multiple conditions and sales projections that require filling gaps in data.

The examples in this chapter illustrate using nested inline views, `CASE` expressions, partition outer join, the `MODEL` and `WITH` clauses, analytic SQL functions, and more. Where relevant to the discussion, query plans will be discussed. This chapter includes:

- Examples of Business Intelligence Queries

## Examples of Business Intelligence Queries

The queries in this chapter illustrate various business intelligence tasks. The topics of the queries and the features used in each query are:

- Percent change in market share based on complex multistep conditions. It illustrates nested inline views, `CASE` expression, and analytic SQL functions.
- Sales projection with gaps in data filled in. It illustrates the `MODEL` clause together with partition outer join and the `CASE` expression.
- Customer analysis grouping customers into purchase-size buckets. It illustrates the `WITH` clause (query subfactoring) and the analytic SQL functions `percentile_cont` and `width_bucket`.
- Customer item grouping into itemsets. It illustrates calculating frequent itemsets using `DBMS_FREQUENT_ITEMSET.FI_TRANSACTIONAL` as a table function.

Example 1 Percent change in market share of products in a calculated set

What was the percent change in market share for a grouping of my top 20% of products for the current three-month period versus same period year ago for accounts that grew by more than 20 percent in revenue?

We define market share as a product's share of total sales. We do this because there is no data for competitors in the `sh` sample schema, so the typical share calculation of product sales and competitors' sales is not possible. The processing required for our share calculation is logically similar to a competitive market share calculation.

Here are the pieces of information we find in the query, in the order we need to find them:

1. Cities whose purchases grew by more than 20% during the specified 3-month period, versus the same 3-month period last year. Note that cities are limited to one country, and sales involving no promotion.
2. Top 20% of the products for the group of cities found in the prior step. That is, find sales by product summed across this customer group, and then select the 20% of products with the best sales.
3. The share of sales for each product found in the prior step. That is, using the products group found in the prior step, find each product's share of sales of all products. Find the shares for the same period a year ago and then calculate the change in share between the two years.

The techniques used in this example are:

- This query is performed using the `WITH` clause and nested inline views. Each inline view has been given a descriptive alias to show its data element, and comment lines indicate the boundaries of each inline view. Although inline views are powerful, we believe that readability and maintenance are much easier if queries are structured to maximize the use of the `WITH` clause.
- This query does not use the `WITH` clause as extensively as it might: some of the nested inline views could have been expressed as separate subclauses of the `WITH` clause. For instance, in the main query, we use two inline views that return just one value. These are used for the denominator of the share calculations. We could have factored out these items and placed them in the `WITH` clause for greater readability. For a contrast that does use the `WITH` clause to its maximum, see the example "Customer analysis by grouping customers into buckets" regarding customer purchase analysis.
- Note the use of `CASE` expressions within the arguments to `SUM` functions. The `CASE` expressions simplify the SQL by acting as an extra set of data filters after the `WHERE` clause. They allow us to sum one column of sales for a desired date and another column for a different date.
```
WITH prod_list AS                     --START: Top 20% of products
   ( SELECT prod_id prod_subset, cume_dist_prod
    FROM                              --START: All products Sales for city subset
    ( SELECT s.prod_id, SUM(amount_sold),
         CUME_DIST() OVER (ORDER BY SUM(amount_sold)) cume_dist_prod
      FROM sales s, customers c, channels ch,  products p, times t
      WHERE s.prod_id = p.prod_id AND p.prod_total_id = 1 AND
            s.channel_id = ch.channel_id AND ch.channel_total_id = 1 AND
            s.cust_id = c.cust_id AND
            s.promo_id = 999 AND
            s.time_id  = t.time_id AND t.calendar_quarter_id = 1776 AND
            c.cust_city_id IN
       (SELECT cust_city_id            --START: Top 20% of cities
       FROM
         (
           SELECT cust_city_id, ((new_cust_sales - old_cust_sales)
                / old_cust_sales ) pct_change, old_cust_sales
           FROM
           (
              SELECT cust_city_id, new_cust_sales, old_cust_sales
              FROM
              (          --START: Cities AND sales for 1 country in 2 periods
                SELECT cust_city_id,
                  SUM(CASE WHEN t.calendar_quarter_id = 1776
                     THEN amount_sold  ELSE  0  END ) new_cust_sales,
                  SUM(CASE WHEN t.calendar_quarter_id = 1772
                     THEN amount_sold ELSE 0 END) old_cust_sales
                FROM sales s, customers c, channels ch,
                     products p, times t
                WHERE s.prod_id = p.prod_id AND p.prod_total_id = 1 AND
                      s.channel_id = ch.channel_id AND ch.channel_total_id = 1 AND
                      s.cust_id = c.cust_id AND c.country_id = 52790 AND
                      s.promo_id = 999 AND
                      s.time_id  = t.time_id AND
                     (t.calendar_quarter_id = 1776 OR t.calendar_quarter_id =1772)
                GROUP BY cust_city_id
              ) cust_sales_wzeroes
              WHERE old_cust_sales > 0
           )  cust_sales_woutzeroes
         )         --END: Cities and sales for country in 2 periods
         WHERE old_cust_sales > 0 AND  pct_change >= 0.20)
                                 --END: Top 20% of cities
GROUP BY s.prod_id
)  prod_sales                    --END: All products sales for city subset
    WHERE cume_dist_prod > 0.8   --END: Top 20% products
)
                                 --START: Main query bloc
SELECT  prod_id, ( (new_subset_sales/new_tot_sales)
              -    (old_subset_sales/old_tot_sales)
                 ) *100  share_changes
FROM
(                                --START: Total sales for country in later period
  SELECT  prod_id,
     SUM(CASE WHEN t.calendar_quarter_id = 1776
                   THEN amount_sold  ELSE  0  END )  new_subset_sales,
        (SELECT SUM(amount_sold) FROM sales s, times t, channels ch,
                customers c, countries co, products p
          WHERE s.time_id  = t.time_id AND t.calendar_quarter_id = 1776 AND
                s.channel_id = ch.channel_id AND ch.channel_total_id = 1 AND
                s.cust_id = c.cust_id AND 
                c.country_id = co.country_id AND co.country_total_id = 52806 AND
                s.prod_id = p.prod_id AND p.prod_total_id = 1 AND
                s.promo_id = 999
        )   new_tot_sales,

                                --END: Total sales for country in later period
                                --START: Total sales for country in earlier period
     SUM(CASE WHEN t.calendar_quarter_id = 1772
                   THEN amount_sold  ELSE  0  END)  old_subset_sales,
        (SELECT SUM(amount_sold) FROM sales s, times t, channels ch, 
                customers c, countries co, products p
          WHERE s.time_id  = t.time_id AND t.calendar_quarter_id = 1772 AND
                s.channel_id = ch.channel_id AND ch.channel_total_id = 1 AND
                s.cust_id = c.cust_id AND
                c.country_id = co.country_id AND co.country_total_id = 52806 AND
                       s.prod_id = p.prod_id AND p.prod_total_id = 1 AND
                s.promo_id = 999
        )   old_tot_sales
                                --END: Total sales for country in earlier period
 FROM sales s, customers c, countries co, channels ch, times t
 WHERE s.channel_id = ch.channel_id AND ch.channel_total_id = 1 AND
       s.cust_id = c.cust_id AND
       c.country_id = co.country_id AND co.country_total_id = 52806 AND
       s.promo_id = 999 AND
       s.time_id  = t.time_id AND 
      (t.calendar_quarter_id = 1776 OR t.calendar_quarter_id = 1772)
         AND s.prod_id IN
     (SELECT prod_subset FROM prod_list)
  GROUP BY prod_id);
```

Example 2 Sales projection that fills in missing data

This query projects sales for 2002 based on the sales of 2000 and 2001. It finds the most percentage changes in sales from 2000 to 2001 and then adds that to the sales of 2002. While this is a simple calculation, there is an important thing to consider: many products have months with no sales in 2000 and 2001. We want to fill in blank values with the average sales value for the year (based on the months with actual sales). It converts currency values by country into US dollars. Finally, the query returns just the 2002 projection values.

The techniques used in this example are:

- By predefining all possible rows of data with the cross join ahead of the `MODEL` clause, we reduce the processing required by `MODEL`.
- The `MODEL` clause uses a reference model to perform currency conversion.
- By using the `CV` function extensively, we reduce the total number of rules needed to just three.
- The most interesting expression is found in the last rule, which uses a nested rule to find the currency conversion factor. To supply the country name needed for this expression, we define country as both a dimension `c` in the reference model, and a measure `cc` in the main model.

The way this example proceeds is to begin by creating a reference table of currency conversion factors. The table will hold conversion factors for each month for each country. Note that we use a cross join to specify the rows inserted into the table. For our purposes, we only set the conversion factor for one country, Canada.

```
CREATE TABLE currency (
   country         VARCHAR2(20),
   year            NUMBER,
   month           NUMBER,
   to_us           NUMBER);

INSERT INTO currency
(SELECT distinct
SUBSTR(country_name,1,20), calendar_year, calendar_month_number, 1
FROM countries
CROSS JOIN times t
WHERE calendar_year IN (2000,2001,2002)
);
UPDATE currency set to_us=.74 WHERE country='Canada';
```

Here is the projection query. It starts with a `WITH` clause that has two subclauses. The first subclause finds the monthly sales per product by country for the years 2000, 2001, and 2002. The second subclause finds a list of distinct times at the month level.

```
WITH  prod_sales_mo AS       --Product sales per month for one country
(
SELECT country_name c, prod_id p, calendar_year  y,
   calendar_month_number  m, SUM(amount_sold) s
FROM sales s, customers c, times t, countries cn, promotions p, channels ch
WHERE  s.promo_id = p.promo_id AND p.promo_total_id = 1 AND
       s.channel_id = ch.channel_id AND ch.channel_total_id = 1 AND
       s.cust_id=c.cust_id  AND 
       c.country_id=cn.country_id AND country_name='France' AND
       s.time_id=t.time_id  AND t.calendar_year IN  (2000, 2001,2002)
GROUP BY cn.country_name, prod_id, calendar_year, calendar_month_number
),
                    -- Time data used for ensuring that model has all dates
time_summary AS(  SELECT DISTINCT calendar_year cal_y, calendar_month_number cal_m
  FROM times
  WHERE  calendar_year IN  (2000, 2001, 2002)
)
                   --START: main query block
SELECT c, p, y, m, s,  nr FROM (
SELECT c, p, y, m, s,  nr
FROM prod_sales_mo s
                   --Use partition outer join to make sure that each combination
                   --of country and product has rows for all month values
  PARTITION BY (s.c, s.p)
     RIGHT OUTER JOIN time_summary ts ON
        (s.m = ts.cal_m
         AND s.y = ts.cal_y
        )
MODEL
  REFERENCE curr_conversion ON
      (SELECT country, year, month, to_us
      FROM currency)
      DIMENSION BY (country, year y,month m) MEASURES (to_us)
                                --START: main model
   PARTITION BY (s.c c)
   DIMENSION BY (s.p p, ts.cal_y y, ts.cal_m m)
   MEASURES (s.s s, CAST(NULL AS NUMBER) nr,
             s.c cc ) --country is used for currency conversion
   RULES (
                      --first rule fills in missing data with average values
      nr[ANY, ANY, ANY]
         = CASE WHEN s[CV(), CV(), CV()] IS NOT NULL
              THEN s[CV(), CV(), CV()]
              ELSE ROUND(AVG(s)[CV(), CV(), m BETWEEN 1 AND 12],2)
           END,
                      --second rule calculates projected values for 2002
      nr[ANY, 2002, ANY] = ROUND(
         ((nr[CV(),2001,CV()] - nr[CV(),2000, CV()])
          / nr[CV(),2000, CV()]) * nr[CV(),2001, CV()]
         + nr[CV(),2001, CV()],2),
                      --third rule converts 2002 projections to US dollars
      nr[ANY,y != 2002,ANY]
         = ROUND(nr[CV(),CV(),CV()]
           * curr_conversion.to_us[ cc[CV(),CV(),CV()], CV(y), CV(m)], 2)
)
ORDER BY c, p, y, m)
WHERE y = '2002'
ORDER BY c, p, y, m;
```

Example 3 Customer analysis by grouping customers into buckets

One important way to understand customers is by studying their purchasing patterns and learning the profitability of each customer. This can help us decide if a customer is worth cultivating and what kind of treatment to give it. Because the `sh` sample schema data set includes many customers, a good way to start a profitability analysis is with a high level view: we will find data for a histogram of customer profitability, dividing profitability into 10 ranges (often called "buckets" for histogram analyses).For each country at an aggregation level of 1 month, we show:

- The data needed for a 10-bucket equiwidth histogram of customer profitability. That is, show the count of customers falling into each of 10 profitability buckets. This is just 10 rows of results, but it involves significant calculations.

For each profitability bucket, we also show:

- The median count of transactions per customer during the month (treating each day's purchases by 1 customer in 1 channel as a single transaction).
- The median transaction size (in local currency) per customer.
- Products that generated the most and least profit.
- Percent change of median transaction count and median transaction size versus last year.

The techniques used in this example illustrate the following:

- Using the `WITH` clause to clarify a query. By dividing the needed data into logical chunks, each of which is expressed in its own `WITH` subclause, we greatly improve readability and maintenance compared to nested inline views. The thorough use of `WITH` subclauses means that the main `SELECT` clause does not need to perform any calculations on the data it retrieves, again contributing to the readability and maintainability of the query.
- Using two analytic SQL functions, `width_bucket` equiwidth histogram buckets and `percentile_cont` to median transaction size and count.

This query shows us the analytic challenges inherent in data warehouse designs: because the `sh` data does not include entries for every transaction, nor a count of transactions, we are forced to make an assumption. In this query, we will make the minimalist interpretation and assume that all products sold to a single customer through a single channel on a single day are part of the same transaction. This approach inevitably undercounts transactions, because some customers will in fact make multiple purchases through the same channel on the same day.

Note that the query below should not be run until a materialized view is created for the initial query subfactor `cust_prod_mon_profit`. Before creating the materialized view, create two additional indexes. Unless these preparatory steps are taken, the query may require significant time to run.The two additional indexes needed and the main query are as follows:

```
CREATE BITMAP INDEX costs_chan_bix
      ON costs (channel_id)
      LOCAL NOLOGGING COMPUTE STATISTICS;
 
CREATE BITMAP INDEX costs_promo_bix
      ON costs (promo_id)
      LOCAL NOLOGGING COMPUTE STATISTICS;
```
```
WITH cust_prod_mon_profit AS
-- profit by cust, prod, day, channel, promo
  (SELECT s.cust_id, s.prod_id, s.time_id,
          s.channel_id, s.promo_id,
          s.quantity_sold*(c.unit_price-c.unit_cost) profit,
          s.amount_sold dol_sold, c.unit_price price, c.unit_cost cost
   FROM sales s, costs c
   WHERE s.prod_id=c.prod_id
     AND s.time_id=c.time_id
     AND s.promo_id=c.promo_id
     AND s.channel_id=c.channel_id
     AND s.cust_id in (SELECT cust_id FROM customers cst
                       WHERE cst.country_id = 52770
     AND s.time_id IN (SELECT time_id FROM times t 
                       WHERE t.calendar_month_desc = '2000-12'
   ),
-- Transaction Definition:  All products sold through a single channel to a 
-- single cust on a single day are assumed to be sold in 1 transaction.
-- Some products in a transacton
-- may be on promotion
-- A customers  daily transaction amount is the sum of ALL products
-- purchased in the same channel in the same day
cust_daily_trans_amt  AS
(  SELECT cust_id, time_id, channel_id,  SUM(dol_sold) cust_daily_trans_amt
   FROM  cust_prod_mon_profit
   GROUP BY cust_id, time_id, channel_id
--A customers  monthly transaction count is the count of all channels
--used to purchase items in the same day, over all days in the month.
--It is really a count of the minimum possible number of transactions
cust_purchase_cnt  AS(  SELECT cust_id,  COUNT(*) cust_purchase_cnt
   FROM  cust_daily_trans_amt
   GROUP BY cust_id
), 
--  Total profit for a customer over 1 month
cust_mon_profit AS
( SELECT cust_id, SUM(profit) cust_profit
       FROM  cust_prod_mon_profit
       GROUP BY cust_id
-- Minimum and maximum profit across all customer
-- sets endpoints for histogram data.
min_max_p AS   
-- Note max profit + 0.1 to allow 10th bucket to include max value
(SELECT 0.1 + MAX(cust_profit) max_p, MIN(cust_profit) min_p 
FROM cust_mon_profit),
-- Profitability bucket found for each customer
cust_bucket AS
(SELECT cust_id, cust_profit,
   width_bucket(cust_profit,
         min_max_p.min_p,
FROM cust_mon_profit,  min_max_p
-- Aggregated data needed for each bucket
histo_data AS
(  SELECT bucket,
     bucket*(( max_p-min_p) /10) top_end , count(*)  histo_count
   FROM  cust_bucket, min_max_p 
   GROUP BY bucket, bucket*(( max_p - min_p) /10)
-- Median count of transactions per cust per month median_trans_count AS 
-- Find median count of transactions per cust per month
(SELECT cust_bucket.bucket, 
      PERCENTILE_CONT(0.5) WITHIN GROUP 
          (ORDER BY cust_purchase_cnt.cust_purchase_cnt) median_trans_count 
    FROM cust_bucket, cust_purchase_cnt
    WHERE cust_bucket.cust_id=cust_purchase_cnt.cust_id
    GROUP BY cust_bucket.bucket
-- Find Mmedian transaction size for custs by profit bucket
cust_median_trans_size AS
(  SELECT cust_bucket.bucket,
      PERCENTILE_CONT(0.5) WITHIN GROUP
          (ORDER BY cust_daily_trans_amt.cust_daily_trans_amt)
           cust_median_trans_ size
    FROM cust_bucket, cust_daily_trans_amt
    WHERE cust_bucket.cust_id=cust_daily_trans_amt.cust_id
    GROUP BY cust_bucket.bucket
-- Profitability of each product sold within each bucket
bucket_prod_profits AS
(  SELECT  cust_bucket.bucket, prod_id, SUM(profit) tot_prod_profit
   FROM  cust_bucket, cust_prod_mon_profit
   WHERE  cust_bucket.cust_id=cust_prod_mon_profit.cust_id
   GROUP BY cust_bucket.bucket, prod_id
),  -- Most and least profitable product by bucket
prod_profit AS
(  SELECT bucket, MIN(tot_prod_profit) min_profit_prod,
                  MAX(tot_prod_profit) max_profit_prod
   FROM bucket_prod_profits 
   GROUP BY bucket
-- Main query block
SELECT  histo_data.bucket, histo_data.histo_count,
        median_trans_count.median_trans_count,
        cust_median_trans_size.cust_median_trans_size,
        prod_profit.min_profit_prod, prod_profit.max_profit_prod
FROM  histo_data, median_trans_count, cust_median_trans_size,
      prod_profit
WHERE  histo_data.bucket=median_trans_count.bucket
  AND  histo_data.bucket=cust_median_trans_size.bucket
  AND  histo_data.bucket=prod_profit.bucket;
```

Example 4 Frequent itemsets

Consider a marketing manager who wants to know which pieces of his firm's collateral are downloaded by users during a single session. That is, the manager wants to know which groupings of collateral are the most frequent itemsets. This is easy to do with the integrated frequent itemsets facility, as long as the Web site's activity log records a user ID and session ID for each collateral piece that is downloaded. For context, first we show a list of the aggregate number of downloads for individual white papers. (In our example data here, we use names of Oracle papers.)

```
White paper titles                                               #
-------------------------------------------------------          ----
Table Compression in Oracle Database 10g                          696
Field Experiences with Large Data Warehouses                      439
Key Data Warehouse Features: A Comparative Performance Analysis   181
Materialized Views in Oracle Database 10g                         167
Parallel Execution in Oracle Database 10g                         166
```

Here is a sample of the type of query that would be used for such analysis. The query uses `DBMS_FREQUENT_ITEMSET.FI_TRANSACTIONAL` as a table function. To understand the details of the query structure, see the [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_frqist.htm#ARPLS007). The query returns the itemset of pairs of papers that were downloaded in a single session:

```
SELECT itemset, support, length, rnk
FROM
  (SELECT itemset, support, length,
   RANK(), OVER (PARTITION BY length ORDER BY support DESC) rnk
FROM
(SELECT CAST(itemset AS fi_char) itemset, support, length, total_tranx
 FROM table(DBMS_FREQUENT_ITEMSET.FI_TRANSACTIONAL
  (CURSOR(SELECT session_id, command
          FROM web_log
          WHERE time_stamp BETWEEN '01-APR-2002' AND '01-JUN-2002'),
          (60/2600), 2, 2, CURSOR(SELECT 'a' FROM DUAL WHERE 1=0),
          CURSOR(SELECT 'a' FROM DUAL WHERE 1=0)))))
   WHERE rnk <= 10;
```

Here are the first three items of results:

```
White paper titles                                                    #
---------------------------------------------------------         -----
Table Compression in Oracle Database 10g                            115
Field Experiences with Large Data Warehouses                           

Data Warehouse Performance Enhancements with Oracle Database 10g    109
Oracle Performance and Scalability in DSS Environments

Materialized Views in Oracle Database 10g                           107
Query Optimization in Oracle Database 10g
```

This analysis yielded some interesting results. If one were to look at the list of the most popular single papers, one would expect the most popular pairs of downloaded papers would often include the white paper "Table Compression in Oracle Database 10g", because it was the most popular download of all papers. However, only one of the top three pairs included this paper.

By using frequent itemsets to analyze the Web log information, a manager can glean much more information than available in a simple report that only lists the most popular pieces of collateral. From these results, the manager can see that visitors to this Web site tend to search for information on a single topic area during a single session: visitors interested in scalability download white papers on compression and large data warehouses, while visitors interested in complex query capabilities download papers on query optimization and materialized views. For a marketing manager, this type of information is helpful in determining what sort of collateral should be written in the future; for a Web designer, this information can provide additional suggestions on how to organize the Web site.

See ["Frequent Itemsets"](analysis.md) for more information.