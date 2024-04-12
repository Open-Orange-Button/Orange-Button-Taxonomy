
.. _whatsnew_dev:

XXXX.0.0
--------

Element changes
~~~~~~~~~~~~~~~
* Adds FailureCause, FailureDateDetected, FailureDetectionMethod, FailureID, FailureMechanism, FailureOperatingCondition, ImpactCapability, ImpactProduction, ImpactSafety (:pull`287`)
* Adds ChecksumType (:pull:`291`)
* Adds ChecksumKey, ChecksumDetail (:pull:`291`)
* Adds PrivateKeyAddress (:pull:`297`)
* Adds IssueCause, IssueCauseConfidenceLevel, IssueConfidenceLevel, IssueID, IssueFoundDate, IssueStatus, IssueResolution, IssueResolutionDate, IssueUUID, UpdateLast, DetectionMethod (:pull:`296`)
* Changes PrivateKeyAddress to CryptographicKeyID (:pull:`298`)

Object changes
~~~~~~~~~~~~~~
* Removes Firmwares array, adds Firmware to ProdCertification. Removes Applied Date, Certification Date from Firmware (:pull:`280`)
* Add Failure (:pull:`287`)
* Adds PrivateKeyAddresses array object and adds PrivateKeyAddresses to Device (:pull:`297`)
* Removes PrivateKeyAddresses array object and replaces it with CryptographicKeyIDs and adds them to Device (:pull:`298`)
* Adds OMIssue and OMIssues (:pull:`296`)

Unit changes
~~~~~~~~~~~~
* Adds enumerations FailureDetectionMethodItemType, FailureMechanismItemType, FailureOperatingConditionItemType, ImpactCapabilityItemType, ImpactProductionItemType, ImpactSafetyItemType  (:pull:`287`)
* Adds ChecksumTypeItemType and enums related to Checksum methods. (:pull:`291`)
* Adds enuemrations DetectionMethodItemType, ConfidenceItemType, IssueStatusItemType (:pull:`296`)

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
 
