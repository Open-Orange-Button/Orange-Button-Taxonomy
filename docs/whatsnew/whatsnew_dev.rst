
.. _whatsnew_dev:

XXXX.0.0
--------

Element changes
~~~~~~~~~~~~~~~
 * JobType name changed to SolarAPPJobType (:pull:`244`)
 * Removes ProductWarranty, PowerWarranty, EquipTypeWarr, EquipTypeWarrEndDate, EquipTypeWarrOutput, EquipTypeWarrStartDate, EquipTypeWarrStartDateMilestone, EquipTypeWarrTerm, ModuleMaterialsAndWorkmanShipWarrInitiationDate, ModulePerfWarrEndDate, ModulePerfWarrGuaranteedOutput, TrackerMaterialsWorkmanshipWarrExp, TrackerMaterialsWorkmanshipWarrInitiation (:pull:`246`)
 * Creates CECPBIMeter, DisplayProximity, DisplayTypes, DisplayIsCECCompliant (:pull:`250`)

Object changes
~~~~~~~~~~~~~~
 * Removes DeviceWarranty (:pull:`246`)
 * Adds CECPBIMeter, DisplayProximity, DisplayTypes, DisplayIsCECCompliant and CommunicationProtocol to ProdMeter (:pull:`250`)

Unit changes
~~~~~~~~~~~~
 * Updates JobTypeItemType to SolarAPPJobTypeItemType (:pull:`244`)
 * Creates DisplayTypeItemType, DisplayProximityItemType and enumerated lists for both. (:pull:`250`)
 * Adds IEEE 2030.5 and IEEE 2800 enums to StandardTypeItemType (:pull:`251`)

Bug fixes
~~~~~~~~~
 * Updated datatype of Decimals and Precision primitives to integer. (:pull:`248`)

Testing
~~~~~~~



Documentation
~~~~~~~~~~~~~
 * Adds Usage Tip to Scope object (:pull:`245`)
 * Updates StartTime documentation to share dual usage purposes of StartTime value. (:pull:`247`)
 * Updates documentation for EnergyCapacityNominal (:pull:`249`)

Contributors
~~~~~~~~~~~~
 * Kevin Kirkley (:ghuser:`kevinkirkl3y`)
 * Tyler Hagen (:ghuser:`THagen-BB`)
 * Cliff Hansen (:ghuser:`cwhanse`)
  
