.. _overview:

Schema overview
===============

The Orange Button schema consists of json objects of the following types: Primitive, Element, Object, Object Array.

Primitives
----------

There are six Primitives:
* Value. Value contains the value of an Element. In an OB instance document, the json type of Value can be string, boolean, integer, or number, or an array of string, boolean, integer or number.
* StartTime. An ISO8601-compliant string defining the start of a time interval, or the single time, associated with Value.
* EndTime. An ISO8601-compliant string defining the end of a time interval associated with Value. EndTime is not used when a single StartTime is associated with a Value.
* Decimals. The number of digits after the decimal point of a Value with json type number.
* Precision. The number of digits, counting from the most significant, or left-most, digit, in a Value with json type number.
* Unit. A string corresponding to a UnitID from the OB Item Type list.


Element, Object and Object Array
--------------------------------

* OB Element: an object whose properties are Primitives.
* OB Object: a json object whose properties are OB Elements or OB Objects.
* OB Object Arrray: a json array of a single OB Object.

