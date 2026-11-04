---
title: IMG-00001 to IMG-02014
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/imgus.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 113 IMG-00001 to IMG-02014

IMG-00001: unable to initialize Oracle Multimedia environment

Cause: The image processing external procedure initialization process failed.

Action: Contact Oracle Support Services.

IMG-00002: unrecoverable error

Cause: This is an internal error.

Action: Contact Oracle Support Services.

IMG-00003: exhausted memory while processing image

Cause: Oracle Multimedia exhausted available Java memory during processing.

Action: Increase the JAVA\_POOL\_SIZE initialization parameter setting.

IMG-00201: unsupported metadata type

Cause: The requested metadata type could not be read from or written to this image format.

Action: Refer to the Oracle Multimedia documentation to select the proper metadata type for this image.

IMG-00202: unsupported character encoding

Cause: The character encoding was not supported for this image format.

Action: Refer to the Oracle Multimedia documentation to select the proper encoding for this image.

IMG-00203: xmlData is invalid

Cause: The XML document was NULL or not schema valid.

Action: Create a schema valid document for input.

IMG-00204: input metadata too long

Cause: The metadata was too long to embed in this image format.

Action: Trim the metadata, or use a different image format.

IMG-00205: cannot add a TIFF directory entry

Cause: No new entries could be added to this directory.

Action: Use a different image format.

IMG-00206: unsupported image format for putMetadata

Cause: Metadata could not be written to this image format.

Action: Use a different image format.

IMG-00207: input parameter is not valid

Cause: The input parameter value contained an invalid value.

Action: Correct the input parameter value.

IMG-00208: metadata format parse error

Cause: The parser detected an error in the embedded metadata.

Action: Verify that the metadata conforms to proper standards.

IMG-00209: error parsing metadata

Cause: There was an internal error while parsing the metadata.

Action: Contact Oracle Support Services.

IMG-00210: unable to get metadata from an empty image

Cause: There was no data in the input image.

Action: Refer to the Oracle Multimedia documentation for information on how to populate image data into the image object.

IMG-00211: metadataType value "string" is invalid

Cause: The metadataType parameter value was NULL or invalid.

Action: Correct the metadataType parameter value.

IMG-00212: encoding value "string" is invalid

Cause: The encoding parameter value was NULL or invalid.

Action: Correct the encoding parameter value.

IMG-00213: xmlData does not contain an \<RDF> element

Cause: The XML document did not contain an \<RDF> element as a child of \<xmpMetadata>.

Action: Create a schema valid document with an \<RDF> element.

IMG-00502: invalid scale value

Cause: An invalid scale value was found while parsing the parameters for the image process function.

Action: Refer to the Oracle Multimedia documentation for a description of the correct usage and syntax for the image processing command string.

IMG-00505: missing value in CUT rectangle

Cause: An incorrect number of values was used to specify a rectangle.

Action: Use exactly four integer values for the lower-left and upper- right vertices.

IMG-00506: extra value in CUT rectangle

Cause: An incorrect number of values was used to specify a rectangle.

Action: Use exactly four integer values for the lower left and upper right vertices.

IMG-00510: string

Cause: A syntax error was found while parsing the parameters for the image process function.

Action: Refer to the Oracle Multimedia documentation for a description of the correct usage and syntax for the image processing command string.

IMG-00511: string

Cause: An error was found while accessing image data.

Action: Contact Oracle Support Services.

IMG-00512: multiple incompatible scaling parameters found

Cause: Multiple incompatible scaling parameters were found in the image process command string. With the exception of XSCALE and YSCALE, which can be used together in a process command string, scaling functions are mutually exclusive and cannot be combined.

Action: Remove scaling functions until only one remains (or two, if they are XSCALE and YSCALE).

IMG-00513: missing value in scaling operation

Cause: An incorrect number of values was used to specify image dimensions. fixedScale and maxScale require exactly two integer values for the X and Y dimensions of the desired image.

Action: Use two values for fixedScale and maxScale.

IMG-00514: extra value in scaling operation

Cause: An incorrect number of values was used to specify image dimensions. fixedScale and maxScale require exactly two integer values for the X and Y dimensions of the desired image.

Action: Use two values for fixedScale and maxScale.

IMG-00515: incorrect number of input channels

Cause: An incorrect number of values was used to specify input channels. InputChannels requires either one or three channels numbers for the gray or red, green, and blue channel assignments.

Action: Use either one or three values to specify the input channels.

IMG-00516: default channel out of range

Cause: An incorrect value was used to specify the default channel selection.

Action: Use a channel number which is less than or equal to the number of bands and greater than zero.

IMG-00517: height or width not present in parameter string

Cause: Height and/or width were not specified in the setProperties parameter string.

Action: Specify both the height and width.

IMG-00518: invalid value for height or width

Cause: Height and/or width were not positive integers"

Action: Specify both the height and width as positive integers"

IMG-00519: illegal combination of parameters

Cause: Other than height, width, dataOffset, and userString no other parameters may be specified in the setProperties parameter string when CCITTG3 or CCITTG4 is used as the compressionFormat.

Action: Supply only the height and width when compessionFormat is either CCITTG3 or CCITTG4. The dataOffset and userString may optionally be supplied as well.

IMG-00520: invalid value for numberOfBands

Cause: NumberOfBands was not a positive integer"

Action: Specify numberOfBands as a positive integer"

IMG-00521: invalid value for dataOffset

Cause: DataOffset was not a positive integer"

Action: Specify dataOffset as a positive integer"

IMG-00522: invalid format for parameter value

Cause: A floating point value was specified where an integer is required, or a character value was specified where a numeric value is required.

Action: Specify the correct type of values for process parameters.

IMG-00523: invalid process verb

Cause: A process verb was specified that is not understood by Oracle Multimedia.

Action: Refer to the Oracle Multimedia documentation for a description of valid process verbs.

IMG-00524: mismatched quotes

Cause: Quotation marks used within a process command string were not matched.

Action: Ensure that quotation marks occur in pairs.

IMG-00525: locale error

Cause: This is an internal error.

Action: Contact Oracle Support Services.

IMG-00526: error parsing foreign image description

Cause: An internal error occurred while processing a foreign image.

Action: Contact Oracle Support Services.

IMG-00527: invalid deletePages specified

Cause: The specified value for the deletePages parameter was not valid.

Action: See the Oracle Multimedia documentation for reference information about valid values for deletePages parameter.

IMG-00528: invalid movePages specified

Cause: The specified value for the movePages parameter was not valid.

Action: See the Oracle Multimedia documentation for reference information about valid values for movePages parameter.

IMG-00529: invalid combination of TIFF page operations

Cause: The specified TIFF page operations were not valid.

Action: See the Oracle Multimedia documentation for reference information about valid values for TIFF page operations.

IMG-00530: internal error while parsing command

Cause: An internal error occurred while parsing the command passed to the image processing function or the foreign image setProperties function.

Action: If you are certain that your command is correct, then contact Oracle Support Services.

IMG-00531: empty or null image processing command

Cause: An empty or null image processing command was passed to the image process function.

Action: Refer to the Oracle Multimedia documentation for a description of the correct usage and syntax for the image processing command string.

IMG-00540: contentFormat and interleave conflict

Cause: Interleave values were specified using both the contentformat and interleave verbs.

Action: Specify interleave using either contentformat or interleave, but not both.

IMG-00541: invalid contentFormat specified

Cause: The specified contentFormat was not valid.

Action: Refer to the Oracle Multimedia documentation for a description of valid contentFormat specifications.

IMG-00542: contentFormat includes invalid extra information

Cause: The specified contentFormat included invalid characters at the end of the parameter string.

Action: Refer to the Oracle Multimedia documentation for a description of valid contentFormat specifications.

IMG-00543: invalid compressionFormat specified

Cause: The specified compressionFormat was not valid.

Action: Refer to the Oracle Multimedia documentation for a description of valid compressionFormat specifications.

IMG-00544: invalid compressionQuality specified

Cause: The specified compressionQuality was not valid.

Action: Refer to the Oracle Multimedia documentation for a description of valid compressionQuality specifications.

IMG-00545: invalid cut values specified

Cause: An invalid value was found while parsing the parameters for the cut operation.

Action: Refer to the Oracle Multimedia documentation for a description of the correct usage and syntax for the image processing command string.

IMG-00546: invalid page number specified

Cause: An invalid page number was specified.

Action: Specify page numbers that are not negative.

IMG-00547: invalid channelOrder specified

Cause: The specified channelOrder was not valid.

Action: Refer to the Oracle Multimedia documentation for a description of valid channelOrder specifications.

IMG-00548: invalid interleave specified

Cause: The specified interleave was not valid.

Action: Refer to the Oracle Multimedia documentation for a description of valid interleave specifications.

IMG-00549: invalid pixelOrder specfied

Cause: The specified pixelOrder was not valid.

Action: Refer to the Oracle Multimedia documentation for a description of valid pixelOrder specifications.

IMG-00550: invalid scanlineOrder specified

Cause: The specified scanline order was not valid.

Action: Refer to the Oracle Multimedia documentation for a description of valid scanlineOrder specifications.

IMG-00551: invalid quantize method specified

Cause: The specified quantization method was not valid.

Action: Refer to the Oracle Multimedia documentation for a description of valid quantization method specifications.

IMG-00552: invalid inputChannels specified

Cause: An invalid value was specified for the inputChannels verb.

Action: Refer to the Oracle Multimedia documentation for a description of the correct usage and syntax for the image processing command string.

IMG-00553: invalid rotate value

Cause: An invalid value was specified for image rotation. Rotation values must be a floating point number.

Action: Correct the statement by providing a valid rotation value.

IMG-00554: extra value in rotate operation

Cause: Multiple arguments were used to specify image rotation. The rotate operation accepts only a single value.

Action: Provide a single value for the rotate operation.

IMG-00555: invalid value for gamma correction

Cause: An invalid value was specified for gamma correction. Gamma values must be positive.

Action: Correct the statement by providing a positive gamma value.

IMG-00556: incorrect number of gamma values

Cause: An incorrect number of values were used to specify gamma correction. Gamma correction requires either one or three gamma values.

Action: Provide either one or three values to specify the gamma correction.

IMG-00557: invalid value for contrast enhancement

Cause: An invalid value was used to specify contrast enhancement.

Action: To specify contrast enhancement using percentages, provide values between 0 and 100. To specify contrast enhancement using bounds, provide values greater than 0.

IMG-00558: incorrect number of contrast values

Cause: An incorrect number of values were used to specify contrast enhancement. Contrast enhancement requires one, two, three, or six contrast values.

Action: Provide one or three values to specify contrast enhancement using percentages; provide two or six values to specify contrast enhancement using contrast bounds.

IMG-00559: invalid frame number

Cause: An incorrect number was used to specify frame in Dicom image. The number should be greater than 0 and less than total frames in Dicom image.

Action: Provide one number greater than 0 and less than total frames in Dicom image.

IMG-00560: input format does not support page selection

Cause: The page verb was specified for an input format that does not support selecting pages.

Action: Refer to the Oracle Multimedia documentation for a description of which image formats support page selection.

IMG-00561: input format does not support channel selection

Cause: The inputChannels verb was specified for an input format that does not support selecting channels.

Action: Refer to the Oracle Multimedia documentation for a description of which image formats support input channel selection.

IMG-00577: invalid quantize argument

Cause: A quantize value was specified that accepts an argument, but the argument provided was not valid.

Action: Provide a valid, non-negative argument for the quantize value.

IMG-00578: missing quantize argument

Cause: A quantize value was specified that requires an argument, but no argument was provided.

Action: Provide an argument for the quantize value.

IMG-00579: extra quantize argument

Cause: An extra argument was provided for a quantize value. Some quantize values accept no arguments, while others accept a single argument.

Action: Provide an argument only for quantize values that accept an argument.

IMG-00580: specified format does not support output

Cause: The output format specified by fileFormat does support output.

Action: Refer to the Oracle Multimedia documentation for a description of which formats support output.

IMG-00581: output format does not support the specified contentFormat

Cause: The specified contentFormat is not supported by the explicitly or implicitly specified output format.

Action: Refer to the Oracle Multimedia documentation for a description of which contentFormat values are supported for each output format.

IMG-00582: output format does not support the specified interleave

Cause: The specified interleave is not supported by the explicitly or implicitly specified output format.

Action: Refer to the Oracle Multimedia documentation for a description of which interleave values are supported for each output format.

IMG-00583: output format does not support the specified compressionFormat

Cause: The specified compressionFormat is not supported by the explicitly or implicitly specified output format.

Action: Refer to the Oracle Multimedia documentation for a description of which compressionFormat values are supported for each output format.

IMG-00584: output format does not support the specified compressionQuality

Cause: The specified compressionQuality is not supported by the explicitly or implicitly specified output format.

Action: Refer to the Oracle Multimedia documentation for a description of which compressionQuality values are supported for each output format.

IMG-00585: output format does not support the specified channelOrder

Cause: The specified channelOrder is not supported by the explicitly or implicitly specified output format.

Action: Refer to the Oracle Multimedia documentation for a description of which channelOrder values are supported for each output format.

IMG-00586: output format does not support the specified pixelOrder

Cause: The specified pixelOrder is not supported by the explicitly or implicitly specified output format.

Action: Refer to the Oracle Multimedia documentation for a description of which pixelOrder values are supported for each output format.

IMG-00587: output format does not support the specified scanlineOrder

Cause: The specified scanlineOrder is not supported by the explicitly or implicitly specified output format.

Action: Refer to the Oracle Multimedia documentation for a description of which scanlineOrder values are supported for each output format.

IMG-00599: internal error

Cause: An internal error has occurred.

Action: Contact Oracle Support Services.

IMG-00601: out of memory while copying image

Cause: Operating system process memory has been exhausted while copying the image.

Action: See the database administrator or operating system administrator to increase process memory quota.

IMG-00602: unable to access image data

Cause: An error occurred while reading or writing image data.

Action: Ensure that the source image can be read from and the destination can be written to.

IMG-00603: unable to access source image data

Cause: The source image SOURCE attribute is invalid.

Action: Ensure that the SOURCE attribute of the source image is populated with image data.

IMG-00604: unable to access destination image data

Cause: The destination image SOURCE attribute is invalid.

Action: Ensure that the SOURCE attribute of the destination image is populated with image data.

IMG-00606: unable to access image data

Cause: An attempt was made to access an invalid image.

Action: Ensure that the SOURCE attribute of the image is populated with image data.

IMG-00607: unable to write to destination image

Cause: The destination image SOURCE attribute is invalid.

Action: Ensure that the SOURCE attribute of the destination image is initialized correctly and that you have sufficient tablespace.

IMG-00609: unable to read image stored in a BFILE

Cause: The image stored in a BFILE cannot be opened for reading.

Action: Ensure that the access privileges of the image file and the image file's directory allow read access.

IMG-00611: unable to access the BLOB for reading

Cause: The BLOB could not be opened for reading.

Action: Contact Oracle Support Services.

IMG-00612: unable to open export destination file

Cause: The file could not be created or opened.

Action: Check that the file does not refer to an existing directory. Check that the file is not locked by another application.

IMG-00613: export destination access denied

Cause: Permission to write to destination file was denied.

Action: Refer to the Oracle Multimedia documentation for information on granting privileges for the export() method.

IMG-00614: I/O error during export

Cause: The export operation failed because of an I/O error.

Action: Check OS logs and contact Oracle Support Services.

IMG-00701: unable to set the properties of an empty image

Cause: There is no data in the image object.

Action: Refer to the Oracle Multimedia documentation for information on how to populate image data into the image object.

IMG-00702: unable to initialize image processing environment

Cause: The image processing external procedure initialization process failed.

Action: Contact Oracle Support Services.

IMG-00703: unable to read image data

Cause: There is no image data in the image object.

Action: Refer to the Oracle Multimedia documentation for information on how to populate image data into the image object.

IMG-00704: unable to read image data

Cause: There is no image data in the image object.

Action: Refer to the Oracle Multimedia documentation for information on how to populate image data into the image object.

IMG-00705: unsupported or corrupted input format

Cause: This is an internal error.

Action: Contact Oracle Support Services.

IMG-00706: unsupported or corrupted output format

Cause: This is an internal error.

Action: Contact Oracle Support Services.

IMG-00707: unable to access image data

Cause: An error occurred while reading or writing image data.

Action: Contact your system administrator.

IMG-00710: unable to write to destination image

Cause: The destination image is invalid.

Action: Ensure that the SOURCE attribute of the destination image is initialized and that you have sufficient tablespace.

IMG-00711: unable to set properties of destination image

Cause: This is an internal error.

Action: Contact Oracle Support Services.

IMG-00712: unable to write to destination image

Cause: The destination image is invalid.

Action: Ensure the row containing the destination image has been locked (this does not apply to temporary BLOBs).

IMG-00713: unsupported destination image format

Cause: A request was made to convert an image to a format that is not supported.

Action: Refer to the Oracle Multimedia Documentation for supported formats.

IMG-00714: internal error

Cause: This is an internal error.

Action: Contact Oracle Support Services.

IMG-00715: unable to open image stored in a BFILE

Cause: The image stored in a BFILE could not be opened for reading.

Action: Ensure that the access privileges of the image file and the image file's directory allow read access.

IMG-00716: source image format does not support process options

Cause: A request was made to apply a processing option not supported by the source image format.

Action: Refer to the Oracle Multimedia Documentation for a discussion of supported processing options.

IMG-00717: destination image format does not support process options

Cause: A request was made to apply a processing option not supported by the destination image format.

Action: Refer to the Oracle Multimedia Documentation for a discussion of supported processing options.

IMG-00718: the same Temporary LOB cannot be used as both source and destination

Cause: A call was made to processCopy with the same Temporary LOB being specified as both the source and destination.

Action: Specify a different LOB for parameter "dest".

IMG-00719: image processing internal error

Cause: This is an internal error.

Action: Contact Oracle Support Services.

IMG-00720: image processing internal error

Cause: This is an internal error.

Action: Contact Oracle Support Services.

IMG-00721: unable to find source plug-in package ORDPLUGINS.ORDX\_string\_SOURCE

Cause: Custom source plug-in for user-specified source type was not found.

Action: Ensure correct source type is specified or proper custom source plug-in package is installed.

IMG-00722: incorrect value of bitsAllocated, bitsStored or highBit for output Dicom image

Cause: incorrect value of bitsAllocated, bitsStored or highBit for output Dicom image.

Action: Ensure correct value of bitsAllocated, bitsStored or highBit for output Dicom image.

IMG-00723: missing value in SHARPEN operation

Cause: An incorrect number of values was used to specify the sharpen parameters.

Action: Use one integer value to specify the kernel type and one float value to specify the gain factor.

IMG-00724: extra value in SHARPEN operation

Cause: An incorrect number of values was used to specify the sharpen parameters.

Action: Use one integer value to specify the kernel type and one float value to specify the gain factor.

IMG-00725: output image will be empty

Cause: The processing commands resulted in an empty output image.

Action: Ensure the resulting output image will not be empty.

IMG-00726: invalid value for the AVI framerate

Cause: An invalid value was used to specify the AVI framerate parameter.

Action: Use a floating-point value to specify the AVI framerate parameter.

IMG-00727: invalid value for the AVI frametime

Cause: An invalid value was used to specify the AVI frametime parameter.

Action: Use a floating-point value to specify the AVI frametime parameter.

IMG-00728: multiple incompatible AVI frame parameters found

Cause: Multiple incompatible AVI frame parameters were found.

Action: Use only one AVI frame parameter.

IMG-00729: output format does not support the specified frame parameters

Cause: The specified frame parameter is not supported by the explicitly or implicitly specified output format.

Action: Specify AVI as the output format in the process command string.

IMG-00730: unable to process empty image

Cause: There is no data in the input image object.

Action: Refer to the Oracle Multimedia documentation for information on how to put image data into the image object.

IMG-00731: specified page could be found in input image

Cause: The specified page does not exist in the input image.

Action: Restrict the value of the page parameter to values specifying pages that exist within the input image object.

IMG-00732: specified inputChannels could not be found in input image

Cause: The specified inputChannel parameter does not exist in the input image.

Action: Restrict the value of the inputChannels parameter to values specifying channels that exist within the input image object.

IMG-00733: invalid watermark property setting

Cause: The specified watermark property setting is not supported by Oracle Multimedia.

Action: See the Oracle Multimedia documentation for a description of valid watermark property settings.

IMG-00734: invalid deflateLevel value

Cause: The specified value for the deflateLevel parameter was not supported by Oracle Multimedia.

Action: See the Oracle Multimedia documentation for a description of the valid values for the deflateLevel parameter.

IMG-00735: incorrect transparencyFillColor values

Cause: The specified value for the transparencyFillColor parameter was not supported by Oracle Multimedia.

Action: See the Oracle Multimedia documentation for a description of the valid values for the transparencyFillColor parameter.

IMG-00800: internal error while parsing attribute string

Cause: An internal error occurred while parsing the attribute string containing the weights of the attributes.

Action: If you are certain that your command is correct, then contact Oracle Support Services.

IMG-00801: cannot extract height and width

Cause: Height and width are not set in the image object.

Action: Set the properties of the image object by calling setProperties and then generate signature.

IMG-00802: empty or null attribute string

Cause: An empty or null attributes string was passed to the image matching operators.

Action: Refer to the Oracle Multimedia documentation for a description of the correct usage and syntax of the attributes string.

IMG-00803: invalid attribute value

Cause: An invalid value was found while parsing the attribute string for the image matching operators.

Action: Refer to the Oracle Multimedia documentation for a description of the correct usage and syntax for the attributes string. The weight values should be between 0.0 and 1.0.

IMG-00804: Syntax error in attribute string

Cause: A syntax error was found while parsing the attribute string for the image matching operators.

Action: Refer to the Oracle Multimedia documentation for a description of the correct usage and syntax of the attributes string.

IMG-00805: SIGNATURE data has been corrupted or is invalid

Cause: The data in the signature is not a valid signature.

Action: Re-create the signature using the generateSignature method.

IMG-00806: invalid input image

Cause: The image data is either corrupt or is in an unsupported format.

Action: Repopulate the image object, set properties of the image, and generate the signature.

IMG-00807: no weights specified in weight string

Cause: All weights passed were zero. At least one attribute must be weighted.

Action: Specify a non-zero weight for at least one attribute

IMG-00808: unable to read an empty image

Cause: There is no data in the image object.

Action: Refer to the Oracle Multimedia documentation for information on how to populate the image object with image data.

IMG-00809: usage of IMGSimilar is incorrect

Cause: Syntax error while using IMGSimilar

Action: Refer to the Oracle Multimedia documentation for information on how to use the IMGSimilar operator. Check whether the value returned by IMGSimilar is compared to the value 1.

IMG-00810: boundary queue initialization failed

Cause: Operating system process memory has been exhausted while initializing the boundary queue.

Action: See the database administrator or operating system administrator to increase process memory quota.

IMG-00811: fail queue initialization failed

Cause: Operating system process memory has been exhausted while initializin the fail queue.

Action: See the database administrator or operating system administrator to increase process memory quota.

IMG-00812: merged area queue initialization failed

Cause: Operating system process memory has been exhausted while initializing the merged area queue.

Action: See the database administrator or operating system administrator to increase process memory quota.

IMG-00813: boundary queue free failed

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number.

IMG-00814: fail queue free failed

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number.

IMG-00815: merged area queue free failed

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number.

IMG-00820: area 0 queue clear failed

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number.

IMG-00821: area N queue clear failed

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number.

IMG-00822: area queue reset failed

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number.

IMG-00823: boundary queue pop failed

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number.

IMG-00824: fail queue pop failed

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number.

IMG-00825: merged area queue pop failed

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number.

IMG-00830: boundary queue is full

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number and the image causing this problem.

IMG-00831: boundary queue size exceeds expected size

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number and the image causing this problem.

IMG-00832: fail queue is full

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number and the image causing this problem.

IMG-00833: boundary queue size exceeds expected size

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number and the image causing this problem.

IMG-00834: merged area queue is full

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number and the image causing this problem.

IMG-00835: merged area queue size exceeds expected size

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number and the image causing this problem.

IMG-00836: area queue merge failed

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number and the image causing this problem.

IMG-00840: image structure allocation failed

Cause: Operating system process memory has been exhausted while initializing the image structure.

Action: See the database administrator or operating system administrator to increase process memory quota.

IMG-00841: image data allocation failed

Cause: Operating system process memory has been exhausted while initializing the image data.

Action: See the database administrator or operating system administrator to increase process memory quota.

IMG-00842: image index allocation failed

Cause: Operating system process memory has been exhausted while initializing the image index.

Action: See the database administrator or operating system administrator to increase process memory quota.

IMG-00843: internal image structure allocation failed

Cause: Operating system process memory has been exhausted while initializing the internal image structure.

Action: See the database administrator or operating system administrator to increase process memory quota.

IMG-00844: internal image data allocation failed

Cause: Operating system process memory has been exhausted while initializing the internal image data.

Action: See the database administrator or operating system administrator to increase process memory quota.

IMG-00845: internal image index allocation failed

Cause: Operating system process memory has been exhausted while initializing the internal image index.

Action: See the database administrator or operating system administrator to increase process memory quota.

IMG-00846: adjacency matrix allocation failed

Cause: Operating system process memory has been exhausted while initializing the adjacency matrix.

Action: See the database administrator or operating system administrator to increase process memory quota.

IMG-00847: area list allocation failed

Cause: Operating system process memory has been exhausted while initializing the area list.

Action: See the database administrator or operating system administrator to increase process memory quota.

IMG-00850: image structure free failed

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number.

IMG-00851: image data free failed

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number.

IMG-00852: image index free failed

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number.

IMG-00853: internal image structure free failed

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number.

IMG-00854: internal image data free failed

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number.

IMG-00855: internal image index free failed

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number.

IMG-00856: adjacency matrix free failed

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number.

IMG-00857: area list free failed

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number.

IMG-00860: assert failure, number of region exceeds allocated

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number and the image causing this problem.

IMG-00861: assert failure, inconsistency in area merge operation

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number and the image causing this problem.

IMG-00862: assert failure, inconsistency in merged area labels

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number and the image causing this problem.

IMG-00870: unsupported aspect ratio or image size

Cause: Signature generation was attempted on an image smaller than the supported size.

Action: Try scaling the image up to have a larger height and width, the suggested size is greater than 21 pixels each. If signature generation still fails, contact Oracle Support Services with the error number and the image causing this problem.

IMG-00871: unexpected number of seeds

Cause: An internal error has occured.

Action: Contact Oracle Support Services with the error number and the image causing this problem.

IMG-00872: unsupported image model

Cause: Signature generation was attempted on an image with an image model that Oracle Multimedia is unable to support.

Action: Try scaling the image down. If signature generation still fails, contact Oracle Support Services with the error number and the image causing this problem.

IMG-00899: signature cannot be generated

Cause: generateSignature could not generate the signature.

Action: Verify that the input image is a format supported by Oracle Multimedia.

IMG-00901: VIR signature version mismatch

Cause: Two signatures to be compared have different versions.

Action: Recompute signatures on the same platform and repeat signature comparison.

IMG-00902: VIR signature free failed

Cause: An internal error has occured.

Action: Contact Oracle Support Services.

IMG-00910: allocation of basic data structure failed

Cause: Operating system process memory has been exhausted while copying the image.

Action: See the database administrator or operating system administrator to increase process memory quota.

IMG-00911: free basic data structure failed

Cause: Operating system process memory has been exhausted while copying the image.

Action: Contact Oracle Support Services.

IMG-00921: threshold out of range

Cause: Threshold is not between 0 and 100

Action: Use a threshold between 0 and 100 and retry query.

IMG-00922: location specified without feature

Cause: only location was specified.

Action: Specify at least one other parameter (color, texture or shape) along with location. Refer to the Oracle Multimedia documentation for more details.

IMG-00923: signature is empty

Cause: Signature has not been generated.

Action: Generate the signature for the image by calling the generateSignature method.

IMG-00924: Incorrect parameter specification during CREATE INDEX

Cause: There is a spelling error, or duplicate parameter specification, or incorrect specification of parameters while creating an index of type ORDIMAGEINDEX.

Action: Refer to the Oracle Multimedia documentation for correct specification of CREATE INDEX parameters.

IMG-00925: unable to write to the ORDImageSignature object

Cause: The signature object was not valid and therefore the write operation failed. This problem is commonly caused by an attempt to invoke the generateSignature method on an uninitialized ORDImageSignature object.

Action: Ensure that the ORDImageSignature object has been initialized and inserted into a table. Also ensure that the row containing the signature object is locked. (The two previous actions do not apply to signature objects created using temporary BLOBs). Ensure that there is sufficient tablespace to contain the signature.

IMG-00926: tablespace specified during CREATE INDEX is not valid

Cause: A tablespace specified in the parameter string of a CREATE INDEX operation did not exist or the current user did not have sufficient privileges on the tablespace.

Action: Create the tablespace, grant appropriate privileges on the tablespace to the current user, or choose a different tablespace.

IMG-01000: unsupported option string

Cause: The function was invoked with an invalid option string.

Action: Ensure that correct option string is passed to the PL/SQL function. Refer to the Oracle Multimedia documentation for more information.

IMG-01001: not a DICOM object

Cause: The input was not a valid DICOM standalone object.

Action: Use an object that conforms to the DICOM standard. Refer to the Oracle Multimedia documentation for more information.

IMG-01002: unsupported DICOM version

Cause: The object header could not be parsed, possibly because the object header did not conform to the DICOM standard release 2003.

Action: Use an object that conforms to the DICOM standard release 2003. Refer to the Oracle Multimedia documentation for more information.

IMG-01003: unsupported DICOM object type

Cause: The category of DICOM objects is not supported by Oracle Multimedia.

Action: Use a DICOM image is supported by Oracle Multimedia. Oracle Multimedia supports image types defined in the DICOM standard release 2003. Refer to the Oracle Multimedia documentation for more details.

IMG-01004: input DICOM object is not an image

Cause: The DICOM object was not a DICOM image. DICOM object types such as structured reporting are not allowed by this function.

Action: Invoke this function with a DICOM image. Refer to the Oracle Multimedia documentation for more details.

IMG-01005: unsupported DICOM transfer syntax

Cause: The operation failed because the transfer syntax in the DICOM object, which describes the binary encoding of the DICOM object, was not supported by Oracle Multimedia.

Action: Use a DICOM object with a transfer syntax supported by Oracle Multimedia. Refer to the Oracle Multimedia documentation for more details.

IMG-01006: DICOM object cannot be parsed

Cause: The DICOM object could not be parsed by Oracle Multimedia, possibly due to an incorrect format or corrupted object.

Action: Verify that the DICOM object is not corrupted. If the DICOM object is valid, contact Oracle Support Services.

IMG-02001: 2FF01 - incorrect image format

Cause: There was a SQL/MM Still Image exception. Either the supplied image BLOB format did not match the image format or the image format is unsupported.

Action: For supported image formats, specify an input BLOB that has the same format as the image. For unsupported image formats, this method is not supported. Refer to the Oracle Multimedia documentation for more information.

IMG-02002: 2FF02 - incorrect average color feature specification

Cause: There was a SQL/MM Still Image exception. The specified average color value was not a valid SI\_Color value.

Action: Specify an average color value that is not null and contains valid SI\_Color values. SI\_Color attribute values must be integers from 0 to 255. Refer to the Oracle Multimedia documentation for more information on constructing valid SI\_Color objects.

IMG-02003: 2FF03 - incorrect color histogram feature specification

Cause: There was a SQL/MM Still Image exception. This exception was caused by one of the following.

\- The specified color value was null or invalid.

\- The specified frequency value was null or invalid.

\- The input color and frequency arrays were not equal in size.

\- The SI\_ColorList array attribute had reached the maximum size.

Action: Ensure that the following are true(as applicable to your case):

\- The color and frequency values are not null.

\- The SI\_Color attribute values are integers from 0 to 255.

\- The frequency value is a double precision number from 0 to 100.

\- The color and frequency arrays are equal in size and the size of the arrays is less than the SI\_MaxHistogramLength value listed in the SI\_VALUES view in the SI\_INFORMTN\_SCHEMA. Refer to the Oracle Multimedia documentation for more information on constructing SI\_ColorHistogram objects.

IMG-02004: 2FF04 - incorrect feature list specification

Cause: There was a SQL/MM Still Image exception. Either the specified feature values were invalid or the specified feature weights were invalid.

Action: Check the values of feature and featureweight pairs. For a non null feature value, the corresponding feature weight value must be a double precision number greater than 0.0. Refer to the Oracle Multimedia documentation for more information on the SI\_FeatureList object type and its methods.

IMG-02005: 2FF05 - incorrect color specification

Cause: There was a SQL/MM Still Image exception. The specified red/green/blue value was null or invalid.

Action: Specify red, green and blue values as integers from 0 to 255.

IMG-02006: 2FF06 - average color feature cannot be determined

Cause: There was a SQL/MM Still Image exception. Either the specified image was null, the image data in the specified image was null, or the average color feature was not supported by the specified image format

Action: Specify an image with non null image data and a supported format. Refer to the SI\_INFORMTN\_SCHEMA views and the Oracle Multimedia documentation for a list of supported image formats and image features.

IMG-02007: 2FF07 - positional color feature cannot be determined

Cause: There was a SQL/MM Still Image exception. Either the specified image was null, the image data in the specified image was null, or the positional color feature was not supported by the specified image format.

Action: Specify an image with non null image data and a supported format. Refer to the SI\_INFORMTN\_SCHEMA views and the Oracle Multimedia documentation for a list of supported image features and formats.

IMG-02008: 2FF08 - color histogram feature cannot be determined

Cause: There was a SQL/MM Still Image exception. Either the specified image was null, the image data in the specified image was null, or the color histogram feature was not supported by the specified image format.

Action: Specify an image with non null image data and a supported format Refer to the SI\_INFORMTN\_SCHEMA views and the Oracle Multimedia documentation for a list of supported image features and formats.

IMG-02009: 2FF09 - texture feature cannot be determined

Cause: There was a SQL/MM Still Image exception. Either the specified image was null, the image data in the specified image was null, or the texture feature was not supported by the specified image format.

Action: Specify an image with non null image data and a supported format. Refer to the SI\_INFORMTN\_SCHEMA views and the Oracle Multimedia documentation for a list of supported image features and formats.

IMG-02010: 2FF10 - illegal image format specification

Cause: There was a SQL/MM Still Image exception. The specified format name was null or invalid.

Action: Specify a format name that is not null. For supported image formats, specify a format name that matches the image BLOB format. For unsupported image formats, specify a format name that is not listed as supported image format. Refer to the SI\_INFORMTN\_SCHEMA views and the Oracle Multimedia documentation for a list of supported image formats.

IMG-02011: 2FF11 - unsupported image format conversion specified

Cause: There was a SQL/MM Still Image exception. Either the specified target format value was null, the specified image had a null format value, or the conversion from the specified image format to the specified target format was not supported.

Action: Specify an image with a supported image format and specify a target format value that is supported for conversion. Refer to the SI\_INFORMTN\_SCHEMA views and the Oracle Multimedia documentation for a list of supported image format conversions.

IMG-02012: 2FF12 - illegal specification for thumbnail generation

Cause: There was a SQL/MM Still Image exception. Either the specified image format did not support thumbnail generation, the specified thumbnail height or width was greater than the image height or width respectively, or the default thumbnail size 80 X 80 was greater than the image height or width respectively.

Action: Specify an image for which thumbnail generation is supported and specify thumbnail height and width values that are less than the image height and width values. Refer to the SI\_INFORMTN\_SCHEMA views and the Oracle Multimedia documentation for a list of supported thumbnail formats.

IMG-02014: 2202D Data exception - Null image value

Cause: There was a SQL/MM Still Image exception. The function was invoked using a null image value.

Action: Specify an image whose image data is not null. Refer to the Oracle Multimedia documentation for more information on constructing SI\_StillImage objects.