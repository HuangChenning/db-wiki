---
title: Power Demand Cartridge Example
book: "Data Cartridge Developer's Guide"
doc_id: E10765-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/pwr_example.htm
tags:
  - oracle
  - 11g
  - data-cartridge-developers-guide
---

## 15 Power Demand Cartridge Example

This chapter explains the power demand sample data cartridge that is discussed throughout this book. The power demand cartridge includes a user-defined object type, extensible indexing, and optimization. The entire cartridge definition is available online in file `extdemo1.sql` in the Oracle demo directory.

This chapter contains the following topics:

See Also:

- [Chapter 8, "Building Domain Indexes"](dom_idx.md) for information about extensible query optimization
- [Chapter 10, "Using Extensible Optimizer"](ext_optimizer.md) for information about extensible indexing
- [Chapter 12, "Using Cartridge Services"](cart_services.md) for information about cartridge services

## Feature Requirements

A power utility, Power-To-The-People, develops a sophisticated model to decide how to deploy its resources. The region served by the utility is represented by a grid laid over a geographic area. This grid is illustrated in Figure 15-1.

Figure 15-1 Region Served by the Power Utility

![Description of Figure 15-1 follows](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img/addci004.gif "Description of Figure 15-1 follows")  
[Description of "Figure 15-1 Region Served by the Power Utility"](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img_text/addci004.htm)  

This region may be surrounded by other regions some of whose power needs are supplied by other utilities. As pictured, every region is composed of geographic quadrants, called cells, on a 10x10 grid. There are several ways of identifying cells — by spatial coordinates (longitude/latitude), by a matrix numbering (1,1; 1,2;...), and by numbering them sequentially, as illustrated in Figure 15-2.

Figure 15-2 Regional Grid Cells in Numbered Sequence

![Description of Figure 15-2 follows](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img/addci006.gif "Description of Figure 15-2 follows")  
[Description of "Figure 15-2 Regional Grid Cells in Numbered Sequence"](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img_text/addci006.htm)  

Within the area represented by each cell, the power used by consumers in that area is recorded each hour. For example, the power demand readings for a particular hour might be represented by Table 15-1 (cells here represented on a matrix).

Table 15-1 Sample Power Demand Readings for an Hour

| \- | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `23` | `21` | `25` | `23` | `24` | `25` | `27` | `32` | `31` | `30` |
| 2 | `33` | `32` | `31` | `33` | `34` | `32` | `23` | `22` | `21` | `34` |
| 3 | `45` | `44` | `43` | `33` | `44` | `43` | `42` | `41` | `45` | `46` |
| 4 | `44` | `45` | `45` | `43` | `42` | `26` | `19` | `44` | `33` | `43` |
| 5 | `45` | `44` | `43` | `42` | `41` | `44` | `45` | `46` | `47` | `44` |
| 6 | `43` | `45` | `98` | `55` | `54` | `43` | `44` | `33` | `34` | `44` |
| 7 | `33` | `45` | `44` | `43` | `33` | `44` | `34` | `55` | `46` | `34` |
| 8 | `87` | `34` | `33` | `32` | `31` | `34` | `35` | `38` | `33` | `39` |
| 9 | `30` | `40` | `43` | `42` | `33` | `43` | `34` | `32` | `34` | `46` |
| 10 | `43` | `42` | `34` | `12` | `43` | `45` | `48` | `45` | `43` | `32` |

The power stations also receives reports from two other sources:

- Sensors on the ground provide temperature readings for every cell
	By analyzing the correlation between historical power demand from cells and the temperature readings for those regions, the utility is able to determine with a close approximation the expected demand, given specific temperatures.
- Satellite cameras provide images regarding current conditions that are converted into grayscale images that match the grid illustrated in Figure 15-3.

Figure 15-3 Grayscale Representation of Satellite Image

![Description of Figure 15-3 follows](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img/addci025.gif "Description of Figure 15-3 follows")  
[Description of "Figure 15-3 Grayscale Representation of Satellite Image "](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img_text/addci025.htm)  

These images are designed so that lighter is colder. Thus, the image shows a cold front moving into the region from the south-west. By correlating the data provided by the grayscale images with temperature readings taken at the same time, the utility has been able to determine what the power demand is given weather conditions viewed from the stratosphere.

The reason that this is important is that a crucial part of this modeling has to do with noting the rapidity and degree of change in the incoming reports as weather changes and power is deployed. The following diagram shows same cold front at a second recording, illustrated in Figure 15-4.

Figure 15-4 Grayscale Representation of Weather Conditions at Second Recording

![Description of Figure 15-4 follows](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img/addci026.gif "Description of Figure 15-4 follows")  
[Description of "Figure 15-4 Grayscale Representation of Weather Conditions at Second Recording"](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img_text/addci026.htm)  

By analyzing the extent and speed of the cold front, the utility is able to project what the conditions are likely to be in the short and medium term, as in Figure 15-5.

Figure 15-5 Grayscale Representation of Conditions as Projected

![Description of Figure 15-5 follows](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img/addci041.gif "Description of Figure 15-5 follows")  
[Description of "Figure 15-5 Grayscale Representation of Conditions as Projected "](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img_text/addci041.htm)  

By combing the data about these conditions and other anomalous situations (such as the failure of a substation), the utility must be able to organize the most optimal deployment of its resources. Figure 15-6 reflects the distribution of substations across the region.

Figure 15-6 Distribution of Power Stations Across the Region

![Description of Figure 15-6 follows](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img/addci020.gif "Description of Figure 15-6 follows")  
[Description of "Figure 15-6 Distribution of Power Stations Across the Region"](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img_text/addci020.htm)  

The distribution of power stations means that the utility can redirect its deployment of electricity to the areas of greatest need. Figure 15-7 gives a pictorial representation of the overlap between three stations.

Figure 15-7 Areas Served by Three Power Stations

![Description of Figure 15-7 follows](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img/addci021.gif "Description of Figure 15-7 follows")  
[Description of "Figure 15-7 Areas Served by Three Power Stations"](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img_text/addci021.htm)  

Depending on fluctuating requirements, the utility must be able to decide how to deploy its resources, and even whether to purchase power from another utility in the event of shortfall.

## Modeling the Application

This section includes a technical and business scenario. The Class Diagram in Figure 15-8 describes the application objects using the Unified Modelling Language (UML) notation.

Figure 15-8 Application Object Model of the Power Demand Cartridge

![Description of Figure 15-8 follows](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img/addci029.gif "Description of Figure 15-8 follows")  
[Description of "Figure 15-8 Application Object Model of the Power Demand Cartridge"](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img_text/addci029.htm)  

### Sample Queries

Modelling the application in this way, makes possible the following specific queries:

- Find the cell (geographic quadrant) with the highest demand for a specified time-period.
- Find the time-period with the highest total demand.
- Find all cells where demand is greater than some specified value.
- Find any cell at any time where the demand equals some specified value.
- Find any time period for which 3 or more cells have a demand greater than some specified.
- Find the time-period for which there was the greatest disparity (difference) between the cell with the minimum demand and the cell with the maximum demand.
- Find the times for which 10 or more cells had demand not less than some specified value.
- Find the times for which the average cell demand was greater than some specified value.
	Note that it is assumed that the average is easily computable through `TotalPowerDemand/100`.
- Find the time-periods for which the median cell demand was greater than some specified value.
	Note that we assume that the median value is not easily computable.
- Find all time-periods for which the total demand rose 10 percent or more over the preceding time's total demand.

These queries are, of course, only a short list of the possible information that could be gleaned from the system. For instance, it is obvious that the developer of such an application would want to build queries that are based on the information derived from prior queries:

- What is the percentage change in demand for a particular cell as compared to a previous time-period?
- Which cells demonstrate rapid increase or decrease in demand measured as percentages that are greater or less than specified values?

Figure 15-9 describes and illustrates the Power Demand cartridge, as implemented.

Figure 15-9 Implementation Model of the Power Demand Cartridge

![Description of Figure 15-9 follows](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img/addci028.gif "Description of Figure 15-9 follows")  
[Description of "Figure 15-9 Implementation Model of the Power Demand Cartridge"](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img_text/addci028.htm)  

The utility receives ongoing reports from weather centers about current conditions and from power stations about ongoing power utilization for specific geographical areas (represented by cells on a 10x10 grid). It then compares this information to historical data so it may predict demand for power in the different geographic areas for given time periods.

Each service area for the utility is considered as a 10x10 grid of cells, where each cell's boundaries are associated with spatial coordinates (longitude/latitude). The geographical areas represented by the cells can be uniform or can have different shapes and sizes. Within the area represented by each cell, the power used by consumers in that area is recorded each hour. For example, the power demand readings for a particular hour might be represented by Table 15-2.

Table 15-2 Sample Power Demand Readings for an Hour

| \- | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `23` | `21` | `25` | `23` | `24` | `25` | `27` | `32` | `31` | `30` |
| 2 | `33` | `32` | `31` | `33` | `34` | `32` | `23` | `22` | `21` | `34` |
| 3 | `45` | `44` | `43` | `33` | `44` | `43` | `42` | `41` | `45` | `46` |
| 4 | `44` | `45` | `45` | `43` | `42` | `26` | `19` | `44` | `33` | `43` |
| 5 | `45` | `44` | `43` | `42` | `41` | `44` | `45` | `46` | `47` | `44` |
| 6 | `43` | `45` | `98` | `55` | `54` | `43` | `44` | `33` | `34` | `44` |
| 7 | `33` | `45` | `44` | `43` | `33` | `44` | `34` | `55` | `46` | `34` |
| 8 | `87` | `34` | `33` | `32` | `31` | `34` | `35` | `38` | `33` | `39` |
| 9 | `30` | `40` | `43` | `42` | `33` | `43` | `34` | `32` | `34` | `46` |
| 10 | `43` | `42` | `34` | `12` | `43` | `45` | `48` | `45` | `43` | `32` |

The numbers in each cell reflect power demand (in some unit of measurement determined by the electric utility) for the hour for that area. For example, the demand for the first cell (1,1) was 23, the demand for the second cell (1,2) was 21, and so on. The demand for the last cell (10, 10) was 32.

The utility uses this data for many monitoring and analytical applications. Readings for individual cells are monitored for unusual surges or decreases in demand. For example, the readings of 98 for (6,3) and 87 for (8,1) might be unusually high, and the readings of 19 for (4,7) and 12 for (10,4) might be unusually low. Trends are also analyzed, such as significant increases or decreases in demand for each neighborhood, for each station, and overall, over time.

## Queries and Extensible Indexing

This section describes kinds of queries that benefit from domain indexes. Using extensible indexing depends on whether queries run as efficiently with a standard Oracle index, or with no index at all.

### Queries Not Benefiting from Extensible Indexing

A query does not require a domain index if both of the following are true:

- The desired information can be made an attribute (column) of the table and a standard index can be defined on that column.
- The operations in queries on the data are limited to those operations supported by the standard index, such as `equals`, `lessthan`, `greaterthan`, `max`, and `min` for a b-tree index.

In the `PowerDemand_Typ` object type cartridge example, the values for three columns (`TotGridDemand`, `MaxCellDemand`, and `MinCellDemand`) are set by functions, after which the values do not change. (For example, the total grid power demand for 13:00 on 01-Jan-1998 does not change after it has been computed.) For queries that use these columns, a standard b-tree index on each column is sufficient and recommended for operations like `equals`, `lessthan`, `greaterthan`, `max`, and `min`.

Examples of queries that would not benefit from extensible indexing (using the power demand cartridge) include:

- Find the cell with the highest power demand for a specific time.
- Find the time when the total grid power demand was highest.
- Find all cells where the power demand is greater than a specified value.
- Find the times for which the average cell demand or the median cell demand was greater than a specified value.
	To make this query run efficiently, define two additional columns in the `PowerDemand_Typ` object type (`AverageCellDemand` and `MedianCellDemand`), and create functions to set the values of these columns. (For example, `AverageCellDemand` is `TotGridDemand` divided by 100.) Then, create b-tree indexes on the `AverageCellDemand` and `MedianCellDemand` columns.

### Queries Benefiting from Extensible Indexing

A query benefits from a domain index if the data being queried against cannot be made a simple attribute of a table or if the operation to be performed on the data is not one of the standard operations supported by Oracle indexes.

Examples of queries that would benefit from extensible indexing (using the power demand cartridge) include:

- Find the first cell for a specified time where the power demand was equal to a specified value.
	By asking for the first cell, the query goes beyond a simple true-false check (such as finding out whether any cell for a specified time had a demand equal to a specified value), and thus benefits from a domain index.
- Find the time for which there was the greatest disparity, or difference between the cell with the minimum demand and the cell with the maximum demand.
- Find all times for which `3` or more cells had a demand greater than a specified value.
- Find all times for which 10 or more cells had a demand not less than a specified value.
- Find all times for which the total grid demand rose 10 percent or more over the preceding time's total grid demand.

## Creating the Domain Index

This section explains the parts of the power demand cartridge as they relate to extensible indexing. Explanatory text and code segments are mixed.

The entire cartridge definition is available online as extdemo1.sql in the standard Oracle demo directory (location is platform-dependent).

### Creating the Schema to Own the Index

Before you create a domain index, create a database user, or schema. to own the index. In the power demand example, the user `PowerCartUser` is created and granted the appropriate privileges. All database structures related to the cartridge are created under this user (that is, while the cartridge developer or DBA is connected to the database as `PowerCartUser`), as demonstrated in Example 15-1.

Example 15-1 Creating a Database User for the Power Demand Cartridge

```
set echo on
connect sys/knl_test7 as sysdba;
drop user PowerCartUser cascade;
create user PowerCartUser identified by PowerCartUser;

-------------------------------------------------------------------
-- INITIAL SET-UP
-------------------------------------------------------------------
-- grant privileges --
grant connect, resource to PowerCartUser;
grant create operator to PowerCartUser;
grant create indextype to PowerCartUser;
grant create table to PowerCartUser;
```

### Creating the Object Type PowerDemand\_Typ

The object type `PowerDemand_Typ` is used to store the hourly power grid readings. This type is used to define a column in the table in which the readings are stored.

First, two types are defined for later use, as demonstrated in Example 15-2.

- `PowerGrid_Typ`, to define the cells in `PowerDemand_Typ`
- `NumTab_Typ`, to be used in the table in which the index entries are stored

Example 15-2 Creating PowerGrid\_Typ and NumTab\_Typ Types for Power Demand Cartridge

```
CREATE OR REPLACE TYPE PowerGrid_Typ as VARRAY(100) of NUMBER;
CREATE OR REPLACE TYPE NumTab_Typ as TABLE of NUMBER;
```

The `PowerDemand_Typ` type, as demonstrated in Example 15-3, includes:

- Three attributes (`TotGridDemand`, `MaxCellDemand`, `MinCellDemand`) that are set by three member procedures
- Power demand readings (`100` cells in a grid)
- The date/time of the power demand readings. (Every hour, `100` areas transmit their power demand readings.)

Example 15-3 Creating PowerDemand\_Typ Type for Power Demand Cartridge

```
CREATE OR REPLACE TYPE PowerDemand_Typ AS OBJECT (
  -- Total power demand for the grid
  TotGridDemand NUMBER,
  -- Cell with maximum/minimum power demand for the grid
  MaxCellDemand NUMBER,
  MinCellDemand NUMBER,
  -- Power grid: 10X10 array represented as Varray(100)
  -- using previously defined PowerGrid_Typ
  CellDemandValues PowerGrid_Typ,
  -- Date/time for power-demand samplings: Every hour,
  -- 100 areas transmit their power demand readings.
  SampleTime DATE,
  --
  -- Methods (Set...) for this type:
  -- Total demand for the entire power grid for a
  -- SampleTime: sets the value of TotGridDemand.
  Member Procedure SetTotalDemand,
  -- Maximum demand for the entire power grid for a
  -- SampleTime: sets the value of MaxCellDemand.
  Member Procedure SetMaxDemand,
  -- Minimum demand for the entire power grid for a
  -- SampleTime: sets the value of MinCellDemand.
  Member Procedure SetMinDemand
);
/
```

### Defining the Object Type Methods

The `PowerDemand_Typ` object type has methods that set the first three attributes in the type definition:

- `TotGridDemand`, the total demand for the entire power grid for the hour in question (identified by `SampleTime`)
- `MaxCellDemand`, the highest power demand value for all cells for the `SampleTime`
- `MinCellDemand`, the lowest power demand value for all cells for the `SampleTime`

The logic for each procedure is not complicated. `SetTotDemand` loops through the cell values and creates a running total. `SetMaxDemand` compares the first two cell values and saves the higher as the current highest value; it then examines each successive cell, comparing it against the current highest value and saving the higher of the two as the current highest value, until it reaches the end of the cell values. `SetMinDemand` uses the same approach as `SetMaxDemand`, but it continually saves the lower value in comparisons to derive the lowest value overall, as demonstrated in Example 15-4.

Example 15-4 Implementing PowerDemand\_Typ Type for Power Demand Cartridge

```
CREATE OR REPLACE TYPE BODY PowerDemand_Typ 
IS
  --
  -- Methods (Set...) for this type:
  -- Total demand for the entire power grid for a
  -- SampleTime: sets the value of TotGridDemand.
  Member Procedure SetTotalDemand 
  IS
  I BINARY_INTEGER;
  Total NUMBER;
  BEGIN
    Total :=0;
    I := CellDemandValues.FIRST;   
    WHILE I IS NOT NULL LOOP
   Total := Total + CellDemandValues(I);
        I := CellDemandValues.NEXT(I);
    END LOOP;
    TotGridDemand := Total;
  END;

  -- Maximum demand for the entire power grid for a
  -- SampleTime: sets the value of MaxCellDemand.
  Member Procedure SetMaxDemand 
  IS
  I BINARY_INTEGER;
  Temp NUMBER;
  BEGIN
    I := CellDemandValues.FIRST;   
    Temp := CellDemandValues(I);
    WHILE I IS NOT NULL LOOP
   IF Temp < CellDemandValues(I) THEN
      Temp := CellDemandValues(I);
   END IF;
        I := CellDemandValues.NEXT(I);
    END LOOP;
    MaxCellDemand := Temp;
  END;

  -- Minimum demand for the entire power grid for a
  -- SampleTime: sets the value of MinCellDemand.
  Member Procedure SetMinDemand 
  IS
  I BINARY_INTEGER;
  Temp NUMBER;
  BEGIN
    I := CellDemandValues.FIRST;   
    Temp := CellDemandValues(I);
    WHILE I IS NOT NULL LOOP
   IF Temp > CellDemandValues(I) THEN
      Temp := CellDemandValues(I);
   END IF;
        I := CellDemandValues.NEXT(I);
    END LOOP;
    MinCellDemand := Temp;
  END;
END;
/
```

### Creating the Functions and Operators

The power demand cartridge is designed so that users can query the power grid for relationships of `equality`, `greaterthan`, or `lessthan`. However, because of the way the cell demand data is stored, the standard operators (`=`, `>`, `<`) cannot be used. Instead, new operators must be created, and a function must be created to define the implementation for each new operator (that is, how the operator is to be interpreted by Oracle).

For this cartridge, each of the three relationships can be checked in two ways:

- Whether a specific cell in the grid satisfies the relationship. For example, are there grids where cell `(3,7)` has demand equal to `25`?
	These operators have names in the form `Power_XxxxxSpecific()`, such as `Power_EqualsSpecific()`, and the implementing functions have names in the form `Power_XxxxxSpecific_Func()`.
- Whether any cell in the grid satisfies the relationship. For example, are there grids where any cell has demand equal to `25`?
	These operators have names in the form `Power_XxxxxAny()`, such as `Power_EqualsAny()`, and the implementing functions have names in the form `Power_XxxxxAny_Func()`.

For each operator-function pair, the function is defined first and then the operator as using the function. The function is the implementation that would be used if there were no index defined. This implementation must be specified so that the Oracle optimizer can determine costs, decide whether the index should be used, and create an execution plan.

Table 15-3 shows the operators and implementing functions:

Table 15-3 Operators and Implementing Functions

| Operator | Implementing Function |
| --- | --- |
| ``` Power_EqualsSpecific() ``` | ``` Power_EqualsSpecific_Func() ``` |
| ``` Power_EqualsAny() ``` | ``` Power_EqualsAny_Func() ``` |
| ``` Power_LessThanSpecific() ``` | ``` Power_LessThanSpecific_Func() ``` |
| ``` Power_LessThanAny() ``` | ``` Power_LessThanAny_Func() ``` |
| ``` Power_GreaterThanSpecific() ``` | ``` Power_GreaterThanSpecific_Func() ``` |
| ``` Power_GreaterThanAny() ``` | ``` Power_GreaterThanAny_Func() ``` |

Each function and operator returns a numeric value of `1` if the condition is true (for example, if the specified cell is equal to the specified value), `0` if the condition is not true, or `null` if the specified cell number is invalid.

The statements in Example 15-5 create the implementing functions, `Power_xxx_Func()`, first the `specific` and then the `any` implementations.

Example 15-5 Implementing Power\_XXX\_Func() Functions for Power Demand Cartridge

```
CREATE FUNCTION Power_EqualsSpecific_Func(
  object PowerDemand_Typ, cell NUMBER, value NUMBER)
RETURN NUMBER AS
  BEGIN
  IF cell <= object.CellDemandValues.LAST
  THEN
     IF (object.CellDemandValues(cell) = value) THEN
   RETURN 1;
     ELSE
   RETURN 0;
     END IF;
  ELSE
     RETURN NULL;
  END IF;
  END;
/
CREATE FUNCTION Power_GreaterThanSpecific_Func(
  object PowerDemand_Typ, cell NUMBER, value NUMBER)
RETURN NUMBER AS
  BEGIN
  IF cell <= object.CellDemandValues.LAST
  THEN
     IF (object.CellDemandValues(cell) > value) THEN
   RETURN 1;
     ELSE
   RETURN 0;
     END IF;
  ELSE
     RETURN NULL;
  END IF;
  END;
/
CREATE FUNCTION Power_LessThanSpecific_Func(
  object PowerDemand_Typ, cell NUMBER, value NUMBER)
RETURN NUMBER AS
  BEGIN
  IF cell <= object.CellDemandValues.LAST
  THEN
     IF (object.CellDemandValues(cell) < value) THEN
   RETURN 1;
     ELSE
   RETURN 0;
     END IF;
  ELSE
     RETURN NULL;
  END IF;
  END;
/
CREATE FUNCTION Power_EqualsAny_Func(
  object PowerDemand_Typ, value NUMBER)
RETURN NUMBER AS
   idx NUMBER;
  BEGIN
    FOR idx IN object.CellDemandValues.FIRST..object.CellDemandValues.LAST LOOP
      IF (object.CellDemandValues(idx) = value) THEN
   RETURN 1;
      END IF;
    END LOOP;
   RETURN 0;
  END;
/
CREATE FUNCTION Power_GreaterThanAny_Func(
  object PowerDemand_Typ, value NUMBER)
RETURN NUMBER AS
   idx NUMBER;
  BEGIN
    FOR idx IN object.CellDemandValues.FIRST..object.CellDemandValues.LAST LOOP
      IF (object.CellDemandValues(idx) > value) THEN
   RETURN 1;
      END IF;
    END LOOP;
   RETURN 0;
  END;
/
CREATE FUNCTION Power_LessThanAny_Func(
  object PowerDemand_Typ, value NUMBER)
RETURN NUMBER AS
   idx NUMBER;
  BEGIN
    FOR idx IN object.CellDemandValues.FIRST..object.CellDemandValues.LAST LOOP
      IF (object.CellDemandValues(idx) < value) THEN
   RETURN 1;
      END IF;
    END LOOP;
   RETURN 0;
  END;
/
```

The statements in Example 15-6 create the operators (`Power_xxx`). Each statement specifies an implementing function.

Example 15-6 Implementing Power\_XXX() Functions for Power Demand Cartridge

```
CREATE OPERATOR Power_Equals BINDING(PowerDemand_Typ, NUMBER, NUMBER)
  RETURN NUMBER USING Power_EqualsSpecific_Func;
CREATE OPERATOR Power_GreaterThan BINDING(PowerDemand_Typ, NUMBER, NUMBER)
  RETURN NUMBER USING Power_GreaterThanSpecific_Func;
CREATE OPERATOR Power_LessThan BINDING(PowerDemand_Typ, NUMBER, NUMBER)
  RETURN NUMBER USING Power_LessThanSpecific_Func;
  
CREATE OPERATOR Power_EqualsAny BINDING(PowerDemand_Typ, NUMBER)
  RETURN NUMBER USING Power_EqualsAny_Func;
CREATE OPERATOR Power_GreaterThanAny BINDING(PowerDemand_Typ, NUMBER)
  RETURN NUMBER USING Power_GreaterThanAny_Func;
CREATE OPERATOR Power_LessThanAny BINDING(PowerDemand_Typ, NUMBER)
  RETURN NUMBER USING Power_LessThanAny_Func;
```

### Creating the Indextype Implementation Methods

The power demand cartridge creates an object type for the indextype that specifies methods for the domain index. These methods are part of the `ODCIIndex` (Oracle Data Cartridge Interface Index) interface, and they collectively define the behavior of the index in terms of the methods for defining, manipulating, scanning, and exporting the index.

Table 15-4 shows the method functions (all but one starting with `ODCIIndex`) created for the power demand cartridge.

Table 15-4 Indextype Methods

| Method | Description |
| --- | --- |
| [ODCIGetInterfaces()](ext_idx_ref.md) | Returns the list interface names implemented by the type. |
| [ODCIIndexCreate()](ext_idx_ref.md) | Creates a table to store index data. If the base table containing data to be indexed is not empty, this method builds the index for existing data.  This method is called when a `CREATE` `INDEX` statement is issued that refers to the indextype. Upon invocation, any parameters specified in the `PARAMETERS` clause are passed in along with a description of the index. |
| [ODCIIndexDrop()](ext_idx_ref.md) | Drops the table that stores the index data. This method is called when a `DROP` `INDEX` statement specifies the index. |
| [ODCIIndexStart()](ext_idx_ref.md) | Initializes the scan of the index for the operator predicate. This method is invoked when a query is submitted involving an operator that can be executed using the domain index. |
| [ODCIIndexFetch()](ext_idx_ref.md) | Returns the `ROWID` of each row that satisfies the operator predicate. |
| [ODCIIndexClose()](ext_idx_ref.md) | Ends the current use of the index. This method can perform any necessary clean-up. |
| [ODCIIndexInsert()](ext_idx_ref.md) | Maintains the index structure when a record is inserted in a table that contains columns or object attributes indexed by the indextype. |
| [ODCIIndexDelete()](ext_idx_ref.md) | Maintains the index structure when a record is deleted from a table that contains columns or object attributes indexed by the indextype. |
| [ODCIIndexUpdate()](ext_idx_ref.md) | Maintains the index structure when a record is updated (modified) in a table that contains columns or object attributes indexed by the indextype. |
| [ODCIIndexGetMetadata()](ext_idx_ref.md) | Allows the export and import of implementation-specific metadata associated with the index. |

#### Type Definition

Example 15-7 creates the `power_idxtype_im` object type. The methods of this type are the ODCI methods to define, manipulate, and scan the domain index. The `curnum` attribute is the cursor number used as context for the scan routines [ODCIIndexStart()](ext_idx_ref.md), [ODCIIndexFetch()](ext_idx_ref.md), and [ODCIIndexClose()](ext_idx_ref.md).

Example 15-7 Creating power\_idxtype\_im Object Type for Power Demand Cartridge

```
CREATE OR REPLACE TYPE power_idxtype_im AS OBJECT
(
  curnum NUMBER,
  STATIC FUNCTION ODCIGetInterfaces(ifclist OUT sys.ODCIObjectList)
     RETURN NUMBER,
  STATIC FUNCTION ODCIIndexCreate (ia sys.ODCIIndexInfo, parms VARCHAR2, 
     env sys.ODCIEnv) RETURN NUMBER,
  STATIC FUNCTION ODCIIndexDrop(ia sys.ODCIIndexInfo, env sys.ODCIEnv)
     RETURN NUMBER,
  STATIC FUNCTION ODCIIndexStart(sctx IN OUT power_idxtype_im,
                                 ia sys.ODCIIndexInfo,
                                 op sys.ODCIPredInfo, qi sys.ODCIQueryInfo,
                                 strt NUMBER, stop NUMBER,
                                 cmppos NUMBER, cmpval NUMBER, env sys.ODCIEnv) 
     RETURN NUMBER,
  STATIC FUNCTION ODCIIndexStart(sctx IN OUT power_idxtype_im,
                                 ia sys.ODCIIndexInfo,
                                 op sys.ODCIPredInfo, qi sys.ODCIQueryInfo,
                                 strt NUMBER, stop NUMBER,
                                 cmpval NUMBER, env sys.ODCIEnv)
     RETURN NUMBER,
  MEMBER FUNCTION ODCIIndexFetch(nrows NUMBER, rids OUT sys.ODCIRidList, 
     env sys.ODCIEnv) RETURN NUMBER,
  MEMBER FUNCTION ODCIIndexClose (env sys.ODCIEnv) RETURN NUMBER,
  STATIC FUNCTION ODCIIndexInsert(ia sys.ODCIIndexInfo, rid VARCHAR2,
                                  newval PowerDemand_Typ, env sys.ODCIEnv)
     RETURN NUMBER,
  STATIC FUNCTION ODCIIndexDelete(ia sys.ODCIIndexInfo, rid VARCHAR2,
                                  oldval PowerDemand_Typ, env sys.ODCIEnv)
     RETURN NUMBER,
  STATIC FUNCTION ODCIIndexUpdate(ia sys.ODCIIndexInfo, rid VARCHAR2,
                                  oldval PowerDemand_Typ, 
                                  newval PowerDemand_Typ, env sys.ODCIEnv) 
     RETURN NUMBER,
  STATIC FUNCTION ODCIIndexGetMetadata(ia sys.ODCIIndexInfo, 
                                       expversion VARCHAR2, 
                                       newblock OUT PLS_INTEGER, 
                                       env sys.ODCIEnv) 
     RETURN VARCHAR2
);
/
```

The `CREATE` `TYPE` statement is followed by a `CREATE` `TYPE` `BODY` statement that specifies the implementation for each member function:

```
CREATE OR REPLACE TYPE BODY power_idxtype_im 
IS
...
```

Each type method is described in a separate section, but the method definitions (except for [ODCIIndexGetMetadata()](ext_idx_ref.md), which returns a `VARCHAR2` string) have the following general form:

```
STATIC FUNCTION function-name (...) 
  RETURN NUMBER
IS
...
END;
```

#### ODCIGetInterfaces() Method

The [ODCIGetInterfaces()](ext_idx_ref.md) function returns the list of names of the interfaces implemented by the type. To specify the current version of these interfaces, the [ODCIGetInterfaces()](ext_idx_ref.md) routine must return `'SYS.ODCIINDEX2'` in the `OUT` parameter, as demonstrated in Example 15-8.

Example 15-8 Registering Interface and Index Functions in Power Demand Cartridge

```
STATIC FUNCTION ODCIGetInterfaces(
  ifclist OUT sys.ODCIObjectList)
RETURN NUMBER IS
BEGIN
  ifclist := sys.ODCIObjectList(sys.ODCIObject('SYS','ODCIINDEX2'));
  return ODCIConst.Success;
END ODCIGetInterfaces;
```

#### ODCIIndexCreate() Method

The [ODCIIndexCreate()](ext_idx_ref.md) function creates the table to store index data. If the base table containing data to be indexed is not empty, this method inserts the index data entries for existing data.

The function takes the index information as an object parameter whose type is `SYS`.`ODCIINDEXINFO`. The type attributes include the index name, owner name, and so forth. The `PARAMETERS` string specified in the `CREATE` `INDEX` statement is also passed in as a parameter to the function, as demonstrated in Example 15-9.

Example 15-9 Registering ODCIIndexCreate() for Power Demand Cartridge

```
STATIC FUNCTION ODCIIndexCreate (
  ia sys.ODCIIndexInfo,
  parms VARCHAR2,
  env sys.ODCIEnv)
RETURN NUMBER IS
  i INTEGER;
  r ROWID;
  p NUMBER;
  v NUMBER;
  stmt1 VARCHAR2(1000);
  stmt2 VARCHAR2(1000);
  stmt3 VARCHAR2(1000);
  cnum1 INTEGER;
  cnum2 INTEGER;
  cnum3 INTEGER;
junk NUMBER;
```

The SQL statement to create the table for the index data is constructed and executed. The table includes the `ROWID` of the base table, `r`, the cell position number (`cpos`) in the grid from 1 to 100, and the power demand value in that cell (`cval`).

```
BEGIN
  -- Construct the SQL statement.
  stmt1 := 'CREATE TABLE ' || ia.IndexSchema || '.' || ia.IndexName ||'_pidx' ||
      '( r ROWID, cpos NUMBER, cval NUMBER)';

  -- Dump the SQL statement.
  dbms_output.put_line('ODCIIndexCreate>>>>>');
  sys.ODCIIndexInfoDump(ia);
  dbms_output.put_line('ODCIIndexCreate>>>>>'||stmt1);

  -- Execute the statement.
  cnum1 := dbms_sql.open_cursor;
  dbms_sql.parse(cnum1, stmt1, dbms_sql.native);
  junk := dbms_sql.execute(cnum1);
  dbms_sql.close_cursor(cnum1);
```

The function populates the index by inserting rows into the table. The function "unnests" the `VARRAY` attribute and inserts a row for each cell into the table. Thus, each 10 X 10 grid (10 rows, 10 values for each row) becomes 100 rows in the table (one row for each cell).

```
-- Now populate the table.
stmt2 := ' INSERT INTO '|| ia.IndexSchema || '.' || ia.IndexName || '_pidx' ||
    ' SELECT :rr, ROWNUM, column_value FROM THE' || ' (SELECT CAST (P.'||
    ia.IndexCols(1).ColName||'.CellDemandValues AS NumTab_Typ)'|| ' FROM ' ||
    ia.IndexCols(1).TableSchema || '.' || ia.IndexCols(1).TableName || ' P' ||
    ' WHERE P.ROWID = :rr)';

-- Execute the statement.
dbms_output.put_line('ODCIIndexCreate>>>>>'||stmt2);

-- Parse the statement.
cnum2 := dbms_sql.open_cursor;
dbms_sql.parse(cnum2, stmt2, dbms_sql.native);

stmt3 := 'SELECT ROWID FROM '|| ia.IndexCols(1).TableSchema || '.' ||
    ia.IndexCols(1).TableName;
dbms_output.put_line('ODCIIndexCreate>>>>>'||stmt3);
cnum3 := dbms_sql.open_cursor;
dbms_sql.parse(cnum3, stmt3, dbms_sql.native);
dbms_sql.define_column_rowid(cnum3, 1, r);   
junk := dbms_sql.execute(cnum3);

 WHILE dbms_sql.fetch_rows(cnum3) > 0 LOOP
  -- Get column values of the row. --
  dbms_sql.column_value_rowid(cnum3, 1, r);
  -- Bind the row into the cursor for the next insert. --
  dbms_sql.bind_variable_rowid(cnum2, ':rr', r);
  junk := dbms_sql.execute(cnum2);
END LOOP;
```

The function concludes by closing the cursors and returning a success status.

```
dbms_sql.close_cursor(cnum2);
  dbms_sql.close_cursor(cnum3);
  RETURN ODCICONST.SUCCESS;
END ODCIInexCreate;
```

#### ODCIIndexDrop() Method

The [ODCIIndexDrop()](ext_idx_ref.md) function drops the table that stores the index data, as demonstrated in Example 15-10. This method is called when a `DROP` `INDEX` statement is issued.

Example 15-10 Registering ODCIIndexDrop() for Power Demand Cartridge

```
STATIC FUNCTION ODCIIndexDrop(ia sys.ODCIIndexInfo, env sys.ODCIEnv)
RETURN NUMBER IS
  stmt VARCHAR2(1000);
  cnum INTEGER;
  junk INTEGER;
BEGIN
  -- Construct the SQL statement.
  stmt := 'drop table ' || ia.IndexSchema || '.' || ia.IndexName || '_pidx';
  
  dbms_output.put_line('ODCIIndexDrop>>>>>');
  sys.ODCIIndexInfoDump(ia);
  dbms_output.put_line('ODCIIndexDrop>>>>>'||stmt);
  
  -- Execute the statement.
  cnum := dbms_sql.open_cursor;
  dbms_sql.parse(cnum, stmt, dbms_sql.native);
  junk := dbms_sql.execute(cnum);
  dbms_sql.close_cursor(cnum);
  
  RETURN ODCICONST.SUCCESS;
END ODCIIndexDrop;
```

#### ODCIIndexStart() Method for Specific Queries

The first definition of the [ODCIIndexStart()](ext_idx_ref.md) function initializes the scan of the index to return all rows that satisfy the operator predicate. For example, if a query asks for all instances where cell `(3,7)` has a value equal to `25`, the function initializes the scan to return all rows in the index-organized table for which that cell has that value. This definition of [ODCIIndexStart()](ext_idx_ref.md) differs from the definition in the section "ODCIIndexStart() Method for Any Queries" in that it includes the `cmppos` parameter for the position of the cell.

The `self` parameter is the context that is shared with the [ODCIIndexFetch()](ext_idx_ref.md) and [ODCIIndexClose()](ext_idx_ref.md) functions. The `ia` parameter contains the index information as an object instance of type `SYS`.`ODCIINDEXINFO`, and the `op` parameter contains the operator information as an object instance of type `SYS`.`ODCIOPERINFO`. The `strt` and `stop` parameters are the lower and upper boundary points for the operator return value. The `cmppos` parameter is the cell position and `cmpval` is the value in the cell specified by the operator `Power_XxxxxSpecific()`. This is demonstrated in Example 15-11.

Example 15-11 Registering ODCIIndexStart() for Power Demand Cartridge

```
STATIC FUNCTION ODCIIndexStart(
  sctx IN OUT power_idxtype_im, 
  ia sys.ODCIIndexInfo,
  op sys.ODCIPredInfo, 
  qi sys.ODCIQueryInfo,
  strt NUMBER, stop NUMBER,
  cmppos NUMBER, 
  cmpval NUMBER, 
  env sys.ODCIEnv ) 
RETURN NUMBER IS
  cnum INTEGER;
  rid ROWID;
  nrows INTEGER;
  relop VARCHAR2(2);
  stmt VARCHAR2(1000);
BEGIN
  dbms_output.put_line('ODCIIndexStart>>>>>');
  sys.ODCIIndexInfoDump(ia);
  sys.ODCIPredInfoDump(op);
  dbms_output.put_line('start key : '||strt);
  dbms_output.put_line('stop key : '||stop);
  dbms_output.put_line('compare position : '||cmppos);
  dbms_output.put_line('compare value : '||cmpval);
```

The function checks for errors in the predicate.

```
-- Take care of some error cases.
-- The only predicates in which btree operators can appear are
--    op() = 1     OR    op() = 0
if (strt != 1) and (strt != 0) then
  raise_application_error(-20101, 'Incorrect predicate for operator');
END if;

if (stop != 1) and (stop != 0) then
  raise_application_error(-20101, 'Incorrect predicate for operator');
END if;
```

The function generates the SQL statement to be executed. It determines the operator name and the lower and upper index value bounds (the start and stop keys). The start and stop keys can both be 1 (= `TRUE`) or both be 0 (= `FALSE`).

```
-- Generate the SQL statement to be executed.
-- First, figure out the relational operator needed for the statement.
-- Take into account the operator name and the start and stop keys. For now, 
-- the start and stop keys can both be 1 (= TRUE) or both be 0 (= FALSE).
if op.ObjectName = 'POWER_EQUALS' then
  if strt = 1 then 
    relop := '=';
  else
    relop := '!=';
  end if;
elsif op.ObjectName = 'POWER_LESSTHAN' then
  if strt = 1 then 
    relop := '<';
  else
    relop := '>=';
  end if;
elsif op.ObjectName = 'POWER_GREATERTHAN' then
  if strt = 1 then 
    relop := '>';
  else
    relop := '<=';
  end if;
else
  raise_application_error(-20101, 'Unsupported operator');
end if;

stmt := 'select r from '||ia.IndexSchema||'.'||ia.IndexName||'_pidx'||
    ' where cpos '|| '=' ||''''||cmppos||''''|| ' and cval ' ||relop||''''||
    cmpval||'''';

dbms_output.put_line('ODCIIndexStart>>>>>' || stmt);
 cnum := dbms_sql.open_cursor;
dbms_sql.parse(cnum, stmt, dbms_sql.native);
dbms_sql.define_column_rowid(cnum, 1, rid);   
nrows := dbms_sql.execute(cnum);
```

The function stores the cursor number in the context, which is used by the `ODCIIndexFetch` function, and sets a success return status.

```
-- Set context as the cursor number.
  stcx := power_idxtype_im(cnum);
 
  -- Return success.
  RETURN ODCICONST.SUCCESS;
END ODCIIndexStart;
```

#### ODCIIndexStart() Method for Any Queries

This definition of the [ODCIIndexStart()](ext_idx_ref.md) function initializes the scan of the index to return all rows that satisfy the operator predicate. For example, if a query asks for all instances where any cell has a value equal to `25`, the function initializes the scan to return all rows in the index-organized table for which that cell has that value. This definition of [ODCIIndexStart()](ext_idx_ref.md) differs from the definition insection "ODCIIndexStart() Method for Specific Queries" in that it does not include the `cmppos` parameter.

The `self` parameter is the context that is shared with the [ODCIIndexFetch()](ext_idx_ref.md) and [ODCIIndexClose()](ext_idx_ref.md) functions. The `ia` parameter contains the index information as an object instance of type `SYS`.`ODCIINDEXINFO`, and the `op` parameter contains the operator information as an object instance of type `SYS`.`ODCIOPERINFO`. The `strt` and `stop` parameters are the lower and upper boundary points for the operator return value. The `cmpval` parameter is the value in the cell specified by the operator `Power_Xxxx()`.

Example 15-12 Registering ODCIIndexStart() for Any Queries for Power Demand Cartridge

```
STATIC FUNCTION ODCIIndexStart(
  sctx IN OUT power_idxtype_im, 
  ia sys.ODCIIndexInfo,
  op sys.ODCIPredInfo, 
  qi sys.ODCIQueryInfo,
  strt NUMBER, 
  stop NUMBER,
  cmpval NUMBER, 
  env sys.ODCIEnv ) 
RETURN NUMBER IS
  cnum INTEGER;
  rid ROWID;
  nrows INTEGER;
  relop VARCHAR2(2);
  stmt VARCHAR2(1000);
BEGIN
  dbms_output.put_line('ODCIIndexStart>>>>>');
  sys.ODCIIndexInfoDump(ia);
  sys.ODCIPredInfoDump(op);
  dbms_output.put_line('start key : '||strt);
  dbms_output.put_line('stop key : '||stop);
  dbms_output.put_line('compare value : '||cmpval);
```

The function checks for errors in the predicate.

```
-- Take care of some error cases.
-- The only predicates in which btree operators can appear are
--    op() = 1     OR    op() = 0
if (strt != 1) and (strt != 0) then
  raise_application_error(-20101, 'Incorrect predicate for operator');
END if;

if (stop != 1) and (stop != 0) then
  raise_application_error(-20101, 'Incorrect predicate for operator');
END if;
```

The function generates the SQL statement to be executed. It determines the operator name and the lower and upper index value bounds (the start and stop keys). The start and stop keys can both be 1 (= `TRUE`) or both be 0 (= `FALSE`).

```
-- Generate the SQL statement to be executed.
-- First, figure out the relational operator needed for the statement.
-- Take into account the operator name and the start and stop keys. For now, 
-- the start and stop keys can both be 1 (= TRUE) or both be 0 (= FALSE).
if op.ObjectName = 'POWER_EQUALSANY' then
  relop := '=';
elsif op.ObjectName = 'POWER_LESSTHANANY' then
  relop := '<';
elsif op.ObjectName = 'POWER_GREATERTHANANY' then
  relop := '>';
else
  raise_application_error(-20101, 'Unsupported operator');
end if;

-- This statement returns the qualifying rows for the TRUE case.
stmt := 'select distinct r from '||ia.IndexSchema||'.'||ia.IndexName||'_pidx'||'
    where cval '||relop||''''||cmpval||'''';
-- In the FALSE case, we must find the  complement of the rows.
if (strt = 0) then
  stmt := 'select distinct r from '||ia.IndexSchema||'.'||ia.IndexName||
        '_pidx'||' minus '||stmt;
end if;

dbms_output.put_line('ODCIIndexStart>>>>>' || stmt);
cnum := dbms_sql.open_cursor;
dbms_sql.parse(cnum, stmt, dbms_sql.native);
dbms_sql.define_column_rowid(cnum, 1, rid);   
nrows := dbms_sql.execute(cnum);
```

The function stores the cursor number in the context, which is used by the [ODCIIndexFetch()](ext_idx_ref.md) function, and sets a success return status.

```
-- Set context as the cursor number.
  self := power_idxtype_im(cnum);
 
  -- Return success.
  RETURN ODCICONST.SUCCESS;
END ODCIIndexStart;
```

#### ODCIIndexFetch() Method

The [ODCIIndexFetch()](ext_idx_ref.md) function, demonstrated in Example 15-13 returns a batch of `ROWIDs` for the rows that satisfy the operator predicate. Each time [ODCIIndexFetch()](ext_idx_ref.md) is invoked, it returns the next batch of rows (`rids` parameter, a collection of type `SYS`.`ODCIRIDLIST`) that satisfy the operator predicate. The maximum number of rows that can be returned on each invocation is specified by the `nrows` parameter.

Oracle invokes [ODCIIndexFetch()](ext_idx_ref.md) repeatedly until all rows that satisfy the operator predicate have been returned.

Example 15-13 Registering ODCIIndexFetch() for Power Demand Cartridge

```
MEMBER FUNCTION ODCIIndexFetch(
  nrows NUMBER, 
  rids OUT sys.ODCIRidList, 
  env sys.ODCIEnv)
RETURN NUMBER IS
  cnum INTEGER;
  idx INTEGER := 1;
  rlist sys.ODCIRidList := sys.ODCIRidList();
  done boolean := FALSE;
```

The function loops through the collection of rows selected by the [ODCIIndexStart()](ext_idx_ref.md) function, using the same cursor number, `cnum`, as in the [ODCIIndexStart()](ext_idx_ref.md) function, and returns the `ROWIDs`.

```
BEGIN
  dbms_output.put_line('ODCIIndexFetch>>>>>');
  dbms_output.put_line('Nrows : '||round(nrows));
 
  cnum := self.curnum;
 
  WHILE not done LOOP
    if idx > nrows then
       done := TRUE;
    else
      rlist.extEND;
      if dbms_sql.fetch_rows(cnum) > 0 then
        dbms_sql.column_value_rowid(cnum, 1, rlist(idx));
        idx := idx + 1;
      else
        rlist(idx) := null;
        done := TRUE;
      END if;
    END if;   
  END LOOP;
 
  rids := rlist;
  RETURN ODCICONST.SUCCESS;
END ODCIIndexFetch;
```

#### ODCIIndexClose() Method

The [ODCIIndexClose()](ext_idx_ref.md) function, demonstrated in Example 15-14, closes the cursor used by the [ODCIIndexStart()](ext_idx_ref.md) and [ODCIIndexFetch()](ext_idx_ref.md) functions.

Example 15-14 Registering ODCIIndexStart() for Power Demand Cartridge

```
MEMBER FUNCTION ODCIIndexClose (env sys.ODCIEnv) 
RETURN NUMBER IS 
  cnum INTEGER;
BEGIN
  dbms_output.put_line('ODCIIndexClose>>>>>');
 
  cnum := self.curnum;
  dbms_sql.close_cursor(cnum);
  RETURN ODCICONST.SUCCESS;
END ODCIIndexClose;
```

#### ODCIIndexInsert() Method

The [ODCIIndexInsert()](ext_idx_ref.md) function, demonstrated in Example 15-15, is called when a record is inserted in a table that contains columns or `OBJECT` attributes indexed by the indextype. The new values in the indexed columns are passed in as arguments along with the corresponding row identifier.

Example 15-15 Registering ODCIIndexInsert() for Power Demand Cartridge

```
STATIC FUNCTION ODCIIndexInsert(
  ia sys.ODCIIndexInfo, 
  rid VARCHAR2, 
  newval PowerDemand_Typ, 
  env sys.ODCIEnv) 
RETURN NUMBER AS 
  cid INTEGER; 
  i BINARY_INTEGER;
  nrows INTEGER;
  stmt VARCHAR2(1000);
BEGIN 
  dbms_output.put_line(' ');
  dbms_output.put_line('ODCIIndexInsert>>>>>'||' TotGridDemand= '||
      newval.TotGridDemand ||' MaxCellDemand= '||newval.MaxCellDemand ||
      ' MinCellDemand= '||newval.MinCellDemand) ;
  sys.ODCIIndexInfoDump(ia); 
      
  -- Construct the statement.
  stmt := ' INSERT INTO '|| ia.IndexSchema || '.' || ia.IndexName || '_pidx' ||
      ' VALUES (:rr, :pos, :val)';
  
  -- Execute the statement.
  dbms_output.put_line('ODCIIndexInsert>>>>>'||stmt);
  -- Parse the statement.
  cid := dbms_sql.open_cursor;
  dbms_sql.parse(cid, stmt, dbms_sql.native);
  dbms_sql.bind_variable_rowid(cid, ':rr', rid);
      
  -- Iterate over the rows of the Varray and insert them.
  i := newval.CellDemandValues.FIRST;   
  WHILE i IS NOT NULL LOOP
    -- Bind the row into the cursor for insert.
    dbms_sql.bind_variable(cid, ':pos', i);   
    dbms_sql.bind_variable(cid, ':val', newval.CellDemandValues(i));
    -- Execute.
    nrows := dbms_sql.execute(cid);
    dbms_output.put_line('ODCIIndexInsert>>>>>('||'RID'||' , '||i|| ' , '||
           newval.CellDemandValues(i)|| ')');
    i := newval.CellDemandValues.NEXT(i);
  END LOOP;

  dbms_sql.close_cursor(cid);
  RETURN ODCICONST.SUCCESS;
END ODCIIndexInsert;
```

#### ODCIIndexDelete() Method

The [ODCIIndexDelete()](ext_idx_ref.md) function, demonstrated in Example 15-16, is called when a record is deleted from a table that contains columns or object attributes indexed by the indextype. The old values in the indexed columns are passed in as arguments along with the corresponding row identifier.

Example 15-16 Registering ODCIIndexDelete() for Power Demand Cartridge

```
STATIC FUNCTION ODCIIndexDelete(
  ia sys.ODCIIndexInfo, 
  rid VARCHAR2,
  oldval PowerDemand_Typ,
  env sys.ODCIEnv) 
RETURN NUMBER AS 
  cid INTEGER; 
  stmt VARCHAR2(1000);
  nrows INTEGER; 
BEGIN 
  dbms_output.put_line(' ');
  dbms_output.put_line('ODCIIndexDelete>>>>>'||' TotGridDemand= '||
      oldval.TotGridDemand ||' MaxCellDemand= '||oldval.MaxCellDemand ||
      ' MinCellDemand= '||oldval.MinCellDemand) ;
  sys.ODCIIndexInfoDump(ia); 
 
  -- Construct the statement.
  stmt := ' DELETE FROM '|| ia.IndexSchema || '.' ||ia.IndexName|| '_pidx' || 
      ' WHERE r=:rr';
  dbms_output.put_line('ODCIIndexDelete>>>>>'||stmt);
 
  -- Parse and execute the statement.
  cid := dbms_sql.open_cursor;
  dbms_sql.parse(cid, stmt, dbms_sql.native);
  dbms_sql.bind_variable_rowid(cid, ':rr', rid);
  nrows := dbms_sql.execute(cid);     
  dbms_sql.close_cursor(cid);
 
  RETURN ODCICONST.SUCCESS;
END ODCIIndexDelete;
```

#### ODCIIndexUpdate() Method

The [ODCIIndexUpdate()](ext_idx_ref.md) function, demonstrated in Example 15-17, is called when a record is updated in a table that contains columns or object attributes indexed by the indextype. The old and new values in the indexed columns are passed in as arguments along with the row identifier.

Example 15-17 Registering ODCIIndexUpdate() for Power Demand Cartridge

```
STATIC FUNCTION ODCIIndexUpdate(
  ia sys.ODCIIndexInfo, 
  rid VARCHAR2, 
  oldval PowerDemand_Typ, 
  newval PowerDemand_Typ, 
  env sys.ODCIEnv) 
RETURN NUMBER AS 
  cid INTEGER; 
  cid2 INTEGER; 
  stmt VARCHAR2(1000);
  stmt2 VARCHAR2(1000);
  nrows INTEGER; 
  i NUMBER;
BEGIN 
  dbms_output.put_line(' ');
  dbms_output.put_line('ODCIIndexUpdate>>>>> Old'||' TotGridDemand= '||
      oldval.TotGridDemand||' MaxCellDemand= '||oldval.MaxCellDemand ||
      ' MinCellDemand= '||oldval.MinCellDemand) ;
  dbms_output.put_line('ODCIIndexUpdate>>>>> New'||' TotGridDemand= '||
      newval.TotGridDemand ||' MaxCellDemand= '||newval.MaxCellDemand ||
      ' MinCellDemand= '||newval.MinCellDemand) ;
  sys.ODCIIndexInfoDump(ia); 

  -- Delete old entries.
  stmt := ' DELETE FROM '||ia.IndexSchema ||'.'||ia.IndexName||'_pidx'|| 
      ' WHERE r=:rr';
  dbms_output.put_line('ODCIIndexUpdate>>>>>'||stmt);
  
  -- Parse and execute the statement.
  cid := dbms_sql.open_cursor;
  dbms_sql.parse(cid, stmt, dbms_sql.native);
  dbms_sql.bind_variable_rowid(cid, ':rr', rid);
  nrows := dbms_sql.execute(cid);     
  dbms_sql.close_cursor(cid);
 
  -- Insert new entries.
  stmt2 := ' INSERT INTO '||ia.IndexSchema||'.'||ia.IndexName||'_pidx'||
      ' VALUES (:rr, :pos, :val)';
  dbms_output.put_line('ODCIIndexUpdate>>>>>'||stmt2);
 
  -- Parse and execute the statement.
  cid2 := dbms_sql.open_cursor;
  dbms_sql.parse(cid2, stmt2, dbms_sql.native);
  dbms_sql.bind_variable_rowid(cid2, ':rr', rid);
     
  -- Iterate over the rows of the Varray and insert them.
  i := newval.CellDemandValues.FIRST;   
  WHILE i IS NOT NULL LOOP
    -- Bind the row into the cursor for insert.
    dbms_sql.bind_variable(cid2, ':pos', i);   
    dbms_sql.bind_variable(cid2, ':val', newval.CellDemandValues(i));
    nrows := dbms_sql.execute(cid2);
    dbms_output.put_line('ODCIIndexUpdate>>>>>('||'RID'||' , '||i ||' , '||
         newval.CellDemandValues(i)|| ')');
    i := newval.CellDemandValues.NEXT(i);
  END LOOP;
  dbms_sql.close_cursor(cid2);
 
  RETURN ODCICONST.SUCCESS;
END ODCIIndexUpdate;
```

`ODCIIndexUpdate` is the last method defined in the `CREATE` `TYPE` `BODY` statement, which ends as follows:

```
END;
/
```

#### ODCIIndexGetMetadata() Method

The optional `ODCIIndexGetMetadata()` function, as demonstrated in Example 15-18, if present, is called by the Export utility to write implementation-specific metadata (which is not stored in the system catalogs) into the export dump file. This metadata might be policy information, version information, user settings, and so on. This metadata is written to the dump file as anonymous PL/SQL blocks that are executed at import time, immediately before the associated index is created.

This method returns strings to the Export utility that comprise the code of the PL/SQL blocks. The Export utility repeatedly calls this method until a zero-length string is returned, thus allowing the creation of any number of PL/SQL blocks of arbitrary complexity. Normally, this method calls functions within a PL/SQL package to make use of package-level variables, such as cursors and iteration counters, that maintain state across multiple calls by Export.

See Also:

[Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/toc.htm) for information about the Export and Import utilities

In the power demand cartridge, the only metadata that is passed is a version string of `V1.0`, identifying the current format of the index-organized table that underlies the domain index. The `power_pkg`.`getversion` function generates a call to the `power_pkg`.`checkversion` procedure, to be executed at import time to check that the version string is `V1.0`.

Example 15-18 Registering ODCIIndexGetMetadata() for Power Demand Cartridge

```
STATIC FUNCTION ODCIIndexGetMetadata(
  ia sys.ODCIIndexInfo, 
  expversion VARCHAR2, 
  newblock OUT PLS_INTEGER, 
  env sys.ODCIEnv) 
RETURN VARCHAR2 IS 
 
BEGIN 
  -- Let getversion do all the work since it has to maintain state across calls. 
 
  RETURN power_pkg.getversion (ia.IndexSchema, ia.IndexName, newblock); 
 
  EXCEPTION 
    WHEN OTHERS THEN 
      RAISE; 
 
END ODCIIndexGetMetaData;
```

The `power_pkg` package is defined as follows:

Example 15-19 Creating Package power\_pkg for the Power Demand Cartridge

```
CREATE OR REPLACE PACKAGE power_pkg AS  
  FUNCTION getversion(
    idxschema IN VARCHAR2, 
    idxname IN VARCHAR2,
    newblock OUT PLS_INTEGER) 
  RETURN VARCHAR2; 

  PROCEDURE checkversion (
  version IN VARCHAR2);  
END power_pkg; 
/ 
SHOW ERRORS; 
 
CREATE OR REPLACE PACKAGE BODY power_pkg AS  
  -- iterate is a package-level variable used to maintain state across calls 
  -- by Export in this session. 
  
  iterate NUMBER := 0;  
  
  FUNCTION getversion(
    idxschema IN VARCHAR2, 
    idxname IN VARCHAR2,  
    newblock OUT PLS_INTEGER) 
  RETURN VARCHAR2 IS  
  
  BEGIN  
  
  -- We are generating only one PL/SQL block consisting of one line of code.
    newblock := 1; 
  
    IF iterate = 0 THEN  
      -- Increment iterate so we'll know we're done next time we're called. 
      iterate := iterate + 1;  
  
      -- Return a string that calls checkversion with a version 'V1.0' 
      -- Note that export adds the surrounding BEGIN/END pair to form the anon. 
      -- block... we don't have to. 
  
      RETURN 'power_pkg.checkversion(''V1.0'');';  
    ELSE  
      -- reset iterate for next index  
      iterate := 0;  
      -- Return a 0-length string; we won't be called again for this index. 
      RETURN '';  
    END IF;  
  END getversion;  
  
  PROCEDURE checkversion (version IN VARCHAR2) 
  IS  
    wrong_version EXCEPTION; 
 
  BEGIN  
    IF version != 'V1.0' THEN 
      RAISE wrong_version; 
    END IF; 
  END checkversion;  

END power_pkg;
```

### Creating the Indextype

The power demand cartridge creates the indextype for the domain index. The specification, in Example 15-20, includes the list of operators supported by the indextype. It also identifies the implementation type containing the OCDI index routines.

Example 15-20 Creating Indextype power\_idxtype for Power Demand Cartridge

```
CREATE OR REPLACE INDEXTYPE power_idxtype
FOR
  Power_Equals(PowerDemand_Typ, NUMBER, NUMBER),
  Power_GreaterThan(PowerDemand_Typ, NUMBER, NUMBER),
  Power_LessThan(PowerDemand_Typ, NUMBER, NUMBER),
  Power_EqualsAny(PowerDemand_Typ, NUMBER),
  Power_GreaterThanAny(PowerDemand_Typ, NUMBER),
  Power_LessThanAny(PowerDemand_Typ, NUMBER)
USING power_idxtype_im;
```

## Defining a Type and Methods for Extensible Optimizing

This section explains the parts of the power demand cartridge as they relate to extensible optimization. Explanatory text and code segments are mixed.

### Creating the Statistics Table, PowerCartUserStats

The table `PowerCartUserStats`, demonstrated in Example 15-21, stores statistics about the hourly power grid readings. The method [ODCIStatsSelectivity()](ext_opt_ref.md) uses these statistics to estimate the selectivity of operator predicates. Because of the types of statistics collected, it is more convenient to use a separate table instead of letting Oracle store the statistics.

The `PowerCartUserStats` table contains the following columns:

- The table and column for which statistics are collected
- The cell for which the statistics are collected
- The minimum and maximum power demand for the given cell over all power grid readings
- The number of non- `null` readings for the given cell over all power grid reading

Example 15-21 Creating Statistics Table PowerCartUserStats for Power Demand Cartridge

```
CREATE TABLE PowerCartUserStats (
  -- Table for which statistics are collected
  tab VARCHAR2(30),
  -- Column for which statistics are collected
  col VARCHAR2(30),
  -- Cell position
  cpos NUMBER,
  -- Minimum power demand for the given cell
  lo NUMBER,
  -- Maximum power demand for the given cell
  hi NUMBER,
  -- Number of (non-null) power demands for the given cell
  nrows NUMBER
);
/
```

### Creating the Extensible Optimizer Methods

The power demand cartridge creates an object type that specifies methods used by the extensible optimizer. These methods are part of the `ODCIStats` interface and they collectively define the methods that are called by the methods of `DBMS_STATS` package, or when the optimizer is deciding on the best execution plan for a query.

Table 15-5 shows the method functions created for the power demand cartridge. Names of all but one of the functions begin with the string `ODCIStats`.

Table 15-5 Extensible Optimizer Methods

| Method | Description |
| --- | --- |
| [ODCIGetInterfaces()](ext_opt_ref.md) | Returns the list of names of the interfaces implemented by the type. |
| [ODCIStatsCollect()](ext_opt_ref.md) | Collects statistics for columns of type PowerDemand\_Typ or domain indexes of indextype power\_idxtype.  This method is called when a statement that refers either to a column of the `PowerDemand_Typ` type or to an index of the `power_idxtype` indextype is issued. Upon invocation, any specified options are passed in along with a description of the column or index. |
| [ODCIStatsDelete()](ext_opt_ref.md) | Deletes statistics for columns of type `PowerDemand_Typ` or domain indexes of indextype `power_idxtype`.  This method is called when a statement to delete statistics for a column of the appropriate type or an index of the appropriate indextype is issued. |
| [ODCIStatsSelectivity()](ext_opt_ref.md) | Computes the selectivity of a predicate involving an operator or its functional implementation.  Called by the optimizer when a predicate of the appropriate type appears in the `WHERE` clause of a query. |
| [ODCIStatsIndexCost()](ext_opt_ref.md) | Computes the cost of a domain index access path.  Called by the optimizer to get the cost of a domain index access path, assuming the index can be used for the query. |
| [ODCIStatsFunctionCost()](ext_opt_ref.md) | Computes the cost of a function.  Ccalled by the optimizer to get the cost of executing a function. The function need not necessarily be an implementation of an operator. |

#### Type Definition

Example 15-22 creates the `power_statistics` object type. This object type's ODCI methods are used to collect and delete statistics about columns and indexes, compute selectivities of predicates with operators or functions, and to compute costs of domain indexes and functions. The `curnum` attribute is not used.

Example 15-22 Creating power\_statistics Object Type Definition for Power Demand Cartridge

```
CREATE OR REPLACE TYPE power_statistics AS OBJECT
(
  curnum NUMBER,
  STATIC FUNCTION ODCIGetInterfaces(ifclist OUT sys.ODCIObjectList) 
    RETURN NUMBER,
  STATIC FUNCTION ODCIStatsCollect(col sys.ODCIColInfo, 
      options sys.ODCIStatsOptions, rawstats OUT RAW, env sys.ODCIEnv) 
    RETURN NUMBER,
  STATIC FUNCTION ODCIStatsDelete(col sys.ODCIColInfo, env sys.ODCIEnv) 
      RETURN NUMBER,
  STATIC FUNCTION ODCIStatsCollect(ia sys.ODCIIndexInfo,
      options sys.ODCIStatsOptions, rawstats OUT RAW, env sys.ODCIEnv) 
    RETURN NUMBER,
  STATIC FUNCTION ODCIStatsDelete(ia sys.ODCIIndexInfo, env sys.ODCIEnv) 
      RETURN NUMBER,
  STATIC FUNCTION ODCIStatsSelectivity(pred sys.ODCIPredInfo,
      sel OUT NUMBER, args sys.ODCIArgDescList, strt NUMBER, stop NUMBER,
      object PowerDemand_Typ, cell NUMBER, value NUMBER, env sys.ODCIEnv) 
    RETURN NUMBER,
  PRAGMA restrict_references(ODCIStatsSelectivity, WNDS, WNPS),
  STATIC FUNCTION ODCIStatsSelectivity(pred sys.ODCIPredInfo, sel OUT NUMBER, 
      args sys.ODCIArgDescList, strt NUMBER, stop NUMBER, object PowerDemand_Typ,
      value NUMBER, env sys.ODCIEnv) 
    RETURN NUMBER,
  PRAGMA restrict_references(ODCIStatsSelectivity, WNDS, WNPS),
  STATIC FUNCTION ODCIStatsIndexCost(ia sys.ODCIIndexInfo, sel NUMBER, 
      cost OUT sys.ODCICost, qi sys.ODCIQueryInfo, pred sys.ODCIPredInfo, 
      args sys.ODCIArgDescList, strt NUMBER, stop NUMBER, cmppos NUMBER, 
      cmpval NUMBER, env sys.ODCIEnv)
    RETURN NUMBER,
  PRAGMA restrict_references(ODCIStatsIndexCost, WNDS, WNPS),
  STATIC FUNCTION ODCIStatsIndexCost(ia sys.ODCIIndexInfo, sel NUMBER, 
      cost OUT sys.ODCICost, qi sys.ODCIQueryInfo, pred sys.ODCIPredInfo, 
      args sys.ODCIArgDescList, strt NUMBER, stop NUMBER, cmpval NUMBER, 
      env sys.ODCIEnv) 
    RETURN NUMBER,
  PRAGMA restrict_references(ODCIStatsIndexCost, WNDS, WNPS),
  STATIC FUNCTION ODCIStatsFunctionCost(func sys.ODCIFuncInfo, 
      cost OUT sys.ODCICost, args sys.ODCIArgDescList, object PowerDemand_Typ,
      cell NUMBER, value NUMBER, env sys.ODCIEnv) 
    RETURN NUMBER,
  PRAGMA restrict_references(ODCIStatsFunctionCost, WNDS, WNPS),
  STATIC FUNCTION ODCIStatsFunctionCost(func sys.ODCIFuncInfo,
      cost OUT sys.ODCICost, args sys.ODCIArgDescList, object PowerDemand_Typ,
      value NUMBER, env sys.ODCIEnv) 
    RETURN NUMBER,
  PRAGMA restrict_references(ODCIStatsFunctionCost, WNDS, WNPS)
  STATIC FUNCTION ODCIStatsFunctionCost(func sys.ODCIFuncInfo,
      cost OUT sys.ODCICost, args sys.ODCIArgDescList, object PowerDemand_Typ,
      cell NUMBER, value NUMBER, env sys.ODCIEnv)
    RETURN NUMBER
);
/
```

The `CREATE TYPE` statement is followed by a `CREATE TYPE BODY` statement that specifies the implementation for each member function:

```
CREATE OR REPLACE TYPE BODY power_statistics
IS
...
```

Each member function is described in a separate section, but the function definitions have the following general form:

```
STATIC FUNCTION function-name (...)
  BEGIN
    RETURN NUMBER IS
  END;
```

#### ODCIGetInterfaces() Method

The [ODCIGetInterfaces()](ext_opt_ref.md) function, demonstrated in Example 15-23, returns the list of names of the interfaces implemented by the type. There is only one set of the extensible optimizer interface routines, called `SYS.ODCISTATS`, but the server supports multiple versions of them for backward compatibility. To specify the current version of the routines, function [ODCIGetInterfaces()](ext_opt_ref.md) must specify `SYS.ODCISTATS2` in the `OUT`, `ODCIObjectList` parameter.

Example 15-23 Registering interfaces and Statistics Functions for Power Demand Cartridge

```
STATIC FUNCTION ODCIGetInterfaces(
  ifclist OUT sys.ODCIObjectList)
RETURN NUMBER IS
BEGIN
  ifclist := sys.ODCIObjectList(sys.ODCIObject('SYS','ODCISTATS2'));
  RETURN ODCIConst.Success;
END ODCIGetInterfaces;
```

#### ODCIStatsCollect() Method for PowerDemand\_Typ Columns

The [ODCIStatsCollect()](ext_opt_ref.md) function, demonstrated in Example 15-24, collects statistics for columns whose data type is the `PowerDemand_Typ` object type. The statistics are collected for each cell in the column over all power grid readings. For a given cell, the statistics collected are the minimum and maximum power grid readings, and the number of non-null readings.

The function takes the column information as an object parameter whose type is `SYS.ODCICOLINFO`. The type attributes include the table name, column name, and so on. Options specified in the `DBMS_STATS` package command used to collect the column statistics are also passed in as parameters. Since the power demand cartridge uses a table to store the statistics, the output parameter `rawstats` is not used in this cartridge.

Example 15-24 Registering ODCIStatsCollect() for Power Demand Cartridge

```
STATIC FUNCTION ODCIStatsCollect(
  col sys.ODCIColInfo,
  options sys.ODCIStatsOptions,
  rawstats OUT RAW, 
  env sys.ODCIEnv)
RETURN NUMBER IS
  cnum                INTEGER;
  stmt                VARCHAR2(1000);
  junk                INTEGER;
  cval                NUMBER;
  colname             VARCHAR2(30) := rtrim(ltrim(col.colName, '"'), '"');
  statsexists         BOOLEAN := FALSE;
  pdemands            PowerDemand_Tab%ROWTYPE;
  user_defined_stats  PowerCartUserStats%ROWTYPE;

  CURSOR c1(tname VARCHAR2, cname VARCHAR2) IS
    SELECT * FROM PowerCartUserStats
    WHERE tab = tname AND col = cname;
  CURSOR c2 IS
    SELECT * FROM PowerDemand_Tab;

  BEGIN
    sys.ODCIColInfoDump(col);
    sys.ODCIStatsOptionsDump(options);

    IF (col.TableSchema IS NULL OR col.TableName IS NULL OR col.ColName IS NULL)
    THEN
      RETURN ODCIConst.Error;
    END IF;

    dbms_output.put_line('ODCIStatsCollect>>>>>');
    dbms_output.put_line('**** Analyzing column '||col.TableSchema|| '.' ||
        col.TableName|| '.' || col.ColName);

    -- Check if statistics exist for this column
    FOR user_defined_stats IN c1(col.TableName, colname) LOOP
      statsexists := TRUE;
      EXIT;
    END LOOP;
```

The function checks whether statistics for this column exist. If so, it initializes them to `NULL`; otherwise, it creates statistics for each of the 100 cells and initializes them to `NULL`.

```
IF not statsexists THEN
  -- column statistics don't exist; create entries for each of the 100 cells
  cnum := dbms_sql.open_cursor;
  FOR i in 1..100 LOOP
    stmt := 'INSERT INTO PowerCartUserStats VALUES( '||''''|| col.TableName ||
        ''', '||''''||colname||''', '||to_char(i)||', '||'NULL, NULL, NULL)';
    dbms_sql.parse(cnum, stmt, dbms_sql.native);
    junk := dbms_sql.execute(cnum);
  END LOOP;
  dbms_sql.close_cursor(cnum);
ELSE
  -- column statistics exist; initialize to NULL
  cnum := dbms_sql.open_cursor;
  stmt := 'UPDATE PowerCartUserStats'||
      ' SET lo = NULL, hi = NULL, nrows = NULL'||' WHERE tab = '||
      col.TableName||' AND col = '||colname;
  dbms_sql.parse(cnum, stmt, dbms_sql.native);
  junk := dbms_sql.execute(cnum);
  dbms_sql.close_cursor(cnum);
END IF;
```

The function collects statistics for the column by reading rows from the table that is being analyzed. This is done by constructing and executing a SQL statement.

```
-- For each cell position, the following statistics are collected:
--   maximum value
--   minimum value
--   number of rows (excluding NULLs)
cnum := dbms_sql.open_cursor;
FOR i in 1..100 LOOP
  FOR pdemands IN c2 LOOP
    IF i BETWEEN pdemands.sample.CellDemandValues.FIRST AND
        pdemands.sample.CellDemandValues.LAST THEN
      cval := pdemands.sample.CellDemandValues(i);
      stmt := 'UPDATE PowerCartUserStats SET '|| 'lo = least(' || 'NVL(' ||
          to_char(cval)||', lo), '||'NVL('||'lo, '||to_char(cval)||')), '||
          'hi = greatest('||'NVL('||to_char(cval)||', hi), '||'NVL('||
          'hi, '||to_char(cval)||')), '||
          'nrows = decode(nrows, NULL, decode('||to_char(cval)||
          ', NULL, NULL, 1), decode('||to_char(cval)|| 
          ', NULL, nrows, nrows+1)) '||'WHERE cpos = '||to_char(i)||
          ' AND tab = '''||col.TableName||''''||' AND col = '''||colname||
          '''';
      dbms_sql.parse(cnum, stmt, dbms_sql.native);
      junk := dbms_sql.execute(cnum);
    END IF;
  END LOOP;
END LOOP;
```

The function concludes by closing the cursor and returning a success status.

```
dbms_sql.close_cursor(cnum);
  rawstats := NULL;
  return ODCIConst.Success;

END ODCIStatsCollect;
```

#### ODCIStatsDelete() Method for PowerDemand\_Typ Columns

The [ODCIStatsDelete()](ext_opt_ref.md) function, demonstrated in Example 15-25, deletes statistics of columns whose data type is the `PowerDemand_Typ` object type. The function takes the column information as an object parameter whose type is `SYS.ODCICOLINFO`. The type attributes include the table name, column name, and so on.

Example 15-25 Registering ODCIStatsDelete() for Power Demand Cartridge

```
STATIC FUNCTION ODCIStatsDelete(
  col sys.ODCIColInfo, 
  env sys.ODCIEnv)
RETURN NUMBER IS
  cnum                INTEGER;
  stmt                VARCHAR2(1000);
  junk                INTEGER;
  colname             VARCHAR2(30) := rtrim(ltrim(col.colName, '"'), '"');
  statsexists         BOOLEAN := FALSE;
  user_defined_stats  PowerCartUserStats%ROWTYPE;

  CURSOR c1(tname VARCHAR2, cname VARCHAR2) IS
    SELECT * FROM PowerCartUserStats
    WHERE tab = tname AND col = cname;
  BEGIN
  sys.ODCIColInfoDump(col);

  IF (col.TableSchema IS NULL OR col.TableName IS NULL OR col.ColName IS NULL)
  THEN
    RETURN ODCIConst.Error;
  END IF;

  dbms_output.put_line('ODCIStatsDelete>>>>>');
  dbms_output.put_line('**** Analyzing (delete) column '|| col.TableSchema|| 
      '.' ||col.TableName||'.'||col.ColName);
```

The function verifies that statistics for the column exist by checking the statistics table. If statistics were not collected, then there is nothing to be done. If, however, statistics are present, it constructs and executes a SQL statement to delete the relevant rows from the statistics table.

```
-- Check if statistics exist for this column
  FOR user_defined_stats IN c1(col.TableName, colname) LOOP
    statsexists := TRUE;
    EXIT;
  END LOOP;

  -- If user-defined statistics exist, delete them
  IF statsexists THEN
    stmt := 'DELETE FROM PowerCartUserStats'||' WHERE tab = '''||col.TableName||
        ''''|| ' AND col = ''' || colname || '''';
    cnum := dbms_sql.open_cursor;
    dbms_output.put_line('ODCIStatsDelete>>>>>');
    dbms_output.put_line('ODCIStatsDelete>>>>>' || stmt);
    dbms_sql.parse(cnum, stmt, dbms_sql.native);
    junk := dbms_sql.execute(cnum);
    dbms_sql.close_cursor(cnum);
  END IF;

  RETURN ODCIConst.Success;
END ODCStatsDelete;
```

#### ODCIStatsCollect() Method for power\_idxtype Domain Indexes

The [ODCIStatsCollect()](ext_opt_ref.md) function, demonstrated in Example 15-26, collects statistics for domain indexes whose indextype is `power_idxtype`. In the power demand cartridge, this function simply analyzes the index-organized table that stores the index data.

The function takes the index information as an object parameter whose type is `SYS.ODCIINDEXINFO`. The type attributes include the index name, owner name, and so on. Options specified by the `DBMS_STATS` package are used to collect the index statistics are also passed in as parameters. The output parameter `rawstats` is not used.

Example 15-26 Registering ODCIStatsCollect() for Power Demand Cartridge

```
STATIC FUNCTION ODCIStatsCollect (
  ia sys.ODCIIndexInfo,
  options sys.ODCIStatsOptions, 
  rawstats OUT RAW, 
  env sys.ODCIEnv)
RETURN NUMBER IS
  stmt                VARCHAR2(1000);
 
BEGIN
  -- To analyze a domain index, analyze the table that implements the index
  sys.ODCIIndexInfoDump(ia);
  sys.ODCIStatsOptionsDump(options);

  stmt := 'dbms_stats.gather_table_stats('
         || '''' || ia.IndexSchema || ''', '
         || '''' || ia.IndexName || '_pidx' || ''');';
  dbms_output.put_line('**** Analyzing index '
         || ia.IndexSchema || '.' || ia.IndexName);
  dbms_output.put_line('SQL Statement: ' || stmt); 
  EXECUTE IMMEDIATE 'BEGIN ' || stmt || ' END;';
  rawstats := NULL;

  RETURN ODCIConst.Success;
END ODCIStatsCollect;
```

#### ODCIStatsDelete() Method for power\_idxtype Domain Indexes

The [ODCIStatsDelete()](ext_opt_ref.md) function, demonstrated in Example 15-27, deletes statistics for domain indexes whose indextype is `power_idxtype`. In the power demand cartridge, this function simply deletes the statistics of the index-organized table that stores the index data.

The function takes the index information as an object parameter whose type is `SYS.ODCIINDEXINFO`. The type attributes include the index name, owner name, and so on.

Example 15-27 Registering ODCIStatsDelete() for Domain Indexes in Power Demand Cartridge

```
STATIC FUNCTION ODCIStatsDelete(
  ia sys.ODCIIndexInfo,
  env sys.ODCIEnv)
RETURN NUMBER IS
  stmt                VARCHAR2(1000);
BEGIN
  -- To delete statistics for a domain index, delete the statistics for the
  -- table implementing the index
  sys.ODCIIndexInfoDump(ia);
  stmt := 'dbms_stats.delete_table_stats('|| '''' || ia.IndexSchema || ''', '
      || '''' || ia.IndexName || '_pidx' || ''');';
  dbms_output.put_line('**** Analyzing (delete) index '||ia.IndexSchema||'.'||
      ia.IndexName);
  dbms_output.put_line('SQL Statement: ' || stmt);

  EXECUTE IMMEDIATE 'BEGIN ' || stmt || ' END;';
  RETURN ODCIConst.Success;
END ODCIStatsDelete;
```

#### ODCIStatsSelectivity() Method for Specific Queries

The first definition of the [ODCIStatsSelectivity()](ext_opt_ref.md) function estimates the selectivity of operator or function predicates for `Specific` queries. For example, if a query asks for all instances where cell `(3,7)` has a value equal to `25`, the function estimates the percentage of rows in which the given cell has the specified value.

The `pred` parameter contains the function information (the functional implementation of an operator in an operator predicate); this parameter is an object instance of type `SYS.ODCIPREDINFO`. The selectivity is returned as a percentage in the `sel` output parameter. The `args` parameter (an object instance of type `SYS.ODCIARGDESCLIST`) contains a descriptor for each argument of the function, and the start and stop values of the function. For example, if an argument is a column, the argument descriptor contains the table name, column name, and so on. The `strt` and `stop` parameters are the lower and upper boundary points for the function return value. If the function in a predicate contains a literal of type `PowerDemand_Typ`, the `object` parameter contains the value in the form of an object constructor. The `cell` parameter is the cell position and the `value` parameter is the value in the cell specified by the function (`PowerXxxxxSpecific_Func`).

The selectivity is estimated by using a technique similar to that used for simple range predicates. For example, a simple estimate for the selectivity of a predicate like

```
c > v
```

is `(M-v)/(M-m)` where `m` and `M` are the minimum and maximum values, respectively, for the column `c` (as determined from the column statistics), provided the value `v` lies between `m` and `M`.

The `get_selectivity` function, demonstrated in Example 15-28, computes the selectivity of a simple range predicate given the minimum and maximum values of the column in the predicate. It assumes that the column values in the table are uniformly distributed between the minimum and maximum values.

Example 15-28 Implementing Selectivity Function for Power Demand Cartridge

```
CREATE FUNCTION get_selectivity(relop VARCHAR2, value NUMBER,
                                lo NUMBER, hi NUMBER, ndv NUMBER)
  RETURN NUMBER AS
  sel NUMBER := NULL;
  ndv NUMBER;
BEGIN
  -- This function computes the selectivity (as a percentage)
  -- of a predicate
  --             col <relop> <value>
  -- where <relop> is one of: =, !=, <, <=, >, >=
  --       <value> is one of: 0, 1
  -- lo and hi are the minimum and maximum values of the column in
  -- the table. This function performs a simplistic estimation of the
  -- selectivity by assuming that the range of distinct values of
  -- the column is distributed uniformly in the range lo..hi and that
  -- each distinct value occurs nrows/(hi-lo+1) times (where nrows is
  -- the number of rows).

  IF ndv IS NULL OR ndv <= 0 THEN
    RETURN 0;
  END IF;

  -- col != <value>
  IF relop = '!=' THEN
    IF value between lo and hi THEN
      sel := 1 - 1/ndv;
    ELSE
      sel := 1;
    END IF;

  -- col = <value>
  ELSIF relop = '=' THEN
    IF value between lo and hi THEN
      sel := 1/ndv;
    ELSE
      sel := 0;
    END IF;

  -- col >= <value>
  ELSIF relop = '>=' THEN
    IF lo = hi THEN
      IF value <= lo THEN
        sel := 1;
      ELSE
        sel := 0;
      END IF;
    ELSIF value between lo and hi THEN
      sel := (hi-value)/(hi-lo) + 1/ndv;
    ELSIF value < lo THEN
      sel := 1;
    ELSE
      sel := 0;
    END IF;

  -- col < <value>
  ELSIF relop = '<' THEN
    IF lo = hi THEN
      IF value > lo THEN
        sel := 1;
      ELSE
        sel := 0;
      END IF;
    ELSIF value between lo and hi THEN
      sel := (value-lo)/(hi-lo);
    ELSIF value < lo THEN
      sel := 0;
    ELSE
      sel := 1;
    END IF;

  -- col <= <value>
  ELSIF relop = '<=' THEN
    IF lo = hi THEN
      IF value >= lo THEN
        sel := 1;
      ELSE
        sel := 0;
      END IF;
    ELSIF value between lo and hi THEN
      sel := (value-lo)/(hi-lo) + 1/ndv;
    ELSIF value < lo THEN
      sel := 0;
    ELSE
      sel := 1;
    END IF;

  -- col > <value>
  ELSIF relop = '>' THEN
    IF lo = hi THEN
      IF value < lo THEN
        sel := 1;
      ELSE
        sel := 0;
      END IF;
    ELSIF value between lo and hi THEN
      sel := (hi-value)/(hi-lo);
    ELSIF value < lo THEN
      sel := 1;
    ELSE
      sel := 0;
    END IF;

  END IF;

  RETURN least(100, ceil(100*sel));

END;
/
```

The [ODCIStatsSelectivity()](ext_opt_ref.md) function, demonstrated in Example 15-29, estimates the selectivity for function predicates which have constant start and stop values. Further, the first argument of the function in the predicate must be a column of type `PowerDemand_Typ` and the remaining arguments must be constants.

Example 15-29 Registering ODCIStatsSelectivity() for Queries for Power Demand Cartridge

```
STATIC FUNCTION ODCIStatsSelectivity(pred sys.ODCIPredInfo,
   sel OUT NUMBER, args sys.ODCIArgDescList, strt NUMBER, stop NUMBER,
   object PowerDemand_Typ, cell NUMBER, value NUMBER, env sys.ODCIEnv)
   RETURN NUMBER IS
   fname               varchar2(30);
   relop               varchar2(2);
   lo                  NUMBER;
   hi                  NUMBER;
   nrows               NUMBER;
   colname             VARCHAR2(30);
   statsexists         BOOLEAN := FALSE;
   stats               PowerCartUserStats%ROWTYPE;
   CURSOR c1(cell NUMBER, tname VARCHAR2, cname VARCHAR2) IS
     SELECT * FROM PowerCartUserStats
     WHERE cpos = cell
       AND tab = tname
       AND col = cname;
BEGIN
  -- compute selectivity only when predicate is of the form:
  --      fn(col, <cell>, <value>) <relop> <val>
  -- In all other cases, return an error and let the optimizer
  -- make a guess. We also assume that the function "fn" has
  -- a return value of 0, 1, or NULL.

  -- start value
  IF (args(1).ArgType != ODCIConst.ArgLit AND
      args(1).ArgType != ODCIConst.ArgNull) THEN
    RETURN ODCIConst.Error;
  END IF;

  -- stop value
  IF (args(2).ArgType != ODCIConst.ArgLit AND
      args(2).ArgType != ODCIConst.ArgNull) THEN
    RETURN ODCIConst.Error;
  END IF;

  -- first argument of function
  IF (args(3).ArgType != ODCIConst.ArgCol) THEN
    RETURN ODCIConst.Error;
  END IF;

  -- second argument of function
  IF (args(4).ArgType != ODCIConst.ArgLit AND
      args(4).ArgType != ODCIConst.ArgNull) THEN
    RETURN ODCIConst.Error;
  END IF;

  -- third argument of function
  IF (args(5).ArgType != ODCIConst.ArgLit AND
      args(5).ArgType != ODCIConst.ArgNull) THEN
    RETURN ODCIConst.Error;
  END IF;

  colname := rtrim(ltrim(args(3).colName, '"'), '"');
```

The first (column) argument of the function in the predicate must have statistics collected for it. If statistics have not been collected, [ODCIStatsSelectivity()](ext_opt_ref.md) returns an error status.

```
-- Check if the statistics table exists (we are using a
-- user-defined table to store the user-defined statistics).
-- Get user-defined statistics: MIN, MAX, NROWS
FOR stats IN c1(cell, args(3).TableName, colname) LOOP
  -- Get user-defined statistics: MIN, MAX, NROWS
  lo := stats.lo;
  hi := stats.hi;
  nrows := stats.nrows;
  statsexists := TRUE;
  EXIT;
END LOOP;

-- If no user-defined statistics were collected, return error
IF not statsexists THEN
  RETURN ODCIConst.Error;
END IF;
```

Each `Specific` function predicate corresponds to an equivalent range predicate. For example, the predicate `Power_EqualsSpecific_Func(col, 21, 25) = 0`, which checks that the reading in cell `21` is not equal to `25`, corresponds to the equivalent range predicate `col[21] != 25`.

The [ODCIStatsSelectivity()](ext_opt_ref.md) function finds the corresponding range predicates for each `Specific` function predicate. There are several boundary cases where the selectivity can be immediately determined.

```
-- selectivity is 0 for "fn(col, <cell>, <value>) < 0"
IF (stop = 0 AND
    bitand(pred.Flags, ODCIConst.PredIncludeStop) = 0) THEN
  sel := 0;
  RETURN ODCIConst.Success;
END IF;

-- selectivity is 0 for "fn(col, <cell>, <value>) > 1"
IF (strt = 1 AND
    bitand(pred.Flags, ODCIConst.PredIncludeStart) = 0) THEN
  sel := 0;
  RETURN ODCIConst.Success;
END IF;

-- selectivity is 100% for "fn(col, <cell>, <value>) >= 0"
IF (strt = 0 AND
    bitand(pred.Flags, ODCIConst.PredExactMatch) = 0 AND
    bitand(pred.Flags, ODCIConst.PredIncludeStart) > 0) THEN
  sel := 100;
  RETURN ODCIConst.Success;
END IF;

-- selectivity is 100% for "fn(col, <cell>, <value>) <= 1"
IF (stop = 1 AND
    bitand(pred.Flags, ODCIConst.PredExactMatch) = 0 AND
    bitand(pred.Flags, ODCIConst.PredIncludeStop) > 0) THEN
  sel := 100;
  RETURN ODCIConst.Success;
END IF;

-- get function name
IF bitand(pred.Flags, ODCIConst.PredObjectFunc) > 0 THEN
  fname := pred.ObjectName;
ELSE
  fname := pred.MethodName;
END IF;

-- convert prefix relational operator to infix:
-- "Power_EqualsSpecific_Func(col, <cell>, <value>) = 1"
-- becomes "col[<cell>] = <value>"

--   Power_EqualsSpecific_Func(col, <cell>, <value>) = 0
--   Power_EqualsSpecific_Func(col, <cell>, <value>) <= 0
--   Power_EqualsSpecific_Func(col, <cell>, <value>) < 1
-- can be transformed to
--   col[<cell>] != <value>
IF (fname LIKE upper('Power_Equals%') AND
    (stop = 0 OR
     (stop = 1 AND
      bitand(pred.Flags, ODCIConst.PredIncludeStop) = 0))) THEN
  relop := '!=';

--   Power_LessThanSpecific_Func(col, <cell>, <value>) = 0
--   Power_LessThanSpecific_Func(col, <cell>, <value>) <= 0
--   Power_LessThanSpecific_Func(col, <cell>, <value>) < 1
-- can be transformed to
--   col[<cell>] >= <value>
ELSIF (fname LIKE upper('Power_LessThan%') AND
       (stop = 0 OR
        (stop = 1 AND
         bitand(pred.Flags, ODCIConst.PredIncludeStop) = 0))) THEN
  relop := '>=';

--   Power_GreaterThanSpecific_Func(col, <cell>, <value>) = 0
--   Power_GreaterThanSpecific_Func(col, <cell>, <value>) <= 0
--   Power_GreaterThanSpecific_Func(col, <cell>, <value>) < 1
-- can be transformed to
--   col[<cell>] <= <value>
ELSIF (fname LIKE upper('Power_GreaterThan%') AND
       (stop = 0 OR
        (stop = 1 AND
         bitand(pred.Flags, ODCIConst.PredIncludeStop) = 0))) THEN
  relop := '<=';

--   Power_EqualsSpecific_Func(col, <cell>, <value>) = 1
--   Power_EqualsSpecific_Func(col, <cell>, <value>) >= 1
--   Power_EqualsSpecific_Func(col, <cell>, <value>) > 0
-- can be transformed to
--   col[<cell>] = <value>
ELSIF (fname LIKE upper('Power_Equals%') AND
       (strt = 1 OR
        (strt = 0 AND
         bitand(pred.Flags, ODCIConst.PredIncludeStart) = 0))) THEN
  relop := '=';

--   Power_LessThanSpecific_Func(col, <cell>, <value>) = 1
--   Power_LessThanSpecific_Func(col, <cell>, <value>) >= 1
--   Power_LessThanSpecific_Func(col, <cell>, <value>) > 0
-- can be transformed to
--   col[<cell>] < <value>
ELSIF (fname LIKE upper('Power_LessThan%') AND
       (strt = 1 OR
        (strt = 0 AND
         bitand(pred.Flags, ODCIConst.PredIncludeStart) = 0))) THEN
  relop := '<';

--   Power_GreaterThanSpecific_Func(col, <cell>, <value>) = 1
--   Power_GreaterThanSpecific_Func(col, <cell>, <value>) >= 1
--   Power_GreaterThanSpecific_Func(col, <cell>, <value>) > 0
-- can be transformed to
--   col[<cell>] > <value>
ELSIF (fname LIKE upper('Power_GreaterThan%') AND
       (strt = 1 OR
        (strt = 0 AND
         bitand(pred.Flags, ODCIConst.PredIncludeStart) = 0))) THEN
  relop := '>';

ELSE
  RETURN ODCIConst.Error;

END IF;
```

After the `Specific` function predicate is transformed into a simple range predicate, [ODCIStatsSelectivity()](ext_opt_ref.md) calls `get_selectivity` to compute the selectivity for the range predicate (and thus, equivalently, for the `Specific` function predicate). It returns with a success status.

```
sel := get_selectivity(relop, value, lo, hi, nrows);
  RETURN ODCIConst.Success;
END;
```

#### ODCIStatsIndexCost() Method for Specific Queries

The first definition of the [ODCIStatsIndexCost()](ext_opt_ref.md) function, demonstrated in Example 15-30, estimates the cost of the domain index for `Specific` queries. For example, if a query asks for all instances where cell `(3,7)` has a value equal to `25`, the function estimates the cost of the domain index access path to evaluate this query. This definition of [ODCIStatsIndexCost()](ext_opt_ref.md) differs from the definition insection "ODCIStatsIndexCost() Method for Any Queries" in that it includes the `cmppos` parameter for the position of the cell.

The `ia` parameter contains the index information as an object instance of type `SYS.ODCIINDEXINFO`. The `sel` parameter is the selectivity of the operator predicate as estimated by the [ODCIStatsSelectivity()](ext_opt_ref.md) function for `Specific` queries. The estimated cost is returned in the `cost` output parameter. The `qi` parameter contains some information about the query and its environment, such as whether the `ALL_ROWS` or `FIRST_ROWS` optimizer mode is being used. The `pred` parameter contains the operator information as an object instance of type `SYS.ODCIPREDINFO`. The `args` parameter contains descriptors of the value arguments of the operator, and the start and stop values of the operator. The `strt` and `stop` parameters are the lower and upper boundary points for the operator return value. The `cmppos` parameter is the cell position and `cmpval` is the value in the cell specified by the operator `Power_XxxxxSpecific()`.

In the power demand cartridge, the domain index cost for `Specific` queries is identical to the domain index cost for `Any` queries, so this version of the [ODCIStatsIndexCost()](ext_opt_ref.md) function simply calls the second definition of the function, described in section "ODCIStatsIndexCost() Method for Any Queries".

Example 15-30 Registering ODCISIndexCost() for Queries for Power Demand Cartridge

```
STATIC FUNCTION ODCIStatsIndexCost(ia sys.ODCIIndexInfo,
   sel NUMBER, cost OUT sys.ODCICost, qi sys.ODCIQueryInfo,
   pred sys.ODCIPredInfo, args sys.ODCIArgDescList,
   strt NUMBER, stop NUMBER, cmppos NUMBER, cmpval NUMBER, env sys.ODCIEnv)
   RETURN NUMBER IS
BEGIN
  -- This is the cost for queries on a specific cell; simply
  -- use the cost for queries on any cell.
  RETURN ODCIStatsIndexCost(ia, sel, cost, qi, pred, args,
                            strt, stop, cmpval, env);
END;
```

#### ODCIStatsIndexCost() Method for Any Queries

The second definition of the [ODCIStatsIndexCost()](ext_opt_ref.md) function, demonstrated in Example 15-31, estimates the cost of the domain index for `Any` queries. For example, if a query asks for all instances where any cell has a value equal to 25, the function estimates the cost of the domain index access path to evaluate this query. This definition of [ODCIStatsIndexCost()](ext_opt_ref.md) differs from the definition in section "ODCIStatsIndexCost() Method for Specific Queries" in that it does not include the `cmppos` parameter.

The `ia` parameter contains the index information as an object instance of type `SYS.ODCIINDEXINFO`. The `sel` parameter is the selectivity of the operator predicate as estimated by the [ODCIStatsSelectivity()](ext_opt_ref.md) function for `Any` queries. The estimated cost is returned in the `cost` output parameter. The `qi` parameter contains some information about the query and its environment, such as whether the `ALL_ROWS` or `FIRST_ROWS` optimizer mode is being used. The `pred` parameter contains the operator information as an object instance of type `SYS.ODCIPREDINFO`. The `args` parameter contains descriptors of the value arguments of the operator, and the start and stop values of the operator. The `strt` and `stop` parameters are the lower and upper boundary points for the operator return value. The `cmpval` parameter is the value in the cell specified by the operator `Power_XxxxxAny()`.

The index cost is estimated as the number of blocks in the index-organized table implementing the index multiplied by the selectivity of the operator predicate times a constant factor.

Example 15-31 Registering ODCIStatsIndexCost() for Any Queries for Power Demand Cartridge

```
STATIC FUNCTION ODCIStatsIndexCost(ia sys.ODCIIndexInfo,
   sel NUMBER, cost OUT sys.ODCICost, qi sys.ODCIQueryInfo,
   pred sys.ODCIPredInfo, args sys.ODCIArgDescList,
   strt NUMBER, stop NUMBER, cmpval NUMBER, env sys.ODCIEnv)
   RETURN NUMBER IS
   ixtable             VARCHAR2(40);
   numblocks           NUMBER := NULL;
   get_table           user_tables%ROWTYPE;
   CURSOR c1(tab VARCHAR2) IS
     SELECT * FROM user_tables WHERE table_name = tab;
BEGIN
  -- This is the cost for queries on any cell.

  -- To compute the cost of a domain index, multiply the
  -- number of blocks in the table implementing the index
  -- with the selectivity

  -- Return if we don't have predicate selectivity
  IF sel IS NULL THEN
    RETURN ODCIConst.Error;
  END IF;

  cost := sys.ODCICost(NULL, NULL, NULL, NULL);

  -- Get name of table implementing the domain index
  ixtable := ia.IndexName || '_pidx';

  -- Get number of blocks in domain index
  FOR get_table IN c1(upper(ixtable)) LOOP
    numblocks := get_table.blocks;
    EXIT;
  END LOOP;

  IF numblocks IS NULL THEN
    -- Exit if there are no user-defined statistics for the index
    RETURN ODCIConst.Error;
  END IF;

  cost.CPUCost := ceil(400*(sel/100)*numblocks);
  cost.IOCost := ceil(1.5*(sel/100)*numblocks);
  RETURN ODCIConst.Success;
END;
```

#### ODCIStatsFunctionCost() Method

The [ODCIStatsFunctionCost()](ext_opt_ref.md) function, demonstrated in Example 15-32, estimates the cost of evaluating a function `Power_XxxxxSpecific_Func()` or `Power_XxxxxAny_Func()`.

The `func` parameter contains the function information; this parameter is an object instance of type `SYS.ODCIFUNCINFO`. The estimated cost is returned in the output `cost` parameter. The `args` parameter as an object instance of type `SYS.ODCIARGDESCLIST` contains a descriptor for each argument of the function. If the function contains a literal of type `PowerDemand_Typ` as its first argument, the `object` parameter contains the value in the form of an object constructor. The `value` parameter is the value in the cell specified by the function `PowerXxxxxSpecific_Func()` or `Power_XxxxxAny_Func()`.

The function cost is simply estimated as some default value depending on the function name. Since the functions do not read any data from disk, the I/O cost is set to zero.

Example 15-32 Registering ODCIStatsFunctionCost() for Power Demand Cartridge

```
STATIC FUNCTION ODCIStatsFunctionCost(func sys.ODCIFuncInfo,
   cost OUT sys.ODCICost, args sys.ODCIArgDescList,
   object PowerDemand_Typ, value NUMBER, env sys.ODCIEnv)
   RETURN NUMBER IS
   fname               VARCHAR2(30);
BEGIN
  cost := sys.ODCICost(NULL, NULL, NULL, NULL);

  -- Get function name
  IF  bitand(func.Flags, ODCIConst.ObjectFunc) > 0 THEN
    fname := func.ObjectName;
  ELSE
    fname := func.MethodName;
  END IF;

  IF fname LIKE upper('Power_LessThan%') THEN
    cost.CPUCost := 5000;
    cost.IOCost := 0;
    RETURN ODCIConst.Success;
  ELSIF fname LIKE upper('Power_Equals%') THEN
    cost.CPUCost := 7000;
    cost.IOCost := 0;
    RETURN ODCIConst.Success;
  ELSIF fname LIKE upper('Power_GreaterThan%') THEN
    cost.CPUCost := 5000;
    cost.IOCost := 0;
    RETURN ODCIConst.Success;
  ELSE
    RETURN ODCIConst.Error;
  END IF;
END;
```

### Associating the Extensible Optimizer Methods with Database Objects

In order for the optimizer to use the methods defined in the `power_statistics` object type, they have to be associated with the appropriate database objects, as demonstrated in Example 15-33.

Example 15-33 Using Statistics Methods with Database Objects for Power Demand Cartridge

```
Associate statistics type with types, indextypes, and functions
ASSOCIATE STATISTICS WITH TYPES PowerDemand_Typ USING power_statistics;
ASSOCIATE STATISTICS WITH INDEXTYPES power_idxtype USING power_statistics
  WITH SYSTEM MANAGED STORAGE TABLES;
ASSOCIATE STATISTICS WITH FUNCTIONS
  Power_EqualsSpecific_Func,
  Power_GreaterThanSpecific_Func,
  Power_LessThanSpecific_Func,
  Power_EqualsAny_Func,
  Power_GreaterThanAny_Func,
  Power_LessThanAny_Func
  USING power_statistics;
```

### Analyzing the Database Objects

Analyzing tables, columns, and indexes ensures that the optimizer has the relevant statistics to estimate accurate costs for various access paths and choose a good plan. Further, the selectivity and cost functions defined in the `power_statistics` object type rely on the presence of statistics. Example 15-34 demonstrates statements that analyze the database objects and verify that statistics were indeed collected.

Example 15-34 Analyzing Database Objects for the Power Demand Cartridge

```
-- Analyze the table
EXECUTE dbms_stats.gather_table_stats(
    'POWERCARTUSER', 'POWERDEMAND_TAB', cascade => TRUE);

-- Verify that user-defined statistics were collected
SELECT tab tablename, col colname, cpos, lo, hi, nrows
FROM PowerCartUserStats
WHERE nrows IS NOT NULL
ORDER BY cpos;

-- Delete the statistics
EXECUTE dbms_stats.delete_table_stats('POWERCARTUSER', 'POWERDEMAND_TAB');

-- Verify that user-defined statistics were deleted
SELECT tab tablename, col colname, cpos, lo, hi, nrows
FROM PowerCartUserStats
WHERE nrows IS NOT NULL
ORDER BY cpos;

-- Re-analyze the table
EXECUTE dbms_stats.gather_table_stats(
   'POWERCARTUSER', 'POWERDEMAND_TAB',cascade => TRUE);

-- Verify that user-defined statistics were re-collected
SELECT tab tablename, col colname, cpos, lo, hi, nrows
FROM PowerCartUserStats
WHERE nrows IS NOT NULL
ORDER BY cpos;
```

## Testing the Domain Index

This section explains the parts of the power demand example that perform some simple tests of the domain index, and how to test the domain index and see if it is causing more efficient execution of queries than would occur without an index. These tests consist of:

- Creating the power demand table (`PowerDemand_Tab`) and populating it with a small amount of data
- Executing some queries before the index is created (and showing the execution plans without an index being used)
	The execution plans show that a full table scan is performed in each case.
- Creating the index on the grid
- Executing the same queries after the index is created (and showing the execution plans with the index being used)
	The execution plans show that Oracle is using the index and not performing full table scans, thus resulting in more efficient execution.

The statements in this section are available online in the example file (tkqxpwr.sql).

### Creating and Populating the Power Demand Table

The power demand table, as demonstrated in Example 15-35, is created with two columns:

- `region` allows the electric utility to use the grid scheme in multiple areas or states. Each region, such as New York, New Jersey, Pennsylvania, and so on, is represented by a `10x10` grid.
- `sample` is a collection of samplings, or power demand readings from each cell in the grid, defined using the `PowerDemand_Typ` object type.

Example 15-35 Creating PowerDemand\_Tab Table for Power Demand Cartridge

```
CREATE TABLE PowerDemand_Tab (
  -- Region for which these power demand readings apply
  region NUMBER,
  -- Values for each "sampling" time (for a given hour)
  sample PowerDemand_Typ
);
```

Several rows are inserted, representing power demand data for two regions, `1` and `2`, for several hourly timestamps. For simplicity, values are inserted only into the first `5` positions of each grid; the remaining `95` values are set to `null`, as demonstrated in Example 15-36.

Example 15-36 Populating PowerDemand\_Tab Table for Power Demand Cartridge

```
-- The next INSERT statements "cheats" by supplying only 5 grid values
  
-- First 5 INSERT statements are for region 1 (1 AM to 5 AM on 01-Feb-1998).
 
INSERT INTO PowerDemand_Tab VALUES(1,
   PowerDemand_Typ(NULL, NULL, NULL, PowerGrid_Typ(55,8,13,9,5),
   to_date('02-01-1998 01','MM-DD-YYYY HH'))
);
 
INSERT INTO PowerDemand_Tab VALUES(1,
   PowerDemand_Typ(NULL, NULL, NULL, PowerGrid_Typ(56,8,13,9,3),
   to_date('02-01-1998 02','MM-DD-YYYY HH'))
);
 
INSERT INTO PowerDemand_Tab VALUES(1,
   PowerDemand_Typ(NULL, NULL, NULL, PowerGrid_Typ(55,8,13,9,3),
   to_date('02-01-1998 03','MM-DD-YYYY HH'))
);
  
INSERT INTO PowerDemand_Tab VALUES(1,
   PowerDemand_Typ(NULL, NULL, NULL, PowerGrid_Typ(54,8,13,9,3),
   to_date('02-01-1998 04','MM-DD-YYYY HH'))
);
 
INSERT INTO PowerDemand_Tab VALUES(1,
   PowerDemand_Typ(NULL, NULL, NULL, PowerGrid_Typ(54,8,12,9,3),
   to_date('02-01-1998 05','MM-DD-YYYY HH'))
);
 
-- Also insert some rows for region 2.
 
INSERT INTO PowerDemand_Tab VALUES(2,
   PowerDemand_Typ(NULL, NULL, NULL, PowerGrid_Typ(9,8,11,16,5),
   to_date('02-01-1998 01','MM-DD-YYYY HH'))
);
  
INSERT INTO PowerDemand_Tab VALUES(2,
   PowerDemand_Typ(NULL, NULL, NULL, PowerGrid_Typ(9,8,11,20,5),
   to_date('02-01-1998 02','MM-DD-YYYY HH'))
);
```

Finally, the values for `TotGridDemand`, `MaxCellDemand`, and `MinCellDemand` are computed and set for each of the newly inserted rows, and these values are displayed, as demonstrated in Example 15-37.

Example 15-37 Computing Grid and Cell Demands for Power Demand Cartridge

```
DECLARE
CURSOR c1 IS SELECT Sample, Region FROM PowerDemand_Tab FOR UPDATE;
s PowerDemand_Typ;
r NUMBER;
BEGIN
  OPEN c1;
  LOOP
     FETCH c1 INTO s,r;
     EXIT WHEN c1%NOTFOUND;
     s.SetTotalDemand;
     s.SetMaxDemand;
     s.SetMinDemand;
     dbms_output.put_line(s.TotGridDemand);
     dbms_output.put_line(s.MaxCellDemand);
     dbms_output.put_line(s.MinCellDemand);
     UPDATE PowerDemand_Tab SET Sample = s WHERE CURRENT OF c1;
  END LOOP;
  CLOSE c1;
END;
/

-- Examine the values. 
SELECT region, P.Sample.TotGridDemand, P.Sample.MaxCellDemand,
   P.Sample.MinCellDemand,
   to_char(P.sample.sampletime, 'MM-DD-YYYY HH') 
 FROM PowerDemand_Tab P;
```

### Querying Without the Index

The queries is this section are executed by applying the underlying function `PowerEqualsSpecific_Func()` for every row in the table, because the index has not yet been defined.

The example file includes queries that check, both for a specific cell number and for any cell number, for values equal to, greater than, and less than a specified value. For example, the equality queries are demonstrated in Example 15-38.

Example 15-38 Making Equality Queries for Power Demand Cartridge

```
SET SERVEROUTPUT ON
-------------------------------------------------------------------
-- Query, referencing the operators (without index)
-------------------------------------------------------------------
explain plan for
SELECT P.Region, P.Sample.TotGridDemand ,P.Sample.MaxCellDemand, 
     P.Sample.MinCellDemand
   FROM PowerDemand_Tab P
   WHERE Power_Equals(P.Sample,2,10) = 1;
@tkoqxpll
 
SELECT P.Region, P.Sample.TotGridDemand ,P.Sample.MaxCellDemand, 
     P.Sample.MinCellDemand
   FROM PowerDemand_Tab P
   WHERE Power_Equals(P.Sample,2,10) = 1;

explain plan for
SELECT P.Region, P.Sample.TotGridDemand ,P.Sample.MaxCellDemand,
     P.Sample.MinCellDemand
   FROM PowerDemand_Tab P
   WHERE Power_Equals(P.Sample,1,25) = 1;
@tkoqxpll

SELECT P.Region, P.Sample.TotGridDemand ,P.Sample.MaxCellDemand,
     P.Sample.MinCellDemand
   FROM PowerDemand_Tab P
   WHERE Power_Equals(P.Sample,1,25) = 1;
 
explain plan for
SELECT P.Region, P.Sample.TotGridDemand ,P.Sample.MaxCellDemand, 
     P.Sample.MinCellDemand
   FROM PowerDemand_Tab P
   WHERE Power_Equals(P.Sample,2,8) = 1;
@tkoqxpll
 
SELECT P.Region, P.Sample.TotGridDemand ,P.Sample.MaxCellDemand, 
     P.Sample.MinCellDemand
   FROM PowerDemand_Tab P
   WHERE Power_Equals(P.Sample,2,8) = 1;
 
explain plan for
SELECT P.Region, P.Sample.TotGridDemand ,P.Sample.MaxCellDemand, 
     P.Sample.MinCellDemand
   FROM PowerDemand_Tab P
   WHERE Power_EqualsAny(P.Sample,9) = 1;
@tkoqxpll
 
SELECT P.Region, P.Sample.TotGridDemand ,P.Sample.MaxCellDemand, 
     P.Sample.MinCellDemand
   FROM PowerDemand_Tab P
   WHERE Power_EqualsAny(P.Sample,9) = 1;
```

The execution plans show that a full table scan is performed in each case:

```
OPERATIONS       OPTIONS         OBJECT_NAME    
---------------  --------------- ---------------
SELECT STATEMENT                                
TABLE ACCESS     FULL            POWERDEMAND_TAB
```

### Creating the Index

The index is created on the `Sample` column in the power demand table, as demonstrated in Example 15-39.

Example 15-39 Creating an Index in PowerDemand\_Tab Table for Power Demand Cartridge

```
CREATE INDEX PowerIndex ON PowerDemand_Tab(Sample) 
   INDEXTYPE IS power_idxtype;
```

### Querying with the Index

The queries in this section are identical to those in "Querying Without the Index", but this time the index is used.

The execution plans show that Oracle is using the domain index and not performing full table scans, thus resulting in more efficient execution, as demonstrated in Example 15-40.

Example 15-40 Making Equality Queries with Index for Power Demand Cartridge

```
SQLPLUS> -------------------------------------------------------------------
SQLPLUS> -- Query, referencing the operators (with index)
SQLPLUS> -------------------------------------------------------------------
SQLPLUS> explain plan for
     2> SELECT P.Region, P.Sample.TotGridDemand ,P.Sample.MaxCellDemand, 
     3>      P.Sample.MinCellDemand
     4>    FROM PowerDemand_Tab P
     5>    WHERE Power_Equals(P.Sample,2,10) = 1;
Statement processed.
SQLPLUS> @tkoqxpll
SQLPLUS> set echo off
Echo                            OFF
Charwidth                       15
OPERATIONS      OPTIONS         OBJECT_NAME    
--------------- --------------- ---------------
SELECT STATEMEN                                
TABLE ACCESS    BY ROWID        POWERDEMAND_TAB
DOMAIN INDEX                    POWERINDEX     
3 rows selected.
Statement processed.
Echo                            ON
SQLPLUS>  
SQLPLUS> SELECT P.Region, P.Sample.TotGridDemand ,P.Sample.MaxCellDemand, 
     2>      P.Sample.MinCellDemand
     3>    FROM PowerDemand_Tab P
     4>    WHERE Power_Equals(P.Sample,2,10) = 1;
REGION     SAMPLE.TOT SAMPLE.MAX SAMPLE.MIN
---------- ---------- ---------- ----------
0 rows selected.
ODCIIndexStart>>>>>
ODCIIndexInfo
Index owner : POWERCARTUSER
Index name : POWERINDEX
Table owner : POWERCARTUSER
Table name : POWERDEMAND_TAB
Indexed column : "SAMPLE"
Indexed column type :POWERDEMAND_TYP
Indexed column type schema:POWERCARTUSER
ODCIPredInfo
Object owner : POWERCARTUSER
Object name : POWER_EQUALS
Method name : 
Predicate bounds flag :
     Exact Match
     Include Start Key
     Include Stop Key
start key : 1
stop key : 1
compare position : 2
compare value : 10
ODCIIndexStart>>>>>select r from POWERCARTUSER.POWERINDEX_pidx where cpos ='2' and cval ='10'
ODCIIndexFetch>>>>>
Nrows : 2000
ODCIIndexClose>>>>>
SQLPLUS>  
SQLPLUS> explain plan for
     2> SELECT P.Region, P.Sample.TotGridDemand ,P.Sample.MaxCellDemand, 
     3>      P.Sample.MinCellDemand
     4>    FROM PowerDemand_Tab P
     5>    WHERE Power_Equals(P.Sample,2,8) = 1;
Statement processed.
SQLPLUS> @tkoqxpll
SQLPLUS> set echo off
Echo                            OFF
Charwidth                       15
OPERATIONS      OPTIONS         OBJECT_NAME    
--------------- --------------- ---------------
SELECT STATEMEN                                
TABLE ACCESS    BY ROWID        POWERDEMAND_TAB
DOMAIN INDEX                    POWERINDEX     
3 rows selected.
Statement processed.
Echo                            ON
SQLPLUS>  
SQLPLUS> SELECT P.Region, P.Sample.TotGridDemand ,P.Sample.MaxCellDemand, 
     2>      P.Sample.MinCellDemand
     3>    FROM PowerDemand_Tab P
     4>    WHERE Power_Equals(P.Sample,2,8) = 1;
REGION     SAMPLE.TOT SAMPLE.MAX SAMPLE.MIN
---------- ---------- ---------- ----------
         1         90         55          5
         1         89         56          3
         1         88         55          3
         1         87         54          3
         1         86         54          3
         2         49         16          5
         2         53         20          5
7 rows selected.
ODCIIndexStart>>>>>
ODCIIndexInfo
Index owner : POWERCARTUSER
Index name : POWERINDEX
Table owner : POWERCARTUSER
Table name : POWERDEMAND_TAB
Indexed column : "SAMPLE"
Indexed column type :POWERDEMAND_TYP
Indexed column type schema:POWERCARTUSER
ODCIPredInfo
Object owner : POWERCARTUSER
Object name : POWER_EQUALS
Method name : 
Predicate bounds flag :
     Exact Match
     Include Start Key
     Include Stop Key
start key : 1
stop key : 1
compare position : 2
compare value : 8
ODCIIndexStart>>>>>select r from POWERCARTUSER.POWERINDEX_pidx where cpos ='2' and cval ='8'
ODCIIndexFetch>>>>>
Nrows : 2000
ODCIIndexClose>>>>>
SQLPLUS>  
SQLPLUS> explain plan for
     2> SELECT P.Region, P.Sample.TotGridDemand ,P.Sample.MaxCellDemand, 
     3>      P.Sample.MinCellDemand
     4>    FROM PowerDemand_Tab P
     5>    WHERE Power_EqualsAny(P.Sample,9) = 1;
Statement processed.
SQLPLUS> @tkoqxpll
SQLPLUS> set echo off
Echo                            OFF
Charwidth                       15
OPERATIONS      OPTIONS         OBJECT_NAME    
--------------- --------------- ---------------
SELECT STATEMEN                                
TABLE ACCESS    BY ROWID        POWERDEMAND_TAB
DOMAIN INDEX                    POWERINDEX     
3 rows selected.
Statement processed.
Echo                            ON
SQLPLUS>  
SQLPLUS> SELECT P.Region, P.Sample.TotGridDemand ,P.Sample.MaxCellDemand, 
     2>      P.Sample.MinCellDemand
     3>    FROM PowerDemand_Tab P
     4>    WHERE Power_EqualsAny(P.Sample,9) = 1;
REGION     SAMPLE.TOT SAMPLE.MAX SAMPLE.MIN
---------- ---------- ---------- ----------
         1         90         55          5
         1         89         56          3
         1         88         55          3
         1         87         54          3
         1         86         54          3
         2         49         16          5
         2         53         20          5
7 rows selected.
ODCIIndexStart>>>>>
ODCIIndexInfo
Index owner : POWERCARTUSER
Index name : POWERINDEX
Table owner : POWERCARTUSER
Table name : POWERDEMAND_TAB
Indexed column : "SAMPLE"
Indexed column type :POWERDEMAND_TYP
Indexed column type schema:POWERCARTUSER
ODCIPredInfo
Object owner : POWERCARTUSER
Object name : POWER_EQUALSANY
Method name : 
Predicate bounds flag :
     Exact Match
     Include Start Key
     Include Stop Key
start key : 1
stop key : 1
compare value : 9
ODCIIndexStart>>>>>select distinct r from POWERCARTUSER.POWERINDEX_pidx where cval ='9'
ODCIIndexFetch>>>>>
Nrows : 2000
ODCIIndexClose>>>>>
SQLPLUS>
SQLPLUS> explain plan for
     2> SELECT P.Region, P.Sample.TotGridDemand ,P.Sample.MaxCellDemand,
     3>      P.Sample.MinCellDemand
     4>    FROM PowerDemand_Tab P
     5>    WHERE Power_GreaterThanAny(P.Sample,50) = 1;
Statement processed.
SQLPLUS> @tkoqxpll
SQLPLUS> set echo off
Echo                            OFF
Charwidth                       15
OPERATIONS      OPTIONS         OBJECT_NAME    
--------------- --------------- ---------------
SELECT STATEMEN                                
TABLE ACCESS    BY ROWID        POWERDEMAND_TAB
DOMAIN INDEX                    POWERINDEX     
3 rows selected.
Statement processed.
Echo                            ON
SQLPLUS>
SQLPLUS> SELECT P.Region, P.Sample.TotGridDemand ,P.Sample.MaxCellDemand,
     2>      P.Sample.MinCellDemand
     3>    FROM PowerDemand_Tab P
     4>    WHERE Power_GreaterThanAny(P.Sample,50) = 1;
REGION     SAMPLE.TOT SAMPLE.MAX SAMPLE.MIN
---------- ---------- ---------- ----------
         1         90         55          5
         1         89         56          3
         1         88         55          3
         1         87         54          3
         1         86         54          3
5 rows selected.
ODCIIndexStart>>>>>
ODCIIndexInfo
Index owner : POWERCARTUSER
Index name : POWERINDEX
Table owner : POWERCARTUSER
Table name : POWERDEMAND_TAB
Indexed column : "SAMPLE"
Indexed column type :POWERDEMAND_TYP
Indexed column type schema:POWERCARTUSER
ODCIPredInfo
Object owner : POWERCARTUSER
Object name : POWER_GREATERTHANANY
Method name :
Predicate bounds flag :
     Exact Match
     Include Start Key
     Include Stop Key
start key : 1
stop key : 1
compare value : 50
ODCIIndexStart>>>>>select distinct r from POWERCARTUSER.POWERINDEX_pidx where cv
al >'50'
ODCIIndexFetch>>>>>
Nrows : 2000
ODCIIndexClose>>>>>
SQLPLUS>
SQLPLUS> explain plan for
     2> SELECT P.Region, P.Sample.TotGridDemand ,P.Sample.MaxCellDemand,
     3>      P.Sample.MinCellDemand
     4>    FROM PowerDemand_Tab P
     5>    WHERE Power_LessThanAny(P.Sample,50) = 0;
Statement processed.
SQLPLUS> @tkoqxpll
SQLPLUS> set echo off
Echo                            OFF
Charwidth                       15
OPERATIONS      OPTIONS         OBJECT_NAME    
--------------- --------------- ---------------
SELECT STATEMEN                                
TABLE ACCESS    BY ROWID        POWERDEMAND_TAB
DOMAIN INDEX                    POWERINDEX     
3 rows selected.
Statement processed.
Echo                            ON
SQLPLUS>
SQLPLUS> SELECT P.Region, P.Sample.TotGridDemand ,P.Sample.MaxCellDemand,
     2>      P.Sample.MinCellDemand
     3>    FROM PowerDemand_Tab P
     4>    WHERE Power_LessThanAny(P.Sample,50) = 0;
REGION     SAMPLE.TOT SAMPLE.MAX SAMPLE.MIN
---------- ---------- ---------- ----------
0 rows selected.
ODCIIndexStart>>>>>
ODCIIndexInfo
Index owner : POWERCARTUSER
Index name : POWERINDEX
Table owner : POWERCARTUSER
Table name : POWERDEMAND_TAB
Indexed column : "SAMPLE"
Indexed column type :POWERDEMAND_TYP
Indexed column type schema:POWERCARTUSER
ODCIPredInfo
Object owner : POWERCARTUSER
Object name : POWER_LESSTHANANY
Method name :
Predicate bounds flag :
     Exact Match
     Include Start Key
     Include Stop Key
start key : 0
stop key : 0
compare value : 50
ODCIIndexStart>>>>>select distinct r from POWERCARTUSER.POWERINDEX_pidx minus se
lect distinct r from POWERCARTUSER.POWERINDEX_pidx where cval <'50'
ODCIIndexFetch>>>>>
Nrows : 2000
ODCIIndexClose>>>>>
```