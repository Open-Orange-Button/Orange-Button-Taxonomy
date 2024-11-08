
.. _whatsnew_dev:

XXXX.0.0
--------

Element changes
~~~~~~~~~~~~~~~
 * Adds ProgramName, EligibleDeviceType, MaxEventsPerSeason, EventDurationMax, SeasonStartDate, Aggregator, AggregatorType, AggregatorName, ServiceSchedule, MaxEventsPerServiceSchedule, MaxEventDurationPerServiceSchedule, ContractTerm, ContractTerms, ServiceSchedules, ServiceProvider, ServiceProviderName, ServiceProviderID, ServiceRequester, SignUpAmount, Capacity, PaymentRateCapacity, PaymentRateEnergy, PaymentRateDuration, PaymentRatePerEvent, Receiver elements

Object changes
~~~~~~~~~~~~~~
 * Adds ContractTerms and Scope to Contract object.
 * Adds ContractES object.

Unit changes
~~~~~~~~~~~~
 * Adds LEI, PEN, DID, DUNS to IdentifierTypeItemType enum list.(#328)
 * Adds Occupant to ContactTypeItemType enum list. (#330)
 * Changes Homeowner to Owner in the ContactTypeItemType enum list. (#330)
 * Adds EU Digital Product Passport to IdentifierTypeItemType. (#331)
 * ContractType changed to ContactTypeItemType.
 * Updates enums of ContactTypeItemType to follow Contract[Type] format, adds ContractES.
 * Adds ProdGenerator and ProdThermostat to ProdTypeItemType.
 * Adds Aggregator, PropertyOwner, Financier to EntityTypeItemType Enums.
 * Creates AggregatorTypeItemType, with Energy, Loan and Lease as Enums.


Bug fixes
~~~~~~~~~

Testing
~~~~~~~

Documentation
~~~~~~~~~~~~~

Contributors
~~~~~~~~~~~~
 * Kevin Kirkley (kevinkirkl3y)