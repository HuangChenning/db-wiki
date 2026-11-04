---
title: "MySQL :: MySQL 26.7 Reference Manual :: 15.1.24 CREATE SPATIAL REFERENCE SYSTEM Statement"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/create-spatial-reference-system.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 15.1.24 CREATE SPATIAL REFERENCE SYSTEM Statement

```sql
CREATE OR REPLACE SPATIAL REFERENCE SYSTEM
    srid srs_attribute ...

CREATE SPATIAL REFERENCE SYSTEM
    [IF NOT EXISTS]
    srid srs_attribute ...

srs_attribute: {
    NAME 'srs_name'
  | DEFINITION 'definition'
  | ORGANIZATION 'org_name' IDENTIFIED BY org_id
  | DESCRIPTION 'description'
}

srid, org_id: 32-bit unsigned integer
```

This statement creates a [spatial reference system](spatial-reference-systems.md) (SRS) definition and stores it in the data dictionary, and requires the [`CREATE_SPATIAL_REFERENCE_SYSTEM`](privileges-provided.md) privilege (or [`SUPER`](privileges-provided.md)). The resulting data dictionary entry can be inspected using the `INFORMATION_SCHEMA` [`ST_SPATIAL_REFERENCE_SYSTEMS`](information-schema-st-spatial-reference-systems-table.md) table.

SRID values must be unique, so if neither `OR       REPLACE` nor `IF NOT EXISTS` is specified, an error occurs if an SRS definition with the given *`srid`* value already exists.

With `CREATE OR REPLACE` syntax, any existing SRS definition with the same SRID value is replaced, unless the SRID value is used by some column in an existing table. In that case, an error occurs. For example:

```sql
mysql> CREATE OR REPLACE SPATIAL REFERENCE SYSTEM 4326 ...;
ERROR 3716 (SR005): Can't modify SRID 4326. There is at
least one column depending on it.
```

To identify which column or columns use the SRID, use this query, replacing 4326 with the SRID of the definition you are trying to create:

```sql
SELECT * FROM INFORMATION_SCHEMA.ST_GEOMETRY_COLUMNS WHERE SRS_ID=4326;
```

With `CREATE ... IF NOT EXISTS` syntax, any existing SRS definition with the same SRID value causes the new definition to be ignored and a warning occurs.

SRID values must be in the range of 32-bit unsigned integers, with these restrictions:

- SRID 0 is a valid SRID but cannot be used with `CREATE SPATIAL REFERENCE           SYSTEM`.
- If the value is in a reserved SRID range, a warning occurs. Reserved ranges are \[0, 32767\] (reserved by EPSG), \[60,000,000, 69,999,999\] (reserved by EPSG), and \[2,000,000,000, 2,147,483,647\] (reserved by MySQL). EPSG stands for the [European Petroleum Survey Group](http://epsg.org/).
- Users should not create SRSs with SRIDs in the reserved ranges. Doing so runs the risk of the SRIDs conflicting with future SRS definitions distributed with MySQL, with the result that the new system-provided SRSs are not installed for MySQL upgrades or that the user-defined SRSs are overwritten.

Attributes for the statement must satisfy these conditions:

- Attributes can be given in any order, but no attribute can be given more than once.
- The `NAME` and `DEFINITION` attributes are mandatory.
- The `NAME` *`srs_name`* attribute value must be unique. The combination of the `ORGANIZATION` *`org_name`* and *`org_id`* attribute values must be unique.
- The `NAME` *`srs_name`* attribute value and `ORGANIZATION` *`org_name`* attribute value cannot be empty or begin or end with whitespace.
- String values in attribute specifications cannot contain control characters, including newline.
- The following table shows the maximum lengths for string attribute values.
	**Table 15.6 CREATE SPATIAL REFERENCE SYSTEM Attribute Lengths**
	| Attribute | Maximum Length (characters) |
	| --- | --- |
	| `NAME` | 80 |
	| `DEFINITION` | 4096 |
	| `ORGANIZATION` | 256 |
	| `DESCRIPTION` | 2048 |

Here is an example `CREATE SPATIAL REFERENCE       SYSTEM` statement. The `DEFINITION` value is reformatted across multiple lines for readability. (For the statement to be legal, the value actually must be given on a single line.)

```sql
CREATE SPATIAL REFERENCE SYSTEM 4120
NAME 'Greek'
ORGANIZATION 'EPSG' IDENTIFIED BY 4120
DEFINITION
  'GEOGCS["Greek",DATUM["Greek",SPHEROID["Bessel 1841",
  6377397.155,299.1528128,AUTHORITY["EPSG","7004"]],
  AUTHORITY["EPSG","6120"]],PRIMEM["Greenwich",0,
  AUTHORITY["EPSG","8901"]],UNIT["degree",0.017453292519943278,
  AUTHORITY["EPSG","9122"]],AXIS["Lat",NORTH],AXIS["Lon",EAST],
  AUTHORITY["EPSG","4120"]]';
```

The grammar for SRS definitions is based on the grammar defined in *OpenGIS Implementation Specification: Coordinate Transformation Services*, Revision 1.00, OGC 01-009, January 12, 2001, Section 7.2. This specification is available at [http://www.opengeospatial.org/standards/ct](http://www.opengeospatial.org/standards/ct).

MySQL incorporates these changes to the specification:

- Only the `<horz cs>` production rule is implemented (that is, geographic and projected SRSs).
- There is an optional, nonstandard `<authority>` clause for `<parameter>`. This makes it possible to recognize projection parameters by authority instead of name.
- The specification does not make `AXIS` clauses mandatory in `GEOGCS` spatial reference system definitions. However, if there are no `AXIS` clauses, MySQL cannot determine whether a definition has axes in latitude-longitude order or longitude-latitude order. MySQL enforces the nonstandard requirement that each `GEOGCS` definition must include two `AXIS` clauses. One must be `NORTH` or `SOUTH`, and the other `EAST` or `WEST`. The `AXIS` clause order determines whether the definition has axes in latitude-longitude order or longitude-latitude order.
- SRS definitions may not contain newlines.

If an SRS definition specifies an authority code for the projection (which is recommended), an error occurs if the definition is missing mandatory parameters. In this case, the error message indicates what the problem is. The projection methods and mandatory parameters that MySQL supports are shown in Table 15.7, “Supported Spatial Reference System Projection Methods” and Table 15.8, “Spatial Reference System Projection Parameters”.

The following table shows the projection methods that MySQL supports. MySQL permits unknown projection methods but cannot check the definition for mandatory parameters and cannot convert spatial data to or from an unknown projection. For detailed explanations of how each projection works, including formulas, see [EPSG Guidance Note 7-2](http://www.epsg.org/Portals/0/373-07-2.pdf).

**Table 15.7 Supported Spatial Reference System Projection Methods**

| EPSG Code | Projection Name | Mandatory Parameters (EPSG Codes) |
| --- | --- | --- |
| 1024 | Popular Visualisation Pseudo Mercator | 8801, 8802, 8806, 8807 |
| 1027 | Lambert Azimuthal Equal Area (Spherical) | 8801, 8802, 8806, 8807 |
| 1028 | Equidistant Cylindrical | 8823, 8802, 8806, 8807 |
| 1029 | Equidistant Cylindrical (Spherical) | 8823, 8802, 8806, 8807 |
| 1041 | Krovak (North Orientated) | 8811, 8833, 1036, 8818, 8819, 8806, 8807 |
| 1042 | Krovak Modified | 8811, 8833, 1036, 8818, 8819, 8806, 8807, 8617, 8618, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035 |
| 1043 | Krovak Modified (North Orientated) | 8811, 8833, 1036, 8818, 8819, 8806, 8807, 8617, 8618, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035 |
| 1051 | Lambert Conic Conformal (2SP Michigan) | 8821, 8822, 8823, 8824, 8826, 8827, 1038 |
| 1052 | Colombia Urban | 8801, 8802, 8806, 8807, 1039 |
| 9801 | Lambert Conic Conformal (1SP) | 8801, 8802, 8805, 8806, 8807 |
| 9802 | Lambert Conic Conformal (2SP) | 8821, 8822, 8823, 8824, 8826, 8827 |
| 9803 | Lambert Conic Conformal (2SP Belgium) | 8821, 8822, 8823, 8824, 8826, 8827 |
| 9804 | Mercator (variant A) | 8801, 8802, 8805, 8806, 8807 |
| 9805 | Mercator (variant B) | 8823, 8802, 8806, 8807 |
| 9806 | Cassini-Soldner | 8801, 8802, 8806, 8807 |
| 9807 | Transverse Mercator | 8801, 8802, 8805, 8806, 8807 |
| 9808 | Transverse Mercator (South Orientated) | 8801, 8802, 8805, 8806, 8807 |
| 9809 | Oblique Stereographic | 8801, 8802, 8805, 8806, 8807 |
| 9810 | Polar Stereographic (variant A) | 8801, 8802, 8805, 8806, 8807 |
| 9811 | New Zealand Map Grid | 8801, 8802, 8806, 8807 |
| 9812 | Hotine Oblique Mercator (variant A) | 8811, 8812, 8813, 8814, 8815, 8806, 8807 |
| 9813 | Laborde Oblique Mercator | 8811, 8812, 8813, 8815, 8806, 8807 |
| 9815 | Hotine Oblique Mercator (variant B) | 8811, 8812, 8813, 8814, 8815, 8816, 8817 |
| 9816 | Tunisia Mining Grid | 8821, 8822, 8826, 8827 |
| 9817 | Lambert Conic Near-Conformal | 8801, 8802, 8805, 8806, 8807 |
| 9818 | American Polyconic | 8801, 8802, 8806, 8807 |
| 9819 | Krovak | 8811, 8833, 1036, 8818, 8819, 8806, 8807 |
| 9820 | Lambert Azimuthal Equal Area | 8801, 8802, 8806, 8807 |
| 9822 | Albers Equal Area | 8821, 8822, 8823, 8824, 8826, 8827 |
| 9824 | Transverse Mercator Zoned Grid System | 8801, 8830, 8831, 8805, 8806, 8807 |
| 9826 | Lambert Conic Conformal (West Orientated) | 8801, 8802, 8805, 8806, 8807 |
| 9828 | Bonne (South Orientated) | 8801, 8802, 8806, 8807 |
| 9829 | Polar Stereographic (variant B) | 8832, 8833, 8806, 8807 |
| 9830 | Polar Stereographic (variant C) | 8832, 8833, 8826, 8827 |
| 9831 | Guam Projection | 8801, 8802, 8806, 8807 |
| 9832 | Modified Azimuthal Equidistant | 8801, 8802, 8806, 8807 |
| 9833 | Hyperbolic Cassini-Soldner | 8801, 8802, 8806, 8807 |
| 9834 | Lambert Cylindrical Equal Area (Spherical) | 8823, 8802, 8806, 8807 |
| 9835 | Lambert Cylindrical Equal Area | 8823, 8802, 8806, 8807 |

The following table shows the projection parameters that MySQL recognizes. Recognition occurs primarily by authority code. If there is no authority code, MySQL falls back to case-insensitive string matching on the parameter name. For details about each parameter, look it up by code in the [EPSG Online Registry](https://www.epsg-registry.org/).

**Table 15.8 Spatial Reference System Projection Parameters**

| EPSG Code | Fallback Name (Recognized by MySQL) | EPSG Name |
| --- | --- | --- |
| 1026 | c1 | C1 |
| 1027 | c2 | C2 |
| 1028 | c3 | C3 |
| 1029 | c4 | C4 |
| 1030 | c5 | C5 |
| 1031 | c6 | C6 |
| 1032 | c7 | C7 |
| 1033 | c8 | C8 |
| 1034 | c9 | C9 |
| 1035 | c10 | C10 |
| 1036 | azimuth | Co-latitude of cone axis |
| 1038 | ellipsoid\_scale\_factor | Ellipsoid scaling factor |
| 1039 | projection\_plane\_height\_at\_origin | Projection plane origin height |
| 8617 | evaluation\_point\_ordinate\_1 | Ordinate 1 of evaluation point |
| 8618 | evaluation\_point\_ordinate\_2 | Ordinate 2 of evaluation point |
| 8801 | latitude\_of\_origin | Latitude of natural origin |
| 8802 | central\_meridian | Longitude of natural origin |
| 8805 | scale\_factor | Scale factor at natural origin |
| 8806 | false\_easting | False easting |
| 8807 | false\_northing | False northing |
| 8811 | latitude\_of\_center | Latitude of projection centre |
| 8812 | longitude\_of\_center | Longitude of projection centre |
| 8813 | azimuth | Azimuth of initial line |
| 8814 | rectified\_grid\_angle | Angle from Rectified to Skew Grid |
| 8815 | scale\_factor | Scale factor on initial line |
| 8816 | false\_easting | Easting at projection centre |
| 8817 | false\_northing | Northing at projection centre |
| 8818 | pseudo\_standard\_parallel\_1 | Latitude of pseudo standard parallel |
| 8819 | scale\_factor | Scale factor on pseudo standard parallel |
| 8821 | latitude\_of\_origin | Latitude of false origin |
| 8822 | central\_meridian | Longitude of false origin |
| 8823 | standard\_parallel\_1, standard\_parallel1 | Latitude of 1st standard parallel |
| 8824 | standard\_parallel\_2, standard\_parallel2 | Latitude of 2nd standard parallel |
| 8826 | false\_easting | Easting at false origin |
| 8827 | false\_northing | Northing at false origin |
| 8830 | initial\_longitude | Initial longitude |
| 8831 | zone\_width | Zone width |
| 8832 | standard\_parallel | Latitude of standard parallel |
| 8833 | longitude\_of\_center | Longitude of origin |