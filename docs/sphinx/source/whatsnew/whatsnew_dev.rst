
.. _whatsnew_dev:

XXXX.0.0
--------

Element changes
~~~~~~~~~~~~~~~
 * Adds ProgramName, StartDateTime, EndDateTime, Aggregator, AggregatorType, AggregatorName, ServiceSchedule, EventsMax, EventDurationMax, ContractTerm, ContractTerms, ServiceSchedules, ServiceProvider, ServiceProviderName, ServiceProviderID, ServiceRequester, SignUpAmount, PaymentRateCapacity, PaymentRateEnergy, PaymentRateDuration, PaymentRatePerEvent, Receiver elements. (#332)

Object changes
~~~~~~~~~~~~~~
 * Adds ContractTerms and Scope to Contract object.(#332)
 * Adds ContractES object.(#332)

Unit changes
~~~~~~~~~~~~
 * Adds LEI, PEN, DID, DUNS to IdentifierTypeItemType enum list.(#328)
 * Adds Occupant to ContactTypeItemType enum list. (#330)
 * Changes Homeowner to Owner in the ContactTypeItemType enum list. (#330)
 * Adds EU Digital Product Passport to IdentifierTypeItemType. (#331)
 * ContractType changed to ContactTypeItemType.(#332)
 * Updates enums of ContactTypeItemType to follow Contract[Type] format, adds ContractES.(#332)
 * Adds ProdGenerator and ProdThermostat to ProdTypeItemType.(#332)
 * Adds Aggregator, PropertyOwner, Financier to EntityTypeItemType Enums.(#332)
 * Creates AggregatorTypeItemType, with Utility and ThirdParty as Enums.(#332)


Bug fixes
~~~~~~~~~

Testing
~~~~~~~

Documentation
~~~~~~~~~~~~~

Contributors
~~~~~~~~~~~~
 * Kevin Kirkley (kevinkirkl3y)