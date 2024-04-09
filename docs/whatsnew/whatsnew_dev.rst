
.. _whatsnew_dev:

XXXX.0.0
--------

Element changes
~~~~~~~~~~~~~~~
* Adds FailureCause, FailureDateDetected, FailureDetectionMethod, FailureID, FailureMechanism, FailureOperatingCondition, ImpactCapability, ImpactProduction, ImpactSafety (:pull`287`)
* Adds ChecksumType (:pull:`291`)
* Adds ChecksumKey, ChecksumDetail (:pull:`291`)
* Updates sample value of ProdType (:pull:`298`)
* Creates InsuranceType element

Object changes
~~~~~~~~~~~~~~
* Removes Firmwares array, adds Firmware to ProdCertification. Removes Applied Date, Certification Date from Firmware (:pull:`280`)
* Add Failure (:pull:`287`)
* Adds InsuranceType to InsurancePolicy object.
* Adds EntityRole to Entity object.

Unit changes
~~~~~~~~~~~~
* Adds enumerations FailureDetectionMethodItemType, FailureMechanismItemType, FailureOperatingConditionItemType, ImpactCapabilityItemType, ImpactProductionItemType, ImpactSafetyItemType  (:pull:`287`)
* Adds ChecksumTypeItemType and enums related to Checksum methods. (:pull:`291`)
* Adds InsuranceTypeItemType and enums related to Insurance Types.
* Removes enums from EntityRole that were related to specific Insurance types.

Bug fixes
~~~~~~~~~

Testing
~~~~~~~

Documentation
~~~~~~~~~~~~~

Contributors
~~~~~~~~~~~~
 * Kevin Kirkley (:ghuser:`kevinkirkl3y`)
 * Cliff Hansen (:ghuser:`cwhanse`)
 
