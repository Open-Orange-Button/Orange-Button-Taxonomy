
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
* Creates TestLabName (:pull:`305`)

Object changes
~~~~~~~~~~~~~~
* Removes Firmwares array, adds Firmware to ProdCertification. Removes Applied Date, Certification Date from Firmware (:pull:`280`)
* Add Failure (:pull:`287`)
* Adds InsuranceType to InsurancePolicy object.(:pull:`305`)
* Adds EntityRole to Entity object.(:pull:`305`)
* Creates TestLab object and adds it to CertificationAgency (:pull:`305`)

Unit changes
~~~~~~~~~~~~
* Adds enumerations FailureDetectionMethodItemType, FailureMechanismItemType, FailureOperatingConditionItemType, ImpactCapabilityItemType, ImpactProductionItemType, ImpactSafetyItemType  (:pull:`287`)
* Adds ChecksumTypeItemType and enums related to Checksum methods. (:pull:`291`)
* Adds InsuranceTypeItemType and enums related to Insurance Types. (:pull:`305`)
* Removes enums from EntityRole that were related to specific Insurance types. (:pull:`305`)
* Adds TestLab and CertificationAgency to enum list of EntityRole. (:pull:`305`)

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
 
