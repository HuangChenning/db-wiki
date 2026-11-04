---
title: ORD_DICOM
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/i_dicom.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 185 ORD\_DICOM

This Oracle Multimedia package supports the management and manipulation of Digital Imaging and Communications in Medicine (DICOM) content stored in BLOBs or BFILEs rather than in an ORDDicom object type. See [Oracle Multimedia DICOM Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10778/ch_dev_ref.htm#IMDCM4000) for a complete description of the ORDDicom object type.

The DICOM standard is the dominant standard for radiology imaging and communication, to which all major manufacturers of radiological devices must conform. Oracle Multimedia DICOM provides native support for DICOM format medical images and other content, such as single-frame and multiframe images, waveforms, slices of 3-D volumes, video segments, and structured reports.

The Oracle Multimedia `ORD_DICOM` package provides functions and procedures in the DICOM relational interface to extract standard and private DICOM metadata from DICOM content into customizable XML documents, to perform image processing operations such as format conversion and thumbnail image generation, and to create new DICOM content. This Oracle Multimedia package also provides functions and procedures to check DICOM content for conformance based on a set of user-specified conformance rules, and to make DICOM content anonymous based on user-defined rules that specify the set of attributes to be made anonymous and the actions to be taken to make those attributes anonymous.

The Oracle Multimedia `ORD_DICOM` package also provides functions and procedures in the DICOM data model utility interface to operate on the DICOM data model repository. See [Oracle Multimedia DICOM Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10778/ch_dtmod_ref.htm#IMDCM3000) for a complete description of the DICOM data model utility interface.

- Documentation of ORD\_DICOM

---

## Documentation of ORD\_DICOM

For a complete description of this package within the context of Oracle Multimedia, see [`ORD_DICOM`](https://docs.oracle.com/cd/E11882_01/appdev.112/e10778/ch_rel_ref.htm#IMDCM6000) in the [Oracle Multimedia DICOM Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10778/toc.htm).